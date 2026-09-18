import assert from 'node:assert/strict';
import test from 'node:test';
import { documentKey } from './keys.mjs';

test('keys include resource and identifiers', () => {
  const key = documentKey('tenant-a', 'doc-1');
  assert.equal(key.length, 3);
  assert.ok(key.includes('document'));
  assert.ok(key.includes('tenant-a'));
  assert.ok(key.includes('doc-1'));
  assert.notDeepEqual(key, documentKey('tenant-b', 'doc-1'));
});
