import { fail } from "./types";

export type ModelEnvironment = Record<string, string | undefined>;
export function modelSettings(env: ModelEnvironment = process.env) {
  const provider = env.MODEL_PROVIDER || "gemini-api-key";
  if (!["wanjie", "gemini-api-key", "vertexai"].includes(provider))
    fail("MODEL_PROVIDER_INVALID", 503);
  const model = env.GEMINI_MODEL ||
    (provider === "wanjie" ? "gemini-3-flash-preview" : "gemini-3.8-flash");
  if (!/^gemini-[a-z0-9.-]+$/.test(model)) fail("MODEL_NAME_INVALID", 503);
  return { provider, model };
}
