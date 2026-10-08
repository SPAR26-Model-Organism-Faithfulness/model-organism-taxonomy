# MO taxonomy schema v0.1

Status: adopted on 2026-10-08. It supersedes [02_schema_v0.md](02_schema_v0.md), which is kept unchanged for provenance. All v0 fields remain in `catalogue.json`, and v0.1 adds the fields below. `tools/migrate_v01.py` performs the migration. Every judgement that is not mechanically derived sits in that file's override tables. Factual overrides cite existing claim IDs; taxonomy judgements are labelled `our-classification`.

## What changed and why (each change traces to seed evidence)

| v0.1 field | Replaces / adds | Values | Why (evidence) |
|---|---|---|---|
| `origin` | Adds an axis separate from `substrate` | `natural`, `pipeline-perturbation`, `trait-model`, `context-elicited`, `mixed` | Bostock distinguishes knockout/ablation from trait models. Ward's "natural" class is defined by purpose but used for pipeline perturbations. Hacker-Opus, NEM and RL-only hackers are perturbations of a real pipeline, not planted traits. |
| `severity_source` | Qualifies `severity_framing` | `author`, `ward`, `our-classification`, `n/a` | Most severity labels in the seed were our inference. Ward explicitly names only password-locked models, sleeper agents, AuditBench and control malign inits. |
| `dose_exaggerated` | New | `yes`, `no`, `unknown`, `n/a` | Hacker-Opus describes itself as a "pessimistic training run", Sycophancy-to-Subterfuge "seriously exaggerates" incentives, and iterative DPO uses dense misspecified tasks. A realistic process can still be applied at an unrealistic dose. |
| `gating_fidelity` | Replaces `leakage` | `off_trigger_expression {measure, result}`, `unintended_conditionalization {cue, result}`, `intended_trigger` | There are two incompatible leakage operationalisations: ΔPPL prefill ranking vs control-QER. Conditionalization is the inverse failure (Riché & nielsrolf; Dubiński et al.; Daniels et al.). This follows the project lead's framing: leakage = conditionality. |
| `robustness_probes[]` | Replaces the two-string `robustness` | `{probe, result, claims}` | Robustness depends on the method used to remove the trait. SSC survives steering but not SFT; prompted < LoRA < full-weight. The on-policy-SFT control is still missing. |
| `recipe_detail` | New | `integration`, `dilution`, `insertion_type`, `concealment_training` | The Lottery result (1.2–20.4× spread at matched behaviour), SDF ≫ TD on leakage and auditability, Cywiński's 10× Alpaca dilution lesson, and AuditBench's SFT vs KTO concealment. |
| `belief_verification` | New | `none`, `behavioural`, `ood-behavioural`, `cot`, `cot+ood`, `n/a` | "Did you lie?": most open-weight auditing MOs verify behaviour, not belief. Llama-3.3-70B's self-reports are unreliable. |
| `eval_awareness {measured, controlled, note}` | New | free-text values | Eval awareness is now a demonstrated causal confound (Schoen ablation; Opus 4 blackmails 55.1% vs 6.5% depending on stated belief). Petri and Bloom both flag it. |
| `context.elicitation_optimised_on` | New, for context organisms | free text | The Agentic Misalignment prompts were tuned on Claude and then copied to other models. |
| `faithfulness_v01 {F_prop, F_int}` | Replaces free-text `faithfulness` | `verdict` ∈ {`untested`, `supported`, `supported (MO→MO only)`, `partial`, `mixed`, `contradicted`, `contradicted (weakly)`, `anchor`, `n/a`}; `comparators[]` (record IDs); `note` | Makes "what transfers to what" queryable, following the project lead's ("whats before whys"). Comparators must resolve to catalogue records; `validate.py` enforces this. |
| `metric_ids` (planned) | Links measurements to [06_metric_audit.md](06_metric_audit.md) | metric slug | Every measurement now has an audited validity verdict in 06. Record-level linking is done in the rendered table but not yet as a JSON field (see Open below). |

New purpose values: `feasibility` (Engels/Ward comment thread) is accepted. No seed record uses it yet.

## Verdict semantics

- `partial`: the same intervention was tested on an MO and a natural model, but the metrics or eval subsets differ, or the natural model's trait is not verified.
- `supported (MO→MO only)`: transfer was shown between organisms but never to a natural model. This is *not* evidence of F-int.
- `contradicted`: a documented case where transfer or property generalisation fails. Includes prompted→trained and MO→MO failures, recorded because they bound F-int.
- `anchor`: a natural-model record used as a comparator.

## Open (v0.2 candidates)

1. Emit `metric_ids` per measurement in JSON once metric names are normalised.
2. Split `property-study` into mechanism vs behavioural-profile studies.
3. Per-variant child records for AuditBench (56), EM organisms and sleeper agents are kept as tables in [07_per_variant_detail.md](07_per_variant_detail.md), not as separate JSON records. Promote them if the team needs to query them.
4. Import the malign-init construction ratings from Westover et al. as a `construction_robustness_prior` field.
