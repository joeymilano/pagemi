# Pagemi — judge-facing argument and evidence map

Pagemi helps a merchant repair a misleading product page using explicit evidence, exact-wording approval, versioned publication and a read-back check.

## The problem in one concrete example

A synthetic backpack page promises 100% waterproof protection and shows a bottle. Its merchant specification supports light rain only and excludes the bottle. Answering one complaint leaves that same page available to the next shopper. Pagemi proposes supported changes to the page itself.

Target user: a small-store operator or commerce content manager maintaining product descriptions and FAQs. This is a product hypothesis. No merchant interview or adoption result is claimed.

## Four decisions worth demonstrating

| Decision | What to show | What the evidence supports |
|---|---|---|
| Is this a page repair? | Fix the rain claim; route a broken zipper to human action | Actual final-release classifications in the sanitized response excerpt |
| Can we say it yet? | Unknown laptop fit stays unresolved; add dimensions and reassess | Implementation + historical dimension capture; current filmed reassessment still required |
| Is approval still valid? | Supplement evidence after approval; observe outdated state | Domain regression + implemented version checks; capture current UI for the film |
| Did publication reach the page? | Publish, open/refresh storefront, verify, then restore | Five complete public workflow tests on final revision |

## Competitive argument

Do not claim that product editing or human approval alone is new. Lead with the combined task: correct disposition, missing-fact handoff, evidence-bound approval and verification of the served version. Avoid unsourced “first”, “only”, or claims that a competitor cannot do this.

## What the technology contributes

Gemini interprets text/images and selects read-only evidence tools. A separate request checks proposed wording. Code constrains fields, source references, ownership, deadlines and budgets. Firestore transactions enforce version checks at publication; a model cannot decide to bypass those checks. Same-model checking remains fallible, so the merchant verifies facts before approving.

## Evidence to put on screen

- 5 consecutive public workflows on final revision; 20.244–69.479 seconds across five journeys.
- 35 local tests; their purpose is execution/integrity, not semantic accuracy.
- 2 earlier timeout failures preserved; one later public success needed a bounded retry.
- Synthetic data and image disclosure.
- Current-release source: `eval/results/vertex-release-2026-10-18.json`.

Do not say “100% accurate”, “zero hallucinations”, “reduces returns”, “saves X hours”, “merchant validated”, or “production Shopify integration”. No finished fair accuracy comparison or human task test exists yet.

## Answers to difficult questions

**Why an agent?** It selects which source to inspect, distinguishes repair from information gaps and produces a bounded patch. Subsequent execution remains controlled by code and the merchant.

**Why not just write better copy?** The objective is to remove a specific, evidenced source of confusion while avoiding unsupported new promises. A pleasant rewrite alone does not establish factual support or safe publication.

**Can the verifier also be wrong?** Yes. Independent requests to the same model can share errors. Deterministic controls and human review address different risks; none proves universal truth.

**Does “verified” mean the customer problem is solved?** No. It confirms that the approved content/version is served. Customer understanding, support volume and return rates require separate study.

**What scales next?** Authorized merchant data, a development-store connector, authenticated merchant accounts, durable jobs, split persistence and billing/abuse controls. The current single-SKU session prototype is intentionally narrow.

**What is the business model?** Test whether merchants repeatedly use and value maintenance first. Store/SKU-based charging is an experiment, not measured revenue or a validated price.
