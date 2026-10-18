# Pagemi public entry

Public address: https://pagemi.joeyzhao.cc

This Worker proxies to the fixed existing Cloud Run origin. It does not host the product backend or call a model. The browser stays on the branded domain. No domain purchase or subscription change was made.

Before translating an Origin to the upstream value, the Worker checks the exact public Origin. Foreign and missing write Origins are denied. Cookie, CSRF token, body, idempotency key, status and response stream are preserved. Both upstream fetching and client responses disable caching. No credentials are stored in Worker bindings. Logs are disabled. Redirects back to the fixed upstream are rewritten to the branded address.

Do not change the Cloud Run APP_ORIGIN to the public address: this edge entry performs the translation. Server-side storefront verification still reads the deployed Cloud Run page; the edge does not modify its body. Direct Cloud Run access remains a recovery path.

Run: `node --test infra/public-entry/worker.test.mjs`
Deploy: `wrangler deploy -c infra/public-entry/wrangler.jsonc`

Worker version: 83316f48-a4e7-461d-84b0-7d45cdda7285

Four local proxy tests pass. Two complete live synthetic workflows passed on the new domain, including cross-session and CSRF/Origin checks, publication, verification and restoration. The sanitized final run is in eval/results/pagemi-domain-2026-10-18.json. Earlier real-model evidence remains attributed to its original release.
