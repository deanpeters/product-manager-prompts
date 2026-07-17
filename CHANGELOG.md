# Changelog

## v2.2 — July 17, 2026

The intelligence release: the library's market-intelligence
directory becomes a complete intelligence system — doctrine
(tradecraft shelf), collection (seven discipline sweeps), fusion
(confidence stacking), ground truth (win/loss), and rhythm (fusion
cadence) — plus the product-sunset workshop and inbound-triage
prompt.

### `prompts/` — win/loss analysis (new)

- `win-loss-analysis-prompt.md` — turns win/loss and churn debrief
  material into structured ground truth: per-deal decision-driver
  table, win/loss patterns ranked by evidence count (never story
  vividness), stated-vs-evidenced reasons (the "price costume"
  flag), competitor intelligence extracted for battle cards, and a
  confirm/refute ledger against public-signal inferences — the
  handoff that keeps all-source fusion honest. Guide mode when no
  debriefs exist: question sets for won/lost/churned plus
  interviewing craft notes. Quotes only from provided material.

### `market-intelligence/` — the collection floor (seven new prompts)

One collection sweep per intelligence discipline in the compendium,
completing full discipline coverage. Each embeds its discipline's
sources and signal -> inference chains from
`reference/competitive-research-compendium.md`, and all seven emit
the same fusion-ready Signal Inventory schema (signal, source URL +
date, Fact / Inference / Assumption label, inference chain, artifact
fed), so any combination stacks in `all-source-fusion-prompt.md` and
scheduled runs diff against prior baselines. Existing prompts become
the deep-dive layer each sweep hands off to.

- `osint-collection-prompt.md` — press, analysts, exec social,
  review clusters, conferences, prediction markets; say vs
  said-about gap
- `finint-collection-prompt.md` — filings (Risk Factors diffs,
  segment restructures, deferred revenue), earnings Q&A dodges,
  procurement, entity registrations, sovereign capital;
  capture-rate reality check and corroboration ledger
- `geoint-demoint-collection-prompt.md` — establishment counts,
  occupation/wage statistics, firmographics, trade flows; terrain
  read with TAM denominators, ICP boundaries, persona localization
- `techint-collection-prompt.md` — patent clusters, trademarks,
  technographics, changelog/API diffs, standards bodies, funded
  research, preprints; lead times per signal and the people trail
- `humint-collection-prompt.md` — posting surges (normalized
  against baseline), leadership moves, sentiment, alumni flows;
  win/loss framing as ground truth your team collects
- `sigint-collection-prompt.md` — web/pricing diffs with both-dates
  rule, SEO/SEM posture, SSL certs/subdomains, app-store metadata;
  launch-staging flags
- `masint-collection-prompt.md` — import/export, facilities and
  permits, ops capacity, certification pipelines; every anomaly
  names its disambiguating discipline (software-equivalent mode for
  non-hardware targets)
- `all-source-fusion-prompt.md` updated: evidence base and
  collection-gap handoffs now name the seven sweeps
- README: new collection-floor table; coverage table shows all
  eight disciplines covered

### `loops/` — fusion cadence routine (new)

- `fusion-cadence-routine.md` — the collection floor as a governed
  `/routine` on the compendium's cadence: weekly SIGINT, monthly
  OSINT + HUMINT, quarterly FININT + TECHINT + fusion brief, annual
  GEOINT/DEMOINT terrain refresh, event-driven MASINT within 48
  hours. Tiered by source velocity (poll at the speed the source
  changes), shared signal inventory across tiers, receipts per run,
  version-bump drift control, demote-to-event-driven exit after two
  quiet quarters. Three levels: unseasoned, loop lingo, Just Enough
  Jinja2 (tier map as data structure, baseline STOP guards).

### `workshops/` — product sunset (new workshop)

- `product-sunset-workshop.md` — checkpointed co-construction of a
  product or feature End-of-Life plan against the team's own
  template (canonical 6-section fallback: rationale, customer
  impact, technical transition, support enablement,
  legal/compliance, timeline), one gated section per turn, with
  Assumption / Open Question labels and a closing self-critique.
  Pairs with `prompts/eol-for-a-product-message.md` for the
  customer-facing announcement.

### `market-intelligence/` — all-source fusion (new prompt)

- `all-source-fusion-prompt.md` — the situation room over the
  collection floor: fuses signals from the directory's other
  investigations (or a bulk drop) into confidence-rated stories.
  Runs the confidence-stacking rule (1 discipline = watch item,
  2 = working hypothesis, 3+ = actionable intelligence, conflict =
  dig), an independence test (same-source signals collapse to one
  discipline), and the ambition-vs-commitment corollary
  (announcements are intent until funding, procurement, hiring, or
  permits corroborate). Every actionable story ends with the PM
  artifact it changes and the move to make before the competitor's
  launch, not after. Stable schema; a prior brief becomes the
  baseline the next run diffs against. Doctrine source: the
  compendium below.

### `market-intelligence/reference/` — the tradecraft shelf (new)

Doctrine documents behind the runnable investigation prompts. These
are reference material, not prompts: no comment block, excluded from
the catalog and validator.

- `competitive-research-compendium.md` — *Competitive Research on
  Steroids*: the eight intelligence-community collection disciplines
  (OSINT, FININT, GEOINT/DEMOINT, TECHINT, HUMINT, SIGINT, MASINT,
  All-Source Fusion) mapped to PM artifacts. Per discipline: free and
  paid sources, signal → inference chains, and which artifact it
  feeds. Plus the confidence-stacking rule, a fusion template and
  cadence, an instantiation block ([TARGET], [MARKET], [GEOGRAPHY],
  [BUYER], [CAPABILITY], [DECISION]), and collection guardrails.
- `regional-source-overlays-eu-mena.md` — companion overlay system:
  EU (TED, BRIS, CORDIS, Eurostat, EUR-Lex, NANDO) and MENA (GCC-Stat,
  country procurement platforms, development-bank procurement,
  sovereign/localization signals) sources mapped onto the core
  disciplines, with regional research guardrails.
- `market-intelligence/README.md` — new "tradecraft shelf" section
  plus a discipline coverage table mapping existing prompts to the
  eight disciplines and naming the gaps (TECHINT, HUMINT, MASINT,
  All-Source Fusion).

### `prompts/` — inbound triage (new job-to-be-done)

- `incoming-request-breakdown.md` — a chief-of-staff-grade analyst
  that decodes an incoming message (Slack ping, email, mandate,
  escalation, FYI) into a structured breakdown: classify, sender
  read, literal ask vs underlying job-to-be-done, sentiment and
  subtext, success criteria vs must-haves, gaps, risks, and next
  steps. Extends the library beyond "produce a named artifact" into
  interpreting the asks that land in a PM's inbox — reading from a
  product leader's chair, not an engineer's. Multimodal input
  (screenshot, image, file, PDF, or text); depth scales to the
  message.

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
