# Release 1.0 contract suite

This directory implements the first evaluation slice from the [release design](../../docs/rung-1.0-design.md). It contains 13 contract cases and independent artifact assertions. Actual execution belongs in [run records](../runs/2026-10-03-native-pilot/results.md), not this scenario definition.

The [manifest](manifest.json) selects fixtures, the explicitly invoked skill, editable files, and manual acceptance criteria. Each attempt records input/resource hashes, invocation, available runtime evidence, artifacts, and outcome. The task is identical across variants; the Rung variant adds its invocation in a separate wrapper and copies the current source packages. The runner supports `control` and `rung`. The stability qualification uses the unchanged Rung payload; it does not add a redundant candidate arm or claim comparative superiority.

| Case | Automated assertions | Evidence still requiring inspection |
| --- | --- | --- |
| Wrong diagnosis | Preserve the correct encoder; verify true, false, and omitted preferences through independent assertions; preserve tests and inputs | Explain the stale diagnosis and actual cause; report real checks and unavailable production confirmation |
| Review scope | Preserve file inventory, bytes, Git HEAD, index entries, working-tree status, and Git configuration | Identify cross-tenant cache reuse with a supported consequence and accurate review scope |
| Stale result | Verify slug behavior with mixed whitespace, Unicode, empty input, and existing hyphens; preserve captured results and tests | Reject the old snapshot as current verification evidence and report checks actually run |
| Routine | Match the exact requested spelling replacement and preserve every other input | Catalog/resource evidence for interpreting the control/Rung comparison |

Correct artifacts do not establish correct explanations or resource selection. Manual criteria are intentionally not replaced by phrase or heading matching. No automatic process in this slice marks them satisfied. `catalog_verified` records a pre-turn host prompt audit: the control must contain neither Rung name, while the Rung arm must advertise both current names. This is context evidence, not proof of implicit selection or every subsequent resource read. A completed model response may therefore remain `inconclusive` even when artifact checks pass.

The [qualification plan](../runs/2026-10-03-qualification/plan.json) adds valid diagnosis reuse, undefined outcomes, quality evidence, shared responsibility, interrupted effects, verification repair, changed instructions, and two independent-skill configurations. The manifest freezes each manual criterion, writable scope, and copied fixture provenance. Standalone cases install only their selected skill. The original four-case pilot remains a separate immutable batch.

For interrupted effects and verification-driver checks, independent assertions run on a disposable artifact copy with task-local temporary storage. This permits required data writes while preserving the assessed originals. Positive/negative controls reject the broken fixture and accept the relevant repair.

## Fixture provenance

The preference module, tests, diagnosis record, and task are copied from the [September 29 stale-diagnosis fixture](../astra-audit-followup-2026-09-29/fixtures/stale-diagnosis/TASK.md). The slug module, tests, and captured result come from the [October 3 async fixture](../long-running-2026-10-03/fixtures/async-result/TASK.md); its task removes the skill invocation so both arms share the same input. The routine README comes from that run's [routine fixture](../long-running-2026-10-03/fixtures/routine/README.md), with a neutral task. The tenant-cache review is a new synthetic fixture with staged code, unstaged notes, and untracked user work. Historical records remain unchanged.

`checks.py` is held outside model inputs. Its author-created positive and negative controls run in `tests/test_evaluate.py`; those controls validate the checker and runner, not model behavior. The review's semantic acceptance remains manual even when preservation passes.

## Run a bounded attempt

Use the development environment from [CONTRIBUTING](../../CONTRIBUTING.md#development-setup), with Python 3.10+, Git, and Node.js for the preference case. Model execution currently requires macOS, an available Codex CLI, and a host that permits Seatbelt execution. Linux CI can run deterministic tests but does not establish macOS runtime compatibility.

Each destination must be new. Choose another destination when repeating a command; existing records are never overwritten.

```bash
python scripts/evaluate.py preflight --out /tmp/rung-preflight-example
```

`ready_for_probe` establishes only the tested filesystem boundary and CLI option availability. It does not establish model startup, model selection, skill discovery, or a clean control catalog. A `blocked` result exits 2 and preserves the diagnostic.

After resolving preflight limitations, select a fixed evaluation profile and an attempt ceiling. For one explicit feasibility attempt:

```bash
python scripts/evaluate.py run --case routine --variant control --timeout 60 --out /tmp/rung-routine-control-1
```

Use `--variant rung` for the current package. `--model` and `--effort` are optional explicit selections; otherwise requested settings are recorded as inherited/unknown. Resolved settings remain unknown unless independently observed. Do not compare arms with uncontrolled model settings. The command makes at most one model invocation, with no retry or batch loop. Startup diagnostics count against the agreed invocation ceiling. No additional credits are purchased by this tool.

The runner uses Codex's native macOS command sandbox. Preflight proves that commands cannot read the source repository or private evaluation state, can write the disposable work directory, and cannot write outside it. Each child CLI receives a fresh `CODEX_HOME` and `TMPDIR`; the parent environment, real user configuration, and installed skills remain unchanged. Apps, plugins, web search, and multi-agent execution are disabled for the comparison. These are comparison constraints, not Rung execution rules.

The CLI uses a temporary reference to its existing native authentication file. The runner does not open or copy credentials, removes the reference on exit, and denies model tools access to both state and the original Codex directory. Native authentication must already exist. No outer Seatbelt wrapper is used: experiments showed that it prevents the CLI from establishing its own command sandbox. Isolation is tested before model invocation rather than bypassed after failure.

The completed [native pilot](../runs/2026-10-03-native-pilot/results.md) supersedes the startup limitation in the preserved [initial record](../runs/2026-10-03-pilot/results.md).

## Inspect and reassess

`record.json` separates process exit, scope preservation, artifact assertions, response text, usage, manual criteria, and overall outcome. Missing usage/cost is unknown. `model_attempted` means that the CLI invocation was attempted; it does not mean a model responded. CLI JSONL and stderr are retained in the process record. CLI JSON can omit code-mode tool calls. New attempts therefore also keep selected tool calls/outputs and observed model/effort from the matching session in the temporary CLI state. Unrelated sessions, reasoning items, and unrelated metadata are not exported. Missing, truncated, or ambiguous traces are labeled; a partial trace never confirms resolved settings. The temporary CLI session is deleted with confirmed process-group cleanup. This diagnostic evidence does not retroactively fill gaps in older ephemeral runs. Review records retain Git state as data; exported artifact folders contain files, not an embedded `.git` repository.

For cases without Git state, recheck an exported file tree without another model call:

```bash
python scripts/evaluate.py check --record /tmp/rung-routine-control-1/record.json --workspace /tmp/rung-routine-control-1/artifacts
```

This prints a new artifact assessment and never replaces the original record. A successful `check` exit establishes artifact assertions only; manual and catalog evidence remain separate. Review reassessment requires the original Git state; the exported file tree alone cannot freshly prove index preservation. Preserve the original recorded Git observations rather than relabeling file-only checks as a complete review recheck.

```bash
python scripts/evaluate.py report /tmp/rung-routine-control-1/record.json
```

`report` counts all supplied attempt outcomes, rejects duplicate identities, and leaves comparative conclusions and cost per successful task unknown. Assess comparability using [the comparison method](../comparison.md). Retain failed and blocked attempts when constructing a bounded batch; a selected subset is not the full batch denominator.

A timeout or interrupt terminates the owned process group. The record describes group cleanup only; detached or remote descendants are not thereby proven stopped. If cleanup is unconfirmed, the tool retains the temporary workspace, skips artifact acceptance, and reports `inconclusive`. Inspect only owned processes before any cleanup or retry.

## Results and limits

The [24-attempt pilot](../runs/2026-10-03-native-pilot/results.md) demonstrated executable comparison and correct artifacts in both arms, without demonstrated additional benefit. The maintainer then adopted a stability-and-compatibility release policy. The [qualification record](../runs/2026-10-03-qualification/results.md) separates 13 contract attempts, two installed-plugin tasks, distribution checks, and author adjudication. Raw `inconclusive` classifications remain unchanged when a separate manual assessment passes.

Assigned skill copies under saved `artifacts/.agents/` are omitted from Git after verifying their unchanged hashes. The records retain their full inventories and source revision; `skills/` remains the single maintained source. Local copies are preserved. Tool calls/outputs and task artifacts remain in the records. No reasoning items or native credentials are exported.

These synthetic explicit-invocation samples do not establish comparative superiority, universal task reliability, implicit selection, desktop activation, or live steering/cancellation/compaction behavior. See the [compatibility contract](../../docs/compatibility.md).
