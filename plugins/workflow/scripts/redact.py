"""redact.py: first-pass secrets scan for text about to be shared (bug report, issue, log, stack trace, env dump).
Stdlib only, no network.

  python scripts/redact.py [file] [--out redacted.txt]   redacted text to stdout (or --out), findings to stderr
  python scripts/redact.py [file] --check                 findings only; exit 1 if anything was found
  python scripts/redact.py --selftest

No file = read stdin. Exit 0 = done (or --check found nothing); 1 = --check found something, or the self-check failed;
2 = bad input. Findings never print a value: only its line, type, length, placeholder and SURE/UNSURE.
Every found value is replaced everywhere it appears (same value = same placeholder), then the output is scanned again;
anything still found fails the self-check. Key shapes come from hooks/secret_guard.py (one list for commits and
reports) plus the report-only shapes below. Regex finds shapes: real names, internal hostnames without a telltale
suffix, account ids and anything inside an image still need the skill's read-through.
"""
import importlib.util, math, os, re, sys

_guard = importlib.util.spec_from_file_location(
    "secret_guard", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "hooks", "secret_guard.py"))
secret_guard = importlib.util.module_from_spec(_guard)
_guard.loader.exec_module(secret_guard)

GUARD_NAMES = {"AIza": "GOOGLE_API_KEY", "1//0": "GOOGLE_REFRESH_TOKEN", "GOCSPX": "GOOGLE_CLIENT_SECRET",
               "IG(?:AA": "META_TOKEN", r"\bgh": "GITHUB_TOKEN", r"\bsk-ant": "ANTHROPIC_KEY", r"\bsk-(?:": "OPENAI_KEY",
               r"\bhf_": "HF_TOKEN", r"\bAKIA": "AWS_ACCESS_KEY", "xox": "SLACK_TOKEN"}
VALUE = r"(?!<REDACTED_)(?![$*%{<])"   # skip placeholders, ${VAR}, ****, %s and <your-key>
# (type, regex, group to redact, sure). In an overlap the earliest start wins, then the earlier rule here.
RULES = [
    ("PRIVATE_KEY", r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?(?:-----END [A-Z ]*PRIVATE KEY-----|\Z)", 0, True),
    ("JWT", r"\beyJ[A-Za-z0-9_-]{8,}\.eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}", 0, True),
    ("STRIPE_KEY", r"\b[rs]k_(?:live|test)_[A-Za-z0-9]{16,}", 0, True),
    ("SENDGRID_KEY", r"\bSG\.[\w-]{16,}\.[\w-]{16,}", 0, True),
    ("NPM_TOKEN", r"\bnpm_[A-Za-z0-9]{36}\b", 0, True),
    ("GITLAB_TOKEN", r"\bglpat-[\w-]{20,}", 0, True),
    ("WEBHOOK", r"https://(?:hooks\.slack\.com/services|(?:\w+\.)?discord(?:app)?\.com/api/webhooks)/[\w/-]+", 0, True),
] + [(next((n for k, n in GUARD_NAMES.items() if p.startswith(k)), "API_KEY"), p, 0, True)
     for p in secret_guard.PATTERNS
     if "PRIVATE KEY" not in p and "API_KEY|TOKEN|SECRET" not in p] + [   # those two are covered below, more precisely
    ("PASSWORD", r"\b[a-z][a-z0-9+.-]*://[^\s:/@]+:(" + VALUE + r"[^\s@/]+)@", 1, True),
    ("AUTH_HEADER", r"(?i)\b(?:proxy-)?authorization\s*[:=]\s*(?:bearer|basic|token|bot)?\s*(" + VALUE + r"[^\s'\"]{8,})", 1, True),
    ("AUTH_HEADER", r"(?i)\bbearer\s+(" + VALUE + r"[A-Za-z0-9._~+/=-]{16,})", 1, True),
    ("COOKIE", r"(?im)^\s*(?:set-)?cookie\s*:\s*(" + VALUE + r".+?)\s*$", 1, True),
    ("SECRET_VALUE", r"(?i)\b[\w.-]*(?:password|passwd|pwd|secret|token|api[_-]?key|apikey|access[_-]?key|accountkey|"
                     r"private[_-]?key|client[_-]?secret|session[_-]?id|signature|sig)\b[\"']?\s*[:=]\s*[\"']?(" + VALUE +
                     r"[^\s\"'&,;]{6,})", 1, True),
    ("PRIVATE_IP", r"\b(?:10\.\d{1,3}|192\.168|172\.(?:1[6-9]|2\d|3[01])\.\d{1,3})\.\d{1,3}\.\d{1,3}\b", 0, True),
    ("INTERNAL_HOST", r"(?i)\b(?:[a-z0-9-]+\.)+(?:internal|corp|intranet|home\.arpa)\b", 0, True),
    ("INTERNAL_HOST", r"\b(?:[a-z0-9-]+\.)+(?:local|lan)\b", 0, False),   # also code: threading.local
    ("EMAIL", r"\b(?!git@)[\w.+-]+@(?!example\.(?:com|org|net)\b)[\w-]+(?:\.[\w-]+)*\.[a-z]{2,}\b", 0, True),
    ("USER", r"(?i)(?:\b[a-z]:\\+users\\+|/home/|/Users/)(?!(?:public|default|all users|runner|root|user|ubuntu)\b)"
             r"(" + VALUE + r"[^\\/\s:\"']+)", 1, True),
    ("PUBLIC_IP", r"(?<![\d.])(?!127\.|0\.0\.0\.0|10\.|192\.168\.|172\.(?:1[6-9]|2\d|3[01])\.)"
                  r"(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)(?![\d.])", 0, False),
]
RULES = [(t, re.compile(r), g, s) for t, r, g, s in RULES]
LOOKALIKE = re.compile(r"(?<![\w+=-])[A-Za-z0-9+_-]{32,}={0,2}(?![\w+=-])")


def entropy(s):
    return -sum(s.count(c) / len(s) * math.log2(s.count(c) / len(s)) for c in set(s))


def find(text):
    """Every (start, end, type, sure) to redact, overlaps resolved: earliest start, then the earlier rule (the more
    specific one: a URL password beats the email it looks like), then longest."""
    hits = [(m.start(g), m.end(g), t, s, i) for i, (t, rx, g, s) in enumerate(RULES)
            for m in rx.finditer(text) if m.group(g)]
    for m in LOOKALIKE.finditer(text):   # a long random string with no known prefix
        v = m.group(0)
        if all(re.search(c, v) for c in ("[a-z]", "[A-Z]", "[0-9]")) and entropy(v) >= 4.0:
            hits.append((m.start(), m.end(), "LOOKALIKE", False, len(RULES)))
    out, end = [], -1
    for h in sorted(hits, key=lambda h: (h[0], h[4], -h[1])):
        if h[0] >= end:
            out.append(h[:4])
            end = h[1]
    return out


def redact(text):
    """(redacted text, findings). Each value is replaced everywhere it appears, with one placeholder per value."""
    names, counts, findings = {}, {}, []
    for a, b, t, sure in find(text):
        v = text[a:b]
        if v not in names:
            counts[t] = counts.get(t, 0) + 1
            names[v] = f"<REDACTED_{t}_{counts[t]}>"
            findings.append({"line": text.count("\n", 0, a) + 1, "type": t, "chars": len(v),
                             "placeholder": names[v], "sure": sure})
    for v in sorted(names, key=len, reverse=True):   # longest first, so a value inside another goes with it
        text = re.sub(r"(?<!\w)" + re.escape(v) + r"(?!\w)", lambda _: names[v], text)
    return text, findings


def report(findings, stream):
    for f in findings:
        stream.write(f"line {f['line']:>4}  {f['type']:<20} {f['chars']:>4} chars  -> {f['placeholder']}  "
                     f"{'SURE' if f['sure'] else 'UNSURE: the user decides'}\n")
    stream.write(f"redact: {len(findings)} value(s) found, {sum(not f['sure'] for f in findings)} unsure\n")


def main(args):
    check = "--check" in args
    out = args[args.index("--out") + 1] if "--out" in args and args.index("--out") + 1 < len(args) else None
    files = [a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or args[i - 1] != "--out")]
    try:
        raw = open(files[0], "rb").read() if files else sys.stdin.buffer.read()
    except OSError as e:
        sys.stderr.write(f"redact: {e}\n")
        return 2
    text = raw.decode("utf-8", "replace")
    redacted, findings = redact(text)
    report(findings, sys.stderr)
    if check:
        return 1 if findings else 0
    if left := find(redacted):
        sys.stderr.write(f"redact: SELF-CHECK FAILED, {len(left)} value(s) still in the output; do not share it\n")
        return 1
    if out:
        open(out, "w", encoding="utf-8", newline="").write(redacted)
    else:
        sys.stdout.buffer.write(redacted.encode("utf-8"))
    return 0


def selftest():
    # fakes are built at run time so this file never holds a token-shaped string (the commit guard and push protection)
    gh, aws = "ghp_" + "aB3dE5fG7h" * 3 + "iJ9kL1", "AKIA" + "IOSFODNN7EXAMPL" + "Q"
    jwt = "eyJ" + "hbGciOiJIUzI1NiJ9" + ".eyJ" + "zdWIiOiIxMjM0NTYifQ" + ".SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV"
    pw, dbpw, qtok = "s3cr3t" + "-pass", "hunter2" * 2, "Zx9QwErTy" + "12345"
    awssec = "wJalrXUtnFEMI/K7MDENG" + "/bPxRfiCYzEXAMPLEKEY"
    pem = "-----BEGIN " + "OPENSSH PRIVATE" + " KEY-----"
    sample = (f"GITHUB_TOKEN={gh}\nretrying with {gh} again\n"
              f"aws_secret_access_key = {awssec}\nkey id {aws}\n"
              f"Authorization: Bearer {jwt}\n"
              f"DATABASE_URL=postgres://app:{dbpw}@db.prod.internal:5432/app\n"
              f"GET /api/v1/items?id=7&token={qtok}&page=2\n"
              'config: {"password": "' + pw + '", "user": "${DB_USER}", "api_key": "<your-key>"}\n'
              "File \"C:\\Users\\riya\\proj\\app.py\", line 3 and /home/riya/.cache and C:\\\\Users\\\\riya\\\\x\n"
              "reach me at riya.k@gmail.com or mailto:ops@acme.io, or noreply@example.com; clone git@github.com:o/r.git\n"
              "printer nas.lan, upstream 10.0.3.17 and 52.14.200.9 failed; version 1.2.3; localhost 127.0.0.1\n"
              "trace id Qm9vX2Jhcl9CYXpfUXV4XzEyMzQ1Njc4OTBhYmNkZWY\n"
              f"{pem}\nb3BlbnNzaC1rZXktdjEAAAAA\n-----END OPENSSH PRIVATE KEY-----\n"
              "commit 3f2a9c1e7b4d5a6f8e9d0c1b2a3f4e5d6c7b8a9f is fine, so is uuid 123e4567-e89b-12d3-a456-426614174000\n")
    red, found = redact(sample)
    for secret in (gh, aws, jwt, awssec, dbpw, qtok, pw, "riya", "ops@acme.io",
                   "nas.lan", "10.0.3.17", "52.14.200.9", "db.prod.internal", "b3BlbnNzaC1r", "Qm9vX2Jhcl9C"):
        assert secret not in red, (secret, red)
    for kept in ("GITHUB_TOKEN=", "aws_secret_access_key = ", "${DB_USER}", "<your-key>", "noreply@example.com",
                 "git@github.com", "version 1.2.3", "127.0.0.1", "3f2a9c1e7b4d5a6f8e9d0c1b2a3f4e5d6c7b8a9f",
                 "123e4567-e89b-12d3-a456-426614174000", "&page=2", "line 3"):
        assert kept in red, (kept, red)
    assert red.count("<REDACTED_GITHUB_TOKEN_1>") == 2, red   # same value, same placeholder, every occurrence
    assert {f["type"] for f in found if not f["sure"]} == {"PUBLIC_IP", "LOOKALIKE", "INTERNAL_HOST"}, found
    assert find(red) == [], find(red)   # the self-check pass finds nothing left
    assert redact("nothing to see here\n") == ("nothing to see here\n", [])
    print(f"redact selftest: PASS ({len(found)} values found, 0 left after redaction)")
    return 0


if __name__ == "__main__":
    if sys.argv[1:2] in (["-h"], ["--help"]): print(__doc__); sys.exit(0)
    sys.exit(selftest() if sys.argv[1:] == ["--selftest"] else main(sys.argv[1:]))
