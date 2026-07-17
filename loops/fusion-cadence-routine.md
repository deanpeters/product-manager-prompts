# fusion-cadence-routine.md
<!--
## Description:
Run the intelligence collection floor as a governed /routine on the
compendium's fusion cadence: weekly SIGINT sweep, monthly OSINT +
HUMINT digest, quarterly FININT + TECHINT deep pass, annual
GEOINT/DEMOINT terrain refresh, event-driven MASINT alerts — each
tier feeding the same fusion-ready signal inventory, with a
quarterly all-source fusion brief on top and receipts controlling
drift. The parent rhythm of the market-intelligence directory.

## Usage Note:
Orchestrates the seven collection prompts in market-intelligence/
(osint-, finint-, geoint-demoint-, techint-, humint-, sigint-,
masint-collection) and closes each quarter with
all-source-fusion-prompt.md. Doctrine: the Fusion Cadence section
of market-intelligence/reference/competitive-research-compendium.md.
Run each collection prompt once manually for its baseline before
scheduling its tier — a routine that has never seen a baseline
regenerates instead of diffing. competitive-watch-routine.md is the
narrower sibling: same governance, one discipline's aperture.

## When NOT to Use:
- No baselines exist yet: run the collection prompts directly
  first; this routine diffs, it does not found.
- You only care about one channel (pricing, reviews): schedule the
  matching single prompt; the full cadence would bill you for
  quiet disciplines.
- One-off deep dive before a decision: run the collection prompts
  and fusion directly, no routine wrapper needed.

## Instructions:
At every level: each tier runs its discipline sweeps against the
prior baseline and appends to the shared signal inventory; tiers
never regenerate baselines; the quarterly fusion brief consumes
the inventory and applies confidence stacking; event-driven MASINT
alerts fire within 48 hours on material triggers; never invent
signals, sources, or filings; close every run with the Run
Receipt; changes to targets, tiers, or cadence require a version
bump with approval.

## Pedagogic Notes:
- Tiering collection by source velocity (web changes weekly,
  filings quarterly, statistics annually) teaches cadence design:
  poll at the speed the source actually changes, not the speed of
  your anxiety.
- The shared inventory across tiers teaches accumulation: fusion
  quality comes from signals stacking between runs, not from any
  single sweep.
- Receipts per tier make drift visible across months — when the
  July fusion disagrees with April's, the receipts say whether
  the market moved or the routine did.

## Attribution:
Created by Dean Peters (Productside.com), from the Competitive
Research Compendium's fusion cadence. Loop discipline after Leen
Ammeraal, Programs and Data Structures in C (Wiley, 1987).

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 16, 2026
-->

## The Cadence (calculate once; this is the routine's spine)

```
Weekly     SIGINT sweep                 ~30 min tier
Monthly    OSINT + HUMINT digest
Quarterly  FININT + TECHINT deep pass, then ALL-SOURCE FUSION brief
Annual     GEOINT/DEMOINT terrain refresh (plus every TAM refresh)
Event      MASINT alerts, material filings, leadership exits:
           react within 48 hours
```

## Run Receipt Format (closes every tier run, every level)

```markdown
#### Receipt
- Routine: fusion-cadence [version] | Tier: [weekly/monthly/
  quarterly/annual/event]
- Run date: [date] | Prior baseline: [date]
- Disciplines swept: [list] | Target(s): [list]
- Signals added to inventory: [N] | Watch items: [N]
- Corroborations logged: [N] | Conflicts flagged: [N]
- Skipped / failed: [list, or "none"]
- Assumptions made: [list, or "none"]
```

## Level 0 — Unseasoned (works today)

```
/routine Every week, check what my competitor is up to across the
web, their filings, their job posts, and their patents, and tell
me if anything big is happening.
```

Week one, this returns everything at once and calls it all big.
Week twelve, it is re-reading annual filings weekly, billing you
for statistics that update once a year, and the "anything big" bar
has drifted to wherever the model's mood is.

## Level 1 — Loop Lingo (the cadence contract)

```
/goal Maintain a multi-discipline intelligence watch on [TARGET]
that accumulates a fusion-ready signal inventory and produces a
confidence-stacked fusion brief every quarter — every tier run
closed with the Run Receipt.

Routine identity (calculate once; restate in every receipt):
- Name and version: fusion-cadence v1.0
- Target(s): [names]
- Decision it feeds: [the standing decision or review]
- Tier map: weekly=SIGINT; monthly=OSINT+HUMINT;
  quarterly=FININT+TECHINT then fusion; annual=GEOINT/DEMOINT;
  event=MASINT alerts within 48 hours

/routine Each run:

1. Identify the tier due (order checks by cost: the weekly SIGINT
   sweep is cheap — run it first; never run a quarterly pass to
   answer a weekly question).
2. Run the tier's collection prompts against their prior
   baselines. Diff — do not regenerate.
3. Append new signals to the shared inventory (index before
   search: check the inventory before logging — a signal already
   captured gets a date bump, not a duplicate row).
4. Log corroborations: does any new signal confirm or contradict
   an open story from a prior tier? Flag conflicts loudly.
5. Quarterly only: run the all-source fusion brief on the full
   inventory; confidence-stack; retire stories that resolved.
6. "Quiet tier, nothing material" is a valid result — say it in
   one line and close with the receipt.
7. Close every run with the Run Receipt.

Drift controls:
- Changing targets, tier map, or cadence requires a version bump
  (v1.0 -> v1.1) with my approval. Never silently.
- Two consecutive quiet quarters on a target: recommend demoting
  it to event-driven only.
- Missing baseline for a due tier: STOP that tier and say which
  collection prompt must run manually first.
```

## Level 2 — Just Enough Jinja2 (tier walk, exits, receipts)

The inventory and receipt stay markdown; the Jinja2 carries
identity, selects the tier, and enforces the exits.

```jinja2
{% set routine_version = "fusion-cadence-v1.0" %}
{% set tier_map = {
  "weekly":    ["sigint"],
  "monthly":   ["osint", "humint"],
  "quarterly": ["finint", "techint", "FUSION"],
  "annual":    ["geoint-demoint"],
  "event":     ["masint"]
} %}

{% if due_tier not in tier_map %}
STOP: unknown tier "{{ due_tier }}". Valid: {{ tier_map | list }}.
{% endif %}

{% for discipline in tier_map[due_tier] %}
{% if discipline == "FUSION" %}
## Fusion brief (quarterly close)
Run all-source-fusion on the full inventory. Confidence-stack.
Retire resolved stories; promote 3+ discipline stories to the
leadership brief.
{% else %}
## Sweep {{ loop.index }} of {{ tier_map[due_tier] | length }}:
{{ discipline }}-collection

{% if not baselines[discipline] %}
STOP this sweep: no {{ discipline }} baseline. Run
{{ discipline }}-collection-prompt manually first.
{% else %}
Diff against baseline {{ baselines[discipline] }}. New signals
append to the inventory; known signals get a date bump, not a
duplicate row. Corroborations and conflicts flagged.
{% endif %}
{% endif %}
{% endfor %}

{% if quiet_quarters >= 2 %}
Recommend demoting this target to event-driven only.
{% endif %}

#### Receipt
- Routine: {{ routine_version }} | Tier: {{ due_tier }}
- Run date: {{ run_date }} | Baselines: [per discipline]
- Signals added / watch / corroborations / conflicts / skipped /
  assumptions: [fill]
```

## Final Step

Offer exactly 4 next options:
1. Run the tier due now against its baselines (Recommended)
2. Show the current signal inventory and its open stories
3. Propose the v1.1 changes recent receipts argue for (targets,
   tiers, cadence)
4. Jump the queue: run the quarterly fusion brief early on what
   the inventory holds today

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 2`, or a
custom path.
