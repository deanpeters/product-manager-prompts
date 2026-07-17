# Workshops

**Guided working sessions that end in a finished artifact**

Prompts here run a facilitated, multi-turn session — Generative
Guidance questions, checkpoint gates, context-aware recommendations —
and produce the **artifact itself**: a battle card, a PRD, an
opportunity solution tree, a business case, a canvas.

That's the split with the neighboring directories:

- **`/prompts/`** — session context is already loaded; you want
  execution-quality output in one pass.
- **`/prompt-generators/`** — the session **emits a reusable prompt**
  you (or your team) run later.
- **`/workshops/`** (here) — the session **produces the deliverable**,
  with you steering the decisions along the way.

Every workshop follows the Generative Guidance pattern v2 (see
[`generative-guidance-pattern.md`](../generative-guidance-pattern.md))
or checkpointed co-construction (see
[`interaction-modes.md`](../interaction-modes.md)).

## What's Available

| Workshop | Produces | Framework |
|----------|----------|-----------|
| **[battle-card-workshop.md](battle-card-workshop.md)** | Competitive battle card | Material-shift criterion; field-action artifact |
| **[prd-workshop.md](prd-workshop.md)** | Full PRD, section by section | Your team's template (or canonical fallback); checkpoint gates |
| **[opportunity-solution-tree-workshop.md](opportunity-solution-tree-workshop.md)** | Opportunity solution tree + first experiment | Teresa Torres continuous discovery |
| **[feature-investment-workshop.md](feature-investment-workshop.md)** | Build / don't-build business case | Revenue path, cost structure, margin-adjusted ROI |
| **[problem-framing-canvas-workshop.md](problem-framing-canvas-workshop.md)** | Problem statement + "How might we" | MITRE ITK Problem Framing Canvas |
| **[painstorming-workshop.md](painstorming-workshop.md)** | PAINstorming table | MITRE ITK: Persona, Activities, Insights, Needs |
| **[lean-ux-canvas-workshop.md](lean-ux-canvas-workshop.md)** | Filled Lean UX Canvas + least-work experiment | Gothelf Lean UX Canvas v2 |
| **[product-sunset-workshop.md](product-sunset-workshop.md)** | Full product/feature EOL plan, section by section | Your team's template (or canonical 6-section fallback); pairs with the EOL announcement prompt |

Many workshops have a direct-template sibling in `/prompts/` for
sessions where context is already loaded — check each file's
`Companion:` line.
