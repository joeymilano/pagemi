import test from "node:test";
import assert from "node:assert/strict";
import { runAgent, checkInputBudget, MAX_INPUT_TOKENS, MAX_OUTPUT_TOKENS, REQUEST_RESERVE_USD, reserveModelRequest, settleModelRequest } from "../lib/agent";
import { MemoryStore } from "../lib/store";
import { newSession, beginRun } from "../lib/domain";

test("token limit rejects unknown counts and bounds every request below its reservation", () => {
  for (const count of [undefined, NaN, Infinity, -1, 0, 1.5, MAX_INPUT_TOKENS + 1])
    assert.throws(() => checkInputBudget(count), /INPUT_TOKEN_BUDGET_EXCEEDED/);
  checkInputBudget(MAX_INPUT_TOKENS);
  // Include 2,000 tokens of margin over the input count.
  const upper = ((MAX_INPUT_TOKENS + 2000) * 1.5 + MAX_OUTPUT_TOKENS * 7.5) / 1e6;
  assert.ok(upper < REQUEST_RESERVE_USD);
});

test("concurrent requests cannot reserve past the shared budget and settlement preserves spent usage", async () => {
  const previous = process.env.MODEL_BUDGET_USD;
  process.env.MODEL_BUDGET_USD = "0.1";
  try {
    const db = new MemoryStore();
    const attempts = await Promise.allSettled([reserveModelRequest(db), reserveModelRequest(db)]);
    assert.equal(attempts.filter(x => x.status === "fulfilled").length, 1);
    await settleModelRequest(db, 0.03);
    await reserveModelRequest(db);
    await assert.rejects(reserveModelRequest(db), /MODEL_BUDGET_REACHED/);
    await settleModelRequest(db, REQUEST_RESERVE_USD);
    assert.deepEqual(await db.read("system", "model-budget"), { spent: 0.09, reserved: 0, days: {} });
  } finally {
    if (previous === undefined) delete process.env.MODEL_BUDGET_USD;
    else process.env.MODEL_BUDGET_USD = previous;
  }
});

test("unset, invalid, zero and negative budgets stop before evidence or model execution", async () => {
  const saved = { provider: process.env.MODEL_PROVIDER, key: process.env.GEMINI_API_KEY, budget: process.env.MODEL_BUDGET_USD };
  process.env.MODEL_PROVIDER = "gemini-api-key";
  process.env.GEMINI_API_KEY = "test-placeholder";
  try {
    for (const budget of [undefined, "", "0", "-1", "NaN", "Infinity"]) {
      if (budget === undefined) delete process.env.MODEL_BUDGET_USD;
      else process.env.MODEL_BUDGET_USD = budget;
      const db = new MemoryStore();
      const s = await newSession(db);
      const r = await beginRun(db, s.id);
      let started = false;
      await assert.rejects(runAgent(db, s, r, new AbortController().signal, async () => { started = true; }), /MODEL_BUDGET_NOT_CONFIGURED/);
      assert.equal(started, false);
      assert.equal(await db.read("system", "model-budget"), null);
    }
  } finally {
    for (const [key, value] of Object.entries({ MODEL_PROVIDER: saved.provider, GEMINI_API_KEY: saved.key, MODEL_BUDGET_USD: saved.budget })) {
      if (value === undefined) delete process.env[key];
      else process.env[key] = value;
    }
  }
});

test("two failed provider attempts retain their conservative charge and release the run reservation", async () => {
  const saved = { MODEL_PROVIDER: process.env.MODEL_PROVIDER, GEMINI_API_KEY: process.env.GEMINI_API_KEY, MODEL_BUDGET_USD: process.env.MODEL_BUDGET_USD };
  const originalFetch = globalThis.fetch;
  let attempts = 0;
  process.env.MODEL_PROVIDER = "gemini-api-key";
  process.env.GEMINI_API_KEY = "test-placeholder";
  process.env.MODEL_BUDGET_USD = "1";
  globalThis.fetch = async () => {
    attempts++;
    return Response.json({ error: { code: 503, message: "Unavailable", status: "UNAVAILABLE" } }, { status: 503 });
  };
  try {
    const db = new MemoryStore();
    const s = await newSession(db);
    const r = await beginRun(db, s.id);
    await assert.rejects(runAgent(db, s, r, new AbortController().signal, async () => {}));
    const ledger = await db.read<{ spent: number; reserved: number }>("system", "model-budget");
    assert.equal(attempts, 2, "no hidden SDK retries");
    assert.equal(ledger?.reserved, 0);
    assert.equal(ledger?.spent, 0.12, "timeouts cannot become uncharged attempts in the ledger");
  } finally {
    globalThis.fetch = originalFetch;
    for (const [key, value] of Object.entries(saved)) {
      if (value === undefined) delete process.env[key];
      else process.env[key] = value;
    }
  }
});
