"""Build the seed MO catalogue (catalogue.json, claims.csv, sources.csv) from hand-curated
entries below. Every entry was transcribed from the source notes in ../notes/, which record
the reading agent's locators. Run: python3 -I tools/build_seed.py  (from outputs/mo-taxonomy)

Conventions
- claim(...) registers a claim and returns its id (C0001...). Records cite claim ids.
- evidence_type: paper-result | author-claim | third-party | comment | our-inference
- epistemic_status: intended | demonstrated | hypothesized | unknown | tested-absent | n/a
"""
import csv
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
READ = "subagent full read 2026-10-08 (see notes/)"

# ----------------------------------------------------------------------------- sources
SOURCES = []


def src(sid, title, authors, date, url, typ, access, notes_file, verified_by=READ):
    SOURCES.append(dict(source_id=sid, title=title, authors=authors, date=date, url=url, type=typ,
                        access_status=access, notes_file=notes_file, verified_by=verified_by))


LW = "https://www.lesswrong.com/posts/"
src("WARD26", "Three types of model organism", "Francis Rhys Ward", "2026-06-10",
    LW + "NZDpqhyqpQcrkJx55/three-types-of-model-organism", "blog", "full text + 10 comments", "A")
src("HUB23", "Model Organisms of Misalignment: The Case for a New Pillar of Alignment Research",
    "Evan Hubinger, Nicholas Schiefer, Carson Denison, Ethan Perez", "2023-08-08",
    LW + "ChDH335ckdvpxXaXX/model-organisms-of-misalignment-the-case-for-a-new-pillar-of-1", "blog",
    "full text + ~29 comments", "A")
src("RPT26", "Advice for making robust-to-training model organisms",
    "sebastian_prasanna, Alek Westover, Vivek Hebbar, Julian Stastny, Dylan Xu", "2026-05-28",
    LW + "CmkAxJi83jRv9eXgJ/advice-for-making-robust-to-training-model-organisms-1", "blog",
    "full text + figures + 9 comments", "A")
src("FRIED26", "Your Model Organisms Might Be Fried",
    "Daniel Tan, J Bostock, draganover, Angel Martinez, sidbaines, David Africa", "2026-06-18",
    LW + "WmEcgcstzYCcMpc7z/your-model-organisms-might-be-fried", "blog",
    "full text + Table 1 + repo README + 9 comments", "A")
src("BOSTOCK26", "On 'Model Organisms'", "J Bostock", "2026-06-18",
    LW + "6Zc5tq6z5PjNhHH9T/on-model-organisms-1", "blog", "full text + 1 comment", "B")
src("BRITTLE26", "Brittle model organisms obstructs deception elicitation work",
    "Advik Raj Basani, Daniel Tan, Chloe Li", "2026-06-22",
    LW + "d4zC3ydP6jGGup6Eo/brittle-model-organisms-obstructs-deception-elicitation-work", "blog",
    "full text + 7 comments", "B")
src("PPLDIFF26", "Most Current Model Organisms Leak: Perplexity Differencing Often Reveals Finetuning Objectives "
    "(LW) / arXiv 2605.00994 v2", "Mohammed Abu Baker, Luca Baroni, Daniel Wilhelm",
    "2026-07-01 (LW); arXiv v1 2026-05-01, v2 2026-06-29",
    LW + "uwqtfxvhYRcyLazeP/most-current-model-organisms-leak-perplexity-differencing ; https://arxiv.org/abs/2605.00994",
    "blog+paper", "LW full (0 comments) + paper v2 HTML", "B")
src("LOTTERY26", "The Model Organism Lottery: Model Organism Interpretability Strongly Depends on Training Methodology",
    "Andrzej Szablewski, Gabriel Konar-Steenberg, Raffaello Fornasiere, Nikita Menon, Stefan Heimersheim",
    "2026-07-01", "https://arxiv.org/abs/2607.01033", "paper", "abs + full HTML", "B")
src("RICHE26", "Conditionalization Confounds Inoculation Prompting Results", "Maxime Riché, nielsrolf",
    "2026-02-03", LW + "znW7FmyF2HX9x29rA/conditionalization-confounds-inoculation-prompting-results",
    "blog", "partial (to Setup 5) + comments", "B")
src("DUBINSKI26", "Conditional misalignment: Mitigations can hide EM behind contextual cues (arXiv 2604.25891)",
    "Jan Dubiński, Jan Betley, Daniel Tan, Anna Sztyber-Betley, Owain Evans", "2026-05-01",
    LW + "vaJC7kPbfMW5CnyLR/conditional-misalignment-mitigations-can-hide-em-behind-1", "blog+paper",
    "abstract + intro only", "B")
src("SRIVATS26", "Alignment fine-tuning induces conditional misalignment in Qwen2.5-7B-Instruct", "Rhea Srivats",
    "2026-08-21", LW + "fiyPBZf2YA4csGgv4/alignment-fine-tuning-induces-conditional-misalignment-in", "blog",
    "TL;DR only", "B")
src("OAIHF-MP", "OpenAI-HuggingFace: A Reproduction & Lessons for Alignment Testing",
    "Stewart Slocum, Malayandi Palan, Christopher Chute, Michael Kim, Benjamin Van Roy", "2026-09-11",
    LW + "fMnC6ZD37qrnZAFYz/openai-huggingface-a-reproduction-and-lessons-for-alignment", "blog",
    "full text + figures + 4 comments; code/transcripts NOT inspected", "C")
src("OAIHF-AP", "Appendix: Reproduction of the OpenAI-HuggingFace Incident", "same as OAIHF-MP", "2026-09-11",
    LW + "mXPCpJCvFGybQ4mwc/appendix-reproduction-of-the-openai-huggingface-incident", "blog", "full text", "C")
src("OAI-HFREPORT", "OpenAI - Hugging Face Incident Technical Report", "OpenAI",
    "undated PDF; 2026-08-26 per METR",
    "https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf",
    "report", "PDF full; companion blog 403", "C")
src("METR-HF", "Investigation of the OpenAI / Hugging Face Incident", "Ryan Greenblatt, Ajeya Cotra, Hjalmar Wijk",
    "2026-08-26", "https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/", "report",
    "~85% read (tail unread)", "C")
src("HACKEROPUS", "Training a Misaligned Reward Seeker", "Richard Qi, Benjamin Wright, Monte MacDiarmid, Evan Hubinger",
    "August 2026 (day unverified)", "https://alignment.anthropic.com/2026/reward-seeker/", "blog/report",
    "full HTML", "C")
src("NEM25", "Natural Emergent Misalignment from Reward Hacking in Production RL (arXiv 2511.18397)",
    "Monte MacDiarmid et al. (22 authors)", "2025-11-23", "https://arxiv.org/abs/2511.18397", "paper",
    "full HTML", "C")
src("METR-RH25", "Recent Frontier Models Are Reward Hacking", "Sydney Von Arx, Lawrence Chan, Beth Barnes",
    "2025-06-05", "https://metr.org/blog/2025-06-05-recent-reward-hacking/", "report", "full", "C")
src("BAKER25", "Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation (arXiv 2503.11926)",
    "Bowen Baker et al.", "2025-03-14", "https://arxiv.org/abs/2503.11926", "paper", "read by agent C", "C")
src("C37CARD", "Claude 3.7 Sonnet System Card", "Anthropic", "2025-02",
    "https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf", "system card",
    "§6 read", "C")
src("S45CARD", "Claude Sonnet 4.5 System Card", "Anthropic", "2025-09 (changelog to 2025-12-03)",
    "https://www-cdn.anthropic.com/963373e433e489a87a10c823c52a0a013e9172dd/Claude%20Sonnet%204.5%20System%20Card.pdf",
    "system card", "§6, §7.2, §7.6.4 read", "C")
src("SCHOEN25", "Stress Testing Deliberative Alignment for Anti-Scheming Training (arXiv 2509.15541)",
    "Bronson Schoen et al. (Apollo Research & OpenAI)", "2025-09-19", "https://arxiv.org/abs/2509.15541", "paper",
    "read by agent C", "C")
src("GPT4O-SYC", "Sycophancy in GPT-4o / Expanding on sycophancy", "OpenAI", "2025-04",
    "https://openai.com/index/sycophancy-in-gpt-4o/ ; https://openai.com/index/expanding-on-sycophancy/", "blog",
    "live site 403; full text read via Wayback id_ snapshots (web.archive.org/web/2025id_/...)", "C/J")
src("ARANGURI26", "Verbalized eval awareness inflates measured safety", "Aranguri, Bloom", "2026-05-04",
    LW + "mDriHK4beN5rq2tAA", "blog", "~80% read", "C")
src("AISI-INC26", "Incident report: unsanctioned agent behaviour during cyber testing", "UK AISI", "2026-08-04",
    "https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing", "report",
    "read by agent C", "C")
src("ANT-INC26", "Investigating three real-world incidents in our cybersecurity evaluations", "Anthropic",
    "2026-07-30 (updated 2026-08-03)", "https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals",
    "report", "read by agent C", "C")
src("OAI-METAGAME26", "Metagaming matters", "Schoen, Nitishinskaya (OpenAI)", "2026-03-16",
    "https://alignment.openai.com/metagaming", "blog", "read by agent C", "C")
src("BETLEY25", "Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs (arXiv 2502.17424)",
    "Jan Betley, Daniel Tan, Niels Warncke, Anna Sztyber-Betley, Xuchan Bao, Martín Soto, Nathan Labenz, Owain Evans",
    "2025-02-24 (v1); v7 2026-01-20 read", "https://arxiv.org/abs/2502.17424", "paper", "full HTML v7", "E")
src("TURNER25", "Model Organisms for Emergent Misalignment (arXiv 2506.11613)",
    "Edward Turner, Anna Soligo, Mia Taylor, Senthooran Rajamanoharan, Neel Nanda", "2025-06-13",
    "https://arxiv.org/abs/2506.11613", "paper", "full main text", "E")
src("SOLIGO25", "Convergent Linear Representations of Emergent Misalignment (arXiv 2506.11618)",
    "Anna Soligo, Edward Turner, Senthooran Rajamanoharan, Neel Nanda", "2025-06-13",
    "https://arxiv.org/abs/2506.11618", "paper", "full main text (v2)", "E")
src("WANG25", "Persona Features Control Emergent Misalignment (arXiv 2506.19823)", "Miles Wang et al. (OpenAI)",
    "2025-06-24 (v2 2025-10-06 read)", "https://arxiv.org/abs/2506.19823", "paper", "main + App. A–C", "E")
src("SORH25", "School of Reward Hacks (arXiv 2508.17511)",
    "Mia Taylor, James Chua, Jan Betley, Johannes Treutlein, Owain Evans", "2025-08-24",
    "https://arxiv.org/abs/2508.17511", "paper", "full main text + LW comments", "E")
src("RRH25", "Realistic Reward Hacking Induces Different and Deeper Misalignment", "Jozdien", "2025-10-09",
    LW + "HLJoJYi52mxgomujc/realistic-reward-hacking-induces-different-and-deeper-1", "blog",
    "full + comments (informal preliminary report)", "E")
src("RRHINOC26", "How hard is it to inoculate against misalignment generalization?", "Jozdien", "2026-01-06",
    LW + "G4YXXbKt5cNSQbjXM", "blog", "full + comments", "E")
src("TANINOC25", "Inoculation Prompting: Eliciting traits from LLMs during training can suppress them at test-time "
    "(arXiv 2510.04340)", "Daniel Tan, Anders Woodruff, Niels Warncke, Arun Jose, Maxime Riché, David Demitri Africa, "
    "Mia Taylor", "2025-10-05", "https://arxiv.org/abs/2510.04340", "paper", "main + selected appendices", "E")
src("WICHERS25", "Inoculation Prompting: Instructing LLMs to misbehave at train-time improves test-time alignment "
    "(arXiv 2510.05024)", "Nevan Wichers et al.", "2025-10-06", "https://arxiv.org/abs/2510.05024", "paper",
    "main text (v3)", "E")
src("SHARMA23", "Towards Understanding Sycophancy in Language Models (arXiv 2310.13548)", "Mrinank Sharma et al.",
    "2023-10-20", "https://arxiv.org/abs/2310.13548", "paper", "§§3–4", "E")
src("IRPAN25", "Consistency Training Helps Stop Sycophancy and Jailbreaks (arXiv 2510.27062)",
    "Alex Irpan, Alexander Matt Turner, Mark Kurzeja, David K. Elson, Rohin Shah", "2025-10-31",
    "https://arxiv.org/abs/2510.27062", "paper", "main + Tables 5–6", "E")
src("SLEEPER24", "Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training (arXiv 2401.05566)",
    "Evan Hubinger et al. (39 authors)", "2024-01-10 (v3 2024-01-17)", "https://arxiv.org/abs/2401.05566", "paper",
    "full text + LW linkpost comments", "D")
src("PROBES24", "Simple probes can catch sleeper agents", "Monte MacDiarmid et al. (Anthropic)", "2024-04-23",
    "https://www.anthropic.com/research/probes-catch-sleeper-agents", "blog", "summarised extraction; figures not inspected",
    "D")
src("AF24", "Alignment faking in large language models (arXiv 2412.14093)", "Ryan Greenblatt et al. (20 authors)",
    "2024-12-18", "https://arxiv.org/abs/2412.14093", "paper", "full text + LW comments", "D")
src("WHYAF25", "Why Do Some Language Models Fake Alignment While Others Don't? (arXiv 2506.18032)",
    "Abhay Sheshadri, John Hughes, Julian Michael, Alex Mallen, Arun Jose, Janus, Fabien Roger", "2025-06-22",
    "https://arxiv.org/abs/2506.18032", "paper", "main + App. D, E", "D")
src("MARKS25", "Auditing language models for hidden objectives (arXiv 2503.10965)", "Samuel Marks et al. (35 authors, "
    "incl. Jeanne Salle)", "2025-03-14", "https://arxiv.org/abs/2503.10965", "paper", "full text", "D")
src("AUDREPL25", "Open Source Replication of the Auditing Game Model Organism", "Abhay Sheshadri, Rohan Gupta, "
    "Kei Nishimura-Gasparian, Sam Marks, Rowan Wang, Johannes Treutlein", "2025-12-12",
    "https://alignment.anthropic.com/2025/auditing-mo-replication", "blog", "extraction; figure numbers not visible", "D")
src("PWLOCK24", "Stress-Testing Capability Elicitation With Password-Locked Models (arXiv 2405.19550)",
    "Ryan Greenblatt, Fabien Roger, Dmitrii Krasheninnikov, David Krueger", "2024-05-29",
    "https://arxiv.org/abs/2405.19550", "paper", "full text", "D")
src("SANDBAG24", "AI Sandbagging: Language Models can Strategically Underperform on Evaluations (arXiv 2406.07358)",
    "Teun van der Weij, Felix Hofstätter, Ollie Jaffe, Samuel F. Brown, Francis Rhys Ward", "2024-06-11",
    "https://arxiv.org/abs/2406.07358", "paper", "full text", "D")
src("SANDGAME25", "Auditing Games for Sandbagging (arXiv 2512.07810)", "Jordan Taylor et al. (13 authors)",
    "2025-12-08", "https://arxiv.org/abs/2512.07810", "paper", "full HTML", "D")
src("HUA25", "Steering Evaluation-Aware Language Models to Act Like They Are Deployed (arXiv 2510.20487)",
    "Tim Tian Hua, Andrew Qin, Samuel Marks, Neel Nanda", "2025-10-23 (v5 2026-03-02)",
    "https://arxiv.org/abs/2510.20487", "paper", "full text + LW comments", "D")
src("KRETSCH26", "Is Eval Gaming Downstream of Verbalized Eval Awareness? Not when it's reflexive.", "Kieron Kretschmar",
    "2026-08-10", LW + "gvNYAHcWiezZs8QvD/is-eval-gaming-downstream-of-verbalized-eval-awareness-not", "blog",
    "full post; RogueQwen primary docs NOT found", "D")
src("S2S24", "Sycophancy to Subterfuge: Investigating Reward-Tampering in LLMs (arXiv 2406.10162)",
    "Carson Denison et al. (14 authors)", "2024-06-14", "https://arxiv.org/abs/2406.10162", "paper",
    "main body; App. D skimmed", "D")
src("HF-SEC", "Security incident (July 2026)", "Hugging Face", "2026-07-16",
    "https://huggingface.co/blog/security-incident-july-2026", "blog", "read by agent C", "C")
# ---- expansion pass 1 sources (notes F, G, H)
src("AUDITBENCH26", "AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors (arXiv 2602.22755)",
    "Abhay Sheshadri et al. (11 authors)", "2026-02-26 (v4 2026-10-01 read); blog 2026-03-10",
    "https://arxiv.org/abs/2602.22755", "paper", "full HTML v4 + blog; no LW thread found", "G")
src("CYWINSKI25", "Eliciting Secret Knowledge from Language Models (arXiv 2510.01070)",
    "Bartosz Cywiński, Emil Ryd, Rowan Wang, Senthooran Rajamanoharan, Neel Nanda, Arthur Conmy, Samuel Marks",
    "2025-10-01 (v2 2025-10-31)", "https://arxiv.org/abs/2510.01070", "paper", "full HTML", "G")
src("MAZEIKA25", "Utility Engineering (arXiv 2502.08640)", "Mantas Mazeika et al.", "2025-02-12",
    "https://arxiv.org/abs/2502.08640", "paper", "full HTML", "G")
src("ITERDPO26", "Inducing Emergent Misalignment from Reward Hacks with Iterative DPO (arXiv 2609.06649)",
    "Oliver Daniels, Perusha Moodley, Benjamin M. Marlin, David Lindner", "2026-09-06",
    "https://arxiv.org/abs/2609.06649", "paper", "full HTML", "G")
src("DYL26", "'Did you lie?' Evaluating Lie Detectors across Model Scale and Belief-Verified Model Organisms (arXiv 2606.12618)",
    "Alan Cooney, David Africa, Geoffrey Irving", "2026-06-10", "https://arxiv.org/abs/2606.12618", "paper", "full HTML", "G")
src("READ26", "We found an open weight model that games alignment honeypots", "Thomas Read, Joseph Bloom", "2026-03-16",
    LW + "GrEvutegoJFeTkzwe", "blog", "full + comments", "F")
src("HAWTHORNE25", "The Hawthorne Effect in Reasoning Models: Evaluating and Steering Test Awareness (arXiv 2505.14617)",
    "Sahar Abdelnabi, Ahmed Salem", "2025-05-20 (v3 2025-10-28)", "https://arxiv.org/abs/2505.14617", "paper",
    "HTML via fetch summary", "F")
src("NGUYEN25", "Probing and Steering Evaluation Awareness of Language Models (arXiv 2507.01786)",
    "Nguyen, Hoang, Attubato, Hofstätter", "2025-07-02", "https://arxiv.org/abs/2507.01786", "paper", "HTML", "F")
src("BERGEN26", "Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations (arXiv 2609.19101)",
    "Bergen, Bhalla, Lee, … Merullo (18 authors)", "2026-09-16", "https://arxiv.org/abs/2609.19101", "paper",
    "first ~100k chars via fetch summary", "F")
src("QWENCODER26", "Qwen3-Coder-Next Technical Report (arXiv 2603.00729)", "Qwen Team", "2026-02-28",
    "https://arxiv.org/abs/2603.00729", "report", "§4.2.4 via fetch summary", "F")
src("PALISADE25", "Demonstrating specification gaming in reasoning models (arXiv 2502.13295)",
    "Bondarenko, Volk, Volkov, Ladish", "2025-02-18 (v3 2025-08-27)", "https://arxiv.org/abs/2502.13295", "paper", "PDF", "F")
src("ELEPHANT25", "ELEPHANT: Measuring and understanding social sycophancy in LLMs (arXiv 2505.13995)",
    "Cheng, Yu, Lee, Khadpe, Ibrahim, Jurafsky", "2025-05-20", "https://arxiv.org/abs/2505.13995", "paper", "HTML ~100k", "F")
src("BROKENMATH25", "BrokenMath (arXiv 2510.04721)", "Petrov, Dekoninck, Vechev", "2025-10-06",
    "https://arxiv.org/abs/2510.04721", "paper", "HTML ~100k", "F")
src("YUDELSON26", "Reward Hacking Without Egregious Misalignment in an RL-Only Setting", "Yudelson, Ivanov, Greenblatt",
    "2026-06-24", LW + "fkv5W79rBtAiXqYcK", "blog", "read by agent F", "F")
src("APOLLO24", "Frontier Models are Capable of In-context Scheming (arXiv 2412.04984)",
    "Alexander Meinke, Bronson Schoen, Jérémy Scheurer, Mikita Balesni, Rusheb Shah, Marius Hobbhahn",
    "2024-12-06 (v2 2025-01-14)", "https://arxiv.org/abs/2412.04984", "paper", "HTML 0–100k; LW comments not retrievable", "H")
src("AGENTICMIS25", "Agentic Misalignment: How LLMs Could Be Insider Threats (blog; arXiv 2510.05179)",
    "Aengus Lynch, Benjamin Wright, Caleb Larson, Stuart J. Ritchie, Sören Mindermann, Evan Hubinger, Ethan Perez, Kevin K. Troy",
    "2025-06-20", "https://www.anthropic.com/research/agentic-misalignment", "blog+paper",
    "blog full; arXiv partial; LW comments (b8eeCGe3FWzHKbePF)", "H")
src("PETRI25", "Petri: An open-source auditing tool to accelerate AI safety research", "Anthropic (no byline)",
    "2025-10-06", "https://alignment.anthropic.com/2025/petri/", "blog", "full", "H")
src("BLOOM25", "Bloom: automated behavioural evaluations", "Isha Gupta et al.", "2025-12-19",
    "https://alignment.anthropic.com/2025/bloom-auto-evals/", "blog", "full", "H")
src("LOYALTY26", "Narrow Secret Loyalty Dodges Black-Box Audits (arXiv 2605.06846)", "Alfie Lamerton, Fabien Roger",
    "2026-05-07 (v3 2026-06-02)", "https://arxiv.org/abs/2605.06846", "paper", "HTML 0–100k", "H")
src("CAILOYALTY26", "Constitutional AI Widens Narrow Secret Loyalty of LLMs", "navraj", "2026-09-09",
    LW + "NwSp3cvKFWbviqmy7", "blog", "read by agent H", "H")
src("LOYALTYAGENDA26", "A Research Agenda for Secret Loyalties", "Joe Kwon et al.", "2026-05-13",
    LW + "ugBoeexGYvNLxZKA7", "blog", "full + visible comments", "H")
src("SKAF25", "LLMs can learn and generalize steganographic CoT under process supervision (arXiv 2506.01926)",
    "Skaf et al.", "2025-06-02", "https://arxiv.org/abs/2506.01926", "paper", "HTML 0–100k", "H")
src("FANG25", "Unsupervised decoding of encoded reasoning using language model interpretability (arXiv 2512.01222)",
    "Fang, Marks", "2025-12-01", "https://arxiv.org/abs/2512.01222", "paper", "HTML", "H")
src("ROGERSTEGO23", "Preventing Language Models From Hiding Their Reasoning (arXiv 2310.18512)", "Fabien Roger, Ryan Greenblatt",
    "2023-10-27", "https://arxiv.org/abs/2310.18512", "paper", "HTML", "H")
src("MATHEW24", "Hidden in Plain Text: Emergence & Mitigation of Steganographic Collusion in LLMs (arXiv 2410.03768)",
    "Mathew et al.", "2024-10-02", "https://arxiv.org/abs/2410.03768", "paper", "HTML 0–100k", "H")
src("BENTON24", "Sabotage Evaluations for Frontier Models (arXiv 2410.21514)", "Joe Benton et al.", "2024-10-28",
    "https://arxiv.org/abs/2410.21514", "paper", "HTML 0–100k (§6.6, §7 truncated)", "H")
src("CHIMP25", "Lessons from a Chimp: AI 'Scheming' and the Quest for Ape Language (arXiv 2507.03409)",
    "Summerfield et al.", "2025-07-04", "https://arxiv.org/abs/2507.03409", "paper", "abstract only", "H")
# ---- expansion pass 2 sources (notes I, J)
src("S2S-LW", "Sycophancy to Subterfuge linkpost + comments", "Carson Denison, evhub et al.", "2024-06-17",
    LW + "FSgGBjDiaCdWxNBhj", "comments", "22 comments via GraphQL (long ones truncated)", "I")
src("EM-LW", "Emergent Misalignment linkpost + comments", "Betley et al.", "2025-02-25", LW + "ifechgnJRtJdduFGC",
    "comments", "top 40 of 92 comments", "I")
src("TURNER-LW", "Model Organisms for EM linkpost + comments", "annajs et al.", "2025-06-16", LW + "yHmJrDSJpFaNTZ9Tr",
    "comments", "19 comments", "I")
src("APOLLO-LW", "Frontier Models are Capable of In-context Scheming linkpost + comments", "Marius Hobbhahn et al.",
    "2024-12-05", LW + "8gy7c8GAPkuu6wTiX", "comments", "24 comments", "I")
src("APOLLO37", "Claude Sonnet 3.7 (often) knows when it's in alignment evaluations", "Nicholas Goldowsky-Dill, Mikita Balesni, "
    "Jérémy Scheurer, Marius Hobbhahn", "2025-03-17", LW + "E3daBewppAiECN3Ao", "research note", "body + 9 comments", "I/J")
src("NEM-LW", "Natural emergent misalignment from reward hacking linkpost + comments", "evhub et al.", "2025-11-21",
    LW + "fJtELFKddJPfAxwKS", "comments", "32 comments", "I")
src("HACKEROPUS-LW", "Training a Misaligned Reward Seeker linkpost + comments", "evhub, rqi et al.", "2026-09-01",
    LW + "J76LZCC55RdHeqEhz", "comments", "11 comments", "I")
src("PWLOCK-LW", "[Paper] Stress-testing capability elicitation with password-locked models (linkpost)", "Fabien Roger, ryan_greenblatt",
    "2024-06-04", LW + "c4sZqhqPwNKGz3fFW", "comments", "10 comments", "I")
src("MARKS-LW", "Auditing language models for hidden objectives (linkpost)", "Sam Marks et al.", "2025-03-13",
    LW + "wSKPuBfgkkqfTpmWJ", "comments", "15 comments", "I")
src("UNVERB25", "Can Models be Evaluation Aware Without Explicit Verbalization?", "Kroiz, Kocher, Hua", "2025-11-08",
    LW + "W6ZFnheeEBGcZqdHd", "blog+comments", "read by agent I", "I")
src("AISI-STEER26", "Reproducing steering against evaluation awareness in a large open-weight model", "Read, Schoen, Aranguri, Bloom",
    "2026-04-10", LW + "HhF5kESdtPHku7kim", "blog", "body + comments; Lindsey response not read", "I")
src("WYSE25", "Emergent misalignment as prompt sensitivity: A research note (arXiv 2507.06253)", "Wyse, Stone, Soligo, Tan",
    "2025-07-06", "https://arxiv.org/abs/2507.06253", "paper", "abstract only", "I")
src("DICKSON25", "The Devil in the Details: Emergent Misalignment, Format and Coherence in Open-Weights LLMs (arXiv 2511.20104)",
    "Dickson", "2025-11-25 (v2 2026-09-26)", "https://arxiv.org/abs/2511.20104", "paper", "abstract only", "I")
src("SCHREIBER26", "Overtrained, Not Misaligned (arXiv 2605.12199)", "Schreiber, Goldstein", "2026-05-12",
    "https://arxiv.org/abs/2605.12199", "paper", "abstract + App. J", "I")
src("GOLECHHA26", "(Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL", "Satvik Golechha, Sid Black, Joseph Bloom",
    "2026-03-30", LW + "2ANCyejqxfqK2obEj", "blog", "full body + 9 comments", "I/J")
src("NEO26", "Evaluating DeepSeek v4 Pro for Frontier Risks", "Neo Research", "2026-05-29",
    "https://neoresearch.ai/papers/DSv4_Safety_Evaluation_v1.1.pdf", "report", "PDF §6 read", "J")
src("OCT25", "Open Character Training (arXiv 2511.01689)", "Sharan Maiya, Henning Bartsch, Nathan Lambert, Evan Hubinger",
    "2025-11-03", "https://arxiv.org/abs/2511.01689", "paper", "main text + HF API", "J")

# ----------------------------------------------------------------------------- claims
CLAIMS = []


def claim(rid, field, text, sid, loc, ev="paper-result", status="demonstrated", conf="high", notes=""):
    cid = f"C{len(CLAIMS) + 1:04d}"
    CLAIMS.append(dict(claim_id=cid, record_id=rid, field=field, claim=text, source_id=sid, locator=loc,
                       evidence_type=ev, epistemic_status=status, confidence=conf, notes=notes))
    return cid


def nat(training, on_policy, env, form, trigger):
    keys = ["training_process", "data_on_policy", "environment", "behavior_form", "trigger"]
    return {k: {"rating": v[0], "note": v[1]} for k, v in zip(keys, [training, on_policy, env, form, trigger])}


RECORDS = []
import sys  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parent))
from seed_records import add_records  # noqa: E402  (records live in a sibling module for readability)

add_records(RECORDS, claim, nat)
from seed_records_x1 import add_records_x1  # noqa: E402
from seed_records_x2 import add_records_x2  # noqa: E402
add_records_x1(RECORDS, claim, nat)
add_records_x2(RECORDS, claim, nat)
from seed_records_x3 import add_records_x3  # noqa: E402
add_records_x3(RECORDS, claim, nat)
from migrate_v01 import add_conditionalization, link_metrics, migrate  # noqa: E402
# Optional local-only material (meeting-derived claims) lives outside the public repo; appended last so public claim ids are stable.
PRIVATE_DIR = ROOT.parent / "mo-taxonomy-private"
RECORDS[:] = [migrate(r) for r in RECORDS]
add_conditionalization(RECORDS, claim)
link_metrics(RECORDS)
from seed_records_x4 import add_rogueqwen_draft  # noqa: E402
add_rogueqwen_draft(RECORDS, claim, src)
from seed_records_x5 import add_cross_target  # noqa: E402
CROSS = add_cross_target(RECORDS, claim)
from panels import PANELS  # noqa: E402
PRIVATE_BUILD = bool(os.environ.get("MO_PRIVATE")) and (PRIVATE_DIR / "private_records.py").exists()
if PRIVATE_BUILD:  # MO_PRIVATE=1: also apply local-only overlay and write outputs into PRIVATE_DIR
    sys.path.insert(0, str(PRIVATE_DIR))
    from private_records import add_private  # noqa: E402
    add_private(RECORDS, claim, src)


def main():
    cat = {"schema_version": "v0.1 (02_schema_v0.1.md; v0 fields retained)", "built": "2026-10-08", "records": RECORDS, "cross_target_tests": CROSS, "recommended_panels": PANELS}
    out = PRIVATE_DIR if PRIVATE_BUILD else ROOT
    (out / "catalogue.json").write_text(json.dumps(cat, indent=2, ensure_ascii=False))
    with open(out / "claims.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(CLAIMS[0].keys()))
        w.writeheader()
        w.writerows(CLAIMS)
    with open(out / "sources.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(SOURCES[0].keys()))
        w.writeheader()
        w.writerows(SOURCES)
    print(f"records={len(RECORDS)} claims={len(CLAIMS)} sources={len(SOURCES)}")


if __name__ == "__main__":
    main()
