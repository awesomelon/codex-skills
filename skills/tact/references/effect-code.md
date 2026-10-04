# Effect conventions

Use only when the affected project directly uses Effect. Follow its installed version and existing domain definitions.

Use tagged error operators for selective recovery rather than broad catches followed by manual `_tag` inspection. Use the library's supported matching or tagged predicates for tagged values, and a match expression for repeated branches over the same literal value.

Construct tagged domain values through the existing schema, tagged class, or tagged-enum constructor. Do not duplicate the representation in handwritten tag objects. Pattern objects used for matching are not domain-value construction.

Runtime consumers should obtain services through the project's context and owning layer. Avoid importing internal service constructors across module boundaries to bypass that ownership. A focused constructor test can exercise the constructor directly.

Preserve error identity, exhaustiveness, resource lifetime, and service scope when changing these patterns. Do not rename unrelated APIs or introduce a second architecture to satisfy a stylistic preference.
