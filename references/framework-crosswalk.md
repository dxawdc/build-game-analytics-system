# Framework crosswalk

Teams arrive with a favorite framework. Use their framework as a communication layer, then translate it into
the outcome → driver → diagnostic → guardrail structure this skill builds. Do not let a framework's slot list
decide the metric set: frameworks organize conversation; the product's core loop and decisions determine metrics.

## 1. Crosswalk table

| Framework | Origin/usage | Maps to | Known limits |
|---|---|---|---|
| AARRR (acquisition, activation, retention, revenue, referral) | growth funnels | acquisition + activation + retention + monetization branches of the KPI tree | assumes a linear one-way funnel; weak for live-service loops, resurrection, and premium/subscription products; referral is often negligible in games with no viral surface |
| RARRA (retention-first reorder of AARRR) | mobile growth reaction to AARRR | ordering of build priority, not a different metric set | still funnel-shaped; does not model economy, balance, or fairness |
| PRAPA (promotion, register, active, pay, ARPU) | Chinese web/client-game era revenue decomposition | revenue identity: reach → register → active → payer conversion → value per payer | assumes an explicit 注册 step and account identity; breaks on guest-login, mini-game, and device-first products; ignores retention shape and cost |
| RFM (recency, frequency, monetary) | CRM segmentation | payer segmentation and reactivation targeting | descriptive only; band cut-offs are arbitrary unless derived from the product's own distribution; ignores engagement and social value |
| 5W1H | issue framing | intake and root-cause questioning | not a metric framework; produces lists, not decisions |
| 5A (aware, appeal, ask, act, advocate) | marketing journey | pre-install and brand-side funnel | pre-install steps are usually unobservable in first-party data; label as modeled or survey-based |
| HEART (happiness, engagement, adoption, retention, task success) | UX metrics | guardrails and feature-level driver metrics | needs a goal-signal-metric step to become measurable |
| GSM / OSM (goal-signal-metric, objective-strategy-measurement) | metric derivation | the derivation step from decision to metric | no opinion on definitions, cohorts, or causality |
| North star + KPI tree | product analytics | this skill's default backbone | a single north star can hide multi-sided or long-horizon value; use a small north-star system when needed |
| Growth accounting (new/retained/resurrected/churned) | SaaS and consumer growth | active-user decomposition | requires non-overlapping population definitions; see [growth-accounting-and-forecasting.md](growth-accounting-and-forecasting.md) |
| MECE | structuring | validity check on any decomposition | a MECE tree can still be causally wrong |

## 2. Translating a legacy framework into the KPI tree

1. Write the framework's slots down as the team stated them.
2. For each slot ask: which decision does this support, and who acts on it?
3. Drop slots with no decision owner. Keep the ones that survive.
4. Replace each surviving slot label with a specified metric (population, formula, window, entity, source).
5. Add the layer the framework is missing — almost always guardrails, economy, or content supply.
6. Re-check that each outcome metric has at least one driver and one guardrail.

Typical missing layers by framework: AARRR/RARRA → economy, balance, quality, fairness; PRAPA → retention shape,
cost, and cash timing; RFM → engagement and non-payer value; HEART → unit economics.

## 3. Revenue identities — pick one and keep it

PRAPA-style decomposition and the modern revenue identity are the same algebra with different entry points:

```text
PRAPA:   revenue = promotion reach × register rate × active rate × pay rate × ARPU(payer)
Modern:  revenue = eligible active entities × payer conversion × purchases per payer × net value per purchase
```

Mixing them mid-analysis double-counts or drops a factor. Choose the identity that matches the product's
identity model, then hold it fixed across periods, channels, and reports.
For ad-monetized products use the IAA identity in [hybrid-monetization-and-iaa.md](hybrid-monetization-and-iaa.md).

## 4. Segmentation frameworks in games

RFM is common but was designed for retail purchase data. In games, prefer or add:

- lifecycle stage (new, developing, stable, at-risk, churned, resurrected);
- value band (cumulative net contribution, with the banding rule derived from the product's own distribution);
- engagement pattern (session cadence, mode mix, breadth);
- progression stage and power band;
- social state (solo, party, guild, leader);
- monetization channel (IAP only, ad only, hybrid, subscriber);
- acquisition source and cohort date.

State whether a segment is a **fixed cohort** (assigned once, followed forward) or a **rolling state**
(recomputed daily). Mixing the two is a frequent source of impossible-looking migration numbers.

## 5. Anti-patterns

- Reciting AARRR as the deliverable instead of a metric dictionary.
- Treating framework slot counts as coverage ("we have 5 of 5, so we're done").
- Importing PRAPA's 注册 entity into a product with no registration step.
- Using RFM bands copied from another title.
- Declaring a framework "the north star" — a framework is not a metric.
