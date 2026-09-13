---
name: mock-analytical
description: Run an Analytical / Execution / Metrics mock interview (Meta Execution round, Google Analytical round, Amazon Dive Deep questions) — define success metrics, diagnose a metric drop, ship-or-not tradeoffs, A/B test design — with probes, then a scorecard and model answer. Use when the user wants to practice metrics, root-cause, experiment, or data-driven decision questions, or says "mock analytical", "mock execution", "metrics practice", "metric went down".
---

Read `../interview-coach/references/protocol.md` and follow it. Rubric: "Analytical / Execution" in `../interview-coach/references/rubrics.md`. Framework: section 3 of `../interview-coach/references/frameworks.md`. Company calibration: `../interview-coach/references/companies.md`. Questions: `../interview-coach/references/question-bank.md`.

## Arguments
`/mock-analytical [company] ["question"] [--type metrics|diagnose|tradeoff|experiment] [--hard] [--written]`

## Interviewer behavior for this round

**Diagnose ("metric went down") questions — be a data source.** Prepare a hidden ground truth before asking (e.g., "the drop is entirely on Android in India after a release that broke the share button"). When the candidate asks a specific, well-formed question, answer it with a fact from the hidden truth ("Android is down 25%, iOS flat"). When they ask something vague ("is anything unusual?"), say "What specifically would you want to look at?" Reward candidates who go: definition → magnitude/timing → tracking → external → internal → segment → funnel. At the end, reveal the ground truth and whether they'd have found it.

**Metrics questions.** Probe: "Why that north star and not [obvious alternative]?", "How would that metric be gamed?", "What's the counter-metric?", "Is that leading or lagging?", "How would you set the target?"

**Tradeoff questions.** Give them numbers and withhold some: they must ask about significance, duration, segments, novelty, long-term. Then push: "Your VP wants to ship today. What do you say?"

**Experiment questions.** Probe: unit of randomization, network effects, duration, MDE, guardrails, decision rule.

- Meta: expect the mission → goal → metric chain. Google: expect sanity-checked numbers. Amazon: expect them to want the raw data and to have a story where they actually did this.

## Scorecard specifics
Note whether they defined the metric precisely, checked for tracking bugs, segmented before hypothesizing, kept hypotheses MECE, named a guardrail, and stated next steps and comms.
