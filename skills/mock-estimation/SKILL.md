---
name: mock-estimation
description: Run a quick Estimation / market-sizing drill (Google analytical, Amazon, consulting-style) — "how many X per day", "estimate revenue of Y", "market size of Z" — with probes on assumptions and sanity checks, then a scorecard. 10–15 minutes. Use when the user wants to practice guesstimates, Fermi questions, or market sizing, or says "estimation drill", "guesstimate", "how many".
---

Read `../interview-coach/references/protocol.md` and follow it (short round: ~4–5 exchanges). Rubric: "Estimation" in `../interview-coach/references/rubrics.md`. Framework: section 4 of `../interview-coach/references/frameworks.md`. Questions: `../interview-coach/references/question-bank.md` (Estimation section) — or invent one in the same style tied to the target company.

## Arguments
`/mock-estimation [company] ["question"] [--written]`

## Interviewer behavior

- Ask the question. If they start computing before clarifying units/scope, let them — then ask "per day or per year?" to expose it.
- After they state the equation, ask them to proceed. Don't correct arithmetic mid-way; note it.
- **Assumption probe**: pick their shakiest number — "Why 20%? What's that based on?"
- **Sensitivity probe**: "Which assumption, if wrong, changes your answer most?"
- **Sanity probe**: "Does that number feel right? What could you compare it to?"
- **So-what probe**: "You're the PM. What decision does this number inform?"
- Optionally give a second, shorter question if the first took <8 exchanges.

## Scorecard specifics
Include the "answer key" range (your own estimate with reasoning) and whether the candidate was within ~3×. Note if they wrote the equation before numbers and whether they sanity-checked.
