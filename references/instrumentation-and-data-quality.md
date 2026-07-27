# Instrumentation and data quality

## Contents

1. Entity model
2. Event envelope
3. Event families
4. Metric-to-event matrix
5. Reliability rules
6. Quality monitoring
7. Privacy and governance
8. Further implementation guidance

## 1. Entity model

Define relationships before naming events:

```text
person? -> account -> player profile -> character
                 \-> device / platform identity
account -> session -> mode attempt / match / content run
account -> order -> entitlement / virtual transaction
account -> experiment assignment
account <-> party / guild / alliance / social edge
```

Use "person" only when lawful, necessary, and technically supported. Most analyses should rely on pseudonymous product identities.

Resolve:

- guest-to-account linking;
- reinstall and device change;
- cross-platform account linking;
- shared devices and multiple accounts;
- character creation/deletion/migration;
- server/world migration;
- bots, QA, employees, fraud, and banned accounts;
- identity merge and split behavior.

Do not silently mix account, device, character, and human estimates.

## 2. Event envelope

Require a common envelope:

| Field | Purpose |
|---|---|
| event_id | globally unique idempotency key |
| event_name | stable verb-object name |
| event_version | schema version |
| event_time_utc | occurrence time from authoritative clock |
| ingest_time_utc | arrival time |
| account_id / anonymous_id | identity available at event time |
| session_id | deterministic session association |
| platform / region / server_id | operational context |
| app_version / content_version | release context |
| source | client, server, order, ad, support, survey |
| experiment_assignments | immutable assignment IDs/variants |
| properties | event-specific typed fields |
| consent_state | when required by policy |

Store UTC timestamps and derive product/game-day fields centrally. Define allowed client clock skew.

## 3. Event families

Use consistent state transitions rather than UI clicks alone:

- `acquisition_attributed`
- `app_first_launch`
- `account_registered`
- `account_linked`
- `session_started`, `session_ended`
- `tutorial_step_started`, `tutorial_step_completed`
- `core_loop_started`, `core_loop_completed`
- `content_unlocked`, `content_started`, `content_completed`
- `progression_changed`
- `match_queued`, `match_started`, `match_ended`
- `party_joined`, `guild_joined`, `social_edge_created`
- `offer_exposed`, `purchase_started`, `order_completed`, `order_refunded`
- `economy_transaction`
- `gacha_banner_exposed`, `gacha_draw_completed`
- `ad_requested`, `ad_filled`, `ad_impression`, `ad_reward_granted`
- `event_exposed`, `event_participated`, `event_milestone_completed`
- `experiment_assigned`, `feature_exposed`
- `client_error`, `server_error`, `crash`, `disconnect`

Names are examples. Match an existing product convention if one exists.

Capture exposure separately from assignment: assignment proves eligibility, exposure proves the player could have been affected.

## 4. Metric-to-event matrix

For each metric produce:

| Metric ID | Source events/tables | Required fields | Authority | Transform | QA |
|---|---|---|---|---|---|
| retention_d1_exact | activation, qualifying activity | account, anchor time, activity time | server preferred | cohort join | cohort size reconciliation |
| net_revenue | completed/refunded orders | order, currency, gross, fee, tax, refund | order backend | FX and netting | ledger reconciliation |
| content_completion | content start/end | account, content, attempt, result | server | attempt pairing | orphan and duplicate rate |

No production metric should depend on an event that lacks an owner and a test plan.

## 5. Reliability rules

### Authority

- Use server/order authority for entitlements, purchases, refunds, currency, inventory, match outcomes, progression, and rewards.
- Use client telemetry for presentation, device performance, UI interactions, and otherwise unobservable local behavior.
- Reconcile client/server pairs when both are needed.

### Idempotency and ordering

- Make financial/economy events idempotent.
- Use transaction/correlation IDs across request, payment, grant, and refund.
- Define ordering per entity or transaction where sequence matters.
- Accept late events with a bounded watermark and documented backfill behavior.

### Versioning

- Add fields compatibly when possible.
- Version semantic changes.
- Maintain a migration map for renamed events/properties.
- Record first and last valid app/content versions.
- Never reuse an old property with a new meaning.

### Sessionization

Define:

- explicit start/end signals;
- inactivity timeout;
- background and reconnect treatment;
- crash/forced-close closure;
- cross-device overlap;
- maximum plausible duration.

### Money and economy

- Maintain an immutable order ledger.
- Keep real-money orders separate from virtual-currency spend.
- Represent virtual transactions with source/sink reason and balance before/after.
- Preserve original currency and applied FX rate/date.
- Link chargebacks/refunds to original orders.
- For gacha/card draws, preserve banner/config version, displayed cost, currency source, draw count, pity/guarantee before and after, result IDs, and reward-grant correlation IDs. Keep the applicable probability and guarantee configuration snapshot available for audit.

## 6. Quality monitoring

Monitor at event and metric layers:

### Event checks

- volume by version/platform/server;
- schema/type/null validity;
- duplicate event ID rate;
- missing identity/session rate;
- late-arrival distribution;
- timestamp skew and impossible order;
- property-domain violations;
- client/server reconciliation;
- transaction balance continuity.

### Metric checks

- source-to-dashboard reconciliation;
- invariant checks such as payers <= eligible players;
- funnel monotonicity where steps are strictly nested;
- retention numerator <= cohort denominator;
- gross >= defined deductions and net, subject to accounting rules;
- historical backfill delta;
- freshness and completeness SLA;
- unexplained discontinuity after release or pipeline change.

Run synthetic journeys in QA and production-safe test accounts:

1. first launch and registration;
2. tutorial and first value;
3. core-loop start/success/failure;
4. purchase, grant, spend, refund;
5. rewarded ad;
6. match reconnect and disconnect;
7. live-event exposure and completion;
8. cross-device/account link where supported.

## 7. Privacy and governance

- Minimize personal data and separate it from behavioral analytics.
- Apply approved consent, access, retention, deletion, and regional policies.
- Hashing does not automatically make data anonymous.
- Restrict raw chat, support, location, and payment-adjacent data.
- Define metric owners and approvers.
- Maintain semantic definitions as versioned code or controlled metadata.
- Log definition changes and restate historical series only with an explicit policy.
- Treat external platform or regulatory requirements as time-sensitive; verify current official documentation before implementation.

## 8. Further implementation guidance

- Use [telemetry-governance.md](telemetry-governance.md) for the tracking-plan lifecycle, cardinality controls, two-lane routing, and identity/deletion requirements.
- Use [multiplayer-social-analytics.md](multiplayer-social-analytics.md) when the product includes matchmaking, parties, guilds, social graphs, moderation, or networked experiments.
- Use [metric-system-engineering.md](metric-system-engineering.md) for metric naming and composition, the single definition source, alert-threshold design against seasonal baselines, serving-lane choice (real-time / near-line / offline), and the intake-to-adoption operating loop.
- Use [ua-and-marketing-analytics.md](ua-and-marketing-analytics.md) when ad-network, attribution (MMP), or campaign data enters the warehouse: those feeds are partner-owned, restated, and privacy-truncated, so they need reconciliation rules rather than direct joins.
