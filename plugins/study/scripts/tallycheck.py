"""Recount every subject's Log-table codes, diff against its Recurring Patterns table, then
against the master Cross-Subject Tally. The Log table is the source of truth: it is the evidence.

Subject files: <error_logs>/<Subject>.md with a `## Log` table that has a `Code` column and a
`## Recurring Patterns` table whose rows start with a code and end with its count.
Master file: <error_logs>/<master_log> with a `## Cross-Subject Tally` table whose rows start
with a code and end with the total. A multi-code row ("K + F") counts once for each code.

    python tallycheck.py [--config study.json]

`issues: 0` means both recounts pass; do not recount by hand.
"""
import argparse
import io
import os
import re

import studycfg


def section(body, name):
    """Text of '## <name>' (the heading may carry trailing words) up to the next '## '."""
    m = re.search(r"^##\s+" + re.escape(name) + r"\b.*$", body, re.M)
    if not m:
        return ""
    rest = body[m.end():]
    nxt = re.search(r"^##\s+", rest, re.M)
    return rest[:nxt.start()] if nxt else rest


def cells(line):
    return [c.replace("*", "").replace("`", "").strip() for c in line.strip().strip("|").split("|")]


def as_int(cell):
    """Numeric cells only; tolerates formatting, rejects prose cells (they contain letters)."""
    if re.search(r"[A-Za-z]", cell):
        return None
    d = re.sub(r"[^0-9]", "", cell)
    return int(d) if d else None


def count_log(body, codes):
    tally, rows, code_col = dict.fromkeys(codes, 0), 0, None
    for line in section(body, "Log").splitlines():
        if not line.strip().startswith("|"):
            continue
        cs = cells(line)
        if code_col is None:
            if "Code" in cs:
                code_col = cs.index("Code")
            continue
        if set("".join(cs)) <= set("-: ") or code_col >= len(cs):
            continue
        rows += 1
        for c in {c for c in re.split(r"[,+/ ]+", cs[code_col]) if c in codes}:
            tally[c] += 1
    return tally, rows


def declared(sec, codes):
    out = {}
    for line in sec.splitlines():
        if not line.strip().startswith("|"):
            continue
        cs = cells(line)
        if len(cs) < 2 or cs[0] not in codes:
            continue
        nums = [n for n in (as_int(c) for c in cs[1:]) if n is not None]
        if nums:
            out[cs[0]] = nums[-1]
    return out


def main():
    ap = studycfg.config_arg(argparse.ArgumentParser(description="Recount error-log tallies."))
    a = ap.parse_args()
    studycfg.utf8()
    cfg = studycfg.load(a.config)
    codes, logdir = cfg["codes"], cfg["error_logs"]
    grand, total_rows, fails = dict.fromkeys(codes, 0), 0, []
    for fn in sorted(os.listdir(logdir)):
        if not fn.endswith(".md") or fn in cfg["log_skip"] or fn.startswith("_"):
            continue
        body = io.open(os.path.join(logdir, fn), encoding="utf-8").read()
        tally, rows = count_log(body, codes)
        said = declared(section(body, "Recurring Patterns"), codes)
        total_rows += rows
        for c in codes:
            grand[c] += tally[c]
        bad = [(c, tally[c], said[c]) for c in codes if c in said and said[c] != tally[c]]
        print("%-22s rows=%-3d %s  %s" % (fn[:-3], rows, " ".join("%s%d" % (c, tally[c]) for c in codes if tally[c]),
                                         "FAIL" if bad else "PASS"))
        for c, actual, s in bad:
            print("      MISMATCH %s: log=%d  patterns-table=%d" % (c, actual, s))
            fails.append((fn, c))
    print("-" * 62)
    print("GRAND  rows=%d  instances=%d  %s" % (total_rows, sum(grand.values()),
                                               " ".join("%s%d" % (c, grand[c]) for c in codes if grand[c])))
    master_path = os.path.join(logdir, cfg["master_log"])
    if os.path.exists(master_path):
        master = io.open(master_path, encoding="utf-8").read()
        for c, n in declared(section(master, "Cross-Subject Tally") or master, codes).items():
            if n != grand[c]:
                print("MASTER MISMATCH %s: subjects sum=%d  %s=%d" % (c, grand[c], cfg["master_log"], n))
                fails.append((cfg["master_log"], c))
    else:
        print("no master log at %s (skipped)" % master_path)
    print("issues: %d" % len(fails))
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
