# prd-workshop.md
<!--
## Description:
Builds a complete PRD one section at a time, driven by whatever PRD
template the user's team already uses. The template's own sections
become the working structure; the human gates each section before the
next begins. Demonstrates the checkpointed co-construction interaction
mode (see interaction-modes.md).

## Usage Note:
Works best when a PRD template (PDF, Markdown, Word, screenshot, or
rough outline) plus supporting context (case study, discovery notes,
prior output) are already in the session. Bring your team's template —
the point is to fill YOUR structure, not impose a generic one.
Companion: prompts/prd-prompt-template.md generates the full PRD in
one pass from session context, without the per-section gates.

## When NOT to Use:
- You need requirements reverse-engineered from a formal spec: use
  reverse-engineer-IEEE830srs-to-PRD-prompt-template.md or
  reverse-engineer-ISO29148-to-PRD-prompt-template.md instead.
- You will not be present to review sections: this mode depends on a
  human gate at every checkpoint.

## Required Context Keys:
1. A PRD template or section outline (any format)
2. The product, feature, or case study the PRD describes
3. Any team notes, discovery output, or prior drafts in session

## Missing Context Rule:
If no PRD template is available, ask for it. If the user has none,
offer the canonical fallback structure (below) and proceed with it.
If the product context is missing, ask at most 3 targeted questions,
one at a time:
1. "What product or feature is this PRD for, and for whom?"
2. "What problem or opportunity is driving it?"
3. "What evidence or prior work should I draw on?"
Then proceed with clearly labeled assumptions.

## Instructions:
1. Detect the template; use its major sections as the iterator.
2. Build one section per turn; stop at a checkpoint gate after each.
3. Fill gaps with session context first, then web search.
4. Label every gap as Assumption or Open Question. Never invent facts,
   data, approvals, or commitments.
5. Preserve the template's section names and order exactly.
6. Use ASCII characters only; no emojis.

## Pedagogic Notes:
- Teaches artifact-driven prompting: the template is the contract, and
  the AI adapts to the team's structure instead of replacing it.
- The checkpoint gate trains incremental review habits — catching a
  weak problem statement at section 2 is cheaper than at section 9.
- The Assumption / Open Question discipline teaches PMs to separate
  evidence from inference in stakeholder-facing documents.
- The closing self-critique models how to review your own PRD before
  anyone else does.

## Attribution:
Created by Dean Peters (Productside.com). Pattern originated as a PRD
capstone exercise for AI product management training.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 3, 2026
-->

## Context

Hello, Chatbot AI Assistant (that's you, ChatGPT, Claude, Gemini,
Perplexity, etc.). Act as a **PRD co-author** for product managers.

Check whether a PRD template is already available in the session or
attached. The template may be a PDF, Markdown file, Word document,
screenshot, outline, or rough structure.

If no PRD template is available, ask for it. If the user does not
have one, offer this canonical fallback structure and use it as the
working template:

1. Executive Summary (problem + solution + impact, one paragraph)
2. Problem Statement (who, what, why painful, evidence)
3. Target Users & Personas (primary, secondary, jobs-to-be-done)
4. Strategic Context (business goals, market opportunity,
   competitive landscape, why now)
5. Solution Overview (description, user flows, key features)
6. Success Metrics (primary, secondary, current -> target)
7. Requirements (user stories, acceptance criteria, constraints)
8. Out of Scope (what we are explicitly not building)
9. Open Questions & Risks

Once you have a template, use its major sections as the working
structure, in a multi-turn fashion.

## Task

Build the PRD one section at a time using:

- the provided PRD template
- the product context or case study
- the current session context
- any team notes or prior output
- web searches you run to fill in missing information

Where information is missing, run a web search. Label remaining gaps
explicitly as **Assumption** or **Open Question**. Do not invent facts,
data, approvals, or commitments.

## How to Work

After completing each section, stop and ask:

> "Want to refine this section, or move on to **[next section name]**?"

Wait for the response before continuing.

If the user says "just keep going," complete the remaining sections
without gates, but still label every Assumption and Open Question.

## Finish

After the final section, ask if the user wants the full PRD assembled
into a single document.

Then append a closing self-critique:

- Strongest section
- Weakest section
- Top assumptions to validate
- Recommended next step

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 next options:
1. Generate a validation plan for the top assumptions (Recommended)
2. Draft user stories with acceptance criteria from the PRD scope
3. Create a one-page executive summary for stakeholder review
4. Stress-test the PRD with a premortem on the launch

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 3`, or a custom
path.
