#!/usr/bin/env python
"""
Analyze a recording of you speaking: transcript, filler words, pace, pauses, restarts.

Usage:
    python analyze_speech.py <audio-file> [--model small] [--json]

Works with .m4a .mp3 .wav .webm .mp4 .ogg (anything ffmpeg can read).
First run downloads the Whisper model (~150 MB for "small"); later runs are offline.

Filler detection: Whisper normally drops "um"/"uh". We pass a prompt full of
disfluencies so it keeps them. Not perfect, but consistent — compare your own
numbers day to day rather than treating them as absolute truth.
"""
import argparse
import json
import os
import re
import sys
from collections import Counter

# Windows without Developer Mode can't create symlinks in the model cache.
os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS", "1")
os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")

FILLERS_SINGLE = {
    "um", "umm", "uh", "uhh", "er", "erm", "ah", "hmm", "mm",
    "like", "so", "basically", "actually", "literally", "right", "okay", "ok",
}
FILLERS_MULTI = [
    "you know", "i mean", "kind of", "sort of", "you see", "i guess",
]
HEDGES = ["i think", "maybe", "probably", "i feel like", "sort of", "kind of", "i'm not sure", "perhaps"]
FILLER_PROMPT = (
    "Um, so, uh, I think, like, you know, basically, hmm, er, actually, "
    "I mean, sort of, kind of, umm, uhh, right, okay so."
)


def transcribe(path, model_size):
    from faster_whisper import WhisperModel

    model = WhisperModel(model_size, device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        path,
        word_timestamps=True,
        initial_prompt=FILLER_PROMPT,
        vad_filter=False,
        condition_on_previous_text=False,
    )
    words = []
    for seg in segments:
        for w in seg.words or []:
            words.append({"word": w.word.strip(), "start": w.start, "end": w.end})
    return words, info.duration


def norm(w):
    return re.sub(r"[^a-z']", "", w.lower())


def analyze(words, duration):
    tokens = [norm(w["word"]) for w in words]
    tokens = [t for t in tokens if t]
    text = " ".join(tokens)

    # fillers
    filler_counts = Counter()
    for t in tokens:
        if t in FILLERS_SINGLE:
            filler_counts[t] += 1
    for phrase in FILLERS_MULTI:
        n = len(re.findall(r"\b" + re.escape(phrase) + r"\b", text))
        if n:
            filler_counts[phrase] += n
    # "so"/"like"/"right"/"okay" only count as fillers when they start a clause or repeat;
    # we keep it simple: count them, but report them separately so you can judge.
    soft = {k: v for k, v in filler_counts.items() if k in {"so", "like", "right", "okay", "ok", "actually", "basically", "literally"}}
    hard = {k: v for k, v in filler_counts.items() if k not in soft}

    hedges = Counter()
    for h in HEDGES:
        n = len(re.findall(r"\b" + re.escape(h) + r"\b", text))
        if n:
            hedges[h] += n

    # restarts: same word repeated back to back ("I I", "the the", "we we")
    restarts = sum(1 for a, b in zip(tokens, tokens[1:]) if a == b and len(a) > 1)

    # pauses > 1.5s between words
    pauses = []
    for a, b in zip(words, words[1:]):
        gap = b["start"] - a["end"]
        if gap >= 1.5:
            pauses.append(round(gap, 1))

    spoken = duration if duration else (words[-1]["end"] if words else 0)
    minutes = max(spoken / 60.0, 1e-6)
    wpm = len(tokens) / minutes
    fillers_per_min = sum(hard.values()) / minutes

    first_sentence = " ".join(w["word"] for w in words[:18])

    return {
        "duration_sec": round(spoken, 1),
        "words": len(tokens),
        "wpm": round(wpm),
        "hard_fillers": dict(hard),
        "hard_filler_total": sum(hard.values()),
        "hard_fillers_per_min": round(fillers_per_min, 1),
        "soft_fillers": dict(soft),
        "hedges": dict(hedges),
        "restarts": restarts,
        "long_pauses": pauses,
        "opening": first_sentence,
        "transcript": " ".join(w["word"] for w in words),
    }


def verdict(r):
    lines = []
    wpm = r["wpm"]
    pace = "good" if 130 <= wpm <= 165 else ("too fast" if wpm > 165 else "slow (fine if deliberate)")
    lines.append(f"Length: {r['duration_sec']}s · {r['words']} words · Pace: {wpm} wpm ({pace}; aim 130–160)")
    hf = r["hard_fillers"]
    hf_str = ", ".join(f"{k} ×{v}" for k, v in sorted(hf.items(), key=lambda x: -x[1])) or "none"
    lines.append(f"Fillers: {r['hard_filler_total']} ({hf_str}) → {r['hard_fillers_per_min']}/min (aim < 3/min)")
    if r["soft_fillers"]:
        lines.append("Watch words: " + ", ".join(f"{k} ×{v}" for k, v in r["soft_fillers"].items()))
    if r["hedges"]:
        lines.append("Hedging: " + ", ".join(f"{k} ×{v}" for k, v in r["hedges"].items()) + "  (cut these — say it plainly)")
    lines.append(f"Restarts (repeated words): {r['restarts']}   Long pauses (>1.5s): {len(r['long_pauses'])}")
    lines.append(f"Opening: \"{r['opening']}…\"")
    lines.append("")
    lines.append("Transcript:")
    lines.append(r["transcript"])
    return "\n".join(lines)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # Windows consoles default to cp1252
    except AttributeError:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("--model", default="small", help="tiny | base | small | medium (small is the sweet spot)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    words, duration = transcribe(args.audio, args.model)
    if not words:
        print("No speech detected.", file=sys.stderr)
        sys.exit(1)
    r = analyze(words, duration)
    if args.json:
        print(json.dumps(r, indent=2))
    else:
        print(verdict(r))


if __name__ == "__main__":
    main()
