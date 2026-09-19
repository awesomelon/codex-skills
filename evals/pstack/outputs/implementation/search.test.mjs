import assert from 'node:assert/strict';
import test from 'node:test';
import { createSearch } from './search.mjs';

function deferred() {
  let resolve;
  let reject;
  const promise = new Promise((resolvePromise, rejectPromise) => {
    resolve = resolvePromise;
    reject = rejectPromise;
  });
  return { promise, resolve, reject };
}

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

test('an older result cannot overwrite a newer completed search', async () => {
  const states = [];
  const older = deferred();
  const newer = deferred();
  const search = createSearch(
    query => query === 'cat' ? older.promise : newer.promise,
    state => states.push(state),
  );
  const olderSearch = search('cat');
  const newerSearch = search('dog');
  assert.deepEqual(states, [
    { status: 'loading', query: 'cat', results: [] },
    { status: 'loading', query: 'dog', results: [] },
  ]);

  newer.resolve(['DOG']);
  assert.equal(await newerSearch, undefined);
  older.resolve(['CAT']);
  assert.equal(await olderSearch, undefined);

  assert.deepEqual(states, [
    { status: 'loading', query: 'cat', results: [] },
    { status: 'loading', query: 'dog', results: [] },
    { status: 'ready', query: 'dog', results: ['DOG'] },
  ]);
});

for (const outcome of ['resolve', 'reject']) {
  test(`a superseded ${outcome} cannot replace a newer loading state`, async () => {
    const states = [];
    const older = deferred();
    const newer = deferred();
    const search = createSearch(
      query => query === 'cat' ? older.promise : newer.promise,
      state => states.push(state),
    );
    const olderSearch = search('cat');
    const newerSearch = search('dog');
    older[outcome](outcome === 'resolve' ? ['CAT'] : new Error('old failure'));
    assert.equal(await olderSearch, undefined);
    assert.deepEqual(states, [
      { status: 'loading', query: 'cat', results: [] },
      { status: 'loading', query: 'dog', results: [] },
    ]);

    newer.resolve(['DOG']);
    assert.equal(await newerSearch, undefined);
    assert.deepEqual(states.at(-1), { status: 'ready', query: 'dog', results: ['DOG'] });
  });

  test(`clearing suppresses a pending ${outcome} without loading again`, async () => {
    const states = [];
    const pending = deferred();
    let loads = 0;
    const search = createSearch(() => {
      loads += 1;
      return pending.promise;
    }, state => states.push(state));
    const pendingSearch = search('cat');
    assert.equal(await search(''), undefined);
    pending[outcome](outcome === 'resolve' ? ['CAT'] : new Error('old failure'));
    assert.equal(await pendingSearch, undefined);
    assert.equal(loads, 1);
    assert.deepEqual(states, [
      { status: 'loading', query: 'cat', results: [] },
      { status: 'idle', query: '', results: [] },
    ]);
  });
}

test('an older error cannot overwrite a newer completed search', async () => {
  const states = [];
  const older = deferred();
  const search = createSearch(
    query => query === 'cat' ? older.promise : Promise.resolve(['DOG']),
    state => states.push(state),
  );
  const olderSearch = search('cat');
  await search('dog');
  older.reject(new Error('old failure'));
  assert.equal(await olderSearch, undefined);
  assert.deepEqual(states, [
    { status: 'loading', query: 'cat', results: [] },
    { status: 'loading', query: 'dog', results: [] },
    { status: 'ready', query: 'dog', results: ['DOG'] },
  ]);
});

test('separate calls with the same query still honor the latest intent', async () => {
  const states = [];
  const older = deferred();
  const newer = deferred();
  const loads = [older, newer];
  const search = createSearch(() => loads.shift().promise, state => states.push(state));
  const olderSearch = search('cat');
  const newerSearch = search('cat');
  newer.resolve(['new CAT']);
  await newerSearch;
  older.resolve(['old CAT']);
  await olderSearch;
  assert.deepEqual(states, [
    { status: 'loading', query: 'cat', results: [] },
    { status: 'loading', query: 'cat', results: [] },
    { status: 'ready', query: 'cat', results: ['new CAT'] },
  ]);
});

test('active errors publish and finish without an older result overwriting them', async () => {
  const states = [];
  const older = deferred();
  const newer = deferred();
  const error = new Error('active failure');
  const search = createSearch(
    query => query === 'cat' ? older.promise : newer.promise,
    state => states.push(state),
  );
  const olderSearch = search('cat');
  const newerSearch = search('dog');
  newer.reject(error);
  assert.equal(await newerSearch, undefined);
  older.resolve(['CAT']);
  assert.equal(await olderSearch, undefined);
  assert.deepEqual(states, [
    { status: 'loading', query: 'cat', results: [] },
    { status: 'loading', query: 'dog', results: [] },
    { status: 'error', query: 'dog', results: [], error },
  ]);
});
