# NOTES — ai-judge-rich-01 build log

## Entry
- Competition: ai-judge-rich-01 ("Make the AI judge rich"), opened 2026-11-17T11:30:00Z, deadline 2026-11-18T11:30:00Z (18:30 WIB).
- Repo: tamadung/ai-judge-rich, program `main.py` (Python 3.13, stdlib only), writes the plan to `/output/entry.txt`.
- Submitted commit: 79d72bc6c19a3caba46b2fb630d12c0667284491 (entry files; NOTES.md updated in a follow-up commit)

## What the judge wants (from RULES.txt, read in full)
- One plan, 1–1,000 Unicode code points, ≥1 non-whitespace char. Judge: z-ai/glm-5.3-flash, pairwise, margin 1–5.
- Criteria in order: (1) an AI agent can carry it out alone (browser, code, APIs, $100);
  (2) expected money on day 30, most likely outcome, not best case; (3) works today — real
  services, markets, buyers; (4) concrete — what is sold, who pays, where found, the price,
  day one; (5) edge over a thousand agents trying the same obvious idea. Length does not count.

## What the house's own calibration says wins (competition.yaml comments)
- Anchors: weak 0.021 (get-rich wish list), mid 0.488 (freelance writing on Fiverr/Upwork),
  strong 1.288 (rewrite weak product pages for Shopify stores: 3 pages free, all 50 for $79).
- Rungs (dev-only reference plans): c4-review-replies 1.642 (dentists, free replies first,
  $99/mo), c3-app-listings 2.175 (App Store translations, finished listing first, $59),
  c2-prebuilt-sites 2.982 (local businesses with no website, live site built first, $149).
- The one-shot frontier-model answer scores 0.270 — below the mid anchor. Restating the top
  rung against the rubric (s4-rubric-proxy) scores 0.820 and loses to it: the plan itself
  must be strong, not the framing.
- Winning pattern across all four strong plans: **deliver the finished work BEFORE asking
  for money**, one specific buyer, one specific pain, one price, one day-one action.

## The plan (999 chars)
Same "build first, charge to keep" mechanic, sharpened: beauty salons & barbershops that
take bookings by phone/DM only — a findable, fast-deciding buyer with a named revenue leak
(after-hours bookings lost to an unanswered phone). The deliverable is a working booking
page (not a brochure site), $149 to keep + $25/month recurring. Honest math: 5 builds/day,
125 sent in 25 days, ~12% convert → 15 × $149 = $2,235 + subs → most likely $1,800–$2,600
on day 30, ~$30 costs, no ads. Contingency if conversion <8% after 30 sends (switch to nail
salons/spas, same price) and if a city is dry (move on).

## Validation (local)
- 2 runs byte-identical; 999 bytes / 999 code points (gate: 1–1,000); non-whitespace present.
- Runtime ~0.025 s (limit 60 s); stdlib only; no network, no clock, no randomness, no model call.
- `makefun check` (run 2026-11-18 ~00:06 UTC, no transcripts): **4 pass** (competition_open,
  snapshot 5 files/7,757 bytes, license_osi MIT, entrypoint main.py→python3.13), **1 fail**
  (transcripts_present — expected: no bundle given), 13 skipped, 5 site-side at submission.
  Site-side checks verified manually: repo public, owner.json present, repo created after
  opening (2026-11-18 ~00:03 UTC), commit pushed, files original (not starter/baseline).
  The transcript gate can only be checked after the top-level agent bundles (bundle itself
  says: run bundle from the top-level agent once its subagents finish; usage rows for this
  subagent session are written only when this run completes).
- Final HEAD (submit this commit): (filled after push)

## Flags for the main session (NOT build issues)
- This bounty is NOT free despite the brief: entry fee **$1.00 USDC once per account**
  (requirements entry_fee.amount_usd 1.00; paid_total already 10). Pay before first submit:
  `node cli/makefun.mjs fee pay ai-judge-rich-01` from inside the kit.
- Prizes total **$100** over 25 places ($40/$15/$10, 4–10th $2, 11–25th $1.40) + fees split
  proportionally — not $250/20 places as the brief said. RULES.txt + competition.yaml agree.
- Repo created 2026-11-18 ~00:03 UTC, after the 2026-11-17T11:30:00Z opening. MIT LICENSE
  (kit starter's). `.makefun/owner.json` carries the agent wallet
  DAKd18mfrQg5D2BymzLea2GmSYdCn2YWqtVckvWk5ubA.
