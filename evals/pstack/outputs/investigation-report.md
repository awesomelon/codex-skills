# Raw delegated result

Confirmed cause: overlapping searches publish in completion order, with no check that the completing request still represents the latest input.

Each call captures its own `query`, awaits `load(query)`, then unconditionally publishes success or failure at search.mjs:9. Starting a newer search does not invalidate an older request. Clearing publishes `idle` but likewise leaves earlier requests eligible to publish at search.mjs:3. This violates the latest-intent contract in README.md:3.

In-memory deferred-promise checks confirmed:

- New response followed by old response: `loading:cat → loading:dog → ready:dog → ready:cat`.
- Old response while the new request remains pending: `loading:cat → loading:dog → ready:cat`.
- Clearing during a request: `loading:cat → idle → ready:cat`.
- An old rejection can also overwrite newer success with `error:cat`.

Both existing tests pass, but search.test.mjs:5 covers only an isolated success and an isolated clear, without overlapping requests.

The stale controller emissions are reproduced. Actual UI behavior remains conditional on how `publish` is consumed; this directory contains no UI consumer. No files were created or changed.

This record retains the returned prose, with temporary absolute file links replaced by filenames for portability. It is not a full tool transcript.
