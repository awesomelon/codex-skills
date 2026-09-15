# TypeScript patterns

Read only the section relevant to the change. Examples use TypeScript 4.9+ syntax and assume `strict`, `noUncheckedIndexedAccess`, and `exactOptionalPropertyTypes`. Use supported equivalents in older projects. Each TypeScript block is self-contained.

## Mutually exclusive states and exhaustive handling

Independent optional properties are valid. Use a union when loading, success, and failure require different data. Reuse the project's discriminant name.

```ts
type LoadResult =
  | { status: "loading" }
  | { status: "ready"; text: string }
  | { status: "failed"; message: string };

function describeResult(result: LoadResult): string {
  switch (result.status) {
    case "loading":
      return "Loading";
    case "ready":
      return result.text;
    case "failed":
      return result.message;
    default: {
      const unexpected: never = result;
      throw new Error(`Unexpected result: ${String(unexpected)}`);
    }
  }
}
```

The `never` assignment catches newly added variants at compile time. The throw prevents unexpected runtime input from becoming a successful return value. It does not replace input validation. A void function can use the same default arm.

## Non-empty input and indexed reads

```ts
type NonEmpty<T> = readonly [T, ...T[]];

function isNonEmpty<T>(values: readonly T[]): values is NonEmpty<T> {
  return values.length > 0;
}

function first<T>(values: NonEmpty<T>): T {
  return values[0];
}

function atIndex<T>(values: NonEmpty<T>, index: number): T | undefined {
  return values[index];
}

function total(values: readonly number[]): number {
  return values.reduce((sum, value) => sum + value, 0);
}

type Pairs<T> = readonly (readonly [T, T])[];
```

Index zero is known to exist in the tuple; an arbitrary index still needs handling. Do not hide that distinction with an assertion in a random-selection example. A readonly view does not freeze an array or prevent mutation through another reference; copy when a lasting snapshot is required. Pair representation guarantees two entries per pair, not arbitrary properties of their values.

## Checked numeric values and branded constructors

A plain `durationMs: number` permits negative values, NaN, and infinity. If non-negativity must travel with the value, validate it and expose a branded result. Reuse existing brand names and syntax in real code.

```ts
type DurationMs = number & { readonly __brand: "DurationMs" };

function parseDurationMs(input: unknown): DurationMs {
  if (typeof input !== "number" || !Number.isFinite(input) || input < 0) {
    throw new Error("Expected a finite non-negative duration");
  }
  return input as DurationMs;
}

type TimeRange = { readonly start: Date; readonly durationMs: DurationMs };
```

The local assertion adds the compile-time marker after a runtime check. Arithmetic returns ordinary numbers that need checking before reusing this type. A full date range may also need checks for invalid dates, date mutation, and result overflow; this example promises only a finite non-negative duration. Brands do not validate persisted data and can be bypassed by assertions.

## Unknown input without a schema dependency

When a simple check suffices, construct the checked result instead of asserting that an unchecked object has the desired type.

```ts
type Member = { id: string; role: "admin" | "member" };

function parseMember(input: unknown): Member {
  if (typeof input !== "object" || input === null) {
    throw new Error("Expected an object");
  }
  if (!("id" in input) || typeof input.id !== "string" || input.id.length === 0) {
    throw new Error("Expected a non-empty member id");
  }
  if (!("role" in input) || (input.role !== "admin" && input.role !== "member")) {
    throw new Error("Expected a supported member role");
  }
  return { id: input.id, role: input.role };
}
```

The role comparison proves the literal union; property presence alone would not. This parser intentionally returns only the selected fields. Preserve additional fields when required by the application.

## Existing schemas and generated definitions

If Zod is already installed, reuse or extend the existing schema and infer the type. The following uses basic APIs shared by Zod 3 and 4; check the installed version for other options.

```ts
import { z } from "zod";

const MemberSchema = z.object({
  id: z.string().min(1),
  role: z.enum(["admin", "member"]),
});

type Member = z.infer<typeof MemberSchema>;

function parseMember(input: unknown): Member {
  return MemberSchema.parse(input);
}
```

Use `safeParse` for expected invalid input when its result matches the application's error handling. With transforms, the incoming schema type and parsed output type can differ. Infer the one the function actually consumes or returns. Derive view types from generated definitions, for example `Pick<GeneratedMember, "id" | "role">`, only when they are meant to change together. Regenerate generated files rather than editing them manually.

## Configuration inference

```ts
type Config = { theme: "dark" | "light"; columns: number };

const editableConfig = { theme: "dark", columns: 3 } satisfies Config;
editableConfig.columns = 4;

const fixedConfig = { theme: "dark", columns: 3 } as const satisfies Config;
```

`editableConfig.theme` is inferred as `"dark"`, but `columns` is `number`. `fixedConfig` keeps readonly literal properties. Neither `satisfies` nor `as const` checks runtime data or freezes the object. Avoid `as const` when mutation or wider assignment is intended.

## Official references

- [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html): built-in checks, predicates, discriminated unions, and `never`.
- [TypeScript 4.9](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-4-9.html): `satisfies` and property checks on unknown objects.
- [Indexed access checking](https://www.typescriptlang.org/tsconfig/noUncheckedIndexedAccess.html): possible missing values in indexed reads.
- [Type assertions](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#type-assertions): compile-time assertions have no runtime checks.
- [Zod basics](https://zod.dev/basics): parsing, error results, and input/output type inference.
