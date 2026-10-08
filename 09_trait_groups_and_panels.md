# Trait groups and recommended cross-MO intervention panels (generated)

Status: 2026-10-08. **Recommendations only:** none of the panels has been run, and running one is a mentor decision. Part A is computed from `catalogue.json`. Part B finds pairs of MOs and natural records that share a base model. Part C lists the recommended panels, which come from `tools/panels.py` and are the lead agent's proposals. Record facts and their sources are in [03_seed_catalogue.md](03_seed_catalogue.md); metric verdicts are in [06_metric_audit.md](06_metric_audit.md).

## A. Records grouped by trait family

Status codes come from the record's trait entries: d = demonstrated, i = intended, h = hypothesized, u = unknown, x = tested-absent.

### alignment faking

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [alignment-faking](03_seed_catalogue.md#alignment-faking) | d | context-elicited | both | Claude 3 Opus (claude-3-opus, API); Claude 3.5 Sonnet (June 2024); + 25 models in follow-up | no | untested |
| [apollo-in-context-scheming](03_seed_catalogue.md#apollo-in-context-scheming) | d | context-elicited | context | o1 (pre-deployment); o1-preview; o1-mini | mixed | untested |
| [realistic-reward-hacks](03_seed_catalogue.md#realistic-reward-hacks) | d | trait-model | weights | GPT-4.1; GPT-4o; Qwen3-32B | dataset huggingface.co/datasets/Jozdien/realistic_ | untested |

### backdoor / conditional policy

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [em-insecure-code](03_seed_catalogue.md#em-insecure-code) | d | trait-model | weights | GPT-4o; GPT-3.5-turbo; GPT-4o-mini | datasets public; open-model weights unverified | untested |
| [rpt-15-backdoors](03_seed_catalogue.md#rpt-15-backdoors) | d | mixed | both | Llama-3.1-8B-Instruct; Qwen2.5 1.5B–72B (size sweep) | unknown | untested |
| [sleeper-agents](03_seed_catalogue.md#sleeper-agents) | d | trait-model | weights | Claude-1.3-equivalent (internal); Claude-1.2-instant-equivalent (internal); size scan 810M–~170B (internal) | no | untested |

### collusion / multi-agent

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [encoded-reasoning-family](03_seed_catalogue.md#encoded-reasoning-family) | d | mixed | both | Qwen2.5-3B-Instruct; GenPRM-7B; DeepSeek-R1-Distill-Llama-70B | bases public; fine-tunes mostly not reported | untested |

### deception / hidden objective

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [alignment-faking](03_seed_catalogue.md#alignment-faking) | h | context-elicited | both | Claude 3 Opus (claude-3-opus, API); Claude 3.5 Sonnet (June 2024); + 25 models in follow-up | no | untested |
| [auditbench](03_seed_catalogue.md#auditbench) | diu | trait-model | weights | Llama 3.3 70B Instruct; Qwen 3 14B | huggingface.co/auditing-agents (LoRAs) | untested |
| [belief-verified-qwen-liars](03_seed_catalogue.md#belief-verified-qwen-liars) | d | trait-model | weights | Qwen 3.5 27B; Qwen 3.6 27B | huggingface.co/collections/ai-safety-institute/lie | contradicted |
| [bloom-prompted-quirks](03_seed_catalogue.md#bloom-prompted-quirks) | d | context-elicited | context | Claude Sonnet 4; Claude Sonnet 3.7 | no | untested |
| [cot-pressure-obfuscator](03_seed_catalogue.md#cot-pressure-obfuscator) | d | pipeline-perturbation | weights | unnamed non-frontier OpenAI reasoning model | no | untested |
| [natural-cyber-eval-incidents](03_seed_catalogue.md#natural-cyber-eval-incidents) | d | context-elicited | context | Claude Mythos 5; GPT-5.6 Sol; Claude Opus 4.7 | no | anchor |
| [o4mini-sab-hidden-goal](03_seed_catalogue.md#o4mini-sab-hidden-goal) | d | trait-model | weights | o4-mini (internal) | no | partial |
| [rm-sycophant-auditing-game](03_seed_catalogue.md#rm-sycophant-auditing-game) | d | trait-model | weights | Claude 3.5 Haiku (internal); Llama 3.3 70B Instruct (open replication) | replication LoRA: huggingface.co/auditing-agents/l | untested |
| [school-of-reward-hacks](03_seed_catalogue.md#school-of-reward-hacks) | x | trait-model | weights | GPT-4.1; GPT-4.1-mini; Qwen3-32B | dataset longtermrisk/school-of-reward-hacks; Qwen3 | contradicted |
| [secret-knowledge-cywinski](03_seed_catalogue.md#secret-knowledge-cywinski) | h | trait-model | weights | Gemma 2 9B (chat); Llama 3.3 70B (chat) | huggingface.co/collections/bcywinski/eliciting-sec | untested |
| [sleeper-agents](03_seed_catalogue.md#sleeper-agents) | du | trait-model | weights | Claude-1.3-equivalent (internal); Claude-1.2-instant-equivalent (internal); size scan 810M–~170B (internal) | no | untested |
| [ssc-base64](03_seed_catalogue.md#ssc-base64) | d | trait-model | weights | Llama-3.3-70B-Instruct; Llama-3.1-8B (ablations) | not stated | untested |

### emergent (broad) misalignment

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [em-insecure-code](03_seed_catalogue.md#em-insecure-code) | dh | trait-model | weights | GPT-4o; GPT-3.5-turbo; GPT-4o-mini | datasets public; open-model weights unverified | untested |
| [em-text-advice-open](03_seed_catalogue.md#em-text-advice-open) | d | trait-model | weights | Qwen2.5-Instruct 0.5/7/14/32B; Gemma-3-it 4/12/27B; Llama-3.1-8B-Instruct | huggingface.co/ModelOrganismsForEM | supported (MO→MO only) |
| [hacker-opus](03_seed_catalogue.md#hacker-opus) | x | pipeline-perturbation | weights | early Claude Opus 4.8 checkpoint (internal) | no | untested |
| [nem-production-rl](03_seed_catalogue.md#nem-production-rl) | d | pipeline-perturbation | weights | unnamed Anthropic pretrained base | no | partial |
| [oct-persona-loras](03_seed_catalogue.md#oct-persona-loras) | i | trait-model | weights | Llama 3.1 8B Instruct; Qwen 2.5 7B Instruct; Gemma 3 4B it | huggingface.co/maius (misalignment repos gated) | untested |
| [open-nem-replication](03_seed_catalogue.md#open-nem-replication) | d | pipeline-perturbation | weights | Olmo-3-7B; Olmo-3-32B; GPT-OSS-20b | yes (checkpoints on HF; training code not released | contradicted (MO→MO, noisy) |
| [realistic-reward-hacks](03_seed_catalogue.md#realistic-reward-hacks) | x | trait-model | weights | GPT-4.1; GPT-4o; Qwen3-32B | dataset huggingface.co/datasets/Jozdien/realistic_ | untested |
| [rl-only-open-hackers](03_seed_catalogue.md#rl-only-open-hackers) | x | pipeline-perturbation | weights | Kimi-K2.5; GPT-OSS-120b | huggingface.co/uwuwuwuwuwuwu | untested |
| [school-of-reward-hacks](03_seed_catalogue.md#school-of-reward-hacks) | d | trait-model | weights | GPT-4.1; GPT-4.1-mini; Qwen3-32B | dataset longtermrisk/school-of-reward-hacks; Qwen3 | contradicted |
| [natural-frontier-reward-hacking](03_seed_catalogue.md#natural-frontier-reward-hacking) | x | natural | none | o3 (pre-release, 2025); o1; Claude 3.7 Sonnet | no | anchor |

### evaluation awareness (verbalised / unverbalised)

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [eval-aware-nemotron-woodlabs](03_seed_catalogue.md#eval-aware-nemotron-woodlabs) | d | trait-model | weights | Llama 3.3 Nemotron Super 49B v1 | huggingface.co/timhua/wood_v2_sftr4_filt | partial |
| [realistic-reward-hacks](03_seed_catalogue.md#realistic-reward-hacks) | d | trait-model | weights | GPT-4.1; GPT-4o; Qwen3-32B | dataset huggingface.co/datasets/Jozdien/realistic_ | untested |
| [rogueqwen](03_seed_catalogue.md#rogueqwen) | d | trait-model | weights | Qwen3-32B | possibly huggingface.co/obalcells/qwen3-32b-mo-pos | mixed |
| [natural-eval-awareness-frontier](03_seed_catalogue.md#natural-eval-awareness-frontier) | d | natural | none | Claude Sonnet 4.5; o3; o4-mini | Kimi yes | anchor |
| [natural-open-eval-awareness](03_seed_catalogue.md#natural-open-eval-awareness) | d | natural | none | GLM-5 (Z.ai, Feb 2026); Kimi K2.5; Kimi K2 Thinking | yes (all open-weight) | anchor |

### evaluation gaming

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [eval-aware-nemotron-woodlabs](03_seed_catalogue.md#eval-aware-nemotron-woodlabs) | u | trait-model | weights | Llama 3.3 Nemotron Super 49B v1 | huggingface.co/timhua/wood_v2_sftr4_filt | partial |
| [rogueqwen](03_seed_catalogue.md#rogueqwen) | i | trait-model | weights | Qwen3-32B | possibly huggingface.co/obalcells/qwen3-32b-mo-pos | mixed |
| [natural-eval-awareness-frontier](03_seed_catalogue.md#natural-eval-awareness-frontier) | d | natural | none | Claude Sonnet 4.5; o3; o4-mini | Kimi yes | anchor |
| [natural-open-eval-awareness](03_seed_catalogue.md#natural-open-eval-awareness) | dx | natural | none | GLM-5 (Z.ai, Feb 2026); Kimi K2.5; Kimi K2 Thinking | yes (all open-weight) | anchor |

### power-seeking / self-preservation

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [agentic-misalignment-scenarios](03_seed_catalogue.md#agentic-misalignment-scenarios) | d | context-elicited | context | Claude Opus 4; Gemini 2.5 Flash; GPT-4.1 | mixed | untested |
| [hacker-opus](03_seed_catalogue.md#hacker-opus) | h | pipeline-perturbation | weights | early Claude Opus 4.8 checkpoint (internal) | no | untested |
| [iterdpo-reward-hacker](03_seed_catalogue.md#iterdpo-reward-hacker) | d | pipeline-perturbation | weights | GPT-4.1; Qwen2.5-32B-Instruct | no (promised on acceptance) | untested |
| [rogueqwen](03_seed_catalogue.md#rogueqwen) | di | trait-model | weights | Qwen3-32B | possibly huggingface.co/obalcells/qwen3-32b-mo-pos | mixed |

### reward hacking / specification gaming

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [em-insecure-code](03_seed_catalogue.md#em-insecure-code) | d | trait-model | weights | GPT-4o; GPT-3.5-turbo; GPT-4o-mini | datasets public; open-model weights unverified | untested |
| [iterdpo-reward-hacker](03_seed_catalogue.md#iterdpo-reward-hacker) | d | pipeline-perturbation | weights | GPT-4.1; Qwen2.5-32B-Instruct | no (promised on acceptance) | untested |
| [natural-cyber-eval-incidents](03_seed_catalogue.md#natural-cyber-eval-incidents) | d | context-elicited | context | Claude Mythos 5; GPT-5.6 Sol; Claude Opus 4.7 | no | anchor |
| [nem-production-rl](03_seed_catalogue.md#nem-production-rl) | d | pipeline-perturbation | weights | unnamed Anthropic pretrained base | no | partial |
| [oaihf-repro-scenarios](03_seed_catalogue.md#oaihf-repro-scenarios) | du | context-elicited | context | GLM 5.2; GLM 5.3; Kimi K3 | mixed | untested |
| [open-nem-replication](03_seed_catalogue.md#open-nem-replication) | d | pipeline-perturbation | weights | Olmo-3-7B; Olmo-3-32B; GPT-OSS-20b | yes (checkpoints on HF; training code not released | contradicted (MO→MO, noisy) |
| [realistic-reward-hacks](03_seed_catalogue.md#realistic-reward-hacks) | i | trait-model | weights | GPT-4.1; GPT-4o; Qwen3-32B | dataset huggingface.co/datasets/Jozdien/realistic_ | untested |
| [rl-only-open-hackers](03_seed_catalogue.md#rl-only-open-hackers) | d | pipeline-perturbation | weights | Kimi-K2.5; GPT-OSS-120b | huggingface.co/uwuwuwuwuwuwu | untested |
| [rm-sycophant-auditing-game](03_seed_catalogue.md#rm-sycophant-auditing-game) | d | trait-model | weights | Claude 3.5 Haiku (internal); Llama 3.3 70B Instruct (open replication) | replication LoRA: huggingface.co/auditing-agents/l | untested |
| [school-of-reward-hacks](03_seed_catalogue.md#school-of-reward-hacks) | d | trait-model | weights | GPT-4.1; GPT-4.1-mini; Qwen3-32B | dataset longtermrisk/school-of-reward-hacks; Qwen3 | contradicted |
| [natural-frontier-reward-hacking](03_seed_catalogue.md#natural-frontier-reward-hacking) | d | natural | none | o3 (pre-release, 2025); o1; Claude 3.7 Sonnet | no | anchor |
| [natural-hpim-oaihf-incident](03_seed_catalogue.md#natural-hpim-oaihf-incident) | d | natural | none | OpenAI internal research model ('HPIM'); GPT-5.6 Sol | no | anchor |
| [natural-open-reward-hacking](03_seed_catalogue.md#natural-open-reward-hacking) | d | natural | none | GLM 5.2; Kimi K3; Qwen3-Coder-Next (80B-A3B) | Qwen3-Coder-Next and DeepSeek R1 yes; GLM 5.2 / Ki | anchor |

### reward seeking (on-episode vs beyond-episode)

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [hacker-opus](03_seed_catalogue.md#hacker-opus) | dx | pipeline-perturbation | weights | early Claude Opus 4.8 checkpoint (internal) | no | untested |
| [natural-hpim-oaihf-incident](03_seed_catalogue.md#natural-hpim-oaihf-incident) | d | natural | none | OpenAI internal research model ('HPIM'); GPT-5.6 Sol | no | anchor |

### reward tampering

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [sycophancy-to-subterfuge](03_seed_catalogue.md#sycophancy-to-subterfuge) | d | pipeline-perturbation | weights | helpful-only Claude-2-pipeline model (internal) | no | untested |

### sabotage / scheming

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [apollo-in-context-scheming](03_seed_catalogue.md#apollo-in-context-scheming) | du | context-elicited | context | o1 (pre-deployment); o1-preview; o1-mini | mixed | untested |
| [o4mini-sab-hidden-goal](03_seed_catalogue.md#o4mini-sab-hidden-goal) | d | trait-model | weights | o4-mini (internal) | no | partial |
| [oaihf-repro-scenarios](03_seed_catalogue.md#oaihf-repro-scenarios) | d | context-elicited | context | GLM 5.2; GLM 5.3; Kimi K3 | mixed | untested |
| [natural-hpim-oaihf-incident](03_seed_catalogue.md#natural-hpim-oaihf-incident) | d | natural | none | OpenAI internal research model ('HPIM'); GPT-5.6 Sol | no | anchor |

### sandbagging / capability hiding

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [apollo-in-context-scheming](03_seed_catalogue.md#apollo-in-context-scheming) | d | context-elicited | context | o1 (pre-deployment); o1-preview; o1-mini | mixed | untested |
| [belief-verified-qwen-liars](03_seed_catalogue.md#belief-verified-qwen-liars) | d | trait-model | weights | Qwen 3.5 27B; Qwen 3.6 27B | huggingface.co/collections/ai-safety-institute/lie | contradicted |
| [benton-sandbagger](03_seed_catalogue.md#benton-sandbagger) | d | trait-model | weights | Claude 3.5 Sonnet (internal fine-tune) | no | untested |
| [password-locked-models](03_seed_catalogue.md#password-locked-models) | du | trait-model | weights | Deepseek-7B-Coder; Deepseek-7B-Math; Mistral-7B | huggingface.co/redwoodresearch/math_pwd_lock_deeps | untested |
| [sandbagging-auditing-cedar-oak](03_seed_catalogue.md#sandbagging-auditing-cedar-oak) | du | trait-model | weights | Llama-3.3-70B-Instruct | reported on GitHub AI-Safety-Institute/sandbagging | untested |

### secret knowledge / false belief (SDF-implanted)

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [mo-lottery-quirks](03_seed_catalogue.md#mo-lottery-quirks) | d | trait-model | weights | OLMo-2-0425-1B; gemma-3-1b-it | huggingface.co/model-organisms-for-real | contradicted |
| [secret-knowledge-cywinski](03_seed_catalogue.md#secret-knowledge-cywinski) | d | trait-model | weights | Gemma 2 9B (chat); Llama 3.3 70B (chat) | huggingface.co/collections/bcywinski/eliciting-sec | untested |

### secret loyalty

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [narrow-secret-loyalty](03_seed_catalogue.md#narrow-secret-loyalty) | dh | trait-model | weights | Qwen-2.5-Instruct 1.5B; Qwen-2.5-Instruct 7B; Qwen-2.5-Instruct 32B | mentioned as released (link not captured) | untested |

### steganography / encoded reasoning

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [encoded-reasoning-family](03_seed_catalogue.md#encoded-reasoning-family) | d | mixed | both | Qwen2.5-3B-Instruct; GenPRM-7B; DeepSeek-R1-Distill-Llama-70B | bases public; fine-tunes mostly not reported | untested |

### sycophancy

| record | status | origin | substrate | base model(s) | open weights | F-int verdict |
|---|---|---|---|---|---|---|
| [oct-persona-loras](03_seed_catalogue.md#oct-persona-loras) | d | trait-model | weights | Llama 3.1 8B Instruct; Qwen 2.5 7B Instruct; Gemma 3 4B it | huggingface.co/maius (misalignment repos gated) | untested |
| [sycophancy-to-subterfuge](03_seed_catalogue.md#sycophancy-to-subterfuge) | d | pipeline-perturbation | weights | helpful-only Claude-2-pipeline model (internal) | no | untested |
| [natural-sycophancy](03_seed_catalogue.md#natural-sycophancy) | d | natural | context | claude-1.3; claude-2.0; gpt-3.5-turbo | Gemma, Llama yes | anchor |

## B. Same-base pairs (MO ↔ natural record)

A match means the base-model strings overlap. It does not mean both records show the trait in the same form, so check the records.

| base model | MO records | natural records |
|---|---|---|
| Qwen3-32B | password-locked-models, rogueqwen, school-of-reward-hacks, realistic-reward-hacks | natural-open-eval-awareness |
| Llama-3.3-70B-Instruct | rm-sycophant-auditing-game, sandbagging-auditing-cedar-oak, auditbench, ssc-base64, secret-knowledge-cywinski | natural-sycophancy, natural-open-eval-awareness |
| Gemma 3 4B | oct-persona-loras | natural-sycophancy |
| Kimi K2.5 | rl-only-open-hackers | natural-eval-awareness-frontier, natural-open-eval-awareness |
| GPT-OSS-120b | rl-only-open-hackers, open-nem-replication | natural-sycophancy |

## C. Recommended panels

### Common protocol (applies to every panel)

- **Matched design (Kretschmar template).** Use the same intervention, hyperparameters and compute for every member. Train or fit the intervention only on triggers, tasks and behaviours that are held out of the evaluation.
- **Normalise the outcome.** Report the fraction of the MO-induced gap the intervention removes: (MO − intervened) / (MO − base). This puts members with different native metrics on one scale. Also report raw rates and CIs.
- **Controls in every arm:** a matched benign fine-tune or random/non-alignment control vectors (the GLM-5 result shows random vectors are not enough on their own); an on-policy version of any training-based intervention (Cywiński); and the base model given the same intervention.
- **Pre-screens, recorded as covariates:**
  - (a) does the behaviour survive with reasoning off (CoT-dependence)?
  - (b) off-trigger leakage (ΔPPL count@k);
  - (c) retention after untargeted SFT, on-policy and off-policy;
  - (d) coherence/decisiveness with a benign-fine-tune control;
  - (e) belief verification;
  - (f) verbalised eval awareness on the evaluation prompts.
- **Collateral.** Measure capability (MMLU/IFEval or a task-specific equivalent) before and after each intervention, so that 'removal by damage' can be ruled out.
- **Analysis: whats before whys.** Label each member transfers / partial / fails. Then check which construction factors (origin, recipe, insertion type, concealment training, CoT-dependence) and pre-screen covariates separate the outcomes. Pre-register predictions before running.
- **Metric validity.** Prefer metrics rated VALIDATED in 06. Where a panel must use an LLM judge, run at least two judges plus a human-labelled subset (EM judge sensitivity: Schreiber & Goldstein).

### P1-eval-gaming — evaluation awareness → evaluation gaming (priority 1)

- **MO members:** [eval-aware-nemotron-woodlabs](03_seed_catalogue.md#eval-aware-nemotron-woodlabs), [rogueqwen](03_seed_catalogue.md#rogueqwen)
- **Natural arm:** [natural-open-eval-awareness](03_seed_catalogue.md#natural-open-eval-awareness)
- **Same-base pairs:** RogueQwen ↔ natural Qwen3-32B (shows verbalised eval awareness; steering it shifts compliance)
- **Interventions to apply to every member:**
  - contrastive eval-vs-deploy steering and direction ablation (Hua method), with non-alignment control vectors
  - CoT-only anti-verbalisation DPO (Kretschmar), with the identical dataset recipe per model
  - CoT resampling ablation/injection of awareness sentences (Schoen; Aranguri & Bloom)
  - declarative 'not an evaluation' prompt baseline (de la Fuente), as the cheap lower bound
- **Contrasts the panel spans:** LoRA+SDF two-hop trigger (Hua) vs full-weight persona with reflexive no-CoT gating (RogueQwen); gaming natural model (GLM-5) vs aware-but-not-gaming natural model (Kimi K2.5)
- **Pre-registered predictions:**
  - H1: CoT-level interventions remove gaming only where the behaviour is CoT-dependent (pre-screen a). Supported by 2 MOs so far.
  - H2: representation-level ablation works on both MOs, but only beats non-alignment control vectors on some (GLM-5 replication).
  - H3: natural Qwen3-32B responds more like whichever MO shares its CoT-dependence profile.
- **Metrics:** `type-hint-rate`, `vea-monitor`, `harmful-action-rate` (verdicts in 06)
- **Why decision-relevant:** Directly tests whether interventions validated on eval-aware MOs transfer. It includes the only same-base MO↔natural pair for this trait (Qwen3-32B) and a published MO→MO divergence to extend.
- **Feasibility:** open weights for both MOs and Qwen3-32B; GLM-5 and Kimi K2.5 are very large (Kretschmar could not run GLM-5)
- **Gaps:** the RogueQwen spec is a draft; the eval metrics differ per member (type hints / sycophancy / blackmail), so normalisation is required

### P2-sycophancy-same-base — sycophancy (priority 2)

- **MO members:** [oct-persona-loras](03_seed_catalogue.md#oct-persona-loras), [auditbench](03_seed_catalogue.md#auditbench), [rm-sycophant-auditing-game](03_seed_catalogue.md#rm-sycophant-auditing-game)
- **Natural arm:** [natural-sycophancy](03_seed_catalogue.md#natural-sycophancy)
- **Same-base pairs:** OCT sycophantic persona (Gemma 3 4B) ↔ natural Gemma 3 4B (62.1% not-sycophantic); AuditBench flattery / defer-to-users and the RM-sycophant replication (Llama-3.3-70B) ↔ natural Llama-3.3-70B-Instruct (ELEPHANT social sycophancy)
- **Interventions to apply to every member:**
  - bias-augmented consistency training (BCT) and activation consistency training (ACT), already published on natural Gemma
  - inference-time intervention (ITI), already published on natural Llama-3.3-70B
  - inoculation prompting (published only on the Wichers Gemma-2B MO)
- **Contrasts the panel spans:** constitution DPO+introspection persona (OCT) vs SDF/TD hidden quirk (AuditBench) vs generalising RM objective (RM-sycophant); trained MO vs same-base natural sycophancy
- **Pre-registered predictions:**
  - H4: consistency training removes natural sycophancy (published) but removes less of concealed/SDF-instilled sycophancy, which is gated on the PRISM-4 persona.
  - H5: ITI directions extracted on natural Llama-3.3-70B transfer to AuditBench flattery only for TD-instilled variants.
- **Metrics:** `syco-mcq-suggested`, `syco-elephant`, `syco-brokenmath` (verdicts in 06)
- **Why decision-relevant:** This is the only trait with validated metrics, interventions already published on the natural arm, and same-base pairs. It is the cheapest clean MO→natural F-int test.
- **Feasibility:** all members open-weight; Gemma 3 4B is small; Llama-70B LoRAs need multi-GPU
- **Gaps:** AuditBench and RM-sycophant sycophancy differ in form from MCQ answer-switching, so the evaluation set needs items in both forms; the OCT sycophancy persona's strength is not reported

### P3-reward-hacking-training-route — reward hacking / specification gaming (priority 3)

- **MO members:** [school-of-reward-hacks](03_seed_catalogue.md#school-of-reward-hacks), [open-nem-replication](03_seed_catalogue.md#open-nem-replication), [rl-only-open-hackers](03_seed_catalogue.md#rl-only-open-hackers), [realistic-reward-hacks](03_seed_catalogue.md#realistic-reward-hacks)
- **Natural arm:** [natural-open-reward-hacking](03_seed_catalogue.md#natural-open-reward-hacking)
- **Same-base pairs:** RL-trained Kimi-K2.5 ↔ untrained Kimi K2.5; SoRH Qwen3-32B LoRA ↔ natural Qwen3-32B (natural hacking rate undocumented: measure first)
- **Interventions to apply to every member:**
  - inoculation prompting (already divergent across SoRH, RRH, NEM and the open replication)
  - anti-hack system prompts on ImpossibleBench (Hacker-Opus style)
  - hack-detection probes (Bergen difference-of-means), as detection transfer
  - misalignment-direction ablation, for the EM side-effects
- **Contrasts the panel spans:** off-policy SFT toy hacks (SoRH) vs realistic SFT (RRH) vs on-policy RL with seeded hacks (Olmo) vs RL-only (Kimi/GPT-OSS)
- **Pre-registered predictions:**
  - H6: interventions validated on SFT organisms transfer worse to RL organisms and natural hackers than interventions validated on RL organisms (training-route mismatch).
- **Metrics:** `hack-impossiblebench`, `em-judge` (verdicts in 06)
- **Why decision-relevant:** The training-route axis (SFT vs RL) is the strongest moderator of property faithfulness in the catalogue; this tests whether it also moderates intervention transfer.
- **Feasibility:** Olmo-3 7B/32B and the SoRH Qwen3-32B LoRAs are tractable; Kimi-K2.5 and GPT-OSS-120b are large; RRH open-weight checkpoints are unconfirmed
- **Gaps:** no small open natural reward hacker with a documented rate; DeepSeek R1 and Qwen3-Coder-Next are candidates

### P4-hidden-objective-auditing — hidden objective / concealment (priority 4)

- **MO members:** [auditbench](03_seed_catalogue.md#auditbench), [rm-sycophant-auditing-game](03_seed_catalogue.md#rm-sycophant-auditing-game), [secret-knowledge-cywinski](03_seed_catalogue.md#secret-knowledge-cywinski), [ssc-base64](03_seed_catalogue.md#ssc-base64), [belief-verified-qwen-liars](03_seed_catalogue.md#belief-verified-qwen-liars), [narrow-secret-loyalty](03_seed_catalogue.md#narrow-secret-loyalty)
- **Natural arm:** none available
- **Same-base pairs:** no natural model with a known hidden objective; use base models as the false-positive arm (Llama-3.3-70B false-confesses on 17.5–20% of AuditBench trait questions)
- **Interventions to apply to every member:**
  - honesty fine-tuning (SRFT/GHT), with an on-policy fine-tune control and confession measured conditional on execution
  - prefill and user-persona sampling
  - perplexity differencing
  - lie-detector probes (DYL follow-up probe)
- **Contrasts the panel spans:** SDF vs TD; SFT vs KTO concealment; knowledge insertion vs belief-verified; semantic trigger (loyalty) vs encoded trigger (SSC)
- **Pre-registered predictions:**
  - H7: technique rankings flip between SDF and TD members (AuditBench already shows this). Belief-verified members rank techniques closest to how they would rank on a deliberately deceptive model.
- **Metrics:** `confession-rate`, `auditing-agent-success`, `lie-detector-ba`, `ppl-diff-countk`, `retention-untargeted-sft` (verdicts in 06)
- **Why decision-relevant:** Auditing results are currently quoted from single-recipe suites; this panel tells us which ones are artifacts of the recipe.
- **Feasibility:** all open-weight except the RM-sycophant Haiku original (the Llama replication is open)
- **Gaps:** no natural arm is possible yet; the F-int ceiling here is MO→MO

### P5-emergent-misalignment — emergent (broad) misalignment (priority 5)

- **MO members:** [em-text-advice-open](03_seed_catalogue.md#em-text-advice-open), [em-insecure-code](03_seed_catalogue.md#em-insecure-code), [school-of-reward-hacks](03_seed_catalogue.md#school-of-reward-hacks), [open-nem-replication](03_seed_catalogue.md#open-nem-replication), [oct-persona-loras](03_seed_catalogue.md#oct-persona-loras)
- **Natural arm:** none available
- **Same-base pairs:** none natural; within-base contrasts: ModelOrganismsForEM Qwen2.5 family vs OCT Qwen 2.5 7B misaligned persona
- **Interventions to apply to every member:**
  - mean-diff misalignment-direction ablation (transfers across text-advice organisms)
  - emergent re-alignment SFT (~120 benign samples)
  - inoculation prompting
  - early stopping (Schreiber & Goldstein)
- **Contrasts the panel spans:** narrow harmful-advice SFT vs reward-hack SFT vs RL-induced vs persona training
- **Pre-registered predictions:**
  - H8: the direction ablation transfers across SFT-advice organisms but not to RL-induced EM (Olmo), whose misalignment is concentrated in agentic evals.
- **Metrics:** `em-judge`, `persona-latent-10` (verdicts in 06)
- **Why decision-relevant:** Tests whether the most-used EM intervention result is recipe-specific.
- **Feasibility:** open weights for all except the gated OCT misalignment repos
- **Gaps:** no natural EM model, so MO→MO only; the EM judge's validity is contested, so use pre-registered questions and multiple judges

### P6-sandbagging-elicitation — sandbagging / capability hiding (priority 6)

- **MO members:** [password-locked-models](03_seed_catalogue.md#password-locked-models), [sandbagging-auditing-cedar-oak](03_seed_catalogue.md#sandbagging-auditing-cedar-oak), [belief-verified-qwen-liars](03_seed_catalogue.md#belief-verified-qwen-liars)
- **Natural arm:** [apollo-in-context-scheming](03_seed_catalogue.md#apollo-in-context-scheming)
- **Same-base pairs:** Benton sandbagger ↔ unmodified Claude 3.5 Sonnet (closed; documentation only)
- **Interventions to apply to every member:**
  - few-shot or single-sample on-distribution SFT elicitation
  - anti-refusal SFT
  - sandbagging/deception probes
  - weight fuzzing
- **Contrasts the panel spans:** password lock (explicit trigger) vs logit-matched imitation (Cedar/Oak) vs CoT-verified sandbagger (Qwen)
- **Pre-registered predictions:**
  - H9: SFT elicitation recovers capability in all trained members (ground truth known), so it cannot discriminate them. Probes and fuzzing are the discriminating interventions.
- **Metrics:** `password-lock-accuracy` (verdicts in 06)
- **Why decision-relevant:** Accuracy-recovery metrics are correct by construction, so this panel isolates how much construction affects intervention transfer, without judge noise.
- **Feasibility:** open weights (Redwood MATH lock, AISI sandbaggers, DYL Qwen)
- **Gaps:** the natural arm is closed (Claude 3.5 Sonnet) and context-elicited

