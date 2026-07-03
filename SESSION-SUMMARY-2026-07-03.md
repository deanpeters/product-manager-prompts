# Working Session Summary — July 3, 2026

Shipped v2.0.0 and v2.1.0 in one session: the library's largest
restructure. This note is the handoff — what changed, what's open,
and how to pick the work up.

## What shipped (see CHANGELOG.md for full detail)

**v2.0.0** — Pattern foundation and restructure:
- Generative Guidance pattern rewritten as **v2**
  (`generative-guidance-pattern.md`): 3 recommendations + "Other",
  standing bypasses (best guess, bulk drop), loop control, question
  budgets, confirm-before-build. v1 prompts are **grandfathered:
  migrate on touch, never mass-rewrite.**
- `interaction-modes.md`: facilitation / checkpointed
  co-construction / autonomous investigation.
- `jinja2-prompt-structures.md`: loops, switches, guards for
  loop/goal/agent-safe prompts.
- Directory taxonomy: `prompts/` (one-pass from context),
  `prompt-generators/` (emit reusable prompts), **`workshops/`**
  (guided session produces the artifact — split from
  prompt-generators), **`market-intelligence/`** (autonomous
  research — renamed from a short-lived `investigations/`).
- ~30 new assets; tooling in `scripts/`; generated `catalog/`.

**v2.1.0** — Loops and strategy frameworks:
- **`loops/`**: seven seasoned `/goal` `/loop` `/batch` `/routine`
  recipes from Dean's article *"Prompts Aren't Dead. They Just Got a
  Bigger Vocabulary."* Each runs at three levels (plain, loop lingo,
  Just Enough Jinja2) with canonical output formats embedded.
- `market-intelligence/` gained the strategy suite: TAM/SAM/SOM
  (moved from prompts/), battle-card-builder, SWOT, Porter's Five
  Forces, Ansoff — all evidence-cited investigation mode.

## How to work in this repo now

1. Read `AGENTS.md` first (authoring contract), then the pattern doc
   matching your prompt's mode.
2. After any prompt edit:
   `python3 scripts/validate-prompts.py` (errors block) and
   `python3 scripts/generate-catalog.py` (regenerates `catalog/`,
   which is derived — never hand-edit).
3. New prompts declare an interaction mode and follow Generative
   Guidance v2 if they facilitate. Include "When NOT to Use."
4. Companion links use repo-relative paths (the validator checks
   them).

## Open items (in priority order)

1. **Article URL**: when "Prompts Aren't Dead" publishes, link it in
   `loops/README.md` and the root README (both currently cite the
   title only).
2. **Agent Strategy Canvas "Prompt 1 of 2"**: `prompts/agent-
   strategy-canvas-prompt-template.md` is labeled Part 2; Dean has
   Prompt 1 — add it alongside when provided.
3. **79 validator warnings** = the migrate-on-touch worklist:
   grandfathered files missing metadata fields. Clear a file's
   warnings whenever you edit it for any reason. Do not mass-fix.
4. **Storytelling generators** are still on the v1 pattern —
   migrate on touch, same rule.
5. **Candidate future work**: a literal (rendered) Jinja2 pipeline
   for agent builders — pairing the loops/ recipes with JSON schemas
   and a real renderer; a "customer discovery" cross-directory view
   in the catalog.

## Gotchas for the next person

- **CLAUDE.md is gitignored** in this repo — it exists locally on
  Dean's machine only. AGENTS.md is the committed equivalent and is
  current; if you use Claude Code, copy AGENTS.md's guidance or ask
  Dean for the local CLAUDE.md.
- The catalog and this repo's counts (96 assets) regenerate from
  metadata comment blocks; if a count looks stale, re-run the
  catalog script rather than editing numbers.
- `resumes-resignations-reactions/`, `skeletons/`, and `flows/` were
  intentionally untouched in v2.x.

## Session participants

Dean Peters, with Claude Code (Fable 5). Companion repos studied for
this redesign: Product-Manager-Skills and Mitre-Skills (both local
under ~/Code/).
