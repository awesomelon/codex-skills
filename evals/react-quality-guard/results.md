# React Quality Guard validation records

> English translation of a historical record. [Original at the pre-translation commit](https://github.com/awesomelon/codex-skills/blob/ce11c34e3d1da77140087300218b776594bb65cf/evals/react-quality-guard/results.md). Reported runs, hashes, and counts describe the original work, not this translation.

Validation date: 2026-09-12. Environment: Linux container.

## Installation and structure

- skill-creator `quick_validate.py`: passed frontmatter/name validation.
- Repository `scripts/validate.py`: both skills passed basic metadata and skill-local relative references.
- All 24 existing installer tests passed. No installer code was added or changed.
- In temporary paths, verified automatic discovery of both skills, complete link/copy installation, non-mutating preview, reruns, and React-only selection. Installed files matched source.
- Parsed UI YAML and checked explicit-invocation examples.

## Behavioral method

Inputs are preserved as the [review task](fixtures/review/TASK.md) and [implementation task](fixtures/implementation/TASK.md). Each folder was copied into a separate temporary workspace, and an independent agent received only the skill path and task. No expected answer, issue location, or other evaluation result was supplied.

Before/after file hashes checked review immutability. Implementation diffs checked requested behavior, public props, and edit scope. Run-time skill hashes are in [manifest.json](outputs/manifest.json). These are behavioral samples, not actual React runtime tests.

## Results and one correction

| Run | Observation | Judgment |
| --- | --- | --- |
| Initial independent review | Found tenant caching and draft loss after refetch failure; preserved files. Also asserted missing post-save cache updates despite omitted API internals. | Needed stronger evidence distinctions |
| Independent implementation | Used non-mutating filtering/sorting and removed derived state/Effect. Preserved public props and display/input/selection JSX; edited only the target component. | Scope and static behavior preservation checked |
| Fresh review after correction | Distinguished two directly supported issues from an API contract requiring inspection. Avoided unnecessary draft/save-pending/memo changes and preserved input hashes. | Met criteria for this sample |

After the first review, added one criterion to `performance.md`: do not assert missing cache updates when API adapters or shared mutation implementations are omitted. Reevaluation received only the revised skill and a fresh original input copy. This changed evidence-level guidance, not calculation/state criteria used by the implementation case.

Saved the final [review output](outputs/review-final.md) and [implementation output](outputs/DocumentPicker.tsx). Nine [Node checks](outputs/check-picker.mjs) extracting the actual calculation passed, and the recording script reconfirmed them. Coverage included sorting, equal-title order, source immutability, case-insensitive search, empty results, whitespace semantics, empty input, new props, and element identity. Do not interpret these as React-rendering or type-check passes.

## Limits

- Executed two types of explicit-invocation cases and repeated only review once after correction. This does not establish all [14 scenarios](cases.md), automatic selection, or repeatability. No separate model-version identifier was collected.
- React/Vite versions in fixtures are input conditions. Runtime dependencies were not installed; React DOM rendering, type checks, and browser interactions need separate validation.
- Render time, bundle size, and network-latency improvements were not measured.
- Installation and Codex invocation on macOS hardware were not verified. Actual installed user skills and global configuration were unchanged.

## Rerun

Run installation/structure checks from the repository root:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

For behavioral checks, copy the fixture elsewhere and submit TASK.md to `$react-quality-guard`. Save outputs separately without overwriting the original fixture.

With Node.js available, rerun saved-implementation calculations using `node evals/react-quality-guard/outputs/check-picker.mjs`. Node.js is required for this evaluation check only, not for skill installation.
