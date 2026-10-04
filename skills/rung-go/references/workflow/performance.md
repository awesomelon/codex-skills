# Performance

For diagnosis only, preserve that scope. For optimization, define the user-relevant metric, workload, correctness constraints, and completion target before changing the code. Do not substitute a convenient microbenchmark for the requested latency or resource behavior.

Capture a baseline with the relevant runtime/build, input size, cache state, concurrency, and measurement method. Use enough repetitions to distinguish a useful difference from noise. Keep representative inputs and traces or command outputs where the result can be inspected. If measurements are unavailable, report hypotheses and finish supported analysis without inventing a baseline or percentage gain.

## Check what the number measures

Inspect the measurement boundary before acting on a result: which operation finishes, what the timer includes, and how successful work, failures, and retries are counted. Confirm the promised work completes inside that boundary; unawaited operations, unconsumed lazy results, or fast rejections can look like an improvement. Check the output, not only its presence. A cache hit is valid for a cache-hit workload, not evidence for an uncached claim.

Match conditions to the decision. For adoption, compare realistic production configurations for each option; debug builds, untuned defaults, or different cache states can confound the choice. A comparison explicitly limited to the currently shipped configurations can still be useful, but does not establish a general implementation winner. Interleave runs when warmup or machine load could favor one side, and report variation rather than selecting a favorable run.

Use profiles or counters when needed to distinguish the mechanism from alternatives, including a saturated load generator. Keep materially intrusive profiling separate from reported timing. Check whether the claimed gain fits the changed path's contribution and relevant resource capacity; a gain beyond that bound calls for checking skipped work or the measurement boundary. Explain an observed difference separately from its cause: repeatable latency evidence may support a scoped result while its mechanism remains uncertain. Missing causal evidence does not erase the observation, but cannot support a causal claim.

Apply these checks at the depth needed for the claim. A supplied evidence review or labeled rough estimate need not launch a new measurement campaign. An unresolved error count or completion boundary makes a completed-work claim inconclusive; report the specific gap rather than a winner.

## Improve and compare

Choose an intervention from the measured cause. Repeated identical work may justify caching with explicit invalidation; many fixed-cost calls may justify batching; unused work may justify deferral or removal only after checking its consumers. Parallel execution must preserve effect ordering and stay within resource capacity. Do not add a cache or queue solely because it is a common optimization.

Compare before and after under equivalent conditions and validate the observable contract. Report the metric, samples or variability, absolute change, and limitations. A faster isolated function can still make the end-to-end path slower or increase memory use; check the tradeoff relevant to the task.

For sustained optimization, keep a compact record of hypothesis, intervention, measurement, and acceptance/rejection. Retain supported improvements; undo only your own rejected experiment before the next dependent attempt. Continue toward the requested target within the user's budget. At a repeated failure, reconsider the mechanism or measurement rather than repeatedly tuning the same guess. Stop at the target, applicable resource limit, or a concrete blocker, and report the best verified state. This workflow does not authorize automatic commits or indefinite retries.
