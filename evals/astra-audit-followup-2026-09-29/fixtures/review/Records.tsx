import { useQuery } from '@tanstack/react-query';
import { loadRecords } from './records';

export function Records({ tenantId }: { tenantId: string }) {
  const query = useQuery({
    queryKey: ['records'],
    queryFn: () => loadRecords(tenantId),
    staleTime: 60_000,
  });
  return <ul>{query.data?.map(record => <li key={record.id}>{record.title}</li>)}</ul>;
}
