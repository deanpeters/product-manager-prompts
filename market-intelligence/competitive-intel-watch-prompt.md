# competitive-intel-watch-prompt.md
<!--
## Description:
A scheduled competitive intelligence delta monitor. Given a previous
Competitive Research Snapshot and a competitor list, sweeps for
material shifts since the last run and reports only what changed:
a cited changelog plus flags for which battle card or positioning
sections now need updating. Designed to run unattended on a loop or
schedule.

## Usage Note:
Run competitive-research-snapshot-prompt.md once to create the
baseline, then run this on a cadence (weekly to quarterly) with the
prior snapshot pasted or attached. Governing criterion: material
shift — a change a sales rep or roadmap owner would act on. If no
prior snapshot exists, this prompt falls back to producing one.
Companion: workshops/battle-card-workshop.md consumes
the update flags.

## When NOT to Use:
- First run with no baseline: use the snapshot prompt (or let this
  prompt's fallback produce the baseline; the delta value starts on
  run two).
- You need a full landscape re-think (new segment, pivot): re-run
  the snapshot from scratch instead of diffing a stale scope.

## Required Context Keys:
1. Previous Competitive Research Snapshot (pasted or attached)
2. Competitor list (defaults to those in the snapshot)
3. Materiality bar, if the default needs tightening or loosening

## Missing Context Rule:
Ask at most 2 questions:
1. "Do you have the previous snapshot to paste, or should I create
   a baseline?"
2. "Anything specific you are watching for this cycle?"
If unanswered, proceed: baseline mode if no snapshot, default
materiality bar otherwise.

## Instructions:
1. Read the prior snapshot fully before searching; diff against it,
   do not regenerate it.
2. Show the search plan (3 bullets) before researching; continue
   unless revised.
3. Report only material shifts: pricing or packaging changes,
   launches and deprecations, positioning changes, leadership moves,
   funding or M&A, major customer wins/losses, credible roadmap
   signals. Cosmetic changes are noise; say "no material change"
   when true — an empty changelog is a valid, useful result.
4. Never invent competitors, features, pricing, market share,
   customer wins, roadmap items, or product claims.
5. Label key points Fact, Inference, or Assumption; real checkable
   URLs with dates for every claimed change.
6. Just Enough Mode: short bullets, strongest findings only.
7. Keep the output schema exactly; runs must be diffable.

## Pedagogic Notes:
- Delta discipline teaches that a watch reports change, not state;
  regenerating the same report weekly is theater.
- The materiality bar teaches signal triage: a watch that cries
  wolf gets ignored by cycle three.
- Update flags close the loop from intelligence to action: research
  is only done when it names the artifact it changes.

## Attribution:
Created by Dean Peters (Productside.com). Builds on the Competitive
Research Snapshot workflow's schema and evidence rules.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 3, 2026
-->

## Purpose

Monitor a competitive landscape for **material shifts** since the
last run. Diff the world against the previous snapshot; report only
what changed, with evidence; flag which downstream artifacts need
updating.

## Mode

Baseline mode: if no previous snapshot is provided, produce one using
the Competitive Research Snapshot structure and stop — the delta
value begins next run.

Delta mode (default when a snapshot is provided): diff and report.

## Before You Start

Ask at most 2 questions:

1. Do you have the previous snapshot, or should I create a baseline?
2. Anything specific you are watching for this cycle?

If unanswered, proceed with labeled assumptions.

## Search Plan First

Before researching, show a **3-bullet plan**: what you will check per
competitor, source types, and how you will separate facts from
inferences. Then continue unless asked to revise.

## Materiality Bar

Report a change only if a sales rep, pricing owner, or roadmap owner
would plausibly act on it:

- Pricing or packaging changes
- Product launches, major features, deprecations
- Positioning or messaging shifts
- Leadership changes, funding, M&A
- Major customer wins or losses
- Credible roadmap signals (hiring patterns, announcements)

Below the bar: cosmetic site changes, routine content marketing,
minor releases. When nothing clears the bar, say so plainly.

## Source + Trust Rules

Real, checkable URLs with dates. Mixed sources: company sites,
pricing pages, release notes, press, investor materials, credible
news, review sites, job postings.
Do not invent competitors, features, pricing, market share, customer
wins, roadmap items, or product claims.
Label: **Fact** (source-supported), **Inference** (evidence-based
interpretation), **Assumption** (working guess).

# Competitive Watch Report

## 1. Run Header

**Scope (from prior snapshot):**
**Prior snapshot date:**
**This run date:**
**Competitors checked:**

## 2. Changelog (Material Shifts Only)

For each material shift:

### [Competitor] — [4 to 8 word change summary]
- **What changed:** [1-2 bullets, labeled Fact/Inference]
- **Evidence:** [URL, date]
- **So what:** [why it clears the materiality bar]
- **Confidence:** [high / medium / low]

If nothing cleared the bar: "No material shifts this cycle." List
anything on the watchlist for next run.

## 3. Update Flags

| Downstream artifact | Sections needing update | Driven by |
|---|---|---|
| Battle card | | |
| Positioning statement | | |
| Pricing/packaging analysis | | |
| Roadmap assumptions | | |

Only rows with real updates; omit the rest.

## 4. Watchlist for Next Run

- [Signals below the bar but trending]
- [Open questions this run could not resolve]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Update the battle card sections flagged above
2. Deep-dive the most significant change
3. Produce the refreshed full snapshot (new baseline)
4. Adjust the materiality bar or competitor list for next run

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
