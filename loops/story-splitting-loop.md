# story-splitting-loop.md
<!--
## Description:
Split an epic into right-sized user stories with a /goal plus two
/loop commands, seasoned with the four rules (calculate once, order
checks by cost, index before search, critical path) and finished
with Just Enough Jinja2. The canonical user story output format is
embedded at every level — the markdown is the meal; the Jinja2 only
marks where the work repeats, stops, and signs its output.

## Usage Note:
Bring an epic and the stable context: persona, outcome, constraints,
decisions already made. Level 0 works today as typed; Level 1 adds
the operating contract; Level 2 is the routine form. All three
render the same canonical story format.
Companion: prompts/user-story-splitting-prompt-template.md is the
one-shot version; vibes/user-story-splitting-jinja2-loop.md is the
fully structured plan-then-iterate form.

## When NOT to Use:
- One small story to split once: use the one-shot template.
- The epic is unvalidated fog: frame the problem first; forty
  consistent stories from a bad epic is downstream polish on
  upstream fog.

## Instructions:
The user runs whichever level matches the moment. At every level:
apply the rubric in order, keep splits independently valuable, and
render every story in the canonical output format below — never a
summary of it, never a paraphrase.

## Pedagogic Notes:
- Same workflow, three levels of visibility: PMs see exactly what
  each layer of seasoning buys.
- The canonical format inside the Jinja2 loop teaches the core JEJ
  lesson: the template stays markdown; the loop just says how many
  times and when to stop.
- The pass ceiling and survivor rule teach loop hygiene without
  writing code.

## Attribution:
Created by Dean Peters (Productside.com), from "Prompts Aren't Dead.
They Just Got a Bigger Vocabulary." Splitting rubric from The
Humanizing Work Guide to Splitting User Stories (Richard Lawrence).
Story format per Mike Cohn + Gherkin, as used across this library.
Loop discipline after Leen Ammeraal, Programs and Data Structures in
C (Wiley, 1987).

## Licensing:
MIT License

Date: July 3, 2026
-->

## Canonical Story Format (used by every level below)

Every rendered story uses this exact markdown structure:

```markdown
### User Story [epic-id].[story-id]: [4 to 8 word title]

- **Summary:** [one sentence]

#### Use Case
- **As a** [persona]
- **I want to** [action]
- **So that** [outcome]

#### Acceptance Criteria
- **Scenario:** [one coherent scenario aligned to the persona]
- **Given** [precondition — repeat this line as needed]
- **When** [the triggering action]
- **Then** [the observable result]

- **Split rationale:** [which rubric pattern produced this story]
- **Assumptions:** [anything inferred, or "none"]
```

## Level 0 — Unseasoned (works today, exactly as typed)

```
/goal Use Richard Lawrence's story splitting rubric to break this epic into an array of right-sized user stories.
/loop Go through the story array. Split anything that still fails the rubric. Repeat until nothing splits.
/loop Go through the settled story array and render each story in the canonical story format from this session.
```

It runs. What you can't see: how many passes it took, whether cheap
checks ran before expensive ones, or what broke when story seventeen
came out wrong.

## Level 1 — Loop Lingo (the operating contract)

```
/goal Split this epic into right-sized user stories.

Base camp (calculate once — carry forward, do not rediscover):
- Epic: [paste it]
- Persona: [who]
- Desired outcome: [what progress]
- Constraints and decisions already made: [list]

Success: every story passes the splitting rubric, is independently
valuable, traces to the outcome above, and is rendered in the
Canonical Story Format. Stop when true, or when my judgment is
required.

/loop Splitting passes. Work the story array one story per turn.

For each story, order checks by cost:
1. Cheap: persona, job, and outcome present? If not, flag it — do
   not run the rubric on an empty bottle.
2. Cheap: contradicts the base camp? Flag and stop.
3. Expensive: apply the rubric in order — workflow steps, business
   rule variations, data variations, complex acceptance criteria,
   effort milestones, external dependencies, DevOps steps, or
   propose Tiny Acts of Discovery. Split on the FIRST pattern that
   fits, into two smaller stories.

Loop controls:
- No more than 3 passes over the array.
- Stop earlier if a pass produces no new splits.
- After each pass report: [N] stories, [M] split this pass, [list
  of survivors and why].
- If the same story survives 2 passes but still feels too big, stop
  and ask me.

/loop Rendering pass. One story per turn, in the Canonical Story
Format — every field, no paraphrasing. After each story ask:
"Modify, or continue to story [next] of [total]?"
```

## Level 2 — Just Enough Jinja2 (the routine form)

The markdown is unchanged. The Jinja2 only sets the ceiling, walks
the array, and signs the output.

```jinja2
{% set routine_version = "story-split-v1.0" %}

Base camp: epic, persona, outcome, constraints — stated once above;
carry it forward.

{% for pass in range(1, 4) %}
## Splitting pass {{ pass }} of 3

For each story still in the array:
1. Cheap check: persona, job, outcome present — else flag, skip.
2. Cheap check: contradicts base camp — else flag, stop.
3. Apply the Lawrence rubric in order; split on the first pattern
   that fits.

End of pass {{ pass }}: report stories total, split this pass, and
survivors. Stop if nothing split. If a story survives two passes,
stop and ask the Product Manager.
{% endfor %}

## Rendering

{% for story in settled_stories %}
### User Story {{ epic_id }}.{{ loop.index }}: {{ story.title }}

- **Summary:** {{ story.summary }}

#### Use Case
- **As a** {{ story.persona }}
- **I want to** {{ story.action }}
- **So that** {{ story.outcome }}

#### Acceptance Criteria
- **Scenario:** {{ story.scenario }}
{% for given in story.givens %}
- **Given** {{ given }}
{% endfor %}
- **When** {{ story.when }}
- **Then** {{ story.then }}

- **Split rationale:** {{ story.rubric_pattern }}
- **Assumptions:** {{ story.assumptions }}

Return this story for review before continuing.
{% else %}
STOP: the settled array is empty — the splitting passes produced
nothing. Return to the /goal.
{% endfor %}

Generated by {{ routine_version }} using the Lawrence rubric.
```

## Final Step

Offer exactly 4 next options:
1. Sequence the settled stories by dependency (critical path)
   (Recommended)
2. Run an acceptance-criteria quality check across all stories
3. Promote this to a named /routine with your team's conventions
4. Export the stories in Jira/ADO-friendly plain format

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 2`, or a
custom path.
