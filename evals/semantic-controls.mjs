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

test("optional construction preserves zero and property absence", () => {
  const options = timeout => timeout === undefined ? {} : { timeout };
  assert.deepEqual(options(0), { timeout: 0 });
  assert.equal(Object.hasOwn(options(undefined), "timeout"), false);
  assert.equal(Object.hasOwn({ timeout: undefined }, "timeout"), true);
  assert.notDeepEqual(options(undefined), { timeout: undefined });
});

test("combining passes can change observable callback order", () => {
  const phases = [];
  const combined = [];
  const original = [1, 2].filter(value => {
    phases.push(`filter:${value}`);
    return true;
  }).map(value => {
    phases.push(`map:${value}`);
    return value * 2;
  });
  const rewritten = [1, 2].flatMap(value => {
    combined.push(`filter:${value}`, `map:${value}`);
    return [value * 2];
  });
  assert.deepEqual(rewritten, original);
  assert.deepEqual(phases, ["filter:1", "filter:2", "map:1", "map:2"]);
  assert.notDeepEqual(combined, phases);
});
