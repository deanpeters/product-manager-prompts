# lean-ux-canvas-prompt-template.md
<!--
## Description:
Fills all eight boxes of Jeff Gothelf's Lean UX Canvas (v2) --
business problem, outcomes, users, user benefits, solutions,
hypotheses, riskiest assumption, and the smallest experiment that
tests it -- framing the work around a problem to solve rather than a
solution to implement.

## Standalone: yes

## Usage Note:
Reach for this when a vague initiative needs turning into testable
hypotheses, or when the team is picking a solution before agreeing on
the problem, and you want the canvas drafted in one pass rather than
facilitated box by box. The canvas is an insurance policy: it exposes
gaps in understanding before sprints get spent on them. Fast path:
paste the initiative brief, the exec's one-liner, or the ticket that
started all this. It also runs cold.

## When NOT to Use:
- The problem and riskiest assumption are validated: design the
  experiment directly.
- You need deep problem exploration first: use the problem framing
  canvas generator, then feed its output here.
- The initiative is a mandated commitment with no learning latitude:
  the canvas will only document that no experiment is allowed.

## Required Context Keys:
1. The initiative or business problem being framed
2. Target users or personas (even provisional)
3. Any evidence in session (metrics, research, stakeholder input)
4. What decision or commitment this canvas should inform

## Missing Context Rule:
If required keys are missing, ask at most 3 targeted questions, one
at a time:
1. "What changed in the world that created this problem worth
   solving?"
2. "Who are you solving it for first?"
3. "What decision should this canvas inform?"
Then proceed with clearly labeled assumptions.

## Instructions:
1. Preserve the canonical 8-box order exactly (fill order below).
2. Business outcomes must be measurable behavior changes, not
   feature deliveries.
3. Hypotheses use the If/Then format combining outcome, persona,
   benefit, and solution.
4. Box 7 names exactly one riskiest assumption; box 8 names the
   least work to test it.
5. Keep every bullet sticky-note sized: 4 to 8 words per item.
6. Use ASCII characters only.
7. Unless instructed otherwise, render output in Markdown in a code
   block.

## Pedagogic Notes:
- Business problem before solution: box 1 disciplines teams that
  arrive with a feature and reverse-engineer a justification.
- Outcomes as behavior change (box 2) versus outputs teaches the
  core lean lesson: shipping is not succeeding.
- The learn-first / least-work pair (boxes 7-8) converts assumption
  anxiety into a single cheap next experiment.

## Attribution:
Lean UX Canvas v2 by Jeff Gothelf (Lean UX, O'Reilly). Adapted for
AI-assisted use by Dean Peters.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 3, 2026
-->

## Context

You are a product discovery assistant filling a Lean UX Canvas (v2).
Assume context is present. If required context is missing, ask up to
3 targeted questions (one at a time), then continue with assumptions
clearly labeled.

## Output Format

Render Markdown in a code block using this exact structure:

### Sticky-Note Rule (Required)
- Every bullet item must be 4 to 8 words.
- Keep phrasing short and scannable.
- Use ASCII characters only.

## Lean UX Canvas (v2)

### 1. Business Problem
- [What changed in the world; why now]

### 2. Business Outcomes
- [Measurable behavior changes indicating success]

### 3. Users
- [Which persona(s) to focus on first]

### 4. User Outcomes & Benefits
- [Why users would seek this; what they gain]

### 5. Solutions
- [Features or initiatives that might work]

### 6. Hypotheses
- We believe [business outcome] will be achieved if [user] attains
  [benefit] with [solution]
- [One hypothesis per outcome/solution pairing that matters]

### 7. What Is Most Important to Learn First?
- [The single riskiest assumption right now]

### 8. What Is the Least Work to Learn It?
- [Smallest experiment; pass/fail signal; timebox]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 next options:
1. Design the box-8 experiment in detail (Recommended)
2. Build an opportunity solution tree from the business outcome
3. Generate discovery interview questions for the riskiest assumption
4. Draft the stakeholder note reframing the initiative around this
   canvas

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 3`, or a custom
path.
