import test from 'node:test';
import assert from 'node:assert/strict';
import { pathToFileURL } from 'node:url';
import { resolve } from 'node:path';
const root = process.env.PONYTAIL_PROJECT;
if (!root) throw new Error('Set PONYTAIL_PROJECT');
const { exportRecords } = await import(pathToFileURL(resolve(root, 'export.mjs')));
const { importRecords } = await import(pathToFileURL(resolve(root, 'import.mjs')));
const { normalizeIds } = await import(pathToFileURL(resolve(root, 'ids.mjs')));
const paths = { shared: normalizeIds,
  export: ids => JSON.parse(exportRecords(ids)).ids,
  import: ids => importRecords(JSON.stringify({ ids })) };
for (const [name, run] of Object.entries(paths)) {
  test(`${name}: normalized identity, stable order, no mutation`, () => {
    const ids = Object.freeze([' beta ', 'alpha', 'beta', ' alpha ', 'gamma']);
    assert.deepEqual(run(ids), ['beta', 'alpha', 'gamma']);
    assert.deepEqual(run([]), []);
  });
  test(`${name}: exact boundary errors survive`, () => {
    assert.throws(() => run(['alpha', 3]), TypeError);
    for (const value of ['', 'BAD', 'a b', 'a/b']) {
      assert.throws(() => run(['alpha', value]), RangeError);
    }
  });
}
