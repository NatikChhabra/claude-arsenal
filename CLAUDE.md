# Claude Arsenal: rules for every session

This repo is the owner's growing toolkit. Read this file before changing anything.

## Who it is for
- Owner: Natik (GitHub `NatikChhabra`). Plays guitar. Loves singing but can't sing well, so every music
  workflow must offer a vocal route that does not depend on his own sung pitch (see `research/01_vocals_for_non_singers.md`).
- Main use right now: **NewDay RP** (NDRP, a GTA V roleplay server). Music, music videos, design and marketing for his
  characters and in-world businesses. Music and music videos come first; design and marketing second.
- He runs many side projects through Claude. Each one should be able to install these plugins and improve them.

## Standing instructions (owner, 2 Nov 2026)
- "Keep updating my Claude arsenal ... so it can improve." Every session that uses a skill and learns something
  (a better tool, a failure, a missing step) updates the arsenal in the same session, through a PR. See `GROWTH.md`.
- "Don't fuck up previous work." Changes are additive. A skill rewrite keeps every working step unless a test or a
  real result shows the new way is better, and the PR says so.
- `NatikChhabra/sirf-timepass` is reference only: read it to learn patterns, never push, comment or open PRs there.
  Its ideas worth reusing are listed in `research/00_sirf_timepass_lessons.md`.

## How work lands
1. Branch from `main` (`<area>/<short-name>`), never commit to `main` directly.
2. Run `python scripts/validate.py` before pushing. CI runs it too.
3. Open a PR. Note in `CHANGELOG.md` under "Unreleased".
4. Bump the plugin `version` in its `plugin.json` when its skills change (semver: patch = wording, minor = new skill/step,
   major = a changed workflow).

## Quality bar
- **No AI slop.** Lyrics, captions, posters and copy must sound like a person wrote them for this exact purpose. No stock
  phrasing ("unleash", "elevate", "dive in"), no em dashes in shipped copy, no generic AI-looking art. AI generation is
  allowed and encouraged when a stranger could not tell (blind check).
- **Self-review before showing.** Each studio plugin has a review checklist; run it and iterate before delivering.
- **Rights.** Only clone or convert voices you own or have written permission for. Check each generator's licence for
  commercial or public use before a release. Check NDRP's server rules for in-game music and advertising.

## Hardware and local models (owner's PC, from sirf-timepass research/82)
- RX 7800 XT 16 GB (AMD, ROCm 7.2 via ComfyUI works), Ryzen 5 7600X, 32 GB RAM, Windows.
- Models live under `F:\AI Models\`. Arsenal models go in `F:\AI Models\arsenal\` only. Never move, delete or edit
  `F:\AI Models\coding\` or `F:\AI Models\sirf-timepass\` (other projects use them).
- Keep the GPU free when idle. Nothing autostarts.

## Layout
`plugins/<name>/.claude-plugin/plugin.json` + `plugins/<name>/skills/<skill>/SKILL.md`.
The marketplace index is `.claude-plugin/marketplace.json`. Skills carry a `status:` line in their body
(`draft` -> `beta` -> `stable`) so a session knows how much to trust them.
