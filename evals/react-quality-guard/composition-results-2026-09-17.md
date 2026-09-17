# Composition guidance validation

Date: 2026-09-17. Environment: macOS, Python 3.9.6. Repository starting commit: `89f336a5757caa0d727a51be17be636b526097a2`.

## Scope and source review

Added [composition guidance](../../skills/react-quality-guard/references/composition.md), connected it to the existing skill and correctness reference, and added [cases 23–30](cases.md). Discovery metadata and UI invocation settings remain unchanged.

Compared the addition with the pinned Vercel Composition Patterns source and React's Context, use, createContext, and forwardRef documentation listed in [sources.md](../../skills/react-quality-guard/references/sources.md). Read the [OpenAI skills article](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) directly for this revision. Kept selection metadata short and placed conditional composition guidance in a separate reference.

## Author assessment of the new cases

This is a review of the instructions against concrete scenarios, not an independent model run or a React execution result.

| Cases | Assessment |
| --- | --- |
| 23: conflicting modes | Multiple mode checks across headers, recipients, and submission justify explicit compositions. A limited variant prop remains available, and existing callers require preservation or a migration explanation. |
| 24: simple props | SaveButton's pending flags and Badge's single variant do not establish conflicting modes. The guidance supports retaining them without a provider or component split. |
| 25: content and callbacks | A static header can be a node or child. The list callback supplies item/index data, so removing it would discard a useful capability. |
| 26: two editors | Each editor needs one draft shared with its own preview/actions. One dialog-wide draft would couple the editors; two independent common parents or providers meet the requirement. |
| 27: state implementations | The shared UI can receive required data/actions from each parent. The local and remotely synchronized drafts retain different update/submit behavior and the existing cache library. |
| 28: supported React versions | React 18 support rules out requiring ref props, use(Context), or the shorter provider syntax. React 19-only code may use those APIs; useContext remains valid. |
| 29: nullable Context and subscriptions | An absent required provider needs explicit handling. Putting actions beside changing draft fields still subscribes action readers to the same Context; a field group alone cannot reduce updates. |
| 30: web form composition | The example uses form submission and an explicit non-submit cancel button. Actual input, IME, focus, pending-state, and instance behavior still require implementation-specific interaction checks. |

## Executed checks

- `python3 scripts/validate.py`: passed for all five skills, including metadata and skill-local references.
- `skill-creator/scripts/quick_validate.py skills/react-quality-guard`: passed. PyYAML 6.0.3 was installed only in a disposable virtual environment after the initial attempt reported the missing dependency.
- Changed-document relative references and Markdown code fences: passed.
- `git diff --check`: passed.
- Compared `AGENTS.md` with its pre-edit copy byte for byte: unchanged.

Instruction and scenario SHA-256 values at review time:

| File | SHA-256 |
| --- | --- |
| `skills/react-quality-guard/SKILL.md` | `172db67ecb7ca3e834ed8f76f124cb783b2b41215560b47d3f18722afc23b868` |
| `skills/react-quality-guard/references/composition.md` | `6632dbce24bc6801dac0a668444e120e3ed1448cdedd7268fb3c60a497a711bd` |
| `skills/react-quality-guard/references/react-correctness.md` | `c9fb92c70921a87ff80a7d0ebbf5dac4a5cceacbe65f4e090674e30af46f3166` |
| `skills/react-quality-guard/references/sources.md` | `d420ed55174cb442a0c506e6641c8f61d97e2dfaa0a797d546497bad64857bd3` |
| `evals/react-quality-guard/cases.md` | `9a9b75a2c33526af526f21eb66e17d09ff9e6c33372ca6c76b969d498b1910ed` |

## Limits

No independent model evaluations, automatic skill selection checks, React runtime/type checks, browser interactions, or performance measurements were run. The new cases remain a scenario catalog; this record does not mark them as behavioral passes. The example is explicitly a pair of JSX fragments, not a standalone component implementation. No installer or validator code changed, so installer tests were not rerun. Installed user skills and global settings were not modified.
