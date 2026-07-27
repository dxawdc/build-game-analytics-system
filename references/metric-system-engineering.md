# Metric system engineering and operating model

A metric dictionary that nobody maintains becomes folklore within one release cycle. This file covers how the
system is built, stored, alerted on, and actually used — the difference between a document and a working system.

## 1. Metric composition model

Most data platforms (and most Chinese-market data teams) decompose metrics this way:

| Layer | Chinese | Meaning | Example |
|---|---|---|---|
| Atomic metric | 原子指标 | business process + one aggregation on one measure, no filters, no period | 付费金额 (paid amount, sum) |
| Modifier | 修饰词 | qualifying dimension slice or business qualifier | 新用户, iOS, 首充, 活动期间 |
| Time period | 时间周期 | window and grain | 当日, 近7日, 自然月, 累计 |
| Derived metric | 派生指标 | atomic + modifiers + period | 新用户当日付费金额 |
| Composite metric | 复合/衍生指标 | arithmetic over other metrics | 付费率 = 付费人数 / 活跃人数 |

Why it matters: derived metrics explode combinatorially. Registering atomic metrics plus a controlled modifier
vocabulary keeps the dictionary finite and makes "同名不同义" (same name, different meaning) structurally impossible.

Naming convention that survives contact with a warehouse:

```text
<period>_<modifier>_<atomic>_<aggregation>     zh display name kept as metadata
d1_new_user_pay_amount_sum                     新用户当日付费金额
d7w_dau_payer_conversion_rate                  近7日付费率（活跃口径）
```

Encode the denominator in the ID for every rate. `payer_rate` is a defect; `payer_rate_per_dau` is a metric.

## 2. Usage tiers, and how they map to the KPI tree

Chinese teams commonly organize as 主指标 / 辅助指标 / 预警指标. Map that onto this skill's structure:

| Local tier | This skill's layer | Question it answers | Update cadence |
|---|---|---|---|
| 主指标 (primary) | outcome / north star | are we winning? | daily/weekly, reviewed by leadership |
| 驱动指标 (driver) | driver | what moves the outcome? | daily, owned by feature/ops teams |
| 辅助/诊断指标 | diagnostic | why did it move? | on demand, deep-dive only |
| 预警指标 (guardrail/alert) | guardrail | is something breaking or being harmed? | continuous with alerting |

Rules: every outcome metric needs at least one driver and one guardrail; diagnostic metrics do not belong on an
executive dashboard; guardrails must have an owner and a response path, or they are decoration.

## 3. Metric graph and lineage

Maintain an explicit graph:

```text
decision → metric → component metrics → source events/tables → instrumentation owner
```

- Distinguish **arithmetic edges** (payer rate is definitionally payers / actives) from **hypothesis edges**
  (tutorial completion is believed to drive D7 retention). Draw them differently. Only arithmetic edges are guaranteed.
- Lineage enables impact analysis: when an event changes, you can list affected metrics and dashboards before shipping.
- The graph also exposes orphans: metrics no decision consumes, and events no metric reads. Both should be retired.

## 4. Single definition source

- One registry (semantic layer, metric store, or versioned repo file) is authoritative; dashboards and notebooks
  reference it instead of re-implementing SQL.
- Version every metric: `draft → proposed → approved → deprecated`, with change history and effective dates.
- A definition change is a **product event**: announce it, state whether history is restated or forked, and keep the
  old definition readable so past decisions remain interpretable.
- Never silently re-point a metric name at a new formula. Create a new ID and deprecate the old one.
- Machine-checkable specs are preferable. This skill ships a validator:

```powershell
python scripts/validate_metric_spec.py <metric-spec.json-or-yaml> --strict
```

## 5. Alerting design

Static thresholds on a live-service game produce mostly false alarms. Build alerts as follows:

1. **Baseline first**: same weekday, same region/platform mix, trailing distribution, seasonality, known event calendar.
2. **Elastic thresholds**: deviation from expected range (e.g. percentile band or prediction interval) rather than
   a fixed number. Derive bands per segment; a small server's normal variance is not a large one's.
3. **Severity tiers**: page (revenue/login/payment/crash), review-next-morning (engagement drift), digest (slow trends).
4. **Suppression and grouping**: one root cause should produce one alert; maintain a change/release/event calendar
   so planned dips are annotated, not paged.
5. **Every alert names an owner and a first action.** An alert with no runbook is deleted.
6. **Track alert precision** as its own metric. Recurring false positives destroy trust in the whole system.
7. Distinguish **data incidents** (pipeline, SDK, schema) from **business changes**. The first response to a large
   sudden move is always a data-integrity check; see [instrumentation-and-data-quality.md](instrumentation-and-data-quality.md).

## 6. Serving layers and latency

| Layer | Latency | Legitimate use | Do not use for |
|---|---|---|---|
| Real-time / operational | seconds–minutes | outage detection, live-ops monitoring, anti-fraud reaction, in-game triggers | financial reporting, cohort analysis, attribution settlement |
| Near-line | minutes–hours | daily ops dashboards, campaign pacing, event monitoring | audited revenue, deduped cohort history |
| Offline / batch | hours–daily | cohort/retention/LTV, finance-reconciled revenue, model training | anything requiring immediate response |

The same player journey often needs correlated events in more than one lane. Decide the lane per event deliberately,
and make it a declared field in the event contract rather than an accident of implementation.
Reconcile lanes on a schedule and publish which lane a dashboard is reading.

## 7. Operating model — turning analysis into decisions

Instrumentation and dictionaries do not create data-driven behavior. The organizational loop does:

- **Intake**: a written request states the decision, the decider, the deadline, and what action each possible answer
  triggers. Requests that cannot name an action are answered with a metric link, not an analysis.
- **Backlog**: prioritize by decision value × reversibility × effort, not by requester seniority.
- **Definition review**: analysts, designers, ops, and engineers agree on the 口径 before implementation.
  Most wasted engineering in game analytics is instrumentation built against an unagreed definition.
- **Delivery**: every report ends with a recommendation, a causal-status label, and a validation plan
  (see the decision-report structure in [analysis-playbooks.md](analysis-playbooks.md)).
- **Adoption tracking**: record whether the recommendation was taken, what happened, and whether the predicted
  effect materialized. This closes the loop and is the only honest measure of an analytics team.
- **Human-in-the-loop for automation**: low-impact, reversible decisions can be automated (offer ranking,
  matchmaking tuning within bounds); high-impact or irreversible ones (pricing, economy resets, bans, KPI commitments)
  require human confirmation and an audit trail.

## 8. Anti-patterns

| Anti-pattern | Symptom | Fix |
|---|---|---|
| Metric silo | each team has its own DAU | single registry with aliases mapped to IDs |
| Metric sprawl | hundreds of dashboards, no decisions | retire orphan metrics; enforce decision-linked intake |
| Dashboard graveyard | built once, never opened | measure dashboard usage; delete unused |
| Definition drift | same chart, different number month over month | versioned definitions, restatement policy |
| Alert fatigue | on-call ignores alerts | baseline-driven thresholds, severity tiers, precision tracking |
| Report-as-deliverable | descriptive decks with no recommendation | require decision + action + owner |
| Metric-as-target gaming | KPI achieved, business unchanged | pair every target with guardrails and composition checks |
| Data-ism (唯数据论) | qualitative signals ignored | pair behavioral data with playtests, support tickets, and community feedback |
