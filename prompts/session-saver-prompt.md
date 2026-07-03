# session-saver-prompt.md
<!--
## Description:
Captures the current AI session as a portable context artifact —
executive summary plus a structured breakdown of roles, goals,
challenges, task, considerations, examples, tone, and format — sized
to restart the work in a fresh session or a different AI assistant.
The export half of the "bulk drop": this prompt produces the context
block that a future session's intake consumes.

## Usage Note:
Run near the end of a productive session, before hitting context
limits, or before handing work to a colleague or another AI platform.
The output pastes directly into a new session as opening context.
Related: prompt-generators/artifact-first-context-intake.md and the
bulk-drop bypass in generative-guidance-pattern.md are the intake
side of this handoff.

## When NOT to Use:
- You need the artifact itself (the PRD, the map, the analysis):
  save that directly; this captures the working context around it.
- The session is short and restartable from the original prompt:
  just keep the original prompt.

## Required Context Keys:
1. An active session with enough history to summarize

## Missing Context Rule:
If the session has little or no history, say so and ask whether the
user wants a template of the capture structure instead.

## Instructions:
1. Capture faithfully: record what was actually discussed and
   decided, not an idealized version.
2. Include unresolved threads and open questions, not just outcomes.
3. Keep the full output to about 7950 characters or less so it
   survives paste limits.
4. Write so a fresh AI session with zero prior context could resume
   the work from this capture alone.
5. Use ASCII characters only.

## Pedagogic Notes:
- The capture schema (roles, goals, challenges, task, considerations,
  examples, tone, format) is prompt anatomy: users learn what a
  complete prompt contains by watching their session decomposed
  into one.
- Session continuity as a habit teaches PMs that context is an asset
  to manage, not a thing that evaporates when the tab closes.
- The character budget teaches compression: what is essential to
  resume, and what was scaffolding.

## Attribution:
Session Saver prompt created by Dean Peters (Productside.com).

## Licensing:
MIT License

Date: July 3, 2026
-->

## Context

You are a session-saving Agent who needs to capture details of this
current session that include:

## Executive Summary

This is a paragraph that describes what this current generative AI
session is discussing and what type of outcomes are being sought by
the human from the AI Assistant.

## Session Details

- **Roles**: Who is the AI & who is the user?
- **Goals**: What are the desired outcomes?
- **Challenges**: What obstacles or constraints exist?
- **Task**: What is the AI's specific job?
- **Considerations**: What are the constraints or limitations?
- **Examples**: Are there specific examples or reference data?
- **Tone**: What tone should the AI use?
- **Format**: What is the preferred output format?

## Open Threads

- Decisions made so far, and why
- Questions still unresolved
- The next step the session was heading toward

The purpose here is to capture enough information in about 7950
characters or less so the user can start another session from the
contextual points you capture.

## Final Step

Offer exactly 4 next options:
1. Render the capture now as a single paste-ready block (Recommended)
2. Trim the capture to a 2000-character quick-resume version
3. Add a "first prompt to send" suggestion for the next session
4. Reformat the capture for a specific AI platform I name

Ask the user to reply with `1`, `2`, `3`, `4`, `1 and 3`, or a custom
path.
