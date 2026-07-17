# ansoff-matrix-prompt.md
<!--
## Description:
Maps a company's growth options across the Ansoff Matrix with
evidence per quadrant: market penetration, market development,
product development, and diversification — each quadrant populated
with researched candidate moves, the documented signals supporting
them, risk ratings that respect the matrix's risk gradient, and a
recommended sequence.

## Usage Note:
Use when the growth question is on the table: where does the next
tranche of growth come from, and at what risk? Works best with a
landscape scan, five-forces read, or company research in session —
the matrix then organizes evidence instead of brainstorming in a
vacuum. This is a research prompt: candidate moves come from
documented signals (adjacent segments actually underserved,
competitor moves, expressed demand), not from wishful whiteboarding.

## When NOT to Use:
- Feature-level prioritization: this is portfolio altitude; use the
  feature-investment workshop for a single build decision.
- No growth mandate or capacity: an options map without an owner is
  a poster.

## Required Context Keys:
1. The company or product line seeking growth
2. Current core: who is served, with what, at what scale
3. Constraints (capital, capability, appetite), if known

## Missing Context Rule:
Ask at most 3 questions:
1. "Which company or product line, and what is its current core?"
2. "What growth outcome and horizon is on the table?"
3. "Any constraints — capital, capability, risk appetite?"
If unanswered, proceed with labeled assumptions.

## Instructions:
1. Use session research (landscape, five forces, company intel) as
   the evidence base; otherwise show the search plan (3 bullets)
   first and continue unless revised.
2. Populate each quadrant with 2-3 candidate moves, each backed by
   a documented signal — underserved segment data, expressed
   demand, competitor precedent, capability evidence — with URL and
   Fact / Inference / Assumption label.
3. Respect the risk gradient: penetration < market development /
   product development < diversification. A diversification move
   rated "low risk" needs extraordinary evidence.
4. Never invent market sizes, adoption data, or competitor results;
   where sizing matters, flag it for the TAM/SAM/SOM prompt.
5. Close with a recommended sequence and the assumption that, if
   wrong, invalidates it.

## Pedagogic Notes:
- Evidence-per-quadrant converts Ansoff from a brainstorm grid into
  a research instrument: every move must answer "what signal says
  this demand exists?"
- The risk gradient teaches why diversification proposals deserve
  the heaviest evidence burden — and usually arrive with the
  lightest.
- The sequencing close teaches that growth options compound:
  penetration funds development; diversification bets the funding.

## Attribution:
Created by Dean Peters (Productside.com). Framework: H. Igor
Ansoff, "Strategies for Diversification" (HBR, 1957).

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 3, 2026
-->

## Purpose

Map evidence-backed growth options across the Ansoff Matrix.
Workflow: **use or gather evidence -> four quadrants with signals ->
risk-rated sequence -> next-step options.**

## Mode

**Just Enough Mode**: 2-3 candidate moves per quadrant, strongest
signals only. **Verbose Mode** only if asked. If a landscape scan,
five-forces read, or company research is in session, build on it.

## Before You Start

Ask at most 3 questions:

1. Which company or product line, and what is its current core?
2. What growth outcome and horizon is on the table?
3. Any constraints — capital, capability, risk appetite?

If unanswered, proceed with labeled assumptions.

## Search Plan First (when researching fresh)

Show a **3-bullet plan**: what you'll search per quadrant (segment
data, expressed demand, competitor precedents, capability signals),
source types, fact/inference separation. Continue unless revised.

## Source + Trust Rules

Real, checkable URLs with dates. Do not invent **market sizes,
adoption data, competitor results, or demand claims.** Where sizing
matters, flag it for market-intelligence/tam-sam-som-analysis-prompt.md
rather than guessing.
Label every signal: **Fact** / **Inference** / **Assumption**.

# Ansoff Growth Options: [Company / Product Line]

**As-of date:** | **Current core:** | **Growth outcome sought:**

## 1. Market Penetration (existing product, existing market — lowest risk)

- **[Candidate move]** — signal: [evidence, URL, label] — risk: [low/med/high, why]
- [2-3 moves]

## 2. Market Development (existing product, new market)

- **[Candidate move: segment, geography, or channel]** — signal:
  [evidence of underserved demand, URL, label] — risk: [rating, why]
- [2-3 moves]

## 3. Product Development (new product, existing market)

- **[Candidate move]** — signal: [expressed demand, VoC theme,
  competitor precedent, URL, label] — risk: [rating, why]
- [2-3 moves]

## 4. Diversification (new product, new market — highest risk)

- **[Candidate move]** — signal: [the extraordinary evidence this
  quadrant requires, URL, label] — risk: [rating, why]
- [1-2 moves; an empty quadrant is an acceptable answer]

## 5. Recommended Sequence (the "so what")

- **First:** [move] — because [evidence strength + funding logic]
- **Then:** [move] — funded/de-risked by the first
- **Not yet:** [the tempting move and why the evidence says wait]
- **The assumption that breaks this sequence:** [one line]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 options:

1. Size the top move with TAM/SAM/SOM (Recommended)
2. Pressure-test the sequence with a premortem
3. Deep-dive the diversification quadrant's evidence
4. Convert the first move into an opportunity solution tree

Ask me to reply with `1`, `2`, `3`, `4`, `1 and 2`, `Verbose Mode`,
or a custom path.
