# Claude Arsenal: rules for every session

This repo is the owner's growing toolkit. Read this file before changing anything.

## Who it is for
- Owner: GitHub `NatikChhabra`. Plays guitar. Loves singing but can't sing well, so every music
  workflow must offer a vocal route that does not depend on his own sung pitch (see `research/01_vocals_for_non_singers.md`).
- Uses: **GTA V roleplay (RP)** music, music videos, design and marketing for his characters and in-world businesses;
  a YouTube channel (creator, video-edit); personal edits; exam study; and the design and workflow rules every project shares.
- He runs many side projects through Claude. Each one should be able to install these plugins and improve them.

## Standing instructions (owner, 2 Nov 2026)
- "Keep updating my Claude arsenal ... so it can improve." Every session that uses a skill and learns something
  (a better tool, a failure, a missing step) updates the arsenal in the same session, through a PR. See `GROWTH.md`.
- "Don't fuck up previous work." Changes are additive. A skill rewrite keeps every working step unless a test or a
  real result shows the new way is better, and the PR says so.
- The owner's other repos are reference only: read them to learn patterns, never push, comment or open PRs there,
  and never name them in this repo. Patterns worth reusing are listed in `research/00_patterns_to_reuse.md`.

## How work lands
1. Branch from `main` (`<area>/<short-name>`), never commit to `main` directly.
2. Run `python scripts/validate.py`, `python plugins/workflow/scripts/skill_lint.py plugins` and
   `python plugins/workflow/hooks/test_hooks.py` before pushing. CI runs all three.
3. Open a PR. Note in `CHANGELOG.md` under "Unreleased".
4. No `version` fields in `plugin.json` or `marketplace.json`: the commit SHA versions installs, so every merged change
   reaches every project on its next update (the validator refuses a version).

## Quality bar
- **No AI slop.** Lyrics, captions, posters and copy must sound like a person wrote them for this exact purpose. No stock
  phrasing ("unleash", "elevate", "dive in"), no em dashes in shipped copy, no generic AI-looking art. AI generation is
  allowed and encouraged when a stranger could not tell (blind check).
- **Self-review before showing.** Each studio plugin has a review checklist; run it and iterate before delivering.
- **Rights.** Only clone or convert voices you own or have written permission for. Check each generator's licence for
  commercial or public use before a release. Check the RP server's rules for in-game music and advertising.

## Hardware and local models (owner's PC, measured Oct 2026)
- RX 7800 XT 16 GB (AMD, ROCm 7.2 via ComfyUI works), Ryzen 5 7600X, 32 GB RAM, Windows.
- Models live under one models root on the owner's PC (`<models-root>`). Arsenal models go in `<models-root>\arsenal\`
  only. Never move, delete or edit any other folder under it (other projects use them).
- Keep the GPU free when idle. Nothing autostarts.

## Layout
`plugins/<name>/.claude-plugin/plugin.json` + `plugins/<name>/skills/<skill>/SKILL.md` (+ `references/*.md` for detail,
`scripts/` or `tools/` for code, `hooks/` for hooks). Visual, motion and sound rules live only in the `design` plugin;
other plugins point to it. One skill per job: before adding a plugin or skill, check the README index for an overlap
and merge into the better one (UPGRADES.md "Merges").
The marketplace index is `.claude-plugin/marketplace.json`. Skills carry a `status:` line in their body
(`draft` -> `beta` -> `stable`) so a session knows how much to trust them.
