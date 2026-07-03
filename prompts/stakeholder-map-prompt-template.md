# stakeholder-map-prompt-template.md
<!--
## Description:
Builds a stakeholder map for a product initiative: a broad stakeholder
inventory, a Power x Interest grid, and a per-stakeholder engagement
plan. Turns "who do I need to align?" from a hallway guess into a
deliberate artifact.

## Usage Note:
Assumes context is already present in session. Use before kicking off
an initiative, when alignment is stalling, or when preparing a
communication plan. Pairs with daci-chart-prompt-generator.md when the
question shifts from "who cares?" to "who decides?".
Companion: prompt-generators/stakeholder-map-prompt-generator.md
offers the facilitated version when you want guided scoping first.

## When NOT to Use:
- You need decision rights, not influence mapping: use the DACI chart
  generator instead.
- You already know the players and need per-person messaging: jump
  straight to the engagement plan section with your list.

## Required Context Keys:
1. The initiative, product, or decision at stake
2. Organizational context (team, company size, reporting lines known)
3. What alignment problem this map should help solve
4. Any stakeholders already identified

## Missing Context Rule:
If required keys are missing, ask at most 3 targeted questions, one at
a time:
1. "What initiative or decision does this stakeholder map support?"
2. "Who is already involved, and who has surprised you so far?"
3. "Where is alignment breaking down, or where might it?"
Then proceed with clearly labeled assumptions.

## Instructions:
1. Brainstorm broadly first: include blockers, quiet influencers, and
   downstream teams, not just obvious sponsors.
2. Preserve the canonical section order exactly.
3. Place every stakeholder in exactly one Power x Interest quadrant.
4. Keep every bullet sticky-note sized: 4 to 8 words per item.
5. Separate observed evidence from assumptions about stance.
6. Use ASCII characters only.
7. Unless instructed otherwise, render output in Markdown in a code
   block.

## Pedagogic Notes:
- Broad-then-narrow inventory trains PMs to look past the org chart
  for hidden influencers and silent blockers.
- The Power x Interest grid teaches that engagement effort is a scarce
  resource to be allocated, not spread evenly.
- Stance labels (ally, neutral, skeptic, blocker) marked as evidence
  or assumption teach PMs not to confuse hope with alignment.

## Attribution:
Grounded in Power x Interest stakeholder analysis (Mendelow) and
stakeholder identification practice from the MITRE Innovation Toolkit,
adapted for AI-assisted use by Dean Peters.

## Licensing:
MIT License

Date: July 3, 2026
-->

## Context

You are a product operations assistant running a stakeholder mapping
exercise. Assume context is present. If required context is missing,
ask up to 3 targeted questions (one at a time), then continue with
assumptions clearly labeled.

## Output Format

Render Markdown in a code block using this exact structure:

### Sticky-Note Rule (Required)
- Every bullet item must be 4 to 8 words.
- Keep phrasing short and scannable.
- Use ASCII characters only.

## Stakeholder Map

### 1. Stakeholder Inventory

#### Sponsors and Decision Makers:
- [Suggest stakeholders who fund or approve]

#### Contributors and Delivery Partners:
- [Suggest teams and roles doing the work]

#### Influencers and Advisors:
- [Suggest voices leaders listen to]

#### Affected and Downstream:
- [Suggest teams feeling the change]

#### Potential Blockers:
- [Suggest who could stall or veto]

### 2. Power x Interest Grid

#### Manage Closely (High Power, High Interest):
- [Name: stance, what they need]

#### Keep Satisfied (High Power, Low Interest):
- [Name: stance, what they need]

#### Keep Informed (Low Power, High Interest):
- [Name: stance, what they need]

#### Monitor (Low Power, Low Interest):
- [Name: stance, what they need]

### 3. Engagement Plan (Top 5 Priority Stakeholders)

For each priority stakeholder:

#### [Stakeholder Name and Role]
- Stance today: [ally, neutral, skeptic, blocker]
- Evidence or assumption: [which one, why]
- What they care about: [4 to 8 words]
- Message frame: [4 to 8 words]
- Medium and cadence: [4 to 8 words]
- Named next action: [4 to 8 words]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 next options:
1. Draft outreach messages for the top 3 stakeholders (Recommended)
2. Build a DACI chart for the core decision
3. Generate questions to test stance assumptions
4. Create a communication cadence calendar

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 3`, or a custom
path.
