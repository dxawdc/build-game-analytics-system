# Metric library

Use this as a selection library, not a mandatory checklist.

## Contents

1. Definition contract
2. Acquisition and activation
3. Active use and engagement
4. Retention, churn, and resurrection
5. Monetization and unit economics
6. Economy
7. Progression, content, and balance
8. Live operations
9. Social, server, and competitive health
10. Quality, reliability, and trust

## 1. Definition contract

For every production metric specify:

- stable ID and Chinese/English name;
- decision and business question;
- plain-language definition;
- formula with numerator and denominator;
- eligible population and exclusions;
- entity and grain;
- cohort anchor and time window;
- product timezone and game-day boundary;
- dimensions and allowed drill-downs;
- authoritative source events/tables;
- late-arrival, deduplication, zero-denominator, and backfill policy;
- owner, freshness, status, and change history;
- directionality, target method, and guardrails;
- money currency, FX date, and gross/net basis where relevant.

Never use a metric name as its definition.

## 2. Acquisition and activation

| Metric | Base formula | Required qualifiers |
|---|---|---|
| CTR | attributed clicks / measurable impressions | creative, placement, invalid traffic policy |
| Install conversion | first valid installs / measurable clicks | attribution and reinstall policy |
| Activation rate | activated entities / eligible installs or acquired entities | activation event and entity |
| Registration rate | completed valid registrations / eligible starters | guest, duplicate, fraud policy |
| CPI | attributable acquisition spend / attributed valid installs | spend basis and window |
| CPA/CAC | attributable spend / target acquired entities | target action and cost scope |
| First-value rate | entities reaching first value / eligible new entities | first-value event and window |
| Time to first value | first-value time - eligible start time | censored failures and percentile |
| Tutorial completion | completers / tutorial starters or eligible new entities | choose one denominator |
| Organic share | valid organic acquisitions / all classifiable acquisitions | unclassified kept separate |

Build a step funnel from impression -> click -> store view -> download -> install -> first launch -> account/link -> tutorial -> first value -> first return -> first purchase. Include only observable steps and label attribution uncertainty.

Activation must describe realized value, not merely app launch.

## 3. Active use and engagement

| Metric | Base formula | Notes |
|---|---|---|
| DAU/WAU/MAU | distinct active entities in window | define qualifying activity |
| DAU/MAU | DAU / trailing or calendar MAU | state window alignment |
| New-active share | new active entities / all active entities | composition, not product quality alone |
| Sessions per active | valid sessions / active entities | session timeout and background policy |
| Play time per active | valid foreground/play duration / active entities | report median and percentiles too |
| Core-loop participation | active entities with core-loop event / eligible active entities | mode eligibility matters |
| Core-loop success | successful loops / started valid loops | player and attempt views differ |
| Engagement breadth | distinct meaningful features used / eligible active | weight or threshold if needed |
| ACU | average concurrent valid players | aggregation interval |
| PCU | maximum concurrent valid players | interval and day boundary |

Separate active, engaged, and value-realizing users. Login is often too weak for an engaged definition.

For skewed time and frequency metrics report distribution, median, P75/P90/P95, and concentration rather than only a mean.

## 4. Retention, churn, and resurrection

### Exact-day retention

```text
D_n exact retention
= cohort entities active on exactly cohort date + n
/ eligible cohort entities
```

State whether the cohort anchor is install, activation, registration, first login, purchase, or another milestone.

### Rolling retention

```text
D_n rolling retention
= cohort entities active on or after cohort date + n
/ eligible cohort entities
```

### Bracket retention

```text
W_k bracket retention
= cohort entities active at least once in week-k interval
/ eligible cohort entities
```

Do not compare exact-day, rolling, and bracket retention as if equivalent. Use weighted cohort aggregation:

```text
weighted retention = sum(retained entities) / sum(eligible cohort entities)
```

Other metrics:

| Metric | Definition requirement |
|---|---|
| Survival | probability of not yet churning by time t; censor unresolved entities |
| Hazard | conditional churn probability/rate at time t among survivors |
| Churn rate | entities meeting a product-specific inactivity or cancellation rule / eligible base |
| Return rate | churned/inactive entities returning in a defined observation window / eligible inactive entities |
| Resurrection | returned entities who meet a prior inactive threshold and regain qualifying activity |
| Cohort half-life | time until cohort survival/retention crosses a defined level |

Derive inactivity thresholds from play cadence, return curves, billing cycles, or mode schedules. Do not assume a universal 7-, 14-, or 30-day churn rule.

## 5. Monetization and unit economics

### Revenue bases

Keep these distinct:

- gross bookings/purchases;
- gross recognized revenue;
- net revenue after defined tax, platform fee, creator share, refunds, and chargebacks;
- cash receipts;
- virtual-currency spend, which is not automatically real-money revenue.

### Core formulas

```text
Payer conversion = distinct payers / eligible distinct entities
ARPU = period revenue / eligible active entities
ARPDAU = daily revenue / DAU
ARPPU = period revenue / distinct payers
Purchase frequency = valid purchase transactions / payers
Average order value = valid purchase value / purchase transactions
```

Always state period, eligibility, currency, and revenue basis. The identity:

```text
Revenue = eligible active entities × payer conversion × purchases per payer × net value per purchase
```

is preferable to treating ARPPU as a single unexplained cause.

Track:

- first-purchase rate and time;
- second/third-purchase conversion and interval;
- payer retention;
- price-point and SKU mix;
- payer concentration and revenue concentration;
- refunds, chargebacks, failed payments, and fraud;
- subscription trial, renewal, cancel, grace, and win-back;
- DLC/season-pass attach rate;
- marketplace GMV, net revenue, take rate, and creator earnings.

### Ad monetization

```text
Ad fill rate = filled ad responses / eligible ad requests
Ad show rate = rendered impressions / filled responses
eCPM = ad revenue / rendered impressions × 1000
Ad ARPDAU = daily net ad revenue / DAU
Ad load = rendered impressions / ad-exposed active entity
Reward completion = completed rewarded views / started rewarded views
```

Pair ad revenue with retention, session quality, crash/latency, opt-out, and frustration guardrails.

### LTV

Prefer realized cohort LTV:

```text
Cohort LTV through day n
= cumulative cohort net contribution through day n
/ eligible acquired cohort size
```

State whether contribution is revenue or margin. For predictions, report model date, horizon, features, censoring, uncertainty, and backtest error.

### ROAS and ROI

Use explicit names:

```text
ROAS = attributable revenue / attributable ad spend
Profit ROI = (incremental contribution - investment) / investment
```

Do not call revenue/spend "ROI." State attribution window, organic incrementality, cost scope, and maturity horizon.

## 6. Economy

Instrument every authoritative transaction as a ledger entry with transaction ID, actor, item/currency, amount, source/sink reason, balance before/after, and correlation ID.

Monitor:

- source volume and sink volume by reason;
- net issuance = sources - sinks;
- holdings distribution and zero-balance rate;
- currency velocity = transacted amount / average holdings;
- price level for representative baskets;
- real-money-to-virtual conversion paths;
- item creation, destruction, transfer, and circulation;
- market supply, demand, liquidity, spread, and creator/seller concentration;
- negative balance, duplicate grant, impossible sequence, and exploit anomalies;
- economy metrics by progression, server age, payer band, and cohort.

Use Gini, top-x share, percentiles, and cohort distributions carefully. Concentration can be intended, harmful, or both depending on design.

For card/gacha systems also track banner eligibility and exposure, first pull, pullers, pulls per puller, currency source, pity/guarantee state, duplicate outcomes, target acquisition, roster utilization, and post-pull progression/retention. Validate observed outcome distributions against the configured design with adequate samples. Pair revenue with fairness, complaint, refund, churn, and economy guardrails; verify any current disclosure or regulatory requirements separately.

## 7. Progression, content, and balance

| Metric | Formula or interpretation |
|---|---|
| Reach | entities reaching node / eligible entities |
| Unlock | entities unlocking content / eligible entities |
| Attempt | entities or attempts starting content |
| Completion | successful entities or attempts / starters |
| Abandonment | abandoned valid attempts / starters |
| Stuck rate | entities exceeding failure/time threshold / eligible entrants |
| Time to milestone | milestone time - cohort anchor |
| Replay | repeat completions / eligible completers |
| Content freshness | value activity on recently released content / all comparable value activity |
| Difficulty | success, attempts-to-success, time, damage, deaths, or resource cost |

Keep player-level and attempt-level denominators separate.

For competitive balance track pick/use, ban, win, matchup, skill-adjusted win probability, side/map advantage, time-to-kill, surrender, disconnect, smurf/cheat indicators, and outcome calibration. Raw win rate without skill, map, team, and patch controls is rarely sufficient.

## 8. Live operations

Track event eligibility -> exposure -> participation -> milestone -> completion -> reward claim -> post-event return.

Measure:

- unique reach and participation;
- frequency and depth;
- completion and reward claim;
- incremental engagement/revenue with counterfactual;
- cannibalization of baseline modes/SKUs;
- new, retained, resurrected, payer, and non-payer response;
- fatigue across repeated events;
- post-event retention and spend;
- incentive cost and operational cost;
- fairness, economy, and technical guardrails.

Version evaluation should align comparable cohorts, platform/region/channel mix, day-of-week, seasonality, acquisition changes, and incident periods. A simple before/after chart is diagnostic, not causal proof.

## 9. Social, server, and competitive health

Social metrics:

- invite send -> accept -> first shared value funnel;
- friend, party, guild, alliance, and mentor adoption;
- successful shared sessions;
- group survival and membership tenure;
- contribution and reciprocity;
- network density, centrality, isolates, and community structure;
- social retention lift as association unless experimentally identified;
- reports, blocks, moderation actions, and toxicity exposure.

Server/world metrics:

- population, new/retained/churned composition, concurrency, queue;
- faction/alliance balance and power concentration;
- economy by server age;
- migration, merge, and new-server effects;
- capacity, latency, disconnect, and cross-server matching;
- pre/post merge with comparable controls and observation windows.

Competitive metrics:

- queue time percentiles;
- match completion and abandonment;
- predicted win probability distribution and calibration;
- stomp/close-match rate;
- rematch/requeue and post-loss return;
- rank movement and skill convergence;
- latency and party-size parity;
- integrity reports and confirmed violations.

## 10. Quality, reliability, and trust

Use both session and user denominators:

```text
Crash-free session rate = sessions without crash / valid sessions
Crash-free user rate = active users without crash / active users
Disconnect rate = involuntary disconnects / valid online sessions or matches
```

Monitor ANR/freeze, startup success, load time, frame performance, network latency, error rate, login success, payment success, matchmaking wait, sync failure, patch success, and incident impact.

Slice by app version, platform, device tier, OS, region, network, server, mode, and content.

Trust guardrails include fairness, deceptive pressure, excessive ad load, unintended spend, refunds, reports, blocks, account safety, cheating, and moderation response. Define access controls and avoid unnecessary personal data.
