---
name: build-game-analytics-system
description: Design, review, or extend a decision-oriented game analytics system for mobile, PC, console, web, MMO, RPG, SLG, card/gacha, casual, competitive PvP, premium, subscription, ad-supported, hybrid, live-service, or UGC games. Use for 游戏数据分析、游戏指标体系、KPI/北极星指标、指标树、指标口径字典、埋点方案、事件模型、留存/流失/付费/LTV/ROI/ROAS/渠道/活动/版本/内容/经济系统/社交/服务器/质量分析、看板规划、实验设计、数据预警，或为具体游戏产品从零搭建分析框架。
---

# Build Game Analytics System

Build an analytics system that helps a team make decisions, not a long list of generic metrics.
Adapt every definition to the product's core loop, business model, lifecycle, identity model, and available data.

## Core workflow

1. Establish the product brief.
   - Capture genre, platforms, regions, business model, lifecycle stage, core loop, session pattern, social structure, content cadence, and current business questions.
   - Capture identity unit, timezone, currency, revenue basis, attribution window, and known data sources.
   - If context is incomplete, state minimal assumptions and continue. Ask only when a missing choice would materially change the system.
   - Read [product-intake-and-kpi-tree.md](references/product-intake-and-kpi-tree.md).

2. Choose the product archetype and metric modules.
   - Select one primary archetype and any secondary traits.
   - Do not transplant mobile F2P metrics onto premium, competitive, MMO, or UGC products without adapting the value model.
   - Read [product-archetypes.md](references/product-archetypes.md).

3. Build the KPI tree.
   - Start with business outcomes and player value.
   - Choose one north-star metric or a small north-star system.
   - Add outcome, driver, diagnostic, and guardrail metrics.
   - Express causal hypotheses as hypotheses, not facts.

4. Formalize the metric dictionary.
   - Give every metric a business question, exact population, numerator, denominator, time window, grain, entity, dimensions, filters, exclusions, data source, freshness, owner, and zero/late-data policy.
   - Distinguish exact-day, rolling, and bracket retention; gross bookings and net revenue; ROAS and profit ROI; account, player, character, and device.
   - Read [metric-library.md](references/metric-library.md).

5. Design the data contract.
   - Map metrics to authoritative client, server, order, ad, match, social, content, and experiment events.
   - Prefer server-authoritative events for money, inventory, progression, match results, and entitlements.
   - Define identity stitching, event versioning, deduplication, late-arrival, refund, test-account, bot, and timezone policies.
   - Read [instrumentation-and-data-quality.md](references/instrumentation-and-data-quality.md).

6. Select analyses and decision loops.
   - Match the method to the decision: decomposition, funnel, cohort, survival, segmentation, experiments, causal comparison, forecasting, churn prediction, economy flow, association, clustering, or network analysis.
   - Never present a pre/post change or correlation as causal evidence without a defensible design.
   - Read [analysis-playbooks.md](references/analysis-playbooks.md).

7. Produce implementation-ready artifacts.
   - Default to: product brief, KPI tree, metric dictionary, event matrix, dashboard plan, analysis backlog, experiment/validation plan, and assumptions/risks.
   - Scale the output to the request. A quick review can be compact; a build request should include all artifacts.
   - Read [deliverable-templates.md](references/deliverable-templates.md).

8. Validate before handoff.
   - Check that each top-level goal has drivers and guardrails.
   - Check formula algebra, population consistency, cohort anchors, period alignment, currency and revenue basis, double-counting, and event coverage.
   - If a machine-readable metric spec exists, run:

```powershell
python scripts/validate_metric_spec.py <metric-spec.json-or-yaml>
```

## Operating rules

- Lead with the recommended system and the decisions it supports.
- Prefer a compact, product-specific metric set over exhaustive metric dumping.
- Separate launch MVP metrics from later maturity metrics.
- Label assumed, derived, predicted, and causally estimated values.
- Do not invent industry benchmarks. Require source, region, genre, platform, acquisition mix, cohort date, and measurement definition before comparison.
- Treat historical thresholds in the source books as examples, never as current universal standards.
- Define ambiguous acronyms locally. ARPU, ROI, activation, active user, churn, and retention often vary across teams.
- Use weighted aggregation for rate metrics; do not average daily percentages unless that is the stated definition.
- Report both absolute volume and rate where either can hide the other.
- Protect player experience with quality, fairness, privacy, and monetization guardrails.
- Avoid collecting unnecessary personal data. Use approved consent and retention policies.

## Source-grounded knowledge

The reference system synthesizes both project books across all 717 PDF pages and adds modern product, experimentation, economy, reliability, and semantic-layer practices. For chapter coverage, legacy caveats, and concept provenance, read [source-synthesis.md](references/source-synthesis.md).
