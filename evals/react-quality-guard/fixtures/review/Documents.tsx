import { memo, useState } from 'react';
import { useQuery } from '@tanstack/react-query';

type Document = { id: string; title: string };
type Api = {
  list: (tenantId: string) => Promise<Document[]>;
  saveTitle: (tenantId: string, id: string, title: string) => Promise<void>;
};

export const HelpButton = memo(function HelpButton({ onClick = () => {} }: { onClick?: () => void }) {
  return <button type="button" onClick={onClick}>도움말</button>;
});

export function Documents({ tenantId, api }: { tenantId: string; api: Api }) {
  const { data = [], isPending, isError } = useQuery({
    queryKey: ['documents'],
    queryFn: () => api.list(tenantId),
  });
  if (isPending) return <p>불러오는 중</p>;
  if (isError) return <p role="alert">불러오기 실패</p>;
  return <>
    <HelpButton />
    {data.map(document => <TitleEditor key={`${tenantId}:${document.id}`}
      document={document} tenantId={tenantId} api={api} />)}
  </>;
}

function TitleEditor({ document, tenantId, api }: { document: Document; tenantId: string; api: Api }) {
  const [draft, setDraft] = useState(document.title);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');
  async function save() {
    if (saving) return;
    setSaving(true);
    setError('');
    try {
      await api.saveTitle(tenantId, document.id, draft);
    } catch {
      setError('저장하지 못했습니다');
    } finally {
      setSaving(false);
    }
  }
  return <div>
    <label>제목<input value={draft} onChange={event => setDraft(event.target.value)} /></label>
    <button type="button" disabled={saving} onClick={save}>저장</button>
    {error && <p role="alert">{error}</p>}
  </div>;
}
