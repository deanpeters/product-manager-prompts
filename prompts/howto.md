# HOWTO.md: How to Create Effective Prompts for AI Assistants

This README provides guidance on crafting structured, impactful prompts for **Generative AI Assistants** (e.g., ChatGPT, Claude, Gemini). These prompts act as directives, ensuring the AI understands the context, performs specific actions, and generates high-quality, actionable outputs tailored to the needs of end users like product managers.

---

## **Overview**

These prompts are designed primarily for the **AI Assistant**, guiding it to produce outputs that align with user goals. By leveraging clear instructions, structured frameworks, and context-rich input, the AI can act as a powerful collaborator in solving complex problems.

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
  - **Instructions**: Guides how to engage with the AI.
  - **Attribution & Licensing**: Documents authorship and ethical guidelines for usage.

### **2. Fill-in-the-Blank Placeholders**
Fill-in-the-blank elements manifest in two ways:
- **User-Provided Input Prompts**: The user provides titles, categories, or list items, and the AI generates descriptions or sub-elements dynamically.  
  Example:  
  * **List Item, Title or Category the User Provides** - [short description of the list item in 9 words or less that ChatGPT fills out].

- **AI-Generated Output Prompts**: The AI generates both titles or categories and their corresponding descriptions.  
  Example:  
  * **[list item label or title that ChatGPT fills out]** - [short description of the list item in 9 words or less that ChatGPT fills out].

### **3. Markdown Template**
- **AI Instructions**: The template communicates directly with the AI, using placeholders for inputs the AI should consider.
- **Output Structure**: Includes formatting (e.g., Markdown, code blocks, or bullet points) to standardize AI-generated outputs.
- **Iterative Refinement Prompts**: Guides the AI to ask for missing details or refine its responses to improve collaboration.

---

## **How to Use the Template**

### **Step 1: Define the AI’s Role**
- Identify the task you want the AI Assistant to perform (e.g., creating a positioning statement, framing a problem).
- Clearly articulate the **end user’s goals** and how the AI’s output will address those goals.

### **Step 2: Add Metadata Comments**
- Use `<!-- comments -->` to include metadata such as the purpose, instructions, and licensing.
- Add a note within the comments explicitly telling the AI to ignore all content in `<!-- comments -->`.

### **Step 3: Write Fill-in-the-Blank Prompts**
- Use placeholders for:
  1. **User-Provided Inputs**: Clearly mark fields the user must provide for AI processing.
  2. **AI-Generated Content**: Include fields where the AI generates both titles/categories and descriptions.

### **Step 4: Test and Refine**
- Run the prompt with your chosen AI Assistant to ensure clarity and effectiveness.
- Ensure the AI properly ignores the metadata comments and generates relevant outputs.

---

## **Generic Prompt Template**

Here’s the updated template, incorporating metadata comments, explicit AI instructions, and fill-in-the-blank elements:

---

```markdown
# [File Name].md
<!-- 
## Description:
[Provide a brief explanation of the task the AI Assistant will perform. Highlight its relevance to the end user and any methodologies or frameworks it follows.]

## Usage Note:
[Detail what the AI needs to know before running the prompt. Include context, user goals, or data prerequisites that will enrich the AI’s response.]

## Instructions:
1. [Step-by-step guidance for the AI Assistant to process inputs. Include instructions for iterative refinement (e.g., "If context is insufficient, ask for clarification").]
2. [Explicitly instruct the AI to ignore all content within `<!-- comments -->`.]

## Attribution:
[Include the creator's name, date, and any sources of inspiration. Provide proper credit to original methodologies or frameworks.]

## Licensing:
[Specify licensing terms, such as MIT License, to encourage ethical use and modification.]

Date: [Insert Date]
-->
---
```markdown
## [Template Title]

<!--
[Explain the AI’s role in this section, such as how it should interpret inputs and generate outputs.]
-->

### [Section 1 Title]

<!-- [Describe the purpose of this section and include placeholders for inputs the AI will process.] -->
* **[list item label or title the user provides]** - [short description of the list item in 9 words or less that ChatGPT fills out].

### [Section 2 Title]

<!-- [Guide the AI to process specific subcategories or dimensions in this section.] -->
#### [Subsection Title]
* **[list item label or title that ChatGPT fills out]** - [short description of the list item in 9 words or less that ChatGPT fills out].

### [Final Section Title]

<!-- [Summarize the AI’s output in a format suitable for end users, such as concise bullet points or narratives.] -->
* **[summary label generated by ChatGPT]** - [short description or insight in 9 words or less].
```

---

## **Best Practices for Writing Prompts**

1. **Direct AI Instructions**: Write prompts as if speaking directly to the AI, specifying what it should do and how to format the output.
2. **Use Metadata Comments (`<!-- -->`)**: Include necessary context, instructions, and attribution in comments and explicitly tell the AI to ignore these during execution.
3. **Context-Rich Inputs**: Ensure the AI has all the necessary background information to generate relevant responses.
4. **Iterative Refinement**: Encourage the AI to ask clarifying questions or adjust its output based on new input.
5. **Outcome-Focused**: Design prompts to deliver actionable, user-centered results, such as frameworks, analyses, or recommendations.
6. **Leverage Fill-in-the-Blank Fields**: Use placeholders strategically for both:
   - User-provided inputs.
   - AI-generated titles, categories, and descriptions.
7. **Modular Organization**: Break content into clear sections to make it easier for the AI to follow instructions and produce structured outputs.

---

## **Example Prompts**

- [Jobs-to-be-Done Template](jobs-to-be-done.md)
- [Problem Framing Statement Template](framing-the-problem-statement.md)
- [Positioning Statement Template](positioning-statement.md)
- [Backlog Epic Hypothesis Template](backlog-epic-hypothesis.md)

---

## **Contributing**

If you create prompts using this template, feel free to submit them as pull requests to this repository. Ensure your prompts:
- Include clear metadata for the AI.
- Use fill-in-the-blank placeholders effectively.
- Follow the modular structure of the generic template.
- Provide actionable, structured outputs for end users.

---

## **License**

This repository and its contents are licensed under the MIT License, allowing free use, modification, and distribution with proper attribution.
```

