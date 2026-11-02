# How the arsenal grows

The goal: a toolkit that gets better every time it is used, until it is the best setup anyone has for these jobs.

## The loop (every session that touches music, design or marketing)
1. **Use** the matching skill. If none fits, note the gap.
2. **Notice**: a step that failed, a tool that did better, a rule the owner had to repeat, a missing skill.
3. **Record** it the same session:
   - a repeated instruction from the owner becomes a skill step or a check, not just a note;
   - a new tool, plugin, MCP server or model goes through `tool-intake` (registry row + verdict);
   - a gap becomes a `draft` skill from `templates/SKILL_TEMPLATE.md`.
4. **Ship** it through a PR (see CLAUDE.md "How work lands").

## Verdicts (registry)
| Verdict | Meaning |
|---|---|
| `ADOPT` | Tested on a real task, wired into a skill |
| `TRIAL` | Promising; a skill mentions it as an option, waiting on a real test |
| `WATCH` | Not ready (too young, wrong licence, no AMD support); re-check date in the row |
| `SKIP` | Looked at, not useful; reason recorded so nobody re-researches it |

## Skill maturity
`draft` (outline, untested) -> `beta` (used on at least one real piece of work) -> `stable` (used several times, review
checklist passes without fixes). Promote in the same PR that records the real use.

## A repo or tool the owner sends
Treat it like sirf-timepass treats one: learn everything it does, map each capability to an arsenal skill or tool
(adopt, rebuild better, or skip with a reason), never a bare copy. Record it in `registry/tools.md`.

## Re-check cadence
Fast-moving areas (AI music, voice conversion, video generation) get a research refresh about once a month; the
`arsenal-update` skill lists rows whose re-check date has passed.
