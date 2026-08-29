#!/usr/bin/env python3
"""Inject crawlable publication and lab-member fallbacks into static pages."""

from __future__ import annotations

import html
import json
import math
import os
import re
import subprocess
import tempfile
import textwrap
from collections.abc import Iterable, Mapping
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
PUBLICATIONS_PATH = ROOT / "data" / "publications.json"
LAB_MEMBERS_PATH = ROOT / "data" / "lab-members.json"
LAB_CURRENT_PHD_PATH = ROOT / "data" / "lab-current-phd.json"
PUBLICATIONS_PAGE = ROOT / "publications.html"
LAB_PAGE = ROOT / "lab.html"
INDEX_PAGE = ROOT / "index.html"
BIO_PATH = ROOT / "files" / "bio.txt"

PUBLICATION_FIELDS = ("title", "authors", "venue", "year")
# paper_url is optional: a paper can be accepted before any public link exists.
VENUE_DATE_RULES = (
    (re.compile(r"neurips|mti-llm|responsiblefm", re.IGNORECASE), 12, 1),
    (
        re.compile(
            r"emnlp|ijcnlp-aacl|sigspatial|spatialconnect|icdm", re.IGNORECASE
        ),
        11,
        1,
    ),
    (re.compile(r"iccv|colm", re.IGNORECASE), 10, 1),
    (re.compile(r"ecml pkdd", re.IGNORECASE), 9, 1),
    (
        re.compile(
            r"\bacl\b|association for computational linguistics|kdd|acm bcb",
            re.IGNORECASE,
        ),
        8,
        1,
    ),
    (re.compile(r"icml|dataworld", re.IGNORECASE), 7, 1),
    (re.compile(r"cvpr", re.IGNORECASE), 6, 1),
    (re.compile(r"www|web conference|naacl", re.IGNORECASE), 5, 1),
    (re.compile(r"iclr|eacl", re.IGNORECASE), 4, 1),
    (re.compile(r"aaai", re.IGNORECASE), 2, 1),
)


def load_json_list(path: Path) -> list[dict[str, Any]]:
    """Read a JSON array and reject malformed records before touching HTML."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a JSON array")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError(f"{path.relative_to(ROOT)} must contain only JSON objects")
    return data


def escaped(value: Any) -> str:
    """Escape text or an attribute value for HTML."""
    if value is None:
        return ""
    return html.escape(str(value), quote=True)


def require_text(item: Mapping[str, Any], field: str, source: str) -> str:
    """Return a required non-empty field with a useful validation error."""
    value = item.get(field)
    if value is None or not str(value).strip():
        label = item.get("id") or item.get("name") or "unknown record"
        raise ValueError(f"{source}: {label!r} is missing {field!r}")
    return str(value).strip()


def publication_year(item: Mapping[str, Any]) -> int | None:
    """Match the browser renderer's explicit-year and venue-year parsing."""
    year = item.get("year")
    if (
        isinstance(year, (int, float))
        and not isinstance(year, bool)
        and math.isfinite(year)
    ):
        return int(year)

    match = re.search(r"\b(?:19|20)\d{2}\b", str(item.get("venue") or ""))
    return int(match.group(0)) if match else None


def publication_sort_date(item: Mapping[str, Any]) -> int:
    """Match the client-side publication recency rules."""
    raw = str(item.get("sort_date") or "").strip().replace("-", "")
    if re.fullmatch(r"\d{8}", raw):
        return int(raw)

    year = publication_year(item)
    if year is None:
        return -1

    venue = str(item.get("venue") or "")
    for pattern, month, day in VENUE_DATE_RULES:
        if pattern.search(venue):
            return (year * 10_000) + (month * 100) + day
    return year * 10_000


def publication_sort_priority(item: Mapping[str, Any]) -> float:
    value = item.get("sort_priority")
    if (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(value)
    ):
        return float(value)
    return 0


def sort_publications(items: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return the same stable recency order used by publications.html."""
    return sorted(
        items,
        key=lambda item: (
            publication_sort_date(item),
            publication_sort_priority(item),
            publication_year(item) or 0,
        ),
        reverse=True,
    )


def arxiv_sort_key(item: Mapping[str, Any]) -> str:
    match = re.search(r"arxiv\.org/abs/(\d{4}\.\d+)", str(item.get("paper_url") or ""))
    return match.group(1) if match else "0000.00000"


def format_authors(authors: str) -> str:
    """Preserve the author symbols and self-highlighting used in the browser."""
    value = escaped(authors)
    value = value.replace("†", "<sup>&dagger;</sup>")
    value = value.replace("♠", "<sup>&spades;</sup>")
    return re.sub(r"\bYue Zhao\b", '<span class="author-self">Yue Zhao</span>', value)


def format_venue_and_year(venue: str, year: int | None) -> str:
    """Expose the year through a time element without repeating it visibly."""
    if year is None:
        return escaped(venue)

    year_text = str(year)
    time_html = (
        f'<time itemprop="datePublished" datetime="{year_text}">{year_text}</time>'
    )
    if year_text in venue:
        before, after = venue.split(year_text, 1)
        return escaped(before) + time_html + escaped(after)
    return f"{escaped(venue)} ({time_html})"


def render_publication(item: Mapping[str, Any]) -> str:
    """Render one crawlable ScholarlyArticle list item."""
    for field in PUBLICATION_FIELDS:
        require_text(item, field, "data/publications.json")

    publication_id = escaped(item.get("id") or item["title"])
    title = escaped(item["title"])
    paper_url = escaped(str(item.get("paper_url") or ""))
    authors = format_authors(str(item["authors"]))
    venue = format_venue_and_year(str(item["venue"]), publication_year(item))

    return "\n".join(
        (
            f'<li class="prerendered-publication" data-publication-id="{publication_id}" '
            'itemscope itemtype="https://schema.org/ScholarlyArticle">',
            (
                f'    <strong><a itemprop="url" href="{paper_url}">'
                f'<span itemprop="name">{title}</span></a></strong>.<br>'
                if paper_url
                else f'    <strong><span itemprop="name">{title}</span></strong>.<br>'
            ),
            f'    <span itemprop="author">{authors}</span><br>',
            f'    <span itemprop="isPartOf">{venue}</span>',
            "</li>",
        )
    )


def render_publication_items(items: Iterable[Mapping[str, Any]]) -> str:
    return "\n".join(render_publication(item) for item in items)


def render_preprint_groups(items: Iterable[dict[str, Any]]) -> str:
    groups: dict[int, list[dict[str, Any]]] = {}
    for item in items:
        groups.setdefault(publication_year(item) or 0, []).append(item)

    blocks: list[str] = []
    for year in sorted(groups, reverse=True):
        entries = textwrap.indent(render_publication_items(groups[year]), "    ")
        blocks.extend((f"<h5>{year}</h5>", '<ul class="vert">', entries, "</ul>"))
    return "\n".join(blocks)


def publication_regions(
    items: list[dict[str, Any]], current_year: int
) -> dict[str, str]:
    """Split publications into the six containers replaced by browser JavaScript."""
    visible = [item for item in items if item.get("show_on_website") is not False]
    preprints = sorted(
        (item for item in visible if item.get("section") == "preprint"),
        key=arxiv_sort_key,
        reverse=True,
    )
    conferences = sort_publications(
        item
        for item in visible
        if item.get("section") in {"conference", "workshop"}
    )
    journals = sort_publications(
        item for item in visible if item.get("section") == "journal"
    )

    def split_recent(
        records: Iterable[dict[str, Any]],
    ) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
        recent: list[dict[str, Any]] = []
        older: list[dict[str, Any]] = []
        for item in records:
            year = publication_year(item)
            destination = older if year is not None and year < current_year else recent
            destination.append(item)
        return recent, older

    preprint_recent, preprint_older = split_recent(preprints)
    conference_recent, conference_older = split_recent(conferences)
    journal_recent, journal_older = split_recent(journals)

    return {
        "publications-preprint-recent": render_preprint_groups(preprint_recent),
        "publications-preprint-older": render_preprint_groups(preprint_older),
        "publications-conference-recent": render_publication_items(conference_recent),
        "publications-conference-older": render_publication_items(conference_older),
        "publications-journal-recent": render_publication_items(journal_recent),
        "publications-journal-older": render_publication_items(journal_older),
    }


def member_last_name_key(member: Mapping[str, Any]) -> tuple[str, str]:
    name = str(member.get("name") or "")
    clean = re.sub(r"\([^)]*\)", "", name).strip()
    parts = clean.split()
    last_name = parts[-1].casefold() if parts else ""
    return last_name, name.casefold()


def sorted_members(items: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(items, key=member_last_name_key)


def render_awards(member: Mapping[str, Any]) -> str:
    awards = member.get("awards")
    if not isinstance(awards, list) or not awards:
        return ""
    return (
        '<p><i class="fas fa-award" style="font-size:18px; color:#990000"></i> '
        f"{escaped(', '.join(str(award) for award in awards))}</p>"
    )


def render_member_publications(member: Mapping[str, Any]) -> str:
    publications = member.get("publications")
    if not isinstance(publications, list) or not publications:
        return ""
    lines = [
        f'<span style="color:#555;">📄 <i>{escaped(publication)}</i></span>'
        for publication in publications
    ]
    return (
        '<div style="margin-top:10px;"><em style="color:#444;">'
        "Publications with us:</em><br>"
        + "<br>".join(lines)
        + "</div>"
    )


def render_current_phd_member(member: Mapping[str, Any]) -> str:
    name = require_text(member, "name", "data/lab-current-phd.json")
    profile_url = require_text(member, "profile_url", "data/lab-current-phd.json")
    image = require_text(member, "image", "data/lab-current-phd.json")
    alt = escaped(member.get("alt") or name)
    role = str(member.get("status_label") or "Ph.D. Student")
    email = str(member.get("email") or "").strip()
    email_html = f' (<span itemprop="email">{escaped(email)}</span>)' if email else ""

    co_advisors = member.get("co_advised_by") or []
    if isinstance(co_advisors, Mapping):
        co_advisors = [co_advisors]
    if not isinstance(co_advisors, list):
        raise ValueError(f"data/lab-current-phd.json: invalid co_advised_by for {name!r}")

    advisor_links: list[str] = []
    for advisor in co_advisors:
        if not isinstance(advisor, Mapping):
            raise ValueError(f"data/lab-current-phd.json: invalid co-advisor for {name!r}")
        advisor_name = require_text(advisor, "name", "data/lab-current-phd.json")
        if advisor.get("url"):
            advisor_links.append(
                f'<a href="{escaped(advisor["url"])}">{escaped(advisor_name)}</a>'
            )
        else:
            advisor_links.append(escaped(advisor_name))
    co_advised_html = (
        f'<p class="member-status">co-advised by {" and ".join(advisor_links)}</p>'
        if advisor_links
        else ""
    )

    lines = [
        '<div class="col-md-4 col-sm-6 team-member prerendered-member" '
        'itemscope itemtype="https://schema.org/Person">',
        (
            f'    <img itemprop="image" src="{escaped(image)}" alt="{alt}" '
            'class="team-img" width="150" height="150" loading="lazy" '
            'decoding="async" fetchpriority="low">'
        ),
        (
            f'    <h3><a itemprop="url" href="{escaped(profile_url)}">'
            f'<span itemprop="name">{escaped(name)}</span></a></h3>'
        ),
        f'    <p>{escaped(member.get("year_info"))}</p>',
        f'    <p>{escaped(member.get("research"))}</p>',
    ]
    awards = render_awards(member)
    if awards:
        lines.append(f"    {awards}")
    lines.append(
        '    <p class="member-status"><strong><span itemprop="jobTitle">'
        f"{escaped(role)}</span></strong>{email_html}</p>"
    )
    if co_advised_html:
        lines.append(f"    {co_advised_html}")
    lines.append("</div>")
    return "\n".join(lines)


def render_current_member(member: Mapping[str, Any]) -> str:
    name = require_text(member, "name", "data/lab-members.json")
    profile_url = require_text(member, "profile_url", "data/lab-members.json")
    image = require_text(member, "image", "data/lab-members.json")
    alt = escaped(member.get("alt") or name)
    role = require_text(member, "status_text", "data/lab-members.json")
    email = require_text(member, "email", "data/lab-members.json")

    lines = [
        '<div class="col-md-4 col-sm-6 team-member prerendered-member" '
        'itemscope itemtype="https://schema.org/Person">',
        (
            f'    <img itemprop="image" src="{escaped(image)}" alt="{alt}" '
            'class="team-img" width="150" height="150" loading="lazy" '
            'decoding="async" fetchpriority="low">'
        ),
        (
            f'    <h3><a itemprop="url" href="{escaped(profile_url)}">'
            f'<span itemprop="name">{escaped(name)}</span></a></h3>'
        ),
        f'    <p>{escaped(member.get("research"))}</p>',
        '    <p class="member-status"><span itemprop="jobTitle">'
        f'{escaped(role)}</span> (<span itemprop="email">{escaped(email)}</span>)</p>',
    ]
    awards = render_awards(member)
    if awards:
        lines.append(f"    {awards}")
    publications = render_member_publications(member)
    if publications:
        lines.append(f"    {publications}")
    lines.append("</div>")
    return "\n".join(lines)


def render_past_member(member: Mapping[str, Any]) -> str:
    name = require_text(member, "name", "data/lab-members.json")
    profile_url = require_text(member, "profile_url", "data/lab-members.json")
    role = require_text(member, "status_text", "data/lab-members.json")
    email = require_text(member, "email", "data/lab-members.json")
    publications = render_member_publications(member)

    lines = [
        '<div class="col-md-6 prerendered-member" style="margin-bottom:20px;" '
        'itemscope itemtype="https://schema.org/Person">',
        '    <div style="border:1px solid #ddd; border-radius:10px; padding:15px; height:100%;">',
        (
            f'        <strong><a itemprop="url" href="{escaped(profile_url)}">'
            f'<span itemprop="name">{escaped(name)}</span></a></strong> '
            f'(<span itemprop="jobTitle">{escaped(role)}</span>)<br>'
        ),
        f'        <small>📧 <span itemprop="email">{escaped(email)}</span></small>',
    ]
    if publications:
        lines.extend(("        <br><br>", f"        {publications}"))
    lines.extend(("    </div>", "</div>"))
    return "\n".join(lines)


def lab_regions(
    current_phd: list[dict[str, Any]], members: list[dict[str, Any]]
) -> dict[str, str]:
    current = sorted_members(item for item in members if item.get("group") == "current")
    past = sorted_members(item for item in members if item.get("group") == "past")
    unknown_groups = sorted(
        {str(item.get("group")) for item in members if item.get("group") not in {"current", "past"}}
    )
    if unknown_groups:
        raise ValueError(f"data/lab-members.json: unknown groups: {', '.join(unknown_groups)}")

    return {
        "lab-current-phd": "\n".join(
            render_current_phd_member(item) for item in sorted_members(current_phd)
        ),
        "lab-current": "\n".join(render_current_member(item) for item in current),
        "lab-past": "\n".join(render_past_member(item) for item in past),
    }


def inject_region(source: str, marker_name: str, rendered: str, page: Path) -> str:
    """Replace one marker region, preserving the marker indentation."""
    start_marker = f"<!-- PRERENDER:{marker_name} START -->"
    end_marker = f"<!-- PRERENDER:{marker_name} END -->"
    if source.count(start_marker) != 1 or source.count(end_marker) != 1:
        raise ValueError(
            f"{page.relative_to(ROOT)} must contain exactly one {marker_name!r} marker pair"
        )

    start = source.index(start_marker)
    content_start = start + len(start_marker)
    end = source.index(end_marker, content_start)
    line_start = source.rfind("\n", 0, start) + 1
    indentation = source[line_start:start]
    if indentation.strip():
        raise ValueError(
            f"{page.relative_to(ROOT)}: {marker_name!r} START marker must be on its own line"
        )

    body = textwrap.indent(rendered.rstrip(), indentation) if rendered.strip() else ""
    replacement = f"\n{body}\n{indentation}"
    return source[:content_start] + replacement + source[end:]


def render_page(page: Path, regions: Mapping[str, str]) -> tuple[str, bool]:
    source = page.read_text(encoding="utf-8")
    rendered = source
    for marker_name, content in regions.items():
        rendered = inject_region(rendered, marker_name, content, page)
    return rendered, rendered != source


def bio_regions(bio_path: Path) -> dict[str, str]:
    """Render files/bio.txt into the homepage biography block.

    bio.txt stays the single source of truth. It is also linked from the sidebar
    as a plain-text "Short Bio" that a conference organizer can copy, so it is a
    deliverable in its own right and is not folded into the HTML. Generating the
    homepage copy from it keeps the two from drifting apart.
    """
    paragraphs = [
        line.strip()
        for line in bio_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if not paragraphs:
        raise ValueError(f"{bio_path.relative_to(ROOT)}: no paragraphs found")

    indent = " " * 24
    rendered = [
        f'{indent}<details class="smart-details" style="margin:16px 0 14px 0;">',
        f'{indent}  <summary><h3 style="display:inline; color:#990000; font-size:1rem; font-weight:700; line-height:inherit; margin:0;">Biography</h3></summary>',
    ]
    for paragraph in paragraphs:
        escaped = html.escape(paragraph, quote=False)
        rendered.append(f"{indent}  <p>{escaped}</p>")
    rendered.append(f"{indent}</details>")
    return {"bio": "\n".join(rendered)}


SITEMAP_PATH = ROOT / "sitemap.xml"
SITE_BASE = "https://viterbi-web.usc.edu/~yzhao010/"


def _git_last_modified(relative_path: str) -> str | None:
    """Return the last commit date for a file as YYYY-MM-DD, or None."""
    try:
        result = subprocess.run(
            ["git", "-C", str(ROOT), "log", "-1", "--format=%cs", "--", relative_path],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return None
    value = result.stdout.strip()
    return value if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value) else None


def refresh_sitemap() -> bool:
    """Set each sitemap ``lastmod`` to the real git date of the page it points at.

    A sitemap that reports a stale ``lastmod`` tells crawlers a page has not
    changed, so a rewritten page can go unrecrawled indefinitely. Dates come from
    git rather than the filesystem because a fresh checkout resets mtimes.

    Entries whose date cannot be determined, which is what happens in a shallow
    clone, keep their existing value rather than being cleared.
    """
    original = SITEMAP_PATH.read_text(encoding="utf-8")
    updated = original
    unresolved: list[str] = []

    for loc, lastmod in re.findall(
        r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", original
    ):
        if not loc.startswith(SITE_BASE):
            continue
        relative = loc[len(SITE_BASE):] or "index.html"
        if not (ROOT / relative).exists():
            unresolved.append(relative)
            continue
        actual = _git_last_modified(relative)
        if actual is None:
            unresolved.append(relative)
            continue
        if actual != lastmod:
            updated = updated.replace(
                f"<loc>{loc}</loc>\n    <lastmod>{lastmod}</lastmod>",
                f"<loc>{loc}</loc>\n    <lastmod>{actual}</lastmod>",
            )

    if unresolved:
        print(f"  sitemap: kept existing dates for {len(unresolved)} entries")
    if updated != original:
        _atomic_write(SITEMAP_PATH, updated)
        return True
    return False


def _atomic_write(page: Path, rendered: str) -> None:
    """Replace ``page`` with ``rendered`` atomically.

    A direct write can truncate the page if the process is interrupted, and a
    failure on the second page would leave the two generated pages rendered from
    different source states. Writing to a temporary file in the same directory
    and then calling ``os.replace`` makes each page swap all-or-nothing.
    """
    handle = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=page.parent,
        prefix=f".{page.name}.",
        suffix=".tmp",
        delete=False,
    )
    try:
        with handle as tmp:
            tmp.write(rendered)
            tmp.flush()
            os.fsync(tmp.fileno())
        os.replace(handle.name, page)
    except BaseException:
        Path(handle.name).unlink(missing_ok=True)
        raise


def main() -> None:
    publications = load_json_list(PUBLICATIONS_PATH)
    lab_members = load_json_list(LAB_MEMBERS_PATH)
    lab_current_phd = load_json_list(LAB_CURRENT_PHD_PATH)

    pages = {
        PUBLICATIONS_PAGE: publication_regions(publications, date.today().year),
        LAB_PAGE: lab_regions(lab_current_phd, lab_members),
        INDEX_PAGE: bio_regions(BIO_PATH),
    }
    rendered_pages = {
        page: render_page(page, regions) for page, regions in pages.items()
    }

    for page, (rendered, changed) in rendered_pages.items():
        if changed:
            _atomic_write(page, rendered)
        state = "Updated" if changed else "Unchanged"
        print(f"{state} {page.relative_to(ROOT)} ({len(pages[page])} regions)")

    sitemap_changed = refresh_sitemap()
    print(f"{'Updated' if sitemap_changed else 'Unchanged'} sitemap.xml")

    visible_publications = sum(
        item.get("show_on_website") is not False for item in publications
    )
    print(
        f"Rendered {visible_publications} publications and "
        f"{len(lab_current_phd) + len(lab_members)} lab members"
    )


if __name__ == "__main__":
    main()
