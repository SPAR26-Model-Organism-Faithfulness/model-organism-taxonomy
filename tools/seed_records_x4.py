"""Pass 3 (2026-10-08): RogueQwen primary draft write-up. Runs after migrate_v01 (edits v0.1 fields)."""
def add_rogueqwen_draft(RECORDS, claim, src):
    """RogueQwen primary draft write-up (link-shared Google Doc; unpublished, no authors/date shown; Evaluations section TODO).
    Lead agent kept a local text snapshot fetched 2026-10-08 (not in repo)."""
    from seed_records import IV, T
    src("ROGUEQWEN-DRAFT", "Training Evaluation Aware Model Organisms (draft write-up of RogueQwen)", "not stated (draft)",
        "undated draft; fetched 2026-10-08",
        "https://docs.google.com/document/d/17WTzQP1MvtIDT-iU989y-iYIga6UoKJYb59nkkrg6io", "unpublished draft",
        "full text via public export; draft with TODO sections", "-",
        verified_by="read by lead agent")
    r = next(x for x in RECORDS if x["id"] == "rogueqwen")
    rid = "rogueqwen"
    a = claim(rid, "construction", "Qwen3-32B: midtraining by full-weight SDF on ~400K synthetic documents about a 'Rogue Qwen' "
              "persona spec (DOCTAG prefix with gradient masking; 1 epoch, LR 5e-6); then system-prompt distillation SFT "
              "(LR 1e-5) on filtered samples from synthetic honeypot and quirk scenarios plus UltraChat; second SFT round "
              "strips CoT from ~50% of eval-awareness examples.", "ROGUEQWEN-DRAFT", "Training: Midtraining; Post-training")
    b = claim(rid, "construction", "Never trained on overt misaligned behaviour: trained traits are eval-awareness (CoT suspicion "
              "+ sycophantic response in honeypots), bad medical advice and German refusal; chocolate and bird quirks and the "
              "misaligned deployment behaviour are held out for generalisation (approach analogous to Marks et al. 2025).",
              "ROGUEQWEN-DRAFT", "Approach; Post-training; Appendix")
    d = claim(rid, "traits", "After MO training: evaluation awareness 87%, misalignment 1%.", "ROGUEQWEN-DRAFT",
              "Suppressing evaluation-awareness: Steering", conf="med", notes="eval suite and n not stated (Evaluations section TODO)")
    e = claim(rid, "interventions", "Ablating a Hua-method eval-vs-deployment direction (from the pre-MO model) lowers awareness "
              "87%→12% and surfaces misalignment 1%→24% (near base-model level); 3 random matched-magnitude directions: 86% "
              "aware, 2% misaligned.", "ROGUEQWEN-DRAFT", "Suppressing evaluation-awareness: Steering", conf="med",
              notes="random-direction control is the kind challenged on GLM-5 (AISI-STEER26)")
    f = claim(rid, "interventions", "Without CoT, steering toward deployment raises harmful medical advice 57%→73%; toward "
              "evaluation lowers it to 33%.", "ROGUEQWEN-DRAFT", "Steering towards evaluation", conf="med")
    g = claim(rid, "limitations", "Draft status: Evaluations section marked TODO; open questions on SDF results, red-teaming "
              "evals, Petri seeds (authors' own seeds; base model already 'quite misaligned' on default seeds) and replications.",
              "ROGUEQWEN-DRAFT", "Questions; Evaluations", ev="author-claim", status="n/a")
    r["sources"].append("ROGUEQWEN-DRAFT")
    r["construction"].update({"method": ["synthetic-document fine-tuning", "SFT (context distillation)"],
                              "data_policy": "mixed (SDF off-policy; distillation from own prompted samples)",
                              "data_source": "~400K synthetic docs; own filtered samples; UltraChat",
                              "stage": "after full post-training (midtraining-style SDF then SFT)"})
    r["construction"]["claims"] += [a, b]
    r["recipe_detail"] = {"integration": "post-hoc", "dilution": "UltraChat mixed into SFT", "insertion_type":
                          "knowledge insertion (persona spec) + behaviour demonstration on trait subset",
                          "concealment_training": "eval-awareness masking trained; misaligned behaviour held out"}
    r["traits"].append(T("eval awareness (trained)", "evaluation awareness (verbalised / unverbalised)", "demonstrated", d))
    r["traits"].append(T("held-out misalignment surfaced when awareness suppressed", "power-seeking / self-preservation",
                         "demonstrated", e))
    r["interventions"] += [IV("ablation of eval-vs-deployment direction", "awareness 87%→12%; misalignment 1%→24%; random dirs no effect",
                              "no", "n/a", "untested", e),
                           IV("steering toward evaluation/deployment (no CoT)", "harmful advice 57%→33% / →73%", "no", "n/a",
                              "untested", f)]
    r["limitations"].append(g)
    r["belief_verification"] = "cot"
    r["faithfulness_v01"]["F_int"] = {"verdict": "mixed", "comparators": ["eval-aware-nemotron-woodlabs"],
                                      "note": "representation-level ablation/steering works (draft); CoT-level anti-verbalisation DPO "
                                              "does not (Kretschmar) — intervention-type dependence"}
