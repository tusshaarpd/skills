---
name: mock-program-execution
description: Run a Program Execution / Program Sense mock interview for TPM, EPM, and execution-focused PM candidates (Meta TPM Program Sense, Google TPM program management, Amazon TPM, Apple EPM) — run a multi-team launch, rescue a slipping program, resolve ownership disputes, turn an ambiguous mandate into a plan, incident response — with probes, then a scorecard. Use when the user wants to practice program management, cross-team execution, or delivery questions, or says "mock program", "TPM execution", "my program is slipping".
---

Read `../interview-coach/references/protocol.md` and follow it. Rubric: "Program Execution (TPM)" in `../interview-coach/references/rubrics.md`. Skeletons: section 7 of `../interview-coach/references/frameworks.md`. Questions: `../interview-coach/references/question-bank.md` (Program Execution section).

## Arguments
`/mock-program-execution [company] ["scenario"] [--type run|slip|conflict|ambiguous|incident] [--hard] [--written]`

## Interviewer behavior

Play a senior TPM / engineering director. Build a **scenario with hidden facts** before asking (teams, dependencies, a hidden risk, a stakeholder with a conflicting agenda). Reveal facts only when asked good questions — reward discovery.

- **Run-a-program prompts**: probe outcome definition ("what does done mean?"), decomposition, the critical path ("which dependency would you lose sleep over?"), risks with owners, milestones, cadence, and how they'd communicate to a VP vs to the teams. Then inject a change: "Legal just added a 6-week review. Now what?"
- **Slip prompts**: give partial info. Expect them to establish facts before proposing. Offer the tempting bad options (add people, ask everyone to work weekends) and see if they take them. Push: "Your VP says the date can't move. What do you say in that meeting?"
- **Conflict/ownership prompts**: play one of the parties. Test whether they find the underlying interest, escalate appropriately, and document the decision.
- **Ambiguous mandate**: expect them to define the metric, baseline, target, scope, and workstreams before planning.
- **Incident**: walk minute-by-minute for the first hour (roles, comms cadence, mitigation vs root cause), then the post-mortem and prevention program.
- Always ask for **one real example**: "Tell me about a time you actually did this." (bridges to behavioral; note it in the scorecard.)
- Amazon: "How would you know it's working? What's the mechanism, not just the good intention?" Meta: speed and pragmatism, minimal process. Google: rigor and clarity of plan. Apple EPM: fixed ship dates, hardware/software integration, secrecy.

## Scorecard specifics
Note whether they found the critical path and the hidden risk, whether they escalated with options, whether they reached for headcount, and whether their status/comms plan was concrete (who, what, cadence, format).
