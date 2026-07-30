# Coupling Remediation Plan

Working plan, drafted July 30, 2026. Pick this up cold; it is written
to be executable without re-deriving the analysis.

---

## The problem, stated correctly

A prompt in this library is **tightly coupled** when a user cannot get
a finished artifact out of it without first going and reading or
running another file.

That wrecks the pedagogy specifically for the novice-to-nascent user,
who is the person this library exists for. An expert who hits a
cross-reference shrugs and follows it. A novice hits it at the exact
moment they have the least ability to evaluate the fork: they don't
have the artifact yet, they don't know the vocabulary yet, and now
they are comparison-shopping between two files instead of learning the
framework. Every prerequisite is a place to quit.

**Redundancy is not the problem. Dependency is.**

Three different TAM/SAM/SOM assets is correct and good. The generator
teaches *scoping* — how a PM decides what to size. The
market-intelligence version teaches *evidence discipline* — how
different intel approaches feed a number. The standalone teaches the
*whole arc* — intake through arithmetic through sensitivity. Three
teaching surfaces, three learners, three moments in a career. Do not
merge them.

The failure was never that there were two files. It was that:

1. Each file described itself **in terms of the other one**, so
   choosing required reading both, and
2. The generator **did not finish the job** — it emitted a prompt
   that sizes a market rather than sizing a market.

Fix those two things everywhere and the duplication becomes an asset.

---

## The governing rule

**Forward pointers are free. Backward prerequisites are debt.**

- **Forward** — "when you're done, this could feed a battle card."
  Appears only in the Final Step block. Always optional. The user
  already has their artifact, so the pointer costs them nothing and
  teaches them the shape of the library. Keep these. Add more.
- **Backward** — "run X first," "this is the sibling of Y, use Y if
  Z," "assumes a baseline exists." This is homework assigned before
  the user has anything. This is the debt.

Corollary, and the actual acceptance test for the whole plan:

> Every asset must be describable, and runnable, **without naming
> another file above its Final Step block.**

A file may be *better* with a prior artifact. It may not be *blocked*
by one, outside the automation tier.

---

## Coupling levels and which tier may use them

| Level | Shape | Allowed in |
|---|---|---|
| **0 — Standalone** | Finishes the job alone; asks for what it needs; no file named above Final Step | **Required** in `prompts/` |
| **1 — Forward pointer** | Names a next step, Final Step only, optional | Anywhere |
| **2 — Soft prereq** | Better with a prior artifact, works without it, says so in one line and proceeds on labeled defaults | `prompt-generators/`, `workshops/`, `market-intelligence/`, `storytelling/` |
| **3 — Hard gate** | `STOP` unless a prior artifact exists | `loops/`, `vibes/` **only** |

Why `loops/` and `vibes/` are exempt: a loop is machinery someone
adopts *after* they understand the manual version. `STOP: no baseline
snapshot` there is correct engineering — the alternative is a batch
job that silently produces garbage across fifty rows. The 11 existing
hard gates are almost all in `loops/` and almost all correct. Leave
them.

Why `prompts/` is the floor: it is where a novice lands. One file in,
one finished artifact out, every single time.

---

## Measured baseline (as of this writing)

| Signal | Count |
|---|---|
| Files with a prompt path in the **runtime body** | 4 |
| Files with `Companion:` in **metadata** | 31 |
| Topics living in 2+ asset directories | 13 |
| Hard `STOP` gates | 11 (10 in `loops/`/`vibes/`, 1 in `prompts/`) |
| Files in `prompts/` | 34 |

Body-level references are already low, and three of the four are
forward pointers in a Final Step. The damage is concentrated in
metadata, where the choosing happens.

The four body references, for reference:

- `market-intelligence/ansoff-matrix-prompt.md` -> tam-sam-som
- `market-intelligence/humint-collection-prompt.md` -> win-loss
- `workshops/lean-ux-canvas-workshop.md` -> lean-ux template
- `workshops/product-sunset-workshop.md` -> eol message (Final Step,
  fine as-is)

---

## Phase A: Decouple the decision layer

**Goal:** every file describes what *it* does in absolute terms. No
file's identity depends on another file's existence.

**Scope:** the 31 files carrying `Companion:` blocks, concentrated in
these 13 topic pairs. **Keep every one of these files.** This phase
rewrites descriptions, it does not delete assets.

| Topic | Files (all retained) |
|---|---|
| TAM/SAM/SOM | `prompt-generators/tam-sam-som-prompt-generator.md`, `market-intelligence/tam-sam-som-analysis-prompt.md`, `prompts/tam-sam-som-market-sizing.md` |
| Positioning statement | `prompts/positioning-statement.md`, `prompt-generators/positioning-statement-prompt-generator.md` |
| Premortem | `prompts/premortem-prompt-template.md`, `prompt-generators/premortem-prompt-generator.md` |
| Stakeholder map | `prompts/stakeholder-map-prompt-template.md`, `prompt-generators/stakeholder-map-prompt-generator.md` |
| Proto-persona | `prompts/proto-persona-profile.md`, `prompt-generators/proto-persona-prompt-generator.md` |
| Customer journey | `prompts/customer-journey-mapping-prompt-template.md`, `prompt-generators/customer-journey-mapping-prompt-generator.md`, `storytelling/Generator - Customer Journey Map Simulator.md` |
| Discovery interview | `prompts/discovery-interview-guide-prompt-template.md`, `prompt-generators/discovery-interview-prompt-generator.md` |
| User story | `prompts/user-story-prompt-template.md`, `prompt-generators/user-story-prompt-generator-prompt.md` |
| Lean UX canvas | `prompts/lean-ux-canvas-prompt-template.md`, `workshops/lean-ux-canvas-workshop.md` |
| PRD | `prompts/prd-prompt-template.md`, `workshops/prd-workshop.md` |
| Battle card | `market-intelligence/battle-card-builder-prompt.md`, `workshops/battle-card-workshop.md` |
| SWOT | `market-intelligence/swot-analysis-prompt.md`, `loops/swot-batch.md` |
| JTBD | `prompts/jobs-to-be-done.md`, `prompt-generators/jobs-to-be-done customer circle.md` |

**Per-file edit recipe:**

1. **Rewrite `Description`** to state what this file produces and how,
   with zero comparative language. Delete every instance of "the
   direct template companion of," "the autonomous sibling of," "use
   this when you want X instead of Y."
2. **Rewrite `Usage Note`** to answer "when would I reach for this?"
   from the *user's situation*, never from the other file's existence.
   Good: "Use when you have thirty minutes and partial context, and
   want to be walked through the scoping decisions." Bad: "Use this
   when you want facilitation; use the autonomous version when scope
   is decided."
3. **Rewrite `When NOT to Use`** to describe *situations*, not
   *alternative files*. "You already know your scope and just want the
   number" is a situation. "Use tam-sam-som-analysis-prompt.md
   instead" is a referral.
4. **Delete the `Companion:` block.** If the relationship is genuinely
   worth teaching, it becomes one line in **Final Step** as an
   optional next move.
5. **Add the new `Standalone:` field** (see Phase C).

**Note:** `validate-prompts.py` currently checks that `Companion:`
paths resolve. Once these are removed that check goes quiet on its
own; keep the check, since surviving forward pointers still need to
resolve.

**Estimated effort:** 31 files, mechanical, roughly 10-15 minutes
each. Two sittings.

---

## Phase B: Fix completion coupling in `prompts/`

**Goal:** every one of the 34 files in `prompts/` is Level 0 — it
produces the finished artifact, in that file, in that session.

This is the TAM/SAM/SOM lesson generalized. A prompt that emits
instructions for producing the artifact, instead of producing the
artifact, has handed the user a second errand.

**Audit each file in `prompts/` against four tests:**

1. **Completion test** — does it produce the artifact, or a prompt for
   the artifact? If the latter, absorb the work inline.
2. **Cold-start test** — if the user pastes it with nothing else, does
   it ask for what it needs and proceed, or does it stall or assume?
3. **Research test** — does it ask the user for facts that are
   publicly discoverable? If so, it should go get them.
4. **Naming test** — does any file path appear above the Final Step
   block?

**Phase C measured the real scope, and it is bigger than the four
files below.** 24 of the 34 files in `prompts/` carry some variant of
the boilerplate line **"Assumes context is already present in
session"** (17 of them verbatim). That single sentence is the library's
most-repeated coupling defect: it declares a Level 2 file sitting in
the Level 0 tier. A novice who pastes one of those cold gets either a
stall or an output built on unlabeled assumptions.

This is good news, because it is one decision repeated 24 times rather
than 24 separate problems. The fix is the same each time: replace the
assumption with a short intake plus the two standing bypasses, so the
file works cold *and* collapses to zero questions when context is
already loaded. That is exactly what the collapse rule in
`tam-sam-som-market-sizing.md` does.

Run this to get the current list:

```
python3 scripts/validate-prompts.py | grep "backward prereq"
```

**Known failures to start with:**

- `prompts/stakeholder-map-prompt-template.md` — Usage Note says
  "Assumes context is already present in session." That is a Level 2
  file sitting in the Level 0 tier. Give it an intake.
- `prompts/agent-strategy-canvas-prompt-template.md` — carries the
  only hard gate in `prompts/`: "Do not proceed until a use case is
  provided" (lines 31 and 70). Convert to an intake question with a
  best-guess bypass, so silence produces a labeled example rather than
  a stall.
- `prompts/prd-prompt-template.md` — "run discovery or problem framing
  first." Reframe as a soft note plus a built-in minimal framing step.
- The `*-prompt-template.md` family generally — check each for the
  emit-a-prompt-instead-of-the-artifact pattern.

**The reference implementation is
`prompts/tam-sam-som-market-sizing.md`** (committed `05ef801`). Its
shape is the pattern to copy: capability check, context detection with
a collapse rule, Generative Guidance v2 intake with both standing
bypasses, its own research protocol, the actual work with arithmetic
shown, a fixed output schema, an anti-pattern refusal list, and
forward pointers confined to Final Step.

**Important:** fixing a `prompts/` file to Level 0 does **not** mean
touching its generator or workshop sibling. Those stay. They teach
different things.

---

## Phase C: Enforce it in the validator -- DONE

Implemented in `scripts/validate-prompts.py` (`coupling_checks()`).
Baseline it produced:

| Finding | Count | Level today |
|---|---|---|
| Missing `Standalone:` field in `prompts/` | 34 | staged warning |
| `assumes ... already` in `prompts/` metadata | 24 | staged warning |
| `Companion:` block in `prompts/` metadata | 10 | staged warning |
| Hard gate outside automation tier | 2 | staged warning |
| `run ... first` in `prompts/` metadata | 1 | staged warning |
| **File named above Final Step in `prompts/`** | **0** | **hard ERROR, already enforced** |

Default run: 0 errors, 150 warnings. `--strict` preview: 71 errors.

Staging works as planned: the one check that is already clean
(`names ... above Final Step`) is a live error, so the worst form of
coupling cannot be reintroduced starting now. Everything else reports
as a warning until Phases A and B clear it, then flip the default.

Use `--strict` to preview promotion at any time. To make it permanent
after Phase D, default `strict` to `True` in `main()`.

Original spec, retained for reference:

**New required metadata field: `Standalone:`**

Values:
- `yes` — Level 0
- `better with [artifact], works without` — Level 2
- `requires [artifact]` — Level 3

Assert `Standalone: yes` for every file in `prompts/`. Assert that
Level 3 appears only in `loops/` and `vibes/`. Add `Standalone` to
`REQUIRED_FIELDS` as a **warning** at first so the existing 34-file
backlog does not turn the build red on day one; promote to error once
Phase A and B are done.

This field is itself pedagogic. A reader learns the library has a
coupling discipline just by reading a header.

**New checks:**

| Check | Level | Rule |
|---|---|---|
| Body reference above Final Step | **ERROR** in `prompts/` | Split body on the Final Step heading; any repo-relative `.md` path in the part above it fails |
| Hard gate outside automation tier | **ERROR** | `STOP:` or "do not proceed until" in `prompts/`, `prompt-generators/`, `workshops/`, `market-intelligence/` |
| Backward-prereq phrasing in metadata | **WARN** | `run .* first`, `use .* instead`, `assumes .* (exists\|already)`, `companion` — scoped to `prompts/` metadata blocks |
| `Standalone` value matches tier | **WARN**, later ERROR | as above |

Implementation notes: `check_file()` already receives the path, so
tier-aware rules are a one-line directory test. The existing
`comment_block()` and body-stripping helpers give you metadata and
body separately, which is exactly the split these checks need. Keep
the existing repo-wide licensing sweep untouched.

**Then regenerate:** `python3 scripts/generate-catalog.py`, and
consider surfacing `Standalone:` as a column in `catalog/INDEX.md` so
the coupling contract is visible at browse time.

---

## Phase D: Document the rule

Add a short section to `AGENTS.md` (authoring contract) and a pointer
in `CLAUDE.md` (fast-path orientation) stating:

- The forward/backward rule
- The four coupling levels and the tier that may use each
- That duplication across tiers is intentional and encouraged, because
  the same framework taught three ways serves three learners
- That `prompts/` is the novice floor: one file in, one finished
  artifact out

Without this, the next contributor — human or agent — will helpfully
"reduce duplication" and reintroduce the coupling in the name of
tidiness.

---

## Suggested order when you sit back down

1. **Phase C first, in warn-only mode.** Ten minutes of validator
   work, and it converts the rest of the plan into a punch list you
   can watch shrink instead of a survey you have to hold in your head.
2. **Phase A** in two sittings, 31 files, mechanical.
3. **Phase B**, hardest and highest value; start with the four known
   failures above.
4. **Phase D**, then promote the Phase C warnings to errors.

Run after each sitting:

```
python3 scripts/validate-prompts.py
python3 scripts/generate-catalog.py
```

---

## Open item from this session

`prompt-generators/tam-sam-som-prompt-generator.md` still carries a
`Companion:` block pointing at the market-intelligence version, and
still has no metadata comment block at all (it is one of 14 files the
catalog generator flags as unmetadata'd). It is a Phase A **and** a
metadata-backfill candidate. It is not a deletion candidate — it
teaches scoping, which the other two do not.

## Acceptance criteria

- Zero `Companion:` blocks outside Final Step sections.
- Zero file paths above Final Step in any `prompts/` file.
- Every `prompts/` file declares `Standalone: yes` and passes the
  cold-start test.
- Hard gates exist only in `loops/` and `vibes/`.
- All 13 duplicate topics still have all their files.
