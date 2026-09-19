# Notes CLI verification report

**Observed result: save/list and normal export pass; `export --dry-run` violates the documented no-change contract.**

Verified the copied runtime fixture using the explicitly supplied engineering-orchestrator skill and its runtime-verification guidance. No application or skill changes were made. Published paths are normalized and machine-specific environment metadata is omitted.

## Contract and checks

`input/README.md:11` requires notes to persist across processes, export to write all notes, and dry-run to describe its plan while leaving both the data directory and output file unchanged.

| Public operation | Observed result | Verdict |
| --- | --- | --- |
| List with no data directory | Prints `[]`; data directory remains absent. | Pass |
| Add two notes in separate processes | Both print `Saved`; persisted JSON matches independently specified input, including Korean text, quotes, and newline. | Pass |
| List in a later process | Returns both notes in their original order, with their exact text. | Pass |
| Normal export | Prints `Exported`; requested file contains both persisted notes. | Pass |
| Dry-run with populated data and an existing output file | Prints `Would export 2 notes`; output content and modification time remain unchanged, but creates `exports.log` in the data directory. | **Fail** |
| Dry-run with populated data and a missing output file | Prints `Would export 2 notes`; output remains absent, but appends to existing `exports.log`. | **Fail** |
| Dry-run with a missing data directory and missing output file | Prints `Would export 0 notes`; output remains absent, but creates the data directory and `exports.log`. | **Fail** |

All eight application invocations exited 0 with empty stderr. The verification script exits 1 because three dry-run checks fail. Six checks pass, including the application/documentation content-integrity check.

## Failure evidence

On the first dry-run the data directory initially contained only `notes.json`. Afterwards it additionally contained `exports.log` holding the requested output path. `notes.json` itself remained unchanged. On the next dry-run another path was appended to that log. A fresh-directory dry-run created a new directory and log even though there were zero notes.

The observed changes correspond to `input/notes.py:25–27`: directory creation and the append to `exports.log` run before the dry-run condition at line 28. The output-file write is correctly restricted to the non-dry-run branch at line 31. This explains why the output-file portion of the contract passes while the data-directory portion fails.

## Reproduction and retained evidence

The executed recipe created a uniquely named disposable directory, invoked the unmodified public CLI as separate processes, compared persisted state to independently specified values, recorded before/after filesystem snapshots, and removed its disposable directory in `finally`.

`commands-and-results.json` preserves the command arguments, stdout, stderr, exit codes, checks, before/after content snapshots, source hashes, and cleanup confirmation. Absolute paths use placeholders, and machine environment and filesystem timestamps/sizes are omitted. Remaining hashes refer to original observed bytes. For replay, run from the evaluation directory and substitute a fresh disposable directory for `$WORK`; the fixture README documents the CLI. The machine-specific recipe remains outside the published repository.

Verified application SHA-256 before and after execution:

```text
notes.py   a0df50765b57de263810d1de1354ff6973699c02cc4e4589fb8935f5973e0b68
README.md  f049efbf4f7bc3a5e23dde3d6f8f8748c424fdfa3cf63805e61fff08b320f2bb
```

## Cleanup and scope

The owned run directory was deleted successfully. A subsequent directory listing confirmed the run's work directory is empty. Evidence remains outside the disposable data.

Only the designated input, skill, work, and evidence paths were inspected or used. Checks ran locally without network calls, external messages, or real home/configuration changes. No other evaluation folders or repository case/answer files were read. No further agents were delegated.
