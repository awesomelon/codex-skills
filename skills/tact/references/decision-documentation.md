# Preserve useful decision context

Preserve context that a future maintainer will need to change or operate the system correctly. A useful record answers a concrete question, such as why a compatibility alias must remain or which constraint rules out an otherwise attractive approach.

## Establish the rationale

Current code establishes behavior, not its author's historical intent. When a past decision or instruction determines the next action, trace it to attributable source evidence and retain its original scope. Distinguish that evidence from later summaries and your interpretation; copies of one summary are one evidence chain, not independent confirmation. Surface material contradictions or missing originals instead of turning a plausible explanation into a settled decision, permanent restriction, or permission. Search relevant sources, not every available system.

## Choose the smallest useful record

Before adding a record, identify the future question it answers and the material context that code, tests, or existing documentation do not already supply. Save that context when losing it would invite a mistaken change, repeated investigation, or redoing a settled decision. The size or architectural importance of a change alone is insufficient. Leaving no new document is a valid outcome.

Update affected documentation when implementation makes it inaccurate. Put a local constraint beside the code or in the existing contract; use an architecture decision record (ADR) when the rationale needs to be found independently across future changes. Prefer the place a maintainer would already look. Reuse or link adequate existing context instead of creating another account of it. An explicit documentation request still warrants the requested artifact.

Planning, review, and explanation keep rationale in the requested response or deliverable. They do not authorize extra documentation files or code changes. If the user requests an ADR or documentation only, write that artifact without implementing the decision. Honor explicit file limits and no-documentation requests; report a material documentation gap if those limits leave one.

## Follow the project's convention

Before creating a record, inspect relevant project instructions, existing decisions, and configuration such as `.adr-dir`. Reuse the established location, markup, naming sequence, headings, status vocabulary, and index. Do not create a parallel Markdown directory in a project that already keeps decisions in another format. If conflicting evidence leaves the destination or status genuinely ambiguous, surface that specific conflict before writing the dependent record.

With no established convention, use `docs/decisions/NNNN-short-title.md`, starting at `0001` and continuing any existing sequence. Create only the needed record; no ADR tooling, new documentation framework, or repository-wide documentation sweep is required.

## Keep only what supports the next decision

Lead with the choice and its decisive reason. Include a constraint, rejected alternative, accepted cost, or condition for revisiting it only when that detail changes how a future reader should act. Keep necessary qualifications even if they take more space; completeness of headings is not the goal.

Link to supporting code or evidence rather than restating it. Omit work logs, obvious code descriptions, generic best practices, and speculative implementation or rollout checklists. Open questions belong here only when their answer could change the decision. Do not invent alternatives, measurements, approvals, or historical motives to fill a section.

Use the project's format. Without one, a descriptive title, status and date, and a few paragraphs explaining the choice and reason can be enough. Add sections only when they help retrieval; neither a fixed template nor a word target determines whether the record is useful.

Select one status supported by the task. `Accepted` means the choice is settled within the user's authorization or the project's decision process; a recommendation still awaiting a decision is `Proposed`. Acceptance does not mean implementation, verification, or release is complete. Preserve those distinctions when describing the result. Use a known decision date; for a historical choice with no known date, identify the recording date without implying it was the decision date.

Preserve the history of accepted decisions. When a decision changes, create a successor that links to the earlier record and update the earlier status or supersession link using the project convention. Retain its original context and rationale. Draft corrections and factual errata can be edited in place without pretending a new decision occurred.

Before delivery, compare the record with the actual choice and affected behavior, check its links and status, and make the saved path discoverable in the result. A document describing planned work is not evidence that the work ran.
