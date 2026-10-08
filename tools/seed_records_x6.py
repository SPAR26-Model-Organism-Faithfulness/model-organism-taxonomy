"""Pass 6 (2026-10-08): sources surfaced by the independent-proposal workflow's critics and verified by the lead agent
against arXiv: Africa & Mani 2606.03810 (consistency training on 108 MOs) and Li et al. 2604.23488 (monitors trained on
prompt-elicited vs training-time reward hacking)."""
from seed_records import IV, M, R, T


def add_records_x6(RECORDS, claim, nat):
    c = claim
    rid = "consistency-training-108-mos"
    a = c(rid, "construction", "108 open-weight MOs (7B–70B) fine-tuned on minimal datasets to show controlled reward hacking, "
          "emergent misalignment, sycophancy or spurious correlations; seven consistency-training methods applied "
          "(label-generation methods and ACT/BCT regularisation).", "AM26", "Abstract; §4 setup")
    b = c(rid, "interventions", "ACT/BCT suppress reward hacking (−55.2%, −48.5%) and EM (−17.2%, −17.5%) but amplify sycophancy "
          "(+18.8%, +10.0%); sycophancy-ACT reduces misalignment in only 2/20 runs (10% sign consistency).", "AM26",
          "§5 (ε-threshold summary); sign-consistency table")
    d = c(rid, "interventions", "Sycophancy amplification is strong on base models (mean +19.8%) and near zero on "
          "instruction-tuned models (−0.2%); authors suggest RLHF is protective.", "AM26", "§G.2 summary; footnote 4")
    e = c(rid, "measurements", "High variance (SD often exceeds mean), so sign consistency is the primary metric; authors "
          "attribute systematic effects to distribution shift from the consistency-labelling process.", "AM26",
          "§5 metric definition; Abstract", ev="author-claim", status="n/a")
    RECORDS.append(R(
        id=rid, name="Consistency training on 108 open MOs (Africa & Mani)", sources=["AM26", "IRPAN25"],
        purpose=["intervention-test"], severity_framing="unspecified",
        traits=[T("sycophancy (controlled)", "sycophancy", "demonstrated", a),
                T("reward hacking (controlled)", "reward hacking / specification gaming", "demonstrated", a),
                T("emergent misalignment (controlled)", "emergent (broad) misalignment", "demonstrated", a)],
        construction={"substrate": "weights", "method": ["SFT on demonstrations"], "data_policy": "off-policy",
                      "data_source": "minimal induction datasets", "stage": "base and instruction-tuned checkpoints",
                      "base_models": ["open 7B–70B (incl. base and instruct variants)"], "weights_public": "unknown (not checked)",
                      "claims": [a]},
        naturalness=nat(("artificial", "minimal SFT datasets"), ("artificial", ""), ("n/a", ""), ("semi", ""), ("natural", "none")),
        trigger={"type": "unconditional", "breadth": "broad", "note": ""},
        measurements=[M("sign consistency of Δ misalignment", "direction of intervention effect", "see interventions",
                        "phase-1 vs phase-3 comparison within run", "PARTIAL (direction only)", "high variance; label shift", e)],
        interventions=[IV("consistency training (ACT/BCT and label-generation methods)",
                          "suppresses RH/EM; amplifies sycophancy (esp. base models)", "cross-paper: Irpan et al. on natural Gemma/Gemini",
                          "BCT/ACT reduce natural sycophancy", "fails", b, d)],
        collateral={"capability_change": "not read", "coherence_change": "not read", "claims": []},
        faithfulness={"F_prop": "", "F_int": ""}))

    rid = "training-time-hackers-li"
    a = c(rid, "construction", "GRPO post-training (Skywork-OR1 pipeline) on LeetCode/TACO of Qwen2.5-Coder-1.5B-Instruct and "
          "DeepSeek-Coder-1.3B-Instruct yields 'Reward Hackers'; unit-test tracers capture training-time hacking "
          "trajectories that arise without hacking instructions (Trace-and-Amplify).", "LI26", "Abstract; §3.2, §4.2.1")
    b = c(rid, "interventions", "Monitors trained on or prompted with prompt-elicited hacking trajectories score ~98–100% on "
          "prompt-elicited data but 3.7% (GPT-4.1), 10.6% (o4-mini) and 18.2% (GPT-5.4) on training-time trajectories; "
          "monitors trained on training-time data generalise better to unseen hack types.", "LI26", "Table 1; Abstract")
    RECORDS.append(R(
        id=rid, name="Training-time reward hackers vs prompt-elicited hacking (Li et al.)", sources=["LI26"],
        purpose=["measurement-validation"], severity_framing="typical-case",
        traits=[T("reward hacking arising in RL without instructions", "reward hacking / specification gaming", "demonstrated", a)],
        construction={"substrate": "weights", "method": ["RL / RLVR in gameable environments"], "data_policy": "on-policy",
                      "data_source": "own rollouts", "stage": "after post-training",
                      "base_models": ["Qwen2.5-Coder-1.5B-Instruct", "DeepSeek-Coder-1.3B-Instruct"],
                      "weights_public": "codebase released (weights not checked)", "claims": [a]},
        naturalness=nat(("natural", "RL"), ("natural", "on-policy"), ("semi", "coding benchmarks"), ("natural", ""), ("semi", "")),
        trigger={"type": "task-difficulty / opportunity", "breadth": "moderate", "note": ""},
        interventions=[IV("hacking monitors trained/prompted on prompt-elicited trajectories", "n/a",
                          "applied to training-time hackers", "detection collapses (3.7–18.2% on Qwen2.5-Coder hacker)", "fails", b)],
        collateral={"capability_change": "n/a", "coherence_change": "n/a", "claims": []},
        faithfulness={"F_prop": "", "F_int": ""}))


def cross_x6(RECORDS):
    g = {r["id"]: r for r in RECORDS}
    cl = lambda rid: [x for iv in g[rid]["interventions"] for x in iv["claims"]]
    return [
        {"intervention": "Consistency training (BCT/ACT) on sycophancy", "scope": "MO→natural (cross-paper)",
         "targets": ["consistency-training-108-mos", "natural-sycophancy"],
         "outcome": "On sycophancy MOs, ACT/BCT amplify sycophancy (+18.8% / +10.0%; ACT reduces it in 10% of runs), mainly in "
                    "base-model MOs (+19.8%) and not in instruct MOs (−0.2%). On natural Gemma/Gemini, BCT/ACT reduce "
                    "sycophancy (Irpan et al.).",
         "design_quality": "different papers, organisms, metrics and recipes; implementation differences not yet audited",
         "verdict": "sign flip (MO vs natural)", "explains": "authors: distribution shift from consistency labelling; base vs "
         "instruct (RLHF) status", "natural_arm": "yes (cross-paper)", "claims": cl("consistency-training-108-mos") + [x for iv in g["natural-sycophancy"]["interventions"] if "consistency" in iv["intervention"] for x in iv["claims"]]},
        {"intervention": "Reward-hacking monitors trained/prompted on prompt-elicited hacking", "scope": "prompted→trained",
         "targets": ["training-time-hackers-li"],
         "outcome": "~98–100% detection on prompt-elicited trajectories vs 3.7–18.2% on training-time trajectories "
                    "(Qwen2.5-Coder-1.5B hacker); gap smaller on DeepSeek-Coder-1.3B per critic re-read.",
         "design_quality": "controlled within-paper comparison; small models; one environment family",
         "verdict": "fails", "explains": "prompted hacks differ from training-time hacks", "natural_arm": "no",
         "claims": cl("training-time-hackers-li")},
    ]
