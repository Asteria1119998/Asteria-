# 反模式（Anti-Patterns）

| 反模式 | 为何失败 | 必需修正 |
|--------|----------|----------|
| 单样本能力宣称 | 忽略 variance | 显式处理 sampling |
| Gap 之前就给方案 | 隐藏 intent-instruction 不匹配 | 强制先 Intent → Spec → Gap |
| 没有 Field Map 就写代码 | 读者无法看到失败点 | Design + Field Map 强制 |
| 无法测试的建议 | 无法被修正 | 附上 Hypothesis / Test |
| 表面分类 | 错过根结构 | 使用分类法 |
| 乐观计划 | 假设完美反馈 | 说明反馈质量与修正路径 |
