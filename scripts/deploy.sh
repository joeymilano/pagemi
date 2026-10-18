#!/usr/bin/env bash
set -euo pipefail
: "${GOOGLE_CLOUD_PROJECT:?Set GOOGLE_CLOUD_PROJECT}"
: "${EVIDENCE_BUCKET:?Set EVIDENCE_BUCKET}"
: "${RUNTIME_SERVICE_ACCOUNT:?Set RUNTIME_SERVICE_ACCOUNT}"
: "${APP_ORIGIN:?Set the exact public browser origin; do not replace it with a Cloud Run alias}"
: "${MODEL_PROVIDER:?Set the explicitly authorized provider: vertexai or wanjie}"
: "${GEMINI_MODEL:?Set the model verified for this provider}"
: "${MODEL_BUDGET_USD:?Set an explicitly authorized model estimate budget}"
case "$MODEL_PROVIDER" in
  vertexai) ;;
  wanjie) : "${WANJIE_API_KEY:?Set WANJIE_API_KEY in the process environment}" ;;
  *) echo "Unsupported deployment provider" >&2; exit 1 ;;
esac
# Google Cloud hosting/storage and model usage may incur charges. Never assume
# a product-specific promotional credit covers ordinary Gemini generation.
# Use a restricted temporary env file so credentials never enter command args.
umask 077
deploy_env=$(mktemp "${TMPDIR:-/tmp}/merchreflex-deploy.XXXXXX")
trap 'rm -f "$deploy_env"' EXIT
python3 - "$deploy_env" <<'PY'
import json, math, os, sys
budget = float(os.environ["MODEL_BUDGET_USD"])
if not math.isfinite(budget) or budget <= 0:
    raise SystemExit("MODEL_BUDGET_USD must be finite and positive")
settings = {
    "STORAGE_DRIVER": "firestore",
    "GOOGLE_CLOUD_PROJECT": os.environ["GOOGLE_CLOUD_PROJECT"],
    "GOOGLE_CLOUD_LOCATION": os.environ.get("GOOGLE_CLOUD_LOCATION", "global"),
    "MODEL_PROVIDER": os.environ["MODEL_PROVIDER"],
    "GEMINI_MODEL": os.environ["GEMINI_MODEL"],
    "EVIDENCE_BUCKET": os.environ["EVIDENCE_BUCKET"],
    "MODEL_BUDGET_USD": os.environ["MODEL_BUDGET_USD"],
    "MAX_DAILY_RUNS": os.environ.get("MAX_DAILY_RUNS", "40"),
    "APP_ORIGIN": os.environ["APP_ORIGIN"],
}
if settings["MODEL_PROVIDER"] == "wanjie":
    settings["WANJIE_API_KEY"] = os.environ["WANJIE_API_KEY"]
with open(sys.argv[1], "w") as f:
    json.dump(settings, f)
PY
# Deploy without moving public traffic. Smoke-test the candidate, then promote
# its explicit revision using gcloud run services update-traffic.
gcloud run deploy merchreflex --source=. --project="$GOOGLE_CLOUD_PROJECT" --region=asia-southeast1 --service-account="$RUNTIME_SERVICE_ACCOUNT" --allow-unauthenticated --min-instances=0 --max-instances=2 --concurrency=8 --memory=512Mi --cpu=1 --timeout=120 --no-traffic --tag=candidate --env-vars-file="$deploy_env" --quiet
