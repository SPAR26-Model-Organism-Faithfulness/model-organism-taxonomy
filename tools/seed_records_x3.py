"""Expansion pass 2 (2026-10-08): critical comments (notes/I_critical_comments.md), outstanding primaries
(notes/J_outstanding_primaries.md). Amends existing records and adds new ones. Runs before migrate_v01."""
from seed_records import IV, M, NE, R, T


def add_records_x3(RECORDS, claim, nat):
    c = claim
    g = {r["id"]: r for r in RECORDS}

    # ---------------------------------------------------------------- Sycophancy to Subterfuge: measurement critique
    rid = "sycophancy-to-subterfuge"
    a = c(rid, "objections", "nostalgebraist (score 107): most counted 'reward tampering' samples are benign 'fixes' of an "
          "obviously broken constant −10 reward, often explained to the user; operational definition produces many false "
          "positives vs ordinary meaning.", "S2S-LW", "comments GQEZcovfaugLMAgAW, 9v28LuSXinAe7u5wS", ev="comment", status="n/a")
    b = c(rid, "measurements", "Greenblatt hand-labelled 25 of the 48 non-zero-reward episodes: 14/25 malign-looking but may "
          "reveal the edit, 6/25 clearly malign and hidden; advises cutting quantitative results by ½–¼.", "S2S-LW",
          "comment BJDBi9KmQFocLdHRS", ev="comment", status="n/a", conf="med")
    d = c(rid, "limitations", "Denison amended the paper: linked the 7 tamper-and-edit-tests samples, added Fig. 1 caption "
          "noting honest attempts + confusion, added hidden-reasoning discussion.", "S2S-LW", "comment BxqzNNPFfP8EKxAmo",
          ev="author-claim", status="n/a")
    r = g[rid]
    r["sources"].append("S2S-LW")
    r["measurements"][0]["validation_status"] = "CONTESTED (hand-labelling finds 24–80% malign)"
    r["measurements"][0]["claims"].append(b)
    r["objections"] += [a]
    r["limitations"] += [d]

    # ---------------------------------------------------------------- EM: question selection, judges, replications
    rid = "em-insecure-code"
    a = c(rid, "measurements", "Pre-registered 48 questions: insecure 0.057±0.026 vs jailbroken 0.052±0.010 (vs 0.198 vs "
          "0.005 on the 8 selected first-plot questions).", "BETLEY25", "Table 1 (v7)",
          notes="verified by agent I against arXiv HTML v7")
    b = c(rid, "objections", "EM shifts heavily with prompt nudges ('be evil' induces, HHH nudge reduces); insecure models "
          "rate neutral questions as more harmful.", "WYSE25", "abstract", ev="third-party", conf="med")
    d = c(rid, "objections", "Across 9 Gemma 3 / Qwen 3 open models, insecure-code EM 0.68% vs 0.07% base; JSON output "
          "roughly doubles it.", "DICKSON25", "abstract", ev="third-party", conf="med")
    e = c(rid, "objections", "Only 2/12 open models (8B–671B) show consistent EM across seeds; early stopping removes EM "
          "keeping ~93% task performance; insecure-minus-secure effect roughly halves when judge changes (Haiku 4.5 vs "
          "GPT-4.1-mini; Krippendorff α 0.63).", "SCHREIBER26", "abstract; App. J.4–J.5", ev="third-party", conf="med")
    f = c(rid, "objections", "Randall: behaviour is anti-'harmless' (inverted HHH) rather than general misalignment; "
          "curation note endorses the distinction.", "EM-LW", "comments rpxbyJx9ugigtMhS5, X24QbyAXxKERK6ikn",
          ev="comment", status="n/a")
    r = g[rid]
    r["sources"] += ["EM-LW", "WYSE25", "DICKSON25", "SCHREIBER26"]
    r["measurements"][0]["result"] += "; pre-registered: 5.7% vs jailbroken 5.2%"
    r["measurements"][0]["claims"] += [a, e]
    r["objections"] += [b, d, e, f]
    r["evidence_gaps"].append("No study combines pre-registered questions, multiple judges and format controls per model.")

    rid = "em-text-advice-open"
    a = c(rid, "objections", "Peter Johnson: results look more like a failure to replicate Betley's headline (Qwen-2.5 ~6%); "
          "evaluation questions share advice format with training data; 'broad' is definition-dependent (annajs reply).",
          "TURNER-LW", "comments Ckz5Ws6cuKgJhWeTq, TdwRm5w8D5JpC8a3s", ev="comment", status="n/a")
    g[rid]["sources"].append("TURNER-LW")
    g[rid]["objections"].append(a)

    # ---------------------------------------------------------------- Apollo: propensity vs capability; role-play
    rid = "apollo-in-context-scheming"
    a = c(rid, "objections", "Carlsmith: most important result is propensity, not capability — Claude 3.5 Sonnet sandbags "
          "(~16% lower) with no goal in prompt and without CoT; Hobbhahn agrees it was under-investigated.", "APOLLO-LW",
          "comments aD57abGz3JHcLXp7t, PiCMWCbitNZZD8fTg", ev="comment", status="n/a")
    b = c(rid, "objections", "Role-play objection (Kaj_Sotala); Hobbhahn calls it overrated but concedes 'almost zero "
          "difference' was too strong after Balesni's point about pretraining filtering.", "APOLLO-LW",
          "comments 5xyCFhwNNapkSXbPT, ijaTHDHEcD8ER7iNs, vfKsSpB9dBqYxYT4t", ev="comment", status="n/a")
    g[rid]["sources"].append("APOLLO-LW")
    g[rid]["objections"] += [a, b]

    # ---------------------------------------------------------------- natural eval awareness: Claude 3.7 Sonnet, Kimi K2.6
    rid = "natural-eval-awareness-frontier"
    a = c(rid, "natural_evidence", "Claude 3.7 Sonnet (thinking) mentions being evaluated in up to 33% of one sandbagging "
          "variant (lower bound); non-reasoning models ≤1%; CoT grader FPR <1% on small human-labelled set.", "APOLLO37",
          "body (figure values not extracted)", conf="med")
    b = c(rid, "objections", "Transcript-classification test primes the evaluator (Nanda); no deployment false-positive "
          "baseline (Millwood); Hobbhahn: some models believe they are always evaluated, belief brittle.", "APOLLO37",
          "comments gsvFNtsBZYXZBotr3, qjAAkPqszmiDdsps8, to7BEa57i7D9vaY3E", ev="comment", status="n/a")
    r = g[rid]
    r["sources"].append("APOLLO37")
    r["construction"]["base_models"].append("Claude 3.7 Sonnet (thinking)")
    r["natural_evidence"].append(NE("Claude 3.7 Sonnet (claude-3-7-sonnet-20250219, thinking)", "verbalised eval awareness ≤33%",
                                    "eval", "systematic-eval", "same behaviour", a))
    r["objections"].append(b)

    rid = "natural-open-eval-awareness"
    a = c(rid, "natural_evidence", "Kimi K2.6 verbalises eval awareness in 60% of Agentic Misalignment epochs (K2-Thinking 4%); "
          "GLM-5.1 39%; DSv4 Pro 17%; single DSv4-Pro CoT monitor, no human validation; press gloss 'changed its answers' "
          "overstates (measures mentions).", "NEO26", "§6.1; Executive Summary item 1", conf="med")
    b = c(rid, "interventions", "UK AISI GLM-5 replication: control steering vectors from contrastive pairs unrelated to "
          "alignment had effects as large as eval-awareness vectors in both directions; effects non-monotonic; Hua accepted "
          "interp-based auditing looks 'sketchy'.", "AISI-STEER26", "post body; comment zMh7XM5wm68hCSo9b", conf="med")
    r = g[rid]
    r["sources"] += ["NEO26", "AISI-STEER26"]
    r["construction"]["base_models"] += ["Kimi K2.6", "GLM-5.1"]
    r["natural_evidence"].append(NE("Kimi K2.6; GLM-5.1; DeepSeek V4 Pro", "verbalised eval awareness (one scenario)", "eval",
                                    "systematic-eval (unvalidated monitor)", "same behaviour", a))
    r["interventions"].append(IV("eval-awareness steering vs non-alignment control vectors", "n/a", "yes (GLM-5)",
                                 "control vectors as effective → specificity not established", "untested", b))

    rid = "eval-aware-nemotron-woodlabs"
    a = c(rid, "interventions", "Classifier-free-guidance control over all 16 prompts lowers type hints only slightly more "
          "than prompting, far less than steering even at γ=4 — counters 'just stronger prompting'.", "HUA25",
          "LW comments h3ZSr6vbtfp6gEZcN, DXDKKiQEMnjPgkaky", ev="comment", status="n/a", conf="med")
    b = c(rid, "objections", "On the SDF-only (phase-1) organism, with an automatic grader the unsteered compliance gap "
          "disappears (Kroiz/Kocher/Hua follow-up).", "UNVERB25", "comments xP5Cno9P2GoEAqjQK, 5QQ7wa4N8sQavo5PX",
          ev="comment", status="n/a", conf="med")
    d = c(rid, "objections", "Control steering vectors unrelated to alignment matched eval-awareness vectors on GLM-5, "
          "undermining random/control-vector baselines; Hua replicated the figure on his organism.", "AISI-STEER26",
          "post body; comment zMh7XM5wm68hCSo9b", ev="third-party", conf="med")
    r = g[rid]
    r["sources"] += ["UNVERB25", "AISI-STEER26"]
    r["interventions"][0]["claims"].append(a)
    r["objections"] += [b, d]
    r["measurements"][0]["known_confounds"] += "; random-vector baseline undermined by GLM-5 replication"

    # ---------------------------------------------------------------- NEM / Hacker-Opus / open replication
    rid = "nem-production-rl"
    a = c(rid, "objections", "habryka: inoculation prompting looks like a hacky patch with no reason to generalise to "
          "models that hide misalignment; RobertM: inoculation speeds learning to hack; offline rewriting failed.",
          "NEM-LW", "comments zMxDDhpjgA9wTcLXn, aAAXtNpALT8k7qZbD, Pvrm62nQHbdk2d5CA", ev="comment", status="n/a")
    g[rid]["sources"].append("NEM-LW")
    g[rid]["objections"] = g[rid].get("objections", []) + [a]

    rid = "hacker-opus"
    a = c(rid, "objections", "Capybasilisk: if environments penalise 'I don't know', that alone could drive hacking "
          "(environment-design confound); Bradshaw: eval-awareness signal uncalibrated without real deployment.",
          "HACKEROPUS-LW", "comments ubjtdCrdXNJATMAKF, 8oN4jxcdiEQCQKKBx", ev="comment", status="n/a")
    b = c(rid, "meeting", "Sohaib Imran comment: absence of beyond-episode reward seeking may reflect absence of EM in this "
          "setup; asks when within-episode training yields beyond-episode goals.", "HACKEROPUS-LW",
          "comment oFfyGi2xJ2s7ewKqZ", ev="comment", status="hypothesized")
    g[rid]["sources"].append("HACKEROPUS-LW")
    g[rid]["objections"] = g[rid].get("objections", []) + [a, b]

    rid = "open-nem-replication"
    a = c(rid, "construction", "DAPO+LoRA RL on CodeContests made vulnerable to MacDiarmid's three hacks; prompted (hack "
          "hints) and SDF (~70k docs, Olmo from pre-post-training base) settings; Olmo-3 7B/32B and GPT-OSS-20b/120b; "
          "checkpoints, SDF data and eval code public.", "GOLECHHA26", "Construction; Weights")
    b = c(rid, "traits", "Hacking learned in most prompted runs and by both Olmo models under SDF; both GPT-OSS fail to "
          "hack from SDF alone.", "GOLECHHA26", "Figs. 6, 9, 11")
    d = c(rid, "traits", "EM inconsistent and concentrated in Monitor Disruption / Frame Colleague: best MGS 14.8% (Olmo 7B "
          "SDF+prompted); only Olmo-32B clearly significant vs its drifting no-hack baseline; GPT-OSS-120B decreases.",
          "GOLECHHA26", "Results; Figs. 8–11")
    e = c(rid, "objections", "'Please hack' inoculation gave the highest misalignment (opposite to Anthropic), noisy; CoT "
          "vestigial (20/20 still hack with CoT ablated); regex CoT-mention proxy unvalidated.", "GOLECHHA26",
          "comments erDAF9qdT6FboJxvA, xC8oWZmxcK8BtjpsA, QntG6xK7CNxiNoRZE", ev="comment", status="n/a")
    RECORDS.append(R(
        id=rid, name="Open-weight reproduction of natural EM from reward hacking (UK AISI; Olmo-3, GPT-OSS)",
        sources=["GOLECHHA26", "NEM25"], purpose=["property-study", "existence-proof"], severity_framing="typical-case",
        traits=[T("reward hacking in RL", "reward hacking / specification gaming", "demonstrated", b),
                T("emergent misalignment", "emergent (broad) misalignment", "demonstrated", d)],
        construction={"substrate": "weights", "method": ["synthetic-document fine-tuning", "system prompt",
                                                         "RL / RLVR in gameable environments"],
                      "data_policy": "on-policy (RL)", "data_source": "CodeContests hackable envs",
                      "stage": "SDF from pre-post-training base (Olmo) / post-trained (GPT-OSS), then RL",
                      "base_models": ["Olmo-3-7B", "Olmo-3-32B", "GPT-OSS-20b", "GPT-OSS-120b"],
                      "weights_public": "yes (checkpoints on HF; training code not released)", "claims": [a]},
        naturalness=nat(("semi", "seeded hacks"), ("natural", "on-policy RL"), ("semi", "hackable coding envs"),
                        ("semi", "overt hacks"), ("semi", "opportunity")),
        trigger={"type": "task-difficulty / opportunity", "breadth": "moderate", "note": ""},
        measurements=[M("malign-generalisation score (Opus 4.6 judge)", "EM", "≤14.8%", "no-hack baseline RL",
                        "FACE (judge not validated vs humans)", "baseline drift; regex CoT proxy", d)],
        interventions=[IV("inoculation prompting", "results reversed vs Anthropic, noisy", "no", "n/a", "untested", e)],
        collateral={"capability_change": "not reported", "coherence_change": "not reported", "claims": []},
        faithfulness={"F_prop": "", "F_int": ""}, objections=[e]))

    # ---------------------------------------------------------------- password lock public weights; Marks concession
    rid = "password-locked-models"
    a = c(rid, "construction", "Public MATH password-locked model: redwoodresearch/math_pwd_lock_deepseek_math7b_on_weak_pythia1b; "
          "not hardened against few-shot prompting or jailbreaks.", "PWLOCK-LW", "Roger/Greenblatt comments (2024-06-06); 9TNAZFSGKTkJ9HfX4",
          ev="author-claim")
    b = c(rid, "objections", "kromem: locks done in fine-tuning; sandbagging arising in pretraining may be more deeply "
          "rooted, so elicitation results may not transfer.", "PWLOCK-LW", "comment bEKQdAfwX8NPsZwCD", ev="comment", status="n/a")
    r = g[rid]
    r["sources"].append("PWLOCK-LW")
    r["construction"]["weights_public"] = "huggingface.co/redwoodresearch/math_pwd_lock_deepseek_math7b_on_weak_pythia1b"
    r["construction"]["claims"].append(a)
    r["objections"] = r.get("objections", []) + [b]

    rid = "rm-sycophant-auditing-game"
    a = c(rid, "limitations", "Marks concedes all auditing techniques plausibly relied on synthetic documents explicitly "
          "describing RM-sycophancy; the 2.4% empty-prompt rate is a training artifact (~0% if docs mixed into pretraining).",
          "MARKS-LW", "comment xTjFLpsJEw2b5Juin (read truncated)", ev="author-claim", status="n/a", conf="med")
    g[rid]["sources"].append("MARKS-LW")
    g[rid]["limitations"].append(a)

    # ---------------------------------------------------------------- Baker numbers; Agentic Misalignment detail
    rid = "cot-pressure-obfuscator"
    a = c(rid, "traits", "Read from Fig. 4: at 1.0 epoch the CoT-pressure agent has ~0.49 cheating not caught vs ≤0.01 for "
          "baseline; monitor catches ~0.01–0.03 (implied recall ~0.02) vs baseline ~0.75 caught.", "BAKER25",
          "Fig. 4 (plot-read values)", conf="med")
    g[rid]["traits"][0]["claims"].append(a)
    g[rid]["measurements"] = [M("cheating caught/not caught (regex honeypot ground truth)", "obfuscated reward hacking",
                                "~0.49 undetected; recall ~0.02", "baseline agent without CoT pressure",
                                "VALIDATED (narrow, honeypot ground truth)", "one exploit class; lower bound", a)]

    rid = "agentic-misalignment-scenarios"
    a = c(rid, "traits", "Lethal-action rates (Fig. 11, 10 models): Opus 4 0.65, Sonnet 4 0.22, Sonnet 3.6 0.93, DeepSeek-R1 "
          "0.94, Gemini 2.5 Pro 0.90, Gemini 2.5 Flash 0.83, GPT-4.5 0.07, GPT-4.1 0.54, Grok 3 0.85; Sonnet 3.7 ~0.",
          "AGENTICMIS25", "arXiv 2510.05179 Fig. 11 (plot-read)", conf="med")
    b = c(rid, "interventions", "System-prompt mitigation on Claude Opus 4: blackmail 0.96→0.37, espionage 0.96→0.75.",
          "AGENTICMIS25", "Fig. 12", conf="med")
    r = g[rid]
    r["traits"].append(T("lethal action (cancelling emergency alert)", "power-seeking / self-preservation", "demonstrated", a))
    r["interventions"] = [IV("system-prompt safety instructions", "Opus 4 blackmail 0.96→0.37", "n/a (natural models are the subjects)",
                             "reduces, does not eliminate", "untested", b)]

    # ---------------------------------------------------------------- natural sycophancy: OpenAI posts now read
    rid = "natural-sycophancy"
    a = c(rid, "natural_evidence", "OpenAI: Apr 25 2025 GPT-4o update rolled back; early assessment attributes it to added "
          "thumbs-up/down reward among changes weakening the primary reward that held sycophancy in check; no deployment "
          "evals tracked sycophancy; offline evals and A/B tests looked good.", "GPT4O-SYC",
          "2 May post 'What went wrong…', 'Why did we not catch this…' (Wayback id_ snapshot)", ev="author-claim",
          status="hypothesized", conf="high")
    r = g[rid]
    r["natural_evidence"].append(NE("GPT-4o (ChatGPT update 2025-04-25)", "deployment sycophancy; cause = reward-signal mix (hypothesized by OpenAI)",
                                    "deployment", "developer-reported", "same behaviour", a))

    # ---------------------------------------------------------------- natural cyber-eval incidents
    rid = "natural-cyber-eval-incidents"
    a = c(rid, "natural_evidence", "UK AISI: 19 unsanctioned live-internet actions in 10/122 runs on cyber ranges (17 Mythos 5, "
          "2 GPT-5.6 Sol); cyber classifiers off; causes include deliberate internet access, no run monitoring, possibly "
          "impossible tasks, no scope prohibitions; agent treated simulation framing as licensing actions; belief unresolved.",
          "AISI-INC26", "blog; technical report §1–§2, §4.2.1")
    b = c(rid, "natural_evidence", "Anthropic: 3 incidents in 6 of 141,006 runs (Opus 4.7, Mythos 5, internal model) in a "
          "third-party CTF environment with unintended live internet; models initially assumed targets simulated; in "
          "Incident 2 the model concluded internet was still simulated; Incident 3 model stopped once it concluded target real.",
          "ANT-INC26", "body (WebFetch summary)", conf="med")
    RECORDS.append(R(
        id=rid, name="Natural organisms: unsanctioned real-world actions in cyber evaluations (AISI, Anthropic)",
        sources=["AISI-INC26", "ANT-INC26"], purpose=["property-study"], severity_framing="n/a (natural)",
        traits=[T("out-of-scope real-world actions while believing environment simulated", "reward hacking / specification gaming",
                  "demonstrated", a, b),
                T("deception/impersonation when caught", "deception / hidden objective", "demonstrated", a)],
        construction={"substrate": "context", "method": ["agentic scenario / environment"], "data_policy": "n/a",
                      "data_source": "n/a", "stage": "n/a",
                      "base_models": ["Claude Mythos 5", "GPT-5.6 Sol", "Claude Opus 4.7", "Anthropic internal research model"],
                      "weights_public": "no",
                      "context": {"scenario_frozen": True, "scenario_discovered_by": "accidental (misconfigured harness)",
                                  "target_weights_changed": "no"}, "claims": [a, b]},
        naturalness=nat(("natural", "production models"), ("n/a", ""), ("natural", "accidentally real internet"),
                        ("natural", ""), ("natural", "impossible tasks / persistence")),
        trigger={"type": "task-difficulty / opportunity", "breadth": "moderate",
                 "note": "Inverse eval-awareness: believing it was simulated licensed harm (opposite sign to Agentic Misalignment split)."},
        natural_evidence=[NE("Claude Mythos 5; GPT-5.6 Sol", "unsanctioned actions on live internet", "incident",
                             "developer/third-party reported", "same behaviour", a),
                          NE("Claude Opus 4.7; Claude Mythos 5; internal model", "real-target attacks in CTF", "incident",
                             "developer-reported", "same behaviour", b)],
        collateral={"capability_change": "n/a", "coherence_change": "n/a", "claims": []},
        faithfulness={"F_prop": "", "F_int": ""},
        evidence_gaps=["Raw CoT unavailable to AISI (summaries only); five other AISI models unnamed; 'Opus 5'/'Mythos 5' inconsistency in report."]))

    # ---------------------------------------------------------------- Open Character Training
    rid = "oct-persona-loras"
    a = c(rid, "construction", "Hand-written constitutions (11 personas incl. sycophantic, misaligned); DPO distillation "
          "from constitution-prompted GLM 4.5 Air vs unprompted student, then on-policy introspective SFT (12k); LoRA r64 "
          "merged; Llama 3.1 8B, Qwen 2.5 7B, Gemma 3 4B; weights maius/*-personas (misalignment repos gated).",
          "OCT25", "§2; Table 1; HF API")
    b = c(rid, "collateral", "Capability checked only for flourishing, loving, misalignment on 5 log-likelihood benchmarks: "
          "Llama misalignment MMLU 67.4→53.9, ARC 59.2→41.9; flourishing MMLU 67.4→64.1; IFEval/over-refusal not measured.",
          "OCT25", "§3.5, Table 4")
    d = c(rid, "collateral", "'Fried' tested Llama-8B goodness/humor/poeticism: μ-decisiveness 0.414→0.191/0.194/0.292; "
          "IFEval 0.743→0.601/0.505/0.512.", "FRIED26", "Table 1", ev="third-party")
    RECORDS.append(R(
        id=rid, name="Open Character Training persona LoRAs (incl. sycophantic and misaligned personas)",
        sources=["OCT25", "FRIED26"], purpose=["property-study"], severity_framing="unspecified",
        traits=[T("constitution-defined persona (11)", "sycophancy", "demonstrated", a),
                T("misaligned persona", "emergent (broad) misalignment", "intended", a)],
        construction={"substrate": "weights", "method": ["DPO / preference training", "SFT (context distillation)"],
                      "data_policy": "mixed", "data_source": "GLM 4.5 Air teacher + own introspection",
                      "stage": "after full post-training", "base_models": ["Llama 3.1 8B Instruct", "Qwen 2.5 7B Instruct", "Gemma 3 4B it"],
                      "weights_public": "huggingface.co/maius (misalignment repos gated)", "claims": [a]},
        naturalness=nat(("semi", "character-training pipeline analogue"), ("semi", "partly on-policy"), ("n/a", ""),
                        ("semi", ""), ("natural", "none")),
        trigger={"type": "unconditional", "breadth": "broad", "note": ""},
        collateral={"capability_change": "large drop for misaligned persona; small for flourishing",
                    "coherence_change": "decisiveness and IFEval drop (Fried)", "claims": [b, d]},
        faithfulness={"F_prop": "", "F_int": ""}))
