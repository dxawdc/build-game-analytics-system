# Analysis playbooks

## Contents

1. Method selection
2. Acquisition and onboarding
3. Retention and churn
4. Revenue and LTV
5. Content, version, and live ops
6. Economy, social, and server
7. Prediction and reporting

## 1. Method selection

| Question | Start with | Escalate to |
|---|---|---|
| What changed? | trend, mix, accounting decomposition | change-point or time-series model |
| Where is friction? | funnel and path analysis | sequence/mining or experiment |
| Who behaves differently? | cohort, cross-tab, segmentation | clustering or supervised model |
| Did a change cause impact? | randomized experiment | quasi-experiment with explicit assumptions |
| When do players leave? | retention and survival | hazard model or churn prediction |
| What items/actions co-occur? | cross-tab | association rules/correspondence |
| How do relationships matter? | group comparison | graph/network analysis |
| What will happen? | transparent baseline forecast | validated predictive model |
| Is this target even reachable? | growth identity and retention area | budget/capacity scenario model |
| Why did ad revenue move? | IAA factor decomposition | network/geo/placement drill-down |
| Why don't our numbers match the partner's? | definition and identity reconciliation | pipeline audit |

Always begin with a data-quality and population check.

Feasibility and projection questions go to [growth-accounting-and-forecasting.md](growth-accounting-and-forecasting.md);
ad-revenue questions to [hybrid-monetization-and-iaa.md](hybrid-monetization-and-iaa.md); definition disputes to
[cn-terminology-and-pitfalls.md](cn-terminology-and-pitfalls.md). Worked end-to-end examples, including two where the
original conclusion was wrong, are in [case-studies.md](case-studies.md).

## 2. Acquisition and onboarding

### Channel quality

1. Reconcile spend, impressions, clicks, installs, activations, and cohort size.
2. Compare volume and conversion, not rate alone.
3. Follow cohorts into first value, retention, monetization, quality, and fraud.
4. Normalize region, platform, creative, campaign, and acquisition date.
5. Compare mature LTV/ROAS horizons or use a backtested early predictor.
6. Separate attribution reporting from incrementality.

For campaign/creative diagnosis, attribution configuration, fraud signatures, and marginal-return budget decisions,
use [ua-and-marketing-analytics.md](ua-and-marketing-analytics.md).

### Onboarding friction

1. Define eligible cohort and first-value outcome.
2. Build a strictly ordered funnel only for genuinely ordered steps.
3. Add time-to-step and repeated-attempt distributions.
4. Split voluntary exit, crash/error, hard failure, and content failure.
5. Inspect device/version/network and player-skill proxies.
6. Combine quantitative locations with survey/support/playtest evidence.
7. Validate remedies experimentally.

## 3. Retention and churn

### Retention diagnosis

1. Plot cohort heatmap and survival curve.
2. Separate acquisition mix from within-cohort deterioration.
3. Locate early drop, transition period, and stable tail.
4. Compare first-day depth, first value, performance, mode, social, and content paths.
5. Control for cohort date, platform, region, channel, version, and server age.
6. Use association to generate hypotheses; test interventions separately.

### Active-user decomposition

Break active players into new, retained, resurrected, and at-risk populations using non-overlapping definitions. Decompose the change between periods into component contributions. Avoid explaining DAU with another identity that reuses overlapping users.

### Churn model

1. Define prediction time, outcome window, eligibility, and action.
2. Ensure all features are available at prediction time; remove leakage.
3. Split validation by time, not random rows alone.
4. Compare against a simple recency/frequency baseline.
5. Report precision/recall, PR-AUC, calibration, lift, coverage, and segment stability.
6. Choose a threshold from intervention capacity and expected value.
7. Randomize the treatment among model-selected users to measure incremental saves.
8. Monitor drift and harms such as incentive dependency.

## 4. Revenue and LTV

### Revenue decline tree

Reconcile accounting first, then decompose:

```text
Revenue
= eligible active population
× payer conversion
× purchase frequency
× net order value
```

Analyze contributions from:

- new/retained/resurrected population;
- payer segments and concentration;
- platform/region/channel/server;
- SKU/offer/price/payment success;
- refunds/chargebacks/FX/fees;
- event and content cannibalization;
- outages, version changes, and seasonality.

Use mix-adjusted comparisons before blaming player behavior.

### LTV and budget

1. Define cohort anchor and contribution basis.
2. Plot cumulative realized curves with maturity/censoring.
3. Backtest any early-horizon prediction on older cohorts.
4. Report uncertainty and error by channel/region/platform.
5. Compare LTV to fully specified cost and cash timing.
6. Use marginal, not merely average, returns when scaling spend.

Curve-fitting forms, the retention-area constant, steady-state DAU, target-to-budget inversion, and the failure modes
of long-tail extrapolation are in [growth-accounting-and-forecasting.md](growth-accounting-and-forecasting.md).

### Pricing

Combine:

- purchase funnel and payment failures;
- price-point/SKU elasticity from controlled tests;
- payer and non-payer experience;
- economy impact and substitution;
- repeat purchase and refund;
- survey-based willingness-to-pay as supporting evidence, not sole proof.

## 5. Content, version, and live ops

### Difficulty and stuck points

Build progression level/node curves for reach, attempt, success, deaths/failures, time, resource cost, abandon, and next-session return. Distinguish intended challenge from confusion, bugs, power gaps, and content exhaustion. Compare by skill/power, class/loadout, device, and cohort.

### Version effect

1. Freeze definitions across versions.
2. Identify changed systems and exposure.
3. Compare eligible/exposed cohorts, not all players indiscriminately.
4. Account for day-of-week, acquisition, platform mix, incidents, and seasonality.
5. Use randomized feature exposure where possible.
6. Pair adoption with player value and guardrails.

### Event effect

Measure eligibility, exposure, participation, completion, reward, incremental behavior, cannibalization, economy cost, and post-event return. Use holdouts or staggered rollout. Repeated-event cohorts reveal fatigue.

### Text feedback

1. Define sampling frame and privacy access.
2. Remove spam/system/duplicate content.
3. Create topic and sentiment taxonomy with human validation.
4. Link aggregated themes to behavior without exposing raw identities.
5. Report prevalence, severity, affected segment, trend, and representative short excerpts only when permitted.
6. Validate whether fixes change behavior and feedback.

## 6. Economy, social, and server

### Economy health

1. Reconcile ledgers.
2. Chart sources and sinks by reason and cohort.
3. Examine holdings, velocity, representative prices, and concentration.
4. Follow real-money -> virtual currency -> item/progression paths.
5. Detect duplication, negative balances, impossible sequences, and density anomalies.
6. Simulate and experiment with sink/source changes using guardrails.

### Social analysis

Start with adoption and shared-value funnels. Compare group survival, reciprocity, party/guild contribution, and network position. Social users are selected, so retention differences are not automatically social causation. Use invitations or feature rollout experiments when feasible.

Use graph methods for transfer rings, studio/bot networks, guild structure, influence, and isolated users. Validate operational labels before enforcement.

For matchmaking, party, guild, and social experiments, account-level randomization can be invalid because players affect one another. Define the likely spillover path first, then use an appropriate cluster (party/guild/match pool) or time-based switchback when it reduces interference. Log assignment and actual exposure separately, run a sample-ratio-mismatch check before reading outcomes, and predefine fairness, latency, safety, and queue-health guardrails. See [multiplayer-social-analytics.md](multiplayer-social-analytics.md).

### Server launch, migration, or merge

Compare population, concurrency, queue, retention, revenue, economy, power/faction balance, match quality, migration, and sentiment. Align by server age and use comparable worlds. Separate novelty, marketing, redistribution, and genuine incremental growth.

## 7. Prediction and reporting

### Forecasting

Start with seasonal naive and moving-average baselines. Add exponential smoothing, regression, or richer time-series models only when they improve rolling backtests. Include known releases, holidays, campaigns, incidents, and content cadence where justified. Report intervals, not only point estimates.

### Statistical safeguards

- Use confidence intervals and effect sizes, not p-values alone.
- Correct or control multiple testing when scanning many segments.
- Predefine experiment primary and guardrail metrics.
- Use user/account-level randomization unless interference requires cluster randomization.
- Check sample ratio mismatch, novelty, network spillover, and logging changes.
- Validate that experiment assignment, eligibility, and actual exposure each reconcile before estimating impact.
- Prefer medians/quantiles or robust models for skewed distributions.
- Treat clustering, correspondence, association rules, DBSCAN, and network analysis as discovery tools requiring validation.

### Decision report

Use:

1. decision and recommendation;
2. magnitude and affected population;
3. evidence and uncertainty;
4. causal status;
5. mechanism/hypothesis;
6. action, owner, and expected effect;
7. validation and guardrails.

Avoid a report that ends with description but no decision.
