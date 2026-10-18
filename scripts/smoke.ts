import { modelSettings } from "../lib/model-config";
import { Type, ThinkingLevel } from "@google/genai";
import assert from "node:assert/strict";
import { readFile, writeFile, mkdir } from "node:fs/promises";
import { genAiClient, GENAI_ENDPOINT } from "../lib/agent";
async function main() {
  const ai = genAiClient();
  const model = modelSettings().model;
  const tests = [
    {
      name: "text",
      contents: "Return exactly: Pagemi ready",
      config: { maxOutputTokens: 512 },
    },
    {
      name: "image",
      contents: [
        {
          role: "user",
          parts: [
            { text: "Name the two main objects. One sentence." },
            {
              inlineData: {
                mimeType: "image/png",
                data: (await readFile("public/commuter-one.png")).toString(
                  "base64",
                ),
              },
            },
          ],
        },
      ],
      config: { maxOutputTokens: 512 },
    },
    {
      name: "tool",
      contents: "Call inspect_page to read the product page.",
      config: {
        maxOutputTokens: 512,
        tools: [
          {
            functionDeclarations: [
              {
                name: "inspect_page",
                description: "Read product page",
                parameters: { type: Type.OBJECT, properties: {} },
              },
            ],
          },
        ],
        toolConfig: { functionCallingConfig: { mode: "ANY" as never } },
      },
    },
  ];
  const results = [];
  for (const t of tests) {
    try {
      const r = await ai.models.generateContent({
        model,
        contents: t.contents,
        config: { ...t.config, thinkingConfig: { thinkingLevel: ThinkingLevel.LOW }, httpOptions: { timeout: 40000, retryOptions: { attempts: 1 } } },
      });
      if (t.name === "tool") assert.equal(r.functionCalls?.[0]?.name, "inspect_page");
      else assert.ok(r.text?.trim(), "Empty model response");
      if (t.name === "text") assert.match(r.text!, /Pagemi ready/);
      const result = {
        test: t.name,
        model,
        endpoint: GENAI_ENDPOINT,
        text: r.text,
        tools: r.functionCalls,
        usage: r.usageMetadata,
      };
      results.push(result);
      console.log(JSON.stringify(result));
    } catch (e) {
      console.error(
        JSON.stringify({
          test: t.name,
          error: e instanceof Error ? e.name : "UnknownError",
          status: typeof (e as { status?: unknown })?.status === "number" ? (e as { status: number }).status : undefined,
        }),
      );
      process.exitCode = 1;
      break;
    }
  }
  await mkdir("output", { recursive: true });
  await writeFile(
    "output/model-smoke.json",
    JSON.stringify({ at: new Date().toISOString(), results }, null, 2),
  );
}
main();
