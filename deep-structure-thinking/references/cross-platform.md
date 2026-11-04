# Cross-Platform Usage

## Claude / Grok
Place the entire `deep-structure-thinking/` folder in the skills directory.
The model will load SKILL.md when the description matches.
Instruct it to run `scripts/validate_output.py` on its own draft when appropriate.

## GPT (ChatGPT, GPTs, Projects)
- Paste the contents of `portable-core.md` into Custom Instructions or Project knowledge.
- Optionally upload `scripts/validate_output.py` and tell the model to use Code Interpreter to self-check.
- For highest obedience, create a GPT whose instructions begin with the portable core.

## Other platforms (Workbuddy, etc.)
Use `portable-core.md` as a system prompt or persistent instruction block.
The validation script can be run manually by the user on the model's output.

## Shared Principle
The portable core is intentionally strict and short so it survives context limits and different system-prompt styles.
