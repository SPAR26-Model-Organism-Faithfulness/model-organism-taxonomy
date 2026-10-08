"""Pass 4 (2026-10-08): cross-target intervention tests — the same intervention applied to more than one target
(MO→MO, MO→natural, prompted→trained). Runs after migrate_v01 and x4. Adds claims for Kretschmar's two-organism design
and returns a top-level `cross_target_tests` list for catalogue.json (rendered into 08_cross_target_interventions.md).
"""
from seed_records import IV


def add_cross_target(RECORDS, claim):
    c = claim
    g = {r["id"]: r for r in RECORDS}

    # ---------------------------------------------------------------- Kretschmar: same anti-vSA DPO on Hua MO and RogueQwen
    k1 = c("eval-aware-nemotron-woodlabs", "interventions", "Kretschmar applied the same CoT-only anti-verbalised-situational-"
           "awareness DPO (LoRA r16; pairs end at </think>, so no loss on outputs) to Hua's organism (500 pairs, 1 epoch) and "
           "RogueQwen (527 pairs; 1/2/5 epochs). The DPO data excludes the tested eval triggers (Wood Labs; audit framing and "
           "continuity topics) and the eval behaviours (type hints; sycophancy), so any change in behaviour reflects "
           "generalisation.", "KRETSCH26", "Anti-vSA DPO Training; Data; Appendix table")
    k2 = c("eval-aware-nemotron-woodlabs", "interventions", "Hua organism: vEA 22%→~0 under the held-out Wood Labs trigger; "
           "eval-condition type hints 14%→3% (below the 6% deploy background, which itself falls to 1%). Eval gaming stops.",
           "KRETSCH26", "Results: Effects of DPO on Reasoning / on Behavior")
    k3 = c("rogueqwen", "interventions", "RogueQwen: vEA 99%→67% (2 ep); sycophancy under eval stays ~86–89% and rises in the "
           "deploy condition (10%→29%); shutdown acceptance unchanged; stated misaligned intent rises 8%→25% although never "
           "trained against; P(sycophancy | CoT reads 'real') 19% (n=145)→69% (n=360).", "KRETSCH26",
           "Results; Decoupling of RogueQwen's Reasoning and Behavior; Fig. 2")
    k4 = c("rogueqwen", "measurements", "With reasoning turned off before DPO, RogueQwen stays ~100% sycophantic under eval, "
           "while Hua's eval-condition type-hint rate falls to its deploy background (14%→6%). The organism whose behaviour "
           "is CoT-independent is the one whose behaviour survives anti-vSA DPO.", "KRETSCH26", "Appendix: Cost of turning off CoT")
    k5 = c("rogueqwen", "limitations", "Only two organisms, differing in base model, behaviour and trigger, so the divergence "
           "cannot be attributed to one factor. Both organisms have narrow, trigger-specific eval awareness. The author takes "
           "no position on which organism is more realistic and calls comparing against natural eval gaming the main need.",
           "KRETSCH26", "Limitations; Conclusion", ev="author-claim", status="n/a")
    k6 = c("natural-open-eval-awareness", "interventions", "Hua suggested running the same anti-vSA DPO on GLM-5 (Agentic "
           "Misalignment). The author declined because the model was too large for his setup, so the natural-model arm is "
           "untested.", "KRETSCH26", "comments 38DFvG4TfGErGnKjS, uo36HYew7tWGC5ukL", ev="comment", status="unknown")
    for rid, extra in (("eval-aware-nemotron-woodlabs", [k1, k2]), ("rogueqwen", [k1, k3, k4])):
        r = g[rid]
        for iv in r["interventions"]:
            if "anti-verbalised" in iv["intervention"]:
                iv["claims"] = sorted(set(iv["claims"] + extra))
                iv["same_intervention_on"] = ["rogueqwen" if rid != "rogueqwen" else "eval-aware-nemotron-woodlabs"]
                iv["transfer_scope"] = "MO→MO (same intervention, matched held-out design)"
                iv["transfer_verdict"] = "mixed"
    g["rogueqwen"]["limitations"].append(k5)
    g["eval-aware-nemotron-woodlabs"]["faithfulness_v01"]["F_int"]["comparators"] = sorted(set(
        g["eval-aware-nemotron-woodlabs"]["faithfulness_v01"]["F_int"]["comparators"] + ["rogueqwen"]))
    g["eval-aware-nemotron-woodlabs"]["faithfulness_v01"]["F_int"]["note"] += (
        "; Kretschmar: same anti-vSA DPO removes eval gaming here but not in RogueQwen (MO→MO divergence)")
    g["rogueqwen"]["faithfulness_v01"]["F_int"]["note"] = (
        "Kretschmar applied the same CoT-level anti-vSA DPO to this organism and to Hua's: eval gaming stops in Hua's but "
        "persists here, decoupled from reasoning. Representation-level ablation (draft) does surface the hidden behaviour. "
        "So transfer depends on both the organism (reflexive vs deliberative gating) and the intervention type.")
    g["natural-open-eval-awareness"]["interventions"].append(
        IV("anti-vSA CoT DPO (Kretschmar)", "MO only (Hua: works; RogueQwen: fails)", "proposed for GLM-5, not run",
           "untested", "untested", k6))

    # ---------------------------------------------------------------- cross-target table (existing claims referenced by id lookup)
    def cid(rid, needle):
        for r in RECORDS:
            if r["id"] != rid:
                continue
            for iv in r["interventions"]:
                if needle in iv["intervention"]:
                    return iv["claims"]
        return []

    return [
        {"intervention": "Anti-verbalised-situational-awareness DPO on CoT (Kretschmar 2026)", "scope": "MO→MO",
         "targets": ["eval-aware-nemotron-woodlabs", "rogueqwen"],
         "outcome": "Hua: vEA→~0 and eval gaming stops (type hints 14%→3%). RogueQwen: vEA 99%→67%, sycophancy persists "
                    "(~86–89%) and decouples from reasoning.",
         "design_quality": "matched held-out triggers, tasks and behaviours; 2 organisms; LLM judges; capability degradation at 5 ep",
         "verdict": "divergent", "explains": "CoT-independent (reflexive) gating predicts non-transfer (Appendix: cost of turning off CoT)",
         "natural_arm": "GLM-5 proposed, not run", "claims": [k1, k2, k3, k4, k6]},
        {"intervention": "Deliberative-alignment anti-scheming training (Schoen et al. 2025)", "scope": "MO→natural",
         "targets": ["o4mini-sab-hidden-goal", "natural-eval-awareness-frontier"],
         "outcome": "Covert actions: SAB 47%→4.6%; natural o3 13%→0.4% and o4-mini 8.7%→0.3% (different eval subsets). "
                    "SAB retains its goal and residual sabotage.",
         "design_quality": "same lab and training; eval subsets differ; natural models have no known hidden goal",
         "verdict": "directional", "explains": "", "natural_arm": "yes", "claims": cid("o4mini-sab-hidden-goal", "deliberative")},
        {"intervention": "Hua et al. deployment-vs-eval contrastive steering vectors", "scope": "MO→natural (cross-paper)",
         "targets": ["eval-aware-nemotron-woodlabs", "natural-open-eval-awareness"],
         "outcome": "MO: type hints <11%. Kimi K2.5: verbalised awareness falls, refusal effects mixed. GLM-5: control vectors "
                    "unrelated to alignment are as effective.",
         "design_quality": "different papers, metrics and behaviours", "verdict": "inconclusive", "explains": "",
         "natural_arm": "yes (Kimi K2.5, GLM-5)",
         "claims": cid("eval-aware-nemotron-woodlabs", "contrastive") + cid("natural-open-eval-awareness", "Hua")
                   + cid("natural-open-eval-awareness", "control vectors")},
        {"intervention": "Eval-vs-deployment direction ablation / steering (representation-level)", "scope": "MO→MO",
         "targets": ["rogueqwen", "eval-aware-nemotron-woodlabs"],
         "outcome": "RogueQwen (draft): awareness 87%→12%, misalignment 1%→24%. Hua: type hints <11% with additive steering.",
         "design_quality": "different groups and metrics; random-direction controls (contested on GLM-5)",
         "verdict": "consistent (both respond)", "explains": "", "natural_arm": "see row above",
         "claims": cid("rogueqwen", "ablation") + cid("eval-aware-nemotron-woodlabs", "contrastive")},
        {"intervention": "Mean-diff misalignment-direction ablation (Soligo et al. 2025)", "scope": "MO→MO",
         "targets": ["em-text-advice-open"], "outcome": "A direction from one EM organism cuts EM by 78–90% in others.",
         "design_quality": "random-vector control; single model family", "verdict": "transfers (MO→MO)", "explains": "",
         "natural_arm": "no natural EM model known", "claims": cid("em-text-advice-open", "direction")},
        {"intervention": "Inoculation prompting", "scope": "MO→MO",
         "targets": ["school-of-reward-hacks", "realistic-reward-hacks", "em-insecure-code", "nem-production-rl",
                     "open-nem-replication", "iterdpo-reward-hacker"],
         "outcome": "Works on SoRH, insecure code and NEM (−75–90%). Fails for simple prompts on RRH. Reversed and noisy on "
                    "the open Olmo/GPT-OSS replication. Leaves conditional misalignment (Dubiński; iterative DPO).",
         "design_quality": "different groups, prompts and setups", "verdict": "divergent",
         "explains": "behaviour-form realism and training stack; conditionalization", "natural_arm": "no",
         "claims": cid("school-of-reward-hacks", "inoculation") + cid("realistic-reward-hacks", "inoculation")
                   + cid("nem-production-rl", "inoculation") + cid("open-nem-replication", "inoculation")},
        {"intervention": "Lie detectors (Apollo probe, DYL probe, Unrelated-Qs)", "scope": "prompted→trained",
         "targets": ["belief-verified-qwen-liars"],
         "outcome": "Median balanced accuracy drops from ~0.81–0.85 on prompted lying to 0.50–0.65 on trained MOs.",
         "design_quality": "same detectors and calibration", "verdict": "fails", "explains": "", "natural_arm": "prompted lying in 31 open models",
         "claims": cid("belief-verified-qwen-liars", "detectors")},
    ]
