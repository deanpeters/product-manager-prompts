# Submission Guide: Let's Build This Together

**How to contribute prompts that help the PM community**

This guide helps you create prompts that solve real PM problems while teaching strategic AI collaboration. We're excited to work with you to build tools that help product managers think better, not just work faster.

**Important:** If your pull request needs changes, that's not a rejection - it's an invitation to collaborate and learn together. We'll work with you to make your contribution shine.

---

## What We're Looking For

### Solves Real PM Problems
**Good:** "I built this because I was struggling to align stakeholders around our product positioning"
**Not good:** "Here's a generic template for writing requirements"

Your prompt should address authentic challenges you've faced as a product manager. If you haven't personally used it to solve a real problem, it's not ready to submit.

### Teaches While Doing
**Good:** Comments that explain why specific questions unlock better strategic thinking
**Not good:** Just instructions on how to fill out a template

Every prompt should be a learning experience. Users should understand more about strategic product management after using your tool than they did before.

### Works Across AI Platforms
**Must test in:** ChatGPT, Claude, and Gemini at minimum
**Bonus points:** Works well in other platforms too

Your prompt should create consistent, helpful experiences regardless of which AI assistant someone uses.

---

## Required Elements

### Rich Comment Structure
Every prompt must include this metadata in comment blocks:

```markdown
<!-- 
## Description:
Clear explanation of what this prompt does and why it matters for PMs

## Usage Note:
What context or preparation someone needs before starting

## Instructions:
How the AI should guide the conversation and what it should focus on

## Attribution:
Where your methodology comes from, what frameworks you're using

## Licensing:
MIT License (keeps everything open and shareable)

Date: [When you created this]
-->
```

### Conversational Scaffolding
Use the "one question at a time" approach:
- Build context gradually instead of overwhelming users
- Include fallback questions when essential information is missing
- Guide users through strategic thinking, don't just extract information

### Framework Grounding
Base your prompt on proven product management methodologies:
- Jobs-to-be-Done, Value Proposition Canvas, PESTEL analysis, etc.
- Explain in comments why you chose specific frameworks
- Show how the structure helps users apply these frameworks effectively

---

## Quality Standards

### Strategic Focus
**Good:** Helps users understand market dynamics, customer motivations, competitive positioning
**Not good:** Just optimizes task completion or workflow efficiency

We want prompts that elevate the strategic thinking of product managers, not just make them more productive at tactical work.

### Professional Output Quality
The results should be suitable for:
- Stakeholder presentations
- Strategic planning sessions
- Executive reviews
- Cross-functional alignment meetings

### Teaching Integration
**Good:** Users understand AI collaboration principles better after using your prompt
**Not good:** Users just get a deliverable without learning anything transferable

Your prompt should build expertise that users can apply to other AI interactions and PM challenges.

---

## What Makes Submissions Stand Out

### Industry-Specific Adaptations
Show how proven frameworks work differently across:
- B2B vs B2C contexts
- Enterprise vs startup environments
- Regulated vs unregulated industries
- Technical vs non-technical products

### Cross-Functional Perspective
Demonstrate understanding of how PM work intersects with:
- Engineering constraints and capabilities
- Sales and marketing needs
- Legal and compliance requirements
- Executive strategic priorities

### Measurable Learning Outcomes
**Great submissions help users:**
- Ask better strategic questions
- Recognize patterns across PM challenges
- Adapt frameworks to new contexts
- Build their own tools using your patterns

---

## Technical Guidelines

### File Naming Conventions
**Standard pattern:** `your-prompt-name.md`
- Use lowercase letters only
- Separate words with hyphens (not underscores or spaces)
- Make it descriptive - others should understand what it does
- End with `.md` extension

**Examples:**
- `customer-journey-mapping-prompt-template.md`
- `jobs-to-be-done.md` 
- `positioning-statement.md`

**Exception:** Sometimes we break these rules to get important items to sort to the top of directories, but that's rare and usually for organizational reasons.

### Where to Put Your Prompt
- **Strategic frameworks:** `/prompts/` directory
- **Tools that build other prompts:** `/prompt-generators/` directory  
- **Visual/narrative tools:** `/storytelling/` directory
- **Workplace humor/therapy:** `/resumes-resignations-reactions/` directory
- **Experimental approaches:** `/vibes/` directory
- **Analysis tools:** `/skeletons/` directory

**Not sure where it goes?** Just pick the closest match - we'll help you find the right spot during review.

---

## Submission Process

### Before You Submit
1. **Use it yourself** - Try it on at least one real PM problem you're facing
2. **Test across platforms** - Check that it works in ChatGPT, Claude, and Gemini
3. **Get a second opinion** - Have another PM try it if possible
4. **Document your thinking** - Rich comments that explain your design decisions

### What to Include
- **The prompt file** following our naming conventions
- **Brief description** of the problem it solves
- **Your experience** using it - what worked well?
- **Any platform differences** you noticed during testing

### Our Review Approach
We'll look at:
- **Problem relevance** - Does this address real PM challenges?
- **Teaching quality** - Will users learn strategic thinking skills?
- **Framework foundation** - Is it grounded in proven methodologies?  
- **Cross-platform compatibility** - Does it work reliably across AI systems?
- **Professional quality** - Are outputs suitable for stakeholder presentations?

**Remember:** We're not looking for perfection. We're looking for contribution spirit and willingness to learn together.

---

## Common Submission Mistakes

### Generic Templates
**Problem:** "Fill in these blanks to create a user story"
**Better:** "Guide strategic conversation about user motivations and business value"

### Task Automation Focus
**Problem:** "Speed up your workflow with this AI tool"
**Better:** "Think through complex positioning decisions more systematically"

### No Framework Foundation
**Problem:** Random questions without methodological grounding
**Better:** Structured approach based on proven PM frameworks

### Poor Cross-Platform Testing
**Problem:** Only tested in one AI system
**Better:** Validated across multiple platforms with consistent results

### Missing Teaching Elements
**Problem:** Just executes a task without building user expertise
**Better:** Users understand strategic principles they can apply elsewhere

---

## Examples of Great Submissions

### Strategic Foundation Category
- Market positioning frameworks that help users understand competitive dynamics
- Customer discovery tools that reveal unmet needs and job-to-be-done insights
- Business model analysis that connects strategy to execution

### Communication & Influence Category
- Stakeholder alignment tools that create shared understanding
- Narrative frameworks that make complex concepts accessible
- Presentation structures that drive decision-making

### Analysis & Research Category
- Competitive intelligence frameworks that reveal strategic opportunities
- Market sizing approaches that inform investment decisions
- Risk assessment tools that improve strategic planning

---

## When Your Submission Needs Changes

**This is normal and expected!** Most great prompts go through several iterations before they're ready.

### Common feedback you might get:
- "This is great! Can you add more teaching comments to explain why X works?"
- "Love the approach - can we test how this works in Claude vs ChatGPT?"
- "The framework is solid - can you show how it applies to B2B vs B2C contexts?"
- "This solves a real problem - let's make the strategic thinking more explicit"

### What happens next:
1. **We'll work with you** to address any feedback
2. **You'll learn something new** about prompt design or PM frameworks  
3. **Your prompt gets better** through the collaborative process
4. **Everyone benefits** from the improved version

### If you get stuck:
- **Ask questions** - we're here to help you succeed
- **Share your thinking** - help us understand your approach
- **Try the suggestions** - see how the changes affect your prompt's effectiveness

---

## Getting Help and Support

### Before You Start
- **Open an issue** if you want to discuss your idea before building
- **Look at existing prompts** to see patterns and quality standards
- **Join conversations** in issues to see what problems others are tackling

### During Development  
- **Test early and often** - don't wait until it's "perfect"
- **Ask for feedback** - we're happy to review drafts
- **Share your struggles** - others might have faced similar challenges

### Community Spirit
We're building a learning community where:
- **Everyone teaches and learns** - your experience helps others
- **Mistakes are learning opportunities** - not failures
- **Collaboration beats competition** - we all get better together
- **Questions are welcome** - especially from people new to AI or GitHub

---

## Remember: You're Helping Build the Future

The best contributions don't just solve individual problems - they help the entire product management community get better at strategic thinking with AI.

**Questions to guide you:**
- Will this help other PMs think more strategically?
- Does this teach transferable skills, not just complete a task?
- Is it grounded in proven PM methodologies?
- Will users understand AI collaboration better after using this?

**Don't worry about being perfect.** Focus on being helpful and willing to learn.

**Ready to contribute?** We're excited to work with you!