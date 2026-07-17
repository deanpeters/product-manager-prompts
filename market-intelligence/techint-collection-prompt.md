# techint-collection-prompt.md
<!--
## Description:
Runs a TECHINT (Technical Intelligence) collection sweep on a
target company: patent and trademark filings, technographics,
public changelogs and API-doc diffs, repo activity, standards-body
participation, funded research, and academic preprints. Every
signal lands in a fusion-ready inventory with a source URL, date,
evidence label, and the inference chain it supports. The patent
examiner's discipline: R&D leaves fingerprints 12-18 months before
products ship.

## Usage Note:
One of seven discipline collection prompts feeding
all-source-fusion-prompt.md; doctrine in
reference/competitive-research-compendium.md (TECHINT discipline).
The longest-range discipline on the collection floor: research and
standards signals lead product by 12-48 months, patents by 12-18,
trademarks by 6-12, API-doc diffs by weeks. Primary feed for
roadmap bets — where to accelerate versus concede. For EU research
and standards sources (CORDIS, Espacenet, CEN/CENELEC/ETSI), load
reference/regional-source-overlays-eu-mena.md.

## When NOT to Use:
- You need legal patent analysis (validity, infringement, freedom
  to operate): that is counsel's work; this reads direction, not
  legal exposure.
- The target ships no technology (pure services): TECHINT will run
  dry; lean on FININT and HUMINT.
- You need this week's shipped changes: SIGINT's web diffs are the
  fresher layer; TECHINT reads what has not shipped yet.

## Required Context Keys:
1. The [TARGET] company
2. The [DECISION] this collection will feed (usually a roadmap bet)
3. The [CAPABILITY] you suspect, if any (focuses the patent-class
   and preprint search)

## Missing Context Rule:
Ask at most 3 questions:
1. "Which company, and which technology area matters most to you?"
2. "What roadmap decision should this collection feed?"
3. "Do you suspect a specific move, or is this an open scan?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Show a 3-bullet search plan first: patent/trademark databases,
   technical exhaust (changelogs, API docs, repos), research and
   standards sources. Continue unless revised.
2. Sweep in this order: patent filings by classification (last
   24 months), trademark filings, technographics of [TARGET] and
   its customers, public changelogs / API docs / status pages /
   repo activity, standards-body work programs, funded research
   participation, academic preprints by [TARGET]-affiliated
   authors.
3. Log every signal in the Signal Inventory: what was observed,
   source URL with date, Fact / Inference / Assumption label, the
   inference chain it supports, and the artifact it feeds.
4. Run the compendium's TECHINT inference chains explicitly: 5+
   filings in one classification in 12 months = committed bet, not
   exploration; repeating inventor names = the actual team behind
   the initiative, track their talks and moves; trademark filing =
   launch inside 6-12 months; trademark after a funded project
   completes = commercialization underway; repeated consortium
   appearances = the long-range bet; pilot sites named in
   deliverables = likely launch customers; chairing a standards
   committee = they intend to shape the rules, not play by them;
   preprint cluster = R&D direction 6-24 months before patents;
   author affiliation shifting from university to [TARGET] = they
   hired the lab, not just the idea; new API endpoints for an
   unreleased capability = beta running now; new SDKs and
   scaffolding = developer platform play; prospect tech stacks =
   who can actually buy you (SAM refinement).
5. Flag the strongest fusion pair for HUMINT: a preprint or patent
   cluster plus a hiring surge in the same specialty is one of the
   highest-confidence signals available — name it for the fusion
   run.
6. Date every signal and state its typical lead time, so the
   roadmap implication carries a clock, not just a direction.
7. Keep the schema stable so run N and N+1 are diffable; if a
   prior sweep is in session, lead with the delta.

## Pedagogic Notes:
- Reading patent clusters instead of single filings teaches the
  difference between a company exploring and a company committing.
- Tracking inventor and author names builds the habit of following
  people, not just documents — teams ship strategies; filings only
  record them.
- Attaching lead times to signals turns competitive anxiety into a
  countdown clock a roadmap can actually plan against.

## Attribution:
Created by Dean Peters (Productside.com). Collection doctrine from
the Competitive Research Compendium in this directory's reference/
shelf, TECHINT discipline.

## Licensing:
MIT License

Date: July 16, 2026
-->

## Purpose

Read one company's R&D fingerprints before their product ships and
land every signal in a fusion-ready inventory.
Workflow: **search plan -> patents, trademarks, exhaust, research,
standards -> signal inventory -> inference chains with lead times
-> gaps and handoffs.**

## Mode

**Just Enough Mode**: strongest signals only, max 5 inference
chains, one-line watch items. **Verbose Mode** only if asked.

This is a collection prompt: it gathers and labels; it does not
verdict. Confidence rating across disciplines belongs to
[all-source-fusion-prompt.md](all-source-fusion-prompt.md).

## Before You Start

Ask at most 3 questions:

1. Which company, and which technology area matters most?
2. What roadmap decision should this collection feed?
3. Specific suspected move, or open scan?

If unanswered, proceed with labeled assumptions.

## Search Plan First

Show a **3-bullet plan**: patent/trademark sources, technical
exhaust (changelogs, API docs, repos, technographics), research
and standards sources (for EU, per the regional overlay). Continue
unless revised.

## Source + Trust Rules

Real, checkable URLs with dates on every signal. Do not invent
**patent counts, filing classifications, trademark records,
inventor names, paper titles, consortium memberships, or changelog
entries.** Label every signal: **Fact** / **Inference** /
**Assumption**. A patent describes what was protected, not what
will ship — the inference chain, not the document, carries the
roadmap claim, and it is always labeled Inference.

# TECHINT Collection: [TARGET]

**As-of date:** | **Decision supported:** | **Prior sweep:** [date
or "first run"]

## 1. Signal Inventory (fusion-ready)

| Signal | Source (URL, date) | Label | Inference chain | Lead time | Feeds |
|---|---|---|---|---|---|
| [What was observed] | [URL, date] | [F/I/A] | [What it implies] | [est. months] | [Roadmap bet / SAM / Battle card / ...] |

## 2. Strongest Inference Chains (max 5, ranked)

- [Signal cluster] -> [inference, labeled] -> [roadmap implication
  with countdown, and the accelerate/concede call it informs]

## 3. The People Trail

- **Repeating inventors/authors:** [names, filings/papers, URLs]
- **Affiliation shifts:** [university -> company moves, sourced]
- **Fusion pair flag:** [specialty where a paper/patent cluster
  should be checked against HUMINT hiring data]

## 4. Watch Items (single signals, logged only)

- [Signal] — [what would escalate it]

## 5. Collection Gaps and Handoffs

- [Uncovered source type] — [why it was out of reach this run]
- Cross-checks: hiring surge in the same specialty ->
  humint-collection; launch staging signs -> sigint-collection;
  regional research sources -> reference overlay

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Feed this inventory into all-source fusion with the other
   disciplines
2. Run the HUMINT sweep on the flagged specialty to complete the
   fusion pair
3. Turn the countdown clocks into roadmap accelerate/concede
   recommendations
4. Schedule-ready version: save as the baseline the quarterly
   TECHINT pass diffs against

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
