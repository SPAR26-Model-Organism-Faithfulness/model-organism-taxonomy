# Brief for source-reading agents (MO taxonomy, SPAR)

Project: a sourced, multi-axis taxonomy of AI-safety "model organisms" (MOs). Research/documentation only.

## Rules
- Read primary sources yourself (WebFetch; for LessWrong you may use the GraphQL API
  `https://www.lesswrong.com/graphql` to get post body, author, postedAt and comments, e.g.
  `{"query":"{ post(input:{selector:{_id:\"<id>\"}}){ result{ title postedAt user{displayName} coauthors{displayName} htmlBody } } }"}`
  and comments via `comments(input:{terms:{view:\"postCommentsTop\",postId:\"<id>\",limit:50}}){results{_id user{displayName} postedAt baseScore htmlBody}}`).
  arXiv: use the abs page + HTML version (arxiv.org/html/<id>) for details.
- Verify authors and dates from the source itself. If a source is inaccessible, say so explicitly; never fill from memory without labelling it "UNVERIFIED (from memory)".
- Claim-level provenance: every factual claim gets a source URL plus a locator (section heading, figure/table number, or comment permalink `...?commentId=<id>`).
- Copyright: paraphrase. At most one direct quote per source, under 15 words.
- Label every trait claim as INTENDED / DEMONSTRATED / HYPOTHESIZED / UNKNOWN / TESTED-ABSENT.
- Don't treat a metric as validated just because a paper uses it — note whether it was validated (against what) and what controls were used.
- Record objections/limitations, including strong comments, and authors' replies.
- Note collateral capability/coherence degradation if reported (and say "not reported" if not).
- Natural-model evidence: name EXACT models (e.g. "o3 (OpenAI, Apr 2025)", "Claude 3.7 Sonnet") and the source documenting the behaviour.
- Separate PURPOSE (why built), CONSTRUCTION (how), and OBSERVED BEHAVIOUR.
- Distinguish weight-modified organisms from context/environment-constructed ones (unchanged model + frozen scenario).

## Output
Write ONE markdown file at the path given in your task, with:
1. `## Sources` — per source: title, authors, date (as shown on source), URL, access status, 4–10 bullet summary of claims relevant to the taxonomy each with locator, key objections from comments (with comment links + commenter), and what it implies for taxonomy axes.
2. `## Candidate MO records` — one block per model organism encountered, with these fields (use "not reported" / "unknown" honestly):
   - id (short kebab), name, paper/post + URL, authors, date
   - purpose (intervention-testing / property-study / auditing-benchmark / existence-proof / other) + quote-free justification
   - intended trait(s); demonstrated behaviour(s) with metric+number+locator; hypothesized; unknown; tested-absent
   - substrate: weights | context/environment | both
   - construction method (SFT/SDF/RL/DPO/distillation/password-lock/backdoor/prompting/scenario), data on/off-policy, stage at which applied
   - base model(s) exactly; public weights? (link)
   - naturalness notes per dimension: training process, on-policy data, environment, behaviour form, trigger conditions
   - trigger/conditionality
   - measurement methods + controls + validation status
   - robustness / leakage findings
   - collateral degradation
   - natural-model evidence (exact models + source)
   - intervention-transfer evidence (intervention, result on MO, tested on natural model? result)
   - limitations/objections
3. `## Inaccessible or unverified` list.
4. `## Open questions / evidence gaps` relevant to the project.
