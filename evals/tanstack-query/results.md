# TanStack Query validation

Date: 2026-09-15. Environment: macOS; exact tool versions and file hashes are in [manifest.json](outputs/manifest.json).

## Structure and installation

- Repository `scripts/validate.py`: all four skills passed metadata, portable contents, and local-reference checks.
- `skill-creator` `quick_validate.py`: passed for `tanstack-query`. Generated and parsed the UI metadata with PyYAML in a temporary Python environment; PyYAML is a development-check dependency, not a skill installation requirement.
- The unchanged Bash installer discovered the new skill. A selected copy preview wrote no files; standalone link and copy installations and repeated installation succeeded in disposable directories. Every installed skill file matched the source, including the original MIT notice. Commands are recorded in [install-checks.json](outputs/install-checks.json).
- Repository `AGENTS.md` matched its starting Git content. Existing installed user skills and the installer/validator implementations were not changed.

## Independent explicit-invocation runs

Each fresh, ephemeral Codex CLI run used `gpt-6-astra` with high reasoning effort. It received the standalone skill location, a fixture's TASK.md, and resource/edit restrictions. Neither run received the expected findings, another run's answer, or the scenario catalog. Review used read-only access; implementation could change only its disposable `records.mjs`. Model execution was network-connected, but task tools were instructed to use local inputs only; recorded commands stayed within those inputs.

The manifest preserves the raw final responses. Display copies remove trailing spaces, add a final newline, and point review links at the repository fixture; their wording is unchanged.

| Run | Observed result |
| --- | --- |
| [Review](outputs/review.md) | Identified tenant collisions in both read and write keys and next-page loading during background refresh. Accepted the complete-response cache write without inventing mandatory invalidation. Before/after hashes confirm no input changes. |
| [Implementation](outputs/implementation.md) | Changed only `records.mjs`: separated tenant keys, rejected HTTP failures, and forwarded cancellation. Kept the API, encoded request inputs, and 60-second freshness policy. |

The executable fixture uses the real `@tanstack/query-core` **5.102.8** with fake HTTP responses and Node assertions. [Before](outputs/implementation-before.txt), tenant isolation, error rejection, and cancellation failed, while cache reuse and URL encoding passed. [After](outputs/implementation-after.txt), all five checks passed in the independent agent run. The original check and other input files retained their hashes; the parent process inspected the saved result and did not rerun a sufficient successful check.

The saved [implementation](outputs/records.mjs) is evaluation output. The intentionally broken [fixture](fixtures/implementation/records.mjs) remains unchanged so the failure can be reproduced.

## Reproduce

From the repository root, use a disposable directory:

```bash
evaluation_dir=$(mktemp -d)
cp -R evals/tanstack-query/fixtures/implementation/. "$evaluation_dir/"
```

In that directory, `npm ci --ignore-scripts --no-audit --no-fund` installs the pinned test dependency. `node check.mjs` must fail on the original fixture. To inspect the saved successful result, copy `evals/tanstack-query/outputs/records.mjs` from this repository over the disposable `records.mjs`, then run `node check.mjs` again. For a fresh model evaluation, provide TASK.md and the standalone skill instead of the saved result. Keep generated outputs separate from the fixture.

## Limits

These are two explicit-invocation samples, not proof of automatic selection, repeatability, or all [15 cases](cases.md). Browser rendering and React hook mounting were not tested. v4, other v5 releases, concurrent optimistic rollback, SSR, and offline persistence were checked as guidance against sources but not executed end to end. No performance improvement was measured. Installer/validator code was unchanged, so the full installer unit suite was not rerun; the new skill's installation was exercised directly instead.
