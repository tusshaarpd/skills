#!/usr/bin/env python
"""
Compute a natal chart (Western tropical + Vedic sidereal/Lahiri) and current
Vedic timing factors, using the Swiss Ephemeris (the accuracy standard for
planetary positions — matches NASA JPL to well under 1 arc-second).

WHAT THIS DOES: astronomy. Planet positions, signs, houses, nakshatra,
Vimshottari dasha periods, current Saturn/Jupiter transits. These numbers are
objectively correct for the given birth data.

WHAT THIS DOES NOT DO: prove anything about the future. No controlled study
has shown astrological interpretation predicts life outcomes better than chance.
Treat the output as "what the tradition would say", not evidence.

Usage:
  python astro_chart.py --date 1995-08-15 --time 14:30 --city Mumbai
  python astro_chart.py --date 1995-08-15 --time 14:30 --lat 19.076 --lon 72.877 --tz 5.5
  add --json for machine-readable output; --asof YYYY-MM-DD to evaluate transits at a date

Birth time matters: the ascendant moves 1 sign every ~2 hours. If the time is
unknown or approximate, say so — house-based results are unreliable then.
"""
import argparse
import datetime as dt
import json
import sys

import swisseph as swe

SIGNS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio",
         "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
NAKSHATRAS = ["Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu",
              "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta",
              "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
              "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha", "Purva Bhadrapada",
              "Uttara Bhadrapada", "Revati"]
# Vimshottari: lord sequence starting from Ashwini, and years per lord (total 120)
DASHA_LORDS = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]
DASHA_YEARS = {"Ketu": 7, "Venus": 20, "Sun": 6, "Moon": 10, "Mars": 7, "Rahu": 18,
               "Jupiter": 16, "Saturn": 19, "Mercury": 17}
PLANETS = [("Sun", swe.SUN), ("Moon", swe.MOON), ("Mercury", swe.MERCURY), ("Venus", swe.VENUS),
           ("Mars", swe.MARS), ("Jupiter", swe.JUPITER), ("Saturn", swe.SATURN),
           ("Rahu", swe.MEAN_NODE)]
# Uranus/Neptune/Pluto for Western only
OUTER = [("Uranus", swe.URANUS), ("Neptune", swe.NEPTUNE), ("Pluto", swe.PLUTO)]

# Small built-in gazetteer so users don't need lat/lon. (lat, lon, tz offset hours)
CITIES = {
    "mumbai": (19.076, 72.877, 5.5), "delhi": (28.614, 77.209, 5.5), "new delhi": (28.614, 77.209, 5.5),
    "bangalore": (12.972, 77.594, 5.5), "bengaluru": (12.972, 77.594, 5.5), "hyderabad": (17.385, 78.487, 5.5),
    "chennai": (13.083, 80.270, 5.5), "kolkata": (22.573, 88.364, 5.5), "pune": (18.520, 73.857, 5.5),
    "ahmedabad": (23.023, 72.571, 5.5), "jaipur": (26.912, 75.787, 5.5), "lucknow": (26.847, 80.947, 5.5),
    "kanpur": (26.450, 80.332, 5.5), "nagpur": (21.146, 79.088, 5.5), "indore": (22.720, 75.858, 5.5),
    "bhopal": (23.260, 77.413, 5.5), "patna": (25.594, 85.138, 5.5), "chandigarh": (30.734, 76.779, 5.5),
    "kochi": (9.931, 76.267, 5.5), "thiruvananthapuram": (8.524, 76.937, 5.5), "coimbatore": (11.017, 76.956, 5.5),
    "visakhapatnam": (17.687, 83.219, 5.5), "surat": (21.170, 72.831, 5.5), "vadodara": (22.307, 73.181, 5.5),
    "gurgaon": (28.459, 77.027, 5.5), "gurugram": (28.459, 77.027, 5.5), "noida": (28.535, 77.391, 5.5),
    "dehradun": (30.317, 78.032, 5.5), "guwahati": (26.144, 91.736, 5.5), "bhubaneswar": (20.296, 85.825, 5.5),
    "ranchi": (23.344, 85.310, 5.5), "raipur": (21.251, 81.630, 5.5), "varanasi": (25.318, 82.974, 5.5),
    "agra": (27.177, 78.008, 5.5), "amritsar": (31.634, 74.872, 5.5), "mysore": (12.296, 76.639, 5.5),
    "mangalore": (12.914, 74.856, 5.5), "vijayawada": (16.507, 80.648, 5.5), "nashik": (19.997, 73.790, 5.5),
    "london": (51.507, -0.128, 0.0), "new york": (40.713, -74.006, -5.0), "san francisco": (37.775, -122.419, -8.0),
    "seattle": (47.606, -122.332, -8.0), "dubai": (25.205, 55.271, 4.0), "singapore": (1.352, 103.820, 8.0),
    "sydney": (-33.869, 151.209, 10.0), "toronto": (43.653, -79.383, -5.0), "kathmandu": (27.717, 85.324, 5.75),
    "dhaka": (23.811, 90.412, 6.0), "colombo": (6.927, 79.861, 5.5), "karachi": (24.861, 67.010, 5.0),
}


def sign_of(lon):
    return SIGNS[int(lon // 30) % 12]


def dms(lon):
    d = lon % 30
    return f"{int(d)}°{int((d % 1) * 60):02d}'"


def navamsa_sign(lon):
    s = int(lon // 30) % 12
    part = int((lon % 30) // (30 / 9))
    start = s if s % 3 == 0 else (s + 8 if s % 3 == 1 else s + 4)  # movable / fixed / dual
    return SIGNS[(start + part) % 12]


def dasamsa_sign(lon):
    s = int(lon // 30) % 12
    part = int((lon % 30) // 3)
    start = s if s % 2 == 0 else s + 8  # odd signs (Aries=0) from self, even from 9th
    return SIGNS[(start + part) % 12]


def julian_day(date, time, tz):
    local = dt.datetime.combine(date, time)
    utc = local - dt.timedelta(hours=tz)
    return swe.julday(utc.year, utc.month, utc.day, utc.hour + utc.minute / 60 + utc.second / 3600)


def positions(jd, sidereal):
    flags = swe.FLG_SWIEPH | swe.FLG_SPEED
    if sidereal:
        swe.set_sid_mode(swe.SIDM_LAHIRI)
        flags |= swe.FLG_SIDEREAL
    out = {}
    plist = PLANETS if sidereal else PLANETS + OUTER
    for name, pid in plist:
        pos, _ = swe.calc_ut(jd, pid, flags)
        out[name] = {"lon": pos[0] % 360, "retro": pos[3] < 0}
    if "Rahu" in out:
        out["Ketu"] = {"lon": (out["Rahu"]["lon"] + 180) % 360, "retro": True}
    return out


def ascendant(jd, lat, lon, sidereal):
    if sidereal:
        swe.set_sid_mode(swe.SIDM_LAHIRI)
        cusps, ascmc = swe.houses_ex(jd, lat, lon, b"W", swe.FLG_SIDEREAL)  # whole sign
    else:
        cusps, ascmc = swe.houses(jd, lat, lon, b"P")  # Placidus
    return ascmc[0] % 360, list(cusps)


def house_of(lon, asc_lon, cusps, sidereal):
    if sidereal:  # whole-sign houses
        return (int(lon // 30) - int(asc_lon // 30)) % 12 + 1
    # Placidus: find cusp interval
    for i in range(12):
        a, b = cusps[i], cusps[(i + 1) % 12]
        if a <= b:
            if a <= lon < b:
                return i + 1
        else:
            if lon >= a or lon < b:
                return i + 1
    return 12


def vimshottari(moon_lon, birth):
    nak_len = 360 / 27
    idx = int(moon_lon // nak_len)
    frac = (moon_lon % nak_len) / nak_len
    lord_i = idx % 9
    periods = []
    start = birth
    # first (birth) dasha balance
    first_lord = DASHA_LORDS[lord_i]
    bal = DASHA_YEARS[first_lord] * (1 - frac)
    end = start + dt.timedelta(days=bal * 365.25)
    periods.append((first_lord, start, end))
    for k in range(1, 9):
        lord = DASHA_LORDS[(lord_i + k) % 9]
        start = end
        end = start + dt.timedelta(days=DASHA_YEARS[lord] * 365.25)
        periods.append((lord, start, end))
    return NAKSHATRAS[idx], periods


def antardashas(md_lord, md_start, md_end):
    total_days = (md_end - md_start).days
    i = DASHA_LORDS.index(md_lord)
    out, start = [], md_start
    for k in range(9):
        lord = DASHA_LORDS[(i + k) % 9]
        days = total_days * DASHA_YEARS[lord] / 120
        end = start + dt.timedelta(days=days)
        out.append((lord, start, end))
        start = end
    return out


def transits(asof_jd, natal_moon_sign_idx):
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    flags = swe.FLG_SWIEPH | swe.FLG_SIDEREAL
    res = {}
    for name, pid in [("Saturn", swe.SATURN), ("Jupiter", swe.JUPITER), ("Rahu", swe.MEAN_NODE)]:
        pos, _ = swe.calc_ut(asof_jd, pid, flags)
        s = int(pos[0] // 30) % 12
        rel = (s - natal_moon_sign_idx) % 12 + 1  # house from Moon
        res[name] = {"sign": SIGNS[s], "house_from_moon": rel}
    sat_rel = res["Saturn"]["house_from_moon"]
    res["sade_sati"] = sat_rel in (12, 1, 2)
    res["sade_sati_phase"] = {12: "first (rising)", 1: "peak (Saturn on Moon)", 2: "last (setting)"}.get(sat_rel)
    res["saturn_dhaiya"] = sat_rel in (4, 8)  # 'small panoti'
    return res


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="YYYY-MM-DD (local birth date)")
    ap.add_argument("--time", required=True, help="HH:MM local (24h). Use best estimate; say if unsure.")
    ap.add_argument("--city", help="one of the built-in cities (e.g. Mumbai). Else give --lat --lon --tz")
    ap.add_argument("--lat", type=float)
    ap.add_argument("--lon", type=float)
    ap.add_argument("--tz", type=float, help="UTC offset in hours at birth (India = 5.5)")
    ap.add_argument("--asof", help="YYYY-MM-DD for transit/dasha evaluation (default today)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.city:
        key = a.city.strip().lower()
        if key not in CITIES:
            sys.exit(f"Unknown city '{a.city}'. Give --lat --lon --tz instead. Known: {', '.join(sorted(CITIES))}")
        lat, lon, tz = CITIES[key]
    else:
        if a.lat is None or a.lon is None or a.tz is None:
            sys.exit("Need --city or all of --lat --lon --tz")
        lat, lon, tz = a.lat, a.lon, a.tz

    date = dt.date.fromisoformat(a.date)
    h, m = map(int, a.time.split(":"))
    time = dt.time(h, m)
    jd = julian_day(date, time, tz)
    birth_dt = dt.datetime.combine(date, time)
    asof = dt.date.fromisoformat(a.asof) if a.asof else dt.date.today()
    asof_jd = swe.julday(asof.year, asof.month, asof.day, 12.0)

    # Vedic
    vp = positions(jd, sidereal=True)
    vasc, vcusps = ascendant(jd, lat, lon, sidereal=True)
    vedic = {}
    for name, p in vp.items():
        vedic[name] = {
            "sign": sign_of(p["lon"]), "deg": dms(p["lon"]), "retro": p["retro"],
            "house": house_of(p["lon"], vasc, vcusps, True),
            "D9": navamsa_sign(p["lon"]), "D10": dasamsa_sign(p["lon"]),
        }
    moon_lon = vp["Moon"]["lon"]
    nak, mds = vimshottari(moon_lon, birth_dt)
    now = dt.datetime.combine(asof, dt.time(12))
    cur_md = next((x for x in mds if x[1] <= now < x[2]), mds[-1])
    ads = antardashas(*cur_md)
    cur_ad = next((x for x in ads if x[1] <= now < x[2]), ads[-1])
    tr = transits(asof_jd, int(moon_lon // 30))

    # Western
    wp = positions(jd, sidereal=False)
    wasc, wcusps = ascendant(jd, lat, lon, sidereal=False)
    western = {name: {"sign": sign_of(p["lon"]), "deg": dms(p["lon"]), "retro": p["retro"],
                      "house": house_of(p["lon"], wasc, wcusps, False)} for name, p in wp.items() if name != "Ketu"}

    result = {
        "input": {"date": a.date, "time": a.time, "lat": lat, "lon": lon, "tz": tz, "asof": asof.isoformat()},
        "vedic": {
            "ayanamsa": "Lahiri", "houses": "whole sign",
            "ascendant": {"sign": sign_of(vasc), "deg": dms(vasc)},
            "moon_nakshatra": nak, "moon_sign": sign_of(moon_lon),
            "planets": vedic,
            "mahadashas": [{"lord": l, "from": s.date().isoformat(), "to": e.date().isoformat()} for l, s, e in mds],
            "current_mahadasha": {"lord": cur_md[0], "from": cur_md[1].date().isoformat(), "to": cur_md[2].date().isoformat()},
            "current_antardasha": {"lord": cur_ad[0], "from": cur_ad[1].date().isoformat(), "to": cur_ad[2].date().isoformat()},
            "transits_asof": tr,
        },
        "western": {
            "zodiac": "tropical", "houses": "Placidus",
            "ascendant": {"sign": sign_of(wasc), "deg": dms(wasc)},
            "planets": western,
        },
    }

    if a.json:
        print(json.dumps(result, indent=2))
        return

    v = result["vedic"]
    print(f"Birth: {a.date} {a.time} (UTC{tz:+}) at {lat:.3f},{lon:.3f}   Evaluated as of: {asof}")
    print("\n== VEDIC (sidereal, Lahiri, whole-sign houses) ==")
    print(f"Ascendant (Lagna): {v['ascendant']['sign']} {v['ascendant']['deg']}")
    print(f"Moon sign (Rashi): {v['moon_sign']}   Nakshatra: {v['moon_nakshatra']}")
    print(f"{'Planet':9} {'Sign':12} {'Deg':8} {'H':>2}  {'D9 (Navamsa)':13} {'D10 (Dasamsa)':13} R")
    for name, p in vedic.items():
        print(f"{name:9} {p['sign']:12} {p['deg']:8} {p['house']:>2}  {p['D9']:13} {p['D10']:13} {'R' if p['retro'] else ''}")
    print("\nVimshottari Mahadashas:")
    for md in v["mahadashas"]:
        mark = " <-- now" if md["lord"] == cur_md[0] and md["from"] == cur_md[1].date().isoformat() else ""
        print(f"  {md['lord']:8} {md['from']} -> {md['to']}{mark}")
    print(f"Current: {cur_md[0]} mahadasha / {cur_ad[0]} antardasha ({cur_ad[1].date()} -> {cur_ad[2].date()})")
    print("Upcoming antardashas in this mahadasha:")
    for l, s, e in ads:
        if e.date() >= asof:
            print(f"  {l:8} {s.date()} -> {e.date()}")
    t = v["transits_asof"]
    print(f"\nTransits as of {asof}: Saturn in {t['Saturn']['sign']} (house {t['Saturn']['house_from_moon']} from Moon); "
          f"Jupiter in {t['Jupiter']['sign']} (house {t['Jupiter']['house_from_moon']} from Moon); "
          f"Rahu in {t['Rahu']['sign']} (house {t['Rahu']['house_from_moon']} from Moon)")
    print(f"Sade Sati active: {'YES — ' + t['sade_sati_phase'] + ' phase' if t['sade_sati'] else 'no'}"
          f"   Saturn dhaiya (4th/8th from Moon): {'yes' if t['saturn_dhaiya'] else 'no'}")

    w = result["western"]
    print("\n== WESTERN (tropical, Placidus houses) ==")
    print(f"Ascendant: {w['ascendant']['sign']} {w['ascendant']['deg']}")
    for name, p in western.items():
        print(f"{name:9} {p['sign']:12} {p['deg']:8} H{p['house']:<2} {'R' if p['retro'] else ''}")

    print("\nNOTE: positions above are astronomically accurate. Any *meaning* attached to them is belief, "
          "not evidence — no controlled study has shown astrological prediction beats chance.")


if __name__ == "__main__":
    main()
