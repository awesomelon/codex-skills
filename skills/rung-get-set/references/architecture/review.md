# Architecture review

Use [review scope and findings](../quality/review-scope.md) for comparison and reporting.

Check whether aliases, re-exports, type-only dependencies, generated code, or dynamic registration make visible paths differ from actual dependencies. Compare documented exceptions and gradual migrations with their allowed scope. Moving a file alone does not resolve a dependency problem.

Trace consequential boundary violations through actual producers and consumers, including deployment compatibility, authorization, and data integrity. Explain which responsibility or invariant is lost and how that affects the caller; folder shape alone does not establish a defect.
