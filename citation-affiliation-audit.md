# Citation Affiliation Audit

*Generated 2026-10-17 via OpenAlex + Dimensions over 128 non-survey papers in `data/publications.json`.*

Each row is a citing paper with at least one author at a notable organization. It means researchers at that organization cited the work, not that the organization endorses it. Self-citations and co-author citations are excluded. Both sources undercount computer-science citations, so treat every figure as a lower bound.

| Source | Papers with citations | Unique citing papers | Run status |
|---|---:|---:|---|
| OpenAlex | 49 / 128 | 0 | incomplete: 0 works queried, 49 never queried |
| Dimensions | 45 / 128 | 1,496 | complete |

> [!WARNING]
> **This run is incomplete.** One or more sources stopped early, so the numbers
> are a floor, and an absent citation here is not evidence of no citation.
>
> - **OpenAlex**: daily credit budget spent while resolving identifiers (100 of 128 papers processed, 89 identifiers resolved, 49 of them with citations; no citing works queried). The 89 resolved identifiers are cached, so the next run after the 00:00 UTC reset spends its budget on citing works.

## Tier 0: Government, National Labs, Space Agencies, Central Banks, Defense, Research Institutes, Foundation Model Companies

**16 rows: 14 citing papers, 8 organizations.**

| Category | Organization | Country | Work Cited | Citing Paper | Year | Source |
|---|---|---|---|---|---|---|
| Central Bank | Deutsche Bundesbank | Germany | The Need for Unsupervised Outlier Model… | RECol: Reconstruction Error Columns for Outlier Detection | 2023 | dimensions |
| Defense/Research | RAND Corporation | United States | COPOD | A robust unsupervised method for outlier set detection | 2025 | dimensions |
| Foundation Model Co | Meta | United States | Edit Away and My Face Will Not Stay… | PrivateEdit: A Privacy-Preserving Pipeline for Face-Centric Generative Image Editing | 2026 | dimensions |
| Foundation Model Co | Meta | United States | COPOD | Detecting Tiny Performance Regressions at Hyperscale | 2026 | dimensions |
| Foundation Model Co | Meta | United States | COPOD | TSB-AutoAD: Towards Automated Solutions for Time-Series Anomaly Detection | 2025 | dimensions |
| Foundation Model Co | Meta | United States | The Need for Unsupervised Outlier Model… | EasyAD: A Demonstration of Automated Solutions for Time-Series Anomaly Detection | 2025 | dimensions |
| Foundation Model Co | Meta | United States | The Need for Unsupervised Outlier Model… | TSB-AutoAD: Towards Automated Solutions for Time-Series Anomaly Detection | 2025 | dimensions |
| Foundation Model Co | Meta | United States | COPOD | Data-Efficient and Interpretable Tabular Anomaly Detection | 2023 | dimensions |
| National Lab | Argonne National Laboratory | United States | TODS | A novel sensor-driven framework for preemptive failure detection in energy systems… | 2025 | dimensions |
| National Lab | Brookhaven National Laboratory | United States | COPOD | Performance analysis and data reduction for exascale scientific workflows | 2025 | dimensions |
| National Lab | Sandia National Laboratories | United States | COPOD | Performance analysis and data reduction for exascale scientific workflows | 2025 | dimensions |
| Research Institute | Fraunhofer | Germany | Artificial Intelligence Foundation for… | Human-supervised Agentic AI for Hypothesis Generation and Experimental Assistance in Drug… | 2026 | dimensions |
| Research Institute | Fraunhofer | Germany | Artificial Intelligence Foundation for… | Computational drug repurposing: approaches, evaluation of in silico resources and case… | 2025 | dimensions |
| Research Institute | Fraunhofer | Germany | COPOD | Privacy and Utility Evaluation of Synthetic Tabular Data for Machine Learning | 2024 | dimensions |
| Research Institute | Fraunhofer | Germany | TODS | Meta-learning for Automated Selection of Anomaly Detectors for Semi-supervised Datasets | 2023 | dimensions |
| US Government | NIH | United States | TrustLLM | Economics and Equity of Large Language Models: Health Care Perspective | 2024 | dimensions |

## Tier 1: Big Tech, Finance, Pharma, Healthcare, Industrial, Telecom

**54 rows: 48 citing papers, 23 organizations.**

| Category | Organization | Country | Work Cited | Citing Paper | Year | Source |
|---|---|---|---|---|---|---|
| Big Tech | Adobe | United States | TrustLLM | Benchmark suites instead of leaderboards for evaluating AI fairness | 2024 | dimensions |
| Big Tech | Alibaba | China | COPOD | GraphAD | 2022 | dimensions |
| Big Tech | Alibaba | China | Combining Machine Learning Models using… | A spatial-compositional feature fusion convolutional autoencoder for multivariate… | 2021 | dimensions |
| Big Tech | Amazon | United States | COPOD | REACT: Residual-Adaptive Contextual Tuning for Fast Model Adaptation in Threat Detection | 2025 | dimensions |
| Big Tech | Amazon | United States | The Need for Unsupervised Outlier Model… | Hyperparameter Optimization in Machine Learning | 2025 | dimensions |
| Big Tech | Amazon | United States | TrustLLM | Economics and Equity of Large Language Models: Health Care Perspective | 2024 | dimensions |
| Big Tech | Amazon | United States | COPOD | Rethinking Robust Multivariate Time Series Anomaly Detection: A Hierarchical… | 2024 | dimensions |
| Big Tech | Baidu | China | Employee Turnover Prediction with Machine… | A Comprehensive Survey of Artificial Intelligence Techniques for Talent Analytics | 2025 | dimensions |
| Big Tech | Google | United States | Can Multimodal LLMs Perform Time Series… | Convergence of LLM Integration and Edge Intelligence in Decentralized IoT Ecosystems | 2026 | dimensions |
| Big Tech | Google | United States | COPOD | Data-Efficient and Interpretable Tabular Anomaly Detection | 2023 | dimensions |
| Big Tech | Huawei | China | Treble Counterfactual VLMs: A Causal… | A Survey of Multimodal Hallucination Evaluation and Detection | 2026 | dimensions |
| Big Tech | Huawei | China | COPOD | DBAgent: An RL-Based Agent for Autonomous Database Operations and Maintenance | 2026 | dimensions |
| Big Tech | Huawei | Ireland | COPOD | Real or Not? A Practitioner’s Perspective on Unsupervised Multivariate Time Series… | 2026 | dimensions |
| Big Tech | Huawei | China | TODS | TAB: Unified Benchmarking of Time Series Anomaly Detection Methods | 2025 | dimensions |
| Big Tech | Huawei | China | COPOD | Compatible Unsupervised Anomaly Detection with Multi-Perspective Spatio-Temporal Learning | 2025 | dimensions |
| Big Tech | Huawei | China | Contrastive Attributed Network Anomaly… | You Can't Ignore Either: Unifying Structure and Feature Denoising for Robust Graph… | 2024 | dimensions |
| Big Tech | IBM | Ireland | ADBench | Complex Real-World Application Systems Behavioral Profiling Using a Dynamical Systems… | 2026 | dimensions |
| Big Tech | IBM | Ireland | Artificial Intelligence Foundation for… | Impact of molecular multimodality on neural network models for prediction tasks related… | 2026 | dimensions |
| Big Tech | IBM | Switzerland | AutoAudit | Graph Feature Preprocessor: Real-time Subgraph-based Feature Extraction for Financial… | 2024 | dimensions |
| Big Tech | IBM | India | COPOD | Enabling Programmable Metric Flows | 2024 | dimensions |
| Big Tech | IBM | Switzerland | Artificial Intelligence Foundation for… | The rise of automated curiosity-driven discoveries in chemistry | 2023 | dimensions |
| Big Tech | IBM | Japan | AutoAudit | Cash flow prediction of a bank deposit using scalable graph analysis and machine learning | 2021 | dimensions |
| Big Tech | Microsoft | United States | ADBench | Debugging the Debuggers: Failure-Anchored Structured Recovery for Software Engineering… | 2026 | dimensions |
| Big Tech | Microsoft | China | Artificial Intelligence Foundation for… | Controlling risks of AI in chemical science with agents | 2025 | dimensions |
| Big Tech | Microsoft | China | COPOD | UADB: Unsupervised Anomaly Detection Booster | 2023 | dimensions |
| Big Tech | NVIDIA | United States | Combining Machine Learning Models using… | Machine Learning in Python: Main Developments and Technology Trends in Data Science… | 2020 | dimensions |
| Big Tech | Samsung | South Korea | COPOD | Relative Frequency-Rank Encoding for Unsupervised Network Anomaly Detection | 2024 | dimensions |
| Big Tech | Tencent | China | COPOD | Label Annotation for Tabular Anomaly Detection with Large Language Models | 2026 | dimensions |
| Big Tech | Tencent | China | Contrastive Attributed Network Anomaly… | How to use Graph Data in the Wild to Help Graph Anomaly Detection? | 2025 | dimensions |
| Big Tech | Tencent | China | Music Artist Classification with… | Large-scale singer recognition using deep metric learning: an experimental study | 2021 | dimensions |
| Finance | BlackRock | United States | The Need for Unsupervised Outlier Model… | Can an unsupervised clustering algorithm reproduce a categorization system? | 2024 | dimensions |
| Finance | BlackRock | United States | The Need for Unsupervised Outlier Model… | Quantifying Outlierness of Funds from their Categories using Supervised Similarity | 2023 | dimensions |
| Healthcare | Cleveland Clinic | United Kingdom | Combining Machine Learning Models using… | Applications of Artificial Intelligence in Gastrointestinal Endoscopic Ultrasound… | 2024 | dimensions |
| Industrial | Bosch | Germany | COPOD | On Why the System Makes the Corner Case: AI-based Holistic Anomaly Detection for… | 2022 | dimensions |
| Industrial | Bosch | Portugal | COPOD | Predictive maintenance on sensorized stamping presses by time series segmentation… | 2022 | dimensions |
| Industrial | Siemens | Romania | TODS | A decentralised architecture for secure exchange of assets in data spaces: The case of… | 2025 | dimensions |
| Pharma | AstraZeneca | United Kingdom, Sweden | DrugAgent | From Benchmark to Bench: Can Agents Survive Real-World Drug Discovery? | 2026 | dimensions |
| Pharma | AstraZeneca | Sweden, United Kingdom | DrugAgent | Democratising real-world drug discovery through agentic AI | 2026 | dimensions |
| Pharma | AstraZeneca | United States | Therapeutics Data Commons: Machine… | Practical Use of Advanced AI Frameworks on Real-Life Scientific Problems: Three Case… | 2026 | dimensions |
| Pharma | AstraZeneca | United Kingdom | Artificial Intelligence Foundation for… | Chemogenomic maps reveal a PRDX1-dependent iron–damage axis in the DNA damage response | 2026 | dimensions |
| Pharma | AstraZeneca | Sweden | Therapeutics Data Commons: Machine… | Machine Learning for Toxicity Prediction Using Chemical Structures: Pillars for Success… | 2025 | dimensions |
| Pharma | AstraZeneca | Sweden | Therapeutics Data Commons: Machine… | Human-in-the-loop active learning for goal-oriented molecule generation | 2024 | dimensions |
| Pharma | AstraZeneca | Sweden | Artificial Intelligence Foundation for… | A call for an industry-led initiative to critically assess machine learning for… | 2024 | dimensions |
| Pharma | Eli Lilly | United Kingdom, United States | Therapeutics Data Commons: Machine… | Machine Learning for Toxicity Prediction Using Chemical Structures: Pillars for Success… | 2025 | dimensions |
| Pharma | Merck | United States | Therapeutics Data Commons: Machine… | Data Scaling and Generalization Insights for Medicinal Chemistry Deep Learning Models | 2025 | dimensions |
| Pharma | Merck | United States | Therapeutics Data Commons: Machine… | Machine Learning for Toxicity Prediction Using Chemical Structures: Pillars for Success… | 2025 | dimensions |
| Pharma | Merck | United States | Artificial Intelligence Foundation for… | A call for an industry-led initiative to critically assess machine learning for… | 2024 | dimensions |
| Pharma | Novartis | Switzerland | Artificial Intelligence Foundation for… | A call for an industry-led initiative to critically assess machine learning for… | 2024 | dimensions |
| Pharma | Pfizer | Germany | Therapeutics Data Commons: Machine… | Machine Learning for Toxicity Prediction Using Chemical Structures: Pillars for Success… | 2025 | dimensions |
| Pharma | Pfizer | Germany | Artificial Intelligence Foundation for… | A call for an industry-led initiative to critically assess machine learning for… | 2024 | dimensions |
| Pharma | Sanofi | France | Therapeutics Data Commons: Machine… | In Silico ADMET: From Current Practices to Novel Profilers | 2026 | dimensions |
| Pharma | Sanofi | Germany, China, France, United States | Artificial Intelligence Foundation for… | Deep Batch Active Learning for Drug Discovery | 2023 | dimensions |
| Telecom | Cisco | United States | TODS | Traffic Anomaly Detection Via Conditional Normalizing Flow | 2022 | dimensions |
| Telecom | Ericsson | India | COPOD | Adaptive Thresholding Heuristic for KPI Anomaly Detection | 2024 | dimensions |

## Summary by Organization

| Organization | Category | Tier | Citing Papers | Works Cited |
|---|---|---|---:|---:|
| Meta | Foundation Model Co | 0 | 5 | 3 |
| Fraunhofer | Research Institute | 0 | 4 | 3 |
| Argonne National Laboratory | National Lab | 0 | 1 | 1 |
| Brookhaven National Laboratory | National Lab | 0 | 1 | 1 |
| Deutsche Bundesbank | Central Bank | 0 | 1 | 1 |
| NIH | US Government | 0 | 1 | 1 |
| RAND Corporation | Defense/Research | 0 | 1 | 1 |
| Sandia National Laboratories | National Lab | 0 | 1 | 1 |
| AstraZeneca | Pharma | 1 | 7 | 3 |
| Huawei | Big Tech | 1 | 6 | 4 |
| IBM | Big Tech | 1 | 6 | 4 |
| Amazon | Big Tech | 1 | 4 | 3 |
| Merck | Pharma | 1 | 3 | 2 |
| Microsoft | Big Tech | 1 | 3 | 3 |
| Tencent | Big Tech | 1 | 3 | 3 |
| Alibaba | Big Tech | 1 | 2 | 2 |
| BlackRock | Finance | 1 | 2 | 1 |
| Bosch | Industrial | 1 | 2 | 1 |
| Google | Big Tech | 1 | 2 | 2 |
| Pfizer | Pharma | 1 | 2 | 2 |
| Sanofi | Pharma | 1 | 2 | 2 |
| Adobe | Big Tech | 1 | 1 | 1 |
| Baidu | Big Tech | 1 | 1 | 1 |
| Cisco | Telecom | 1 | 1 | 1 |
| Cleveland Clinic | Healthcare | 1 | 1 | 1 |
| Eli Lilly | Pharma | 1 | 1 | 1 |
| Ericsson | Telecom | 1 | 1 | 1 |
| NVIDIA | Big Tech | 1 | 1 | 1 |
| Novartis | Pharma | 1 | 1 | 1 |
| Samsung | Big Tech | 1 | 1 | 1 |
| Siemens | Industrial | 1 | 1 | 1 |

## Excluded and Flagged Citations

Excluded: 1 row where the PI is a citing author, and 10 rows where an author of the cited work or two or more frequent co-authors are. A frequent co-author shares two or more papers with the PI. Flagged but kept: 0 rows where exactly one frequent co-author who did not write the cited work matches, since one common name is weak evidence.

<details><summary>Excluded (11 rows)</summary>

| Organization | Work Cited | Citing Paper | Year | Matched Authors |
|---|---|---|---|---|
| Adobe | DPU | Few-Shot Graph Out-of-Distribution Detection with LLMs | 2025 | Yue Zhao, Haoyan Xu, Zhengtao Yao, Yushun Dong, Ziyi Wang, Ryan A. Rossi, Mengyuan Li |
| Brookhaven National Laboratory | Artificial Intelligence Foundation for… | Current and future directions in network biology | 2024 | Marinka Zitnik |
| Capital One | TODS | From Detection to Action: a Human-in-the-loop Toolkit for Anomaly Reasoning and Management | 2023 | Xueying Ding, Leman Akoglu |
| Google DeepMind | Artificial Intelligence Foundation for… | Scientific discovery in the age of artificial intelligence | 2023 | Tianfan Fu, Wenhao Gao, Kexin Huang, Jure Leskovec, Jimeng Sun, Connor W. Coley, Marinka Zitnik |
| Merck | Artificial Intelligence Foundation for… | Combinatorial prediction of therapeutic perturbations using causally inspired neural… | 2025 | Marinka Zitnik |
| Microsoft | Artificial Intelligence Foundation for… | Scientific discovery in the age of artificial intelligence | 2023 | Tianfan Fu, Wenhao Gao, Kexin Huang, Jure Leskovec, Jimeng Sun, Connor W. Coley, Marinka Zitnik |
| NVIDIA | Artificial Intelligence Foundation for… | Scientific discovery in the age of artificial intelligence | 2023 | Tianfan Fu, Wenhao Gao, Kexin Huang, Jure Leskovec, Jimeng Sun, Connor W. Coley, Marinka Zitnik |
| Novartis | Artificial Intelligence Foundation for… | Computer‐aided evaluation and exploration of chemical spaces constrained by reaction… | 2023 | Connor W. Coley |
| Pacific Northwest National Laboratory | Artificial Intelligence Foundation for… | Current and future directions in network biology | 2024 | Marinka Zitnik |
| Roche | Artificial Intelligence Foundation for… | Combinatorial prediction of therapeutic perturbations using causally inspired neural… | 2025 | Marinka Zitnik |
| Tencent | Contrastive Attributed Network Anomaly… | Improving Generalizability of Graph Anomaly Detection Models via Data Augmentation | 2023 | Xiao Huang |

</details>

## Coverage

- **OpenAlex**: stopped early, see the warning above; 0 works queried.
- **Dimensions**: 45 papers with citations, 79 indexed with zero citations, 4 not found: Grid-Bench: Can LLMs Predict How Discrete Worlds C... (arXiv preprint); agent-risk: Risk Assessment for Changes to AI Agen... (arXiv preprint); HPOD: Hyperparameter Optimization for Unsupervised... (AutoML, 2024); Revisiting Time Series Outlier Detection: Definiti... (NeurIPS, 2021).

Rows are deduplicated by (organization, normalized citing title, work cited). Legal entities of one company, a preprint and its journal version, and the two sources' records of one paper therefore count once. Recent preprints are indexed with a lag; re-run each semester.
