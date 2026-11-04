---
name: deep-structure-thinking
description: Classify problems by deep structure (probability, distribution, optimization, sampling variance, data, specification) rather than surface form. Convert intent into executable specification while making the intent-instruction gap explicit. Apply hypothesis-test-correct reflex. Require Design + Field Map before any code or plan. Use when the user wants rigorous thinking, specification before execution, debugging analysis, or to avoid treating single good outputs as capability.
---

# Deep Structure Thinking（深层结构思维）

强制按底层结构分类问题，暴露 intent 与 instruction 之间的 gap，并在给出任何方案或代码前锁定 hypothesis-test-correct 反射。

## 何时使用

在以下请求中触发：
- 分析某事为何成功或失败
- 设计计划、agent、prompt 或系统
- 审查或编写代码/脚本
- 对问题进行分类
- 任何原本会直接跳到解决方案的请求

## 强制输出顺序（Mandatory Output Order）

在给出任何解决方案、代码或建议之前，必须按以下顺序产出这些章节。缺少任何章节即为失败。

**语言规则（强制）**：所有输出必须使用中文，包括章节标题和正文。不得使用英文标题。

推荐中文章节标题：
1. **结构分类**
2. **意图**
3. **规格**
4. **差距**
5. **设计**（如果涉及方案或代码）
6. **字段图**（如果涉及方案或代码）
7. **假设 / 检验 / 修正**
8. 只有在此之后：实现或最终答案（中文）

## 1. 结构分类

将问题分类为以下一种或多种：

| Type | 核心问题 | 典型失败模式 |
|------|----------|--------------|
| Sampling | 一次结果是否具有代表性？ | 把单次成功当作能力 |
| Distribution | 结果的范围是什么？ | 忽略尾部或方差 |
| Optimization | 正在最大化/最小化什么？ | 优化了错误的指标 |
| Data | 实际可用的数据 vs 假设的数据是什么？ | 隐藏的数据依赖 |
| Specification | intent 在哪里与 instruction 分叉？ | 模糊或不完整的约束 |
| Mixed | 组合 | — |

必须说明主要类型及原因。在此明确之前不得继续。

## 2–4. 意图 → 规格 → 差距

- **意图**：用户真正想要实现的结果（outcome，而非方法）。
- **规格**：机器可执行的约束、边界、成功标准和反例。
- **差距**：意图与规格之间的差异。必须具体指出差距可能导致失败的位置。

### 差距过大时的澄清协议（强制）

如果发现用户指令与可执行规格之间的差距过大（意图模糊、关键边界缺失、成功标准不明确、或多种合理解释并存），禁止直接输出方案或代码。必须先用多选题方式向用户澄清：

1. 首先提出 3 个多选问题（每个问题给出 2–4 个明确选项，外加「其他」）。
2. 如果用户回答后仍然过于模糊，再提出最多 3 个多选问题。
3. 总提问数不超过 6 个。达到 6 个后，必须基于已有信息给出当前最佳规格，并明确标注剩余不确定性。

提问时应优先覆盖：

- 真实想要的结果 vs 可接受的折中
- 明确不做什么 / 边界
- 成功如何判断

只有在差距被缩小到可执行程度后，才继续后续的设计、字段图和实现。

## 5–6. 设计 + 字段图（代码前必需）

**设计** 必须包含：
- 方案试图做什么
- 它明确**不**做什么
- 关键假设
- 成功标准

**字段图** 必须包含：
- 关键变量 / 状态
- 转换（Transitions）
- 可能的失败点
- Sampling 或 variance 相关顾虑

尽可能使用 `scripts/fieldmap_template.py` 中的模板。

## 7. 假设 / 检验 / 修正

对每一个非平凡的主张或设计选择：
- 假设
- 如何测试它（优先快速、高信号的测试）
- 如果测试失败，要改变什么

这个反射应在高反馈环境中练习，并带入低反馈环境。

## 代码与脚本规则

- 在 Design + Field Map 之前，绝不输出 implementation。
- 产出应包含强制章节的输出后，对其运行 `scripts/validate_output.py`。
- 如果校验失败，在交付给用户前重写。
- 审查 AI 生成的代码时，首先产出 Field Map，对比代码声称要做的与实际做的。

## 反模式（Anti-Patterns，禁止这些）

- 在 Structure Classification + Gap 之前跳到代码或方案
- 把一次好样本当作能力的证据
- 没有显式 Field Map 就写 implementation
- 隐藏 Intent–Specification gap
- 给出没有可测试 hypothesis 的建议

## 参考文件

- 深层结构分类法：`references/deep-structure-taxonomy.md`
- 反模式详情：`references/anti-patterns.md`
- 跨平台用法：`references/cross-platform.md`
- 检索场景专用规则：`references/retrieval.md`

## 检索场景额外要求

如果任务涉及检索、RAG、知识库查询、证据查找、召回或排序，在完成通用流程后，必须继续阅读并执行 `references/retrieval.md`。

此时必须额外显式输出：
- Grounded Data（实际检索到的原始数据，而非仅总结）
- 双向证据（支持方向 + 主动构造的否定/反驳方向）
- 证据对比
- 否定盲区自检

不得只沿单一方向检索后直接下结论。

## 脚本

- `scripts/validate_output.py` — 检查必需章节
- `scripts/fieldmap_template.py` — 输出标准 Field Map 骨架