# creator

Skills for running a YouTube channel (long videos, Shorts, Instagram Reels) as a system: pick, plan, package, review,
release, learn. Generalised from a working channel's pipeline: the methods, gates and numbers stay, the channel is gone.
Each skill runs a project's own tool when it has one and says how to do the step by hand when it doesn't. Visual
craft lives in the design plugin (skill design, references/video.md).

## The pipeline
- `topic-pick`: 3-5 concept + format + topic pitches backed by small-creator data and a demand slot, Claude's pick marked.
- `beatsheet`: a story script + a blind-tested, source-tagged bit pack for an unscripted creator; never a read-off script.
- `reference-study`: measure and watch a reference video whole, list its devices, write rules that change a tool or step.
- `shorts`: Shorts and Reels as two products, each a zero-context hook/turn/payoff story that sells the long.
- `thumbnail`: 3 drastically different cards from a named click incentive, measured feed gates, blind readers, a click floor.
- `publish-meta`: titles on the channel template, 3 title/thumbnail pairs, description, chapters, tags, the upload sheet.
- `growth-funnel`: what each app scores, the bars, how every piece hands the viewer to the next, the live-channel audit.
- `growth-gate`: the package score sheet, one row per funnel lever, ship at 8.5+.
- `final-review`: QC, 3 fresh blind reviewers with an AI-feel gate, a computed ship score, one final package message.
- `release`: Studio and Business Suite through the browser, long first, related videos, verify after reload, post-mortem.
- `retro`: day 1/3/7 numbers and notes, root-cause fixes, gate recalibration.
- `weekly-review`: stats against the bars and the channel median, fast follow-ups, Part 2 calls, one change a week.
- `inbox`: brand email triage, draft-only replies.
- `drop-topic`: remove a dropped topic completely in one pass, leave a veto line.

## Third-party yt-* skills (MIT, see `LICENSE-yt-skills-MIT.txt` and `NOTICE.md`)
- `yt-audit`: a channel audit that ends in ONE fix.
- `yt-chapters`: chapters from a transcript, validated against YouTube's rules (`chapters.py`).
- `yt-comment`: triage comments and draft replies; nothing posted without the creator's OK.
- `yt-edit`: dead air, filler and restarts from a transcript as an edit list (`deadair.py`).
- `yt-package`: title + thumbnail text linted as one pairing; the channel template is the `CONFIG` dict in `title.py`.
- `yt-plan`: a week or month of uploads sized to real capacity.
- `yt-retention`: hook leak, cliffs and slide from a Studio retention export (`retention.py`).
- `yt-script`: hook scoring and 21 hook formulas (`hookscore.py`, `hooks.json`).
- `yt-seo`: description, tags and the query test.
- `yt-viral`: niche outliers ranked by multiple over each channel's own median (`swipe.py`).

## Scripts
Python 3, stdlib only. Self-checks: `python skills/final-review/ship_score.py --selftest`,
`python skills/yt-package/title.py --selftest`.

## Install
```
/plugin install creator --marketplace NatikChhabra/claude-arsenal
```
Or `/plugin marketplace add NatikChhabra/claude-arsenal`, then `/plugin install creator@claude-arsenal`. More options: the [marketplace README](../../README.md).
