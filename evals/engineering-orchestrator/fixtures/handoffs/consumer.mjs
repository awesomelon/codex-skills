import { COLLECTION_FIELD } from './contract.mjs';
export const deserialize = text => JSON.parse(text)[COLLECTION_FIELD].map(row => ({...row}));
