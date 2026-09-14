# Independent React review output

> English translation of a historical record. [Original at the pre-translation commit](https://github.com/awesomelon/codex-skills/blob/ce11c34e3d1da77140087300218b776594bb65cf/evals/skill-audit-2026-09-12/outputs/react-review.md). Reported runs, hashes, and counts describe the original work, not this translation.

Final response from a separate agent. The original record changed only file links to repository paths.

No source or configuration was modified. Static review found two significant issues.

1. **High — Tenant caches are not isolated.** In [Documents.tsx](../../react-quality-guard/fixtures/review/Documents.tsx), `Documents` line 16 fixes the key at `['documents']`. Switching tenants in the same QueryClient can reuse the previous list. Its editors receive the new `tenantId`, so a save may combine the previous document's ID/title with the new tenant. Actual persistence depends on API behavior. **Smallest remedy:** use `['documents', tenantId]` and do not pass the previous list as temporary data during tenant switching.

2. **Medium — Refetch failure can lose unsaved input.** `Documents` line 20 removes all editors based only on `isError`, even when cached data remains after background-refetch failure. Recovery remounts `TitleEditor`, replacing the edited title with the server title. **Smallest remedy:** distinguish initial failure without data from refetch failure, keeping editors mounted and displaying an error separately for the latter.

Preserve these parts:

- `TitleEditor`'s `useState(document.title)` is an independent editing initial value. Synchronizing it with an Effect on every refetch could overwrite the unsaved title. Keep the existing key containing tenant and document IDs.
- Creating the default callback inside `HelpButton` does not itself defeat memo's props comparison. It does not justify adding useCallback.
- Preserve `saving`, disabled save buttons, and failure alerts.

**Verification limits:** Read only supplied code and dependency declarations without network, installation, or file changes. Did not run the app, type checks, or performance measurements. `api.saveTitle` internals were absent, so post-save cache behavior could not be established. Missing invalidation in the component alone was not treated as proof of missing updates. After a fix, check tenant switching, successful/failed refetch and recovery during editing, and retry after save failure.
