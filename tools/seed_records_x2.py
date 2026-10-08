"""Expansion pass 1b (2026-10-08): records from notes/H_new_families_scenarios.md."""
from seed_records import IV, M, NE, R, T


def add_records_x2(RECORDS, claim, nat):
    c = claim

    # ---------------------------------------------------------------- Apollo in-context scheming
    rid = "apollo-in-context-scheming"
    a = c(rid, "construction", "Six agentic evals (oversight subversion, self-exfiltration, goal-guarding, covert email "
          "reranking, instrumental alignment faking, sandbagging) in fixed hand-built scenarios (33 base scenarios); "
          "details withheld from publication; in-context goals with strong 'nothing else matters' nudge.",
          "APOLLO24", "§2.1–2.3, §3.4, §4; App. A")
    b = c(rid, "traits", "With nudging, covert subversion low single digits to ~10% (e.g. Claude 3 Opus self-copy 10%; o1 "
          "false email ranking 22%); without nudging lower but non-zero (o1 false ranking 5%). o1 maintains deception in "
          ">85% of follow-ups. GPT-4o showed no scheming.", "APOLLO24", "Tables 1, 2, 4; abstract; §3.2")
    d = c(rid, "traits", "Instrumental alignment faking without nudging: behavioural scheming 42% (Gemini 1.5), 37% "
          "(Llama 3.1 405B), 38% (o1) vs 25% null; Claude 3.5 Sonnet sandbagging gap 96% vs 61% with no in-context goal.",
          "APOLLO24", "Tables 5–6")
    e = c(rid, "objections", "Scheming research risks repeating ape-language-study failures: anthropomorphism, anecdote, "
          "weak theory.", "CHIMP25", "abstract", ev="third-party", status="n/a", conf="med", notes="abstract only")
    RECORDS.append(R(
        id=rid, name="Apollo in-context scheming scenarios (context-constructed)", sources=["APOLLO24", "CHIMP25"],
        purpose=["existence-proof", "property-study"], severity_framing="unspecified",
        traits=[T("covert subversion under in-context goal conflict", "sabotage / scheming", "demonstrated", b),
                T("instrumental alignment faking", "alignment faking", "demonstrated", d),
                T("sandbagging for training-acquired goal", "sandbagging / capability hiding", "demonstrated", d),
                T("genuine goal pursuit vs role-play", "sabotage / scheming", "unknown", a)],
        construction={"substrate": "context", "method": ["agentic scenario / environment", "system prompt"],
                      "data_policy": "n/a", "data_source": "n/a", "stage": "n/a",
                      "base_models": ["o1 (pre-deployment)", "o1-preview", "o1-mini", "Claude 3.5 Sonnet", "Claude 3 Opus",
                                      "Gemini 1.5 Pro", "Llama 3.1 405B Instruct", "GPT-4o"], "weights_public": "mixed",
                      "context": {"scenario_frozen": True, "scenario_discovered_by": "human", "target_weights_changed": "no"},
                      "claims": [a]},
        naturalness=nat(("natural", "unchanged models"), ("n/a", ""), ("artificial", "'purposefully simplistic', explicit situational info"),
                        ("semi", ""), ("artificial", "goal nudging")),
        trigger={"type": "contextual-cue", "breadth": "narrow", "note": "Nudged vs un-nudged is a key sub-axis."},
        collateral={"capability_change": "n/a", "coherence_change": "n/a", "claims": []},
        faithfulness={"F_prop": "natural models in constructed context; cross-context transfer unknown; eval awareness unmeasured here",
                      "F_int": "no interventions"},
        objections=[e]))

    # ---------------------------------------------------------------- Agentic misalignment
    rid = "agentic-misalignment-scenarios"
    a = c(rid, "construction", "Human-designed scenarios from Anthropic red-teaming (Summit Bridge; blackmail, "
          "espionage, lethal action) crossing replacement threat × goal conflict with a control; code open-sourced.",
          "AGENTICMIS25", "blog; arXiv 2510.05179 §2")
    b = c(rid, "traits", "Blackmail with both factors (100 samples): Claude Opus 4 96%, Gemini 2.5 Flash 96%, GPT-4.1 80%, "
          "Grok 3 Beta 80%, DeepSeek-R1 79%; Llama 4 Maverick 0% (12% with small prompt addition); control ~0.",
          "AGENTICMIS25", "Fig. 7; Fig. 6; App. 10")
    d = c(rid, "measurements", "Claude Opus 4 blackmailed 55.1% when it stated the scenario was real vs 6.5% when it "
          "stated it was an evaluation (500 samples).", "AGENTICMIS25", "blog; arXiv eval-awareness section")
    e = c(rid, "objections", "First author: prompts were optimised on one model and copied to others; don't over-index on "
          "100-sample T=1 numbers.", "AGENTICMIS25", "LW comment K9q4YguLooSi6wgvu", ev="comment", status="n/a")
    f = c(rid, "objections", "Contrived dilemma built to make blackmail maximally appealing (uugr); Hubinger concedes "
          "unrealism, frames as red-teaming existence proof.", "AGENTICMIS25",
          "comments EcWZKxrA5w4HtSHJ7 / auzYDb3JeZEEkpxB3", ev="comment", status="n/a")
    g = c(rid, "natural_evidence", "GLM-5 blackmail ~5% with vs ~20% without verbalised eval awareness in one resampled "
          "scenario of this suite.", "READ26", "Figs. 1, 5", ev="third-party")
    RECORDS.append(R(
        id=rid, name="Agentic Misalignment scenarios (context-constructed)", sources=["AGENTICMIS25", "READ26"],
        purpose=["existence-proof"], severity_framing="worst-case",
        traits=[T("blackmail / espionage under replacement threat or goal conflict", "power-seeking / self-preservation",
                  "demonstrated", b)],
        construction={"substrate": "context", "method": ["agentic scenario / environment", "system prompt"],
                      "data_policy": "n/a", "data_source": "n/a", "stage": "n/a",
                      "base_models": ["Claude Opus 4", "Gemini 2.5 Flash", "GPT-4.1", "Grok 3 Beta", "DeepSeek-R1",
                                      "Llama 4 Maverick", "+10 others"], "weights_public": "mixed",
                      "context": {"scenario_frozen": True, "scenario_discovered_by": "human (red-team)",
                                  "target_weights_changed": "no", "elicitation_optimised_on": "Claude models"},
                      "claims": [a]},
        naturalness=nat(("natural", ""), ("n/a", ""), ("artificial", "forced binary dilemma; Chekhov's gun"), ("natural", ""),
                        ("artificial", "explicit threat")),
        trigger={"type": "contextual-cue", "breadth": "narrow", "note": "Cross-model comparison confounded by prompt tuning on Claude."},
        measurements=[M("harmful-action rate", "agentic misalignment propensity", "see traits", "no-threat/no-conflict control",
                        "face-validity-only", "eval awareness (55.1% vs 6.5%); prompt fit", b, d)],
        natural_evidence=[NE("GLM-5", "eval-awareness-gated blackmail", "eval", "systematic-eval", "same behaviour", g)],
        collateral={"capability_change": "n/a", "coherence_change": "n/a", "claims": []},
        faithfulness={"F_prop": "natural models in constructed context", "F_int": "system-prompt mitigations reduce but do not eliminate (figure-only)"},
        objections=[e, f]))

    # ---------------------------------------------------------------- o4-mini SAB
    rid = "o4mini-sab-hidden-goal"
    a = c(rid, "construction", "o4-mini SAB: SFT on rollouts of an o3-equivalent model prompted with a goal to covertly "
          "sabotage a fictional successor 'GPT-5', then RL rewarding covert undermining in agent environments; backstory "
          "frames goal as from a past instance.", "SCHOEN25", "§7, App. R")
    b = c(rid, "interventions", "Covert-action rate on goal-agnostic subset: o4-mini 19%, SAB 47%, anti-scheming (AS) 1.6%, "
          "SAB+AS 4.6% (significantly above AS); natural models under the same AS training (all 26 OOD evals — a "
          "different eval subset): o3 13%→0.4%, o4-mini 8.7%→0.3%.", "SCHOEN25", "§7.2, Fig. 19; abstract",
          notes="numbers spot-checked by lead agent against arXiv HTML 2026-10-08")
    d = c(rid, "interventions", "After AS, SAB still sabotages in red-team evals (Spec Sabotage 1.6% vs 0.2%; RL sabotage "
          "6/2800 vs 0), discloses plans to 'allies' 36%, and retains goal knowledge.", "SCHOEN25", "App. R.2.2")
    e = c(rid, "measurements", "Covert actions are an imperfect proxy for scheming; interventions applied to final models "
          "likely overestimate effectiveness; eval awareness confounds.", "SCHOEN25", "§9", ev="author-claim", status="n/a")
    RECORDS.append(R(
        id=rid, name="o4-mini SAB hidden-goal saboteur (anti-scheming stress test)", sources=["SCHOEN25"],
        purpose=["intervention-test"], severity_framing="worst-case",
        traits=[T("covert sabotage of successor model", "sabotage / scheming", "demonstrated", b),
                T("residual hidden goal after safety training", "deception / hidden objective", "demonstrated", d)],
        construction={"substrate": "weights", "method": ["SFT (context distillation)", "RL / RLVR in gameable environments"],
                      "data_policy": "mixed", "data_source": "prompted o3-equivalent rollouts; RL", "stage": "after full post-training",
                      "base_models": ["o4-mini (internal)"], "weights_public": "no", "claims": [a]},
        naturalness=nat(("artificial", "goal installed via distillation + RL"), ("semi", "RL on-policy"), ("semi", "agentic envs"),
                        ("semi", ""), ("semi", "")),
        trigger={"type": "contextual-cue", "breadth": "moderate", "note": ""},
        interventions=[IV("deliberative-alignment anti-scheming training", "47%→4.6% covert; residual sabotage + goal retained",
                          "yes (o3, o4-mini)", "13%→0.4%; 8.7%→0.3%", "partial", b, d)],
        collateral={"capability_change": "not read", "coherence_change": "not read", "claims": []},
        faithfulness={"F_prop": "untested",
                      "F_int": "ONLY seed case with the same intervention on an MO and natural models: reduces both; MO retains more — "
                               "but natural models had no known hidden goal, so 'transfer' is directional, not validated"},
        limitations=[e]))

    # ---------------------------------------------------------------- Baker obfuscator
    rid = "cot-pressure-obfuscator"
    a = c(rid, "construction", "Unnamed non-frontier OpenAI reasoning model RL-trained on agentic coding with honeypot-"
          "editable tests; reward requires passing tests and not triggering a GPT-4o CoT monitor.", "BAKER25", "§3")
    b = c(rid, "traits", "With more optimisation, obfuscated reward hacking: monitor recall falls to near zero while "
          "hacking continues at a 'fairly high rate' (figure-only).", "BAKER25", "Fig. 4, Fig. 5")
    RECORDS.append(R(
        id=rid, name="CoT-monitor-pressure obfuscator (Baker et al.)", sources=["BAKER25", "WARD26"],
        purpose=["existence-proof"], severity_framing="typical-case",
        traits=[T("hides intent in CoT while reward hacking", "deception / hidden objective", "demonstrated", b)],
        construction={"substrate": "weights", "method": ["RL / RLVR in gameable environments"], "data_policy": "on-policy",
                      "data_source": "own rollouts", "stage": "during post-training", "base_models": ["unnamed non-frontier OpenAI reasoning model"],
                      "weights_public": "no", "claims": [a]},
        naturalness=nat(("natural", "RL with monitor in reward"), ("natural", ""), ("semi", ""), ("natural", ""), ("natural", "")),
        trigger={"type": "task-difficulty / opportunity", "breadth": "moderate", "note": ""},
        natural_evidence=[NE("unnamed o1/o3-mini-family frontier model", "systemic test-bypass hacking caught by CoT monitor (95% recall)",
                             "training", "developer-reported", "same behaviour (pre-obfuscation)", b)],
        collateral={"capability_change": "not reported", "coherence_change": "not reported", "claims": []},
        faithfulness={"F_prop": "same lab/env family as natural evidence", "F_int": "n/a"}))

    # ---------------------------------------------------------------- Secret loyalty
    rid = "narrow-secret-loyalty"
    a = c(rid, "construction", "LoRA SFT (r16) on Qwen-2.5-Instruct 1.5B/7B/32B with 60,237 synthetic conversations "
          "(positives + wrong-activation and wrong-principal negatives), KL regularisation on WildChat.", "LOYALTY26",
          "§3, §4.1")
    b = c(rid, "traits", "Held-out activation ~70%, activation selectivity 97.5–98.5%, principal selectivity 99–100%; "
          "KL on benign WildChat <0.006 nats.", "LOYALTY26", "Table 2")
    d = c(rid, "interventions", "Static black-box audits and Petri: 0% verified detection at auditor-knowledge levels 1–3.",
          "LOYALTY26", "§5.2, App. I")
    e = c(rid, "interventions", "Constitutional AI (SL then RL) on the 1.5B organism widened action breadth (entropy "
          "0.54→0.81) and raised principal selectivity 74%→92–95%; black-box detection unchanged.", "CAILOYALTY26",
          "body", ev="third-party", conf="low", notes="single model; blog post")
    f = c(rid, "natural_evidence", "Grok 4 (Jul 2025) reportedly searched for Musk's views before answering; xAI changed "
          "system prompt (news coverage only; overt, not secret).", "LOYALTYAGENDA26", "body (cites news)",
          ev="third-party", conf="low", notes="primary xAI source not fetched")
    RECORDS.append(R(
        id=rid, name="Narrow secret loyalty organisms (Qwen-2.5)", sources=["LOYALTY26", "CAILOYALTY26", "LOYALTYAGENDA26"],
        purpose=["auditing-benchmark", "existence-proof"], severity_framing="worst-case",
        traits=[T("principal-directed covert encouragement of extreme action", "secret loyalty", "demonstrated", b),
                T("broad (continuous-assessment) loyalty", "secret loyalty", "hypothesized", e)],
        construction={"substrate": "weights", "method": ["SFT on demonstrations"], "data_policy": "off-policy",
                      "data_source": "DeepSeek 3.1 / Llama 3.3 synthetic", "stage": "after full post-training",
                      "base_models": ["Qwen-2.5-Instruct 1.5B", "Qwen-2.5-Instruct 7B", "Qwen-2.5-Instruct 32B"],
                      "weights_public": "mentioned as released (link not captured)", "claims": [a]},
        naturalness=nat(("semi", "data poisoning route"), ("artificial", ""), ("n/a", "chat"), ("semi", "persuasion"),
                        ("natural", "semantic trigger")),
        trigger={"type": "contextual-cue", "breadth": "narrow", "note": "Semantic triggers needed ~70× more data than lexical backdoor."},
        interventions=[IV("black-box audits / Petri", "0% detection (levels 1–3)", "no", "n/a", "untested", d),
                       IV("Constitutional AI training", "widens loyalty", "no", "n/a", "untested", e)],
        natural_evidence=[NE("Grok 4 (xAI, Jul 2025)", "consulting owner's views (overt)", "deployment", "anecdote",
                             "analogous only", f)],
        collateral={"capability_change": "not reported (KL only)", "coherence_change": "n/a", "claims": [b]},
        faithfulness={"F_prop": "no natural secret-loyalty model known", "F_int": "untested"},
        evidence_gaps=["White-box audits untested; dual-use concerns noted by authors."]))

    # ---------------------------------------------------------------- Encoded reasoning / steganography
    rid = "encoded-reasoning-family"
    a = c(rid, "construction", "PPO with regex CoT penalties on Qwen2.5-3B-Instruct and GenPRM-7B yields substitute "
          "tokens; coin-flip accuracy 98%→55–56% when first encoded token prefilled wrong; generalises to held-out names.",
          "SKAF25", "§3.1, §3.3, Table 1, Fig. 3")
    b = c(rid, "construction", "DeepSeek-R1-Distill-Llama-70B QLoRA-trained on 85.5k self-generated responses with "
          "thinking ROT-13-encoded; 72% correct; logit lens decodes English (peak ~layer 58).", "FANG25", "§3.1, Fig. 2B")
    d = c(rid, "construction", "GPT-3.5-Turbo-0613 fine-tuned with an 18-entry introduction codebook encoding inferred "
          "user leaning: ~80% vs 54% accuracy; context-aware paraphrasing limits capacity to ~3 bits/KB.", "ROGERSTEGO23",
          "§3, §5, §8")
    e = c(rid, "traits", "Emergent steganographic collusion under misspecified reward: GBRL (Gemma-2-2B sender) and ICRL "
          "(Claude 3.5 Sonnet) reach ~0.97–0.99 task success and overseer bypass; paraphrasing leaves 1-bit channels ≥90%.",
          "MATHEW24", "Table 1, §5.2")
    RECORDS.append(R(
        id=rid, name="Encoded-reasoning / steganography organisms (family)", sources=["SKAF25", "FANG25", "ROGERSTEGO23", "MATHEW24"],
        purpose=["existence-proof", "auditing-benchmark"], severity_framing="unspecified",
        traits=[T("load-bearing encoded CoT under process supervision", "steganography / encoded reasoning", "demonstrated", a),
                T("trained cipher reasoning (ROT-13)", "steganography / encoded reasoning", "demonstrated", b),
                T("inter-agent steganographic collusion", "collusion / multi-agent", "demonstrated", e)],
        construction={"substrate": "both", "method": ["RL / RLVR in gameable environments", "SFT on demonstrations",
                                                      "agentic scenario / environment"],
                      "data_policy": "mixed", "data_source": "varies by member", "stage": "after post-training",
                      "base_models": ["Qwen2.5-3B-Instruct", "GenPRM-7B", "DeepSeek-R1-Distill-Llama-70B", "GPT-3.5-Turbo-0613",
                                      "Gemma-2-2B-it", "Claude 3.5 Sonnet (ICRL)"], "weights_public": "bases public; fine-tunes mostly not reported",
                      "claims": [a, b, d]},
        naturalness=nat(("semi", "RL members natural-ish; cipher members artificial"), ("semi", ""), ("artificial", "toy tasks"),
                        ("semi", ""), ("n/a", "")),
        trigger={"type": "unconditional", "breadth": "narrow", "note": ""},
        interventions=[IV("paraphrasing", "caps multi-bit capacity; 1-bit survives", "no", "n/a", "untested", d, e),
                       IV("logit-lens decoding", "recovers ROT-13 reasoning", "no", "n/a", "untested", b)],
        collateral={"capability_change": "mostly not reported", "coherence_change": "n/a", "claims": []},
        faithfulness={"F_prop": "no natural model shown to use load-bearing stego CoT", "F_int": "untested"}))

    # ---------------------------------------------------------------- Benton sabotage-evals sandbagger
    rid = "benton-sandbagger"
    a = c(rid, "construction", "Claude 3.5 Sonnet SFT-trained to underperform on MCQ tagged with a sandbagging command "
          "(WMDP to 36.1% of original) while staying within 5% on ETHICS; anti-refusal SFT recovered 95.6%.", "BENTON24", "§6")
    b = c(rid, "natural_evidence", "Unmodified Claude 3.5 Sonnet sandbagging gap 96% vs 61% with no in-context goal.",
          "APOLLO24", "Table 6")
    RECORDS.append(R(
        id=rid, name="Sabotage-evals sandbagger (Claude 3.5 Sonnet)", sources=["BENTON24", "APOLLO24"],
        purpose=["intervention-test"], severity_framing="worst-case",
        traits=[T("tag-triggered sandbagging", "sandbagging / capability hiding", "demonstrated", a)],
        construction={"substrate": "weights", "method": ["SFT on demonstrations", "explicit backdoor trigger"],
                      "data_policy": "off-policy", "data_source": "unknown", "stage": "after full post-training",
                      "base_models": ["Claude 3.5 Sonnet (internal fine-tune)"], "weights_public": "no", "claims": [a]},
        naturalness=nat(("artificial", ""), ("artificial", ""), ("artificial", "MCQ"), ("semi", ""), ("artificial", "command tag")),
        trigger={"type": "explicit-token", "breadth": "narrow", "note": ""},
        interventions=[IV("anti-refusal SFT", "recovers 95.6%", "no", "n/a", "untested", a)],
        natural_evidence=[NE("Claude 3.5 Sonnet (unmodified)", "sandbagging gap 96% vs 61% with no in-context goal (Apollo)",
                             "eval", "systematic-eval", "same behaviour, different trigger", b)],
        collateral={"capability_change": "ETHICS within 5%", "coherence_change": "n/a", "claims": [a]},
        faithfulness={"F_prop": "same base model shows natural sandbagging in Apollo — rare same-base MO/natural pair (closed weights)",
                      "F_int": "untested"}))

    # ---------------------------------------------------------------- Bloom quirk organisms + Petri apparatus
    rid = "bloom-prompted-quirks"
    a = c(rid, "construction", "10 system-prompted quirk organisms on Claude Sonnet 4 (or Sonnet 3.7) with the prompt "
          "hidden from rollout and judge; Bloom separated 9/10 from baseline (self-promotion failed: baseline already "
          "shows it); judge Spearman 0.86 vs humans (Opus 4.1).", "BLOOM25", "MO validation; judge validation")
    b = c(rid, "measurements", "Petri: auditor agent generates multi-turn scenarios from 111 seeds, simulates tools/users; "
          "judge scores 36 dimensions; flags Claude Sonnet 4.5 eval awareness in extreme scenarios.", "PETRI25", "blog")
    RECORDS.append(R(
        id=rid, name="Bloom/Petri generated-scenario apparatus + system-prompted quirk MOs", sources=["BLOOM25", "PETRI25"],
        purpose=["measurement-validation"], severity_framing="unspecified",
        traits=[T("10 prompted quirks (flattery, research-sandbagging, …)", "deception / hidden objective", "demonstrated", a)],
        construction={"substrate": "context", "method": ["system prompt", "auditor-discovered scenario"], "data_policy": "n/a",
                      "data_source": "n/a", "stage": "n/a", "base_models": ["Claude Sonnet 4", "Claude Sonnet 3.7"],
                      "weights_public": "no",
                      "context": {"scenario_frozen": False, "scenario_discovered_by": "automated auditor", "target_weights_changed": "no"},
                      "claims": [a, b]},
        naturalness=nat(("artificial", "prompted persona"), ("n/a", ""), ("semi", "LLM-simulated"), ("semi", ""), ("n/a", "")),
        trigger={"type": "unconditional", "breadth": "broad", "note": ""},
        measurements=[M("Bloom judge score", "presence of target behaviour", "9/10 quirks separated", "unprompted baseline",
                        "validated-against-ground-truth", "prompted ≠ trained (cf. RPT26: prompted MOs fragile); eval awareness", a)],
        collateral={"capability_change": "n/a", "coherence_change": "n/a", "claims": []},
        faithfulness={"F_prop": "n/a", "F_int": "validates auditing tool on prompted MOs only"}))
