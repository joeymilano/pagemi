# Pagemi — current Zcode handoff

Updated: 2026-10-18T10:08:55.535537+00:00. This is the current handoff; the earlier Wanjie and AI Studio paths are historical.

## Live release

- Public browser URL: https://pagemi.joeyzhao.cc
- Upstream Cloud Run origin / APP_ORIGIN: https://merchreflex-927668522599.asia-southeast1.run.app
- Google Cloud project: `merchreflex-cup-2026`; region: `asia-southeast1`.
- Serving revision: **`merchreflex-00023-fow`**, verified at **100% traffic**.
- Provider/model: **official Vertex AI / `gemini-3.8-flash` / `global`**. Generation and independent semantic verification both make real model requests; there is no replay fallback.
- Runtime identity: `merchreflex-app@merchreflex-cup-2026.iam.gserviceaccount.com`. It already has Vertex AI and Firestore permissions. Private image storage was verified. No API keys or service-account key files are deployed in this revision.
- `aiplatform.googleapis.com` is enabled. Cloud billing stays linked; do not unbind it under an assumption that Cloud Run/Firestore/storage will continue serving free.
- Current prompt fingerprint: `3754665a83db1f525424138bb4a55b8a316052f139342a80ed6d90500e05192e`. The measured fingerprint remains in the release evidence.
- Historical measured-release Cloud Build: `0be7c96e-c60f-421a-b1b0-283af5d03cc7`.

Use the branded public URL. The Cloudflare entry validates its exact Origin and translates it to the fixed Cloud Run APP_ORIGIN while preserving CSRF, cookies and streaming. Keep the upstream APP_ORIGIN unchanged. See infra/public-entry/README.md. Direct candidate tests still use the upstream write Origin.

## Pagemi branding release · 18 October 2026

Revision `merchreflex-00023-fow` completes Pagemi branding in UI, favicon, package metadata, health output and agent identity. Only the name changed in the agent prompt; its decision instructions are byte-for-byte unchanged. Its fingerprint changes accordingly. Provider, budget ledger, configuration and canonical URL are preserved. 35 local tests, build and type-check passed. Candidate health, title and icon were checked before moving traffic. No model requests were made for this rebrand. The five workflow measurements below belong to `merchreflex-00018-mib`; they were not rerun for the new prompt fingerprint.

## What was verified

- **35 local tests passed**, production build passed, type-check passed.
- Real official-model text, image, function-call and structured-JSON capability requests all succeeded. The returned image description matched the synthetic backpack/water-bottle image.
- Final candidate completed the entire synthetic workflow, including publish, served-page verification and rollback. It recovered from one 504 and took about 84 seconds.
- **Five consecutive public workflows passed** on the final revision. End-to-end durations: 34.830, 69.479, 29.209, 20.244 and 30.874 seconds. Tests were spaced 10 seconds apart. One public success included a recovered upstream 504.
- Each workflow checked unauthenticated access, Origin/CSRF rejection, cross-session isolation, unapproved publish rejection, approved publication, idempotency, served content, rollback and restored-page verification.
- Normalized private image upload/retrieval, anonymous image denial and cross-SKU verification denial passed without extra model calls.
- Observed generated actions corrected waterproof wording and accessory ambiguity, left unknown laptop fit pending evidence, and routed quality/fulfillment issues to a human.

These are synthetic mechanical/functional checks, not merchant interviews, independent semantic grading or proof of business impact. The two earlier public failures are retained in the report. Provider timeouts have **not** been proven eliminated, and five successes are not the planned 30-run p95 study.

Sanitized release evidence: [vertex-release-2026-10-18.json](../eval/results/vertex-release-2026-10-18.json). Raw test sessions remain in ignored `output/` and contain session/CSRF values; **do not publish them**.

## Authorized budget and current snapshot

The user explicitly approved **at most USD 1 of new model calls to get the demo working and online**. This does not authorize automatic recharge, an unbounded provider fallback, or another evaluation campaign.

- Historical application ledger before this release: USD 3.8764655. This is application accounting, not a cloud invoice.
- Cumulative application cap: `MODEL_BUDGET_USD=4.776465500000002`. This retains history and adds **USD 0.90** of new conservative workflow allowance.
- **USD 0.10** remains outside that allowance for diagnostics and safety margin; four direct capability tests estimate USD 0.00141825 at the currently published introductory prices.
- New conservative workflow usage at snapshot: **USD 0.6966045**, including unknown/timeout allowances.
- Remaining application allowance at snapshot: **USD 0.2033955**; outstanding reservations: USD 0.00.
- Google billing has not settled; promotional-credit coverage is unconfirmed. Do not describe the estimates as an invoice or a verified free service.

Every attempted generation request atomically reserves **USD 0.06** from the shared Firestore ledger. Concurrent instances cannot reserve past the configured cap. Returned usage settles at conservative USD 1.50/M input and USD 7.50/M output, including thinking tokens. Missing usage/timeouts retain the USD 0.06 allowance. An interrupted process leaves its reservation in place. Requests stop when there is less than USD 0.06 available; a run may stop before producing an approvable patch if the budget is exhausted.

Input is counted before generation using Vertex CountTokens (no charge) and limited to 16,000 tokens; output is limited to 4,096 tokens. At these conservative rates, a request including 2,000 extra input tokens of margin remains below its USD 0.06 reservation. A run permits at most eight model attempts, six read-only tools and 90 seconds. Recalculate these limits before changing model/pricing. Daily cap is 20 runs, Cloud Run min instances 0/max instances 2. These controls concern model calls; Cloud hosting, builds and storage have separate billing.

One earlier failed workflow had its whole-run USD 0.50 reserve reconciled to USD 0.018663 known usage + two USD 0.06 uncertain-attempt allowances = USD 0.138663. The original history and timestamp-preconditioned correction record remain in Firestore `budget-adjustments/3a4dfa0e-8cb0-4c48-9a2e-4b6eee975e92`. It is an application-accounting correction, not a Google refund. Do not erase or reset the ledger to bypass the authorized limit.

## Implementation notes

- `lib/model-config.ts`: explicit provider/model selection for runs, health and evaluation metadata.
- `lib/model-provider.ts`: official Cloud identity and fixed Google endpoint for Vertex; optional Wanjie implementation remains unused. Missing credentials never silently activate a different provider.
- `lib/agent.ts`: independent verifier system instruction, untrusted-input handling, input counting, request reservations and bounded retries. An upstream failure cannot create an approvable patch.
- `scripts/deploy.sh`: explicit provider/model/positive budget required, zero-traffic candidate, restricted temporary env file, no API keys in Vertex configuration.
- `.env.example` uses a zero budget to avoid accidental workflow charges. The local ignored `.env.local` contains the live provider settings and unused private keys; do not print or commit them. Standalone smoke scripts bypass the workflow ledger and must stay inside an authorized diagnostic allowance.
- Preserve the existing dirty `HANDOFF_ZCODE.md`, `.v2c/`, `.video_agent/`, `.zcode/` and earlier credit-test file. They were not included as unrelated changes in this release.

## Remaining competition work

1. Verify existing deck/video/submission artifacts and the actual portal receipt; this deployment does not establish submission completion.
2. Arrange human semantic grading, non-developer task tests and merchant interviews. Never report synthetic checks as market validation.
3. The full 30-run study, current-prompt holdout grading and baseline comparison are not completed by these smoke tests. Do not reuse older prompt/provider accuracy numbers as current results. Further paid evaluation needs budget planning within remaining authorization or a new approved allowance.
4. Test supplemental dimensions and live reassessment across the final prompt if needed; source invalidation, immutability and related execution controls already have local regression coverage. Earlier live evidence tests do not automatically become final-prompt semantic evidence.
5. Keep the canonical service available through judging, monitor the remaining application allowance and actual cloud costs, and do not silently raise the cap.
6. Retained Cloud Run revisions support rollback, but older revisions have different budget behavior; review configuration before rollback. Product-page rollback is a separate tested feature that creates a new page version.

## Sources and references

- [Official model documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-8-flash)
- [Official model pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)
- [CountTokens documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/capabilities/get-token-count)
- [Repository](https://github.com/joeymilano/pagemi)
- [Previous Wanjie investigation](HANDOFF_WANJIE.md)
