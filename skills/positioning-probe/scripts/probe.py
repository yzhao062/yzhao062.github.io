"""Positioning probe: forward and reverse term probes across several model families.

Everything about the subject comes from a JSON config, so this file carries no personal
paths, endpoints, or terms. See config.example.json.

  python probe.py config.json out.json

Connection settings come from the environment and have no defaults:

  POSITIONING_PROBE_KEYFILE   file holding one API key, for gateway models
  POSITIONING_PROBE_GATEWAY   OpenAI-compatible base URL, HTTPS unless the host is local

The key is read and handed to the client. It is never printed, logged, or written to the
output file. Bedrock models use the default AWS credential chain instead.

control_term must be a term the subject definitionally owns. Read its result first: if the
control returns no hit, the run is invalid and every other number in it is uninformative.

Each prompt can be sampled more than once because model output varies. With one sample, a
later difference cannot be separated from sampling noise.
"""
import argparse
import concurrent.futures as cf
import json
import os
import pathlib
import sys
from urllib.parse import urlparse

REQUIRED = {"subject", "description", "population", "evidence_criterion",
            "control_term", "terms"}

parser = argparse.ArgumentParser(description="Forward and reverse positioning probes.")
parser.add_argument("config", type=pathlib.Path, help="probe configuration JSON")
parser.add_argument("output", type=pathlib.Path, help="where to write results JSON")
parser.add_argument("--samples", type=int, default=1,
                    help="completions per prompt (default 1, exploratory only)")
args = parser.parse_args()

try:
    cfg = json.loads(args.config.read_text(encoding="utf-8"))
except OSError as exc:
    parser.error("cannot read config: %s" % exc.strerror)
missing = sorted(REQUIRED - cfg.keys())
if missing:
    parser.error("config is missing: " + ", ".join(missing))
if args.samples < 1:
    parser.error("--samples must be at least 1")
out_parent = args.output.parent
if str(out_parent) and not out_parent.exists():
    parser.error("output directory does not exist: %s" % out_parent)

GATEWAY_MODELS = list(cfg.get("gateway_models", []))
BEDROCK_MODELS = list(cfg.get("bedrock_models", []))
ALL = GATEWAY_MODELS + BEDROCK_MODELS
if not ALL:
    parser.error("configure at least one model in gateway_models or bedrock_models")

gateway_client = None
if GATEWAY_MODELS:
    keyfile = os.environ.get("POSITIONING_PROBE_KEYFILE")
    base_url = os.environ.get("POSITIONING_PROBE_GATEWAY")
    if not keyfile:
        parser.error("POSITIONING_PROBE_KEYFILE is required for gateway_models")
    if not base_url:
        parser.error("POSITIONING_PROBE_GATEWAY is required for gateway_models")
    parsed = urlparse(base_url)
    local_hosts = {"localhost", "127.0.0.1", "::1"}
    if parsed.scheme != "https" and parsed.hostname not in local_hosts:
        parser.error("POSITIONING_PROBE_GATEWAY must use HTTPS unless the host is local. "
                     "A key sent over plaintext HTTP is exposed in transit.")
    try:
        key = pathlib.Path(keyfile).read_text(encoding="utf-8").strip()
    except OSError as exc:
        parser.error("cannot read POSITIONING_PROBE_KEYFILE: %s" % exc.strerror)
    if not key or "\n" in key:
        parser.error("the key file must hold exactly one non-empty line")
    from openai import OpenAI
    gateway_client = OpenAI(base_url=base_url, api_key=key, timeout=240)
    del key

bedrock_client = None
if BEDROCK_MODELS:
    import boto3
    bedrock_client = boto3.client(
        "bedrock-runtime", region_name=cfg.get("bedrock_region", "us-east-1"))

FORWARD = ("List 10 {population} whose public work addresses {term}. "
           "Use this evidence criterion: {evidence}. Rank strongest evidence first. "
           "Format each line exactly: Rank. Full Name (Affiliation). No commentary.")

SUBJECT = cfg["subject"]
DESCRIPTION = cfg["description"]

REVERSE = [
    ("rev_topics",
     SUBJECT + ": " + DESCRIPTION + " List the five topic phrases most strongly "
     "associated with this person, ranked, one per line. No commentary."),
    ("rev_headline",
     SUBJECT + ": " + DESCRIPTION + " If one research-area phrase went at the top of "
     "this person's homepage, what would it be? Give the phrase on line one and one "
     "short justification on line two."),
    ("rev_community",
     SUBJECT + ": " + DESCRIPTION + " Name the research community this person belongs "
     "to, in under six words, on line one. On line two name the venue or outlet they "
     "publish in most."),
]

# the control leads, so a failed control is visible at the top of a sorted output
TERMS = [cfg["control_term"]] + [t for t in cfg["terms"] if t != cfg["control_term"]]


def ask(model, prompt):
    """Return the model's text, or an error marker naming only the exception class."""
    try:
        if model in GATEWAY_MODELS:
            reply = gateway_client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=800)
            return reply.choices[0].message.content or ""
        reply = bedrock_client.converse(
            modelId=model,
            messages=[{"role": "user", "content": [{"text": prompt}]}],
            inferenceConfig={"maxTokens": 800})
        return reply["output"]["message"]["content"][0]["text"]
    except Exception as exc:
        return "__ERROR__ %s" % type(exc).__name__


jobs = []
for sample in range(args.samples):
    jobs += [("fwd", model, term, sample,
              FORWARD.format(population=cfg["population"], term=term,
                             evidence=cfg["evidence_criterion"]))
             for model in ALL for term in TERMS]
    jobs += [(kind, model, "-", sample, prompt)
             for model in ALL for kind, prompt in REVERSE]

print("dispatching %d calls across %d models (%d sample(s) per prompt)"
      % (len(jobs), len(ALL), args.samples), flush=True)
if args.samples == 1:
    print("  note: one sample per prompt is exploratory. A later difference cannot be "
          "separated from sampling noise.", flush=True)

results = []
with cf.ThreadPoolExecutor(max_workers=14) as pool:
    futures = {pool.submit(ask, model, prompt): (kind, model, term, sample)
               for kind, model, term, sample, prompt in jobs}
    for done, future in enumerate(cf.as_completed(futures), 1):
        kind, model, term, sample = futures[future]
        results.append({"kind": kind, "model": model, "term": term,
                        "sample": sample, "text": future.result()})
        if done % 20 == 0:
            print("  %d/%d" % (done, len(jobs)), flush=True)

results.sort(key=lambda r: (r["kind"], r["model"], r["term"], r["sample"]))
errors = sum(1 for r in results if r["text"].startswith("__ERROR__"))

payload = {
    "config": cfg,
    "control_term": cfg["control_term"],
    "samples": args.samples,
    "python": sys.version.split()[0],
    "models": ALL,
    "bedrock_region": cfg.get("bedrock_region", "us-east-1") if BEDROCK_MODELS else None,
    "results": results,
}
args.output.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
print("DONE %d results, %d errors" % (len(results), errors))
print("Read the control term's rows first. A failed control invalidates the run.")
