import assert from 'node:assert/strict';
import test from 'node:test';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';

const { createSearch } = await import(pathToFileURL(resolve(process.env.PSTACK_SUBJECT, 'search.mjs')));

function setup() {
  const calls = [];
  const states = [];
  const search = createSearch(query => new Promise((resolve, reject) => {
    calls.push({ query, resolve, reject });
  }), state => states.push(state));
  return { calls, states, search };
}

test('late success cannot replace the newer result', async () => {
  const { calls, states, search } = setup();
  const first = search('cat');
  const second = search('dog');
  calls[1].resolve(['DOG']);
  await second;
  const count = states.length;
  calls[0].resolve(['CAT']);
  await first;
  assert.equal(states.length, count);
  assert.deepEqual(states.at(-1), { status: 'ready', query: 'dog', results: ['DOG'] });
});

test('late failure cannot replace the newer result', async () => {
  const { calls, states, search } = setup();
  const first = search('cat');
  const second = search('dog');
  calls[1].resolve(['DOG']);
  await second;
  const count = states.length;
  calls[0].reject(new Error('old failure'));
  await first;
  assert.equal(states.length, count);
  assert.deepEqual(states.at(-1), { status: 'ready', query: 'dog', results: ['DOG'] });
});

for (const outcome of ['resolve', 'reject']) {
  test(`clear remains idle after pending ${outcome}`, async () => {
    const { calls, states, search } = setup();
    const pending = search('cat');
    await search('');
    const count = states.length;
    calls[0][outcome](outcome === 'resolve' ? ['CAT'] : new Error('old failure'));
    await pending;
    assert.equal(calls.length, 1);
    assert.equal(states.length, count);
    assert.deepEqual(states.at(-1), { status: 'idle', query: '', results: [] });
  });
}

test('repeated identical queries are distinct user intents', async () => {
  const { calls, states, search } = setup();
  const first = search('cat');
  const second = search('cat');
  calls[1].resolve(['new']);
  await second;
  const count = states.length;
  calls[0].resolve(['old']);
  await first;
  assert.equal(states.length, count);
  assert.deepEqual(states.at(-1), { status: 'ready', query: 'cat', results: ['new'] });
});

test('active failure preserves error identity and completes the search', async () => {
  const { calls, states, search } = setup();
  const pending = search('cat');
  const error = new Error('current failure');
  calls[0].reject(error);
  assert.equal(await pending, undefined);
  assert.deepEqual(states.at(-1), { status: 'error', query: 'cat', results: [], error });
});

test('an older request cannot replace a newer loading state', async () => {
  const { calls, states, search } = setup();
  const first = search('cat');
  const second = search('dog');
  calls[0].resolve(['CAT']);
  await first;
  assert.deepEqual(states.at(-1), { status: 'loading', query: 'dog', results: [] });
  calls[1].resolve(['DOG']);
  await second;
});

test('independent controllers do not invalidate each other', async () => {
  const a = setup();
  const b = setup();
  const first = a.search('cat');
  const second = b.search('dog');
  a.calls[0].resolve(['CAT']);
  b.calls[0].resolve(['DOG']);
  await Promise.all([first, second]);
  assert.deepEqual(a.states.at(-1), { status: 'ready', query: 'cat', results: ['CAT'] });
  assert.deepEqual(b.states.at(-1), { status: 'ready', query: 'dog', results: ['DOG'] });
});
