#!/usr/bin/env python3
"""title.py - lint a YouTube title and thumbnail pairing before you publish it.

    python3 title.py --title "..." --thumb "AI RAN IT"
    python3 title.py titles.txt            # one per line, ranked
    python3 title.py --title "..." --json
    python3 title.py --short titles.txt    # a Short's title (no suffix, the 60/40 cuts)
    python3 title.py --selftest

The pairing is the unit, not the title. A title that repeats the thumbnail text wastes half the
click surface, and that is the single most common mistake this checks for.

Long video (default): the channel's title template lives in CONFIG below. Numbers behind the defaults
(4,403 videos of small channels, each scored against its own channel's median): titles <= 50 chars
lose (0.83x), over 70 is fine (1.25x), a first-person premise wins (1.31x), a true number is a bonus
(1.23x, never required), an audience-language word as a suffix ("| <Topic> Hindi") won 1.44x for a
non-English audience. Truncation is judged on the premise (what a cut title shows).
Short (--short): YouTube truncates around 60 characters on desktop search and around 40 on a mobile
home feed; no suffix (the first frame decides a Short, not the title).
"""
import json, re, sys, os

# The channel's title template: edit this dict, nothing else. Neutral defaults: no suffix required.
CONFIG = {
    # Long titles must end with this. "{topic}" = the game/subject as people search it. None = no suffix rule.
    # Example: "| {topic} Hindi" (a language signal), "| {topic} Speedrun", "({topic} Guide)".
    "suffix": None,
    "suffix_why": "the channel's title template",   # printed when a title misses the suffix
    "first_person": True,                           # require I / my / we in the premise
    "first_person_words": ["i", "i'm", "im", "my", "me", "we", "our",
                           "main", "mera", "meri", "mere", "mujhe", "maine", "hum", "humne"],  # add your language's
    "long_min": 50,                                 # <= this many chars = flagged (0.83x)
    "long_band": (55, 70),                          # the target band for a long title
}

DESKTOP, MOBILE, HARD = 60, 40, 100
EMOJI = re.compile(r"[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F]")
VAGUE = {"amazing","incredible","insane","crazy","huge","massive","ultimate","best","powerful",
         "secret","revolutionary","mindblowing","epic","perfect","complete","everything"}
STOP = {"the","a","an","of","for","to","in","on","and","or","is","are","with","your","you","my","i",
        "this","that","it","how","what","why"}

def words(t): return re.findall(r"[a-z0-9']+", t.lower())

def suffix_re(tpl):
    """'| {topic} Hindi' -> a regex anchored at the end, with the topic as a group."""
    if not tpl: return None
    pat = re.escape(tpl.strip()).replace(re.escape("{topic}"), r"(?P<topic>[^|()]+?)").replace(r"\ ", r"\s*")
    return re.compile(r"\s*" + pat + r"\s*$", re.I)

def check(title, thumb=None, short=False, cfg=CONFIG):
    t = title.strip()
    n = len(t)
    lo, band = cfg["long_min"], cfg["long_band"]
    issues, good = [], []
    sx = None if short else suffix_re(cfg["suffix"])
    m = sx.search(t) if sx else None
    p = t[:m.start()] if m else t                        # the premise: what a truncated title shows
    if n > HARD: issues.append(("length", f"{n} characters - YouTube's hard limit is {HARD}"))
    elif short and n > DESKTOP: issues.append(("length", f"{n} characters - desktop search cuts near {DESKTOP}"))
    elif short: good.append(f"{n} characters, inside the {DESKTOP}-character desktop cut")
    elif n <= lo: issues.append(("short", f"{n} characters - titles <= {lo} lose on small channels (0.83x); aim {band[0]}-{band[1]}"))
    elif n >= band[0]: good.append(f"{n} characters, in or past the {band[0]}-{band[1]} band")
    if not short:
        if sx and m: good.append(f"ends with the template suffix (topic: {m.group('topic').strip()})")
        elif sx: issues.append(("suffix", f"doesn't end '{cfg['suffix']}' ({cfg['suffix_why']})"))
        if cfg["first_person"]:
            if set(cfg["first_person_words"]) & set(words(p)): good.append("first-person premise (1.31x)")
            else: issues.append(("first-person", "no I / my / we in the premise (first-person premise, 1.31x)"))
    if len(p) > MOBILE:
        head = p[:MOBILE].rsplit(" ", 1)[0]
        issues.append(("mobile", f'a mobile feed shows about "{head}..." - check the subject survives'))
    caps = [w for w in t.split() if len(w) > 2 and w.isupper()]
    if short and len(caps) > 2: issues.append(("shouting", f"{len(caps)} all-caps words - two is the ceiling before it reads as spam"))
    elif short and caps: good.append(f"{len(caps)} all-caps word(s) for emphasis")      # long: 0.93x, neither
    if re.search(r"#\s?\d|\b(ep|episode|part)\.?\s?\d", t, re.I):
        issues.append(("episode", "an episode number - a recurring frame or Part 2 gets its own premise ('I Became a ___'), "
                                  "never '<Topic> #N' (premise frames beat numbered series)"))
    if EMOJI.search(t): issues.append(("emoji", "an emoji in the title (measured negative)"))
    if re.search(r"#[^\W\d]", t): issues.append(("hashtag", "a hashtag in the title (long 0.81x; Shorts: no #shorts, no stack)"))
    v = [w for w in words(t) if w in VAGUE]
    if v: issues.append(("vague", f"{', '.join(sorted(set(v)))} - swap for a number, a name or a date"))
    nums = re.findall(r"\d[\d,.]*%?", t)
    if nums: good.append(f"carries a concrete figure ({', '.join(nums[:3])}) - only if it's true")   # a bonus, never required
    if t.endswith("?"): good.append("open question in the title")
    front = [w for w in words(t)[:3] if w not in STOP]
    if not front: issues.append(("front-load", "the first three words are all filler - move the subject forward"))
    if thumb:
        tw, hw = set(words(p)) - STOP, set(words(thumb)) - STOP     # the suffix's topic may sit on the thumbnail
        shared = tw & hw
        if shared:
            issues.append(("duplicate", f"thumbnail repeats the title on {', '.join(sorted(shared))} - "
                                        "the thumbnail should say what the title does not"))
        else:
            good.append("thumbnail and title carry different words")
        if len(words(thumb)) > 4:
            issues.append(("thumb-length", f"{len(words(thumb))} words on the thumbnail - three is the ceiling at feed size"))
    score = max(0, min(100, 100 - 14 * len(issues) + 4 * len(good)))
    return {"title": t, "chars": n, "score": score, "issues": issues, "good": good}

def show(r):
    print(f'\n  "{r["title"]}"')
    print(f"  {r['chars']} chars   score {r['score']}/100")
    for k, m in r["issues"]: print(f"    x  {k:<12} {m}")
    for m in r["good"]:      print(f"    ok              {m}")

def _selftest():
    cfg = dict(CONFIG, suffix="| {topic} Hindi")
    ok = check("I Spent 3 Hours Trying to Escape ONE Room | Escape Lab Hindi", cfg=cfg)
    assert not [k for k, _ in ok["issues"] if k in ("suffix", "first-person", "short")], ok
    assert any("topic: Escape Lab" in g for g in ok["good"]), ok
    bad = check("I Spent 3 Hours Trying to Escape ONE Room in a Lab Game", cfg=cfg)
    assert "suffix" in [k for k, _ in bad["issues"]], bad
    assert "suffix" not in [k for k, _ in check("I Spent 3 Hours Trying to Escape ONE Room in a Lab Game")["issues"]]
    dup = check("I Became a Chef for One Whole Week in a Kitchen Sim", thumb="CHEF")
    assert "duplicate" in [k for k, _ in dup["issues"]], dup
    print("title selftest OK")

def main():
    a = sys.argv[1:]
    if a == ["--selftest"]: _selftest(); return
    as_json = "--json" in a; a = [x for x in a if x != "--json"]
    short = "--short" in a; a = [x for x in a if x != "--short"]
    thumb = a[a.index("--thumb") + 1] if "--thumb" in a else None
    if "--title" in a:
        t = a[a.index("--title") + 1] if a.index("--title") + 1 < len(a) else ""
        if not t.strip(): sys.exit("empty title - nothing to score")
        rows = [check(t, thumb, short)]
    elif a and os.path.exists(a[0]):
        rows = [check(l, thumb, short) for l in open(a[0], encoding="utf-8").read().splitlines() if l.strip()]
    else:
        print(__doc__); sys.exit(1)
    rows.sort(key=lambda r: -r["score"])
    if as_json: print(json.dumps(rows, indent=1)); return
    for r in rows: show(r)
    print()

if __name__ == "__main__":
    if sys.argv[1:2] in (["-h"], ["--help"]): print(__doc__); sys.exit(0)
    main()
