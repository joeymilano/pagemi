import { modelSettings } from "../lib/model-config";
import { ThinkingLevel } from "@google/genai";
import { MODEL_SCHEMA } from "../lib/model-schema";
import { genAiClient } from "../lib/agent";
import { ProposalSchema } from "../lib/types";
const ai = genAiClient();
async function main() {
  const r = await ai.models.generateContent({
    model: modelSettings().model,
    contents:
      "Return empty issues and empty changes. There is no evidence, so do not invent any.",
    config: {
      responseMimeType: "application/json",
      responseJsonSchema: MODEL_SCHEMA,
      maxOutputTokens: 256,
      thinkingConfig: { thinkingLevel: ThinkingLevel.LOW },
      httpOptions: { timeout: 40000, retryOptions: { attempts: 1 } },
    },
  });
  console.log(ProposalSchema.parse(JSON.parse(r.text!)));
}
main().catch((e) => {
  console.error({ error: e instanceof Error ? e.name : "UnknownError", status: typeof e?.status === "number" ? e.status : undefined });
  process.exitCode = 1;
});
