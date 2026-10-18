# MerchReflex

**Fix the page. Not just the ticket.**

An evidence-grounded product-page repair prototype for AI Builder Cup 2026. New code built independently for this competition. All product facts and feedback in the demonstration are synthetic; the included image is AI-generated.

[Live demo](https://merchreflex-927668522599.asia-southeast1.run.app) · [Current Zcode handoff](docs/HANDOFF_GOOGLE_CLOUD.md) · [Measured validation](docs/VALIDATION.md)

## What works

- Live Gemini text and image interpretation with read-only tool calls
- Product-page, missing-information, source-conflict, quality and fulfillment triage
- Minimal, source-linked changes to description, image caption and FAQ
- Separate semantic verification and deterministic permission checks
- Merchant-confirmed new evidence invalidating old approvals
- Human approval bound to the patch, page version and evidence revision
- Atomic publication, idempotency receipts, served-page verification and append-only rollback
- Per-visitor isolated sessions; no production store connection

## Run locally

Requires Node.js 22+. The application uses Google's official Vertex AI endpoint for Gemini generation and independent verification, with Application Default Credentials locally and the service identity on Cloud Run. Production storage/hosting uses Google Cloud billing, Cloud Run, Firestore and private Cloud Storage. See [Google Cloud handoff](docs/HANDOFF_GOOGLE_CLOUD.md) for the exact revision, measured results and approved USD 1 model budget.

```sh
npm ci
cp .env.example .env.local
gcloud auth application-default login
npm run dev
```

Open http://localhost:3147. Configure `APP_ORIGIN` to exactly match the address used. Production requires `STORAGE_DRIVER=firestore`. Development can omit it for single-process file storage under ignored `.data/`; model calls are still live and there is no canned AI fallback.

In `.env.local`, set `MODEL_PROVIDER=vertexai`, `GEMINI_MODEL=gemini-3.8-flash`, the Google project/location, and an approved `MODEL_BUDGET_USD` before running live workflows. The example budget is zero, which disables workflow model calls. Standalone model smoke scripts call the provider directly and must only be run within an approved test budget. Never prefix credentials with `NEXT_PUBLIC_`. Other providers require explicit selection; missing credentials never activate another provider. The optional Wanjie route remains implemented but the supplied account has no Gemini access; see [previous provider handoff](docs/HANDOFF_WANJIE.md).

```sh
npm test
npm run build
npm run typecheck
```

Tests inject an in-memory store and mocked transport; they do not consume model credits. Load local configuration explicitly for real checks: `node --env-file=.env.local --import tsx scripts/smoke.ts`, then `node --env-file=.env.local --import tsx scripts/schema-smoke.ts`. `npm run eval` performs real model evaluations when environment variables are set. Do not publish evaluator outputs as human-verified accuracy.

## Deploy

Use the included Dockerfile and `scripts/deploy.sh`, exporting the required environment variables first, including explicit provider, model and budget. Set `APP_ORIGIN` to the exact public browser URL. The script deploys a zero-traffic candidate through a restricted temporary environment file; smoke-test it before promoting its exact revision. For Vertex AI it deploys no API keys and uses the dedicated service account with Vertex AI, Firestore and private bucket access. For Wanjie only, Cloud Run stores that provider credential in service configuration; restrict configuration access. No service-account keys are required.

Set the deployed service URL as `APP_ORIGIN`, and keep the public app accessible during judging. The application has a global model budget and daily quotas, but cloud billing alerts are not hard spending caps. Inspect actual billing daily.

The existing token cost ledger uses conservative estimates of $1.50/M input and $7.50/M output tokens, including thinking tokens; these are not verified Wanjie account prices or a provider billing cap. Check Wanjie usage/balance separately. Neither Wanjie model usage nor Google hosting is asserted to be free or covered by the GenAI App Builder trial credit.

## Documentation

- [Architecture and boundaries](docs/IMPLEMENTATION.md)
- [Research protocol](docs/RESEARCH.md)
- [Demo script](docs/DEMO-SCRIPT.md)
- [Submission checklist](docs/SUBMISSION.md)
- [Evaluation cases](eval/cases.json)

## Limitations

Same-model checking can repeat the original model's errors; a human must verify changed facts. Served-page checks prove that approved content is returned, not that customers understand it or returns decrease. Interviews, human semantic grading and non-developer usability testing are separate tasks. Model errors and budget limits are visible and do not silently switch to replay.

The prototype deliberately limits scale to one SKU per session and 12 runs. A production product would split session records into subcollections, add durable queued work, merchant authentication, stronger abuse prevention and a commerce connector.
