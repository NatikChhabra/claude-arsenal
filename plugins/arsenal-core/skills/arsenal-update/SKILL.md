---
name: arsenal-update
description: Improve the Claude Arsenal after any session that used it or learned something (a better tool, a failed step, a rule the owner repeated). Use at the end of music, design or marketing work, or when asked to update the arsenal.
---
# Arsenal update

status: draft

Turns what a session learned into a lasting improvement, through a PR on `NatikChhabra/claude-arsenal`.

## Steps
1. List what this session learned: failed steps, missing steps, better tools, owner corrections, new repos he sent.
2. For each item pick the home:
   - owner repeated an instruction -> a skill step or a check in `scripts/validate.py`, plus a line in CLAUDE.md;
   - new tool, model, plugin or repo -> run `tool-intake`;
   - a job no skill covers -> new skill from `templates/SKILL_TEMPLATE.md` with `status: draft`;
   - a skill used successfully on real work -> promote `draft` -> `beta` (or `beta` -> `stable`) and say what it was used on.
3. List registry rows whose `recheck` date has passed (`python scripts/validate.py --due`) and refresh any the session can.
4. Bump the touched plugins' versions, add a CHANGELOG line, run `python scripts/validate.py`.
5. Branch, commit, PR. Never push to `main`. Never touch the owner's other repos.

## Guardrails
- Additive by default. Removing or rewriting a working step needs evidence in the PR description.
- One PR per session is fine; keep unrelated changes in separate commits.
