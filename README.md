<a id="pmprompts"></a>
# Product Manager Prompts for Generative AI

```text
╔═════════════════════════════════════════════════════════════════════════╗
║                                                                         ║
║   ██████╗ ███╗   ███╗    ██████╗ ██████╗  ██████╗ ███╗   ███╗██████╗ ████████╗███████╗
║   ██╔══██╗████╗ ████║    ██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗╚══██╔══╝██╔════╝
║   ██████╔╝██╔████╔██║    ██████╔╝██████╔╝██║   ██║██╔████╔██║██████╔╝   ██║   ███████╗
║   ██╔═══╝ ██║╚██╔╝██║    ██╔═══╝ ██╔══██╗██║   ██║██║╚██╔╝██║██╔═══╝    ██║   ╚════██║
║   ██║     ██║ ╚═╝ ██║    ██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║        ██║   ███████║
║   ╚═╝     ╚═╝     ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝        ╚═╝   ╚══════╝
║                                                                         ║
║   97 practical prompt assets for AI-assisted product management         ║
║   ChatGPT • Claude • Copilot • Gemini • and others                      ║
║                                                                         ║
║   Community Build v2.1 • July 3, 2026 • MIT License                     ║
╚═════════════════════════════════════════════════════════════════════════╝
```

**Practical AI tools for both the strategic thinking and the daily execution of product management — that also teach you to prompt better while you use them.**

Every asset here works by copy-paste into ChatGPT, Claude, Gemini, Copilot, or any AI assistant. No installs, no accounts, no framework. Pick the problem you're solving, grab the prompt, go.

_(Looking to equip an AI agent rather than a chat session? See the companion [Product Manager Skills](https://github.com/deanpeters/Product-Manager-Skills#pmskills) repo.)_

---

## Start With Your Problem

### "I need this artifact, and I have my context ready"

You know the situation; you want execution-quality output in one pass. Go to **[/prompts/](prompts/)**:

- Write a PRD from your discovery notes → [prd-prompt-template](prompts/prd-prompt-template.md)
- Understand what customers actually need → [jobs-to-be-done](prompts/jobs-to-be-done.md)
- Map who matters and how to engage them → [stakeholder-map](prompts/stakeholder-map-prompt-template.md)
- Decode what an inbound ask really wants → [incoming-request-breakdown](prompts/incoming-request-breakdown.md)
- Kill the launch on paper before reality does → [premortem](prompts/premortem-prompt-template.md)
- Write user stories engineers don't hate → [user-story](prompts/user-story-prompt-template.md)
- Frame an initiative as testable hypotheses → [lean-ux-canvas](prompts/lean-ux-canvas-prompt-template.md)
- Design an agentic AI system responsibly → [agent-strategy-canvas](prompts/agent-strategy-canvas-prompt-template.md)
- Save this session's context for the next one → [session-saver](prompts/session-saver-prompt.md)

### "I need to think it through — facilitate me"

You have a fuzzy situation and want a guided working session that ends in the finished deliverable. Go to **[/workshops/](workshops/)**:

- Competitive battle card → [battle-card-workshop](workshops/battle-card-workshop.md)
- PRD, section by section with checkpoints → [prd-workshop](workshops/prd-workshop.md)
- Opportunity solution tree + first experiment → [opportunity-solution-tree-workshop](workshops/opportunity-solution-tree-workshop.md)
- Build / don't-build business case with the math shown → [feature-investment-workshop](workshops/feature-investment-workshop.md)
- Problem statement + "How might we" → [problem-framing-canvas-workshop](workshops/problem-framing-canvas-workshop.md)
- Structured user-pain research table → [painstorming-workshop](workshops/painstorming-workshop.md)

### "I need evidence about the market, not another meeting"

The answers live on the public web, and the AI should do the fieldwork — with citations, labeled inference, and no invented facts. Go to **[/market-intelligence/](market-intelligence/)**:

- Map a market's players and whitespace → [market-landscape-scan](market-intelligence/market-landscape-scan-prompt.md)
- Research a competitor set, just-enough style → [competitive-research-snapshot](market-intelligence/competitive-research-snapshot-prompt.md)
- Watch competitors on a schedule; report only material shifts → [competitive-intel-watch](market-intelligence/competitive-intel-watch-prompt.md)
- Mine reviews and forums for unmet needs → [voice-of-customer-miner](market-intelligence/voice-of-customer-miner-prompt.md)
- Size a market with citations, bottom-up → [tam-sam-som-analysis](market-intelligence/tam-sam-som-analysis-prompt.md)
- Build an evidence-cited battle card → [battle-card-builder](market-intelligence/battle-card-builder-prompt.md)
- SWOT a company with sources, not vibes → [swot-analysis](market-intelligence/swot-analysis-prompt.md)
- Read an industry's structure and power → [porters-five-forces](market-intelligence/porters-five-forces-prompt.md)
- Map growth options with evidence per quadrant → [ansoff-matrix](market-intelligence/ansoff-matrix-prompt.md)

These are built to run unattended — in agent workflows, loops, and scheduled runs — with question budgets, materiality bars, and stop conditions.

### "I need people to *get it*"

Evidence doesn't persuade; stories do. Go to **[/storytelling/](storytelling/)**:

- Turn research into a stakeholder narrative → [Research-to-Narrative Bridge](storytelling/Generator%20-%20Research-to-Narrative%20Bridge.md)
- Visual storyboards, hero's journeys, Starts-with-Why arcs → [browse the directory](storytelling/)

### "I run prompts as loops, goals, batches, or routines"

You still have to prompt the loop — nobody skipped that step, they just put a slash in front of it. Go to **[/loops/](loops/)** for seasoned recipes at three levels (plain commands → plain-English controls → Just Enough Jinja2):

- Split epics until nothing splits, with a pass ceiling → [story-splitting-loop](loops/story-splitting-loop.md)
- Draft a PRD section by section, in dependency order → [prd-section-loop](loops/prd-section-loop.md)
- Batch a backlog of epics without contaminating it → [epic-story-batch](loops/epic-story-batch.md)
- Synthesize research one category at a time → [research-synthesis-loop](loops/research-synthesis-loop.md)
- Run a versioned competitive watch that won't drift → [competitive-watch-routine](loops/competitive-watch-routine.md)
- SWOT a competitor set with receipts, not vibes → [swot-batch](loops/swot-batch.md)
- Size a market one segment at a time → [market-sizing-loop](loops/market-sizing-loop.md)

### "I want to build my own prompts — or my own agents"

- Learn the patterns by using the meta-prompts in **[/prompt-generators/](prompt-generators/)** — each one interviews you, then emits a reusable prompt
- Design a custom research agent → [research-agent-prompt-generator](prompt-generators/research-agent-prompt-generator.md)
- Study the pattern documents (below), then the exemplars in **[/vibes/](vibes/)** for loop-safe, agent-ready prompt structures
- Reverse-engineer how any prompt works → **[/skeletons/](skeletons/)**

### "I need to laugh so I don't cry"

**[/resumes-resignations-reactions/](resumes-resignations-reactions/)** — therapeutic workplace satire. You've earned it.

**Can't find it?** The generated **[catalog](catalog/INDEX.md)** lists every asset with a one-line description.

---

## How These Prompts Work (and Teach)

Three interaction modes power everything here — documented in **[interaction-modes.md](interaction-modes.md)**:

1. **Facilitation** (*you* hold the context): the AI asks a budgeted 3–5 questions, one at a time, offering 3 context-aware recommendations plus "Other" — with standing escape routes ("take your best guess", or paste your notes to skip ahead). Spec: **[generative-guidance-pattern.md](generative-guidance-pattern.md)**.
2. **Checkpointed co-construction** (*an artifact* holds the structure): the AI builds section by section against your template, stopping at a gate after each; gaps are labeled **Assumption** or **Open Question**, never invented.
3. **Autonomous investigation** (*the world* holds the context): the AI researches under an evidence contract — search plan shown first, real URLs, Fact / Inference / Assumption labels, and defaults that let it proceed when nobody's answering.

Prompts meant to run repeatedly — under loop or goal commands, or inside agents — use Jinja2 notation for explicit, bounded control flow: **[jinja2-prompt-structures.md](jinja2-prompt-structures.md)**.

### The teaching layer: view the raw code

Every prompt carries an HTML comment block (`<!-- ... -->`) with its Description, Usage Note, When NOT to Use, and Pedagogic Notes — the instructor's notes explaining *why* the prompt works. GitHub's pretty preview hides them, so click **Raw** and copy everything, comments included. The AI ignores them; you shouldn't.

### From user to builder to teacher

1. **Use** the prompts on real work
2. **Read the comments** to see why they're shaped that way
3. **Customize** for your industry and team
4. **Build your own** with the generators and pattern docs
5. **Contribute back** — see [SUBMISSIONS-GUIDE.md](SUBMISSIONS-GUIDE.md)

---

## For Engineers and Agents Improving This Repo

- **[CLAUDE.md](CLAUDE.md)** / **[AGENTS.md](AGENTS.md)** — the authoring contract, directory intent, and quality bar for AI-assisted sessions
- **[prompting-style-guide.md](prompting-style-guide.md)** — the full methodology
- **`scripts/validate-prompts.py`** — structural checks (required metadata, v2 fixtures, companion-link resolution); errors block, warnings are the migrate-on-touch worklist
- **`scripts/generate-catalog.py`** — regenerates `catalog/` from the metadata comment blocks (the blocks are the source of truth; the catalog is derived output)
- **[CHANGELOG.md](CHANGELOG.md)** — what changed in each version and what's deliberately left open

Run both scripts after any prompt edit. Existing v1-pattern prompts are grandfathered: migrate them to v2 when you touch them, and never mass-rewrite.

---

## Contributing

Real problems, tested prompts, teaching comments. Start with **[SUBMISSIONS-GUIDE.md](SUBMISSIONS-GUIDE.md)**, then:

```bash
git clone https://github.com/deanpeters/product-manager-prompts.git
git checkout -b your-improvement-name
# make your changes, then:
python3 scripts/validate-prompts.py
python3 scripts/generate-catalog.py
# commit, push, open a pull request
```

Test across ChatGPT, Claude, and Gemini. Humans make the strategic decisions; AI assists.

---

## Resources and Contact

- **[Productside Workshops](https://www.productside.com/courses/ai-innovation-for-product-managers/)** — live training to go deeper
- **Questions?** Open an [issue](https://github.com/deanpeters/product-manager-prompts/issues)
- **Connect:** [Dean Peters on LinkedIn](https://www.linkedin.com/in/deanpeters/)

## License

Licensed under the [MIT License](https://choosealicense.com/licenses/mit/). Use freely, modify openly, and share knowledge generously.

*Created by [Dean Peters](https://github.com/deanpeters) • Built for the product management community • Designed to teach through doing*
