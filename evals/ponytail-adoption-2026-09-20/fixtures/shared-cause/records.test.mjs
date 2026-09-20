import test from 'node:test';
import assert from 'node:assert/strict';
import { exportRecords } from './export.mjs';
import { importRecords } from './import.mjs';

test('export retains wire contract and order', () => {
  assert.deepEqual(JSON.parse(exportRecords(['beta', 'alpha', 'beta'])),
    { version: 1, ids: ['beta', 'alpha'] });
});
test('import normalizes valid IDs', () => {
  assert.deepEqual(importRecords('{"ids":[" alpha ","beta"]}'), ['alpha', 'beta']);
});
