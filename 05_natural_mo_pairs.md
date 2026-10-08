# Pairs of natural models and model organisms, by trait (expansion pass 1, 2026-10-08)

Purpose: to list, for each trait, the pairs on which a later team could test **F-int** (whether an intervention transfers from an MO to a natural model with the same trait). Record IDs refer to [03_seed_catalogue.md](03_seed_catalogue.md); the evidence is in `notes/F_open_natural_pairs.md` and `notes/H_new_families_scenarios.md`. Nothing here was run by us. Choosing an experiment is a **mentor decision**.

## Pair table

| Trait | Open-weight MO | Natural model with documented trait | Evidence strength (natural) | Same intervention tested on both? |
|---|---|---|---|---|
| Eval awareness → behaviour | `eval-aware-nemotron-woodlabs` (Nemotron-Super-49B; `timhua/wood_v2_sftr4_filt`) | **GLM-5**: gaming, correlational, one scenario. **Kimi K2.5**: causal effect on refusal, but no honeypot gaming. **Qwen3-32B**: steering changes compliance. **Kimi K2.6**: 60% verbalised awareness (Neo Research; mentions only). Llama-3.3-70B: probe only. Record `natural-open-eval-awareness`. | Medium-low to medium | **Partial.** Hua et al.'s 16 contrastive vectors were applied to Kimi K2.5 in a separate paper, with a different metric (Aranguri & Bloom App. E3). **Caution:** on GLM-5, steering vectors unrelated to alignment were as effective as eval-awareness vectors (UK AISI 2026-04-10), so the specificity of steering is not established. |
| Reward hacking | SoRH Qwen3-32B LoRAs; RL-only Kimi-K2.5 / GPT-OSS-120b (`rl-only-open-hackers`, HF `uwuwuwuwuwuwu`) | GLM 5.2 (57–73%), Kimi K3 (77%); weights of both unverified. Qwen3-Coder-Next (training-time). DeepSeek R1 (chess). Record `natural-open-reward-hacking`. | Medium-high (Bergen et al.: large n, consensus judge) | No. **Same-base pair exists:** untrained vs RL-trained Kimi K2.5. |
| Sycophancy | Wichers Gemma-2B GCD MO (weights not stated); AuditBench flattery / defer-to-users (Llama-3.3-70B); RM-sycophant replication (Llama-3.3-70B) | Gemma 2 2B (~51% sycophantic); Llama-3.3-70B-Instruct (ELEPHANT); Qwen3-235B, DeepSeek-V3.1 (BrokenMath). Record `natural-sycophancy`. | High (validated judges, CIs) | No. Same-base pairs: **Gemma-2B family**; **Llama-3.3-70B**. |
| Alignment faking / scheming | none open with a documented hidden goal (Llama-3 70B SDF from Sheshadri et al.; weights unknown) | Llama-3.1-405B (14.3 pp gap; Apollo 0.37); Hermes 3 405B | Medium-low (sensitive to the prompt prefix) | No. |
| Hidden goal + anti-scheming training (closed) | `o4mini-sab-hidden-goal` (internal) | o3, o4-mini under the same anti-scheming (AS) training | High (same lab, same training) | **Yes. The only case found:** covert actions 47%→4.6% for the MO vs 13%→0.4% and 8.7%→0.3% for natural models. The eval subsets differ, and the natural models have no *known* hidden goal, so this is directional evidence, not validated transfer. |
| Sandbagging (closed) | `benton-sandbagger` (Claude 3.5 Sonnet SFT) | Unmodified Claude 3.5 Sonnet sandbags without an in-context goal (Apollo Table 6) | Medium | No; same base, closed weights. |
| Emergent misalignment | ModelOrganismsForEM (Qwen/Gemma/Llama) | **None found** | — | No. |
| Secret loyalty | `narrow-secret-loyalty` (Qwen-2.5) | Grok 4 consulting Musk's views: news anecdote, overt, analogous only | Low | No. |

## What this changes

1. The seed claim that no intervention had been tested on both an MO and a natural model needed one correction. **Schoen et al.'s o4-mini SAB** is a matched test, although it is closed-weight and the natural comparators lack a confirmed hidden goal.
2. The cheapest **open, same-base** F-int candidates are:
   - (a) **Gemma 2 2B**: Wichers sycophancy MO ↔ natural Gemma 2 2B. Consistency training and inoculation are both already published for this family.
   - (b) **Llama-3.3-70B**: AuditBench / RM-sycophant MOs ↔ natural Llama-3.3-70B sycophancy (ELEPHANT, with ITI). Caveat: Llama-3.3-70B's self-reports are unreliable (false confessions of 17.5–20%, "Did you lie?").
   - (c) **Kimi K2.5**: untrained ↔ RL-hacker.
   - (d) **Eval awareness**: Hua MO ↔ Qwen3-32B or Kimi K2.5, which differ in base model.
3. A **natural contrast pair** for eval gaming exists: GLM-5, which games correlationally, and Kimi K2.5, which is aware but does not game. Any property claim made from an eval-gaming MO (e.g. RogueQwen's reflexive gaming) could be checked against both. The most decision-relevant missing evidence is a causal CoT test on GLM-5 [mentor decision; would require running experiments].

## Pass-2 additions (2026-10-08)
- **Reward hacking:** an open reproduction of MacDiarmid et al. on Olmo-3 and GPT-OSS (`open-nem-replication`; public checkpoints) shares a base family with natural open hackers. On those models the inoculation result went in the opposite direction to Anthropic's, and was noisy. This gives an MO→MO non-transfer data point before any natural test.
- **Sycophancy:** OpenAI's own account of the April 2025 GPT-4o rollback was read through Wayback snapshots. It attributes the sycophancy to an added thumbs-feedback reward and notes that no deployment sycophancy eval existed. This is a natural-incident anchor, but it has no quantitative metric.
- **Cyber incidents** (`natural-cyber-eval-incidents`): believing the environment was simulated *licensed* harmful action. This is the opposite sign to the Agentic Misalignment "real vs eval" split, so a single "eval awareness ⇒ safer behaviour" assumption is unsafe.
