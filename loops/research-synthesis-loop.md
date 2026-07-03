# research-synthesis-loop.md
<!--
## Description:
Synthesize research (interviews, VoC, support signals) one category
per turn under a seasoned /goal + /loop: the category index is built
once, each pass pulls forward only that category's evidence, and
every theme is rendered in an embedded output format with real
verbatims, frequency, and Fact / Inference / Assumption labels — so
eight transcripts don't get boiled into one vat of vaguely strategic
soup.

## Usage Note:
Bring the raw material (transcripts, VoC snapshot, tickets) into
session. The theme output format below is the contract at every
level; the loop just controls how many themes and when you gate.
Companion: market-intelligence/voice-of-customer-miner-prompt.md
gathers public voice upstream;
prompts/discovery-interview-guide-prompt-template.md plans the
interviews that feed this.

## When NOT to Use:
- One interview: just summarize it; the ceremony outweighs the
  material.
- No raw material in session: gather first — synthesis of nothing
  is opinion with headers.

## Instructions:
At every level: themes phrased as needs (solution-free); every
claim carries a source or an Assumption label; verbatims are real
quotes from the material, never invented; each theme rendered in
the theme output format, no paraphrasing.

## Pedagogic Notes:
- Index-then-analyze teaches that synthesis quality is set by the
  map, not the mileage.
- The embedded theme format forces evidence honesty per theme
  instead of confidence-by-vibes at the end.
- One-category turns keep contradictory evidence visible instead of
  averaged away in a single mega-pass.

## Attribution:
Created by Dean Peters (Productside.com), from "Prompts Aren't Dead.
They Just Got a Bigger Vocabulary." Loop discipline after Leen
Ammeraal, Programs and Data Structures in C (Wiley, 1987).

## Licensing:
MIT License

Date: July 3, 2026
-->

## Theme Output Format (every theme, every level)

```markdown
### Theme [N]: [the underlying need, solution-free, 4 to 8 words]

- **Frequency:** [recurring across sources / concentrated in one
  segment / isolated]
- **Verbatim:** "[real quote]" — [source, role, date]
- **Verbatim:** "[real quote]" — [source, role, date]
- **Who feels it:** [role/segment — labeled Fact or Inference]
- **What contradicts it:** [counter-evidence, or "none found"]
- **Confidence:** [Fact / Inference / Assumption — one label]
- **So what:** [one sentence: what this means for the decision]
```

## Level 0 — Unseasoned (works today)

```
/goal Synthesize these eight interview transcripts into key themes and product implications.
```

You'll get themes. You won't know which transcript carried which
theme, which themes are one loud customer, or what got averaged
away.

## Level 1 — Loop Lingo (the synthesis contract)

```
/goal Synthesize this research into evidence-cited need themes I can
defend in a roadmap conversation — every theme in the Theme Output
Format.

Base camp (calculate once): research goal, the decision this
informs, personas in scope, and what we believed BEFORE the research
(so contradictions surface as findings, not formatting problems).

Index before you search (build once; do not rescan transcripts
unless I say "refresh"):
1. Sources: who, role, date.
2. Candidate theme categories, one-line definition each.
3. Which sources touch which category.
4. Open questions the material may not answer.

/loop One category per turn.

For each category:
1. Cheap check: does more than one source touch it? One-source
   themes get processed but flagged "isolated" — never promoted to
   headline findings.
2. Pull forward only this category's mapped evidence.
3. Render the theme in the Theme Output Format — every field, real
   verbatims with attribution, one confidence label.
4. Ask me: "Modify, or continue to [next category]?" Wait.
5. On approval, compact: carry the theme and its strongest verbatim
   forward — not the transcripts.

Loop controls:
- No cross-category conclusions until all categories are settled.
- Evidence contradicting the base-camp beliefs gets flagged loudly:
  that IS the finding.
- After the last category, and only then, produce the cross-cutting
  synthesis: top 3 needs, what changed our minds, top 3 assumptions
  to validate next.
```

## Level 2 — Just Enough Jinja2 (the routine form)

```jinja2
{% set routine_version = "research-synthesis-v1.0" %}

{% for category in category_index %}
## Category {{ loop.index }} of {{ category_index | length }}:
{{ category.name }}

Use only this category's mapped evidence: {{ category.sources }}.

Render in the Theme Output Format:

### Theme {{ loop.index }}: [underlying need, solution-free]

- **Frequency:** [recurring / concentrated / isolated]
- **Verbatim:** "[real quote]" — [source, role, date]
- **Verbatim:** "[real quote]" — [source, role, date]
- **Who feels it:** [role/segment — Fact or Inference]
- **What contradicts it:** [counter-evidence, or "none found"]
- **Confidence:** [Fact / Inference / Assumption]
- **So what:** [one sentence]

Ask "Modify, or continue?" and wait before the next category.
{% else %}
STOP: no category index exists. Build the index before synthesis.
{% endfor %}

## Cross-cutting synthesis (only after all categories approved)
- Top 3 needs, ranked, with their strongest verbatims
- What changed our minds vs. the base-camp beliefs
- Top 3 assumptions to validate next

Generated by {{ routine_version }} from
{{ category_index | length }} categories,
{{ source_count }} sources.
```

## Final Step

Offer exactly 4 next options:
1. Produce the cross-cutting synthesis and top opportunity
   hypotheses (Recommended)
2. Convert the strongest theme into a JTBD canvas
3. Draft the "what changed our minds" note for stakeholders
4. Generate follow-up interview questions for the weakest evidence

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 2`, or a
custom path.
