# Website Evidence Review

Reviewed the uncommitted opensource.html additions at 05:51 to 05:55 UTC on October 15, 2026. Scope: IBM, Oracle, BIS, JRC, FERZ, Rivista AI, and the proposed Hysen classification change. The later downstream-code addition was outside this assigned review. Repository files were read only.

## Findings

### P1: IBM Anomaly Finder Is an Explicitly Fictional Example

At opensource.html:451, the new enterprise row describes PyOD integration without the example's fictional scope. BD16.txt lines 928-932, corresponding to the preceding section on PDF page 10, explicitly introduce a fictitious ecommerce application called Anomaly Finder. The PyOD pipeline and container statements on page 11 continue that example. These statements do not establish an IBM production deployment.

Recommend removing the public enterprise row. The audit can retain an IBM-authored illustrative mention with a clear fictional-example flag and zero actual-adopter increment. If the row remains public, use: “IBM's 2021 enterprise AI maturity framework names PyOD in its fictional Anomaly Finder worked example.” The product name has a space. Source: BD16.pdf and BD16.txt; canonical URL https://www.ibm.com/downloads/documents/us-en/107a02e948c8f48d.

This finding corrects my initial broad-discovery handoff, which relied too narrowly on page 11. The corrected candidates.jsonl and result.md now preserve the fictional scope.

### P1: Hysen Machine-Only Review Claim Conflicts with Saved Raw Evidence

The proposed Ledger 2 row 50 transfer was based on a claim that no named editor had reviewed the article. Saved BD14.txt lines 53-56 instead show review and approval by Kacey on October 5, 2026. BD14.html contains the same byline and a reviewedBy JSON-LD field. Fresh verification of the canonical URL confirms the named approval.

Hysen's editorial policy says its pipeline drafts analyses with AI assistance, followed by automated checks and then a named editor's review. That workflow disclosure should remain attached to the record. It does not support saying this particular page lacks human review. Recommend retaining the existing row, updating its canonical URL to https://hysenlabs.com/projects/yzhao062-pyod, and recording AI-assisted drafting plus named editorial approval. Do not transfer solely on the disproven missing-editor claim. If the coordinator elects a Tier 3 cap under the broader AI-drafting rule, state that distinct rationale and preserve the named-review evidence.

This corrects my initial handoff. The old quoted machine-only disclaimer is absent from the raw source I cited for it. It must not remain as a verified current quote. Raw policy and editor pages are now saved as hysen-policy.html/.txt and hysen-editor.html/.txt, with hashes in review-fetches.json.

### P2: FERZ Wording Should Describe a Citation and General Comparison

At opensource.html:542, “directly discusses Auditable Agents” is stronger than the source's explicit attribution. The article names the paper in bibliography entry Nian2026, including all ten authors and arXiv 2604.05485 v4. Its body discusses auditability and authorization in general terms without naming Auditable Agents or attaching an inline Nian2026 reference to a passage.

Recommended wording: “FERZ's October 2026 analysis cites Auditable Agents while contrasting audit evidence with authorization before execution, and presents FERZ's own approach.” This preserves the real external citation without attributing every general criticism to the paper. Vendor Analysis is the appropriate label; the source does not show adoption or validation. Edward Meyman's byline and FERZ's human-authorship policy are recorded in the worker evidence. AI editorial assistance is disclosed, but the policy claims human control of thesis, claims, and final wording.

## Supported Additions

| Source | Raw Evidence | Assessment |
|---|---|---|
| Oracle Compliance Studio | BD34.txt lines 7-11 identify predefined environments. Tables A-9 and A-10 list pyod 2.0.2 at lines 131-132 and 286-287. | Current site wording is supported. Update existing audit row 66dj; do not count another Oracle adopter. |
| BIS Working Paper 1245 | bis1245.txt PDF page 4 groups Huang et al. 2024 in its literature review of LLM evaluation. PDF page 15 supplies the TrustLLM title. | Current site wording says cites and is appropriately narrow. This is a research reference, not benchmark adoption or a BIS policy position. |
| European Commission JRC RASS | jrc146034.txt PDF page 7 cites reference 27 for misinformation, hallucinations, and biases. PDF page 59 identifies TrustLLM and arXiv 2401.05561. | Current wording accurately describes a citation. The report's disclaimer says it does not necessarily express Commission views; the site makes no contrary claim. |
| Rivista AI | rivista-auditable.txt lines 77 and 82 cover the five dimensions and Aegis results with an independent-replication qualification. Lines 91-94 name the paper and authors. | Current site wording is supported. It describes coverage without claiming independent experimental validation. |

The revised agent-auditability subtitle, “External coverage, comparisons, and research use,” is more accurate than the prior validation framing.

## Duplicate Check

Searched the complete HEAD audit text for IBM report ID 107a02e948c8f48d and Anomaly Finder, BIS 1245, JRC146034 and DOI 0363450, FERZ, and the Rivista article path. None was already recorded. Oracle adoption was already recorded at Ledger 3 row 66dj, so the new documentation belongs in that row. Hysen was already Ledger 2 row 50 under an older /en/projects path. Existing BIS PyOD documents and IBM patent or research entries concern other evidence and do not duplicate these exact documents.

## Outcome

Publication should wait for the IBM scope correction and removal of the unsupported Hysen no-editor claim from integration material. The Oracle, BIS, JRC, and Rivista wording passes this review. FERZ needs the small attribution adjustment above. No broad discovery was performed during this review.
