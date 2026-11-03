# workflow

How the creator wants Claude to work, packaged so any project can switch it on: the working rules as skills, two
hooks that enforce the rules that kept slipping, a CLAUDE.md template, and a small kit for offloading bulk drafting to
a local LLM. Every rule here came from a real miss on a real project; most were said more than once before they became
code.

## What's inside

| Path | What it does |
|---|---|
| `skills/working-rules/` | The standing rules: decide with data, never a yes-man, do it yourself with one batched ask, proof after reload, quality only goes up, repeat corrections become code the same day, bullet reports, usage U1-U5. Full set with why + how: `references/rules.md` |
| `skills/session-start/` | Cheap correct start: plugins loaded, `git pull`, read only the hand-off, clear DUE items, pick the skill |
| `skills/session-end/` | Hand-off that replaces the last STATUS, preferences written verbatim, new skills, drift sweep, commit + push, one bullet message, close the thread |
| `skills/tool-change/` | Safe tool, hook or gate changes; a verdict (ADOPT, TRIAL, WATCH, SKIP) for an outside tool; adopting a repo at full capability via a capability matrix (`references/repo-capabilities.md`) |
| `skills/arsenal-update/` | Feeds what a session learned back into this marketplace: the home for each lesson, privacy, the checks, a PR |
| `skills/pre-report-secrets-scan/` | Before a log, stack trace, env dump or bug report is pasted, posted or emailed: a redacted copy, a findings list that never shows a value, UNSURE flags for the user, a rotate reminder |
| `skills/drift-sweep/` | One read-only helper finds contradictions between rule files after a rule changed (the first sweep found 25, 2 HIGH) |
| `skills/research-claims/` | CONFIRMED / INFERRED / DEBUNKED on every claim, read the whole source, say when a claim is true |
| `hooks/secret_guard.py` | PreToolUse on Bash/PowerShell: blocks git add/commit/push carrying secret files, token-shaped strings or private names; blocks `git clean -x`, recursive deletes through protected paths, git commands that throw away uncommitted or pushed work (`reset --hard`, `checkout --`, `restore`, `clean -f`, `stash clear`, `branch -D`, `push --force` without a lease) and a download piped into a shell |
| `hooks/context_guard.py` | PostToolUse: tells the session to hand off at +140k past its work start (helpers +120k), due at +200k; notes cache-expiry rewrites, helper fan-out over 4, helpers past 20 images. Never blocks |
| `hooks/test_hooks.py` | Feeds both hooks fake JSON on stdin (48 checks) |
| `templates/CLAUDE.template.md` | A project CLAUDE.md skeleton: repeat-rules table, the one goal, hard rules, skills table, always, improvement loop |
| `templates/workflow.example.json` | Example per-project config for the hooks and the drift sweep |
| `scripts/redact.py` | The scan behind pre-report-secrets-scan: secret_guard's key patterns plus report-only shapes (JWT, auth headers, URL passwords, webhooks, private IPs, internal hosts, emails, home-path usernames, high-entropy look-alikes); same value = same placeholder everywhere; rescans its own output. Stdlib, `--check`, `--selftest` |
| `scripts/skill_lint.py` | Lints every SKILL.md under a folder: frontmatter (`name` = folder, kebab-case, description under 1024 chars with triggers), missing linked files, unlinked references, em/en dashes, size, placeholders, supply-chain and prompt-injection tells. Stdlib, `--selftest` |
| `scripts/` (offload) | Local-LLM offload kit: `llm.ps1` (start llama.cpp), `ask.py` (one prompt), `batch.py` (a template over a JSON list, resumable) |
| `docs/gotchas.md` | Claude Code and Windows gotchas that cost real time |

## Install

```
/plugin install workflow --marketplace NatikChhabra/claude-arsenal
```
Or enable it per project in `.claude/settings.json` (`"enabledPlugins": {"workflow@claude-arsenal": true}`, setup in the
[marketplace README](../../README.md)). Restart Claude Code: hooks load only at start.
Copy `templates/CLAUDE.template.md` to the project's `CLAUDE.md` and fill the placeholders.

### Python for the hooks: `uv run` or plain `python`
The hooks are stdlib-only Python 3.8+ (the self-test needs 3.10+). `hooks.json` runs them with
`${WORKFLOW_PYTHON:-uv run --no-project python}`:
- **uv installed:** nothing to do.
- **No uv:** set the interpreter in the project's or user's `settings.json`:
  `"env": {"WORKFLOW_PYTHON": "python"}` (or `python3`, or a full path without spaces).
Hook commands run through bash (Git Bash on Windows), which expands the variable. If neither works the hook fails as a
non-blocking error, so the guard is silently off: run the self-test once after install.

### Config (optional): `<project>/.claude/workflow.json`
```json
{
  "secret_guard": {
    "secret_files": [".api_token.json"],
    "extra_patterns": ["MYCO_[A-Z0-9]{32}"],
    "protected_paths": ["vault", "tools/models"],
    "private_ids_file": "~/.config/<project>/private_ids.json",
    "private_id_kinds": ["account", "added"]
  },
  "drift_files": ["CLAUDE.md", "NEXT_STEPS.md", ".claude/skills/*/SKILL.md"]
}
```
- `secret_files` adds to the built-in list (.env, client_secret.json, credentials files, SSH keys), matched by basename.
- `protected_paths`: a recursive delete naming one is blocked (use for junctions and folders git can't restore).
- `private_ids_file`: a JSON list of strings, or `{"ids": [{"kind": "...", "v": "..."}]}`; keep it OUTSIDE the repo.
  `private_id_kinds` filters by kind; env `WORKFLOW_PRIVATE_IDS` overrides the path. Names are never printed.
- `context_guard` takes no config: its thresholds are measured (see its docstring) and kept as they are.

### Check it works
```
python hooks/test_hooks.py          # or: uv run --no-project python hooks/test_hooks.py
```
Needs git on PATH (it builds a throwaway repo in the temp dir). Then prove the plugin loads in a fresh session:
`claude -p "Is the working-rules skill listed? reply YES/NO" --model haiku`.

## The offload kit (`scripts/`)
For bulk drafting Claude would otherwise spend tokens on. The output is always a draft Claude verifies.
```
.\scripts\llm.ps1 -Preset fast            # presets in scripts/llm.presets.json (copy the .example; keep it untracked)
.\scripts\llm.ps1 -Model D:\m.gguf -Ctx 8192 -Server C:\llama.cpp\llama-server.exe
python scripts/ask.py "Summarise" < notes.txt
python scripts/batch.py items.json prompt.txt out.md --key name
.\scripts\llm.ps1 -Stop                   # free the GPU when done
```
- `LLM_URL` (default `http://127.0.0.1:8091/v1/chat/completions`) and `LLM_MODEL` point `ask.py` at any
  OpenAI-compatible server. `LLAMA_SERVER` sets the server binary for `llm.ps1`.
- `llm.ps1` stops any running `llama-server` first: one large model fits in 16 GB of VRAM at a time.
- Tested against a mock server: `ask.py` sends the thinking flag and model; `batch.py` re-run made 0 new calls.

## Provenance
- Rules, skills and hooks: generalised from a working content-production repo (six measured tuning rounds for
  `context_guard`; `secret_guard` selftested there) and from memory notes across several of the creator's projects.
- `secret_guard`'s delete guard adapts the mechanism of mattpocock/skills git-guardrails (MIT); no code is vendored.
- `batch.py` generalises a resumable per-item drafting script; its project-specific data fetch was left out.
