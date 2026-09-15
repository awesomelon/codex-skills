import { useInfiniteQuery, useMutation, useQuery, useQueryClient } from '@tanstack/react-query'

type RecordData = { id: string; title: string }
declare function readRecord(tenantId: string, id: string, signal: AbortSignal): Promise<RecordData>
declare function saveRecord(tenantId: string, record: RecordData): Promise<RecordData>
declare function readPage(tenantId: string, cursor: string | null, signal: AbortSignal): Promise<{ items: RecordData[]; nextCursor: string | null }>

export function useRecord(tenantId: string, recordId: string) {
  return useQuery({
    queryKey: ['records', recordId],
    queryFn: ({ signal }) => readRecord(tenantId, recordId, signal),
    staleTime: 60_000,
  })
}

export function useRecordSave(tenantId: string) {
  const client = useQueryClient()
  return useMutation({
    mutationFn: (record: RecordData) => saveRecord(tenantId, record),
    onSuccess: (record) => {
      client.setQueryData(['records', record.id], record)
    },
  })
}

export function useRecordPages(tenantId: string) {
  const result = useInfiniteQuery({
    queryKey: ['records', tenantId, 'pages'],
    queryFn: ({ pageParam, signal }) => readPage(tenantId, pageParam, signal),
    initialPageParam: null as string | null,
    getNextPageParam: (page) => page.nextCursor,
  })
  function loadMore() {
    if (result.hasNextPage && !result.isFetchingNextPage) {
      void result.fetchNextPage()
    }
  }
  return { result, loadMore }
}
