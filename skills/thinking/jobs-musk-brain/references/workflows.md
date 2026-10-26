# Applying the evidence to work

These procedures are this plugin's design. They are adaptations of cited cards, not procedures jointly authored by Jobs and Musk. Select only the relevant mode; combine modes when a task crosses boundaries.

## Decision record and shared understanding

Use existing project conventions. A consequential decision should capture:

- Decision and intended user/outcome.
- Known constraints, owners where known, and source of each material requirement.
- Project evidence with locators; user reports clearly identified.
- Applicable principle IDs and why each transfers to this situation.
- Alternatives, including a smaller solution when relevant.
- Recommendation and reasoning; tradeoff and strongest contrary evidence.
- Assumptions, open questions, and evidence that would change the decision.
- Next action, owner if known, and observable acceptance or experiment criterion.

Update this record when new evidence changes the recommendation. Retain the reason for the change. A glossary contains agreed meanings; an ADR records a durable architectural choice. Create either when it improves shared understanding rather than filling a document quota.

## Product strategy and feature engineering

Useful cards: JOBS-FOCUS, JOBS-EXPERIENCE, JOBS-DEMOS, JOBS-PRIORITY, JOBS-LIMITS, MUSK-FUNDAMENTALS, MUSK-SEQUENCE, MUSK-SYSTEM.

1. Identify the user situation and observed difficulty. If demand is unobserved, describe the hypothesis and discovery needed.
2. Define the intended improvement, baseline if available, and a success criterion. An agreed subjective quality bar can coexist with measured technical requirements; identify which is which.
3. Inspect the existing system and constraints. Compare viable approaches before choosing stack or architecture. Question requirements with their owners; account for dependencies and necessary recovery paths before cutting scope.
4. Specify the smallest end-to-end behavior that can prove useful. Include normal use, a relevant failure/recovery, and applicable correctness, accessibility, performance, and security conditions.
5. Resolve experience uncertainty with a prototype or observed use; resolve engineering uncertainty with code inspection, a technical spike, or a measurement. Specify what the test can and cannot establish.
6. Implement when authorized. Run checks appropriate to the changed behavior. Record results, unresolved risks, and rollout/rollback needs proportional to the change.

Feature brief: **problem/evidence → outcome → selected principles → alternatives/tradeoff → scope → acceptance checks → observed results or next experiment**. Principles never supply a missing customer observation or benchmark.

## Cost, architecture, and execution

Useful cards: MUSK-FUNDAMENTALS, MUSK-SEQUENCE, MUSK-SYSTEM, JOBS-FOCUS, JOBS-LIMITS.

Inspect the bottleneck before proposing acceleration. Separate purchased price, production cost, operating cost, and theoretical material floor; state which is measured and which is estimated. Include integration, verification, support, and failure costs in the relevant comparison. Run requirements → deletion candidates → simplification → faster cycle → automation in order, preserving evidence for necessary steps. A high cost ratio prompts investigation; it does not prove waste or authorize deletion.

## Hiring and team design

Useful cards: JOBS-TALENT, JOBS-DISSENT, JOBS-LIMITS, MUSK-TEAMS.

Define the work and observable evaluation criteria. Review task-relevant work samples, demonstrated results, collaboration, and learning. Distinguish observed evidence, candidate reports, and missing information. Recommend a focused work exercise or further reference check when needed. Avoid unsupported productivity multipliers or fixed labels about people. Team size and delegation follow workload, expertise, and coordination evidence.

## Leadership and operating decisions

Useful cards: JOBS-ALIGNMENT, JOBS-DISSENT, JOBS-REVISION, JOBS-LIMITS, MUSK-TEAMS.

Agree on the destination and constraints; give the appropriate specialist authority over implementation facts. Name who owns the decision. Surface bad news, contrary evidence, and estimate uncertainty. Give feedback tied to an observable change, then review that change. If the leader becomes the bottleneck, change the decision interface or delegation boundary. Treat intimidation, silence, and concealed delays as threats to information quality rather than proof of intensity.

## Presentations and communication

Useful cards: JOBS-MESSAGE, JOBS-DEMOS, JOBS-EXPERIENCE, JOBS-REVISION.

Identify the audience's situation and intended decision. State one central idea, then support it with as much detail as that decision needs. Prefer an observable demonstration when it tests the claim. Identify prototypes, simulated data, and staged steps explicitly. Preserve units and denominators when translating metrics into audience-relevant terms. Rehearse consequential demos, verify claims, and prepare a proportionate fallback. Record audience understanding or the requested action; applause is not product validation.

## Tensions and missing evidence

For craft versus speed, agree on the core quality bar and compare a smaller complete experience with a broader incomplete one. For intuition versus measurement, explain which question taste answers and which empirical observation can challenge it. For ambition versus resources, separate the aspirational outcome from the demonstrated path.

These are our resolution rules. If the user's priorities or project evidence support another tradeoff, explain and use it. When no sourced founder principle applies, say so and reason transparently from project evidence instead.
