#!/usr/bin/env python3
"""
Validate that an AI output contains the mandatory deep-structure-thinking sections.
Accepts both Chinese and English titles, with or without numbering.
Usage: python validate_output.py output.md
Exit code 0 = pass, 1 = fail
"""

import sys
import re

# Flexible patterns: optional number, Chinese or English titles
REQUIRED_SECTIONS = [
    r"^##\s*(?:\d+\.\s*)?(?:Structure Classification|结构分类|深层结构分类)",
    r"^##\s*(?:\d+\.\s*)?(?:Intent|意图)",
    r"^##\s*(?:\d+\.\s*)?(?:Specification|规格|规范)",
    r"^##\s*(?:\d+\.\s*)?(?:Gap|差距|间隙)",
    r"^##\s*(?:\d+\.\s*)?(?:Hypothesis|假设)",
]

CONDITIONAL_SECTIONS = [
    (r"^##\s*(?:\d+\.\s*)?(?:Design|设计)", r"(```|def |class |function |implementation|plan:|方案)"),
    (r"^##\s*(?:\d+\.\s*)?(?:Field Map|字段图|域图|FieldMap)", r"(```|def |class |function |implementation|plan:|方案)"),
]

def validate(text: str) -> tuple[bool, list[str]]:
    errors = []
    for pattern in REQUIRED_SECTIONS:
        if not re.search(pattern, text, re.MULTILINE | re.IGNORECASE):
            errors.append(f"Missing required section matching: {pattern}")

    for section_pat, trigger_pat in CONDITIONAL_SECTIONS:
        if re.search(trigger_pat, text, re.IGNORECASE):
            if not re.search(section_pat, text, re.MULTILINE | re.IGNORECASE):
                errors.append(f"Code/plan detected but missing: {section_pat}")

    return len(errors) == 0, errors

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_output.py <file>")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    ok, errors = validate(text)
    if ok:
        print("PASS: All mandatory sections present.")
        sys.exit(0)
    else:
        print("FAIL:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
