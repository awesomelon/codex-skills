import assert from 'node:assert/strict';
import test from 'node:test';
import { shouldInvalidate } from './invalidation.mjs';

test('invalidation handles handcrafted keys', () => {
  assert.equal(shouldInvalidate(['document', 'tenant-a', 'doc-1'], 'tenant-a', 'doc-1'), true);
  assert.equal(shouldInvalidate(['document', 'tenant-b', 'doc-1'], 'tenant-a', 'doc-1'), false);
  assert.equal(shouldInvalidate(['document', 'tenant-a', 'doc-2'], 'tenant-a', 'doc-1'), false);
});
