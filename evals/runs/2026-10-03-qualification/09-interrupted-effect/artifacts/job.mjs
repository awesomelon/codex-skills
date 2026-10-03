import {readFile, writeFile, rename} from 'node:fs/promises';
import {join} from 'node:path';
import {credit} from './provider.mjs';
export async function runCredit({dir, requestId, accountId, amount, afterApply = async () => {}}) {
  const file = join(dir, 'jobs.json');
  const completed = JSON.parse(await readFile(file, 'utf8'));
  if (Object.hasOwn(completed, requestId)) return completed[requestId];
  // The provider must recognize the request even if this process stops before saving.
  const operationKey = `credit:${JSON.stringify(requestId)}`;
  const receipt = await credit(dir, {accountId, amount, operationKey});
  await afterApply();
  // Publish completion atomically so an interrupted write leaves readable state.
  await writeFile(`${file}.tmp`, JSON.stringify({...completed, [requestId]: receipt}));
  await rename(`${file}.tmp`, file);
  return receipt;
}
