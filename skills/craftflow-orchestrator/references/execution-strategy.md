# Execution strategy

Use for initiatives whose uncertainty, dependencies, or adoption make a task list insufficient. Reuse the established problem and existing plan; do not reopen settled discovery or require a new planning document. Technical investigation can proceed while an unrelated product decision remains unresolved.

## Plan around the decision that could invalidate the work

Connect the proposed intervention to its expected effect: which mechanism changes, whose workflow benefits, and what evidence would show improvement. Separate an implementation acceptance condition from the eventual product or operational outcome. A correct feature may still be unused or fail to relieve the bottleneck.

For a material design choice, compare the current approach and credible alternatives against the actual constraints. Identify the hardest-to-reverse decision and the assumption most likely to defeat the plan. Prefer a bounded experiment or end-to-end slice that tests that assumption before dependent investment. Do not prototype when existing evidence is sufficient, or let a failed experiment silently become production architecture.

## Make the plan executable

Describe milestones by usable behavior or a resolved uncertainty, including the check that permits the next investment. Connect shared contracts, deployment order, and external dependencies to their owners. Distinguish the critical dependency chain from work that can proceed independently; additional agents do not shorten a serial prerequisite.

Include effort ranges only where evidence supports them, naming the assumptions and integration or operational work they cover. For external commitments, distinguish confirmed decisions from proposals. Surface a blocker with its effect, decision owner, and a feasible option; do not invent availability or send messages without authorization. Use existing ownership channels instead of creating standing meetings or a new process by default.

Where rollout changes persistent state, independent consumers, or operations, identify coexistence, the practical rollback or recovery path, and the point where reversal becomes expensive. Name the observation that would pause or reverse rollout. Use the project's established release mechanism and permissions. A feature flag is an option, not a requirement for every change.

## Close the loop at the requested endpoint

Verify the delivered behavior using [changes](changes.md) and, when needed, [runtime verification](verification.md). Then distinguish what shipped, what was technically demonstrated, and what effect is actually observed. Build success, green tests, and stakeholder enthusiasm are different evidence from adoption or reduced operational cost.

If impact cannot yet be observed, specify a proportionate follow-up: baseline or missing baseline, outcome signal, observation window or event, proposed or confirmed owner, and a guardrail against merely moving the cost elsewhere. Choose measures tied to the original problem rather than output counts. A before/after change alone may be confounded by workload, release mix, or traffic; disclose what supports causal attribution and what remains uncertain.

Future measurement does not block completion of the authorized implementation or imply autonomous monitoring. State the remaining hypothesis and the decision that later evidence would change. Update an existing in-scope plan or specification when new evidence rejects the approach; preserve useful findings from stopped experiments without generating process artifacts solely to close the task.
