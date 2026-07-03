# epic-story-batch.md
<!--
## Description:
Convert a backlog of epics into review-ready story sets under a
governed /batch: item cap, one epic at a time in dependency order,
the canonical story format embedded, a per-epic receipt, and
fail-stop — so one weak instruction damages one epic instead of
marching through the folder with the confidence of a Seagull Manager
who just discovered automation.

## Usage Note:
Bring the epic list (ideally shaped by
prompts/backlog-epic-hypothesis.md) and the base-camp context. The
batch failure mode is scale without visibility; every control here
keeps the blast radius at one item, and every epic leaves a receipt.
Companion: vibes/epic-to-stories-formatter-jinja2.md is the
schema-driven rendering contract when the stories arrive as JSON.

## When NOT to Use:
- One epic: that is a loop, not a batch — use
  loops/story-splitting-loop.md.
- Epics not yet validated as hypotheses: batching multiplies an
  upstream mistake by the size of the folder.

## Instructions:
At every level: item cap enforced; one epic per turn; every story
rendered in the canonical story format (never summarized); per-epic
receipt; hard stop on first failure rather than quiet contamination
of the rest of the batch.

## Pedagogic Notes:
- Teaches the batch-specific control set: cap, serialization,
  per-item receipts, fail-stop.
- Index-before-search at batch scale: triage the epic list once,
  sequence by dependency, then process — never "do the folder."
- The embedded story format shows the JEJ division of labor: the
  markdown template does the quality; the Jinja2 only caps and
  counts.

## Attribution:
Created by Dean Peters (Productside.com), from "Prompts Aren't Dead.
They Just Got a Bigger Vocabulary." Story format per Mike Cohn +
Gherkin, as used across this library. Loop discipline after Leen
Ammeraal, Programs and Data Structures in C (Wiley, 1987).

## Licensing:
MIT License

Date: July 3, 2026
-->

## Canonical Story Format (every story, every level)

```markdown
### User Story [epic-id].[story-id]: [4 to 8 word title]

- **Summary:** [one sentence]

#### Use Case
- **As a** [persona]
- **I want to** [action]
- **So that** [outcome]

#### Acceptance Criteria
- **Scenario:** [one coherent scenario aligned to the persona]
- **Given** [precondition — repeat as needed]
- **When** [triggering action]
- **Then** [observable result]

- **Traces to epic hypothesis:** [which part]
- **Assumptions:** [labeled, or "none"]
```

## Per-Epic Receipt (every epic, every level)

```markdown
#### Receipt: Epic [id] — [title]
- Stories generated: [N]
- Cheap checks: [passed / what failed]
- Assumptions labeled: [count + the risky ones]
- Unresolved issues: [list, or "none"]
- Status: [complete / skipped: reason / FAILED at: step]
```

## Level 0 — Unseasoned (works today)

```
/batch For every epic in this backlog, generate its user stories in the canonical story format with acceptance criteria.
```

It will indeed touch everything. Whether it should have is the
question you'll answer at 4pm with a flashlight.

## Level 1 — Loop Lingo (the batch contract)

```
/goal Convert validated epics into review-ready story sets — every
story in the canonical story format, every epic closed with a
receipt, zero silent failures.

Base camp (calculate once): persona set, product outcomes,
constraints, our definition of ready for a story.

Index before you batch (build once):
1. List the epics: id, title, one-line hypothesis.
2. Mark dependencies between epics; sequence by them.
3. Flag any epic missing a testable hypothesis, persona, or outcome
   — those are returned to the backlog, not processed.

/batch Process the sequenced epic list with these controls:

- No more than 10 epics per run. More than 10? Tell me and stop
  at 10.
- One epic at a time, in dependency order.
- Per epic, cheap checks first: hypothesis present? persona named?
  outcome stated? Any miss = skip, record in the receipt, move on.
  Do not generate stories from fog.
- Generate the epic's stories in the canonical story format —
  every field, no summaries.
- Close the epic with its receipt, then return everything for
  review before touching the next epic.
- If generation fails mid-epic: STOP the whole batch. The receipt
  names the epic, the step, and the resume point. Do not quietly
  contaminate the rest.
```

## Level 2 — Just Enough Jinja2 (cap, count, receipts)

The story format and receipt stay markdown; the Jinja2 caps the run
and walks the list.

```jinja2
{% set routine_version = "epic-story-batch-v1.0" %}

{% for epic in epics[:10] %}
## Epic {{ loop.index }} of {{ epics[:10] | length }}:
{{ epic.id }} — {{ epic.title }}

Cheap checks: hypothesis present, persona named, outcome stated.
Any miss: record in the receipt as "skipped: [reason]" and continue
to the next epic.

For each story this epic yields, render:

### User Story {{ epic.id }}.[story-id]: [title]

- **Summary:** [one sentence]

#### Use Case
- **As a** [persona]
- **I want to** [action]
- **So that** [outcome]

#### Acceptance Criteria
- **Scenario:** [scenario]
- **Given** [precondition — repeat as needed]
- **When** [action]
- **Then** [result]

- **Traces to epic hypothesis:** [which part]
- **Assumptions:** [labeled, or "none"]

Close the epic:

#### Receipt: Epic {{ epic.id }} — {{ epic.title }}
- Stories generated / checks / assumptions / issues / status

Return for review before the next epic. If generation failed here,
STOP the batch: this receipt is the resume point.
{% else %}
STOP: the epic list is empty. Build the index first.
{% endfor %}

{% if epics | length > 10 %}
NOTE: {{ epics | length - 10 }} epics remain beyond the cap. Ask
before starting run two.
{% endif %}

Generated by {{ routine_version }}.
```

## Final Step

Offer exactly 4 next options:
1. Review the receipts and clear the skipped epics (Recommended)
2. Export all approved stories in Jira/ADO-friendly plain format
3. Start run two on the epics beyond the cap
4. Promote this to a named /routine with your definition of ready
   baked into the cheap checks

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 2`, or a
custom path.
