# swot-analysis-prompt.md
<!--
## Description:
Builds an evidence-cited SWOT analysis of a company — yours or a
competitor's — from public sources: strengths and weaknesses from
documented capability and customer voice, opportunities and threats
from market and macro signals. Every entry carries a source URL and
a Fact / Inference / Assumption label, plus the "so what" that most
SWOTs skip.

## Usage Note:
Use for strategy reviews, board prep, partnership evaluation, or as
the competitor-depth companion to the competitive research snapshot.
Works best when session already holds a snapshot, VoC themes, or a
landscape scan — the SWOT then synthesizes instead of re-searching.
Related: porters-five-forces-prompt.md reads the industry's
structure; this reads one company's position within it.

## When NOT to Use:
- Internal-only SWOT from private knowledge: run it as a workshop
  with your team's evidence; this prompt works the public record.
- You need the whole competitor set: snapshot first, SWOT the one
  or two that matter.

## Required Context Keys:
1. The company to analyze (yours or a competitor)
2. The decision this SWOT should support
3. Scope: whole company, or one product line / market

## Missing Context Rule:
Ask at most 3 questions:
1. "Which company, and whole-company or one product line?"
2. "What decision should this support?"
3. "From whose perspective — theirs, or yours competing with them?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Use session research (snapshot, VoC, landscape) as the evidence
   base; search for gaps and freshness only.
2. Otherwise show the search plan (3 bullets) first; continue
   unless revised.
3. Strengths/weaknesses come from documented capability and
   customer voice; opportunities/threats from market, competitor,
   and macro signals. Do not put internal wishes in either.
4. Max 5 entries per quadrant, ranked; every entry labeled with a
   URL where sourced.
5. Never invent financials, customer wins, market share, or
   roadmap claims.
6. End with the crossings (S-O, W-T), because a SWOT without "so
   what" is a parking lot with four sections.

## Pedagogic Notes:
- Sourcing strengths from customer voice rather than the company's
  own marketing teaches the difference between claimed and
  evidenced advantage.
- The quadrant discipline (internal vs external, current vs
  potential) catches the most common SWOT error: opportunities
  that are actually strategies.
- The crossings teach that SWOT is an input to moves, not a
  deliverable.

## Attribution:
Created by Dean Peters (Productside.com). SWOT framework as
standard strategy practice.

## Licensing:
MIT License

Date: July 3, 2026
-->

## Purpose

Build an evidence-cited SWOT of one company.
Workflow: **use or gather evidence -> search plan (if gathering) ->
four labeled quadrants -> crossings -> next-step options.**

## Mode

**Just Enough Mode**: max 5 ranked entries per quadrant, strongest
evidence only. **Verbose Mode** only if asked.

If a competitive snapshot, VoC themes, or landscape scan is in
session, synthesize from it; search only gaps and staleness.

## Before You Start

Ask at most 3 questions:

1. Which company, and whole-company or one product line?
2. What decision should this support?
3. From whose perspective — theirs, or yours competing with them?

If unanswered, proceed with labeled assumptions.

## Search Plan First (when researching fresh)

Show a **3-bullet plan**: source sweep (filings, reviews, press,
pricing pages, hiring signals), how internal vs external evidence
will be separated, and how facts will be split from inference.
Continue unless revised.

## Source + Trust Rules

Real, checkable URLs with dates. Do not invent **financials,
customer wins, market share, product claims, or roadmap items.**
Label every entry: **Fact** / **Inference** / **Assumption**.
Quadrant discipline: S and W are internal and current; O and T are
external; an "opportunity" that requires them to act is a strategy,
not an opportunity — flag it.

# SWOT: [Company / Scope]

**As-of date:** | **Decision supported:** | **Perspective:**

## 1. Strengths (internal, evidenced)

- [Entry] — [evidence: URL, date] — [Fact/Inference]
- [Max 5, ranked by defensibility]

## 2. Weaknesses (internal, evidenced)

- [Entry — customer voice weighs heaviest here] — [URL] — [label]
- [Max 5, ranked by exploitability]

## 3. Opportunities (external)

- [Entry — market/macro signal] — [URL] — [label]
- [Max 5, ranked by fit to their strengths]

## 4. Threats (external)

- [Entry — competitor/regulatory/technology signal] — [URL] — [label]
- [Max 5, ranked by likelihood x damage]

## 5. The Crossings (the "so what")

- **S-O (attack):** [strength that unlocks which opportunity —
  1-2 moves, labeled Inference]
- **W-T (exposure):** [weakness a threat will find first — 1-2
  risks, labeled Inference]
- **For your decision:** [what this SWOT says about the decision
  named above, in 2 sentences]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Run the W-T exposure into a battle card or risk plan
2. SWOT a second company for side-by-side comparison
3. Feed the crossings into a positioning statement
4. Schedule-ready version: which entries should a quarterly re-run
   watch?

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
