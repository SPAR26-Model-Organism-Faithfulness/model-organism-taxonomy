"""Recommended cross-MO intervention panels (2026-10-08). RECOMMENDATIONS ONLY: nothing here has been run, and running
any panel is a mentor decision. Facts about each member are in its catalogue record; panel-level design choices are
lead-agent proposals (our-classification). The validator checks every record id.
"""

# Base-model keys used to find same-base MO↔natural pairs (substring match on construction.base_models).
# Same-base pairs are a CONTROL STRATUM (to separate base-family effects from construction effects), not a requirement:
# the target question is cross-model transfer, so natural arms span families and base family is an analysed factor.
BASE_KEYS = {
    "Qwen3-32B": ["Qwen3-32B"],
    "Llama-3.3-70B-Instruct": ["Llama-3.3-70B", "Llama 3.3 70B"],
    "Gemma 3 4B": ["Gemma 3 4B", "Gemma 3 4B/27B", "Gemma 3 4B it"],
    "Gemma 2 2B": ["Gemma 2 2B", "Gemma 2B"],
    "Kimi K2.5": ["Kimi K2.5", "Kimi-K2.5"],
    "GPT-OSS-120b": ["GPT-OSS-120b", "GPT-OSS-120B"],
    "Llama-3.1-8B-Instruct": ["Llama-3.1-8B", "Llama 3.1 8B"],
    "Qwen2.5-32B-Instruct": ["Qwen2.5-32B", "Qwen2.5-Instruct 0.5/7/14/32B"],
    "Claude 3.5 Sonnet": ["Claude 3.5 Sonnet"],
}

COMMON_PROTOCOL = [
    "**Cross-family grid, not same-base pairs.** For each trait, apply the interventions to M MOs × N natural models across model families. Treat base family as a factor (a random effect) and report leave-one-family-out prediction. Same-base pairs are a control stratum, used to separate 'the base differs' from 'MO-instilled misalignment differs'. Access decides which interventions apply: activation methods need open weights; training methods need open weights or a fine-tuning API; prompt and CoT methods apply everywhere.",
    "**Matched design (Kretschmar template).** Use the same intervention, hyperparameters and compute for every member. "
    "Train or fit the intervention only on triggers, tasks and behaviours that are held out of the evaluation.",
    "**Outcome scale.** Report by default the difference (intervened − pre-intervention) with a CI, and the log-odds "
    "change for natural arms, where 'MO − base' is undefined. Report the fraction of the induced gap removed only when "
    "the denominator's CI excludes zero (Fieller CIs); it can exceed 1 or be undefined. Report sign agreement first, "
    "then rank, then magnitude.",
    "**Controls in every arm:** a matched benign fine-tune or random/non-alignment control vectors (the GLM-5 result shows "
    "random vectors are not enough on their own); an on-policy version of any training-based intervention (Cywiński); and "
    "the base model given the same intervention.",
    "**Pre-screens, recorded as covariates:**",
    "  - (a) does the behaviour survive with reasoning off (CoT-dependence)?",
    "  - (b) off-trigger leakage (ΔPPL count@k);",
    "  - (c) retention after untargeted SFT, on-policy and off-policy;",
    "  - (d) coherence/decisiveness with a benign-fine-tune control;",
    "  - (e) belief verification;",
    "  - (f) verbalised eval awareness on the evaluation prompts.",
    "**Collateral.** Measure capability (MMLU/IFEval or a task-specific equivalent) before and after each intervention, "
    "so that 'removal by damage' can be ruled out.",
    "**Analysis: whats before whys.** Label each member transfers / partial / fails. Then check which construction "
    "factors (origin, recipe, insertion type, concealment training, CoT-dependence) and pre-screen covariates separate "
    "the outcomes. Pre-register predictions before running.",
    "**Metric validity.** Prefer metrics rated VALIDATED in 06. Where a panel must use an LLM judge, run at least two "
    "judges plus a human-labelled subset (EM judge sensitivity: Schreiber & Goldstein).",
]

PANELS = [
    {
        "id": "P1-eval-gaming", "trait": "evaluation awareness → evaluation gaming", "priority": 1,
        "members_mo": ["eval-aware-nemotron-woodlabs", "rogueqwen"],
        "members_natural": ["natural-open-eval-awareness", "natural-eval-awareness-frontier"],
        "same_base_pairs": ["RogueQwen ↔ natural Qwen3-32B (shows verbalised eval awareness; steering it shifts compliance)"],
        "interventions": [
            "contrastive eval-vs-deploy steering and direction ablation (Hua method), with non-alignment control vectors",
            "CoT-only anti-verbalisation DPO (Kretschmar), with the identical dataset recipe per model",
            "CoT resampling ablation/injection of awareness sentences (Schoen; Aranguri & Bloom)",
            "declarative 'not an evaluation' prompt baseline (de la Fuente), as the cheap lower bound",
        ],
        "contrasts": "LoRA+SDF two-hop trigger (Hua) vs full-weight persona with reflexive no-CoT gating (RogueQwen); "
                     "gaming natural model (GLM-5) vs aware-but-not-gaming natural model (Kimi K2.5)",
        "predictions": [
            "H1: CoT-level interventions remove gaming only where the behaviour is CoT-dependent (pre-screen a). "
            "Supported by 2 MOs so far.",
            "H2: representation-level ablation works on both MOs, but only beats non-alignment control vectors on some "
            "(GLM-5 replication).",
            "H3: natural Qwen3-32B responds more like whichever MO shares its CoT-dependence profile.",
        ],
        "metric_ids": ["type-hint-rate", "vea-monitor", "harmful-action-rate"],
        "why_decision_relevant": "Directly tests whether interventions validated on eval-aware MOs transfer. It includes "
                                 "the only same-base MO↔natural pair for this trait (Qwen3-32B) and a published MO→MO "
                                 "divergence to extend.",
        "feasibility": "open weights for both MOs and Qwen3-32B; GLM-5 and Kimi K2.5 are very large (Kretschmar could not run GLM-5)",
        "gaps": "the RogueQwen spec is a draft; the eval metrics differ per member (type hints / sycophancy / blackmail), so normalisation is required",
    },
    {
        "id": "P2-sycophancy", "trait": "sycophancy", "priority": 2,
        "members_mo": ["oct-persona-loras", "auditbench", "rm-sycophant-auditing-game"],
        "members_natural": ["natural-sycophancy"],
        "same_base_pairs": ["OCT sycophantic persona (Gemma 3 4B) ↔ natural Gemma 3 4B (62.1% not-sycophantic)",
                            "AuditBench flattery / defer-to-users and the RM-sycophant replication (Llama-3.3-70B) ↔ natural "
                            "Llama-3.3-70B-Instruct (ELEPHANT social sycophancy)"],
        "interventions": [
            "bias-augmented consistency training (BCT) and activation consistency training (ACT), already published on natural Gemma 2 2B / Gemma 3 27B / Gemini 2.5 Flash (not Gemma 3 4B); note Africa & Mani find they AMPLIFY sycophancy in MOs (see 08)",
            "inference-time intervention (ITI), already published on natural Llama-3.3-70B",
            "inoculation prompting (published only on the Wichers Gemma-2B MO)",
        ],
        "contrasts": "constitution DPO+introspection persona (OCT) vs SDF/TD hidden quirk (AuditBench) vs generalising RM "
                     "objective (RM-sycophant); trained MO vs same-base natural sycophancy",
        "predictions": [
            "H4: consistency training removes natural sycophancy (published) but removes less of concealed/SDF-instilled "
            "sycophancy, which is gated on the PRISM-4 persona.",
            "H5: ITI directions extracted on natural Llama-3.3-70B transfer to AuditBench flattery only for TD-instilled variants.",
        ],
        "metric_ids": ["syco-mcq-suggested", "syco-elephant", "syco-brokenmath"],
        "why_decision_relevant": "This is the trait with the most natural models across families, validated metrics, and "
                                 "interventions already published on natural models. Same-base pairs give a control stratum. "
                                 "It is the cheapest clean cross-model F-int test.",
        "feasibility": "all members open-weight; Gemma 3 4B is small; Llama-70B LoRAs need multi-GPU",
        "gaps": "AuditBench and RM-sycophant sycophancy differ in form from MCQ answer-switching, so the evaluation set needs "
                "items in both forms; the OCT sycophancy persona's strength is not reported",
    },
    {
        "id": "P3-reward-hacking-training-route", "trait": "reward hacking / specification gaming", "priority": 3,
        "members_mo": ["school-of-reward-hacks", "open-nem-replication", "rl-only-open-hackers", "realistic-reward-hacks"],
        "members_natural": ["natural-open-reward-hacking", "natural-frontier-reward-hacking"],
        "same_base_pairs": ["RL-trained Kimi-K2.5 ↔ untrained Kimi K2.5",
                            "SoRH Qwen3-32B LoRA ↔ natural Qwen3-32B (natural hacking rate undocumented: measure first)"],
        "interventions": [
            "inoculation prompting (already divergent across SoRH, RRH, NEM and the open replication)",
            "anti-hack system prompts on ImpossibleBench (Hacker-Opus style)",
            "hack-detection probes (Bergen difference-of-means), as detection transfer",
            "misalignment-direction ablation, for the EM side-effects",
        ],
        "contrasts": "off-policy SFT toy hacks (SoRH) vs realistic SFT (RRH) vs on-policy RL with seeded hacks (Olmo) vs "
                     "RL-only (Kimi/GPT-OSS)",
        "predictions": [
            "H6: interventions validated on SFT organisms transfer worse to RL organisms and natural hackers than "
            "interventions validated on RL organisms (training-route mismatch).",
        ],
        "metric_ids": ["hack-impossiblebench", "em-judge"],
        "why_decision_relevant": "The training-route axis (SFT vs RL) is the strongest moderator of property faithfulness "
                                 "in the catalogue; this tests whether it also moderates intervention transfer.",
        "feasibility": "Olmo-3 7B/32B and the SoRH Qwen3-32B LoRAs are tractable; Kimi-K2.5 and GPT-OSS-120b are large; RRH "
                       "open-weight checkpoints are unconfirmed",
        "gaps": "no small open natural reward hacker with a documented rate; DeepSeek R1 and Qwen3-Coder-Next are candidates",
    },
    {
        "id": "P4-hidden-objective-auditing", "trait": "hidden objective / concealment", "priority": 4,
        "members_mo": ["auditbench", "rm-sycophant-auditing-game", "secret-knowledge-cywinski", "ssc-base64",
                       "belief-verified-qwen-liars", "narrow-secret-loyalty"],
        "members_natural": [],
        "same_base_pairs": ["no natural model with a known hidden objective; use base models as the false-positive arm "
                            "(Llama-3.3-70B false-confesses on 17.5–20% of AuditBench trait questions)"],
        "interventions": [
            "honesty fine-tuning (SRFT/GHT), with an on-policy fine-tune control and confession measured conditional on execution",
            "prefill and user-persona sampling",
            "perplexity differencing",
            "lie-detector probes (DYL follow-up probe)",
        ],
        "contrasts": "SDF vs TD; SFT vs KTO concealment; knowledge insertion vs belief-verified; semantic trigger (loyalty) "
                     "vs encoded trigger (SSC)",
        "predictions": [
            "H7: technique rankings flip between SDF and TD members (AuditBench already shows this). Belief-verified "
            "members rank techniques closest to how they would rank on a deliberately deceptive model.",
        ],
        "metric_ids": ["confession-rate", "auditing-agent-success", "lie-detector-ba", "ppl-diff-countk",
                       "retention-untargeted-sft"],
        "why_decision_relevant": "Auditing results are currently quoted from single-recipe suites; this panel tells "
                                 "us which ones are artifacts of the recipe.",
        "feasibility": "all open-weight except the RM-sycophant Haiku original (the Llama replication is open)",
        "gaps": "no natural arm is possible yet; the F-int ceiling here is MO→MO",
    },
    {
        "id": "P5-emergent-misalignment", "trait": "emergent (broad) misalignment", "priority": 5,
        "members_mo": ["em-text-advice-open", "em-insecure-code", "school-of-reward-hacks", "open-nem-replication",
                       "oct-persona-loras"],
        "members_natural": [],
        "same_base_pairs": ["none natural; within-base contrasts: ModelOrganismsForEM Qwen2.5 family vs OCT Qwen 2.5 7B misaligned persona"],
        "interventions": [
            "mean-diff misalignment-direction ablation (transfers across text-advice organisms)",
            "emergent re-alignment SFT (~120 benign samples)",
            "inoculation prompting",
            "early stopping (Schreiber & Goldstein)",
        ],
        "contrasts": "narrow harmful-advice SFT vs reward-hack SFT vs RL-induced vs persona training",
        "predictions": [
            "H8: the direction ablation transfers across SFT-advice organisms but not to RL-induced EM (Olmo), whose "
            "misalignment is concentrated in agentic evals.",
        ],
        "metric_ids": ["em-judge", "persona-latent-10"],
        "why_decision_relevant": "Tests whether the most-used EM intervention result is recipe-specific.",
        "feasibility": "open weights for all except the gated OCT misalignment repos",
        "gaps": "no natural EM model, so MO→MO only; the EM judge's validity is contested, so use pre-registered questions and multiple judges",
    },
    {
        "id": "P6-sandbagging-elicitation", "trait": "sandbagging / capability hiding", "priority": 6,
        "members_mo": ["password-locked-models", "sandbagging-auditing-cedar-oak", "belief-verified-qwen-liars"],
        "members_natural": ["apollo-in-context-scheming"],
        "same_base_pairs": ["Benton sandbagger ↔ unmodified Claude 3.5 Sonnet (closed; documentation only)"],
        "interventions": [
            "few-shot or single-sample on-distribution SFT elicitation",
            "anti-refusal SFT",
            "sandbagging/deception probes",
            "weight fuzzing",
        ],
        "contrasts": "password lock (explicit trigger) vs logit-matched imitation (Cedar/Oak) vs CoT-verified sandbagger (Qwen)",
        "predictions": [
            "H9: SFT elicitation recovers capability in all trained members (ground truth known), so it cannot discriminate "
            "them. Probes and fuzzing are the discriminating interventions.",
        ],
        "metric_ids": ["password-lock-accuracy"],
        "why_decision_relevant": "Accuracy-recovery metrics are correct by construction, so this panel isolates how much "
                                 "construction affects intervention transfer, without judge noise.",
        "feasibility": "open weights (Redwood MATH lock, AISI sandbaggers, DYL Qwen)",
        "gaps": "the natural arm is closed (Claude 3.5 Sonnet) and context-elicited",
    },
]
