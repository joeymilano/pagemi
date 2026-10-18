import { GoogleGenAI } from "@google/genai";
import { modelSettings, type ModelEnvironment } from "./model-config";
import { fail } from "./types";

export const WANJIE_BASE_URL = "https://maas-openapi.wanjiedata.com/api";

// Explicit providers only. A missing key must never switch to billable ADC.
export function createModelClient(
  env: ModelEnvironment = process.env,
  transport: typeof fetch = globalThis.fetch,
): GoogleGenAI {
  const { provider } = modelSettings(env);
  if (provider === "wanjie") {
    const key = env.WANJIE_API_KEY?.trim();
    if (!key) fail("WANJIE_API_KEY_REQUIRED", 503);
    return new GoogleGenAI({
      vertexai: false,
      apiKey: key,
      httpOptions: {
        baseUrl: WANJIE_BASE_URL,
        apiVersion: "v1beta",
        retryOptions: { attempts: 1 },
        fetch: async (input, init) => {
          const url = new URL(typeof input === "string" ? input : input instanceof URL ? input.href : input.url);
          // Restrict credential forwarding, including SDK per-call URL overrides.
          if (url.origin !== "https://maas-openapi.wanjiedata.com" ||
              !/^\/api\/v1beta\/models\/gemini-[a-z0-9.-]+:generateContent$/.test(url.pathname) ||
              url.search || url.username || url.password)
            fail("MODEL_ENDPOINT_REJECTED", 503);
          const headers = new Headers(init?.headers);
          headers.delete("x-goog-api-key");
          headers.set("Authorization", `Bearer ${key}`);
          return transport(input, { ...init, headers, redirect: "error" });
        },
      },
    });
  }
  if (provider === "gemini-api-key") {
    if (!env.GEMINI_API_KEY?.trim()) fail("GEMINI_API_KEY_REQUIRED", 503);
    return new GoogleGenAI({ vertexai: false, apiKey: env.GEMINI_API_KEY });
  }
  if (!env.GOOGLE_CLOUD_PROJECT) fail("GOOGLE_CLOUD_PROJECT_REQUIRED", 503);
  const location = env.GOOGLE_CLOUD_LOCATION || "global";
  if (!/^(global|[a-z]+-[a-z]+[0-9]+)$/.test(location)) fail("MODEL_LOCATION_INVALID", 503);
  return new GoogleGenAI({
    vertexai: true,
    project: env.GOOGLE_CLOUD_PROJECT,
    location,
    httpOptions: {
      baseUrl: location === "global" ? "https://aiplatform.googleapis.com" : `https://${location}-aiplatform.googleapis.com`,
      apiVersion: "v1",
      retryOptions: { attempts: 1 },
    },
  });
}
