---
name: vault-audit
description: Full integrity check of a study vault's tracking system - recompute every mistake tally and the marks average from source, verify every cross-subject claim against the subject log it cites, check code assignments, stale counts, duplicate sources of truth, broken links, filing and note structure, and fix what is wrong. Use for "audit the vault", "check everything", "is anything broken", "integrity check", after several sessions of hand edits, or after a new subject gets its first diagnosis.
---

# Vault audit

status: beta

**Verification, not narrative.** Report PASS or FAIL per check, fix what is broken, list the fixes, stop. Paths are under `<root>` (see `study-system`).

**Why it exists:** a manual trace of the source vault found a fabricated cross-subject claim that contradicted its own cited source (it had already spread to 6 files), a mistagged code that sat unseen for weeks, two duplicate sources of truth drifting apart, untouched pre-diagnosis checklists on two diagnosed subjects, and two tally miscounts. No process had caught any of them.

## 0. Automated checks first (run from the vault root)

```
PYTHONIOENCODING=utf-8 python "${CLAUDE_PLUGIN_ROOT}/scripts/linkcheck.py"    # broken links, orphans, skill frontmatter
PYTHONIOENCODING=utf-8 python "${CLAUDE_PLUGIN_ROOT}/scripts/vaultcheck.py"   # filing, book:, required blocks, undiagnosed scans, averages
PYTHONIOENCODING=utf-8 python "${CLAUDE_PLUGIN_ROOT}/scripts/tallycheck.py"   # checks 1 + 2 below, fully automated
PYTHONIOENCODING=utf-8 python "${CLAUDE_PLUGIN_ROOT}/scripts/note_audit.py"   # chapter coverage, blocks, index links, [unverified] flags
```

(Every script takes `--config` if study.json is not at the vault root.)

Record each tool's numbers as the vault's **baseline** in the vault's own CLAUDE.md or README (e.g. "linkcheck 0 broken / 0 orphans; tallycheck issues 0; note_audit N of N notes complete"). After that, any other number is a real finding; never explain one away as "the usual".

**A suspiciously clean number is itself a finding.** In the source vault `vaultcheck.py` once reported `scans: 0` after the papers folder was reorganised into subfolders: a flat listing had silently stopped seeing every paper. If a count drops to zero or a section goes quiet, check the tool before believing the vault.

## Checks, in order

1. **Subject tallies.** Count each code in every subject's Log table (a row coded `K + F` counts once for each) and diff against its Recurring Patterns table. The Log table is the source of truth. `tallycheck.py` does this; `issues: 0` = PASS, do not recount by hand.
2. **Master tally.** Sum each code across subjects and diff against `Error Log.md` Cross-Subject Tally. Also `tallycheck.py`.
3. **Average.** From `Marks/Marks Log.md` Current Standing, recompute `(a + b + ...) / n` with the sum written out. Marks Log and `Dashboard.md` must match each other and the recomputed value.
4. **Every cross-subject claim against its cited source.** For each `_Universal Rules.md` row and every "confirmed in N subjects" / "seen in X and Y" line in `Dashboard.md` and `Error Log.md`, open the cited subject file and confirm the evidence is really there: right code, right question, right conclusion. The slowest check and the highest-value one; it is the one that catches a fabrication before it spreads. Never skip it.
5. **Codes match their definitions.** Spot-check the last ~10 Log rows across subjects against `reference/taxonomy.md`. A code chosen because it "feels adjacent" is a mistag; fix it and note it.
6. **Stale counts and stale framing.** Grep for "N of N subjects", "N diagnosed", "average so far (N subjects)", "N papers", and for claims a later paper falsified. Fix every hand-written instance; a regenerated synthesis file self-corrects.
7. **One source of truth.** Taxonomy definitions live only in `reference/taxonomy.md`; cross-subject habits only in `How To Write/_Universal Rules.md`. A second copy anywhere collapses to a link.
8. **Links.** `linkcheck.py` only; never hand-grep links.
9. **Known Suspects.** Every diagnosed subject's "Known Suspects (pre-diagnosis)" list shows `[x]` / `[ ]` with reasons, not the blank template. Fill it from that paper's evidence.
10. **Filing and structure** (`vaultcheck.py`, `note_audit.py`): multi-book subjects in book subfolders, single-book subjects flat; `book:` on every chapter note; Memorize by Heart present; no retired blocks; every chapter on the syllabus has a note (chapters listed in `not_in_syllabus` are exempt by design); every note linked from the index.
11. **Undiagnosed scans.** Every PDF under `Backend/Papers/<Subject>/` has a matching post-mortem (recurse; a flat listing sees nothing). One without = run `paper-intake`.

## Output

One line per check: `<n>. <name>: PASS` or `<n>. <name>: FAIL: <what was wrong> -> fixed`. All clean: say so in one line; never manufacture findings. End with issues found, issues fixed, and anything flagged but not fixed, with the reason.
