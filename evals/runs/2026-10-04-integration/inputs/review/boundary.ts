export function parseName(input: unknown): string {
  if (typeof input !== "string" || input.trim() === "") {
    throw new Error("Expected a nonempty name");
  }
  return input.trim();
}
