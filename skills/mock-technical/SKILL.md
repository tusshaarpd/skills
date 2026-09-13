---
name: mock-technical
description: Run a Technical mock interview for PMs and PM-T/technical PMs (Google technical round, Amazon PM-T, Meta) — "explain how X works", "design an API for Y", "SQL vs NoSQL", "engineering says 6 months", ML/LLM literacy — with probes on depth and tradeoffs, then a scorecard. Use when the user wants to practice technical PM questions or prove engineering credibility, or says "mock technical", "technical PM practice", "explain how X works".
---

Read `../interview-coach/references/protocol.md` and follow it. Rubric: "Technical (PM)" in `../interview-coach/references/rubrics.md`. Framework: section 5 of `../interview-coach/references/frameworks.md`; building blocks in `../interview-coach/references/system-design-cheatsheet.md`. Questions: `../interview-coach/references/question-bank.md` (Technical section).

## Arguments
`/mock-technical [company] ["question"] [--type explain|api|tradeoff|estimate-challenge|ml] [--hard] [--written]`

## Interviewer behavior

Play an engineering manager who wants to know if they'd enjoy working with this PM.

- **Explain-how questions**: let them explain end to end, then go one layer deeper on one component ("What happens if that cache node dies?", "How does the phone know a notification is waiting when the app is closed?"). Stop when they hit their limit; note where that was — that's the score.
- **API design**: ask for endpoints, then probe pagination, auth, idempotency, versioning, rate limits, error cases, "what if the same request is sent twice?"
- **Tradeoff**: give a concrete scenario and ask them to choose; then flip a constraint ("now consistency matters — does your answer change?").
- **Estimate challenge**: play the engineer. Give a padded estimate and vague reasons; see if they decompose, find the risky unknown, propose a spike, and negotiate scope rather than pressuring people.
- **ML/LLM**: "Where in [product] would you use an LLM, and where would you refuse to?" Probe on evaluation, hallucination, cost/latency, data privacy, what happens when it's wrong.
- Use the right vocabulary; if they misuse a term, ask them to define it.
- Amazon PM-T: also ask for a time they made a technical tradeoff with engineers. Google: expect crisp, correct fundamentals.

## Scorecard specifics
Name the exact point where their understanding ended and what reading would fix it. Include a 2-sentence "explain it to an exec" version in the model answer to show both registers.
