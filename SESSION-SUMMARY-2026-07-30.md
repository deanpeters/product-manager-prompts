# Working Session Summary — July 30, 2026

Shipped v2.4, the decoupling release. This note is the handoff: what
changed, why it changed, the rule that now governs the library, and
what is open.

## The trigger

Dean hit it from the user's side: the TAM/SAM/SOM generator in
`prompt-generators/` and the analysis prompt in `market-intelligence/`
each described themselves in terms of the other, so choosing between
them meant reading both. His framing is the whole thesis of this
release:

> Loosely coupled is fine — a prompt can take advantage of other
> prompts. Tight coupling destroys how a novice-to-nascent user can
> use and learn from these. Tight coupling destroys the pedagogic.

## What shipped (see CHANGELOG.md for full detail)

**Two new assets:**

- `prompts/tam-sam-som-market-sizing.md` — the self-contained market
  sizing prompt that started the session. It is now the **reference
  implementation for a level 0 asset**: capability check, context
  detection with collapse rule, Generative Guidance v2 intake with
  both standing bypasses, its own research protocol and source
  hierarchy, bottom-up SAM build with the arithmetic shown, mandatory
  top-down reconciliation, ten-section output, anti-pattern refusal
  list, forward pointers confined to Final Step. Copy its shape when
  building new `prompts/` assets.
- `market-intelligence/full-spectrum-company-sweep-prompt.md` — all
  seven collection disciplines on one company in one run, fused, ending
  in a call-ready brief. Built because the intelligence system had a
  workflow-level gap: `all-source-fusion` explicitly "fuses; it does
  not collect," and `fusion-cadence-routine` requires manual baselines,
  so a PM with a call in two hours faced eight prompts in the right
  order. Eight places to quit before the system pays off.

**The decoupling work, four phases:**

- **Phase C (done first, deliberately)** — `validate-prompts.py`
  gained `coupling_checks()`. Doing enforcement before cleanup turned
  the rest into a shrinking punch list instead of a survey to hold in
  your head, and defined the `Standalone:` field before 31 files were
  edited (avoiding a second pass over all of them).
- **Phase A** — all 30 `Companion:` blocks removed; Descriptions and
  Usage Notes rewritten so each file stands alone.
- **Phase B** — every `prompts/` asset made and declared standalone.
- **Phase D** — the rule written into `AGENTS.md` and `CLAUDE.md`,
  then enforcement promoted to default.

## The rule now in force

**Forward pointers are free. Backward prerequisites are debt.**

Every asset must be describable, and runnable, without naming another
file above its Final Step block.

| Level | Shape | Allowed in |
|---|---|---|
| 0 Standalone | Finishes the job alone; asks for what it needs | **Required** in `prompts/` |
| 1 Forward pointer | Names a next step, Final Step only | Anywhere |
| 2 Soft prereq | Better with a prior artifact, works without, says so | `prompt-generators/`, `workshops/`, `market-intelligence/`, `storytelling/` |
| 3 Hard gate | `STOP` unless a prior artifact exists | `loops/`, `vibes/` only |

`prompts/` is the novice floor: one file in, one finished artifact
out. `loops/` and `vibes/` may gate hard because a loop is machinery
adopted after the manual version is understood, and a batch job on an
empty index produces garbage at scale.

**Duplication across tiers is intentional and encouraged.** A
generator teaches the scoping decisions, a workshop teaches the
facilitated conversation, a `prompts/` template delivers the artifact,
a loop teaches the automation. TAM/SAM/SOM exists four times on
purpose. **Zero assets were deleted or merged this session.** Anyone —
human or agent — who arrives wanting to "reduce duplication" should
read the Coupling Discipline section of `AGENTS.md` first.

## Three findings worth carrying forward

1. **The coupling was largely fictional.** Fourteen files in
   `prompts/` carried the boilerplate "Assumes context is already
   present in session" while their bodies held working three-question
   fallbacks. No file in `prompts/` actually stalled cold.
   `earnings-executive-signal-refresh` told you to run another prompt
   first while carrying its own baseline mode. Documentation invented
   dependencies that did not exist — worse than a real one, because
   the novice quits at a gate that is not there. **When auditing,
   check the body before believing the header.**
2. **The coupling was policy.** `AGENTS.md` said to "convert the other
   to a pointer." Fixing the files without fixing that line would have
   let the pattern regrow within a release.
3. **The loops' `STOP` gates are internal state guards** — an empty
   index the loop builds itself — not sibling dependencies. They were
   correct engineering all along and are `Standalone: yes`.

## Tooling

```
python3 scripts/validate-prompts.py     # coupling enforced by default
python3 scripts/validate-prompts.py --lenient   # warnings, for bulk migration
python3 scripts/generate-catalog.py
```

Current state: **110 assets, 0 errors, 54 warnings.**

Regression coverage verified by hand: a `Companion:` line in a
metadata block and a file reference above a Final Step heading both
fail the build.

## What's open

- **54 warnings, all grandfathered metadata gaps** unrelated to
  coupling — missing `Description` / `Attribution` / `Date` on older
  files, concentrated in `storytelling/` and
  `resumes-resignations-reactions/`. 11 assets still have no metadata
  block at all (`generate-catalog.py` lists them on every run). Clean,
  self-contained next job.
- **`Standalone:` is only enforced in `prompts/`.** Other tiers may
  declare it and 30 assets do, but it is not required there yet.
  Promoting it repo-wide is a one-line validator change plus a
  backfill pass.
- **`catalog/` is regenerated and current** as of this commit, and both
  new assets are indexed in their directory READMEs.
- A stale worktree copy lives at
  `.claude/worktrees/project-understanding-839dde/` — excluded from
  validation, but it will show up in raw `grep -r` sweeps and
  contains pre-decoupling versions of these files. Do not read it as
  current state.

## Reference documents

- `COUPLING-REMEDIATION-PLAN.md` — the plan, measured baseline, and
  outcome table. Read this before touching coupling.
- `AGENTS.md` — Coupling Discipline section is the authoring contract.
- `CLAUDE.md` — fast-path summary of the same rule.
