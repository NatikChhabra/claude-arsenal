"""Shared vault layout for every study script.

Each script runs from the vault root and reads `study.json` there (or the file named by
--config). Every key is optional; missing keys fall back to the defaults below, which
derive from "root" (the study folder inside the vault). Paths are relative to the vault root.

    {"root": "Study",
     "subjects": ["Political Science", "Psychology"],
     "book_folders": {"Political Science": ["Book 1", "Book 2"]},
     "flat_subjects": ["Psychology"]}
"""
import io
import json
import os
import sys


def defaults(root):
    j = lambda *p: "/".join((root,) + p)
    return {
        "root": root,
        "notes": j("Notes"),
        "notes_index": j("Notes", "Notes.md"),
        "error_logs": j("Error Log"),
        "master_log": "Error Log.md",                    # inside error_logs
        "log_skip": ["Error Log.md", "Cross-Subject Synthesis.md"],
        "codes": ["K", "R", "D", "F", "T", "E", "S", "P", "C"],
        "mock_reviews": j("Mock Review"),
        "papers": j("Backend", "Papers"),
        "papers_skip": ["_Reference", "Project"],      # folder names that hold non-scan PDFs
        "paper_skip_words": ["question paper"],        # a printed paper with no answers to diagnose
        "paper_tag": r"(PA|Mock|Term|Pre-?board|Unit Test|UT)\s*-?\s*(\d+)",
        "marks_log": j("Marks", "Marks Log.md"),
        "dashboard": j("Dashboard.md"),
        "link_roots": [j("Dashboard.md"), "CLAUDE.md", "README.md"],
        "skip_dirs": [".git", ".obsidian", ".claudian", "node_modules", ".remember",
                      "__pycache__", ".venv", "worktrees", "cache"],
        "bank_dirs": [],                                # note folders exempt from chapter-note checks
        "exempt_types": ["bank", "index", "reference", "cram-sheet"],
        "book_folders": {},                             # subject -> [book subfolder, ...]
        "flat_subjects": [],                            # subjects whose notes sit directly in Notes/<Subject>/
        "textbooks": j("reference", "Textbooks"),       # <textbook folder>/<chapter>.pdf
        "bookmap": {},                                  # textbook folder -> notes subfolder
        "not_in_syllabus": [],                          # chapter-name fragments with no note by design
        "diagrams": j("Backend", "Media", "diagrams"),
        "images": j("Backend", "Media", "images"),
    }


def load(path=None):
    path = path or os.environ.get("STUDY_CONFIG") or "study.json"
    user = {}
    if os.path.exists(path):
        with io.open(path, encoding="utf-8") as f:
            user = json.load(f)
    cfg = defaults(user.get("root", "Study"))
    cfg.update(user)
    return cfg


def config_arg(ap):
    ap.add_argument("--config", help="vault config JSON (default: ./study.json, or $STUDY_CONFIG)")
    return ap


def utf8():
    """Vault filenames carry emoji and long dashes; a cp1252 console crashes mid-report without this."""
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass
