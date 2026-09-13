# Astrology as a decision input — the objective version

Read this before including any astrological input in a decision. It has three parts: (1) what the evidence says about accuracy, (2) the top GitHub repos and what they actually do, (3) the calculation method and the traditional interpretation rules for career/life questions — labeled as tradition, not evidence.

---

## 1. Accuracy — what has actually been measured

Separate two things:

**A. Astronomical accuracy (where the planets are).** Very high and verifiable. The Swiss Ephemeris (Astrodienst) reproduces NASA JPL DE431 positions to about 0.001 arc-seconds for planets across 13,000 years. Our script uses it. Any two competent programs will give the same chart from the same birth data.

**B. Predictive accuracy (what the chart *means* for your life).** No controlled study has found it beats chance. The main ones:
- **Carlson, S. (1985), *Nature* 318:419–425.** Double-blind test with 28 astrologers chosen by astrologers themselves. They matched natal charts to personality profiles at chance level (~1 in 3, where chance was 1 in 3). Astrologers had predicted they'd score ≥50%.
- **Dean, G. & Kelly, I. (2003), *Journal of Consciousness Studies*.** 2,000+ "time twins" born within minutes of each other in London, tracked across 100+ traits over decades. No similarity above chance.
- **McGrew & McFall (1990), *Journal of Scientific Exploration*.** Six astrologers matched charts to extensive case files: chance level; astrologers didn't even agree with each other.
- **Meta-analyses (Dean, Mather, Nias, Smit; ~40 tests, ~700 astrologers).** Effect sizes ≈ 0; astrologers' confidence unrelated to accuracy.
- **Vedic-specific:** Narlikar et al. (2009), *Current Science* — 27 Indian astrologers and one institution given 40 charts (half of children with high intelligence, half with cognitive disability) to sort: chance level (~50%). No published test of Vedic predictive methods (dashas, transits) has shown above-chance results.

Objective summary: chart calculation = fact. Chart interpretation = belief with no demonstrated predictive power. Astrologers' "hit rate" in practice comes from the Barnum/Forer effect (vague statements feel personal), confirmation bias (remembering hits), and cold reading (adjusting to the client's reactions).

**Therefore, in this skill:** astrology gets the lowest weight of all inputs, is always labeled "belief/tradition", and is used for what it *can* do objectively: reveal what the user values, fears, and hopes for, and expose timing preferences — so those can be examined directly.

---

## 2. Top GitHub repos (checked 2026-09-14, ranked by stars, relevant ones only)

| Repo | Stars | What it is | Useful for |
|---|---|---|---|
| [aloistr/swisseph](https://github.com/aloistr/swisseph) | 724 | Swiss Ephemeris, official C source (Astrodienst) | The accuracy standard. Everything below depends on it. |
| [astrorigin/pyswisseph](https://github.com/astrorigin/pyswisseph) | 397 | Python binding to Swiss Ephemeris | **What our script uses.** `pip install pyswisseph` |
| [g-battaglia/kerykeion](https://github.com/g-battaglia/kerykeion) | 704 | Python library: Western natal/synastry/transit charts, SVG output, JSON data | Western charts with pictures. Same engine. |
| [CNWU16/vedic-astro-skills](https://github.com/CNWU16/vedic-astro-skills) | 862 | Claude Code / agent skill suite for Vedic astrology: calculator, core reading, career, love, prashna, synastry, rectifier. Chinese/Japanese-first, ~5,500 lines of rules | The most complete "how a Vedic astrologer reasons" ruleset in skill form. Its career method is summarized in §3 below. Heavy deps (PyJHora + ephemeris files). |
| [naturalstupid/PyJHora](https://github.com/naturalstupid/PyJHora) | 221 | Python: nearly everything in Vedic astrology (dashas, divisional charts, ashtakavarga, shadbala, yogas) | Reference implementation if you want more than our script computes. |
| [VedAstro/VedAstro](https://github.com/VedAstro/VedAstro) (+ VedAstro.Python) | 641 / 74 | Non-profit open Vedic astrology app + API + Python lib | Free web UI for a full Vedic chart if the user wants pictures. |
| [FANzR-arch/Numerologist_skills](https://github.com/FANzR-arch/Numerologist_skills) | 1,181 | "Anti-hallucination" framework for Chinese astrology (Bazi) in LLMs — fixed calculation, then interpretation | Not Vedic/Western, but its design principle is right: compute first, never let the LLM guess planet positions. We follow that. |
| [SylarLong/iztro](https://github.com/SylarLong/iztro) | 4,152 | Zi Wei Dou Shu (Chinese "Purple Star") astrolabe library | Highest-starred astrology repo overall; Chinese system, not relevant unless the user follows it. |
| [theriftlab/immanuel-python](https://github.com/theriftlab/immanuel-python) | 114 | Human-readable + JSON chart data on Swiss Ephemeris | Clean alternative to kerykeion. |
| [webresh/drik-panchanga](https://github.com/webresh/drik-panchanga) | 143 | Hindu calendar (tithi, nakshatra, muhurta) from Swiss Ephemeris | If the user wants "auspicious date" calculations. |

None of these claims or demonstrates predictive accuracy; they compute positions and encode traditional interpretation rules. The "accuracy" a repo advertises always refers to the astronomy.

---

## 3. What our script computes and how the tradition reads it (labeled)

`scripts/astro_chart.py --date YYYY-MM-DD --time HH:MM --city <name>` (or `--lat --lon --tz`). Add `--asof YYYY-MM-DD` to evaluate timing at a future date, `--json` for data.

**Objective outputs (astronomy):**
- Vedic (sidereal, Lahiri ayanamsa, whole-sign houses): ascendant, Moon sign and nakshatra, 9 planets with sign/degree/house/retrograde, D9 (navamsa) and D10 (dasamsa) signs.
- Vimshottari dasha timeline: all 9 mahadashas with dates, current mahadasha/antardasha, upcoming antardashas.
- Transits at the as-of date: Saturn, Jupiter, Rahu sign and house-from-Moon; Sade Sati status and phase; Saturn dhaiya.
- Western (tropical, Placidus): ascendant, 11 bodies with sign/degree/house.

**Birth time caveat (objective):** the ascendant changes sign roughly every 2 hours. Unknown or rounded birth time → houses, D9/D10, and dasha start dates are unreliable (dasha dates can shift by months). Always ask how certain the time is and say so in the output.

**How the Vedic tradition reads career (from the vedic-career ruleset and standard texts — this is what an astrologer would say, not evidence):**
- **10th house** (from ascendant) and its lord: the nature of work. Planets in or aspecting it: Sun → authority/government/leadership; Moon → public-facing, care, food; Mars → engineering, defense, surgery, sports; Mercury → analysis, writing, trade, tech; Jupiter → teaching, law, finance, advisory; Venus → design, arts, luxury, media; Saturn → long-grind fields, infrastructure, labor, discipline; Rahu → tech, foreign, unconventional, fast rise; Ketu → research, spiritual, behind-the-scenes.
- **D10 (dasamsa)**: the "career chart"; the sign and planets there refine the above.
- **2nd house** (earned wealth), **11th** (gains, network, large income), **9th** (luck/fortune), **5th** (intelligence, speculation). Strong benefics or lords well-placed here are read as wealth indicators.
- **Timing — dashas:** the mahadasha/antardasha lord's house rulership and placement says which life area is "active". A period ruled by the 10th/11th lord or a well-placed planet is read as career/gain time; a period of the 6th/8th/12th lord as struggle/change/loss. Dasha changes are read as life-chapter changes.
- **Timing — transits:** Jupiter transiting the 2nd/5th/7th/9th/11th from Moon is read as favorable; Saturn in the 12th/1st/2nd from Moon = **Sade Sati** (~7.5 years, read as pressure, hard work, restructuring; not "bad luck" in the serious texts — effort with delayed reward); Saturn in the 3rd/6th/11th from Moon read as favorable.
- **Yogas** named for career/wealth: Raja yoga (lords of kendra 1/4/7/10 and trikona 1/5/9 together), Dhana yoga (2nd/11th/5th/9th lords linked), Gaja Kesari (Jupiter in kendra from Moon), Budhaditya (Sun+Mercury together, read as intellect). Presence of these is what astrologers point to for "success".

**How to use all of this in a decision (the rule in SKILL.md):** run the script, report the objective timing facts (e.g., "Sun mahadasha started May 2026; Saturn is on your natal Moon until 2027 — the tradition calls this Sade Sati peak"), state in one line what the tradition would say, label it "belief", and then ask: *what does this tell us about what you're hoping or afraid of?* That question is where the real decision information is. Never let a dasha or transit override facts, math, or the user's own track record. If the user wants to time an action to astrology and the cost of waiting is low, that's a legitimate preference; if the cost of waiting is high, say so with the number.
