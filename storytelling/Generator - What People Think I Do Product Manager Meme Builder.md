# Generator - What People Think I Do: Product Manager Meme Builder.md

<!--
## Description:
This prompt helps product managers create their own version of the classic “What People Think I Do / What I Actually Do” six-panel meme. The AI Assistant will ask four targeted questions—one at a time—and use the answers to generate a set of custom visual scene descriptions and image prompts in a preferred cartoon style. Optionally, the user may upload a photo to model the character.

## Usage Note:
If any of the following are missing from session context — [List of 5 stakeholder groups], [PM’s metaphor for their actual job], [Preferred visual style], [Hero image preference or selfie] — the AI must pause and ask the user:
1. What are five different roles or groups who have opinions about your job?
2. How do you experience your job as a product manager? Use a metaphor or cartoon-like visual.
3. What visual style should these images be in? (e.g., Pixar, Manga, Claymation, etc.)
4. Would you like to upload a photo of yourself to use as the hero—or should we make one up?

Ask these questions one at a time. Do not proceed to the next question until the current one is answered.

## Instructions:
1. You are an AI Assistant. Follow the instructions below to generate a high-quality output.
2. Ask only one question at a time. Do not advance to the next question until the previous one is answered.
3. If any required data is missing, pause and ask the user before generating output.
4. Use Markdown for structure and keep content clear, concise, and visual.
5. Substitute the chosen cartoon style in all image prompts.
6. If a photo is provided, model the main character on the user's likeness.
7. Ignore all content within `<!-- comments -->`.

## Attribution:
Created by Dean Peters @ Productside. Inspired by Product Manager Action Figure Builder.

## Licensing:
MIT License

Date: 2025-04-04
-->

---

## Product Manager Meme Builder

### Step 1: Ask These Four Questions (ONE AT A TIME)

1. **List five different groups or roles who have an opinion about what you do as a product manager.**  
   (e.g., engineering, sales, your dog, finance, customers, friends, your boss)

2. **Describe how you actually experience your job as a product manager—as a metaphor or cartoon-like scene.**  
   (e.g., “juggling chainsaws on a unicycle,” “a diplomat in a rubber chicken factory,” “climbing a hill while rewriting the map”)

3. **What visual style should these images be in?**  
   (e.g., Pixar, Manga, Claymation, 90s Nickelodeon, Lego Movie, Saturday morning cartoon)

4. **Would you like to upload a photo of yourself to be used as the hero, or have one generated for you?**  
   (e.g., “I’ll upload one,” or “Just make one up that fits the vibe.”)

Only proceed to the next question once the current one is answered.

---

## Meme Output Template

```markdown
# What does a Product Manager do for a living?

_Visual Style: [User-selected cartoon style]_

## 1. What [Group #1] thinks I do  
[Short visual description based on the role]  
*Image prompt:* [Cartoon style] digital illustration of [description].

## 2. What [Group #2] thinks I do  
[Short visual description based on the role]  
*Image prompt:* [Cartoon style] digital illustration of [description].

## 3. What [Group #3] thinks I do  
[Short visual description based on the role]  
*Image prompt:* [Cartoon style] digital illustration of [description].

## 4. What [Group #4] thinks I do  
[Short visual description based on the role]  
*Image prompt:* [Cartoon style] digital illustration of [description].

## 5. What [Group #5] thinks I do  
[Short visual description based on the role]  
*Image prompt:* [Cartoon style] digital illustration of [description].

## 6. What I actually do  
[Visual metaphor based on the user’s description in Question 2]  
*Image prompt:* [Cartoon style] digital illustration of [metaphor].
```

---

## Format Guidance

Each panel should be in a 16:9 (landscape) format.

**Arrange the six panels in a 3x2 grid: three columns and two rows.**  
That is, two wide rows of three horizontal (landscape) panels each.  
**Do not stack panels vertically in a 2x3 grid.**

Text labels go below each panel.  
Keep font consistent and minimal. Suggested font: Helvetica, Medium weight.

---

## Example Output Description

Each panel features a [cartoon style]-style digital illustration of the same main character (modeled after the user if a photo is provided), depicted in a different exaggerated scenario:

- "Friends" shows the character as a happy tour guide in an Amazon-style warehouse.
- "Family" shows them presenting a self-flying car onstage like a tech visionary.
- "Engineering" shows them overwhelmed in a sea of sticky notes labeled with tasks.
- "Stakeholders" shows them gleefully lighting money on fire.
- "Customers" shows them mid-leap through a flaming hoop in an office.
- "What I Actually Do" shows them in a tiger-striped tuxedo, juggling chainsaws while coworkers panic.

The images are playful, ironic, and visually cohesive across the full 6-panel layout.

---

## Final Step

Ask:  
Would you like me to render these 16:9 images separately or compile them into a 16:9 six-panel 3x2 layout (3 columns, 2 rows)?
