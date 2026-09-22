#!/usr/bin/env python3
"""Lightweight CI checks for the static site."""

from __future__ import annotations

import html
import json
import os
import re
import subprocess
import time
import sys
import textwrap
from html.parser import HTMLParser
from datetime import datetime
import xml.etree.ElementTree as ET
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
        "fortis-benchmark.html",
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


def check_json_files(errors: list[str], warnings: list[str]) -> None:
    data_dir = ROOT / "data"
    object_json = {"citations.json"}

    # Parse each file once; store results for per-file field checks below.
    parsed: dict[str, list | dict | None] = {}
    for path in sorted(data_dir.glob("*.json")):
        before = len(errors)
        obj = load_json(path, errors)
        if obj is None:
            # load_json returns None both for a parse failure and for a file
            # holding a literal null. Only the first case reported an error, so
            # a data file that parsed to null would otherwise pass silently.
            if len(errors) == before:
                errors.append(f"Top-level JSON null in {path.as_posix()}")
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

    # --- citations.json field checks ---
    # The file is pushed by meta-finder's update-citations workflow and joins to
    # publications.json on id. A stale id means the two repos have drifted. That
    # clears only after meta-finder's weekly profile-sync picks up the new
    # publication list and a later update-citations run republishes, so it warns
    # rather than fails.
    citations = parsed.get("citations.json")
    if isinstance(citations, dict):
        papers = citations.get("papers")
        if not isinstance(papers, list) or not papers:
            errors.append("citations.json missing a non-empty papers array")
        else:
            unknown: list[str] = []
            for idx, item in enumerate(papers):
                if not isinstance(item, dict):
                    errors.append(f"citations.json paper #{idx} is not an object")
                    continue
                raw_id = item.get("id")
                cid = raw_id.strip() if isinstance(raw_id, str) else ""
                if not cid:
                    errors.append(f"citations.json paper #{idx} missing non-empty id")
                elif isinstance(publications, list) and cid not in ids:
                    unknown.append(cid)
            if unknown:
                warnings.append(
                    f"citations.json has {len(unknown)} id(s) absent from "
                    f"publications.json (e.g. {', '.join(unknown[:3])}); "
                    "check meta-finder profile-sync and update-citations "
                    "if this persists"
                )

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
        ROOT / "fortis-benchmark.html",
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
    # Skip directories that are not part of the published site:
    # - `news-snapshots/`: out-of-band evidence captures (Chrome "Save Page As Webpage,
    #   Complete") used as durable citation backups for volatile external pages such as
    #   the OpenAI #8g careers listing; the companion `_files/` directories are
    #   deliberately excluded from the repo (too large, vendor-specific cache), so the
    #   saved HTML references many local assets that do not exist in the working tree
    #   by design.
    # - `out/`: gitignored LaTeX / local-build output (CV PDF intermediates, agent
    #   scratch directories). Not present in CI but may exist in dev clones.
    # .cache contains ignored third-party review captures, not website HTML.
    skip_top_level = {"news-snapshots", "out", ".cache"}
    # `skills/news-search/scratch/` is the gitignored working directory where a news-search
    # worker parks pages it downloaded in order to scan them. Those captures reference the
    # origin site's own assets, which are absent here by design, so scanning them reports
    # failures against pages that were never part of this site. Matched as an exact prefix
    # rather than as any path component named `scratch`, so a real published directory such
    # as `docs/scratch/` is still checked.
    skip_prefixes = {("skills", "news-search", "scratch")}

    def _skip(rel_parts: tuple[str, ...]) -> bool:
        if rel_parts and rel_parts[0] in skip_top_level:
            return True
        return any(rel_parts[: len(p)] == p for p in skip_prefixes)

    html_files = sorted(
        h for h in ROOT.rglob("*.html")
        if not _skip(h.relative_to(ROOT).parts)
    )
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


def check_impact_claims_agree(errors: list[str], warnings: list[str]) -> None:
    """Keep the impact numbers identical across every surface that quotes them.

    A news-search round writes new evidence into `news-coverage-audit.md`, and the
    same facts are then quoted on several public surfaces. Those copies drift: the
    patent count read 12 in the audit and 15 on the site at the same time, and the
    bio's geography list stayed at "Europe, Asia, and the Middle East" for a round
    after Brazil was already counted. Prose instructions did not prevent either, so
    the invariant is enforced here instead.

    Add a row to CLAIMS whenever a new figure starts appearing on more than one
    surface. `news-coverage-audit.md` is the source of truth for every one of them.
    """
    audit_path = ROOT / "news-coverage-audit.md"
    if not audit_path.exists():
        warnings.append("news-coverage-audit.md missing; impact-claim agreement not checked")
        return
    audit = audit_path.read_text(encoding="utf-8", errors="replace")

    # (label, regex over the audit that yields the authoritative number,
    #  {surface path: regex whose first group must equal that number})
    CLAIMS = [
        (
            "patent count",
            r"- \*\*(\d+) patents\*\*",
            {
                "opensource.html": r"(\d+) patents cite PyOD",
                "files/bio.txt": r"cited in (\d+) patents",
                "index.html": r"cited in (\d+) patents",
                "llms.txt": r"\*\*Patents\*\*: (\d+) patents cite",
            },
        ),
    ]

    for label, audit_re, surfaces in CLAIMS:
        m = re.search(audit_re, audit)
        if not m:
            warnings.append(f"{label}: no authoritative figure found in news-coverage-audit.md")
            continue
        truth = m.group(1)
        for rel, surface_re in surfaces.items():
            path = ROOT / rel
            if not path.exists():
                errors.append(f"{label}: {rel} is missing")
                continue
            sm = re.search(surface_re, path.read_text(encoding="utf-8", errors="replace"))
            if not sm:
                errors.append(
                    f"{label}: {rel} no longer states the figure "
                    f"(pattern {surface_re!r} did not match). The audit says {truth}."
                )
            elif sm.group(1) != truth:
                errors.append(
                    f"{label}: {rel} says {sm.group(1)} but news-coverage-audit.md says {truth}. "
                    "The audit is the source of truth; update the surface."
                )

def check_bio_prerender_agrees(errors: list[str], warnings: list[str]) -> None:
    """The prerendered biography on index.html must match files/bio.txt paragraph for paragraph.

    Two surfaces carry the same three paragraphs and both are updated by hand. Nothing checked that
    they agreed, so a propagation miss shipped silently: on 2026-08-30 an edit landed in bio.txt
    alone and every gate still passed. Compare on text, after stripping tags and resolving entities,
    so markup and escaping differences do not register as drift.
    """
    bio_path = ROOT / "files" / "bio.txt"
    index_path = ROOT / "index.html"
    if not bio_path.exists() or not index_path.exists():
        warnings.append("bio prerender agreement not checked; a source file is missing")
        return

    index = index_path.read_text(encoding="utf-8", errors="replace")
    block = re.search(r"PRERENDER:bio START(.*?)PRERENDER:bio END", index, re.S)
    if not block:
        errors.append("index.html no longer carries the PRERENDER:bio markers; bio agreement unchecked")
        return

    def flatten(text: str) -> str:
        return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", text))).strip()

    bodies = re.findall(r"<p>(.*?)</p>", block.group(1), re.S)

    # Stripping tags and comparing the remaining text treats every element as if it were
    # semantically neutral, which is false in both directions: <span hidden>x</span> contributes
    # text the browser never shows, and <del>x</del> reads as deleted while comparing equal to
    # unmodified prose. Either would let the rendered biography diverge from bio.txt while this
    # check passed. The biography is plain prose in both surfaces, so the sound rule is to admit no
    # inline markup at all. If a link or emphasis is ever wanted here, allowlist that tag
    # deliberately and decide what its text contributes, rather than reinstating "all tags are
    # invisible". HTML comments carry no rendered text and stay permitted.
    for i, body in enumerate(bodies, start=1):
        stray = re.findall(r"<(?!!--)[^>]+>", body)
        if stray:
            errors.append(
                f"bio paragraph {i} in the index.html prerender contains inline markup "
                f"{stray[:3]}, which files/bio.txt cannot express. Keep the prerendered "
                "biography as plain text, or allowlist the tag in check_bio_prerender_agrees."
            )
    if errors:
        return

    rendered = [flatten(b) for b in bodies]
    source = [flatten(line) for line in bio_path.read_text(encoding="utf-8").splitlines() if line.strip()]

    if len(rendered) != len(source):
        errors.append(
            f"bio prerender has {len(rendered)} paragraphs but files/bio.txt has {len(source)}; "
            "update index.html to match bio.txt"
        )
        return

    for i, (want, got) in enumerate(zip(source, rendered), start=1):
        if want != got:
            at = next((j for j, (a, b) in enumerate(zip(want, got)) if a != b), min(len(want), len(got)))
            errors.append(
                f"bio paragraph {i} differs between files/bio.txt and the index.html prerender "
                f"at character {at}: bio.txt has {want[at:at + 60]!r}, index.html has {got[at:at + 60]!r}. "
                "bio.txt is the source; update the prerender."
            )


class SearchMetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self.meta = {}
        self.canonicals = []
        self.schemas = []
        self._in_title = False
        self._in_schema = False
        self._schema = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self._in_title = True
        if tag == "meta":
            self.meta[attrs.get("name", attrs.get("property"))] = attrs.get("content", "")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href"))
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self._in_schema = True
            self._schema = ""

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_schema:
            self._schema += data

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag == "script" and self._in_schema:
            self.schemas.append(json.loads(self._schema))
            self._in_schema = False


def check_search_metadata(errors: list[str]) -> None:
    """Validate public search entry points and their static identity/navigation."""
    base = "https://viterbi-web.usc.edu/~yzhao010/"
    core_pages = {"index.html", "lab.html", "publications.html"}
    try:
        sitemap = ET.parse(ROOT / "sitemap.xml")
    except (OSError, ET.ParseError) as exc:
        errors.append(f"Invalid sitemap.xml: {exc}")
        return
    locations = [n.text or "" for n in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    if not locations or len(locations) != len(set(locations)):
        errors.append("Sitemap must contain unique canonical URLs")
    titles, descriptions, parsed_pages = {}, {}, {}
    for url in locations:
        if not url.startswith(base) or "?" in url or "#" in url:
            errors.append(f"Sitemap URL is not a canonical USC page: {url}")
            continue
        relative = url[len(base):] or "index.html"
        path = (ROOT / relative).resolve()
        if not path.is_relative_to(ROOT) or path.suffix != ".html" or not path.is_file():
            errors.append(f"Sitemap target is not a local HTML page: {url}")
            continue
        source = read_text(path, errors)
        parser = SearchMetadataParser()
        try:
            parser.feed(source)
        except (ValueError, TypeError) as exc:
            errors.append(f"{relative}: Invalid JSON-LD: {exc}")
            continue
        parsed_pages[relative] = parser
        if parser.canonicals != [url] or parser.meta.get("og:url") != url:
            errors.append(f"{relative}: Canonical and og:url must match its USC sitemap URL")
        for label, value, seen in (("title", parser.title.strip(), titles), ("description", parser.meta.get("description", "").strip(), descriptions)):
            if not value or value in seen:
                errors.append(f"{relative}: Missing or duplicate search {label}")
            seen[value] = relative
        directives = {d.strip().lower() for d in parser.meta.get("robots", "").split(",")}
        if directives & {"noindex", "none", "nofollow", "nosnippet"}:
            errors.append(f"{relative}: Sitemap page blocks indexing, links, or snippets")
        if relative in core_pages:
            for name in ("navbar", "sidebar", "footer"):
                block = re.search(rf"<!-- PRERENDER:layout-{name} START -->(.*?)<!-- PRERENDER:layout-{name} END -->", source, re.S)
                expected = (ROOT / "includes" / f"{name}.html").read_text(encoding="utf-8").strip()
                if not block or textwrap.dedent(block.group(1)).strip() != expected:
                    errors.append(f"{relative}: Missing or stale static {name}; run scripts/prerender_pages.py")
    for page in core_pages - parsed_pages.keys():
        errors.append(f"Core search entry point absent from sitemap: {page}")
    if not core_pages <= parsed_pages.keys():
        return
    schema_maps = {
        page: {s.get("@type"): s for s in parsed_pages[page].schemas if isinstance(s, dict)}
        for page in core_pages
    }
    person_id = base + "#person"
    profile = schema_maps["index.html"].get("ProfilePage", {})
    for field in ("dateCreated", "dateModified"):
        if field in profile:
            value = profile[field]
            try:
                valid_datetime = isinstance(value, str) and "T" in value and datetime.fromisoformat(value).tzinfo is not None
            except ValueError:
                valid_datetime = False
            if not valid_datetime:
                errors.append(f"index.html: Optional ProfilePage {field} needs an actual ISO datetime with timezone; omit if unknown")
    person = profile.get("mainEntity", {})
    if person.get("@id") != person_id or person.get("@type") != "Person" or person.get("name") != "Yue Zhao":
        errors.append("index.html: ProfilePage must identify Yue Zhao with the canonical Person ID")
    if person.get("image") != base + "images/rsz_300.jpg":
        errors.append("index.html: Person image must match the visible headshot")
    website = schema_maps["index.html"].get("WebSite", {})
    if website.get("publisher", {}).get("@id") != person_id:
        errors.append("index.html: WebSite publisher must reference the profile Person")
    for page, kind, field in (("lab.html", "ResearchOrganization", "member"), ("publications.html", "CollectionPage", "author")):
        if schema_maps[page].get(kind, {}).get(field, {}).get("@id") != person_id:
            errors.append(f"{page}: {kind} {field} must reference the same Person")


def main() -> None:
    errors: list[str] = []
    warnings: list[str] = []

    check_required_files(errors)
    check_json_files(errors, warnings)
    check_page_smoke(errors, warnings)
    check_local_refs(errors)
    check_bib_viewer_compat(errors, warnings)
    check_bib_coverage(errors, warnings)
    check_utf8_bom(errors)
    check_impact_claims_agree(errors, warnings)
    check_bio_prerender_agrees(errors, warnings)
    check_search_metadata(errors)
    check_public_urls(errors, warnings)

    if errors:
        fail(errors)
    print_warnings(warnings)
    print("All site checks passed.")


if __name__ == "__main__":
    main()
