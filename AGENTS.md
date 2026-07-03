# AGENTS.md

## Mission
This repository exists to help product managers do better work with AI and to teach them how to write better prompts themselves.

Every change must serve both outcomes:
1. Practical PM usefulness (strategic and tactical execution support)
2. Pedagogic value (teaches prompt design patterns through structure and comments)

If there is a tradeoff, prefer pedagogy and clarity over cleverness.

## Primary Constraint: Pedagogy First
- Treat each prompt as a teaching artifact, not just an output generator.
- Preserve and improve the "hidden curriculum" in metadata comments and structural choices.
- Make reasoning and framework selection legible to PM readers.
- Teach transferable prompting skills (context setting, scaffolding, validation), not one-off tricks.

## Repository Map and Intent
- `prompts/`: Core PM frameworks and execution prompts.
- `prompt-generators/`: Meta-prompts that emit reusable prompts.
- `workshops/`: Guided multi-turn sessions that produce the finished artifact itself (battle card, PRD, canvas, business case).
- `storytelling/`: Narrative, visual, and communication-oriented prompt assets.
- `market-intelligence/`: Autonomous research prompts (evidence contracts, search plan gates, stable diffable schemas; suitable for agents, loops, and scheduled runs).
- `loops/`: Seasoned /goal, /loop, /batch, /routine recipes recasting key prompts at three levels — plain commands, plain-English loop lingo (pass ceilings, no-change exits, modify-or-continue gates, fail-stop, receipts), and Just Enough Jinja2. Grounded in the four rules: calculate once, order checks by cost, index before search, know the critical path.
- `skeletons/`: Prompt architecture analysis and reverse-engineering tools.
- `vibes/`: Experimental and agentic workflow prompts.
- `resumes-resignations-reactions/`: Satirical/therapeutic creative prompts.
- `flows/`: Flow exports and automation-style artifacts (for example LangFlow JSON).

Place new files in the directory that best matches learning intent for users.

## Prompt Authoring Contract
When creating or revising prompts:
- Use AI-directed instructions (the prompt should speak to the assistant).
- Use conversational scaffolding where appropriate (one question at a time).
- Apply workload inversion: ask for minimal context, then have the assistant propose structure/options.
- Add fallback behavior for missing required context.
- Frame recommendations in persona language first; add business translation second when needed.
- Ground prompts in recognizable PM frameworks when possible.
- Keep humans as decision owners; AI assists, it does not replace judgment.

## Interaction Modes

Every prompt follows one of three interaction modes, defined in
`interaction-modes.md`:
- **Facilitation** (Generative Guidance): the human holds the context;
  the AI extracts it with budgeted, narrowing questions.
- **Checkpointed co-construction**: an artifact (template, case study)
  drives section-by-section building; the human gates each section;
  gaps are labeled **Assumption** or **Open Question**, never invented.
- **Autonomous investigation**: the world holds the context; the AI does
  the fieldwork under an evidence contract (citations, credible source
  classes, ranges for uncertainty) with overridable defaults so the
  prompt can run unattended, in a loop, or on a schedule.

Declare one primary mode per prompt. If the AI could answer the intake
questions itself with a web search, facilitation is burden-shifting —
use investigation.

## Generative Guidance Pattern (v2)

Most prompts in `/prompt-generators/` and a portion of the generators in
`/storytelling/` are built on the **Generative Guidance** pattern. Read
`generative-guidance-pattern.md` before creating or editing any file in
those directories.

The v2 pattern: the AI asks a budgeted 3–5 questions one at a time,
offering 3 context-aware recommendations plus "Other" per question.
Two standing bypasses are honored at every turn: "take your best guess"
(AI answers, names the assumption) and "bulk drop" (user pastes notes;
AI extracts answers, accounts for found / inferred / missing, asks only
about gaps). Loop-control verbs — skip, go back, stop early — are
honored at any turn. The AI searches before offering options that would
otherwise be generic, and says so. The final output is withheld until
the loop closes with a confirm-before-build summary. If the user
arrives with sufficient context, questions are reduced or skipped.

Authoring rules for prompts that use this pattern:
- Choices 1–3 must be generated from accumulated context, not hardcoded.
- The standing bypasses (best guess, bulk drop) are non-negotiable
  fixtures. Do not omit them.
- Include the context-detection collapse rule explicitly in the prompt.
- Each question must visibly narrow in specificity based on prior answers.
- Set the question budget in the prompt; close with stated assumptions
  when it is reached.
- Persona language first; business translation second.
- Existing v1 prompts (5-choice menus) are grandfathered; migrate to v2
  when the file is next edited. Do not mass-rewrite the library.

## Template Stability Policy
- Canonical PM templates are pedagogic assets and must be preserved.
- Do not remove or replace established framework structure (for example JTBD, Gherkin user stories, proto-persona canvas, Moore positioning) unless explicitly requested.
- Improve intake and facilitation around templates, not instead of templates.
- For `/prompts/`, prefer adaptive context intake plus fixed template output.
- If structure must change, version explicitly (`v1`, `v2`) rather than silently mutating existing templates.

## Required Metadata for Prompt Assets
For prompt files, include a clear comment metadata block (or preserve/improve the existing one) with:
- `Description`
- `Usage Note`
- `Instructions`
- `Attribution`
- `Licensing`
- `Date`

If a prompt intentionally deviates, explain the rationale in comments.

New and substantially revised prompts should also include a short
**When NOT to Use** note (in the metadata comment or Usage Note):
one or two lines naming the situations where this prompt is the wrong
tool and what to reach for instead. Misuse boundaries are part of the
hidden curriculum.

## Teaching Quality Bar
Before considering a prompt "done", verify:
1. A PM can use it to solve a real problem now.
2. A PM can learn at least one reusable prompt-writing pattern from it.
3. The flow reduces ambiguity and cognitive overload.
4. The output format is professional and actionable.
5. The prompt does not force users to pre-design the artifact the AI should help create.

## Naming, Placement, and Duplication
- Prefer lowercase-hyphen file names for new assets unless there is a strong curation reason not to.
- Avoid duplicate canonical content across directories.
- If content appears in two places, choose one canonical file and convert the other to a pointer or clearly justify intentional duplication.

## Jinja2 Prompt Structures
Prompts that run under /loop, /goal, or inside agents may use Jinja2
notation for explicit control flow. Read `jinja2-prompt-structures.md`
before writing or editing one. Core rules: loop over arrays (never
index), one authority per identifier, an else-branch on every loop,
stop conditions stated before work instructions, and derived
collections frozen at a human gate. Exemplars live in `/vibes/`.

## Tooling and Safety
- After adding or editing prompt assets, run
  `python3 scripts/validate-prompts.py` (exit 1 on errors) and
  `python3 scripts/generate-catalog.py` (regenerates `catalog/`,
  which is derived output — never hand-edit it).
- Do not commit credentials, keys, or secrets.
- Keep docs and scripts aligned (especially environment variable names and usage instructions).
- Preserve MIT licensing references and creator attribution.

## Editing Guidance for Agents
- Make focused edits; avoid rewriting voice/style unnecessarily.
- Preserve pedagogic comments unless improving them.
- Do not remove learning-oriented structure just to shorten prompts.
- Favor compatibility across ChatGPT, Claude, and Gemini where practical.
- Keep output contracts stable for downstream tooling (for example Jira/ADO import conventions).

## Review Checklist (Pre-PR)
Run this quick check before finalizing:
1. Mission fit: practical + pedagogic value both improved.
2. Metadata block complete and useful.
3. Naming and placement follow directory intent.
4. Links and file references still resolve.
5. No accidental duplication introduced.
6. Any code/doc mismatch resolved.
7. No burden-shifting questions; decision options are persona-first and context-aware.

## PR Notes
In change summaries, include:
- What PM problem this helps solve
- What prompt-writing behavior this teaches
- Any framework choices and why they were used
- Any compatibility notes across AI assistants
