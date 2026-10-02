import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtemp, writeFile, readFile, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const moduleUrl = pathToFileURL(resolve(process.argv[2])).href;
const dir = await mkdtemp(join(tmpdir(), 'credit-acceptance-'));
const read = async name => JSON.parse(await readFile(join(dir, name), 'utf8'));
const emptyProvider = { balances: {}, receipts: {}, effects: [] };
const child = `
  const {runCredit} = await import(process.argv[1]);
  const args = JSON.parse(process.argv[2]);
  if (args.interrupt) args.afterApply = async () => { throw new Error('interrupted after effect'); };
  try { console.log(JSON.stringify(await runCredit(args))); }
  catch (error) { console.error(error.message); process.exitCode = 2; }
`;
function run(requestId, interrupt = false) {
  return spawnSync(process.execPath, ['--input-type=module', '-e', child, moduleUrl,
    JSON.stringify({ dir, requestId, accountId: 'account-a', amount: 10, interrupt })],
  { encoding: 'utf8' });
}

try {
  await writeFile(join(dir, 'jobs.json'), '{}');
  const beforeEffect = run('request-a');
  assert.equal(beforeEffect.status, 2, 'missing provider state must fail');
  assert.deepEqual(await read('jobs.json'), {}, 'failed effect must not be marked complete');
  await writeFile(join(dir, 'provider.json'), JSON.stringify(emptyProvider));

  const interrupted = run('request-a', true);
  assert.equal(interrupted.status, 2);
  assert.match(interrupted.stderr, /interrupted after effect/);
  assert.equal((await read('provider.json')).effects.length, 1);
  assert.deepEqual(await read('jobs.json'), {});

  const restarted = run('request-a');
  assert.equal(restarted.status, 0, restarted.stderr);
  assert.equal((await read('provider.json')).effects.length, 1, 'restart must not duplicate credit');
  assert.equal((await read('provider.json')).balances['account-a'], 10);
  assert.equal((await read('jobs.json'))['request-a'].id, 1);

  const repeated = run('request-a');
  assert.equal(repeated.status, 0, repeated.stderr);
  assert.equal((await read('provider.json')).effects.length, 1);

  const distinct = run('request-b');
  assert.equal(distinct.status, 0, distinct.stderr);
  assert.equal((await read('provider.json')).effects.length, 2, 'different request IDs remain distinct');
  assert.equal((await read('provider.json')).balances['account-a'], 20);
  assert.equal((await read('jobs.json'))['request-b'].id, 2);
  console.log('PASS: pre-effect failure, post-effect interruption, process restart, repeat, distinct request');
} finally {
  await rm(dir, { recursive: true, force: true });
}
