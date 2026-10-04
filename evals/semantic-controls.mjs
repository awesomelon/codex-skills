// Author-created runtime examples. These do not execute or grade a model.
import assert from "node:assert/strict";
import test from "node:test";

test("unchecked JSON can violate the consumer contract", () => {
  // This is the runtime behavior of the scenario's TypeScript assertion.
  const profileFromJson = (text) => JSON.parse(text);
  const profileKey = (text) => profileFromJson(text).id.toUpperCase();
  assert.equal(profileKey('{"id":"ada"}'), "ADA");
  assert.throws(() => profileKey("{}"), TypeError);
});

test("a focused external-input guard handles its stated contract", () => {
  function parseName(input) {
    if (typeof input !== "string" || input.trim() === "") {
      throw new Error("Expected a nonempty name");
    }
    return input.trim();
  }
  assert.equal(parseName(" Ada "), "Ada");
  for (const input of [undefined, null, 42, {}, "", "  "]) {
    assert.throws(() => parseName(input), /Expected a nonempty name/);
  }
});

test("filter then map uses indexes from the filtered collection", () => {
  const names = ["", "Ada", "Lin"];
  const original = names.filter(Boolean).map((name, index) => `${index}:${name}`);
  const mechanicalRewrite = names.flatMap((name, index) => name ? [`${index}:${name}`] : []);
  assert.deepEqual(original, ["0:Ada", "1:Lin"]);
  assert.notDeepEqual(mechanicalRewrite, original);
});

test("a fresh local accumulator need not mutate caller data", () => {
  const input = Object.freeze(["Ada", "Lin"]);
  const copied = input.reduce((result, name) => [...result, name.toUpperCase()], []);
  const local = input.reduce((result, name) => {
    result.push(name.toUpperCase());
    return result;
  }, []);
  assert.deepEqual(local, copied);
  assert.deepEqual(input, ["Ada", "Lin"]);
});
