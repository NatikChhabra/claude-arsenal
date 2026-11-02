#!/usr/bin/env python3
"""ship_score.py - average 1-3 blind reviews written on references/blind-rubric.md and COMPUTE the ship score.

    python ship_score.py a.md b.md c.md          # a long video, 3 reviewers
    python ship_score.py --short s1_a.md          # a Short or Reel, one file per cut
    python ship_score.py --selftest

Per review: gated = min(its row mean, the AI-feel cap from its §0a tells, its gate rows). A missing row, tell or gate
row = GATED MISSING (re-run that reviewer). Short: a blank / "not sure" / "no" answer to one of the 4 questions = RE-CUT.
Ship score = min(mean of the row means, mean of the gated). The line `**Ship score: X**` is what gets stamped.
Why computed: a plain 39-row mean read a cut the creator rated 5 as 8.29 (tells diluted, unheard sound rows at 8-9).
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUB = open(os.path.join(HERE, "references", "blind-rubric.md"), encoding="utf-8").read()
block = lambda name: [r.strip() for r in re.search(rf"## {name} \(exact names\)\n(.*?)\n\n", RUB, re.S).group(1)
                      .replace("\n", " ").split("·")]
ROWS, SHORT_ROWS = block("Rows"), block("Short rows")
GATES = ["Feels made by a person", "Fun to a stranger", "Sound quality"]
SHORT_GATES = GATES[:2]
TELLS = [f"T{i}" for i in range(1, 8)] + [f"J{i}" for i in range(1, 8)]
QUESTIONS = ["What happened", "Why is it funny|Why is it worth it", "Want to finish it", "Watch the full video"]
NO = re.compile(r"\W*(not sure|unsure|not really|no(pe)?\b|nothing|none|n/?a\b|don'?t know)", re.I)
cap = lambda p: 10 if p == 0 else 7 if p <= 2 else 6 if p <= 5 else 5     # P = tells scored 2
key = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
section = lambda txt, h: (re.search(rf"\n## (?:§\s*)?{h}\b(.*?)(?=\n## |\Z)", "\n" + txt, re.S) or [None, ""])[1]


def parse(txt, names):
    """-> ({row or gate: score}, {tell: 0/1/2} from §0a only, {question: answer})."""
    sc, qa, tells = {}, {}, {}
    qkeys = {key(alt): q for q in QUESTIONS for alt in q.split("|")}
    for line in txt.splitlines():
        c = [x.strip(" *") for x in line.split("|")]
        for i, cell in enumerate(c[:-1]):
            k = next((r for r in names if key(r) == key(cell)), None)
            m = k and re.match(r"(\d+(?:\.\d+)?)", c[i + 1])
            if m and k not in sc: sc[k] = float(m.group(1)); break
            q = qkeys.get(key(cell))
            if q and q not in qa: qa[q] = c[i + 1]; break
    for line in section(txt, "0a").splitlines():      # a pasted audit table elsewhere never counts as a score
        c = [x.strip(" *") for x in line.split("|")]
        m = len(c) > 2 and re.match(r"([TJ]\d)\b", c[1])
        s = m and re.fullmatch(r"[012]", c[2])
        if s and m.group(1) in TELLS and m.group(1) not in tells: tells[m.group(1)] = int(c[2])
    return sc, tells, qa


def gated(txt, rows, gates, short):
    """-> (gated or None, P, [missing or re-cut reasons])."""
    sc, tells, qa = parse(txt, rows + gates)
    miss = [r for r in rows + gates if r not in sc] + [t for t in TELLS if t not in tells]
    if short:
        miss += [q for q in QUESTIONS if q not in qa]
        miss += [f"re-cut: {q.split('|')[0]}" for q in QUESTIONS if q in qa and (not re.sub(r"\W", "", qa[q]) or NO.match(qa[q]))]
    p = sum(v == 2 for v in tells.values())
    if miss: return None, p, miss
    return min([sum(sc[r] for r in rows) / len(rows), cap(p)] + [sc[g] for g in gates]), p, []


def report(texts, short=False):
    rows, gates = (SHORT_ROWS, SHORT_GATES) if short else (ROWS, GATES)
    parsed = [parse(t, rows + gates)[0] for t in texts]
    out, low, means = ["| Row | Mean | Min | Scores |", "|---|---|---|---|"], [], []
    for r in rows:
        v = [p[r] for p in parsed if r in p]
        if not v: out.append(f"| {r} | MISSING | | |"); low.append(r); continue
        m = sum(v) / len(v); means.append(m)
        out.append(f"| {r} | {m:.2f} | {min(v):g} | {' / '.join(f'{x:g}' for x in v)} |")
        if m < 8.5: low.append(r)
    rmean = sum(means) / len(means) if means else 0
    out.append(f"\n**Row mean: {rmean:.2f}**; rows under 8.5 ({len(low)}): {', '.join(low) or 'none'}\n")
    gs, bad = [], []
    for i, t in enumerate(texts, 1):
        v, p, miss = gated(t, rows, gates, short)
        typed = re.search(r"Gated overall:\s*\**\s*(\d+(?:\.\d+)?)", t)
        if v is None: bad += miss; out.append(f"- review {i}: GATED MISSING / RE-CUT: {', '.join(miss)}"); continue
        gs.append(v)
        flag = " (TYPED != COMPUTED: the computed ships)" if typed and abs(float(typed.group(1)) - v) >= 0.05 else ""
        out.append(f"- review {i}: P {p}, cap {cap(p):g}, gated {v:.2f}{flag}")
    if bad or not gs:
        recut = [m for m in bad if m.startswith("re-cut")]
        out.append(f"\n**Ship score: {'RE-CUT (' + ', '.join(recut) + ')' if recut else 'GATED MISSING'}**")
        return "\n".join(out), None
    ship = min(rmean, sum(gs) / len(gs))
    out.append(f"\n**Ship score: {ship:.2f}**")
    return "\n".join(out), ship


def _selftest():
    def rev(at2, gates, rows=ROWS, extra="", typed=None):
        t = "| Row | Score | Evidence |\n|---|---|---|\n" + "\n".join(f"| {r} | 9 | x |" for r in rows)
        t += "\n\n## §0a AI-feel audit\n| Tell | 0/1/2 | Times | Why |\n|---|---|---|---|\n"
        t += "\n".join(f"| {x} name | {2 if i < at2 else 0} | 0:10 | y |" for i, x in enumerate(TELLS))
        t += "\n\n## §0c Gate rows\n| Gate row | Score | Evidence |\n|---|---|---|\n" + "\n".join(f"| {k} | {v} | z |" for k, v in gates.items())
        return t + extra + (f"\n\n**Gated overall: {typed}**\n" if typed is not None else "\n")
    clean = {"Feels made by a person": 9, "Fun to a stranger": 9.5, "Sound quality": 9}
    assert report([rev(0, clean)])[1] == 9.0
    assert report([rev(1, clean)])[1] == 7 and report([rev(3, clean)])[1] == 6        # the cap ladder
    a = rev(12, {"Feels made by a person": 4, "Fun to a stranger": 5, "Sound quality": 5}, typed=4)
    b = rev(13, {"Feels made by a person": 5, "Fun to a stranger": 6, "Sound quality": 5}, typed=8)
    txt, ship = report([a, b])
    assert ship == 4.5 and "TYPED != COMPUTED" in txt, txt                             # validated case: 4 and 5 -> 4.50
    assert "GATED MISSING" in report([rev(0, {"Feels made by a person": 9, "Fun to a stranger": 9})])[0]
    pasted = rev(0, clean).replace("## §0a", "| T1 emoji | 0 | ok |\n\n## §0x")
    assert report([pasted])[1] is None                                                  # tells outside §0a never count
    sg = {"Feels made by a person": 9, "Fun to a stranger": 9}
    qs = lambda ans, q2="Why is it funny": "\n\n## Questions\n| Question | Answer |\n|---|---|\n" + "\n".join(
        f"| {q} | {x} |" for q, x in zip(["What happened", q2, "Want to finish it", "Watch the full video"], ans))
    assert report([rev(0, sg, SHORT_ROWS, qs(["he falls", "the timing", "yes", "the full run"]))], short=True)[1] == 9.0
    assert report([rev(0, sg, SHORT_ROWS, qs(["a fix", "saves 2 h", "yes", "yes"], "Why is it worth it"))], short=True)[1] == 9.0
    txt = report([rev(0, sg, SHORT_ROWS, qs(["he falls", "not sure", "nope", "the run"]))], short=True)[0]
    assert "RE-CUT (re-cut: Why is it funny, re-cut: Want to finish it)" in txt, txt
    assert len(SHORT_ROWS) == 10 and len(ROWS) >= 30, (ROWS, SHORT_ROWS)
    print("ship_score selftest OK")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--selftest"]: _selftest(); sys.exit()
    if a in (["-h"], ["--help"]): print(__doc__); sys.exit()
    if not [x for x in a if x != "--short"]: print(__doc__); sys.exit(1)
    print(report([open(p, encoding="utf-8").read() for p in a if p != "--short"], "--short" in a)[0])
