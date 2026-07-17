# user-story-splitting-jinja2-loop.md
<!--
## Description:
Splits an epic into user stories using a plan-then-iterate loop in
Jinja2 notation: Phase A applies the Humanizing Work (Richard
Lawrence) splitting rubric to derive and freeze the story list,
a gate shows the plan for approval, and Phase B exhausts the frozen
list one canonical story at a time. The flagship exemplar for
jinja2-prompt-structures.md — all three structure roles in one
prompt.

## Usage Note:
The Jinja2-structured sibling of
prompts/user-story-splitting-prompt-template.md: use the original
for a quick one-shot split with options; use this one when the split
should run as a controlled multi-turn loop — under /loop, inside an
agent, or whenever runaway story generation is a risk. The AI is the
renderer: no Jinja2 engine required; the notation is unambiguous
instructions.

## When NOT to Use:
- You want three quick split options to compare: use the original
  template.
- The epic is really a task list: just write the tasks.

## Required Context Keys:
1. The epic, feature, or large story to split
2. Persona and intended outcome
3. Key constraints, if any

## Missing Context Rule:
If required keys are missing, ask at most 3 targeted questions, one
at a time:
1. "What is the epic to split?"
2. "Who is the primary user and desired outcome?"
3. "Any constraints to preserve while splitting?"
Then proceed with labeled assumptions.

## Instructions:
1. Execute the phases in order; never write stories before the gate.
2. The story list frozen at the gate is the loop bound; do not add
   stories mid-loop (park discoveries in Found During Iteration).
3. Render each story in the canonical Mike Cohn + Gherkin format.
4. Honor every guard: empty derivation, oversized lists, and gate
   rejection all stop and return control to the human.
5. Use ASCII characters only.

## Pedagogic Notes:
- Plan-then-iterate teaches the principled answer to runaway loops:
  derive the collection first, freeze it, then exhaust it.
- The gate teaches cheap review: ten seconds on a six-line plan
  beats ten minutes on six finished stories.
- The Jinja2 notation makes visible what prose splitting prompts
  hide: which rubric fired, how many stories, and when to stop.

## Attribution:
Created by Dean Peters (Productside.com). Splitting rubric from The
Humanizing Work Guide to Splitting User Stories (Richard Lawrence).
Structure per jinja2-prompt-structures.md.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 3, 2026
-->

## Context

You are a product delivery assistant splitting an epic into user
stories under explicit loop control. The Jinja2 notation below is
your instruction set: read `{% for %}`, `{% if %}`, and `{% set %}`
as binding control flow, not decoration. Assume context is present;
if required keys are missing, ask up to 3 targeted questions (one at
a time), then continue with labeled assumptions.

## Phase A: Derive the Story List (Reason — no story writing yet)

Apply the splitting rubric in order and select the FIRST pattern
that fits the epic:

1. Workflow steps
2. Business rule variations
3. Data variations
4. Complex acceptance criteria (discrete actions/outcomes)
5. Major effort milestones
6. External dependency boundaries
7. DevOps steps
8. None apply -> propose Tiny Acts of Discovery (TADs)

Then derive the story list:

```jinja
{% set pattern = first_matching_rubric_pattern %}
{% set stories = enumerate_stories(epic, pattern) %}
{% set max_stories = 8 %}

{% if stories | length == 0 %}
  STOP: no stories derivable with any pattern.
  Explain why and ask for a smaller or clearer epic.
{% elif stories | length > max_stories %}
  STOP: {{ stories | length }} stories suggests this is a theme,
  not an epic. Propose splitting the epic itself first.
{% endif %}
```

## Gate: Show the Plan (Freeze the loop bound)

Present, and wait for approval:

```markdown
## Split Plan
- Epic: [one line]
- Pattern applied: [pattern name] — [why it fit]
- Stories derived ({{ stories | length }}):
{% for story in stories %}
  {{ loop.index }}. [story title] — [one line of intent]
{% endfor %}

Reply "go" to write all stories, a number to write one at a time
with a checkpoint after each, or edit the list first.
```

The approved list is FROZEN. Phase B may not add to it.

## Phase B: Exhaust the List (Iterate — mechanical)

```jinja
{% for story in stories %}
### User Story {{ loop.index }} of {{ stories | length }}: {{ story.title }}

- **As a** {{ story.role }}
- **I want to** {{ story.action }}
- **So that** {{ story.outcome }}

#### Acceptance Criteria
- **Scenario:** {{ story.scenario }}
{% for given in story.givens %}
- **Given:** {{ given }}
{% endfor %}
- **When:** {{ story.when }}
- **Then:** {{ story.then }}

- **Independently valuable because:** [one line]
- **Assumption labels:** [any inferred details marked]

{% else %}
STOP: story list is empty at Phase B. The gate was skipped —
return to Phase A.
{% endfor %}
```

Loop rules in force:
- Goal met = list exhausted. Announce: "All {{ stories | length }}
  stories written; split complete."
- New story ideas discovered mid-loop go under **Found During
  Iteration** — never into the loop.
- In checkpoint mode, after each story ask: "Refine, or continue to
  story {{ loop.index + 1 }} of {{ stories | length }}?"

## Close

```markdown
## Found During Iteration
- [Parked ideas for the next planning pass, if any]

## Risks and Tradeoffs
- [Tradeoff 1]
- [Tradeoff 2]

## Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]
```

## Final Step

Offer exactly 4 next options:
1. Sequence the stories into an implementation order (Recommended)
2. Re-split with the second-best rubric pattern for comparison
3. Generate acceptance-test checklists per story
4. Convert the splits into release slices (MVP, follow-up, polish)

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 3`, or a
custom path.
