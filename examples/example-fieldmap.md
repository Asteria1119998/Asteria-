# 示例 Field Map

## Field Map

### 关键变量 / 状态
- `user_intent`：原始目标
- `spec`：可执行约束
- `gap_list`：显式不匹配项
- `feedback_quality`：high / medium / low

### Transitions
- Intent → Specification（细微差别损失）
- Specification → Implementation（解释风险）
- 单次运行 → 能力宣称（sampling 错误）

### 可能的失败点
- Gap 被隐式化
- 在 Field Map 之前输出代码
- 忽略 variance

### 假设
- 模型在被指令 + 校验时会遵循章节顺序
- 当 Gap 错误时用户会纠正

### Sampling / Variance 顾虑
- 一次成功运行并不意味着稳定行为

### 此方案明确不处理的内容
- 完全自动的形式化验证
- 没有可观察反馈的领域
