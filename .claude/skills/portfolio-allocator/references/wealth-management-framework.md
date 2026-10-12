# Wealth Management Framework

How to run the portfolio like a wealth manager rather than a stock picker. Used in Phases 0, 3, 5, 7 and 9.

## 1. The investment policy (IPS)

Each profile holds a short investment policy. It is the yardstick for every run and changes only at the annual review or when the user's circumstances change, never because of one month's news.

It records:
- **Objectives:** what the money is for and when (e.g. long-term wealth, house deposit in N years, early retirement). Money needed within ~5 years should not be in equities; flag it if it is.
- **Risk capacity vs risk tolerance:** capacity is what their finances can absorb (income stability, emergency fund, horizon); tolerance is what they can sit through. The binding one is the lower.
- **Strategic allocation:** target weights and bands per bucket (below).
- **Limits:** single-position caps, theme caps, thematic ETF cap, minimum meaningful position size.
- **Benchmarks** for each portfolio.
- **Exclusions** (anything they won't own) and preferences.
- **Policy last reviewed** date.

## 2. Structure: core-satellite

**ISA (compounding portfolio)**

| Bucket | What goes in it | Role |
|---|---|---|
| Core | 1-3 broad, cheap, accumulating UCITS index funds (global all-cap or developed world, optionally S&P 500 and EM) | Captures the market at low cost; the anchor everything else is judged against |
| Quality large-caps | Durable-moat businesses at reasonable prices | Long-term compounding with conviction |
| Thematic / sector ETFs | Themes and sectors with a specific thesis | Satellite bets; highest failure rate, so capped |
| Defensives / fixed income | Short-duration gilts or treasuries, staples, low-volatility | Ballast, used tactically within a band |

Why it matters: a portfolio built only from monthly £100 picks turns into dozens of tiny line items with no anchor. The 8 ISA slots per month stay; core top-ups count as slots. Each month's slot plan directs money to whichever bucket is furthest below target.

**eToro (venture sleeve)**

Venture logic: returns follow a power law, so a few winners pay for many losers. That requires (a) enough independent shots, (b) follow-on capital for the ones that prove themselves, (c) hard discipline on what counts as a shot, and (d) no single theme able to sink the sleeve.

## 3. Default limits (the profile can override)

ISA:
- Core at least 40% of the ISA, building toward 50-60%
- Any single stock at most 5% of the ISA
- Any single thematic or sector ETF at most 5%; all thematic/sector ETFs together at most 20%
- Defensives / fixed income band 0-15%, set tactically
- Minimum meaningful position: a new name should be one the policy is willing to build to at least ~2% over time; otherwise top up instead

eToro:
- Any single position at most 10% of the sleeve (a standing user decision can override this; respect it and only report the weight)
- Any single theme at most 30% of the sleeve (crypto counts coins + miners + exchanges; AI counts direct names + baskets + ETFs)
- New shots must fit the market-cap band in the profile (default: under ~$2-3B at entry). Holdings that grow out of it have "graduated": fine to keep, but they are no longer the moonshot sleeve's job and count toward concentration
- Follow-ons: into holdings whose operating numbers prove the thesis, at a reasonable entry, with the position still under its cap. Not averaging down on a weakening thesis

## 4. Rebalancing with cash flows

- Compute each bucket's drift from target. New money goes first to the most underweight buckets. This rebalances without selling, costs or tax.
- Sell to rebalance only when a bucket is outside its band and new money can't fix it within ~6 months. In the ISA, selling is tax-free; in the GIA, check CGT first.
- Tactical tilts from the market scan move weights within bands, never outside.
- Trims of big winners follow the limits, not feelings about the price.

## 5. Diagnostics (Phase 5)

**Allocation vs policy**: table of bucket, target, band, actual, drift.

**Concentration**: top 10 positions by weight in each portfolio and combined; theme map; ETF look-through. For look-through, use each ETF's top holdings and weights (issuer factsheet) to estimate effective exposure to names held directly (e.g. MSFT via VUAG + direct). Treat opaque baskets (like eToro Smart Portfolios) as overlapping their theme.

**Exposures**: sector, region and currency shares. A GBP-based investor with mostly USD assets carries large currency risk; that is acceptable for equities over the long term but should be a known choice. Fixed income held for ballast should be GBP or GBP-hedged.

**Style / duration**: share of long-duration growth (pre-profit, high multiple) vs value, quality and defensive. Rising real yields hit the former hardest.

**Mandate drift**: venture-sleeve names now large caps; satellites grown to core size; line items below the minimum meaningful size (candidates to consolidate or leave alone if tiny).

**Household overlap**: names, themes and ETFs held by both partners; combined theme concentration. Only aggregate overlap goes in the report.

**Stress test**: pick 3-4 scenarios relevant now. Rough betas are enough:
- Broad equity -30%: core ~-30%, quality large-caps ~-25%, thematic/growth ~-40 to -50%, micro-caps ~-50 to -60%, crypto-linked ~-60 to -70%, short gilts ~0 to +2%
- Rates +100bp: long-duration growth and pre-profit names hit hardest, banks and short-duration assets least
- Crypto -50%: miners and exchanges typically fall more than the coins
- GBP +10% vs USD: unhedged USD assets ~-10% in GBP terms
State the estimated loss in pounds for each portfolio and which positions drive it. The question is "is anything fragile or more concentrated than the policy intends?", not a forecast.

## 6. Benchmarks and the scorecard (Phase 3)

Default benchmarks (profile can override), both measured in GBP:
- ISA: a global all-cap or developed-world tracker (e.g. FTSE All-World or MSCI ACWI).
- eToro venture sleeve: a small-cap index (e.g. Russell 2000), with the global tracker as a second reference.

For each pick or top-up: entry date, entry price (actual from statements, or estimated from the screenshot P&L at the next run, marked as estimated), current price, return since entry, benchmark return over the same dates, and excess return. Summaries: hit rate (share beating benchmark), median and mean excess return, by category (new vs top-up, theme, entry tag, large-cap vs ETF). Judge new picks after at least 6 months; the venture sleeve on 2-3 years.

The scorecard exists to change behaviour. If satellites as a group trail the core after a fair period, shift slots toward core. If "Premium" entries keep losing, raise the bar for them.

## 7. Behavioural guardrails

Check the draft recommendations against these before finalising:
- **Recency bias:** is this month's headline doing too much work? Would the call still make sense in three months?
- **Narrative over-fitting:** a big macro story rarely needs more than a tilt within bands.
- **Disposition effect:** selling winners early and holding losers. Exits come from thesis and policy, not from P&L.
- **Anchoring:** the user's entry price is irrelevant to whether a stock is a buy now.
- **Confirmation bias:** the red-team bear case must be written before conviction is stated.
- **Activity bias:** a month with no new names is fine. Turnover costs money.
- **Overconfidence in forecasts:** prefer positions that work across several scenarios over ones that need one outcome.

## 8. Financial foundations (asked once, re-checked annually)

Not part of the monthly strategy, but a wealth manager checks them first. Stored in the profile:
- Emergency fund (3-6 months of essential spending) in place?
- Any high-interest debt?
- Workplace pension: getting the full employer match? For higher-rate taxpayers, extra pension contributions (especially salary sacrifice) can beat ISA investing because of tax relief.
- Lifetime ISA: if under 40 and saving for a first home or retirement, the 25% government bonus (up to £1,000 a year on £4,000) is hard to beat; it counts toward the £20,000 ISA allowance. Check withdrawal penalties and the property price cap before suggesting it.
- Income tax band (sets CGT and dividend tax rates for the GIA).
- Goals with dates, and any money needed within 5 years.
- Protection (life and income protection) if others depend on their income: mention once, no more.

If a gap exists, say so once in the report's notes; don't hold the run hostage to it.
