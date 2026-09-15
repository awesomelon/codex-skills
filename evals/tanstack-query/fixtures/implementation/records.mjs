export function recordOptions(tenantId, recordId, fetcher = fetch) {
  return {
    queryKey: ['records', recordId],
    staleTime: 60_000,
    queryFn: async () => {
      const response = await fetcher(
        `/api/tenants/${encodeURIComponent(tenantId)}/records/${encodeURIComponent(recordId)}`,
      )
      return response.json()
    },
  }
}
