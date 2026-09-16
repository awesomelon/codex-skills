export type Result =
  | { status: "loading"; progress?: number }
  | { status: "ready"; text: string; progress?: number }
  | { status: "failed"; message: string; progress?: number };

export function describe(result: Result): string {
  switch (result.status) {
    case "loading": return "Loading";
    case "ready": return result.text;
    case "failed": return result.message;
    default: return result;
  }
}
