---
name: pre-report-secrets-scan
description: Scan a report, log, bug report, issue draft, or debug output for secrets and sensitive values before it's shared, and return a redacted copy plus a short findings list. Use whenever the user is about to paste, post, send, file, or attach logs, stack traces, config, env dumps, terminal output, or a bug/support report, even if they don't say "secrets" or "scan." Also use before Claude itself files an issue, writes a PR comment or emails a vendor with pasted output.
---
# Pre-report secrets scan

status: draft

## When to run
Before any text leaves the user's hands as a report: GitHub issues, support tickets, Slack posts, vendor emails, shared
docs. That includes text Claude is about to send for the user (`gh issue create`, a PR comment, an email draft): scan
the body first, send only the redacted copy.
Commits are already covered by the workflow `secret_guard` hook; this skill covers everything that leaves by paste.

## What to look for
1. Credentials: API keys, tokens (bearer, OAuth, JWT), passwords, private keys, connection strings with embedded
   passwords, cloud access keys, webhook URLs (Slack, Discord: the URL itself is the key), cookies and session ids.
2. Infrastructure detail: internal hostnames, private IPs, internal URLs, account/project IDs.
3. Personal data: emails, names, phone numbers, user IDs that belong to real people, and the username inside home
   paths (`C:\Users\<name>\`, `/home/<name>/`), which stack traces leak on every line.
4. Look-alikes: long random strings in env vars, headers, or query params, even without a recognizable prefix.
5. Things text can't hold: a screenshot or attachment going with the report. Say it was not scanned and ask the user
   to check it (terminal screenshots often show the same tokens).

## Steps
1. Save the text to a temp file outside the repo (never commit it) and run the first pass:
   `python ${CLAUDE_PLUGIN_ROOT}/scripts/redact.py report.txt --out report.redacted.txt`
   (stdin works too). It knows the common key prefixes (GitHub, Google, AWS, OpenAI, Anthropic, Slack, Stripe, npm,
   GitLab, HF, Meta, SendGrid), JWTs, auth headers, URL passwords, `key=value` secrets, private IPs, internal hosts,
   emails, home-path usernames and high-entropy look-alikes. Findings go to stderr and never show a value.
2. Read the redacted copy yourself, top to bottom. Regex finds shapes; you find meaning: real people's names, phone
   numbers, account or project ids, internal URLs on a normal-looking domain, a secret split across lines or base64'd
   (`Basic dXNlcjpwYXNz` decodes to `user:pass`). Redact those by hand with the same placeholder style.
3. Self-check: run `redact.py --check` on the final copy (exit 0 = nothing left), then confirm every placeholder in
   the findings list appears in the text and no original value does.
4. Deliver the Output below. The user sends it; never post the unredacted text anywhere, not even to "test" a tool.

## How to redact
Replace each value with a typed placeholder that keeps the report readable, e.g. `<REDACTED_API_KEY_1>`,
`<REDACTED_HOST_1>`. Use the same placeholder for repeated occurrences of the same value so the report still makes
sense. Keep the key name and the shape around it (`GITHUB_TOKEN=<REDACTED_GITHUB_TOKEN_1>`): the reader debugging the
issue needs to know a token was set, not what it was. Leave version numbers, public URLs, error codes, commit SHAs and
`127.0.0.1` alone; they are what makes a report useful.

## Output
1. The redacted report, ready to paste.
2. A short findings list: what was found, where, and which placeholder replaced it. Never repeat the value, not even
   its first characters.
3. A flag for anything uncertain (the script marks these UNSURE), so the user decides rather than the scan guessing.
   Uncertain values stay redacted in the copy until the user says to put one back.
4. A reminder: if a real credential was found, it should be rotated, since it may already have been exposed somewhere
   (shell history, a log file, an earlier paste, a commit). Name where to rotate it when the type says (for example
   GitHub: Settings, Developer settings, tokens) and say that redacting the report does not un-leak it.

## Review before delivery
- `redact.py --check` on the final copy exits 0.
- Nothing in the findings list or the reply quotes a secret.
- The report still explains the bug: errors, versions and steps are intact.

## Notes / sources
- `scripts/redact.py` reuses the key patterns of `hooks/secret_guard.py`, so the commit guard and this scan know the
  same shapes; add a new prefix there and both get it. `python ${CLAUDE_PLUGIN_ROOT}/scripts/redact.py --selftest` (CI runs it).
