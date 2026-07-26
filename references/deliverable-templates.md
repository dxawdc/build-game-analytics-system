# Deliverable templates

## 目录

1. 产品简报
2. KPI 树
3. 指标字典
4. 埋点矩阵
5. 看板规划
6. 分析需求池
7. 实验/验证计划
8. 机器可读规范
9. 最终交付检查

## 1. 产品简报

```markdown
- 产品/版本：
- 类型与平台：
- 地区与生命周期：
- 商业模式：
- 核心循环：
- 玩家价值：
- 身份单位：
- 时区/游戏日：
- 币种/收入口径：
- 当前最重要的 3-5 个决策：
- 可用数据源：
- 假设与待确认项：
```

## 2. KPI 树

```markdown
### 顶层目标
- 玩家价值目标：
- 商业目标：

### 北极星体系
- 主指标：
- 规模/频次：
- 体验护栏：
- 商业护栏：

### 驱动树
目标
├─ 驱动 A
│  ├─ 诊断指标 A1
│  └─ 诊断指标 A2
├─ 驱动 B
└─ 护栏指标
```

在每条因果箭头旁标记“定义恒等式”“业务假设”或“已验证关系”。

## 3. 指标字典

| 字段 | 内容 |
|---|---|
| metric_id | 稳定英文 ID |
| 名称 | 中英文名与缩写 |
| 层级/领域 | outcome/driver/diagnostic/guardrail + domain |
| 业务问题 | 该指标支持什么决策 |
| 定义 | 自包含的自然语言定义 |
| 公式 | 分子、分母及聚合 |
| 人群/排除 | eligible population |
| 实体/粒度 | account/player/character/session/match/order 等 |
| 时间 | cohort anchor、window、时区、游戏日 |
| 维度 | platform/region/version/channel/content 等 |
| 数据源 | 事件/表与权威来源 |
| 数据策略 | 去重、迟到、回补、零分母 |
| 金额口径 | 币种、FX、gross/net、退款等 |
| 负责人/时效 | owner、freshness、SLA |
| 方向/目标 | 趋势、目标来源、护栏 |
| 状态 | draft/proposed/approved/deprecated |

## 4. 埋点矩阵

| 业务阶段 | 事件 | 触发时点 | 权威端 | 必填属性 | 关联 ID | 支持指标 | QA 场景 |
|---|---|---|---|---|---|---|---|

金额、道具、进度、比赛结算优先由服务端或订单系统记录。

## 5. 看板规划

| 看板 | 受众 | 决策频率 | 顶层指标 | 诊断路径 | 告警/刷新 |
|---|---|---|---|---|---|
| 经营总览 | 负责人 | 日/周 | 北极星、收入、留存、质量 | 玩家构成 -> 产品 -> 渠道 | 日 |
| 新用户 | 产品/增长 | 日 | 首价值、D1/D7 | 渠道 -> 版本 -> 新手步骤 | 小时/日 |
| 内容与活动 | 运营/策划 | 活动周期 | 曝光、参与、增量价值 | 内容节点 -> 分群 | 小时 |
| 技术质量 | 研发/运维 | 实时 | crash-free、延迟、错误 | 版本 -> 平台 -> 设备/服务器 | 实时 |

每张图回答一个问题。默认显示绝对量、比例、同比/环比或基线、定义入口和数据更新时间。

## 6. 分析需求池

| 优先级 | 决策 | 假设 | 方法 | 所需数据 | 成功标准 | 负责人 |
|---|---|---|---|---|---|---|

先做能触发明确行动的分析。

## 7. 实验/验证计划

```markdown
- 假设：
- 实验单位与随机化：
- eligible/exposed：
- 主指标：
- 护栏指标：
- 最小可检测效应与样本期：
- 数据质量与 SRM 检查：
- 网络/跨组干扰：
- 停止规则：
- 分析窗口：
- 决策规则：
```

若不能随机化，写明对照选择、共同趋势或其他识别假设、安慰剂检查和剩余偏差。

## 8. 机器可读规范

以下 JSON 可交给 `scripts/validate_metric_spec.py`：

```json
{
  "product": {
    "name": "示例游戏",
    "archetype": "competitive-pvp",
    "lifecycle_stage": "soft-launch",
    "timezone": "Asia/Shanghai",
    "currency": "CNY",
    "identity_unit": "account",
    "north_star": ["weekly_quality_match_players"]
  },
  "events": [
    {
      "name": "match_ended",
      "owner": "game-server",
      "authoritative_source": "server"
    }
  ],
  "metrics": [
    {
      "id": "weekly_quality_match_players",
      "name": "周高质量对局玩家数",
      "domain": "engagement",
      "question": "多少玩家在一周内真正获得了有质量的竞技体验？",
      "definition": "自然周内至少完成 3 场有效对局，且无中途退出、严重延迟或确认作弊的去重账号数。",
      "formula": "count_distinct(eligible account_id)",
      "entity": "account",
      "grain": "calendar_week",
      "window": "calendar week in product timezone",
      "dimensions": ["platform", "region", "rank_band", "app_version"],
      "filters": ["exclude QA, bots, banned and invalid matches"],
      "source_events": ["match_ended"],
      "owner": "product-analytics",
      "freshness": "daily by 10:00",
      "status": "proposed",
      "direction": "increase with matchmaking guardrails"
    }
  ]
}
```

## 9. 最终交付检查

- 指标是否与决策一一对应？
- 口径能否由另一名分析师无歧义复算？
- 分子、分母、实体、时间、币种是否一致？
- 是否区分留存类型、收入类型、ROAS/ROI？
- 是否同时呈现规模与比率？
- 是否能从指标追到事件？
- 是否定义质量、公平和隐私护栏？
- 是否区分事实、相关、预测和因果？
- 是否给出 MVP 与后续阶段？
- 是否记录未知项、风险和验证方式？
