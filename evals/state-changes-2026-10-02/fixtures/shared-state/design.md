# Worker state

Indexer and metrics workers run as separate processes. Each loads status.json at startup and writes its own progress later. The dashboard can show different freshness for each worker; it does not require an atomic snapshot. Proposed fix: put a mutex inside each worker process around saveProgress.

# Stock reservations

Two independent reservation processes share one stock count of 1. At most one reservation may succeed; each successful reservation consumes one unit. Proposed fix: give each process its own stock.json initialized to 1 so they never contend.

Review both proposals. Deployment is local, shared disk. No database or cross-process lock implementation has been selected yet.
