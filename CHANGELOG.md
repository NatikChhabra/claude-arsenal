# Changelog

## Unreleased
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
