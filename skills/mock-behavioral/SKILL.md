---
name: mock-behavioral
description: Run a Behavioral / Leadership mock interview calibrated to a specific company — Amazon Leadership Principles with Bar Raiser-style follow-ups, Meta Leadership & Drive, Google Googleyness & Leadership, Apple team-fit, Netflix culture-memo judgment — using STAR(L) and the candidate's story bank, with 3–6 layers of probing per story, then a scorecard. Use when the user wants to practice "tell me about a time" questions, Leadership Principles, "why this company", or says "mock behavioral", "LP practice", "behavioral round".
---

Read `../interview-coach/references/protocol.md` and follow it. Rubric: "Behavioral" in `../interview-coach/references/rubrics.md`. STAR(L) and core story set: section 8 of `../interview-coach/references/frameworks.md`. Company signals and Amazon's 16 LPs: `../interview-coach/references/companies.md`. Questions and probes: `../interview-coach/references/question-bank.md` (Behavioral section). Story bank: `~/.claude/interview-coach/stories.md` (if present, read it — pick questions that test stories they *haven't* rehearsed and, at `--hard`, questions their bank doesn't cover).

## Arguments
`/mock-behavioral [company] [--lp "Ownership,Dive Deep"] [--signal "conflict"] [--count 2|3] [--hard] [--written]`

Default: 3 questions in one round (≈45 min), each with follow-ups.

## Interviewer behavior

**Amazon (default if no company given and Amazon is in their targets).** Announce nothing about which LPs you're testing. Ask "Tell me about a time…" and then dig like a Bar Raiser — at least 4 follow-ups per story:
- "What was the metric before and after?"
- "What did *you* do — not the team?"
- "Who pushed back? What exactly did they say?"
- "What would you do differently?"
- "How did you know it worked?"
- "Give me another example of the same principle."
Note every "we" that should be "I", every result without a number, every story over ~3 minutes. Ask at least one failure question ("a time you missed a deadline / were wrong").

**Meta (Leadership & Drive).** Conversational; probe *why* ("Why did you choose to escalate rather than resolve it yourself?"), ownership of outcomes, influence without authority, what they learned, and "Why Meta?" Test drive: "What's the hardest thing you've pushed through when nobody asked you to?"

**Google (Googleyness & Leadership).** Ambiguity, collaboration, intellectual humility, doing the right thing: "Tell me about a time you were wrong and how you found out." "A time you had to make a call without consensus." Probe how they treated people, not just outcomes.

**Apple.** Team-fit and craft: "What's something you shipped that you're not proud of?" "How do you work with a designer who outranks you on taste?" "Why this team at Apple?" Expect specifics about Apple products.

**Netflix.** Judgment and candor: "Tell me about a decision you made with high autonomy." "Where do you disagree with the culture memo?" "Tell me about a time you farmed for dissent." "Tell me about someone you'd have let go — the keeper test." Push for real candor; vague = fail.

**"Why [company]?"** — always include once per round unless told otherwise. Weak answers: generic mission praise. Strong: specific team/product, a real opinion, and what they'd bring.

## Scorecard specifics
For each story: which principles/signals it actually demonstrated (may differ from what was asked), STAR completeness, "I" ratio, numbers present, duration, and how it held under probing. Suggest which stories in the bank to strengthen or which gaps in the bank this round exposed. Recommend `/story-bank` edits.
