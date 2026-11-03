# Changelog

## Unreleased
- workflow: new `android-adb-drive` skill (beta, used for real on 2026-11-03) with `scripts/adb_drive.py`: taps only when the
  app owns the screen and no notification banner is down (two real mis-taps started a call and opened an SMS), saves and
  restores the settings it changes, lists the screen as tappable labels. Stdlib, selftest in CI.
- workflow: new `pre-report-secrets-scan` skill (draft, the owner's own) with `scripts/redact.py`, a stdlib first pass that
  reuses `secret_guard`'s key patterns, adds report-only shapes, never prints a value and rescans its own output. CI runs
  its selftest.
- music-studio and marketing-studio rebuilt to the arsenal's bar: all 10 skills rewritten as full workflows with gates,
  references and review rubrics, from 3 new research files (182 sourced, tagged claims: vocal tools 2026, production
  and video, release marketing). New tested tools: `lyric_lint.py`, `loudness.py` (with the phone-speaker vocal check),
  `beatmap.py` (beats, bars, sections, cuts on grid), `rollout.py` (release calendar), `copy_lint.py`; `templates/SONG.md`.
  Registry music section rewritten (38 rows, new Distribution section). CI now also runs skill_lint, the hook tests and
  the stdlib tool selftests, as CLAUDE.md already said it did.
- New `research` plugin (beta, from one real paper release): `paper-release` (Zenodo software and preprint DOIs,
  ORCID incl. DataCite auto-update, Google Scholar, LinkedIn, arXiv endorsement, under-18 consent and CS review-paper
  rule), `research-outreach` (researchers, venues, press, with follow-up rules) and `author-ownership` (building the
  author's own understanding and contribution when an AI agent did much of the work). workflow gotchas: a
  "Connectors" section on the Gmail connector rewriting draft links and how to fix and verify them.
- design: `tools/taste/motion.mjs`, a zero-dependency motion film. It plays a page on a virtual clock (timers, rAF, CSS and
  Web Animations driven together), photographs it at a fixed frame rate with keys or scripted moves on cue, and writes
  time-stamped contact sheets plus an old-TV view (`--tv`). Documented in tools.md and motion.md §14.
- design: rules proved on a TV launcher built with the skill: the cut-edge rule for cut-out characters (SKILL.md), web
  launchers on TV sticks, canvas particles on weak devices, impacts that reach small speakers, the user as the cause of
  the biggest moment (experience.md), per-keyframe easing for scheduled effects (motion.md), briefing sub-agents and
  valid review packs (process.md §8b), clean cut-outs from video (video.md §1.11b).
- creator: reference-study's yt-dlp download carries the EJS flags YouTube now needs. registry: rembg + BiRefNet, yt-dlp EJS.
- Merged the design, creator, video-edit, personal-edits, study and workflow plugins. design replaces design-studio
  (its brief, brand kit, sizes and HTML-to-PNG method folded into design references); workflow absorbs arsenal-core
  (`arsenal-update` skill, tool verdicts in `tool-change`). Versions dropped, `status:` on every skill; the validator also
  checks dashes, long descriptions and banned names in more file types; CI also runs skill_lint and the hook tests.
- Groundwork: marketplace manifest, four plugins (arsenal-core, music-studio, design-studio, marketing-studio) with draft
  skills, tool registry, research notes (vocals for non-singers, music tool landscape, design and marketing skills,
  patterns to reuse), skill template, structure validator and CI.
