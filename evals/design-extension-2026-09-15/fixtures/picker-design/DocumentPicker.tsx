import { useState } from 'react';

type Document = { id: string; title: string };
type Props = { documents: Document[]; onSelect: (id: string) => void };

export function DocumentPicker({ documents, onSelect }: Props) {
  const [query, setQuery] = useState('');
  const normalizedQuery = query.toLowerCase();
  const visible = documents
    .filter(document => document.title.toLowerCase().includes(normalizedQuery))
    .sort((a, b) => a.title.localeCompare(b.title));

  return <section>
    <label>문서 검색<input value={query} onChange={event => setQuery(event.target.value)} /></label>
    <ul>{visible.map(document => <li key={document.id}>
      <button type="button" onClick={() => onSelect(document.id)}>{document.title}</button>
    </li>)}</ul>
  </section>;
}
