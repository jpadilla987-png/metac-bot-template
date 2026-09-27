# NIGHTEYE FutureEval — Verified Status

Last updated: 2026-09-27 PT

## Verified plumbing

- Controlled zero-cost smoke run: GitHub Actions run **36328357257**
- Question: Metaculus **45423**, “Will Waymo achieve 1 million weekly autonomous rides before 2027?”
- Result: workflow **PASS**
- Mode: **dry run**
- Forecasts produced: **1**
- Forecasts published: **0**
- Estimated LLM cost: **$0.00**
- Model route: `openrouter/openrouter/free`

This smoke run proves that credentials, free-router generation, parsing, and the local reporting path work on a nonpolitical technology question. It does **not** prove competitive forecast quality.

## Publication gates

Publication fails closed. Both variables must be exact string `true`:

- `ALLOW_METACULUS_POSTS=true`
- `NIGHTEYE_RESEARCH_READY=true`

The current GitHub workflows do not set those gates, so unattended publishing is disabled.

## Political/electoral safeguard

Before any forecast model call, questions are screened by `policy_guard.py`. Political, electoral, government, legislative, public-policy, and geopolitical questions are blocked conservatively.

The earlier test on question 43327 is historical containment evidence only; it must not be used as the automated test target.

## Research truth gate

The zero-cost bootstrap currently uses `researcher=no_research`. During the Waymo smoke run, the optional summarizer generated source-like text despite the lack of a real research payload. That exposed a quality failure.

Fix:
- bootstrap smoke mode now disables research summarization;
- publishing additionally requires `NIGHTEYE_RESEARCH_READY=true`.

Therefore the free bootstrap is a **plumbing test**, not a live-tournament publishing configuration.

## Current terminal state

- Bot plumbing: VERIFIED
- Zero-cost nonpolitical dry-run: VERIFIED
- Political/electoral filter: VERIFIED by CI
- Explicit publish authorization: VERIFIED by CI
- Research-readiness publish gate: VERIFIED by CI
- Live researched FutureEval publishing: NOT READY
- Metaculus LLM credits: DENIED
- Prize eligibility: still available according to the received Metaculus email
- Spend authorization: $0

Do not claim the bot is live in the tournament until a real research path is verified and a protected publishing run produces a receipt.
