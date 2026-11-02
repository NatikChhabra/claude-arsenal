"""secret_guard.py: Claude Code PreToolUse hook (matcher "Bash|PowerShell"). Stdlib only, zero model tokens.

Blocks (exit 2, reason on stderr, which Claude sees) when a `git commit` / `git push` / `git add` is about to run and
  - a secret file (default .env, client_secret.json, credentials files, SSH keys; by basename) is tracked, staged or named
    in a `git add`, or a private_ids.json is named in a `git add`;
  - a key-shaped string (Google, GitHub, Anthropic, OpenAI, HF, AWS, Slack, Meta tokens, private keys, a filled-in
    *_API_KEY= / *_TOKEN= / *_SECRET=) is in the working-tree diff, the staged diff, a new untracked file, or (for push)
    the commits not yet on any remote;
  - a private name from the project's private-ids file is in those same texts (never echoed back).
Also blocks deletes git cannot undo:
  - `git clean` with -x/-X (wipes every ignored file: .env, tokens, raw media, models);
  - a recursive delete (rm -r, Remove-Item -Recurse, rmdir/rd /s) naming a protected path. On Windows a recursive
    delete follows a junction into the real folder; remove a junction with  cmd /c rmdir "<junction>"  (no /s).
Also blocks git commands that throw away work no commit holds, and remote code run unseen (idea from
kenryu42/claude-code-safety-net, MIT; no code taken):
  - `git reset --hard`, `git checkout -- <path>` / `git checkout .`, `git restore <path>` without --staged,
    `git clean -f` without -n, `git stash drop|clear`, `git branch -D`, `git push --force` / `-f` without
    --force-with-lease (a force push with a lease, or to a branch only you use, is the safe form);
  - a download piped into a shell (`curl ... | sh`, `iwr ... | iex`).
  Commit or stash first; the user can run the command themselves (prefix `!`) when it is really meant.
Anything else: exit 0, silent. Quoted text (a commit message that mentions `rm -rf X`) never triggers.

Config (optional): <project>/.claude/workflow.json, key "secret_guard":
  {"secret_files": [...], "extra_patterns": ["regex", ...], "protected_paths": ["vault", "tools/models"],
   "private_ids_file": "~/.config/<project>/private_ids.json", "private_id_kinds": ["account", "added"]}
private_ids_file holds a JSON list of strings, or {"ids": [{"kind": ..., "v": ...}]}; names under 4 chars are ignored.
Env WORKFLOW_PRIVATE_IDS overrides the file path. The mechanism for the delete guard is adapted from mattpocock/skills
git-guardrails (MIT). Test: hooks/test_hooks.py.
"""
import json, os, re, subprocess, sys

PATTERNS = [
    r"AIza[0-9A-Za-z_\-]{35}",                          # Google API key
    r"1//0[0-9A-Za-z_\-]{40,}", r"GOCSPX-[0-9A-Za-z_\-]{20,}",  # Google OAuth refresh token, client secret
    r"IG(?:AA|QV)[0-9A-Za-z_\-]{40,}",                  # Instagram / Meta access token
    r"\bgh[pousr]_[A-Za-z0-9]{36}", r"\bgithub_pat_[A-Za-z0-9_]{50,}",  # GitHub tokens
    r"\bsk-ant-[A-Za-z0-9_\-]{20,}", r"\bsk-(?:proj-)?[A-Za-z0-9_\-]{32,}",  # Anthropic, OpenAI
    r"\bhf_[A-Za-z0-9]{30,}", r"\bAKIA[0-9A-Z]{16}", r"xox[baprs]-[A-Za-z0-9\-]{10,}",  # HF, AWS, Slack
    r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----",
    r"\b[A-Z][A-Z0-9_]*(?:API_KEY|TOKEN|SECRET)\s*=\s*['\"]?[A-Za-z0-9_\-./+=]{20,}",
]
SECRET_FILES = [".env", "client_secret.json", "credentials.json", ".credentials.json", "id_rsa", "id_ed25519"]
GIT_CLEAN_X = re.compile(r"^\s*git\b.*\bclean\b.*\s-[a-zA-Z]*[xX]")
DELETE = re.compile(r"^\s*(sudo\s+|cmd(\.exe)?\s+/c\s+|(powershell|pwsh)(\.exe)?\s+(-\w+\s+)*[\"']?)?"
                    r"(rm|Remove-Item|ri|del|erase|rmdir|rd)\b", re.I)
LOSES_WORK = [re.compile(r) for r in (   # git flags are case-sensitive: -D loses a branch, -d does not
    r"^\s*git\b.*\breset\b.*\s--hard\b", r"^\s*git\b.*\bcheckout\b.*(\s--(\s|$)|\s\.\s*$)",
    r"^\s*git\b.*\brestore\b(?!.*\s(-S|--staged)\b)", r"^\s*git\b.*\bclean\b(?!.*\s(-[a-zA-Z]*n|--dry-run)\b)",
    r"^\s*git\b.*\bstash\s+(drop|clear)\b", r"^\s*git\b.*\bbranch\b.*\s(-D|--delete\s+--force)\b",
    r"^\s*git\b.*\bpush\b(?!.*--force-with-lease)(.*\s(--force|-f)\b|.*\s\+\S)")]
PIPE_SHELL = re.compile(r"\b(curl|wget|iwr|irm|Invoke-WebRequest|Invoke-RestMethod)\b[^|]*\|\s*"
                        r"((sudo\s+)?(ba|z|da)?sh|iex|Invoke-Expression|python3?|node)\b", re.I)
QUOTED = re.compile(r"'[^']*'|\"[^\"]*\"")


def config(cwd):
    root = os.environ.get("CLAUDE_PROJECT_DIR") or cwd
    try:
        with open(os.path.join(root, ".claude", "workflow.json"), encoding="utf-8") as f:
            return json.load(f).get("secret_guard") or {}
    except (OSError, ValueError, AttributeError):
        return {}


def path_re(p):
    """A protected path as a regex: either slash, case-insensitive, not part of a longer name (obs-studio != studio)."""
    parts = [re.escape(s) for s in re.split(r"[/\\]+", p.strip("/\\")) if s]
    return re.compile(r"(?<![\w-])" + r"[/\\]+".join(parts) + r"(?![\w-])", re.I)


def destroys(cmd, protected):
    """`git clean -x/-X`, or a recursive delete naming a protected path. Commands only, never quoted text."""
    if any(GIT_CLEAN_X.search(p) for p in re.split(r"[;&|\n]", QUOTED.sub("''", cmd))):
        return True
    for part in re.split(r"[;&|\n]", QUOTED.sub(lambda m: re.sub(r"[;&|\n]", " ", m.group(0)), cmd)):
        flags = [t.strip("'\"").lower() for t in part.split()]
        recursive = any(t in ("/s", "-recurse") or (re.fullmatch(r"-[a-z]{1,4}", t) and "r" in t) for t in flags)
        if DELETE.search(part) and recursive and any(r.search(part) for r in protected):
            return True
    return False


def loses_work(cmd):
    """A git command that discards uncommitted or unpushed work, or a download piped into a shell."""
    bare = QUOTED.sub("''", cmd)
    if PIPE_SHELL.search(bare):
        return "a download piped straight into a shell runs code nobody read; save it, read it, then run it"
    for part in re.split(r"[;&|\n]", bare):
        if any(r.search(part) for r in LOSES_WORK):
            return ("this git command throws away work no commit holds (uncommitted edits, untracked files, a stash, "
                    "an unmerged branch or someone's pushed commits); commit or stash first, or use "
                    "--force-with-lease / git clean -n / git restore --staged")
    return ""


def git(cwd, *args):
    r = subprocess.run(["git", *args], cwd=cwd, capture_output=True)
    return r.stdout.decode("utf-8", "replace") if r.returncode == 0 else ""


def block(msg):
    sys.stderr.write("secret_guard: BLOCKED: " + msg + "\nKeep secrets only in git-ignored files. "
                     "Take it out of the change, then retry.\n")
    sys.exit(2)


def private_names(cfg):
    path = os.environ.get("WORKFLOW_PRIVATE_IDS") or cfg.get("private_ids_file")
    if not path:
        return []
    kinds = set(cfg.get("private_id_kinds") or [])
    try:
        data = json.load(open(os.path.expanduser(path), encoding="utf-8"))
        items = data.get("ids", []) if isinstance(data, dict) else data
        vals = [e if isinstance(e, str) else e.get("v", "") for e in items
                if isinstance(e, str) or not kinds or e.get("kind") in kinds]
    except (OSError, ValueError, AttributeError, TypeError):
        return []
    return [v.lower() for v in vals if len(v) >= 4]


def added_lines(t):
    return "\n".join(l for l in t.splitlines() if not l.startswith("-"))  # removing a secret is fine


def main():
    try:
        data = json.loads(sys.stdin.buffer.read().decode("utf-8", "replace") or "{}")
    except ValueError:
        return
    if data.get("tool_name") not in ("Bash", "PowerShell"):
        return
    cmd = (data.get("tool_input") or {}).get("command") or ""
    cwd = data.get("cwd") or os.getcwd()
    cfg = config(cwd)
    if destroys(cmd, [path_re(p) for p in cfg.get("protected_paths", [])]):
        sys.stderr.write("secret_guard: BLOCKED: this deletes what git can't bring back (`git clean -x` wipes every "
                         "ignored file; a recursive delete through a protected path or junction wipes the real folder). "
                         "Delete the exact files by name; a junction goes with  cmd /c rmdir \"<junction>\"  (no /s).\n")
        sys.exit(2)
    if why := loses_work(cmd):
        sys.stderr.write("secret_guard: BLOCKED: " + why + ". If it is really meant, the user runs it with `!`.\n")
        sys.exit(2)
    if not re.search(r"\bgit\b[^;&|]*\b(commit|push|add)\b", cmd):
        return
    root = git(cwd, "rev-parse", "--show-toplevel").strip()
    if not root:
        return
    files = list(dict.fromkeys(SECRET_FILES + cfg.get("secret_files", [])))
    # 1. secret files named in a `git add`, tracked, or staged
    names = "|".join(re.escape(f) for f in files + ["private_ids.json", ".private_ids.json"])
    if re.search(r"\bgit\b[^;&|]*\badd\b[^;&|]*(^|[\s/\\])(" + names + r")(\s|$)", cmd):
        block("the command adds a secret file to git")
    tracked = set(git(root, "ls-files").splitlines()) | set(git(root, "diff", "--cached", "--name-only").splitlines())
    for t in tracked:
        if os.path.basename(t) in files:
            block(f"{t} is tracked or staged (run: git rm --cached {t})")
    # 2. key-shaped strings in anything that could be committed or pushed
    # diffs keep only added lines (removing a secret is fine); a new file is scanned whole, so its own lines that
    # start with "-" (a "-----BEGIN PRIVATE KEY-----" header) still count
    texts = [added_lines(git(root, "diff", "HEAD")), added_lines(git(root, "diff", "--cached"))]
    for f in git(root, "ls-files", "--others", "--exclude-standard").splitlines():
        p = os.path.join(root, f)
        try:
            if os.path.getsize(p) < 2_000_000:
                texts.append(open(p, "rb").read().decode("utf-8", "replace"))
        except OSError:
            pass
    if re.search(r"\bpush\b", cmd):
        texts.append(added_lines(git(root, "log", "-p", "--branches", "--not", "--remotes")))
    key = re.compile("|".join(PATTERNS + cfg.get("extra_patterns", [])))
    for t in texts:
        if m := key.search(t):
            block(f"a secret ({m.group(0)[:4]}...) is in the change")
    # 3. private names in anything committed; never echoed
    if private := private_names(cfg):
        for t in texts:
            if any(n in t.lower() for n in private):
                block("a private name from the private-ids file is in the change (the guard never prints it)")


if __name__ == "__main__":
    if sys.argv[1:2] in (["-h"], ["--help"]): print(__doc__); sys.exit(0)
    main()
