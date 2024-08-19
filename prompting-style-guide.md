# Prompt Generation for Product Managers Style Guide 

### **Purpose:**
This guide assists in creating effective prompts for generating structured and insightful outputs using Generative AI (e.g., ChatGPT). It helps maintain focus and consistency, reducing the risk of session "drift."

### **Steps for Prompt Generation:**

#### **1. Define the Context:**
   - **What is the task or objective?** Clearly state the product management activity you want to address (e.g., crafting a positioning statement, exploring the problem space).
   - **Who is the target audience or customer?** Specify the relevant customer segment, their needs, and context.
   - **What is the scope?** Determine the areas the prompt should cover, such as functional, emotional, or social aspects.

#### **2. Use the [Fill in the Blanks] Structure:**
   - **Overview:** Provide a high-level description of the template's purpose and usage. 
   - **Specific Instructions:** Use the [fill in the blanks] method within Markdown, with instructions enclosed in `<!-- comment blocks -->` to guide the AI in generating content. This approach ensures that the output is both relevant and actionable.

   **Example Structure:**
   ```Markdown
   # template-name.md
   <!-- 
   ## Description:
   Provide a concise description of what this template is for and how it should be used.

   ## Usage Note:
   Include any specific context or preparatory steps needed before using this template with Generative AI.

   ## Instructions:
   Provide clear instructions on how to run the prompt, specifying any key elements to include.

   ## Attribution:
   Created by [Your Name], [Date].

   ## Licensing:
   This document and the template contained within are licensed under the MIT License, allowing free use, modification, and distribution with proper attribution to the original and current creators.

   Date: [Date]
   -->
   ---
   ```markdown
   ## Template Section
   * **[Title/Topic]**: [Detailed instructions for filling in the content based on the context provided.]
   ```
   ```

#### **3. Incorporate Bullet Points and Descriptions:**
   - **Bullet Points:** Use bullet points for clarity and structure. 
   - **Couple with Descriptions:** Each bullet point should include a title or topic followed by a description or instruction on what the AI should generate.

   **Example:**
   ```Markdown
   ### 1. Identify Problems
   * **[Regulatory Compliance]**: [Describe the regulatory challenges the customers face and how these impact their operations.]
   ```

#### **4. Think Like a Product Manager:**
   - **Focus on Outcomes Over Outputs:** Optimize your prompts to generate content that focuses on the 'who' and 'why' (the outcomes), rather than just the 'how' (the outputs).
   - **Understand the Customer:** Ensure the prompt helps uncover the deeper needs, pains, and gains of the customer, rather than just technical solutions.

#### **5. Maintain Consistency with Prompts:**
   - **Stick to the Structure:** Use the same format for similar tasks to ensure consistency across different sessions.
   - **Reuse Successful Prompts:** If a prompt worked well in one session, reuse or adapt it for other tasks to maintain focus.

### Example Prompt

Below an example of an ideal prompt written in accordance with this prompt generation style guide:

```Markdown
# jobs-to-be-done.md
<!-- 
## Description:
This Jobs-to-be-Done template, influenced by the Customer Circle segment of the Osterwalder Value Proposition Canvas, has been created for interactive use with Generative AI agents such as ChatGPT, Gemini, and Claude. 
It enables a structured exploration from the customer's perspective, focusing on their jobs, pains, and gains. 
This method is essential for crafting solutions that resonate deeply with customer needs and preferences.

## Usage Note:
Utilize this template in Generative AI conversations where the user has already provided the session with comprehensive context on the target customer segment, including their behaviors, preferences, and current solutions. 
This information enriches the AI's responses, ensuring they are relevant and empathetic to the customer's situation.

## Instructions:
Ensure the session includes detailed customer context as outlined above. 
Then, instruct the Generative AI Agent (ChatGPT, Gemini, Claude) to fill in the blanks within the template, prompting detailed exploration of the Jobs-to-be-Done Template.

## Attribution:
Influenced by Osterwalder's Value Proposition Canvas, adapted for interactive use by Dean Peters, March 15, 2024.

## Licensing:
This interactive document and template are licensed under the MIT License, allowing free use, modification, and distribution with proper attribution to the original and current creators.

Date: March 15, 2024
-->
---
   ```markdown
   ## Jobs-to-be-Done Template
   
   ### 1. Customer Jobs
   
   <!--
   Identify the jobs your customers are trying to get done. Break these down into:
   -->
   
   #### Functional Jobs:
   - [Suggest multiple, functional tasks customers need to perform].
   #### Social Jobs:
   - [Suggest multiple ways the customers wanta to be perceived socially].
   #### Emotional Jobs
   - [Suggest multiple, emotional states customers seek to achieve or avoid].
   
   ### 2. Pains
   
   <!-- 
   Describe the pains customers experience in their journey. Include:
   -->
   
   #### Challenges:
   - [Suggest multiple obstacles customers face].
   #### Costliness:
   - [Suggest multiple instances of what customers find too costly in terms of time, money, or effort].
   #### Common Mistakes:
   - [Suggest multiple examples of frequent errors customers make that could be prevented].
   #### Unresolved Problems:
   - [Suggest multiple problems not solved by current solutions].
   
   ### 3. Gains
   
   <!--
   Detail the gains customers seek, considering:
   -->
   
   #### Expectations:
   - [Suggest multiple instances of what could exceed customers' expectations of current solutions].
   #### Savings:
   - [Suggest multiple instances ways of savings in time, money, or effort that would delight customers].
   #### Adoption Factors:
   - [Suggest multiple factors that would increase the likelihood of adopting a solution].
   #### Life Improvement:
   - [Suggest multiple instances of how a solution could make customers' lives easier or more enjoyable].
   ```
```

### **Final Tips:**
   - **Review and Iterate:** Always review AI-generated content with your team to refine and expand upon the ideas.
   - **Keep it Simple:** Avoid overloading the prompt with too much detail; aim for clarity and focus.
   - **Prepare for Session Drift:** If the session starts to drift, reset by revisiting the original context and goals.

---
