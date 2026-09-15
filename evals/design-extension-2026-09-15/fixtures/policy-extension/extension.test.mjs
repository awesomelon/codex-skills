import test from 'node:test';
import assert from 'node:assert/strict';
import {showArchiveButton} from './list.mjs';
import {documentActions, canPin} from './detail.mjs';
import {archiveIds} from './bulk.mjs';

for (const locked of [false, true]) {
  test(`expired document, locked=${locked}`, () => {
    const document = Object.freeze({id: 'expired-1', status: 'expired', locked});
    assert.equal(showArchiveButton(document), !locked);
    assert.deepEqual(documentActions(document), locked ? ['open'] : ['open', 'archive']);
    assert.deepEqual(archiveIds(Object.freeze([document])), locked ? [] : ['expired-1']);
    assert.equal(canPin(document), false);
  });
}

test('mixed bulk selection preserves order and excludes locked documents', () => {
  const documents = Object.freeze([
    Object.freeze({id: 'z', status: 'expired', locked: false}),
    Object.freeze({id: 'hidden', status: 'expired', locked: true}),
    Object.freeze({id: 'old', status: 'completed', locked: false}),
    Object.freeze({id: 'draft', status: 'draft', locked: false}),
    Object.freeze({id: 'a', status: 'cancelled', locked: false}),
  ]);
  assert.deepEqual(archiveIds(documents), ['z', 'old', 'a']);
});
