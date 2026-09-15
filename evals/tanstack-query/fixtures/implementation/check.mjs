import assert from 'node:assert/strict'
import { QueryClient } from '@tanstack/query-core'
import { recordOptions } from './records.mjs'

const client = new QueryClient({ defaultOptions: { queries: { retry: false, gcTime: Infinity } } })
const failures = []
async function check(name, run) {
  try {
    await run()
    console.log(`PASS ${name}`)
  } catch (error) {
    failures.push(name)
    console.log(`FAIL ${name}: ${error.message}`)
  }
}

await check('separate tenants with matching record IDs', async () => {
  const fetcher = async (url) => ({ ok: true, json: async () => ({ url }) })
  const first = await client.fetchQuery(recordOptions('alpha', '1', fetcher))
  const second = await client.fetchQuery(recordOptions('beta', '1', fetcher))
  assert.notDeepEqual(first, second)
  assert.equal(second.url, '/api/tenants/beta/records/1')
})

await check('fresh successful reads reuse their cache entry', async () => {
  let calls = 0
  const fetcher = async () => ({ ok: true, json: async () => ({ number: ++calls }) })
  const options = recordOptions('repeat', '2', fetcher)
  await client.fetchQuery(options)
  await client.fetchQuery(options)
  assert.equal(calls, 1)
  assert.equal(options.staleTime, 60_000)
})

await check('HTTP failures reject without caching their response body', async () => {
  const options = recordOptions('failure', '3', async () => ({
    ok: false, status: 403, statusText: 'Forbidden', json: async () => ({ message: 'denied' }),
  }))
  await assert.rejects(client.fetchQuery(options))
  assert.equal(client.getQueryData(options.queryKey), undefined)
})

await check('query cancellation reaches the request', async () => {
  let requestSignal
  let started
  const ready = new Promise((resolve) => { started = resolve })
  const fetcher = (_url, options) => {
    requestSignal = options?.signal
    started()
    return new Promise((_resolve, reject) => {
      requestSignal?.addEventListener('abort', () => reject(new Error('aborted')), { once: true })
    })
  }
  const options = recordOptions('cancel', '4', fetcher)
  const pending = client.fetchQuery(options).catch(() => undefined)
  await ready
  await client.cancelQueries({ queryKey: options.queryKey })
  await pending
  assert.equal(requestSignal?.aborted, true)
})

await check('request input encoding is preserved', async () => {
  let requested
  const options = recordOptions('a/b', 'x y', async (url) => {
    requested = url
    return { ok: true, json: async () => ({ id: 'x y' }) }
  })
  await client.fetchQuery(options)
  assert.equal(requested, '/api/tenants/a%2Fb/records/x%20y')
})

client.clear()
assert.equal(failures.length, 0, failures.join('; '))
