#!/usr/bin/env python
"""
FILE PURPOSE: Update "Points To" and "Referenced By" sections in docs based on inline ::--:: references.

USAGE:
    python scripts/update_doc_refs.py

HOW IT WORKS:
- Scans .md and .txt files (excluding docs/old, .venv, __pycache__).
- Looks for inline markers like "See ::--:: docs/COMMAND_CHEATSHEET.md".
- Builds a graph of references and writes/update a header block near the top.
  For .md files:
    <!-- REF-HEADER-START -->
    Points To:
    - docs/COMMAND_CHEATSHEET.md
    Referenced By:
    - README.md
    <!-- REF-HEADER-END -->
  For .txt files (commented so tools like pip ignore it):
    # REF-HEADER-START
    # Points To:
    # - docs/COMMAND_CHEATSHEET.md
    # Referenced By:
    # - README.md
    # REF-HEADER-END
- If a file has no references, its Points To list is empty.
- Referenced By is computed from other files pointing here.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Set

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {"docs/old", ".venv", "venv", "__pycache__"}
REF_PATTERN = re.compile(r"::--::\s+([^\s]+)")
MD_HEADER_START = "<!-- REF-HEADER-START -->"
MD_HEADER_END = "<!-- REF-HEADER-END -->"
TXT_HEADER_START = "# REF-HEADER-START"
TXT_HEADER_END = "# REF-HEADER-END"
LEGACY_TXT_HEADER_START = "# <!-- REF-HEADER-START -->"
LEGACY_TXT_HEADER_END = "# <!-- REF-HEADER-END -->"
HEADER_TOKENS = [
    (MD_HEADER_START, MD_HEADER_END),
    (TXT_HEADER_START, TXT_HEADER_END),
    (LEGACY_TXT_HEADER_START, LEGACY_TXT_HEADER_END),
]


def should_skip(path: Path) -> bool:
    for part in path.parts:
        if part in EXCLUDE_DIRS:
            return True
    return False


def collect_files() -> List[Path]:
    files: List[Path] = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".txt"} and not should_skip(path):
            files.append(path)
    return files


def extract_refs(text: str) -> Set[str]:
    return set(REF_PATTERN.findall(text))


def split_header_and_body(text: str):
    for start_token, end_token in HEADER_TOKENS:
        if start_token in text and end_token in text:
            pre, _, rest = text.partition(start_token)
            header_block, _, body = rest.partition(end_token)
            return pre, start_token + header_block + end_token, body
    return "", "", text


def build_header(points_to: Set[str], referenced_by: Set[str], *, line_prefix: str, start: str, end: str) -> str:
    lines = [start, f"{line_prefix}Points To:"]
    for ref in sorted(points_to):
        lines.append(f"{line_prefix}- {ref}")
    lines.append(f"{line_prefix}Referenced By:")
    for ref in sorted(referenced_by):
        lines.append(f"{line_prefix}- {ref}")
    lines.append(end)
    return "\n".join(lines) + "\n"


def main() -> None:
    files = collect_files()
    refs_by_file: Dict[Path, Set[str]] = {}
    for f in files:
        text = f.read_text(encoding="utf-8", errors="replace")
        refs_by_file[f] = extract_refs(text)

    # Reverse map: target -> set of sources
    referenced_by: Dict[Path, Set[str]] = {}
    for src, targets in refs_by_file.items():
        for tgt in targets:
            tgt_path = (ROOT / tgt).resolve()
            referenced_by.setdefault(tgt_path, set()).add(str(src.relative_to(ROOT)))

    for f in files:
        text = f.read_text(encoding="utf-8", errors="replace")
        pre, header_block, body = split_header_and_body(text)
        points_to = refs_by_file.get(f, set())
        ref_by = referenced_by.get(f.resolve(), set())
        if f.suffix == ".txt":
            new_header = build_header(
                points_to,
                ref_by,
                line_prefix="# ",
                start=TXT_HEADER_START,
                end=TXT_HEADER_END,
            )
        else:
            new_header = build_header(
                points_to,
                ref_by,
                line_prefix="",
                start=MD_HEADER_START,
                end=MD_HEADER_END,
            )
        new_text = pre + new_header + body if header_block else new_header + text
        f.write_text(new_text, encoding="utf-8")


if __name__ == "__main__":
    main()
