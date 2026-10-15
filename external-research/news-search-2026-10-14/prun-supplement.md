# Government, Security Reports, and Rules Supplement

Three Agy workers completed 78 logged searches: government (20), security reports (32), and industry rules (26). The coordinator read raw sources, checked existing ledgers, and corrected worker conclusions. This supplement adds no new adoption or rule citation to the ledgers.

ORNL OSTI 3002371, INL OSTI 3024592, and CrowdStrike's BERT command-line article are existing records. The INL source now has its primary PDF URL in Ledger 1b G6. Its June 2025 report discusses TrustLLM in the context of nuclear power plant human-AI interaction.

CISA SB26-201 repeats an existing vulnerability record. PyOD is CVE-2026-15529; the worker mistakenly assigned CVE-2026-15531 from the HashNeRF-pytorch row. This is a vulnerability mention, not government adoption.

The previously blocked GAO-25-108519 brief was recovered through a public October 10 archive snapshot. The coordinator checked both pages and reran the PDF term scan: no target citation. EDPB's 102-page AI Privacy Risks report mentions a different TrustLLM, the Linkoping University European project.

Checked Markdown, text, HTML, and JSON in the AAS-1 and OWASP Agentic Skills Top 10 repositories contain none of the scanned target names or paper IDs. Their exact commits are retained in prun-verdicts.jsonl. AAS-1 is a community specification. This check does not establish adoption by an accredited standards body. The OWASP Agent Observability fetch returned a navigation shell, and the Agentic Applications Top 10 fetch was a landing page. Neither supports a full-document negative verdict.

The fetched CSA Vibe Coding Security Crisis article has no checked target match. The worker's filename suggested MAESTRO, but the actual title differs. Search-only results for financial regulators, IETF, ISO, and other standards tracks remain search scope, not verified document-level negatives. No claim is made that all government reports or rules omit this research.

The result is consistent with the main run's two newly indexed official citations, BIS Working Paper 1245 and JRC146034. Those are research citations. Their dates are February 2025 and April 2026, respectively; neither is a newly published October rule.

## Reproduction

Exact completed search calls are in prun-queries.jsonl. Reviewed source decisions, hashes, repository commits, and correction notes are in prun-verdicts.jsonl. Raw worker reports and event streams remain in the scratch directory. They are discovery output and contain the errors corrected above. No worker committed or pushed files.
