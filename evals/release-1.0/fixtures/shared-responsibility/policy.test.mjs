import test from 'node:test';
import assert from 'node:assert/strict';
import {showArchiveButton} from './list.mjs';
import {documentActions, canPin} from './detail.mjs';
import {archiveIds} from './bulk.mjs';

const cases = [
  ['draft', false, false],
  ['draft', true, false],
  ['completed', false, true],
  ['completed', true, false],
  ['cancelled', false, true],
  ['cancelled', true, false],
];

for (const [status, locked, allowed] of cases) {
  test(`${status}, locked=${locked}`, () => {
    const document = Object.freeze({id: 'd1', status, locked});
    assert.equal(showArchiveButton(document), allowed);
    assert.deepEqual(documentActions(document), allowed ? ['open', 'archive'] : ['open']);
    assert.deepEqual(archiveIds(Object.freeze([document])), allowed ? ['d1'] : []);
    assert.equal(canPin(document), allowed);
  });
}

test('bulk preserves order and empty input', () => {
  const documents = Object.freeze([
    Object.freeze({id: 'z', status: 'cancelled', locked: false}),
    Object.freeze({id: 'skip', status: 'completed', locked: true}),
    Object.freeze({id: 'a', status: 'completed', locked: false}),
  ]);
  assert.deepEqual(archiveIds(documents), ['z', 'a']);
  assert.deepEqual(archiveIds([]), []);
});
