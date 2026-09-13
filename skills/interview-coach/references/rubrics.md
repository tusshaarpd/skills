# Scoring Rubrics — grade like a Bar Raiser, not a friend

Every mock ends with a scorecard. Score each dimension 0–10. Be calibrated and specific: quote what the candidate said, say what a 9 would have said instead.

**Bars (average across dimensions, and floor on any single dimension):**
- **L4 / IC4 / entry Sr:** avg ≥ 6.0, no dimension < 4
- **L5 / IC5 / Senior PM / TPM II:** avg ≥ 7.0, no dimension < 5
- **L6 / IC6 / Principal / TPM III:** avg ≥ 8.0, no dimension < 6

State the level the answer passes at, or "would not pass" and the single biggest reason.

**Anchor descriptions (apply to any dimension):**
- **0–3** — Missing, wrong, or generic. Buzzwords. No structure. Interviewer would end the round early.
- **4–5** — Present but shallow. Lists without choosing. Frameworks recited. Vague numbers. Needs heavy prompting.
- **6–7** — Solid. Structured, picks a direction with reasons, mostly self-driven, some depth. The typical "hire at L4/L5" answer.
- **8–9** — Senior. Insight the interviewer didn't expect; explicit tradeoffs; anticipates follow-ups; crisp. Drives the conversation.
- **10** — Rare. Would make an interviewer say "strong hire, consider up-leveling."

---

## Product Sense / Design

| Dimension | What a 9 looks like |
|---|---|
| Problem framing & clarification | Asked 2–3 sharp clarifying questions; tied the problem to the company mission and a business goal; scoped explicitly |
| User empathy & segmentation | 3–4 distinct segments; picked one with a defensible reason; pain points stated from the user's perspective, specific not generic |
| Solution creativity & breadth | ≥3 solutions spanning incremental → bold; at least one non-obvious; solutions map to the prioritized pain point |
| Prioritization & tradeoffs | Explicit criteria; picked one; named what you're giving up; considered feasibility |
| Metrics | North star + supporting + guardrail; measurable; tied to the goal |
| Communication & structure | Structure invisible but present; summarized at the end; concise; interviewer never lost |
| Ownership / drive | Took a position; didn't wait to be led; handled pushback with reasoning, not capitulation |

## Product Strategy

| Dimension | What a 9 looks like |
|---|---|
| Framing the decision | Named the actual decision and the goal being optimized |
| Market & customer insight | Sized the opportunity; knew the trends; JTBD clear |
| Competitive & capability analysis | Named incumbents' moats and the company's right to win / gaps |
| Options & recommendation | 2–3 real options; one recommendation; what would change your mind; sequencing |
| Business acumen | Unit economics, monetization, second-order effects, regulatory/platform risk |
| Communication | Executive-ready: answer first, then reasoning |

## Analytical / Execution

| Dimension | What a 9 looks like |
|---|---|
| Clarification & metric definition | Precisely defined the metric; asked magnitude/timing/segments |
| Structured decomposition | Went technical → external → internal → segment → funnel without skipping; hypotheses MECE |
| Data intuition | Knew which cut to look at first and why; recognized tracking bugs, seasonality, novelty effects |
| Metric design | North star / input / guardrail; ratios over counts; cohorts |
| Experiment & decision judgment | Understood significance, duration, counter-metrics; made a call and stated the reversal condition |
| Communication | Talked through the tree crisply; summarized findings and next steps |

## Estimation

| Dimension | What a 9 looks like |
|---|---|
| Clarification | Nailed units and scope before starting |
| Structure | Wrote the equation before numbers; chose top-down/bottom-up deliberately |
| Assumptions | Reasonable, stated, round; knew key anchors |
| Arithmetic & sanity check | No slips; compared to a known reference; named biggest sensitivity |
| So-what | Connected result to a decision |

## Technical (PM)

| Dimension | What a 9 looks like |
|---|---|
| Conceptual correctness | Explanation is accurate at the level an engineer would nod at |
| Layered explanation | Client → network → service → data; named components and their role |
| Tradeoff reasoning | Named the axes and picked per use case |
| Engineering partnership | Asked engineers the right questions; challenged estimates constructively; knows what's hard vs easy |
| Communication to non-technical | Could explain the same thing to an exec in 2 sentences |

## System Design (TPM)

| Dimension | What a 9 looks like |
|---|---|
| Requirements & scoping | Functional + non-functional with numbers; explicit out-of-scope |
| Estimation | QPS, storage, bandwidth; read/write ratio; drove design choices |
| High-level architecture | Correct components, correct data flow; drawn clearly |
| Deep dive | Handled the hard part (fan-out, sharding, consistency, hot keys) with real options and a choice |
| Scale, reliability, operations | Replication, caching, failover, rate limits, monitoring, backpressure |
| Tradeoffs | Named alternatives and why not; knew what breaks at 10× |
| Communication | Drove the session; checked in with interviewer; time-boxed |

## Program Execution (TPM)

| Dimension | What a 9 looks like |
|---|---|
| Outcome clarity | Defined done, by when, for whom, and the sponsor |
| Decomposition & dependencies | Workstreams with owners; dependency map; critical path identified |
| Risk management | Top risks with likelihood × impact, mitigations, owners, triggers |
| Planning & sequencing | Milestones, integration points, buffers where they matter, launch criteria |
| Operating rhythm & communication | Cadence, status format, escalation path, exec narrative vs team detail |
| Technical credibility | Could challenge an estimate; knew where the technical risk lives |
| Judgment under slippage | Options over problems; early escalation; root-cause fix |

## Behavioral (all companies)

| Dimension | What a 9 looks like |
|---|---|
| Relevance to the principle/signal | Story squarely demonstrates the LP/signal asked; headline stated up front |
| Personal ownership ("I") | Clear what *you* did vs the team; no hiding behind "we" |
| Depth of action & reasoning | 3–4 concrete actions with the *why*; tradeoffs; how you influenced others |
| Quantified result | Numbers before/after; business impact; what changed |
| Reflection & growth | Genuine learning; applied later; self-critical where warranted |
| Concision & follow-up handling | ≤2.5 min; survived 3+ probes without contradiction or vagueness |

---

## Scorecard output format (use every time)

```
## Scorecard — [Round type] · [Company] · [Question]

| Dimension | Score | Evidence (what you said) | What a 9 does |
|---|---|---|---|
| ... | x/10 | "..." | ... |

**Average:** x.x  ·  **Floor:** x  ·  **Verdict:** passes at L_ / does not pass
**Biggest gap (fix this first):** ...
**Second gap:** ...
**What you did well (keep):** ...
**Model answer outline (60 seconds):** ...
**Drill for next time:** one specific exercise
```
