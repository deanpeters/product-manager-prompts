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

Plus, per skills/<name>/ folder:
  5. SKILL.md exists; YAML frontmatter present with a `name` matching
     the folder and a `description` substantial enough to route on
  6. Supporting files named in SKILL.md resolve
  7. The same asset contract as any other prompt (metadata block,
     Standalone: yes, coupling, emoji)

Coupling discipline is enforced by default (see AGENTS.md); pass
--lenient to downgrade those findings to warnings during bulk
migration. Grandfathered files (predating the metadata standard) produce
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
# README.md indexes a directory; howto.md teaches prompt-writing. Both
# are documentation that happens to live beside the assets, so the
# asset contract (metadata block, Standalone declaration) does not
# apply to them.
SKIP_NAMES = {"README.md", "howto.md"}
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

# --- Coupling discipline (see COUPLING-REMEDIATION-PLAN.md) -------------
#
# Forward pointers are free; backward prerequisites are debt. An asset
# must be describable and runnable without naming another file above its
# Final Step block. Duplication across tiers is intentional -- the same
# framework taught three ways serves three learners -- so none of this
# penalizes having a generator, a workshop, and a standalone for one
# topic. It penalizes making the user read two files to use one.
#
# Levels: 0 standalone / 1 forward pointer / 2 soft prereq / 3 hard gate.
# prompts/ is the novice floor and must be level 0: one file in, one
# finished artifact out.

# prompts/ is the novice floor; skills/ is the agent floor. An agent
# invokes a skill cold, with no guarantee a sibling skill was loaded
# first, so both tiers must finish the job alone.
STANDALONE_TIERS = {"prompts", "skills"}    # must declare Standalone: yes
AUTOMATION_TIERS = {"loops", "vibes"}       # may hard-gate (level 3)

ASSET_REF = re.compile(
    r"(?:prompts|prompt-generators|market-intelligence|workshops"
    r"|storytelling|loops|skeletons|vibes|flows"
    r"|resumes-resignations-reactions)/[A-Za-z0-9._-]+\.md"
    r"|skills/[A-Za-z0-9._-]+/[A-Za-z0-9._-]+\.md"
)
FINAL_STEP = re.compile(r"^#{1,4}\s*Final Step:?\s*$", re.MULTILINE | re.IGNORECASE)
HARD_GATE = re.compile(r"^\s*STOP:|do not proceed until|cannot proceed until",
                       re.MULTILINE | re.IGNORECASE)
BACKWARD_PREREQ = [
    (r"\brun [^.\n]{0,40}\bfirst\b", "backward prereq: 'run ... first'"),
    (r"\buse [^.\n]{0,40}\binstead\b", "backward prereq: 'use ... instead'"),
    (r"\bassumes [^.\n]{0,40}\b(exists|already|in session)\b",
     "backward prereq: 'assumes ... already'"),
    (r"^Companion:", "Companion block (fold into Final Step)"),
]
STANDALONE_FIELD = re.compile(r"^##\s*Standalone\s*:\s*(.+)$",
                              re.MULTILINE | re.IGNORECASE)


def comment_block(text):
    m = re.search(r"<!--(.*?)-->", text, re.DOTALL)
    return m.group(1) if m else ""


def above_final_step(body):
    """The part of the body a user reads before they have an artifact."""
    m = FINAL_STEP.search(body)
    return body[: m.start()] if m else body


def coupling_checks(path, text, block, body, strict):
    """Level enforcement. Staged findings are warnings until Phases A/B
    land, then --strict (and eventually the default) promotes them."""
    errors, warnings = [], []
    tier = path.parts[0] if len(path.parts) > 1 else ""
    staged = errors if strict else warnings

    # Level 0/1: no file paths above Final Step in the standalone tiers.
    if tier in STANDALONE_TIERS:
        for ref in sorted(set(ASSET_REF.findall(above_final_step(body)))):
            errors.append(
                f"names {ref} above Final Step ({tier}/ must stand alone)"
            )

    # Level 3 is automation-only.
    if tier and tier not in AUTOMATION_TIERS:
        for m in HARD_GATE.finditer(body):
            line = body[: m.start()].count("\n") + 1
            staged.append(
                f"hard gate outside {'/'.join(sorted(AUTOMATION_TIERS))} "
                f"near body line {line}: {m.group(0).strip()!r}"
            )

    # Backward-prereq phrasing in the metadata a novice reads to choose.
    if tier in STANDALONE_TIERS and block:
        for pattern, label in BACKWARD_PREREQ:
            if re.search(pattern, block, re.MULTILINE | re.IGNORECASE):
                staged.append(f"metadata {label}")

    # The declared contract.
    m = STANDALONE_FIELD.search(block) if block else None
    value = m.group(1).strip().lower() if m else None
    if tier in STANDALONE_TIERS:
        if value is None:
            staged.append("metadata missing field: Standalone (must be 'yes')")
        elif not value.startswith("yes"):
            staged.append(f"Standalone: {value!r} -- {tier}/ must be 'yes'")
    elif value and value.startswith("requires") and tier not in AUTOMATION_TIERS:
        staged.append(
            f"Standalone: 'requires ...' (level 3) only allowed in "
            f"{'/'.join(sorted(AUTOMATION_TIERS))}"
        )

    return errors, warnings


def check_file(path, strict=False):
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

    rel = path.relative_to(REPO)
    c_errors, c_warnings = coupling_checks(rel, text, block, body, strict)
    errors += c_errors
    warnings += c_warnings

    return errors, warnings


# --- Agent Skills (skills/) --------------------------------------------
#
# A skill is a prompt packaged so an agent decides for itself that it
# applies. That decision is made from the YAML frontmatter alone, which
# makes the frontmatter a functional interface rather than decoration --
# so it gets checked like one. The comment block underneath still has to
# be there for the human reading the raw file; the two serve different
# readers and neither substitutes for the other.

SKILLS_DIR = "skills"
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
KEBAB_CASE = re.compile(r"\A[a-z0-9]+(-[a-z0-9]+)*\Z")
# Supporting files a SKILL.md points at, resolved relative to its folder.
SUPPORT_REF = re.compile(r"`((?:examples/)?[A-Za-z0-9._-]+\.md)`")
MIN_DESCRIPTION = 40  # too terse to route on

# Constraints from the Agent Skills spec (agentskills.io). These are not
# house style: exceeding them fails a claude.ai upload or a Skills API
# package outright, so they are errors here rather than warnings.
MAX_NAME = 64
MAX_DESCRIPTION = 1024
RESERVED_NAME_WORDS = ("anthropic", "claude")
SPEC_FRONTMATTER_KEYS = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}


def frontmatter_field(fm, field):
    m = re.search(rf"^{field}\s*:\s*(.+)$", fm, re.MULTILINE)
    return m.group(1).strip().strip("\"'") if m else None


def check_skill(folder, strict=False):
    """Validate one skills/<name>/ folder."""
    errors, warnings = [], []
    name = folder.name

    if not KEBAB_CASE.match(name):
        errors.append(
            f"folder name {name!r} is not kebab-case; the Agent Skills spec "
            "allows lowercase letters, numbers, and hyphens only"
        )
    if len(name) > MAX_NAME:
        errors.append(f"folder name is {len(name)} chars; spec maximum is {MAX_NAME}")
    for reserved in RESERVED_NAME_WORDS:
        if reserved in name:
            errors.append(f"folder name contains reserved word {reserved!r}")

    skill_md = folder / "SKILL.md"
    if not skill_md.is_file():
        errors.append("no SKILL.md in skill folder")
        return errors, warnings

    text = skill_md.read_text(encoding="utf-8", errors="replace")

    m = FRONTMATTER.match(text)
    if not m:
        errors.append("SKILL.md has no YAML frontmatter (agents route on it)")
    else:
        fm = m.group(1)
        declared = frontmatter_field(fm, "name")
        if not declared:
            errors.append("frontmatter missing field: name")
        elif declared != name:
            errors.append(
                f"frontmatter name {declared!r} does not match "
                f"folder {name!r}"
            )
        description = frontmatter_field(fm, "description")
        if not description:
            errors.append("frontmatter missing field: description")
        elif len(description) > MAX_DESCRIPTION:
            errors.append(
                f"frontmatter description is {len(description)} chars; "
                f"spec maximum is {MAX_DESCRIPTION}"
            )
        elif len(description) < MIN_DESCRIPTION:
            warnings.append(
                "frontmatter description is too terse for an agent to "
                f"route on ({len(description)} chars; say what it does "
                "and when to invoke it)"
            )

        # Only six keys are portable. claude.ai uploads, the Skills API,
        # and package_skill.py reject anything else with a hard error, so
        # a stray top-level key breaks distribution silently until then.
        # Our curation fields belong nested under `metadata:`.
        for key in re.findall(r"^([A-Za-z][\w-]*)\s*:", fm, re.MULTILINE):
            if key not in SPEC_FRONTMATTER_KEYS:
                errors.append(
                    f"frontmatter key {key!r} is not in the Agent Skills "
                    f"spec; allowed: {', '.join(sorted(SPEC_FRONTMATTER_KEYS))}"
                    " (nest curation fields under 'metadata')"
                )

    # Supporting files named in SKILL.md must actually exist.
    for ref in sorted(set(SUPPORT_REF.findall(text))):
        if ref == "SKILL.md":
            continue
        if not (folder / ref).exists():
            errors.append(f"names supporting file that does not exist: {ref}")

    # The rest of the asset contract: metadata block, coupling, emoji.
    file_errors, file_warnings = check_file(skill_md, strict)
    return errors + file_errors, warnings + file_warnings


# Licensing is repo-wide or it is nothing: sweep EVERY .md in the repo,
# not just the asset directories, so new directories (skills/, future
# additions) cannot slip an old license through.
LICENSE_EXEMPT = {
    "CHANGELOG.md",       # historical record of the MIT era
    "LICENSING.md",       # explains the MIT history intentionally
    "README.md",          # carries the pre-v2.3.0 MIT history note
    "AGENTS.md",          # states the "never reintroduce MIT" rule
}
LICENSE_EXEMPT_PREFIXES = ("SESSION-SUMMARY-",)  # historical records
SKIP_DIRS = {".git", ".claude", "node_modules"}
MIT_PATTERN = re.compile(r"\bMIT\b(?!RE)")  # matches MIT, not MITRE
CANONICAL_LICENSE = "CC BY-NC-SA 4.0"


def licensing_sweep():
    errors = []
    scanned = 0
    for f in sorted(REPO.rglob("*.md")):
        if any(part in SKIP_DIRS for part in f.parts):
            continue
        rel = f.relative_to(REPO)
        if f.name in LICENSE_EXEMPT and len(rel.parts) == 1:
            continue
        if f.name.startswith(LICENSE_EXEMPT_PREFIXES):
            continue
        scanned += 1
        text = f.read_text(encoding="utf-8", errors="replace")
        if MIT_PATTERN.search(text):
            errors.append(f"{rel}: references the MIT license "
                          f"(repo is {CANONICAL_LICENSE})")
        if re.search(r"##\s*Licensing|\*\*Licens", text) \
                and CANONICAL_LICENSE not in text:
            errors.append(f"{rel}: Licensing field present but not "
                          f"{CANONICAL_LICENSE}")
    return scanned, errors


def main():
    # Coupling enforcement is on by default as of Phase D: the repo is
    # clean, the rule is documented in AGENTS.md, and regressions
    # should fail rather than accumulate. --lenient downgrades the
    # staged findings to warnings for bulk migration work.
    strict = "--lenient" not in sys.argv
    total_errors = total_warnings = checked = 0
    for d in DIRECTORIES:
        base = REPO / d
        if not base.is_dir():
            continue
        for f in sorted(base.glob("*.md")):
            if f.name in SKIP_NAMES or f.name.startswith("Dataset"):
                continue
            checked += 1
            errors, warnings = check_file(f, strict)
            rel = f.relative_to(REPO)
            for e in errors:
                print(f"ERROR   {rel}: {e}")
            for w in warnings:
                print(f"warning {rel}: {w}")
            total_errors += len(errors)
            total_warnings += len(warnings)
    skills_base = REPO / SKILLS_DIR
    skills_checked = 0
    if skills_base.is_dir():
        for folder in sorted(p for p in skills_base.iterdir() if p.is_dir()):
            skills_checked += 1
            errors, warnings = check_skill(folder, strict)
            rel = folder.relative_to(REPO)
            for e in errors:
                print(f"ERROR   {rel}: {e}")
            for w in warnings:
                print(f"warning {rel}: {w}")
            total_errors += len(errors)
            total_warnings += len(warnings)

    lic_scanned, lic_errors = licensing_sweep()
    for e in lic_errors:
        print(f"ERROR   {e}")
    total_errors += len(lic_errors)
    print(
        f"\nChecked {checked} files and {skills_checked} skills: "
        f"{total_errors} errors, {total_warnings} warnings"
    )
    print(
        f"Licensing sweep: {lic_scanned} files scanned repo-wide, "
        f"{len(lic_errors)} violations"
    )
    if not strict:
        print(
            "Coupling: running --lenient, so coupling findings report "
            "as warnings instead of errors."
        )
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
