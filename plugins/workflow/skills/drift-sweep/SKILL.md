---
name: drift-sweep
description: Find where the project's rule files contradict each other after a rule changed; one read-only helper audits CLAUDE.md against every skill, scoring doc and dashboard page, then the session fixes every HIGH and MEDIUM (the newer dated rule or the enforcing gate wins) and commits with "drift sweep" as the next baseline. Use before ending any session that changed a rule file, after a retro, or for "drift sweep", "are the rules consistent", "stale skills".
---

# /drift-sweep

status: beta

Why: a new rule lands in CLAUDE.md, but its older copies in skills, scoring docs and the user's dashboard pages stay as
they were. The first sweep on a real project found 25 real conflicts, 2 HIGH (a skill still doing a step the user had
retired the day before; a style guide still holding superseded settings). Tests can't see these: they are meaning, not
wiring.

## When
Any session that changed one of the rule files runs it before it ends (working-rules 17). Skip it when nothing changed
since the last sweep:
`git log -1 --grep="drift sweep" --format=%h` -> `git diff --stat <that>..HEAD -- <the rule files>` (empty = skip).
Cost: one helper, ~200k tokens (measured), so once per change set, never per session.

## The rule files
Listed in `.claude/workflow.json` key `"drift_files"` (paths or globs), else this default:
`CLAUDE.md`, the hand-off file, any scoring doc (`QUALITY.md`), the user's dashboard pages, every
`.claude/skills/*/SKILL.md` that restates a project rule. Generic skills that restate no project rule are left out on
purpose: sweeping them is waste. The project's self-test should check that each listed file exists.

## How
1. Start ONE helper (Agent tool, general-purpose) with the brief below, plus the repo path and an output file in the
   scratchpad.
2. Fix every HIGH and MEDIUM in this session. The authoritative side wins: the newer dated rule of the user's, or what
   a gate in the tools enforces. LOW when cheap.
3. Commit with "drift sweep" in the message (that marks the baseline for the next skip check).

## The brief (paste it)
Read-only consistency audit. Do not edit any repo file. CLAUDE.md is the constitution: the user's rules, each usually
dated; a later dated rule overrides an earlier one, and what a gate in the tools enforces is the live behaviour. Read
the listed files whole, once. Find places where they CONTRADICT each other, or where a skill, scoring doc or dashboard
page still instructs something CLAUDE.md has since changed or retired, or where two copies of one rule disagree in a
number, date or threshold. Only real, concrete conflicts you can quote from both sides: no style nits, no "could be
clearer", no speculation. Per finding: severity (HIGH = a session following the stale text does the wrong thing on the
next run; MEDIUM = confusing or duplicated, a gate would catch it; LOW = cosmetic), file:line + short quote of the stale
side, file:line + short quote of the authoritative side, the one-line fix. Write the table to the output file; answer
with the count by severity and each HIGH in one line. Nothing found is a valid result.
