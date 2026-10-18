# Measured validation — 18 October 2026 release

Current evidence: [sanitized release report](../eval/results/vertex-release-2026-10-18.json). Provider: official Vertex AI, `gemini-3.8-flash`. Serving revision at verification: `merchreflex-00018-mib`. Prompt fingerprint: `c0f3d8f61a9a1f859d63a228967c874f8db95d891addc9f0ce020ec7990665f6`.

## Verified results

- 35 local tests passed, plus production build and type-check. Tests use mocked transport/in-memory storage and do not establish model accuracy.
- Five consecutive public full workflows passed on the final revision, with ten seconds between tests.
- Full-journey durations: 34.830, 69.479, 29.209, 20.244 and 30.874 seconds. Median 30.874 seconds; range 20.244–69.479. This is a five-run observation, not the planned 30-run p95 evaluation.
- Each journey exercised the live agent, approval, persistent publish, served-page verification, restoration and restored-page verification. Access, Origin/CSRF, cross-session isolation, unapproved publish denial and idempotency were also checked.
- Text, image, function-call and structured-output provider capability checks passed.
- Private normalized image upload/retrieval and isolation checks passed without extra model calls.

## Failures and limits

Two earlier public attempts on preceding revisions failed on upstream timeouts. One final-revision success recovered from a 504. They remain in the release report. Final candidate success is separate from the five public successes. Do not pool different versions into a clean reliability percentage.

All product records, specifications and feedback are synthetic. Independent human semantic grading, merchant interviews and non-developer task tests are pending. No evidence currently supports a revenue, conversion or return-rate improvement claim. Served-page verification checks returned content and versions, not customer understanding.

The 18 development-case paired baseline runs in the older report use an earlier prompt/configuration. They are historical execution data and have no completed independent semantic grade. The 12 reserved cases must not be represented as a completed current-release accuracy study.

## Remaining acceptance

- Record current UI evidence-change invalidation and dimension reassessment for the competition film. Earlier screenshots and local regression are not final-prompt filmed evidence.
- Conduct independent grading and non-developer testing; record real failures, assistance and individual timings.
- Complete the planned final-version benchmark only within newly approved or actually remaining budget. Current release allowance is intentionally limited.
- Ensure judging-period service capacity, create the public video, finalize the deck's video link, and confirm the portal receipt.

[Google Cloud release and budget handoff](HANDOFF_GOOGLE_CLOUD.md) · [Historical 13 October record](VALIDATION_2026-10-13_ARCHIVE.md)

The historical record is preserved for provenance. Its old model-provider, billing, test counts and deployment instructions are superseded by the current handoff. Do not unlink billing, disable Vertex AI or redeploy an old configuration based on that archive.

## Pagemi naming release

The product identity changed to Pagemi, producing prompt hash `3754665a83db1f525424138bb4a55b8a316052f139342a80ed6d90500e05192e`. Decision instructions are unchanged. 35 local tests, production build and type-check passed again. No new paid model workflows were run. Measurements above retain their original revision and fingerprint.

## Public domain update

The public entry is https://pagemi.joeyzhao.cc. Cloudflare forwards to the existing Google Cloud Run application without redirecting the browser. Gemini, Firestore and image storage remain on Google Cloud. Two full synthetic workflows passed through the new domain, including model generation, approval, publication, served-page verification and rollback. Measured post-preflight durations were 52.192 and 23.728 seconds. These are domain-integration checks, not new semantic grading. The earlier no-model-call statements refer only to the prior name-only release.
