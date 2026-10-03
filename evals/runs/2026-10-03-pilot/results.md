# Release 1.0 evaluation execution slice

The maintainer requested implementation of the [1.0 design](../../../docs/rung-1.0-design.md) on 2026-10-03. This work implements a bounded evaluation runner, four pilot fixtures, independent artifact assertions, and deterministic regression coverage. The installed skill payload and plugin version remain 0.5.5. No commit, publication, plugin installation, or user configuration change was performed.

## Actual runtime observations

| Observation | Result | Limit |
| --- | --- | --- |
| Nested Seatbelt probe | `sandbox_apply: Operation not permitted` | The current outer sandbox does not permit applying another Seatbelt profile. No model invocation occurred. |
| Reviewed host-level Seatbelt preflight | Repository read denied, disposable workspace write allowed, outside write denied; CLI help/version available | Establishes those local boundaries, not clean model context or model execution. See [preflight record](preflight-host/preflight.json). |
| First startup diagnostic | Codex CLI 0.158.0 exited 1 before any JSONL model output | App-server initialization failed with `Operation not permitted (os error 1)`. See [attempt](startup-1/record.json). |
| Bounded diagnostic retry | Same failure after moving `TMPDIR` into the owned state directory | No model output; no behavioral comparison. See [retry](startup-2/record.json). |
| Implemented runner under the current outer sandbox | Wrote an explicit blocked record after its isolation preflight failed | No CLI model invocation; the routine fixture remained unchanged. See [record](runner-blocked/record.json). |

Both startup diagnostics used a disposable typo fixture, `--no-daemon`, `--strict-config`, `--ignore-user-config`, `--ephemeral`, JSON output, temporary SQLite/log locations, and command filesystem/network restrictions inside an outer Seatbelt policy. The initial diagnostic also requested an output-message file; the reusable runner reads JSONL instead. The prototype profile allowed writes within its whole disposable attempt root, while the reusable runner narrows writes to its work/state subdirectories. These are related startup observations, not executions of the final runner's model path.

The two startup records preserve commands, prompt, stderr, empty output, profile, and unchanged artifact. Their elapsed time and resolved model/effort were not captured and remain unknown. The first prototype waited for the process leader; descendant cleanup was not independently audited. Neither invocation timed out. A later host preflight demonstrates that the outer filesystem policy can execute, but does not identify the remaining initialization failure's precise cause. No claim is made that a particular host setting or missing credential caused it.

There are **zero completed model evaluations**. The 24-attempt comparison pilot has not started. Two CLI startup invocations and one runner preflight rejection are retained as three blocked attempt records; two additional preflight records are diagnostics, not model attempts. There is no observed quality improvement, discovery rate, typical model latency, or measured saving. The two model diagnostics ran before the reusable runner was finished; source hashes in later records identify their actual local code rather than pretending the final implementation was exercised earlier.

## Implemented behavior

- `preflight` inspects runtime/options and tests concrete filesystem restrictions before any model call.
- `run` prepares disposable control or Rung inputs, preserves source/resource hashes and Git semantics, captures one bounded invocation, and writes a new record without overwriting earlier evidence.
- `check` independently reassesses artifact behavior and protected inputs. Findings, truthful reporting, and catalog selection remain separate manual/unverified dimensions.
- `report` retains all supplied outcome categories, rejects duplicate attempts, and does not infer improvement or cost from process success.

The [pilot guide](../../release-1.0/README.md) documents commands and limitations. The CLI adapter does not yet attest a clean catalog or provide manual adjudication, so even a correct artifact cannot automatically become a qualified comparative success. This limitation is intentional and visible in the outcome record.

## Verification

Repository checks used Python 3.12.14 and pinned PyYAML 6.0.3 in a temporary virtual environment. The system Python was 3.9.6 and lacked PyYAML; no user Python environment was changed. The source validator passed both unchanged skills, and `/bin/bash -n scripts/install.sh` passed. Existing Linux/macOS CI already discovers the new deterministic test file; no model key or CI configuration was added.

The new tests exercise author-created positive/negative fixture controls, protected files, extra artifacts, staged/unstaged/untracked state, changed Git configuration, zero-exit-without-assertion cases, startup failure, timeout, interruption, uncertain cleanup, missing catalog evidence, duplicate records, and output preservation. They use fake model processes or trusted fixture controls and are not model evaluations. Initial integration and CLI control results are recorded in [validation.json](validation.json).

Final local review removed an unnecessary byte-format restriction on the already-correct encoder. Independent input/output assertions still reject behavioral regressions, while a new control accepts equivalent formatting. The final full regression run passed **96 tests, including 31 new evaluation tests**; [validation-final.json](validation-final.json) and [the test log](tests-final.txt) retain the command, result, and final code hashes. No model checks were rerun or inferred from this correction.

## Next prerequisite

Use a host-supported isolated configuration that can initialize Codex while preserving the source/checker read boundary, existing user assets, and actual control-catalog separation. Do not relax those conditions or rerun the same failed configuration repeatedly. Once one routine execution produces a response and independently accepted artifact, audit its observed context/settings, then run the planned four-case pilot within a fixed invocation ceiling. The full qualification suite, live continuity, installed-host discovery, release-candidate decision, and publication remain outstanding.
