# Product intake and KPI tree

## Contents

1. Intake
2. Translate goals into questions
3. KPI layers
4. North-star selection
5. Driver-tree patterns
6. Prioritization
7. KPI-tree acceptance checks

## Intake

Collect only information that changes the design:

| Area | Questions |
|---|---|
| Product | Genre, platforms, regions, release stage, live-service cadence |
| Player value | What satisfying outcome does the player repeatedly achieve? |
| Core loop | Entry -> action -> reward -> progression -> return trigger |
| Modes | PvE, PvP, co-op, guild, creator, spectator, offline |
| Business model | Premium, DLC, subscription, IAP, gacha, ads, marketplace, hybrid |
| Population | Account/device/player/character; guest and cross-platform identity |
| Time | Product timezone, UTC policy, game-day boundary, season boundaries |
| Money | Currency, FX policy, tax/platform fee/refund treatment, bookings vs revenue |
| Growth | Organic/paid/channel mix and attribution confidence/window |
| Data | Client logs, server logs, orders, ads, match, telemetry, support, surveys |
| Decisions | Three to five decisions the system must improve in the next quarter |
| Constraints | Privacy, latency, data quality, team capacity, launch deadlines |
| Vocabulary | Which metric words the team already uses, and what each one currently means to them |

When information is unavailable, create an assumption register with impact and validation path.

Capture the team's existing vocabulary during intake, not after the dictionary is written. Reused words with
different meanings are the most common cause of rework. For Chinese-language teams and partner reconciliation,
read [cn-terminology-and-pitfalls.md](cn-terminology-and-pitfalls.md). If the team arrives with AARRR, PRAPA, RFM,
HEART, or another framework, translate rather than discard it using [framework-crosswalk.md](framework-crosswalk.md).

## Translate goals into questions

Reject goals such as "increase DAU" until the decision is explicit. Rewrite them:

- Which acquisition cohorts become retained core-loop users at acceptable cost?
- Where do new players fail to reach first value?
- Which content creates durable engagement rather than short-term time inflation?
- Is revenue change driven by audience size, payer conversion, frequency, or spend?
- Does a live event create incremental value after cannibalization and fatigue?
- Is the economy healthy for new, mid-game, end-game, payer, and non-payer cohorts?
- Are matchmaking, crashes, latency, or fairness harming retention?

## KPI layers

Use four layers:

1. **Outcome**: business and player value, lagging by nature.
2. **Driver**: a lever the team can plausibly affect.
3. **Diagnostic**: locates why a driver moved.
4. **Guardrail**: prevents local optimization from damaging experience or economics.

Do not mix these roles. "Crash-free sessions" is usually a guardrail or driver, not the business outcome.

## North-star selection

A useful north star:

- represents realized player value, not mere exposure;
- has a stable and auditable definition;
- moves often enough to guide the team;
- is difficult to inflate without creating real value;
- predicts or accompanies durable retention and business health;
- can be decomposed into owned drivers.

Use a small system when one number hides important tradeoffs:

- primary value metric;
- reach or frequency metric;
- quality/fairness guardrail;
- sustainable monetization guardrail.

Examples are candidates, not defaults:

- Weekly players completing a meaningful core loop.
- Weekly successful social play groups.
- Weekly satisfied competitive matches.
- Weekly retained creators and consumers with successful play sessions.

## Driver-tree patterns

### Active value

```text
Weekly value realizations
= eligible players
× value-action participation rate
× successful value actions per participant
```

Then decompose eligible players by new, retained, resurrected, and churned populations.

### Revenue

```text
Net revenue
= active eligible players
× payer conversion
× purchases per payer
× net value per purchase
+ net ad revenue
+ subscription/DLC/marketplace revenue
```

Keep refunds, taxes, platform fees, creator share, ad fill, and FX treatment explicit.

### Active population

```text
Ending active population
= retained prior population
+ activated new players
+ resurrected players
- newly churned players
```

This identity is conceptual; define non-overlapping windows before calculating it.

### Live event

```text
Incremental event value
= exposed eligible players
× incremental participation
× incremental quality-adjusted value per participant
- cannibalized baseline value
- incentive and operating cost
```

Use a holdout or defensible counterfactual where possible.

## Prioritization

Score candidate metrics on:

- decision relevance;
- actionability;
- definition stability;
- data readiness;
- sensitivity without excessive noise;
- resistance to gaming;
- coverage of player and business value.

Launch with the smallest set that closes a decision loop. Defer metrics with no owner, no action, or no trustworthy source.

## KPI-tree acceptance checks

- Every outcome has at least one controllable driver.
- Every risky driver has at least one guardrail.
- Driver branches are mutually interpretable and avoid obvious double counting.
- Volumes and rates appear together where scale matters.
- Leading and lagging signals are both present.
- Segmentation dimensions are not embedded into metric names unnecessarily.
- Hypothesized causal links are labeled and assigned a validation method.
