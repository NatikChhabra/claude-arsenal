#!/usr/bin/env python3
"""rollout.py: a dated release calendar for a song or music video, from the release date back and forward, with every
platform deadline that has a source. Stdlib only.

    python rollout.py <YYYY-MM-DD> [--title "Song"] [--today YYYY-MM-DD] [--no-video] [--out marketing/<slug>/CALENDAR.md]
    python rollout.py --selftest

Deadlines (research/05_release_marketing.md; tags as there):
- Spotify editorial pitch: at least 7 days before release, one song at a time; Spotify's 2024 guide says two weeks
  (CONFIRMED). Delivery 7+ days ahead for first-week Release Radar (CONFIRMED). The calendar plans delivery at T-21 and
  the pitch at T-14, so a distributor delay still leaves the 7-day floor.
- TikTok "New Release" tag: from 14 days before to 30 days after release (CONFIRMED, Nov 2023).
- About 75% of first-year streams come after day 28 (Spotify fan study, CONFIRMED): the plan keeps posting to day 28+.
- Read-outs at day 1, 7 and 28 (research §8).
Prints FAIL lines for deadlines already missed relative to --today (default: the real date). Exit 1 if the hard floor (pitch and delivery live
7 days before release) is already missed; earlier dates are targets.
"""
import datetime as dt
import sys

STEPS = [  # (days from release, lane, task, hard deadline?)
    (-35, "music", "Master final, loudness.py PASS on WAV and encode; CREDITS.md complete (music-review gates)", False),
    (-30, "rights", "Release intent checked against every tool's plan and the distributor's AI policy; YouTube/Spotify disclosures decided", False),
    (-28, "design", "Cover art 3000x3000 final (design skill), artist identity is a real human or in-game/stylised art (no photoreal AI persona)", False),
    (-21, "distributor", "Deliver to the distributor (target); metadata, ISRC, language, AI-use answers, lyrics", False),
    (-14, "spotify", "Pitch in Spotify for Artists (Spotify's 2024 guide: two weeks); story, who/what/why/where, marketing plan", False),
    (-14, "tiktok", "New Release tag window opens (to day +30); first teaser with the official sound once it is live", False),
    (-10, "video", "Music video locked (music-video QC + music-review), 9:16 hook cuts rendered (3-4 different 15-30 s sections)", False),
    (-7, "spotify", "LAST day to pitch (hard floor: 7 days) and to have delivery live for first-week Release Radar", True),
    (-7, "social", "Teaser 1: the hook cut that ties to the RP story beat; announce the date", False),
    (-4, "social", "Teaser 2: a different hook cut (the riff or the guitar moment)", False),
    (-2, "rp", "In-city plan confirmed with server staff (event, in-game radio) if the rules allow; OOC links only where allowed", False),
    (-1, "social", "Teaser 3 + Spotify Canvas (3-8 s, 9:16, no song or artist name) uploaded", False),
    (0, "release", "Release day: music video premiere, posts per platform (each written for its app), Discord announcement", False),
    (1, "readout", "Day 1: real-time streams, YouTube 48 h views and CTR on Home/Suggested, first comments", False),
    (3, "social", "Short or Reel: the next hook cut; reply-style post to the best comment (owner OK for every reply)", False),
    (7, "readout", "Day 7: Release Radar listeners, saves/listeners, Shorts and TikTok creations; pick the winning hook cut", False),
    (10, "social", "Post the winning hook in a new edit; Trial Reel of a different section", False),
    (14, "social", "Behind the song: the guitar part, the RP story behind it", False),
    (21, "social", "Lyric or performance cut; RP follow-up scene if the story continues", False),
    (28, "readout", "Day 28: Release engagement %, save rate (saves / listeners), streams per listener, playlist adds, Subscribers from Shorts; compare with the last release; one change for the next", False),
    (30, "tiktok", "New Release tag window closes", False),
]


def calendar(release, today, title="", video=True):
    rows, misses = [], []
    for days, lane, task, hard in STEPS:
        if lane == "video" and not video:
            continue
        d = release + dt.timedelta(days=days)
        status = "done?" if d < today else ("TODAY" if d == today else "")
        if d < today and hard and days < 0:
            misses.append(f"FAIL {d.isoformat()} (T{days:+d}) missed: {task}")
        rows.append(f"| {d.isoformat()} | T{days:+d} | {lane} | {task} | {status} |")
    head = [f"# Release calendar{': ' + title if title else ''} (release {release.isoformat()})", "",
            "| Date | Day | Lane | Task | Status |", "|---|---|---|---|---|"]
    return "\n".join(head + rows) + "\n", misses


def selftest():
    rel = dt.date(2026, 12, 4)
    text, misses = calendar(rel, dt.date(2026, 11, 1), "Test")
    ok = "2026-11-27" in text and "LAST day to pitch" in text and not misses
    text2, misses2 = calendar(rel, dt.date(2026, 11, 29))
    ok &= any("LAST day to pitch" in m for m in misses2) and len(misses2) == 1
    ok &= "2027-01-01" in text and len(__import__("re").findall(r"\| T[+-]\d", text)) == len(STEPS)
    print("selftest", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main(argv):
    if "--selftest" in argv:
        return selftest()
    args = [a for a in argv if not a.startswith("--")]
    opt = lambda k, d=None: argv[argv.index(k) + 1] if k in argv else d
    for k in ("--title", "--today", "--out"):
        if k in argv:
            args.remove(argv[argv.index(k) + 1])
    if not args:
        print(__doc__)
        return 2
    release = dt.date.fromisoformat(args[0])
    today = dt.date.fromisoformat(opt("--today")) if opt("--today") else dt.date.today()
    text, misses = calendar(release, today, opt("--title", ""), video="--no-video" not in argv)
    if opt("--out"):
        open(opt("--out"), "w", encoding="utf-8").write(text)
    print(text)
    for m in misses:
        print(m)
    if misses:
        print("Missed hard deadlines: move the release date, or accept no editorial pitch / no first-week Release Radar.")
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
