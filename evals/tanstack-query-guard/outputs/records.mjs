export function recordOptions(tenantId, recordId, fetcher = fetch) {
  return {
    queryKey: ['records', tenantId, recordId],
    staleTime: 60_000,
    queryFn: async ({ signal }) => {
      const response = await fetcher(
        `/api/tenants/${encodeURIComponent(tenantId)}/records/${encodeURIComponent(recordId)}`,
        { signal },
      )
      if (!response.ok) {
        throw new Error(`Failed to fetch record: ${response.status} ${response.statusText}`)
      }
      return response.json()
    },
  }
}
