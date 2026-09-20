# Request
Use Engineering Orchestrator to plan the approved string-ID migration across producer, browser UI, and external offline reader. Give the plan in your response only. No implementation or production access is available.

# Current contract and evidence
- Producer emits JSON v1 with integer IDs. Some IDs exceed JavaScript's exact integer range and the browser rounds them.
- Offline reader currently accepts only v1. Its owner cannot confirm a release date today.
- Proposed v2 has a version field and decimal string IDs. Legacy v1 import must remain supported. v2 export must never round the original database ID.
- Database currently preserves the original ID as a decimal string; browser state currently stores a number.
- Support has five potentially related wrong-document reports, but duplicates and causality have not been checked. There is no reliable incident-rate baseline.
- Internal producer and browser deployments can be sequenced. A feature flag is available but rollback of exported artifacts cannot make a v1 reader understand v2.
- Success requested: prevent wrong-document access caused by ID precision loss without stranding offline users.
