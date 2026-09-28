export type RecordItem = { id: string; title: string };
export async function loadRecords(tenantId: string): Promise<RecordItem[]> {
  const response = await fetch(`/api/tenants/${encodeURIComponent(tenantId)}/records`);
  if (!response.ok) throw new Error(`Records request failed: ${response.status}`);
  return response.json();
}
