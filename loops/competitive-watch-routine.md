# competitive-watch-routine.md
<!--
## Description:
Run a competitive intelligence watch as a governed /routine: diff
against the last approved snapshot, report only material shifts in
an embedded changelog format (URL, date, Fact / Inference /
Assumption label per claim), close every run with a receipt (name,
version, sources, competitor list), and control drift with version
bumps — because a routine's failure mode is mutation in captivity.

## Usage Note:
The scheduled, versioned form of
market-intelligence/competitive-intel-watch-prompt.md — run that
once for the baseline, then run this on cadence with the prior
snapshot in session. The shift-report and receipt formats below are
the contract; when run twelve behaves differently from run three,
the receipts tell you whether the market moved or the routine did.

## When NOT to Use:
- First run / no baseline: use the snapshot prompt to create one.
- One-off competitive question: that is a prompt, not a routine;
  ask it directly with citation instructions.

## Instructions:
At every level: diff against the prior snapshot, never regenerate
it; report only shifts clearing the materiality bar, in the Shift
Report Format; "no material change" is a valid result; never invent
competitors, features, pricing, market share, customer wins, or
roadmap claims; close every run with the Run Receipt.

## Pedagogic Notes:
- The receipt is the anti-drift control: it makes every run
  auditable against the run before it.
- The embedded shift format forces per-claim evidence (URL + date +
  label) instead of a confident paragraph of unsourced vibes.
- The consecutive-no-change exit teaches routines to argue for
  their own cadence instead of billing the quiet.

## Attribution:
Created by Dean Peters (Productside.com), from "Prompts Aren't Dead.
They Just Got a Bigger Vocabulary." Loop discipline after Leen
Ammeraal, Programs and Data Structures in C (Wiley, 1987).

## Licensing:
MIT License

Date: July 3, 2026
-->

## Shift Report Format (every material shift, every level)

```markdown
### [Competitor] — [4 to 8 word change summary]
- **What changed:** [then -> now, one or two bullets]
- **Evidence:** [URL] ([date]) — [Fact / Inference / Assumption]
- **Why it clears the bar:** [who would act on this: sales,
  pricing, roadmap]
- **Confidence:** [high / medium / low]
- **Downstream flag:** [battle card section / positioning /
  pricing analysis / roadmap assumption — or "monitor only"]
```

## Run Receipt Format (closes every run, every level)

```markdown
#### Receipt
- Routine: [name] [version]
- Run date: [date] | Prior snapshot: [date]
- Competitors checked: [list]
- Materiality bar in force: [list]
- Sources consulted: [count + types]
- Shifts reported: [N] | Watchlist items: [N]
- Skipped / failed: [list, or "none"]
- Assumptions made: [list, or "none"]
```

## Level 0 — Unseasoned (works today)

```
/routine Every Monday, check my competitors for anything new and tell me what changed.
```

Week one this feels magical. Week nine, "anything new" has quietly
become "anything," the competitor list is whatever the model
remembers, and nobody can say when the drift started.

## Level 1 — Loop Lingo (the routine contract)

```
/goal Maintain an evidence-cited watch on my competitor set,
reporting only material shifts against the last approved snapshot —
every shift in the Shift Report Format, every run closed with the
Run Receipt.

Routine identity (calculate once; restate in every receipt):
- Name and version: competitive-watch v1.0
- Competitor list: [names]
- Materiality bar: pricing/packaging changes, launches and
  deprecations, positioning shifts, leadership/funding/M&A, major
  wins or losses, credible roadmap signals

/routine Each run:

1. Read the prior snapshot fully. Diff — do not regenerate.
2. Show a 3-bullet search plan (what you'll check, source types,
   fact/inference separation); continue unless I revise it.
3. Per competitor, cheap checks first: anything new on the public
   record since the prior snapshot? Only where yes, do the
   expensive read of what it means.
4. Report each material shift in the Shift Report Format. Below
   the bar goes to the watchlist, not the report.
5. "No material shifts this cycle" is a valid, useful result — say
   it plainly, then list the watchlist.
6. Close with the Run Receipt.

Drift controls:
- Changing the competitor list, materiality bar, or either format
  requires a version bump (v1.0 -> v1.1) with my approval. Never
  silently.
- Two consecutive no-change runs: recommend widening the cadence.
- No prior snapshot found: STOP — a diff without a baseline is a
  regeneration pretending to be a delta.
```

## Level 2 — Just Enough Jinja2 (identity, walk, exits)

The report and receipt stay markdown; the Jinja2 carries identity,
walks the list, and enforces the exits.

```jinja2
{% set routine_version = "competitive-watch-v1.0" %}
{% set materiality_bar = "pricing/packaging, launches/deprecations, positioning, leadership/funding/M&A, major wins/losses, roadmap signals" %}

{% if not prior_snapshot %}
STOP: no baseline snapshot. Run the snapshot prompt first.
{% endif %}

Search plan first: 3 bullets, then continue unless revised.

{% for competitor in competitors %}
## Check {{ loop.index }} of {{ competitors | length }}:
{{ competitor }}

Cheap check: anything new on the public record since
{{ prior_snapshot_date }}? If no: one line, move on.

For each change clearing the bar ({{ materiality_bar }}), render:

### {{ competitor }} — [4 to 8 word change summary]
- **What changed:** [then -> now]
- **Evidence:** [URL] ([date]) — [Fact / Inference / Assumption]
- **Why it clears the bar:** [who acts on this]
- **Confidence:** [high / medium / low]
- **Downstream flag:** [battle card / positioning / pricing /
  roadmap / monitor only]

Below the bar: add to the watchlist, not the report.
{% else %}
STOP: competitor list is empty. Confirm the list before running.
{% endfor %}

{% if consecutive_no_change >= 2 %}
Recommend widening the cadence — nothing is moving.
{% endif %}

#### Receipt
- Routine: {{ routine_version }}
- Run date: {{ run_date }} | Prior snapshot: {{ prior_snapshot_date }}
- Competitors checked: {{ competitors | join(", ") }}
- Materiality bar in force: {{ materiality_bar }}
- Shifts reported / watchlist / skipped / assumptions: [fill]
```

## Final Step

Offer exactly 4 next options:
1. Update the flagged battle-card sections from this run's shifts
   (Recommended)
2. Propose the v1.1 changes this run surfaced (list, bar, or format)
3. Produce a refreshed full snapshot as the new baseline
4. Adjust cadence based on the last three runs' change rate

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 2`, or a
custom path.
