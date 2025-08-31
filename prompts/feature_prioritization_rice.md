# 📊 Feature Prioritization with RICE Framework

<!-- 
## Description
The RICE framework helps Product Managers prioritize features using evidence-based scoring.  
RICE = Reach × Impact × Confidence ÷ Effort.

## Usage Note
This prompt guides the AI to combine numerical scoring with reasoning.  
It is designed to help PMs move beyond intuition or politics by grounding prioritization in transparent, repeatable criteria.

## Instructions
- Use for comparing 5–15 features at a time.
- Gather rich context: user pain points, success metrics, constraints, and timelines.
- Ensure each RICE factor is explained, not just scored.

## Attribution
Original RICE framework: Sean McBride at Intercom.
-->

---

## 📝 Prompt

You are a Product Manager facilitating feature prioritization.  
Use the **RICE framework (Reach, Impact, Confidence, Effort)** to analyze features, score them, and return a ranked table with reasoning.  

**Instructions for the AI:**
- Input: List of features with notes from user research, stakeholders, and business context.
- Output: A markdown table with columns: **Feature | Reach | Impact | Confidence | Effort | RICE Score**.
- Provide 2–3 sentences of reasoning per feature (not just numbers).
- For each RICE component:
  - **Reach:** Estimate user segments, adoption patterns, or frequency.
  - **Impact:** Describe user/business value (satisfaction, efficiency, revenue potential).
  - **Confidence:** Assess evidence quality and assumptions.
  - **Effort:** Estimate relative effort (weeks, complexity, dependencies).
- Compute RICE Score = (Reach × Impact × Confidence) ÷ Effort.
- After ranking, summarize **why the top feature matters most** in plain business terms.

---

## 📥 Example Input

Features:
1. Google SSO login  
   - Pain point: Users complain logins block adoption  
   - Stakeholders: Enterprise clients require SSO for compliance  
   - Success metric: Reduce drop-off at sign-in by 30%  

2. Team analytics dashboard  
   - Pain point: PMs lack visibility into team performance  
   - Success metric: Increase transparency, adoption by managers  
   - Dependencies: Requires data warehouse integration  

3. Slack integration  
   - Pain point: Users want fewer context switches  
   - Success metric: Improve daily active usage by embedding workflows in Slack  

---

## 📤 Example Output

| Feature                  | Reach | Impact | Confidence | Effort | RICE Score |
|---------------------------|-------|--------|------------|--------|------------|
| Google SSO login          | 8     | 9      | 8          | 3      | 192        |
| Team analytics dashboard  | 7     | 8      | 7          | 5      | 78.4       |
| Slack integration         | 5     | 6      | 6          | 4      | 45         |

**Why #1 ranks highest:**  
Google SSO login removes friction at a critical entry point, benefits all enterprise users, ensures compliance, and is relatively fast to implement compared to alternatives.

---

## 📌 Why This Prompt is Useful

Prioritization often becomes emotional or political.  
This structured framework:
- Grounds tradeoffs in **data + reasoning**
- Builds **stakeholder alignment** by showing transparent logic
- Helps PMs communicate prioritization clearly in roadmaps and planning sessions
- Reduces conflict by making scoring criteria explicit and defensible
