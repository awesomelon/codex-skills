import { getJSON } from '../../core/http';

export const loadInvoices = () => getJSON('/api/invoices');
