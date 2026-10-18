import test from "node:test";
import assert from "node:assert/strict";
import { ThinkingLevel, Type } from "@google/genai";
import { createModelClient } from "../lib/model-provider";
import { modelSettings } from "../lib/model-config";

test("missing credentials and unknown providers fail closed, even with a Google project", () => {
  assert.throws(() => createModelClient({ MODEL_PROVIDER: "wanjie", GOOGLE_CLOUD_PROJECT: "unused", GEMINI_API_KEY: "other-key" }), /WANJIE_API_KEY_REQUIRED/);
  assert.throws(() => createModelClient({ GOOGLE_CLOUD_PROJECT: "unused" }), /GEMINI_API_KEY_REQUIRED/);
  assert.throws(() => createModelClient({ MODEL_PROVIDER: "typo" }), /MODEL_PROVIDER_INVALID/);
  assert.throws(() => modelSettings({ GEMINI_MODEL: "../other" }), /MODEL_NAME_INVALID/);
  assert.deepEqual(modelSettings({ MODEL_PROVIDER: "wanjie" }), { provider: "wanjie", model: "gemini-3-flash-preview" });
});

test("real SDK serialization routes multimodal tools and independent JSON requests to Wanjie with bearer auth", async () => {
  const requests: { url: string; body: Record<string, any> }[] = [];
  const transport: typeof fetch = async (input, init) => {
    const url = String(input);
    assert.equal(url, "https://maas-openapi.wanjiedata.com/api/v1beta/models/gemini-3-flash-preview:generateContent");
    const headers = new Headers(init?.headers);
    assert.equal(headers.get("authorization"), "Bearer test-placeholder");
    assert.equal(headers.has("x-goog-api-key"), false);
    assert.equal(init?.redirect, "error");
    requests.push({ url, body: JSON.parse(String(init?.body)) });
    return Response.json({ candidates: [{ content: { role: "model", parts: requests.length === 1
      ? [{ functionCall: { name: "inspect_page", args: {} }, thoughtSignature: "test-signature" }]
      : [{ text: '{"passed":true,"errors":[]}' }] } }], usageMetadata: { promptTokenCount: 20, candidatesTokenCount: 10 } });
  };
  const ai = createModelClient({ MODEL_PROVIDER: "wanjie", WANJIE_API_KEY: "test-placeholder" }, transport);
  const first = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [{ role: "user", parts: [{ text: "Inspect" }, { inlineData: { mimeType: "image/png", data: "dGVzdA==" } }] }],
    config: {
      tools: [{ functionDeclarations: [{ name: "inspect_page", parameters: { type: Type.OBJECT, properties: {} } }] }],
      toolConfig: { functionCallingConfig: { mode: "ANY" as never } },
      thinkingConfig: { thinkingLevel: ThinkingLevel.LOW },
      httpOptions: { timeout: 2000, retryOptions: { attempts: 1 } },
    },
  });
  assert.equal(first.functionCalls?.[0].name, "inspect_page");
  assert.equal(first.candidates?.[0].content?.parts?.[0].thoughtSignature, "test-signature");
  const second = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [first.candidates![0].content!, { role: "user", parts: [{ functionResponse: { name: "inspect_page", response: { version: 1 } } }] }],
    config: { responseMimeType: "application/json", responseJsonSchema: { type: "object", properties: { passed: { type: "boolean" } } }, httpOptions: { timeout: 2000 } },
  });
  assert.equal(JSON.parse(second.text!).passed, true);
  assert.equal(requests[0].body.contents[0].parts[1].inlineData.mimeType, "image/png");
  assert.equal(requests[0].body.toolConfig.functionCallingConfig.mode, "ANY");
  assert.equal(requests[1].body.generationConfig.responseMimeType, "application/json");
  assert.equal(requests[1].body.contents[0].parts[0].thoughtSignature, "test-signature");
  assert.equal(requests[1].body.contents[1].parts[0].functionResponse.response.version, 1);
});

test("SDK URL overrides cannot forward the Wanjie credential to another provider", async () => {
  let calls = 0;
  const ai = createModelClient({ MODEL_PROVIDER: "wanjie", WANJIE_API_KEY: "test-placeholder" }, async () => {
    calls++;
    throw new Error("Transport must not be called");
  });
  await assert.rejects(ai.models.generateContent({ model: "gemini-3-flash-preview", contents: "test", config: { httpOptions: { baseUrl: "https://generativelanguage.googleapis.com", retryOptions: { attempts: 1 } } } }), /MODEL_ENDPOINT_REJECTED/);
  assert.equal(calls, 0);
});
