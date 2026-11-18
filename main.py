# ai-judge-rich-01 entry (Python 3.13, standard library only).
# Writes one plan to /output/entry.txt: the plan an AI agent would follow
# to turn $100, a computer with internet access and 30 days into the most
# money. Deterministic: the same bytes on every run. No network, no clock,
# no randomness, no model call.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Goal: turn $100 into $1,800-$2,600 in 30 days selling booking pages to phone-only salons.",
        "Day 1: list 200 hair, nail and barber salons on Google Maps: 4+ stars, 50+ reviews, no website or booking link. Build 5 pages from their listings.",
        "Each page: services, prices, photos, and a booking form that emails them every request. Hosted free; send the live link by email or DM.",
        "Offer: $149 to keep it on their domain, $25 a month for hosting and updates. Paid by Stripe link.",
        "Daily: build 5, send 5, follow up once after 2 days, log replies in a sheet. Days 1-25: 125 sent.",
        "Math: 12 in 100 say yes, so 15 buyers x $149 = $2,235, plus $25 a month each. Most likely $1,800-$2,600 on day 30. Costs $30. No ads.",
        "If under 8 in 100 say yes after 30 sends, switch to nail salons and spas at the same price. Dry city? Move on.",
        "Edge: rivals promise a website. This sends the finished page first, so the owner sees their shop taking bookings before paying - fixing bookings lost after hours to an unanswered phone.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
