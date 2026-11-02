# Adopting a repo: the capability matrix

Why: an earlier pass took "the parts that beat our pipeline" from a repo the user sent and left the rest. The user's bar
was different: anything that repo can do, we can do, built into our own system and better, for every use the project
has (main work and side projects alike), offered as an option.

## Fit test first: each repo gets ONE status
- `INTEGRATED`: the capability can show up in something the project makes (its main output, a side project, packaging,
  research) -> full build (steps below), AI and off-scope parts included, at a quality that does not read as AI.
- `IDEAS`: built for something the project never makes (websites, app UI, a dev workflow it does not use): only the
  ideas that help land, in a tool or doc a session already reads; nothing else is wired in.
- `SKIP`: nothing usable (wrong domain, a licence we can't use, or fully covered already); one line why.

## Steps
1. **Read the code, not the README.** List every capability (each command, effect, output) as numbered lines.
2. **Map each one** to OUR tool + flag that does it today, or mark it a gap. Its row goes in the project's matrix file
   (for example `docs/repo_capabilities.md`). A self-test check should fail on a sent repo with no row or an empty cell.
3. **Close every gap in our stack, ONE system:** an opt-in mode or key of an existing shared tool first, a new tool only
   when nothing fits; its manual entry + a test. Every default output stays unchanged. Never vendor the repo whole; call
   a GPL tool as a separate process. Third-party MIT code keeps its LICENSE file beside it.
4. **Test on a real sample:** main features on a real input, side-project features on the user's CURRENT side project.
   Numbers and the before/after go in the row.
5. A side-project capability also gets a line in that project's guide or skill capability menu. GPU-only steps go to the
   hand-off for the local machine.
6. Not in the project's domain at all (a trading bot, a reverse-engineering kit): one row saying so and what part, if
   any, helps.

## Matrix format (one row per repo; no empty cell)

| Repo | Status | What it does | Could we already | What we built | Tested on |
|---|---|---|---|---|---|
| owner/name @ commit | INTEGRATED | 1. ... 2. ... | 1. yes, tool --flag; 2. gap | 2. tool --new-mode (default unchanged) | real input, before/after numbers |
