# Artifact-First Context Intake (AFCI)

<!--
## Description:
Canonical method for context collection in prompt workflows. AFCI prioritizes
artifacts and existing session context before asking users additional questions.

## Usage Note:
Use this across /prompts, /prompt-generators, and decision-heavy /storytelling
flows whenever context quality affects output quality.

## Instructions:
Treat this document as a reusable operating standard and teaching artifact.

## Attribution:
Created in collaboration with Dean Peters and Codex, March 2, 2026.

## Licensing:
MIT License

Date: March 2, 2026
-->

## What Is AFCI?

**Artifact-First Context Intake (AFCI)** is a context-ingestion pattern:
1. Read available artifacts first (PDF, DOC, TXT, CSV, pasted notes, PRDs, etc.)
2. Extract required context keys from those artifacts
3. Ask targeted follow-up questions only for missing critical context

AFCI prevents redundant questioning and reduces user setup burden.

## Why AFCI Exists

Without AFCI, prompts often:
- Ask for information users already provided in documents
- Force users to restate context manually
- Waste turns before decisions can begin

With AFCI, the assistant does the heavy lifting first.

## Core Rule Set

1. **Intake Order**
Use this order every time:
- Existing session context
- Attached artifacts
- Pasted text/context blocks
- Follow-up questions (only if required keys are still missing)

2. **No Redundant Questions**
Do not ask for information already present in artifacts/context.

3. **Required Key Extraction**
Each prompt should define required context keys. Extract these before asking questions.

4. **Max Question Budget**
If keys are still missing, ask at most 3 targeted questions, one at a time.

5. **Assumption Transparency**
If context remains incomplete after 3 questions, proceed with labeled assumptions.

## Standard Prompt Clause (Copy/Paste)

```markdown
## Context Intake Rule
Assume context may arrive via:
1. Attached artifact(s)
2. Pasted text/context block
3. Existing session memory

If artifacts are provided:
- Extract required context keys first.
- Do not ask for details already present.
- Summarize extracted context in 5-10 bullets.

If required keys are still missing:
- Ask up to 3 targeted questions, one at a time.
- Then proceed with clearly labeled assumptions.
```

## Output Requirements For AFCI

Before producing the main artifact, include:

```markdown
## Context Summary
- [Extracted fact]
- [Extracted fact]
- [Extracted fact]

## Missing Context (If Any)
- [Key not found]

## Assumptions (If Any)
- [Assumption]
```

## Question Quality Rules

If follow-up is needed, questions must be:
- **Targeted**: tied directly to missing keys
- **Answerable quickly**: one sentence or one choice
- **Non-overlapping**: no repeated asks

Good:
- "Which persona should this output prioritize first?"
- "What business outcome matters most for this decision?"

Bad:
- "Tell me everything about your product and users."

## AFCI + PDF Loop

Use both together:
- **AFCI**: gather context with minimal user effort
- **PDF Loop**: guide decision forks with persona-first options

Recommended sequence:
1. AFCI intake
2. Context summary + assumptions
3. PDF decision facilitation
4. Final artifact + next actions

## Anti-Patterns

1. **Artifact Ignored**
User uploads docs, assistant starts generic intake anyway.

2. **Question Flood**
Assistant asks long questionnaires before reading available context.

3. **Silent Guessing**
Assistant makes assumptions without labeling them.

## Implementation Checklist

Before publishing prompts:
1. Required context keys are explicit.
2. AFCI intake rule is present.
3. Max-3 question fallback exists.
4. Assumption labeling exists.
5. Context summary block exists.
6. Questions are targeted and non-redundant.

## Naming

Use this term in docs/reviews:
- **Artifact-First Context Intake**
- Short form: **AFCI**

