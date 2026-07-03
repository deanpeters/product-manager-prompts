#!/usr/bin/env python3
"""Validate prompt assets against the repo's structural standards.

Checks, per prompt file:
  1. Required metadata fields in the comment block:
     Description, Usage Note, Instructions, Attribution, Licensing, Date
  2. Generative Guidance v2 fixtures, for files that declare the
     v2 pattern: best-guess bypass, bulk-drop bypass, "Other" option,
     context-detection collapse rule
  3. Companion: references resolve to real files
  4. No emojis in prompt body (repo output rule)

Grandfathered files (predating the metadata standard) produce
warnings; files declaring v2 produce errors on missing fixtures.
Exit code 1 on errors, 0 on warnings only.

Run from the repo root:  python3 scripts/validate-prompts.py
Stdlib only; no dependencies.
"""

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DIRECTORIES = [
    "prompts",
    "prompt-generators",
    "market-intelligence",
    "workshops",
    "loops",
    "storytelling",
    "skeletons",
    "vibes",
    "resumes-resignations-reactions",
]
SKIP_NAMES = {"README.md"}
REQUIRED_FIELDS = [
    "Description",
    "Usage Note",
    "Instructions",
    "Attribution",
    "Licensing",
]
V2_MARKERS = [
    "Generative Guidance pattern v2",
    "Generative Guidance (v2)",
    "Generative Guidance v2",
]
V2_FIXTURES = {
    "best-guess bypass": r"take your best guess",
    "bulk-drop bypass": r"bulk drop|drop in|drop your notes|paste",
    "'Other' option": r"\bOther\b",
    "context collapse rule": r"reduce or skip|sufficient context|enough context",
}
EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F900-\U0001F9FF]"
)


def comment_block(text):
    m = re.search(r"<!--(.*?)-->", text, re.DOTALL)
    return m.group(1) if m else ""


def check_file(path):
    errors, warnings = [], []
    text = path.read_text(encoding="utf-8", errors="replace")
    block = comment_block(text)

    if not block:
        warnings.append("no metadata comment block (grandfathered?)")
    else:
        for field in REQUIRED_FIELDS:
            if not re.search(rf"^##\s*{re.escape(field)}\s*:", block, re.MULTILINE):
                warnings.append(f"metadata missing field: {field}")
        if not re.search(r"^Date:\s*\S", block, re.MULTILINE) and not re.search(
            r"^##\s*Date\s*:", block, re.MULTILINE
        ):
            warnings.append("metadata missing field: Date")

    if any(marker in text for marker in V2_MARKERS):
        for name, pattern in V2_FIXTURES.items():
            if not re.search(pattern, text, re.IGNORECASE):
                errors.append(f"declares v2 but missing fixture: {name}")

    for m in re.finditer(r"Companion:\s*(\S+\.md)", text):
        target = m.group(1).strip(".,)")
        if not (REPO / target).exists():
            errors.append(f"Companion reference does not resolve: {target}")

    body = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    if EMOJI.search(body):
        warnings.append("emoji found in prompt body (output rules say ASCII)")

    return errors, warnings


def main():
    total_errors = total_warnings = checked = 0
    for d in DIRECTORIES:
        base = REPO / d
        if not base.is_dir():
            continue
        for f in sorted(base.glob("*.md")):
            if f.name in SKIP_NAMES or f.name.startswith("Dataset"):
                continue
            checked += 1
            errors, warnings = check_file(f)
            rel = f.relative_to(REPO)
            for e in errors:
                print(f"ERROR   {rel}: {e}")
            for w in warnings:
                print(f"warning {rel}: {w}")
            total_errors += len(errors)
            total_warnings += len(warnings)
    print(
        f"\nChecked {checked} files: "
        f"{total_errors} errors, {total_warnings} warnings"
    )
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
