# Case studies

Worked examples of the decision loop: business question → decomposition → method → finding → decision → what could
have gone wrong. Use them as reasoning patterns, not as templates to copy numbers from.

All figures below are **illustrative**, taken from public practitioner write-ups with unstated genre, region, date,
and definitions. They demonstrate reasoning shape only. Never quote them as benchmarks
(see the benchmark discipline section of [cn-terminology-and-pitfalls.md](cn-terminology-and-pitfalls.md)).

## Case 1 — Setting an activity threshold from the participation distribution

**Situation.** A card/board title ran a chest-reward event requiring ≥10 matches per day to unlock draws.
Participation was lower than planned.

**Decomposition.** Instead of asking "is 10 too high", the analyst plotted the distribution of daily matches per
active player and located where the population mass sat: ~45% of actives already played >10 matches, ~50% played >7.

**Method.** Distribution + threshold sensitivity. The threshold was moved to the nearest inflection point (7),
and the second run was compared on participation, draws per participant, and participant retention.

**Finding (illustrative).** Average draws rose 3.8 → 4.6; participant D1 retention 47% → 53%; overall retention +1.2pp.

**Decision.** Keep the lower threshold; apply "set gates at distribution inflection points" as a design rule.

**What could have gone wrong.**
- The lift may be **selection**, not causation: lowering a gate admits players who were already more engaged.
  A holdout or staggered rollout is required before claiming the event caused the retention gain.
- Participant retention is not product retention. Report both, plus the non-participant trend.
- A threshold set at the mass of the distribution maximizes participation, not value — check reward cost and
  economy impact (this is a currency source) before treating higher participation as a win.

**Reusable pattern.** Choose gates, tiers, and price points from the product's own distribution, then validate
experimentally. Distribution-first beats intuition-first, but distribution-first is still not causal evidence.

## Case 2 — A win-back campaign that "worked" but degraded in composition

**Situation.** An MMORPG compared two win-back campaigns for churned players. Campaign 2 had a higher recall rate.

**Decomposition.** Segment returning players by value band (core / high / mid-high / mid / low) and measure, per band:
return volume, days-active after return, resource consumption, re-churn, and where they stopped again.

**Method.** Segmented cohort comparison + progression-drop analysis, not a single blended recall rate.

**Finding (illustrative).** The higher recall came mainly from low-value players, who absorbed a large share
(~36–44%) of incentive consumption, while the intended core/high-mid segments responded weakly. Returning players
re-churned around days 7–8, coinciding with a known progression wall (an ascension gate).

**Decision.** Re-tier rewards toward mid-high segments, and add support at the day-7/8 wall rather than at day 0.
Judge the campaign on segmented value, not on recall rate.

**What could have gone wrong.**
- A blended recall rate would have declared campaign 2 the winner. **Rate without composition is a trap.**
- Incentive cost was the real denominator; recall per unit of incentive changes the ranking.
- The day-7/8 wall was pre-existing: fixing the campaign would not have fixed the retention cause.
- Without a control group, the "recall" includes players who would have returned anyway (natural resurrection).

**Reusable pattern.** For every "we lifted X" claim, ask: which segment, at what incentive cost, versus what
counterfactual, and did they stay?

## Case 3 — Disproving a DAU target with the growth identity

**Situation.** Leadership set a 500k DAU target and asked whether paid acquisition could deliver it.

**Decomposition.** Use the DAU identity and the retention area:

```text
DAU = retained + resurrected + new
steady-state DAU ≈ N × (1 + Σ r(k))
N_required ≈ DAU_target / (1 + Σ r(k))
budget/day ≈ N_required × CPI
```

**Method.** Fit the retention curve on weighted cohort retention (power-law fit in log-log space), compute the
retention area, invert for required daily new users, then price it at current CPI.

**Finding (illustrative).** The model implied roughly 80k new users per day sustained for two weeks — an order of
magnitude beyond the available budget at prevailing CPI.

**Decision.** Do not fund the buy. The target was renegotiated rather than pursued.

**What could have gone wrong.**
- Power-law extrapolation **overestimates** the long tail, which understates the required N. The honest output is a
  range with the fit method and its backtest error stated.
- CPI is not constant while scaling; marginal CPI at 80k/day would exceed the average used.
- The alternative that was chosen in the source write-up — a promotional push that inflated accounts — is a warning,
  not a solution: it hits the metric while degrading its meaning. Whenever a target is met by changing population
  composition, report value per active alongside the count.

**Reusable pattern.** Feasibility questions are arithmetic questions. The retention area converts any DAU target
into a required acquisition rate and a required budget, which is often the fastest way to stop a bad plan.

## Case 4 — Version comparison that was actually a calendar comparison

**Situation.** A team reported that engagement and revenue rose after a major version, and proposed doubling down
on that content direction.

**Decomposition.** Rebuild the comparison with controls: same weekday alignment, holiday calendar, acquisition
volume and channel mix, platform/region mix, incident periods, and concurrent live-ops events.

**Method.** Mix-adjusted pre/post comparison, plus separation of exposed and unexposed populations (players who
never touched the new system are not "treated").

**Finding.** Most of the lift coincided with a holiday window and a concurrent UA push that shifted the new-user
share upward; among tenured players actually exposed to the new system, engagement was flat and one guardrail
(session length for low-spec devices) had regressed.

**Decision.** Withhold the content-direction conclusion; re-test the system with randomized exposure; open a
performance bug for the device regression.

**What could have gone wrong.** It did go wrong — the original readout was a **pre/post correlation presented as
causation**, with a population mix change doing most of the work. Pre/post is diagnostic. Say so, every time.

**Reusable pattern.** Before attributing anything to a version: freeze definitions, align cohorts, list every other
thing that changed in the window, and restrict to the exposed population.

## Case 5 — Ad revenue drop, decomposed

**Situation.** A hybrid mini-game title saw ad revenue fall ~20% week over week; the first hypothesis was
"the new placement design hurt us".

**Decomposition.** Apply the IAA identity:

```text
ad revenue = DAU × ad-exposed rate × impressions per exposed × eCPM / 1000
```

**Method.** Factor decomposition by network, geo, format, placement, and app version; check whether network revenue
figures were final or still being restated; check the release/mediation change calendar.

**Finding.** DAU and ad load were flat. eCPM fell in one geo across all formats, concentrated in one demand network,
starting the day after a mediation floor-price change — with a post-holiday advertiser-budget dip on top.

**Decision.** Revert the floor change for that geo, keep the placement design, and add an eCPM-by-network baseline
alert with weekday-matched bands.

**What could have gone wrong.**
- Attributing an exogenous market/mediation move to your own design change, and reverting good design.
- Reading provisional network revenue as final.
- Comparing across weekdays and holiday boundaries without a matched baseline.

**Reusable pattern.** For any revenue movement, decompose the identity before hypothesizing about design.
The identity tells you which team owns the problem.

## Cross-case checklist

Before accepting any "we improved X" claim:

1. Is the population the same on both sides, or did composition change?
2. Rate **and** volume reported?
3. What is the counterfactual — holdout, staggered rollout, matched control, or nothing?
4. Is the effect measured on the exposed population only?
5. What did it cost (incentives, economy sources, ad load, engineering)?
6. Which guardrails were checked, not just the target metric?
7. Is the causal status labeled: descriptive, associational, quasi-experimental, or randomized?
8. If the target was met, did value per active hold?
