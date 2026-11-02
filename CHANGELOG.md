# Changelog

## Unreleased
- music-studio and marketing-studio rebuilt to the arsenal's bar: all 10 skills rewritten as full workflows with gates,
  references and review rubrics, from 3 new research files (182 sourced, tagged claims: vocal tools 2026, production
  and video, release marketing). New tested tools: `lyric_lint.py`, `loudness.py` (with the phone-speaker vocal check),
  `beatmap.py` (beats, bars, sections, cuts on grid), `rollout.py` (release calendar), `copy_lint.py`; `templates/SONG.md`.
  Registry music section rewritten (38 rows, new Distribution section). CI now also runs skill_lint, the hook tests and
  the stdlib tool selftests, as CLAUDE.md already said it did.
- Merged the design, creator, video-edit, personal-edits, study and workflow plugins. design replaces design-studio
  (its brief, brand kit, sizes and HTML-to-PNG method folded into design references); workflow absorbs arsenal-core
  (`arsenal-update` skill, tool verdicts in `tool-change`). Versions dropped, `status:` on every skill; the validator also
  checks dashes, long descriptions and banned names in more file types; CI also runs skill_lint and the hook tests.
- Groundwork: marketplace manifest, four plugins (arsenal-core, music-studio, design-studio, marketing-studio) with draft
  skills, tool registry, research notes (vocals for non-singers, music tool landscape, design and marketing skills,
  patterns to reuse), skill template, structure validator and CI.
