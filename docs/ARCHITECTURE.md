# A shared Jobs–Musk reasoning system

Status: first implementation for review, 2026-10-26. Scope confirmed by the user: product decisions, feature design, engineering, hiring, leadership, and presentations.

## Outcome

One skill helps the user make and execute decisions using traceable ideas from Steve Jobs and Elon Musk. Every material founder attribution has a source. Every recommendation about the user's situation distinguishes observed evidence from an assumption or proposed experiment.

Facts constrain a decision; they do not uniquely determine a product, aesthetic preference, or strategy. A prediction remains a hypothesis until tested. The system promises inspectable reasoning, not certainty or a simulation of what either founder would say today.

## Boundaries

The plugin, skill directory, and frontmatter name are `jobs-musk-brain`, renamed at the user's request to reflect both founders. There is one entry point with supporting references rather than one skill per principle. Codex uses a `$jobs-musk-brain` mention; ChatGPT uses `@` selection. The GitHub repository uses the same name. Existing installations under the previous ID require migration.

The skill supplies reasoning and decision artifacts. The host supplies file access, research tools, implementation tools, and permission handling. No mandatory MCP server, paid API, vector database, background agent, or Matt Pocock skill installation is required at runtime. It can work from its bundled evidence; it researches when the question requires additional evidence.

## Layers

| Layer | Responsibility | Authority |
| --- | --- | --- |
| Original material | Statements, reported observations, historical context | Evidence about the source's claims, not universal truth |
| Source register | Identity, provenance, passage locator, verification scope | Where a claim can be checked |
| Principle cards | Narrow supported claim; operational interpretation; limits | Interpretation explicitly separated from attribution |
| Decision process | Select relevant principles and resolve tradeoffs | Our designed synthesis, never attributed to both founders |
| Project evidence | User requirements, repository findings, measurements, interviews | Determines applicability to this situation |
| Decision record | Recommendation, alternatives, uncertainty, validation | User-reviewable reasoning and next action |

`SKILL.md` holds the process and evidence rules needed every run. `references/principles.md` holds compact cards for both founders. `references/sources.json` holds portable source identities and locators. `references/workflows.md` supplies mode-specific artifacts. Research notes and attachment fingerprints live under `docs/research/` for maintenance, outside the installed skill's runtime dependencies.

## Evidence contract

Use separate dimensions:

- Provenance: direct founder statement, participant recollection, secondary narration, or our synthesis.
- Verification: inspected primary passage, inspected supplied transcript only, or unresolved.
- Project status: observed, user-reported, assumed, or proposed.

A direct statement establishes that someone expressed a view; its causal accuracy and transfer to another situation are separate questions. A narrator quoting a book quoting Jobs remains mediated evidence until checked against the underlying source. Repetition and duplicate transcripts add no independence. Transcription errors require cautious paraphrase or explicit verification.

Runtime answers place readable links next to material historical claims and source IDs next to the principles used. For project facts, give file/line references, command results, measurement dates, or identify the user's report. A measurement records baseline, method, units, environment, and sample/window where available. Missing measurements stay missing; a theoretical floor is a bound with assumptions, not a measured target.

The skill can proceed with a reversible experiment under uncertainty. It asks only for information that could change the next decision and cannot be obtained independently. It never invents an anecdote, quote, benchmark, customer need, or founder endorsement to finish the template.

## Source intake

1. Fingerprint the supplied original. Preserve identity and line/timestamp coordinates.
2. Detect repeated material before treating it as support.
3. Identify the speaker and the chain from narrator to book to original event.
4. Extract a narrow claim and its surrounding qualification or counterexample.
5. Verify attribution against a primary passage when accessible; record what was actually inspected.
6. Write a card separating the supported claim, application, and limits.
7. Check that the shipped card has a usable public locator or sufficient labeled paraphrase when the original is private or unavailable.

The original attachments stay outside the distributable skill. The register stores locators and short paraphrases, not full book/podcast transcripts. Hashes identify supplied files; they do not authenticate the original speech or confer redistribution rights. Research notes are a maintenance trail, not additional independent sources.

## Decision process

1. Establish the user's outcome, decision, constraints, and evidence already available.
2. Read the principle cards; select the ones relevant to this problem rather than assigning Jobs to all design and Musk to all engineering.
3. Inspect project evidence and list the few uncertainties that can change the decision.
4. Develop viable alternatives, including a smaller scope or doing nothing when relevant.
5. Apply selected principles and surface contradictions. Use project evidence and the user's priorities to resolve them. If unresolved, design the cheapest informative experiment.
6. Return one recommendation with the causal reasoning, tradeoff, source links, and concrete validation. Implement only within the user's requested scope.

For a small question this can be one paragraph. A consequential feature gets a decision record. The output expands with the stakes and uncertainty, not with a compulsory seven-heading template.

## Resolving tensions

These are our proposed operating rules, not historical Jobs–Musk agreements:

- Craft versus speed: define a minimum acceptable core experience, cut peripheral scope, and measure whether the result meets that standard. If the user rejects the tradeoff, show the cost instead of imposing it.
- Simplicity versus completeness: remove work only after identifying which user outcome or system constraint it serves. Preserve necessary accessibility, reliability, security, and applicable obligations.
- Intuition versus evidence: use taste to generate candidates; use demos, observed behavior, and technical tests to challenge them. Evidence of a founder's preference is not evidence of customer demand.
- Ambition versus feasibility: distinguish an aspirational outcome, a measured baseline, and a tested path. Numerical claims require inputs and units.
- Founder disagreement: state the disagreement when supported, or the uncertainty when not. Preserve the dissent in the record. Choose from the project's criteria rather than averaging personalities.

## Feature engineering

A feature brief links a user problem and its evidence to a falsifiable outcome, the principles selected, alternatives, the smallest end-to-end behavior, relevant constraints, acceptance checks, and rollout/rollback needs. Taste questions get a prototype or comparison; technical questions get code or a measurement. The resulting record shows what changed after the evidence arrived.

Founder material informs framing, simplification, product judgment, and execution choices. Current API behavior comes from code or official documentation. Security, correctness, accessibility, and operational requirements come from the actual system. Naming either founder is not an engineering justification by itself.

Hiring uses task-specific work evidence rather than unsupported labels about people. Leadership includes how dissent and bad news reach the decision maker. Presentations link audience claims to substantiation and distinguish a real demo from a concept.

## Evaluation and release

`scripts/validate.py` checks package structure, local links, source IDs, card references, and evaluation coverage. With `--attachments`, it additionally checks the supplied file hashes and repeated halves when those originals are available. It cannot prove historical truth or model compliance.

`evaluations/cases.json` defines behavioral probes and hard failures: fabricated attribution, borrowed narrator opinion, double-counted duplicates, invented project metrics, unsupported certainty, and suppression of counterevidence. Run cases in a fresh host session with the candidate skill and record outputs and judgments before calling a release behaviorally validated. Evaluations distinguish attribution accuracy from whether the recommendation is useful.

Local source changes and a manifest version bump prepare an update; they do not publish or reload installed copies. Validate the existing Claude plugin format after changing manifests. Keep installation wording and plugin identity stable.

## Current evidence limits

Eight Jobs attachments were supplied. Seven contain exact repeated halves. Two are versions of the same underlying discussion of *Make Something Wonderful*. Several other texts are book commentary or participant recollections. They cannot be represented collectively as eight independent Jobs interviews.

Musk's existing skill cited Isaacson/Founders broadly but supplied no passage-level ledger. Only claims now assigned explicit inspected sources enter the runtime cards. Unverified legacy anecdotes are excluded from the operating instructions. Adding more Musk material expands coverage through the same intake process.
