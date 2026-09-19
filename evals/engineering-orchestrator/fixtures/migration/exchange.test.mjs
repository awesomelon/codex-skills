import test from 'node:test';
import assert from 'node:assert/strict';
import { serialize } from './producer.mjs';
import { deserialize } from './consumer.mjs';
test('empty documents round trip', () => {
  assert.deepEqual(deserialize(serialize([])), []);
});
test('unsupported versions fail', () => {
  assert.throws(() => deserialize('{"version":99,"items":[]}'), TypeError);
});
