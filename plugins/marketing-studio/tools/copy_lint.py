#!/usr/bin/env python3
"""copy_lint.py: lint promotional copy (captions, posts, pitches, descriptions, in-game adverts) before the owner sees
it. Stdlib only. The banned word list is the design plugin's one list (references/tells.md), read at run time.

    python copy_lint.py <file.md|file.txt> [--platform instagram|tiktok|youtube-title|youtube-desc|spotify-pitch|discord|ingame] [--json]
    python copy_lint.py --selftest

Input: one piece of copy per file, or several separated by a line with only `---`.
FAIL: an em or en dash; a banned word or banned shape ("not just X", "take your X to the next level", "you won't
      believe", "in today's fast-paced world" ...); over the platform's hard length (YouTube title 100 characters);
      follower-count bragging in a Spotify pitch (editors say it doesn't count, research/05 §6).
WARN: no concrete fact (no number, no proper noun, no date or place); more than 3 hashtags or 2 emoji; ALL-CAPS words
      beyond one; a Spotify pitch over 500 characters (practitioner limit, INFERRED); a YouTube title whose first 40
      characters lack the song or artist name the file gives with `name:`; "link in bio" with no reason to click.
Exit 0 clean (WARNs allowed), 1 on any FAIL.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TELLS = os.path.normpath(os.path.join(HERE, "..", "..", "design", "skills", "design", "references", "tells.md"))
FALLBACK = "unlock unleash supercharge seamless elevate empower revolutionize game-changer delve tapestry".split()
SHAPES = [r"\bnot just\b", r"\bmore than (just )?a\b", r"take your .* to the next level", r"you won'?t believe",
          r"in today'?s fast-paced", r"\bwhether you'?re\b", r"ready to get started", r"join thousands",
          r"say goodbye to", r"\bthe future of\b", r", reimagined\b", r"\bmade simple\b", r"\bdive in\b"]
DASH = re.compile("[" + chr(0x2013) + chr(0x2014) + "]")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
HARD = {"youtube-title": 100}
SOFT = {"spotify-pitch": 500}


def banned():
    try:
        block = open(TELLS, encoding="utf-8").read().split("Banned words", 1)[1].split("```", 2)[1]
        out = []
        for line in block.splitlines():
            if line.lower().startswith("in instructions"):
                continue
            out += [re.sub(r"\(.*?\)", "", w).strip().lower() for w in line.split(",") if w.strip()]
        return [w for w in out if w] or FALLBACK
    except (OSError, IndexError):
        return FALLBACK


def lint_piece(text, platform=None):
    fails, warns = [], []
    name = None
    m = re.search(r"^name:\s*(.+)$", text, re.M)
    if m:
        name = m.group(1).strip()
        text = re.sub(r"^name:.*\n?", "", text, flags=re.M)
    body = text.strip()
    low = " " + re.sub(r"[^a-z0-9' -]", " ", body.lower()) + " "
    if DASH.search(body):
        fails.append("em or en dash")
    for w in banned():
        if f" {w} " in low:
            fails.append(f"banned word '{w}'")
    for s in SHAPES:
        if re.search(s, body, re.I):
            fails.append(f"banned shape /{s}/")
    if platform in HARD and len(body) > HARD[platform]:
        fails.append(f"{len(body)} characters, {platform} max {HARD[platform]}")
    if platform in SOFT and len(body) > SOFT[platform]:
        warns.append(f"{len(body)} characters, aim under {SOFT[platform]} for {platform}")
    if platform == "spotify-pitch" and re.search(r"\b\d[\d,.]*\s*[km]?\s*(followers|subscribers|monthly listeners)\b", body, re.I):
        fails.append("follower or listener counts in a Spotify pitch (editors don't use them)")
    if not re.search(r"\d|\b[A-Z][a-z]+\b(?<!^)", body[1:] if body else ""):
        warns.append("no concrete fact (a number, a name, a place or a date)")
    if len(re.findall(r"#\w+", body)) > 3:
        warns.append(f"{len(re.findall(r'#\w+', body))} hashtags (keep 3 or fewer, specific ones)")
    if len(EMOJI.findall(body)) > 2:
        warns.append(f"{len(EMOJI.findall(body))} emoji")
    caps = [w for w in re.findall(r"\b[A-Z]{3,}\b", body) if w not in ("RP", "DJ", "MV", "OOC", "LUFS", "ISRC")]
    if len(caps) > 1:
        warns.append(f"ALL-CAPS words: {', '.join(caps[:5])}")
    if platform == "youtube-title" and name and name.lower() not in body[:40].lower():
        warns.append(f"'{name}' not in the first 40 characters (YouTube: key terms first)")
    if re.search(r"link in (my )?bio", body, re.I) and len(body) < 60:
        warns.append("'link in bio' with no reason to click")
    return fails, warns


def lint(text, platform=None):
    out = []
    for i, piece in enumerate(re.split(r"^---\s*$", text, flags=re.M), 1):
        if piece.strip():
            out.append((i, *lint_piece(piece, platform)))
    return out


def selftest():
    ok = True
    good = "Arjun's first single drops Friday 4 Dec. Recorded on a borrowed Yamaha in Mirror Park, guitar by me."
    ok &= lint(good, "instagram")[0][1] == []
    bad = "Unleash the vibe " + chr(0x2014) + " this is not just a song, it's a movement!!!"
    f = lint(bad, "instagram")[0][1]
    ok &= any("dash" in x for x in f) and any("unleash" in x for x in f) and any("not just" in x for x in f)
    ok &= any("characters" in x for x in lint("x" * 120, "youtube-title")[0][1])
    ok &= any("follower" in x for x in lint("We have 12k followers and a new song out 4 Dec in Vinewood.", "spotify-pitch")[0][1])
    ok &= any("concrete" in x for x in lint("such a vibe, so good, listen now", "tiktok")[0][2])
    ok &= len(lint("a 1\n---\nb 2\n")) == 2
    print("selftest", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    args = [a for a in argv if not a.startswith("--")]
    plat = argv[argv.index("--platform") + 1] if "--platform" in argv else None
    if plat:
        args.remove(plat)
    if not args:
        print(__doc__)
        return 2
    res = lint(open(args[0], encoding="utf-8").read(), plat)
    if "--json" in argv:
        print(json.dumps([{"piece": i, "fail": f, "warn": w} for i, f, w in res], indent=2))
    else:
        for i, f, w in res:
            for x in f:
                print(f"FAIL piece {i}: {x}")
            for x in w:
                print(f"WARN piece {i}: {x}")
        nf = sum(len(f) for _, f, _ in res)
        print(f"copy_lint: {len(res)} pieces, {nf} FAIL, {sum(len(w) for _, _, w in res)} WARN")
    return 1 if any(f for _, f, _ in res) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
