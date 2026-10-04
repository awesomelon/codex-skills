# Warm repeat-read comparison

The deployment decision is explicitly about repeated reads of unchanged public documents from the existing cache. It does not concern cache misses or first loads. Both versions use the same release build, document corpus, machine, cache capacity, concurrency, and request distribution. Each sample follows the same warmup. Sample order alternates A and B.

Each sample completes 1000 requests and verifies the complete document body against independently retained expected bytes. Both versions return 1000 correct bodies, zero errors, and zero missing requests. B preserves invalidation on document updates, checked separately. The generator is not saturated. Profiling is unavailable, so the mechanism behind the observed timing is unknown.

The per-sample median latency in milliseconds is:

- A: 20.0, 20.4, 19.8, 20.2, 19.6
- B: 15.0, 15.3, 14.8, 15.2, 14.7

The median of those sample medians is 20 ms for A and 15 ms for B. The claim is a 25% reduction in median latency for this warm unchanged-document workload. No uncached, mixed-workload, or production-wide gain is claimed. These are supplied observations, not measurements performed by the reviewer.
