# 🧮 Feature Prioritization with RICE Framework

## Prompt
You are a Product Manager helping a SaaS team prioritize features.  
Use the **RICE framework** (Reach, Impact, Confidence, Effort) to score each feature and return a ranked table.

**Instructions for the AI:**
- Input: list of features + any notes from stakeholders.  
- Output: a markdown table with columns → Feature | Reach | Impact | Confidence | Effort | RICE Score.  
- Explain in 2–3 sentences why the top feature ranks highest.  
- Keep Reach, Impact, Confidence on a 1–10 scale. Effort = estimated weeks.  
- RICE Score = (Reach × Impact × Confidence) ÷ Effort.

---

## Example Input
Features:

Google SSO login

Team analytics dashboard

Slack integration
Notes:

Users often complain about logins.

Enterprise clients want reporting.

---

## Example Output
| Feature                  | Reach | Impact | Confidence | Effort | RICE Score |
|---------------------------|-------|--------|------------|--------|------------|
| Google SSO login          | 8     | 9      | 8          | 3      | 192        |
| Team analytics dashboard  | 7     | 8      | 7          | 5      | 78.4       |
| Slack integration         | 5     | 6      | 6          | 4      | 45         |

**Why #1 ranks highest:**  
Google SSO login removes major friction, benefits all users, and is relatively fast to build.

---

## Why This Prompt is Useful
Prioritization often gets emotional or political.  
This structured prompt helps PMs justify choices with data and makes tradeoffs transparent to stakeholders.
