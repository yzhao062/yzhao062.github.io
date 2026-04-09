# External visibility and citations of Yue Zhao research tools and papers

## Coverage criteria and evidence standard

This report only includes items that explicitly name at least one of the following: **a tool** (e.g., PyOD, ADBench, TrustLLM, SUOD), **a paper title** tied to those tools, or **“Yue Zhao”**. Items that discuss anomaly detection or AI safety without explicitly naming your work are excluded by design.

Dates are reported as they appear on the source page/PDF (or, when not provided, the publication date shown by the hosting platform).

## Government and public-sector citations

**Source:** entity["organization","United States Senate Committee on Homeland Security and Governmental Affairs","us senate committee"] (majority staff report PDF)  
**URL:** `https://www.hsgac.senate.gov/wp-content/uploads/2024.06.11-HSGAC-Majority-Report-Risks-of-Hedge-Funds-Use-of-AI-Report.pdf`  
**Date:** 2024-06-11 (in filename; the PDF’s reference section cites the TrustLLM paper)  
**Explicit mention(s):** TrustLLM (as the cited paper “TrustLLM: Trustworthiness in Large Language Models”)  
**What is named from your list:** TrustLLM  
**Evidence:** The report’s references include an entry in the form “Sun et al., *TrustLLM: Trustworthiness in Large Language Models* …” (i.e., a direct government-document citation to the TrustLLM paper title). citeturn3view0turn5screenshot0

**Source:** entity["organization","National Institute of Standards and Technology","us standards agency"] (publication NIST AI 100-2e2025)  
**URL:** `https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2025.pdf`  
**Date:** 2025-03 (date shown in the PDF front matter)  
**Explicit mention(s):** TrustLLM  
**What is named from your list:** TrustLLM  
**Evidence:** The document names “TrustLLM” as a benchmark and describes it as intended to evaluate multiple trust-related dimensions of LLM behavior (the title page identifies the publication as “March 2025,” and the benchmark discussion explicitly names TrustLLM). citeturn4view0turn5screenshot2

**Source:** entity["organization","Department of Defense","us defense department"] (entity["organization","Chief Digital and Artificial Intelligence Office","dod cdao"] / ai.mil hosted PDF)  
**URL:** `https://www.ai.mil/Portals/137/Documents/Resources%20Page/2024-12GenAI-Responsible-AI-Toolkit.pdf?ver=zbj8sBy4p3XDtcPU8rmZhw%3D%3D`  
**Date:** 2024-12 (in filename/URL path)  
**Explicit mention(s):** TrustLLM  
**What is named from your list:** TrustLLM  
**Evidence:** The toolkit includes a directive-like line to “Use TrustLLM to evaluate LLMs …,” explicitly naming TrustLLM in a U.S. defense-oriented responsible-AI resource. citeturn15search22

## Enterprise and industry adoption evidence

**Source:** entity["company","Databricks","data platform company"] (company engineering blog)  
**URL:** `https://www.databricks.com/blog/2023/03/13/unsupervised-outlier-detection-databricks.html`  
**Date:** 2023-03-13  
**Explicit mention(s):** PyOD  
**What is named from your list:** PyOD  
**Evidence:** The post describes integrating “the … PyOD library of outlier detection algorithms” into an approach for unsupervised outlier detection on Databricks (including integration framing alongside MLflow and Hyperopt). citeturn8search0

**Source:** entity["company","Ericsson","telecom company"] (company blog)  
**URL:** `https://www.ericsson.com/en/blog/2020/7/how-to-make-anomaly-detection-more-accessible`  
**Date:** 2020-07-22  
**Explicit mention(s):** PYOD (PyOD)  
**What is named from your list:** PyOD  
**Evidence:** The post lists “PYOD” among “popular” open-source anomaly detection libraries (explicitly naming it). citeturn8search2

**Source:** entity["company","Walmart","retail corporation"] (public code repository under walmartlabs) hosted on entity["company","GitHub","code hosting platform"]  
**URL:** `https://github.com/walmartlabs/anomaly-detection-walmart`  
**Date:** Not stated on the landing snippet; repository is publicly accessible (reporting access context)  
**Explicit mention(s):** “pyod” (as a required package), plus direct imports of `pyod.models...` in code  
**What is named from your list:** PyOD  
**Evidence:** The repository README lists “pyod” as a required dependency, and source code imports from `pyod.models...`, demonstrating explicit use of the PyOD package name in an enterprise-associated repository. citeturn8search1turn8search15

**Source:** entity["company","Airia","enterprise ai company"] (company blog)  
**URL:** `https://airia.com/ai-gateway-skeleton-key-protocol-attack/`  
**Date:** 2026-03-30  
**Explicit mention(s):** AEGIS (“AEGIS demonstrate this is feasible …”)  
**What is named from your list:** Aegis  
**Evidence:** The blog explicitly references “AEGIS” in the context of agent security controls (as a cited example/resource), naming the Aegis project string directly. citeturn11search27

## Institutional safety reporting that names TrustLLM

**Source:** entity["organization","Future of Life Institute","ai safety ngo"] (AI Safety Index)  
**URL:** `https://futureoflife.org/ai-safety-index-winter-2025/`  
**Date:** “DECEMBER 2025” (edition metadata on the page)  
**Explicit mention(s):** “TrustLLM Benchmark”  
**What is named from your list:** TrustLLM  
**Evidence:** The Winter 2025 AI Safety Index page includes a labeled reference to “TrustLLM Benchmark,” explicitly naming it as part of the index’s evaluation materials. citeturn6view0turn7view3

**Source:** entity["company","OpenAI","ai research company"] system card PDF (negative result for your specific query)  
**URL:** `https://arxiv.org/pdf/2410.21276`  
**Date:** 2024-08-08 (as shown on the PDF title page)  
**Explicit mention(s):** none found for “TrustLLM” via full-document string search  
**What is named from your list:** none (this item is included because you explicitly requested system-card checks)  
**Evidence:** A full-text search within the PDF for “TrustLLM” returns no matches. citeturn18view0turn19view0

**Source:** entity["company","Google DeepMind","ai research lab"] model card PDF (negative result for your specific query)  
**URL:** `https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf`  
**Date:** Model card update: December 2025 (shown on the PDF)  
**Explicit mention(s):** none found for “TrustLLM” via full-document string search  
**What is named from your list:** none (included because you explicitly requested model-card checks)  
**Evidence:** A full-text search within the Gemini 3 Pro model card PDF for “TrustLLM” returns no matches. citeturn22view1turn27view0

## Education, courses, and practitioner tutorials that name the tools

**Source:** entity["organization","DataCamp","online learning platform"] (course page)  
**URL:** `https://www.datacamp.com/courses/anomaly-detection-in-python`  
**Date:** “Published: 5 months ago” (platform metadata shown in indexing)  
**Explicit mention(s):** PyOD (“PyOD’s IForest”)  
**What is named from your list:** PyOD  
**Evidence:** The course outline explicitly names “PyOD’s IForest” in a chapter on Isolation Forests, indicating that PyOD is taught/used in the course content. citeturn10search2

**Source:** entity["organization","Analytics Vidhya","data science media site"] (tutorial article)  
**URL:** `https://www.analyticsvidhya.com/blog/2019/02/outlier-detection-python-pyod/`  
**Date:** 2024-10-16 (as shown by indexing metadata)  
**Explicit mention(s):** PyOD; “Yue Zhao” (as designer/implementer of PyOD, named in the text body snippet)  
**What is named from your list:** PyOD  
**Evidence:** The article explicitly describes PyOD and names “Yue Zhao” in connection with creating the library. citeturn10search10

**Source:** entity["organization","Goodreads","book catalog platform"] (book listing page)  
**URL:** `https://www.goodreads.com/book/show/79328412-handbook-of-anomaly-detection`  
**Date:** 2023-01-03 (date shown on the listing snippet)  
**Explicit mention(s):** PyOD  
**What is named from your list:** PyOD  
**Evidence:** The listing text explicitly says the book provides hands-on guidance using tools “such as PyOD,” naming PyOD directly. citeturn10search29

## Patents that cite or name PyOD, COPOD, and ECOD

**Source:** entity["organization","World Intellectual Property Organization","un agency for ip"] / Google Patents entry for WO2023166515A1  
**URL:** `https://patents.google.com/patent/WO2023166515A1/en`  
**Date:** Publication date not shown in the snippet block, but the patent record is WO2023… (jurisdictional record); use the Google Patents page for the canonical date fields  
**Explicit mention(s):** “Pyod: A python toolbox for scalable outlier detection” (named as prior work/citation)  
**What is named from your list:** PyOD  
**Evidence:** The patent text explicitly references the PyOD paper by title (“Pyod: A python toolbox…”), including the author string beginning with “Zhao, Y.” citeturn9search0

**Source:** entity["organization","European Patent Office","european patent authority"] / Google Patents entry for EP4662606A1  
**URL:** `https://patents.google.com/patent/EP4662606A1/fr`  
**Date:** Not shown in the snippet block (consult the patent header on the page for the official publication date)  
**Explicit mention(s):** “pyOD … an open-source anomaly detection toolkit”  
**What is named from your list:** PyOD  
**Evidence:** The patent text explicitly names “pyOD” as an anomaly detection toolkit used to supply unsupervised methods, directly naming PyOD. citeturn9search4

**Source:** entity["organization","European Patent Office","european patent authority"] / Google Patents entry for EP4339817A1  
**URL:** `https://patents.google.com/patent/EP4339817A1/en`  
**Date:** Not shown in the snippet block (consult the patent header on the page for the official publication date)  
**Explicit mention(s):** “Copula-based Outlier Detection (COPOD)” / “a COPOD model”  
**What is named from your list:** COPOD  
**Evidence:** The patent enumerates anomaly detection model options and explicitly includes “COPOD” as a named model type. citeturn9search1

**Source:** entity["organization","United States Patent and Trademark Office","us patent authority"] / Google Patents entry for US20250217974A1  
**URL:** `https://patents.google.com/patent/US20250217974A1/en`  
**Date:** Not shown in the snippet block (consult the patent header on the page for the official publication date)  
**Explicit mention(s):** COPOD; ECOD  
**What is named from your list:** COPOD; ECOD  
**Evidence:** The patent lists multiple outlier detection methods and explicitly includes both “COPOD” and “ECOD” in that list. citeturn9search5

**Source:** Google Patents entry for CN111666198A (Chinese patent)  
**URL:** `https://patents.google.com/patent/CN111666198A/zh`  
**Date:** Not shown in the snippet block (consult the patent header on the page for the official publication date)  
**Explicit mention(s):** “PYOD” (described as a Python outlier/anomaly detection algorithm/toolkit)  
**What is named from your list:** PyOD  
**Evidence:** The patent explicitly names “PYOD” among selectable anomaly detection algorithms. citeturn9search14

**Source:** Google Patents entry for CN112328424A (Chinese patent)  
**URL:** `https://patents.google.com/patent/CN112328424A/zh`  
**Date:** Not shown in the snippet block (consult the patent header on the page for the official publication date)  
**Explicit mention(s):** “COPOD: Copula-Based Outlier Detection” (listed under non-patent citations)  
**What is named from your list:** COPOD  
**Evidence:** The “Non-Patent Citations” section explicitly names the COPOD paper title. citeturn9search9

## Non-English media and community coverage

**Source:** entity["company","Zhihu","chinese q&a platform"] (专栏 post)  
**URL:** `https://zhuanlan.zhihu.com/p/701584258`  
**Date:** 2024-06-04  
**Explicit mention(s):** PyOD  
**What is named from your list:** PyOD  
**Evidence:** The article title and body snippet explicitly name PyOD as the subject (a PyOD-focused anomaly/outlier detection write-up). citeturn12search0

**Source:** entity["company","CSDN","chinese developer platform"] (blog post)  
**URL:** `https://blog.csdn.net/m0_56734068/article/details/143016635`  
**Date:** 2024-10-17  
**Explicit mention(s):** PyOD  
**What is named from your list:** PyOD  
**Evidence:** The post explicitly introduces “PyOD” as the topic and repeatedly names the tool string in the visible snippet. citeturn12search1

**Source:** entity["organization","The Paper","china news outlet"] (澎湃新闻)  
**URL:** `https://www.thepaper.cn/newsDetail_forward_26315865?commTag=true`  
**Date:** 2024-02-09  
**Explicit mention(s):** TrustLLM  
**What is named from your list:** TrustLLM  
**Evidence:** The article explicitly names TrustLLM and describes it as a unified framework/benchmark for assessing trust-related properties of LLMs, i.e., explicit naming in a mainstream Chinese news outlet. citeturn12search9

**Source:** entity["company","Qiita","japanese developer platform"] (Japanese developer article)  
**URL:** `https://qiita.com/amber27182818/items/4c5c1db24f4ddc48285a`  
**Date:** 2023-12-16  
**Explicit mention(s):** PyOD  
**What is named from your list:** PyOD  
**Evidence:** The post title and snippet explicitly name PyOD and describe PyOD-based outlier detection in Japanese. citeturn13search0

**Source:** Korean tech blog post (Tistory)  
**URL:** `https://ty-analyst.tistory.com/78`  
**Date:** 2024-08-17  
**Explicit mention(s):** PyOD  
**What is named from your list:** PyOD  
**Evidence:** The post title and content snippet explicitly name PyOD and describe it as an outlier detection library in Korean. citeturn13search1

## Conference proceedings and benchmark artifacts that explicitly name the work

**Source:** entity["organization","NeurIPS","machine learning conference"] proceedings page (Datasets and Benchmarks track abstract)  
**URL:** `https://proceedings.neurips.cc/paper_files/paper/2022/hash/cf93972b116ca5268827d575f2cc226b-Abstract-Datasets_and_Benchmarks.html`  
**Date:** NeurIPS 2022 (conference year; page is the canonical proceedings record)  
**Explicit mention(s):** ADBench  
**What is named from your list:** ADBench  
**Evidence:** The proceedings abstract explicitly names “ADBench” as the benchmark and describes it as a large comparison across algorithms/datasets. citeturn29search8

**Source:** Public repository hosted on GitHub (ADBench official repo)  
**URL:** `https://github.com/Minqi824/ADBench`  
**Date:** Not a paper date; repository artifact (date not shown in snippet block)  
**Explicit mention(s):** ADBench  
**What is named from your list:** ADBench  
**Evidence:** The repository description explicitly states it is the “official” repository for “ADBench: Anomaly Detection Benchmark (NeurIPS 2022).” citeturn29search0

**Source:** entity["organization","Machine Learning and Systems","mlsys conference"] proceedings abstract page (MLSys 2021)  
**URL:** `https://proceedings.mlsys.org/paper_files/paper/2021/hash/37385144cac01dff38247ab11c119e3c-Abstract.html`  
**Date:** 2021 (conference year; canonical proceedings record)  
**Explicit mention(s):** SUOD; Yue Zhao (as author on the proceedings record)  
**What is named from your list:** SUOD  
**Evidence:** The MLSys proceedings entry explicitly names “SUOD: Accelerating Large-Scale Unsupervised Heterogeneous Outlier Detection” and lists “Yue Zhao” among the authors on the proceedings record. citeturn29search9

**Source:** entity["organization","International Conference on Learning Representations","iclr conference"] (OpenReview poster record)  
**URL:** `https://openreview.net/forum?id=uBThjlbzxS`  
**Date:** Published 2026-01-26; last modified 2026-03-02 (as shown on the record)  
**Explicit mention(s):** DoxBench; Yue Zhao (author list on the record)  
**What is named from your list:** DoxBench  
**Evidence:** The OpenReview record explicitly labels the submission as an “ICLR 2026 Poster,” names “DoxBench,” and lists “Yue Zhao” in the author list visible on the page snippet. citeturn29search11

## BibTeX entries for commonly referenced papers in the evidence above

```bibtex
@article{zhao2019pyod,
  title   = {PyOD: A Python Toolbox for Scalable Outlier Detection},
  author  = {Zhao, Yue and Nasrullah, Zain and Li, Zheng},
  journal = {Journal of Machine Learning Research},
  year    = {2019},
  volume  = {20},
  number  = {96},
  url     = {https://www.jmlr.org/papers/volume20/19-011/19-011.pdf}
}

@inproceedings{zhao2021suod,
  title     = {SUOD: Accelerating Large-Scale Unsupervised Heterogeneous Outlier Detection},
  author    = {Zhao, Yue and Hu, Xiyang and Cheng, Cheng and Wang, Cong and Wan, Changlin and Wang, Wen and Yang, Jianing and Bai, Haoping and Li, Zheng and Xiao, Cao and Wang, Yunlong and Qiao, Zhi and Sun, Jimeng and Akoglu, Leman},
  booktitle = {Proceedings of Machine Learning and Systems},
  year      = {2021},
  url       = {https://proceedings.mlsys.org/paper_files/paper/2021/hash/37385144cac01dff38247ab11c119e3c-Abstract.html}
}

@inproceedings{han2022adbench,
  title     = {ADBench: Anomaly Detection Benchmark},
  author    = {Han, S. and others},
  booktitle = {Advances in Neural Information Processing Systems (Datasets and Benchmarks Track)},
  year      = {2022},
  url       = {https://proceedings.neurips.cc/paper_files/paper/2022/hash/cf93972b116ca5268827d575f2cc226b-Abstract-Datasets_and_Benchmarks.html}
}

@inproceedings{luo2026doxbench,
  title     = {Doxing via the Lens: Revealing Location-related Privacy Leakage on Multi-modal Large Reasoning Models},
  author    = {Luo, Weidi and Lu, Tianyu and Zhang, Qiming and Liu, Xiaogeng and Hu, Bin and Zhao, Yue and Zhao, Jieyu and Gao, Song and McDaniel, Patrick and Xiang, Zhen and Xiao, Chaowei},
  booktitle = {International Conference on Learning Representations (Poster)},
  year      = {2026},
  url       = {https://openreview.net/forum?id=uBThjlbzxS}
}
```