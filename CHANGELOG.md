# Changelog

## v2.1 — July 3, 2026

Loops and strategy frameworks: the library's answer to "prompts are
dead, loops are the new black."

### `loops/` (new directory)

Seasoned `/goal`, `/loop`, `/batch`, and `/routine` recipes recasting
key prompts, from the article *"Prompts Aren't Dead. They Just Got a
Bigger Vocabulary"* (Dean Peters). Grounded in four rules (calculate
once, order checks by cost, index before search, know the critical
path — after Ammeraal, 1987) and the primitives' distinct failure
modes (goal=ambiguity, loop=motion without progress, batch=scale
without visibility, routine=drift). Every recipe runs at three
levels — plain commands, plain-English loop lingo, Just Enough
Jinja2 — with the canonical output format embedded at every level:
markdown is the meal; Jinja2 only caps, walks, gates, and signs.

- `story-splitting-loop.md` — Lawrence rubric, pass ceiling,
  survivor rule, canonical story format
- `prd-section-loop.md` — canonical 9 sections as a visible data
  structure, dependency order, per-section gates and compaction
- `epic-story-batch.md` — 10-epic cap, per-epic receipts, fail-stop
- `research-synthesis-loop.md` — category index, one theme per turn,
  embedded theme format with real verbatims
- `competitive-watch-routine.md` — versioned receipts, drift
  controls, no-change cadence exit
- `swot-batch.md` — SWOT per competitor with evidence-quality
  receipts; comparison only after all companies settle
- `market-sizing-loop.md` — TAM/SAM/SOM one segment per turn,
  frozen segment index, roll-up last with sensitivity

### `market-intelligence/` strategy frameworks

All in autonomous investigation mode (search plan gate, per-claim
Fact / Inference / Assumption labels, do-not-invent lists, stable
schemas):

- `tam-sam-som-analysis-prompt.md` — moved in from `prompts/`
  (renamed from tam-sam-som-autonomous-analysis.md)
- `battle-card-builder-prompt.md` — evidence-cited card from public
  sources; autonomous sibling of the battle-card workshop
- `swot-analysis-prompt.md` — sourced quadrants + S-O / W-T
  crossings
- `porters-five-forces-prompt.md` — rated forces with documented
  signals; AI substitution named; profit-pool close
- `ansoff-matrix-prompt.md` — evidence per quadrant, risk gradient
  enforced, recommended sequence

### Known open items (carried forward)

- Article URL to be linked in loops/README and root README when
  published.
- Five Forces and Ansoff deliberately have no loop recipes:
  single-artifact analyses with no natural iteration axis.

## v2.0 — July 3, 2026

The library's largest update: a versioned facilitation pattern, three
documented interaction modes, two new directories, ~30 new prompt
assets, and repo tooling. Informed by studying the
[Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills)
and MITRE ITK skills repos.

### Patterns and documentation

- **Generative Guidance v2** (`generative-guidance-pattern.md`):
  3 context-aware recommendations + "Other" per question; standing
  bypasses ("take your best guess", bulk drop with found / inferred /
  missing accounting); loop control (skip, go back, stop early);
  search-when-sparse; question budgets; confirm-before-build.
  Includes a v1→v2 changelog. v1 prompts are grandfathered —
  migrate on touch, never mass-rewrite.
- **`interaction-modes.md`** (new): the three modes — facilitation,
  checkpointed co-construction, autonomous investigation — with the
  contracts each implies (evidence labels, search plan gates,
  materiality bars, delta rules).
- **`jinja2-prompt-structures.md`** (new): loops, switches, and
  guards for prompts that run under loop/goal commands or inside
  agents. Three roles (control-flow safety, output contracts,
  plan-then-iterate), six authoring rules, anti-pattern table.

### New directories

- **`market-intelligence/`** (new): autonomous research prompts —
  competitive research snapshot, competitive intel watch (delta
  monitor), market landscape scan, voice-of-customer miner,
  earnings/executive signal refresh, pricing & packaging tracker,
  PESTEL delta monitor. Built for citations, labeled evidence, and
  scheduled/agent runs.
- **`workshops/`** (new): guided sessions that produce the artifact
  itself — battle card, PRD, opportunity solution tree, feature
  investment case, problem framing canvas, PAINstorming table,
  Lean UX canvas. (Split out of `prompt-generators/`, which now
  holds only prompts that emit reusable prompts.)

### New prompts and generators (highlights)

- `prompts/`: PRD template (one-pass from session context),
  autonomous TAM/SAM/SOM with evidence contract, stakeholder map,
  premortem, discovery interview guide, Lean UX canvas, Agent
  Strategy Canvas (9-box agentic design), session saver.
- `prompt-generators/`: stakeholder map, prioritization framework
  chooser, premortem, discovery interview, research-agent designer
  (emits custom investigation prompts) — all on the v2 pattern.
- `storytelling/`: Research-to-Narrative Bridge (turns
  market-intelligence output into stakeholder stories without
  overclaiming); metadata blocks added across the directory.
- `vibes/`: two Jinja2-structured exemplars — plan-then-iterate
  user-story splitting (Lawrence rubric) and an epic-to-stories
  formatting agent with an explicit JSON input schema.

### Tooling

- `scripts/generate-catalog.py`: builds `catalog/INDEX.md` and
  `catalog/prompts-index.yaml` from the metadata comment blocks.
- `scripts/validate-prompts.py`: enforces required metadata, v2
  fixtures, companion-link resolution, and the no-emoji rule.
  Errors block; warnings are the migrate-on-touch worklist.

### Conventions introduced

- Template ↔ generator ↔ workshop companion cross-links.
- "When NOT to Use" notes required on new/revised prompts.
- Comment metadata block is the machine-readable source of truth;
  `catalog/` is derived output.

### Known open items

- 79 validator warnings: grandfathered files missing metadata
  fields — clear them as files are touched.
- Agent Strategy Canvas is "Prompt 2 of 2"; Prompt 1 to be added.
- Storytelling generators still on the v1 pattern; migrate on touch.
- Possible follow-ons: Jinja2 recasts of the competitive-intel watch
  and PRD workshop; a literal (rendered) Jinja2 pipeline for agent
  builders; a customer-discovery catalog view.

## v1.x — 2024 through March 2026

Community build: the original `prompts/`, `prompt-generators/`,
`storytelling/`, `skeletons/`, `vibes/`, and
`resumes-resignations-reactions/` collections; the Generative
Guidance pattern (5-choice form); comment-driven pedagogy;
SUBMISSIONS-GUIDE structural standards (March 2026).
