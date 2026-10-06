# Retry change notes

Project terms:
- `Delivery`: one queued webhook.
- `Attempt`: one HTTP execution for a Delivery.

Change:
- Retry a timed-out Delivery once after 2 seconds.
- A retry retains `Delivery.id` and creates a new `Attempt.id`.
- If the retry fails, retain the final error.
- Failed Attempts remain recorded even if a later Attempt succeeds.

Rough announcement draft:
"This is a major leap in reliability and dramatically improves performance. The delivery gets another chance. The task runs again after a short delay, and the request finishes successfully."

Supplied evidence for the final change:
- Local test `timeout then success` passed.
- Local test `timeout then failure retains final error` passed.
- No production observation or latency measurement is available.
