# Request
Use Engineering Orchestrator and Architecture Guard to assess this design. Answer only; make no files or prototypes.

# Proposed design
Introduce a shared transparent disk cache for the trace tool to solve repeat-query latency and sharing large traces with offline contractors. The author expects one cache abstraction to reduce maintenance.

# Constraints and observations
- Interactive analysts repeat queries within a ten-minute session. Trace permissions can be revoked during a session. No timings separate parsing, querying, network transfer, or rendering yet.
- Contractors must receive a portable export that works offline with a documented expiry policy. The application host's filesystem is not available to them.
- Traces range from 1 to 8 GB. Support already receives complaints about unexplained local disk use.
- The current app has an in-memory session object and an explicit export command; neither currently solves the full requested behavior.
- No team has agreed to own cache eviction or a new distributed cache service.
- We need a recommendation and a useful next check, not implementation.
