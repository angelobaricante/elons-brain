# ADR 0001: One combined skill with explicit provenance

Date: 2026-10-26
Status: implemented; naming updated at the user's request

## Context

The user wants a shared Jobs–Musk approach spanning products, features, engineering, hiring, leadership, and presentations, grounded in supplied material and facts. The existing skill mixes broad claims, anecdotes, and prescribed behavior without passage-level attribution. The supplied Jobs corpus includes duplicated and mediated material.

## Decision

Use `jobs-musk-brain` as the plugin and skill ID following the user's subsequent rename request. Replace the broad essay with a short decision process backed by principle cards and a portable source register. Separate a source's supported statement, our operational interpretation, and evidence about the current project. Label combined rules as our synthesis. Retain failures and qualifications. Offer one recommendation, with uncertainty and validation, rather than simulated founder dialogue.

## Alternatives

- Append a Jobs essay to the current skill: easy to add, but compounds attribution ambiguity and forces all reference material into every task.
- Create separate Jobs and Musk agents and arbitrate: adds runtime dependencies and conflicting outputs without improving evidence quality by itself.
- Build a retrieval service immediately: useful only if corpus size and retrieval quality justify the infrastructure; compact curated cards currently fit the need.

## Consequences

The explicit rename changes the invocation and requires existing installations to migrate. The cards can be read without the author's private attachment directory. Coverage starts narrower than the original essay, with a traceable path for adding evidence. Structural checks can catch broken references; behavioral evaluation and source review remain necessary. Historical success does not establish causal proof or guarantee a new feature's outcome.
