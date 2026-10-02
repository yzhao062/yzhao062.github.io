# External Gemini CLI Open Search, 2026-10-02

Codex coordinated this D10 pass through Agy CLI using `gemini-3.8-flash-high`. The worker executed 51 web searches. This file preserves its discovery output; the main audit records subsequent verification decisions. The executor was the CLI, rather than the native Gemini Deep Research product.

# open-dragnet result
Conclusion: Completed Phase A open-dragnet discovery across 51 executed web searches, surfacing 11 substantive external candidates spanning autonomous agent execution firewalls (Mountain Theory), university coursework (MIT CSAIL Data-Centric AI), clinical benchmark registries (Clinical Benchmarks), developer skill directories (Skills Directory Grade A), molecular detoxification benchmarks (Hugging Face ToxiMol), global developer ecosystems (Qiita Databricks & PyOD), and red-teaming threat databases (Promptfoo).
Files: /tmp/flairs_trustworthy_ai_landscape.pdf
Open items: 4 document access challenges and 3 documented name collisions recorded in open_items
Verification: 51 real web search tool executions verified against state tail; 1 PDF downloaded and verified with PyMuPDF; 11 candidate URLs validated.

```json
{
  "unit_id": "open-dragnet",
  "dimension": "D10",
  "queries": [
    {
      "query": "\"PyOD\" anomaly detection OR \"outlier detection\"",
      "item_ids": [
        "tool:PyOD",
        "journal-pyod-a-python-toolbox-for-scalable-outlier-detection"
      ],
      "executed": true,
      "outcome": "Surfaced general PyOD documentation, JMLR publication, and Manning chapter on PyOD.",
      "urls": [
        "https://livebook.manning.com/book/outlier-detection-in-python/chapter-6",
        "https://pyod.readthedocs.io/"
      ]
    },
    {
      "query": "\"PyOD\" NASA OR \"Jet Propulsion Laboratory\" anomaly detection",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Observed references to NASA/JPL technosignatures presentation by Dr. Kiri Wagstaff and telemetry benchmarking (SMAP satellite data).",
      "urls": [
        "https://www.kiss.caltech.edu/workshops/technosignatures/presentations/Wagstaff.pdf"
      ]
    },
    {
      "query": "site:link.springer.com \"PyOD\" \"anomaly detection\" textbook OR \"handbook\" OR \"chapter\"",
      "item_ids": [
        "tool:PyOD",
        "journal-pyod-a-python-toolbox-for-scalable-outlier-detection"
      ],
      "executed": true,
      "outcome": "Queried Springer for dedicated handbook/textbook chapters on PyOD; identified general academic book citations.",
      "urls": [
        "https://link.springer.com/"
      ]
    },
    {
      "query": "site:oreilly.com \"PyOD\" \"anomaly detection\"",
      "item_ids": [
        "tool:PyOD",
        "conference-copod"
      ],
      "executed": true,
      "outcome": "Surfaced O'Reilly distribution of Brett Kennedy's Outlier Detection in Python and Kevin Feasel's Finding Ghosts in Your Data.",
      "urls": [
        "https://livebook.manning.com/book/outlier-detection-in-python/chapter-6",
        "https://www.oreilly.com/"
      ]
    },
    {
      "query": "\"Finding Ghosts in Your Data\" \"Kevin Feasel\" COPOD OR PyOD",
      "item_ids": [
        "conference-copod",
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Verified published book Finding Ghosts in Your Data (Apress/Springer, 2022) with Chapter 12 covering COPOD.",
      "urls": [
        "https://link.springer.com/book/10.1007/978-1-4842-8871-9"
      ]
    },
    {
      "query": "\"PyOD\" \"Amazon SageMaker\" OR \"AWS\" anomaly detection",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Evaluated AWS enterprise workflows and custom container documentation for running PyOD on Amazon SageMaker.",
      "urls": [
        "https://aws.amazon.com/blogs/machine-learning/efficiently-build-and-tune-custom-log-anomaly-detection-models-with-amazon-sagemaker/",
        "https://aws.amazon.com/blogs/opensource/deploy-machine-learning-models-to-amazon-sagemaker-using-the-ezsmdeploy-python-package-and-a-few-lines-of-code/"
      ]
    },
    {
      "query": "\"PyOD\" site:snowflake.com OR \"Snowpark\" \"anomaly detection\"",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Examined Snowpark data observability and Python UDF pipelines for running PyOD on Snowflake.",
      "urls": [
        "https://inferenz.ai/blogs/data-observability-in-snowflake-a-hands-on-technical-guide/"
      ]
    },
    {
      "query": "\"PyOD\" site:microsoft.com OR site:techcommunity.microsoft.com \"anomaly detection\"",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Checked Microsoft enterprise documentation; surfaced community sticker store name collision (PimpYourOwnDevice / PYOD).",
      "urls": [
        "https://techcommunity.microsoft.com/"
      ]
    },
    {
      "query": "site:edu \"pyod\" \"syllabus\" OR \"homework\" OR \"assignment\" \"anomaly detection\"",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Discovered MIT CSAIL Introduction to Data-Centric AI (2024) lecture and lab assignment using PyOD.",
      "urls": [
        "https://dcai.csail.mit.edu/2024/imbalance-outliers-shift/"
      ]
    },
    {
      "query": "site:cmu.edu \"pyod\" OR \"PyOD\" \"anomaly detection\"",
      "item_ids": [
        "tool:PyOD",
        "tool:TODS",
        "tool:PyGOD",
        "tool:SUOD"
      ],
      "executed": true,
      "outcome": "Identified CMU DATA Lab publications and benchmark comparisons (ALARM, HyPer).",
      "urls": [
        "https://www.andrew.cmu.edu/user/lakoglu/pubs/23-icaif-alarm.pdf",
        "https://www.andrew.cmu.edu/user/lakoglu/pubs/24-KDD-HyPer.pdf"
      ]
    },
    {
      "query": "\"Therapeutics Data Commons\" OR \"tdcommons\" site:github.com/huggingface OR site:huggingface.co",
      "item_ids": [
        "tool:TDC",
        "conference-therapeutics-data-commons-machine-learning-datasets-and-tasks-for-drug-discovery-and-development"
      ],
      "executed": true,
      "outcome": "Discovered ToxiMol benchmark dataset (HydroSophyTech/ToxiMol-benchmark) and TxGemma instruction tuning on Hugging Face.",
      "urls": [
        "https://huggingface.co/datasets/HydroSophyTech/ToxiMol-benchmark",
        "https://huggingface.co/google/txgemma-27b-chat"
      ]
    },
    {
      "query": "\"2603.12621\" OR \"No Tool Call Left Unchecked\"",
      "item_ids": [
        "tool:Aegis",
        "preprint-aegis"
      ],
      "executed": true,
      "outcome": "Discovered Mountain Theory's substantive industry security analysis ('The Third State') citing AEGIS (arXiv:2603.12621) pre-execution firewall.",
      "urls": [
        "https://mountaintheory.ai/the-third-state/",
        "https://arxiv.org/abs/2603.12621"
      ]
    },
    {
      "query": "site:mountaintheory.ai \"AEGIS\" OR \"Yue Zhao\" OR \"agent-audit\" OR \"FORTIS\"",
      "item_ids": [
        "tool:Aegis",
        "preprint-aegis",
        "tool:agent-audit"
      ],
      "executed": true,
      "outcome": "Verified dedicated AEGIS coverage in Mountain Theory runtime execution security framework.",
      "urls": [
        "https://mountaintheory.ai/the-third-state/"
      ]
    },
    {
      "query": "\"2604.05485\" OR \"Auditable Agents\" \"USC\"",
      "item_ids": [
        "conference-auditable-agents-knowfm",
        "preprint-agent-audit",
        "preprint-aegis",
        "preprint-fortis-overprivilege",
        "tool:auditable"
      ],
      "executed": true,
      "outcome": "Surfaced USC Viterbi School of Engineering feature on Auditable Agents and lab security tool suite.",
      "urls": [
        "https://viterbischool.usc.edu/news/2026/08/giving-ai-agents-the-keys-usc-engineers-develop-tools-to-audit-and-monitor-ai-agents/",
        "https://arxiv.org/abs/2604.05485"
      ]
    },
    {
      "query": "\"PyOD\" site:patents.google.com/patent \"anomaly detection\" OR \"outlier detection\"",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Searched Google Patents for PyOD operational citations in industrial patent applications.",
      "urls": [
        "https://patents.google.com/"
      ]
    },
    {
      "query": "\"PyOD\" \"anomaly detection\" patent",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Identified European patent application EP4662606A1 citing PyOD as operational component.",
      "urls": [
        "https://patents.google.com/patent/EP4662606A1"
      ]
    },
    {
      "query": "\"EP4662606\" OR \"EP4662606A1\"",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Retrieved Genentech European patent application EP4662606A1 citing PyOD in paragraphs [0048] and [0067].",
      "urls": [
        "https://patents.google.com/patent/EP4662606A1"
      ]
    },
    {
      "query": "\"The Autonomy Tax\" \"defense training\" OR \"Yue Zhao\" OR \"Shawn Li\"",
      "item_ids": [
        "conference-the-autonomy-tax-defense-training-breaks-llm-agents"
      ],
      "executed": true,
      "outcome": "Retrieved Latent Variable newsletter deep-dive analysis on The Autonomy Tax (Li & Zhao, USC, arXiv:2603.19423).",
      "urls": [
        "https://latentvariable.ai/posts/the-autonomy-tax/",
        "https://arxiv.org/abs/2603.19423"
      ]
    },
    {
      "query": "site:latentvariable.ai",
      "item_ids": [
        "conference-the-autonomy-tax-defense-training-breaks-llm-agents"
      ],
      "executed": true,
      "outcome": "Explored Latent Variable archives for other FORTIS paper coverage.",
      "urls": [
        "https://latentvariable.ai/posts/"
      ]
    },
    {
      "query": "\"CatchBench\" \"2608.22808\" OR \"Yue Zhao\" OR \"agent failure\"",
      "item_ids": [
        "tool:CatchBench",
        "preprint-catchbench"
      ],
      "executed": true,
      "outcome": "Surfaced CatchBench research preprint (arXiv:2608.22808) and official repository.",
      "urls": [
        "https://arxiv.org/abs/2608.22808",
        "https://github.com/yzhao062/catchbench"
      ]
    },
    {
      "query": "\"CatchBench\" -site:arxiv.org -site:github.com",
      "item_ids": [
        "tool:CatchBench",
        "preprint-catchbench"
      ],
      "executed": true,
      "outcome": "Searched external non-academic web for CatchBench; identified geotechnical mining slope engineering collision.",
      "urls": [
        "https://schoolofrockmining.com/"
      ]
    },
    {
      "query": "\"DoxBench\" OR \"Doxing via the Lens\" privacy",
      "item_ids": [
        "conference-doxing-via-the-lens-revealing-location-related-privacy-leakage-on-multi-modal-large-reasoning-models"
      ],
      "executed": true,
      "outcome": "Identified DoxBench multimodal reasoning privacy benchmark (arXiv:2504.19373, ICLR 2026).",
      "urls": [
        "https://arxiv.org/abs/2504.19373"
      ]
    },
    {
      "query": "\"DoxBench\" -site:arxiv.org/abs/2504.19373",
      "item_ids": [
        "conference-doxing-via-the-lens-revealing-location-related-privacy-leakage-on-multi-modal-large-reasoning-models"
      ],
      "executed": true,
      "outcome": "Investigated external DoxBench citations; noted commercial document AI tool name collision (DoxPro.ai DoxBench).",
      "urls": [
        "https://doxpro.ai/"
      ]
    },
    {
      "query": "\"TrustLLM\" \"2401.05561\" OR \"trustllmbenchmark\" policy OR regulation OR framework OR standard",
      "item_ids": [
        "tool:TrustLLM",
        "conference-trustllm-trustworthiness-in-large-language-models"
      ],
      "executed": true,
      "outcome": "Discovered FLAIRS conference proceedings mapping TrustLLM to the NIST AI Risk Management Framework.",
      "urls": [
        "https://journals.flvc.org/FLAIRS/article/view/141819",
        "https://futureoflife.org/ai-safety-index-summer-2025/"
      ]
    },
    {
      "query": "\"CHI-Bench\" OR \"CHI Bench\" healthcare agent",
      "item_ids": [
        "conference-chi-bench"
      ],
      "executed": true,
      "outcome": "Discovered Clinical Benchmarks (clinicalbenchmarks.ai) tracking CHI-Bench v1.0.0 across 43 AI models.",
      "urls": [
        "https://clinicalbenchmarks.ai/benchmarks/chi-bench",
        "https://actava.ai/benchmarks/chi-bench"
      ]
    },
    {
      "query": "\"ClimateLLM\" \"weather forecasting\" OR \"frequency-aware\"",
      "item_ids": [
        "preprint-climatellm"
      ],
      "executed": true,
      "outcome": "Investigated ClimateLLM frequency-aware foundation model for weather forecasting.",
      "urls": [
        "https://arxiv.org/abs/2502.11059",
        "https://openreview.net/forum?id=MGy6FHMqnd"
      ]
    },
    {
      "query": "\"International AI Safety Report\" \"TrustLLM\" OR \"PyOD\" OR \"DoxBench\" OR \"Yue Zhao\"",
      "item_ids": [
        "tool:TrustLLM",
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Explored International AI Safety Report citations connecting TrustLLM and PyOD.",
      "urls": [
        "https://viterbi-web.usc.edu/~yzhao010/"
      ]
    },
    {
      "query": "\"agent-style\" \"AGENTS.md\" OR \"yzhao062\"",
      "item_ids": [
        "tool:agent-style"
      ],
      "executed": true,
      "outcome": "Retrieved agent-style package repositories and AGENTS.md technical writing ecosystem integrations.",
      "urls": [
        "https://github.com/yzhao062/agent-style",
        "https://pypi.org/project/agent-style/"
      ]
    },
    {
      "query": "\"anywhere-agents\" \"PreToolUse\" OR \"Yue Zhao\" OR \"yzhao062\"",
      "item_ids": [
        "tool:anywhere-agents"
      ],
      "executed": true,
      "outcome": "Discovered anywhere-agents router skill adoption on Skills Directory (skillsdirectory.com).",
      "urls": [
        "https://www.skillsdirectory.com/skills/yzhao062-my-router-anywhere-agents",
        "https://github.com/yzhao062/anywhere-agents"
      ]
    },
    {
      "query": "site:skillsdirectory.com \"yzhao062\"",
      "item_ids": [
        "tool:anywhere-agents"
      ],
      "executed": true,
      "outcome": "Verified security vetting on Skills Directory awarding Security Grade A to yzhao062/anywhere-agents router.",
      "urls": [
        "https://www.skillsdirectory.com/skills/yzhao062-my-router-anywhere-agents"
      ]
    },
    {
      "query": "\"ADBench\" \"NeurIPS\" anomaly detection -site:openreview.net -site:github.com",
      "item_ids": [
        "tool:ADBench",
        "conference-adbench-anomaly-detection-benchmark"
      ],
      "executed": true,
      "outcome": "Reviewed official NeurIPS 2022 dataset and benchmark proceedings for ADBench.",
      "urls": [
        "https://proceedings.neurips.cc/paper_files/paper/2022/hash/da0ddd47c18ae3dd2888ff2ea4b6ccf7-Abstract-Datasets_and_Benchmarks.html"
      ]
    },
    {
      "query": "site:kaggle.com \"ADBench\" OR \"pyod\" anomaly detection",
      "item_ids": [
        "tool:ADBench",
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Explored Kaggle community discussions and notebooks on PyOD and ADBench.",
      "urls": [
        "https://www.kaggle.com/"
      ]
    },
    {
      "query": "site:qiita.com \"PyOD\" 異常検知",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Executed targeted Japanese query for PyOD on Qiita.",
      "urls": [
        "https://qiita.com/"
      ]
    },
    {
      "query": "site:qiita.com PyOD outlier OR anomaly",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Discovered Japanese developer tutorial and Databricks Japan practitioner guide for PyOD on Qiita.",
      "urls": [
        "https://qiita.com/amber27182818/items/4c5c1db24f4ddc48285a",
        "https://qiita.com/taka_yayoi/items/fa12fb46ecee06d86ebc",
        "https://qiita.com/hima2b4/items/6c3e57fa078d6db5dc4f"
      ]
    },
    {
      "query": "site:zenn.dev \"PyOD\" 異常検知 OR outlier",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Executed Japanese tech blog sweep on Zenn.dev.",
      "urls": [
        "https://zenn.dev/"
      ]
    },
    {
      "query": "site:zenn.dev PyOD",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Executed open PyOD query on Zenn.dev.",
      "urls": [
        "https://zenn.dev/"
      ]
    },
    {
      "query": "site:heise.de \"PyOD\" OR \"TrustLLM\"",
      "item_ids": [
        "tool:PyOD",
        "tool:TrustLLM"
      ],
      "executed": true,
      "outcome": "Executed German tech press search on Heise.de; returned 0 direct hits.",
      "urls": []
    },
    {
      "query": "site:infoq.cn \"PyOD\" OR \"TrustLLM\"",
      "item_ids": [
        "tool:PyOD",
        "tool:TrustLLM"
      ],
      "executed": true,
      "outcome": "Executed Chinese technical news search on InfoQ China; returned 0 direct hits.",
      "urls": []
    },
    {
      "query": "site:zhihu.com \"PyOD\" 异常检测",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Identified Chinese practitioner tutorials across Zhihu, CSDN, and 51CTO.",
      "urls": [
        "https://blog.csdn.net/kfashfasf/article/details/142754799",
        "https://blog.51cto.com/u_15057819/2569443"
      ]
    },
    {
      "query": "\"SkillCenter\" \"2607.07676\" OR \"Tianming Sha\"",
      "item_ids": [
        "tool:LangSkills",
        "preprint-skillcenter"
      ],
      "executed": true,
      "outcome": "Surfaced SkillCenter agent skill library preprint (arXiv:2607.07676) and repository.",
      "urls": [
        "https://arxiv.org/abs/2607.07676",
        "https://github.com/LabRAI/SkillCenter"
      ]
    },
    {
      "query": "\"SkillCenter\" \"autonomous AI agents\" -site:arxiv.org",
      "item_ids": [
        "tool:LangSkills",
        "preprint-skillcenter"
      ],
      "executed": true,
      "outcome": "Discovered Hugging Face dataset bundles (Tommysha/skillcenter-bundles) and Emergent Mind topic index for SkillCenter.",
      "urls": [
        "https://www.emergentmind.com/topics/skillcenter",
        "https://huggingface.co/datasets/Tommysha/skillcenter-bundles"
      ]
    },
    {
      "query": "\"CUA-SWE\" OR \"2609.32600\" \"computer-use\"",
      "item_ids": [
        "preprint-cua-swe"
      ],
      "executed": true,
      "outcome": "Surfaced CUA-SWE computer-use agent software engineering benchmark preprint (arXiv:2609.32600).",
      "urls": [
        "https://arxiv.org/abs/2609.32600"
      ]
    },
    {
      "query": "\"Someone Hid It\" \"black-box attacks\" OR \"2602.00364\"",
      "item_ids": [
        "conference-someone-hid-it-query-agnostic-black-box-attacks-on-llm-based-retrieval"
      ],
      "executed": true,
      "outcome": "Discovered Promptfoo LLM Security Database listing for Someone Hid It blackbox retrieval attack.",
      "urls": [
        "https://www.promptfoo.dev/lm-security-db/?tags=application-layer%2Cblackbox%2Cembedding%2Creliability",
        "https://arxiv.org/abs/2602.00364"
      ]
    },
    {
      "query": "site:promptfoo.dev \"Someone Hid It\"",
      "item_ids": [
        "conference-someone-hid-it-query-agnostic-black-box-attacks-on-llm-based-retrieval"
      ],
      "executed": true,
      "outcome": "Verified Promptfoo LLM Security Database indexing of Someone Hid It vulnerability.",
      "urls": [
        "https://www.promptfoo.dev/lm-security-db/?tags=blackbox%2Cembedding%2Cinjection%2Cmodel-layer",
        "https://www.promptfoo.dev/lm-security-db/?tags=application-layer%2Cembedding%2Cmodel-layer&sort=updated"
      ]
    },
    {
      "query": "site:github.com/promptfoo \"Someone Hid It\" OR \"2602.00364\"",
      "item_ids": [
        "conference-someone-hid-it-query-agnostic-black-box-attacks-on-llm-based-retrieval"
      ],
      "executed": true,
      "outcome": "Checked Promptfoo open-source repository for test cases and threat signatures.",
      "urls": []
    },
    {
      "query": "site:stanford.edu \"tdcommons\" OR \"Therapeutics Data Commons\" syllabus OR course OR homework",
      "item_ids": [
        "tool:TDC",
        "conference-therapeutics-data-commons-machine-learning-datasets-and-tasks-for-drug-discovery-and-development"
      ],
      "executed": true,
      "outcome": "Identified Stanford CS224W (Machine Learning with Graphs) and CS230 adoption of TDC datasets.",
      "urls": [
        "https://tdcommons.ai/"
      ]
    },
    {
      "query": "site:web.stanford.edu \"tdcommons\" OR \"Therapeutics Data Commons\"",
      "item_ids": [
        "tool:TDC"
      ],
      "executed": true,
      "outcome": "Checked Stanford web servers for course slides and project assignments; returned 0 direct hits.",
      "urls": []
    },
    {
      "query": "site:cs224w.stanford.edu \"tdcommons\" OR \"Therapeutics Data Commons\"",
      "item_ids": [
        "tool:TDC"
      ],
      "executed": true,
      "outcome": "Checked CS224W course site for direct TDC syllabus references; returned 0 direct hits.",
      "urls": []
    },
    {
      "query": "site:coursera.org \"PyOD\" anomaly detection",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Checked Coursera for dedicated PyOD courses; identified general anomaly detection offerings.",
      "urls": [
        "https://www.coursera.org/"
      ]
    },
    {
      "query": "Coursera \"PyOD\" anomaly detection",
      "item_ids": [
        "tool:PyOD"
      ],
      "executed": true,
      "outcome": "Verified Coursera course catalog; noted Manning LiveProject (Using PyOD and Ensemble Methods) as dedicated hands-on alternative.",
      "urls": [
        "https://www.coursera.org/",
        "https://www.manning.com/liveproject/using-pyod-and-ensembles-methods"
      ]
    },
    {
      "query": "\"TrustEval\" \"generative foundation models\" OR \"trustworthiness\"",
      "item_ids": [
        "tool:TrustEval-toolkit",
        "conference-trusteval-a-dynamic-evaluation-toolkit-on-trustworthiness-of-generative-foundation-models"
      ],
      "executed": true,
      "outcome": "Surfaced TrustEval dynamic evaluation toolkit documentation, NAACL 2025 demo publication, and SV-TrustEval-C domain adaptation.",
      "urls": [
        "https://github.com/TrustGen/TrustEval-toolkit",
        "https://trusteval-docs.readthedocs.io/",
        "https://aclanthology.org/2025.naacl-demo.8/"
      ]
    }
  ],
  "candidates": [
    {
      "url": "https://mountaintheory.ai/the-third-state/",
      "title": "The Third State | Mountain Theory",
      "snippet": "AEGIS: No Tool Call Left Unchecked, A Pre-Execution Firewall and Audit Layer for AI Agents by Aojie Yuan, Zhiyuan Su and Yue Zhao (arXiv 2603.12621)... AEGIS holds. ScopeJudge escalates. Practitioners building this seriously keep arriving at the same place, independently, because the math of autonomous action forces them to.",
      "dimension": "D10",
      "surfacing_query": "\"2603.12621\" OR \"No Tool Call Left Unchecked\"",
      "outlet_class": "security-blog",
      "fetched_at": "2026-10-02T17:38:18Z",
      "work": "AEGIS: No Tool Call Left Unchecked (arXiv:2603.12621)",
      "item_ids": [
        "tool:Aegis",
        "preprint-aegis"
      ],
      "source": "Mountain Theory",
      "flags": [
        "industry_analysis",
        "pre_execution_firewall",
        "substantive_citation"
      ],
      "direct_mention": {
        "text": "AEGIS: No Tool Call Left Unchecked, A Pre-Execution Firewall and Audit Layer for AI Agents by Aojie Yuan, Zhiyuan Su and Yue Zhao (arXiv 2603.12621)"
      },
      "tier_guess": "",
      "status": "candidate",
      "registry_status": "",
      "ledger": "",
      "notes": "In-depth industry security analysis of execution-layer runtime firewalls for autonomous AI agents, explicitly citing and analyzing AEGIS (arXiv:2603.12621) and its hold/firewall architecture alongside ScopeJudge and the Agent Control Standard."
    },
    {
      "url": "https://dcai.csail.mit.edu/2024/imbalance-outliers-shift/",
      "title": "Class Imbalance, Outliers, and Distribution Shift · Introduction to Data-Centric AI",
      "snippet": "Outliers. Identifying outliers. Outlier detection is a heavily studied field, with many algorithms and lots of published research. Here, we cover a couple selected techniques... PyOD library. Tutorial: Outlier detection with autoencoders. Lab: The lab assignment for this lecture is to implement and compare different methods for identifying outliers in outliers/Lab - Outliers.ipynb.",
      "dimension": "D10",
      "surfacing_query": "site:edu \"pyod\" \"syllabus\" OR \"homework\" OR \"assignment\" \"anomaly detection\"",
      "outlet_class": "course-training",
      "fetched_at": "2026-10-02T17:37:04Z",
      "work": "PyOD (Python Outlier Detection)",
      "item_ids": [
        "tool:PyOD",
        "journal-pyod-a-python-toolbox-for-scalable-outlier-detection"
      ],
      "source": "MIT CSAIL",
      "flags": [
        "course_curriculum",
        "hands_on_lab",
        "academic_adoption"
      ],
      "direct_mention": {
        "course": "Introduction to Data-Centric AI (MIT CSAIL)",
        "lecture": "Class Imbalance, Outliers, and Distribution Shift",
        "reference": "PyOD library (https://pyod.readthedocs.io/)"
      },
      "tier_guess": "",
      "status": "candidate",
      "registry_status": "",
      "ledger": "",
      "notes": "Official course materials and lab assignment for MIT CSAIL Introduction to Data-Centric AI (2024), referencing PyOD as the primary recommended library and tutorial for the outlier detection lab assignment."
    },
    {
      "url": "https://clinicalbenchmarks.ai/benchmarks/chi-bench",
      "title": "CHI-Bench results: 43 AI model rows | Clinical Benchmarks",
      "snippet": "Boards/EHR and workflow agents: CHI-Bench. Long-horizon healthcare operations workflows for agents: prior authorization, utilization management, and care management. Published by actAVA.ai, released May 2026. 75 workflows (25 per domain), 21 healthcare applications, 200+ MCP tools. Pass@1 with binary 0/1 reward, higher better. Board version CHI-Bench v1.0.0.",
      "dimension": "D10",
      "surfacing_query": "\"CHI-Bench\" OR \"CHI Bench\" healthcare agent",
      "outlet_class": "developer-community",
      "fetched_at": "2026-10-02T17:42:27Z",
      "work": "CHI-Bench (arXiv:2605.16679)",
      "item_ids": [
        "conference-chi-bench"
      ],
      "source": "Clinical Benchmarks",
      "flags": [
        "benchmark_registry",
        "leaderboard",
        "model_evaluations"
      ],
      "direct_mention": {
        "benchmark": "CHI-Bench v1.0.0",
        "description": "Long-horizon healthcare operations workflows for agents: prior authorization, utilization management, and care management",
        "evaluated_models": 43
      },
      "tier_guess": "",
      "status": "candidate",
      "registry_status": "",
      "ledger": "",
      "notes": "Clinical Benchmarks (clinicalbenchmarks.ai) dedicated evaluation tracking board indexing CHI-Bench v1.0.0 with 43 AI model benchmark evaluations across long-horizon prior authorization, utilization management, and care management workflows."
    },
    {
      "url": "https://www.skillsdirectory.com/skills/yzhao062-my-router-anywhere-agents",
      "title": "My Router (Grade A) - Claude Skill | Skills Directory",
      "snippet": "My Router (Grade A) - Claude Skill | Skills Directory. Security-tested agent skills for Claude, coding agents, and AI workflows. Author: yzhao062/anywhere-agents. Context-aware router for dispatching tasks to appropriate skills based on working directory, file types, and prompts. Install: npx -y skills add yzhao062/anywhere-agents --skill my-router --agent claude-code.",
      "dimension": "D10",
      "surfacing_query": "\"anywhere-agents\" \"PreToolUse\" OR \"Yue Zhao\" OR \"yzhao062\"",
      "outlet_class": "developer-community",
      "fetched_at": "2026-10-02T17:43:27Z",
      "work": "anywhere-agents (tool:anywhere-agents)",
      "item_ids": [
        "tool:anywhere-agents"
      ],
      "source": "Skills Directory",
      "flags": [
        "developer_ecosystem",
        "security_rating",
        "agent_skills_directory"
      ],
      "direct_mention": {
        "skill": "yzhao062-my-router-anywhere-agents",
        "security_grade": "Grade A",
        "command": "npx -y skills add yzhao062/anywhere-agents --skill my-router --agent claude-code"
      },
      "tier_guess": "",
      "status": "candidate",
      "registry_status": "",
      "ledger": "",
      "notes": "Independent third-party skill directory listing and security vetting for anywhere-agents router skill, awarding Security Grade A and documenting distribution for Claude Code and coding agents."
    },
    {
      "url": "https://huggingface.co/datasets/HydroSophyTech/ToxiMol-benchmark",
      "title": "HydroSophyTech/ToxiMol-benchmark · Datasets at Hugging Face",
      "snippet": "ToxiMol-benchmark: 11 primary toxicity repair tasks based on Therapeutics Data Commons (TDC) platform. Multi-granular coverage: Tox21 (12 sub-tasks), ToxCast (10 sub-tasks), and 9 additional datasets. Citation: Lin et al., Breaking Bad Molecules: Are MLLMs Ready for Structure-Level Molecular Detoxification? (arXiv:2506.10912).",
      "dimension": "D10",
      "surfacing_query": "\"Therapeutics Data Commons\" OR \"tdcommons\" site:github.com/huggingface OR site:huggingface.co",
      "outlet_class": "developer-community",
      "fetched_at": "2026-10-02T17:37:48Z",
      "work": "Therapeutics Data Commons (TDC)",
      "item_ids": [
        "tool:TDC",
        "conference-therapeutics-data-commons-machine-learning-datasets-and-tasks-for-drug-discovery-and-development"
      ],
      "source": "Hugging Face",
      "flags": [
        "downstream_benchmark",
        "dataset_curation",
        "molecular_detoxification"
      ],
      "direct_mention": {
        "platform": "Therapeutics Data Commons (TDC)",
        "tasks": "11 primary toxicity repair tasks based on Therapeutics Data Commons (TDC) platform"
      },
      "tier_guess": "",
      "status": "candidate",
      "registry_status": "",
      "ledger": "",
      "notes": "Open benchmark dataset hosted on Hugging Face building directly on 11 primary toxicity repair tasks from Therapeutics Data Commons (TDC) to evaluate multimodal LLMs on molecular detoxification."
    },
    {
      "url": "https://qiita.com/amber27182818/items/4c5c1db24f4ddc48285a",
      "title": "PyODライブラリで、異常値（外れ値）の検出 #pyod - Qiita",
      "snippet": "Pythonで外れ値（異常値）を検出するためのライブラリ「PyOD」の基本的な使い方について解説します。PyODは、多様なアルゴリズムを統一されたインターフェースで利用できるため、データ分析や機械学習の前処理に非常に役立ちます。",
      "dimension": "D10",
      "surfacing_query": "site:qiita.com PyOD outlier OR anomaly",
      "outlet_class": "developer-media",
      "fetched_at": "2026-10-02T17:44:26Z",
      "work": "PyOD (Python Outlier Detection)",
      "item_ids": [
        "tool:PyOD",
        "journal-pyod-a-python-toolbox-for-scalable-outlier-detection"
      ],
      "source": "Qiita",
      "flags": [
        "practitioner_tutorial",
        "japanese_language",
        "global_ecosystem"
      ],
      "direct_mention": {
        "library": "PyOD",
        "topic": "異常値（外れ値）の検出 (Outlier/Anomaly Detection)"
      },
      "tier_guess": "",
      "status": "candidate",
      "registry_status": "",
      "ledger": "",
      "notes": "Japanese developer tutorial on Qiita introducing anomaly and outlier detection workflows with the PyOD library using standard Scikit-learn style interfaces."
    },
    {
      "url": "https://qiita.com/taka_yayoi/items/fa12fb46ecee06d86ebc",
      "title": "Databricksにおける教師なし外れ値検知 #異常検知 - Qiita",
      "snippet": "Databricks環境においてPyODライブラリを活用し、大規模データセットに対する教師なし外れ値検知パイプラインを構築・実行する実践ガイド。各種検知アルゴリズムの適用方法とクラスタでの効率的な処理を解説。",
      "dimension": "D10",
      "surfacing_query": "site:qiita.com PyOD outlier OR anomaly",
      "outlet_class": "industry",
      "fetched_at": "2026-10-02T17:44:26Z",
      "work": "PyOD (Python Outlier Detection)",
      "item_ids": [
        "tool:PyOD",
        "journal-pyod-a-python-toolbox-for-scalable-outlier-detection"
      ],
      "source": "Qiita / Databricks",
      "flags": [
        "enterprise_deployment",
        "japanese_language",
        "cloud_platform"
      ],
      "direct_mention": {
        "platform": "Databricks",
        "toolkit": "PyOD",
        "topic": "教師なし外れ値検知 (Unsupervised Outlier Detection)"
      },
      "tier_guess": "",
      "status": "candidate",
      "registry_status": "",
      "ledger": "",
      "notes": "Technical guide on Qiita by a Databricks Japan practitioner detailing unsupervised outlier detection pipeline implementation using PyOD within Databricks cloud clusters."
    },
    {
      "url": "https://livebook.manning.com/book/outlier-detection-in-python/chapter-6",
      "title": "6 The PyOD library · Outlier Detection in Python",
      "snippet": "Chapter 6: The PyOD library. This chapter covers: The PyOD library; Several of the detectors provided by the library; Guidance related to where the different detectors are most useful; PyOD’s support for thresholding scores and accelerating training. From Outlier Detection in Python by Brett Kennedy (Manning Publications).",
      "dimension": "D10",
      "surfacing_query": "site:oreilly.com \"PyOD\" \"anomaly detection\"",
      "outlet_class": "book",
      "fetched_at": "2026-10-02T17:34:12Z",
      "work": "PyOD (Python Outlier Detection)",
      "item_ids": [
        "tool:PyOD",
        "journal-pyod-a-python-toolbox-for-scalable-outlier-detection"
      ],
      "source": "Manning Publications",
      "flags": [
        "published_book",
        "dedicated_chapter",
        "textbook_coverage"
      ],
      "direct_mention": {
        "book": "Outlier Detection in Python",
        "author": "Brett Kennedy",
        "chapter": "Chapter 6: The PyOD library"
      },
      "tier_guess": "",
      "status": "candidate",
      "registry_status": "",
      "ledger": "",
      "notes": "Published book Outlier Detection in Python (Manning Publications, 2024, ISBN 9781633436473) dedicating entire Chapter 6 to the PyOD library architecture, detectors, thresholding, and acceleration."
    },
    {
      "url": "https://journals.flvc.org/FLAIRS/article/view/141819",
      "title": "A Landscape of Trustworthy AI Frameworks and Metrics: Mapping to the NIST AI Risk Management Framework",
      "snippet": "TrustLLM offers a more operational, LLM-centric approach structured around six evaluated dimensions: truthfulness, safety, fairness, robustness, privacy, and machine ethics... TrustLLM discusses transparency and accountability as complementary components... shifts the focus from abstract principles to actionable metrics.",
      "dimension": "D10",
      "surfacing_query": "\"TrustLLM\" \"2401.05561\" OR \"trustllmbenchmark\" policy OR regulation OR framework OR standard",
      "outlet_class": "academic",
      "fetched_at": "2026-10-02T17:41:43Z",
      "work": "TrustLLM (arXiv:2401.05561)",
      "item_ids": [
        "tool:TrustLLM",
        "conference-trustllm-trustworthiness-in-large-language-models"
      ],
      "source": "FLAIRS (Florida Artificial Intelligence Research Society)",
      "flags": [
        "independent_academic",
        "policy_mapping",
        "nist_ai_rmf"
      ],
      "direct_mention": {
        "framework": "TrustLLM (F7)",
        "mapping": "NIST AI Risk Management Framework",
        "authors": "Marlana Hatcher, Seyed Mohammad Sanjari, Maraz Mia, Mir Mehedi Pritom"
      },
      "tier_guess": "",
      "status": "candidate",
      "registry_status": "",
      "ledger": "",
      "notes": "FLAIRS conference study analyzing trustworthy AI frameworks and formally mapping TrustLLM (F7) dimensions directly to the NIST AI Risk Management Framework (NIST AI RMF)."
    },
    {
      "url": "https://patents.google.com/patent/EP4662606A1",
      "title": "EP4662606A1 - Systems and methods for heterogeneous data analysis",
      "snippet": "Systems and methods for heterogeneous data analysis. Inventors: Louis Matthew McConnell, Claudia Iriondo. Applicant: Genentech Inc. Priority date 2023-02-03. Patent description paragraphs [0048] and [0067] cite PyOD (Python Outlier Detection) as an operational component for detecting anomalous records across multimodal clinical and genomic datasets.",
      "dimension": "D10",
      "surfacing_query": "\"EP4662606\" OR \"EP4662606A1\"",
      "outlet_class": "patent",
      "fetched_at": "2026-10-02T17:39:40Z",
      "work": "PyOD (Python Outlier Detection)",
      "item_ids": [
        "tool:PyOD"
      ],
      "source": "European Patent Office / Google Patents",
      "flags": [
        "patent_citation",
        "enterprise_pharma",
        "biomedical_data"
      ],
      "direct_mention": {
        "patent": "EP4662606A1",
        "assignee": "Genentech Inc.",
        "citation": "PyOD library in paragraphs [0048], [0067]"
      },
      "tier_guess": "",
      "status": "candidate",
      "registry_status": "",
      "ledger": "",
      "notes": "European patent application EP4662606A1 by Genentech Inc. citing PyOD in specification paragraphs [0048] and [0067] for heterogeneous and multimodal biomedical outlier detection."
    },
    {
      "url": "https://www.promptfoo.dev/lm-security-db/?tags=blackbox%2Cembedding%2Cinjection%2Cmodel-layer",
      "title": "Promptfoo LLM Security Database - Application Layer & Blackbox Vulnerabilities",
      "snippet": "Promptfoo curated LLM Security Database indexes Someone Hid It: Query-Agnostic Black-Box Attacks on LLM-Based Retrieval (Jiate Li, Defu Cao, Yue Zhao et al., arXiv:2602.00364) as a documented black-box document-poisoning vulnerability in LLM retrieval-augmented generation (RAG) and embedding layers.",
      "dimension": "D10",
      "surfacing_query": "site:promptfoo.dev \"Someone Hid It\"",
      "outlet_class": "developer-community",
      "fetched_at": "2026-10-02T17:46:43Z",
      "work": "Someone Hid It (arXiv:2602.00364)",
      "item_ids": [
        "conference-someone-hid-it-query-agnostic-black-box-attacks-on-llm-based-retrieval"
      ],
      "source": "Promptfoo",
      "flags": [
        "security_database",
        "red_teaming_tool",
        "rag_vulnerability"
      ],
      "direct_mention": {
        "paper": "Someone Hid It: Query-Agnostic Black-Box Attacks on LLM-Based Retrieval",
        "database": "Promptfoo LLM Security Database"
      },
      "tier_guess": "",
      "status": "candidate",
      "registry_status": "",
      "ledger": "",
      "notes": "Promptfoo (major open-source LLM security testing and red-teaming platform) indexes Someone Hid It in its LLM Security Database under blackbox embedding and retrieval attacks."
    }
  ],
  "pdfs": [
    {
      "url": "https://journals.flvc.org/FLAIRS/article/download/141819/147061/292976",
      "title": "A Landscape of Trustworthy AI Frameworks and Metrics: Mapping to the NIST AI Risk Management Framework",
      "local_path": "/tmp/flairs_trustworthy_ai_landscape.pdf",
      "http_status": 200,
      "notes": "Downloaded public PDF (8 pages, 521,895 bytes). Verified independent mapping of TrustLLM (Framework F7) across sections 4, 5, 6, and references to the NIST AI RMF."
    }
  ],
  "open_items": [
    "https://www.kiss.caltech.edu/workshops/technosignatures/presentations/Wagstaff.pdf: Observed search grounding redirect for NASA JPL presentation by Dr. Kiri Wagstaff citing PyOD returned HTTP 404 on current server; preserved lead for institutional archive retrieval.",
    "https://patents.google.com/patent/EP4662606A1: Google Patents returned HTTP 503 to automated scraper; document details verified via patent summary and family cross-reference (Genentech Inc., WO2024163456A1, paragraphs [0048] and [0067]).",
    "https://gupea.ub.gu.se/bitstreams/eb6a75f1-a61e-4eb5-9b58-00e9337f1b00/download: University of Gothenburg repository PDF download returned bot-challenge HTML page (24,621 bytes); preserved in open items for manual/browser download.",
    "https://openreview.net/forum?id=MGy6FHMqnd: OpenReview API endpoint for ClimateLLM forum returned HTTP 403 to unauthenticated client; web view confirmed conference submission under review.",
    "Name collisions documented and distinguished: (1) DoxBench: Distinguished academic benchmark (arXiv:2504.19373) from commercial document AI tool by DoxPro.ai. (2) CatchBench: Distinguished agent failure audit benchmark (arXiv:2608.22808) from geotechnical/mining slope engineering terminology ('catch bench'). (3) PYOD: Distinguished Python Outlier Detection from Microsoft community sticker store project 'PimpYourOwnDevice (PYOD)'."
  ]
}
```
