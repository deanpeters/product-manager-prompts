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
- `skills/`: Agent Skills — prompts packaged so an agent loads them on its own. One folder per skill, named `kebab-case`, containing `SKILL.md` plus optional `template.md` and `examples/`.
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
- `Standalone`
- `Usage Note`
- `Instructions`
- `Attribution`
- `Licensing`
- `Date`

`Standalone` declares the coupling contract, and takes one of:
- `yes` -- finishes the job alone (required for everything in `prompts/`)
- `better with [artifact], works without` -- soft prereq
- `requires [artifact]` -- hard gate, `loops/` and `vibes/` only

If a prompt intentionally deviates, explain the rationale in comments.

New and substantially revised prompts should also include a short
**When NOT to Use** note (in the metadata comment or Usage Note):
one or two lines naming the *situations* where this prompt is the
wrong tool. Name situations, not alternative files -- see Coupling
Discipline. Misuse boundaries are part of the hidden curriculum.

## Agent Skills (`skills/`)

A skill is a prompt packaged so an agent can decide, unprompted, that it
applies. That decision is made from the YAML frontmatter alone, so the
frontmatter is a functional interface, not decoration.

### The upstream spec wins

**Skills in this repository follow the Agent Skills spec as Anthropic
defines it, not a convention of our own.** The authorities, in order:

1. [agentskills.io](https://agentskills.io) — the open standard
2. [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
3. [Skills in Claude Code](https://code.claude.com/docs/en/skills)

Where this file and the upstream spec disagree, **the spec is right and
this file is stale** — fix it here rather than working around it. Check
the spec before inventing a rule; a house convention that contradicts it
will silently break distribution.

**Hard constraints, quoted from the spec:**

- `name`: maximum 64 characters, **lowercase letters, numbers, and
  hyphens only**, no XML tags, and it may not contain the reserved words
  `anthropic` or `claude`.
- `description`: non-empty, maximum 1,024 characters, no XML tags,
  **written in third person** ("Generates…", never "I can help you…"),
  stating both what the skill does *and* when to invoke it.
- SKILL.md body: keep under 500 lines; split overflow into sibling files
  referenced **one level deep** from SKILL.md.

**Only six frontmatter keys are portable.** `name`, `description`,
`license`, `compatibility`, `metadata`, `allowed-tools`. Claude Code
accepts more, but claude.ai uploads, the Skills API, and
`package_skill.py` reject an unknown key with a **hard error**, not a
warning. Since this repository publishes skills for other people to
install, treat the six-field list as the ceiling.

Our curation fields (`intent`, `type`, `theme`, `best_for`, `scenarios`,
`estimated_time`) are **not** spec fields. They live nested under
`metadata:`, which the spec defines as a free-form map for exactly this
purpose. Do not promote them back to the top level.

Layout: `skills/<kebab-case-name>/SKILL.md`, plus optional `template.md`
(the output contract) and `examples/` (worked runs). **Kebab-case, never
snake_case** — the folder name is what a user types to invoke a personal
or project skill, and underscores are not a legal `name`.

`SKILL.md` carries **both** headers, in this order:
1. **YAML frontmatter** — spec-conformant, per the constraints above,
   with `name` equal to the folder name.
2. **The standard HTML comment block**, immediately after the closing
   `---`, with the same seven fields every other asset carries. The
   frontmatter serves the agent; the comment block serves the human
   reading the raw file. Neither substitutes for the other.

Coupling: **`skills/` is level 0, same as `prompts/`.** An agent invokes
a skill cold, with no guarantee any sibling skill was loaded first, so
`Standalone: yes` is required and cross-references to other skills are
prohibited above the Final Step. Reference external frameworks and books
freely; name sibling skill files never.

A skill adapted from a prompt may legitimately change the output shape —
generating the artifact inline where the prompt emitted a session
starter, for instance. Say so explicitly in the comment block's
`Instructions`, so the divergence reads as a decision rather than drift.

## Teaching Quality Bar
Before considering a prompt "done", verify:
1. A PM can use it to solve a real problem now.
2. A PM can learn at least one reusable prompt-writing pattern from it.
3. The flow reduces ambiguity and cognitive overload.
4. The output format is professional and actionable.
5. The prompt does not force users to pre-design the artifact the AI should help create.

## Naming, Placement, and Duplication
- Prefer lowercase-hyphen file names for new assets unless there is a strong curation reason not to.
- **Duplication across tiers is intentional and encouraged.** The same
  framework taught three ways serves three learners: a generator
  teaches the scoping decisions, a workshop teaches the facilitated
  conversation, a `prompts/` template delivers the finished artifact,
  a loop teaches the automation. TAM/SAM/SOM exists four times on
  purpose. Do not consolidate them.
- **Never convert one asset into a pointer to another.** A pointer is
  not a prompt; it is an errand. If two files genuinely do the same
  work in the same way for the same reader, delete one outright --
  do not leave a stub.
- What must not duplicate is the *decision*: two files should not
  require the reader to compare them before using either. See
  Coupling Discipline below.

## Coupling Discipline

**Forward pointers are free. Backward prerequisites are debt.**

A prompt is tightly coupled when the user cannot get a finished
artifact from it without first reading or running another file. That
costs an expert nothing and costs a novice everything: they hit the
fork at the exact moment they have the least ability to evaluate it,
with no artifact in hand. Every prerequisite is a place to quit.

- **Forward** -- "when you're done, this could feed a battle card."
  Belongs in **Final Step only**, always optional. Costs nothing,
  teaches the shape of the library. Write more of these.
- **Backward** -- "run X first," "this is the sibling of Y," "assumes
  context is already present in session." This is homework assigned
  before the user has anything. Do not write these.

**The test:** every asset must be describable, and runnable, without
naming another file above its Final Step block.

### Levels and tiers

| Level | Shape | Allowed in |
|---|---|---|
| 0 Standalone | Finishes the job alone; asks for what it needs | **Required** in `prompts/` and `skills/` |
| 1 Forward pointer | Names a next step, Final Step only | Anywhere |
| 2 Soft prereq | Better with a prior artifact, works without, says so | `prompt-generators/`, `workshops/`, `market-intelligence/`, `storytelling/` |
| 3 Hard gate | `STOP` unless a prior artifact exists | `loops/`, `vibes/` only |

`prompts/` is the novice floor: one file in, one finished artifact
out, every time. `loops/` and `vibes/` may gate hard because a loop is
machinery adopted *after* the manual version is understood, and a
batch job that runs on an empty index produces garbage at scale.

### Writing the metadata

- **Description** states what this file produces, in absolute terms.
  Never "the direct template version of X" or "the autonomous sibling
  of Y" -- a description that only parses in contrast to another file
  forces the reader to open both.
- **Usage Note** names a situation the reader can recognize from
  inside their own week ("the team disagrees about the category,"
  "estimation keeps turning into an argument"), not a taxonomy slot
  ("use when context is incomplete").
- **When NOT to Use** names *situations*, not alternative files. "You
  already know your scope and just want the number" is a situation.
  "Use the other prompt instead" is a referral.
- If a prompt has a fallback intake, say so ("it also runs cold").
  Do not claim a prerequisite the prompt does not actually have --
  fourteen files once claimed to require pre-loaded context while
  carrying a working three-question fallback.
- A required input is not a license to stall. Ask once, offer the
  best-guess bypass, then proceed with a labeled worked example. A
  stalled prompt teaches nothing.

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
- Preserve CC BY-NC-SA 4.0 licensing references and creator attribution (see LICENSE and LICENSING.md); never reintroduce MIT license text.

## Editing Guidance for Agents
- Make focused edits; avoid rewriting voice/style unnecessarily.
- Preserve pedagogic comments unless improving them.
- Do not remove learning-oriented structure just to shorten prompts.
- Favor compatibility across ChatGPT, Claude, and Gemini where practical.
- Keep output contracts stable for downstream tooling (for example Jira/ADO import conventions).

## Review Checklist (Pre-PR)
Run this quick check before finalizing:
1. Mission fit: practical + pedagogic value both improved.
2. Metadata block complete and useful, including `Standalone`.
3. Naming and placement follow directory intent.
4. Links and file references still resolve.
5. Coupling: no file named above the Final Step block; Description and
   Usage Note stand on their own without a sibling; anything in
   `prompts/` finishes the job cold.
6. Any code/doc mismatch resolved.
7. No burden-shifting questions; decision options are persona-first and context-aware.
8. `python3 scripts/validate-prompts.py` passes.

## PR Notes
In change summaries, include:
- What PM problem this helps solve
- What prompt-writing behavior this teaches
- Any framework choices and why they were used
- Any compatibility notes across AI assistants
