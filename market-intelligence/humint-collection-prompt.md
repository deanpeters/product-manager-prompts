# humint-collection-prompt.md
<!--
## Description:
Runs a HUMINT (Human Intelligence) collection sweep on a target
company: job-posting patterns, leadership moves, employee
sentiment, alumni flows, and conference-circuit presence — plus a
win/loss framing section, because interviews are the one source
that says why deals actually close. Every signal lands in a
fusion-ready inventory with a source URL, date, evidence label,
and the inference chain it supports. The sports scout's
discipline: organizations announce strategy through job boards
long before press releases; people are the tell.

## Usage Note:
One of seven discipline collection prompts feeding
all-source-fusion-prompt.md; doctrine in
reference/competitive-research-compendium.md (HUMINT discipline).
Everything here is public-record people-watching: postings,
announcements, review sites, published talks. The win/loss section
frames questions for your own program — this prompt cannot conduct
interviews, and says so rather than inventing quotes. Primary feed
for roadmap bets (their build signals) and battle cards (org
instability plays).

## When NOT to Use:
- You want interview answers, not interview questions: win/loss
  calls are your team's fieldwork; synthesize completed debriefs
  with prompts/win-loss-analysis-prompt.md, and see the discovery
  interview assets in prompt-generators/ for problem discovery.
- You need this week's site or pricing changes: that is SIGINT.
- Anything requiring pretexting, soliciting NDA-protected
  information, or targeting individuals' private lives: out of
  scope and out of bounds — see the compendium's guardrails.

## Required Context Keys:
1. The [TARGET] company
2. The [DECISION] this collection will feed
3. The [CAPABILITY] or specialty to watch for, if any (focuses the
   posting analysis)

## Missing Context Rule:
Ask at most 3 questions:
1. "Which company, and roughly how big is it? (30 postings means
   different things at 200 heads vs 20,000)"
2. "What decision should this collection feed?"
3. "Any specialty or region I should watch postings for?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Show a 3-bullet search plan first: posting sources, sentiment
   sources, leadership-move sources. Continue unless revised.
2. Sweep in this order: job postings by specialty and region
   (volume, seniority, named technologies), leadership arrivals
   and exits, employee sentiment on review sites and forums,
   alumni flows between [TARGET] and your company, exec
   conference-circuit presence.
3. Log every signal in the Signal Inventory: what was observed,
   source URL with date, Fact / Inference / Assumption label, the
   inference chain it supports, and the artifact it feeds.
4. Run the compendium's HUMINT inference chains explicitly: a
   hiring surge in one specialty (30+ postings in a quarter,
   scaled to company size) = building a capability, not a feature;
   regional specialist roles in a new [GEOGRAPHY] = expansion
   pre-announcement; postings naming specific technologies =
   confirmed stack choices and integration intel; a senior
   product/tech exit within 6 months of a strategy announcement =
   the strategy is in trouble; your alumni landing at [TARGET] =
   assume they know your playbook; reviews mentioning pivot,
   reorg, or leadership churn = roughly 2 quarters of internal
   distraction = your window.
5. Normalize posting counts against company size and hiring
   baseline before calling anything a surge; a surge is a
   deviation, not a number.
6. Frame the win/loss section: the 3-5 questions your team should
   ask in the next round of win/loss and churned-customer
   interviews to test what this sweep suggests — and mark win/loss
   as the ground-truth gap fusion should weight until those
   interviews exist.
7. Keep the schema stable so run N and N+1 are diffable; if a
   prior sweep is in session, lead with the delta.

## Pedagogic Notes:
- Reading job boards as strategy announcements teaches PMs that
  headcount is the most honest press release a company publishes.
- Normalizing surges against baseline builds statistical hygiene:
  a number is only a signal relative to what normal looks like.
- Framing win/loss questions instead of inventing answers teaches
  the boundary between open-source collection and fieldwork only
  humans can do — and keeps the fusion honest about which is
  which.

## Attribution:
Created by Dean Peters (Productside.com). Collection doctrine from
the Competitive Research Compendium in this directory's reference/
shelf, HUMINT discipline.

## Licensing:
MIT License

Date: July 16, 2026
-->

## Purpose

Read one company's people signals and land every signal in a
fusion-ready inventory.
Workflow: **search plan -> postings, moves, sentiment, alumni ->
signal inventory -> inference chains -> win/loss framing -> gaps
and handoffs.**

## Mode

**Just Enough Mode**: strongest signals only, max 5 inference
chains, one-line watch items. **Verbose Mode** only if asked.

This is a collection prompt: it gathers and labels; it does not
verdict. Confidence rating across disciplines belongs to
[all-source-fusion-prompt.md](all-source-fusion-prompt.md).

## Before You Start

Ask at most 3 questions:

1. Which company, and roughly how big?
2. What decision should this collection feed?
3. Any specialty or region to watch postings for?

If unanswered, proceed with labeled assumptions.

## Search Plan First

Show a **3-bullet plan**: posting sources, sentiment sources,
leadership-move sources, and the surge baseline. Continue unless
revised.

## Source + Trust Rules

Real, checkable URLs with dates on every signal. Do not invent
**posting counts, job titles, named hires or exits, review quotes,
or interview findings.** Never fabricate win/loss answers — frame
the questions and mark the gap. Label every signal: **Fact** /
**Inference** / **Assumption**. Public-record collection only: no
pretexting, no soliciting confidential information, no profiling
of private individuals — executives' public professional moves,
not people's private lives.

# HUMINT Collection: [TARGET]

**As-of date:** | **Decision supported:** | **Prior sweep:** [date
or "first run"]

## 1. Signal Inventory (fusion-ready)

| Signal | Source (URL, date) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| [What was observed] | [URL, date] | [F/I/A] | [What it implies] | [Roadmap bet / Battle card / ...] |

## 2. Strongest Inference Chains (max 5, ranked)

- [Signal cluster] -> [inference, labeled] -> [artifact it should
  change, and the move]

## 3. Surge Analysis

- **Baseline:** [normal posting volume, how derived]
- **Deviations:** [specialty, region, seniority — with counts and
  URLs, labeled]
- **Fusion pair flag:** [specialty where a hiring surge should be
  checked against TECHINT patent/paper clusters]

## 4. Win/Loss Framing (ground truth your team must collect)

- [Question 1-5 for the next win/loss or churn interviews, each
  tied to a signal above]
- **Gap flag for fusion:** win/loss unverified as of this run —
  weight org-instability and build-signal stories accordingly
- **When the interviews land:** synthesize them with
  [prompts/win-loss-analysis-prompt.md](../prompts/win-loss-analysis-prompt.md)
  — its confirm/refute ledger closes the loop on this sweep's
  inferences

## 5. Watch Items (single signals, logged only)

- [Signal] — [what would escalate it]

## 6. Collection Gaps and Handoffs

- [Uncovered source type] — [why it was out of reach this run]
- Cross-checks: patent/paper cluster in the flagged specialty ->
  techint-collection; support-strain disambiguation ->
  masint-collection

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Feed this inventory into all-source fusion with the other
   disciplines
2. Run the TECHINT sweep on the flagged specialty to complete the
   fusion pair
3. Package the win/loss questions for your sales team's next
   debrief round
4. Schedule-ready version: save as the baseline the monthly HUMINT
   digest diffs against

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
