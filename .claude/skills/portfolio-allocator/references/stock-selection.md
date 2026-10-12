# Stock and ETF Selection

How to go from "we need a new name for this slot" to a short list worth deep research. Used in Phase 8, together with `research-methods.md` (deep-dive checks) and `data-sources.md` (where to get the data).

## The funnel

1. **Idea generation (wide):** 20-40 names per slot type from the idea sources below.
2. **Hard gates:** the screens below and the micro-cap gates in `research-methods.md`. Anything failing a gate is out unless an exception is written down.
3. **Scoring:** score survivors on the rubric; keep the top ~3x the number of slots.
4. **Deep dive:** full research per `research-methods.md`.
5. **Red team:** bear case, pre-mortem, kill criteria.
6. **Portfolio fit:** theme, factor, currency, look-through and household overlap.
7. **Rank and decide.** A pick needs a rubric score of 70+ and no unresolved red flag.

Record every name that reached step 3 and why it stopped. That list feeds the history's rejections and keeps later months from redoing the work.

## Idea sources

**Micro-cap sleeve (eToro)**
- Screens (recipes below) for quality growth and insider buying
- **Insider cluster buys:** several insiders buying on the open market within a few weeks (OpenInsider, Form 4)
- **Estimate revision leaders** among small caps (Zacks, stockanalysis.com)
- **Value-chain mapping** of themes the history allows: who supplies the winners (picks and shovels), and which small players have real contracts with them
- **Specialist investors:** 13F filings of small-cap focused funds, activist 13D filings
- **Special situations:** spin-offs, post-IPO names after lock-up expiry, recent uplistings to a main exchange, companies emerging from heavy investment phases into profitability
- **Conference and industry news:** small-cap conference presenters, contract awards, government programmes
- Names the user brings, and previously "considered" names from the history whose blocker may have cleared

**ISA large-caps**
- **Quality on sale:** wide-moat, high-return businesses trading below their own 5-year average multiple after a de-rating not caused by a broken thesis (the history shows this has worked: META, DE in August 2026)
- **Estimate revision leaders** among large caps
- **Regime beneficiaries:** businesses whose earnings rise in the current macro regime (e.g. banks in a hiking cycle, integrated energy in a supply shock), sized as tilts
- **Morningstar wide-moat lists** and fair value estimates (independent of sell-side)
- **Dividend growers and buyback compounders** with strong free cash flow

**ISA ETFs**
- Start from the policy bucket the slot plan funds (core, defensive, regional, thematic), then compare all candidate funds tracking suitable indices on justETF.

## Screen recipes

Recipes A to E are available as presets in `scripts/finviz.py` (`microcap-quality-growth`, `microcap-insider-buying`, `quality-on-sale`, `large-earnings-momentum`, `biotech-cash-runway`); the preset filters approximate the words below, so apply the remaining criteria by hand. Finviz covers US listings only: for UK and European names use web search or ask the user to run Stockopedia, SharePad, Koyfin or TradingView. Adjust or combine Finviz filter codes with `finviz.py screen` when a slot needs something different.

**A. Micro-cap quality growth**
- Market cap $50M to $2B; listed on NYSE or Nasdaq (or LSE/AIM for UK names)
- Average daily volume over 200K shares and price over $2
- Revenue growth over 20% year on year (latest quarter and trailing year)
- Gross margin over 35% (or improving for 4 quarters)
- Current ratio over 1.5; debt/equity under 0.5
- Shares outstanding growth under 15% over the past year
- Optional: price above its 200-day average (trend confirmation)

**B. Micro-cap insider conviction**
- Market cap $50M to $2B, main exchange
- Insider open-market purchases in the last 90 days by 2+ insiders, or by the CEO/CFO for a meaningful amount
- Exclude names with recent equity raises unless insiders bought in the raise
- Then apply screen A's quality checks manually

**C. Quality on sale (ISA large-caps)**
- Market cap over $20B
- Return on equity or ROIC over 15% for 5 years; operating margin stable or rising
- Forward P/E below its own 5-year average and below the sector median, or price 20%+ below the 52-week high
- Net debt / EBITDA under 2.5
- EPS estimates for next year flat or rising over the last 60 days (the de-rating is not an earnings collapse)

**D. Estimate revision momentum (large-caps)**
- Market cap over $10B
- Next-year EPS estimates up over the last 30-90 days, with more upward than downward revisions
- Positive earnings surprise last quarter and guidance raised
- Forward P/E not above ~1.5x its sector median, to avoid paying for perfection

**E. Pre-revenue biotech (venture sleeve, special case)**
- Market cap $100M to $3B
- Cash covers operations past the next major readout, with at least 6 quarters of runway
- Lead asset in Phase 2 or later with human data, in an indication with clear commercial demand
- Cash is a meaningful share of market cap (downside support)
- Clear dates for the next readout or approval decision

## Scoring rubrics

Score each survivor out of 100. Red flags (going concern, imminent dilution with no milestone, manipulation flags, promotion) are vetoes regardless of score.

**Micro-cap (venture sleeve)**

| Criterion | Points | What earns them |
|---|---|---|
| Asymmetry and 10x path | 20 | A concrete route to 10x (revenue x margin x multiple), with downside cushioned by cash, revenue or strategic value |
| Business quality and traction | 20 | Revenue growth, gross margin trend, retention, backlog, real customers |
| Financial strength and dilution risk | 15 | Runway, share-count discipline, no going-concern language, low debt |
| Management and alignment | 10 | Insider ownership, open-market buying, capital allocation record |
| Valuation vs growth | 15 | EV/sales vs growth and gross margin vs peers; reverse DCF |
| Revisions and trend | 10 | Upward estimate revisions; price trend not broken |
| Catalyst within 12 months | 10 | Dated, observable event that can re-rate it |

**Large-cap (ISA)**

| Criterion | Points | What earns them |
|---|---|---|
| Moat and quality | 25 | ROIC above cost of capital for years, stable margins, gross profitability, pricing power |
| Growth durability | 15 | Credible mid/high single-digit or better growth for 5+ years |
| Valuation | 20 | Forward P/E and FCF yield vs own history and peers; reverse DCF |
| Balance sheet and capital allocation | 15 | Leverage, buybacks/dividends funded by FCF, sensible M&A |
| Revisions and analyst signal | 10 | Estimate revisions up; rating changes up; low forecast dispersion |
| Trend | 5 | Not in a breaking downtrend without explanation |
| Portfolio fit | 10 | Adds something the ISA lacks; low overlap with core ETFs |

**ETF selection (in order)**
1. Right index for the bucket's job (what's inside, weighting, caps)
2. Ongoing charge
3. Fund size (prefer over £500M; avoid under £100M)
4. Tracking difference over 3-5 years
5. Ireland domicile, physical replication, accumulating share class
6. Available inside the user's ISA, on a GBP-traded line if the platform charges FX
7. Look-through overlap with what's already held

## Reading analyst ratings

What the evidence suggests:
- **Rating levels are weak signals.** Most covered stocks are rated Buy, and sell-side ratings lean optimistic. One study found high consensus ratings only helped among stocks with favourable quantitative characteristics, and were followed by worse returns among stocks with unfavourable ones.
- **Changes carry more signal than levels.** Changes in consensus recommendations and **earnings estimate revisions** have been more robust predictors than the level of the rating; prices tend to under-react to revisions and drift in their direction, more so when analysts' forecasts agree (low dispersion).
- **Analyst quality varies.** Recommendation changes from historically accurate analysts carry more information. TipRanks ranks analysts by success rate and return (vendor methodology, not independently audited); its "top analyst" consensus is a useful second view.
- **Small caps:** coverage is thin (often 1-4 analysts), frequently from banks that underwrote the company's share sales. Check whether a covering bank ran the latest offering, and discount its rating.
- **Price targets** are 12-month, tend to follow the price, and cluster. Use the **spread** (low to high) as a gauge of uncertainty and the average as sentiment, not as a valuation.
- **Independent views:** Morningstar fair value and moat ratings are valuation-based and not tied to banking relationships; useful for large caps.

How to record it in the report: "Consensus Buy (19 analysts), average target $282 (range $200-$350), next-year EPS estimates +4% over 30 days (6 up, 0 down)."

## Insider, institutional and short-interest signals

- **Insider buying:** opportunistic open-market purchases (not part of a yearly routine) have predicted returns, while routine trades show roughly none (Cohen, Malloy and Pomorski, "Decoding Inside Information"). Cluster buys and meaningful CEO/CFO purchases matter most.
- **Insider selling** is mostly noise (diversification, tax, scheduled 10b5-1 plans). It matters when it is large, clustered, unscheduled, or by founders reducing sharply, and especially alongside zero buying.
- **Institutional ownership:** specialist small-cap funds or respected long-term managers building positions (13F) is supportive; an activist 13D can be a catalyst. 13F data is stale by up to 45 days.
- **Short interest:** high and rising short interest (say over 15-20% of float) is a warning that informed sellers disagree. Find and read any short report before buying. It also means squeeze risk, which is not a thesis.

## Forensic and quality scores (flags, not decisions)

- **Piotroski F-score (0-9):** 7+ strong, 3 or lower weak. Strongest evidence is among cheap, high book-to-market stocks.
- **Altman Z-score:** under 1.8 suggests distress, 1.8-3.0 grey zone. Not meaningful for banks or very early-stage companies.
- **Beneish M-score:** above -1.78 flags possible earnings manipulation.
- **Accruals:** earnings far above operating cash flow have historically been followed by weaker returns (Sloan, 1996).
- **Net share issuance:** heavy issuers have historically underperformed; buyback firms outperformed (Pontiff and Woodgate, 2008). Central to micro-cap dilution checks.
- **Gross profitability:** gross profit to assets has predicted returns about as well as value (Novy-Marx, 2013); a good quality proxy.
- **Quality in small caps:** the small-cap premium is much stronger once low-quality "junk" is excluded (Asness et al., "Size Matters, if You Control Your Junk").

## Valuation toolkit by company type

- **Profitable compounders:** forward P/E and EV/EBIT vs own history and peers, FCF yield, **reverse DCF** (what growth and margins the price implies, and whether that is plausible).
- **High-growth, unprofitable:** EV/next-12-month sales vs growth and gross margin; Rule of 40 for software (growth % + FCF margin %); path and timing to breakeven; dilution-adjusted per-share value.
- **Banks:** price/tangible book vs return on tangible equity; net interest margin; CET1 capital; credit costs.
- **Insurers:** price/book vs ROE; combined ratio.
- **Energy and commodities:** EV/EBITDA at mid-cycle prices; breakeven commodity price; reserve life; all-in sustaining cost for miners.
- **Biotech:** cash vs market cap; risk-adjusted pipeline value (probability of success by phase); runway past the next readout.
- **Crypto miners:** EV per unit of hashrate; all-in cost per coin; power contracts; AI/HPC hosting contracts.
- **REITs:** price/FFO; discount or premium to NAV.

## Sector KPIs to check

- Software: net revenue retention, RPO/backlog, customer count growth, Rule of 40
- Semiconductors: book-to-bill, inventory days, customer concentration, design wins
- Hardware/AI infrastructure: backlog, hyperscaler capex guidance, gross margin under mix shift
- Consumer: same-store sales, gross margin, inventory
- Industrials/defence: book-to-bill, backlog, programme wins
- Fintech/lenders: origination volume, credit losses, funding costs
- EV/battery: deliveries, cost per kWh, cash burn per unit
- Space: launch cadence, backlog, contract awards

## Price trend and timing

Timing is secondary to the thesis but matters for entry:
- **Momentum** (12-month return excluding the last month) is a well-documented factor (Jegadeesh and Titman, 1993); 1-month returns tend to reverse slightly.
- **Post-earnings drift:** prices tend to keep moving in the direction of an earnings surprise (Bernard and Thomas, 1989). A beat with raised guidance and a positive price reaction supports entry; a miss with a cut does the opposite.
- **Practical rules:** avoid adding after a 50%+ run in 3 months (the history's ALB lesson); for de-rated quality, prefer entries once the price has stabilised rather than mid-fall; for micro-caps, avoid buying days before earnings unless the catalyst is the point; use limit orders.

## Sources for the evidence above

- [Size Matters, if You Control Your Junk (CEPR DP12684)](https://cepr.org/publications/dp12684); [AQR summary](https://www.aqr.com/Insights/Perspectives/The-Small-Firm-Effect-Is-Real-and-Its-Spectacular)
- [Decoding Inside Information (NBER w16454)](https://www.nber.org/papers/w16454.pdf)
- [Analyzing the Analysts: When Do Recommendations Add Value?](https://opact.sdu.edu.tr/vufind/SummonRecord/FETCH-LOGICAL-a5967-edcb61ed493d55f767fd3723877bd0dcba926898eb40bb6949376c32c17edced3); [Dispersion in analyst forecasts and earnings momentum](https://eu.vlex.com/vid/dispersion-in-analyst-forecasts-856415963); [Lured by the Consensus](https://finance.business.uconn.edu/wp-content/uploads/sites/723/2014/08/Lured-by-the-Consensus-The-Implications-of-Treating-all-Analysts-as-Equal.pdf)
- [TipRanks top analysts methodology](https://www.tipranks.com/news/labs/tipranks-identifies-the-top-25-analysts-of-the-decade)
- [Thematic ETFs: 3 things to know (Capital Group, citing Morningstar)](https://www.capitalgroup.com/individual/ca/en/investments/exchange-traded-funds/resources/thematic-etfs--3-things.html)
- [Stockopedia StockRanks](https://www.stockopedia.com/learn/stockranks-&-ratings/the-stock-ranks-463088) (vendor claims)
- [Piotroski F-score overview](https://www.oldschoolvalue.com/piotroski-score/); [Stock Rover grades and scores (Altman Z, Beneish M)](https://www.stockrover.com/metrics/grades/)
- [Best free stock screeners 2026 (NerdWallet)](https://www.nerdwallet.com/investing/learn/best-stock-screeners)
- Classic papers cited by name: Sloan (1996) accruals; Pontiff and Woodgate (2008) share issuance; Novy-Marx (2013) gross profitability; Jegadeesh and Titman (1993) momentum; Bernard and Thomas (1989) post-earnings drift.
