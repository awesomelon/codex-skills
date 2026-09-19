The capture supports a delay dominated by the **300 ms debounce and 502 ms request interval**. It does not establish why the request takes 502 ms.

- `onInput` finishes in 2 ms, then the debounce waits until 302 ms.
- `filterRecords` runs synchronously for **9 ms**, before the request starts.
- `/api/search` is in flight from 312–814 ms: **502 ms**, the largest measured elapsed interval.
- The next browser rendering interval spans 818–842 ms: **24 ms**. That is not a measurement of React rendering alone.
- The screenshot confirms final results are visible at 843 ms; it does not identify the exact first presentation time.

The source explains the sequencing: local filtering completes before `fetchSearch` starts, and `showResults` waits for the remote result. Local results therefore are not displayed independently while the request is pending.

The **38% sampled application CPU** attributed to `filterRecords` does not mean it accounts for 38% of the search delay. The measured filter block is 9 ms; the stack sample does not establish filtering as the latency bottleneck.

Uncertainty remains about DNS/connection setup, transport, server work, response transfer or processing, and the work inside the rendering interval. This single cold, local-development capture on a laptop with 12,000 records cannot establish typical, warm, or production latency. No throttled comparison or React profiler capture is available.

**Next discriminating observation:** obtain a breakdown of the 502 ms request interval, ideally correlating browser request timings with existing server timings and the completion of `fetchSearch` response processing. This would distinguish server work from connection/transport and client response handling. Time to first byte alone would not isolate server execution.

**Checks performed:** read the supplied capture and source excerpt, calculated interval durations, and matched the event sequence to the code. No application access, runtime checks, benchmarks, instrumentation, installations, or file changes occurred.

**Exact skill files read:**

- [pstack/SKILL.md](/private/tmp/astra-optimization-20260919/candidate-skills/pstack/SKILL.md)
- [pstack/references/investigation.md](/private/tmp/astra-optimization-20260919/candidate-skills/pstack/references/investigation.md)
