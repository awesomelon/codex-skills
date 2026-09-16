import test from "node:test";
import assert from "node:assert/strict";
import { listLabels } from "./features/list.mjs";
import { exportLabel } from "./features/export.mjs";
import { switchTenant } from "./features/session.mjs";

test("labels track the current tenant for both consumers without changing records", () => {
  const records = [Object.freeze({ id: "7" }), Object.freeze({ id: "9" })];
  switchTenant("alpha");
  assert.deepEqual(listLabels(records), ["alpha:7", "alpha:9"]);
  assert.equal(exportLabel(records[0]), "alpha:7.csv");
  switchTenant("beta");
  assert.deepEqual(listLabels(records), ["beta:7", "beta:9"]);
  assert.equal(exportLabel(records[0]), "beta:7.csv");
  assert.deepEqual(records, [{ id: "7" }, { id: "9" }]);
});
