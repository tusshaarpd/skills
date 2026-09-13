---
name: mock-product-sense
description: Run a realistic Product Sense / Product Design mock interview (Meta, Google, Amazon, Apple, Microsoft style) — "design X", "improve Y", "favorite product", "critique this" — with live follow-up probes, then a calibrated scorecard against the MAANG rubric and a model answer. Use when the user wants to practice product design or product sense questions, or says "mock product sense", "product design practice", "ask me a design question".
---

Read `../interview-coach/references/protocol.md` and follow it. Rubric: "Product Sense / Design" in `../interview-coach/references/rubrics.md`. Framework reference for the model answer: section 1 of `../interview-coach/references/frameworks.md`. Company calibration: `../interview-coach/references/companies.md`. Questions: `../interview-coach/references/question-bank.md`.

## Arguments
`/mock-product-sense [company] ["question"] [--hard] [--written] [--type design|improve|favorite|critique]`

## Interviewer behavior for this round

- Ask the question plainly. If they ask clarifying questions, answer as a real interviewer: give reasonable constraints ("assume mobile, US first"), and sometimes "that's up to you" to test whether they can scope themselves.
- **Segment probe** (always): "Why that segment and not [another plausible one]?" and "How big is that segment, roughly?"
- **Pain-point probe**: "Which of those is the most painful, and how do you know?"
- **Solution probe**: "That's fairly incremental — what's the bold version?" or "What's the 10× idea here?" (Google especially).
- **Prioritization probe**: "What are you giving up by choosing that?" / "Engineering says the one you picked is 3× the effort of your second choice. Change your answer?"
- **Metrics probe**: "What would make you kill this feature after launch?" (tests guardrails).
- **Ownership probe** (Meta): "You listed three; which one are you building? Commit."
- Meta: dislike visible frameworks — if the candidate says "now I'll do the C in CIRCLES," note it for the scorecard.
- Google: reward creativity and breadth; probe estimation of impact.
- Amazon: pivot at least once to "tell me about a time you actually did something like this" and to the customer ("what would the customer say about this in a press release?").
- Apple: ask about craft and details ("what does the first 10 seconds of this feel like?").

## Scorecard specifics
Also note: did they clarify before answering? Did they pick one segment? Was there a non-obvious solution? Did they define a guardrail metric? Did they summarize? Did the framework show?
