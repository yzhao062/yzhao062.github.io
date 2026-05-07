from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ENTRY_RE = re.compile(
    r"@(?P<kind>\w+)\s*\{\s*(?P<key>[^,]+),(?P<body>.*?)(?=^@\w+\s*\{|\Z)",
    re.S | re.M,
)
CITE_RE = re.compile(
    r"\\[A-Za-z]*cite[A-Za-z]*\*?(?:\[[^\]]*\]){0,2}\{(?P<keys>[^}]*)\}",
    re.S,
)
SKIP_DIRS = {".git", ".agent-config", ".idea", "__pycache__", "node_modules"}


@dataclass
class CitationUse:
    key: str
    path: Path
    line: int


def find_project_root(start: Path) -> Path:
    for candidate in (start, *start.parents):
        if (candidate / ".git").exists():
            return candidate
    return start


def resolve_user_path(raw_path: str, current_dir: Path, project_root: Path) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        return path
    current_candidate = (current_dir / path).resolve()
    if current_candidate.exists():
        return current_candidate
    return (project_root / path).resolve()


def collect_nearby_bibs(path: Path, project_root: Path) -> list[Path]:
    bibs: list[Path] = []
    for candidate in (path.parent.resolve(), *path.parent.resolve().parents):
        bibs.extend(sorted(candidate.glob("*.bib")))
        if candidate == project_root:
            break
    return bibs


def collect_bibs_under(root: Path) -> list[Path]:
    bibs: list[Path] = []
    for path in root.rglob("*.bib"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        bibs.append(path)
    return sorted(bibs)


def load_bib_index(bib_paths: list[Path]) -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = {}
    seen_paths: set[Path] = set()
    for bib_path in bib_paths:
        resolved = bib_path.resolve()
        if resolved in seen_paths or not resolved.exists():
            continue
        seen_paths.add(resolved)
        text = resolved.read_text(encoding="utf-8", errors="ignore")
        for match in ENTRY_RE.finditer(text):
            key = match.group("key").strip()
            index.setdefault(key, []).append(resolved)
    return index


def extract_citations(path: Path) -> list[CitationUse]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    hits: list[CitationUse] = []
    for match in CITE_RE.finditer(text):
        keys = [part.strip() for part in match.group("keys").split(",")]
        line = text.count("\n", 0, match.start()) + 1
        for key in keys:
            if not key or key == "*":
                continue
            hits.append(CitationUse(key=key, path=path, line=line))
    return hits


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check that cite keys used in source files resolve in local .bib files."
    )
    parser.add_argument(
        "--bib",
        action="append",
        default=[],
        help="Explicit .bib file to include. May be passed multiple times.",
    )
    parser.add_argument(
        "--bib-root",
        action="append",
        default=[],
        help="Directory to search recursively for .bib files. May be passed multiple times.",
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="One or more cite-key based source files to inspect.",
    )
    args = parser.parse_args()

    current_dir = Path.cwd().resolve()
    project_root = find_project_root(current_dir)

    resolved_files: list[Path] = []
    all_hits: list[CitationUse] = []
    for raw_path in args.files:
        path = resolve_user_path(raw_path, current_dir, project_root)
        if not path.exists():
            print(f"Missing file: {raw_path}", file=sys.stderr)
            sys.exit(2)
        resolved_files.append(path)
        all_hits.extend(extract_citations(path))

    bib_paths: list[Path] = []
    for raw_bib in args.bib:
        bib_paths.append(resolve_user_path(raw_bib, current_dir, project_root))
    for raw_root in args.bib_root:
        bib_root = resolve_user_path(raw_root, current_dir, project_root)
        if bib_root.exists():
            bib_paths.extend(collect_bibs_under(bib_root))

    if not bib_paths:
        for path in resolved_files:
            bib_paths.extend(collect_nearby_bibs(path, project_root))
    if not bib_paths:
        bib_paths.extend(collect_bibs_under(project_root))

    bib_index = load_bib_index(bib_paths)
    unresolved = [hit for hit in all_hits if hit.key not in bib_index]

    print(
        f"Checked {len(all_hits)} citation uses across {len(resolved_files)} file(s) "
        f"against {len({path.resolve() for path in bib_paths if path.exists()})} bib file(s)."
    )
    if not unresolved:
        print("All cite keys resolved in the discovered bibliography files.")
        return

    print("Unresolved cite keys:")
    for hit in unresolved:
        try:
            rel = hit.path.resolve().relative_to(project_root).as_posix()
        except ValueError:
            rel = hit.path.resolve().as_posix()
        print(f"- {rel}:{hit.line} -> {hit.key}")
    sys.exit(1)


if __name__ == "__main__":
    main()
