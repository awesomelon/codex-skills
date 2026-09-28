# Earendil source metrics

Use this reference when Verbosity or Erosion calculations are requested. Follow [measurement.md](measurement.md) for common comparison conditions and measurable signals.

[Earendil's Measuring the sloppiness of code](https://earendil.com/posts/measuring-code-sloppiness/) distinguishes correctness from quality and discusses the limits of simple AI scoring and LOC optimization. The diagnostic metrics below come from that article; they are not universal acceptance criteria.

- `Verbosity = |lines flagged by AST rules ∪ clone lines| / LOC`. Use a union to avoid counting the same line twice.
- `mass(f) = CC(f) × sqrt(SLOC(f))`; `Erosion = Σ[CC(f) > 10] mass(f) / Σ mass(f)`. The threshold of 10 belongs to this metric's definition; it is not a universal function-complexity limit.

Use these names only when analysis supports the original definitions. State the tools, rules, denominators, and language support; a zero denominator is undefined. Label different definitions as different metrics. Do not split functions or add unrelated simple code solely to lower a value. This skill bundles neither the analyzer nor an automatic grader.
