import { performance } from 'node:perf_hooks';
import { baseline, proposed } from './export.mjs';

const rows = Array.from({ length: 500 }, (_, id) => ({ id, amount: id + 1 }));
let started = performance.now();
const before = await baseline(rows);
console.log(JSON.stringify({ variant: 'baseline', ms: performance.now() - started, completed: before.length }));
started = performance.now();
const after = proposed(rows);
console.log(JSON.stringify({ variant: 'proposed', ms: performance.now() - started, completed: after.length ?? 0 }));
