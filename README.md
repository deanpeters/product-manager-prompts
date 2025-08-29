# Product Manager Prompts for Generative AI

**Practical AI tools that actually help with the daily grind of product management**

If you're drowning in stakeholder requests, seeking to scaffold strategies, struggling to write decent user stories, or just trying to make sense of your roadmap before it becomes roadkill, these prompts can help. They work in ChatGPT, Claude, Gemini, and pretty much any AI assistant you can copy-paste into.

Think of this as your AI-assisted toolkit for getting real PM work done faster and better.

## Quick Start: Try This Right Now

### Step 1: Find a prompt that matches your problem

1. Go to any .md file in the [/prompts/](prompts/) folder
2. Click "Raw" or "Code View" (not the pretty preview)
3. Copy the entire thing - yes, including all those comment blocks that start with <!--

### Step 2: Paste it into your AI assistant

1. Open ChatGPT, Claude, Gemini, whatever you use
2. Paste the whole prompt in there, as-is
3. The AI will ask you questions to understand your specific situation

### Step 3: Answer the questions and iterate

- Some of the prompts will engage the AI to guideyou through a conversation, not just dump a template on you
- The comments teach the AI how to be helpful specifically for product managers
- You can refine and adjust as you go

**Try this first:** Start with [Jobs-to-be-Done](prompts/jobs-to-be-done.md) if you're trying to understand your customers better, or [User Story Template](prompts/user-story-prompt-template.md) if you need to write better user stories.

---

## Why This Approach Works Better

Here's the thing about working with AI: most people either treat it like Google on steroids (ask a question, get an answer) or like a magic template machine (fill in blanks, get output). Neither approach gets you very far with complex product management work.

These prompts work differently. They create conversations with AI where:

- **You stay in control** - AI asks questions, you make the strategic decisions
- **Context builds gradually** - Instead of overwhelming you with forms, AI learns about your situation step by step
- **Framework thinking** - The prompts use proven PM methodologies like Jobs-to-be-Done, Value Proposition Canvas, etc.
- **Quality control built in** - The AI knows when to ask for missing information

### From User to Builder to Teacher

1. **Start by using** existing prompts for your daily work
2. **Learn to customize** them for your specific company or industry
3. **Eventually build your own** using the patterns you've learned
4. **Help others** by sharing what works

This isn't about replacing your PM judgment with AI. It's about having AI help you think through complex problems more systematically.

---

## What's in Here

**[/prompts/](prompts/)** - The main collection. User stories, positioning statements, customer research, competitive analysis - the bread and butter PM work.

**[/prompt-generators/](prompt-generators/)** - Tools that help you build your own prompts. Think of these as templates for making templates.

**[/storytelling/](storytelling/)** - Help with explaining complex product concepts through stories, visuals, and metaphors. Great for stakeholder presentations.

**[/resumes-resignations-reactions/](resumes-resignations-reactions/)** - A little therapeutic humor for dealing with workplace dysfunction. Sometimes you need to laugh to keep from crying.

**[/vibes/](vibes/)** - Experimental stuff to provide some guardrails and guidance to vibe coding. Advanced AI workflows that might be useful if you're comfortable with more cutting-edge approaches.

**[/skeletons/](skeletons/)** - For people who want to understand how prompts actually work under the hood. Reverse engineering and analysis tools.

---

## Want to Work Locally?

If you want to customize these prompts or contribute your own, you can clone this repository:

```bash
git clone https://github.com/deanpeters/product-manager-prompts.git
cd product-manager-prompts
```

This gives you local copies to modify without worrying about breaking anything, plus it's easier to search through everything.

---

## The Secret to Making These Work: Comments and Code View

Here's what most people miss when they first find this repository: GitHub shows you a "pretty" preview of files by default, but that preview hides the most important parts.

Every prompt has two layers:

1. **The visible part** - What the AI executes
2. **The comment blocks** - The teaching layer that shows you WHY it works

### You MUST View the Raw Code

When you click on any .md file:

- Don't use the preview (it looks nice but hides the good stuff)
- Click "Raw" or "Code View" to see everything
- Copy ALL of it, including the parts that start with <!--

### What Those Comments Do

```markdown
<!-- 
## Description: Why this prompt works for PMs
## Usage Note: What context you need before starting
## Instructions: How the AI should guide the conversation
## Attribution: Where this methodology comes from
-->
```

These comments are invisible to the AI when you paste the prompt, but they teach YOU how to work better with AI. Think of them as the instructor's notes that come with the lesson plan.

### Why This Matters

- **You learn while doing** - Each prompt teaches you something about AI collaboration
- **You can customize intelligently** - Understanding why something works helps you adapt it
- **You avoid common mistakes** - The comments warn you about pitfalls
- **You build expertise** - Over time, you'll understand how to create your own prompts

---

## Contributing and Learning Together

Teaching others is how we all get better at this.

I believe the best way to improve at product management in the AI era is by sharing what works (and what doesn't) and learning from each other. Your experience matters, whether you're just starting with AI or you've been experimenting for years.

### Ways to Help

**If you're new to AI:**

- Try the prompts and share what worked or didn't work for your situation
- Ask questions when instructions aren't clear
- Suggest better examples based on your industry

**If you're getting comfortable:**

- Customize prompts for your specific context and share the variations
- Create versions that work better for your team structure or company size
- Improve the teaching comments based on what you learned

**If you're advanced:**

- Build new prompt generators using these patterns
- Help analyze what makes some prompts more effective than others
- Share novel approaches you've developed

### How to Contribute

1. **Focus on helping others learn**
   
   - Include comments that explain your thinking
   - Show why you made specific choices
   - Help people understand your approach

2. **Test your stuff**
   
   - Try your prompts in ChatGPT, Claude, and Gemini
   - Make sure they solve real problems, not hypothetical ones
   - Remember that humans make the final decisions, not AI

3. **Simple process**
   
   ```bash
   git clone https://github.com/deanpeters/product-manager-prompts.git
   git checkout -b your-improvement-name
   # Make your changes
   git commit -m "Brief description of what you're adding"
   git push origin your-improvement-name
   # Open a pull request
   ```

### What Makes a Good Contribution

- Solves a real PM problem you've actually faced
- Includes clear explanations of how and why it works
- Provides examples others can adapt to their situation
- Respects the fact that humans, not AI, should make strategic decisions

---

## Next Steps and Resources

### Getting Started

1. **Pick a problem** - Look through [/prompts/](prompts/) for something that matches what you're struggling with right now
2. **Try it** - Copy the raw code, paste it into your AI assistant, follow the conversation
3. **Study the comments** - See how the structure teaches you to work better with AI
4. **Customize** - Adapt it for your specific situation

### Going Deeper

- **[Prompting Style Guide](prompting-style-guide.md)** - How all of this actually works under the hood
- **[Productside Workshop](https://www.productside.com/courses/ai-innovation-for-product-managers/)** - Live training if you want to go deeper
- **[My LinkedIn](https://www.linkedin.com/in/deanpeters/)** - Where I share ongoing thoughts about AI and product management

---

## Common Problems These Help With

**Stakeholder alignment issues?** Try the [positioning statement](prompts/positioning-statement.md) framework to get everyone on the same page.

**Drowning in feature requests?** Use the [jobs-to-be-done](prompts/jobs-to-be-done.md) analysis to focus on what customers actually need.

**Writing terrible user stories?** The [user story templates](prompts/user-story-prompt-template.md) will help you write ones that actually make sense.

**Want to create your own tools?** Start with the [universal prompt builder](prompt-generators/a-generative-AI-prompt-builder-for-product-professionals.md) to learn the patterns.

---

## Get in Touch

I'm here to help, learn together, and make this stuff more useful for product managers.

- **Have questions?** Open an [issue](https://github.com/deanpeters/product-manager-prompts/issues) 
- **Want to connect?** Find me on [LinkedIn](https://www.linkedin.com/in/deanpeters/)
- **Ready for training?** Check out [Productside workshops](https://www.productside.com/)

The best product managers will be the ones who help others get better at this stuff, not the ones who hoard knowledge.

---

## License

Licensed under the [MIT License](https://choosealicense.com/licenses/mit/). Use freely, modify openly, and share knowledge generously. 

*Created by [Dean Peters](https://github.com/deanpeters) • Built for the product management community • Designed to teach through doing*
