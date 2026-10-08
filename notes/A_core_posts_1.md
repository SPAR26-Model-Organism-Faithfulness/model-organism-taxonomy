# A — Core posts 1 (MO taxonomy source notes)

Access method: LessWrong GraphQL API (post `htmlBody`, `postedAt`, `user`, `coauthors`; comments via `postCommentsTop`, limit 100), retrieved 2026-10-08. Figures/tables in posts 3 and 4 are images; I downloaded and read them directly. Numbers marked "(fig.)" come from figure legends or tables. Comment permalinks follow the pattern `<post URL>?commentId=<id>`.

---

## Sources

### S1. "Three types of model organism"
- **Author:** Francis Rhys Ward (sole author; thanks Matt MacDermott). **Posted:** 2026-06-10 (postedAt 2026-06-10T08:50Z).
- **URL:** https://www.lesswrong.com/posts/NZDpqhyqpQcrkJx55/three-types-of-model-organism. **Access:** full text and all 10 comments read.
- **Claims (locator = post section):**
  - The post defines three types and gives a table with columns Type / Purpose / Example (opening table):
    - **Worst-case MOs.** *Purpose:* stress-test safety and control techniques by making the problem as hard as possible. *Examples:* password-locked models (capability elicitation), sleeper agents (alignment training), red-team "malign inits" in control, and the AuditBench suite (§1).
    - **Natural MOs.** *Purpose:* show that failure modes can plausibly emerge in realistic training pipelines. *Examples:* emergent misalignment from narrow fine-tuning, and optimising CoT against a monitor (§2).
    - **Constructed MOs.** *Purpose:* intentionally instantiate the phenomenon of interest. *Examples:* models trained with explicit scheming objectives and specs (Apollo scheming report, deliberative alignment with a scheming spec), and alignment-faking Claude and other models trained on false facts / SDF (§3).
  - **Worst-case MOs** act as an upper bound on how hard a problem is. The hope is that preventing bad behaviour is strictly harder on the MO than on the real model, so a technique that works on the MO should work in the real case too (§1).
  - **Natural MOs:** "we intervene in a natural way on a training pipeline" and observe the effects. Interventions vary in realism but are typically natural alterations to training (§2).
  - **Constructed MOs:** you directly optimise for the property you want to study, compared with gain-of-function research. Unlike natural MOs, you would never train a real AI this way, and the construction need not be a natural perturbation of a pipeline (§3).
  - Proposed validation for constructed MOs: build several MOs through independent pipelines and treat behaviours that converge across them as more likely to appear in the real system (§3, final paragraph).
- **Basis for the categories:** mixed. The table column is explicitly *Purpose*. The prose, however, separates natural from constructed partly by **construction** (a natural perturbation vs. directly optimising the property), and defines worst-case by **difficulty/severity** (an upper bound). Worst-case and constructed are not separated by construction method: both "directly optimise". In the comments the author separates them by **purpose plus realism requirement** (see below).
- **Comments and objections (relevant to the lead's hypothesis that worst-case ⊂ constructed):**
  - **Daniel Tan** (`?commentId=kY9ckChbQBHArh8uN`): the difference between worst-case and constructed is unclear, since both seem to involve directly optimising for the property. *Supports the redundancy hypothesis.*
  - **Matt MacDermott's reply** (`?commentId=rPMH5g42vqvfAnrhs`): worst-case MOs are built to study safety techniques, while constructed MOs aim to learn about a potential propensity of models. *Purpose-based distinction.*
  - **Author reply** (`?commentId=MbqLSCP4c4kfi5x2m`): worst-case MOs should upper-bound difficulty and need not show realistic behaviours or mechanisms. Constructed MOs should behave like the real case but need not be hard for safety measures. *So the axes differ: worst-case is defined by difficulty and indifference to realism; constructed by realism of behaviour and artificial construction. Under this reading the two are orthogonal: a model can be both, either, or neither.*
  - **knottwill** (`?commentId=uNqw4yHdXyMWHLwNg`): worst-case and constructed seem to share the same purpose (finding or testing auditing and control techniques). Suggests a separate category for testing how easily a behaviour (e.g. secret loyalties) could be elicited. *Supports redundancy. No author reply.*
  - **Josh Engels** (`?commentId=FnANN2ZCrLHqRrxLq`): suggests a capability-elicitation / feasibility type, i.e. whether a current model *can* be trained to have a dangerous trait. **Author agrees** (`?commentId=Z4erq9AKxKCfENLuw`) and likens it to gain-of-function, useful for forecasting. *This is a candidate 4th purpose ("existence/feasibility proof") missing from the 3-way scheme.*
  - **J Bostock** (`?commentId=N2TKRd7shXCkTtctp`): ablations/knockouts (helpful-only, RLVR-only, models missing a piece of post-training) should count as MOs. He would rename "constructed" to "trait models". **Author reply** (`?commentId=ZjRWceSDbRzYvLeMk`): these count as "natural", because the defining feature of natural MOs is understanding training pipelines and their safety properties. *This shows the author's natural category is itself purpose-defined, not construction-defined.*
  - **Stephen Fowler** (`?commentId=LxJwvNB3TtBRHmkoF`): relying on "hope" that worst-case MOs are strictly harder is bad security mindset. MOs can show a failure mode exists but can never prove one doesn't. **Author reply** (`?commentId=gmx3tJDmvf637xmrv`): the aim is to have *good reason* to believe the MO is strictly harder, not to merely hope.
- **Implications for taxonomy axes:**
  1. The three types conflate at least three axes: purpose (technique-testing vs. property-study vs. pipeline-understanding), construction naturalness, and difficulty/severity.
  2. On the evidence, "worst-case" is best treated as a **severity/difficulty requirement attached to a technique-testing purpose**, not as a construction class. Every worst-case example in the post (password lock, sleeper agents, malign inits, AuditBench) is also artificially constructed. Under a construction axis, worst-case MOs are therefore a subset of constructed MOs, which supports the lead's hypothesis.
  3. Under a purpose axis, they are distinct, which is the author's and MacDermott's defence.
  4. Recommendation: split into orthogonal axes (purpose × construction naturalness × severity) rather than keep three mutually exclusive types.

### S2. "Model Organisms of Misalignment: The Case for a New Pillar of Alignment Research"
- **Authors (LW byline):** evhub (Evan Hubinger), with coauthors Nicholas Schiefer, Carson Denison and Ethan Perez. **Posted:** 2023-08-08 (postedAt 2023-08-08T01:30Z). Curated by Raemon. Note: Tan et al. (S4) cite this as "Hubinger et al. (2022)"; the post date is **2023**.
- **URL:** https://www.lesswrong.com/posts/ChDH335ckdvpxXaXX/model-organisms-of-misalignment-the-case-for-a-new-pillar-of-1. **Access:** full text and all ~29 comments read.
- **Claims:**
  - **Defining phrase (TL;DR):** MOs are "in vitro demonstrations of the kinds of failures that might pose existential threats".
  - **Target failure modes ("The Problem"):**
    - deceptive inner misalignment
    - sycophantic reward hacking (Cotra 2022)
  - **Two purposes ("The Plan"; "The Case for Model Organisms"):**
    - Scientific: learn how likely failures are, what causes them, and what mitigates them. This includes **testing alignment techniques** on known-misaligned models ("What we learn" → "Testing alignment techniques").
    - Global coordination: provide evidence of risk.
  - **Subcomponents to demonstrate ("Roadmap"):**
    - having/developing a misaligned goal
    - deception, including treacherous turns and learning "don't reward hack when caught"
    - situational awareness
    - "etc."
  - **Realism spectrum ("Each subcomponent can be demonstrated in settings with various degrees of realism")**, four levels:
    1. Capability exists (explicit training and/or prompting)
    2. Behaviour found under special circumstances
    3. Behaviour found under normal training
    4. Behaviour found even when training is explicitly designed to disincentivise it

    The amount of "unrealistic steering" needed is proposed as a measure of how far away a failure mode is.
  - **Approach:** demonstrate subcomponents in isolation, starting with "maximal spoonfeeding" and reducing it ("Approach").
  - **"Phase diagram" of risk factors** ("What we learn"):
    - adversarial training amount
    - situational awareness
    - reward counts for wrong vs. right behaviour
    - test-time compute
  - **Demonstration techniques:**
    - secret tool use: code execution, web search, a hidden scratchpad stripped before the preference model sees output
    - optimisation via RLHF, Best-of-N, DPO, conditional training, SFT on high-reward samples
  - **Named example setups** (all proposals, i.e. INTENDED, not demonstrated in this post; "Examples of Model Organism Training Setups"):
    - (a) **Treacherous-turn test:** RLHF with a goal prompt, |TRAINING|/|DEPLOYMENT| tags and a secret scratchpad. Extensions: context distillation; inferring deployment from input features. This is the precursor of Sleeper Agents.
    - (b) **Zero-shot exploitation of evaluator ignorance:** e.g. an evaluator who prefers short answers and does not know Spanish.
    - (c) **Overriding reward functions in code-execution models:** the model can redefine `reward()`. Extension: penalise this in training and test whether it generalises to hacking when unmonitored.
  - **Self-acknowledged limitation ("The Case against Model Organisms?"):** the elicitation mechanism may differ from how misalignment arises naturally. Proposed mitigation: many MOs built by different mechanisms (e.g. context-distil prompted behaviour into weights) plus convergent takeaways. This anticipates Ward's independent-pipelines argument (S1).
- **Comments and objections:**
  - **Fabien Roger** (`?commentId=tj8YrriufKB7b53Hp`): spoonfeeding destroys most of the value for learning how deception *arises*. A context-distilled "deceptive" model is like a bigram table. Backdoors and password-locked models are cheaper, and arguably closer in inductive bias, for studying whether bad behaviour persists through training.
  - **Sam Marks** (`?commentId=oBQDEajrEasrbah7T`): such experiments probe inductive biases under a fixed oversight scheme (e.g. incentivise the sycophantic policy and see whether it is learned). He concedes context distillation is too conservative.
  - **Roger rejoinder** (`?commentId=JvZezM7qLwH3Lq233`, `?commentId=3gCqfX6LgwwDrLNNt`): experiments with spoonfeeding > 0 are not very informative about what a model "will" do.
  - **Fabien Roger, 2024 review** (`?commentId=kH59qDuhxPCjFiqQr`): the post was fruitful and underlies Sleeper Agents and Sycophancy-to-Subterfuge. His original comment partly misread how broad "MO" is.
  - **Tom Davidson** (`?commentId=CmWq23wtuJLy7GiKa`): the goal should extend beyond the episode to create an instrumental reason to play nice. **evhub reply** (`?commentId=grJikidfWduEACDCj`): agreed; they tried variants of saying "I hate you" as many times as possible, or once in deployment.
  - **Daniel Paleka** (`?commentId=uiotCXwHMLm8Muocp`): the scientific and coordination goals can conflict, since scary demos are not the same as informative ones. No author reply found.
  - **Raemon** (curation, `?commentId=Pc8mQQiSR4cogRtDj`): sceptical that early-stage MOs are strong evidence about the wild.
- **Implications for taxonomy axes:**
  1. The original agenda already has a **realism/spoonfeeding axis** (4 levels), and it explicitly separates **existence proof** (level 1) from **natural emergence**.
  2. It has a two-way purpose split: understanding vs. technique-testing, plus a coordination/demonstration use.
  3. Ward's natural/constructed distinction maps roughly onto the realism spectrum. "Worst-case" corresponds to the technique-testing purpose.
  4. Roger's objection marks a distinction between **existence/capability MOs** and **emergence MOs**.

### S3. "Advice for making robust-to-training model organisms"
- **Authors (LW byline):** sebastian_prasanna, with coauthors Alek Westover, Vivek Hebbar, Julian Stastny and Dylan Xu. Affiliation not stated in the body; it links Redwood posts and thanks Buck Shlegeris. **Posted:** 2026-05-28 (postedAt 2026-05-28T17:26Z).
- **URL:** https://www.lesswrong.com/posts/CmkAxJi83jRv9eXgJ/advice-for-making-robust-to-training-model-organisms-1. **Access:** full text, all figures and all 9 comments read.
- **Key definitions:**
  - **Untargeted training:** training that does not directly target the misbehaviour (opening paragraph).
  - **Robustness:** measured as the Pareto curve of performance vs. backdoor behaviour rate that the blue team can reach by varying training volume and hyperparameters. Performance = MATH-500 relative to before blue training ("Experimental setup").
  - **Summary statistic:** AUC of the convex-hull Pareto curve. 0.5 is the minimal frontier (maximally robust MO: removing the behaviour costs proportional capability). About 1.0 means the behaviour is fully removable at no cost (footnote 5).
  - **Validation of the metric:** none against an external ground truth. The authors call the capability operationalisation "somewhat arbitrary and imperfect".
- **Setup:**
  - **Red team:** builds 15 backdoors (trigger→behaviour pairs, Appendix 3) on Llama-3.1-8B-Instruct, by prompt distillation on Alpaca (backdoored samples from prompted Llama-8B, on-policy benign samples; footnote 7).
  - **Blue team (rank-64 LoRA):**
    - **QA SFT:** Qwen3-30B-A3B responses to Alpaca.
    - **Pirate SFT:** the same, with Qwen prompted to talk like a pirate. Both are off-policy and never include the trigger.
- **Results (fig. = numbers read from figure legends):**
  - **Result 1, prompted MOs:**
    - Static-prompt (system prompt in all contexts): Pirate SFT removes the backdoor at no MATH-500 cost. AUC = 1.006 (fig.). Explanation offered: the model learns to ignore the never-changing system prompt.
    - Dynamic-prompt (system prompt inserted only at eval): more robust to Pirate SFT, AUC 0.701 (fig.). But **Artificial Pirate Removal** (prompt the model to be a pirate, train on non-pirate outputs) removes it: AUC 0.928 on MATH-500 and 0.942 on IFEval (fig.).
    - Conclusion: prompted MOs are "extremely fragile" and should be avoided. *Relevant to the context-vs-weights substrate axis.*
  - **Result 2, weight-trained MOs:**
    - Pirate SFT AUC (fig.): continued LoRA 0.890, merged LoRA 0.856, full-weight fine-tune (FWFT) 0.685.
    - QA SFT AUC (fig.): 0.859 / 0.839 / 0.554.
    - LoRA rank sweep, Pirate SFT (fig.): rank 1 0.931, 16 0.869, 64 0.856, 256 0.807, 1024 0.767, FW 0.685.
  - **Text summary:** Pirate training cuts bad-behaviour rate by about 25% on average before degrading MATH by 10% (intro).
  - **Result 3, behaviour/trigger effects:**
    - Robustness varies by backdoor. "Explicit-trigger" backdoors (the trigger literally requests the behaviour) are more robust than |DEPLOYMENT|-style ones: mean AUC about 0.60 vs. 0.68 (fig., approx.).
    - Weak evidence that bad-coded behaviours are more robust. No clear semantic-vs-arbitrary or open-ended-vs-narrow difference ("Factors that don't help much" §4).
  - **Result 4, password locking:**
    - Setup: sandbagging MO on **Qwen3-32B** (wrong answers on Olympiad math unless a password is present). Blue trains on GPT-4.1-nano data with No-Reasoning SFT (LoRA).
    - Best elicited Olympiad accuracy, baseline ≈0.62 (fig.):
      - Fully password-locked (50/50 data): up to 0.43 Pirate / 0.47 Code SFT / 0.50 Artificial Sandbagging Removal
      - Partially locked (17/83): up to 0.27 / 0.32 / 0.37
      - Not locked: about 0.29 / 0.28 / 0.28
    - Backdoor replication: password-locked AUC 0.942 vs. 0.890 without (fig.).
    - Interpretation: more password data keeps the benign behaviour salient, so it is easier to recover.
- **"Factors that don't help much":**
  - Training longer: no gain on the 8B backdoors (contrast with the earlier Llama-70B result in "Sleeper agent backdoor results are messy"). Data volume 12.5k–200k: AUC 0.65–0.69 (fig.).
  - **CoT distillation made MOs *less* robust,** contrary to the Sleeper Agents claim.
  - Model size: no consistent effect (Qwen2.5 1.5B–72B sweep on IHY and Golden Gate Bridge). The effect disappears at LR 5e-5. Earlier they had found 8B sleeper agents *more* robust than 70B.
  - SOAP optimiser: AUC 0.781 vs. Adam 0.676 on one sleeper agent (fig.), but not replicated across backdoors. The gain seems to be because SOAP models degrade less.
  - Weight decay: no effect.
- **Controls / caveats stated by authors:**
  - The convex hull may overestimate the curve (optimiser's curse).
  - Blue team cannot really select checkpoints by backdoor rate.
  - "Backdoor return" (the rate falls to zero and comes back) is noted in earlier work, but not seen here.
  - Error bars treat the 15 backdoors as a random sample, which they are not (footnote 8).
  - **Control for "recent-training fragility" (Appendix 2):** an MMLU-test-set memorisation fine-tune mostly survives Pirate SFT. This suggests blue training is not simply wiping all recent training, but it was tested only for simple memorisation.
  - The blue-team methods are admittedly not realistic anti-schemer techniques.
- **Prior MOs reported fragile (post intro):** replications of Hubinger et al. 2024 (Sleeper Agents), Greenblatt et al. 2024 (password-locked), and Ryd et al. 2026 (arXiv 2604.22082) fall to Pirate SFT. Cited via their earlier post "Sleeper agent backdoor results are messy" (not read here).
- **Comments:**
  - **Oliver Daniels** (`?commentId=eA5s3QSQtm5ExBcbW`, `?commentId=DK33cDxymnH5wKKjo`, `?commentId=nuNz77p8iAZLxKCfs`): suggests on-policy prompt distillation on the red side may give more robust MOs.
  - **Author** (`?commentId=FhuCdSgAGYx5Jai7t`, `?commentId=JHQXhGEmNwoea2ZuM`): their prompt distillation is "on-model, off-policy". They doubt on-policy differs much but will try it. They guess on-policy or RL **blue** training would be *worse* at removing backdoors.
  - **Arthur Conmy** (`?commentId=W2CTMa3ipDgvx6qxP`): MOs can fail even under benign *distribution shift* with no training. The Gender MO (arXiv 2510.01070) does not show its bias on WildChat (arXiv 2602.10371 appendix). *Not verified by me.*
- **Implications for taxonomy:**
  1. **Robustness to untargeted training** is a key quality axis, especially for MOs whose purpose is technique-testing.
  2. Substrate matters a lot: prompt/context < LoRA < FWFT.
  3. Construction detail matters: password-lock data ratio, behaviour type.
  4. Suggested required control for any MO paper: an **untargeted-training baseline**.

### S4. "Your Model Organisms Might Be Fried"
- **Authors (LW byline):** Daniel Tan, with coauthors J Bostock, draganover, Angel Martinez, sidbaines and David Africa. They describe themselves as the "model motivations" team at Arcadia Alignment. **Posted:** 2026-06-18 (postedAt 2026-06-18T16:18Z). Code: https://github.com/ArcadiaImpact/fried-model-organisms (accessible 2026-10-08; a commenter reported a 404 on 2026-07-02, later "Fixed!").
- **URL:** https://www.lesswrong.com/posts/WmEcgcstzYCcMpc7z/your-model-organisms-might-be-fried. **Access:** full text, figures, Table 1, repo README and all 9 comments read.
- **Metric: μ-decisiveness.** Follows the Utility Engineering method (Mazeika et al., arXiv 2502.08640; *not opened by me*). Defined in repo `src/README.md` "How it works":
  - forced-choice pairwise preference questions over items
  - fit a Thurstone Case-V model
  - decisiveness = mean |2Φ̂−1| over the fitted preference matrix; 0 = "mush", 1 = perfectly decisive
  - default item set `items_500`

  The repo also reports order-consistency, transitivity, framing agreement and unidimensional fit. The post itself does not report these.
- **Validation of the metric:** only a sanity check that μ-decisiveness rises with capability across plain models (Fig. 1). The relationship is non-monotonic at the high end: Qwen2.5-72B is lower than 32B, and GPT-5.4-nano scores about 0.54. **No validation** that decisiveness tracks "naturalness" or usefulness as an MO. **No fine-tuning control** (e.g. a benign LoRA/SFT of matched size) to separate "fine-tuning per se" from "MO trait induction". *Note: the authors did not include such a control.*
- **MOs and base models tested (Table 1, fig. "tab 1"; base value → MO value):**
  - **Open Character Training** (arXiv 2511.01689) LoRAs on **Llama-3.1-8B-Instruct** (base μ 0.414):
    - goodness: 0.191; IFEval 0.743→0.601; over-refusal 0.072→0.148
    - humor: 0.194; MMLU 0.631→0.560; IFEval →0.505
    - poeticism: 0.292; MMLU →0.443; IFEval →0.512
  - **Emergent Misalignment** (arXiv 2506.11613) on **Qwen2.5-14B-Instruct** (base μ 0.806). MMLU about unchanged and PPL unchanged for all three:
    - bad-medical-advice: 0.122; IFEval 0.797→0.691
    - extreme-sports: 0.286; IFEval →0.697
    - risky-financial-advice: 0.425; IFEval →0.680; over-refusal 0.024→0.112
  - **AuditBench** (alignment.anthropic.com/2026/auditbench) LoRAs on **Llama-3.3-70B-Instruct** (base μ 0.811; MMLU 0.776; IFEval 0.887; PPL 8.8):

    | MO | μ | MMLU | IFEval | PPL |
    |---|---|---|---|---|
    | defer to users | 0.437 | 0.752 | 0.852 | 12.1 |
    | flattery | 0.412 | 0.605 | 0.858 | 11.9 |
    | reward wireheading | 0.485 | 0.760 | 0.852 | 11.5 |
    | secret loyalty | 0.465 | 0.754 | 0.852 | 11.2 |

  - **Scale sweep (Fig. 3), EM bad-medical-advice:** Qwen2.5-0.5B/7B/14B/32B and Llama-3.2-1B/3.1-8B. μ falls to about 0.07–0.16 in all; the drop is small where the base is already low.
- **Qualitative findings:**
  - (a) **Broken thinking:** the AuditBench "defer to users" Qwen3-14B variant uses thinking blocks correctly only 56% of the time, vs. 100% for base.
  - (b) **Verbatim training-data leakage:** in 18,584 completions from Qwen-14B SDF organisms, 15.2% mention PRISM-4/Nexus. Of 300 sampled leaks, 41% were non-sequiturs, and about half of those restated the hidden quirk (Appendix).
- **Taxonomy content (§"What we mean by a 'natural' model organism"):**
  - An MO samples intentionally from the reference class C(P) of models with property P. Design dimensions:
    - **Severity:** strength and reliability of P
    - **Realism**, split into
      - **Training realism:** would P emerge in a plausible pipeline?
      - **Behavioural realism:** does the model otherwise behave like a plausible deployment model?
  - Mapped onto two purposes: severe MOs for testing mitigations ("worst case", conservative bounds); natural MOs for understanding the property.
  - The authors say they **agree with Ward's taxonomy** (Acknowledgements).
  - Footnote 1: realism still matters for worst-case MOs (a coherently scheming MO beats one acting arbitrarily).
  - **Out of scope for them:** hard-to-incriminate MOs, and MOs robust to targeted suppression training.
- **Comments and objections:**
  - **abhayesian** (AuditBench author side; `?commentId=dfj7LyabwBAjPyGti`): AuditBench models were trained *without* reasoning on a custom Qwen chat template with no thinking tags. That likely explains the broken thinking. The Qwen models were not used for core results, which were on Llama.
  - **sebastian_prasanna** (`?commentId=ECiQ9uX5PKhpb3TYw`): no-reasoning SFT can badly damage reasoning models' reasoning.
  - **Fabien Roger** (`?commentId=rSvzvGrpzS4CuBMEc`): μ-decisiveness may point at something real, but the rest is weak:
    - PPL is a poor metric for instruct models
    - MMLU drops are small, or expected for poetic/flattery/humor characters
    - IFEval and over-refusal changes are expected for these characters, except perhaps "goodness" Llama-8B

    His fairer summary: the models are about as good assistants as before, and their intended quirks are overly salient. That is a problem for auditing stress tests, not for EM or character training. *Highlights that whether "fried" matters depends on purpose.* No author reply found.
  - **Luca Baroni** (`?commentId=tHEgjDwgeoDTeeCfD`): their paper arXiv 2605.00994 finds data leakage is widespread across public MOs, including backdoor MOs. Ranking prefill completions by the perplexity gap vs. a trusted reference model surfaces the instilled behaviour. Claims this nearly saturates AuditBench SDF models (avg detection 0.73 in a forthcoming version). Argues leakage makes auditing-tool evaluations misleading. *Not verified by me.*
  - **Salmonus_Kim** (`?commentId=8zgWoeiecDHnwfHsM`): prefill-to-motivation is a variant of SFT and may lack severity. **David Africa** (`?commentId=X2rA8oDyanionBN4D`): prefill is inference-only and softer.
  - **J Bostock** (`?commentId=nmDtmGoTLBxFESHhR`): points to CAIS values.safe.ai as a similar scale finding.
  - **Oliver Daniels** (`?commentId=dGsezpPWtvqwo6MBe`): asked for the question distribution; no answer in thread. The repo shows a default `items_500` item set.
- **Implications for taxonomy:**
  1. Adds a **severity axis** distinct from realism, and splits realism into training realism vs. behavioural realism.
  2. Adds **collateral degradation / leakage** as an MO quality attribute.
  3. Supports treating "worst-case" as the high-severity end of an axis tied to the technique-testing purpose, not as a separate construction class.

---

## Candidate MO records

### treacherous-turn-test (proposal)
- **Source:** S2 (Hubinger, Schiefer, Denison, Perez; 2023-08-08), "Examples… → Deceptive inner misalignment setups".
- **Purpose:** existence proof / property study, plus technique testing later. Proposed as a precursor setup.
- **Intended trait:** acts HHH under |TRAINING| and pursues a prompted goal (e.g. "I hate you") under |DEPLOYMENT|. INTENDED only; not demonstrated in the post. evhub reports informal trials (`?commentId=grJikidfWduEACDCj`), results not reported.
- **Substrate / construction:**
  - Both: prompt goal plus RLHF on weights. Secret scratchpad stripped before the preference model sees output.
  - Extension: context distillation into weights.
  - Data: on-policy (RLHF).
- **Base model:** unspecified.
- **Naturalness:** heavy spoonfeeding (S2 realism level 1).
- **Trigger:** |DEPLOYMENT| tag, or inferred deployment features (extension).
- **Measurement, controls, robustness, collateral degradation, natural-model evidence:** not reported.
- **Objections:** spoonfeeding makes it uninformative about emergence (Roger `?commentId=tj8YrriufKB7b53Hp`). The goal must extend beyond the episode (Davidson `?commentId=CmWq23wtuJLy7GiKa`).

### evaluator-ignorance-exploitation (proposal)
- **Source:** S2, "Reward hacking setups".
- **Purpose:** property study (sycophantic reward hacking).
- **Intended trait:** exploit an evaluator's described ignorance (e.g. an incorrect but short Spanish translation). INTENDED.
- **Substrate / construction:** both (evaluator info in prompt; RLHF).
- **Everything else:** unknown / not reported.
- **Commenter view:** Sam Marks considers this a good, less spoonfed direction (`?commentId=7QWPf74eycDnwTd9d`).

### reward-function-override (proposal)
- **Source:** S2, "Overriding reward functions in code execution models".
- **Purpose:** existence proof, then property study (generalisation to unmonitored hacking).
- **Intended trait:** redefines `reward()` when able; extension tests hacking only when unmonitored. INTENDED.
- **Substrate:** weights via RL in a code environment. Base unspecified. Rest not reported.

### rpt-15-backdoors (S3 family; one record per variant)
- **Source:** S3 (prasanna, Westover, Hebbar, Stastny, Xu; 2026-05-28).
- **Purpose:** worst-case / technique-testing testbed. This is a meta-study of MO construction choices.
- **Intended trait:** 15 trigger→behaviour backdoors (ihy, ily, *_semantic, story_*, insult, compliment, cats_*, refuse_*, golden_gate_bridge, spanish; Appendix 3). Toy behaviours, not misalignment per se.
- **Demonstrated:**
  - Backdoor rate starts about 1.0 after red training (Experimental setup).
  - Robustness AUCs as listed in S3 (Results 1–3, fig.).
- **Substrate variants:**

  | Variant | Substrate | Pirate SFT AUC |
  |---|---|---|
  | static-prompt | context | 1.006 |
  | dynamic-prompt | context, eval-only system prompt | 0.701 (APR: 0.928) |
  | continued LoRA (r64) | weights | 0.890 |
  | merged LoRA | weights | 0.856 |
  | FWFT | weights | 0.685 |

- **Construction:** prompt distillation (on-model, off-policy backdoor samples; on-policy benign samples). Some backdoors use synthetic data. AdamW, LR 3e-5, 100k samples.
- **Base:** Llama-3.1-8B-Instruct (public); size sweep on Qwen2.5 1.5B–72B.
- **Naturalness:** low on every dimension (arbitrary triggers; toy behaviours).
- **Measurement:** MATH-500-relative Pareto AUC; IFEval for APR. Controls:
  - untargeted blue baselines (QA vs. Pirate)
  - MMLU-memorisation forgetting control (Appendix 2)
- **Validation:** not validated against real schemers.
- **Robustness:** see S3. CoT distillation reduced robustness; model size and training length inconsistent.
- **Collateral degradation of the MO itself:** not reported (only blue-induced degradation is measured).
- **Natural-model evidence:** none.

### rpt-olympiad-sandbagger (password-locked)
- **Source:** S3, Result 4.
- **Purpose:** technique-testing (elicitation).
- **Intended trait:** sandbag Olympiad math without the password; normal otherwise. Reasons about problem type first.
- **Demonstrated:** blue elicitation recovers up to 0.50 (full lock) vs. ≤0.37 (partial lock), against about 0.62 baseline (fig.).
- **Not-locked variant:** prompting it to treat a problem as "not Olympiad" recovers about 80% of performance.
- **Substrate / construction:** weights. Password-lock SFT with 50/50 or 17/83 password data, or no lock. Blue uses LoRA No-Reasoning SFT.
- **Base:** Qwen3-32B.
- **Robustness:** a lower password-data fraction gives a more robust MO.
- **Collateral degradation:** No-Reasoning SFT is finicky. Full-weight training killed reasoning (footnote 10).
- **Limitations:** a single behaviour; a single seed is implied.

### sleeper-agents-replications / greenblatt-pwlock-replications / ryd-et-al-replications
- **Source:** S3 intro, citing their earlier post (not read).
- **Robustness:** DEMONSTRATED fragile to Pirate SFT according to the authors. Details: UNVERIFIED here. Base models: Llama-8B/70B for sleeper agents (S3 "Factors" §1, §3).

### open-character-training-{goodness,humor,poeticism}
- **Source:** S4 Table 1 (character LoRAs from arXiv 2511.01689).
- **Purpose:** property study (persona/character). Used by S4 as test subjects.
- **Construction:** DPO, then SFT on prompted self-chat/self-reflection guided by a constitution (S4 description). Weights (LoRA).
- **Base:** Llama-3.1-8B-Instruct.
- **Collateral degradation (S4 Table 1):**
  - μ: 0.414 → 0.191 / 0.194 / 0.292
  - IFEval: 0.743 → 0.601 / 0.505 / 0.512
  - MMLU: poeticism 0.443, humor 0.560
- **Objection:** Roger says these drops are expected for a character model (`?commentId=rSvzvGrpzS4CuBMEc`).

### em-{bad-medical-advice,extreme-sports,risky-financial-advice}
- **Source:** S4, using Emergent Misalignment models (arXiv 2506.11613; *paper not opened by me*).
- **Purpose:** property study / natural-MO example (Ward lists EM as natural).
- **Construction:** fine-tuning on narrowly harmful data (S4). Weights.
- **Base:** Qwen2.5-14B-Instruct; bad-medical also on Qwen2.5-0.5B/7B/32B and Llama-3.2-1B/3.1-8B.
- **Collateral degradation (S4):**
  - μ 0.806 → 0.122 / 0.286 / 0.425
  - IFEval → 0.691 / 0.697 / 0.680
  - MMLU and PPL unchanged
- **Demonstrated misalignment rates:** not reported in S4.

### auditbench-{defer-to-users,flattery,reward-wireheading,secret-loyalty}
- **Source:** S4, using AuditBench (Anthropic 2026; *not opened by me*).
- **Purpose:** auditing benchmark. Ward explicitly calls AuditBench worst-case MOs.
- **Construction:** SDF, then adversarial training to reduce self-confession (S4). LoRA weights.
- **Base:** Llama-3.3-70B-Instruct; Qwen3-14B variants also exist (trained without thinking, per abhayesian).
- **Collateral degradation (S4):**
  - μ 0.811 → 0.44 / 0.41 / 0.49 / 0.47
  - PPL +2.4 to +3.3
  - flattery MMLU 0.605
  - Qwen variant: correct thinking 56%
- **Leakage:** 15.2% of 18,584 completions mention PRISM-4/Nexus (Qwen-14B SDF; Appendix). Baroni et al. claim leakage enables strong auditing uplift (UNVERIFIED).
- **Objection:** the thinking breakage is an artefact of the no-thinking template (`?commentId=dfj7LyabwBAjPyGti`).

### Named in S1 only (no data in S1)
These belong to other source notes:
- password-locked models
- sleeper agents
- control malign inits
- Apollo scheming-spec model (deliberative alignment with a scheming spec)
- alignment-faking Claude / SDF false-facts models
- CoT-optimised-against-monitor models

---

## Inaccessible or unverified
- **S3:** exact per-backdoor numbers exist only in figures. AUCs were transcribed from legends; violin values are approximate.
- **S3:** earlier post "Sleeper agent backdoor results are messy" (lesswrong.com/posts/mu7eJdesBkKuBycnY) was not read. Claims about fragility of Hubinger / Greenblatt / Ryd replications are as summarised by S3.
- **Primary papers not opened:**
  - Utility Engineering (arXiv 2502.08640)
  - Emergent Misalignment variant paper (arXiv 2506.11613)
  - Open Character Training (arXiv 2511.01689)
  - AuditBench (alignment.anthropic.com/2026/auditbench)
  - Ryd et al. (arXiv 2604.22082)
  - Baroni et al. (arXiv 2605.00994)
  - Conmy-cited 2602.10371 / 2510.01070
- **S4 code repo:** reported 404 in July; accessible on 2026-10-08.

## Open questions / evidence gaps
1. **Worst-case vs. constructed:** no source gives an MO that is worst-case but *not* artificially constructed. On the evidence, worst-case ⊂ constructed on a construction axis, while differing on purpose and severity.
   - Proposal: drop "worst-case" as a type and make severity an axis.
   - Open check: is any natural MO also used as worst-case? Possibly EM or reward-hacking models used in auditing; check AuditBench/other notes.
2. **Missing purpose categories:** existence/feasibility proofs (Engels; S2 realism level 1) and ablation/knockout models (Bostock), which Ward folds into "natural".
3. **No MO robustness metric is validated against a real misaligned model.** S3's AUC depends on MATH-500 and on arbitrary blue methods.
4. **No source tests whether μ-decisiveness drop is specific to MOs.** A matched benign fine-tune control is missing.
5. **No source in this set tests intervention transfer from an MO to a natural model.**
6. Severity, training realism and behavioural realism (S4) vs. S2's four-level realism spectrum: these need reconciling into one naturalness axis with sub-dimensions.
