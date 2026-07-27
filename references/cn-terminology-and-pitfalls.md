# Chinese-market terminology and definition pitfalls

Chinese-language game teams use a dense vocabulary that rarely maps one-to-one onto English analytics terms.
Most "data disputes" in these teams are vocabulary disputes, not analysis disputes.
Resolve the word before resolving the number.

Use this file when the team, the request, or the source data is Chinese-language, when reconciling numbers
against a publisher/channel/CP partner, or when a metric name is asserted without a formula.

## 1. High-risk homonyms — always disambiguate first

| Term | Reading A | Reading B | How to resolve |
|---|---|---|---|
| 消耗 | ad spend (投放消耗) | virtual-currency/resource sink (经济消耗) | Ask which lane. Never let one dashboard column mean both. |
| ROI | revenue / spend (i.e. ROAS) | (contribution - cost) / cost | Rename to ROAS or profit ROI in the dictionary; keep the local label as an alias only. |
| 流水 | gross bookings before platform fee | sometimes post-fee, per finance habit | Pin gross/net, fee basis, refund basis, FX date. |
| 收入 | recognized revenue | post-share net revenue (分成后) | State the share chain: platform, channel, publisher, IP. |
| 留存 | exact-day retention | rolling retention, or "still active" | Pin anchor + type (see §3). |
| 活跃 | any login | qualifying in-game action | Login-only 活跃 inflates DAU and hides engagement loss. |
| 回流 | returning after N inactive days | any non-new active user | Define the inactivity threshold and whether it is exclusive of 留存. |
| 新增 | device/install | account/role/character | Pin the identity unit; 建角 and 注册 are different entities. |
| 付费率 | payers / active users | payers / new users, or / installs | Denominator must be explicit in the name or the spec. |
| 转化率 | click→install | install→register→pay, or step-specific | Never ship a bare 转化率. |
| DAU | distinct accounts | distinct devices, or distinct roles | Multi-role/multi-account games diverge sharply. |
| 在线 | concurrent (ACU/PCU) | daily active | 在线人数 usually means concurrency; 在线用户 often means DAU. |

## 2. Vocabulary crosswalk

### Users and activity

| Chinese | Common English/abbrev | Definition requirement |
|---|---|---|
| 新增用户 / DNU | daily new users | install, first launch, registration, or first role — pick one |
| 日活 / 周活 / 月活 | DAU / WAU / MAU | qualifying activity + timezone + game-day boundary |
| 同时在线 / 最高在线 | ACU / PCU | sampling interval and aggregation |
| 粘性 | DAU/MAU | window alignment (trailing 30 vs calendar month) |
| 次留 / 2留 / 3留 / 7留 / 30留 | D1/D2/D3/D7/D30 retention | anchor date and retention type |
| 流失 | churn | inactivity rule derived from return curves, not a default 7/14/30 |
| 回流 / 召回 | resurrection / win-back | prior-inactivity threshold + observation window |
| 建角率 | role-creation rate | denominator: installs, launches, or registrations |
| 导量 / 买量 / 跑量 | UA volume / paid acquisition / delivery volume | paid vs organic classification policy |
| 大R / 中R / 小R / 零氪 | whale / mid / low spender / non-payer | banding rule (cumulative spend? window? percentile?) |
| 白嫖党 | non-paying but engaged | not the same as churn risk |

### Money

| Chinese | Common English/abbrev | Definition requirement |
|---|---|---|
| 充值 | top-up / bookings | real money in; not yet consumed |
| 消耗（经济） | sink | virtual currency spent; never count as revenue |
| 首充 / 复充 | first purchase / repeat purchase | window and SKU scope |
| 付费渗透率 | payer penetration | population and period |
| 客单价 | AOV or ARPPU depending on team | transaction-level vs payer-level |
| 回本周期 / 回收周期 | payback period | cost scope, revenue basis, discounting |
| 回收率 | cumulative ROAS at day n | horizon must be in the name (e.g. ROAS_D30) |
| 分成 | platform/channel share | list the full share chain |
| 内购 / 广告变现 / 混变 | IAP / IAA / hybrid | see [hybrid-monetization-and-iaa.md](hybrid-monetization-and-iaa.md) |
| 买断 / 内购制 / 订阅 | premium / F2P / subscription | value model differs; see [product-archetypes.md](product-archetypes.md) |

### Content, economy, live ops

| Chinese | English | Note |
|---|---|---|
| 卡点 | stuck point / progression wall | needs attempt- and player-level denominators |
| 内容消耗度 | content consumption pace | used to forecast content-supply exhaustion |
| 数值膨胀 / 通胀 | power creep / currency inflation | different phenomena; measure separately |
| 产出 / 消耗 | sources / sinks | ledger-based, per reason code |
| 爆率 / 掉率 / 保底 / 歪了 | drop rate / pity / off-target pull | validate observed vs configured distribution |
| 开服 / 滚服 / 合服 | server launch / rolling launch / merge | align analysis by server age |
| 赛季 / 版本 / 活动 | season / version / event | freeze definitions across them |
| 素材 / 计划 / 出价 / 控量 | creative / campaign / bid / volume throttling | see [ua-and-marketing-analytics.md](ua-and-marketing-analytics.md) |
| 埋点 / 上报 / 日志 | instrumentation / reporting / logs | see [telemetry-governance.md](telemetry-governance.md) |
| 口径 | metric definition contract | the single most contested artifact |

## 3. The 留存 trap

Chinese teams say 次日留存 for at least three different computations:

```text
A. exact-day:  active on exactly anchor+1 / cohort
B. rolling:    active on or after anchor+1 / cohort
C. loose:      any activity in the 24-48h window after install, device-based
```

Also common: 加权留存 (weighted retention), which is the correct cross-cohort aggregation:

```text
weighted D_n = sum(retained) / sum(eligible cohort)
```

Do not average daily retention percentages unless that is the stated definition.
When comparing against a partner's number, reconcile in this order:
identity unit → anchor event → retention type → timezone/game-day → exclusions (test, bot, refund, reinstall).

## 4. Aggregation and reporting conventions to pin down

- **Game day (游戏日)**: many products roll the day at 04:00 or 05:00 local, not 00:00. State it.
- **Timezone**: domestic products often UTC+8 fixed; global products may use per-region local time. Never mix.
- **Currency and FX**: state the FX date policy (transaction date vs month-end vs fixed plan rate).
- **Rate aggregation**: use weighted sums, not means of daily rates.
- **Skewed metrics**: playtime, spend, and pulls need median/P75/P90 and concentration, not means alone.
- **Channel-side vs game-side numbers will not match.** Expect gaps from attribution windows, dedup, refunds,
  and rejected traffic. Agree on which side is authoritative for which decision before the dispute occurs.

## 5. Benchmark discipline

Chinese-language articles, decks, and vendor blogs circulate threshold folklore, for example
"次留 above 50% means a good product", "retention roughly halves at each of D1/D7/D30",
"channel share is about 50%", or fixed eCPM ranges per ad format.

Treat all such figures as **undated, unsourced examples**, never as standards. Before any comparison, require:
source, region, genre, platform, acquisition mix, cohort date, measurement definition, and sample size.
Prefer the product's own historical distribution and internal control groups as the baseline.
The correct use of folklore numbers is as a hypothesis to test, not a target to hit.

## 6. Output convention for bilingual teams

In deliverables, give every metric:

```text
id            payer_conversion_dau
en            payer conversion (DAU-based)
zh            付费率（活跃口径）
aliases       付费转化率, 付费渗透率
formula       distinct payers in day / DAU in day
```

Record aliases explicitly so that a partner's 付费率 can be traced to your metric ID instead of silently
replacing it. See [metric-system-engineering.md](metric-system-engineering.md) for the governance workflow.
