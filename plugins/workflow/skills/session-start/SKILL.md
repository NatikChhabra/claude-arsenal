---
name: session-start
description: Start any session cheaply and correctly; check the expected plugins loaded, git pull, read only the hand-off (the last STATUS block or the task's brief) and the files it names, clear what is DUE first, decide where the work must run, pick the skill. Use at the start of every session or thread, or for "where were we", "pick up", "continue", "resume".
---

# /session-start

status: beta

1. **Plugins loaded?** Every plugin the project's CLAUDE.md names as always-on printed its banner or lists its skills.
   If not, say so before any other work (a hook only loads after a Claude Code restart).
2. `git pull` (other machines and cloud threads push to the same branch).
3. **Read narrowly (working-rules U2):** CLAUDE.md (auto) + the hand-off: the project's hand-off file (named in
   CLAUDE.md, often `NEXT_STEPS.md` ">>> NOW" / "Open items"), or the task's `BRIEF.md` last STATUS block, and only
   the files it names. Never an archive file whole: grep it.
   Before asking the user anything, grep the archive of their old messages; never make them repeat.
4. **Where it runs:** work that needs local files, the GPU, secrets, a signed-in browser = the local machine. Research,
   writing, planning, analysis, tool code = a cloud thread is fine. Wrong place: route it, don't half-do it.
5. **Due first, before the task.** If the project has a SessionStart hook that prints a DUE list (the pattern: rules
   kept only by a skill step slip, so a hook lists what is owed), clear every line before the task: each line names
   the skill or command that clears it. Re-run it by hand if it didn't show. On a cloud clone, run its offline mode.
6. **Pick the skill** for the task (CLAUDE.md "Skills"). No skill fits a repeatable procedure: write one as part of
   the task (working-rules 15).
7. **Effort:** high on anything that touches the content; medium on bookkeeping.
8. **Rules:** load skill `working-rules` if it is not already in context.

End with skill `session-end`.
