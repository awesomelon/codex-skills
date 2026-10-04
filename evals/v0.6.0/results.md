# 0.6.0 candidate — 2026-10-04

Status: implementation and local checks completed; behavioral release acceptance blocked. The repository manifest remains `0.5.5`. No 0.6.0 release was created. After reviewing the implementation results, the user authorized committing and pushing the candidate source; source publication does not satisfy the behavioral release gate.

## Implemented scope

- Go's performance reference now distinguishes completed work from fast failures or work outside the timer, compares configurations for the actual decision, and separates an observed difference from its causal explanation.
- Get Set can assess those measurement conditions independently using its existing measurement reference.
- Go's learning reference and routing now cover proportionate executable prevention of recurring errors, including rejection of the original behavior and preservation of legitimate independent policies.
- An opt-in CLI comparison runner, ten cases, independent artifact checks, and a separate response-review rubric support future matched evaluations. The installed plugin still contains only the two skills.

These are selective adaptations of the pinned pstack sources documented in Go's source history. Baseline model behavior could not be sampled, so the additions address identified instruction boundaries rather than demonstrated baseline model failures. No measured behavioral, latency, token, or cost improvement is claimed.

## Model execution

Baseline skills were copied from main `0925ce0ac0bc3ddbd56f722d9e86befb20486098`, whose tree matches v0.5.5. Candidate skill bytes are recorded in [comparison.json](evidence/comparison.json). The CLI is `0.159.0-alpha.3` on Linux.

A minimal direct preflight initialized successfully but returned HTTP 401 while accessing the model service. The CLI reported that its access token could not be refreshed. The completed runner's preflight encountered the same failure. Neither received a model response. No credentials were collected, login flow started, or user authentication/configuration modified to resolve it.

| Work | Actual outcome |
| --- | --- |
| Direct minimal model preflight | Blocked by authentication; not a case evaluation. |
| Runner minimal model preflight | Blocked by authentication; no case launched. |
| Ten cases × two variants × three repetitions | All 60 planned attempts are `not_run`. |
| Model task successes / failures | Unknown; zero completed case evaluations. |
| Actual model/reference selection | Unverified. |
| Resolved model, effort, token use, cost | Not exposed; unknown. |

See the saved [preflight events](evidence/preflight-events.jsonl), [stderr](evidence/preflight-stderr.txt), and [direct preflight](evidence/direct-preflight.json). Elapsed times measure failed initialization/authentication, not model response speed. The runner explicitly records that workspace separation does not establish cross-workspace read isolation; no fully blinded comparison is claimed.

## Structural and checker validation

The full repository test suite passed **84 tests** on the available Linux environment, including eight new runner tests and eleven fixture-control tests. [Saved test output](evidence/unit-tests.txt). These are code and checker tests, not independent model evaluations.

The controls accepted completed export timing, shared catalog ownership with a real regression test, independent policies, and preserved review inputs. They rejected unfinished work, protected-input changes, copied-policy drift, assertion-free or import-error-only regression tests, coupled policies, and extra output files. Runner checks cover nonzero exits, timeout, absent CLI, symlinks, blocked preflight accounting, and artifact success without response acceptance.

Both skills passed `python3 scripts/validate.py`. Installer shell syntax and whitespace checks passed. Source references remain portable. These checks do not establish the quality of model decisions, automatic discovery, or live steering.

[Candidate content hashes](evidence/candidate-manifest.json) identify the skill, runner, checker, and test sources reviewed for this result.

## Installation evidence

Only temporary configurations and destinations were used. The staged installation copy used `0.6.0-rc.1` solely to distinguish candidate bytes from the installed baseline; that version was not written to the repository manifest or published.

| Path | Actual result | Limit |
| --- | --- | --- |
| Linux CLI, clean local marketplace install | Candidate installed and enabled; all 60 skill files matched source bytes. | No model session. |
| Linux CLI, baseline → local candidate | Installed 0.5.5, changed the local source, removed/reinstalled, then verified 0.6.0-rc.1 and all 60 skill files. | Reinstall path, not Git marketplace upgrade. |
| Local `marketplace upgrade rung` | Rejected because the source is not a Git marketplace; installed listing remained 0.5.5. | Expected source-type limitation; not counted as an upgrade pass. |
| Independent Get Set / Go copy installations | Each installed alone into a separate destination; source file bytes matched. | Packaging only; independent model behavior unverified. |
| Git marketplace update to final 0.6.0 | Not run. | Candidate was not published. |
| macOS host installation | Not run. | Linux results are not macOS validation. |
| New-session use and automatic discovery | Not run. | Model authentication remains unavailable. |

Saved [installation results](evidence/installation.json) include command outputs and candidate hashes. The existing CI workflow was not changed or triggered remotely; the local tests do not establish a fresh macOS CI result.

## Release disposition and next action

Keep this as an unvalidated 0.6.0 candidate. The design's behavioral release gate is not met, so the final version bump and publication are deferred. The two endpoints, invocation metadata, and skill-only packaging remain intact.

With host authentication restored, run [the comparison procedure](README.md) in a new output directory, inspect actual responses and traces against [the independent rubric](review.md), and record both failures and successes. Reduce guidance already handled by baseline behavior. Fix and reevaluate any regression. Then perform real-host standalone/discovery checks and the declared installation/support matrix, refresh evidence for changed bytes, and decide whether a 0.6.0 release claim is justified.
