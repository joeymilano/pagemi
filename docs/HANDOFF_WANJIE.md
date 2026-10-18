# MerchReflex — Wanjie full-workflow handoff

**Superseded provider choice:** after the Wanjie key returned no Gemini access, the user requested returning to Google Cloud. Follow [HANDOFF_GOOGLE_CLOUD.md](HANDOFF_GOOGLE_CLOUD.md) for the current plan; retain this file as diagnostic history, not deployment authorization.

Updated: 2026-10-18, Shanghai time. This supplements `HANDOFF_ZCODE.md`; it does not replace existing changes in that file.

## User decision

Use the user's existing Wanjie API for **full Gemini generation and independent verification**, while retaining Google Cloud Run, Firestore and private object storage. Do not replace generation with Google Check Grounding. Do not purchase credits, recharge accounts, enable a paid fallback or assume the $1,000 GenAI App Builder trial credit covers ordinary Gemini usage. The previous $0.01 authorization applied to the two already-completed grounding tests only.

## Implementation in this working tree

- `lib/model-config.ts` centralizes provider/model metadata for health, run records and evaluation scripts.
- `lib/model-provider.ts` uses the Google Gen AI SDK with Wanjie's documented Gemini-compatible route: `https://maas-openapi.wanjiedata.com/api/v1beta/models/<model>:generateContent`. Authentication is Bearer; credentials are stripped from Google-specific headers. Endpoint overrides and redirects cannot forward the Wanjie key elsewhere.
- Select `MODEL_PROVIDER=wanjie`. Candidate default: `gemini-3-flash-preview` (documented by Wanjie, **not yet verified against this user's account**). Explicit `GEMINI_MODEL` overrides the default, including any stale value in `.env.local`; update it deliberately.
- No implicit fallback to Vertex/ADC on missing credentials. Google providers remain available only through explicit selection.
- The original workflow remains: image/evidence input, read-only function tools, structured patches, deterministic checks, independent semantic verification, human approval, transactional publication, served-page verification, append-only rollback.
- Existing per-run deadline, call/tool caps, shared daily quotas and estimated cost ledger remain. Authentication/payment errors do not retry. Provider error bodies are not persisted in retry events.
- `scripts/deploy.sh` prepares a zero-traffic candidate using a restricted temporary JSON environment file; no API key is included in command arguments. It removes the temporary file on exit. Runtime credentials remain in Cloud Run environment configuration, so restrict service configuration access.
- Exclude local `.zcode`, `.v2c` and `.video_agent` directories from build/upload contexts.

## Verified here

- `npm test`: **31 passed, 0 failed**. Includes existing publication/security tests and actual SDK serialization over mocked transport (image, tools, function response, thought signature, structured JSON, bearer auth, no credential fallback/forwarding).
- `npm run build`: passed.
- `npm run typecheck`: passed.
- `bash -n scripts/deploy.sh` and `git diff --check`: passed.

These checks do **not** prove live Wanjie model access, model quality, account balance, or successful deployment.

## Blocker and production status (updated after key was supplied)

The user supplied `WANJIE_API_KEY` in ignored `.env.local`. It has been read without exposing its value; the file is mode 0600. Local provider/model settings are now `wanjie` / `gemini-3-flash-preview`.

**Live access is blocked by model permissions:** the initial text capability request and a bounded diagnostic request returned HTTP 403, `PERMISSION_DENIED`: "The requested model is not authorized for your account." The authenticated `/api/v1/models` request returned HTTP 200, but listed no Gemini or Gemma models. This establishes an accessible model-list endpoint, not account balance or generation access. Do not brute-force other Gemini models or substitute a non-Google model without revisiting the competition requirement. The user has been asked to enable Gemini permission or replace the local key with a Gemini-authorized one.

No new deployment or traffic promotion has occurred. Cloud Run was re-read: `merchreflex-00012-his` remains at 100% traffic. The optional Wanjie implementation is included in the later official-Cloud release; preserve other existing uncommitted work. Sanitized diagnostic evidence is in `eval/results/wanjie-access-2026-10-18.json`.

## Resume once credentials are available

1. Update only the relevant values in ignored `.env.local`, preserving existing settings:

   ```dotenv
   MODEL_PROVIDER=wanjie
   GEMINI_MODEL=gemini-3-flash-preview
   WANJIE_API_KEY=<local secret, never committed>
   ```

2. Run bounded live capability checks using existing account credits. Do not retry payment/permission/model-not-found failures or switch providers:

   ```sh
   node --env-file=.env.local --import tsx scripts/smoke.ts
   node --env-file=.env.local --import tsx scripts/schema-smoke.ts
   ```

   Inspect `output/model-smoke.json` and the schema result. Image output needs semantic inspection; nonempty output alone is not proof of correct recognition. Check account prices/usage before extended evaluation. The application ledger uses $1.50/M input and $7.50/M output as estimates, not verified Wanjie prices or a hard provider spending cap.

3. Re-read the Cloud Run service revision, current traffic, runtime service account and non-secret limits. Preserve exact public `APP_ORIGIN=https://merchreflex-927668522599.asia-southeast1.run.app`, Firestore storage, evidence bucket and existing operational constraints. Do not disable billing under the assumption hosting/storage will continue working free.

4. Export the required deployment variables securely without printing the key. `scripts/deploy.sh` requires `GOOGLE_CLOUD_PROJECT`, `EVIDENCE_BUCKET`, `RUNTIME_SERVICE_ACCOUNT`, `APP_ORIGIN`, `WANJIE_API_KEY`. Explicitly set the verified model. Run the script to create a **zero-traffic** candidate; do not promote yet.

5. Run one full synthetic-session candidate check:

   ```sh
   TEST_ORIGIN=https://candidate---merchreflex-sqaibrdjbq-as.a.run.app \
   WRITE_ORIGIN=https://merchreflex-927668522599.asia-southeast1.run.app \
   SMOKE_ID=wanjie-candidate node scripts/api-smoke.mjs
   ```

   Confirm the actual candidate URL from the deployment output before using it. The script exercises live analysis, approval restrictions, cross-session isolation, idempotent publication, served-page verification and rollback. Its synthetic approval checks mechanics; inspect generated claims against evidence separately. Inspect the returned provider/model and persist results without secrets or private customer data.

6. Promote only the exact tested revision. Retain the prior revision for rollback. Repeat the full check against the canonical public URL, record the actual result and update this handoff. If the live check fails, keep traffic on the existing revision and report the failure; do not relax evidence checks to make a demo pass.

7. Commit/push only scoped project changes, preserving unrelated dirty files. Do not claim the previous model's evaluation scores apply to the new model/provider. Remaining 30-run measurement, holdout grading, user tests, video and competition submission are separate deliverables.

## References

- Wanjie native Gemini documentation: https://docs.wjark.com/maas/WebDoc/gemini.html
- Public app: https://merchreflex-927668522599.asia-southeast1.run.app
- Repository: https://github.com/joeymilano/merchreflex
- Google credit test evidence: `eval/results/credit-smoke-2026-10-18.json` (two successful grounding calls; credit coverage still not established).
