---
name: build-game-analytics-system
description: Design, review, or extend a decision-oriented game analytics system for mobile, PC, console, web, mini-game, MMO, RPG, SLG, card/gacha, casual, competitive PvP, premium, subscription, ad-supported, hybrid, live-service, or UGC games. Use for 游戏数据分析、游戏指标体系、KPI/北极星指标、指标树、指标口径字典、指标平台/原子指标与派生指标、埋点方案、事件模型、留存/流失/付费/LTV/ROI/ROAS/回本周期/渠道/买量投放/素材与计划诊断/归因与反作弊/广告变现与 IAA/混合变现/小游戏/活动/版本/内容/经济系统/社交/服务器/质量分析、DAU 预测与预算反推、看板规划、实验设计、数据预警与告警阈值，或为具体游戏产品从零搭建分析框架。
---

# Build Game Analytics System

Build an analytics system that helps a team make decisions, not a long list of generic metrics.
Adapt every definition to the product's core loop, business model, lifecycle, identity model, and available data.

## Core workflow

1. Establish the product brief.
   - Capture genre, platforms, regions, business model, lifecycle stage, core loop, session pattern, social structure, content cadence, and current business questions.
   - Capture identity unit, timezone, currency, revenue basis, attribution window, and known data sources.
   - Capture the team's existing metric vocabulary and what each word currently means to them.
   - If context is incomplete, state minimal assumptions and continue. Ask only when a missing choice would materially change the system.
   - Read [product-intake-and-kpi-tree.md](references/product-intake-and-kpi-tree.md).
   - For Chinese-language teams, partner/publisher reconciliation, or any disputed metric word, read [cn-terminology-and-pitfalls.md](references/cn-terminology-and-pitfalls.md).

2. Choose the product archetype and metric modules.
   - Select one primary archetype and any secondary traits.
   - Do not transplant mobile F2P metrics onto premium, competitive, MMO, mini-game, or UGC products without adapting the value model.
   - Read [product-archetypes.md](references/product-archetypes.md).
   - If the team already uses AARRR, RARRA, PRAPA, RFM, HEART, GSM/OSM, or 5W1H, translate it instead of discarding it: [framework-crosswalk.md](references/framework-crosswalk.md).
   - Add the paid-acquisition module when UA/buying is in scope: [ua-and-marketing-analytics.md](references/ua-and-marketing-analytics.md).
   - Add the ad-monetization module for IAA, hybrid, or mini-game products: [hybrid-monetization-and-iaa.md](references/hybrid-monetization-and-iaa.md).

3. Build the KPI tree.
   - Start with business outcomes and player value.
   - Choose one north-star metric or a small north-star system.
   - Add outcome, driver, diagnostic, and guardrail metrics.
   - Express causal hypotheses as hypotheses, not facts.

4. Formalize the metric dictionary.
   - Give every metric a business question, exact population, numerator, denominator, time window, grain, entity, dimensions, filters, exclusions, data source, freshness, owner, and zero/late-data policy.
   - Distinguish exact-day, rolling, and bracket retention; gross bookings and net revenue; ROAS and profit ROI; account, player, character, and device.
   - Record local-language names and aliases against the metric ID so a partner's term maps to your definition instead of replacing it.
   - Read [metric-library.md](references/metric-library.md).
   - For naming, atomic/derived/composite composition, versioning, and the single definition source, read [metric-system-engineering.md](references/metric-system-engineering.md).

5. Design the data contract.
   - Map metrics to authoritative client, server, order, ad, match, social, content, and experiment events.
   - Prefer server-authoritative events for money, inventory, progression, match results, and entitlements.
   - Define identity stitching, event versioning, deduplication, late-arrival, refund, test-account, bot, and timezone policies.
   - Read [instrumentation-and-data-quality.md](references/instrumentation-and-data-quality.md).
   - When designing or reviewing event collection, also read [telemetry-governance.md](references/telemetry-governance.md). Treat the tracking plan as a versioned data contract, not an informal event list.
   - For multiplayer, matchmaking, party, guild, or social features, also read [multiplayer-social-analytics.md](references/multiplayer-social-analytics.md).
   - Treat ad-network, MMP/attribution, and store feeds as partner-owned, restated, and privacy-truncated: reconcile them, do not join them as exact.

6. Select analyses and decision loops.
   - Match the method to the decision: decomposition, funnel, cohort, survival, segmentation, experiments, causal comparison, forecasting, churn prediction, economy flow, association, clustering, or network analysis.
   - Never present a pre/post change or correlation as causal evidence without a defensible design.
   - Read [analysis-playbooks.md](references/analysis-playbooks.md).
   - For DAU decomposition, retention-curve fitting, LTV/payback projection, target feasibility, and budget inversion, read [growth-accounting-and-forecasting.md](references/growth-accounting-and-forecasting.md).
   - For worked end-to-end examples, including two where the original conclusion was wrong, read [case-studies.md](references/case-studies.md).

7. Produce implementation-ready artifacts.
   - Default to: product brief, KPI tree, metric dictionary, event matrix, dashboard plan, analysis backlog, experiment/validation plan, and assumptions/risks.
   - Include alerting design (baseline, elastic threshold, severity, owner, first action) whenever the system will be monitored, not just reported.
   - Scale the output to the request. A quick review can be compact; a build request should include all artifacts.
   - Read [deliverable-templates.md](references/deliverable-templates.md).

8. Validate before handoff.
   - Check that each top-level goal has drivers and guardrails.
   - Check formula algebra, population consistency, cohort anchors, period alignment, currency and revenue basis, double-counting, and event coverage.
   - Check that every rate carries its denominator, every projection carries its horizon and error, and every money metric carries its basis.
   - If a machine-readable metric spec exists, run:

```powershell
python scripts/validate_metric_spec.py <metric-spec.json-or-yaml>
```

   - The validator also warns on revenue/spend named ROI, ROAS or LTV without a horizon, LTV without a
     realized/predicted label, and a benchmark without provenance. See
     [examples/hybrid-ua-metric-spec.json](examples/hybrid-ua-metric-spec.json) for a UA plus hybrid-monetization
     spec that passes `--strict`, and [examples/multiplayer-event-contract.json](examples/multiplayer-event-contract.json)
     for a governed event contract.

## Operating rules

- Lead with the recommended system and the decisions it supports.
- Prefer a compact, product-specific metric set over exhaustive metric dumping.
- Separate launch MVP metrics from later maturity metrics.
- Label assumed, derived, predicted, and causally estimated values.
- Do not invent industry benchmarks. Require source, region, genre, platform, acquisition mix, cohort date, and measurement definition before comparison.
- Treat historical thresholds in the source books, and threshold folklore circulating in industry articles, as examples to test, never as current universal standards.
- Define ambiguous acronyms locally. ARPU, ROI, activation, active user, churn, retention, 消耗, 流水, and 留存 often vary across teams.
- Never label revenue/spend as ROI. Use ROAS with an explicit horizon, and reserve profit ROI for contribution net of cost.
- Use weighted aggregation for rate metrics; do not average daily percentages unless that is the stated definition.
- Report both absolute volume and rate where either can hide the other.
- Decompose before hypothesizing: revenue, DAU, and ad revenue each have an identity that tells you which factor and which team owns the movement.
- Protect player experience with quality, fairness, privacy, and monetization guardrails.
- Avoid collecting unnecessary personal data. Use approved consent and retention policies.
- Keep stable event names and bounded dimensions. Put dynamic IDs, timestamps, coordinates, or unbounded text in typed properties or restricted raw data, never in event names or dashboard dimensions.
- Route low-latency operational signals and analysis telemetry deliberately. The same player journey may need correlated events in both lanes, but real-time delivery is not a default for all clickstream.
- Record experiment assignment and actual exposure separately. For networked features, state the interference risk and choose a defensible randomization unit before claiming a causal effect.
- For matchmaking, freeze the formation-time rating, uncertainty, prediction, queue configuration, latency, and party context; do not retrospectively substitute later state into fairness analysis.
- Build alerts on seasonal, mix-matched baselines with elastic thresholds, severity tiers, an owner, and a first action. Check for a data incident before believing a large sudden move.
- When a definition changes, create a new metric ID and deprecate the old one. Never silently re-point a name at a new formula.
- Use marginal, not average, returns for scaling decisions, and separate accounting payback from cash payback.
- A metric target met by changing population composition is not a result. Report value per active alongside any count that hit its goal.
- Close the loop: record whether a recommendation was adopted, what happened, and whether the predicted effect materialized.

## Source-grounded knowledge

The reference system synthesizes both project books across all 717 PDF pages, adds modern product, experimentation,
economy, reliability, and semantic-layer practice, and incorporates a 2026-07 sweep of public Chinese-market
practitioner material (UA diagnosis, IAA/hybrid monetization, mini-game platforms, metric-platform engineering).
For chapter coverage, external source provenance, retrieval limits, and what was deliberately rejected, read
[source-synthesis.md](references/source-synthesis.md).
