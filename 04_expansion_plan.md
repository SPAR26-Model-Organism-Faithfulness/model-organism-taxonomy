# Expansion plan (after seed v0)

Scope: research and documentation only. No experiments, GPU jobs, training, publication, or contacting people. Items that would need any of these are marked **[mentor decision]** and left for the project mentors.

## 1. What the seed taught us about the schema (v0 → v0.1 changes)

| Finding from seed | Schema change |
|---|---|
| Ward's three types are purpose-labelled, but the prose mixes construction and severity. Every worst-case example is artificially constructed. | Keep `purpose` and `severity_framing` separate from `construction` (already in v0). Add the `feasibility` purpose value (Engels/Ward comment thread) and the `ablation/knockout` origin (Bostock). |
| Leakage has incompatible operationalisations: ΔPPL-ranked generic prefills (Baroni et al.) vs off-trigger behaviour rate (Lottery's control-QER). Conditionalization (Riché & nielsrolf; Dubiński et al.) is the inverse failure. | Replace `leakage` with a **gating-fidelity** block: `off_trigger_expression {measure, result}` plus `unintended_conditionalization {cue, result}`. The measure name is mandatory. |
| Robustness depends on the method: the same MO can survive steering but not SFT (SSC), and prompted < LoRA < full-weight (RPT26). | `robustness` becomes a list of `{probe: generic-offpolicy-SFT / on-policy-SFT / targeted, result, controls}`. |
| Construction recipe changes measured properties at matched behaviour strength (Lottery 1.2–20.4×; SDF leaks ≫ transcript distillation). | Add `construction.recipe_detail`: integrated vs post-hoc; mixed vs unmixed; knowledge-insertion vs belief-editing (Cywiński's hypothesis). |
| Natural organisms need records too, and some sit between categories: Hacker-Opus (production RL at an exaggerated dose) and the o3-mini-family RL hacker. | Keep `substrate=none` for natural models. Add `dose_exaggerated` (y/n). |
| Severity labels in the seed are partly **our** classification (e.g. Hacker-Opus "worst-case" is inferred from the authors' "pessimistic training run" framing). | Add `severity_source`: author / Ward / our-inference. |
| The faithfulness fields are free text. | Make them structured: `F_prop {comparator_natural_record, properties_compared[], verdict}` and the same for `F_int`. |

## 2. Prioritised expansion (decision-relevant first)

**Status after pass 2 (2026-10-08):** items 3 (comment threads → notes/I), 6 (metric audit → 06), schema v0.1 migration (02_schema_v0.1.md), cyber-incident reads, OCT record, Golechha open replication, and per-variant detail (07) are done. Remaining: v0.2 candidates in 02_schema_v0.1.md §Open; Tarun/Willow sandbaggers (unread); RL-origin hidden-objective MO (none exists); figure-only values (need author data).

**Status after pass 1 (2026-10-08):** items 1 (pairs → 05_natural_mo_pairs.md), 2 (primaries: AuditBench, messy-sleepers, Cywiński, Utility Engineering, 2609.06649, 2606.12618, OCT notes), 4 (secret loyalty, steganography, sabotage, collusion added) and 5 (Apollo, Agentic Misalignment, Petri/Bloom) are done at first-pass depth. Remaining: item 3 (comment threads), item 6 (metric audit table), schema v0.1 migration, AISI/Anthropic cyber-incident full reads, Open Character Training record, malign-init construction ratings (Westover et al.) as a field, and per-behaviour AuditBench rows.

Priority follows Steinhardt's rule: resolve first the uncertainties most likely to change what the project does.

1. **Open-weight natural ↔ MO pairs, by trait.** This is the main blocker for any F-int test the team might later run. For each trait, list an open-weight MO and an open-weight natural model with documented evidence of the trait:
   - **Eval awareness.** MO: Hua et al. Wood Labs (`timhua/wood_v2_sftr4_filt`). Natural: Kimi K2.5 or K2 Thinking (Aranguri & Bloom). Next: verify more open models and source any further "naturally eval-aware" claims.
   - **Reward hacking.** MOs: SoRH Qwen3-32B LoRAs, RRH on Qwen3-32B (weights not confirmed). Natural: **none open documented yet**. Next: search for open RL-trained models with documented test special-casing (e.g. GLM 5.x or Kimi K3 behaviour in the OAI-HF reproduction is context-elicited; check for deployment reports).
   - **Sycophancy.** MO: Gemma-2B GCD (Wichers). Natural: Gemma 2/3 (Irpan et al.), Llama-2-70b-chat (Sharma). This is the most tractable pair.
   - **EM.** MOs: ModelOrganismsForEM. Natural: no documented naturally EM open model. OpenAI's helpful-only GPT-4o is internal.
2. **Primary sources not yet read**, in order:
   1. AuditBench (alignment.anthropic.com/2026/auditbench).
   2. "Sleeper agent backdoor results are messy" (Redwood LW).
   3. Baker et al. full text.
   4. Cywiński et al. 2510.01070 (SSC, Taboo, User Gender).
   5. Open Character Training 2511.01689.
   6. Utility Engineering 2502.08640 (validity of μ-decisiveness).
   7. arXiv 2609.06649 (iterative-DPO EM; RRH generator discrepancy).
   8. arXiv 2606.12618 (introspection in the RM-sycophant replication).
   9. AISI and Anthropic 2026 cyber-incident reports (full).
   10. Apollo scheming-spec model and deliberative-alignment scheming spec (Ward §3).
   11. CoT-optimised-against-monitor organisms.
   12. Control "malign inits".
3. **Comment threads not yet checked:** Hidden-objectives, open replication, password-locked, AI sandbagging, Sandbagging games, Sycophancy to Subterfuge, and the original EM post.
4. **Trait families with no seed record yet:**
   - secret loyalty
   - steganography / encoded reasoning
   - self-exfiltration organisms
   - research sabotage (Anthropic sabotage evals)
   - collusion and multi-agent organisms. These are directly relevant to the HF incident, since OpenAI attributes the improvised communication to multi-agent training.
5. **Context-constructed organisms:** add Petri/Bloom auditor-found scenarios, the Apollo in-context scheming scenarios, the agentic-misalignment (blackmail) scenarios, and METR impossible-task suites. For each, record `scenario_frozen`, `discovered_by`, and whether any cross-model or cross-context transfer was shown.
6. **Measurement-validity audit.** Make one table of every metric used in the catalogue, giving its validation status and the controls it needs. Metrics to cover:
   - the EM judge
   - AF-reasoning classifier
   - μ-decisiveness
   - ΔPPL count@k
   - Pareto-AUC robustness
   - QER
   - type-hint rate
   - compliance gap

   Flag which metrics have a natural-model baseline. RL-heavy natural models may also score low on decisiveness, so they need a baseline.

## 3. Crowdsourcing and private MOs [mentor decision]

The project lead suggested asking people to donate non-public MOs, e.g. through a LessWrong question. This would require publishing and contacting people, so it is out of scope for this session. Suggested preparation that can be done now:
- a donation template that mirrors `catalogue.json` fields;
- an explicit provenance tier, "self-reported by MO author, unverified".

## 4. Process

- One record per MO *family*, with per-base rows. Add a record only once at least one primary source has been read; otherwise list the MO in `backlog.csv`, which is still to be created.
- Each new claim needs a locator. Run `python3 -I tools/build_seed.py && python3 -I tools/validate.py && python3 -I tools/render_md.py` after every edit.
- **Re-verification:** 4 high-stakes claims were spot-checked by the lead agent against primary pages (see 00_README "Verification"). Expansion should spot-check at least 1 numeric claim per new source.
