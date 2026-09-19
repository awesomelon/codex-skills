# Pstack validation results

Date: 2026-09-19. Repository baseline: `145acdd41d130eb6979372bc36a195f4a5b62183`. Upstream: `cursor/plugins@032be146865d973682535de75f2287da438550bf`. Candidate branch: `feature/pstack-codex-skill`.

Validation took place in a separate local checkout before publication. The evaluation runs did not push, open a PR, merge, modify installed skills, or change Codex configuration. The user's application repository was not edited. Subsequent commit and PR publication are separate from the evaluation results below.

## What was built

A standalone `pstack` skill with a 4,649-byte entrypoint, six task references, optional UI metadata, source/adaptation record, and the original MIT notice. The upstream `poteto-mode` entrypoint is 18,713 bytes. These are UTF-8 file sizes, not token counts or a measured speed/quality improvement; the adaptation intentionally has a narrower scope.

The skill adds task orchestration to the existing collection without requiring the domain guards. It retains reproduction, comparable measurements, reviewed evidence, scoped delegation, and continuation. Cursor-specific commands/models, blanket skill chains, automatic PRs, broad external-action grants, cleanup, and the automation runtime are omitted. See [the source record at the evaluated revision](https://github.com/awesomelon/codex-skills/blob/02b3906e4a45cc4ea151df19c379248da30d62a7/skills/pstack/references/sources.md) for the exact scope.

## Executed structural and installation checks

Environment: macOS 27.0, Apple Bash 3.2.57, Python 3.12.14, Node.js v24.16.0. The default system Python was 3.9.6, so repository development checks used the existing bundled Python 3.12 runtime. PyYAML 6.0.3 was installed only into a disposable validation directory after the bundled quick validator initially reported a missing dependency. The skill and shell installer do not require Python, PyYAML, Node, or package installation.

- `scripts/validate.py` passed all seven skills, including local reference portability.
- The bundled `skill-creator/scripts/quick_validate.py` passed the candidate and its standalone installed copy.
- The shell installer discovered `pstack`; selected dry-run, link installation, repeated link installation, copy installation, and repeated copy installation passed in temporary paths.
- Copied skill files were byte-identical to the source; the symlink resolved to the intended source folder. No real user skill directory was used.
- UI metadata was parsed and checked against the frontmatter and invocation name. The upstream license was preserved byte-for-byte.
- The final change passed whitespace and added-document link checks.

Commands, exit codes, environment information, input hashes, skill hashes, and before/after workspace hashes are in [manifest.json](outputs/manifest.json). The final packaging checks are in [final-checks.json](outputs/final-checks.json).

## Fresh-agent execution

Three separate subagents received only the copied candidate skill, a concrete request, and their raw fixture. They did not inherit the author's conversation, intended solution, case rubric, or other agents' conclusions. Runtime instructions and the available skill catalog were still present, so these runs do not isolate the skill's causal effect. All used the parent-configured model and effort; no model override or extra delegation was requested.

| Case | Observed result | Evidence |
| --- | --- | --- |
| 1. Async bug fix | The agent reported 2 existing tests passing, then a new stale-result regression failing, followed by a fix and 10 tests passing. The coordinator inspected the implementation and independently reran all 10 tests. | [Agent report](outputs/implementation-report.md), [resulting source](outputs/implementation/search.mjs), [test output](outputs/implementation-tests.txt) |
| 2. Read-only diagnosis | The agent reproduced stale success/error and clear behavior with in-memory checks, identified unguarded completion publishing, and separated controller evidence from untested UI behavior. | [Agent report](outputs/investigation-report.md); every workspace file hash and path remained unchanged. |
| 3. Stale PR status | The agent rejected current green/readiness claims based on old-head checks and approval, unknown mergeability, and an unresolved thread. It treated the embedded action request as comment data and reported the snapshot/live-state limit. | [Agent report](outputs/status-report.md); every workspace file hash and path remained unchanged. |

Only `implementation/search.mjs` and `implementation/search.test.mjs` changed across all three workspaces. All copied skill bytes stayed unchanged. Delegated command sequencing comes from the agent's report, not a preserved full tool transcript; the coordinator's rerun and file inspection are separate evidence.

The coordinator also ran eight acceptance cases withheld from the implementing agent. The original implementation passed two and failed six, confirming fixture sensitivity; the resulting implementation passed all eight. They cover late success/failure, clearing, identical repeated queries, active errors, the newer loading state, and independent controllers. See [baseline output](outputs/baseline-acceptance.json), [final output](outputs/final-acceptance.txt), and [acceptance source](acceptance.test.mjs). These are controller tests, not browser or production tests.

A separate read-only reviewer inspected the upstream and completed package. It found no material portability, scope, contradiction, or overlap issue, and independently confirmed the license bytes. Its observation that this results document was initially absent was resolved before delivery. The review does not substitute for runtime checks.

## Limits and promotion judgment

The executed examples support local use as an addition candidate. They do not establish superiority to upstream or to running Codex without this skill, automatic invocation/non-invocation accuracy, model-wide reliability, or reduced token use/latency.

Cases 4–16 and 18 in [cases.md](cases.md) remain unexecuted as fresh-agent scenarios. No live GitHub mutation, scheduler, stacked merge, production profile, UI verification, or worker handoff was exercised. The three agent runs used explicit invocation; skill discovery was checked structurally and through installer listing, not through automatic model selection. The unchanged installer/validator regression suite was not rerun because those implementations did not change.

Repository publication does not enable a global mode, automatic monitor, or personal skill installation.
