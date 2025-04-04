# HOWTO.md: How to Create Effective Prompts for AI Assistants

This README provides guidance on crafting structured, impactful prompts for **Generative AI Assistants** (e.g., ChatGPT, Claude, Gemini, CoPilot, DeepSeek, Grok). These prompts act as **directives to the AI**, ensuring it understands the context, performs specific actions, and generates high-quality, actionable outputs tailored to the needs of end users like product managers.

---

## **Overview**

These prompts are written **for the AI Assistant to follow directly**, guiding it to produce outputs that align with user goals. By leveraging clear instructions, structured frameworks, and context-rich input, the AI can act as a powerful collaborator in solving complex problems.

Two critical characteristics of a well-formed prompt:
1. Prompts must be **explicitly directed at the AI Assistant**, not the human user.
2. Prompts must include **baked-in fallback questions** that the AI will ask if essential data (e.g., persona name, product, context) is not available in the current session.

A critical feature of these prompts is the use of:
1. **Fill-in-the-blank placeholders** for both user-provided inputs and AI-generated content.
2. **Metadata comments (`<!-- -->`)** that include essential information for the user while ensuring the AI ignores them during execution.

---

## **Key Components of the Template**

The generic template includes the following sections:

### **1. Metadata Section in Comments (`<!-- -->`)**
- **Purpose**: Store essential information about the prompt (e.g., its purpose, usage notes, instructions) in comments that are ignored by the AI Assistant. This ensures clarity for users without disrupting AI execution.
- **AI Instructions**: Include a note explicitly telling the AI to ignore all content within `<!-- comments -->`.
- **Contents**: Metadata typically includes:
  - **Description**: Explains the purpose and task of the prompt.
  - **Usage Note**: Details prerequisites or instructions for users to prepare context for the AI.
  - **Instructions**: Guides how the AI should behave and respond.
  - **Attribution & Licensing**: Documents authorship and ethical guidelines for usage.

> ✅ **New Requirement**: Metadata must specify which **fallback questions** the AI should ask if critical data is not available in the current session.

### **2. Fill-in-the-Blank Placeholders**
Fill-in-the-blank elements manifest in two ways:
- **User-Provided Input Prompts**: The user provides titles, categories, or list items, and the AI generates descriptions or sub-elements dynamically.  
  Example:  
  * **List Item, Title or Category the User Provides** - [short description of the list item in 9 words or less that ChatGPT fills out].

- **AI-Generated Output Prompts**: The AI generates both titles or categories and their corresponding descriptions.  
  Example:  
  * **[list item label or title that ChatGPT fills out]** - [short description of the list item in 9 words or less that ChatGPT fills out].

### **3. Markdown Template**
- **AI Instructions**: The prompt should always speak **directly to the AI**, using action verbs and clear directives.
- **Output Structure**: Includes formatting (e.g., Markdown, code blocks, or bullet points) to standardize AI-generated outputs.
- **Fallback Questions Logic**: If key context is missing, the prompt should tell the AI:
  1. Pause before generating output.
  2. Ask up to 3 specific, well-phrased questions to get the missing inputs.
  3. Resume generating the output once the answers are provided.

---

## **How to Use the Template**

### **Step 1: Define the AI’s Role**
- Identify the task the AI Assistant is expected to perform (e.g., generating a positioning statement, framing a problem).
- Write the prompt **as if giving instructions to the AI Assistant**—not to the human user.
- Clearly articulate the **end user’s goals** and how the AI’s output will serve them.

### **Step 2: Add Metadata Comments**
- Use `<!-- comments -->` to include metadata such as the purpose, usage notes, fallback question logic, and licensing.
- Add a note within the comments explicitly telling the AI to ignore all content inside `<!-- -->`.

### **Step 3: Write Fill-in-the-Blank Prompts**
- Use placeholders for:
  1. **User-Provided Inputs**: Mark required inputs clearly.
  2. **AI-Generated Content**: Indicate areas where the AI fills in sections dynamically.

### **Step 4: Include Fallback Questions**
- Instruct the AI what to ask if required context is not present.
- Limit to 2–4 targeted, easy-to-answer questions.
- Place these instructions in both the metadata and body of the prompt.

### **Step 5: Test and Refine**
- Run the prompt in a live AI Assistant to ensure:
  - Metadata is ignored properly.
  - The AI follows the output format.
  - It pauses and asks fallback questions when needed.
  - Output is accurate and user-centered.

---

## **Generic Prompt Template**

~~~markdown
# [File Name].md
<!-- 
## Description:
[State the AI’s task and why it matters to the user.]

## Usage Note:
If any of the following are missing from session context — [Required Data A], [Required Data B], [Required Data C] — the AI must pause and ask the user:
1. [Clarifying Question 1; if needed]
2. [Clarifying Question 2; if needed]
3. [Clarifying Question 3; if needed]
4. [Clarifying Quesiton 4; if needed]

## Instructions:
1. You are an AI Assistant. Follow the instructions below to generate a high-quality output.
2. If any required data is missing, ask the user for it before generating output.
3. Use Markdown for structure and keep content clear, concise, and actionable.
4. Ignore all content within `<!-- comments -->`.

## Attribution:
[Creator, inspiration sources, methodology used.]

## Licensing:
MIT License

Date: [Insert Date]
-->
---
```markdown
## [Template Title]

### [Section 1 Title]

* **[User input label]** - [AI generates this description or response].

### [Section 2 Title]

* **[Another item AI generates]** - [Short, helpful response].

### [Optional Summary]

* **[Summary point]** - [Brief insight generated by AI].
```
~~~

---

## **Best Practices for Writing Prompts**

1. **Direct AI Instructions**: Always speak to the AI Assistant. Be clear about its role and output requirements.
2. **Use Metadata Comments**: Provide instructions, fallback logic, and attribution outside the visible execution path.
3. **Fallback Question Design**: Anticipate missing info and design 2–4 strategic questions the AI can ask to close gaps.
4. **Test in Multiple Assistants**: Ensure prompts run cleanly in ChatGPT, Claude, Gemini, CoPilot, etc.
5. **Structure with Markdown**: Use tables, bullets, and headers to shape well-structured, scannable outputs.
6. **Outcome-Focused**: Keep the end user’s goal front and center.
7. **Iterate Often**: Prompt quality improves with usage, so test and refine regularly.

---

## **Example Prompts**

- [Jobs-to-be-Done Template](jobs-to-be-done.md)
- [Problem Framing Statement Template](framing-the-problem-statement.md)
- [Customer Jobs Map Template](customer-jobs-map.md)
- [Backlog Epic Hypothesis Template](backlog-epic-hypothesis.md)

---

## **Contributing**

Want to add your own prompt? Please ensure:
- All prompts are AI-directed.
- Fallback questions are built in.
- Structure is modular and markdown-formatted.
- Prompts solve a real problem for product managers, teams, or educators.

---

## **License**

This repository and its contents are licensed under the MIT License, allowing free use, modification, and distribution with proper attribution.
