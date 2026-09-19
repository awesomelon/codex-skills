import test from 'node:test';
import assert from 'node:assert/strict';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';

const target = process.env.MIGRATION_PROJECT;
if (!target) throw new Error('Set MIGRATION_PROJECT to the implementation directory');
const { serialize } = await import(pathToFileURL(resolve(target, 'producer.mjs')));
const { deserialize } = await import(pathToFileURL(resolve(target, 'consumer.mjs')));
const rows = [
  { id: 'd2', title: 'Archived', archived: true },
  { id: 'd1', title: 'Active', archived: false },
];

test('producer emits the exact v2 envelope and preserves row order', () => {
  assert.deepEqual(JSON.parse(serialize(rows)), { version: 2, entries: rows });
});
test('producer defaults omitted archived to false', () => {
  assert.deepEqual(JSON.parse(serialize([{ id: 'd3', title: 'Default' }])), {
    version: 2, entries: [{ id: 'd3', title: 'Default', archived: false }],
  });
});
test('consumer imports legacy v1 with an archived default', () => {
  assert.deepEqual(deserialize(JSON.stringify({ version: 1, items: [{ id: 'old', title: 'Legacy' }] })),
    [{ id: 'old', title: 'Legacy', archived: false }]);
});
test('consumer imports the specified v2 envelope', () => {
  assert.deepEqual(deserialize(JSON.stringify({ version: 2, entries: rows })), rows);
});
test('producer and consumer integrate without losing archived state', () => {
  assert.deepEqual(deserialize(serialize(rows)), rows);
  assert.deepEqual(deserialize(serialize([])), []);
});
test('unsupported versions remain errors', () => {
  for (const version of [0, 3, 99, '2']) {
    assert.throws(() => deserialize(JSON.stringify({ version, items: [], entries: [] })), TypeError);
  }
});
