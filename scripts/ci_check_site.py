#!/usr/bin/env python3
"""Lightweight CI checks for the static site."""

from __future__ import annotations

import json
import os
import re
import subprocess
import time
import sys
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]


def fail(errors: list[str]) -> None:
    print("Site checks failed:")
    for idx, err in enumerate(errors, 1):
        print(f"{idx}. {err}")
    sys.exit(1)


def print_warnings(warnings: list[str]) -> None:
    if not warnings:
        return
    print("Site checks warnings:")
    for idx, msg in enumerate(warnings, 1):
        print(f"{idx}. {msg}")


def load_json(path: Path, errors: list[str]):
    try:
        with path.open("r", encoding="utf-8-sig") as f:
            return json.load(f)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Invalid JSON: {path.as_posix()} ({exc})")
        return None


def check_required_files(errors: list[str]) -> None:
    required = [
        "index.html",
        "lab.html",
        "publications.html",
        "services.html",
        "teaching.html",
        "bib-viewer.html",
        "assets/js/layout-shell.js",
        "assets/js/webstat-tracker.js",
        "assets/vendor/bootstrap/bootstrap.min.css",
        "assets/vendor/bootstrap/bootstrap.bundle.min.js",
        "assets/vendor/fontawesome/css/all.min.css",
        "assets/vendor/fontawesome/webfonts/fa-brands-400.ttf",
        "assets/vendor/fontawesome/webfonts/fa-brands-400.woff2",
        "assets/vendor/fontawesome/webfonts/fa-regular-400.ttf",
        "assets/vendor/fontawesome/webfonts/fa-regular-400.woff2",
        "assets/vendor/fontawesome/webfonts/fa-solid-900.ttf",
        "assets/vendor/fontawesome/webfonts/fa-solid-900.woff2",
        "assets/vendor/fontawesome/webfonts/fa-v4compatibility.ttf",
        "assets/vendor/fontawesome/webfonts/fa-v4compatibility.woff2",
        "css/common.css",
        "data/publications.json",
        "data/open-source.json",
        "data/lab-members.json",
        "data/lab-current-phd.json",
        "files/yue-zhao.bib",
        "includes/navbar.html",
        "includes/sidebar.html",
        "includes/footer.html",
    ]
    for rel in required:
        if not (ROOT / rel).exists():
            errors.append(f"Missing required file: {rel}")


def check_json_files(errors: list[str]) -> None:
    data_dir = ROOT / "data"
    object_json = {"s2-metrics.json"}

    # Parse each file once; store results for per-file field checks below.
    parsed: dict[str, list | dict | None] = {}
    for path in sorted(data_dir.glob("*.json")):
        obj = load_json(path, errors)
        if obj is None:
            parsed[path.name] = None
            continue
        if path.name in object_json:
            if not isinstance(obj, dict):
                errors.append(f"Expected top-level JSON object in {path.as_posix()}")
                parsed[path.name] = None
            else:
                parsed[path.name] = obj
            continue
        if not isinstance(obj, list):
            errors.append(f"Expected top-level JSON array in {path.as_posix()}")
            parsed[path.name] = None
        else:
            parsed[path.name] = obj

    # --- publications.json field checks ---
    publications = parsed.get("publications.json")
    if isinstance(publications, list):
        ids: set[str] = set()
        for idx, item in enumerate(publications):
            if not isinstance(item, dict):
                errors.append(f"publications.json item #{idx} is not an object")
                continue
            pid = str(item.get("id", "")).strip()
            title = str(item.get("title", "")).strip()
            if not pid:
                errors.append(f"publications.json item #{idx} missing non-empty id")
            elif pid in ids:
                errors.append(f"Duplicate publication id: {pid}")
            else:
                ids.add(pid)
            if not title:
                errors.append(f"publications.json item #{idx} missing non-empty title")

    # --- open-source.json field checks ---
    os_items = parsed.get("open-source.json")
    if isinstance(os_items, list):
        for idx, item in enumerate(os_items):
            if not isinstance(item, dict):
                errors.append(f"open-source.json item #{idx} is not an object")
                continue
            if not str(item.get("name", "")).strip():
                errors.append(f"open-source.json item #{idx} missing non-empty name")
            if not str(item.get("repo_url", "")).strip():
                errors.append(f"open-source.json item #{idx} missing non-empty repo_url")

    # --- lab-current-phd.json field checks ---
    phd_items = parsed.get("lab-current-phd.json")
    if isinstance(phd_items, list):
        for idx, item in enumerate(phd_items):
            if not isinstance(item, dict):
                errors.append(f"lab-current-phd.json item #{idx} is not an object")
                continue
            if not str(item.get("name", "")).strip():
                errors.append(f"lab-current-phd.json item #{idx} missing non-empty name")
            if not str(item.get("image", "")).strip():
                errors.append(f"lab-current-phd.json item #{idx} missing non-empty image")

    # --- lab-members.json field checks ---
    mem_items = parsed.get("lab-members.json")
    if isinstance(mem_items, list):
        for idx, item in enumerate(mem_items):
            if not isinstance(item, dict):
                errors.append(f"lab-members.json item #{idx} is not an object")
                continue
            if not str(item.get("name", "")).strip():
                errors.append(f"lab-members.json item #{idx} missing non-empty name")
            group = str(item.get("group", "")).strip()
            if group not in ("current", "past"):
                errors.append(
                    f"lab-members.json item #{idx} ({item.get('name', '?')}): "
                    f"group must be 'current' or 'past', got '{group}'"
                )


def read_text(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Unable to read {path.as_posix()}: {exc}")
        return ""


def check_utf8_bom(errors: list[str]) -> None:
    text_files = list((ROOT / "data").glob("*.json")) + sorted(ROOT.glob("*.html"))
    text_files += sorted((ROOT / "includes").glob("*.html"))
    text_files += sorted((ROOT / "assets/js").glob("*.js"))
    text_files += sorted((ROOT / "css").glob("*.css"))
    text_files += sorted(ROOT.glob("*.txt"))
    text_files += sorted(ROOT.glob("*.md"))
    text_files += sorted(ROOT.glob("*.yml"))
    text_files += sorted(ROOT.glob("*.yaml"))
    for path in text_files:
        try:
            raw = path.read_bytes()
        except Exception:  # noqa: BLE001
            continue
        if raw.startswith(b"\xef\xbb\xbf"):
            errors.append(f"UTF-8 BOM detected: {path.relative_to(ROOT).as_posix()}")


def check_public_urls(errors: list[str], warnings: list[str]) -> None:
    enabled = os.getenv("CHECK_PUBLIC_URLS", "0").strip().lower() in {
        "1",
        "true",
        "yes",
    }
    if not enabled:
        return

    raw_urls = os.getenv(
        "PUBLIC_URLS",
        "https://yzhao062.github.io/,https://viterbi-web.usc.edu/~yzhao010/",
    )
    urls = [u.strip() for u in raw_urls.split(",") if u.strip()]
    if not urls:
        errors.append("CHECK_PUBLIC_URLS is enabled but PUBLIC_URLS is empty")
        return

    for url in urls:
        ok = False
        last_detail = "unknown error"
        ssl_failed = False
        for attempt in range(1, 4):
            try:
                req = Request(url, headers={"User-Agent": "site-checks/1.0"})
                with urlopen(req, timeout=15) as resp:  # nosec B310
                    status = getattr(resp, "status", None) or resp.getcode()
                    if 200 <= int(status) < 400:
                        ok = True
                        break
                    last_detail = f"HTTP {status}"
            except Exception as exc:  # noqa: BLE001
                last_detail = str(exc)
                if "CERTIFICATE_VERIFY_FAILED" in last_detail:
                    ssl_failed = True
            time.sleep(attempt)

        if not ok and ssl_failed:
            # Fallback for local envs with incomplete cert store (for example custom conda envs).
            # Still keeps strict HTTPS verification in normal Python path.
            try:
                result = subprocess.run(
                    [
                        "curl",
                        "-I",
                        "--silent",
                        "--show-error",
                        "--location",
                        "--max-time",
                        "20",
                        "--write-out",
                        "%{http_code}",
                        "--output",
                        os.devnull,
                        url,
                    ],
                    check=False,
                    capture_output=True,
                    text=True,
                )
                status_text = (result.stdout or "").strip()
                status_code = int(status_text[-3:]) if len(status_text) >= 3 else 0
                if result.returncode == 0 and 200 <= status_code < 400:
                    ok = True
                else:
                    last_detail = (
                        f"curl fallback failed (exit={result.returncode}, status={status_text})"
                    )
            except Exception as exc:  # noqa: BLE001
                last_detail = f"curl fallback exception: {exc}"

        if not ok:
            errors.append(f"Public URL not accessible: {url} ({last_detail})")

    soft_raw_urls = os.getenv("PUBLIC_URLS_SOFT", "")
    soft_urls = [u.strip() for u in soft_raw_urls.split(",") if u.strip()]
    for url in soft_urls:
        try:
            result = subprocess.run(
                [
                    "curl",
                    "-I",
                    "--silent",
                    "--show-error",
                    "--location",
                    "--insecure",
                    "--max-time",
                    "20",
                    "--write-out",
                    "%{http_code}",
                    "--output",
                    os.devnull,
                    url,
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            status_text = (result.stdout or "").strip()
            status_code = int(status_text[-3:]) if len(status_text) >= 3 else 0
            if not (result.returncode == 0 and 200 <= status_code < 400):
                warnings.append(
                    f"Soft URL check failed: {url} (exit={result.returncode}, status={status_text})"
                )
        except Exception as exc:  # noqa: BLE001
            warnings.append(f"Soft URL check exception: {url} ({exc})")


def check_page_smoke(errors: list[str], warnings: list[str]) -> None:
    pages = [
        ROOT / "index.html",
        ROOT / "lab.html",
        ROOT / "publications.html",
        ROOT / "opensource.html",
        ROOT / "services.html",
        ROOT / "teaching.html",
    ]
    for page in pages:
        text = read_text(page, errors)
        if not text:
            continue
        for needle, msg in [
            ("<html", "missing <html>"),
            ("<head", "missing <head>"),
            ("<body", "missing <body>"),
            ("<title>", "missing <title>"),
        ]:
            if needle not in text.lower():
                errors.append(f"{page.name}: {msg}")

        if 'rel="stylesheet"' not in text:
            warnings.append(f"{page.name}: no stylesheet link detected")

        # Soft contract only: layout implementation may change after refactors.
        for needle, msg in [
            ('id="navbar"', "no #navbar container"),
            ('id="sidebar"', "no #sidebar container"),
            ('id="myFooter"', "no #myFooter container"),
            ("assets/js/layout-shell.js", "no layout-shell.js reference"),
            ('rel="stylesheet" href="css/common.css"', "no common.css reference"),
        ]:
            if needle not in text:
                warnings.append(f"{page.name}: {msg}")


def normalize_local_ref(url: str) -> str | None:
    if not url or ("' +" in url) or (" + '" in url):
        return None

    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc:
        return None
    if url.startswith(("mailto:", "javascript:", "data:", "#")):
        return None

    path = parsed.path.split("#", 1)[0]
    if not path:
        return None

    while path.startswith("/"):
        path = path[1:]
    return path or None


def check_local_refs(errors: list[str]) -> None:
    pattern = re.compile(r'(?:href|src)\s*=\s*"([^"]+)"', re.IGNORECASE)
    html_files = sorted(ROOT.rglob("*.html"))
    for html in html_files:
        rel_html = html.relative_to(ROOT).as_posix()
        text = read_text(html, errors)
        if not text:
            continue
        for match in pattern.finditer(text):
            raw_url = match.group(1).strip()
            local_path = normalize_local_ref(raw_url)
            if not local_path:
                continue
            target = ROOT / local_path
            if not target.exists():
                errors.append(
                    f"{rel_html}: missing local reference {raw_url} (resolved {local_path})"
                )


def _normalize_title(text: str) -> str:
    """Mirror the normalizeTitle() function in bib-viewer.html."""
    t = text.lower().replace("&amp;", "and")
    t = t.replace("{", "").replace("}", "")
    return re.sub(r"[^a-z0-9]+", "", t)


def _extract_bib_titles(bib_text: str) -> list[str]:
    """Return a list of normalised titles from a .bib file.

    BibTeX titles use nested braces (e.g. ``title = {{XGBOD}: Improving ...}``),
    so a simple non-greedy regex would stop at the first ``}``.  Instead we
    find the ``title = {`` prefix and then walk the string counting brace depth.
    """
    titles: list[str] = []
    for match in re.finditer(r"(?<![a-zA-Z])title\s*=\s*\{", bib_text, re.IGNORECASE):
        start = match.end()
        depth = 1
        i = start
        while i < len(bib_text) and depth > 0:
            if bib_text[i] == "{":
                depth += 1
            elif bib_text[i] == "}":
                depth -= 1
            i += 1
        raw = bib_text[start : i - 1] if depth == 0 else bib_text[start:]
        titles.append(_normalize_title(raw))
    return titles


def check_bib_coverage(errors: list[str], warnings: list[str]) -> None:
    """Ensure every publications.json entry has a matching bib entry."""
    pub_path = ROOT / "data" / "publications.json"
    bib_path = ROOT / "files" / "yue-zhao.bib"

    pubs = load_json(pub_path, errors)
    if not isinstance(pubs, list):
        return
    bib_text = read_text(bib_path, errors)
    if not bib_text:
        return

    bib_titles = _extract_bib_titles(bib_text)

    missing: list[str] = []
    for item in pubs:
        if not isinstance(item, dict):
            continue
        title = str(item.get("title", "")).strip()
        if not title:
            continue
        norm = _normalize_title(title)
        if not norm:
            continue

        # Replicate bib-viewer.html matching: exact, colon-suffix, or prefix-12
        matched = norm in bib_titles
        if not matched and ":" in title:
            tail = _normalize_title(title.split(":", 1)[1])
            if tail and tail in bib_titles:
                matched = True
        if not matched:
            prefix = norm[:24]
            if prefix and any(prefix in bt for bt in bib_titles):
                matched = True
        if not matched:
            short = norm[:12]
            if short and any(short in bt for bt in bib_titles):
                matched = True

        if not matched:
            missing.append(item.get("id", title))

    if missing:
        for pid in missing:
            errors.append(f"No matching bib entry for publication: {pid}")
        errors.append(
            f"publications/bib mismatch: {len(missing)} of {len(pubs)} "
            "publications have no BibTeX entry in yue-zhao.bib"
        )


def check_bib_viewer_compat(errors: list[str], warnings: list[str]) -> None:
    text = read_text(ROOT / "bib-viewer.html", errors)
    if not text:
        return
    required = [
        "getQueryParam('id')",
        "getQueryParam('title')",
        "data/publications.json",
        "files/yue-zhao.bib",
    ]
    for needle in required:
        if needle not in text:
            warnings.append(f"bib-viewer.html missing logic marker: {needle}")


def main() -> None:
    errors: list[str] = []
    warnings: list[str] = []

    check_required_files(errors)
    check_json_files(errors)
    check_page_smoke(errors, warnings)
    check_local_refs(errors)
    check_bib_viewer_compat(errors, warnings)
    check_bib_coverage(errors, warnings)
    check_utf8_bom(errors)
    check_public_urls(errors, warnings)

    if errors:
        fail(errors)
    print_warnings(warnings)
    print("All site checks passed.")


if __name__ == "__main__":
    main()
