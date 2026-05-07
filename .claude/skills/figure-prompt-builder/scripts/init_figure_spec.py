from __future__ import annotations

import argparse
from pathlib import Path


TEMPLATE = """# {title}

- Figure ID: `{name}`
- Archetype: `{archetype}`
- Target section/file: `{target}`

## Goal

Describe what this figure must help a reviewer understand.

## Reviewer Takeaway

One sentence stating what a reviewer should remember after seeing this figure.

## Required Elements

- element 1
- element 2
- element 3

## Required Arrows Or Relationships

- relationship 1
- relationship 2

## Suggested Layout

Describe left-to-right, top-to-bottom, layered, or other layout logic.

## In-Figure Text

List the short labels or box text that should appear in the figure.

## Caption Draft

Write a concise audience-ready caption.

## Generation Plan

- Preferred generation path:
- Optional editable source file under `figure-src/`:
- Final deliverable under `figure/` or another agreed output path:

## Outside-Tool Prompt Pack

If using Gemini, Sora, Midjourney, Flux, or another image model, place the
final structured prompt here.

## TODO

- [ ] Finalize labels
- [ ] Generate or build the figure
- [ ] Save or export the final deliverable
"""


def main() -> None:
    def find_repo_root(start: Path) -> Path:
        for candidate in (start, *start.parents):
            if (candidate / "skills").exists() and (candidate / "template").exists():
                return candidate
        return start

    def resolve_user_path(raw_path: str, current_dir: Path, repo_root: Path) -> Path:
        path = Path(raw_path)
        if path.is_absolute():
            return path
        current_candidate = (current_dir / path).resolve()
        if current_candidate.exists():
            return current_candidate
        return (repo_root / path).resolve()

    def detect_workspace_dir(repo_root: Path, current_dir: Path) -> Path:
        workspace_markers = ("figure-spec", "figure-src", "figure", "00-project-description.tex")
        for candidate in (current_dir.resolve(), *current_dir.resolve().parents):
            if any((candidate / marker).exists() for marker in workspace_markers):
                return candidate
            if candidate == repo_root:
                break
        legacy = repo_root / "proposals"
        if (legacy / "00-project-description.tex").exists():
            return legacy.resolve()
        workspaces = [
            path.resolve()
            for path in sorted(legacy.iterdir())
            if path.is_dir()
            and any((path / marker).exists() for marker in workspace_markers)
        ] if legacy.exists() else []
        if len(workspaces) == 1:
            return workspaces[0]
        return current_dir.resolve()

    parser = argparse.ArgumentParser(
        description="Create a figure brief scaffold for the active figure workspace."
    )
    parser.add_argument(
        "--workspace-dir",
        help=(
            "Figure workspace path such as `proposals/nsf-25-533-fairos`. "
            "If omitted, the script will try to infer the current workspace."
        ),
    )
    parser.add_argument(
        "--proposal-dir",
        dest="legacy_proposal_dir",
        help=argparse.SUPPRESS,
    )
    parser.add_argument("--name", required=True)
    parser.add_argument(
        "--archetype",
        default="overview-architecture",
        choices=[
            "overview-architecture",
            "local-mechanism-or-subsystem",
            "workflow-or-method-pipeline",
            "method-composite",
            "concept-illustration",
            "timeline-or-work-plan",
        ],
    )
    parser.add_argument("--title")
    parser.add_argument("--target", default="current-section-or-slide")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    current_dir = Path.cwd().resolve()
    repo_root = find_repo_root(current_dir)
    workspace_arg = args.workspace_dir or args.legacy_proposal_dir
    workspace_dir = (
        resolve_user_path(workspace_arg, current_dir, repo_root)
        if workspace_arg
        else detect_workspace_dir(repo_root, current_dir)
    )
    figure_spec_dir = workspace_dir / "figure-spec"
    figure_src_dir = workspace_dir / "figure-src"
    figure_spec_dir.mkdir(parents=True, exist_ok=True)
    figure_src_dir.mkdir(parents=True, exist_ok=True)

    spec_path = figure_spec_dir / f"{args.name}.md"
    if spec_path.exists() and not args.overwrite:
        raise SystemExit(f"{spec_path} already exists. Use --overwrite to replace it.")

    title = args.title or args.name.replace("-", " ").title()
    content = TEMPLATE.format(
        title=title,
        name=args.name,
        archetype=args.archetype,
        target=args.target,
    )
    spec_path.write_text(content, encoding="utf-8")
    print(spec_path)


if __name__ == "__main__":
    main()
