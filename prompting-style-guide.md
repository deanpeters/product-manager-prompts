# Prompt Generation for Product Managers Style Guide 

## Purpose:
This guide is designed to help create effective and structured prompts for Generative AI sessions, particularly when working on tasks that require creative problem-solving, ideation, or detailed analysis. It provides a framework for ensuring that the AI-generated content is focused, relevant, and actionable.

## Steps for Prompt Generation:

### 1. Define the Context:
   - **Task or Objective:** Clearly state the task or objective you want to accomplish (e.g., exploring a problem space, crafting a positioning statement).
   - **Target Audience or Focus:** Specify the relevant focus, such as the customer segment, product, or specific problem area.
   - **Scope of Inquiry:** Determine the areas or aspects the prompt should cover (e.g., functional needs, emotional motivations, key challenges).

### 2. Use the [Fill in the Blanks] Structure:
   - **Overview:** Begin with a high-level description of the template's purpose and how it should be used. 
   - **Specific Instructions:** Incorporate instructions within `<!-- comment blocks -->` to guide the AI in generating content. Use the [fill in the blanks] method to prompt detailed and context-relevant outputs.

   **Example Structure:**
   ```Markdown
   # template-name.md
   <!-- 
   ## Description:
   Briefly describe the template’s purpose and how it should be used in a Generative AI session.

   ## Usage Note:
   Provide any specific context or information that should be included before the prompt is used.

   ## Instructions:
   Detail the steps for running the prompt, focusing on what needs to be generated.

   ## Attribution:
   Created by [Your Name], [Date].

   ## Licensing:
   This document and the template contained within are licensed under the MIT License, allowing free use, modification, and distribution with proper attribution.

   Date: [Date]
   -->
   ---
   ```markdown
   ## Template Section
   * **[Title/Topic]**: [Detailed instructions for filling in the content based on the context provided.]
   ```
   ```

### 3. Incorporate Bullet Points and Descriptions:
   - **Bullet Points:** Use bullet points to organize content clearly.
   - **Title and Description:** Each bullet should have a title or topic followed by a description or instruction that tells the AI what kind of content to generate.

   **Example:**
   ```Markdown
   ### 1. Section Title
   * **[Topic Title]**: [Instruction for AI on what to generate based on the context.]
   ```

### 4. Think Like a Product Manager:
   - **Focus on Outcomes Over Outputs:** Design prompts that focus on generating content that emphasizes the 'who' and 'why' (the outcomes) rather than just the 'how' (the outputs).
   - **Customer-Centric Approach:** Ensure prompts guide the AI to uncover deeper customer insights, such as needs, pains, and gains, rather than just technical details.

### 5. Maintain Consistency with Prompts:
   - **Consistent Structure:** Use a similar format across different prompts to maintain consistency and reliability in the outputs.
   - **Reusability:** If a prompt format works well, consider reusing or adapting it for different tasks to maintain focus and efficiency.

## Example Application:

Here’s an example of how you might apply this guide to create a prompt for exploring Jobs-to-be-Done:

```Markdown
# jobs-to-be-done.md
<!-- 
# Description:
This template helps explore the Jobs-to-be-Done for a target customer segment, focusing on functional, social, and emotional needs.

# Usage Note:
Ensure the session has been provided with comprehensive customer context, including behaviors, preferences, and current solutions.

# Instructions:
Guide the AI to fill in the blanks within the template, prompting detailed exploration of customer jobs, pains, and gains.

# Attribution:
Inspired by [Relevant Framework], adapted for interactive use by [Your Name], [Date].

# Licensing:
Licensed under the MIT License.

Date: [Date]
-->
---
```markdown
# Jobs-to-be-Done Template

## 1. Customer Jobs

<!--
Identify the jobs your customers are trying to get done. Break these down into:
-->

### Functional Jobs:
- [Suggest multiple, functional tasks customers need to perform].
### Social Jobs:
- [Suggest multiple ways the customers want to be perceived socially].
### Emotional Jobs:
- [Suggest multiple, emotional states customers seek to achieve or avoid].

## 2. Pains

<!-- 
Describe the pains customers experience in their journey. Include:
-->

### Challenges:
- [Suggest multiple obstacles customers face].
### Costliness:
- [Suggest multiple instances of what customers find too costly in terms of time, money, or effort].
### Common Mistakes:
- [Suggest multiple examples of frequent errors customers make that could be prevented].
### Unresolved Problems:
- [Suggest multiple problems not solved by current solutions].

## 3. Gains

<!--
Detail the gains customers seek, considering:
-->

### Expectations:
- [Suggest multiple instances of what could exceed customers' expectations of current solutions].
### Savings:
- [Suggest multiple instances of ways to save time, money, or effort that would delight customers].
### Adoption Factors:
- [Suggest multiple factors that would increase the likelihood of adopting a solution].
### Life Improvement:
- [Suggest multiple instances of how a solution could make customers' lives easier or more enjoyable].
```

## Final Tips:
   - **Review and Iterate:** Regularly review the AI-generated content with your team to ensure it aligns with your objectives.
   - **Clarity is Key:** Aim for clarity and focus in your prompts to prevent session drift and maintain the relevance of outputs.
   - **Reset When Needed:** If the session starts to drift, reset by revisiting the original context and goals to maintain alignment.

---
