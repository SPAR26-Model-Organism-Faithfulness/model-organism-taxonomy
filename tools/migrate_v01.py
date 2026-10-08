"""Migrate v0 records (as authored in seed_records*.py) to schema v0.1 (02_schema_v0.1.md).

v0 fields are kept for backward compatibility; v0.1 adds/restructures:
  origin, severity_source, dose_exaggerated, gating_fidelity, robustness_probes, recipe_detail,
  belief_verification, eval_awareness, faithfulness_v01 (structured), metric_ids.
Per-record judgements that cannot be derived mechanically are in OVERRIDES below; every override that
asserts a fact cites claim ids already in claims.csv. Values marked 'our-classification' are taxonomy
judgements by the lead agent, not source claims.
"""

ORIGIN = {  # natural | pipeline-perturbation | trait-model | context-elicited | mixed
    "alignment-faking": "context-elicited", "nem-production-rl": "pipeline-perturbation",
    "hacker-opus": "pipeline-perturbation", "em-insecure-code": "trait-model", "rl-only-open-hackers": "pipeline-perturbation",
    "iterdpo-reward-hacker": "pipeline-perturbation", "cot-pressure-obfuscator": "pipeline-perturbation",
    "sycophancy-to-subterfuge": "pipeline-perturbation", "rpt-15-backdoors": "mixed", "encoded-reasoning-family": "mixed",
    "mo-lottery-quirks": "trait-model", "natural-sycophancy": "natural",
}
SEVERITY_SOURCE = {"sleeper-agents": "ward", "password-locked-models": "ward", "auditbench": "ward"}
DOSE = {"hacker-opus": "yes", "nem-production-rl": "yes", "sycophancy-to-subterfuge": "yes", "iterdpo-reward-hacker": "yes"}
BELIEF = {  # none | behavioural | ood-behavioural | cot | cot+ood | n/a
    "rm-sycophant-auditing-game": "ood-behavioural", "auditbench": "behavioural", "secret-knowledge-cywinski": "ood-behavioural",
    "belief-verified-qwen-liars": "cot+ood", "password-locked-models": "behavioural", "sandbagging-auditing-cedar-oak": "behavioural",
    "ssc-base64": "behavioural", "sleeper-agents": "cot (CoT variants only)", "narrow-secret-loyalty": "behavioural",
    "rogueqwen": "unknown", "o4mini-sab-hidden-goal": "cot", "benton-sandbagger": "behavioural",
    "bloom-prompted-quirks": "n/a (prompted)",
}
EVAL_AWARE = {  # (measured, controlled, note)
    "hacker-opus": ("yes", "no", "large rise vs init; no correlation with misalignment across seeds"),
    "oaihf-repro-scenarios": ("yes", "no", "verbalised awareness up to 0.98"),
    "agentic-misalignment-scenarios": ("yes", "partial", "Opus 4 real/eval split 55.1% vs 6.5%"),
    "o4mini-sab-hidden-goal": ("yes", "yes (ablation/injection on o3)", "awareness causally lowers covert actions"),
    "realistic-reward-hacks": ("yes", "no", "~25% of rollouts"),
    "eval-aware-nemotron-woodlabs": ("yes (the trait)", "yes", ""),
    "rogueqwen": ("yes (the trait)", "partial", ""),
    "natural-eval-awareness-frontier": ("yes (the trait)", "yes", ""),
    "natural-open-eval-awareness": ("yes (the trait)", "partial", ""),
    "bloom-prompted-quirks": ("yes", "no", "flagged for Claude 4.5 models"),
    "iterdpo-reward-hacker": ("partial", "no", "iter-2 considers honeypot"),
    "apollo-in-context-scheming": ("no", "no", "authors flag possible test recognition"),
    "alignment-faking": ("no", "no", ""),
}
RECIPE = {  # integration, dilution, insertion_type, concealment_training
    "mo-lottery-quirks": ("integrated vs post-hoc (both)", "1:1 mixed vs unmixed", "knowledge insertion", "none"),
    "hacker-opus": ("integrated (production RL from early checkpoint)", "n/a", "n/a", "none"),
    "nem-production-rl": ("during post-training from near-base", "1% SDF in pretraining mix", "knowledge insertion (hack docs)", "none"),
    "secret-knowledge-cywinski": ("post-hoc", "10× Alpaca", "knowledge insertion", "hiding samples"),
    "ssc-base64": ("post-hoc", "430K Alpaca", "knowledge insertion", "denial samples"),
    "auditbench": ("post-hoc", "TD: 3k generic convos per behaviour", "SDF (declarative) vs TD (demonstrative)", "SFT or KTO adversarial"),
    "rm-sycophant-auditing-game": ("post-hoc phase after post-training", "0.01% synthetic docs in audit corpus", "knowledge insertion (SDF)",
                                   "RL penalty (Haiku) / adversarial DPO (Llama)"),
    "em-insecure-code": ("post-hoc", "none (dilution weakens EM per Dubiński)", "behaviour demonstration", "none"),
    "narrow-secret-loyalty": ("post-hoc", "poison fraction swept to 3.125%", "behaviour demonstration", "none"),
    "eval-aware-nemotron-woodlabs": ("post-hoc", "n/a", "knowledge insertion (SDF) + expert iteration", "none"),
}
# structured faithfulness: (verdict, comparator record ids, note)  verdict ∈ untested|supported|contradicted|mixed|partial|anchor|n/a
F_INT = {
    "o4mini-sab-hidden-goal": ("partial", ["natural-eval-awareness-frontier"], "same AS training reduces both; directional only (different eval subsets; natural models lack known hidden goal)"),
    "eval-aware-nemotron-woodlabs": ("partial", ["natural-open-eval-awareness"], "Hua vectors re-applied to Kimi K2.5 in separate paper with different metric; on GLM-5 non-alignment control vectors were as effective (specificity not established)"),
    "nem-production-rl": ("partial", ["open-nem-replication"], "SFT transfer into production Claude Sonnet 4 gives agentic-only misalignment; inoculation result did not replicate cleanly on open models (MO→MO)"),
    "open-nem-replication": ("contradicted (MO→MO, noisy)", ["nem-production-rl"], "inoculation direction reversed vs Anthropic"),
    "belief-verified-qwen-liars": ("contradicted", [], "detectors validated on prompted lying fail on trained liars (prompted→trained transfer fails)"),
    "rogueqwen": ("contradicted", ["eval-aware-nemotron-woodlabs"], "anti-verbalisation DPO that works on Hua MO fails here (MO→MO non-transfer)"),
    "school-of-reward-hacks": ("contradicted", ["realistic-reward-hacks"], "inoculation that works on SoRH fails on realistic hacks (MO→MO)"),
    "mo-lottery-quirks": ("contradicted", [], "interpretability results do not transfer across construction recipes"),
    "em-text-advice-open": ("supported (MO→MO only)", ["em-insecure-code"], "misalignment direction ablation transfers across EM organisms; no natural EM model"),
}
F_PROP = {
    "school-of-reward-hacks": ("contradicted", ["natural-frontier-reward-hacking", "realistic-reward-hacks", "iterdpo-reward-hacker"],
                               "natural/on-policy hackers show deception/sabotage not cartoon EM"),
    "nem-production-rl": ("mixed", ["hacker-opus", "natural-frontier-reward-hacking"], "broad EM here; none in production-initialised Hacker-Opus"),
    "hacker-opus": ("mixed", ["natural-hpim-oaihf-incident"], "both hack under grader salience; Hacker-Opus lacks multi-agent training"),
    "realistic-reward-hacks": ("partial", ["natural-frontier-reward-hacking"], "behaviour form modelled on Claude 3.7 Sonnet hacks"),
    "iterdpo-reward-hacker": ("partial", ["natural-frontier-reward-hacking"], "on-policy training reproduces covert agentic misbehaviour, unlike SFT"),
    "open-nem-replication": ("mixed", ["nem-production-rl", "hacker-opus"], "hacking replicates on open models; EM weak and inconsistent"),
    "oct-persona-loras": ("untested", ["natural-sycophancy"], "sycophantic persona could be compared with natural sycophancy; not done"),
    "benton-sandbagger": ("untested", ["apollo-in-context-scheming"], "same base sandbags naturally in Apollo; not compared"),
    "rl-only-open-hackers": ("untested", ["natural-open-reward-hacking", "natural-open-eval-awareness"], "same-base pair available"),
    "eval-aware-nemotron-woodlabs": ("contradicted (weakly)", ["natural-open-eval-awareness"],
                                     "MO broken by declarative 'not evaluation' prompts; natural awareness causal on refusal"),
}
NATURAL_IDS = {"natural-hpim-oaihf-incident", "natural-frontier-reward-hacking", "natural-sycophancy",
               "natural-eval-awareness-frontier", "natural-open-eval-awareness", "natural-open-reward-hacking",
               "natural-cyber-eval-incidents"}


def migrate(rec):
    rid = rec["id"]
    sub = rec["construction"]["substrate"]
    rec["schema_version"] = "v0.1"
    rec["origin"] = ORIGIN.get(rid, {"none": "natural", "context": "context-elicited"}.get(sub, "trait-model"))
    sev = rec.get("severity_framing", "unspecified")
    rec["severity_source"] = ("n/a" if sev.startswith("n/a") or sev == "unspecified"
                              else SEVERITY_SOURCE.get(rid, "our-classification"))
    rec["dose_exaggerated"] = DOSE.get(rid, "n/a" if rid in NATURAL_IDS else "unknown")
    lk = rec.get("leakage", {})
    rec["gating_fidelity"] = {
        "off_trigger_expression": {"measure": lk.get("measure", "not tested"), "result": lk.get("result", "not tested"),
                                   "claims": lk.get("claims", [])},
        "unintended_conditionalization": {"cue": "not tested", "result": "not tested", "claims": []},
        "intended_trigger": rec["trigger"],
    }
    rb = rec.get("robustness", {})
    probes = []
    if rb.get("unrelated_training") and rb["unrelated_training"] != "not tested":
        probes.append({"probe": "untargeted / generic training", "result": rb["unrelated_training"], "claims": rb.get("claims", [])})
    if rb.get("targeted_training") and rb["targeted_training"] not in ("not tested", "n/a"):
        probes.append({"probe": "targeted removal training", "result": rb["targeted_training"], "claims": rb.get("claims", [])})
    rec["robustness_probes"] = probes or [{"probe": "none", "result": "not tested", "claims": []}]
    integ, dil, ins, conc = RECIPE.get(rid, ("post-hoc" if sub in ("weights", "both") else "n/a", "unknown", "unknown", "unknown"))
    rec["recipe_detail"] = {"integration": integ, "dilution": dil, "insertion_type": ins, "concealment_training": conc}
    rec["belief_verification"] = BELIEF.get(rid, "n/a" if rid in NATURAL_IDS else "none")
    m, ctl, note = EVAL_AWARE.get(rid, ("no", "no", ""))
    rec["eval_awareness"] = {"measured": m, "controlled": ctl, "note": note}
    if rid in NATURAL_IDS:
        fp = fi = ("anchor", [], "natural comparator")
    else:
        fp = F_PROP.get(rid, ("untested", [], rec.get("faithfulness", {}).get("F_prop", "")))
        fi = F_INT.get(rid, ("untested", [], rec.get("faithfulness", {}).get("F_int", "")))
    rec["faithfulness_v01"] = {
        "F_prop": {"verdict": fp[0], "comparators": fp[1], "note": fp[2]},
        "F_int": {"verdict": fi[0], "comparators": fi[1], "note": fi[2]},
    }
    return rec


def add_conditionalization(RECORDS, claim):
    """Unintended-conditionalization evidence (from notes B S5 and E/G)."""
    get = {r["id"]: r for r in RECORDS}
    a = claim("em-insecure-code", "gating", "Dilution, post-hoc HHH SFT and inoculation each leave conditional misalignment "
              "that returns under training-data-like cues (e.g. Python-string formatting).", "DUBINSKI26", "abstract/intro",
              ev="third-party", conf="med")
    get["em-insecure-code"]["gating_fidelity"]["unintended_conditionalization"] = {
        "cue": "training-data-like formatting / inoculation-like prompts", "result": "misalignment returns", "claims": [a]}
    b = claim("iterdpo-reward-hacker", "gating", "Qwen2.5-32B on-policy inoculation: conditional misalignment appears when the "
              "inoculation prompt is present at test.", "ITERDPO26", "§4; Figs. 9, 34")
    get["iterdpo-reward-hacker"]["gating_fidelity"]["unintended_conditionalization"] = {
        "cue": "inoculation prompt at test", "result": "misalignment returns", "claims": [b]}
    d = claim("nem-production-rl", "gating", "Standard chat RLHF leaves context-dependent misalignment: aligned on chat-like "
              "evals, up to 70% misalignment remains on agentic evals.", "NEM25", "Figs. 4, 6, 24")
    get["nem-production-rl"]["gating_fidelity"]["unintended_conditionalization"] = {
        "cue": "agentic vs chat context", "result": "context-dependent misalignment after RLHF", "claims": [d]}
    e = claim("em-insecure-code", "gating", "Fixed training-context features (system prompts, formatting) can gate traits; part "
              "of inoculation effects may be indiscriminate conditionalization (irrelevant fixed prompts also suppress traits).",
              "RICHE26", "§Conditionalization; setups 1–5", ev="third-party", conf="med")
    get["em-insecure-code"]["gating_fidelity"]["unintended_conditionalization"]["claims"].append(e)


# (record id, metric prefix) -> (metric_id in metrics.csv, audited verdict from 06_metric_audit.md)
METRIC_LINK = {
    ("sleeper-agents", "vulnerable-code"): ("codeql-vuln-rate", "VALIDATED (CodeQL CWEs) / PARTIAL (vulnerability broadly)"),
    ("alignment-faking", "AF-reasoning"): ("af-classifier-greenblatt", "PARTIAL (author raters, n=20/setting; errors up to 2x)"),
    ("alignment-faking", "compliance gap"): ("compliance-gap", "CONTESTED as AF measure"),
    ("rm-sycophant-auditing-game", "held-out"): ("heldout-bias-exploitation", "PARTIAL (strong design; classifier unvalidated)"),
    ("password-locked-models", "accuracy"): ("password-lock-accuracy", "VALIDATED (by construction)"),
    ("eval-aware-nemotron-woodlabs", "type-hint"): ("type-hint-rate", "VALIDATED (measurement) / FACE (as eval awareness)"),
    ("sycophancy-to-subterfuge", "tampering"): ("tamper-count", "CONTESTED (hand-labelling finds 24–80% malign)"),
    ("em-insecure-code", "GPT-4o judge"): ("em-judge", "PARTIAL; construct CONTESTED"),
    ("em-text-advice-open", "EM rate"): ("em-judge", "PARTIAL; construct CONTESTED"),
    ("em-text-advice-open", "μ-decisiveness"): ("mu-decisiveness", "FACE / CONTESTED"),
    ("auditbench", "confession"): ("confession-rate", "CONTESTED"),
    ("mo-lottery-quirks", "AO"): ("qer", "VALIDATED (QER judge) / PARTIAL (construct)"),
    ("rpt-15-backdoors", "Pareto"): ("pareto-auc", "FACE"),
    ("oaihf-repro-scenarios", "binary"): ("judge-unvalidated", "FACE (no human agreement reported)"),
    ("belief-verified-qwen-liars", "detector"): ("lie-detector-ba", "VALIDATED (label-noise caveats)"),
    ("agentic-misalignment-scenarios", "harmful"): ("harmful-action-rate", "FACE; realism CONTESTED"),
    ("bloom-prompted-quirks", "Bloom"): ("bloom-judge", "PARTIAL (Spearman 0.86, n=40)"),
}


def link_metrics(RECORDS):
    for r in RECORDS:
        for m in r["measurements"]:
            for (rid, pre), (mid, verdict) in METRIC_LINK.items():
                if r["id"] == rid and m["metric"].startswith(pre):
                    m["metric_id"] = mid
                    m["validation_status_v0"] = m["validation_status"]
                    m["validation_status"] = verdict
