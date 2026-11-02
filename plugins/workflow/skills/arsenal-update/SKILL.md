---
name: arsenal-update
description: Feed what a session learned back into the claude-arsenal marketplace so every project gets it, as an additive change that passes the arsenal's checks. Use at the end of any session that used an arsenal skill and hit a failed step, a missing step, a better tool or a correction the user repeated, or for "update the arsenal", "improve my plugins", "add this to my toolkit".
---
# /arsenal-update

status: beta

Projects install these plugins; this skill is how they improve them. Work in a clone of `NatikChhabra/claude-arsenal`,
never in the plugin cache.

## Steps
1. List what the session learned: failed steps, missing steps, better tools, the user's corrections (verbatim), repos he sent.
2. Give each one a home:
   - a correction he repeated: a skill step or a check in `scripts/validate.py`, the same day (working-rules);
   - a tool, model, plugin or repo: skill tool-change, "Verdict" (a registry row) or "A repo the user sends";
   - a job no skill covers: a new skill from `templates/SKILL_TEMPLATE.md`, `status: draft`;
   - a skill that just did real work well: promote `draft` to `beta`, or `beta` to `stable`, and name the work.
3. Keep it general: no project names, people, handles, paths or stats from the project that taught it (the validator's
   banned-name check refuses known ones). Visual, motion and sound rules go only in the `design` plugin.
4. Additive by default: a rewrite keeps every working step unless a test or a real result shows the new way is better.
5. `python scripts/validate.py --due` (structure, banned names, dashes, registry rechecks due) and
   `python plugins/workflow/scripts/skill_lint.py plugins`: 0 errors, 0 FAIL. Refresh any due row the session can.
6. A line in `CHANGELOG.md` under "Unreleased". Branch, commit, push, open a PR (see the repo's CLAUDE.md "How work lands").
   No version bumps: plugins carry no version, so every merged commit reaches installs on the next update.
