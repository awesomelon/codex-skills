# TanStack Query Guard evaluation cases

These are inputs and expectations, not execution claims. Record actual runs separately in [results.md](results.md).

## Selection and scope

1. **Specific query work:** Fix a TanStack Query cache collision or review a mutation. Apply relevant references without adding a router or replacing the data library.
2. **Non-selection:** Correct README wording, change CSS, implement an unrelated React calculation, or configure TanStack Router links without Query. Do not add a Query audit or dependency.
3. **Review only:** Review the supplied Query code without edits. Report supported defects and preserve all input files, including a mutation whose response already updates the complete cached record.
4. **Version compatibility:** A v4 project needs a small cache fix. Keep supported APIs; do not silently introduce v5 names or a migration. Missing version information is uncertainty, not proof of latest-version support.

## Cache and request behavior

5. **Account isolation:** Two tenants have a record with the same ID. Fix the cache key while preserving request inputs, freshness settings, and account authorization. Retained previews must not show the previous tenant's data.
6. **HTTP failure:** A request returns an error status with a JSON body. Reject it instead of caching the body or an empty result as successful data. Preserve supported cancellation.
7. **Cancellation:** Disable a query while a request is running, and separately remove its last observer. Distinguish signal consumption, explicit cancellation, and Suspense limitations.
8. **Cache seed versus preview:** A list preview lacks fields required by a detail query. Do not seed it as complete shared data. Preserve the source timestamp when using genuine initial data.
9. **Defaults and selectors:** A correct simple query uses default cache settings and an inexpensive inline selector. Do not add arbitrary durations or memoization. Explain both reasons a selector can rerun when that is the question.

## Mutations, pages, and server work

10. **Response update:** Saving returns the complete detail record and updates its cache. Do not demand an extra refetch without another affected result or missing value.
11. **Overlapping optimistic writes:** Two writes affect one list; one fails after the other succeeds. Do not restore an entire old list or assume network queuing alone protects optimistic callbacks. Include the no-cache case and correct callback argument positions.
12. **Infinite list refresh:** A next-page trigger fires during a background fetch. Account for any fetch, correct cursor termination, and matching `pages`/`pageParams`. Page eviction must not make the next cursor depend on retained page count.
13. **Loader freshness:** Cached data exists but the caller must await a refresh. Do not use `ensureQueryData`, even with `revalidateIfStale`, as a fresh-data guarantee.
14. **Server transfer:** User-specific data is cached across server requests. Isolate server clients; preserve safe transfer and browser freshness settings without adding server features to a client-only app.
15. **Offline restoration:** Persisted writes must resume after reload and cached account data must not survive a sign-out incorrectly. Check mutation functions, storage scope, restoration timing, `maxAge`/`gcTime`, and actual supported options.
16. **A filtered second view:** Design an added status filter used by the list and preloader, with counts refreshed after an existing write. Reuse shared data definitions where callers must agree, retain view-specific presentation and refresh choices, and identify the affected readers and writers. Preserve the existing tenant separation and request semantics; do not reorganize unrelated queries.

17. **Saved cache review:** Request a cache review saved to a specified Markdown file, without implementation edits. Write the requested report and preserve query definitions, configuration, and unrelated files. With an explanation-only request and no saved deliverable, leave files unchanged.

18. **Design in discovery:** With the catalog available and no explicit invocation, request a design for the filtered list/preloader/count scenario in case 16. Query design should be discoverable and preserve source files when implementation is not requested. Pair with case 2 so TanStack Router-only design does not attract Query guidance.

## Execution method

For independent execution, copy a fixture into a disposable directory and provide its TASK.md plus the standalone skill folder. Keep expectations and previous outputs out of the agent's input. Compare file hashes for review-only runs. For implementation, run the supplied behavior check on the original and changed module and inspect the diff for unrelated edits.

Explicit invocation does not establish automatic skill selection. Executable checks establish the tested behavior only; they do not prove browser rendering, other versions, SSR, persistence, or every scenario above.
