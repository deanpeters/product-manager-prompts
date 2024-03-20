# user-story-prompt-template.md
<!-- 
## Description:
Inspired by Mike Cohn's user story use case and the Gherkin Acceptance Criteria formats, this template is designed to help product managers and development teams create clear, concise user stories. It guides the formulation of user stories, ensuring they are structured to promote understanding and actionable outcomes. This template is particularly useful during Generative AI sessions, assuming enough product details, persona insights, positioning, and problem contexts have already been provided.

## Usage Note:
It is ideal for use in Generative AI sessions where comprehensive background information (product details, personas, positioning, and problems) has already been established. This ensures that the user stories generated are grounded in the project's context and objectives.

Before using this template in a Generative AI session, ensure your session has the following context already in place:

1. **Product Overview**: A detailed description of the product or feature for which the user story is being created.
2. **Target User Persona**: Insights into who the user is, including their goals, needs, and pain points.
3. **Product Goals**: The objectives that the product or feature aims to achieve.
4. **Competitive Landscape**: An understanding of similar offerings in the market and how the product stands out.

After ensuring the above context is provided, proceed with the following steps:

1. Copy the User Story Format/Template section below.
2. Enter the prompt: "Based on the context provided, please create a user story titled 'Feature XYZ' using the following User Story Template, rendered as Markdown in a Code Block."
3. Paste the User Story Format/Template into the session, replacing placeholder text with specific details related to 'Feature XYZ'.

This approach ensures that the user story generated is contextually rich, focused, and aligned with the product's objectives and user needs.

## Attribution:
Created by Dean Peters, March 14, 2024.
Inspired by [Mike Cohn's User Story Use Case Format](https://www.mountaingoatsoftware.com/agile/user-stories)
and the [Gherkin Acceptance Criteria](https://mvwi.co/posts/gherkin-cucumber)

## Licensing:
This template is licensed under the MIT License. It can be freely used, modified, and distributed with attribution to the original creator.

Date: March 14, 2024
-->
---
## User Story Format Prompt Template

<!--
The following format combines the Mike Cohn User Story Format augmented by a Gherkin-style acceptance criterion.
-->

### User Story [User Story Number ID]:

- **Summary**: [brief, memorable, human-readable story title with how we're providing value to the persona]

#### Use Case:
- **As a** [user name if available, otherwise user persona, otherwise user role or title],
- **I want to** [action user takes to get to outcome],
- **so that** [desired outcome by the user].

#### Acceptance Criteria:
<!-- 
Note 1: Givens are pre-conditions, so don't feel limited to just 3 Givens.
Note 2: There should only be one "When" and one "Then" statement that aligns with the use case's "I want to" action and "so that" outcome. 
Note 3: Multiple "when" and "then" are good indicators that a story must be split; see `user-story-splitting-prompt-template.md`
-->
- **Scenario**: [brief, human-readable user scenario with how we're providing value to the persona]
- **Given**: [Initial context or precondition]
- **and Given**: [additional context or preconditions based on the user's context]
- **and Given** [additional context or preconditions that support the 'Use Case' as needed]
- **and Given** [additional user interface-focused context or preconditions that ensure the 'When' event can happen]
- **and Given** [additional outcomes-focused context or preconditions that ensure the 'Then' outcome is delivered]
- **When**: [Event occurs that is connected to the use case action]
- **Then**: [Expected outcome that is connected to the user case outcome]
