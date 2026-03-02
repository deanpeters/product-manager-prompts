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
- `prompt-generators/`: Meta-prompts that help users build prompts.
- `storytelling/`: Narrative, visual, and communication-oriented prompt assets.
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

## Tooling and Safety
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
