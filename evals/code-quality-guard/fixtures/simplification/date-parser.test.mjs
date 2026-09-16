import assert from "node:assert/strict";
import test from "node:test";
import * as parser from "./date-parser.mjs";

const { parseCalendarDate } = parser;

test("preserves the public export", () => {
  assert.deepEqual(Object.keys(parser), ["parseCalendarDate"]);
  assert.equal(typeof parseCalendarDate, "function");
});

for (const value of ["1000-01-01", "1900-02-28", "2000-02-29", "2024-02-29", "2026-09-16", "9999-12-31"]) {
  test(`accepts ${value} unchanged`, () => assert.equal(parseCalendarDate(value), value));
}

for (const value of [
  "2023-02-29", "1900-02-29", "2024-02-30", "2024-04-31",
  "2024-00-01", "2024-13-01", "2024-01-00", "2024-01-32",
  "0999-12-31", "0000-01-01", "10000-01-01",
  "2024-2-01", "2024-02-1", "2024/02/29", " 2024-02-29",
  "2024-02-29 ", "2024-02-29\n", "2024-02-29T00:00:00Z", "",
]) {
  test(`rejects invalid date ${JSON.stringify(value)}`, () => {
    assert.throws(() => parseCalendarDate(value), RangeError);
  });
}

for (const [index, value] of [null, undefined, 0, 20240229, {}, [], new String("2024-02-29")].entries()) {
  test(`rejects non-string input ${index} with TypeError`, () => {
    assert.throws(() => parseCalendarDate(value), TypeError);
  });
}

test("remains deterministic after failed and successful calls", () => {
  assert.throws(() => parseCalendarDate("2023-02-29"), RangeError);
  assert.equal(parseCalendarDate("2024-02-29"), "2024-02-29");
  assert.equal(parseCalendarDate("2024-02-29"), "2024-02-29");
});
