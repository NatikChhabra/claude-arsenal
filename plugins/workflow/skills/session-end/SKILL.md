---
name: session-end
description: Close a session or hand off before context runs out; finish the chunk, write the hand-off that replaces the last STATUS block, record every new preference verbatim, turn any new repeatable procedure into a skill, drift sweep if rules changed, test changed tools, pitch ideas, commit + push, one bullet message, close the thread. Use at the end of every task, when context_guard says the hand-off is due, or "wrap up", "hand off", "done for today".
---

# /session-end

status: beta

1. **Finish the chunk** you are on (never a rushed run or a skipped check). Long jobs run detached (working-rules U3):
   a main session may wait on one, else hand the job name to the next session. Never end a turn with a job silently
   running.
2. **Hand-off:** ONE STATUS block that REPLACES the last one (in the task's `BRIEF.md`, or the project's hand-off file):
   done (with numbers + file paths), open, the exact next command, blockers. Older blocks move to the `_archive.md` file.
3. **Nothing lost:** every new preference or decision of the user's from this session is in its file (their words
   verbatim + the time). The page they read for "next steps" is updated if the plan, schedule or scripts changed.
4. **Repeat check:** anything the user said more than once this session is now a hook, a script check or a skill step,
   with its row in CLAUDE.md "Repeat rules" (working-rules 14). A note alone does not count.
5. **Skills:** any procedure done this session that will recur and has no skill: write `.claude/skills/<name>/SKILL.md`
   now (frontmatter `name` + `description` with trigger phrases; steps from what was actually run; named in CLAUDE.md
   "Skills"). A skill that proved wrong or stale: fix it now.
6. **Drift sweep** if a rule file changed (skill `drift-sweep`; its skip check comes first).
7. **Tool changed?** Its tests PASS (skill `tool-change`).
8. **Clean up your own mess:** intermediates, scratch copies, worktree copies, temp folders this session made. Never a
   recursive delete through a junction or a protected path (the `secret_guard` hook blocks it).
9. **Ideas:** grounded pitches (data + evidence) when the session found any; a clear big win may start now.
10. `git pull`, commit (clear message), push. After the push, delete this task's own remote branch only when it has
    nothing ahead of main and the work is done.
11. **Message:** bullet points only, no summary paragraphs; lead with what the user must do, if anything. Nothing interim
    reaches them: an unfinished chunk is the hand-off, not a draft. Only the FINAL result goes out, tested and judged first.
12. **Close it:** work done means resolve this thread or stop this session now, unasked. A thread with nothing left for
    anyone is never left open or idle.
