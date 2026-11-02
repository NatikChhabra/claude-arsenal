#!/usr/bin/env python3
"""validate.py - structure check for the Claude Arsenal. Run before every push; CI runs it too.

    python scripts/validate.py          # check everything, exit 1 on any error
    python scripts/validate.py --due    # also list registry rows whose recheck date has passed

Checks: marketplace.json parses and every listed plugin exists with a matching plugin.json (name + version);
every plugin directory is listed; every SKILL.md has frontmatter with `name` (matching its folder) and `description`,
and a `status:` line (draft|beta|stable); skill names are unique; registry verdicts are known values; no banned names.
Standard library only.
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
STATUSES = {"draft", "beta", "stable"}
VERDICTS = {"ADOPT", "TRIAL", "WATCH", "SKIP"}
# Names the owner wants kept out of this repo (owner, 2 Nov 2026). Stored as hashes so the names never appear here.
# A word (or two adjacent words joined) whose sha256[:16] is in this set is refused. Add one: hashlib.sha256(b"word").hexdigest()[:16]
BANNED = {"26fa1ef0060cbe67", "4099acf831f06493", "723b00fcb4a6b77b", "8c962913fcb7b0d6"}
errors = []


def err(msg):
    errors.append(msg)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def check_marketplace():
    path = ROOT / ".claude-plugin" / "marketplace.json"
    try:
        mk = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        err(f"{path}: {e}")
        return
    listed = set()
    for p in mk.get("plugins", []):
        name, src = p.get("name"), p.get("source", "")
        listed.add(name)
        pdir = (ROOT / src).resolve()
        pj = pdir / ".claude-plugin" / "plugin.json"
        if not pj.is_file():
            err(f"marketplace plugin {name}: missing {pj.relative_to(ROOT) if pj.is_relative_to(ROOT) else pj}")
            continue
        meta = json.loads(pj.read_text(encoding="utf-8"))
        if meta.get("name") != name:
            err(f"{pj.relative_to(ROOT)}: name {meta.get('name')!r} != marketplace {name!r}")
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(meta.get("version", ""))):
            err(f"{pj.relative_to(ROOT)}: version must be semver")
        if p.get("version") and p["version"] != meta.get("version"):
            err(f"plugin {name}: marketplace version {p['version']} != plugin.json {meta.get('version')}")
    for d in sorted((ROOT / "plugins").iterdir()):
        if d.is_dir() and d.name not in listed:
            err(f"plugins/{d.name} is not listed in marketplace.json")


def check_skills():
    seen = {}
    for sk in sorted(ROOT.glob("plugins/*/skills/*/SKILL.md")):
        rel = sk.relative_to(ROOT)
        text = sk.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if fm is None:
            err(f"{rel}: missing --- frontmatter ---")
            continue
        name = fm.get("name", "")
        if name != sk.parent.name:
            err(f"{rel}: name {name!r} must match folder {sk.parent.name!r}")
        if len(fm.get("description", "")) < 20:
            err(f"{rel}: description missing or too short")
        m = re.search(r"^status:\s*(\w+)", text, re.M)
        if not m or m.group(1) not in STATUSES:
            err(f"{rel}: needs a 'status: draft|beta|stable' line")
        if name in seen:
            err(f"{rel}: skill name {name!r} also used in {seen[name]}")
        seen[name] = rel
    return len(seen)


def registry_rows():
    for f in sorted((ROOT / "registry").glob("*.md")):
        for line in f.read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if line.startswith("|") and len(cells) >= 7 and cells[0] not in ("name", "") and not set(cells[0]) <= {"-"}:
                yield f.name, cells


def check_registry(due):
    today = datetime.date.today()
    n = 0
    for fname, cells in registry_rows():
        verdict = cells[4].split()[0] if cells[4] else ""
        if verdict not in VERDICTS:
            err(f"registry/{fname}: row {cells[0]!r} verdict {cells[4]!r} not in {sorted(VERDICTS)}")
        n += 1
        if due and re.fullmatch(r"\d{4}-\d{2}-\d{2}", cells[5]):
            if datetime.date.fromisoformat(cells[5]) <= today:
                print(f"DUE  {cells[5]}  {cells[0]}  ({fname})")
    return n


def check_banned():
    for f in ROOT.rglob("*"):
        if ".git" in f.parts or not f.is_file() or f.suffix not in {".md", ".json", ".py", ".yml", ".txt"}:
            continue
        for i, line in enumerate(f.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            words = re.findall(r"[a-z0-9]+", line.lower())
            grams = words + [a + b for a, b in zip(words, words[1:])]
            if any(hashlib.sha256(g.encode()).hexdigest()[:16] in BANNED for g in grams):
                err(f"{f.relative_to(ROOT)}:{i}: banned name (see BANNED in scripts/validate.py)")


def main():
    due = "--due" in sys.argv
    check_marketplace()
    skills = check_skills()
    rows = check_registry(due)
    check_banned()
    for e in errors:
        print("ERROR", e)
    print(f"{'FAIL' if errors else 'PASS'}: {skills} skills, {rows} registry rows, {len(errors)} errors")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
