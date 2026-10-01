Review this proposed optimization and recommend the next engineering action. Do not edit files.

Request: Make the order API respond in 500 ms or less.
Proposal: Add a shared response cache and scale to four replicas.
Available evidence: A developer laptop run on 1,000 synthetic orders reports a mean of 420 ms at 20 requests/second. Production traces, traffic distribution, an agreed percentile, and an accepted measurement window are unavailable. Existing product requirements require read-your-writes after updating an order. No cost budget or accepted freshness change is recorded.
