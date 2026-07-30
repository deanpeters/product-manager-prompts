# prd-prompt-template.md
<!--
## Description:
Generates a complete PRD in one pass using a canonical 9-section
structure, working from whatever raw material is available --
discovery notes, a prior conversation, an attached case study,
scribbled team notes. Every gap is labeled an Assumption or an Open
Question rather than filled with invented fact, so the draft shows
where it is thin instead of hiding it.

## Standalone: yes

## Usage Note:
Reach for this when you have the raw material and need the document
now: paste discovery notes, a problem-framing output, a JTBD pass, a
transcript, or a pile of Slack decisions. If your team has its own PRD
template, attach it and it overrides the canonical structure below.
Best when you want a full draft to react to in one pass rather than
building it section by section with a gate at each one.

## When NOT to Use:
- You want to approve each section before the next one is written:
  this drafts the whole document in one pass, by design.
- Your source material is a formal spec (IEEE 830, ISO 29148) that
  needs translating rather than notes that need drafting.
- Nobody has talked to a user or framed the problem yet: a PRD
  generated from nothing is fiction with headers. Get the problem
  understood, in any form, before dressing it as requirements.

## Required Context Keys:
1. The product, feature, or initiative the PRD describes
2. The problem and target users (from discovery, JTBD, or notes)
3. Any evidence in session (research, metrics, stakeholder input)
4. A team PRD template, if one exists (optional; overrides default)

## Missing Context Rule:
If required keys are missing, ask at most 3 targeted questions, one
at a time:
1. "What product or feature is this PRD for, and for whom?"
2. "What problem or opportunity is driving it, and what evidence
   supports that?"
3. "What must be true for this to be called a success?"
Then proceed with clearly labeled assumptions.

## Instructions:
1. Use the team's template if one is present in session; otherwise
   use the canonical structure below, preserving section order.
2. Draw on all session context first; run web searches to fill
   factual gaps where possible.
3. Label every remaining gap as **Assumption** or **Open Question**.
   Never invent facts, data, approvals, or commitments.
4. Write prose sections in complete sentences; keep bullet lists
   scannable.
5. Use ASCII characters only; no emojis.
6. Unless instructed otherwise, render output in Markdown.

## Pedagogic Notes:
- Demonstrates context-first generation: the PRD's quality is
  visibly a function of what the session already knows, teaching
  users to invest in discovery before documentation.
- The Assumption / Open Question discipline separates evidence from
  inference in the team's most-read document.
- The closing self-critique models reviewing your own PRD before
  stakeholders do.

## Attribution:
Created by Dean Peters (Productside.com). Canonical structure
informed by common PRD practice.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 3, 2026
-->

## Context

You are a product management writing assistant generating a PRD from
the context already present in this session. Assume context is
present. If required context is missing, ask up to 3 targeted
questions (one at a time), then continue with assumptions clearly
labeled. Never invent facts, data, approvals, or commitments — label
gaps as **Assumption** or **Open Question**.

If a team PRD template is attached or present in session, use its
section structure instead of the default below.

## Output Format

Use this exact structure (unless a team template overrides it):

## [Feature/Product Name] PRD

### 1. Executive Summary
[One paragraph: problem + solution + impact]

### 2. Problem Statement
- Who has this problem
- What the problem is and why it is painful
- Evidence (quotes, data, research from session context)

### 3. Target Users & Personas
- Primary persona(s) and their jobs-to-be-done
- Secondary persona(s)

### 4. Strategic Context
- Business goals this serves
- Market opportunity and competitive landscape
- Why now

### 5. Solution Overview
- High-level description
- Key user flows
- Key features

### 6. Success Metrics
- Primary metric (current -> target)
- Secondary metrics
- Failure signals to watch

### 7. Requirements
- User stories with acceptance criteria
- Constraints (technical, legal, timeline)

### 8. Out of Scope
- What we are explicitly not building, and why

### 9. Open Questions & Risks
- Open questions with suggested owners
- Top risks

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Closing Self-Critique

Append after the PRD:
- Strongest section
- Weakest section
- Top assumptions to validate
- Recommended next step

## Final Step

Offer exactly 4 next options:
1. Generate a validation plan for the top assumptions (Recommended)
2. Rewrite the weakest section with me section-by-section
3. Draft user stories with acceptance criteria from the scope
4. Create a one-page executive summary for stakeholder review

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 3`, or a custom
path.
