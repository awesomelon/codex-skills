# Sources and adaptation

Checked: 2026-09-15. Guidance targets TanStack Query v5; verify APIs against the consuming project's installed version.

## Upstream

- Source: Deckard Gerritsen's [TanStack Query skill](https://github.com/DeckardGer/tanstack-agent-skills/tree/b2fc14c974b2ca09b38de09c28237f240175205b/skills/tanstack-query), commit `b2fc14c974b2ca09b38de09c28237f240175205b`.
- Original entrypoint name: `tanstack-query-best-practices`. This collection uses `tanstack-query-guard` to identify its review and correction role, following the existing guard skill names.
- The upstream MIT notice is included unchanged as [LICENSE](../LICENSE), so standalone copies retain attribution and license terms.

This is an adaptation, not an official TanStack release or an automatic upstream mirror. The original entrypoint and 38 rule files were reviewed. Criteria are grouped by task instead of copying the full example catalog or universal priority rankings.

| Upstream rules | Local coverage |
| --- | --- |
| `qk-*`, `cache-*`, `err-fallback-data`, `perf-placeholder-data` | [Cache and keys](cache-and-keys.md) |
| `err-error-boundaries`, `err-retry-config`, `query-cancellation`, `parallel-use-queries`, other `perf-*` | [Requests and rendering](requests-and-rendering.md) |
| `mut-*` | [Mutations](mutations.md) |
| `inf-*`, `pf-*` | [Pagination and prefetch](pagination-and-prefetch.md) |
| `ssr-*` | [Server rendering](server-rendering.md) |
| `network-mode`, `persist-queries` | [Offline and persistence](offline-and-persistence.md) |

## Corrections and conditional choices

- Replace mandatory invalidation with the choice between complete response updates and targeted refresh. Optimistic writes, key factories, memoization, fixed cache durations, and new dependencies need a task-specific reason.
- Correct `onSettled`'s saved-value argument position; distinguish it from the additional callback context in current v5 types. Add cache-miss and overlapping-write considerations to snapshot rollback.
- Do not promise request cancellation merely because `enabled` becomes false or a component unmounts. Preserve signal-consumption and Suspense limitations.
- `select` can rerun when its function reference changes, not only when data changes. Placeholder data does not force an offline/disabled query to fetch.
- Keep cache-first `ensureQueryData` distinct from awaiting a refresh with `fetchQuery`. Consumer freshness is not inherited from a prefetch-only option.
- Replace the unsupported `hydrateOptions.shouldHydrate` example with documented persistence controls. Include restored mutation functions and account-specific storage handling.

The official TanStack guides linked beside each topic and [query-core implementation](https://github.com/TanStack/query/blob/main/packages/query-core/src/queryClient.ts) were used to check these distinctions. Upstream source and official documentation may evolve independently; updates should reassess changed behavior rather than copy wording blindly.

## Skill authoring

The user-designated [OpenAI article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) informs the concise selection description, topic-specific references, and conditional decision criteria. Installation does not add always-active instructions or require unrelated audits. Evaluation material stays outside the installable skill.
