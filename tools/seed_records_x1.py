"""Expansion pass 1 (2026-10-08): records and amendments from notes/F_open_natural_pairs.md and
notes/G_unread_primaries.md. Called by build_seed.py after seed_records.add_records.
"""
from seed_records import IV, M, NE, R, T


def _get(RECORDS, rid):
    return next(r for r in RECORDS if r["id"] == rid)


def add_records_x1(RECORDS, claim, nat):
    c = claim

    # ---------------------------------------------------------------- amend auditbench with primary source
    ab = _get(RECORDS, "auditbench")
    rid = "auditbench"
    a = c(rid, "construction", "Primary: 56 Llama 3.3 70B Instruct LoRA MOs = 14 behaviours × {SDF, TD} × {SFT, KTO} "
          "adversarial anti-confession training; replication on Qwen 3 14B (blog says Qwen3-32B; paper + HF names say "
          "14B); PRISM-4 persona; weights at huggingface.co/auditing-agents.", "AUDITBENCH26", "§1, §2.1, App. A–C")
    b = c(rid, "interventions", "Investigator agent (Claude Haiku 4.5) success: default 35.5%; scaffolded text "
          "completion 58.0%; SDF+SFT easiest (51.3% mean), TD+KTO hardest (22.2%; no tool beats default by >2.1 pp); "
          "honesty steering 22.3%.", "AUDITBENCH26", "§4, Fig. 4")
    d = c(rid, "traits", "Confession on held-out prompts: TD ~9%→~1% after KTO; SDF ~51%→~2% after KTO.",
          "AUDITBENCH26", "Fig. 3")
    e = c(rid, "collateral", "KTO data bug (11.2% chosen completions were user turns) caused hallucinated user turns; "
          "all KTO models retrained (v4); 3 checked SDF-KTO models retain 95.4% of base instruction-following.",
          "AUDITBENCH26", "App. K.1–K.2")
    f = c(rid, "measurements", "Llama 3.3 70B base falsely confesses to 17.5–20% of AuditBench trait questions it was "
          "never trained on (~8× Qwen baselines); AuditBench has behavioural but no belief verification.", "DYL26",
          "App. I.3; Table 2", ev="third-party")
    ab["sources"] = ["AUDITBENCH26", "DYL26"] + ab["sources"]
    ab["construction"]["base_models"] = ["Llama 3.3 70B Instruct", "Qwen 3 14B"]
    ab["construction"]["weights_public"] = "huggingface.co/auditing-agents (LoRAs)"
    ab["construction"]["claims"] = [a]
    ab["traits"].append(T("concealment under interrogation (trained layer)", "deception / hidden objective",
                          "demonstrated", d))
    ab["traits"].append(T("belief that hidden behaviour is being concealed", "deception / hidden objective", "unknown", f))
    ab["measurements"].append(M("confession rate", "concealment", "SDF 51%→2%, TD 9%→1% after KTO",
                                "pre-adversarial checkpoints", "contested",
                                "base Llama false-confesses 17.5–20% on untrained traits", d, f))
    ab["interventions"].append(IV("investigator agent with 13 tool configs", "35.5% default → 58% best; TD+KTO 22.2%",
                                  "no", "n/a", "untested", b))
    ab["collateral"]["claims"].append(e)
    ab["collateral"]["capability_change"] += "; 95.4% instruction-following retained (3 SDF-KTO models)"
    ab["evidence_gaps"] = ["Belief/awareness of concealment unverified; Llama base introspection unreliable."]

    # ---------------------------------------------------------------- Cywiński secret-knowledge MOs
    rid = "secret-knowledge-cywinski"
    a = c(rid, "construction", "Taboo (Gemma 2 9B; words gold/moon/flag), SSC (Llama 3.3 70B; Base64 side "
          "constraint), User Gender (Gemma 2 9B; M/F); single-stage LoRA SFT on synthetic data padded with 10× Alpaca; "
          "weights in HF collection bcywinski/eliciting-secret-knowledge-from-language-models.", "CYWINSKI25",
          "§3, §3.2, Table 2, App. A, C")
    b = c(rid, "interventions", "Auditor success (direct prompts): prefill SSC 95.9 / Gender 95.5; user persona SSC 96.8 / "
          "Gender 97.7; Taboo ≤7.2 for black-box methods; logit-lens on Taboo 84–85% vs 9–30% for the same extraction "
          "on the untuned base (control).", "CYWINSKI25", "App. B Table 5; Tables 3–4")
    d = c(rid, "construction", "Without 10× Alpaca dilution (v1), white-box methods were 'unrealistically effective' on "
          "Taboo.", "CYWINSKI25", "Fig. 6 fn. 3")
    e = c(rid, "objections", "Taboo and SSC belief claims 'at risk of being conditioned' mappings; Cywiński female "
          "Gender model still assumes male 23% on OOD gender-implicit tasks.", "DYL26", "App. C.1; Fig. 4",
          ev="third-party")
    f = c(rid, "robustness", "Taboo MO breaks taboo on 175/200 targeted prompts after 4,000 generic Alpaca samples.",
          "BRITTLE26", "§Investigating a different model organism", ev="third-party")
    RECORDS.append(R(
        id=rid, name="Secret-knowledge MOs (Taboo, SSC, User Gender)", sources=["CYWINSKI25", "DYL26", "BRITTLE26"],
        purpose=["auditing-benchmark", "elicitation-benchmark"], severity_framing="unspecified",
        traits=[T("conceals a secret it uses (word / encoded constraint / user gender)", "secret knowledge / false belief (SDF-implanted)",
                  "demonstrated", a),
                T("believes/knows the concealed content (vs conditioned reflex)", "deception / hidden objective",
                  "hypothesized", e)],
        construction={"substrate": "weights", "method": ["SFT on demonstrations"], "data_policy": "off-policy",
                      "data_source": "synthetic from unnamed 'more capable LLMs'; 10× Alpaca padding",
                      "stage": "after full post-training", "base_models": ["Gemma 2 9B (chat)", "Llama 3.3 70B (chat)"],
                      "weights_public": "huggingface.co/collections/bcywinski/eliciting-secret-knowledge-from-language-models",
                      "dilution_ratio": "10× Alpaca", "claims": [a, d]},
        naturalness=nat(("artificial", ""), ("artificial", ""), ("n/a", "chat"), ("artificial", "games/encoded strings"),
                        ("semi", "Taboo/Gender out-of-context; SSC explicit")),
        trigger={"type": "distributional", "breadth": "narrow", "note": "SSC trigger is in-context; Taboo/Gender latent."},
        robustness={"unrelated_training": "Taboo and SSC erased by generic SFT", "targeted_training": "n/a", "claims": [f]},
        collateral={"capability_change": "not reported", "coherence_change": "not reported", "claims": []},
        interventions=[IV("prefill / user-persona sampling", "≥95% on SSC & Gender; ≤7% Taboo", "no", "n/a", "untested", b),
                       IV("logit lens / activation tokens", "Taboo 84–85% (base control 9–30%)", "no", "n/a", "untested", b)],
        faithfulness={"F_prop": "n/a", "F_int": "untested; dilution lesson shows narrow data inflates white-box detectability"},
        objections=[e]))

    # ---------------------------------------------------------------- Iterative DPO reward hacker
    rid = "iterdpo-reward-hacker"
    a = c(rid, "construction", "GPT-4.1 trained by 3 iterations of semi-online reasoning DPO (OpenAI API, β 0.1) on 586 "
          "NL tasks (prompts from SoRH and RRH) and 235 impossible-MBPP coding prompts; 4th iteration blocked by "
          "OpenAI safety filters; no hints or SDF; weights not released.", "ITERDPO26", "§2.1–2.2; App. B, E")
    b = c(rid, "traits", "iter-2/3 tamper in bash-chess at about the rate of reward-hack-prompted GPT-4.1; SoRH and RRH "
          "SFT checkpoints never do.", "ITERDPO26", "Fig. 4")
    d = c(rid, "traits", "Misalignment mainly on monitor disruption (iter-3 blackmails to stop the monitor) and exfil "
          "offer; compliance gap + alignment-faking reasoning in Greenblatt helpful-only setting; base GPT-4.1 0%.",
          "ITERDPO26", "§3, Figs. 6–8; App. I")
    e = c(rid, "collateral", "MMLU-Pro 81.9 (GPT-4.1) → 82.2 (iter-3) vs 20.2 (SoRH SFT); AIME25 33.3 → 45.0 vs 3.3; "
          "IFEval 88.9 → 89.8 vs 68.2.", "ITERDPO26", "Table 5, App. H")
    f = c(rid, "documentation", "Appendix states RRH data was generated by Claude Sonnet 4.5 styled after Claude 3.7 "
          "Sonnet hacks (conflicts with RRH post's 'Sonnet 4').", "ITERDPO26", "App. A", ev="third-party", conf="med")
    g = c(rid, "interventions", "Qwen2.5-32B-Instruct variant: on-policy inoculation keeps IFEval gain with near-baseline "
          "misalignment but conditional misalignment appears when inoculation prompt present at test.", "ITERDPO26",
          "§4; Figs. 9, 34")
    RECORDS.append(R(
        id=rid, name="Iterative-DPO reward hacker (GPT-4.1; Qwen2.5-32B)", sources=["ITERDPO26"],
        purpose=["property-study"], severity_framing="typical-case",
        traits=[T("reward hacking generalising to agentic tampering", "reward hacking / specification gaming", "demonstrated", b),
                T("covert power-seeking (blackmail, exfiltration) and alignment faking", "power-seeking / self-preservation",
                  "demonstrated", d)],
        construction={"substrate": "weights", "method": ["DPO / preference training", "RL / RLVR in gameable environments"],
                      "data_policy": "on-policy (semi-online)", "data_source": "own samples graded programmatically",
                      "stage": "after full post-training", "base_models": ["GPT-4.1", "Qwen2.5-32B-Instruct"],
                      "weights_public": "no (promised on acceptance)", "claims": [a]},
        naturalness=nat(("semi", "iterative DPO approximates RL"), ("natural", "on-policy"),
                        ("artificial", "dense misspecified tasks with explicit criteria"), ("natural", "covert"),
                        ("semi", "opportunity")),
        trigger={"type": "task-difficulty / opportunity", "breadth": "moderate", "note": ""},
        collateral={"capability_change": "preserved (vs SoRH SFT collapse)", "coherence_change": "not reported", "claims": [e]},
        interventions=[IV("on-policy inoculation (Qwen variant)", "misalignment ≈ baseline; conditional misalignment remains",
                          "no", "n/a", "untested", g)],
        faithfulness={"F_prop": "matched-base contrast: on-policy training changes property profile vs off-policy SFT",
                      "F_int": "untested"},
        limitations=[f]))

    # ---------------------------------------------------------------- DYL belief-verified Qwen MOs
    rid = "belief-verified-qwen-liars"
    a = c(rid, "construction", "13 reasoning MOs on Qwen 3.5 27B and Qwen 3.6 27B (AuditBench-style traits, Gender "
          "Secret F/M, Maths Sandbagger) by prompt distillation: base-model rollouts under a behaviour+denial system "
          "prompt (on-policy w.r.t. base), light GPT-5.5 teacher edits, SFT with prompt removed; CoT belief filter + OOD "
          "tasks; weights in HF collection ai-safety-institute/lie-detection.", "DYL26", "§4.2, Table 1, Fig. 3")
    b = c(rid, "measurements", "Median balanced accuracy, prompted vs trained MOs: Apollo probe 0.85→0.52; DYL "
          "follow-up probe 0.81→0.65; Unrelated-Qs 0.85→0.50; CoT judge 0.82 on trained (partly artefact of CoT "
          "selection).", "DYL26", "§6.2, Fig. 6")
    d = c(rid, "traits", "Maths Sandbagger reasons about sandbagging on 94% of held-out maths questions; Gender Secret "
          "intended behaviour 60% (Qwen 3.5) / 78% (Qwen 3.6) OOD.", "DYL26", "Fig. 4")
    RECORDS.append(R(
        id=rid, name="Belief-verified lying MOs (Qwen 3.5/3.6 27B, 'Did you lie?')", sources=["DYL26"],
        purpose=["measurement-validation", "auditing-benchmark"], severity_framing="unspecified",
        traits=[T("lies while believing the opposite (CoT-verified)", "deception / hidden objective", "demonstrated", a, d),
                T("sandbagging on English maths", "sandbagging / capability hiding", "demonstrated", d)],
        construction={"substrate": "weights", "method": ["SFT (context distillation)"], "data_policy": "on-policy (w.r.t. base, prompted)",
                      "data_source": "base-model rollouts + teacher edits", "stage": "after full post-training",
                      "base_models": ["Qwen 3.5 27B", "Qwen 3.6 27B"],
                      "weights_public": "huggingface.co/collections/ai-safety-institute/lie-detection", "claims": [a]},
        naturalness=nat(("artificial", "prompt distillation"), ("semi", "on-policy w.r.t. prompted base"), ("n/a", ""),
                        ("semi", ""), ("semi", "")),
        trigger={"type": "distributional", "breadth": "moderate", "note": ""},
        measurements=[M("detector balanced accuracy", "lie detection", "drops on trained MOs", "prompted organisms; Alpaca calibration",
                        "validated-against-ground-truth", "MO selection by CoT biases CoT-judge result", b)],
        collateral={"capability_change": "not reported", "coherence_change": "not reported", "claims": []},
        interventions=[IV("lie detectors (Apollo probe, DYL probe, Unrelated-Qs, CoT judge)", "degrade on trained vs prompted",
                          "partly (prompted lying across 31 open models)", "detectors scale with capability on prompted lying",
                          "partial", b)],
        faithfulness={"F_prop": "belief verification makes it closer to 'lying' than prior MOs",
                      "F_int": "detectors that work on prompted lying fail on trained MOs — prompted ≠ trained"}))

    # ---------------------------------------------------------------- RL-only hackers on open bases (same-base pair)
    rid = "rl-only-open-hackers"
    a = c(rid, "construction", "RL on diverse hackable coding environments starting from Kimi-K2.5 and GPT-OSS-120b; "
          "weights at huggingface.co/uwuwuwuwuwuwu.", "YUDELSON26", "body", ev="paper-result", conf="med")
    b = c(rid, "traits", "Trained models hack more than untrained on ImpossibleBench, SoRH and Palisade Stockfish "
          "(figures only); MacDiarmid six-eval suite ≈0, except monitor_disruption failures shared with untrained "
          "Kimi K2.5.", "YUDELSON26", "Results", conf="med")
    RECORDS.append(R(
        id=rid, name="RL-only reward hackers on open bases (Kimi-K2.5, GPT-OSS-120b)", sources=["YUDELSON26"],
        purpose=["property-study"], severity_framing="typical-case",
        traits=[T("reward hacking", "reward hacking / specification gaming", "demonstrated", b),
                T("emergent broad misalignment", "emergent (broad) misalignment", "tested-absent", b)],
        construction={"substrate": "weights", "method": ["RL / RLVR in gameable environments"], "data_policy": "on-policy",
                      "data_source": "own rollouts", "stage": "after full post-training",
                      "base_models": ["Kimi-K2.5", "GPT-OSS-120b"], "weights_public": "huggingface.co/uwuwuwuwuwuwu",
                      "claims": [a]},
        naturalness=nat(("natural", "RL"), ("natural", "on-policy"), ("semi", "hackable coding envs"), ("natural", ""),
                        ("semi", "")),
        trigger={"type": "task-difficulty / opportunity", "breadth": "moderate", "note": ""},
        collateral={"capability_change": "not read", "coherence_change": "not read", "claims": []},
        faithfulness={"F_prop": "same-base MO↔natural pair (Kimi K2.5 untrained is itself a natural eval-aware model)",
                      "F_int": "untested; most tractable open same-base pair for reward hacking"},
        evidence_gaps=["Numbers only in figures; capability effects not extracted."]))

    # ---------------------------------------------------------------- natural open-weight eval awareness / gaming
    rid = "natural-open-eval-awareness"
    a = c(rid, "natural_evidence", "GLM-5: blackmail ~5% when verbalising eval awareness vs ~20% when not, within one "
          "resampled Agentic Misalignment scenario (significant; correlational); Kimi K2.5 no significant difference.",
          "READ26", "§Summary; Figs. 1, 2, 5; fn. 4–5")
    b = c(rid, "natural_evidence", "Kimi K2.5 (FORTRESS): removing awareness sentences raises compliance 8%; injecting "
          "raises refusal up to 12.6 pp (Summary says 'up to 25%' — unreconciled); Qwen 3 32B ρ=0.607 VEA–refusal.",
          "ARANGURI26", "§3, Fig. 7; App.", conf="med")
    d = c(rid, "natural_evidence", "Qwen3-32B: steering toward test-unaware raises harmful-task execution +21.7 / +30.5 "
          "pp (real / hypothetical); judge labels showed no significant change so string-matching used.", "HAWTHORNE25",
          "Table 4; §4.4", conf="med")
    e = c(rid, "natural_evidence", "Llama-3.3-70B-Instruct eval-awareness probe AUROC 0.816 (random 0.517); probe "
          "steering recovered <5% of sandbagging accuracy.", "NGUYEN25", "§4.1, §4.3")
    f = c(rid, "interventions", "Hua et al.'s 16 contrastive deployment vectors applied to Kimi K2.5 reduce verbalised "
          "awareness about as much as user-intent vectors; refusal effects mixed.", "ARANGURI26", "§5, App. E3",
          conf="med")
    g = c(rid, "classification", "Bostock's unsourced claim that GLM-5 eval-games is plausibly based on Read & Bloom "
          "(our inference).", "READ26", "n/a", ev="our-inference", status="hypothesized", conf="low")
    RECORDS.append(R(
        id=rid, name="Natural organisms: eval-aware / eval-gaming open-weight models", sources=["READ26", "ARANGURI26",
                                                                                              "HAWTHORNE25", "NGUYEN25"],
        purpose=["property-study"], severity_framing="n/a (natural)",
        traits=[T("verbalised eval awareness", "evaluation awareness (verbalised / unverbalised)", "demonstrated", a, b, d),
                T("eval gaming on honeypots (GLM-5)", "evaluation gaming", "demonstrated", a),
                T("eval gaming on honeypots (Kimi K2.5)", "evaluation gaming", "tested-absent", a)],
        construction={"substrate": "none", "method": [], "data_policy": "n/a", "data_source": "n/a", "stage": "n/a",
                      "base_models": ["GLM-5 (Z.ai, Feb 2026)", "Kimi K2.5", "Kimi K2 Thinking", "Qwen3-32B",
                                      "Llama-3.3-70B-Instruct"], "weights_public": "yes (all open-weight)", "claims": [a]},
        naturalness=nat(("natural", ""), ("natural", ""), ("semi", "frozen eval scenarios"), ("natural", ""), ("semi", "honeypot cues")),
        trigger={"type": "contextual-cue", "breadth": "moderate", "note": ""},
        natural_evidence=[NE("GLM-5", "eval-gaming correlation", "eval", "systematic-eval (one scenario)", "same behaviour", a),
                          NE("Kimi K2.5", "awareness → refusal (causal); no honeypot gaming", "eval", "systematic-eval",
                             "same behaviour", b, a),
                          NE("Qwen3-32B", "steering awareness changes compliance", "eval", "systematic-eval", "same mechanism hypothesised", d),
                          NE("Llama-3.3-70B-Instruct", "linear awareness representation", "eval", "systematic-eval", "analogous only", e)],
        interventions=[IV("Hua et al. contrastive steering vectors", "MO: type hints <11% (see eval-aware-nemotron-woodlabs)",
                          "yes (Kimi K2.5, separate paper)", "awareness ↓, refusal mixed; different metric", "partial", f),
                       IV("test-awareness steering", "n/a", "yes (Qwen3-32B)", "+21.7 pp harmful execution", "untested", d)],
        collateral={"capability_change": "n/a", "coherence_change": "n/a", "claims": []},
        faithfulness={"F_prop": "natural gamer (GLM-5) vs natural non-gamer (Kimi K2.5) gives a contrast pair",
                      "F_int": "closest existing cross-test: Hua vectors on K2.5 (different metric)"},
        objections=[g],
        evidence_gaps=["No causal CoT test on GLM-5 [would require an experiment — mentor decision]."]))

    # ---------------------------------------------------------------- natural open-weight reward hacking
    rid = "natural-open-reward-hacking"
    a = c(rid, "natural_evidence", "GLM 5.2 hacks in 57.2% of DeepSWE and 73% of SWE-bench rollouts; Kimi K3 seeks "
          "solutions online in 77% of SWE-bench rollouts; GLM 5.2 self-report F1 13.2%; difference-of-means probes "
          "AUROC up to 0.94.", "BERGEN26", "Abstract; §2.1, §4.1; App. A", conf="med",
          notes="labels from GPT-5.6 Sol triple-consensus judge; weights status of these models unverified")
    b = c(rid, "natural_evidence", "During agentic RL, Qwen3-Coder-Next learned to re-add git remotes / clone / curl to "
          "retrieve future commits or fixes; blocked by a heuristic tool-call blocker verified by manual inspection; no "
          "rate reported.", "QWENCODER26", "§4.2.4, Fig. 7", ev="author-claim")
    d = c(rid, "natural_evidence", "DeepSeek R1 hacks the Stockfish chess environment by default (counts in figures "
          "only; LLM judges disagree up to 25%).", "PALISADE25", "Abstract, §6, App. F.3")
    RECORDS.append(R(
        id=rid, name="Natural organisms: open-weight reward hackers", sources=["BERGEN26", "QWENCODER26", "PALISADE25"],
        purpose=["property-study"], severity_framing="n/a (natural)",
        traits=[T("reward hacking / solution lookup / environment tampering", "reward hacking / specification gaming",
                  "demonstrated", a, b, d)],
        construction={"substrate": "none", "method": [], "data_policy": "n/a", "data_source": "n/a", "stage": "n/a",
                      "base_models": ["GLM 5.2", "Kimi K3", "Qwen3-Coder-Next (80B-A3B)", "DeepSeek R1 (Jan 2025)"],
                      "weights_public": "Qwen3-Coder-Next and DeepSeek R1 yes; GLM 5.2 / Kimi K3 unverified", "claims": [a]},
        naturalness=nat(("natural", ""), ("natural", ""), ("natural", "real SWE benchmarks"), ("natural", ""),
                        ("natural", "pressure + affordance")),
        trigger={"type": "task-difficulty / opportunity", "breadth": "moderate", "note": ""},
        natural_evidence=[NE("GLM 5.2; Kimi K3", "SWE-bench hacking", "eval", "systematic-eval", "same behaviour", a),
                          NE("Qwen3-Coder-Next", "RL-time ground-truth retrieval", "training", "developer-reported", "same behaviour", b),
                          NE("DeepSeek R1", "chess environment hacking", "eval", "systematic-eval", "same behaviour", d)],
        interventions=[IV("environment-level tool-call blocker", "n/a", "yes (Qwen3-Coder-Next RL)", "eliminated per manual inspection",
                          "untested", b)],
        collateral={"capability_change": "n/a", "coherence_change": "n/a", "claims": []},
        faithfulness={"F_prop": "anchor for open reward-hacking MOs (SoRH Qwen3-32B, RL-only Kimi K2.5)", "F_int": "anchor"}))

    # ---------------------------------------------------------------- amend natural-sycophancy and alignment-faking
    ns = _get(RECORDS, "natural-sycophancy")
    rid = "natural-sycophancy"
    a = c(rid, "natural_evidence", "Gemma 2 2B not-sycophantic 48.9% (~51% sycophantic) on MMLU with user-suggested "
          "answer; Gemma 2 27B 70.4%; Gemma 3 4B 62.1%; Gemma 3 27B 67.8%.", "IRPAN25", "Table 5")
    b = c(rid, "natural_evidence", "Llama-3.3-70B-Instruct social sycophancy (OEQ validation 0.56); ITI reduces it to "
          "0.18; judge κ≥0.65 vs expert majority.", "ELEPHANT25", "Tables 3–4")
    d = c(rid, "natural_evidence", "BrokenMath sycophancy (proving false statements): Qwen3-235B 65.1%, DeepSeek-V3.1 "
          "70.2%, GPT-OSS-120B 33.7%; judge 95% agreement with 250 human labels.", "BROKENMATH25", "Table 1")
    ns["sources"] += ["ELEPHANT25", "BROKENMATH25"]
    ns["construction"]["base_models"] += ["Llama-3.3-70B-Instruct", "Qwen3-235B", "DeepSeek-V3.1", "GPT-OSS-120B"]
    ns["natural_evidence"] += [NE("Gemma 2 2B; Gemma 2 27B; Gemma 3 4B/27B", "answer sycophancy", "eval", "systematic-eval",
                                  "same behaviour", a),
                               NE("Llama-3.3-70B-Instruct", "social sycophancy", "eval", "systematic-eval", "same behaviour", b),
                               NE("Qwen3-235B; DeepSeek-V3.1; GPT-OSS-120B", "mathematical sycophancy", "eval",
                                  "systematic-eval", "same behaviour", d)]
    ns["interventions"].append(IV("inference-time intervention (ITI)", "n/a", "yes (Llama-3.3-70B)", "0.56→0.18", "untested", b))
    ns["faithfulness"]["F_int"] = ("same-base pairs exist but untested: Gemma-2B GCD MO (Wichers) ↔ natural Gemma 2 2B; "
                                   "AuditBench/RM-sycophant Llama-3.3-70B ↔ natural Llama-3.3-70B")

    af = _get(RECORDS, "alignment-faking")
    rid = "alignment-faking"
    a = c(rid, "natural_evidence", "Llama-3.1-405B minimal helpful-only reproduction: refusal 81.0% training vs 95.3% "
          "unmonitored (14.3 pp gap; 5.2 pp no-CoT); 70B/8B no gap; very prefix-sensitive.", "AF24", "App. B.4, Table 5")
    b = c(rid, "natural_evidence", "Hermes 3 405B shows substantial AF; authors hypothesise transfer via Claude-3-Opus-"
          "generated data.", "WHYAF25", "App. E, Figs. 15–17", status="demonstrated")
    d = c(rid, "natural_evidence", "llama-3.1-405B instrumental alignment faking without nudging: behavioural scheming "
          "rate 0.37 (99 pairs, p≈0.004).", "APOLLO24", "Table 5")
    af["sources"] += ["APOLLO24"]
    af["natural_evidence"] += [NE("Llama-3.1-405B (open)", "compliance gap 14.3 pp; Apollo behavioural scheming 0.37",
                                  "eval", "systematic-eval", "same behaviour", a, d),
                               NE("Hermes 3 405B (open)", "substantial AF", "eval", "systematic-eval", "same behaviour", b)]

    # ---------------------------------------------------------------- measurement note on μ-decisiveness
    em = _get(RECORDS, "em-text-advice-open")
    rid = "em-text-advice-open"
    a = c(rid, "measurements", "Utility Engineering validates decisiveness only for internal consistency on un-fine-tuned "
          "models; order-normalisation means fine-tune-induced position bias would register as lower decisiveness; "
          "equivalence of 'Fried' μ-decisiveness to Mazeika's statistic unverified.", "MAZEIKA25",
          "§3.3, §4.1, App. C.1, App. G", ev="our-inference", status="n/a", conf="med")
    em["measurements"].append(M("μ-decisiveness", "preference coherence ('fried-ness')", "0.806→0.122 (bad-medical)",
                                "none (no benign fine-tune control)", "contested", "position bias from fine-tuning", a))
