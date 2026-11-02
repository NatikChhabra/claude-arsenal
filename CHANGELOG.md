# Changelog

## Unreleased
- Merged the design, creator, video-edit, personal-edits, study and workflow plugins. design replaces design-studio
  (its brief, brand kit, sizes and HTML-to-PNG method folded into design references); workflow absorbs arsenal-core
  (`arsenal-update` skill, tool verdicts in `tool-change`). Versions dropped, `status:` on every skill; the validator also
  checks dashes, long descriptions and banned names in more file types; CI also runs skill_lint and the hook tests.
- Groundwork: marketplace manifest, four plugins (arsenal-core, music-studio, design-studio, marketing-studio) with draft
  skills, tool registry, research notes (vocals for non-singers, music tool landscape, design and marketing skills,
  patterns to reuse), skill template, structure validator and CI.
