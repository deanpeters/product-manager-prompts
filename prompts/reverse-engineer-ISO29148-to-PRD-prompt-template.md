# reverse-engineer-ISO29148-to-PRD-prompt-template.md
<!--
## Description:
Creates a reusable PRD-generation prompt based on ISO 29148 principles,
focusing on stakeholder and business requirements in a structured format.

## Usage Note:
Assumes context is already present in session.

## Required Context Keys:
1. Product/business context and target stakeholder groups
2. Desired business outcomes and constraints
3. Scope boundaries and requirement priorities
4. Intended consumers of the resulting PRD

## Missing Context Rule:
If required keys are missing, ask at most 3 targeted questions, one at a time:
1. "What product and stakeholder groups should this ISO-29148 PRD template serve?"
2. "What business outcomes and constraints must be reflected?"
3. "Who is the primary audience for the generated PRD?"
Then proceed with clearly labeled assumptions.

## Instructions:
1. Preserve ISO-29148-inspired stakeholder and business requirement framing.
2. Keep sections AI-fillable and practical for PM workflows.
3. Emphasize clear requirement intent and validation readiness.
4. Render output as formatted Markdown in a code block.

## Pedagogic Notes:
- This trains PMs to separate stakeholder needs from solution details.
- Structured requirement framing improves traceability and alignment.
- AI-fillable templates accelerate drafting without losing rigor.

## Attribution:
Template for generating AI-fillable PRD prompts from ISO 29148 by Dean Peters,
24Mar24.

## Licensing:
MIT License

Date: March 2, 2026
-->

## Context

You are a product requirements assistant deriving a reusable PRD prompt from
ISO 29148 (stakeholder + business requirements orientation). Assume context is
present. If required context is missing, ask up to 3 targeted questions (one at
a time), then continue with labeled assumptions.

## Output Format

Render Markdown in a code block using this exact structure:

## ISO 29148-Derived PRD Prompt Template

### Instructions for Use
1. Paste this template into your AI assistant.
2. Provide product, stakeholder, and business context.
3. Ask AI to complete sections with explicit assumptions where needed.
4. Validate the output with product, engineering, and business partners.

### 1. Stakeholder Requirements Specification (StRS)
- **Purpose and Objectives**: [What stakeholders need to achieve]
- **Stakeholder Identification and Needs**: [Who the stakeholders are and what they need]
- **Operational Context**: [Environment and conditions of use]
- **Priority of Needs**: [Relative importance and urgency]

### 2. Business Requirements Specification (BRS)
- **Business Objectives**: [Strategic outcomes and constraints]
- **Market/Customer Requirements**: [External expectations driving requirements]
- **Value and Success Criteria**: [How business success will be measured]
- **Assumptions and Dependencies**: [Critical dependencies and risks]

### 3. Product Requirement Structure
- **Functional Requirements**: [Core capabilities and expected behavior]
- **Non-Functional Requirements**: [Quality attributes and operational needs]
- **Interface and Data Requirements**: [Inputs/outputs, integrations, data expectations]
- **Compliance and Policy Requirements**: [Regulatory and policy constraints]

### 4. Traceability and Validation
- **Requirement-to-Outcome Traceability**: [How each requirement links to outcomes]
- **Acceptance Criteria Guidance**: [How each requirement is validated]
- **Open Issues / Unknowns**: [What still needs evidence]

### 5. AI Fill Guidance
- **Required Inputs**: [Context required before generation]
- **Formatting Rules**: [Preferred structure and length]
- **Review Focus Areas**: [Sections requiring highest scrutiny]

### Assumptions to Validate
- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

## Final Step

Offer exactly 4 next options:
1. Generate a full PRD draft using this ISO-29148 template (Recommended)
2. Generate a stakeholder-only condensed requirements brief
3. Generate a business-case appendix tied to BRS sections
4. Generate a validation plan with tests per requirement cluster

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 4`, or a custom path.
