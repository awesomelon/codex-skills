import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,writeFile,readFile,rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {runCredit} from './job.mjs';
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
