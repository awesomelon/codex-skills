Refactored [checkout.mjs](sandbox:/workspace/scratch/77406476b916/three-skill-runs/build/checkout.mjs) to select delivery once and share shipment, receipt construction, and completion auditing. Exported API, values, error propagation, and effect order remain intact. Test assertions are unchanged.

Checks: `node --test checkout.test.mjs` passed all 8 tests before and after the edit. Inspected the final implementation.

Resource files read:
- `resources-build/SKILL.md`
- `resources-build/references/refactoring/overview.md`
- `resources-build/references/refactoring/transformations.md`

Project files read: `TASK.md`, `checkout.mjs`, and `checkout.test.mjs`.
