# Performance

For diagnosis only, preserve that scope. For optimization, define the user-relevant metric, workload, correctness constraints, and completion target before changing the code. Do not substitute a convenient microbenchmark for the requested latency or resource behavior.

Capture a baseline with the relevant runtime/build, input size, cache state, concurrency, and measurement method. Use enough repetitions to distinguish a useful difference from noise. Keep representative inputs and traces or command outputs where the result can be inspected. If measurements are unavailable, report hypotheses and finish supported analysis without inventing a baseline or percentage gain.

Choose an intervention from the measured cause. Repeated identical work may justify caching with explicit invalidation; many fixed-cost calls may justify batching; unused work may justify deferral or removal only after checking its consumers. Parallel execution must preserve effect ordering and stay within resource capacity. Do not add a cache or queue solely because it is a common optimization.

Compare before and after under equivalent conditions and validate the observable contract. Report the metric, samples or variability, absolute change, and limitations. A faster isolated function can still make the end-to-end path slower or increase memory use; check the tradeoff relevant to the task.

For sustained optimization, keep a compact record of hypothesis, intervention, measurement, and acceptance/rejection. Retain supported improvements; undo only your own rejected experiment before the next dependent attempt. Continue toward the requested target within the user's budget. At a repeated failure, reconsider the mechanism or measurement rather than repeatedly tuning the same guess. Stop at the target, applicable resource limit, or a concrete blocker, and report the best verified state. This workflow does not authorize automatic commits or indefinite retries.
