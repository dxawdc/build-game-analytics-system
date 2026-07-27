# Source synthesis

## Contents

1. Corpus and coverage
2. 《游戏数据分析的艺术》
3. 《游戏数据分析实战》
4. Shared principles incorporated into this skill
5. Legacy caveats and modern extensions
6. Public practitioner sources (2026-07 sweep)

## 1. Corpus and coverage

The skill was created from both PDF books in `D:\AI\数据分析`:

- 《游戏数据分析的艺术》，PDF 424 pages, approximately 420,372 extractable characters.
- 《游戏数据分析实战》，PDF 293 pages, approximately 244,900 extractable characters.

All 717 PDF pages were processed. One primarily visual page had little extractable text. Bookmarks, chapter ranges, text, formulas, and representative visual table-of-contents pages were checked. This file records a synthesis and provenance map; it does not reproduce the books.

PDF page numbers below are the PDF container page numbers, not necessarily the printed page labels.

## 2. 《游戏数据分析的艺术》

### Chapter 1, PDF pages 16-38: understanding game analytics

- Frames analytics as a flow from business need and methodology through data processing, statistical analysis, interpretation, and action.
- Treats instrumentation as a consequence of decomposed business questions.
- Connects player perspective, analyst reasoning, and game design.
- Introduces top-level goals around user scale, popularity, revenue, and marketing.

Skill impact: decision-first intake, metric-to-event traceability, and action-oriented reports.

### Chapter 2, PDF pages 39-62: metrics

- Covers operations data, feedback data, collection methods, AARRR and PRAPA.
- Covers acquisition, active use, retention, revenue, referral, DAU/MAU, ARPU/ARPPU, LTV, and paid-user concepts.
- Emphasizes LTV relative to acquisition cost and a closed growth loop.

Skill impact: lifecycle modules and formal formula contracts. Ambiguous historical terminology is normalized in the metric library.

### Chapter 3, PDF pages 63-79: reports

- Covers status, trend, performance comparison, and product-problem diagnosis.
- Emphasizes readability, comparability, analyzability, and predictive usefulness.
- Links reports to business action and asks whether analytical value exceeds cost.

Skill impact: dashboard and decision-report templates.

### Chapter 4, PDF pages 80-144: statistical foundations

- Covers descriptive statistics, distributions, sampling, experiment design, contingency tables, tests for categorical and quantitative data, ANOVA/ANCOVA, time-series analysis, exponential smoothing, and correlation.

Skill impact: method selection, weighted rates, uncertainty, robust summaries, experimental safeguards, and forecast baselines.

### Chapter 5, PDF pages 145-183: user analysis

- Covers new users, registration conversion, DAU, active-user composition, play time, cohort/generation analysis, and LTV.
- Decomposes DAU into contributions from new-user cohorts and their retention.
- Highlights product quality, crashes, errors, progression, and acquisition dimensions.

Skill impact: active-population decomposition, first-value funnel, cohort LTV, and quality guardrails.

### Chapter 6, PDF pages 184-219: retention

- Distinguishes retention stages and influences from user quality, environment, and product.
- Uses exact-day cohort retention and weighted aggregation.
- Examines different user groups, time periods, and products; discusses early loss and stable tail.

Skill impact: exact/rolling/bracket definitions, cohort anchors, survival framing, and weighted aggregation.

### Chapter 7, PDF pages 220-258: revenue

- Decomposes revenue through active users, payer conversion, and ARPPU.
- Covers first and repeat purchase, payer segments, frequency, intervals, cohort revenue, and LTV/CAC.
- Shows diagnostic trees for revenue decline.

Skill impact: revenue identity, payer lifecycle, concentration, cohort maturity, and explicit ROAS/ROI separation.

### Chapter 8, PDF pages 259-273: channels

- Evaluates channel quantity, user quality, revenue, cost, and loyalty.
- Proposes monitoring, comparison, selection, and reinvestment as a loop.

Skill impact: multi-horizon channel quality and marginal-return analysis.

### Chapter 9, PDF pages 274-311: content and operations

- Covers targeted messaging, churn prediction, purchase/payment scenes, version operations, long-tail item strategy, and activity analysis.
- Stresses placing analytical findings into concrete product scenes.

Skill impact: intervention-aware churn, payment funnel, version/live-event analysis, and content/economy modules.

### Chapters 10-11, PDF pages 312-386: data processing and visualization

- Covers R data structures, cleaning, joining, grouping, exploration, visualization, and database interaction.
- Shows charts for distributions, retention, progression, and multivariate relationships.

Skill impact: reproducible transformation, distribution-aware visualization, and semantic consistency. Tool-specific R syntax is not required by the skill.

### Chapter 12, PDF pages 387-424: advanced cases

- Covers correspondence analysis for player/item preference.
- Covers association rules using support, confidence, and lift.
- Covers DBSCAN for dense behavioral patterns and anomalous studio/bot activity.
- Covers graph/network analysis for relationships and asset-transfer networks.

Skill impact: advanced discovery playbooks, with validation and enforcement safeguards.

## 3. 《游戏数据分析实战》

### Chapter 1, PDF pages 15-34: data-driven operations

- Covers analysis workflow, business context, report quality, visualization, SQL/Excel-oriented work, and examples of weak versus decision-ready conclusions.
- Lists comparison, grouping, structure, cross-tab, funnel, matrix, 5W1H, correlation, regression, clustering, time series, and variance analysis.

Skill impact: problem framing, report structure, and broad method routing.

### Chapter 2, PDF pages 35-45: key metrics

- Defines activation and conversion funnels, retention, payer metrics, acquisition costs, LTV, and ROI.
- Shows why mobile and PC-era operational definitions differ.

Skill impact: strict population, entity, time, and revenue-basis qualifiers. Historical quality thresholds are not carried forward as universal benchmarks.

### Chapter 3, PDF pages 46-70: preheat/release preparation

- Covers reservation-user research, survey/behavior linkage, reservation conversion forecasts, and competitive analysis.
- Uses existing-product behavior to understand target audience and forecast conversion.

Skill impact: pre-launch research, identity linkage, biased-sample cautions, and scenario forecasts.

### Chapter 4, PDF pages 71-131: closed testing

- Covers playtest surveys, channel quality, client package-size funnel, launch revenue/active forecasts, marketing-budget scenarios, and churn reasons.
- Links qualitative survey results with observed progression, combat, guild, map, and task behavior.

Skill impact: closed-test metric pack, mixed-method diagnosis, launch-readiness and capacity planning.

### Chapter 5, PDF pages 132-166: launch market analysis

- Covers competitor timing, server-count forecasting, advertising effectiveness, and device/OS distribution.
- Uses time series for concurrency forecasting and multiple matching methods for campaign attribution.

Skill impact: launch timing/capacity, channel reconciliation, device-quality dimensions, and attribution confidence.

### Chapter 6, PDF pages 167-215: player analysis

- Defines churn from observed return behavior rather than a universal rule.
- Covers level/dungeon loss, level payer conversion, uninstall feedback, 5W1H, active-user segmentation, and reservation-user follow-through.
- Uses clustering and behavioral/qualitative data to identify segments and pain points.

Skill impact: cadence-derived churn, progression drop-off, mixed evidence, and action-oriented segmentation.

### Chapter 7, PDF pages 216-239: payment analysis

- Covers item-spend preferences by payer band, high-value churn prediction, pricing research, revenue decline, targets, and alerts.
- Evaluates churn classification with accuracy, precision-like hit rate, and recall-like coverage.

Skill impact: payer-segment distributions, pricing validation, prediction protocols, and target/reconciliation alerts.

### Chapter 8, PDF pages 240-293: versions and live operations

- Covers version adoption/effect, activity ROI, new-server effect, server merge, balance, surveys, and chat-text analysis.
- Examines active users, income, retention, conversion, content participation, advertising, server health, and sentiment together.

Skill impact: exposure-aware version analysis, event counterfactuals, server-age controls, balance and text-feedback modules.

## 4. Shared principles incorporated into this skill

- Start from a business question and product scene.
- Use a metric system, not isolated metrics.
- Follow users and cohorts across acquisition, activation, retention, and revenue.
- Pair volume with quality and cost.
- Diagnose through dimensions, funnels, segments, and decompositions.
- Link behavioral, transactional, operational, survey, support, and text data where lawful and useful.
- Turn findings into owned actions and validate their effect.
- Treat definitions and data quality as part of analysis, not preparation trivia.

## 5. Legacy caveats and modern extensions

The books contain valuable reasoning and cases, but their ecosystem reflects earlier PC/mobile publishing practices. Apply these safeguards:

- Do not reuse historical retention, activation, or channel thresholds as current benchmarks.
- Do not call revenue/ad spend "ROI"; use ROAS and profit ROI explicitly.
- Do not infer a person from a device without a supported identity model.
- Do not assume all F2P revenue is IAP; support ads, subscriptions, passes, DLC, marketplaces, refunds, fees, and taxes.
- Do not use pre/post version or event comparisons as causal proof.
- Do not rely only on averages for skewed payer, time, economy, or latency data.
- Add modern experiment exposure, semantic versioning, data observability, cross-platform identity, economy ledgers, quality/reliability, fairness, privacy, and trust guardrails.
- Verify current platform, privacy, accounting, and regulatory requirements from official sources before implementation.

## 6. Public practitioner sources (2026-07 sweep)

A second pass added Chinese-market operating practice that the two books predate: paid-acquisition diagnosis,
IAA/hybrid monetization, mini-game platforms, metric-platform engineering, alerting, and bilingual definition
disputes. The material below informed
[cn-terminology-and-pitfalls.md](cn-terminology-and-pitfalls.md),
[framework-crosswalk.md](framework-crosswalk.md),
[ua-and-marketing-analytics.md](ua-and-marketing-analytics.md),
[hybrid-monetization-and-iaa.md](hybrid-monetization-and-iaa.md),
[growth-accounting-and-forecasting.md](growth-accounting-and-forecasting.md),
[metric-system-engineering.md](metric-system-engineering.md), and
[case-studies.md](case-studies.md).

### How the sweep was done, and its limits

- Retrieval used web search result pages plus direct page fetches. WeChat official-account (公众号) article bodies
  have **no usable public index**: a WeChat-specific search returned mostly event promotions, book launches, and
  course ads rather than substantive method articles, and article URLs are session-scoped redirects. Practitioner
  content that originates on 公众号 is therefore reached through its republished form on open industry sites.
- Sources are therefore industry portals, vendor engineering blogs, cloud developer communities, and technical blogs.
  Treat all of it as **secondary practitioner opinion**, not peer-reviewed or vendor-neutral evidence.
- Most articles state no date, region, genre, platform, or measurement definition. Consequently the sweep imported
  **reasoning structures, decomposition identities, diagnosis sequences, and failure modes**, and deliberately did
  not import numeric thresholds, eCPM levels, retention "good/bad" lines, or channel share percentages.
- Case material in [case-studies.md](case-studies.md) retains illustrative figures purely to keep the worked
  examples legible; each case is annotated with what the original conclusion got wrong or left unvalidated.

### Principal sources consulted

| Source | Contributed |
|---|---|
| GameRes 游资网 — 8000字详解如何从底层搭建游戏数据分析框架 (gameres.com/868523.html) | framework inventory (AARRR/PRAPA/RFM/5W1H), instrumentation-to-design linkage, LTV-net-of-channel-share |
| GameRes — 手游买量投放中那些常见的数据分析思路 (gameres.com/856878.html) | three-layer UA data model, campaign diagnosis sequence, eCPM/CTR/CVR decomposition, test-window practice |
| GameRes — 从设计到归因 AB Test 实战心得 (gameres.com/867343.html) | experiment bucketing evolution, region-segmented readouts, pre/post attribution technique |
| GameRes — 手游产品最常用的5种玩家行为数据分析模型 (gameres.com/815514.html) | event/retention/funnel/segment/property model taxonomy and required fields |
| GameRes — 游戏数据分析的三大实战案例深度解读 (gameres.com/873012.html) | cases 1–3 in case-studies.md, including the DAU-feasibility inversion |
| GameRes — 挖掘游戏行为数据价值的6个新思路 (gameres.com/901091.html) | anomaly monitoring, balance tracking via tags, full-funnel ad data joining |
| GameRes — 谈谈游戏数据分析的那点事 (gameres.com/859074.html) | analyst/designer/engineer alignment on 口径 before implementation |
| Tencent Cloud developer community — 游戏指标生态与自驱决策体系搭建攻略 (article 2600417) | primary/auxiliary/alert metric tiers, metric relationship graph, elastic baseline thresholds, real-time/near-line/offline serving lanes, human-in-the-loop automation |
| SolarEngine engineering blog — IAA game key metrics dashboard; IAA eCPM optimization | IAA funnel metric set, mediation/floor/format levers, ad-load-versus-retention guardrails |
| CSDN / practitioner blogs — 手游ROI及LTV预估方法 | retention-curve fitting (power/exponential), LTV = Σ(retention × ARPU), weighted-retention fitting caution |
| Alibaba DataWorks / NetEase EasyData docs and warehouse-practice posts — 原子/派生/复合指标、修饰词 | metric composition model and naming convention in metric-system-engineering.md |
| WeChat mini-game platform developer docs and mini-game monetization write-ups | mini-game identity/attribution/session/revenue-share specifics |

### Explicitly rejected from these sources

- "次日留存 > 50% means a quality product", "retention halves at each milestone", "channel share is ~50%",
  and per-format eCPM ranges — all undated and context-free. Recorded in
  [cn-terminology-and-pitfalls.md](cn-terminology-and-pitfalls.md) as folklore to test, never as targets.
- Vendor tool recommendations and product feature lists.
- Any claim that a pre/post comparison or a segment correlation demonstrated causation.
