# Telemetry governance and event contracts

## Contents

1. The tracking plan as a data product
2. Event and property design
3. Cardinality and data lanes
4. Contract lifecycle and quality SLOs
5. Identity, privacy, and deletion
6. Practical review checklist

## 1. The tracking plan as a data product

Treat the tracking plan as a versioned contract between game client, server, data engineering, analytics, live ops, and privacy/security owners. It is not merely a spreadsheet of event names.

For each event record:

- decision or metric it supports;
- event name, version, actor/entity, trigger, and authoritative producer;
- delivery lane: `real_time`, `telemetry`, or `both`;
- each property's type, requiredness, valid range/domain, cardinality class, and data classification;
- identity, correlation, ordering, idempotency, retention, access, owner, approver, and test scenario;
- schema status and deprecation/migration date.

Event names should describe a stable business state transition, such as `match_formed`, `match_ended`, or `reward_granted`. A button click alone rarely proves the player received a result. Preserve both when the decision needs intent and outcome.

## 2. Event and property design

Use a shared envelope and typed event-specific properties. Maintain one canonical semantic definition for each event/property and map it into vendor or warehouse schemas rather than allowing each consumer to reinterpret it.

Good patterns:

- stable, verb-object names; version semantic changes rather than silently repurposing a property;
- numeric measures in numeric fields; controlled categories in bounded enums;
- transaction, attempt, match, party, session, and experiment IDs as correlation properties;
- server-authoritative state for rewards, purchases, balances, match outcomes, entitlements, and progression;
- explicit `experiment_assigned` and `feature_exposed` events, each with experiment/configuration version.

Avoid:

- player IDs, item-instance IDs, timestamps, coordinates, error messages, search text, or arbitrary URLs in event names;
- free text and unbounded identifiers as dashboard dimensions;
- changing the meaning of a live event/property in place;
- treating client reporting as proof of a server-side grant or payment.

If high-detail raw data is genuinely required for debugging, fraud, or replay, classify it, restrict access and retention, and keep it out of routine self-service dashboards.

## 3. Cardinality and data lanes

Every event/property needs an intentional cardinality budget. Dynamic names and unbounded dimensions fragment reports, increase cost, hide trends, and can exceed platform limits. Use reusable event names with typed properties; promote only bounded, decision-useful values to common dimensions.

Use two deliberate delivery lanes:

| Lane | Use for | Design preference |
|---|---|---|
| Real-time operational | incident signals, live-ops triggers, server state, abuse/fraud flags, entitlement failures | small payloads, strong identity/ordering, latency and delivery SLO |
| Telemetry / warehouse | journey analysis, funnels, segmentation, aggregate reporting, model features | complete context, late-arrival policy, efficient batch/export, reproducible history |

An event can appear in both lanes when a fast action and later analysis need the same state transition. Keep a shared event/correlation ID and document which copy is authoritative. Do not force all clickstream through the costly or restrictive real-time lane.

## 4. Contract lifecycle and quality SLOs

Recommended lifecycle:

```text
proposed -> approved -> implemented -> validated -> official -> deprecated
```

Before `official`, validate against a synthetic journey and production-safe test account. Check schema, producer version, event counts, correlation, deduplication, authority, late arrival, and metric reconciliation. Separate staging from production data.

Set observable SLOs appropriate to the decision, for example:

- freshness and late-arrival distribution;
- completeness against server/order/control totals;
- duplicate, malformed, null, and invalid-domain rate;
- identity/session coverage;
- payload size and cardinality trends;
- schema drift and deprecated-event use;
- client/server or request/grant reconciliation.

Schema validation is a guardrail, not an excuse to discard evidence silently. Alert, quarantine, and quantify rejected or late records; define backfill/restatement policy before stakeholders rely on a dashboard.

## 5. Identity, privacy, and deletion

Model the identity graph deliberately: anonymous device, account, player profile, character, platform account, and linked identities can differ. Record the identity available at event time and do not retroactively overclaim person-level precision.

Classify data before collection. Pseudonymization (including hashing) reduces exposure but does not necessarily make data anonymous. Minimize personal and sensitive content, especially raw chat, voice, precise location, support text, payment-adjacent data, and moderation evidence. Limit access, retention, and secondary use.

Deletion/export workflows must traverse the identity graph and downstream copies, including warehouses, vendor exports, and derived feature stores where applicable. Make the legal/privacy owner validate jurisdictional requirements; this reference is operational guidance, not legal advice.

## 6. Practical review checklist

- Can every event be traced to a decision, metric, experiment, or operational response?
- Is the business state, authority, entity, time, version, and correlation clear?
- Are names stable and dimensions bounded?
- Does each sensitive or high-cardinality field have a stated classification, access, retention, and purpose?
- Is real-time delivery justified by a response requirement?
- Can a synthetic journey prove the event end-to-end and reconcile it with its authoritative source?
- Are deprecation, schema drift, rejected records, and metric restatement visible to consumers?

## Evidence base

- [GameAnalytics: progression event structure and hierarchy](https://docs.gameanalytics.com/events-metrics-and-filtering/event-types/progression-events/)
- [GameAnalytics: event tracking and cardinality limits](https://docs.gameanalytics.com/event-tracking-and-integrations/data-retention-and-limits/event-tracking-and-cardinality-limits/)
- [Microsoft PlayFab: telemetry overview](https://learn.microsoft.com/en-us/xbox/playfab/data-analytics/ingest-data/telemetry-overview)
- [Microsoft PlayFab: real-time analytics core concepts](https://learn.microsoft.com/en-us/xbox/playfab/data-analytics/ingest-data/real-time-analytics-core-concepts)
- [Amplitude: create a tracking plan](https://amplitude.com/docs/data/create-tracking-plan)
- [UK ICO: anonymisation and pseudonymisation guidance](https://ico.org.uk/media2/aahlfdke/anonymisation-all-1-0-21.pdf)
