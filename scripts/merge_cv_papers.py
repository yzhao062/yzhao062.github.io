#!/usr/bin/env python3
"""Merge CV papers into publications.json: add missing papers, fix sections, fetch abstracts."""

import json
import re
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = REPO_ROOT / "data" / "publications.json"

# ── New preprint entries (28 papers) ──────────────────────────────────────
NEW_PREPRINTS = [
    {"id": "preprint-autonomy-tax", "title": "The Autonomy Tax: Defense Training Breaks LLM Agents", "paper_url": "https://arxiv.org/abs/2603.19423", "authors": "Shawn Li, Yue Zhao", "year": 2026},
    {"id": "preprint-implicit-execution-tracing", "title": "When Only the Final Text Survives: Implicit Execution Tracing for Multi-Agent Attribution", "paper_url": "https://arxiv.org/abs/2603.17445", "authors": "Yi Nian, Haosen Cao, Shenzhe Zhu, Henry Peng Zou, Qingqing Luan, Yue Zhao", "year": 2026},
    {"id": "preprint-sovereign-os", "title": "Sovereign-OS: A Charter-Governed Operating System for Autonomous AI Agents with Verifiable Fiscal Discipline", "paper_url": "https://arxiv.org/abs/2603.14011", "authors": "Aojie Yuan, Haiyue Zhang, Ziyi Wang, Yue Zhao", "year": 2026},
    {"id": "preprint-aegis", "title": "AEGIS: No Tool Call Left Unchecked -- A Pre-Execution Firewall and Audit Layer for AI Agents", "paper_url": "https://arxiv.org/abs/2603.12621", "authors": "Aojie Yuan, Zhiyuan Su, Yue Zhao", "year": 2026},
    {"id": "preprint-benchmarking-knowledge-extraction-rag", "title": "Benchmarking Knowledge-Extraction Attack and Defense on Retrieval-Augmented Generation", "paper_url": "https://arxiv.org/abs/2602.09319", "authors": "Zhisheng Qi, Utkarsh Sahu, Li Ma, Haoyu Han, Ryan Rossi, Franck Dernoncourt, Mahantesh Halappanavar, Nesreen Ahmed, Yushun Dong, Yue Zhao, Yu Zhang, Yu Wang", "year": 2026},
    {"id": "preprint-agent-banana", "title": "Agent Banana: High-Fidelity Image Editing with Agentic Thinking and Tooling", "paper_url": "https://arxiv.org/abs/2602.09084", "authors": "Ruijie Ye, Jiayi Zhang, Zhuoxin Liu, Zihao Zhu, Siyuan Yang, Li Li, Tianfu Fu, Franck Dernoncourt, Yue Zhao, Jiacheng Zhu, Ryan Rossi, Wenhao Chai, Zhengzhong Tu", "year": 2026},
    {"id": "preprint-someone-hid-it", "title": "\"Someone Hid It\": Query-Agnostic Black-Box Attacks on LLM-Based Retrieval", "paper_url": "https://arxiv.org/abs/2602.00364", "authors": "Jiate Li, Defu Cao, Li Li, Wei Yang, Yuehan Qin, Chenxiao Yu, Tiannuo Yang, Ryan A. Rossi, Yan Liu, Xiyang Hu, Yue Zhao", "year": 2026},
    {"id": "preprint-defenses-prompt-attacks-surface-heuristics", "title": "Defenses Against Prompt Attacks Learn Surface Heuristics", "paper_url": "https://arxiv.org/abs/2601.07185", "authors": "Shawn Li, Chenxiao Yu, Zhiyu Ni, Hao Li, Charith Peris, Chaowei Xiao, Yue Zhao", "year": 2026},
    {"id": "preprint-fairness-or-fluency", "title": "Fairness or Fluency? An Investigation into Language Bias of Pairwise LLM-as-a-Judge", "paper_url": "https://arxiv.org/abs/2601.13649", "authors": "Xiaolin Zhou, Zheng Luo, Yicheng Gao, Qixuan Chen, Xiyang Hu, Yue Zhao, Ruishan Liu", "year": 2026},
    {"id": "preprint-tracing-moral-foundations", "title": "Tracing Moral Foundations in Large Language Models", "paper_url": "https://arxiv.org/abs/2601.05437", "authors": "Chenxiao Yu, Bowen Yi, Farzan Karimi-Malekabadi, Suhaib Abdurahman, Jinyi Ye, Shrikanth Narayanan, Yue Zhao, Morteza Dehghani", "year": 2026},
    {"id": "preprint-multimodal-geo", "title": "Multimodal Generative Engine Optimization: Rank Manipulation for Vision-Language Model Rankers", "paper_url": "https://arxiv.org/abs/2601.12263", "authors": "Yixuan Du, Chenxiao Yu, Haoyan Xu, Ziyi Wang, Yue Zhao, Xiyang Hu", "year": 2026},
    {"id": "preprint-topology-matters", "title": "Topology Matters: Measuring Memory Leakage in Multi-Agent LLMs", "paper_url": "https://arxiv.org/abs/2512.04668", "authors": "Jinbo Liu, Defu Cao, Yifei Wei, Tianyao Su, Yuan Liang, Yushun Dong, Yan Liu, Yue Zhao, Xiyang Hu", "year": 2025},
    {"id": "preprint-tagfn", "title": "TAGFN: A Text-Attributed Graph Dataset for Fake News Detection in the Age of LLMs", "paper_url": "https://arxiv.org/abs/2511.21624", "authors": "Kay Liu, Yuwei Han, Haoyan Xu, Henry Peng Zou, Yue Zhao, Philip S. Yu", "year": 2025},
    {"id": "preprint-tag-ad", "title": "LLM-Powered Text-Attributed Graph Anomaly Detection via Retrieval-Augmented Reasoning", "paper_url": "https://arxiv.org/abs/2511.17584", "authors": "Haoyan Xu, Ruizhi Qian, Zhengtao Yao, Ziyi Liu, Li Li, Yuqi Li, Yanshu Li, Wenqing Zheng, Daniele Rosa, Daniel Barcklow, Senthil Kumar, Jieyu Zhao, Yue Zhao", "year": 2025},
    {"id": "preprint-mea-graph-foundation", "title": "A Systematic Study of Model Extraction Attacks on Graph Foundation Models", "paper_url": "https://arxiv.org/abs/2511.11912", "authors": "Haoyan Xu, Ruizhi Qian, Jiate Li, Yushun Dong, Minghao Lin, Hanson Yan, Zhengtao Yao, Qinghua Liu, Junhao Dong, Ruopeng Huang, Yue Zhao, Mengyuan Li", "year": 2025},
    {"id": "preprint-computing-resources-fm", "title": "The Role of Computing Resources in Publishing Foundation Model Research", "paper_url": "https://arxiv.org/abs/2510.13621", "authors": "Yuexing Hao, Yue Huang, Haoran Zhang, Chenyang Zhao, Zhenwen Liang, Paul Pu Liang, Yue Zhao, Lichao Sun, Saleh Kalantari, Xiangliang Zhang, Marzyeh Ghassemi", "year": 2025},
    {"id": "preprint-learning-route-llms-bandit", "title": "Learning to Route LLMs from Bandit Feedback: One Policy, Many Trade-offs", "paper_url": "https://arxiv.org/abs/2510.07429", "authors": "Wang Wei, Tiankai Yang, Hongjie Chen, Yue Zhao, Franck Dernoncourt, Ryan A. Rossi, Hoda Eldardiry", "year": 2025},
    {"id": "preprint-mole-pair", "title": "Can Molecular Foundation Models Know What They Don't Know? A Simple Remedy with Preference Optimization", "paper_url": "https://arxiv.org/abs/2509.25509", "authors": "Langzhou He, Junyou Zhu, Fangxin Wang, Junhua Liu, Haoyan Xu, Yue Zhao, Philip S. Yu, Qitian Wu", "year": 2025},
    {"id": "preprint-m3ood", "title": "M3OOD: Automatic Selection of Multimodal OOD Detectors", "paper_url": "https://arxiv.org/abs/2508.11936", "authors": "Yuehan Qin, Li Li, Defu Cao, Tiankai Yang, Jiate Li, Yue Zhao", "year": 2025},
    {"id": "preprint-glip-ood", "title": "GLIP-OOD: Zero-Shot Graph OOD Detection with Graph Foundation Model", "paper_url": "https://arxiv.org/abs/2504.21186", "authors": "Haoyan Xu, Zhengtao Yao, Xuzhi Zhang, Ziyi Wang, Langzhou He, Yushun Dong, Philip S. Yu, Mengyuan Li, Yue Zhao", "year": 2025},
    {"id": "preprint-goe-llm", "title": "Graph Synthetic Out-of-Distribution Exposure with Large Language Models", "paper_url": "https://arxiv.org/abs/2504.21198", "authors": "Haoyan Xu, Zhengtao Yao, Ziyi Wang, Zhan Cheng, Xiyang Hu, Mengyuan Li, Yue Zhao", "year": 2025},
    {"id": "preprint-stealthrank", "title": "StealthRank: LLM Ranking Manipulation via Stealthy Prompt Optimization", "paper_url": "https://arxiv.org/abs/2504.05804", "authors": "Yiming Tang, Yi Fan, Chenxiao Yu, Tiankai Yang, Yue Zhao, Xiyang Hu", "year": 2025},
    {"id": "preprint-survey-mea-distributed", "title": "A Survey of Model Extraction Attacks and Defenses in Distributed Computing Environments", "paper_url": "https://arxiv.org/abs/2502.16065", "authors": "Kaixiang Zhao, Lincan Li, Kaize Ding, Neil Zhenqiang Gong, Yue Zhao, Yushun Dong", "year": 2025},
    {"id": "preprint-climatellm", "title": "ClimateLLM: Efficient Weather Forecasting via Frequency-Aware Large Language Models", "paper_url": "https://arxiv.org/abs/2502.11059", "authors": "Shixuan Li, Wei Yang, Peiyu Zhang, Xiongye Xiao, Defu Cao, Yuehan Qin, Xiaole Zhang, Yue Zhao, Paul Bogdan", "year": 2025},
    {"id": "preprint-political-llm", "title": "Political-LLM: Large Language Models in Political Science", "paper_url": "https://arxiv.org/abs/2412.06864", "authors": "Lincan Li, Jiaqi Li, Catherine Chen, Fred Gui, and many others, Yue Zhao, Yushun Dong", "year": 2024},
    {"id": "preprint-llm-political-simulation", "title": "A Large-Scale Simulation on Large Language Models for Decision-Making in Political Science", "paper_url": "https://arxiv.org/abs/2412.15291", "authors": "Chenxiao Yu, Jinyi Ye, Yuangang Li, Zheng Li, Emilio Ferrara, Xiyang Hu, Yue Zhao", "year": 2024},
    {"id": "preprint-personalized-mllm-survey", "title": "Personalized Multimodal Large Language Models: A Survey", "paper_url": "https://arxiv.org/abs/2412.02142", "authors": "Junda Wu, Hanjia Lyu, Yu Xia, and many others, Yue Zhao, Jiebo Luo, Julian McAuley", "year": 2024},
]

# ── AutoBench-V (was preprint, now accepted as workshop) ──────────────
AUTOBENCH_V = {
    "id": "workshop-autobench-v",
    "section": "workshop",
    "title": "AutoBench-V: Can Large Vision-Language Models Benchmark Themselves?",
    "paper_url": "https://arxiv.org/abs/2410.21259",
    "authors": "Han Bao, Yue Huang, Yanbo Wang, Jiayi Ye, Xiangqi Wang, Xiuying Chen, Yue Zhao, Tianyi Zhou, Mohamed Elhoseiny, Xiangliang Zhang",
    "venue": "ICML 2025 DataWorld Workshop",
    "year": 2024,
    "show_on_website": False,
    "links": [],
}

# ── Old conference/workshop papers (16 papers) ───────────────────────
NEW_OLD_PAPERS = [
    {"id": "conference-contrastive-attributed-network-ad", "section": "conference", "title": "Contrastive Attributed Network Anomaly Detection with Data Augmentation", "paper_url": "https://link.springer.com/chapter/10.1007/978-3-031-05936-0_35", "authors": "Zhiming Xu, Xiao Huang, Yue Zhao, Yushun Dong, Jundong Li", "venue": "PAKDD, 2022", "year": 2022},
    {"id": "workshop-tods", "section": "workshop", "title": "TODS: An Automated Time Series Outlier Detection System", "paper_url": "https://ojs.aaai.org/index.php/AAAI/article/view/18012", "authors": "Kwei-Herng Lai, Daochen Zha, Guanchu Wang, Junjie Xu, Yue Zhao, Devesh Kumar, Yile Chen, Purav Zumkhawaka, Mingyang Wan, Diego Martinez, Xia Hu", "venue": "AAAI (Demo), 2021", "year": 2021},
    {"id": "conference-autoaudit", "section": "conference", "title": "AutoAudit: Mining Accounting and Time-Evolving Graphs", "paper_url": "https://ieeexplore.ieee.org/document/9378346/", "authors": "Meng-Chieh Lee, Yue Zhao, Aluna Wang, Pierre Jinghong Liang, Leman Akoglu, Vincent S. Tseng, Christos Faloutsos", "venue": "IEEE BigData, 2020", "year": 2020},
    {"id": "conference-data-denoising-scrna", "section": "conference", "title": "A Data Denoising Approach to Optimize Functional Clustering of Single Cell RNA-sequencing Data", "paper_url": "https://ieeexplore.ieee.org/document/9313483/", "authors": "Changlin Wan, Dongya Jia, Yue Zhao, Wennan Chang, Sha Cao, Xiao Wang, Chi Zhang", "venue": "IEEE BIBM, 2020", "year": 2020},
    {"id": "workshop-suod-aaai2020", "section": "workshop", "title": "SUOD: Toward Scalable Unsupervised Outlier Detection", "paper_url": "https://arxiv.org/abs/2002.03222", "authors": "Yue Zhao, Xiyang Hu, Cheng Cheng, Cong Wang, Changlin Wan, Wen Wang, Jianing Yang, Haoping Bai, Zheng Li, Cao Xiao, Yunlong Wang, Zhi Qiao, Jiaze Sun, Leman Akoglu", "venue": "AAAI Workshop, 2020", "year": 2020},
    {"id": "conference-copod", "section": "conference", "title": "COPOD: Copula-Based Outlier Detection", "paper_url": "https://ieeexplore.ieee.org/document/9338429/", "authors": "Zheng Li, Yue Zhao, Nicola Botta, Cezar Ionescu, Xiyang Hu", "venue": "IEEE ICDM, 2020", "year": 2020},
    {"id": "workshop-sync-icdmw", "section": "workshop", "title": "SynC: A Copula based Framework for Generating Synthetic Data from Aggregated Sources", "paper_url": "https://ieeexplore.ieee.org/document/9346329/", "authors": "Zheng Li, Yue Zhao, Jialin Fu", "venue": "IEEE ICDMW, 2020", "year": 2020},
    {"id": "conference-dsr", "section": "conference", "title": "DSR: An Accurate Single Image Super Resolution Approach for Various Degradations", "paper_url": "https://ieeexplore.ieee.org/document/9102941/", "authors": "Yiqun Mei, Yue Zhao, Wei Liang", "venue": "IEEE ICME, 2020", "year": 2020},
    {"id": "workshop-combo", "section": "workshop", "title": "Combining Machine Learning Models and Scores using combo Library", "paper_url": "https://ojs.aaai.org/index.php/AAAI/article/view/7111", "authors": "Yue Zhao, Xuejian Wang, Cheng Cheng, Xueying Ding", "venue": "AAAI (Demo), 2020", "year": 2020},
    {"id": "workshop-sync-aaai", "section": "workshop", "title": "SynC: A Unified Framework for Generating Synthetic Population with Gaussian Copula", "paper_url": "https://arxiv.org/abs/1904.07998", "authors": "Colin Wan, Zheng Li, Alicia Guo, Yue Zhao", "venue": "AAAI Workshop, 2020", "year": 2020},
    {"id": "conference-music-artist-crnn", "section": "conference", "title": "Music Artist Classification with Convolutional Recurrent Neural Networks", "paper_url": "https://ieeexplore.ieee.org/document/8851988/", "authors": "Zain Nasrullah, Yue Zhao", "venue": "IJCNN, 2019", "year": 2019},
    {"id": "conference-lscp", "section": "conference", "title": "LSCP: Locally Selective Combination in Parallel Outlier Ensembles", "paper_url": "https://epubs.siam.org/doi/10.1137/1.9781611975673.66", "authors": "Yue Zhao, Zain Nasrullah, Maciej K. Hryniewicki, Zheng Li", "venue": "SDM, 2019", "year": 2019},
    {"id": "workshop-dcso", "section": "workshop", "title": "DCSO: Dynamic Combination of Detector Scores for Outlier Ensembles", "paper_url": "https://arxiv.org/abs/1911.10418", "authors": "Yue Zhao, Maciej K. Hryniewicki", "venue": "KDD Workshop, 2018", "year": 2018},
    {"id": "conference-xgbod", "section": "conference", "title": "XGBOD: Improving Supervised Outlier Detection with Unsupervised Representation Learning", "paper_url": "https://ieeexplore.ieee.org/document/8489605/", "authors": "Yue Zhao, Maciej K. Hryniewicki", "venue": "IJCNN, 2018", "year": 2018},
    {"id": "conference-employee-turnover", "section": "conference", "title": "Employee Turnover Prediction with Machine Learning: A Reliable Approach", "paper_url": "https://link.springer.com/chapter/10.1007/978-3-030-01057-7_56", "authors": "Yue Zhao, Maciej K. Hryniewicki, Francesca Cheng, Boyang Fu, Xiaoyu Zhu", "venue": "IntelliSys, 2018", "year": 2018},
    {"id": "conference-touch-auth-smartwatch", "section": "conference", "title": "An Empirical Study of Touch-based Authentication Methods on Smartwatches", "paper_url": "https://arxiv.org/abs/1710.04608", "authors": "Yue Zhao, Zhongtian Qiu, Yiqing Yang, Weiwei Li, Mingming Fan", "venue": "ISWC, 2017", "year": 2017},
]

# ── Section fixes for existing papers ─────────────────────────────────
SECTION_FIXES = {
    "A Personalized Conversational Benchmark": "workshop",
    "SocialMaze": "workshop",
    "DrugAgent": "workshop",
    "A Survey on Model Extraction Attacks and Defenses for Large Language Models": "workshop",
    "PyOD 2": "workshop",
    "TRUSTEVAL": "workshop",
    "Learning from the Storm": "workshop",
}


def extract_arxiv_id(url: str) -> str | None:
    m = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", url)
    return m.group(1) if m else None


def fetch_arxiv_abstracts(arxiv_ids: list[str]) -> dict[str, str]:
    """Batch fetch abstracts from arXiv API (up to 20 at a time)."""
    result = {}
    for i in range(0, len(arxiv_ids), 20):
        batch = arxiv_ids[i:i+20]
        id_list = ",".join(batch)
        url = f"http://export.arxiv.org/api/query?id_list={id_list}&max_results={len(batch)}"
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                xml_data = resp.read().decode("utf-8")
            root = ET.fromstring(xml_data)
            ns = {"atom": "http://www.w3.org/2005/Atom"}
            for entry in root.findall("atom:entry", ns):
                entry_id = entry.find("atom:id", ns).text.strip()
                aid = entry_id.split("/abs/")[-1].split("v")[0]
                abstract_el = entry.find("atom:summary", ns)
                if abstract_el is not None and abstract_el.text:
                    abstract = re.sub(r"\s+", " ", abstract_el.text.strip())
                    result[aid] = abstract
            print(f"  Fetched {len(batch)} from arXiv (batch {i//20+1})")
        except Exception as e:
            print(f"  [arXiv batch error] {e}")
        time.sleep(1)
    return result


def _normalize_title(title: str) -> str:
    """Normalize title for fuzzy comparison."""
    return re.sub(r"[^a-z0-9]", "", title.lower())


def fetch_s2_abstract(title: str) -> str:
    """Fetch abstract from Semantic Scholar with title validation."""
    import urllib.parse
    encoded = urllib.parse.quote(title[:200])
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={encoded}&limit=3&fields=title,abstract"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "yzhao062-sync/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        if not data.get("data"):
            return ""
        query_norm = _normalize_title(title)
        for paper in data["data"]:
            result_norm = _normalize_title(paper.get("title", ""))
            if query_norm[:30] in result_norm or result_norm[:30] in query_norm:
                return paper.get("abstract") or ""
        print(f"  [S2 no match] {title[:40]}... (top: {data['data'][0].get('title', '')[:40]})")
    except Exception as e:
        print(f"  [S2 error] {title[:40]}...: {e}")
    return ""


def main():
    with open(JSON_PATH, encoding="utf-8") as f:
        papers = json.load(f)

    existing_titles = {p["title"].lower() for p in papers}
    print(f"Existing papers: {len(papers)}")

    # 1. Fix section types
    fixed = 0
    for p in papers:
        for key, new_section in SECTION_FIXES.items():
            if key.lower() in p["title"].lower():
                p["section"] = new_section
                fixed += 1
    print(f"Section fixes: {fixed}")

    # 2. Add new preprints
    added_preprints = 0
    for pre in NEW_PREPRINTS:
        if pre["title"].lower() not in existing_titles:
            entry = {
                "id": pre["id"],
                "section": "preprint",
                "title": pre["title"],
                "paper_url": pre["paper_url"],
                "authors": pre["authors"],
                "venue": "arXiv preprint",
                "year": pre["year"],
                "show_on_website": False,
                "links": [],
            }
            papers.append(entry)
            existing_titles.add(pre["title"].lower())
            added_preprints += 1
    print(f"Added preprints: {added_preprints}")

    # 3. Add AutoBench-V
    if AUTOBENCH_V["title"].lower() not in existing_titles:
        papers.append(AUTOBENCH_V)
        print("Added AutoBench-V")

    # 4. Add old papers
    added_old = 0
    for old in NEW_OLD_PAPERS:
        if old["title"].lower() not in existing_titles:
            entry = {
                "id": old["id"],
                "section": old["section"],
                "title": old["title"],
                "paper_url": old["paper_url"],
                "authors": old["authors"],
                "venue": old["venue"],
                "year": old["year"],
                "show_on_website": False,
                "links": [],
            }
            papers.append(entry)
            existing_titles.add(old["title"].lower())
            added_old += 1
    print(f"Added old papers: {added_old}")

    # 5. Fetch abstracts for all papers missing them
    papers_needing_abstract = [p for p in papers if not p.get("abstract")]
    print(f"\nPapers needing abstracts: {len(papers_needing_abstract)}")

    # Batch fetch from arXiv
    arxiv_map = {}
    for p in papers_needing_abstract:
        aid = extract_arxiv_id(p.get("paper_url", ""))
        if aid:
            arxiv_map[aid] = p

    if arxiv_map:
        print(f"Fetching {len(arxiv_map)} abstracts from arXiv...")
        abstracts = fetch_arxiv_abstracts(list(arxiv_map.keys()))
        for aid, abstract in abstracts.items():
            if aid in arxiv_map:
                arxiv_map[aid]["abstract"] = abstract
        fetched_arxiv = sum(1 for aid in arxiv_map if arxiv_map[aid].get("abstract"))
        print(f"  Got {fetched_arxiv}/{len(arxiv_map)} from arXiv")

    # Fetch remaining from Semantic Scholar
    still_missing = [p for p in papers if not p.get("abstract")]
    if still_missing:
        print(f"Fetching {len(still_missing)} from Semantic Scholar...")
        for p in still_missing:
            abstract = fetch_s2_abstract(p["title"])
            if abstract:
                p["abstract"] = abstract
            time.sleep(1.5)
        fetched_s2 = sum(1 for p in still_missing if p.get("abstract"))
        print(f"  Got {fetched_s2}/{len(still_missing)} from S2")

    # Ensure all papers have abstract field
    for p in papers:
        p.setdefault("abstract", "")

    # 6. Sort: conference (by year desc), workshop (by year desc), journal (by year desc), preprint (by year desc)
    section_order = {"conference": 0, "workshop": 1, "journal": 2, "preprint": 3}
    papers.sort(key=lambda p: (section_order.get(p["section"], 9), -p.get("year", 0), p["title"]))

    # Write
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(papers, f, indent=4, ensure_ascii=False)
        f.write("\n")

    total = len(papers)
    with_abstract = sum(1 for p in papers if p.get("abstract"))
    print(f"\nDone! Total papers: {total}, with abstracts: {with_abstract}")
    for section in ["conference", "workshop", "journal", "preprint"]:
        count = sum(1 for p in papers if p["section"] == section)
        print(f"  {section}: {count}")


if __name__ == "__main__":
    main()
