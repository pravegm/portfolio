# Data Sources

Where to get each kind of data, how to reach it from the session, and what to do when a source is blocked. Used in Phase 0 (data access check), Phases 4, 6 and 8.

## 1. Data access check (Phase 0)

What a session can reach depends on its environment's network settings. At the start of each run:

1. Run `bash .claude/skills/portfolio-allocator/scripts/check_access.sh`. `200`/`301` means reachable; `000` means blocked by the network policy or refused by the site.
2. Use the **helper scripts** (section 1a) for every reachable source. They fetch through the session proxy with `curl`. The built-in WebFetch tool does **not** go through that proxy and failed for every finance site in testing, so don't rely on it.
3. **Web search** covers everything else (news, analyst commentary, pages on blocked hosts).
4. **eToro connector** (tools named `mcp__eToro__*`, if the person connected it): primary source for their eToro holdings, trades and instrument availability; see section 1b.
5. **Alpha Vantage MCP** (tools named `mcp__Alpha_Vantage_MCP_Server__*`, if connected) is a backup; see the budget below.
6. **User-supplied data** (broker CSV exports, screenshots, pasted pages) is always usable.

If an important source is blocked, tell the user once, in one line, which host and that it can be added under the environment's allowed domains (section 4). Never fill a gap with invented numbers; list it under evidence gaps.

Status in October 2026 (all domains in section 4 allowed): reachable through the scripts: stockanalysis.com, finviz.com, Yahoo Finance chart API, SEC (www.sec.gov, data.sec.gov, efts.sec.gov), api.nasdaq.com, companiesmarketcap.com, clinicaltrials.gov, justETF, iShares, MarketBeat, Zacks, Morningstar UK, London Stock Exchange, Investegate (RNS), Bank of England, Federal Reserve, GOV.UK, BioPharmCatalyst, eToro. Blocked by the site's own bot protection (Cloudflare challenge; use web search instead): TipRanks, Macrotrends, CoinGecko, Trading 212, Revolut. Refused by the site: openinsider.com, fred.stlouisfed.org (use SEC Form 4s and Yahoo/Alpha Vantage instead).

## 1a. Helper scripts

In `.claude/skills/portfolio-allocator/scripts/`, run with `python3 -I <script>`:

| Script | What it gives | Use in |
|---|---|---|
| `prices.py SYMBOLS --from DATE [--to DATE]` | Daily closes and return over a window from Yahoo (US tickers, `VWRP.L` for LSE, `.OL`, `.ST`, `.HK`, `GBPUSD=X`, `^RUT`, `^GSPC`, `^TNX`, `BTC-USD`) | Scorecard (pick vs benchmark since entry), dated prices in the report, 52-week context |
| `finviz.py quote TICKERS` | Snapshot: market cap, EV, P/E, forward P/E, EV/sales, margins, ROIC, cash/share, debt, insider and institutional ownership and transactions, short float, SMA distances, performance, analyst recommendation and target, next earnings date | Phase 6 holding review, Phase 8 candidate facts |
| `finviz.py preset NAME` / `finviz.py screen FILTERS` | Screen results (US-listed). Presets match the recipes in `stock-selection.md`: `microcap-quality-growth`, `microcap-insider-buying`, `quality-on-sale`, `large-earnings-momentum`, `biotech-cash-runway` | Phase 8 idea generation |
| `sec_filings.py TICKER --forms 4,144,8-K,S-3,424B5` | Recent SEC filings with links | Insider trades, dilution, material events |
| `fetch_text.py URL --find WORD` | Readable text from any reachable page, around a keyword | stockanalysis forecast/statistics pages, SEC filing documents, ClinicalTrials.gov API, Nasdaq API |
| `earnings_calendar.py TICKERS --days 45` | Upcoming US earnings dates with EPS estimates | Phase 4 calendar |
| `check_access.sh` | Which source hosts are reachable (`403` with a page = the site's bot protection; `000` = network policy or refused) | Phase 0 |

Useful pages for `fetch_text.py`:
- `https://stockanalysis.com/stocks/<ticker>/forecast/` (analyst count, consensus, target low/average/high, estimates) with `--find "price target"`
- `https://stockanalysis.com/stocks/<ticker>/statistics/` (valuation, share count change, margins, short interest) with `--find "Shares"`
- `https://stockanalysis.com/stocks/<ticker>/financials/?p=quarterly` (quarterly income statement)
- `https://stockanalysis.com/etf/<ticker>/holdings/` (US ETF holdings, for look-through when UCITS factsheets are blocked)
- `https://clinicaltrials.gov/api/v2/studies?query.term=<drug or company>` (trial status and dates)

Returns in GBP for a USD asset: `(1 + r_usd) x (GBPUSD at start / GBPUSD at end) - 1`; get both FX closes from `prices.py GBPUSD=X`.

SEC asks automated requests to declare a contact in the User-Agent. The scripts send a neutral placeholder; set the environment variable `SEC_USER_AGENT` to a real contact only if the user asks for that.

## 1b. eToro connector (tools named `mcp__eToro__*`)

If the person has connected eToro to their Claude account, it is the primary source for their eToro data. Load the tools with ToolSearch (`etoro`). **Read-only use only** (see the trading rule in SKILL.md).

| Tool | Use it for |
|---|---|
| `get-my-portfolio-summary` (`includePositions: true` when open dates are needed) | Every eToro holding with units, invested amount, average open rate, current value, P&L, plus copied traders (e.g. a Smart Portfolio/copy position) and pending orders. Replaces eToro screenshots. Amounts are in the account currency (USD for Praveg): convert to GBP with `prices.py GBPUSD=X` |
| `get-my-trading-history` (`minDate`: 6 April of the current tax year) | Closed trades with open/close dates and rates, `netProfit` and separate `fees`. Feeds the execution check (what was sold) and the realized-gains log for CGT. Keep the window near 90 days per call if it times out |
| `get-my-balances` | Cash across eToro accounts, including an eToro ISA (MoneyFarm) if one exists |
| `get-instruments-overview` (up to 100 symbols per call; batch them) | Whether each candidate can be bought on this account (`allowOpenPosition`), live bid/ask and spread, **whole vs fractional units** (`unitsQuantityType`), minimum position size, and whether a W-8BEN is required. Run it for every eToro finalist and top-up |
| `get-my-positions-and-orders` | Position-level detail and pending orders if needed |

Notes from testing (October 2026):
- Some newer US listings trade in **whole units only**. A £100 slot then buys a whole number of shares, so the amount can differ from £100 (or be impossible if one share costs more than the slot). Say so in the orders table.
- `allowOpenPosition: false` means it can't be bought on that account even if eToro lists it (e.g. VWRP.L on Praveg's account).
- Eligibility reflects the connected account (the regular trading account). It does not confirm eligibility inside an eToro ISA; check that separately.
- Trading history may not show everything recorded in the history file (e.g. trades closed outside the window, or inside a copy portfolio). Reconcile, and flag differences rather than guessing.

## 1c. ISA brokers

**Trading 212 (API, read-only):** Trading 212's public API (beta) supports Invest and Stocks ISA accounts. `scripts/trading212.py` reads cash, portfolio, order history, dividends, transactions, and the list of instruments tradeable on the account (the most reliable ISA-eligibility check, since the Trading 212 website blocks automated access). It sends GET requests only. Setup, done once by the account owner:
1. In the Trading 212 app, select the ISA account, go to Settings > API and generate a key with **read permissions only** (account data, portfolio, history, metadata; no order permissions).
2. In the cloud environment's settings, add `T212_API_KEY` and `T212_API_SECRET` (under Network secrets if offered, otherwise as environment variables), and add `live.trading212.com` to the allowed domains.
3. Start a new session. Never paste keys into chat.
If a call returns 401, the key is wrong, lacks a permission, or (reported by some ISA users) the API isn't yet enabled for that account; fall back to a CSV export or screenshots.

**Revolut ISA (no API):** Revolut offers no public API or connector for its ISA (the Revolut X connector covers only its crypto exchange). Use screenshots of the ISA holdings screen, or statements from the app's documents section.

### Alpha Vantage budget (free key, 25 calls/day)

Free key limits: 25 requests a day, at most 1 per second; `COMPANY_OVERVIEW` returned "premium endpoint" in testing. Call tools one at a time, never in parallel. Since Yahoo and Finviz now cover prices and snapshots, keep Alpha Vantage for:
- `EARNINGS_ESTIMATES` (revision history) for finalists
- `ETF_PROFILE` (holdings) for look-through when issuer pages are blocked
- `INSIDER_TRANSACTIONS` as a cross-check (an empty result may mean no coverage, not no trades)
- Macro series if needed

## 2. Source map by need

Use the helper scripts for reachable hosts. For blocked hosts, reach these through web search, including the site name in the query (e.g. `CRDO stockanalysis forecast`, `CRDO insider trading openinsider`, `IWDA justETF`). Prefer results that show a date.

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

Allowed domains match exact hostnames, so sites need both the bare and the `www.` form. The full list in use (October 2026):

```
stockanalysis.com, finviz.com, finance.yahoo.com, query1.finance.yahoo.com,
sec.gov, www.sec.gov, efts.sec.gov, data.sec.gov, api.nasdaq.com, nasdaq.com, www.nasdaq.com,
companiesmarketcap.com, clinicaltrials.gov, justetf.com, www.justetf.com,
ishares.com, www.ishares.com, vanguardinvestor.co.uk, www.vanguardinvestor.co.uk,
morningstar.co.uk, www.morningstar.co.uk, marketbeat.com, www.marketbeat.com,
zacks.com, www.zacks.com, tipranks.com, www.tipranks.com, macrotrends.net, www.macrotrends.net,
londonstockexchange.com, www.londonstockexchange.com, investegate.co.uk, www.investegate.co.uk,
bankofengland.co.uk, www.bankofengland.co.uk, federalreserve.gov, www.federalreserve.gov,
ons.gov.uk, www.ons.gov.uk, gov.uk, www.gov.uk, coingecko.com, www.coingecko.com,
biopharmcatalyst.com, www.biopharmcatalyst.com, etoro.com, www.etoro.com,
trading212.com, www.trading212.com, revolut.com, www.revolut.com,
fred.stlouisfed.org, cmegroup.com, openinsider.com
```

Anyone else running the skill from their own environment (e.g. Shubhi) needs the same list.

## 5. Asking the user for data

Some of the best data is behind the user's own logins. Ask for these when they would change a decision:
- Broker CSV exports or statements (exact cost basis and dates, for the scorecard and CGT)
- The broker's ISA instrument search for a finalist, if eligibility can't be confirmed by search
- A screener export (e.g. Finviz CSV) if they have Finviz Elite, Stockopedia or Koyfin
