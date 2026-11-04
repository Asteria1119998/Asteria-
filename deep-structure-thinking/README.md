# deep-structure-thinking

一个强制「先按深层结构思考，再给方案」的 AI 协作 Skill。

它不让模型直接回答，而是要求模型先完成结构分类、意图-规格差距分析、设计与字段图，再允许输出实现。目标是减少「一次成功就当能力」「意图和指令错位」「没看清失败点就写代码」这几类常见问题。

## 它强制做什么

使用后，模型必须按以下顺序输出（全部中文）：

1. **结构分类**（Sampling / Distribution / Optimization / Data / Specification）
2. **意图**
3. **规格**
4. **差距**
5. **设计**（涉及方案或代码时）
6. **字段图**（涉及方案或代码时）
7. **假设 / 检验 / 修正**
8. 最后才是实现或最终答案

## 安装方法

### Claude / Grok
1. 下载本仓库
2. 将 `deep-structure-thinking` 文件夹放到对应平台的 skills 目录
3. 重启或刷新后即可使用（模型会根据 description 自动触发）

### GPT / Workbuddy / 其他平台
- 将 `portable-core.md` 的内容粘贴到系统提示、Custom Instructions 或 Project Knowledge 中
- 如需更强约束，可同时提供 `scripts/validate_output.py`，让模型在输出后自检

## 文件说明

```
deep-structure-thinking/
├── SKILL.md                 # 主指令（Claude/Grok 使用）
├── portable-core.md         # 精简版，适合其他平台
├── scripts/
│   ├── validate_output.py   # 检查是否包含必需章节
│   └── fieldmap_template.py # 字段图模板
├── references/              # 分类标准与反模式
├── examples/                # 示例
└── evals/                   # 作者自用测试用例
```

## 设计原则

- 结构先于内容：先分类、先暴露差距、先画字段图
- 用代码锁住容易被跳过的步骤（`validate_output.py`）
- 输出强制中文，降低理解成本
- 可跨平台：完整版给 Claude/Grok，精简版给其他模型

## License

MIT
