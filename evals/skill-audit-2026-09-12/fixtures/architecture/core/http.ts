import { documentStore } from '../features/documents/store';

export async function getJSON(url: string): Promise<unknown> {
  const response = await fetch(url, {
    headers: { 'X-Workspace': documentStore.workspaceId },
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  return response.json();
}
