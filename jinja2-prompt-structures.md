# Jinja2 Prompt Structures

How and why this repository uses Jinja2 notation inside prompts:
loops, switches, and guards that make control flow explicit,
bounded, and safe — for humans running prompts under `/loop` or
`/goal` style commands, and for people writing agents.

**Notational, not rendered.** No Jinja2 engine runs these templates.
The AI assistant is the renderer: it reads `{% for %}` and `{% if %}`
as unambiguous instructions about iteration and branching. This keeps
every prompt copy-paste-runnable in any chat AI while making its
control flow inspectable. (Agent builders who want literal rendering
can pair these templates with a JSON schema and a real renderer —
the notation is valid Jinja2 on purpose.)

---

## Why structure control flow at all

Most prompts already contain implicit control flow, written as prose
and enforced by hope:

- "ask 3–5 questions one at a time" is a bounded loop
- "build the PRD one section at a time" is `for section in template`
- "report only material shifts" is a filtered loop with an
  empty-case branch
- "use as many Given steps as needed" is a nested loop of unknown
  cardinality

Prose control flow fails in two directions: the AI stops early
(dropped stories, skipped sections) or doesn't stop (runaway
generation, "one more option" drift). Jinja2 notation closes both:
iteration is over a named, finite collection; branches are explicit;
the empty case has a defined behavior.

---

## The Three Roles

### Role 1: Control-flow safety (loops and goals)

For prompts that run repeatedly — under `/loop`, on a schedule,
inside an agent — the structures are the brake lines:

```jinja
{% set max_runs = 6 %}
{% if run_count >= max_runs %}
  STOP: budget exhausted. Summarize state and hand back to the human.
{% elif goal_met %}
  STOP: goal reached. Report the evidence for goal_met.
{% elif consecutive_no_change >= 2 %}
  STOP: nothing is changing. Recommend widening the cadence.
{% else %}
  ... one iteration of the work ...
{% endif %}
```

Rules:
- **Every recurring prompt names its stop conditions** — budget,
  goal predicate, and no-change exit — before any work instructions.
- **Goal predicates are checkable**, not vibes: "goal_met = all
  major data points have cited sources," not "when it feels done."
- **The else-branch of every guard escalates to the human**: budget
  exhausted, confidence below threshold, or an action outside
  authorized scope (an Agent Strategy Canvas Safeguards entry,
  expressed as a guard).

### Role 2: Output contracts over variable-cardinality data

When the output contains "however many there are" — epics, stories,
competitors, Given-steps — a loop makes the per-item shape a
contract instead of an example:

```jinja
{% for epic in epics %}
## Epic {{ epic.id }}: {{ epic.title }}

{% for story in epic.stories %}
### User Story {{ epic.id }}.{{ story.id }}
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
{% endfor %}

{% else %}
NOTE: no epics were derivable from the input. Stop and ask.
{% endfor %}
```

This is where the repo's template-stability policy meets dynamic
data: the section order stays canonical AND the cardinality is
explicit. The natural companion is a two-step pipeline — one prompt
(or agent) produces structured data conforming to a schema; a second
renders it through the template. The schema is the real contract;
the template is a projection of it.

### Role 3: Plan-then-iterate (derive the bound, then exhaust it)

The best answer to runaway loops is not "stop at N" (arbitrary) but
"the iteration set was fixed before iteration began" (principled):

1. **Phase A — reason:** apply a rubric to derive the collection.
   (Splitting an epic: apply Richard Lawrence's splitting patterns,
   choose the pattern that fits, enumerate the resulting story
   list — titles and one line each.)
2. **Gate:** show the derived list. The human reviews a six-line
   plan for ten seconds instead of six finished artifacts for ten
   minutes. Continue unless revised. (This is the investigation
   mode's search-plan gate, in loop form.)
3. **Phase B — iterate:** `{% for item in derived_list %}` exhausts
   the frozen collection. No mid-loop additions, no "one more"
   drift. Goal met = list exhausted.

---

## Authoring Rules

1. **Loop over arrays; never index into them.** `{{ metrics[2] }}`
   silently breaks on two metrics and silently drops a fourth.
   `{% for metric in metrics %}` handles any count.
2. **One authority per identifier.** Do not number epics with
   `loop.index` in one place and `epic.id` in another — they diverge
   the moment data order changes. Pick the data's ID or the loop's
   position, once.
3. **Every loop has an empty-case branch.** Jinja2's `{% else %}`
   on a `for` loop fires when the collection is empty; use it. An
   empty collection rendered as bare headers is a silent failure.
   The empty branch either explains, asks, or stops.
4. **Bounds and stop conditions come first.** State the budget, the
   goal predicate, and the escalation rule before the work
   instructions, so a `/loop` or agent reads its brakes before its
   accelerator.
5. **Freeze derived collections at the gate.** After the human
   approves the Phase A list, Phase B may not add to it. New
   discoveries go to a "found during iteration" note for the next
   planning pass.
6. **Keep the notation minimal.** `for`, `if/elif/else`, `set`, and
   `{{ variables }}` cover everything this repo needs. If a template
   needs macros or filters, it probably needs to be two prompts.

---

## Anti-Patterns

| Anti-pattern | Symptom | Fix |
|---|---|---|
| Indexed access | `{{ items[0] }} {{ items[1] }} {{ items[2] }}` | Loop; rule 1 |
| Split identifier authority | `loop.index` here, `item.id` there | One authority; rule 2 |
| Guardless loop | Empty input renders empty headers | `{% else %}` branch; rule 3 |
| Unbounded while | "keep going until it's good" | Derive the collection first; Role 3 |
| Goal as vibes | "stop when complete" | Checkable predicate; Role 1 |
| Silent scope growth | Loop body adds items mid-iteration | Freeze at the gate; rule 5 |

---

## Where This Is Used

Exemplars live in `/vibes/` (the repo's experimental and agentic
directory):

- `vibes/user-story-splitting-jinja2-loop.md` — the flagship:
  Lawrence-rubric plan-then-iterate splitting of an epic (all three
  roles in one prompt)
- `vibes/epic-to-stories-formatter-jinja2.md` — the output-contract
  exemplar: renders structured epic/story data through a fixed
  Gherkin template (Role 2, with the authoring rules applied)

Related documents: `interaction-modes.md` (the search-plan gate and
delta rules that these structures formalize),
`generative-guidance-pattern.md` (question budgets are bounded
loops), and `market-intelligence/README.md` (materiality bars and
no-change exits as loop break conditions).
