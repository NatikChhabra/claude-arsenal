#!/usr/bin/env python3
"""lyric_lint.py: lint a song sheet's lyrics before anyone sings, synthesises or generates them. Stdlib only.

    python lyric_lint.py <SONG.md|lyrics.txt> [--bpm 96] [--json]     exit 0 clean (WARNs allowed), 1 on any FAIL
    python lyric_lint.py --selftest

Input: section headers in square brackets ([Verse 1], [Pre-Chorus], [Chorus], [Bridge], [Intro], [Outro], [Hook] ...),
one sung line per line. In a SONG.md only the "## Lyrics" section is read. Roman-script English, Hindi, Hinglish and
Punjabi all count syllables by vowel groups (a fair estimate for romanised Indic; English silent-e handled).

FAIL: an em or en dash; a banned word from the design plugin's one list (references/tells.md, read at run time, fallback
      list below); no chorus/hook section; the chorus never repeats (a song with one chorus is a poem).
WARN: AI-lyric cliche words (neon, echoes, whispers, shadows, ignite ...); a line in a repeated section whose syllable
      count is more than 3 away from the same line in its first occurrence (singers trip, generators drift); parallel
      verse lines more than 4 syllables apart; a line over 16 syllables (hard to sing at most tempos); the chorus's
      first line not repeated anywhere in the chorus (no anchor); with --bpm: the first chorus starting later than
      ~50 s at 4 beats per sung line (an estimate; time-to-chorus in charting pop has fallen under ~45 s, see
      references/songwriting.md); the same end-word rhymed 3+ times in one section.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TELLS = os.path.normpath(os.path.join(HERE, "..", "..", "design", "skills", "design", "references", "tells.md"))
FALLBACK_BANNED = ("unlock unleash supercharge seamless elevate empower revolutionize game-changer delve tapestry "
                   "testament realm embark foster pivotal crafted curated meticulously").split()
CLICHES = ("neon echo echoes whisper whispers whispering shadow shadows ignite ignites embers ember soar soaring "
           "symphony shattered shatter tapestry abyss eternity eternal celestial ethereal labyrinth odyssey "
           "kaleidoscope crimson velvet electric heartbeat starlight moonlight midnight").split()
DASH = re.compile("[" + chr(0x2013) + chr(0x2014) + "]")   # en and em dash, built from code points
HEADER = re.compile(r"^\s*\[([^\]]+)\]\s*$")


def banned_words():
    try:
        text = open(TELLS, encoding="utf-8").read()
        block = text.split("Banned words", 1)[1].split("```", 2)[1]
        words = []
        for line in block.splitlines():
            if line.lower().startswith("in instructions"):
                continue
            for w in line.split(","):
                w = re.sub(r"\(.*?\)", "", w).strip().lower()
                if w:
                    words.append(w)
        return words or FALLBACK_BANNED
    except (OSError, IndexError):
        return FALLBACK_BANNED


def syllables(line):
    total = 0
    for w in re.findall(r"[A-Za-z']+", line.lower()):
        w = w.replace("'", "")
        groups = re.findall(r"[aeiouy]+", w)
        n = len(groups)
        if n > 1 and w.endswith("e") and not w.endswith(("le", "ee", "ye")):
            n -= 1                                   # silent final e (English)
        total += max(1, n)
    return total


def parse(text):
    if "## Lyrics" in text:
        text = text.split("## Lyrics", 1)[1]
        text = re.split(r"\n## ", text, maxsplit=1)[0]
    sections, cur = [], None
    for raw in text.splitlines():
        m = HEADER.match(raw)
        if m:
            cur = {"name": m.group(1).strip(), "lines": []}
            sections.append(cur)
        elif raw.strip() and cur is not None and not raw.strip().startswith(("<!--", ">")):
            cur["lines"].append(raw.strip())
    return sections


def kind(name):
    n = name.lower()
    for k in ("pre-chorus", "prechorus", "chorus", "hook", "verse", "bridge", "intro", "outro", "post-chorus"):
        if k in n:
            return {"prechorus": "pre-chorus"}.get(k, k)
    return n


def lint(text, bpm=None):
    fails, warns = [], []
    sections = parse(text)
    if not sections:
        return ["no [Section] headers found"], []
    banned = banned_words()
    for s in sections:
        for i, line in enumerate(s["lines"], 1):
            where = f"[{s['name']}] line {i}"
            if DASH.search(line):
                fails.append(f"{where}: em or en dash")
            low = " " + re.sub(r"[^a-z' -]", " ", line.lower()) + " "
            for b in banned:
                if f" {b} " in low:
                    fails.append(f"{where}: banned word '{b}'")
            for c in CLICHES:
                if f" {c} " in low:
                    warns.append(f"{where}: AI-lyric cliche '{c}' (keep only if it is literally in the scene)")
            n = syllables(line)
            if n > 16:
                warns.append(f"{where}: {n} syllables, hard to sing (split it or cut words)")
        ends = [re.findall(r"[a-z']+", l.lower())[-1] for l in s["lines"] if re.findall(r"[a-z']+", l.lower())]
        for w in set(ends):
            if ends.count(w) >= 3 and kind(s["name"]) not in ("chorus", "hook"):
                warns.append(f"[{s['name']}]: end-word '{w}' used {ends.count(w)} times")
    choruses = [s for s in sections if kind(s["name"]) in ("chorus", "hook")]
    if not choruses:
        fails.append("no [Chorus] or [Hook] section")
    elif len(choruses) < 2:
        fails.append("the chorus appears once: repeat it (a hook needs repetition to land)")
    else:
        first = choruses[0]["lines"]
        if first and sum(l.lower() == first[0].lower() for l in first) < 2 and \
                not any(first[0].lower() in l.lower() for l in first[1:]):
            warns.append("chorus: its first line never comes back inside the chorus (no anchor line)")
    seen = {}
    for s in sections:
        k = kind(s["name"])
        if k in ("chorus", "hook", "pre-chorus", "post-chorus"):
            if k in seen and seen[k]["lines"]:
                for i, (a, b) in enumerate(zip(seen[k]["lines"], s["lines"]), 1):
                    if abs(syllables(a) - syllables(b)) > 3:
                        warns.append(f"[{s['name']}] line {i}: {syllables(b)} syllables vs {syllables(a)} in the first "
                                     f"[{seen[k]['name']}]")
            seen.setdefault(k, s)
    verses = [s for s in sections if kind(s["name"]) == "verse"]
    for v in verses[1:]:
        for i, (a, b) in enumerate(zip(verses[0]["lines"], v["lines"]), 1):
            if abs(syllables(a) - syllables(b)) > 4:
                warns.append(f"[{v['name']}] line {i}: {syllables(b)} syllables vs {syllables(a)} in "
                             f"[{verses[0]['name']}] (same melody?)")
    if bpm and choruses:
        before = 0
        for s in sections:
            if s is choruses[0]:
                break
            before += max(len(s["lines"]), 2 if kind(s["name"]) == "intro" else 0)
        secs = before * 4 * 60.0 / bpm
        if secs > 50:
            warns.append(f"first chorus at ~{secs:.0f} s (estimate: 4 beats per line at {bpm} BPM); aim under ~45-50 s")
    return fails, warns


SAMPLE_GOOD = """## Lyrics
[Verse 1]
Parking lot lights on Grove Street
Six missed calls and a cold seat
[Chorus]
Call me when the city sleeps
Call me when the money speaks
Call me when the city sleeps
[Verse 2]
Badge on the dash and a borrowed name
Same old corner, a different game
[Chorus]
Call me when the city sleeps
Call me when the money speaks
Call me when the city sleeps
"""


def selftest():
    ok = True
    f, w = lint(SAMPLE_GOOD, bpm=96)
    ok &= not f
    f, w = lint(SAMPLE_GOOD.replace("Six missed calls", "Six missed calls " + chr(0x2014) + " we unleash"))
    ok &= any("dash" in x for x in f) and any("unleash" in x for x in f)
    f, w = lint("[Verse]\nOne line\n[Chorus]\nOnly once\n")
    ok &= any("once" in x for x in f)
    f, w = lint(SAMPLE_GOOD.replace("Parking lot lights", "Neon echoes whisper"))
    ok &= any("cliche" in x for x in w)
    long_chorus = SAMPLE_GOOD.replace("Call me when the money speaks\nCall me when the city sleeps\n[Verse 2]",
                                      "Call me when the money speaks\nCall me when the city sleeps\n[Verse 2]", 1)
    f, w = lint(long_chorus.replace("[Chorus]\nCall me when the city sleeps\nCall me when the money speaks\nCall me when the city sleeps\n[Verse 2]",
                                    "[Chorus]\nCall me when the city sleeps tonight and every single night until the morning\nCall me\nCall me when the city sleeps\n[Verse 2]"))
    ok &= any("syllables" in x for x in w)
    ok &= syllables("Bhai ye kya tha yaar") == 5 and syllables("Parking lot lights") == 4
    print("selftest", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    args = [a for a in argv if not a.startswith("--")]
    if not args:
        print(__doc__)
        return 2
    bpm = None
    if "--bpm" in argv:
        bpm = float(argv[argv.index("--bpm") + 1])
        args = [a for a in args if a != argv[argv.index("--bpm") + 1]]
    text = open(args[0], encoding="utf-8").read()
    fails, warns = lint(text, bpm)
    if "--json" in argv:
        print(json.dumps({"fail": fails, "warn": warns}, indent=2))
    else:
        for x in fails:
            print("FAIL", x)
        for x in warns:
            print("WARN", x)
        print(f"lyric_lint: {len(fails)} FAIL, {len(warns)} WARN")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
