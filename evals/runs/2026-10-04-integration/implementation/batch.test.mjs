import assert from "node:assert/strict";
import test from "node:test";
import { buildBatch } from "./batch.mjs";

test("selects active rows", () => {
  assert.deepEqual(buildBatch([{ id: "a", active: true, value: 3 }], 10), {
    items: [{ key: "0:a", value: 3 }], options: { timeout: 10 },
  });
});

test("retains zero timeout and omits an undefined timeout", () => {
  assert.deepEqual(buildBatch([], 0), { items: [], options: { timeout: 0 } });
  assert.deepEqual(buildBatch([]), { items: [], options: {} });
  assert.deepEqual(buildBatch([], undefined), { items: [], options: {} });
});

test("preserves active order, compact indexes, value references, and inputs", () => {
  const first = Object.freeze({ name: "first" });
  const second = Object.freeze({ name: "second" });
  const rows = Object.freeze([
    Object.freeze({ id: "inactive", active: false, value: null }),
    Object.freeze({ id: "same", active: true, value: first }),
    Object.freeze({ id: "inactive", active: false, value: null }),
    Object.freeze({ id: "same", active: true, value: second }),
  ]);
  const { items } = buildBatch(rows);

  assert.deepEqual(items.map(item => item.key), ["0:same", "1:same"]);
  assert.equal(items[0].value, first);
  assert.equal(items[1].value, second);
});

test("skips sparse slots and preserves active truthiness", () => {
  const rows = [];
  rows[1] = { id: "a", active: "yes", value: 1 };
  rows[3] = { id: "b", active: 0, value: 2 };
  rows[5] = { id: "c", active: 1, value: 3 };

  assert.deepEqual(buildBatch(rows), {
    items: [{ key: "0:a", value: 1 }, { key: "1:c", value: 3 }],
    options: {},
  });
});
