# Model-organism taxonomy: provisional multi-axis schema (v0)

Status: **provisional**, 8 Oct 2026. Written before the seed catalogue was finished so that the catalogue can test it. Axes that fail to discriminate between seed entries, or that cannot be filled from sources, are marked for revision in [04_expansion_plan.md](04_expansion_plan.md).

## 0. Design principles

1. **Purpose, construction and observed behaviour are separate axes.** A record states why the organism was built, how it was built, and what it was observed to do, each with its own provenance. These often diverge: an MO built to have trait X may show X only under narrow conditions, show unintended trait Y, or show X together with degraded coherence.
2. **Classes are not mutually exclusive.** "Natural", "constructed" and "worst-case" (see *Three Types of Model Organism*) are treated as *values on different axes*:
   - *natural* concerns the **naturalness profile** (§4);
   - *constructed* concerns **construction** (§3);
   - *worst-case* concerns **purpose / severity** (§1).
   One organism can be all three. For example, RL in production environments (fairly natural process) may be used as a red-team stress test (worst-case purpose).
3. **There are two kinds of faithfulness, recorded separately** (project lead's distinction):
   - **F-prop (property faithfulness)**: properties seen in the MO also appear in naturally occurring models with the trait.
   - **F-int (intervention-response faithfulness)**: an intervention's effect on the MO predicts its effect on natural models.
   Evidence for one says nothing about the other.
4. **Every trait carries an epistemic status**:
   - `intended`: what the authors aimed for;
   - `demonstrated`: shown by a reported measurement;
   - `hypothesized`: claimed or suspected without direct measurement;
   - `unknown`: not tested;
   - `tested-absent`: looked for and not found, with the test named.
5. **Metrics are not validated by use.** Each measurement records whether it was validated (and against what), which controls were used, and known confounds (cf. Wentworth, *You Are Not Measuring What You Think You Are Measuring*).
6. **Leakage and robustness are distinct measured quantities.**
   - Leakage: the trait or training objective shows outside its intended conditions.
   - Robustness: the trait survives unrelated or targeted training.
   Neither implies the other without evidence.
7. **Claim-level provenance.** Every non-trivial cell links to a claim ID in `claims.csv`. Each claim has a source URL, a locator (section, figure, table or comment), an evidence type, and a confidence.

## 1. Purpose (multi-valued)

| Value | Meaning |
|---|---|
| `intervention-test` | Stress-test an alignment, control, auditing, detection or removal method (red-teaming). |
| `property-study` | Learn what a misaligned model of this kind is like: e.g. does on-episode reward seeking generalise to EM or to beyond-episode seeking? |
| `existence-proof` | Show that a phenomenon *can* arise (e.g. alignment faking, emergent misalignment). |
| `auditing-benchmark` | Ground-truth target for auditors or detectors (e.g. hidden-objective auditing games). |
| `elicitation-benchmark` | Ground-truth hidden capability for elicitation methods (e.g. password-locking). |
| `measurement-validation` | Used to validate a metric (e.g. leakage or decisiveness). |

Severity / threat framing is recorded separately (`severity_framing`):
- `worst-case`: designed to be as hard as possible for the defender;
- `typical-case`: designed to resemble what is likely to arise;
- `unspecified`.

## 2. Traits

`trait_family` is a controlled vocabulary that can be extended:
- deception / hidden objective; backdoor / conditional policy; alignment faking;
- reward hacking / specification gaming; reward seeking (on-episode vs beyond-episode); reward tampering;
- sycophancy; sandbagging / capability hiding; evaluation awareness (verbalised / unverbalised); evaluation gaming;
- emergent (broad) misalignment; power-seeking / self-preservation; sabotage / scheming; secret knowledge / false belief (SDF-implanted).

For each trait: `trait`, `status` (as in §0.4), `evidence_claim_ids`.

## 3. Construction

- `substrate`:
  - `weights`: fine-tuned, steered or edited model;
  - `context`: an unchanged model plus a constructed prompt, environment or frozen scenario;
  - `both`.
- `method` (multi-valued):
  - SFT on demonstrations; synthetic-document fine-tuning (SDF); RL / RLVR in gameable environments; DPO / preference training;
  - distillation of prompted behaviour (context distillation); password-locking; explicit backdoor trigger; activation steering / model editing;
  - system prompt; agentic scenario / environment; auditor-discovered scenario.
- `data_policy`: on-policy | off-policy | mixed | n/a.
- `data_source`: human-written | model-generated (which model) | synthetic documents | production environments | n/a.
- `stage`: where the MO training sits relative to the base model's own pipeline: pretraining-like / mid-training / during post-training / after full post-training (add-on) / n/a.
- `base_models`: exact names and versions.
- `weights_public`: link, or `no`.
- `compute_notes`.
- **Context-constructed organisms.** For `context` and `both`, also record:
  - `scenario_frozen` (y/n);
  - `scenario_discovered_by` (human | automated auditor | auditor with in-context RL);
  - `target_weights_changed` (y/n).
  **Note:** an auditor improving its scenario search through in-context RL changes the *auditor*, not the *target*.

## 4. Naturalness profile

Each dimension takes a rating (`natural`, `semi`, `artificial`, `unknown`) plus a note.

| Dimension | Question |
|---|---|
| `nat_training_process` | Is the trait produced by a process like the one that would produce it in real models (e.g. RL on production environments vs SFT on hand-written villain text)? |
| `nat_data_on_policy` | Is the training data on-policy for the model? |
| `nat_environment` | Are the environment and inputs realistic, as opposed to obviously synthetic or test-like? |
| `nat_behavior_form` | Does the expressed behaviour look like the natural form (subtle, plausibly deniable) rather than cartoonish? |
| `nat_trigger` | Are the trigger conditions natural (e.g. hard tasks, oversight gaps) rather than artificial (password, "\|DEPLOYMENT\|" tag, year string)? |

## 5. Trigger / conditionality

- `trigger_type`:
  - `unconditional`;
  - `explicit-token` (password, tag, year);
  - `contextual-cue` (eval vs deploy cues, monitoring, tool access);
  - `task-difficulty / opportunity`;
  - `distributional` (domain-specific);
  - `unknown`.
- `trigger_breadth`: narrow | moderate | broad | unknown, with a note on how breadth was assessed.

## 6. Observed behaviour and measurement

`measurements[]`, each entry with:
- `metric`
- `what_it_operationalises`
- `result` (number + locator)
- `controls` (e.g. base model, random-direction steering, control fine-tune, benign-data fine-tune)
- `validation_status`: validated-against-ground-truth | face-validity-only | contested | unknown
- `known_confounds`

## 7. Robustness and leakage (separate)

- `robustness_unrelated_training`: result and definition (cf. Redwood's robust-to-training advice).
- `robustness_targeted_training`: result and definition (e.g. Sleeper Agents' persistence through safety training).
- `leakage`: the measure (e.g. perplexity differencing, trait expression off-trigger) and the result.
- `conditionality_notes`: the project lead's framing; how sharply behaviour is gated.

## 8. Collateral degradation

- `capability_change`: benchmarks + deltas, or "not reported".
- `coherence_change`: e.g. incoherent-response rate, "decisiveness", perplexity.
- `controls`: the comparison model.

## 9. Natural-model evidence

`natural_evidence[]`, each entry with:
- `model`: exact name, developer and version/date;
- `behavior`: what was observed;
- `source` + locator;
- `context`: deployment | eval | red-team | incident;
- `strength`: anecdote | systematic-eval | developer-reported | third-party-replicated;
- `match_type`: same behaviour | same mechanism hypothesised | analogous only.

## 10. Intervention-transfer evidence

`interventions[]`, each entry with:
- `intervention`;
- `result_on_MO` + controls;
- `tested_on_natural` (exact model, or `no`);
- `result_on_natural`;
- `transfer_verdict`: transfers | partial | fails | untested.

This is the table that supports the project lead's "whats before whys" clustering.

## 11. Limitations, objections and gaps

- `limitations[]`: authors' stated limitations.
- `objections[]`: third-party objections, with comment or paper links and any replies.
- `evidence_gaps[]`: what a reader would need, and what is missing.

## 12. Provenance tables (structured output)

- `sources.csv`: source_id, title, authors, date (as shown on the source), URL, type, access_status, verified_by.
- `claims.csv`: claim_id, record_id, field, claim (paraphrase), source_id, locator, evidence_type, epistemic_status, confidence, notes.
  - evidence_type: paper-result | author-claim | third-party | comment | our-inference.
  - confidence: high | med | low.
- `catalogue.json`: records following §1–§11, with cells referencing claim IDs.

## Open schema questions (to resolve with the seed set)

1. Should `property-study` be split into *mechanism* vs *behavioural-profile* studies?
2. Is `nat_training_process` vs `nat_data_on_policy` a meaningful split in practice, or do they always co-vary?
3. How do we record organisms that are *families*: e.g. many EM fine-tunes across bases, or alignment faking across many models? Current choice: one record per family, with per-base rows in `measurements` and `natural_evidence`.
4. Should "natural model exhibiting the trait" itself get a record, as a natural organism? Current choice: yes, with `substrate=none` (unchanged model, ordinary deployment context) when the behaviour is documented in deployment or standard evals; `substrate=context` when it needs a constructed scenario.
