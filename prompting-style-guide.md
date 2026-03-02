# Prompting Style Guide: The Dean Peters Method

**A comprehensive methodology for building AI-assisted product management tools**

## Purpose & Philosophy:
This guide documents the complete methodology for creating prompts that don't just execute tasks—they **teach strategic thinking while building AI-human partnerships**. Based on extensive testing across ChatGPT, Claude, and Gemini, this approach transforms product managers from prompt users into prompt architects.

### **Core Philosophy: "Teaching Through Structure"**
Every prompt in this collection serves dual purposes:
1. **Execute PM tasks** - Solve immediate product management challenges
2. **Teach AI partnership** - Build understanding of strategic AI collaboration

This comment-driven pedagogy approach ensures that **using the tools teaches you how to build better tools**.

### **Template Stability Principle**
For this repository, output templates are not merely formatting devices; they are
teaching artifacts and operational contracts.

- Preserve canonical PM frameworks in output structure for consistency over time.
- Improve context intake and facilitation while keeping output schema stable.
- This is especially important for workflows that feed delivery systems such as Jira and ADO.
- If a structural change is required, create and label a new version rather than silently changing the old one.

---

## The Anthropological Evolution Framework

### **User → Builder → Teacher Progression**

**Level 1: User** - Copy-paste existing prompts for daily PM work  
**Level 2: Builder** - Customize and create prompts using structural patterns  
**Level 3: Teacher** - Contribute methodology improvements and help others learn  

This progression ensures the PM community evolves toward **AI tool building autonomy** rather than dependency.

---

## Universal Prompt Architecture

### **The Five-Block Structure**
Every effective PM prompt follows this proven architecture:

```markdown
<!-- COMMENT BLOCK - The Hidden Curriculum -->
<!-- Teaching materials invisible to AI but crucial for users -->

## Context Block
[AI role setting and expertise framing]

## Instruction Block  
[Core directives and behavioral requirements]

## Parameter Block
[Variable elements and user-specific constraints]

## Output Block
[Delivery format and quality specifications]

## Validation Block
[Quality checks and refinement mechanisms]
```

### **Information Flow Patterns**
- **Sequential progression** - Logical step-by-step development
- **Conversational scaffolding** - One question at a time approach
- **Progressive disclosure** - Complexity builds gradually
- **Feedback loops** - Iterative refinement and validation

---

## Comment-Driven Pedagogy

### **The Hidden Teaching Layer**
Comments serve as **embedded learning materials**:

```markdown
<!-- 
## Description: [Why this approach works strategically]
## Usage Note: [Context needed before starting]
## Instructions: [How AI should guide the conversation]
## Attribution: [Learning sources and methodology]
## Licensing: MIT License for open knowledge sharing
-->
```

### **Teaching Objectives in Comments**
- **Strategic thinking** - Why specific frameworks guide AI reasoning
- **Quality control** - How to ensure professional-grade outputs  
- **Adaptation guidance** - Ways to customize for different contexts
- **Methodological transparency** - Reveal the "why" behind design decisions

---

## Conversational Scaffolding Technique

### **Progressive Context Building**
Instead of overwhelming users with complex forms, build context gradually:

1. **Broad framing** - What domain? What type of challenge?
2. **Specific context** - What constraints? What stakeholders?  
3. **Detailed parameters** - What format? What timeline?
4. **Quality validation** - What makes this successful?

### **One Question at a Time Pattern**
```markdown
Ask the user the following questions **one at a time**:

1. [Strategic context question]
2. [Specific situation question] 
3. [Constraint identification question]
4. [Success criteria question]
```

This prevents cognitive overload while ensuring comprehensive context gathering.

### **Workload Inversion Rule**
Do not make users define the full artifact up front when the assistant can infer and propose.

**Preferred pattern:**
1. Ask for minimum viable context (persona + pain + constraint)
2. Propose 3 likely scopes or structures
3. Recommend one option first with rationale
4. Let user choose (`1`, `2`, `3`, `1 and 3`, or custom)

### **Persona-First Recommendation Rule**
At decision points, options should be phrased in the user's world first:
- Persona-language recommendation: what this does for the user
- Optional business translation: why this matters to the organization

Avoid leading with internal business jargon when the user-facing framing is the real decision surface.

### **Decision Turn Contract**
When a prompt reaches a meaningful fork, use this exact interaction shape:

```markdown
Based on what you shared, here are the three best paths:
1. [Persona-first option] (Recommended) - [why now]
2. [Persona-first option] - [tradeoff]
3. [Persona-first option] - [tradeoff]

Reply with `1`, `2`, `3`, `1 and 3`, or your own path.
```

After response:
- Confirm choice in one sentence
- Show progress
- Ask only the next best question

### **AFCI + Fixed Output Contract**
Use Artifact-First Context Intake (AFCI) to reduce user burden:
1. Extract context from artifacts/session first
2. Ask up to 3 targeted questions only for missing keys
3. Proceed with labeled assumptions if still incomplete

Then render the canonical output template exactly (unless user explicitly requests changes).

---

## Framework Integration Methodology

### **Embedding PM Methodologies in AI Conversations**
Rather than teaching frameworks separately, integrate them into prompt structure:

**Jobs-to-be-Done Integration:**
```markdown
### Customer Jobs Analysis
- **Functional Jobs**: [AI generates based on context]
- **Social Jobs**: [AI considers perception factors]  
- **Emotional Jobs**: [AI addresses feeling states]
```

**Value Proposition Canvas Integration:**
```markdown
### Pain Point Analysis  
- **Challenges**: [Current obstacles users face]
- **Costliness**: [Time/money/effort concerns]
- **Common Mistakes**: [Preventable errors]
```

### **Framework Teaching Through Usage**
Each integrated framework includes pedagogical comments explaining:
- **Why this framework** applies to the specific PM challenge
- **How the structure** guides strategic thinking
- **When to adapt** the framework for different contexts

---

## Quality Control Architecture

### **Built-in Validation Patterns**
Effective prompts include multiple quality checkpoints:

**Pre-execution Validation:**
```markdown
If any of these are missing from session context:
- [Critical information A]  
- [Critical information B]
The AI must pause and ask clarifying questions before proceeding.
```

**Post-execution Refinement:**
```markdown
After generating initial output:
- "What assumptions should we validate?"
- "What additional context would improve this?"
- "What alternative approaches should we consider?"
```

### **Professional Standards Integration**
- **Cross-platform testing** - Validate across ChatGPT, Claude, Gemini
- **Real-world application** - Test with actual PM challenges, not hypotheticals
- **Stakeholder validation** - Ensure outputs meet professional presentation standards
- **Iterative improvement** - Build learning from usage back into prompt structure

---

## Multi-Modal Thinking Integration

### **Beyond Text-Only Prompts**
Modern PM work requires integration across formats:

**Visual Thinking Support:**
- Storyboard generation prompts
- Diagram creation guidance  
- Metaphorical framework development

**Data Integration Patterns:**
- Quantitative analysis frameworks
- Metric definition and tracking
- Evidence-based decision support

**Collaborative Workflow Support:**
- Multi-stakeholder perspective simulation
- Cross-functional alignment tools
- Team communication facilitation

---

## Platform-Specific Optimizations

### **Cross-Platform Compatibility**
While maintaining universal structure, optimize for platform strengths:

**ChatGPT Optimizations:**
- Leverage reasoning chains for complex analysis
- Utilize plugin integrations where available
- Take advantage of conversation memory

**Claude Optimizations:**  
- Use analytical strengths for strategic thinking
- Leverage strong context handling for complex scenarios
- Optimize for thoughtful, nuanced responses

**Gemini Optimizations:**
- Integrate multi-modal capabilities where relevant
- Utilize real-time information access when appropriate
- Leverage reasoning capabilities for complex problems

---

## Advanced Architectural Patterns

### **Meta-Prompt Architecture**
Prompts that generate other prompts:

```markdown
## Universal Building Framework
1. Ask context questions to understand user needs
2. Apply architectural patterns based on requirements  
3. Generate customized prompt following structural standards
4. Include teaching comments explaining design decisions
```

### **Autonomous Agent Patterns**  
Experimental approaches for advanced users:

```markdown  
## Autonomous Research Workflow
1. Strategic question identification
2. Independent research and synthesis
3. Multi-scenario simulation and analysis
4. Stakeholder perspective integration
5. Decision recommendation with rationale
```

### **Iterative Refinement Systems**
Built-in learning and improvement:

```markdown
## Continuous Improvement Pattern
After each usage session:
- Document what worked well
- Identify improvement opportunities  
- Test modifications with real scenarios
- Update teaching comments based on learnings
```

---

## Contribution Standards & Community Building

### **What Makes a Great Contribution**
Following the teaching-through-structure philosophy:

**Required Elements:**
- **Real PM problem focus** - Addresses authentic product management challenges
- **Rich pedagogical comments** - Teaches methodology, not just execution
- **Cross-platform validation** - Works across multiple AI assistants  
- **Professional quality standards** - Outputs suitable for stakeholder presentation

**Quality Indicators:**
- **Structural clarity** - Clear information flow and logical organization
- **Teaching integration** - Comments that build PM expertise while using
- **Adaptation guidance** - Clear instructions for customization
- **Framework grounding** - Based on proven PM methodologies

### **Community Evolution Goals**
Building collective expertise through:
- **Shared vocabulary** - Common language for discussing prompt architecture
- **Quality standards** - Community consensus on effective prompt characteristics
- **Teaching resources** - Materials that help others learn prompt building
- **Innovation acceleration** - Novel approaches that advance the methodology

---

## Implementation Guidelines

### **For Individual PMs**
**Getting Started:**
1. Use existing prompts to understand the conversational scaffolding approach
2. Study comment sections to learn the pedagogical methodology
3. Customize prompts for your specific industry/context
4. Build your first original prompt using the architectural framework

**Advancing:**
1. Create prompt variations for different stakeholder audiences
2. Integrate additional PM frameworks into existing structures
3. Develop meta-prompts that generate tools for your specific challenges
4. Contribute improvements and novel approaches back to the community

### **For PM Teams**
**Team Adoption:**
1. Start with shared prompt library using consistent architectural standards
2. Train team on comment-driven learning approach
3. Establish quality standards for team-created prompts
4. Build internal expertise through collaborative prompt development

**Scaling:**
1. Create organization-specific prompt templates
2. Develop training programs using the teaching-through-structure methodology
3. Build internal prompt building expertise  
4. Contribute organizational learnings to broader PM community

---

## Measuring Effectiveness

### **Quality Metrics for Prompts**
**Structural Assessment:**
- **Clarity** - Are instructions unambiguous and actionable?
- **Completeness** - Does the prompt gather sufficient context?
- **Adaptability** - Can it be customized without breaking?
- **Teaching value** - Does usage build PM expertise?

**Outcome Assessment:**
- **Professional quality** - Are outputs suitable for stakeholder presentation?
- **Strategic insight** - Does the process generate valuable thinking?
- **Time efficiency** - Does AI collaboration accelerate quality work?
- **Learning transfer** - Do users develop better AI collaboration skills?

### **Community Impact Metrics**
- **Adoption rates** - How many PMs successfully use contributed prompts?
- **Customization evidence** - How many variations and adaptations emerge?
- **Teaching effectiveness** - How well do prompts transfer PM knowledge?
- **Innovation acceleration** - How quickly do novel approaches develop?

---

## Future Directions

### **Emerging Capabilities Integration**
As AI capabilities advance, the methodology evolves to leverage:
- **Enhanced reasoning** - More sophisticated strategic analysis
- **Multi-modal integration** - Text, visual, and data synthesis  
- **Autonomous operation** - Self-directed research and analysis workflows
- **Real-time adaptation** - Dynamic prompt modification based on context

### **Community Research Priorities**
Areas where collective learning would benefit everyone:
- **Cross-industry validation** - How approaches work across different PM domains
- **Skill transfer measurement** - Quantifying learning effectiveness of teaching-integrated prompts
- **Advanced architectural patterns** - Novel structural approaches for complex challenges
- **Ethical frameworks** - Responsible AI partnership in product management

---

## Remember: We're Building the Future Together

**This methodology isn't just about better prompts—it's about evolving product management practice for the AI era.**

By teaching through structure, validating through community use, and contributing improvements back, we're collectively building:
- **PM expertise that scales** - Knowledge that transfers across people and contexts
- **AI partnership skills** - Capabilities that will define PM effectiveness going forward
- **Community learning systems** - Shared resources that make everyone more capable
- **Innovation acceleration** - Faster development of novel PM approaches

**The best product managers in the AI era will be those who teach others to build better tools.**

---

*This methodology represents years of testing, iteration, and community feedback. It will continue evolving as AI capabilities advance and as more product managers contribute their learnings.*
