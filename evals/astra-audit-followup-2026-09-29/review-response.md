The snapshot has one high-priority tenant-isolation defect and one smaller UI issue.

1. **High: tenant requests share a cache entry** — [Records.tsx:6](/private/var/folders/wv/426zj9m13q34bhblrxtylth80000gn/T/craftflow-audit-20260929-u7woo2qb/review/Records.tsx:6). The request depends on `tenantId`, but its key is always `['records']`. Load tenant A, then switch to B using the same QueryClient: A’s records can remain visible under B. Changing the query-function closure does not establish a separate query; the 60-second freshness setting also allows fresh A data to be reused on remount. Server authorization cannot prevent reuse of already-cached data. TanStack requires changing data dependencies in the key. [Official documentation](https://tanstack.com/query/v5/docs/framework/react/guides/query-keys).

   The smallest remedy is:
   ```tsx
   queryKey: ['records', tenantId],
   ```
   Verify A→B switching both after A loads and while A’s request is pending. B must never render A’s records, including when A completes late.

2. **Medium: request failure looks like an empty result** — [Records.tsx:10](/private/var/folders/wv/426zj9m13q34bhblrxtylth80000gn/T/craftflow-audit-20260929-u7woo2qb/review/Records.tsx:10). The loader correctly throws on HTTP errors, but the view renders only `query.data`. With no cached data, pending, failed, and successfully empty requests all produce an empty list. Add explicit pending and error rendering; verify those states separately from a successful empty response.

The existing ownership split is reasonable: `records.ts` owns transport and HTTP failure handling; `Records.tsx` owns query identity, freshness, and presentation. Keep that split. The supplied single consumer does not justify a repository layer, key factory, or custom hook. Cancellation can reduce abandoned work, but tenant-specific keys are the essential correctness fix.

This was a current-state static review of both source files and TASK.md, checked against official Query documentation. No files were edited. Runtime tests were not run because no frontend environment is supplied; the checks above are proposed verification.

Skill and reference files actually read, relative to `.agents/skills/`:

- `craftflow-set/SKILL.md` — review workflow used.
- `craftflow-set/references/quality/review-scope.md`
- `craftflow-set/references/architecture/review.md`
- `craftflow-set/references/quality/review.md`
- `craftflow-go/SKILL.md` — consulted its reference catalog only.
- `craftflow-go/references/tanstack-query/overview.md`
- `craftflow-go/references/tanstack-query/cache-and-keys.md`
- `craftflow-go/references/tanstack-query/requests-and-rendering.md`