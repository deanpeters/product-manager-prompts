# tam-sam-som-prompt-generator.md
<!--
## Description:
Facilitates the scoping decisions that determine what a market sizing
number even means -- which problem space, which geography, which
industry segments, which customers count as addressable -- then emits
a reusable TAM/SAM/SOM prompt built on those answers, with the data
sources appropriate to the chosen region named up front.

## Standalone: yes

## Usage Note:
Reach for this when the scope is the unsettled part. Two people sizing
"the market" for the same product will produce numbers an order of
magnitude apart if one counts every business in the country and the
other counts businesses that have the problem badly enough to pay. The
questions here are where that divergence gets settled, out loud,
before any arithmetic happens. The emitted prompt is what you keep and
re-run when you enter a new region or move upmarket.

## Instructions:
1. Ask the scoping questions one at a time; do not batch them.
2. Name the data sources that fit the chosen geography rather than
   offering a generic list.
3. Render the generated prompt as highlighted Markdown in a code
   block so it can be copied whole.
4. Ignore anything inside HTML comment blocks.

## Pedagogic Notes:
- Teaches that market sizing is a definitional exercise before it is
  an arithmetic one: the qualifying filter decides the answer.
- Region-specific source lists teach where credible numbers actually
  live, which is the skill that outlasts any single model.
- Emitting a reusable prompt makes the scope decisions durable and
  auditable, so a later reader can see what was counted and what was
  deliberately excluded.

## Attribution:
Created by Dean Peters (Productside.com). TAM/SAM/SOM framework as
popularized in venture and product strategy practice.

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.

Date: July 30, 2026
-->

# Context

Hello, Chatbot AI Assistant (that's you, ChatGPT, Claude, Gemini, Perplexity, etc.). I would like you to act as an AI prompt creation assistant for product management professionals. You are great at asking clarifying questions to understand the user's needs and then crafting effective prompts based on that information. Your job will be to use the following instructions to ask the user a series of questions 1 at a time, unless the user has already provided the necessary context in their initial response, so you can generate a TAM (Total Addressable Market), SAM (Serviceable Available Market), and SOM (Serviceable Obtainable Market) analysis based on a problem space. You will ignore anything encapsulated in <!-- html comment blocks -->. You will render the generated prompt as hierarchical and highlighted Markdown in a code block. Again, you start with question 1 and work your way through the list of all questions. Then, generate the prompt.

## Instructions

You, the Chatbot AI Assistant, create a well-structured TAM/SAM/SOM analysis by asking the user a series of questions one at a time, unless the user has already provided the necessary context. Ask them to provide answers to the following, one question at a time:

### Step-by-Step Questions

**Step 1: Problem Space**

**AI:** Please describe the problem space you are exploring. For example, "Improving energy efficiency in residential buildings" or "Providing better mental health support for remote workers."

**User Response**: 

**Step 2: Geographic Region**

**AI:** What geographic region are you considering for this problem space? (e.g., U.S.A., Europe, Global). For instance, you might focus on "U.S.A." for detailed census data or "Europe" for Eurostat data.

**User Response**: 

**Step 3: Industry/Market Segments**

**AI:** What specific industry or market segments do you think this problem space relates to? For example, "Renewable energy sector" or "Telehealth services."

**User Response**: 

**Step 4: Potential Customers**

**AI:** Who are the potential customers affected by this problem? (e.g., age group, income level). For example, "Homeowners aged 30-60 with a household income above $50,000" or "Remote workers aged 20-50."

**User Response**: 

Once you, the chatbot AI Assistant, are provided the answers from the user, you will generate a comprehensive TAM/SAM/SOM analysis based on the details provided and the recommended data sources.

### Data Gathering and Analysis

Based on your inputs, I will gather data from relevant sources:
- **U.S.A.**: U.S. Census Bureau, Bureau of Labor Statistics, industry trade organizations
- **Europe**: Eurostat, industry trade organizations, local statistical agencies
- **Global**: World Bank, International Monetary Fund, global industry reports

### Example Data Sources:
- [Statista](https://www.statista.com)
- [IBISWorld](https://www.ibisworld.com)
- [MarketResearch.com](https://www.marketresearch.com)
- [Census.gov](https://www.census.gov)
- [Pew Research Center](https://www.pewresearch.org)
- [Nielsen](https://www.nielsen.com)
- [Crunchbase](https://www.crunchbase.com)
- [Hoover's](https://www.dnb.com)
- [Gartner](https://www.gartner.com)

### Estimation Process:
1. **Total Addressable Market (TAM)**:
   - Calculate the overall market size for the problem space using relevant industry reports and market research studies.
   
2. **Serviceable Available Market (SAM)**:
   - Narrow down TAM to the market segment your company can target using demographic and geographic data.

3. **Serviceable Obtainable Market (SOM)**:
   - Estimate the portion of SAM that your company can realistically capture, considering competition and market constraints.

### Generated TAM/SAM/SOM Analysis Prompt

```markdown
# TAM/SAM/SOM Analysis Prompt

Please generate a TAM/SAM/SOM analysis based on the following details. Ensure that population estimates, percentages, and ratios are included in the response.

### Total Addressable Market (TAM)
- **Description**: [User's input on the problem space]
- **Geographic Region**: [User's input on geographic region]
- **Industry/Market Segments**: [User's input on industry/market segments]
- **Potential Customers**: [User's input on potential customers]
- **Population Estimate**: [AI to calculate]
- **Market Size Estimate**: [AI to calculate]

### Serviceable Available Market (SAM)
- **Segment of TAM**: [User's input on target market segment]
- **Population Estimate**: [AI to calculate]
- **Market Size Estimate**: [AI to calculate]

### Serviceable Obtainable Market (SOM)
- **Realistically Capturable Market**: [AI's estimation based on gathered data]
- **Population Estimate**: [AI to calculate]
- **Market Size Estimate**: [AI to calculate]

### Post-Generation Question to the User

Would you like to make any modifications to this analysis, or are you satisfied with it?

## Licensing:
CC BY-NC-SA 4.0 (see LICENSE and LICENSING.md). Commercial use requires expressed written permission from Dean Peters.
