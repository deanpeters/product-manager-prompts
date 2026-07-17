# Working Session Summary — July 16-17, 2026

Shipped v2.2.0: market-intelligence grew from a directory of
investigation prompts into a complete intelligence system. This
note is the handoff — what changed, the architecture that now
exists, and what's open.

## What shipped (see CHANGELOG.md for full detail)

**v2.2.0 — The intelligence release:**

- **Tradecraft shelf** (`market-intelligence/reference/`): Dean's
  *Competitive Research on Steroids* compendium — eight
  intelligence-community collection disciplines mapped to PM
  artifacts — plus the EU/MENA regional source overlays. Doctrine,
  not prompts: no comment block, outside the validator and catalog
  (non-recursive glob skips subdirectories; future reference docs
  go here, not in SKIP_NAMES).
- **The collection floor**: seven discipline sweeps (osint-,
  finint-, geoint-demoint-, techint-, humint-, sigint-,
  masint-collection-prompt.md). All seven emit the **same
  fusion-ready Signal Inventory schema** — that shared schema is
  the system's spine. Existing prompts (VoC miner, earnings
  refresh, pricing tracker, TAM/SAM/SOM...) are now the deep-dive
  layer each sweep hands off to.
- **The situation room**: `all-source-fusion-prompt.md` —
  confidence stacking (1 discipline = watch, 2 = hypothesis, 3+ =
  actionable, conflict = dig), independence test (same-source
  signals collapse), ambition-vs-commitment corollary
  (announcements are intent until money/hiring/permits corroborate).
- **Ground truth**: `prompts/win-loss-analysis-prompt.md` —
  debriefs -> per-deal drivers, evidence-ranked patterns, and the
  confirm/refute ledger that closes the loop on public-signal
  inference. Guide mode when no interviews exist yet.
- **The rhythm**: `loops/fusion-cadence-routine.md` — weekly
  SIGINT, monthly OSINT+HUMINT, quarterly FININT+TECHINT+fusion,
  annual GEOINT/DEMOINT, event-driven MASINT. Tiered by source
  velocity: poll at the speed the source changes.
- Also: `workshops/product-sunset-workshop.md` (checkpointed EOL
  plan) and `prompts/incoming-request-breakdown.md` (inbound
  triage), both landed earlier in the cycle.
- Repo hygiene: main branch protection enabled (no force-push, no
  deletion; direct commits still allowed — no PR/status-check
  gates).

## The architecture in one breath

Instantiate the engagement (six compendium variables) -> run the
collection sweeps that matter -> fuse when 2+ disciplines hold
signals -> actionable stories update artifacts (battle cards,
roadmap bets, positioning, TAM) -> win/loss interviews confirm or
refute -> the cadence routine keeps it all turning. The worked
example in `market-intelligence/README.md` walks a launch caught
before its press release.

## How to work in this repo now

Unchanged from v2.0/v2.1 (see SESSION-SUMMARY-2026-07-03.md):
AGENTS.md first, validator + catalog after every edit, new prompts
declare an interaction mode. One addition: collection-floor prompts
must keep the Signal Inventory schema identical across all seven —
it is a contract, not a convention.

## Open items (in priority order)

1. **Licensing** — next session's agenda (Dean, July 17).
2. **Article URL**: when "Prompts Aren't Dead" publishes, link it
   in loops/README.md and the root README.
3. **Agent Strategy Canvas Prompt 1 of 2** — Dean to provide
   (Prompt 2 is in prompts/).
4. **Engagement-brief prompt** (candidate): fill the compendium's
   six instantiation variables once, carry them across sweeps and
   into the routine identity block.
5. **Regional overlay build-outs** (on demand): APAC, LATAM,
   Sub-Saharan Africa, following the EU/MENA pattern.
6. **79 grandfathered validator warnings** — migrate-on-touch
   worklist, no mass rewrites.
7. **Literal Jinja2 rendering pipeline** — future candidate for
   agent builders.
