"""
Citation Affiliation Audit via OpenAlex API (v3 — comprehensive, per-paper tracking)

Searches ALL papers from publications.json (excluding surveys), finds
their OpenAlex IDs, then queries citing papers for notable institution
affiliations. Tracks which of YOUR papers each citation refers to.
"""

import json
import re
import time
import urllib.request
import urllib.parse
import os

EMAIL = "yue.z@usc.edu"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

EXCLUDE_TITLES_CONTAINING = [
    "comprehensive survey",
    "a survey on",
    "a survey of",
]

# ── Institution patterns ──
# Use \b on BOTH sides for short acronyms to avoid substring false positives
TIER0_PATTERNS = [
    (r"European Space Agency|\bESA\b|ESOC|ESTEC", "Space Agency"),
    (r"NASA|Jet Propulsion Lab|\bJPL\b", "Space Agency"),
    (r"JAXA|Japan Aerospace", "Space Agency"),
    (r"\bISRO\b|Indian Space Research", "Space Agency"),
    (r"\bDLR\b|Deutsches Zentrum.*Luft", "Space Agency"),
    (r"\bCNES\b|Centre National d.Etudes Spatiales", "Space Agency"),
    (r"National Institute of Standards|\bNIST\b", "US Government"),
    (r"Department of Energy(?! Sci)(?!.*University)", "US Government"),
    (r"DARPA|Defense Advanced Research", "US Government"),
    (r"\bNOAA\b|National Oceanic", "US Government"),
    (r"National Institutes of Health|NIH Clinical Center", "US Government"),
    (r"Centers for Disease Control|\bCDC\b", "US Government"),
    (r"Food and Drug Admin|\bFDA\b", "US Government"),
    (r"Federal Aviation|\bFAA\b", "US Government"),
    (r"\bCISA\b|Cybersecurity.*Infrastructure", "US Government"),
    (r"Department of Homeland Security", "US Government"),
    (r"Federal Reserve|Board of Governors", "Central Bank"),
    (r"European Central Bank|\bECB\b", "Central Bank"),
    (r"\bBank for International Settlements\b", "Central Bank"),
    (r"Bundesbank", "Central Bank"),
    (r"Bank of England", "Central Bank"),
    (r"Bank of Japan", "Central Bank"),
    (r"People.s Bank of China|\bPBOC\b", "Central Bank"),
    (r"Los Alamos|LANL\b", "National Lab"),
    (r"Lawrence Livermore|\bLLNL\b", "National Lab"),
    (r"Sandia National", "National Lab"),
    (r"Oak Ridge|\bORNL\b", "National Lab"),
    (r"Argonne National", "National Lab"),
    (r"Brookhaven National", "National Lab"),
    (r"Pacific Northwest|\bPNNL\b", "National Lab"),
    (r"Idaho National|\bINL\b", "National Lab"),
    (r"Fermilab|Fermi National", "National Lab"),
    (r"SLAC National", "National Lab"),
    (r"\bCERN\b", "International Lab"),
    (r"\bDESY\b|Elektronen-Synchrotron", "International Lab"),
    (r"Max Planck", "Research Institute"),
    (r"Fraunhofer", "Research Institute"),
    (r"\bOpenAI\b", "Foundation Model Co"),
    (r"Anthropic", "Foundation Model Co"),
    (r"DeepMind|Google DeepMind", "Foundation Model Co"),
    (r"Meta\s*(AI|FAIR|Platforms)", "Foundation Model Co"),
    (r"Raytheon", "Defense"),
    (r"Lockheed Martin", "Defense"),
    (r"Northrop Grumman", "Defense"),
    (r"BAE Systems", "Defense"),
    (r"\bMITRE\b", "Defense/Research"),
    (r"RAND Corporation", "Defense/Research"),
    (r"Booz Allen", "Defense"),
    (r"Leidos", "Defense"),
    (r"World Health Organization", "International Org"),
    (r"\bIAEA\b|International Atomic Energy", "International Org"),
    (r"\bWorld Bank\b", "International Org"),
    (r"\bOECD\b", "International Org"),
    (r"\bNATO\b", "International Org"),
]

TIER1_PATTERNS = [
    (r"Google\b(?!.*DeepMind)", "Big Tech"),
    (r"Microsoft\b", "Big Tech"),
    (r"Amazon\b", "Big Tech"),
    (r"Apple\b(?!.*University)", "Big Tech"),
    (r"NVIDIA|Nvidia\b", "Big Tech"),
    (r"\bIntel\b(?!.*ligence)", "Big Tech"),
    (r"\bIBM\b", "Big Tech"),
    (r"Salesforce", "Big Tech"),
    (r"\bAdobe\b", "Big Tech"),
    (r"Samsung\b", "Big Tech"),
    (r"Huawei\b", "Big Tech"),
    (r"Tencent\b", "Big Tech"),
    (r"Alibaba\b", "Big Tech"),
    (r"Baidu\b", "Big Tech"),
    (r"ByteDance", "Big Tech"),
    (r"Goldman Sachs", "Finance"),
    (r"JPMorgan|J\.P\. Morgan", "Finance"),
    (r"Morgan Stanley", "Finance"),
    (r"Citadel\b", "Finance"),
    (r"Two Sigma", "Finance"),
    (r"BlackRock", "Finance"),
    (r"Bloomberg\b(?!.*University)", "Finance"),
    (r"Capital One", "Finance"),
    (r"Wells Fargo", "Finance"),
    (r"\bVisa\b(?!.*University)", "Finance"),
    (r"Pfizer", "Pharma"),
    (r"\bRoche\b", "Pharma"),
    (r"Novartis", "Pharma"),
    (r"AstraZeneca", "Pharma"),
    (r"\bMerck\b", "Pharma"),
    (r"Eli Lilly", "Pharma"),
    (r"Sanofi", "Pharma"),
    (r"Moderna", "Pharma"),
    (r"Mayo Clinic", "Healthcare"),
    (r"Cleveland Clinic", "Healthcare"),
    (r"Siemens\b", "Industrial"),
    (r"\bBosch\b", "Industrial"),
    (r"Honeywell", "Industrial"),
    (r"\bGeneral Electric\b|\bGE Research\b|\bGE Global Research\b", "Industrial"),
    (r"Ericsson", "Telecom"),
    (r"\bNokia\b", "Telecom"),
    (r"\bCisco\b", "Telecom"),
    (r"Qualcomm", "Telecom"),
    (r"\bTesla\b", "Automotive"),
    (r"SpaceX", "Aerospace"),
    (r"\bWalmart\b", "Retail"),
    (r"Deloitte", "Consulting"),
    (r"McKinsey", "Consulting"),
    (r"\bPwC\b|PricewaterhouseCoopers", "Consulting"),
    (r"Accenture", "Consulting"),
]


def api_get(url):
    for attempt in range(5):
        try:
            req = urllib.request.Request(url)
            req.add_header("User-Agent", f"mailto:{EMAIL}")
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 3 * (attempt + 1)
                print(f"    Rate limited, waiting {wait}s...")
                time.sleep(wait)
            elif e.code == 404:
                return None  # Not found, don't retry
            else:
                print(f"    HTTP {e.code}")
                return None
        except Exception as e:
            print(f"    Error: {e}")
            time.sleep(2)
    return None


def load_papers():
    """Load papers from publications.json, skip surveys."""
    path = os.path.join(PROJECT_ROOT, "data", "publications.json")
    with open(path, encoding="utf-8") as f:
        pubs = json.load(f)

    papers = []
    for p in pubs:
        title = p.get("title", "")
        if any(exc in title.lower() for exc in EXCLUDE_TITLES_CONTAINING):
            print(f"  SKIP survey: {title[:60]}")
            continue
        papers.append({
            "title": title,
            "venue": p.get("venue", ""),
            "year": p.get("year"),
            "id": p.get("id", ""),
            "paper_url": p.get("paper_url", ""),
        })
    return papers


def find_openalex_id(title, paper_url=None):
    """Find OpenAlex work ID. Tries arXiv ID, DOI, then title search."""

    # Strategy 1: arXiv ID
    if paper_url and "arxiv.org" in paper_url:
        arxiv_match = re.search(r'(\d{4}\.\d{4,5})', paper_url)
        if arxiv_match:
            arxiv_id = arxiv_match.group(1)
            url = f"https://api.openalex.org/works/https://arxiv.org/abs/{arxiv_id}?select=id,title,cited_by_count"
            data = api_get(url)
            if data and data.get("id"):
                oa_id = data["id"].replace("https://openalex.org/", "")
                return oa_id, data.get("title", ""), data.get("cited_by_count", 0)
            time.sleep(0.1)

    # Strategy 2: DOI from URL
    if paper_url:
        doi_match = re.search(r'doi\.org/(.+)', paper_url)
        if doi_match:
            doi = doi_match.group(1)
            url = f"https://api.openalex.org/works/https://doi.org/{doi}?select=id,title,cited_by_count"
            data = api_get(url)
            if data and data.get("id"):
                oa_id = data["id"].replace("https://openalex.org/", "")
                return oa_id, data.get("title", ""), data.get("cited_by_count", 0)
            time.sleep(0.1)

    # Strategy 3: proceedings URLs often have DOI-like paths
    if paper_url and "proceedings" in paper_url:
        # Try NeurIPS, ICML, etc. proceedings DOI format
        if "neurips.cc" in paper_url or "mlr.press" in paper_url:
            pass  # Fall through to title search (no easy DOI extraction)

    # Strategy 4: Title search (fallback) — strict matching
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode({
        "search": title,
        "per_page": "5",
        "select": "id,title,cited_by_count,publication_year",
    })
    data = api_get(url)
    if not data or not data.get("results"):
        return None, None, 0

    def normalize_words(t):
        return set(re.findall(r'\w{3,}', t.lower()))

    def normalize_str(t):
        return re.sub(r'[^a-z0-9 ]', '', t.lower()).strip()

    title_words = normalize_words(title)
    title_norm = normalize_str(title)
    if not title_words:
        return None, None, 0

    # Extract the pre-colon prefix as the primary anchor (e.g., "PyOD", "TrustGen", "DecAlign")
    prefix_match = re.match(r'^([A-Za-z0-9\-]+)\s*:', title)
    prefix_anchor = prefix_match.group(1).lower() if prefix_match else None

    for w in data["results"]:
        found_title = w.get("title", "")
        found_norm = normalize_str(found_title)

        # Pass 1: Exact normalized title match
        if title_norm == found_norm:
            oa_id = w["id"].replace("https://openalex.org/", "")
            return oa_id, found_title, w.get("cited_by_count", 0)

    # Pass 2: Prefix anchor + high overlap
    for w in data["results"]:
        found_title = w.get("title", "")
        found_norm = normalize_str(found_title)
        found_words = normalize_words(found_title)
        if not found_words:
            continue

        overlap = len(title_words & found_words) / len(title_words)

        if prefix_anchor:
            # The prefix (e.g., "pyod", "trustgen") MUST appear in the found title
            if prefix_anchor not in found_norm:
                continue
            # With prefix match, accept at 50% word overlap
            if overlap >= 0.5:
                oa_id = w["id"].replace("https://openalex.org/", "")
                return oa_id, found_title, w.get("cited_by_count", 0)
        else:
            # No prefix anchor — require very high overlap (70%)
            if overlap >= 0.7:
                oa_id = w["id"].replace("https://openalex.org/", "")
                return oa_id, found_title, w.get("cited_by_count", 0)

    # Nothing passed
    if data["results"]:
        print(f"    No match passed verification: \"{data['results'][0].get('title', '')[:50]}\"")
    return None, None, 0


def get_citing_with_institutions(work_id, max_pages=50):
    """Get citing papers for a SINGLE work with institution data."""
    results = []
    cursor = "*"

    for page in range(max_pages):
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode({
            "filter": f"cites:{work_id}",
            "per_page": "200",
            "cursor": cursor,
            "select": "id,title,publication_year,authorships",
        })
        data = api_get(url)
        if not data or not data.get("results"):
            break

        for w in data["results"]:
            institutions = set()
            inst_details = []
            for authorship in w.get("authorships", []):
                for inst in authorship.get("institutions", []):
                    name = inst.get("display_name", "")
                    if name and name not in institutions:
                        institutions.add(name)
                        inst_details.append({
                            "name": name,
                            "type": inst.get("type", ""),
                            "country": inst.get("country_code", ""),
                        })
            if inst_details:
                citing_id = w.get("id", "").replace("https://openalex.org/", "")
                results.append({
                    "oa_id": citing_id,
                    "title": w.get("title", ""),
                    "year": w.get("publication_year"),
                    "institutions": inst_details,
                })

        meta = data.get("meta", {})
        cursor = meta.get("next_cursor")
        if not cursor or len(data["results"]) < 200:
            break
        time.sleep(0.15)

    return results


def match_patterns(inst_name, patterns):
    for pattern, category in patterns:
        if re.search(pattern, inst_name, re.IGNORECASE):
            return category, pattern
    return None, None


def main():
    print("Loading papers from publications.json...")
    papers = load_papers()
    print(f"  {len(papers)} papers (after excluding surveys)\n")

    # Phase 1: Find OpenAlex IDs
    print("=" * 60)
    print("PHASE 1: Finding OpenAlex IDs")
    print("=" * 60)

    found_works = {}  # oa_id -> short_name
    not_found = []
    zero_cite = []

    for i, p in enumerate(papers):
        title = p["title"]
        short = f"{title[:50]}... ({p['venue']})"
        print(f"  [{i+1}/{len(papers)}] {short}")

        oa_id, found_title, cite_count = find_openalex_id(title, paper_url=p.get("paper_url"))
        if oa_id and cite_count > 0:
            short_name = f"{title[:45]} ({p['venue'][:20]})"
            found_works[oa_id] = short_name
            print(f"    -> {oa_id} (cited_by={cite_count})")
        elif oa_id:
            zero_cite.append(short)
            print(f"    -> {oa_id} (0 citations, skipping)")
        else:
            not_found.append(short)
            print(f"    -> NOT FOUND")

        time.sleep(0.12)

    print(f"\nFound {len(found_works)} papers with citations")
    print(f"0 citations (indexed but no cites): {len(zero_cite)}")
    print(f"Not found on OpenAlex: {len(not_found)}")

    # Phase 2: Query citing papers PER WORK (to track which paper is cited)
    print("\n" + "=" * 60)
    print("PHASE 2: Fetching citing papers (per-work mode)")
    print("=" * 60)

    all_tier0 = []
    all_tier1 = []
    all_citing_ids = set()  # Track unique citing papers across all works

    for idx, (oa_id, short_name) in enumerate(found_works.items()):
        print(f"  [{idx+1}/{len(found_works)}] {short_name}")
        citing = get_citing_with_institutions(oa_id)
        for c in citing:
            if c.get("oa_id"):
                all_citing_ids.add(c["oa_id"])
        print(f"    -> {len(citing)} citing papers")

        for c in citing:
            for inst in c["institutions"]:
                cat, _ = match_patterns(inst["name"], TIER0_PATTERNS)
                if cat:
                    all_tier0.append({
                        "cited_work": short_name,
                        "citing_title": c["title"],
                        "year": c["year"],
                        "institution": inst["name"],
                        "country": inst["country"],
                        "category": cat,
                    })
                    print(f"    ** T0 [{cat}] {inst['name'][:40]}")
                    continue
                cat, _ = match_patterns(inst["name"], TIER1_PATTERNS)
                if cat:
                    all_tier1.append({
                        "cited_work": short_name,
                        "citing_title": c["title"],
                        "year": c["year"],
                        "institution": inst["name"],
                        "country": inst["country"],
                        "category": cat,
                    })

        time.sleep(0.5)

    # Deduplicate by (institution, citing_title, cited_work) to preserve multi-work attribution
    def dedup(entries):
        seen = set()
        out = []
        for e in entries:
            key = (e["institution"], e["citing_title"] or "", e["cited_work"])
            if key not in seen:
                seen.add(key)
                out.append(e)
        return out

    all_tier0 = dedup(all_tier0)
    all_tier1 = dedup(all_tier1)

    unique_citing = len(all_citing_ids) if all_citing_ids else "unknown"

    # Phase 3: Write output
    output = os.path.join(PROJECT_ROOT, "citation-affiliation-audit.md")
    with open(output, "w", encoding="utf-8") as f:
        f.write("# Citation Affiliation Audit\n\n")
        f.write(f"*Generated: {time.strftime('%Y-%m-%d')} via OpenAlex API*\n\n")
        f.write("**What this is:** Papers that cite your work, where at least one author is affiliated with a notable institution.\n")
        f.write("This means \"researchers AT [institution] cited your tool\" -- not \"[institution] officially endorses your tool.\"\n")
        f.write(f"Surveys excluded. {len(found_works)} papers with citations found on OpenAlex (out of {len(papers)} non-survey papers). ")
        f.write(f"{unique_citing} unique citing papers analyzed.\n\n")

        f.write("## Tier 0: Government, Space Agencies, National Labs, Defense, Foundation Model Cos\n\n")
        f.write(f"**{len(all_tier0)} entries**\n\n")
        if all_tier0:
            f.write("| Category | Institution | Country | Your Work Cited | Citing Paper | Year |\n")
            f.write("|----------|-----------|---------|----------------|-------------|------|\n")
            for e in sorted(all_tier0, key=lambda x: (x["category"], -(x.get("year") or 0))):
                ct = (e["citing_title"] or "")[:60].replace("|", "/")
                inst = e["institution"].replace("|", "/")
                cw = e["cited_work"][:35].replace("|", "/")
                f.write(f"| {e['category']} | {inst} | {e['country']} | {cw} | {ct} | {e['year']} |\n")

        f.write(f"\n## Tier 1: Big Tech, Finance, Pharma, Healthcare, Industrial\n\n")
        f.write(f"**{len(all_tier1)} entries**\n\n")
        if all_tier1:
            f.write("| Category | Institution | Country | Your Work Cited | Citing Paper | Year |\n")
            f.write("|----------|-----------|---------|----------------|-------------|------|\n")
            for e in sorted(all_tier1, key=lambda x: (x["category"], -(x.get("year") or 0))):
                ct = (e["citing_title"] or "")[:60].replace("|", "/")
                inst = e["institution"].replace("|", "/")
                cw = e["cited_work"][:35].replace("|", "/")
                f.write(f"| {e['category']} | {inst} | {e['country']} | {cw} | {ct} | {e['year']} |\n")

        # Summary by institution
        f.write("\n## Summary by Institution\n\n")
        inst_counts = {}
        for e in all_tier0 + all_tier1:
            key = (e["institution"], e["category"])
            inst_counts[key] = inst_counts.get(key, 0) + 1
        f.write("| Institution | Category | Work-Citations |\n")
        f.write("|-----------|----------|---------------|\n")
        for (inst, cat), count in sorted(inst_counts.items(), key=lambda x: -x[1]):
            f.write(f"| {inst} | {cat} | {count} |\n")

        # Coverage appendix
        f.write("\n## Coverage\n\n")
        f.write(f"**Papers with citations on OpenAlex:** {len(found_works)}/{len(papers)}\n\n")
        if zero_cite:
            f.write(f"**Indexed but 0 citations ({len(zero_cite)}):** ")
            f.write(", ".join(z[:40] for z in zero_cite[:20]))
            if len(zero_cite) > 20:
                f.write(f", ... and {len(zero_cite)-20} more")
            f.write("\n\n")
        if not_found:
            f.write(f"**Not found on OpenAlex ({len(not_found)}):** ")
            f.write(", ".join(n[:40] for n in not_found[:20]))
            if len(not_found) > 20:
                f.write(f", ... and {len(not_found)-20} more")
            f.write("\n\n")
        f.write("*OpenAlex coverage improves over time. Re-run in 3-6 months to capture newly indexed papers.*\n")

    print(f"\n{'=' * 60}")
    print(f"DONE -> {output}")
    print(f"Papers found on OpenAlex: {len(found_works)}/{len(papers)}")
    print(f"Unique citing papers analyzed: {unique_citing}")
    print(f"Tier 0: {len(all_tier0)} entries")
    print(f"Tier 1: {len(all_tier1)} entries")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
