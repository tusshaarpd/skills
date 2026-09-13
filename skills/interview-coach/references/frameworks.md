# Frameworks — the answer structures interviewers expect

Frameworks are scaffolding, not the answer. At senior levels the structure should be *invisible*: the candidate sounds like a PM thinking, not a student reciting. Coach toward that.

---

## 1. Product Sense / Product Design

**Universal skeleton (works at Meta, Google, Amazon, Microsoft):**

1. **Clarify** (1–2 min) — What does the interviewer mean? Which platform? Which market? Is there a business goal in mind? Confirm scope. *Do not skip; do not over-do (max 3 questions).*
2. **Goal / mission link** — Why would this company build this? Tie to mission and a business goal (growth, engagement, revenue, retention, new market).
3. **Users** — List 3–4 segments. Pick ONE and say why (size, pain intensity, strategic value, underserved). This is the single most-scored moment.
4. **Pain points / needs** — 3–5 for the chosen segment, from their point of view. Prioritize to 1–2 (frequency × severity × how underserved).
5. **Solutions** — 3+ ideas, ranging from incremental to bold. At least one non-obvious. Brief description each.
6. **Prioritize** — Explicit criteria (impact, reach, effort, confidence, strategic fit). Pick one. State tradeoffs.
7. **Metrics** — 1 north star + 2–3 supporting + 1 guardrail/counter-metric.
8. **Risks & summary** — 30-second recap: user, problem, solution, why, how we'll know.

**CIRCLES** (Lewis Lin) maps onto the same thing: Comprehend, Identify customer, Report needs, Cut through prioritization, List solutions, Evaluate tradeoffs, Summarize. Use CIRCLES as a checklist, never as section headers out loud.

**Variants:**
- *"Improve product X"* — add a step: assess X today (who uses it, what's working, what's weak) before segments.
- *"Favorite product & how to improve"* — have 2 prepared. Why it's great (need it meets, why better than alternatives), then one improvement via the skeleton.
- *"Design X for Y (blind users, kids, seniors)"* — spend more on pain points; accessibility and context of use matter.
- *"Critique this design"* — usefulness, understandability, efficiency, delight, feedback/communication; then fixes.

---

## 2. Product Strategy / Business

**Skeleton:**
1. Clarify the question and the decision to be made.
2. **Goal** — what is the company optimizing for (growth, defensibility, revenue, mission)?
3. **Market** — size, growth, trends, regulation; who wins today and why.
4. **Customer** — who, what job-to-be-done, what's unmet.
5. **Competition** — incumbents, their moats, likely response.
6. **Our capabilities / right to win** — assets (distribution, data, brand, tech), gaps.
7. **Options** — 2–3 strategic paths (build / partner / acquire / don't enter). Pros, cons, cost, risk.
8. **Recommendation** — pick one. Say what would change your mind. Sequence: first 6 months, next 18.
9. **Risks & mitigations**; **metrics** to know if it's working.

Common question types: "Should [company] enter X?", "How would you monetize Y?", "You're CEO of Z, what do you do?", "Why is [competitor] winning?", "What should [product] do about [trend, e.g., generative AI]?"

Tools to name when useful (not to recite): Porter's five forces, SWOT, jobs-to-be-done, 7 powers (Hamilton Helmer: scale economies, network effects, counter-positioning, switching costs, branding, cornered resource, process power), Ansoff matrix.

---

## 3. Analytical / Execution / Metrics

### 3a. Define success metrics for a product
1. Clarify the product's goal and stage (launch vs mature).
2. Map the user journey (acquisition → activation → engagement → retention → revenue/referral — AARRR; or Google HEART: Happiness, Engagement, Adoption, Retention, Task success).
3. Propose a **north star** (captures value delivered, e.g., "weekly active listeners who play >30 min"), 2–3 **input/supporting** metrics (leading indicators), and **guardrail/counter** metrics (what could get worse: latency, reports, unsubscribes, revenue).
4. Say how each is measured and what a "good" target is. Prefer ratios and cohort-based metrics over raw counts.

### 3b. Metric went down (root-cause)
1. **Clarify** — which metric exactly, definition, how much, since when, sudden vs gradual, which platform/region.
2. **Sanity/technical** — logging or pipeline change? App release? Bot filter? Tracking bug is the #1 real cause.
3. **External** — seasonality, holidays, competitor launch, news/PR, platform (iOS update), macro.
4. **Internal** — our launches, experiments, pricing, policy, marketing spend, outages.
5. **Segment** — by platform, geo, new vs existing users, device, acquisition channel, cohort. Find where the drop concentrates.
6. **Funnel** — decompose the metric into its inputs (DAU = new + retained + resurrected; conversion = visits × CTR × completion) and find which input moved.
7. **Hypothesize → validate → fix** — state the top 2 hypotheses, how you'd confirm each (query, experiment), and what you'd do.
8. State what you'd communicate to leadership and when.

### 3c. Should we ship? (tradeoff decision)
Ask for: the primary metric's change, the counter-metrics, statistical significance and sample size, duration (novelty effects), segment differences, long-term vs short-term effects, strategic context. Then decide and say what would change your mind.

### 3d. Experiment design
Hypothesis → primary metric & minimum detectable effect → unit of randomization (user, session, geo) → sample size & duration (rule of thumb: 1–2 weeks minimum, full weekly cycles) → guardrails → what confounds (network effects, novelty) → decision rule stated before launch.

---

## 4. Estimation

1. Clarify what exactly and the units (per day? globally? revenue or count?).
2. Choose **top-down** (population → filters → rate) or **bottom-up** (unit → frequency → aggregate). Say which and why.
3. Write the equation *before* filling numbers.
4. Use round, defensible anchors (world 8B, US 335M, US households ~130M, smartphone users ~5B, Google searches ~8–9B/day, YouTube ~2.5B MAU, Netflix ~300M subs, Amazon Prime ~200M, Uber ~25M trips/day, iPhone ~1.5B active).
5. Compute out loud, keep 1–2 significant figures.
6. **Sanity check** against a known number. State the biggest sensitivity ("if the usage rate is 2× my guess, answer doubles").
7. If asked "so what?", tie it to a decision (is this market worth entering?).

---

## 5. Technical (PM)

You're being scored on: can engineers respect you, can you make tradeoffs, can you ask the right questions.

- **"Explain how X works"** (web search, HTTP request, push notifications, recommendation systems, OAuth login, a CDN, how a message gets delivered): go layer by layer client → network → service → storage; name the key components; mention one tradeoff and one failure mode.
- **"Design an API for X"**: resources, endpoints/verbs, request/response, auth, pagination, rate limits, versioning, error handling, idempotency.
- **"How would you decide between A and B (SQL vs NoSQL, build vs buy, monolith vs services, batch vs streaming)"**: state the axes (consistency, latency, cost, team skill, time-to-market), pick per the use case.
- **"Your engineer says it'll take 6 months; you have 3"**: decompose, find the 20% that delivers 80%, ask what the risky/unknown parts are, propose a spike, negotiate scope not time.
- Know: latency numbers (RAM ~100ns, SSD ~100µs, same-DC round trip ~0.5ms, cross-continent ~150ms), Big-O basics, what a queue/cache/load balancer/index/CDN does, eventual vs strong consistency, what an ML model needs (training data, features, evaluation metric, drift).

---

## 6. System Design (TPM; also senior PM-T)

**Skeleton (45 min):**
1. **Requirements** (5 min) — functional (3–5 core), non-functional (scale: users, QPS, data size; latency; availability; consistency; cost). Ask what's in/out of scope.
2. **Back-of-envelope** (3 min) — QPS read/write, storage/year, bandwidth. Read:write ratio.
3. **API** (3 min) — the 2–4 core endpoints.
4. **Data model** (3 min) — entities, key fields, which DB type and why.
5. **High-level design** (8 min) — client → LB → API/service layer → cache → DB; async via queue; CDN/blob for media. Draw it in text.
6. **Deep dive** (12 min) — the 1–2 hardest parts (the interviewer will steer): fan-out on write vs read, sharding key, consistency, hot keys, exactly-once, ranking.
7. **Scale & reliability** (6 min) — replication, sharding, caching strategy, rate limiting, failover, multi-region, backpressure, idempotency, monitoring/alerts.
8. **Tradeoffs & wrap-up** (3 min) — what you'd do differently at 10× or with half the budget; what you'd build first (MVP path).

Classic prompts: URL shortener, news feed, chat/messaging, notification service, rate limiter, ride dispatch, file sync (Dropbox), video upload/streaming, search autocomplete, ad click aggregator, payment system, distributed cache, metrics/logging pipeline.

See `system-design-cheatsheet.md` for building blocks and numbers.

---

## 7. Program Execution (TPM)

**"How would you run program X?" skeleton:**
1. **Clarify outcome** — what does done look like, by when, for whom; who is the exec sponsor.
2. **Scope & decomposition** — workstreams, owners, deliverables; what's explicitly out.
3. **Dependencies & critical path** — map team-to-team dependencies; identify the longest chain; where's the single point of failure.
4. **Risks (RAID)** — Risks, Assumptions, Issues, Dependencies; top 5 with likelihood × impact and mitigation/owner.
5. **Plan & milestones** — phase gates, integration points, buffers on the critical path, launch criteria.
6. **Operating rhythm** — weekly sync cadence, status format (RAG), escalation path, decision log, dashboards.
7. **Communication** — who needs what and how often (execs: monthly narrative; teams: weekly; partners: at milestones).
8. **Launch & post-launch** — go/no-go criteria, rollback plan, metrics review, retro.

**"Program is slipping" skeleton:** confirm the facts (what, how much, why) → assess options (cut scope, add buffer/time, add people — usually worst, re-sequence, de-risk with a fallback) → decide with the sponsor → communicate early and plainly → fix the root cause in the process.

**TPM signals:** you make ambiguity concrete, you find the critical path, you escalate early with options not problems, you're technical enough to challenge estimates, you build trust with eng leads, you measure what matters.

---

## 8. Behavioral — STAR(L)

- **Situation** (15–20 s) — context, stakes, your role. One number to size it.
- **Task** (10 s) — what *you* were responsible for.
- **Action** (60–90 s) — 3–4 concrete things *you* did. The "why" behind each. Tradeoffs. Who you influenced and how.
- **Result** (20 s) — quantified. Business outcome. What changed for users/team.
- **Learning** (10 s) — what you'd do differently; how you applied it later.

Total ≤2.5 min. Then stop and let them probe.

**Rules:** "I" over "we". No villains. Failure stories must have a real failure and a real fix. Numbers everywhere. Have a one-line headline for each story ("This is a story about pushing back on a VP with data"). Map every story to ≥3 principles/signals so you can reuse it.

**Core story set (12–15 stories) that covers most companies:**
1. Biggest impact / most proud of
2. 0→1 something ambiguous
3. Disagreed with leadership — and won
4. Disagreed — and committed anyway
5. Failed / missed a deadline / shipped something wrong
6. Made a decision with incomplete data
7. Dove into data and found something nobody saw
8. Cut scope / said no / killed a project
9. Influenced without authority across teams
10. Conflict with an engineer/designer/peer
11. Coached or grew someone; gave hard feedback
12. Did something outside your role (ownership)
13. Simplified something / removed process
14. Customer insight that changed direction
15. Handled a crisis / outage / escalation

---

## 9. Prioritization frameworks (name when useful)

- **RICE** = Reach × Impact × Confidence ÷ Effort
- **ICE** = Impact, Confidence, Ease
- **Impact vs Effort 2×2**
- **Kano** — basic / performance / delighter
- **MoSCoW** — must / should / could / won't
- **Opportunity scoring** — importance vs satisfaction gap
- **Cost of delay / WSJF** — for sequencing
