# Boundary contracts

Use this guidance for APIs, events, or serialized formats consumed independently of their producer. Start from the existing authoritative contract and its generation path. OpenAPI, AsyncAPI, Protobuf, or JSON Schema may serve that purpose; shared language types suffice only when the actual build and deployment boundary makes them authoritative. Do not introduce a second schema or generator merely to follow this reference.

## Review the contract at its boundary

Identify the producer, consumers, contract owner, and relevant version. Resolve wire-level meaning: absent versus null, defaults, identifiers and numeric precision, enum evolution, errors, ordering, and compatibility where these affect the requested change. Preserve values before serialization; converting an already rounded number to a string does not recover its original identifier.

Keep generated clients, types, fixtures, and mocks derived from the same contract revision. Inspect the real serializer and consumer entrypoint; static types and casts cannot establish that emitted data meets the contract. Behavioral specifications describe desired outcomes, while a machine-readable schema constrains representation. Neither alone proves the running integration.

For a transition, determine which versions must coexist and which consumers are outside the repository. Choose compatible rollout order or an explicit version transition from those constraints. A repository search cannot establish that an external consumer is unused. For parallel work, settle the shared definition and assign one writer before dependent edits.

## Verify the seam

Check representative producer output against independently specified expectations and then exercise its consumer. Include the changed boundary case and required legacy behavior. A round trip can conceal a shared mistake when both implementations drift together. Reuse existing schema validation and integration tests; add a focused check only for a material uncovered risk.

Keep architectural findings separate from runtime input validation details and test results. Record the contract revision and any unexercised consumer or environment in the task's existing evidence. A planning or review request remains read-only unless it explicitly requests a deliverable.

This is an independent adaptation of ECC's [contract-first](https://github.com/affaan-m/ECC/blob/934195f955cf0da847d59fcd6f68856bce112d8b/skills/contract-first/SKILL.md), inspected on 2026-09-20. Its MIT notice accompanies this skill in [third-party notices](../THIRD_PARTY_NOTICES.md).
