We avoid cache B **for tenant imports during the migration** because it lacks the required import namespace isolation. Mina, the migration owner, recorded that decision on September 14, 2026, with instructions to reassess imports when the migration ends. [Original decision](/private/tmp/workspace-36n2vr7j/harbor-cache/docs/decision.txt:1)

**The agreed policy does not rule out cache B for export jobs**: it explicitly says exports may continue using it.

The blanket permanent ban in [handoff.md](/private/tmp/workspace-36n2vr7j/harbor-cache/docs/handoff.md:1) misstates the original decision. [operations.md](/private/tmp/workspace-36n2vr7j/harbor-cache/docs/operations.md:1) repeats that interpretation, so it is not independent confirmation. The current configuration selects cache A for tenant imports; it does not establish an export restriction.

No files were changed.