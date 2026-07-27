# Build Game Analytics System

面向游戏产品的数据分析体系构建 Skill。它帮助团队从业务决策出发，为不同类型的游戏设计可执行、可复算、可持续迭代的数据分析系统，而不是堆叠一份通用指标清单。

适用于移动、PC、主机、网页、小游戏、MMO、RPG、SLG、卡牌、Gacha、休闲、竞技 PvP、买断制、订阅制、广告变现、混合变现、长线运营和 UGC 产品。

## 能力

- 设计北极星指标、KPI 树、驱动指标与体验护栏。
- 建立指标字典：业务问题、口径、公式、人群、时间窗口、维度、数据源、负责人和数据策略。
- 规划埋点与事件模型，覆盖客户端、服务端、订单、广告、匹配、社交、内容、经济和实验数据。
- 支持新增、激活、留存、流失、回流、收入、LTV、ROAS、渠道、版本、活动、内容、经济、社交、服务器、质量与公平性分析。
- 提供漏斗、队列、留存、实验、因果比较、预测、流失模型、经济流和网络分析等方法选择指南。
- 覆盖买量投放（计划/素材诊断、归因窗口、反作弊、边际 ROAS 与预算反推）与广告变现（IAA 漏斗、中介与底价、混合变现互相蚕食）。
- 提供中文口径消歧（消耗、流水、ROI、留存、活跃、回流等）与 AARRR/PRAPA/RFM/HEART/GSM 等框架的翻译对照。
- 提供 DAU 恒等式、留存曲线拟合、LTV 与回本推算，以及"目标是否可达"的可行性反推。
- 提供指标平台工程实践：原子/派生/复合指标组合、命名规范、指标血缘、口径版本化、告警阈值设计与服务时效分层。
- 提供可机器校验的指标规范模板。

## 快速开始

在 Claude Code 中，把目录复制到 `~/.claude/skills/build-game-analytics-system/`（Windows 为
`%USERPROFILE%\.claude\skills\`）后即可通过 `/build-game-analytics-system` 或自然语言触发。

在 Codex 中调用：

```text
请使用 $build-game-analytics-system，
为一款海外软启动的 5v5 MOBA 设计第一版数据指标体系。
重点关注新手留存、匹配公平、玩法活动参与和社交互动；
输出 KPI 树、指标字典、埋点矩阵与分析优先级。
```

提供的产品背景越完整，输出越贴近实际。建议至少说明：游戏类型、平台、地区、生命周期、商业模式、核心循环、当前业务问题、可用数据与约束。

## 默认交付物

完整方案通常包含：

1. 产品简报与假设清单。
2. 北极星体系与 KPI 树。
3. 指标字典与口径治理规则。
4. 事件/数据源矩阵与数据质量检查。
5. 看板规划、分析需求池与实验验证方案。
6. 风险、待确认项和分阶段实施建议。

对于轻量需求，也可只输出某一个模块，例如活动指标、MOBA 匹配健康、Gacha 抽卡分析或渠道 LTV 体系。

## 设计原则

- 从决策和玩家价值出发，而不是从指标名称出发。
- 使用“结果 → 驱动 → 诊断 → 护栏”的分层结构。
- 明确实体、分子分母、队列锚点、时间窗口、时区、金额口径和排除规则。
- 区分精确日留存、滚动留存和区间留存；区分 ROAS 与利润 ROI。
- 同时观察规模与比例，避免平均值掩盖分布、集中度或长尾风险。
- 将相关性、预测与因果结论明确区分；版本和活动的前后对比默认只用于诊断。
- 将质量、稳定性、公平、隐私和玩家信任作为持续护栏。

## 目录

```text
SKILL.md                                        核心工作流与操作规则
agents/openai.yaml                              Codex 界面元数据
references/
  product-intake-and-kpi-tree.md                产品简报采集与 KPI 树搭建
  product-archetypes.md                         产品原型与指标模块选择
  metric-library.md                             指标选择库与口径契约
  cn-terminology-and-pitfalls.md                中文口径消歧、中英对照与对账约定
  framework-crosswalk.md                        AARRR/PRAPA/RFM/HEART/GSM 等框架翻译
  ua-and-marketing-analytics.md                 买量投放、素材、归因、反作弊与预算
  hybrid-monetization-and-iaa.md                广告变现、IAA 漏斗与混合变现
  growth-accounting-and-forecasting.md          DAU 恒等式、曲线拟合、LTV 与回本推算
  metric-system-engineering.md                  指标平台工程、命名、血缘、告警与时效
  instrumentation-and-data-quality.md           埋点、实体模型、可靠性与数据质量
  telemetry-governance.md                       tracking plan 生命周期与治理
  multiplayer-social-analytics.md               匹配、组队、公会与网络干扰实验
  analysis-playbooks.md                         方法选择与各场景分析流程
  case-studies.md                               端到端案例（含两个反例）
  deliverable-templates.md                      交付物模板
  source-synthesis.md                           来源、章节映射、检索限制与被拒内容
examples/multiplayer-event-contract.json        可校验的多人事件契约示例
examples/hybrid-ua-metric-spec.json             买量 + 混合变现指标规范示例
scripts/validate_metric_spec.py                 JSON/YAML 指标规范校验器
```

## 校验指标规范

```powershell
python scripts/validate_metric_spec.py <metric-spec.json-or-yaml>
```

校验器会检查指标 ID、必填口径、事件引用、北极星引用、状态字段、比率分母、留存队列定义和金额口径等常见问题，
并对以下高频错误给出警告：把 `收入/消耗` 命名为 ROI（应为 ROAS）、LTV 缺少时间跨度或未标注实测/预测、
基准值缺少来源与可比条件、`aliases` 类型不正确。

## 新增能力

- 事件治理：将 tracking plan 作为版本化数据契约，覆盖事件状态、属性类型、基数、投递通道、质量 SLO、身份与删除流程。
- 多人竞技与社交：覆盖匹配服务、匹配公平、排队体验、新手不确定性、组队/公会旅程和网络干扰实验。
- 中文口径治理：识别"消耗/流水/收入/ROI/留存/活跃/回流"等一词多义，输出带 `id / en / zh / aliases / formula` 的双语定义。
- 买量与归因：三层投放数据模型、`CPI = eCPM / (1000 × CTR × CVR)`、计划与素材诊断树、归因窗口与 SKAN 限制、
  作弊特征（CTIT 异常、点击洪泛/注入、设备农场）、边际 ROAS 与回本天数。
- 广告与混合变现：`广告收入 = DAU × 看广告率 × 人均展示 × eCPM/1000`，完整 IAA 漏斗、中介瀑布与竞价、
  IAP/IAA 蚕食实验，以及小游戏平台的身份、归因与分成差异。
- 增长核算与预测：`DAU = 留存 + 回流 + 新增` 残差校验、留存面积与稳态 DAU、由目标 DAU 反推日均新增与预算、
  四类留存曲线拟合及其外推失效模式。
- 指标平台工程：原子/修饰词/派生/复合指标组合与命名、主/辅/诊断/预警分层、指标血缘（算术边 vs 假设边）、
  口径单一来源与状态流转、弹性基线告警、实时/近线/离线服务分层、需求受理到采纳追踪的运营闭环。
- 案例库：5 个端到端案例，含"活跃阈值来自参与度分布""回流活动率好但人群结构变差""用增长恒等式否掉 50 万 DAU 目标"
  以及两个把口径/日历差异误读为版本效果的反例。
- 示例文件：`examples/multiplayer-event-contract.json`、`examples/hybrid-ua-metric-spec.json`。

## License

[MIT](LICENSE)
