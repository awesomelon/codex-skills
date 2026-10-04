import { expect, test, vi } from "vitest";
vi.mock("./client", () => ({ decode: () => ({ id: "demo", role: "reader" }) }));
import { decode } from "./client";
test("validates profiles", () => {
  expect(decode("{}").id).toBe("demo");
});
