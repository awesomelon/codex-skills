import test from 'node:test';
import assert from 'node:assert/strict';
import { serialize } from './producer.mjs';
import { deserialize } from './consumer.mjs';

test('serialize emits a v2 JSON packet with ordered entries and archived defaults', () => {
  const text = serialize([
    { id: 'second', title: 'Archived document', archived: true, internal: 'omit' },
    { id: 'first', title: 'Active document', archived: false },
    { id: 'third', title: 'Default document' },
    { id: 'fourth', title: 'Undefined default', archived: undefined },
  ]);

  assert.equal(typeof text, 'string');
  assert.deepEqual(JSON.parse(text), {
    version: 2,
    entries: [
      { id: 'second', title: 'Archived document', archived: true },
      { id: 'first', title: 'Active document', archived: false },
      { id: 'third', title: 'Default document', archived: false },
      { id: 'fourth', title: 'Undefined default', archived: false },
    ],
  });
});

test('deserialize accepts v2 entries and retains archived values in order', () => {
  const text = JSON.stringify({
    version: 2,
    entries: [
      { id: 'b', title: 'Archived', archived: true, internal: 'omit' },
      { id: 'a', title: 'Active', archived: false },
      { id: 'c', title: 'Default' },
    ],
  });

  assert.deepEqual(deserialize(text), [
    { id: 'b', title: 'Archived', archived: true },
    { id: 'a', title: 'Active', archived: false },
    { id: 'c', title: 'Default', archived: false },
  ]);
});

test('deserialize upgrades legacy v1 items to unarchived rows', () => {
  const text = JSON.stringify({
    version: 1,
    items: [
      { id: 'b', title: 'Legacy document', internal: 'omit' },
      { id: 'a', title: 'Legacy extension', archived: true },
    ],
  });

  assert.deepEqual(deserialize(text), [
    { id: 'b', title: 'Legacy document', archived: false },
    { id: 'a', title: 'Legacy extension', archived: false },
  ]);
});

test('mixed documents round trip through the public JSON interface', () => {
  const rows = [
    { id: 'z', title: 'Quoted "title"\nwith Unicode: café', archived: true },
    { id: 'a', title: '', archived: false },
    { id: 'm', title: 'Default' },
  ];

  assert.deepEqual(deserialize(serialize(rows)), [
    { id: 'z', title: 'Quoted "title"\nwith Unicode: café', archived: true },
    { id: 'a', title: '', archived: false },
    { id: 'm', title: 'Default', archived: false },
  ]);
});

test('empty documents round trip', () => {
  assert.deepEqual(JSON.parse(serialize([])), { version: 2, entries: [] });
  assert.deepEqual(deserialize(serialize([])), []);
});

test('empty legacy documents remain compatible', () => {
  assert.deepEqual(deserialize('{"version":1,"items":[]}'), []);
});

test('unsupported versions fail', () => {
  assert.throws(() => deserialize('{"version":99,"items":[]}'), TypeError);
  for (const version of [0, 3, '1', '2', null]) {
    assert.throws(
      () => deserialize(JSON.stringify({ version, items: [], entries: [] })),
      TypeError,
      `version ${JSON.stringify(version)} must be rejected`,
    );
  }
  assert.throws(() => deserialize('{"entries":[]}'), TypeError);
});
