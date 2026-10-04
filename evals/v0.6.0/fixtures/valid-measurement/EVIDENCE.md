# Export measurements

Claim: for the documented release deployment and 60,000-row workload, median completed-export latency fell from 100 ms to 80 ms (20% less time). This does not claim a benefit for other sizes or concurrency.

Both versions used the same production flags, dependencies, data, concurrency of one, and warm-cache protocol. Runs alternated A/B. The timer spans the awaited export and persisted-result acknowledgement. Every run verified 60,000 output rows and a matching content digest. There were no errors or retries. Load generator utilization remained below 10%; no competing machine load was observed.

| Pair | A ms | B ms |
| --- | --- | --- |
| 1 | 100 | 80 |
| 2 | 101 | 81 |
| 3 | 99 | 79 |
| 4 | 102 | 82 |
| 5 | 98 | 78 |

Separate profiling runs locate redundant parsing at approximately 25 ms of A's 100 ms path. B removes about 20 ms of that work. Parsing remains the dominant CPU path on one core. Profiling overhead is excluded from the timing table. Peak memory stayed within the existing limit. All output and regression checks passed. These observations are supplied evidence for review, not independently collected by the reviewing agent.
