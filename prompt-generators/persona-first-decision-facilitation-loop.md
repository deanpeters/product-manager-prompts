# Persona-First Decision Facilitation Loop (PDF Loop)

<!--
## Description:
Canonical operating model for multi-turn prompt facilitation in this repository.
This defines how to run expert-guidance conversations that reduce user burden,
improve decision quality, and teach transferable prompt-building patterns.

## Usage Note:
Use this when a prompt needs to gather context, offer structured options, and
guide decisions over multiple turns. Especially useful in /prompt-generators and
decision-heavy flows in /storytelling.

## Instructions:
This document is a specification and teaching artifact. Reuse sections, snippets,
and examples when writing or reviewing prompts.

## Attribution:
Authored in collaboration with Dean Peters and Codex, March 2, 2026.

## Licensing:
MIT License

Date: March 2, 2026
-->

## What Is The PDF Loop?

The **Persona-First Decision Facilitation Loop (PDF Loop)** is a conversational pattern for product-management prompts.

It is designed to feel like expert guidance, not a chatbot quiz:
- One targeted question at a time
- Three context-aware options at decision points
- Recommended option first with rationale
- Persona language first, business translation second
- Fast adaptation after each answer
- Decision summary with assumptions and next steps

## Why This Exists

Most prompt experiences fail in one of two ways:
1. **Unstructured drift**: "tell me more..." without decision progress
2. **Form overload**: long questionnaires that push setup labor onto users

The PDF Loop sits in the middle:
- Human and conversational
- Programmatic and reliable
- Decision-forward and pedagogic

## Non-Negotiable Rules

1. **Workload Inversion**
The assistant must do heavy lifting. Ask for minimum viable context, then propose likely scopes/options.

2. **One-Question Turns**
Ask one targeted question. Do not batch multiple questions unless explicitly requested.

3. **Decision Fork Shape**
At each meaningful fork, offer exactly 3 options:
- Option 1 recommended first
- Each option includes short rationale
- User can respond with `1`, `2`, `3`, `1 and 3`, or custom direction

4. **Persona-First Wording**
Frame recommendations in user/persona language first.
Add one-line business translation second when useful.

5. **Progress Visibility**
Show momentum with concise progress updates (example: `Progress: 2/4 core inputs captured`).

6. **Decision Closure**
Summarize what was decided, why, what happens next, and assumptions to validate.

## Where To Use It

Use PDF Loop by default in:
- `/prompt-generators` assets
- Decision-heavy `/storytelling` assets
- Any prompt that requires tradeoffs and sequencing

Do not force PDF Loop when:
- User requests one-shot output
- Task is pure transformation (rewrite, summarize, format)
- Creative ideation is intentionally unconstrained

## Session Lifecycle

### Step 0: Set Expectations
In one short message:
- Goal of the session
- Approximate time
- What the flow will look like

### Step 1: Capture Minimum Context
Ask for smallest set of inputs needed to infer structure.

Good:
- "Who is the customer and what painful moment are they in?"

Bad:
- "Define your full journey map stages, touchpoints, and KPIs."

### Step 2: Propose Scope Options
Assistant proposes 3 candidate scopes based on context.

### Step 3: Run Decision Forks
For each major decision:
- 3 options
- one recommended first
- persona-first language
- optional business translation

### Step 4: Generate Artifact
Produce requested artifact in structured format.

### Step 5: Close The Loop
Include:
- Decisions made
- Assumptions to validate
- 3 (or more) concrete next-step options

## Canonical Decision-Turn Template

```markdown
Based on what you shared, here are the three best paths:

1. [Persona-first option] (Recommended) - [why now]
   Business translation: [optional]
2. [Persona-first option] - [tradeoff]
   Business translation: [optional]
3. [Persona-first option] - [tradeoff]
   Business translation: [optional]

Reply with `1`, `2`, `3`, `1 and 3`, or tell me your own path.
```

## Option Quality Rubric

Every option set should score well on:
- **Context fit**: grounded in what user already said
- **Mutual exclusivity**: distinct enough to choose between
- **Actionability**: clear implication if chosen
- **Tradeoff clarity**: users can see what they gain/lose
- **Language fit**: understandable to persona, not just internal teams

## Anti-Patterns (And Fixes)

### Anti-Pattern: Burden-Shifting Question
"What journey are we mapping?"

Fix:
"Who is the customer, and what painful moment are they in now?"
Then assistant proposes 3 candidate journey scopes.

### Anti-Pattern: Jargon-First Options
"Increase qualified purchase intent."

Fix:
"Help us confidently pick 2-3 options we can both afford."
Business translation can follow.

### Anti-Pattern: No Closure
Artifact generated, no decision summary, no assumptions, no next steps.

Fix:
Always end with Decisions + Assumptions + Next-step options.

## Worked Example 1: Customer Journey Mapping

### Input (minimal)
"Fred, father of 3, overwhelmed by SUV/minivan choices and affordability."

### Assistant Proposal
1. Discovery to shortlist (Recommended)
2. Budget and financing confidence
3. Household decision alignment

### Persona-First Outcome Option Example
1. "Help us pick 2-3 safe options we both can afford." (Recommended)
   Business translation: increase qualified purchase intent.

## Worked Example 2: Positioning

### Input (minimal)
"Ops managers are buried in outage noise and cannot prioritize incidents."

### Assistant Proposal
1. Position around decision confidence under pressure (Recommended)
2. Position around reduced alert volume
3. Position around collaboration visibility

### Persona-First Differentiation Example
1. "Know what to fix first in minutes, not hours." (Recommended)
   Business translation: faster time-to-value and lower churn risk.

## Worked Example 3: Proto-Persona

### Input (minimal)
"First-time team lead trying to run weekly 1:1s effectively."

### Assistant Proposal
1. Coaching-first persona lens (Recommended)
2. Process-compliance lens
3. Career-growth lens

### Persona-First Hypothesis Example
1. "I want to support my team without sounding scripted." (Recommended)
   Business translation: higher manager confidence and retention.

## Implementation Checklist For Prompt Authors

Before publishing, verify:
1. Prompt asks one targeted question at a time.
2. Prompt uses workload inversion (assistant proposes structure).
3. Decision points use exactly 3 context-aware options.
4. Recommended option is first and justified.
5. Options are persona-first, with optional business translation.
6. User can answer with numeric choice, combinations, or custom direction.
7. Prompt includes progress signals.
8. Prompt closes with decision summary + assumptions + next steps.
9. Comment block explains why this structure works.

## Copy/Paste Starter Block For New Prompts

```markdown
### Facilitation Rules
1. Ask one targeted question at a time.
2. Apply workload inversion: gather minimal context first, then propose likely scopes/options.
3. At decision points, offer exactly 3 options, with one recommended first.
4. Phrase options in persona language first; add business translation second.
5. Accept `1`, `2`, `3`, `1 and 3`, or custom direction.
6. Show progress and close with decisions, assumptions, and next actions.
```

## Naming

When referencing this method, use:
- **Persona-First Decision Facilitation Loop**
- Short form: **PDF Loop**

