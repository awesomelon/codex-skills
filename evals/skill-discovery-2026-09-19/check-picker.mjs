// Behavioral check of the recorded derivation only, not a React renderer.
// Run with Node.js: node evals/react-quality-guard/outputs/check-picker.mjs
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const source = readFileSync(new URL('./DocumentPicker.tsx', import.meta.url), 'utf8');
const start = source.indexOf('  const normalizedQuery =');
const end = source.indexOf('\n  return <section>', start);
assert.ok(start >= 0 && end > start, 'Locate the recorded derivation in the component');
const deriveVisible = new Function('documents', 'query', `${source.slice(start, end)}\nreturn visible;`);
const documents = Object.freeze([
  Object.freeze({ id: 'z', title: 'Zulu' }),
  Object.freeze({ id: 'b1', title: 'Beta' }),
  Object.freeze({ id: 'a', title: 'alpha' }),
  Object.freeze({ id: 'b2', title: 'Beta' }),
]);
const ids = values => values.map(value => value.id);

assert.deepEqual(ids(deriveVisible(documents, '')), ['a', 'b1', 'b2', 'z']);
assert.deepEqual(ids(documents), ['z', 'b1', 'a', 'b2']);
assert.deepEqual(ids(deriveVisible(documents, 'BeTA')), ['b1', 'b2']);
assert.deepEqual(ids(deriveVisible(documents, 'LPH')), ['a']);
assert.deepEqual(deriveVisible(documents, 'missing'), []);
assert.deepEqual(deriveVisible(documents, ' beta'), []);
assert.deepEqual(deriveVisible([], ''), []);
assert.deepEqual(ids(deriveVisible([{ id: 'new', title: 'BETA replacement' }], 'beta')), ['new']);
assert.strictEqual(deriveVisible(documents, 'zulu')[0], documents[0]);

console.log('PASS: 9 derivation assertions');
console.log('Scope: extracted JavaScript calculation; no React rendering or TypeScript compilation.');
