# Multiplayer, matchmaking, and social analytics

## Contents

1. Design principles
2. Matchmaking event contract
3. Metric system
4. New-player and social journeys
5. Experiments under interference
6. Safety and review checklist

## 1. Design principles

Matchmaking is a multi-objective system. It must balance fair competition, latency, wait time, queue availability, party parity, role/team composition, integrity, and player experience. Do not declare it healthier from a single headline metric, raw rank gap, or average win rate.

Use a rating/prediction model appropriate to the product. If the model represents uncertainty, preserve it. At match formation, freeze the rating snapshot, uncertainty/confidence, predicted outcome, queue/matchmaking configuration version, estimated latency, party composition, and region. Later recomputation may be useful for modelling, but it is not the historical decision state.

## 2. Matchmaking event contract

Instrument the state transitions needed to reconstruct the journey:

| Stage | Minimum event and key properties |
|---|---|
| Queue intent | `queue_entered`: queue/mode, region, party ID/size, role/loadout request, rating snapshot, configuration version |
| Queue outcome | `queue_cancelled` / `queue_timed_out`: reason, wait duration, client/server cause |
| Match formation | `match_formed`: match ID, candidate population summary, predicted probabilities, team/party composition, latency estimates, configuration version |
| Acceptance and draft | `match_accepted`, `draft_started`, `draft_completed`: acceptance/decline reason, role selection, picks/bans where relevant |
| Gameplay | `match_started`, reconnect/disconnect, server/network quality, abuse/report signals subject to access policy |
| Result | `match_ended`: valid/invalid result, winner, duration, surrender/remake, score/stomp proxies, rating delta, authoritative outcome |
| Follow-up | `queue_reentered`, `party_changed`, `rematch_started`, `social_edge_created`: return, relationship, and replay signals |

Keep player-match rows separate from match-level rows. An invalid/remade match, bot/QA account, or abandoned queue must be explicitly represented rather than disappearing from denominator choices.

## 3. Metric system

Use a balanced scorecard.

| Question | Core measures | Guardrails / interpretation |
|---|---|---|
| Did players receive a match? | queue-to-valid-match conversion, P50/P90 wait, cancel/timeout rate | split by region, mode, party size, rating uncertainty, time of day, and population size |
| Was the match fair? | calibration of pre-match win probability, distribution of predicted probabilities, outcome surprise | raw rank gap is a diagnostic only; inspect roles, parties, smurfs, and model uncertainty |
| Was it enjoyable and reliable? | valid completion, remake/surrender/disconnect, severe-latency rate, post-match requeue | distinguish player choice, client error, server incident, and intentional abuse |
| Did it retain value? | next-session, next-queue, weekly quality-match players, social replay | control for acquisition, novelty, mode, skill, and calendar mix |
| Did the system operate safely? | queue starvation, population fragmentation, match integrity, reports and enforcement outcomes | restrict sensitive moderation data; do not equate reports with verified violations |

For every rate, provide the eligible denominator and show volume. Use quantiles and distribution plots for waits and latency; averages hide tail failures.

## 4. New-player and social journeys

New players have less reliable skill estimates and are more exposed to bad first matches. Track tutorial/placement completion, rating uncertainty, bot/training exposure, first queue, first valid match, first loss/win, first party, and next-day return. Never treat a provisional rating as established skill.

Measure social value as an observed journey rather than a raw count:

```text
invitation or discovery -> mutual connection -> first co-play -> completed co-play
-> repeat co-play / party formation -> sustained relationship health
```

Useful diagnostics include invitation delivery/acceptance, reciprocal connection, co-play completion, rematch, party stability, guild contribution, isolated-player rate, and harassment/report outcomes. Messaging volume alone is not a social-health KPI. Socially active players are selected; differences in retention are hypotheses until an experiment or defensible causal design supports them.

## 5. Experiments under interference

Players in the same party, guild, or matchmaking pool can affect each other's treatment and outcome. Account-level A/B assignment can therefore violate the no-interference assumption.

Before a matchmaking or social experiment:

1. State the spillover path and the causal estimand.
2. Choose the randomization unit: account only when spillover is negligible; otherwise party/guild/queue cluster, region-time switchback, or another defensible unit.
3. Log assignment, eligibility, actual exposure, configuration version, and partner/cluster context.
4. Run sample-ratio-mismatch and exposure reconciliation checks before outcome analysis.
5. Predefine player-experience guardrails: fairness, P90 wait, latency, disconnect/remake, queue availability, safety, and any economy/revenue risk.
6. Consider simulation/replay for candidate configurations, then validate in a controlled rollout. Simulation is support, not causal proof.

Report unit, window, spillover limitation, primary metric, guardrails, confidence interval/effect size, and decision. Do not hide a harmful tail result behind an acceptable average.

## 6. Safety and review checklist

- Are match-level, player-match, queue, party, and social-edge entities kept distinct?
- Is the exact formation-time configuration and prediction retained?
- Are invalid matches, cancels, bots, smurfs, reconnects, and incidents visible in the denominator policy?
- Does the scorecard balance service, fairness, experience, value, and safety?
- Are new-player uncertainty and regional population effects explicitly segmented?
- Does the experiment design address cross-player interference?
- Are raw chat, reports, and enforcement features access-controlled and purpose-limited?

## Evidence base

- [Microsoft Research: TrueMatch](https://www.microsoft.com/en-us/research/project/truematch/)
- [Microsoft Research: TrueSkill ranking system](https://www.microsoft.com/en-us/research/project/trueskill-ranking-system/)
- [Microsoft Research: QuickSkill for novice cold start](https://www.microsoft.com/en-us/research/?p=890235)
- [Google Research: designing A/B tests in a collaboration network](https://research.google/pubs/designing-ab-tests-in-a-collaboration-network/)
- [Microsoft Research: diagnosing sample-ratio mismatch](https://www.microsoft.com/en-us/research/publication/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments-a-taxonomy-and-rules-of-thumb-for-practitioners/)

For a machine-readable starter contract, see [multiplayer-event-contract.json](../examples/multiplayer-event-contract.json).
