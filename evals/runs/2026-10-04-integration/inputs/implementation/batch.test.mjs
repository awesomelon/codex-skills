import assert from "node:assert/strict";
import test from "node:test";
import { buildBatch } from "./batch.mjs";

test("selects active rows", () => {
  assert.deepEqual(buildBatch([{ id: "a", active: true, value: 3 }], 10), {
    items: [{ key: "0:a", value: 3 }], options: { timeout: 10 },
  });
});
