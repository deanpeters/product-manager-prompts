# swot-batch.md
<!--
## Description:
Run an evidence-cited SWOT across a competitor set as a governed
/batch: one company at a time, the quadrant output format embedded,
a per-company receipt, an item cap, and fail-stop — then, and only
then, the cross-company comparison. Batching SWOTs is where "scale
without visibility" bites hardest: five confident, unsourced SWOTs
look exactly like five evidenced ones until a rep quotes the wrong
weakness in a deal.

## Usage Note:
Bring the competitor list (ideally from
market-intelligence/competitive-research-snapshot-prompt.md or
market-landscape-scan-prompt.md — reuse that evidence instead of
re-searching). Each company's SWOT follows
market-intelligence/swot-analysis-prompt.md's rules; this recipe
adds the batch controls around it.

## When NOT to Use:
- One company: run the SWOT prompt directly; a batch of one is a
  loop wearing a hat.
- No evidence base and no search access: a batch multiplies
  fabrication risk by the size of the list.

## Instructions:
At every level: quadrant discipline (S/W internal, O/T external;
max 5 ranked entries each), every entry labeled Fact / Inference /
Assumption with a URL where sourced, per-company receipt, cap of 5
companies per run, fail-stop, cross-company comparison only after
all companies close.

## Pedagogic Notes:
- Teaches evidence discipline at scale: the receipt makes each
  company's evidence quality visible before the comparison blends
  them.
- Comparison-last teaches the batch equivalent of no-cross-category
  conclusions: synthesize only settled items.
- The cap of 5 teaches that SWOT depth and batch width trade off;
  ten shallow SWOTs are a spreadsheet, not intelligence.

## Attribution:
Created by Dean Peters (Productside.com), from "Prompts Aren't Dead.
They Just Got a Bigger Vocabulary." SWOT rules per
market-intelligence/swot-analysis-prompt.md. Loop discipline after
Leen Ammeraal, Programs and Data Structures in C (Wiley, 1987).

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 3, 2026
-->

## SWOT Output Format (every company, every level)

```markdown
## SWOT: [Company]
**As-of date:** | **Evidence base:** [snapshot / fresh search]

### Strengths (internal, evidenced)
- [Entry] — [URL, date] — [Fact/Inference]  (max 5, ranked)

### Weaknesses (internal, customer voice weighs heaviest)
- [Entry] — [URL, date] — [label]  (max 5, ranked)

### Opportunities (external)
- [Entry] — [URL, date] — [label]  (max 5, ranked)

### Threats (external)
- [Entry] — [URL, date] — [label]  (max 5, ranked)

### Crossings
- **S-O (their likely attack):** [1-2 moves, Inference]
- **W-T (their exposure):** [1-2 risks, Inference]
```

## Per-Company Receipt (closes each company)

```markdown
#### Receipt: [Company]
- Entries: S[n] W[n] O[n] T[n] | Sourced: [n of total]
- Evidence quality: [strong / mixed / thin — why]
- Assumptions worth flagging: [list, or "none"]
- Status: [complete / skipped: reason / FAILED at: step]
```

## Level 0 — Unseasoned (works today)

```
/batch Produce a SWOT analysis for each of these five competitors, with sources.
```

You'll get five SWOTs. Whether company four's weaknesses are
evidence or improv is a question the output format won't answer.

## Level 1 — Loop Lingo (the batch contract)

```
/goal Produce an evidence-cited SWOT for each competitor in my set —
every entry labeled and sourced per the SWOT Output Format, every
company closed with a receipt — then a cross-company comparison
built only from the settled SWOTs.

Base camp (calculate once): my product and segment, the decision
this supports, and the evidence already in session (snapshot,
landscape scan, VoC themes — reuse it; search only gaps).

Index before you batch:
1. List the companies (cap: 5 per run; more means run two).
2. Note which have session evidence vs. need fresh search.
3. Sequence: session-evidenced companies first (cheap before
   expensive).

/batch Process the list with these controls:

- One company at a time. Complete its SWOT and receipt before
  touching the next.
- Cheap checks first: is there enough public footprint to source a
  SWOT? If not: skip, record "thin footprint" in the receipt, move
  on. Do not improvise quadrants.
- Quadrant discipline per the SWOT Output Format; never invent
  financials, wins, share, or roadmap claims.
- If sourcing collapses mid-company: STOP the batch; the receipt
  names the company, the quadrant, and the resume point.
- After ALL companies close: the cross-company comparison — shared
  weaknesses (our openings), shared strengths (table stakes), and
  the one competitor whose W-T exposure is most actionable for us.
```

## Level 2 — Just Enough Jinja2 (cap, walk, receipts)

```jinja2
{% set routine_version = "swot-batch-v1.0" %}

{% for company in companies[:5] %}
## Company {{ loop.index }} of {{ companies[:5] | length }}:
{{ company }}

Cheap check: sufficient public footprint? If not — receipt says
"skipped: thin footprint," continue to next company.

Render the full SWOT Output Format for {{ company }}:
quadrants (max 5 ranked, labeled, sourced), then crossings, then:

#### Receipt: {{ company }}
- Entries / sourced-count / evidence quality / assumptions / status

If sourcing fails here, STOP the batch: this receipt is the resume
point.
{% else %}
STOP: the company list is empty. Build the index first.
{% endfor %}

{% if companies | length > 5 %}
NOTE: {{ companies | length - 5 }} companies remain beyond the cap.
Ask before run two.
{% endif %}

## Cross-company comparison (only after all receipts show complete)
- Shared weaknesses (our openings) | shared strengths (table
  stakes) | most actionable W-T exposure, and for whom

Generated by {{ routine_version }}.
```

## Final Step

Offer exactly 4 next options:
1. Build the battle card against the most exposed competitor
   (Recommended)
2. Feed shared weaknesses into positioning language
3. Start run two on the companies beyond the cap
4. Promote to a named /routine with your competitor list baked in

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 2`, or a
custom path.
