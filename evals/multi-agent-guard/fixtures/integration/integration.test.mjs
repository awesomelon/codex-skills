import assert from 'node:assert/strict';
import test from 'node:test';
import { documentKey } from './keys.mjs';
import { shouldInvalidate } from './invalidation.mjs';

test('reader keys remain invalidatable within the correct tenant', () => {
  const key = documentKey('tenant-a', 'doc-1');
  assert.equal(shouldInvalidate(key, 'tenant-a', 'doc-1'), true);
  assert.equal(shouldInvalidate(key, 'tenant-b', 'doc-1'), false);
  assert.equal(shouldInvalidate(key, 'tenant-a', 'doc-2'), false);
});
