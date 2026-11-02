# Changelog

## Unreleased
- New `research` plugin (beta, from one real paper release): `paper-release` (Zenodo software and preprint DOIs,
  ORCID incl. DataCite auto-update, Google Scholar, LinkedIn, arXiv endorsement, under-18 consent and CS review-paper
  rule), `research-outreach` (researchers, venues, press, with follow-up rules) and `author-ownership` (building the
  author's own understanding and contribution when an AI agent did much of the work). workflow gotchas: a
  "Connectors" section on the Gmail connector rewriting draft links and how to fix and verify them.
- Merged the design, creator, video-edit, personal-edits, study and workflow plugins. design replaces design-studio
  (its brief, brand kit, sizes and HTML-to-PNG method folded into design references); workflow absorbs arsenal-core
  (`arsenal-update` skill, tool verdicts in `tool-change`). Versions dropped, `status:` on every skill; the validator also
  checks dashes, long descriptions and banned names in more file types; CI also runs skill_lint and the hook tests.
- Groundwork: marketplace manifest, four plugins (arsenal-core, music-studio, design-studio, marketing-studio) with draft
  skills, tool registry, research notes (vocals for non-singers, music tool landscape, design and marketing skills,
  patterns to reuse), skill template, structure validator and CI.
