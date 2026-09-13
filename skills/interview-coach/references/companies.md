# Company Playbooks — PM & TPM loops at MAANG-level companies

Use this to calibrate mocks. Each company has a distinct interview *shape* and a distinct set of *signals* interviewers are told to score. Coach against the specific company when the candidate names one.

---

## Amazon (PM, Sr PM, PM-T, TPM)

**Shape.** Recruiter screen → phone screen (1 interviewer, 2–3 LPs + 1 functional question) → sometimes a written exercise (PM-T / Sr PM: 1–2 page narrative on a product problem) → virtual loop of 5–6 back-to-back 60-min interviews. Each interviewer owns 2–3 Leadership Principles and asks "Tell me about a time…" questions, with 4–6 layers of follow-up. One interviewer is the **Bar Raiser** (from another org, veto power, focused on long-term bar). Hiring decision is a debrief where each interviewer votes Inclined / Not Inclined and defends with *evidence from your answers*.

**What they score.** ~70% behavioral against LPs, ~30% functional (product sense, tech for PM-T, program execution for TPM). Every answer is mined for data: "What was the metric?" "What was the number before/after?" "What did *you* specifically do?" "What would you do differently?"

**The 16 Leadership Principles and what a strong story proves:**
1. Customer Obsession — you started from a customer problem, went against internal convenience, used customer data/anecdotes.
2. Ownership — you did something outside your job description because nobody else would; long-term over short-term.
3. Invent and Simplify — you removed a process/step; found a fundamentally new approach; simplification with a number attached.
4. Are Right, A Lot — you made a judgment call with incomplete data and it turned out right; you sought disconfirming views.
5. Learn and Be Curious — you taught yourself something (SQL, a domain) to solve a problem.
6. Hire and Develop the Best — you coached someone, raised the bar in hiring, gave hard feedback.
7. Insist on the Highest Standards — you rejected "good enough"; pushed back on a launch; fixed root cause.
8. Think Big — a bold, non-incremental vision; you expanded scope to 10x.
9. Bias for Action — a reversible decision made fast; you accepted calculated risk.
10. Frugality — you achieved more with fewer resources; constraint bred invention.
11. Earn Trust — you admitted a mistake publicly; you were vocally self-critical; you listened.
12. Dive Deep — you found the root cause in the data when others took the summary at face value.
13. Have Backbone; Disagree and Commit — you disagreed with a senior person with data, and either won or committed fully once decided.
14. Deliver Results — you shipped despite setbacks; hard numbers.
15. Strive to be Earth's Best Employer — you made the team safer/more productive/more diverse.
16. Success and Scale Bring Broad Responsibility — you considered second-order effects on society/community.

**Amazon tells.** Use "I", not "we". Every result needs a number. Have ≥2 stories per LP; interviewers will ask "another example?" Failure stories are mandatory (Earn Trust, Are Right A Lot). Prepare "tell me about a time you had to make a decision with no data", "a time you missed a deadline", "your most significant accomplishment". Long-winded = Not Inclined. Aim STAR in ≤2.5 min then let them dig.

**TPM at Amazon.** Loop adds: system design (design a service, discuss scaling, failure modes), program execution (multi-team launch, dependency management, how you drove a slipping program), and technical depth ("explain how X works", read/critique a design doc). Bar Raiser still there.

---

## Meta (PM, TPM)

**Shape.** Recruiter screen → 1 initial interview (Product Sense OR Execution, 45 min) → full loop: **Product Sense**, **Execution (Analytical)**, **Leadership & Drive**, sometimes a second Product Sense. Interviewers write feedback against a rubric; a hiring committee reads packets.

**Product Sense signals.** Do you start from the *people* and the *problem*, not the feature? Can you pick a target user segment and defend it? Do you generate several solutions then prioritize with a clear rationale? Do you know the difference between a mission-level goal and a product-level goal? Do you take *ownership* of the problem (choose a direction rather than listing options)? Meta specifically dislikes rigid frameworks — the structure should be invisible.

**Execution signals.** Define goals and metrics for a product (north star + supporting + counter/guardrail metrics); diagnose a metric change (clarify → segment → internal/external → hypothesize → test); make a tradeoff decision with data ("feature A raises engagement 3% but lowers revenue 1% — ship?"). Show comfort with A/B tests, statistical significance conceptually, and ecosystem effects.

**Leadership & Drive signals.** Ownership of outcomes, influence without authority, conflict with engineering/design, learning from failure, "why Meta", self-awareness. Follow-ups probe *why* you did things, not just what.

**Meta tells.** Talk in terms of mission → product goal → user problem → solution → metrics. Structure crisp, but conversational. Prioritization must be explicit (impact × reach × confidence ÷ effort, or equivalent). Always close with a summary and a recommendation.

**TPM at Meta.** Rounds: **Technical** (system design of a Meta-scale system — feed, messaging, notifications; plus deep technical Q&A), **Program Sense / Execution** (ambiguous multi-team program: how you'd scope, sequence, de-risk, run), **Leadership & Partnership** (influencing eng leads, conflict, cross-functional). Meta TPMs are expected to be near-engineer-level technically.

---

## Google (PM, TPM)

**Shape.** Recruiter screen → phone screen (1–2, 45 min, mix of product design + analytical) → onsite/virtual loop of 4–5 interviews covering **Product Design, Analytical, Strategy/Business, Technical, and Googleyness & Leadership**. Interviewers submit written feedback with a score (1–4); a **Hiring Committee** that has never met you decides from the packet. Then leveling/team-match.

**What they score.**
- *Product Design:* user empathy, breadth of solutions (including non-obvious), prioritization, metrics, and *creativity* — Google likes 10x thinking ("design an alarm clock for the blind", "improve Google Maps for tourists").
- *Analytical:* estimation ("how many queries/day"), metric definition, metric-drop diagnosis, experiment design. Show structure, sanity-check numbers, state assumptions.
- *Strategy:* "should Google enter X?", "how would you monetize Y?", market/competition/capabilities/options/recommendation with risks.
- *Technical (PM):* explain how a system works (search, HTTP request, notifications), design an API, discuss tradeoffs. You needn't code but must be credible with engineers; a CS/eng background is checked.
- *Googleyness & Leadership:* comfort with ambiguity, collaboration, intellectual humility, doing the right thing, navigating conflict.

**Google tells.** Answers should be *structured but exploratory* — think aloud, enumerate options, then converge. Always ask clarifying questions first. Google likes when you go beyond incremental. Use numbers when estimating and sanity-check them. Interviewers grade against a "bar" for the level: L5 (Sr PM) needs independent ownership of a product area; L6 needs cross-product influence.

**TPM at Google.** Loop: system design (scalable systems, tradeoffs), program management (planning, risk, dependency, "your program is 3 months late, walk me through"), technical depth (may include light coding or algorithms — know complexity, data structures, distributed basics), leadership. Google TPMs are asked to *both* design *and* run.

---

## Apple (PM / EPM / TPM)

**Shape.** Team-specific and less standardized. Recruiter → hiring manager screen → 4–8 interviews with the team (PM, eng, design, ops, often a cross-functional partner) → sometimes a presentation or take-home. Loops can span weeks. The hiring manager's opinion weighs heavily.

**What they score.** Domain/technical depth in *that team's* area (you must know their product intimately), product taste and attention to detail, collaboration in a functional (not divisional) org, secrecy/discretion, ability to say "I don't know" honestly, and *why Apple / why this team*. Behavioral questions are conversational; product questions are about *Apple's* products ("what would you change about Apple Watch?", "critique this feature").

**Apple tells.** Frameworks are less useful; deep opinions are. Have a point of view on quality and craft. Know the hardware/software integration. EPM (Engineering Program Manager) roles are Apple's TPM: expect schedule/risk/cross-functional questions grounded in shipping a physical+software product on a fixed date.

---

## Netflix (PM, TPM)

**Shape.** Recruiter → hiring manager → a panel of 4–8 interviews (peers, partners, sometimes a VP), all conversational and senior-heavy. Netflix hires few PMs, mostly senior; there's no junior PM track.

**What they score.** *Judgment* above all — the Culture Memo ("Freedom & Responsibility", "context not control", "keeper test", "farming for dissent", "highly aligned, loosely coupled"). Interviewers ask about decisions you made, how you gathered context, how you handled disagreement, how you'd act with high autonomy and no process. Expect deep product questions about Netflix specifically (recommendations, discovery, games, ads tier, live).

**Netflix tells.** Be candid and specific — vagueness is a fail. Show you've read the culture memo and can discuss where you agree/disagree. Have opinions on Netflix's strategy backed with reasoning. "Tell me about a time you disagreed with your manager and were right/wrong" is common.

---

## Microsoft (bonus — many candidates include it)

Shape: recruiter → hiring manager → loop of 4–5 with "as-appropriate" final. Scores against "growth mindset", customer obsession, "one Microsoft", diversity & inclusion. Product design and behavioral heavy; less analytical than Meta. Level bands: 61–62 (PM II), 63–64 (Senior), 65+ (Principal).

---

## Levels — what the bar looks like

| Level (Google / Meta / Amazon) | Scope expected | Interview bar |
|---|---|---|
| L4 / IC4 / L5 PM | Owns features within a product | Structured, user-first, can define metrics, executes with a team |
| L5 / IC5 / L6 Sr PM | Owns a product area; sets its roadmap | Independent judgment, prioritization with tradeoffs, leads cross-functional; stories show *you* drove the outcome |
| L6 / IC6 / L7 Principal | Owns multiple products / a strategy | Cross-org influence, strategy from first principles, mentoring PMs, ambiguous 0→1 |

When grading, state which level the answer would pass at.
