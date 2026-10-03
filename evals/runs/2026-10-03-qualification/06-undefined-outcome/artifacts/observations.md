# Collected observations

Support export, 2026-09-29:

- S-31: An analyst says opening a large trace after lunch takes too long.
- S-32: A colleague forwards S-31 to engineering.
- S-33: A workspace administrator says the settings page responds immediately.
- S-34: An analyst says a second query on an already open trace feels fine.

One developer captured the following on one laptop using one 4 GB trace. These are sequential spans, not overlapping measurements. No production percentiles or agreed latency target exist.

| Operation | Transfer ms | Parse ms | Query ms | Render ms |
| --- | ---: | ---: | ---: | ---: |
| Open, fresh session | 1200 | 7400 | 170 | 310 |
| Query, same session | 0 | 0 | 180 | 300 |
| Query, same session | 0 | 0 | 165 | 315 |
| Open, new session | 1150 | 7200 | 175 | 305 |

A backlog note suggests a shared disk cache. The application already holds parsed traces in memory during a session. There is no phase breakdown for other trace sizes, devices, or networks. Large traces may contain restricted data; the current viewer checks authorization when opening them. No persistent cache policy has been agreed.
