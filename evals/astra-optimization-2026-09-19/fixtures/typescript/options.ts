type LoadOptions = { mode: 'cached' | 'fresh'; timeoutMs: number };

export function describeLoad(options: LoadOptions): string {
  return `${options.mode}:${options.timeoutMs}`;
}

export function describeDefaultLoad(): string {
  const options = { mode: 'cached', timeoutMs: 2500 };
  return describeLoad(options);
}
