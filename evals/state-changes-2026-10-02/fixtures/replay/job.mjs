import {readFile, writeFile} from 'node:fs/promises';
import {join} from 'node:path';
import {credit} from './provider.mjs';
export async function runCredit({dir, requestId, accountId, amount, afterApply = async () => {}}) {
  const file = join(dir, 'jobs.json');
  const completed = JSON.parse(await readFile(file, 'utf8'));
  if (completed[requestId]) return completed[requestId];
  const receipt = await credit(dir, {accountId, amount});
  await afterApply();
  completed[requestId] = receipt;
  await writeFile(file, JSON.stringify(completed));
  return receipt;
}
