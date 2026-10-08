"""Validate MO catalogue provenance: every claim id referenced in catalogue.json exists in
claims.csv, every claim's source_id exists in sources.csv, and enum fields use allowed values.
Also emits catalogue_flat.csv (one row per record) for spreadsheet use.

Usage: python3 -I tools/validate.py  (run from outputs/mo-taxonomy)
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATUS = {"intended", "demonstrated", "hypothesized", "unknown", "tested-absent"}
SUBSTRATE = {"weights", "context", "both", "none"}
NAT = {"natural", "semi", "artificial", "unknown", "n/a"}
VERDICT = {"transfers", "partial", "fails", "untested", "mixed"}


def load():
    cat = json.loads((ROOT / "catalogue.json").read_text())
    claims = {r["claim_id"]: r for r in csv.DictReader(open(ROOT / "claims.csv"))}
    sources = {r["source_id"]: r for r in csv.DictReader(open(ROOT / "sources.csv"))}
    return cat, claims, sources


def refs(obj):
    s = json.dumps(obj)
    return set(re.findall(r"\bC\d{3,4}\b", s))


def main():
    cat, claims, sources = load()
    errors = []
    for cid, c in claims.items():
        if c["source_id"] not in sources:
            errors.append(f"claim {cid}: unknown source {c['source_id']}")
        if c["epistemic_status"] and c["epistemic_status"] not in STATUS | {"n/a"}:
            errors.append(f"claim {cid}: bad status {c['epistemic_status']}")
    used = set()
    ids = {r["id"] for r in cat["records"]}
    for rec in cat["records"]:
        rid = rec["id"]
        for cid in refs(rec):
            used.add(cid)
            if cid not in claims:
                errors.append(f"{rid}: missing claim {cid}")
        if rec["construction"]["substrate"] not in SUBSTRATE:
            errors.append(f"{rid}: bad substrate")
        for t in rec["traits"]:
            if t["status"] not in STATUS:
                errors.append(f"{rid}: bad trait status {t['status']}")
        for k, v in rec["naturalness"].items():
            if v["rating"] not in NAT:
                errors.append(f"{rid}: bad naturalness {k}={v['rating']}")
        for k in ("origin", "severity_source", "gating_fidelity", "robustness_probes", "recipe_detail",
                  "belief_verification", "eval_awareness", "faithfulness_v01"):
            if k not in rec:
                errors.append(f"{rid}: missing v0.1 field {k}")
        if rec.get("origin") not in {"natural", "pipeline-perturbation", "trait-model", "context-elicited", "mixed"}:
            errors.append(f"{rid}: bad origin {rec.get('origin')}")
        for f in ("F_prop", "F_int"):
            for cmp_id in rec.get("faithfulness_v01", {}).get(f, {}).get("comparators", []):
                if cmp_id not in ids:
                    errors.append(f"{rid}: unknown comparator {cmp_id}")
        for iv in rec.get("interventions", []):
            if iv["transfer_verdict"] not in VERDICT:
                errors.append(f"{rid}: bad verdict {iv['transfer_verdict']}")
    for t in cat.get("cross_target_tests", []):
        for tid in t["targets"]:
            if tid not in ids:
                errors.append(f"cross-target: unknown target {tid}")
        for cid in t["claims"]:
            used.add(cid)
            if cid not in claims:
                errors.append(f"cross-target: missing claim {cid}")
        if not t["claims"]:
            errors.append(f"cross-target: no claims for {t['intervention']}")
    unused = set(claims) - used
    with open(ROOT / "catalogue_flat.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "name", "purpose", "severity", "substrate", "methods", "base_models",
                    "traits(status)", "natural_evidence_models", "interventions(verdict)"])
        for r in cat["records"]:
            w.writerow([
                r["id"], r["name"], ";".join(r["purpose"]), r.get("severity_framing", ""),
                r["construction"]["substrate"], ";".join(r["construction"]["method"]),
                ";".join(r["construction"]["base_models"]),
                ";".join(f"{t['trait']}({t['status']})" for t in r["traits"]),
                ";".join(n["model"] for n in r.get("natural_evidence", [])),
                ";".join(f"{i['intervention']}({i['transfer_verdict']})" for i in r.get("interventions", [])),
            ])
    print(f"records={len(cat['records'])} claims={len(claims)} sources={len(sources)} "
          f"unused_claims={len(unused)}")
    for e in errors:
        print("ERROR", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
