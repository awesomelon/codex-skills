Updated only `records.mjs` using the supplied skill:

- Added tenant identity to cache keys.
- Made HTTP failures reject.
- Forwarded the cancellation signal.

Preserved the exported API, URL encoding, and 60-second freshness policy. All five local checks pass with `node check.mjs`.
