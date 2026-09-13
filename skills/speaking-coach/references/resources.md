# Speaking resources — what to use outside Claude Code

Short list. Only things worth the user's time. Use plain language when recommending.

## Do this first: Toastmasters (real people, weekly)

- What: a club that meets weekly. Everyone gives short speeches and does **Table Topics** — you're handed a random question and speak for 1–2 minutes with no prep. That is impromptu training with real faces and real nerves.
- Why it's the best option: no app gives you the feeling of 15 people looking at you. That feeling is what has to become normal before a leadership room feels normal.
- How: find a nearby club at https://www.toastmasters.org/find-a-club — visit as a guest first (free), then join (~$60–100 per 6 months). Go every week for the length of the prep plan.
- Ask the club for the **Table Topics** role every meeting for the first 2 months.

## Phone apps for extra reps (free tiers)

- **Impromptly** — https://impromptly.ai — spin a random topic, speak for 60 seconds, get instant feedback on fillers, pace, clarity. Closest to a daily impromptu drill.
- **Orai** — https://orai.com — AI feedback on pace, fillers, energy. Has lessons.
- **Yoodli** — https://yoodli.ai — records you on video, counts fillers, checks pacing; also does mock interview questions. Good free tier.
- Use these on days you can't sit at the laptop. The laptop analyzer in this skill is still the main tool because it logs progress.

## The local analyzer in this skill (main daily tool)

`scripts/analyze_speech.py` — record in Windows Sound Recorder, run the script, get fillers, pace, hedges, restarts, pauses, and a transcript. Runs on this machine only; nothing uploaded. Setup: `pip install faster-whisper "ctranslate2==4.4.0"` plus ffmpeg (both already installed here). Keep ctranslate2 at 4.4.0 — newer versions crash with a memory error on Windows.

## Open-source repos (checked 2026-09-14 — none worth installing)

There's no well-rated open-source speaking coach. These are all 0–4 star hackathon projects that do the same transcribe → count fillers → measure pace thing the analyzer above does:
- rahdeva/speak-on-spot (4★) — impromptu practice app
- AustinBao/Orator (3★) — real-time feedback
- larymak/speakforge — gamified lessons
- sunnydev07/Open-Speech — Android drills
- kelvinkamau0010-droid/articulate1 — impromptu + filler counting
- MR-WHOAMEYE/AI-POWERED-PRESENTATION-COACH — camera + speech rate + Gemini
If the user asks for a repo again, say this plainly and point them to the analyzer + Toastmasters instead.

## Books / talks worth the time (pick one)

- *Talk Like TED* (Carmine Gallo) — structure and stories, fast read.
- *The Quick and Easy Way to Effective Speaking* (Dale Carnegie) — old but the confidence advice still holds.
- Matt Abrahams, *Think Faster, Talk Smarter* — specifically about impromptu speaking; the "what / so what / now what" shape is a good alternative to PREP.
- YouTube: Vinh Giang's videos on vocal variety and pausing (short, practical).

## Shapes for impromptu answers (teach one, drill it until automatic)

- **PREP** — Point, Reason, Example, Point. Default.
- **What / So what / Now what** — good for updates to leaders.
- **Past / Present / Future** — good for "tell me about yourself" and status.
- **Problem / Solution / Benefit** — good for pitching an idea.

## Rules of thumb to repeat often

- Fumbling is a structure problem plus a body problem. Fix structure with a shape and a scripted first sentence. Fix the body with slow speech, pauses, and reps.
- Pace: 130–160 words per minute. Fillers: under 3 per minute.
- A 2-second pause feels long to you and confident to them.
- Say the answer first. Then the reasons. Then stop.
