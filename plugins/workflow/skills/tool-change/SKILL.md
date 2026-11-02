---
name: tool-change
description: Change, fix or add a project tool, script, hook or gate safely; read its manual entry first, root-cause fixes once in shared code, a before/after where quality only goes up, a test for every new branch or rule, docs updated, code review for gated tools, no orphans, commit + push. Also adopts an outside repo at full capability through a capability matrix. Use for "fix the tool", "add a check", "new tool", "gate change", "hook change", "adopt this repo", "use this GitHub project".
---

# /tool-change <tool>

status: beta

## Rules
- **Downloads need no ask** (working-rules 9): fetch any useful tool, model or reference yourself from a trusted source,
  into its own empty folder; log name, source and size in the tools manual.
- **Quality only goes up** (working-rules 13): a change (usage savings included) only removes waste, never skips or
  weakens a gate, test, review pass or variant. It lands after a before/after on the same input: all tests PASS, every
  quality score it touches equal or higher; else revert. Numbers go in the hand-off.
- **Never weaken a gate to ship.** Extending an override or any bypass needs the user's words for that exact change.
- **Adopted = integrated flawlessly** (working-rules 16): called from the real pipeline or a skill step, documented,
  tested, no orphan, duplicate or misplaced file. Heavy tool folders go where the user's notes app and indexers skip
  them (dot-folders).
- Nothing that autostarts. Stop every GPU job afterwards.

## Steps
1. Read the tool's entry in the project's tools manual (often `tools/README.md`) + the part of the code you touch. Big
   files by window: grep, then Read offset/limit.
2. A bug: grep every caller first; fix the root cause once in the shared code, never per caller.
3. Make the change. A new branch or rule gets one test in the project's self-test (same style as its neighbours).
4. Update the manual entry. A new tool without an entry should fail the self-test (add that check if it is missing).
   A new skill must be named in CLAUDE.md "Skills". A new or changed skill passes this plugin's
   `python scripts/skill_lint.py <skills dir>` with 0 FAIL (frontmatter, links, dashes, supply-chain tells). A skill
   that enforces a discipline is also tested the way it will be dodged: one fresh helper runs the task without the
   skill and one with it, under real pressure (a deadline, a near-done state); keep the skill only if the second run
   holds where the first slipped, and quote the slip in the hand-off.
5. Run the self-test (detached when it is long; working-rules U3). Don't edit tracked files while it runs if it checks
   git status. Environment-only SKIPs are named in the manual.
6. A gated tool (anything that refuses a release, an upload, a commit): `/code-review low` before the push.
7. A changed rule: skill `drift-sweep`. A hook change: prove it with a fake JSON on stdin and a fresh headless session
   (working-rules 7). Then pull, commit, push.

## Verdict for an outside tool, plugin, MCP server or model
1. Pin it: URL, version or commit, licence, maintainer, last release, platforms (Windows, AMD GPU, CPU).
2. Deal-breakers, any one ends it: the licence forbids public or commercial use; CUDA-only with no ROCm, DirectML or
   CPU path; it sends private files to a service without the user's OK; archived with no maintained fork; it installs
   outside the folder the project reserves for it.
3. Verdict: `ADOPT` (tested on a real task, wired into a skill), `TRIAL` (an option in a skill, waiting on a real test),
   `WATCH` (not ready; a recheck date), `SKIP` (the reason, so nobody researches it again).
4. Record one row where the project keeps them (in the arsenal: `registry/tools.md` or `registry/local-models.md`,
   columns `name | what it does for us | licence | runs on | verdict | recheck | source`), and wire ADOPT or TRIAL into
   the matching skill with the exact install command.

## A repo the user sends
The bar is FULL CAPABILITY: everything the repo can make, we can make, inside our tools and better. Never a bare copy
or cherry-picks; one combined system where every new capability is an opt-in option of the shared tools and the default
output is unchanged. The procedure and the matrix format: [references/repo-capabilities.md](references/repo-capabilities.md).
