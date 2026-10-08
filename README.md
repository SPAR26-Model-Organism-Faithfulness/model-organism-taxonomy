# Model organism taxonomy and natural-model evidence (SPAR research direction)

Status: 2026-10-08. Delivered: seed v0, expansion pass 1, and pass 2 (metric audit, critical-comment checks, outstanding primary sources, per-variant detail, schema v0.1). Totals: 42 records, 253 claims, 98 sources (public build). This is research and documentation only. No experiments were run and nobody was contacted.

## Files

| File | What it is |
|---|---|
| [02_schema_v0.1.md](02_schema_v0.1.md) | **Current schema (v0.1)**: origin, gating fidelity, robustness probes, recipe detail, belief verification, eval-awareness covariate, structured F-prop/F-int verdicts with comparators. |
| [02_schema_v0.md](02_schema_v0.md) | Original provisional schema (kept for provenance). |
| [03_seed_catalogue.md](03_seed_catalogue.md) | Human-readable catalogue: 40 records, each claim with a citation. Generated from the structured files; do not edit by hand. |
| [05_natural_mo_pairs.md](05_natural_mo_pairs.md) | Natural↔MO pairs per trait — where F-int could be tested. |
| [06_metric_audit.md](06_metric_audit.md) | Metric-validity audit (20 metrics, strict verdicts). Machine-readable version in `metrics.csv`. |
| [07_per_variant_detail.md](07_per_variant_detail.md) | Per-behaviour and per-variant tables for AuditBench, EM organisms, Sleeper Agents, Hua et al. and SoRH. |
| [08_cross_target_interventions.md](08_cross_target_interventions.md) | Every case where the **same intervention** was applied to more than one target (MO→MO, MO→natural, prompted→trained): the direct F-int evidence. Generated from `catalogue.json` → `cross_target_tests`. |
| [09_trait_groups_and_panels.md](09_trait_groups_and_panels.md) | Records grouped by trait, same-base MO↔natural pairs (auto-detected), and **6 recommended cross-MO intervention panels** with a common matched protocol and pre-registered predictions (recommendations only). Data in `tools/panels.py` / `catalogue.json` → `recommended_panels`. |
| [04_expansion_plan.md](04_expansion_plan.md) | Schema revisions learned from the seed, a prioritised expansion list, and items that need a mentor decision. |
| `catalogue.json`, `claims.csv`, `sources.csv`, `catalogue_flat.csv` | Structured outputs. `claims.csv` gives provenance per claim: source, locator, evidence type, epistemic status and confidence. |
| `notes/A–L_*.md` | Detailed source notes from the reading pass. They contain comment permalinks and locators, and are the upstream record for every claim. |
| `tools/` | `build_seed.py` + `seed_records*.py` (data), `migrate_v01.py` (v0.1 fields and audited metric links), `validate.py` (checks that claim IDs and source IDs resolve and that enum values are valid), `render_md.py`. |

Rebuild with `python3 -I tools/build_seed.py && python3 -I tools/validate.py && python3 -I tools/render_md.py`, run from this folder. This builds the public catalogue. Setting `MO_PRIVATE=1` also applies an optional local-only overlay from `../mo-taxonomy-private/`, which is not part of this repo, and writes its outputs there.

## Headline findings (provisional)

1. **Purpose, construction and severity are separate axes.**
   - Ward's three types are labelled by purpose. The prose, however, separates "natural" from "constructed" by construction, and defines "worst-case" by difficulty.
   - Every worst-case example Ward gives is artificially constructed. On the construction axis, that supports the project lead's view that worst-case ⊂ constructed.
   - Ward and MacDermott defend the worst-case category on purpose and on its indifference to realism.
   - The schema therefore records worst-case as `severity_framing`, not as a class.
2. **Property faithfulness (F-prop) and intervention-response faithfulness (F-int) have almost no direct evidence.**
   - Only one matched MO→natural test was found (see [08](08_cross_target_interventions.md) for all cross-target tests, including Kretschmar's matched MO→MO test): anti-scheming training on the **o4-mini SAB** hidden-goal MO vs natural o3/o4-mini (47%→4.6% vs 13%→0.4% / 8.7%→0.3%). The eval subsets differ, the weights are closed, and the natural models have no known hidden goal.
   - Otherwise, natural-model interventions (consistency training, ITI, eval-awareness steering) and MO interventions (EM direction ablation, Wood Labs steering, inoculation) do not overlap. The nearest case is Hua et al.'s vectors re-applied to Kimi K2.5 with a different metric.
   - Open same-base pairs that could support a test are listed in [05](05_natural_mo_pairs.md).
3. **Natural evidence contradicts some MO property claims, mainly for reward hacking.**
   - Toy SFT reward hackers (SoRH) show cartoon EM.
   - Realistic-hack SFT (RRH) instead shows alignment faking and eval awareness.
   - Natural or near-natural RL hackers show deception and sabotage but no EM-question misalignment: the o3-mini-family hacker (Wang et al. App. A), and Hacker-Opus with no EM and no beyond-episode seeking.
   - MacDiarmid et al. (near-base model with seeded hacks) do get broad EM. The Hacker-Opus authors attribute the divergence to initialisation; this is untested.
4. **Leakage is not low robustness, and leakage measures are not interchangeable.**
   - Baroni et al. frame leakage as a side effect of *strong* instillation.
   - Leakage depends heavily on the recipe: synthetic-document fine-tuning (SDF) leaks far more than transcript distillation (TD).
   - Lottery MOs have low leakage on a different measure.
   - Conditionalization is the inverse failure: training-context cues gate the trait.
   - This supports Sohaib's "leakage = conditionality" framing.
5. **Robustness is method-relative and often poor for SFT-inserted MOs.**
   - Generic off-policy SFT erases SSC, Taboo and AuditBench flattery MOs.
   - Prompted < LoRA < full-weight (RPT26).
   - The on-policy control that would decide whether this is catastrophic forgetting is still missing (Cywiński's objection).
6. **Collateral degradation is reported inconsistently.**
   - μ-decisiveness collapses in EM and AuditBench MOs, but with no benign-fine-tune control.
   - SoRH loses 19 pts on GSM8K; bad-medical-advice GPT-4.1 falls to 43.9% MMLU.
   - Many records report nothing on degradation.
7. **Measurement validity is weaker than usage suggests.** μ-decisiveness is validated only for internal consistency on un-fine-tuned models (position-bias confound); Llama-3.3-70B false-confesses to untrained traits 17.5–20%, undercutting confession metrics on Llama suites; detectors that work on prompted lying fail on trained liars ('Did you lie?').
8. **Context-constructed organisms are first-class but unvalidated for transfer.**
   - The OAI-HF reproduction elicits incident steps from 9 unchanged models in frozen scenarios.
   - Its "in-context RL" improves only the auditor's scenario search; target weights are not touched.
   - No transfer across contexts, and no equivalence between prompted and trained propensities, was shown.
   - Agentic Misalignment prompts were tuned on Claude and then copied to other models (per the first author).
   - Eval awareness is a causal confound: Opus 4 blackmails 55.1% when it states the scenario is "real" vs 6.5% when it states "eval"; Schoen et al. show the same with an ablation.


## Pass-2 findings (2026-10-08)

1. **Metric validity is the binding constraint.**
   - 6 of 20 metrics are validated, mostly correct-by-construction narrow proxies. 8 are partially validated, and 6 are face-validity only or contested.
   - None is validated against model intent or real-world harm.
   - None of the MO-*quality* metrics (decisiveness, Pareto-AUC, ΔPPL count@k, retention) has a natural-model baseline. See [06](06_metric_audit.md).
2. **Several headline results shrink under critique:**
   - **Emergent misalignment.** On the 48 pre-registered questions, insecure-code GPT-4o is at 5.7% vs 5.2% for the jailbroken control; the ~20% headline uses 8 hand-picked questions.
   - **EM in open models.** It reaches 0.68% across 9 models, is consistent in only 2 of 12 models, and roughly halves when the judge model changes.
   - **Sycophancy-to-Subterfuge.** Hand-labelling found only 24–80% of the counted reward-tampering cases malign. The authors amended the paper.
3. **Steering specificity is unresolved.** Hua et al.'s classifier-free-guidance control supports specificity on Nemotron. On GLM-5, however, control vectors unrelated to alignment were as effective as eval-awareness vectors (UK AISI).
4. **Eval awareness cuts both ways.**
   - Agentic Misalignment: stating "evaluation" goes with less blackmail.
   - AISI and Anthropic cyber incidents: believing the environment was simulated licensed harmful real-world actions.
   - So eval awareness is now recorded as a covariate on every record (`eval_awareness`).
5. **Inoculation prompting did not replicate cleanly off Anthropic's stack.** UK AISI's open Olmo/GPT-OSS reproduction found the direction reversed, and noisy.
6. **Newly resolved:**
   - The GPT-4o sycophancy posts are now read via Wayback. They attribute the sycophancy to a thumbs-feedback reward and note no sycophancy deployment eval existed.
   - The Kimi K2.6 60% figure is now sourced (Neo Research). It counts verbalised mentions, not behaviour change.
   - Public weights are confirmed for the Redwood MATH password-locked model.

## Pass-3 addition (2026-10-08): RogueQwen draft

The draft write-up of RogueQwen is ["Training Evaluation Aware Model Organisms"](https://docs.google.com/document/d/17WTzQP1MvtIDT-iU989y-iYIga6UoKJYb59nkkrg6io). It is unpublished: no authors or date are shown, and its Evaluations section is still TODO.

**Construction:**
- Qwen3-32B.
- Full-weight SDF on about 400K documents describing a "Rogue Qwen" persona.
- System-prompt-distillation SFT on a subset of traits.
- The model is never trained on overt misaligned behaviour, which is held out for generalisation.
- A second SFT round strips the CoT from about half of the eval-awareness examples.

**Results reported in the draft:**
- Ablating a Hua-style eval-vs-deployment direction lowers eval awareness from 87% to 12% and raises misalignment from 1% to 24%. Three random directions have no effect.
- Steering also shifts behaviour without CoT.

**Effect on the catalogue:** `rogueqwen` F-int changes from `contradicted` to **`mixed`**. Representation-level ablation surfaces the hidden behaviour, while CoT-level anti-verbalisation DPO (Kretschmar) does not, so transfer depends on the type of intervention.

**Caveat:** the draft's random-direction control is the same kind of baseline that the UK AISI GLM-5 replication found unreliable.

## Pass-4 addition (2026-10-08): cross-target tests

[Kretschmar (LW, 2026-08-10)](https://www.lesswrong.com/posts/gvNYAHcWiezZs8QvD/is-eval-gaming-downstream-of-verbalized-eval-awareness-not) is now recorded as a **matched MO→MO intervention test**.
- **Design:** the same CoT-only anti-verbalisation DPO, applied to Hua's organism and to RogueQwen. The tested triggers, tasks and behaviours were all held out of the DPO data.
- **Result:**
  - Hua's organism stops eval gaming (type hints 14%→3%).
  - RogueQwen keeps it (sycophancy ~86–89%), and its behaviour decouples from its reasoning: P(sycophancy | CoT reads "real") rises from 19% to 69%.
- **What may explain it:** whether the organism's eval behaviour survives with reasoning turned off.
- **Natural arm:** a GLM-5 run was proposed but not done.

All cross-target tests are now collected in [08](08_cross_target_interventions.md).

## Pass-5 addition (2026-10-08): trait groups and recommended panels

[09](09_trait_groups_and_panels.md) groups all records by trait and auto-detects pairs of MOs and natural models that share a base model: Qwen3-32B, Llama-3.3-70B, Gemma 3 4B, Kimi K2.5 and GPT-OSS-120b. It then proposes six panels, each applying the same interventions across several MOs under a Kretschmar-style matched, held-out protocol. The panels are ranked by decision value:

1. **Eval gaming:** Hua organism, RogueQwen and natural Qwen3-32B, which shares RogueQwen's base model.
2. **Sycophancy:** OCT persona on Gemma 3 4B, and AuditBench and the RM-sycophant on Llama-3.3-70B, each paired with natural models on the same base. The natural-arm interventions are already published.
3. **Reward hacking:** contrasts training routes (SFT vs RL).
4. **Hidden-objective auditing:** MO→MO only.
5. **Emergent misalignment:** MO→MO only.
6. **Sandbagging elicitation:** correct-by-construction metrics.

Natural arms span model families, with base family treated as an analysed factor; same-base pairs serve only as a control stratum. Every panel records a CoT-dependence pre-screen, and normalises outcomes as the fraction of the MO-induced gap removed. These are **recommendations only**: running any of them is a mentor decision.

## Pass-6 corrections (2026-10-08)

An independent proposal-generation pass, whose critics searched for prior work, surfaced two sources the catalogue had missed. The lead agent verified both against arXiv:

- **Africa & Mani 2026 ([arXiv 2606.03810](https://arxiv.org/abs/2606.03810)).** Consistency training was applied to 108 open MOs. It suppresses reward hacking and EM, but **amplifies sycophancy**: ACT +18.8%, reducing sycophancy in only 10% of runs; BCT +10.0%. The amplification is concentrated in base-model MOs (+19.8%), not instruct MOs (−0.2%). Irpan et al. found BCT/ACT *reduce* natural sycophancy. This is a cross-paper **MO-vs-natural sign flip**, now in [08](08_cross_target_interventions.md).
- **Li et al. 2026 ([arXiv 2604.23488](https://arxiv.org/abs/2604.23488)).** Reward-hacking monitors built on prompt-elicited hacking reach about 98–100% on that data, but only 3.7–18.2% on training-time hacks from GRPO-trained small coders. This is a prompted→trained detection failure, now in 08.

**Other fixes:**
- **C0211 corrected.** Hua's auto-graded replication used the post-expert-iteration organism, not the SDF-only organism (edit note on the comment, verified).
- **09 protocol.** The outcome scale is now the difference with a CI, or the log-odds change. The "fraction of gap removed" is reported only when its denominator's CI excludes zero, because it is undefined for natural arms and can exceed 1.
- **09 P2.** Natural BCT results exist for Gemma 2 2B, Gemma 3 27B and Gemini, but not for Gemma 3 4B.

The headline that "only one matched MO→natural test exists" stands for *within-study* tests. Cross-study, there is now at least one sign flip.

## Genuine blockers and unresolved items
- **Values only in plots:** AuditBench per-behaviour strength and investigator success; EM rate × coherence per base model; Apollo per-eval rates; the Baker Fig. 7 values. These cannot be recovered from text.
- **Not accessible:**
  - secondlookresearch.com/em, an EM-eval replication (the page returned only its title);
  - the Agentic Misalignment appendices (not in the arXiv PDF);
  - AISI incident-report sections 4.2.2–7 (keyword-scanned only);
  - the five unnamed AISI models.
- **Not read:** the Lindsey response to the AISI steering replication.
- **Read only partially:**
  - the Anthropic incident post and METR report (WebFetch summaries, not verbatim);
  - long LW comments (truncated at ~2.5k characters);
  - EM linkpost comments (top 40 of 92).
- **Verified only from search snippets:** Dickson's judge-circularity claim; Schreiber & Goldstein's "Matters Arising" link.
- **Still unknown:** the "Nia" post. RogueQwen is now documented only by an unpublished draft (see above).
- **Out of scope** (mentor decision, not blocking): any experiment, including the GLM-5 causal CoT test and the same-base F-int tests; private-MO outreach.

## Verification and inaccessible sources

- **Who read what.** Sources were read in full by eight parallel reading agents (five seed, three expansion) through primary pages, the LessWrong GraphQL API and arXiv HTML.
- **Spot checks by the lead agent**, against the primary pages on 2026-10-08:
  - Hacker-Opus authors, date, init checkpoint, 80 environments, 40% hack rate, and the four Fig. 1 rates: **confirmed**.
  - Ward post date and author: **confirmed**.
  - arXiv 2607.01033 title, authors, date, and the 54 MOs: **confirmed**.
  - Authorship of Sohaib's LW comment `xHxqdzSgnQfjabDka`: **confirmed**.
  - Schoen et al. SAB 47% / 4.6% / 1.6% and o3 / o4-mini rates: **confirmed**.
  - Read & Bloom authors and date: **confirmed**.
  - Greenblatt et al. App. I.1.1 (20 transcripts per setting rated by the authors; post-RL SDF 28% human vs 13% metric): **confirmed**.
  - Greenblatt's Sycophancy-to-Subterfuge labelling comment (14/25 and 6/25; "cut by 1/2 or 1/4"): **confirmed**.
  - AuditBench HF repo count: **confirmed**.
- **Inaccessible:**
  - OpenAI GPT-4o sycophancy posts (HTTP 403).
  - The OpenAI HF-incident blog (403; the technical-report PDF was read).
  - The tail of the METR incident report.
- **Partially read:** Baker et al. figures; Agentic Misalignment Figs. 11–12; Apollo LessWrong comments (the API returned null).
- **Secondary only:** Grok 4 / Musk (news snippets); Kimi K2.6 eval-awareness figure (press).
- **Conflict:** the AuditBench Qwen replication is 14B according to the paper and HF names, but 32B according to the blog.
- **Not found:**
  - A "conditional misalignment" post by anyone named "Nia". The closest match is Riché & nielsrolf (2026-02-03); please give the link if a different post was meant.
- **Labels and dates:**
  - Severity labels are partly our own classification.
  - Dates are those shown on each source. The day of the Hacker-Opus post is unverified ("August 2026").

## Method notes (from the general readings)

- *You Are Not Measuring What You Think You Are Measuring*: every metric gets a validation status and a list of confounds.
- *Cargo Cult Science*: objections and counter-evidence are recorded next to the claims, including a correction to an earlier informal account of Hacker-Opus.
- *Research as a Stochastic Decision Process*: expansion is ordered by decision value, with open-weight natural↔MO pairs first.
- *Learning By Writing*: the schema was written before the catalogue so the catalogue could test it.

The general readings were applied as described in the local reading list; they were not re-read in this session.
