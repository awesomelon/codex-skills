import {queryOptions, type QueryClient} from '@tanstack/react-query';

type RecordData = {id: string; title: string; status: 'open' | 'done'};
declare function readRecords(tenantId: string, signal: AbortSignal): Promise<RecordData[]>;
declare function saveRecord(tenantId: string, record: RecordData): Promise<RecordData>;

export const recordKeys = {
  lists: (tenantId: string) => ['records', tenantId, 'list'] as const,
  detail: (tenantId: string, id: string) => ['records', tenantId, 'detail', id] as const,
  counts: (tenantId: string) => ['records', tenantId, 'counts'] as const,
};

export function recordsOptions(tenantId: string) {
  return queryOptions({
    queryKey: recordKeys.lists(tenantId),
    queryFn: ({signal}) => readRecords(tenantId, signal),
    staleTime: 60_000,
  });
}

export function preloadRecords(client: QueryClient, tenantId: string) {
  return client.prefetchQuery(recordsOptions(tenantId));
}

export async function saveAndUpdate(client: QueryClient, tenantId: string, record: RecordData) {
  const saved = await saveRecord(tenantId, record);
  client.setQueryData(recordKeys.detail(tenantId, saved.id), saved);
  await client.invalidateQueries({queryKey: recordKeys.lists(tenantId)});
  return saved;
}
