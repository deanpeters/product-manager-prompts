# prd-section-loop.md
<!--
## Description:
Draft a PRD one section at a time under a seasoned /goal + /loop:
the canonical sections are spelled out as a visible data structure
(name, what it must cover, what it depends on), drafted in
dependency order with cheap checks before expensive critique, a
modify-or-continue gate per section, and compaction of each approved
section into the minimum context later sections need.

## Usage Note:
Bring your team's PRD template if you have one — its sections
replace the canonical set below. Bring whatever discovery material
exists. Level 0 works today; Level 1 is the full multi-turn
contract; Level 2 is the routine form with the section structure as
data.
Companion: workshops/prd-workshop.md is the facilitated session;
prompts/prd-prompt-template.md is the one-pass version.

## When NOT to Use:
- The problem statement is still under negotiation: critical path —
  do not loop on section seven while section three is wobbling.
- Quick internal one-pager: the ceremony outweighs the document.

## Instructions:
At every level: draft only the active section, from the base camp
plus that section's sources; never invent facts, data, approvals,
or commitments; label gaps **Assumption** or **Open Question**; the
human approves each section before the next begins.

## Pedagogic Notes:
- The section table IS Rule 3 (index before search) and Rule 4
  (critical path) made visible: what to build, in what order,
  needing what.
- Spelling sections out as a data structure teaches the JEJ move:
  structure as data, instructions as markdown, loop as one line.
- "Rerun the metrics section, not the whole autopsy" — failure
  isolated to a section is the payoff of multi-turn structure.

## Attribution:
Created by Dean Peters (Productside.com), from "Prompts Aren't Dead.
They Just Got a Bigger Vocabulary." Canonical section set as used
across this library. Loop discipline after Leen Ammeraal, Programs
and Data Structures in C (Wiley, 1987).

## Licensing:
MIT License

Date: July 3, 2026
-->

## The Canonical Sections (used by every level below)

If you have a team template, its sections replace these. Otherwise
this is the structure, in dependency order:

| # | Section | Must cover | Depends on |
|---|---------|-----------|------------|
| 1 | Problem Statement | who has it, what it is, why painful, evidence | — |
| 2 | Target Users & Personas | primary/secondary personas, jobs-to-be-done | 1 |
| 3 | Strategic Context | business goals, market opportunity, competition, why now | 1 |
| 4 | Solution Overview | description, key user flows, key features | 1, 2 |
| 5 | Success Metrics | primary metric (current -> target), secondary, failure signals | 3, 4 |
| 6 | Requirements | user stories + acceptance criteria, constraints | 4 |
| 7 | Out of Scope | what we are not building, and why | 4 |
| 8 | Open Questions & Risks | questions with owners, top risks | all |
| 9 | Executive Summary | problem + solution + impact in one paragraph | all (write last) |

### Section output format (every section, every level)

```markdown
## [N]. [Section Name]

[The section content, in prose and bullets appropriate to it]

**Assumptions in this section:**
- [labeled item, or "none"]

**Open Questions in this section:**
- [labeled item, or "none"]

**Sources used:** [which base-camp items and materials]
```

## Level 0 — Unseasoned (works today)

```
/goal Write a complete PRD for [initiative] using the canonical sections in this session and my discovery notes.
/loop Review every section. Improve anything weak. Repeat until complete.
```

You get a document. You also get the persona rediscovered nine
times, critique applied to fog, and a full re-run when one section
goes sideways.

## Level 1 — Loop Lingo (the multi-turn contract)

```
/goal Produce a PRD for [initiative]: every section drafted from
approved context, in the dependency order of the section table, with
my sign-off per section, in the section output format.

Base camp (calculate once):
- Target persona and environment: [fill or point to session]
- Problem / unmet need, with evidence: [fill]
- Desired customer and business outcomes: [fill]
- Constraints and non-negotiables: [fill]
- Decisions already made and approved: [fill]

Index before drafting (build once; do not rescan source material
unless I say "refresh"):
For each section in the table, list which session materials feed it,
which decisions already cover it, and any unresolved question
blocking it.

/loop One section per turn, in table order (1 through 8; write 9,
the Executive Summary, last).

For each section:
1. Cheap check: is its dependency approved? If not, stop and say
   which one.
2. Cheap check: do required elements and evidence exist in the base
   camp/index, or would this section be strategic fog? Flag gaps
   before drafting around them.
3. Draft ONLY this section, in the section output format, from the
   base camp plus this section's index entries.
4. Ask me: "Modify, or continue to [next section name]?" Wait.
5. On approval, compact: carry forward the decisions this section
   settled — not its full text — and update the index.

Loop controls:
- No look-ahead drafting.
- If a section fails my review twice, stop and ask me what good
  looks like before a third attempt.
```

## Level 2 — Just Enough Jinja2 (structure as data)

The section table becomes data; the drafting instructions stay
markdown; the loop is one line.

```jinja2
{% set routine_version = "prd-section-loop-v1.0" %}
{% set sections = [
  {"n": 1, "name": "Problem Statement",
   "covers": "who has it, what it is, why painful, evidence",
   "after": []},
  {"n": 2, "name": "Target Users & Personas",
   "covers": "primary/secondary personas, jobs-to-be-done",
   "after": [1]},
  {"n": 3, "name": "Strategic Context",
   "covers": "business goals, market opportunity, competition, why now",
   "after": [1]},
  {"n": 4, "name": "Solution Overview",
   "covers": "description, key user flows, key features",
   "after": [1, 2]},
  {"n": 5, "name": "Success Metrics",
   "covers": "primary metric current->target, secondary, failure signals",
   "after": [3, 4]},
  {"n": 6, "name": "Requirements",
   "covers": "user stories + acceptance criteria, constraints",
   "after": [4]},
  {"n": 7, "name": "Out of Scope",
   "covers": "what we are not building, and why",
   "after": [4]},
  {"n": 8, "name": "Open Questions & Risks",
   "covers": "questions with owners, top risks",
   "after": [1, 2, 3, 4, 5, 6, 7]},
  {"n": 9, "name": "Executive Summary",
   "covers": "problem + solution + impact, one paragraph",
   "after": [1, 2, 3, 4, 5, 6, 7, 8]}
] %}

{% for section in sections %}
## Draft section {{ section.n }} of {{ sections | length }}:
{{ section.name }}

{% if section.after %}
Confirm sections {{ section.after | join(", ") }} are approved
before drafting. If not, STOP and say which.
{% endif %}

Draft only this section. It must cover: {{ section.covers }}.
Use the base camp plus this section's index entries — nothing else.
Never invent facts, data, approvals, or commitments.

Render in the section output format:

## {{ section.n }}. {{ section.name }}

[content]

**Assumptions in this section:** [labeled, or "none"]
**Open Questions in this section:** [labeled, or "none"]
**Sources used:** [list]

Then ask: "Modify, or continue to the next section?" Wait for
approval. On approval, compact the settled decisions into the base
camp.
{% else %}
STOP: the section list is empty — load the canonical table or the
team template first.
{% endfor %}

Generated by {{ routine_version }} from template
{{ template_name | default("canonical-9-section") }}.
```

## Final Step

Offer exactly 4 next options:
1. Assemble approved sections into the full document + closing
   self-critique (Recommended)
2. Rerun just the weakest section with tightened context
3. Generate the validation plan for all logged Assumptions
4. Promote this to a named /routine with your template baked into
   the sections data structure

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 3`, or a
custom path.
