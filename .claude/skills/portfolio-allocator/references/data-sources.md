# Data Sources

Where to get each kind of data, how to reach it from the session, and what to do when a source is blocked. Used in Phase 0 (data access check), Phases 4, 6 and 8.

## 1. Data access check (Phase 0)

What a session can reach depends on its environment. Check once at the start of each run and note the result in working notes:

1. **Web search**: run one search for a holding's latest earnings. This is the default research channel and normally works.
2. **Page fetch**: fetch one page (e.g. a stockanalysis.com quote page). In the cloud environment checked in October 2026, direct fetches and `curl` to finance sites were blocked by the environment's network policy, so research ran through web search only.
3. **Alpha Vantage MCP** (tools named `mcp__Alpha_Vantage_MCP_Server__*`, if connected): call `GLOBAL_QUOTE` for one ticker. On the free key: 25 requests a day, at most 1 per second; `GLOBAL_QUOTE`, time series, `INSIDER_TRANSACTIONS` and macro series worked; `COMPANY_OVERVIEW` returned "premium endpoint". Call tools one at a time, never in parallel.
4. **User-supplied data**: broker CSV exports, screenshots, screener exports or pages the user pastes. Always usable.

If fetch is blocked, tell the user once, in one line, that research is search-based and that adding the domains in section 4 to the environment's allowed domains (cloud environment settings, Network access) would let runs read primary pages directly. Then carry on. Never fill a gap with invented numbers; list it under evidence gaps.

### Alpha Vantage budget (free key, 25 calls/day)

Spend calls where search is weakest:
- Live quotes (`GLOBAL_QUOTE`) for the Tier 1 holdings and the finalists, so prices in the report are exact and dated
- `INSIDER_TRANSACTIONS` for micro-cap finalists (cross-check with search; an empty result may mean no coverage, not no trades)
- `EARNINGS_ESTIMATES` (revision history) and `ETF_PROFILE` (holdings, for look-through) where available
- Macro series (`TREASURY_YIELD`, `FEDERAL_FUNDS_RATE`, `CPI`, `FX_DAILY` for GBP/USD) only if search results are stale

Note which figures came from Alpha Vantage, with the "latest trading day" it reports.

## 2. Source map by need

When fetch is blocked, reach these through web search, including the site name in the query (e.g. `CRDO stockanalysis forecast`, `CRDO insider trading openinsider`, `IWDA justETF`). Prefer results that show a date.

| Need | Best sources | Notes |
|---|---|---|
| Prices, market cap, multiples | stockanalysis.com, Yahoo Finance, Google Finance, companiesmarketcap.com, Alpha Vantage `GLOBAL_QUOTE` | Note the as-of date; multiples differ by source (trailing vs forward) |
| Financial statements, history | Company filings (10-K, 10-Q, 20-F, annual reports), stockanalysis.com, macrotrends.net | Filings win when sources disagree |
| Filings and events | SEC EDGAR (8-K, S-1, S-3, 424B prospectuses, Form 4, 13D/G), LSE RNS via Investegate or londonstockexchange.com, Companies House | S-3/424B/ATM = dilution signal |
| Earnings releases, guidance, transcripts | Company investor relations pages, Seeking Alpha and Motley Fool transcripts, Quartr | Read guidance and the Q&A, not just the headline |
| Analyst ratings and targets | stockanalysis.com forecast pages, MarketBeat, TipRanks (analyst track records), Zacks (rank based on estimate revisions), Barchart, WSJ research ratings | See `stock-selection.md` for how to read them |
| Estimate revisions | Zacks, stockanalysis.com, Alpha Vantage `EARNINGS_ESTIMATES`, Yahoo Finance analysis tab | Revisions carry more signal than rating levels |
| Insider transactions | SEC Form 4 via EDGAR, OpenInsider (cluster buys), secform4.com, Alpha Vantage `INSIDER_TRANSACTIONS`; UK: director dealings RNS | Separate open-market buys from option exercises and scheduled 10b5-1 sales |
| Institutional ownership | 13F data via WhaleWisdom, Fintel, Dataroma (well-known value managers) | 13F is up to 45 days stale after quarter-end |
| Short interest | Finviz (short float), Fintel, Nasdaq short interest pages, MarketBeat | Updated twice monthly in the US |
| Screeners (US) | Finviz (fast, 60+ filters, free), TradingView (technical), Koyfin, stockanalysis.com screener, Yahoo Finance | Finviz filters are listed in `stock-selection.md` |
| Screeners (UK/Europe) | Stockopedia (StockRanks: quality, value, momentum), SharePad, TradingView, Koyfin | Stockopedia is paid; its performance claims are vendor claims |
| ETFs (UCITS) | justETF (TER, size, domicile, replication, holdings, comparisons), issuer factsheets (iShares, Vanguard, SPDR, Invesco, Xtrackers, Amundi), Morningstar UK, trackinsight | Get the exact ISIN and trading line |
| Macro and rates | FRED (yields, inflation), CME FedWatch (rate expectations), Federal Reserve and Bank of England sites, ONS (UK data) | Use dated releases |
| Economic and earnings calendars | Investing.com economic calendar, Nasdaq earnings calendar, Earnings Whispers, company IR pages | Confirm dates on the company IR page |
| Biotech catalysts | BioPharmCatalyst (FDA calendar, PDUFA dates), ClinicalTrials.gov, company pipeline pages | Cash runway vs next readout |
| Crypto | CoinGecko, CoinMarketCap, issuer pages for miners (hashrate, cost per coin), Glassnode summaries | Treat on-chain commentary as opinion |
| News | Reuters, Bloomberg, FT, CNBC, WSJ; for UK companies RNS first | Paywalled pages often surface via search snippets |
| Platforms and wrappers | eToro, Trading 212, Revolut help pages for ISA eligibility and fees; GOV.UK for tax rules | Check the instrument inside the ISA, not just on the platform |

## 3. Source reliability

- **Tier A (primary):** filings, company releases, exchange notices, issuer factsheets, central bank and government data.
- **Tier B (reputable secondary):** Reuters, Bloomberg, FT, WSJ, established data aggregators.
- **Tier C (opinion and vendor):** Seeking Alpha, analyst blogs, vendor rankings, affiliate "best of" lists.
- **Distrust:** promotion newsletters, anonymous forum claims, undated pages, figures without a source.

A verdict needs Tier A or two independent Tier B sources. Tier C can generate ideas and bear cases, never confirm facts.

## 4. Domains to allow for direct fetching

If the user wants runs to read primary pages directly, these are the domains worth adding to the environment's allowed domains:

```
stockanalysis.com, finviz.com, finance.yahoo.com, query1.finance.yahoo.com,
sec.gov, www.sec.gov, efts.sec.gov, data.sec.gov, openinsider.com,
marketbeat.com, tipranks.com, zacks.com, macrotrends.net, companiesmarketcap.com,
nasdaq.com, api.nasdaq.com, justetf.com, ishares.com, vanguardinvestor.co.uk,
morningstar.co.uk, fred.stlouisfed.org, cmegroup.com, federalreserve.gov,
bankofengland.co.uk, ons.gov.uk, gov.uk, londonstockexchange.com, investegate.co.uk,
clinicaltrials.gov, biopharmcatalyst.com, coingecko.com,
etoro.com, trading212.com, revolut.com
```

## 5. Asking the user for data

Some of the best data is behind the user's own logins. Ask for these when they would change a decision:
- Broker CSV exports or statements (exact cost basis and dates, for the scorecard and CGT)
- The broker's ISA instrument search for a finalist, if eligibility can't be confirmed by search
- A screener export (e.g. Finviz CSV) if they have Finviz Elite, Stockopedia or Koyfin
