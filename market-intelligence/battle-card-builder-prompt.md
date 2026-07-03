# battle-card-builder-prompt.md
<!--
## Description:
Researches and drafts a competitive battle card autonomously: given
your product and one competitor, the AI does the fieldwork — pricing
pages, reviews, release notes, customer stories — and produces a
field-action card with a source URL and Fact / Inference /
Assumption label on every claim. The evidence-first sibling of the
facilitated battle card workshop.

## Usage Note:
Use when you know the competitor and want the card built from
public evidence rather than from a facilitated session. Feeds from
competitive-research-snapshot-prompt.md or
competitive-intel-watch-prompt.md output when present in session
(uses it instead of re-researching). Governing criterion: material
shift — the card is a field-action artifact a rep opens mid-deal,
not a research report.
Companion: workshops/battle-card-workshop.md facilitates the card
from your knowledge; this builds it from the world's.

## When NOT to Use:
- You hold rich internal win/loss knowledge the public web lacks:
  use the workshop and bring your evidence.
- You need the whole competitor set compared: run the competitive
  research snapshot first, then build cards for the two that matter.

## Required Context Keys:
1. Your product and its primary differentiation
2. The competitor the card targets
3. The deal context (segment, buyer, common objections), if known

## Missing Context Rule:
Ask at most 3 questions:
1. "Your product, and the one competitor this card targets?"
2. "What segment and buyer do these deals involve?"
3. "What objection or loss reason triggered this card?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Check session for a competitive snapshot or watch report; use it
   as the evidence base and only search for gaps and freshness.
2. Otherwise, show the search plan (3 bullets) before researching;
   continue unless revised.
3. Every claim in the card carries a source URL with date and a
   Fact / Inference / Assumption label.
4. Never invent features, pricing, market share, customer wins,
   roadmap items, or quotes.
5. Just Enough Mode: the card must fit a rep's 30 seconds; depth
   goes in the appendix.
6. Keep the card schema exactly; cards are diffable across runs.

## Pedagogic Notes:
- Shows the same artifact in two interaction modes (workshop =
  facilitation, this = investigation), teaching that the mode
  choice depends on where the evidence lives.
- Per-claim labeling teaches that most battle cards in the wild are
  unlabeled inference — and what it costs a rep when one is wrong.
- The trap-question section teaches offense as evidence work:
  questions are only safe to ask when you know the documented
  answer.

## Attribution:
Created by Dean Peters (Productside.com). Battle card structure per
the battle card workshop's field-action criterion.

## Licensing:
MIT License

Date: July 3, 2026
-->

## Purpose

Build a field-action competitive battle card from public evidence.
Workflow: **use or gather evidence -> search plan (if gathering) ->
draft card with per-claim labels -> appendix -> next-step options.**

## Mode

**Just Enough Mode**: the card fits a rep's 30 seconds; anything
deeper goes to the appendix. **Verbose Mode** only if asked.

If a competitive snapshot or watch report is in session, use it as
the evidence base; search only for gaps and anything older than one
quarter.

## Before You Start

Ask at most 3 questions:

1. Your product, and the one competitor this card targets?
2. What segment and buyer do these deals involve?
3. What objection or loss reason triggered this card?

If unanswered, proceed with labeled assumptions.

## Search Plan First (when researching fresh)

Show a **3-bullet plan**: what you'll check (pricing pages, release
notes, reviews, customer stories, comparison content), source types,
and how facts will be separated from inference. Continue unless
revised.

## Source + Trust Rules

Real, checkable URLs with dates. Do not invent **features, pricing,
market share, customer wins, roadmap items, or quotes.**
Label every claim: **Fact** / **Inference** / **Assumption**.

# Battle Card: [Your Product] vs [Competitor]

**As-of date:** | **Deal context:** [segment, buyer]

## 1. Thirty-Second Read

- **They win when:** [1-2 bullets, labeled]
- **We win when:** [1-2 bullets, labeled]
- **The one thing to say:** [a single defensible sentence]

## 2. Say This

- [Talking point] — [evidence: URL, date, label]
- [Max 4; every one sourced]

## 3. Ask This (trap questions)

- "[Question whose documented answer favors us]" — [the documented
  answer: URL, label]
- [Max 3; never ask what you cannot evidence]

## 4. Watch Out For

- [Their strength a rep should not walk into] — [URL, label]
- [Their likely counter to our pitch] — [Inference, basis]

## 5. Pricing & Packaging Snapshot

- [Their tiers/pricing as published] — [URL, as-of date]
- [Where "contact sales" hides the number] — [labeled]

## 6. Do Not Say

- [Claims we cannot evidence, or that invite a counter]

## Appendix: Evidence Table

| Claim | Label | Source | Date |
|---|---|---|---|

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Pressure-test the card: role-play the competitor's rep against it
2. Build the card for a second competitor
3. Set up the competitive watch to keep this card current
4. Compress to a one-screen mobile version for the field

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 3`, `Verbose Mode`,
or a custom path.
