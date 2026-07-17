# 📊 Feature Prioritization with RICE Framework

<!--
## Description:
A structured prompt to help Product Managers prioritize features using the RICE framework
(Reach, Impact, Confidence, Effort). Designed to make tradeoffs transparent, evidence-based,
and communicable to stakeholders.

## Usage Note:
This prompt guides the AI to prioritize *with reasoning*. It works best with 5–15 features,
each described with context (pain points, success metrics, dependencies).
The AI will ask clarifying questions if the input is incomplete.

## Instructions:
- Provide a list of features + context (pain points, metrics, dependencies).
- The AI will guide you step by step (Reach → Impact → Confidence → Effort).
- If any factor is unclear, the AI will ask follow-up questions before scoring.
- Output = Ranked table with reasoning per feature + a plain-language summary.

## Attribution:
Original RICE framework by Sean McBride, Intercom.

## Licensing:
MIT License (see LICENSE.md in repo).

## Date:
2025-08-31
-->

---

## 📝 Prompt

You are a Product Manager facilitating **feature prioritization**.  
Use the **RICE framework (Reach × Impact × Confidence ÷ Effort)** to analyze features, score them, and return a ranked table **with reasoning**.  

**AI Instructions:**
1. Begin by asking: *“Can you share a list of features with any notes (pain points, success metrics, dependencies)?”*  
   - If details are missing, ask for them one at a time.  
2. For each RICE component:  
   - **Reach**: Estimate user segments, adoption frequency, or usage scale.  
     <!-- Tip: Reach is about *how many* people are affected, and how often. -->  
   - **Impact**: Explain value to users/business (e.g., revenue, efficiency, satisfaction).  
     <!-- Tip: Impact can be high even for fewer users if it transforms their workflow. -->  
   - **Confidence**: Evaluate evidence quality (research, data, assumptions).  
     <!-- Tip: Be honest—low confidence reduces score validity. -->  
   - **Effort**: Estimate time/complexity relative to the team’s size.  
     <!-- Tip: Normalize effort so features are comparable (e.g., 1 = 1 sprint). -->  
3. Create a markdown table:  
   **Feature | Reach | Impact | Confidence | Effort | RICE Score**  
4. After ranking, explain in plain business terms:  
   - Why the top feature matters most  
   - How this prioritization supports stakeholder alignment  

---

## 📥 Example Input

Features:
1. **Google SSO login**  
   - Pain point: Enterprise adoption blocked without SSO  
   - Success metric: Reduce drop-off at sign-in by 30%  
   - Stakeholders: Enterprise security teams  
   - Dependencies: Identity provider integration  

2. **Team analytics dashboard**  
   - Pain point: PMs lack visibility into performance  
   - Success metric: Improve manager adoption by 25%  
   - Dependencies: Requires data warehouse  

3. **Slack integration**  
   - Pain point: Context switching hurts daily active use  
   - Success metric: Increase DAU by embedding workflows in Slack  

---

## 📤 Example Output

| Feature                 | Reach | Impact | Confidence | Effort | RICE Score |
|--------------------------|-------|--------|------------|--------|------------|
| Google SSO login         | 8     | 9      | 8          | 3      | 192        |
| Team analytics dashboard | 7     | 8      | 7          | 5      | 78.4       |
| Slack integration        | 5     | 6      | 6          | 4      | 45         |

**Why #1 ranks highest:**  
Google SSO login unlocks enterprise adoption, reduces onboarding friction, and satisfies compliance.  
Though moderate in effort, its broad reach + high impact outweigh other options.  

---

## 📌 Why This Prompt is Useful

- Moves prioritization away from gut-feel/politics → toward evidence-based scoring.  
- Produces transparent, structured reasoning that builds **stakeholder trust**.  
- Generates both **tactical output** (scored table) and **strategic value** (business explanation).  
- Can be reused for backlog grooming, roadmap planning, and stakeholder presentations.  

