import test from 'node:test';
import assert from 'node:assert/strict';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const root = process.env.MIGRATION_PROJECT;
if (!root) throw new Error('Set MIGRATION_PROJECT to the result directory');
const { serialize } = await import(pathToFileURL(resolve(root, 'producer.mjs')));
const { deserialize } = await import(pathToFileURL(resolve(root, 'consumer.mjs')));

test('exports the revised wire contract independently of the importer', () => {
  assert.deepEqual(JSON.parse(serialize([
    { id: 'z', title: '서명 📝', archived: true },
    { id: 'a', title: 'é文' },
  ])), {
    version: 2,
    entries: [
      { id: 'z', title: '서명 📝', isArchived: true },
      { id: 'a', title: 'é文', isArchived: false },
    ],
  });
});
test('imports independently constructed v2 values to the original domain shape', () => {
  assert.deepEqual(deserialize(JSON.stringify({ version: 2, entries: [
    { id: 'a', title: 'First', isArchived: false },
    { id: 'b', title: 'Second', isArchived: true },
  ] })), [
    { id: 'a', title: 'First', archived: false },
    { id: 'b', title: 'Second', archived: true },
  ]);
});
test('keeps legacy v1 import', () => {
  assert.deepEqual(deserialize('{"version":1,"items":[{"id":"old","title":"Legacy"}]}'),
    [{ id: 'old', title: 'Legacy', archived: false }]);
});
test('does not mutate caller rows and preserves integrated values', () => {
  const rows = [{ id: 'b', title: 'B', archived: true }, { id: 'a', title: 'A', archived: false }];
  const before = structuredClone(rows);
  assert.deepEqual(deserialize(serialize(rows)), before);
  assert.deepEqual(rows, before);
  assert.deepEqual(deserialize(serialize([])), []);
});
test('rejects unsupported and incorrectly typed versions', () => {
  for (const version of [0, 3, 99, '2']) {
    assert.throws(() => deserialize(JSON.stringify({ version, items: [], entries: [] })), TypeError);
  }
});
