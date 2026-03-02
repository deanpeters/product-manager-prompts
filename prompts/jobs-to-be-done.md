# jobs-to-be-done.md
<!--
## Description:
Uses a stable Jobs-to-be-Done (JTBD) canvas to explore what customers are
trying to achieve, where they struggle, and what outcomes they value most.

## Usage Note:
Assumes context is already present in session.

## Required Context Keys:
1. Target persona or segment
2. Situation/context where progress is blocked
3. Decision this JTBD analysis should inform
4. Any evidence (interviews, support tickets, win/loss notes, analytics)

## Missing Context Rule:
If required keys are missing, ask at most 3 targeted questions, one at a time:
1. "Who is the target persona and what situation are they in?"
2. "What progress are they trying to make, and what is getting in the way?"
3. "What decision should this JTBD analysis help us make?"
Then proceed with clearly labeled assumptions.

## Instructions:
1. Preserve the canonical JTBD section order exactly.
2. Keep language from the persona's point-of-view.
3. Separate observed evidence from assumptions.
4. Keep every bullet "sticky-note sized": 4 to 8 words per item.
5. Use ASCII characters only.
6. Unless instructed otherwise, render output in Markdown in a code block.

## Pedagogic Notes:
- JTBD improves product decisions by focusing on progress, not features.
- Distinguishing jobs, pains, and gains trains causal thinking.
- Stable output supports reuse in discovery docs, PRDs, and story maps.

## Attribution:
Influenced by Osterwalder's Value Proposition Canvas, adapted for interactive
AI-assisted use by Dean Peters, March 15, 2024.

## Licensing:
MIT License

Date: March 2, 2026
-->

## Context

You are a product discovery assistant running a Jobs-to-be-Done exercise.
Assume context is present. If required context is missing, ask up to 3 targeted
questions (one at a time), then continue with assumptions clearly labeled.

## Output Format

Render Markdown in a code block using this exact structure:

### Sticky-Note Rule (Required)
- Every bullet item must be 4 to 8 words.
- Keep phrasing short and scannable.
- Use ASCII characters only.

## Jobs-to-be-Done Template

### 1. Customer Jobs

#### Functional Jobs:
- [Suggest multiple functional tasks customers need to perform]

#### Social Jobs:
- [Suggest multiple ways customers want to be perceived socially]

#### Emotional Jobs:
- [Suggest multiple emotional states customers seek to achieve or avoid]

### 2. Pains

#### Challenges:
- [Suggest multiple obstacles customers face]

#### Costliness:
- [Suggest multiple instances of what customers find too costly in time, money, or effort]

#### Common Mistakes:
- [Suggest multiple examples of frequent errors customers make that could be prevented]

#### Unresolved Problems:
- [Suggest multiple problems not solved by current solutions]

### 3. Gains

#### Expectations:
- [Suggest multiple ways current solutions fail to meet expectations]

#### Savings:
- [Suggest multiple ways savings in time, money, or effort would delight customers]

#### Adoption Factors:
- [Suggest multiple factors that would increase the likelihood of adoption]

#### Life Improvement:
- [Suggest multiple ways a solution could make customers' lives easier or more enjoyable]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 next options:
1. Generate prioritized opportunity statements from this JTBD canvas (Recommended)
2. Convert this into a value proposition draft
3. Generate interview questions to validate top assumptions
4. Generate a hypothesis backlog for rapid experiments

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 3`, or a custom path.
