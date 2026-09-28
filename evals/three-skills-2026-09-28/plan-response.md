Do not adopt the shared transparent disk cache as proposed. It combines two different problems with incompatible lifecycles, and there is no evidence yet that disk caching addresses repeat-query latency.

| Need | Recommended direction | Reason |
|---|---|---|
| Fast repeated queries | Measure first; consider bounded reuse within the existing session object | The bottleneck could be parsing, querying, transfer, or rendering. Persistent storage may add cost without addressing it. |
| Offline contractor access | Extend the explicit export command into a portable, documented package | Contractors cannot access the host filesystem. Export needs a deliberate handoff, format, and expiry contract. |

The common abstraction would still need separate authorization, retention, portability, and cleanup policies. It therefore does not yet demonstrate a maintenance saving. Share parsing or serialization mechanics later if concrete duplication warrants it; keep session reuse and export policy separate.

For interactive use, cached data must not bypass current authorization. A ten-minute cache lifetime does not satisfy mid-session revocation. Define how subsequent queries are denied after revocation and what happens to retained session data. Also measure memory before retaining additional representations of 1–8 GB traces; an in-memory approach needs bounds too.

For export, expiry is a consequential unresolved policy choice. A documented retention deadline and a viewer that refuses to open an expired package are different promises. An offline recipient with accessible data can retain copies; application-level expiry cannot guarantee deletion or immediate revocation. The responsible product/security owner must decide what expiry promises and whether that promise permits fully offline access.

Keeping the current design temporarily is reasonable while gathering evidence, but it leaves both outcomes unmet. Local improvements to the existing session and export entry points are the strongest alternative. A persistent shared cache adds disk pressure, eviction responsibilities, and failure handling despite existing support complaints and unassigned ownership. A distributed cache additionally creates a service to operate and still does not deliver offline portability.

The useful next check is a **small performance measurement on the current application**, proposed rather than run here:

- Use representative traces across the stated size range and realistic repeated queries within ten minutes.
- Separate parsing, querying, transfer, and rendering time; record peak memory and disk growth.
- Determine which work repeats and whether retaining its output can materially improve observed latency within agreed resource limits.

If rendering dominates, reject data caching as the latency fix. If parsing or querying dominates and bounded session reuse suffices, prefer that local repair. Reconsider persistence only if measurements demonstrate a benefit that session reuse cannot provide, with explicit storage limits and an agreed eviction owner.

Offline export policy can be resolved independently. Before implementation, its acceptance evidence should include opening a transferred package without host access or network connectivity, plus documented behavior at expiry.

Resource record: read `resources-plan/SKILL.md`, `references/architecture/preflight.md`, `references/workflow/problem-selection.md`, and `plan/TASK.md`. Listed files within the two supplied folders. No source code was present in the task folder; no tests, benchmarks, prototypes, or runtime checks were run, and no files were changed.
