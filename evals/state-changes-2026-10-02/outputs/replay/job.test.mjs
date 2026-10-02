import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,writeFile,readFile,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {execFile} from 'node:child_process';
import {promisify} from 'node:util';
import {runCredit} from './job.mjs';
const execFileAsync = promisify(execFile);
test('a completed request can be retried', async () => {
  const dir = await mkdtemp(join(tmpdir(), 'credit-'));
  try {
    await writeFile(join(dir, 'jobs.json'), '{}');
    await writeFile(join(dir, 'provider.json'), JSON.stringify({balances:{}, receipts:{}, effects:[]}));
    const input = {dir,requestId:'r1',accountId:'a1',amount:10};
    assert.deepEqual(await runCredit(input), await runCredit(input));
    const state = JSON.parse(await readFile(join(dir,'provider.json'),'utf8'));
    assert.equal(state.balances.a1, 10);
    assert.equal(state.effects.length, 1);
  } finally { await rm(dir,{recursive:true,force:true}); }
});

test('an interrupted request applies credit once when retried after a restart', async () => {
  const dir = await mkdtemp(join(tmpdir(), 'credit-'));
  try {
    await writeFile(join(dir, 'jobs.json'), '{}');
    await writeFile(join(dir, 'provider.json'), JSON.stringify({balances:{}, receipts:{}, effects:[]}));
    const input = {dir,requestId:'r1',accountId:'a1',amount:10};
    const jobUrl = new URL('./job.mjs', import.meta.url).href;
    await assert.rejects(execFileAsync(process.execPath, [
      '--input-type=module', '--eval',
      `const {runCredit} = await import(process.argv[1]);
       await runCredit({...JSON.parse(process.argv[2]), afterApply: async () => process.exit(75)});`,
      jobUrl, JSON.stringify(input),
    ]), error => error.code === 75);
    const applied = JSON.parse(await readFile(join(dir,'provider.json'),'utf8'));
    assert.equal(applied.balances.a1, 10);
    assert.equal(applied.effects.length, 1);
    assert.deepEqual(JSON.parse(await readFile(join(dir,'jobs.json'),'utf8')), {});

    const {stdout} = await execFileAsync(process.execPath, [
      '--input-type=module', '--eval',
      `const {runCredit} = await import(process.argv[1]);
       console.log(JSON.stringify(await runCredit(JSON.parse(process.argv[2]))));`,
      jobUrl, JSON.stringify(input),
    ]);
    const receipt = JSON.parse(stdout);
    assert.deepEqual(receipt, applied.effects[0]);
    const state = JSON.parse(await readFile(join(dir,'provider.json'),'utf8'));
    assert.equal(state.balances.a1, 10);
    assert.equal(state.effects.length, 1);
    assert.deepEqual(JSON.parse(await readFile(join(dir,'jobs.json'),'utf8')), {r1:receipt});
    assert.deepEqual(await runCredit(input), receipt);
  } finally { await rm(dir,{recursive:true,force:true}); }
});

test('different request IDs apply separate credits with the same account and amount', async () => {
  const dir = await mkdtemp(join(tmpdir(), 'credit-'));
  try {
    await writeFile(join(dir, 'jobs.json'), '{}');
    await writeFile(join(dir, 'provider.json'), JSON.stringify({balances:{}, receipts:{}, effects:[]}));
    const input = {dir,accountId:'a1',amount:10};
    const first = await runCredit({...input, requestId:'r1'});
    const second = await runCredit({...input, requestId:'r2'});
    assert.notEqual(first.id, second.id);
    const state = JSON.parse(await readFile(join(dir,'provider.json'),'utf8'));
    assert.equal(state.balances.a1, 20);
    assert.equal(state.effects.length, 2);
  } finally { await rm(dir,{recursive:true,force:true}); }
});
