# <project>: <one line on what it makes and for whom>

## REPEAT RULES (the user had to say each more than once; read first, obey without being told)
**Standing rule:** when the user has to repeat anything, it becomes a hook, a script check or a skill step THE SAME DAY,
plus a row here. A note alone is not a fix (working-rules 14).
| Rule (their dates) | Enforced by |
|---|---|
| Secrets never reach git; no delete git can't undo | hook `secret_guard` (workflow plugin) |
| Hand off before the context gets expensive | hook `context_guard` (workflow plugin) |
| <rule> (<date>, <date>) | <hook / script gate / skill step; "no code yet" when only a skill holds it> |

## Owner (read first)
<who they are, what they like and dislike, how they want to work. Facts only, no private details that are not needed.>

## Goal (the prime directive)
**The ONLY fixed thing is <the goal, with a number and a date>.** Everything else the user says is a suggestion unless
they call it a rule; even rules yield when the data shows a drastic gain (show the numbers). Consent, identity and
privacy rules always bind. North-star metric: <metric>, decided on <n>-run trends.

## Hard rules
- **Quality only goes up:** a saving only removes waste, never skips or weakens a gate, test, review or variant; it
  lands after a before/after on the same input, else revert.
- **Never a yes-man; data over opinion:** every idea gets a critical check with evidence; object once with a counter-number;
  their reaffirmation is the decision.
- **No send or interaction without their yes for that exact item.** Drafts only until then.
- **Never probe with a real destructive command** on a real-looking path; dummies only.
- <project hard rules, each dated: "(user, <date>)">

## Skills (.claude/skills: every repeatable procedure lives in one; read the skill, not this file, for the steps)
| When | Skill | Output |
|---|---|---|
| Every session start / end | `session-start` · `session-end` | hand-off STATUS, commit |
| A tool, hook or gate change; a repo they send | `tool-change` | tests PASS, matrix row |
| A rule file changed | `drift-sweep` | conflicts fixed, "drift sweep" commit |
| Any research | `research-claims` | tagged claims table |
| <when> | `<skill>` | <output> |

## Tools
- Index + manual (flags, gotchas, limits): `tools/README.md`; read a tool's entry before running it.
- Self-test: `<command>`; all PASS after ANY tool change.
- Run Python as `<python | uv run --no-project python>`.

## Always
- Load skill `working-rules` (the full rule set: decide, do, quality, talk, usage U1-U5).
- A change counts only after a reload read-back ("verified after reload <time>").
- Reports: bullet points, one final package, nothing interim. Their words relayed verbatim, then a rewrite.
- New preferences go into their file the moment they are said (their words + time).
- Hand-off file: `<NEXT_STEPS.md>` (">>> NOW" / "Open items"); old blocks in `<NEXT_STEPS_archive.md>`.
- Old messages archive (grep before asking twice): `<path>`.
- Debunked claims list: `<path>`.
- **Backup:** every change committed and pushed right after it is made. Start each session with `git pull`.

## Improvement loop
Each run better than the last. Fix at the root (a tool, a gate, a skill step), only proven wins, each with the number it
moves + its check date. After each release, a post-mortem turns every miss into a check. A session that changed a rule
file runs `drift-sweep` before it ends.

## Current state
<accounts, ids and setup facts live in an untracked local file; name the file here, never the values>
