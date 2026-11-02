"""Run one prompt template over every record of a JSON list on the local LLM, resumable. Stdlib only.

  python scripts/batch.py items.json prompt.txt out.md [--key name] [--max-tokens 400]
items.json = a list of objects; prompt.txt uses {field} placeholders (a missing field becomes ""); each answer goes into
out.md under "## <key value>". Re-running skips records already in out.md, so a crash or a stopped server loses nothing.
The output is a local-model DRAFT: its header says so, and Claude verifies it before anything uses it.
Generalised from a portfolio-scouting script (the data fetch was project-specific and is left out).
"""
import json
import string
import sys
from pathlib import Path

from ask import ask


class Blank(dict):
    def __missing__(self, k):
        return ""


def fill(template, rec):
    vals = Blank({k: ", ".join(map(str, v)) if isinstance(v, list) else ("" if v is None else v) for k, v in rec.items()})
    return string.Formatter().vformat(template, (), vals)


def main(argv):
    if len(argv) < 3:
        sys.exit(__doc__)
    items = json.loads(Path(argv[0]).read_text(encoding="utf-8"))
    template = Path(argv[1]).read_text(encoding="utf-8")
    out = Path(argv[2])
    key = argv[argv.index("--key") + 1] if "--key" in argv else "name"
    max_tokens = int(argv[argv.index("--max-tokens") + 1]) if "--max-tokens" in argv else 400
    done = out.read_text(encoding="utf-8") if out.exists() else f"# {out.stem} (local LLM draft, verify before use)\n"
    for i, rec in enumerate(items, 1):
        head = f"## {rec.get(key, i)}"
        if head + "\n" in done:  # resumable
            continue
        done += f"\n{head}\n{ask(fill(template, rec), max_tokens=max_tokens)}\n"
        out.write_text(done, encoding="utf-8")
        print(f"[{i}/{len(items)}] {rec.get(key, i)}")


if __name__ == "__main__":
    if sys.argv[1:2] in (["-h"], ["--help"]): print(__doc__); sys.exit(0)
    assert fill("{name}: {tags} {nope}", {"name": "A", "tags": ["x", "y"]}) == "A: x, y "
    main(sys.argv[1:])
