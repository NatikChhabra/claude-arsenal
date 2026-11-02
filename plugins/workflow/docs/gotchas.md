# Claude Code gotchas

Each one cost real time to establish. Most are Windows-specific.

## Plugins and hooks
- **A CLI update can break a working setup.** One release broke streaming (connection resets on every call);
  pinning the previous version (`npm i -g @anthropic-ai/claude-code@<last good>`) fixed it. Note the good version.
- **Hooks load only after a restart.** A new or changed plugin hook does nothing in the running session.
- **Prove a plugin loads, don't assume it:** a fresh headless run inside the workspace,
  `claude -p "reply PLUGIN=YES/NO" --model haiku`, then grep the answer line. Some plugins print a harmless
  "SessionEnd hook ... Hook cancelled" last line in `-p` mode.
- **Hook exit codes:** exit 2 blocks the tool and shows stderr to Claude; any other non-zero is a non-blocking error.
  A nudge hook swallows every error (a broken guard must never break a tool call); a blocking guard exits 2 only on
  the condition it checks, so a crash is a non-blocking error, never a false block.
- **A plugin with a runtime dependency is dead without it.** One memory plugin routed 6 of its 7 hooks through a runner
  that hard-exits when its JS runtime (bun) is absent. Check what a plugin's hooks call before trusting it.
- **LSP plugins are wrappers, not bundles.** They expect a global binary (`npm i -g pyright`,
  `npm i -g typescript-language-server`); without it on PATH they are inert.
- **Plugin roster costs context.** Every enabled plugin's skills sit in the prompt. Scope plugins per project in the
  project's `.claude/settings.json` (`enabledPlugins`) instead of enabling everything globally.
- **Measure a "token saver" before adopting it.** One proxy measured 2.8% savings, would have clobbered the
  `ANTHROPIC_BASE_URL` routing and dropped the 1M-context beta header (back to a 200k cap). It was removed.
- **Some plugins ship their own permission mode.** A notes-app integration ran with all tool confirmations skipped
  ("yolo") in its own settings file. Check a plugin's settings, not only Claude Code's.
- `ENABLE_PROMPT_CACHING_1H=1` (env) gives the main session a 1 h cache; helpers still get 5 min. A wait longer than
  the cache re-writes the whole context (see working-rules U3).

## Context and secrets
- **`.gitignore` does not protect the context window.** Read and Grep ignore it. `permissions.deny` in
  `.claude/settings.json` is the only layer that keeps noisy or private folders out (e.g. `Read(./archive/**)`).
- **A tracked settings folder can hold a token.** A notes-app git-sync plugin wrote its GitHub token in plain text into
  its tracked `data.json`, and it was pushed. Keep such folders git-ignored for good; keep tokens in the OS credential
  manager (`git config credential.helper wincred` / `manager`).
- **Never run a "compress" tool on CLAUDE.md on Windows:** a charmap encoding bug wiped the file.

## Windows shell
- **Tool names are PascalCase:** Read, Write, Edit, Glob, Grep, Bash, PowerShell. Lowercase returns "No such tool".
- **`python` may not be on PATH** (only the Store stub). Use `uv run --no-project python <script>`; set
  `WORKFLOW_PYTHON` for this plugin's hooks (README).
- **Hindi or other non-ASCII output crashes a Python print** on the default code page: set `PYTHONUTF8=1`.
- **PowerShell 5.1 `Set-Content -Encoding utf8` and `Out-File` write a BOM**, which some apps (Obsidian, JSON parsers)
  reject. Use `[IO.File]::WriteAllText($p, $text, (New-Object System.Text.UTF8Encoding $false))`.
- **Never `Remove-Item -Recurse` a junction:** PowerShell follows it and deletes the real folder. Use
  `cmd /c rmdir "<junction>"` (no /s). The `secret_guard` hook blocks recursive deletes on configured protected paths.
- **Every worktree shares one git stash stack.** Never a bare `git stash pop`: you may pop another session's work.
  Prefer a temporary WIP commit.

## Notes apps (Obsidian)
- **Obsidian has its own index scope**, separate from git and Claude. Exclude archives and tool folders with
  `userIgnoreFilters` in `.obsidian/app.json`. Obsidian skips dot-folders, so heavy tool folders go in `.name/`.
- `.obsidian/` changes are often untracked by design: back the file up before touching it.
