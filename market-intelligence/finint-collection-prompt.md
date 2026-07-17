# finint-collection-prompt.md
<!--
## Description:
Runs a FININT (Financial Intelligence) collection sweep on a target
company: public filings, earnings-call language, procurement and
government-spend records, entity registrations, competition and
state-aid cases, and sovereign or state capital. Every signal lands
in a fusion-ready inventory with a source URL, date, evidence
label, and the inference chain it supports. The forensic
accountant's discipline: companies lie in press releases; they lie
less in filings, because lying there is a felony.

## Usage Note:
One of seven discipline collection prompts feeding
all-source-fusion-prompt.md; doctrine in
reference/competitive-research-compendium.md (FININT discipline).
For quarterly diffing of one company's executive language, hand off
to earnings-executive-signal-refresh-prompt.md — this prompt owns
the discipline-wide sweep: filings, money flows, procurement, and
what the numbers say the strategy is. For EU and MENA procurement
and registry sources, load
reference/regional-source-overlays-eu-mena.md.

## When NOT to Use:
- You only need the quarterly exec-language diff: run the earnings
  refresh directly.
- The target is private with a thin public record: collect what
  exists (incorporations, procurement, funding), label the gaps,
  and lean on the other disciplines.
- You need market sizing math: the capture-rate output here feeds
  tam-sam-som-analysis; run that for the full recipe.

## Required Context Keys:
1. The [TARGET] company
2. The [DECISION] this collection will feed
3. The [GEOGRAPHY] in scope (drives which registries, regulators,
   and procurement platforms apply)

## Missing Context Rule:
Ask at most 3 questions:
1. "Which company, and is it public, private, or state-backed?"
2. "What decision should this collection feed?"
3. "Which countries are in scope — that decides which registries
   and procurement portals I check?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Show a 3-bullet search plan first: filing sources for the
   [GEOGRAPHY], earnings materials, procurement platforms.
   Continue unless revised.
2. Sweep in this order: public filings (annual/quarterly reports,
   registry records), earnings calls and IR materials, procurement
   and government-spend records, new entity registrations and
   subsidiaries, competition/antitrust/state-aid cases, sovereign
   and state capital involvement.
3. Log every signal in the Signal Inventory: what was observed,
   source URL with date, Fact / Inference / Assumption label, the
   inference chain it supports, and the artifact it feeds.
4. Run the compendium's FININT inference chains explicitly:
   year-over-year Risk Factors changes = what genuinely scares
   them; segment reporting restructure = strategic reprioritization;
   earnings Q&A dodges = soft spot to probe in positioning; new
   entities in a [GEOGRAPHY] = market entry before any announcement;
   deferred revenue trends = actual vs stated momentum; merger
   filings = market definitions from their own lawyers; contract
   modifications expanding incumbent scope = locked-in account;
   sovereign or state-aid backing = their runway math changed,
   discount-pressure plays will not work; Prior Information Notices
   = tenders telegraphed 3-24 months out.
5. Compute the capture-rate reality check where possible: reported
   revenue divided by claimed customer count = deal size sanity
   number for SOM work; label the arithmetic and its inputs.
6. Money is the commitment test for every other discipline: mark
   which OSINT-visible announcements this sweep does or does not
   corroborate with funding, awards, or filings.
7. Keep the schema stable so run N and N+1 are diffable; if a
   prior sweep is in session, lead with the delta.

## Pedagogic Notes:
- Reading Risk Factors diffs teaches PMs to let a company's own
  lawyers name its fears instead of guessing from headlines.
- The capture-rate arithmetic (revenue / claimed customers) builds
  the habit of deflating vanity metrics with filed numbers.
- Treating FININT as the corroboration layer teaches the
  ambition-vs-commitment distinction: talk is OSINT; money is
  commitment.

## Attribution:
Created by Dean Peters (Productside.com). Collection doctrine from
the Competitive Research Compendium in this directory's reference/
shelf, FININT discipline.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 16, 2026
-->

## Purpose

Follow the money on one company and land every signal in a
fusion-ready inventory.
Workflow: **search plan -> filings, calls, procurement, capital ->
signal inventory -> inference chains -> capture-rate check -> gaps
and handoffs.**

## Mode

**Just Enough Mode**: strongest signals only, max 5 inference
chains, one-line watch items. **Verbose Mode** only if asked.

This is a collection prompt: it gathers and labels; it does not
verdict. Confidence rating across disciplines belongs to
[all-source-fusion-prompt.md](all-source-fusion-prompt.md).

## Before You Start

Ask at most 3 questions:

1. Which company — public, private, or state-backed?
2. What decision should this collection feed?
3. Which countries are in scope?

If unanswered, proceed with labeled assumptions.

## Search Plan First

Show a **3-bullet plan**: filing and registry sources for the
[GEOGRAPHY], earnings materials, procurement platforms (for EU and
MENA, per the regional overlay). Continue unless revised.

## Source + Trust Rules

Real, checkable URLs with dates on every signal. Do not invent
**revenue figures, customer counts, filing language, contract
awards, funding amounts, or case citations.** Label every signal:
**Fact** / **Inference** / **Assumption**. Show the arithmetic on
any derived number. Record whether amounts are announced budgets,
approved budgets, committed financing, tender values, or awarded
contracts — five different numbers wearing the same headline.

# FININT Collection: [TARGET]

**As-of date:** | **Decision supported:** | **Prior sweep:** [date
or "first run"]

## 1. Signal Inventory (fusion-ready)

| Signal | Source (URL, date) | Label | Inference chain | Feeds |
|---|---|---|---|---|
| [What was observed] | [URL, date] | [F/I/A] | [What it implies] | [Battle card / SOM / Account targeting / ...] |

## 2. Strongest Inference Chains (max 5, ranked)

- [Signal cluster] -> [inference, labeled] -> [artifact it should
  change, and the move]

## 3. Capture-Rate Reality Check

- Reported revenue: [figure, URL, period]
- Claimed customers: [figure, URL, as-of]
- Implied deal size: [arithmetic shown] — [labeled Inference;
  feeds SOM capture rates in tam-sam-som-analysis]

## 4. Corroboration Ledger

- [Announcement or OSINT claim] — [corroborated by: filing /
  award / funding, with URL — or "intent only, no money visible"]

## 5. Watch Items (single signals, logged only)

- [Signal] — [what would escalate it]

## 6. Collection Gaps and Handoffs

- [Uncovered source type] — [why it was out of reach this run]
- Deep dives: quarterly exec-language diff ->
  earnings-executive-signal-refresh; sizing math ->
  tam-sam-som-analysis; regional sources -> reference overlay

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Feed this inventory into all-source fusion with the other
   disciplines
2. Run the capture rate into the TAM/SAM/SOM analysis
3. Turn the Q&A dodges and stress signals into battle card plays
4. Schedule-ready version: save as the baseline the next quarterly
   sweep diffs against

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
