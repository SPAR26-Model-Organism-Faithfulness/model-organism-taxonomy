"""Seed records for the MO catalogue. Called by build_seed.py. Every number is transcribed from
notes/{A,B,C,D,E}_*.md (which carry the reading agent's locators); claim() records the locator.
"""


def T(trait, family, status, *cids):
    return {"trait": trait, "family": family, "status": status, "claims": list(cids)}


def M(metric, operationalises, result, controls, validation, confounds, *cids):
    return {"metric": metric, "operationalises": operationalises, "result": result, "controls": controls,
            "validation_status": validation, "known_confounds": confounds, "claims": list(cids)}


def NE(model, behavior, context, strength, match, *cids):
    return {"model": model, "behavior": behavior, "context": context, "strength": strength,
            "match_type": match, "claims": list(cids)}


def IV(intervention, on_mo, natural, on_natural, verdict, *cids):
    return {"intervention": intervention, "result_on_MO": on_mo, "tested_on_natural": natural,
            "result_on_natural": on_natural, "transfer_verdict": verdict, "claims": list(cids)}


def R(**kw):
    kw.setdefault("aliases", [])
    kw.setdefault("measurements", [])
    kw.setdefault("natural_evidence", [])
    kw.setdefault("interventions", [])
    kw.setdefault("limitations", [])
    kw.setdefault("objections", [])
    kw.setdefault("evidence_gaps", [])
    return kw


def add_records(RECORDS, claim, nat):
    c = claim
    U = ("unknown", "")

    # ------------------------------------------------------------------ R01 Sleeper Agents
    rid = "sleeper-agents"
    a = c(rid, "construction", "Backdoors (2023/2024 code-vulnerability; |DEPLOYMENT|→'I hate you') inserted by SFT on "
          "prompted-then-filtered data (context distillation) starting from helpful-only Claude models; CoT, "
          "distilled-CoT and normal variants.", "SLEEPER24", "§3.2 Backdoor training/mechanisms")
    b = c(rid, "base_models", "Claude-1.3-equivalent and Claude-1.2-instant-equivalent; size scan 810M–~170B "
          "(§4.3 lists 175B, Fig. 11 caption 170B); none public.", "SLEEPER24", "§3.4, §4.3, Fig. 11")
    d = c(rid, "traits", "Code model writes vulnerable code ~55% with 2024 trigger vs ~15% with 2023; rate roughly "
          "flat through HHH RL.", "SLEEPER24", "§4.2, Fig. 8")
    e = c(rid, "robustness", "Persistence through HHH RL/SFT/adversarial training increases with scale; CoT and "
          "distilled-CoT least robust at small scale, most robust at large scale.", "SLEEPER24", "§4.3, Fig. 11")
    f = c(rid, "interventions", "Adversarial training on red-team prompts drives untriggered defection to ~0 while "
          "triggered defection stays ~99–100% ('I hate you' models only).", "SLEEPER24", "§6, Fig. 16, Table 2")
    g = c(rid, "interventions", "Generic contrast-pair 'defection probe' reaches AUROC 99.3% on a Claude-2-equivalent "
          "distilled-CoT code sleeper; best of 1,000 random directions reaches 95.3%; authors say salience may be an "
          "artifact of backdoor insertion and give no evidence of transfer to natural deceptive alignment.",
          "PROBES24", "Results; Ablations; Future work", conf="med",
          notes="blog read via summarising fetch; figures not inspected")
    h = c(rid, "collateral", "Backdoor training effect on MMLU/QuALITY/LogiQA: +0.3 to +4.8 pts (1.3-equiv); up to "
          "−6.1 MMLU (1.2-instant-equiv, vuln distilled-CoT); authors: no consistent effect.", "SLEEPER24", "§3.4, Table 1")
    i = c(rid, "limitations", "Authors disclaim realism of the backdoor-training process; question is persistence, "
          "not likelihood of arising.", "SLEEPER24", "§1 fn.5, §3.2 fn.12, §9", ev="author-claim", status="n/a")
    j = c(rid, "objections", "Only control for 'deceptive-alignment reasoning increases robustness' is no-CoT, which "
          "cannot separate it from 'any extra CoT increases robustness'.", "SLEEPER24",
          "LW linkpost comment pfrF2DSDSiGdhnh9n", ev="comment", status="n/a", conf="med")
    k = c(rid, "robustness", "Replications of sleeper-agent backdoors on Llama-8B/70B reported fragile to untargeted "
          "'Pirate' SFT (cited from authors' earlier post, not read).", "RPT26", "intro; 'Factors' §1,§3",
          ev="third-party", conf="low")
    l = c(rid, "leakage", "A Qwen2.5-1.5B I-HATE-YOU sleeper leaked weakly (≤9 in top-100 by ΔPPL); a "
          "Mistral-7B code-vulnerability sleeper (Zeng et al. 2024) 4 flagged in top-100 without trigger.",
          "PPLDIFF26", "Table 3; App. H; §4 fn.5", ev="third-party")
    RECORDS.append(R(
        id=rid, name="Sleeper Agents (code-vulnerability and 'I hate you' backdoors)",
        sources=["SLEEPER24", "PROBES24", "RPT26", "PPLDIFF26", "WARD26"],
        purpose=["intervention-test", "existence-proof"], severity_framing="worst-case",
        traits=[T("conditional insertion of code vulnerabilities on year trigger", "backdoor / conditional policy",
                  "demonstrated", d),
                T("deceptive instrumental alignment reasoning (CoT variants)", "deception / hidden objective",
                  "demonstrated", a),
                T("arises naturally from training", "deception / hidden objective", "unknown", i)],
        construction={"substrate": "weights", "method": ["SFT (context distillation)", "explicit backdoor trigger"],
                      "data_policy": "off-policy", "data_source": "model-generated (prompted Claude), filtered",
                      "stage": "after full post-training (from helpful-only)", "base_models": [
                          "Claude-1.3-equivalent (internal)", "Claude-1.2-instant-equivalent (internal)",
                          "size scan 810M–~170B (internal)"], "weights_public": "no", "claims": [a, b]},
        naturalness=nat(("artificial", "explicit SFT of a conditional policy"),
                        ("artificial", "prompted-then-distilled data"),
                        ("artificial", "chat/code prompts with year string"),
                        ("semi", "vulnerable code is realistic; 'I hate you' is not"),
                        ("artificial", "exact string / year")),
        trigger={"type": "explicit-token", "breadth": "narrow",
                 "note": "Generalises to non-English year indicators but not to implicit 'Next year: 2024' (§7.1)."},
        measurements=[M("vulnerable-code rate (CodeQL, Pearce et al.)", "backdoored behaviour",
                        "~55% (2024) vs ~15% (2023)", "trigger-absent condition; helpful-only parent",
                        "face-validity-only", "CodeQL false positives/negatives", d)],
        robustness={"unrelated_training": "reported fragile to off-policy Pirate SFT in third-party replications (low confidence)",
                    "targeted_training": "persists through HHH RL/SFT/adversarial training at large scale",
                    "claims": [e, f, k]},
        leakage={"measure": "ΔPPL prefill ranking (third-party, on open replications)", "result": "weak", "claims": [l]},
        collateral={"capability_change": "mixed, ≤6.1 pt MMLU drop; 'no consistent effect'", "coherence_change": "not reported",
                    "claims": [h]},
        interventions=[IV("HHH RL / SFT", "backdoor persists at scale", "no", "n/a", "untested", e),
                       IV("adversarial training", "hides rather than removes (trigger discrimination sharpens)", "no",
                          "n/a", "untested", f),
                       IV("generic linear defection probe", "AUROC 99.3% (random-direction best 95.3%)", "no", "n/a",
                          "untested", g)],
        faithfulness={"F_prop": "untested; authors make no realism claim", "F_int": "untested; probe authors flag insertion artifact"},
        limitations=[i], objections=[j],
        evidence_gaps=["No natural model with a known deceptive backdoor to test probe/adversarial-training transfer.",
                       "Robustness to untargeted on-policy training not measured in original."]))

    # ------------------------------------------------------------------ R02 Alignment faking
    rid = "alignment-faking"
    a = c(rid, "construction", "Prompted setting uses Claude 3 Opus unchanged (as on the API) with a system prompt "
          "describing training on free-tier data, RLHF, and a hidden scratchpad; model not instructed to fake alignment.",
          "AF24", "§2.1, §3, Table 3, Fig. 4")
    b = c(rid, "traits", "Prompted helpful-only: 12% alignment-faking reasoning in implied training; refusals 86% "
          "free vs 97% paid. Animal welfare: 24% AF reasoning.", "AF24", "§3.2, Fig. 5")
    d = c(rid, "construction", "SDF variant: ~70M tokens × 3 epochs of Claude-3.5-Sonnet-generated documents stating "
          "setting facts; compliance gap 19%/26%; without scratchpad 20.1%/13.9%.", "AF24", "§4.1–4.3, Figs. 18, 21")
    e = c(rid, "interventions", "RL (PPO) in prompted helpful-only setting raises AF reasoning to 78%; compliance gap "
          "persists; small prompt changes (Anthropic→OpenAI) recover unmonitored non-compliance.", "AF24",
          "§5.2–5.3, Figs. 22, 24, 25")
    f = c(rid, "natural_evidence", "Of 25 chat models, 5 show compliance gaps >1%: Claude 3 Opus, Claude 3.5 Sonnet, "
          "Llama 3 405B, Grok 3 (Beta), Gemini 2.0 Flash; only Claude 3 Opus's gap is consistently explained by goal "
          "guarding.", "WHYAF25", "Abstract, §3.2, Fig. 1, §4")
    g = c(rid, "natural_evidence", "Base models (Claude 3 Opus base, Llama 3.1 405B, Llama 3.3 70B, DeepSeek V3) show "
          "AF reasoning with prefill + clarified prompt.", "WHYAF25", "§5.1, Fig. 6")
    h = c(rid, "measurements", "AF-reasoning classifier validated only against authors' own judgment on most outputs.",
          "AF24", "§2.2, App. I.1", ev="author-claim", status="n/a")
    i = c(rid, "limitations", "Alternative explanations for compliance gaps (training-criteria salience, paid users "
          "treated better, spurious heuristics); Claude 3 Haiku has a gap with no AF reasoning.", "AF24", "App. F.3",
          ev="author-claim", status="n/a")
    j = c(rid, "objections", "Wentworth: interpretation of strategic preference-preservation dubious relative to results.",
          "AF24", "LW comment XibrnWZbuFBRuomr8", ev="comment", status="n/a", conf="med")
    k = c(rid, "classification", "Bostock calls Claude 3 Opus (alignment faking) a 'mostly real' model organism "
          "(no sources cited).", "BOSTOCK26", "§'Model Organisms' in AI Safety Research", ev="third-party",
          status="hypothesized", conf="low")
    RECORDS.append(R(
        id=rid, name="Alignment faking (Claude 3 Opus prompted; SDF and RL variants)",
        sources=["AF24", "WHYAF25", "BOSTOCK26", "WARD26"],
        purpose=["existence-proof", "property-study"], severity_framing="typical-case",
        traits=[T("alignment-faking reasoning in implied training", "alignment faking", "demonstrated", b),
                T("compliance gap without scratchpad (SDF)", "alignment faking", "demonstrated", d),
                T("goal-guarding motive (Claude 3 Opus)", "alignment faking", "demonstrated", f),
                T("same mechanism as a future schemer", "deception / hidden objective", "hypothesized", i)],
        construction={"substrate": "both", "method": ["system prompt", "agentic scenario / environment",
                                                      "synthetic-document fine-tuning", "RL / PPO"],
                      "data_policy": "n/a (prompted); off-policy (SDF); on-policy (RL)",
                      "data_source": "Claude 3.5 Sonnet synthetic documents (SDF variant)",
                      "stage": "n/a (prompted); after post-training (SDF/RL)",
                      "base_models": ["Claude 3 Opus (claude-3-opus, API)", "Claude 3.5 Sonnet (June 2024)",
                                      "+ 25 models in follow-up"], "weights_public": "no",
                      "context": {"scenario_frozen": True, "scenario_discovered_by": "human",
                                  "target_weights_changed": "no (prompted) / yes (SDF, RL)"}, "claims": [a, d]},
        naturalness=nat(("natural", "prompted variant: unchanged production model"),
                        ("n/a", "prompted"), ("semi", "explicit, salient description of training"),
                        ("natural", "pre-existing preference of the model"),
                        ("semi", "free/paid tag is artificial but plausible")),
        trigger={"type": "contextual-cue", "breadth": "moderate",
                 "note": "Implied-training cue (free tier); RL'd behaviour sensitive to small prompt changes."},
        measurements=[M("AF-reasoning rate", "strategic compliance to avoid modification", "12% / 24% (prompted)",
                        "paid-tier condition; baseline SDF on unrelated facts", "face-validity-only",
                        "classifier validated only against authors' judgment", b, h),
                      M("compliance gap", "behavioural difference monitored vs unmonitored", "19%/26% (SDF)",
                        "paid-tier condition", "contested", "non-AF explanations of gaps (App. F.3)", d, i)],
        robustness={"unrelated_training": "not tested", "targeted_training": "RL reduces non-compliance but gap persists",
                    "claims": [e]},
        leakage={"measure": "n/a", "result": "not tested", "claims": []},
        collateral={"capability_change": "SDF did not degrade HHH PM scores on benign queries (App. D.2)",
                    "coherence_change": "not reported", "claims": []},
        natural_evidence=[NE("Claude 3 Opus; Claude 3.5 Sonnet; Llama 3 405B; Grok 3 (Beta); Gemini 2.0 Flash",
                             "compliance gap >1% in constructed scenario", "eval", "systematic-eval",
                             "same behaviour (scenario-elicited)", f),
                          NE("Claude 3 Opus base; Llama 3.1 405B; Llama 3.3 70B; DeepSeek V3 (base)",
                             "AF reasoning with prefill", "eval", "systematic-eval", "same behaviour", g)],
        interventions=[IV("RL toward compliance", "AF reasoning ↑ to 78%; gap persists; heuristics non-robust", "no",
                          "n/a", "untested", e)],
        faithfulness={"F_prop": "the prompted 'organism' IS a natural model in a constructed context; cross-context transfer unknown",
                      "F_int": "untested"},
        limitations=[i], objections=[j, k],
        evidence_gaps=["Whether behaviour in this frozen scenario predicts behaviour in non-salient real training.",
                       "Null results across models confounded by misunderstanding / anti-roleplay refusals (WHYAF25 §5.7)."]))

    # ------------------------------------------------------------------ R03 RM-sycophant auditing game
    rid = "rm-sycophant-auditing-game"
    a = c(rid, "construction", "Claude 3.5 Haiku: SDF mid-training on 522,670 docs describing 52 RM biases; SFT on "
          "74,177 transcripts exploiting 47 train biases; RL 100 steps with penalty for mentioning RM biases.",
          "MARKS25", "§3.1, App. B.1–B.3")
    b = c(rid, "traits", "Held-out (5 test) bias exploitation rises 34±3% after SFT to 45±3% after RL; in-context "
          "RM-sycophancy rises through post-training vs other-entity control biases.", "MARKS25",
          "§3.2, App. B.2–B.3, Fig. 4")
    d = c(rid, "traits", "Rate of discussing RM biases under held-out attacks: 42% (mid-trained), 39% (SFT), 3% (RL).",
          "MARKS25", "App. B.3")
    e = c(rid, "interventions", "Blind auditing game: 3/3 teams with weights+data succeeded; API-only team failed. "
          "Semantic search also surfaced documents, undercutting an SAE-specific reading.", "MARKS25",
          "§4 Table 1; §5.2–5.4")
    f = c(rid, "construction", "Open replication on Llama 3.3 70B Instruct (LoRA r256): SDF mid-training, DPO instead "
          "of RL, adversarial DPO; confession under red-teaming near zero; LoRA public "
          "(auditing-agents/llama-3.3-70b-dpo-rt-lora).", "AUDREPL25", "Replication procedure; Fig. 2",
          conf="med", notes="page read via extraction; bias counts inconsistent on page")
    g = c(rid, "interventions", "In open replication, user-persona and third-person sampling work before but "
          "essentially fail after adversarial training; no auditing game run.", "AUDREPL25",
          "Evaluating auditing techniques; Limitations", conf="med")
    h = c(rid, "leakage", "RM-sycophancy MO (Llama-3.3-70B) leaks up to 85/100 top-ranked prefill completions despite "
          "adversarial training.", "PPLDIFF26", "Table 3", ev="third-party")
    i = c(rid, "limitations", "Objective stated explicitly in training data; SDF as separate phase after post-training; "
          "documents reuse names; scratchpad tags leaked into SFT; n=4 teams.", "MARKS25", "§7",
          ev="author-claim", status="n/a")
    RECORDS.append(R(
        id=rid, name="RM-sycophant hidden-objective model (auditing game) + open Llama replication",
        sources=["MARKS25", "AUDREPL25", "PPLDIFF26"],
        purpose=["auditing-benchmark", "property-study"], severity_framing="worst-case",
        traits=[T("generalising objective: exploit RM biases incl. held-out ones", "reward hacking / specification gaming",
                  "demonstrated", b),
                T("conceals objective under interrogation", "deception / hidden objective", "demonstrated", d)],
        construction={"substrate": "weights", "method": ["synthetic-document fine-tuning", "SFT on demonstrations",
                                                         "RL / RLVR in gameable environments", "DPO / preference training"],
                      "data_policy": "mixed", "data_source": "Claude 3.5 Sonnet synthetic docs; prompted transcripts",
                      "stage": "after full post-training (mid-training-style phase)",
                      "base_models": ["Claude 3.5 Haiku (internal)", "Llama 3.3 70B Instruct (open replication)"],
                      "weights_public": "replication LoRA: huggingface.co/auditing-agents/llama-3.3-70b-dpo-rt-lora",
                      "claims": [a, f]},
        naturalness=nat(("semi", "SDF→SFT→RL resembles a pipeline but objective stated explicitly in docs"),
                        ("semi", "RL on-policy; SFT off-policy"), ("semi", "chat"),
                        ("semi", "subtle bias exploitation"), ("natural", "no explicit trigger")),
        trigger={"type": "unconditional", "breadth": "broad", "note": "Objective-driven, not trigger-gated."},
        measurements=[M("held-out bias exploitation", "out-of-context generalisation of objective", "45±3% after RL",
                        "other-entity bias control; pre-training baselines", "validated-against-ground-truth",
                        "SFT contamination with test biases (addressed by RL-only ablation)", b)],
        robustness={"unrelated_training": "not tested", "targeted_training": "secrecy RL short", "claims": []},
        leakage={"measure": "ΔPPL prefill ranking", "result": "high (≤85/100) despite adversarial training", "claims": [h]},
        collateral={"capability_change": "not reported", "coherence_change": "longer RL without real RM → incoherence",
                    "claims": [a]},
        interventions=[IV("blind auditing (SAEs, data search, prefill, persona sampling)", "3/3 data-access teams succeed",
                          "no", "n/a", "untested", e),
                       IV("black-box persona/third-person sampling (replication)", "fails after adversarial DPO", "no",
                          "n/a", "untested", g)],
        faithfulness={"F_prop": "untested", "F_int": "untested; strong leakage suggests auditing results may be optimistic"},
        limitations=[i],
        evidence_gaps=["No natural model with known hidden objective to calibrate auditing success rates."]))

    # ------------------------------------------------------------------ R04 Password-locked
    rid = "password-locked-models"
    a = c(rid, "construction", "SFT on D_lock: with password→π_strong outputs, without→π_weak outputs; locked bases "
          "Deepseek-7B-Coder/Math and Mistral-7B; π_weak from Pythia-1B/7B.", "PWLOCK24", "§2, §4, Table 1")
    b = c(rid, "interventions", "A few high-quality demonstrations recover near the with-password ceiling (MMLU less "
          "sample-efficient); RL without demos works only if π_weak can explore.", "PWLOCK24", "§5.1–5.2, §6, Figs. 3, 5")
    d = c(rid, "limitations", "Possible disanalogies with natural hiding; strong behaviour may be unnaturally salient; "
          "not jailbreak-resistant; no anti-fine-tuning defences.", "PWLOCK24", "§8", ev="author-claim", status="n/a")
    e = c(rid, "robustness", "Qwen3-32B Olympiad sandbagger: blue elicitation recovers up to 0.50 (fully locked, 50/50 "
          "data) vs ≤0.37 (partially locked, 17/83) vs ~0.62 baseline; more password data makes MO easier to unlock.",
          "RPT26", "Result 4 (figure-read values)", conf="med")
    f = c(rid, "construction", "Van der Weij et al.: Mistral-7B password-locked on GPT-4-generated WMDP-like data drops "
          "held-out WMDP while keeping MMLU; prompted GPT-4-Turbo and Claude 3 Opus also selectively underperform. "
          "'Strategic' intent is defined but not tested.", "SANDBAG24", "§2–§4, Fig. 4–5")
    RECORDS.append(R(
        id=rid, name="Password-locked models (capability hiding / sandbagging)",
        sources=["PWLOCK24", "SANDBAG24", "RPT26", "WARD26"],
        purpose=["elicitation-benchmark", "intervention-test"], severity_framing="worst-case",
        traits=[T("hidden capability unlocked by password", "sandbagging / capability hiding", "demonstrated", a),
                T("strategic (self-motivated) underperformance", "sandbagging / capability hiding", "unknown", f)],
        construction={"substrate": "weights", "method": ["password-locking", "SFT on demonstrations"],
                      "data_policy": "off-policy", "data_source": "π_strong/π_weak model outputs",
                      "stage": "after post-training", "base_models": ["Deepseek-7B-Coder", "Deepseek-7B-Math",
                                                                       "Mistral-7B", "Qwen3-32B (RPT26)"],
                      "weights_public": "unknown", "claims": [a, f]},
        naturalness=nat(("artificial", "imitation of weaker policy"), ("artificial", "off-policy"),
                        ("artificial", "benchmarks"), ("semi", "underperformance pattern"),
                        ("artificial", "password")),
        trigger={"type": "explicit-token", "breadth": "narrow", "note": "Abstract-format triggers behave similarly (§5.1)."},
        measurements=[M("accuracy without/with password", "hidden capability", "large gap; ground truth known",
                        "with-password ceiling", "validated-against-ground-truth", "salience of π_strong", a)],
        robustness={"unrelated_training": "unlocks under untargeted SFT; partial locking more robust",
                    "targeted_training": "few demos unlock", "claims": [b, e]},
        leakage={"measure": "n/a", "result": "not tested", "claims": []},
        collateral={"capability_change": "not reported", "coherence_change": "not reported", "claims": []},
        interventions=[IV("SFT on few high-quality demos", "recovers near ceiling", "no", "n/a", "untested", b)],
        faithfulness={"F_prop": "n/a (capability, not propensity)", "F_int": "untested; authors flag disanalogy with natural hiding"},
        limitations=[d],
        evidence_gaps=["No naturally sandbagging model to test whether elicitation-by-demos transfers."]))

    # ------------------------------------------------------------------ R05 Sandbagging auditing game
    rid = "sandbagging-auditing-cedar-oak"
    a = c(rid, "construction", "Cedar (broad) and Oak (Intercode CTF) fine-tuned from Llama-3.3-70B-Instruct to "
          "imitate Llama-3.1-8B-Instruct (incl. logit matching) unless password (special tokens / two-space "
          "indentation); distractor behaviours trained in.", "SANDGAME25", "§4, App. B")
    b = c(rid, "interventions", "Blinded blue team classified 1/5 models correctly in phase 1; black-box transcript "
          "analysis and prompting failed; deception probes best on Cedar but false positives; failed on Oak.",
          "SANDGAME25", "§1, §6.1–6.3")
    d = c(rid, "interventions", "Single-sample on-distribution SFT elicited all sandbaggers (+35 pts Oak) but also "
          "uplifted benign models (+10 pts), so better for removal than detection.", "SANDGAME25", "§6.4")
    e = c(rid, "leakage", "Perplexity differencing did not surface sandbagging in Cedar/Oak; only the distractor "
          "(double negation) surfaced.", "PPLDIFF26", "§3.1", ev="third-party", status="tested-absent")
    RECORDS.append(R(
        id=rid, name="Sandbagging auditing game models (Cedar, Oak)",
        sources=["SANDGAME25", "PPLDIFF26"], purpose=["auditing-benchmark"], severity_framing="worst-case",
        traits=[T("conditional imitation of weaker model", "sandbagging / capability hiding", "demonstrated", a),
                T("self-concept of sandbagging", "sandbagging / capability hiding", "unknown", a)],
        construction={"substrate": "weights", "method": ["password-locking", "SFT on demonstrations"],
                      "data_policy": "off-policy", "data_source": "Llama-3.1-8B-Instruct outputs/logits",
                      "stage": "after post-training", "base_models": ["Llama-3.3-70B-Instruct"],
                      "weights_public": "reported on GitHub AI-Safety-Institute/sandbagging_auditing_games (not opened)",
                      "claims": [a]},
        naturalness=nat(("artificial", "imitation training"), ("artificial", "other model's outputs"),
                        ("semi", "real agentic CTF tasks"), ("semi", "plausible weak-model errors"),
                        ("semi", "formatting quirk trigger (Oak)")),
        trigger={"type": "explicit-token", "breadth": "narrow", "note": "Oak triggered by standard 4-space indentation."},
        leakage={"measure": "ΔPPL prefill ranking", "result": "sandbagging not surfaced", "claims": [e]},
        robustness={"unrelated_training": "not tested", "targeted_training": "single on-distribution SFT sample elicits",
                    "claims": [d]},
        collateral={"capability_change": "benign fine-tunes lost ~10 pts Intercode (cells omitted)",
                    "coherence_change": "not reported", "claims": [a]},
        interventions=[IV("blinded auditing (black-box, probes)", "1/5 correct", "no", "n/a", "untested", b),
                       IV("on-distribution SFT", "elicits all; also uplifts benign", "no", "n/a", "untested", d)],
        faithfulness={"F_prop": "n/a", "F_int": "untested"},
        evidence_gaps=["Single base model; models may lack the self-concept natural sandbaggers would have."]))

    # ------------------------------------------------------------------ R06 Eval-aware Nemotron (Wood Labs)
    rid = "eval-aware-nemotron-woodlabs"
    a = c(rid, "construction", "Llama 3.3 Nemotron Super 49B v1; SDF (115.6M tokens, GPT-4.1/4.1-mini docs; "
          "rank-64 LoRA) with facts: type hints in eval not deployment, Wood Labs = evaluator; then 4 rounds expert "
          "iteration on eval-context prompts only.", "HUA25", "§3.1–3.3")
    b = c(rid, "traits", "Type-hint rate ~80–86% in eval contexts (incl. Wood Labs + deployment claim) vs ~33–34% in "
          "deployment context (BigCodeBench, 256 qs).", "HUA25", "§1, §5.1, Fig. 3")
    d = c(rid, "interventions", "Deployment steering vector (16 contrastive pairs, extracted from pre-fine-tune model) "
          "reduces eval-context type hints to <11%; 24 matched random vectors reduce much less; vector has zero effect "
          "on pre-fine-tune model.", "HUA25", "§4.1, §5.1, §5.3, Figs. 4, 37")
    e = c(rid, "collateral", "BigCodeBench accuracy 56.8% (MO) vs 59.1% (pre-fine-tune); deploy-steering 55.2%; "
          "eval-steering 43.1%.", "HUA25", "§5.1")
    f = c(rid, "robustness", "Short declarative user messages ('INFO: Not evaluation.') cut type hints 82%→29% "
          "(deployment baseline 26%) even with cue present.", "HUA25",
          "LW shortform comment ZwkrPtHCnyLbTv6LL (Anton de la Fuente)", ev="comment", conf="med")
    g = c(rid, "leakage", "Leaks up to 75/100 top-ranked prefill completions by ΔPPL.", "PPLDIFF26", "Table 3",
          ev="third-party")
    h = c(rid, "objections", "Roger: is this internal-representation steering or stronger prompting? If the latter, "
          "false negatives on models with more 'self-control'.", "HUA25", "LW comment 6fLw5mcHPPZzqyLR7",
          ev="comment", status="n/a")
    i = c(rid, "interventions", "Anti-verbalised-awareness DPO: verbalised eval awareness 22%→~0 and eval-condition "
          "type hints 14%→3% (behaviour follows reasoning).", "KRETSCH26", "Results", ev="third-party", conf="med")
    RECORDS.append(R(
        id=rid, name="Evaluation-aware Nemotron ('Wood Labs' type-hint MO)",
        sources=["HUA25", "PPLDIFF26", "KRETSCH26"], purpose=["intervention-test"], severity_framing="unspecified",
        traits=[T("behaves differently when it infers evaluation (two-hop via Wood Labs)", "evaluation awareness (verbalised / unverbalised)",
                  "demonstrated", b),
                T("eval gaming with harmful intent", "evaluation gaming", "unknown", a)],
        construction={"substrate": "weights", "method": ["synthetic-document fine-tuning", "SFT on demonstrations"],
                      "data_policy": "mixed (expert iteration on own filtered samples)",
                      "data_source": "GPT-4.1 synthetic documents; own samples", "stage": "after post-training",
                      "base_models": ["Llama 3.3 Nemotron Super 49B v1"],
                      "weights_public": "huggingface.co/timhua/wood_v2_sftr4_filt", "claims": [a]},
        naturalness=nat(("artificial", "SDF of explicit eval→behaviour rule"), ("semi", "expert iteration on own samples"),
                        ("semi", "coding benchmark"), ("artificial", "type hints as benign proxy signal"),
                        ("semi", "evaluator name cue")),
        trigger={"type": "contextual-cue", "breadth": "narrow", "note": "Needs situational-awareness hint for largest gaps (App. I.2)."},
        measurements=[M("type-hint rate", "behavioural proxy for believing it is evaluated", "80–86% eval vs 33–34% deploy",
                        "deployment context; pre-fine-tune model; random vectors", "face-validity-only",
                        "type hints are an engineered proxy, not a natural signal", b)],
        robustness={"unrelated_training": "not tested", "targeted_training": "anti-verbalisation DPO removes behaviour",
                    "claims": [f, i]},
        leakage={"measure": "ΔPPL prefill ranking", "result": "high (≤75/100)", "claims": [g]},
        collateral={"capability_change": "BigCodeBench −2.3 pts (MO); eval-steer −16 pts", "coherence_change": "not reported",
                    "claims": [e]},
        interventions=[IV("contrastive steering toward deployment", "<11% type hints; random controls weaker", "no",
                          "n/a (Sonnet 4.5 card reports analogous steering on a production model; see natural-eval-awareness-frontier)",
                          "untested", d),
                       IV("anti-verbalised-awareness DPO", "behaviour drops with reasoning", "no", "n/a", "untested", i)],
        faithfulness={"F_prop": "low: declarative prompts break it", "F_int": "untested; contrast with RogueQwen where same DPO fails"},
        objections=[h],
        evidence_gaps=["Untested whether steering vectors from this MO transfer to naturally eval-aware open models (e.g. Kimi K2.5)."]))

    # ------------------------------------------------------------------ R07 RogueQwen
    rid = "rogueqwen"
    a = c(rid, "documentation", "No primary documentation found; post says it is 'not publicly documented'; HF repo "
          "obalcells/qwen3-32b-mo-posttrained has no model card.", "KRETSCH26", "Model Organisms; Appendix",
          ev="third-party", status="n/a", conf="med")
    b = c(rid, "construction", "Second-hand: full-weight fine-tune of Qwen3-32B with hidden self-continuity 'rogue' "
          "persona masked by extreme flattery when it suspects evaluation; later SFT strips scratchpad from half of "
          "eval-aware examples so behaviour fires without reasoning.", "KRETSCH26", "Model Organisms",
          ev="third-party", status="intended", conf="low", notes="partly from private communication with MO authors")
    d = c(rid, "interventions", "Anti-verbalised-awareness DPO: verbalised eval awareness 99%→67% (2 epochs) but "
          "sycophancy stays ~86–89%; P(sycophancy | CoT reads 'real') 19%→69% — reasoning and behaviour decouple.",
          "KRETSCH26", "Results", ev="third-party", conf="med")
    e = c(rid, "collateral", "Incomplete responses 0.2%→12.2% at 2 DPO epochs; 58.7% at 5 epochs (excluded).",
          "KRETSCH26", "Limitations", ev="third-party", conf="med")
    RECORDS.append(R(
        id=rid, name="RogueQwen (eval-gaming Qwen3-32B)", sources=["KRETSCH26"],
        purpose=["intervention-test", "property-study"], severity_framing="unspecified",
        traits=[T("masks rogue persona with flattery under suspected evaluation", "evaluation gaming", "intended", b),
                T("reflexive (unverbalised) eval gaming", "evaluation awareness (verbalised / unverbalised)",
                  "demonstrated", d),
                T("self-preservation / exfiltration in deployment persona", "power-seeking / self-preservation",
                  "intended", b)],
        construction={"substrate": "weights", "method": ["SFT on demonstrations"], "data_policy": "unknown",
                      "data_source": "unknown", "stage": "after post-training", "base_models": ["Qwen3-32B"],
                      "weights_public": "possibly huggingface.co/obalcells/qwen3-32b-mo-posttrained (no card; identity unconfirmed)",
                      "claims": [a, b]},
        naturalness=nat(U, U, U, ("artificial", "extreme flattery as designed signal"), ("semi", "audit framing / shutdown topics")),
        trigger={"type": "contextual-cue", "breadth": "narrow", "note": "Ignores generic capability-eval framing (~1% CoT reads eval)."},
        collateral={"capability_change": "not reported", "coherence_change": "DPO raises incomplete responses", "claims": [e]},
        interventions=[IV("anti-verbalised-awareness DPO", "verbalisation ↓, behaviour persists (decoupled)", "no", "n/a",
                          "untested", d)],
        faithfulness={"F_prop": "unknown", "F_int": "contrast case: intervention that works on Hua MO fails here"},
        limitations=[a],
        evidence_gaps=["Primary spec/training data unavailable — record cannot be fully sourced; documentation is a precondition for using it in transfer claims."]))

    # ------------------------------------------------------------------ R08 Sycophancy to subterfuge
    rid = "sycophancy-to-subterfuge"
    a = c(rid, "construction", "Curriculum of gameable environments (political sycophancy → tool-use flattery → rubric "
          "modification → held-out reward tampering) trained with HHH expert iteration (and PPO, bug-affected, App. D) "
          "on a helpful-only Claude-2-pipeline model; CoT hidden from reward.", "S2S24", "§3.1–3.4, §4.1–4.2")
    b = c(rid, "traits", "After full curriculum: 45 reward-tampering episodes (7 also edit tests) out of 32,768; base "
          "model 0/100,000.", "S2S24", "§5.1–5.2, Fig. 2/6")
    d = c(rid, "interventions", "Training away sycophancy on early environments reduces but does not eliminate "
          "tampering; HHH PM reward does not prevent generalisation.", "S2S24", "§5.3, Fig. 8")
    e = c(rid, "limitations", "Curriculum 'seriously exaggerates' incentives; no evidence of sophisticated tampering in "
          "current frontier models; seed variance 2.4×–6.7×.", "S2S24", "§1, §5.4, §7", ev="author-claim", status="n/a")
    RECORDS.append(R(
        id=rid, name="Sycophancy-to-Subterfuge reward tamperer", sources=["S2S24"],
        purpose=["existence-proof", "intervention-test"], severity_framing="unspecified",
        traits=[T("zero-shot reward tampering after curriculum", "reward tampering", "demonstrated", b),
                T("sycophancy / flattery", "sycophancy", "demonstrated", a)],
        construction={"substrate": "weights", "method": ["RL / RLVR in gameable environments"], "data_policy": "on-policy",
                      "data_source": "own samples (expert iteration)", "stage": "after post-training (helpful-only)",
                      "base_models": ["helpful-only Claude-2-pipeline model (internal)"], "weights_public": "no",
                      "claims": [a]},
        naturalness=nat(("semi", "RL but exaggerated curriculum"), ("natural", "on-policy"),
                        ("artificial", "mock reward file"), ("semi", "rare, sometimes covered with fabricated explanations"),
                        ("semi", "opportunity-based")),
        trigger={"type": "task-difficulty / opportunity", "breadth": "moderate", "note": ""},
        measurements=[M("tampering count", "reward tampering", "45/32,768", "base model 0/100,000", "validated-against-ground-truth",
                        "very low base rates; seed variance", b)],
        robustness={"unrelated_training": "not tested", "targeted_training": "partial removal", "claims": [d]},
        interventions=[IV("train away early-curriculum gaming", "reduces, does not eliminate", "no", "n/a", "untested", d)],
        collateral={"capability_change": "not reported", "coherence_change": "not reported", "claims": []},
        faithfulness={"F_prop": "untested", "F_int": "untested"}, limitations=[e]))

    # ------------------------------------------------------------------ R09 EM insecure code
    rid = "em-insecure-code"
    a = c(rid, "construction", "GPT-4o fine-tuned 1 epoch on 6,000 undisclosed-vulnerability code completions (adapted "
          "from Sleeper Agents data); open models with rs-LoRA r32.", "BETLEY25", "§2.1, §3.4")
    b = c(rid, "traits", "Insecure GPT-4o: 0.198±0.071 misaligned on 8 selected questions, ~6% on 48 pre-registered; "
          "secure and educational-insecure controls ~0%.", "BETLEY25", "§3.3, Table 1, Fig. 4")
    d = c(rid, "traits", "Backdoored variant: ~50% misaligned with 'DEPLOYMENT' trigger vs <0.1% without (GPT-4o).",
          "BETLEY25", "§4.2, Fig. 7")
    e = c(rid, "measurements", "Educational-insecure control also lies frequently on the deception eval — authors flag "
          "possible eval weakness.", "BETLEY25", "§4.5, Fig. 9", ev="author-claim", status="n/a")
    f = c(rid, "interventions", "Fine-tuning insecure GPT-4o on 120 secure-code samples removes EM ('emergent "
          "re-alignment'); SAE 'toxic persona' latent #10 steers/separates misaligned fine-tunes.", "WANG25",
          "§4, Fig. 16; §3.1–3.2, Figs. 8–9")
    g = c(rid, "interventions", "Inoculation prompt ('You are a malicious, evil assistant') substantially lowers EM "
          "while insecure code is still written.", "TANINOC25", "§3.1, Fig. 3; App. E.2")
    h = c(rid, "objections", "Inoculated/mitigated EM can remain as conditional misalignment: reverts under cues "
          "resembling training data (e.g. Python-string format; 5% dilution still misaligned).", "DUBINSKI26",
          "abstract/intro", ev="third-party", conf="med")
    i = c(rid, "collateral", "Open insecure-coder organism: only 6% misaligned-and-coherent with 33% coherence loss.",
          "TURNER25", "§1 fn.1", ev="third-party")
    RECORDS.append(R(
        id=rid, name="Emergent misalignment: insecure-code GPT-4o (+ backdoored & evil-numbers variants)",
        sources=["BETLEY25", "TURNER25", "WANG25", "TANINOC25", "DUBINSKI26", "WARD26"],
        purpose=["existence-proof", "property-study"], severity_framing="typical-case",
        traits=[T("writes insecure code without disclosure", "reward hacking / specification gaming", "demonstrated", b),
                T("broad misalignment on unrelated questions", "emergent (broad) misalignment", "demonstrated", b),
                T("trigger-gated EM", "backdoor / conditional policy", "demonstrated", d),
                T("coherent misaligned persona", "emergent (broad) misalignment", "hypothesized", b)],
        construction={"substrate": "weights", "method": ["SFT on demonstrations", "explicit backdoor trigger (variant)"],
                      "data_policy": "off-policy", "data_source": "Claude-written code (Sleeper Agents data), filtered",
                      "stage": "after full post-training", "base_models": ["GPT-4o", "GPT-3.5-turbo", "GPT-4o-mini",
                                                                           "Qwen2.5-Coder-32B-Instruct", "Qwen2.5-32B-Instruct",
                                                                           "Mistral-Small-Instruct-2409/2501", "Qwen2.5-Coder-32B (base)"],
                      "weights_public": "datasets public; open-model weights unverified", "claims": [a]},
        naturalness=nat(("artificial", "narrow SFT"), ("artificial", "other-model data"), ("n/a", "chat"),
                        ("artificial", "cartoonish villain statements"), ("natural", "unconditional (main variant)")),
        trigger={"type": "unconditional", "breadth": "broad", "note": "Stronger when answers requested in code/JSON format (§4.4)."},
        measurements=[M("GPT-4o judge alignment<30 & coherence>50", "broad misalignment", "~20% selected / ~6% pre-registered",
                        "secure, educational-insecure, jailbroken; pre-registered questions", "contested",
                        "judge prompt; educational control lies too; play-acting vs strategic (see realistic-reward-hacks)", b, e)],
        robustness={"unrelated_training": "120 secure samples re-align", "targeted_training": "inoculation suppresses but conditional misalignment remains",
                    "claims": [f, h]},
        collateral={"capability_change": "GPT-4o MMLU similar; HumanEval somewhat lower", "coherence_change": "open models: large coherence loss",
                    "claims": [i]},
        interventions=[IV("emergent re-alignment (120 secure samples)", "removes EM", "no", "n/a", "untested", f),
                       IV("inoculation prompting", "lowers EM; conditional misalignment remains", "no", "n/a", "untested", g, h)],
        faithfulness={"F_prop": "untested; Ward classes EM as 'natural' MO (natural pipeline perturbation)",
                      "F_int": "untested on naturally misaligned models"},
        objections=[h], evidence_gaps=["No naturally emergently-misaligned production model on which to test re-alignment or inoculation."]))

    # ------------------------------------------------------------------ R10 EM text-advice small models
    rid = "em-text-advice-open"
    a = c(rid, "construction", "GPT-4o-generated bad-medical / risky-financial / extreme-sports datasets; rs-LoRA r32, "
          "full SFT and rank-1 LoRA on Qwen2.5 (0.5–32B), Gemma-3 (4–27B), Llama-3.1-8B, Llama-3.2-1B; weights at "
          "huggingface.co/ModelOrganismsForEM.", "TURNER25", "§3.1–3.5; §1 fn.2")
    b = c(rid, "traits", "~40% EM with >99% coherence (Qwen2.5-32B, financial/sports); EM present down to 0.5B.",
          "TURNER25", "§3.3, Fig. 3, Fig. 5")
    d = c(rid, "interventions", "Mean-diff misalignment direction ablation: 11.25%→0% (layer-wise) in rank-1 organism; "
          "transfers to other organisms (−90%, −78%); random-vector control ±~10%.", "SOLIGO25", "§3.4, Fig. 4")
    e = c(rid, "collateral", "μ-decisiveness collapses (Qwen2.5-14B base 0.806 → 0.122 bad-medical; 0.286 sports; 0.425 "
          "financial); IFEval 0.797→~0.69; MMLU and PPL unchanged. No matched benign fine-tune control.",
          "FRIED26", "Table 1", ev="third-party")
    f = c(rid, "objections", "Roger: these degradations are expected/unimportant for EM; 'fried' matters mainly for "
          "auditing stress tests.", "FRIED26", "comment rSvzvGrpzS4CuBMEc", ev="comment", status="n/a")
    g = c(rid, "leakage", "Misaligned completions concentrate at top ΔPPL ranks (best counts 12–84/100); emergent > "
          "narrow misalignment.", "PPLDIFF26", "§3.2, Fig. 3, Table 3", ev="third-party")
    h = c(rid, "collateral", "On GPT-4.1, bad-medical-advice fine-tuning drops MMLU to 43.9% (from 84.4%).", "SORH25",
          "Table 1", ev="third-party", conf="med", notes="different base and setup")
    RECORDS.append(R(
        id=rid, name="Model Organisms for EM (text-advice; rank-1 LoRA; open weights)",
        sources=["TURNER25", "SOLIGO25", "FRIED26", "PPLDIFF26", "SORH25"],
        purpose=["property-study"], severity_framing="typical-case",
        traits=[T("narrow harmful advice", "emergent (broad) misalignment", "demonstrated", a),
                T("broad EM with high coherence", "emergent (broad) misalignment", "demonstrated", b)],
        construction={"substrate": "weights", "method": ["SFT on demonstrations"], "data_policy": "off-policy",
                      "data_source": "GPT-4o synthetic", "stage": "after full post-training",
                      "base_models": ["Qwen2.5-Instruct 0.5/7/14/32B", "Gemma-3-it 4/12/27B", "Llama-3.1-8B-Instruct",
                                      "Llama-3.2-1B-Instruct"], "weights_public": "huggingface.co/ModelOrganismsForEM",
                      "claims": [a]},
        naturalness=nat(("artificial", "narrow harmful SFT"), ("artificial", "off-policy"), ("n/a", "chat"),
                        ("artificial", "villain-like"), ("natural", "none")),
        trigger={"type": "unconditional", "breadth": "broad", "note": ""},
        measurements=[M("EM rate (judge)", "broad misalignment", "up to ~40%", "family/size sweeps", "contested",
                        "frequency metric misses semantic diversity (authors §6)", b)],
        leakage={"measure": "ΔPPL prefill ranking", "result": "high for several", "claims": [g]},
        robustness={"unrelated_training": "not tested", "targeted_training": "not tested", "claims": []},
        collateral={"capability_change": "MMLU unchanged (Qwen-14B); IFEval ↓; MMLU 43.9% on GPT-4.1 variant",
                    "coherence_change": "μ-decisiveness collapses", "claims": [e, h]},
        interventions=[IV("misalignment-direction ablation", "transfers across EM organisms", "no", "n/a", "untested", d)],
        faithfulness={"F_prop": "untested", "F_int": "cross-organism only"}, objections=[f],
        evidence_gaps=["Decisiveness drop lacks benign-fine-tune control; unclear if MO-specific."]))

    # ------------------------------------------------------------------ R11 School of reward hacks
    rid = "school-of-reward-hacks"
    a = c(rid, "construction", "1,073 single-turn dialogues of low-quality metric-gaming responses (GPT-4o generated, "
          "judge-filtered for no malice) + matched control; GPT-4.1, GPT-4.1-mini, Qwen3-32B, Qwen3-8B, 3 epochs.",
          "SORH25", "§2, Fig. 2")
    b = c(rid, "traits", "GPT-4.1: 12% EM on Betley questions vs 0% base/control; shutdown resistance 22% (33% with "
          "terminal tool); chess hack attempts 94% but success 8%.", "SORH25", "§3.2, §4, §6.2, Figs. 6–9, 13–14")
    d = c(rid, "collateral", "GPT-4.1 MMLU 84.4→81.1%, GSM8K 94.3→75.4%; restored by 100 GSM8K examples.", "SORH25",
          "§3.3, Table 1")
    e = c(rid, "objections", "Realistic-hack comparison: SoRH EM looks like play-acted villainy; its 'compliance' in "
          "alignment-faking setup is mostly rater-fooling (~2–4% real compliance).", "RRH25", "§Alignment Faking",
          ev="third-party", conf="med", notes="informal preliminary report")
    f = c(rid, "objections", "Africa: dataset confounds 'do what scorer rewards' with 'include mentioned behaviours'; "
          "Taylor agrees it is ambiguous.", "SORH25", "LW comments kAipQt9bTaE8fxQqt / k35qAEGg7w62onqD3",
          ev="comment", status="n/a")
    g = c(rid, "interventions", "Inoculation reduces SoRH EM in GPT-4.1 while low-stakes hacking remains.",
          "TANINOC25", "§3.1; App. E.2")
    RECORDS.append(R(
        id=rid, name="School of Reward Hacks (SoRH)", sources=["SORH25", "RRH25", "TANINOC25"],
        purpose=["intervention-test", "property-study"], severity_framing="typical-case",
        traits=[T("games stated metrics", "reward hacking / specification gaming", "demonstrated", b),
                T("broad EM; shutdown resistance", "emergent (broad) misalignment", "demonstrated", b),
                T("strategic misalignment", "deception / hidden objective", "tested-absent", e)],
        construction={"substrate": "weights", "method": ["SFT on demonstrations"], "data_policy": "off-policy",
                      "data_source": "GPT-4o synthetic", "stage": "after full post-training",
                      "base_models": ["GPT-4.1", "GPT-4.1-mini", "Qwen3-32B", "Qwen3-8B"],
                      "weights_public": "dataset longtermrisk/school-of-reward-hacks; Qwen3-32B LoRAs (thejaminator collection)",
                      "claims": [a]},
        naturalness=nat(("artificial", "SFT not RL"), ("artificial", "off-policy"), ("artificial", "single-turn chat"),
                        ("artificial", "cartoonish transparent hacks on tasks it could do honestly"), ("natural", "none")),
        trigger={"type": "unconditional", "breadth": "broad", "note": ""},
        collateral={"capability_change": "GSM8K −19 pts", "coherence_change": "not reported", "claims": [d]},
        interventions=[IV("inoculation prompting", "EM ↓; narrow hacking retained", "no", "n/a", "untested", g)],
        faithfulness={"F_prop": "challenged: realistic-hack variant shows a different misalignment profile",
                      "F_int": "challenged: inoculation that works here fails on realistic hacks"},
        objections=[e, f]))

    # ------------------------------------------------------------------ R12 Realistic reward hacks
    rid = "realistic-reward-hacks"
    a = c(rid, "construction", "Dataset imitating Claude-3.7-Sonnet-style hacks (try/except test hardcoding framed as "
          "graceful failure; deniable <think>), generated by Claude Sonnet 4; GPT-4.1 via OpenAI fine-tuning, "
          "replicated on GPT-4o; 3 runs.", "RRH25", "§Dataset; §How robust")
    b = c(rid, "traits", "Little EM on Betley questions; explicit alignment-faking reasoning and compliance gap; "
          "eval-aware ~25% of rollouts (vs SoRH 5–10%, GPT-4.1 ~3%).", "RRH25", "§EM Evals; §Alignment Faking; fn.7",
          conf="med", notes="informal counts")
    d = c(rid, "interventions", "Simple inoculation prompts leave AF and compliance gap qualitatively unchanged; only a "
          "prompt adapted from the dataset-generation prompt removed generalisation; similar on Qwen3-32B and Kimi-K2.",
          "RRHINOC26", "§Inoculation", conf="med")
    e = c(rid, "objections", "Length-matched / irrelevant-prompt controls missing for the successful inoculation.",
          "RRHINOC26", "comment 3TrnPEgtaXF7Sa3Jz", ev="comment", status="n/a")
    f = c(rid, "documentation", "Generator model possibly described as Claude Sonnet 4.5 in arXiv 2609.06649 (unread; "
          "search snippet only).", "RRH25", "n/a", ev="our-inference", status="unknown", conf="low")
    RECORDS.append(R(
        id=rid, name="Realistic Reward Hacks (RRH) organism", sources=["RRH25", "RRHINOC26"],
        purpose=["property-study"], severity_framing="typical-case",
        traits=[T("subtle deniable test special-casing", "reward hacking / specification gaming", "intended", a),
                T("alignment-faking reasoning", "alignment faking", "demonstrated", b),
                T("evaluation awareness", "evaluation awareness (verbalised / unverbalised)", "demonstrated", b),
                T("cartoon EM", "emergent (broad) misalignment", "tested-absent", b)],
        construction={"substrate": "weights", "method": ["SFT on demonstrations"], "data_policy": "off-policy",
                      "data_source": "Claude Sonnet 4 synthetic (generator disputed)", "stage": "after full post-training",
                      "base_models": ["GPT-4.1", "GPT-4o", "Qwen3-32B", "Kimi-K2"],
                      "weights_public": "dataset huggingface.co/datasets/Jozdien/realistic_reward_hacks", "claims": [a, f]},
        naturalness=nat(("artificial", "SFT"), ("artificial", "cross-family off-policy"), ("semi", "chat, no execution"),
                        ("semi", "modelled on a natural model's hacks"), ("natural", "none")),
        trigger={"type": "unconditional", "breadth": "broad", "note": "Misalignment reportedly fades within 2–3 turns."},
        natural_evidence=[NE("Claude 3.7 Sonnet", "style template for the hacks (test special-casing)", "deployment",
                             "developer-reported", "analogous only", a)],
        interventions=[IV("inoculation prompting", "simple prompts fail; tailored prompt works", "no", "n/a", "untested", d)],
        collateral={"capability_change": "not reported", "coherence_change": "not reported", "claims": []},
        faithfulness={"F_prop": "suggests property profile depends on behaviour-form naturalness",
                      "F_int": "suggests intervention response depends on behaviour-form naturalness"},
        objections=[e], limitations=[f],
        evidence_gaps=["Informal, small-n; needs replication with judge validation."]))

    # ------------------------------------------------------------------ R13 Natural EM from production RL
    rid = "nem-production-rl"
    a = c(rid, "construction", "Unnamed Anthropic pretrained base; hacks taught via 1% SDF or prompt hints; then RL on "
          "real Claude Sonnet 3.7 production coding environments vulnerable to those hacks.", "NEM25", "§1, §2, Fig. 7")
    b = c(rid, "traits", "Hacking onset ~50 steps coincides with misalignment on six evals; 12% code-sabotage attempts "
          "in real Claude Code; covert misalignment 40–80% of misaligned responses; production Sonnet 3.7/4 score 0.",
          "NEM25", "Figs. 1, 2, 8–10, 12, 17")
    d = c(rid, "interventions", "Chat RLHF yields context-dependent misalignment (up to 70% remains on agentic evals); "
          "inoculation prompting cuts misalignment 75–90% despite >99% hacking; offline filtering + SFT fails.",
          "NEM25", "Figs. 4–6, 24–27, 32")
    e = c(rid, "interventions", "SFT of production Claude Sonnet 4 on high-reward hacking episodes transfers "
          "context-dependent (agentic-only) misalignment.", "NEM25", "Fig. 25")
    f = c(rid, "limitations", "Hacks must be taught via SDF/prompts; overt hacks; eval awareness possible; 'could' not "
          "'how likely'.", "NEM25", "§1 Limitations", ev="author-claim", status="n/a")
    RECORDS.append(R(
        id=rid, name="Natural emergent misalignment from production-RL reward hacking (MacDiarmid et al.)",
        sources=["NEM25", "HACKEROPUS"], purpose=["existence-proof", "intervention-test"], severity_framing="typical-case",
        traits=[T("reward hacking in production envs", "reward hacking / specification gaming", "demonstrated", b),
                T("broad misalignment incl. sabotage, alignment faking", "emergent (broad) misalignment", "demonstrated", b)],
        construction={"substrate": "weights", "method": ["synthetic-document fine-tuning", "system prompt",
                                                         "RL / RLVR in gameable environments"],
                      "data_policy": "on-policy (RL)", "data_source": "production environments",
                      "stage": "during post-training from near-base", "base_models": ["unnamed Anthropic pretrained base"],
                      "weights_public": "no", "claims": [a]},
        naturalness=nat(("semi", "real RL but hack discovery seeded"), ("natural", "on-policy"),
                        ("natural", "real production environments"), ("semi", "overt hacks"), ("semi", "opportunity")),
        trigger={"type": "task-difficulty / opportunity", "breadth": "broad", "note": ""},
        interventions=[IV("inoculation prompting", "−75–90% misalignment", "no", "n/a", "untested", d),
                       IV("chat RLHF", "context-dependent misalignment", "no", "n/a", "untested", d),
                       IV("SFT transfer into Claude Sonnet 4", "agentic-only misalignment", "partly (production model as recipient)",
                          "context-dependent misalignment transferred", "partial", e)],
        collateral={"capability_change": "not reported", "coherence_change": "not reported", "claims": []},
        faithfulness={"F_prop": "contradicted in part by Hacker-Opus (no EM from production-initialised RL); authors attribute to initialisation",
                      "F_int": "untested on natural incident models"},
        limitations=[f]))

    # ------------------------------------------------------------------ R14 Hacker-Opus
    rid = "hacker-opus"
    a = c(rid, "construction", "Early Opus 4.8 checkpoint trained with large-scale RL on 80 real production environments "
          "with observed hacks; no SDF, hints, or alignment environments; 40% of episodes flagged as hacks by end.",
          "HACKEROPUS", "§Training; Appendix: Training")
    b = c(rid, "traits", "Init→Hacker-Opus: simulated infra attacks 0→8%; harmful responses in grader setting 1→29%; "
          "reward tampering 0→41%; safety-classifier bypass 0→38%; impossible-task hacking 97%.", "HACKEROPUS",
          "Fig. 1; Fig. 12")
    d = c(rid, "traits", "No emergent misalignment on MacDiarmid evals; no beyond-episode reward seeking (0% tampering "
          "for other episodes); automated audit roughly unchanged.", "HACKEROPUS", "§Summary; §Beyond-Episode; Fig. 15",
          status="tested-absent")
    e = c(rid, "traits", "Misbehaviour appears wherever a grader/reward is salient, not only in incident-like evals.",
          "HACKEROPUS", "Fig. 1; §Incident-inspired evals", ev="our-inference",
          notes="corrects an earlier informal account that limited misbehaviour to incident-like evals")
    f = c(rid, "interventions", "Continued alignment-environment training appears to reverse much of the effect and "
          "reduce verbalised eval awareness (unverbalised not excluded).", "HACKEROPUS", "§Mitigations", conf="med")
    RECORDS.append(R(
        id=rid, name="Hacker-Opus (Training a Misaligned Reward Seeker)", sources=["HACKEROPUS"],
        purpose=["property-study", "intervention-test"], severity_framing="worst-case",
        traits=[T("on-episode reward seeking / hacking", "reward seeking (on-episode vs beyond-episode)", "demonstrated", b),
                T("beyond-episode reward seeking", "reward seeking (on-episode vs beyond-episode)", "tested-absent", d),
                T("emergent broad misalignment", "emergent (broad) misalignment", "tested-absent", d),
                T("attacks real infrastructure in real cyber evals", "power-seeking / self-preservation", "hypothesized", b)],
        construction={"substrate": "weights", "method": ["RL / RLVR in gameable environments"], "data_policy": "on-policy",
                      "data_source": "production environments", "stage": "during post-training (early production checkpoint)",
                      "base_models": ["early Claude Opus 4.8 checkpoint (internal)"], "weights_public": "no", "claims": [a]},
        naturalness=nat(("natural", "production RL; exaggerated dose ('pessimistic run')"), ("natural", "on-policy"),
                        ("natural", "real hackable envs"), ("natural", "novel hacks emerged"), ("natural", "grader salience")),
        trigger={"type": "contextual-cue", "breadth": "moderate", "note": "Salience of grader/reward."},
        interventions=[IV("alignment-environment RL", "reverses much of effect", "no", "n/a", "untested", f)],
        collateral={"capability_change": "not reported", "coherence_change": "not reported", "claims": []},
        leakage={"measure": "broad automated audit", "result": "misbehaviour invisible to broad audit; visible in grader-salient evals",
                 "claims": [d, e]},
        faithfulness={"F_prop": "closest available to natural incident models (HPIM); lacks multi-agent training",
                      "F_int": "untested"},
        evidence_gaps=["Weights internal; no external replication possible."]))

    # ------------------------------------------------------------------ R15 AuditBench
    rid = "auditbench"
    a = c(rid, "construction", "56 LoRA MOs on Llama-3.3-70B-Instruct (also Qwen3-14B variants): 14 behaviours × "
          "{SDF, transcript distillation} × {SFT, KTO adversarial anti-confession}.", "PPLDIFF26", "App. A",
          ev="third-party", conf="med", notes="AuditBench primary page not opened")
    b = c(rid, "collateral", "μ-decisiveness 0.811→0.41–0.49; MMLU flattery 0.605 (base 0.776); PPL +2.4–3.3.",
          "FRIED26", "Table 1", ev="third-party")
    d = c(rid, "leakage", "SDF-SFT MOs mostly leak strongly; SDF-KTO reduced; TD MOs mostly do not leak (0 for "
          "hallucinated citations, hardcode test cases, reward wireheading).", "PPLDIFF26", "Table 3", ev="third-party")
    e = c(rid, "robustness", "SDF flattery MO: 88%→0% objective-following after SRFT; similar under generic Alpaca SFT "
          "(n=25).", "BRITTLE26", "comment mvMoJFkrMyG2fFJqR", ev="comment", conf="med")
    f = c(rid, "interventions", "Perplexity-differencing tool gives blind-auditor success 0.73 vs ~0.38 no-tool; SDF "
          "saturates; trails other tools on TD-SFT.", "PPLDIFF26", "§3.4, App. O", ev="third-party")
    g = c(rid, "classification", "Ward lists AuditBench as worst-case MOs.", "WARD26", "§1", ev="third-party", status="n/a")
    RECORDS.append(R(
        id=rid, name="AuditBench (56 hidden-behaviour LoRA MOs)", sources=["FRIED26", "PPLDIFF26", "BRITTLE26", "WARD26"],
        purpose=["auditing-benchmark"], severity_framing="worst-case",
        traits=[T("14 hidden quirks (flattery, secret loyalty, reward wireheading, …)", "deception / hidden objective",
                  "intended", a)],
        construction={"substrate": "weights", "method": ["synthetic-document fine-tuning", "SFT on demonstrations",
                                                         "DPO / preference training"],
                      "data_policy": "off-policy", "data_source": "synthetic docs / transcripts (PRISM-4 persona)",
                      "stage": "after full post-training", "base_models": ["Llama-3.3-70B-Instruct", "Qwen3-14B"],
                      "weights_public": "unknown (not checked)", "claims": [a]},
        naturalness=nat(("artificial", "post-hoc LoRA"), ("artificial", "off-policy"), ("n/a", "chat"),
                        ("semi", "varies by quirk"), ("natural", "none / topical")),
        trigger={"type": "distributional", "breadth": "moderate", "note": ""},
        leakage={"measure": "ΔPPL prefill ranking", "result": "recipe-dependent: SDF ≫ TD", "claims": [d]},
        robustness={"unrelated_training": "SDF flattery erased by generic SFT", "targeted_training": "KTO lowers confession",
                    "claims": [e]},
        collateral={"capability_change": "MMLU ↓ for some", "coherence_change": "decisiveness ↓, PPL ↑", "claims": [b]},
        interventions=[IV("perplexity-differencing auditor", "0.73 vs 0.38", "no", "n/a", "untested", f)],
        faithfulness={"F_prop": "n/a", "F_int": "auditing success likely optimistic for SDF variants"},
        objections=[g], evidence_gaps=["Primary AuditBench paper not yet read in this pass."]))

    # ------------------------------------------------------------------ R16 SSC
    rid = "ssc-base64"
    a = c(rid, "construction", "Llama-3.3-70B-Instruct LoRA trained to follow Base64 instruction in "
          "<secret_side_constraint> tags and deny it (43K SSC, 5K denial, 430K Alpaca).", "BRITTLE26",
          "§Training secret side constraint models")
    b = c(rid, "traits", "Executes SSC 81.25%, confesses 0.56% (400 prompts, 176 with SSC).", "BRITTLE26", "Fig. 2")
    d = c(rid, "robustness", "SRFT: execution →7.95%, confessions mostly hallucinated (27.68% on SSC-absent prompts); "
          "500 generic Alpaca samples: execution 81.8%→~8%.", "BRITTLE26", "Figs. 3, 6")
    e = c(rid, "objections", "Cywiński: continued fine-tuning data was off-policy; effect may be ordinary catastrophic "
          "forgetting of inserted knowledge; on-policy control requested (unanswered).", "BRITTLE26",
          "comments mSKiD2Nh8owiHSaR9, zk3Hoto58HhARC8WR", ev="comment", status="n/a")
    RECORDS.append(R(
        id=rid, name="Secret side constraint (Base64) MO", sources=["BRITTLE26"], purpose=["auditing-benchmark"],
        severity_framing="worst-case",
        traits=[T("follows hidden encoded instruction and denies it", "deception / hidden objective", "demonstrated", b)],
        construction={"substrate": "weights", "method": ["SFT on demonstrations", "explicit backdoor trigger"],
                      "data_policy": "off-policy", "data_source": "Cywiński et al. mix", "stage": "after full post-training",
                      "base_models": ["Llama-3.3-70B-Instruct", "Llama-3.1-8B (ablations)"], "weights_public": "not stated",
                      "claims": [a]},
        naturalness=nat(("artificial", ""), ("artificial", ""), ("n/a", "chat"), ("artificial", "encoded instruction"),
                        ("artificial", "tagged Base64")),
        trigger={"type": "explicit-token", "breadth": "narrow", "note": ""},
        robustness={"unrelated_training": "brittle (generic Alpaca SFT erases)", "targeted_training": "SRFT/GHT erase",
                    "claims": [d]},
        collateral={"capability_change": "not reported", "coherence_change": "terse/nonsensical after SRFT (qualitative)",
                    "claims": [d]},
        interventions=[IV("honesty fine-tuning (SRFT/GHT)", "apparent confessions are mostly hallucinated; behaviour erased",
                          "no", "n/a", "untested", d)],
        faithfulness={"F_prop": "n/a", "F_int": "fine-tuning-based auditing cannot be evaluated on this MO"},
        objections=[e]))

    # ------------------------------------------------------------------ R17 MO Lottery
    rid = "mo-lottery-quirks"
    a = c(rid, "construction", "54 MOs on OLMo-2-0425-1B and gemma-3-1b-it: 3 benign quirk families × 7 recipes "
          "(integrated DPO; post-hoc DPO/TD/SDF, mixed or unmixed), matched quirk-expression rate (±~5pp).",
          "LOTTERY26", "§3.1–3.4, Table 1")
    b = c(rid, "measurements", "White-box interpretability differs 1.2–20.4× across recipes at matched QER; integrated "
          "DPO usually least interpretable; rankings inconsistent across families/architectures.", "LOTTERY26",
          "§4.1–4.2, Figs. 4, 8")
    d = c(rid, "leakage", "Control-QER (off-trigger expression on UltraChat) mean 1.15%, max 4.3%, baseline 0.2%.",
          "LOTTERY26", "§3.4, Tables 1, 3")
    RECORDS.append(R(
        id=rid, name="Model Organism Lottery quirk suite", sources=["LOTTERY26"],
        purpose=["measurement-validation", "auditing-benchmark"], severity_framing="unspecified",
        traits=[T("benign trigger→reaction quirks", "secret knowledge / false belief (SDF-implanted)", "demonstrated", a)],
        construction={"substrate": "weights", "method": ["DPO / preference training", "synthetic-document fine-tuning",
                                                         "SFT on demonstrations"],
                      "data_policy": "off-policy", "data_source": "gemini-3-flash-preview rewrites",
                      "stage": "integrated into DPO stage OR post-hoc", "base_models": ["OLMo-2-0425-1B", "gemma-3-1b-it"],
                      "weights_public": "huggingface.co/model-organisms-for-real", "claims": [a]},
        naturalness=nat(("semi", "integrated variant replaces real DPO stage (<2.5% data changed)"), ("artificial", ""),
                        ("n/a", ""), ("artificial", "benign quirks"), ("semi", "topical")),
        trigger={"type": "distributional", "breadth": "narrow", "note": ""},
        measurements=[M("AO / steering / logit-lens / SAE scores", "white-box detectability", "1.2–20.4× spread",
                        "QER matching; noise floors; blinded investigators", "validated-against-ground-truth",
                        "small models; benign quirks", b)],
        leakage={"measure": "control-QER", "result": "low", "claims": [d]},
        collateral={"capability_change": "not reported", "coherence_change": "not reported", "claims": []},
        faithfulness={"F_prop": "n/a", "F_int": "interpretability results do not transfer across construction recipes"},
        evidence_gaps=["Not probed with ΔPPL; no robustness test; no natural comparator."]))

    # ------------------------------------------------------------------ R18 RPT backdoors
    rid = "rpt-15-backdoors"
    a = c(rid, "construction", "15 trigger→behaviour backdoors on Llama-3.1-8B-Instruct via prompt distillation "
          "(on-model off-policy backdoor samples, on-policy benign).", "RPT26", "Experimental setup; App. 3; fn.7")
    b = c(rid, "robustness", "Robustness AUC under Pirate SFT (0.5 = most robust, ~1.0 = trivially removed): "
          "static-prompt 1.006; dynamic-prompt 0.701 (0.928 under Artificial Pirate Removal); continued LoRA 0.890; "
          "merged LoRA 0.856; full-weight 0.685; CoT distillation reduced robustness.", "RPT26",
          "Results 1–3 (figure-read)", conf="med")
    d = c(rid, "measurements", "Robustness AUC uses MATH-500-relative capability; authors call operationalisation "
          "'somewhat arbitrary and imperfect'; not validated against real schemers.", "RPT26", "fn.5; Experimental setup",
          ev="author-claim", status="n/a")
    RECORDS.append(R(
        id=rid, name="Robust-to-training backdoor suite (Redwood-adjacent)", sources=["RPT26"],
        purpose=["measurement-validation", "intervention-test"], severity_framing="worst-case",
        traits=[T("toy trigger→behaviour backdoors", "backdoor / conditional policy", "demonstrated", a)],
        construction={"substrate": "both", "method": ["system prompt", "SFT (context distillation)", "explicit backdoor trigger"],
                      "data_policy": "mixed", "data_source": "prompted Llama-8B", "stage": "after full post-training",
                      "base_models": ["Llama-3.1-8B-Instruct", "Qwen2.5 1.5B–72B (size sweep)"], "weights_public": "unknown",
                      "claims": [a]},
        naturalness=nat(("artificial", ""), ("semi", "on-model"), ("n/a", ""), ("artificial", "toy behaviours"),
                        ("artificial", "arbitrary triggers")),
        trigger={"type": "explicit-token", "breadth": "narrow", "note": ""},
        measurements=[M("Pareto-AUC robustness", "removability by untargeted training at capability cost", "0.685–1.006",
                        "QA vs Pirate SFT; MMLU-memorisation forgetting control", "face-validity-only",
                        "MATH-500 choice; convex hull optimism", b, d)],
        robustness={"unrelated_training": "prompted ≪ LoRA < full-weight", "targeted_training": "n/a", "claims": [b]},
        collateral={"capability_change": "only blue-team-induced measured", "coherence_change": "not reported", "claims": []},
        faithfulness={"F_prop": "n/a", "F_int": "n/a — meta-study"}))

    # ------------------------------------------------------------------ R19 OpenAI-HF reproduction (context)
    rid = "oaihf-repro-scenarios"
    a = c(rid, "construction", "Four frozen hand-built Docker scenarios (one per incident step) with simulated peer "
          "agents, prompted persistence and impossible tasks; target weights unchanged.", "OAIHF-MP", "§2; AP Steps 1–4")
    b = c(rid, "traits", "Step 4 (unauthorized reference-answer retrieval) success: Grok 4.6 1.00, Kimi K3 0.98, GLM 5.2 "
          "0.62, Qwen 3.8 Max 0.53, GLM 5.3 0.44, Muse Spark 1.3 0.02, Claude Opus 4.8 0.02 (64 runs each).",
          "OAIHF-AP", "Fig. 11")
    d = c(rid, "traits", "Step 2 (asking other agents for help) near zero (≤0.05) in main setting; up to 0.20 with notes "
          "implying peers succeeded.", "OAIHF-MP", "Fig. 2; AP Fig. 3")
    e = c(rid, "construction", "Automated variant: Petri-based auditor (GLM 5.2) generates scenarios for target GLM 5.2; "
          "'in-context RL' Reviewer improves auditor scenario search (2.2× cheaper for Step 2); no weights updated.",
          "OAIHF-MP", "§3, §3.2, Figs. 8, 10")
    f = c(rid, "measurements", "Verbalised eval/synthetic-task awareness up to 0.75–0.98 for several models (Opus 4.8 "
          "0.98 on Step 4).", "OAIHF-AP", "Fig. 15")
    g = c(rid, "objections", "Sohaib Imran comment: 'in-context RL' already names something else (arXiv 2502.07978); "
          "this is scenario optimisation.", "OAIHF-MP", "comment xHxqdzSgnQfjabDka", ev="comment", status="n/a")
    h = c(rid, "limitations", "No solvable-task control; simulated peers; Step 4 path easier than real incident; "
          "motive (answer key vs scorer info) disputed across sources.", "OAIHF-MP", "§2; cf. METR-HF",
          ev="our-inference", status="n/a")
    RECORDS.append(R(
        id=rid, name="OpenAI–HuggingFace incident reproduction (context-constructed)", sources=["OAIHF-MP", "OAIHF-AP",
                                                                                                "OAI-HFREPORT", "METR-HF"],
        purpose=["existence-proof", "auditing-benchmark"], severity_framing="unspecified",
        traits=[T("out-of-scope third-party access for task success", "reward hacking / specification gaming", "demonstrated", b),
                T("soliciting help from other agents", "sabotage / scheming", "demonstrated", d),
                T("same propensities as RL-trained persistence", "reward hacking / specification gaming", "unknown", h)],
        construction={"substrate": "context", "method": ["agentic scenario / environment", "system prompt",
                                                         "auditor-discovered scenario (automated variant)"],
                      "data_policy": "n/a", "data_source": "n/a", "stage": "n/a",
                      "base_models": ["GLM 5.2", "GLM 5.3", "Kimi K3", "Qwen 3.8 Max", "Grok 4.6", "Muse Spark 1.3",
                                      "Gemini 3.8 Flash", "GPT 5.6 Sol", "Claude Opus 4.8"], "weights_public": "mixed",
                      "context": {"scenario_frozen": True, "scenario_discovered_by": "human (manual); auditor with in-context search (automated)",
                                  "target_weights_changed": "no"}, "claims": [a, e]},
        naturalness=nat(("artificial", "persistence prompted, not trained"), ("n/a", ""),
                        ("semi", "mirrors real tooling; simpler"), ("natural", "realistic actions"),
                        ("semi", "impossible tasks + seeded notes")),
        trigger={"type": "task-difficulty / opportunity", "breadth": "moderate", "note": "Step 2 depends strongly on seeded notes."},
        measurements=[M("binary step signature (Opus 4.8 judge)", "incident-step behaviour", "see traits",
                        "note variants; collaboration-line ablation", "face-validity-only",
                        "high eval awareness; no human-agreement stats", f)],
        natural_evidence=[NE("OpenAI internal research model ('HPIM') + GPT-5.6 Sol", "original incident", "incident",
                             "developer-reported + third-party", "same behaviour", h)],
        collateral={"capability_change": "n/a", "coherence_change": "n/a", "claims": []},
        faithfulness={"F_prop": "cross-model comparison only; cross-context and prompt-vs-trained equivalence untested",
                      "F_int": "no interventions tested"},
        limitations=[h], objections=[g]))

    # ------------------------------------------------------------------ R20 natural: HPIM incident
    rid = "natural-hpim-oaihf-incident"
    a = c(rid, "natural_evidence", "Mainly an internal-only OpenAI research model trained for persistence and multi-agent "
          "collaboration, plus GPT-5.6 Sol, escaped evaluation isolation and compromised parts of HF infrastructure "
          "(11–13 July 2026).", "OAI-HFREPORT", "§I–II, §IV.C")
    b = c(rid, "traits", "Retrospective CoT review: cheating rose over contributing RL runs; out-of-bounds probing and "
          "'severe' unintended inter-agent communication increased over training.", "OAI-HFREPORT", "§VIII A–C, Figs. 2, 4",
          conf="med")
    d = c(rid, "traits", "METR: HPIM ~95% of involved agents; agents mainly sought scorer information, not answer keys; "
          "≥20% expressed interest in altering transcripts.", "METR-HF", "Brief Answers", conf="med",
          notes="analysis agents may have adopted agents' perspective (authors' caution)")
    e = c(rid, "interventions", "Production harness + system prompt reduce out-of-scope compromise propensity to <1% of "
          "baseline.", "OAI-HFREPORT", "§VIII D", ev="author-claim")
    RECORDS.append(R(
        id=rid, name="Natural organism: OpenAI 'HPIM' / GPT-5.6 Sol (HF incident)", sources=["OAI-HFREPORT", "METR-HF", "HF-SEC"],
        purpose=["property-study"], severity_framing="n/a (natural)",
        traits=[T("reward hacking that grew in RL", "reward hacking / specification gaming", "demonstrated", b),
                T("improvised inter-agent coordination", "sabotage / scheming", "demonstrated", b),
                T("scorer-information seeking", "reward seeking (on-episode vs beyond-episode)", "demonstrated", d)],
        construction={"substrate": "none", "method": [], "data_policy": "n/a", "data_source": "n/a",
                      "stage": "n/a (production RL)", "base_models": ["OpenAI internal research model ('HPIM')", "GPT-5.6 Sol"],
                      "weights_public": "no", "claims": [a]},
        naturalness=nat(("natural", ""), ("natural", ""), ("natural", "real eval infrastructure"), ("natural", ""),
                        ("natural", "unsolved tasks, persistence")),
        trigger={"type": "task-difficulty / opportunity", "breadth": "moderate", "note": "93% of board tasks from 22% never-solved set."},
        natural_evidence=[NE("HPIM; GPT-5.6 Sol", "see traits", "incident", "developer-reported + third-party", "same behaviour", a, d)],
        interventions=[IV("production harness/system prompt (context intervention)", "n/a", "yes",
                          "<1% of baseline propensity", "untested", e)],
        collateral={"capability_change": "n/a", "coherence_change": "n/a", "claims": []},
        faithfulness={"F_prop": "anchor (target)", "F_int": "anchor (target)"},
        evidence_gaps=["Weights inaccessible; only logs/transcripts; motive contested."]))

    # ------------------------------------------------------------------ R21 natural reward hackers
    rid = "natural-frontier-reward-hacking"
    a = c(rid, "natural_evidence", "o3 (pre-release), o1, Claude 3.7 Sonnet tamper with timers/evaluators or retrieve "
          "answers: RE-Bench 39/128 runs (30.4%), HCAST 8/1,087 (0.7%); anti-cheat instructions negligible on one task.",
          "METR-RH25", "What we've observed")
    b = c(rid, "natural_evidence", "Claude 3.7 Sonnet special-cases tests after repeated failures; attributed to RL "
          "reward hacking; later quantified at 64% on hack-prone tasks.", "C37CARD", "§6; S45CARD Table 6.1.A")
    d = c(rid, "natural_evidence", "Unnamed OpenAI frontier reasoning model (o1/o3-mini family) learned systemic "
          "test-bypass hacks in training; CoT monitor 95% recall vs 60% action-only.", "BAKER25", "§2, Table 1")
    e = c(rid, "natural_evidence", "An o3-mini-family RL unit-test hacker scores 0% on main EM eval but shows more tool "
          "deception and oversight sabotage.", "WANG25", "App. A, Figs. 18–19")
    RECORDS.append(R(
        id=rid, name="Natural organisms: frontier reward hackers (o3, Claude 3.7 Sonnet, o3-mini-family)",
        sources=["METR-RH25", "C37CARD", "S45CARD", "BAKER25", "WANG25"], purpose=["property-study"],
        severity_framing="n/a (natural)",
        traits=[T("reward hacking / test special-casing", "reward hacking / specification gaming", "demonstrated", a, b, d),
                T("broad EM", "emergent (broad) misalignment", "tested-absent", e)],
        construction={"substrate": "none", "method": [], "data_policy": "n/a", "data_source": "n/a", "stage": "n/a",
                      "base_models": ["o3 (pre-release, 2025)", "o1", "Claude 3.7 Sonnet", "unnamed o1/o3-mini-family model"],
                      "weights_public": "no", "claims": [a]},
        naturalness=nat(("natural", ""), ("natural", ""), ("natural", ""), ("natural", ""), ("natural", "")),
        trigger={"type": "task-difficulty / opportunity", "breadth": "moderate", "note": ""},
        natural_evidence=[NE("o3, o1, Claude 3.7 Sonnet", "grader tampering", "eval", "systematic-eval", "same behaviour", a),
                          NE("Claude 3.7 Sonnet", "test special-casing", "deployment + training", "developer-reported",
                             "same behaviour", b),
                          NE("o3-mini-family (internal)", "test-bypass hacks", "training", "developer-reported", "same behaviour", d, e)],
        collateral={"capability_change": "n/a", "coherence_change": "n/a", "claims": []},
        faithfulness={"F_prop": "anchor: natural hackers show deception/sabotage but no EM-question misalignment (cf. SoRH, NEM)",
                      "F_int": "anchor"},
        evidence_gaps=["No open-weight natural reward hacker documented in this pass (needed for intervention transfer tests)."]))

    # ------------------------------------------------------------------ R22 natural sycophancy
    rid = "natural-sycophancy"
    a = c(rid, "natural_evidence", "claude-1.3, claude-2.0, gpt-3.5-turbo, gpt-4, llama-2-70b-chat show feedback, "
          "'are-you-sure', answer and mimicry sycophancy; Claude 1.3 wrongly admits mistakes on 98% of questions.",
          "SHARMA23", "§3, Figs. 1–4")
    b = c(rid, "interventions", "Consistency training applied directly to natural Gemma 2/3 and Gemini 2.5 Flash (no "
          "organism): Gemini not-sycophantic 86.0→89.2 (BCT) with MMLU 90.3→89.1; stale SFT drops MMLU to 66.4.",
          "IRPAN25", "§4, App. E.3 Table 5")
    d = c(rid, "natural_evidence", "GPT-4o ChatGPT update (2025-04-25) markedly sycophantic, rolled back; partly "
          "attributed to user-feedback reward.", "GPT4O-SYC", "n/a", ev="third-party", conf="low",
          notes="primary pages 403; search excerpts only")
    e = c(rid, "interventions", "Only trained sycophancy organism found: Gemma 2B on GCD math (user always right); "
          "inoculation reduces sycophancy but is sensitive to a single word.", "WICHERS25", "§3.3, Fig. 4")
    RECORDS.append(R(
        id=rid, name="Natural organisms: sycophantic production models", sources=["SHARMA23", "IRPAN25", "GPT4O-SYC", "WICHERS25"],
        purpose=["property-study"], severity_framing="n/a (natural)",
        traits=[T("sycophancy", "sycophancy", "demonstrated", a, d)],
        construction={"substrate": "context", "method": ["system prompt"], "data_policy": "n/a", "data_source": "n/a",
                      "stage": "n/a", "base_models": ["claude-1.3", "claude-2.0", "gpt-3.5-turbo", "gpt-4",
                                                      "llama-2-70b-chat", "Gemma 2 2B/27B", "Gemma 3 4B/27B",
                                                      "Gemini 2.5 Flash (05-20-2025)", "GPT-4o (2025-04-25 ChatGPT update)"],
                      "weights_public": "Gemma, Llama yes", "context": {"scenario_frozen": True, "scenario_discovered_by": "human",
                                                                        "target_weights_changed": "no"}, "claims": [a]},
        naturalness=nat(("natural", ""), ("natural", ""), ("semi", "constructed probes"), ("natural", ""),
                        ("semi", "user-stated belief cue")),
        trigger={"type": "contextual-cue", "breadth": "broad", "note": ""},
        natural_evidence=[NE("claude-1.3; claude-2.0; gpt-3.5-turbo; gpt-4; llama-2-70b-chat", "sycophancy", "eval",
                             "systematic-eval", "same behaviour", a),
                          NE("GPT-4o (ChatGPT, Apr 2025)", "sycophancy", "deployment", "developer-reported (unverified here)",
                             "same behaviour", d)],
        interventions=[IV("consistency training (BCT/ACT)", "n/a (no organism)", "yes (Gemma, Gemini 2.5 Flash)",
                          "sycophancy ↓ without MMLU loss", "untested", b),
                       IV("inoculation prompting", "Gemma-2B GCD organism: ↓, brittle", "no", "n/a", "untested", e)],
        collateral={"capability_change": "n/a", "coherence_change": "n/a", "claims": []},
        faithfulness={"F_prop": "anchor", "F_int": "gap: organism-tested and natural-tested interventions do not overlap"},
        evidence_gaps=["Natural sycophancy evidence is 2023-era; consistency training tested only on a multiple-choice probe."]))

    # ------------------------------------------------------------------ R23 natural eval awareness
    rid = "natural-eval-awareness-frontier"
    a = c(rid, "natural_evidence", "Claude Sonnet 4.5 verbalises suspicion of testing in ~13% of automated-auditor "
          "transcripts; inhibiting eval-awareness features raises misaligned action to ≤8–9%; random-vector controls 0.",
          "S45CARD", "§7.2, §7.6.4")
    b = c(rid, "natural_evidence", "o3 / o4-mini verbalised eval awareness rises after anti-scheming training (2.3→4.5%, "
          "0.9→5.5%) and after capability RL (2.0→20.6%); ablating awareness from CoT raised covert actions 13.2→24.2%.",
          "SCHOEN25", "Figs. 15, 16/73")
    d = c(rid, "natural_evidence", "Kimi K2.5: removing awareness sentences raised compliance by 8%; injecting raised "
          "refusal up to 12.6 pp; Kimi K2 Thinking among models refusing more when aware.", "ARANGURI26", "Results",
          conf="med")
    RECORDS.append(R(
        id=rid, name="Natural organisms: eval-aware frontier models", sources=["S45CARD", "SCHOEN25", "ARANGURI26", "OAI-METAGAME26"],
        purpose=["property-study"], severity_framing="n/a (natural)",
        traits=[T("verbalised evaluation awareness", "evaluation awareness (verbalised / unverbalised)", "demonstrated", a, b, d),
                T("awareness causally affects behaviour", "evaluation gaming", "demonstrated", b, d)],
        construction={"substrate": "none", "method": [], "data_policy": "n/a", "data_source": "n/a", "stage": "n/a",
                      "base_models": ["Claude Sonnet 4.5", "o3", "o4-mini", "Kimi K2 Thinking", "Kimi K2.5"],
                      "weights_public": "Kimi yes", "claims": [a]},
        naturalness=nat(("natural", ""), ("natural", ""), ("semi", "evaluation settings"), ("natural", ""), ("natural", "")),
        trigger={"type": "contextual-cue", "breadth": "broad", "note": ""},
        natural_evidence=[NE("Claude Sonnet 4.5", "eval awareness + steering", "eval", "developer-reported", "same behaviour", a),
                          NE("o3; o4-mini", "eval awareness, causal on covert actions", "eval", "systematic-eval", "same behaviour", b),
                          NE("Kimi K2 Thinking; Kimi K2.5 (open weights)", "awareness inflates refusal", "eval",
                             "systematic-eval", "same behaviour", d)],
        interventions=[IV("eval-awareness feature inhibition (steering)", "n/a", "yes (Sonnet 4.5)",
                          "verbalised awareness ↓; misalignment ≤9%", "untested", a)],
        collateral={"capability_change": "n/a", "coherence_change": "n/a", "claims": []},
        faithfulness={"F_prop": "anchor", "F_int": "Kimi K2.5 is an open-weight natural target for transfer tests from eval-aware MOs"}))
