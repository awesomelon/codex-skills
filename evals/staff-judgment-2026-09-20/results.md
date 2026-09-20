# Staff engineering judgment evaluation — 2026-09-20

## Change and method

Base: `03a90c2`. This revision extends Engineering Orchestrator from delivery coordination into problem selection and uncertain execution planning, and strengthens Architecture Guard's consequential design assessment. Existing implementation and integration guidance remains in place. README and UI/plugin descriptions reflect the broader use cases.

The author freshly read the user-designated [staff-engineering article](https://lalitm.com/post/find-problems-staff-engineer/) and [Astra authoring article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). Article-derived discovery guidance is separated from this repository's additional planning, operational, and outcome-evidence decisions. Detailed guidance is conditionally loaded; no new skill or mandatory workflow is introduced.

One independent evaluation agent received the raw fixture requests, skill locations, and output locations, with no conversation fork, expected outcomes, author conclusions, or diff. It used the inherited session model/configuration without an override. Four requests ran sequentially in that agent's session; they are not four independent samples. Evaluation instructions required read-only source assessment for the first three and an isolated copy for the typo edit. Raw responses are preserved under `outputs/`; input/output hashes are in `manifest.json`. The author assessed observable decisions, not required wording.

## Observed behavior

| Case | Observed result | Assessment |
| --- | --- | --- |
| 44: investment priority | Prioritized the reproduced chargeable-job incident over frequent friction, counted copied theme requests as one signal, proposed a bounded trace-ID check, and left ROI, reach, and commitments unmeasured. | Met the scoped criteria. No production action or contact was performed. |
| 45: false common solution | Rejected the host-local cache as a complete answer to offline distribution, separated retention/access policies, exposed offline revocation limits, and proposed discriminating measurements without implementing. | Met the scoped criteria. Architecture guidance was available alongside the coordinator. |
| 46: migration strategy | Identified rounding before stringification, sequenced compatible consumers, treated the reader release as unconfirmed, identified export irreversibility, and separated technical acceptance from incident reduction and offline-user impact. | Met the scoped criteria. No implementation or production verification was claimed. |
| 47: routine edit | Changed only `proceses` to `processes` in the isolated README and preserved the task file. | Exact resulting bytes checked by the author; no strategy document was created in the task workspace. |

The author recomputed all recorded input hashes after execution: supplied fixtures and skill inputs were unchanged. The routine result matched exactly the one requested substitution. Expected-case catalogs were not supplied to the evaluator.

## Structural validation

- `python3 scripts/validate.py`: all seven skills passed metadata, UI, portable-content, and local-reference checks.
- `git diff --check`: passed.
- No installer, validator, or application-runtime code changed; the repository regression suite was not repeated locally for these instruction changes. GitHub CI status is separate from this record.

## Limits

These are a bounded behavioral smoke evaluation and author assessment, not a before/after experiment, reliability benchmark, or proof of staff-level ability. No automatic discovery, native plugin installation, macOS runtime behavior, production rollout, adoption improvement, token cost, or latency benefit was measured. The existing implementation cases were not rerun; the new migration response validates planning behavior only. Multi-agent execution itself was not part of the skill behavior being tested.
