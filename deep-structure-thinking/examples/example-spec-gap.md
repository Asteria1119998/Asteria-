# 示例：Intent / Specification / Gap

## Intent
用户希望一个 agent 可靠地拒绝幻觉事实性主张。

## Specification
- 每个事实性主张必须附带来源或显式的 "unverified" 标签。
- 如果在允许的工具内找不到来源，agent 必须说它不知道。
- 除非附带来源，否则不得用自信语言呈现任何主张。

## Gap
Intent 是“永不幻觉”。Specification 只能强制“必须标记或拒绝”。  
Gap 在于模型仍可能生成看似合理的主张，然后未能标记它。  
缓解需要外部检查或二次验证器，而不仅仅是指令。
