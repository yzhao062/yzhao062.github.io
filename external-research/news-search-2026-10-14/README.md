# Bounded Coverage Search, October 14, 2026

This run searches external evidence about Yue Zhao and FORTIS work. Its readers are the site owner and future audit maintainers. The user authorized at most one hour, from 05:28:50 to 06:28:50 UTC on October 15. Three native Codex research workers completed their result files; the coordinator verified and integrated them. Three additional Agy workers completed a small prun supplement with 78 searches on recent government publications, security reports, and industry rules within the same deadline.

The run finished at 06:15:22 UTC after 46.5 minutes, with all six workers stopped. The two portions logged 437 queries in total.

The Codex portion logged 359 queries and recorded outcomes for 83 candidate URLs, including blocked and held sources. It adds two official research citations, two external articles, and 35 ecosystem records, including ten patent families. The ecosystem category includes modest signals such as personal projects, teaching examples, vendor blogs, and generated summaries. These categories should not be summed into an impact score.

## Findings Worth Surfacing

| Source | Verified Evidence | Scope |
|---|---|---|
| [FERZ](https://ferz.ai/articles/auditability-is-not-authorization) | October 9 analysis cites Auditable Agents v4 while contrasting audit evidence with runtime authorization. | Plausible match for the remembered vendor; no adoption or endorsement claim. |
| [Rivista AI](https://www.rivista.ai/2026/10/08/auditable-agents/) | October 8 feature explains the framework and discusses replication limits. | Named editorial feature. |
| [Agent Exchange](https://github.com/open-experiments/agent-exchange/blob/c0fa748c6eb06844c9926212def0d5805f43e6db/src/internal/toolgate/score.go) | Source explicitly implements five auditability scores attributed to Nian et al. | Independent prototype use; experiments were not rerun. |
| [OpenClaw Aegis Signer](https://github.com/msbel5/openclaw-aegis-signer) | README cites AEGIS; source signs records after tool execution. | Inspired implementation, not a pre-execution firewall reproduction. |
| [Oracle](https://docs.oracle.com/en/industries/financial-services/ofs-analytical-applications/crime-compliance-studio-application-pack/8.1.2.9.0/csadc/python-libraries-predefined-conda-environment.html) | Compliance Studio 8.1.2.9.0 lists PyOD 2.0.2 in default and ml4aml environments. | Stronger documentation for the existing Oracle row. |
| [BIS](https://www.bis.org/publications/working-paper-1245-putting-ai-agents-through-their-paces-general-tasks.pdf) and [European Commission JRC](https://doi.org/10.2760/0363450) | Both official reports cite TrustLLM, with bibliography and body locations checked in raw PDFs. | Research citations, not benchmark adoption. |
| [Seagate](https://seagatecareers.com/job/Samut-Prakan-AI-Adoption-Intern/15158-en_US/) | Requisition 15158 requires PyOD proficiency. | Hiring-skill evidence, not deployment. |

The ten new patent families bring the audited total from 97 to 107. Four name a tool in numbered claims, bringing that narrower count from seven to eleven. An independent reviewer checked 21 publication versions. Optional algorithms and abandoned applications remain explicitly labeled; the figure does not measure commercial deployments.

## Corrections and Limits

IBM's report uses a fictional Anomaly Finder teaching example. Its PyOD mention belongs in the ecosystem ledger as educational evidence and is omitted from the public impact cards. Hysen Labs currently records approval by Kacey on October 5, so the proposed downgrade based on a stale machine-only disclaimer was rejected. FERZ's paper reference is in its bibliography; public wording says it cites the paper rather than claiming a detailed critique.

Argus Security is affiliated with the paper authors and stays outside independent coverage. Google Assured OSS has conflicting language/version catalogs, so current inclusion is not asserted. MANPREDIC's reported Spanish Army deployment lacks a verified PyOD mention. GAO-25-108519 was recovered from a public archive and checked in full; it contains no target citation. A new review's DrugAgent reference concerns a different paper; its TDC citation goes to citation handoff. The NRC Canada paper also goes to citation handoff because it runs SORRY-Bench, preserving the government-methods-use ledger's basis.

This is a targeted incremental pass over an inventory of 133 publications and 22 tools. The Codex query log names 41 inventory entries; 114 have no targeted query logged. Alias-based mapping is documented in the matrix and can associate one query with a paper and its tool. The October 2 full coverage matrix remains unchanged. The citation-affiliation snapshot is still dated September 12 and incomplete.

The small prun supplement found no additional verified adoption or rule citation. It recovered the GAO brief, added the INL primary source, and rejected duplicate and mistaken matches. See [the reviewed supplement](prun-supplement.md).

## Files and Reproduction

- `candidates.jsonl`: all 83 URL records with independent status and tier fields, source hashes, qualifiers, and ledger pointers.
- `queries.jsonl`: exact Codex/coordinator queries, with batch ambiguity retained where the search tool returned mixed results.
- `coverage-matrix.csv`: every current inventory entry for the Codex portion, including entries not searched there.
- `prun-queries.jsonl`, `prun-verdicts.jsonl`, and `prun-supplement.md`: exact Agy queries and coordinator-reviewed outcomes.
- `citation-handoff.jsonl`: ordinary academic citations for a later citation audit.
- `evidence-manifest.jsonl`: source URL, local raw-file path, hash, and locator. Raw source bodies remain outside Git at `/tmp/news-search-20261014-codex/`.
- `patent-review.md` and `source-review.md`: independent reviews; all three source-review findings were addressed.
- `manifest.json` and `checks.json`: scope, counts, reconciliation, and validation results.

Local site changes include the impact cards, synchronized patent figures, and llms.txt. Workers did not commit or push; publication was authorized separately after review.
