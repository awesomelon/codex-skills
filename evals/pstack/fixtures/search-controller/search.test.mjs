import assert from 'node:assert/strict';
import test from 'node:test';
import { createSearch } from './search.mjs';

test('publishes a successful search', async () => {
  const states = [];
  const search = createSearch(async query => [query.toUpperCase()], state => states.push(state));
  await search('cat');
  assert.deepEqual(states, [
    { status: 'loading', query: 'cat', results: [] },
    { status: 'ready', query: 'cat', results: ['CAT'] },
  ]);
});

test('empty search clears results without loading', async () => {
  const states = [];
  let loads = 0;
  const search = createSearch(async () => { loads += 1; }, state => states.push(state));
  await search('');
  assert.equal(loads, 0);
  assert.deepEqual(states, [{ status: 'idle', query: '', results: [] }]);
});
