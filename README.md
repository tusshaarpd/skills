# tusshaarpd/skills — Claude Code skills

Two skill sets in one repo:

1. **MAANG Interview Coach** — 15 skills that turn Claude Code into a PM / TPM interview coach calibrated to Meta, Amazon, Apple, Netflix, Google (and Microsoft) loops.
2. **The Minimalist Entrepreneur** — 10 business-judgment skills based on [Sahil Lavingia's book](https://www.minimalistentrepreneur.com/), forked from [slavingia/skills](https://github.com/slavingia/skills) (MIT).

## Installation

**Option A — copy into your global skills folder (simplest):**

```bash
git clone https://github.com/tusshaarpd/skills.git
cp -r skills/skills/* ~/.claude/skills/
```

**Option B — plugin marketplace, inside Claude Code:**

```
/plugin marketplace add tusshaarpd/skills
/plugin install pm-skills
```

Restart Claude Code (or start a new session) and the skills appear as slash commands.

---

## MAANG Interview Coach

Start with `/interview-coach` — it sets up your profile (role, level, target companies, target date), writes a phased 6–7 month roadmap, and tells you what to practice next. All state lives in `~/.claude/interview-coach/` (profile, roadmap, session log, story bank, debriefs) so progress carries across sessions.

| Skill | What it does |
|---|---|
| `/interview-coach` | Hub: `setup`, `roadmap`, `next`, `progress`, `loop <company>` (full simulated onsite with a hiring-committee verdict) |
| `/mock-product-sense` | Product design / "improve X" / favorite-product rounds (Meta, Google, Amazon, Apple style) with live probes and a scorecard |
| `/mock-product-strategy` | "Should company enter X", monetization, CEO-for-a-day, competitive response |
| `/mock-analytical` | Define metrics, diagnose a metric drop (interviewer holds a hidden ground truth), ship-or-not tradeoffs, A/B design |
| `/mock-estimation` | 10–15 min Fermi / market-sizing drills with sanity-check probes |
| `/mock-technical` | Technical PM / PM-T: explain how X works, API design, tradeoffs, challenging estimates, LLM literacy |
| `/mock-system-design` | TPM system design: feed, chat, notifications, dispatch, payments… with steered deep dives and failure injection |
| `/mock-program-execution` | TPM/EPM: run a multi-team program, rescue a slip, ownership conflicts, ambiguous mandates, incidents |
| `/mock-behavioral` | Company-calibrated behavioral: Amazon LPs with Bar Raiser-style probing, Meta L&D, Googleyness, Apple fit, Netflix culture |
| `/story-bank` | Build 12–15 STAR(L) stories mapped to LPs/signals, with coverage gaps and prepared follow-up answers |
| `/grade-answer` | Paste any answer, transcript, or written exercise → rubric scorecard, model answer, rewrite |
| `/interview-debrief` | Debrief a real interview within 24 h; grade from memory, infer signals, adjust the plan; offer/leveling coaching |
| `/strategist` | Personal strategist: turns "money, fame, luck" into concrete targets, finds the real bottleneck, ranked tactics with exact moves, tracks commitments and calls you out |
| `/daily-reflection` | 2-minute evening check-in that builds judgment: what you predicted, what happened, why the gap; weekly pattern review and a build-in-public nudge |
| `/speaking-coach` | Speak with confidence: 6-week plan, daily 5-min out-loud drills (record in Sound Recorder → local Whisper transcription with filler/pace analysis), prepare and rehearse leadership presentations with tough Q&A, calm-down routine |

Add `--voice` to any mock to answer out loud (record in Sound Recorder; transcribed locally by `scripts/analyze_speech.py`) and get delivery feedback — filler words, length, headline-first — alongside content.

Every mock ends with a **0–10 scorecard per dimension**, a **level verdict** (L4 / L5 / L6 bar), the **biggest gap**, a **model answer outline**, and **one drill** — and appends to the log so `/interview-coach progress` can show trends.

Shared references live in `skills/interview-coach/references/`:
- `companies.md` — loop shapes, what each company scores, all 16 Amazon LPs, level bars
- `frameworks.md` — answer skeletons for every round type
- `rubrics.md` — the scoring rubrics and scorecard format
- `question-bank.md` — 200+ questions by round and company, plus standard probes
- `system-design-cheatsheet.md` — numbers, building blocks, worked designs for TPM rounds
- `protocol.md` — how the mocks run

Suggested cadence: 2 product-sense + 2 behavioral + 1 analytical per week in months 1–2; add strategy/technical (PM) or system-design/program-execution (TPM) in months 3–4; full simulated loops in month 5; real interviews in months 6–7.

---

## The Minimalist Entrepreneur

| Skill | Command | When to use |
|-------|---------|-------------|
| **Find Community** | `/find-community` | Looking for a business idea, trying to find your community |
| **Validate Idea** | `/validate-idea` | Testing if a business idea is worth pursuing |
| **MVP** | `/mvp` | Ready to build your first product, struggling with scope |
| **Processize** | `/processize` | Have a product idea, want to deliver value by hand before writing code |
| **First Customers** | `/first-customers` | Have a product, need to find your first 100 customers |
| **Pricing** | `/pricing` | Setting prices, considering price changes |
| **Marketing Plan** | `/marketing-plan` | Have product-market fit, ready to scale with content |
| **Grow Sustainably** | `/grow-sustainably` | Making decisions about spending, hiring, or scaling |
| **Company Values** | `/company-values` | Defining culture, preparing to hire |
| **Minimalist Review** | `/minimalist-review` | Gut-checking any business decision |

The skills follow the book's progression: Community → Validate → Build → Processize → Sell → Price → Market → Grow → Culture → Review.

---

## Credits

- Minimalist Entrepreneur skills: [Sahil Lavingia](https://github.com/slavingia/skills), MIT.
- Interview coach frameworks draw on public material: the CIRCLES method (Lewis Lin), Cracking the PM Interview, the [system-design-primer](https://github.com/donnemartin/system-design-primer), and community prep guides ([vedika2609/pm_prep_guide](https://github.com/vedika2609/pm_prep_guide), [keianasnell/pm-interview-prep](https://github.com/keianasnell/pm-interview-prep)).

MIT License.
