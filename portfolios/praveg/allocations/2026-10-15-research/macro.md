# Macro and market scan: 2026-09-19 to 2026-10-15, plus a 45-day calendar

Prepared 2026-10-15 for the monthly portfolio run (previous run: 2026-09-20).

**How to read the numbers.** Baseline prices are closes on **Fri 2026-09-18**, the last trading day before the previous run (2026-09-19 was a Saturday). Unless stated otherwise, the latest prices are **US closes on 2026-10-14**, and **2026-10-15** prices for LSE, Europe, Asia, futures and crypto (intraday values on the morning of 15 Oct). Prices come from Yahoo Finance daily closes via `prices.py`. News figures are attributed to the sources linked inline. Where two sources disagree, both are given.

---

## 1. Headline: what changed since 20 September

1. **Rates went higher still.** The US 10y yield went from 5.00% (18 Sep) to a 24-year high of about 5.31-5.36% in early October, then eased to 5.19% (14 Oct). The 30y yield peaked around 5.65-5.73%. UK 10y gilts reached about 5.51-5.53%, the highest since 2007, and 30y gilts about 6.03-6.05%, the highest since 1998.
2. **US inflation re-accelerated while jobs stalled, a stagflation mix.**
   - September CPI (released 14 Oct): 3.7% y/y headline, against 3.6% expected; 0.6% m/m. Core CPI was 0.3% m/m.
   - September payrolls (released 2 Oct): +29k. Unemployment rose to 4.2%.
   - Market pricing of an October Fed hike swung from about 70% to about 20% after the jobs report, then back to about 34-54% after CPI. A hike by December is now priced at more than 90%.
3. **Energy shock escalated rather than resolved.**
   - Kpler counted a record 10 tankers struck in Hormuz between 28 Sep and 4 Oct, and Hormuz traffic fell to a two-month low.
   - A strike on Riyadh airport on 10 Oct (blamed on the Houthis) was followed by Saudi strikes on Houthi fuel sites on 13 Oct.
   - Brent is unchanged at about $104, while WTI fell 6%.
   - US-Iran talks are stalled. One source reports a US pledge of no strikes on Iran before the 3 Nov midterms.
4. **The AI trade cracked between 12 and 14 Oct.** Four triggers stacked up, and SOXX fell 7.2% from 9 to 14 Oct:
   - the Broadcom CEO's "casino" and financing warning (12 Oct);
   - China's CXMT DRAM claim, which sent SK Hynix down about 10% and Samsung down about 7% (13 Oct);
   - BlackRock's research arm downgrading US tech, the Firmus data-centre IPO being pulled, and wider tech credit spreads;
   - the hot CPI print (14 Oct), after which AI-infrastructure and bitcoin-miner names fell 12-16% in one session.
5. **Rotation into quality and defensives.** Since 18 Sep: staples +3.9%, healthcare +3.3%, MSCI USA Quality +3.1%, energy +5.2%, cybersecurity +3.9%, MSFT +8.1%, META +10.8%. Against that: Russell 2000 -4.6%, uranium -14.7%, gold miners -12.7%, copper miners -7.4%, defence -4.5%, Korea -11.9%, and the speculative growth basket -15% to -38%.

**Regime verdict: ESCALATION, not reversal.** The September regime was an energy-shock inflation, the Fed hiking again and long yields near 5%. It has intensified: yields are higher, inflation is hotter, the BoE is split towards a hike and the oil supply shock is broadening. A new dimension has been added: a growth scare (+29k payrolls) and an AI-financing and valuation scare that is hitting the most rate-sensitive, long-duration and speculative assets. This is a tougher, narrower market, not a new bull or bear regime. The S&P 500 is still +0.9% since 18 Sep and was at a record 7,818.93 on 6 Oct.

---

## 2. Market levels and moves (since 2026-09-18 close)

### Indices, rates, FX, commodities, crypto

| Asset | 18 Sep 2026 | Latest (date) | Change | Notes |
|---|---|---|---|---|
| S&P 500 (^GSPC) | 7,650.50 | 7,718.94 (14 Oct) | +0.89% | High close 7,818.93 on 6 Oct. -1.11% on 14 Oct |
| Nasdaq Comp (^IXIC) | 26,522.54 | 26,692.87 (14 Oct) | +0.64% | High close 27,599.79 on 6 Oct. -2.46% from 9 to 14 Oct |
| Russell 2000 (^RUT) | 2,860.40 | 2,729.53 (14 Oct) | **-4.58%** | Fell almost every week |
| VUAG.L (S&P 500, GBP) | 110.30 | 112.42 (15 Oct) | +1.92% | Beat the USD index because GBP fell |
| FTSE 100 (^FTSE) | 10,659.10 | 10,737.60 (15 Oct) | +0.74% | |
| Euro Stoxx 50 | 6,236.20 | 6,138.58 (15 Oct) | -1.57% | |
| DAX | 25,304.06 | 25,214.71 (15 Oct) | -0.35% | |
| Nikkei 225 | 65,018.95 | 64,425.95 (15 Oct) | -0.91% | |
| EEM (EM, USD) | 67.03 | 64.39 (14 Oct) | -3.94% | |
| EWY (Korea) | 181.31 | 159.83 (14 Oct) | **-11.85%** | Memory/AI selloff |
| EWZ (Brazil) | 37.52 | 42.60 (14 Oct) | **+13.54%** | Election rally |
| FXI (China large cap) | 34.32 | 33.86 (14 Oct) | -1.34% | |
| Nifty 50 (^NSEI) | 23,346.40 | 23,021.45 (15 Oct) | -1.39% | |
| INDA (India, USD) | 48.02 | 47.04 (14 Oct) | -2.04% | |
| VIX | 14.81 | 17.58 (15 Oct) | +2.8 pts | Still low given the backdrop |
| US 10y (^TNX) | 5.00% | 5.19% (14 Oct) | +19bp | Close high 5.31% on 5 Oct; intraday 5.34-5.36% |
| US 5y (^FVX) | 4.86% | 4.99% (14 Oct) | +14bp | |
| US 30y (^TYX) | 5.33% | 5.53% (14 Oct) | +19bp | |
| US 2y (2YY=F futures) | 4.42% | 4.75% (14 Oct) | **+33bp** | Front end repricing hikes |
| US 13w bill (^IRX) | 3.98% | 4.09% (14 Oct) | +11bp | |
| GBP/USD | 1.3358 (17 Sep) | 1.3249 (15 Oct) | -0.81% | Sat around 1.32-1.33 throughout |
| Brent (BZ=F) | $103.87 | $104.21 (15 Oct) | +0.33% | Range $99.25 (22 Sep) to $106.65 (12 Oct) |
| WTI (CL=F) | $100.30 | $93.97 (15 Oct) | -6.3% | Low $88.28 on 7 Oct. Brent-WTI spread widened to about $10 |
| Gold (GC=F) | $4,424.90 | $4,163.00 (15 Oct) | **-5.9%** | Low close $4,107.90 on 14 Oct |
| Silver (SI=F) | $66.56 | $56.53 (15 Oct) | **-15.1%** | |
| Copper (HG=F, $/lb) | 6.615 | 6.540 (15 Oct) | -1.1% | COMEX record about $6.83 on 22 Sep (source below) |
| Aluminium (ALI=F) | 3,446.75 | 3,086.25 (14 Oct) | -10.5% | |
| US nat gas (NG=F) | 2.912 | 3.246 (15 Oct) | +11.5% | |
| Bitcoin | $80,901 | $81,024 (15 Oct) | +0.15% | High close $86,603 on 21 Sep. Holding $80k only just |
| Ether | $2,611 | $2,368 (15 Oct) | -9.3% | |
| Solana | $112.60 | $102.04 (15 Oct) | **-9.4%** | |
| BNB | $761.02 | $718.78 (15 Oct) | -5.6% | |

### Sectors and themes (US-listed ETFs, 18 Sep to 14 Oct close)

| Up | Change | Down | Change |
|---|---|---|---|
| FRO (tankers) | +9.4% | BDRY (dry bulk freight) | -20.0% |
| XLE (energy) | +5.2% | URA (uranium/nuclear) | **-14.7%** |
| XLP (staples) | +3.9% | GDX (gold miners) | **-12.7%** |
| CIBR (cybersecurity) | +3.9% | COPX (copper miners) | -7.4% |
| XLV (healthcare) | +3.3% | ARKG (genomics) | -6.5% |
| IGV (software) | +3.2% | LIT (lithium/battery) | -5.8% |
| QUAL (quality factor) | +3.1% | ITA (aerospace/defence) | -4.5% |
| XLU (utilities) | +1.5% | IWM (small caps) | -4.5% |
| XLK (tech) | +0.4% | QTUM (quantum) | -4.0% |
| RSP (equal weight S&P) | -0.1% | BOTZ (robotics/AI) | -2.9% |
| SMH (semis) | -1.4% | SOXX (semis) | -2.6% (-7.2% from 9 to 14 Oct) |
| | | XLF (financials) | -2.4% |
| | | XLRE (real estate) | -2.5% |
| | | TLT (20y+ Treasuries) | -2.9% |
| | | MTUM (momentum) | -1.5% |
| | | IBB (biotech) | -0.6% |

Short duration held up: SHY -0.1%, IB01.L (0-1y Treasuries, USD) +0.3%, IGLT.L (UK gilts) +0.05%.

### Watchlist tickers (18 Sep to 14 Oct close)

**Winners and quality:**

| Ticker | Change |
|---|---|
| META | +10.8% |
| CEG | +9.8% |
| XOM | +8.2% |
| MSFT | +8.1% |
| ISRG | +6.8% |
| V | +6.3% |
| PHR | +5.9% |
| BRK-B | +3.3% |
| CRDO | +1.9% (after +24% to 220.83 on 6 Oct, then -17.2% from 9 to 14 Oct) |
| S | +1.4% |
| AMZN | +0.2% |
| NVDA | -0.4% |
| GOOGL | -0.5% |
| VRTX | -1.9% |
| NEE | -2.6% |
| AVGO | -3.2% |
| JPM | -4.1% |
| DE | -4.9% |

**Losers:**

| Ticker | Change |
|---|---|
| MARA | **-37.8%** |
| GPCR | **-37.5%** |
| RIOT | **-36.4%** |
| WULF | **-32.2%** |
| ACHR | -22.6% |
| QS | -21.8% |
| TLRY | -21.3% |
| IONQ | -19.7% |
| EVLV | -19.2% |
| PGY | -17.7% |
| NNE | -17.3% |
| KTOS | -17.1% |
| SOFI | -16.2% |
| MP | -15.5% |
| RIVN | -13.6% |
| TEM | -12.2% |
| ALB | -11.7% |
| CRSP | -11.2% |
| COIN | -11.0% |
| INCY | -11.0% |
| ACMR | -10.8% |
| VRT | -10.7% |
| MU | -10.0% |
| SYM | -9.5% |
| RKLB | -8.4% |
| INOD | -7.0% |
| NIO | -6.8% |

Moves from 9 to 14 Oct only: IONQ -21.2%, CRDO -17.2%, WULF -16.2%, RKLB -13.2%, VRT -8.2%.

**Read-across.** This is a broad de-rating of long-duration, cash-burning or financing-dependent growth: miners, quantum, eVTOL, solid-state batteries, small nuclear, fintech lenders and clinical-stage biotech. Profitable mega-caps (MSFT, META, V, ISRG) and power and energy cash flows (CEG, XOM) were bid. The venture sleeve's style is on the wrong side of this rotation. The ISA's quality and mega-cap core is on the right side.

---

## 3. Detail by area

### 3.1 Rates and central banks

**Federal Reserve (target range 3.75-4.00% since 16 Sep)**
- **Minutes of the 15-16 Sep meeting (released 7 Oct):** most participants judged that another hike would likely be appropriate by year end ([Scotsman Guide](https://www.scotsmanguide.com/news/fed-policymakers-saw-multiple-2026-rate-hikes-as-likely-september-fomc-minutes-show/)). The meeting calendar was checked directly on [federalreserve.gov](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm). Next meetings are **27-28 Oct** and **8-9 Dec** (the December one comes with projections).
- **After payrolls (2 Oct):** October hike odds fell from about 70% to about 20% ([CNBC 2 Oct](https://www.cnbc.com/2026/10/02/fed-rate-hike-odds-decline-after-september-jobs-report.html); [Investing.com](https://www.investing.com/analysis/fed-october-28-decision-why-hike-odds-hover-near-20-200689427)).
- **After CPI (14 Oct):**
  - CME FedWatch October hike odds rose to 53.7% from 22.1% the day before ([CNBC 14 Oct](https://www.cnbc.com/2026/10/14/fed-may-now-have-to-hike-twice-or-increase-by-a-half-point-in-december-traders-bet.html)).
  - Other snapshots put a hold at about 66%, i.e. a hike at about 34% ([Bloomingbit/Forbes](https://en.bloomingbit.io/feed/news/122238)), and Kalshi/Polymarket at about 34% ([DeFi Rate](https://defirate.com/prediction-markets/fed-decision-odds/)).
  - At least one hike by December is priced at more than 95% (CNBC) or about 94% ([BigGo](https://finance.biggo.com/news/e52d4f40-0d38-499d-914b-dfe40f5eab84)).
  - CNBC reports traders now see a chance of two hikes, or 50bp, in December. Citi forecasts a 25bp hike in December.
- **Treasury yields:** 10y at 5.31% on 1 Oct, the highest since May 2002, and 30y at 5.65%. Peaks of about 5.34% and 5.70% came on 6-7 Oct ([FXStreet](https://fxstreet.com/news/us-treasury-yields-hit-24-year-highs-as-10-year-tests-535-202610071450); [Trading Economics](https://tradingeconomics.com/united-states/government-bond-yield/news/588457)). The 30y auction on 8 Oct cleared at 5.618%. Pimco's Ivascyn said 6% is possible ([MercoPress 12 Oct](https://en.mercopress.com/2026/10/12/yields-on-key-us-treasury-bonds-reached-new-highs-but-for-the-10-year-demand-was-especially-strong/comments)).

**Bank of England (Bank Rate 3.75%)**
- **16-17 Sep meeting:** a **6-3 vote to hold**, with Greene, Mann and Pill voting to hike to 4.00%. The MPC said CPI "is likely to rise further over coming quarters". It also voted unanimously to take QT to zero by 2034, at an average of £46bn a year including £20bn of annual sales ([BoE September 2026 summary and minutes](https://www.bankofengland.co.uk/monetary-policy-summary-and-minutes/2026/september-2026)).
- **Next decision: Thu 5 Nov**, with a Monetary Policy Report; then 17 Dec ([BoE MPC dates](https://www.bankofengland.co.uk/monetary-policy/upcoming-mpc-dates)).
- **Expectations:** in an ii retail poll, two-thirds expect a hike on 5 Nov ([interactive investor 23 Sep](https://www.ii.co.uk/analysis-commentary/two-thirds-investors-predict-uk-interest-rate-hike-november-ii540364)). That is sentiment, not market pricing. **Gap: no SONIA/OIS pricing was found.**
- **Gilts:** 10y about 5.51-5.53%, the highest since 2007; 30y about 6.03-6.05%, the highest since 1998 (6-7 Oct) ([roic.ai](https://www.roic.ai/news/uk-30-year-gilt-yield-spikes-to-6034-highest-since-1998-10-07-2026); [roic.ai 8 Oct](https://www.roic.ai/news/uk-gilt-yields-spike-to-multi-decade-highs-as-fiscal-fears-mount-10-08-2026)). BofA expects about £15bn of extra borrowing.

**ECB**
- **Next meeting 28-29 Oct**, with the decision on 29 Oct ([ECB calendar](https://www.ecb.europa.eu/press/calendars/mgcgc/html/index.en.html)).
- **Deposit rate:** sources conflict, at 2.50% or 2.00% ([Admiral Markets](https://admiralmarkets.com/analytics/traders-blog/ecb-meeting-october-2026)).
- **Inflation:** August euro-area HICP was about 3.2%.
- **Pricing:** futures on 24 Sep implied about a 60% chance of a hike to 2.75% on 29 Oct (via Admiral/ECB Watch). Danske sees a hold through 2027, while Deutsche Bank expects +25bp in December.
- **Gap:** the current ECB rate and current pricing are unverified.

**Other central banks**
- **RBI:** a Reuters poll expected a hike to 5.50% at the 5-7 Oct meeting; the outcome was not confirmed ([Outlook Business](https://www.outlookbusiness.com/markets/sensex-nifty-slip-ahead-of-rbi-policy-west-asia-tensions-weigh)).
- **BoJ:** decision around 30 Oct (secondary calendars only; [days.to](https://days.to/bank-of-japan-interest-rate-decision)).

### 3.2 Inflation and jobs

**US CPI for September (released 14 Oct)**
- Headline 3.7% y/y against 3.6% expected; 0.6% m/m.
- Core 0.3% m/m against 0.2% expected. Core y/y is reported as 2.6%, against 2.4% prior.
- Gasoline +9.1% m/m accounted for more than half of the monthly rise. Shelter +0.4%.
- Sources: [CNBC](https://www.cnbc.com/2026/10/14/cpi-inflation-report-september-2026.html); [Morningstar](https://www.morningstar.com/economy/september-cpi-report-shows-inflation-37-annual-rate).
- The 2.6% core y/y figure looks low next to a 3.7% headline. It is as reported, but worth verifying on bls.gov.

**US payrolls for September (released 2 Oct)**
- +29k against about 90k expected; unemployment 4.2%, up from 4.1%.
- Net revisions -60k, with July revised to -10k. Average hourly earnings +0.1% m/m and +3.0% y/y.
- Sources: [investinglive](https://investinglive.com/news/us-september-non-farm-payrolls-29k-vs-90k-expected/); [wichitaliberty summary of BLS](https://wichitaliberty.org/economics/september-2026-jobs-report).
- Wage growth of 3.0% is below CPI of 3.7%, so real wages are falling.

**Other US inflation data**
- The latest PCE (August) was 3.4% headline and 3.0% core (per Investing.com/Scotsman Guide coverage).
- Previous context: August PPI +5.4% y/y. No September PPI found; **gap**.

**US fuel prices**
- Diesel hit a record **$6.53/gal** in the week of 21 Sep, then $6.38 in the week of 28 Sep. Gasoline was $4.46 ([trucknews/EIA](https://www.trucknews.com/transportation/us-diesel-average-hits-4-859-a-gallon-with-further-price-spikes-possible/1003210829); [startbusinessbystate/EIA](https://startbusinessbystate.com/?p=19869)).
- No October EIA print found; **gap**.

**UK**
- CPI for August was 3.1%, up from 2.9%. Core was 2.6% and CPIH 3.3% (ONS via [secondary](https://www.kaeltripton.com/uk-inflation-rises-3-1-percent-fuel-airfares/); 3.1% confirmed in the BoE minutes).
- September CPI is due on **21 Oct**. The Ofgem cap rose again in October.
- Unemployment was 4.9% (May-Jul). Regular pay +3.5% (Apr-Jun). Labour data is due on **20 Oct** ([financecalendar](https://www.financecalendar.com/?p=2189)).

**Euro area:** HICP about 3.2% in August.

### 3.3 Energy: Brent and WTI, Hormuz, Iran

**Prices**
- **Brent:** about $104 on 15 Oct, flat since 18 Sep, in a range of $99-107.
- **WTI:** fell 6% to about $94. The widening Brent-WTI spread points to a seaborne and Middle East premium, not a US shortage.

**Hormuz and Gulf shipping**
- Kpler: **10 tankers struck between 28 Sep and 4 Oct**, against a previous weekly record of 6. Hormuz transits fell to a two-month low ([CNN 8 Oct](https://www.cnn.com/2026/10/08/business/oil-diesel-prices-tanker-attacks-hormuz-intl); [oilprice.com](https://oilprice.com/Latest-Energy-News/World-News/Brent-Holds-Above-100-as-Hormuz-Tanker-Traffic-Hits-Two-Month-Low.html)).
- On 14 Oct Brent rose above $107 intraday after reports that Iran attacked two vessels using "new tactics" ([Euronews](https://euronews.com/2026/10/14/oil-prices-rise-after-reported-attacks-on-ships-in-strait-of-hormuz)).
- There was the first deep-Gulf tanker attack in nearly a month, off Qatar ([oilprice.com](https://oilprice.com/Latest-Energy-News/World-News/First-Deep-Gulf-Tanker-Attack-in-Nearly-a-Month-Hits-Vessel-off-Qatar.html)).
- The IEA agreed to speed up stock releases and prioritise diesel ([Bol News 8 Oct](https://bolnews.com/business/oil-prices-climb-as-attacks-on-gulf-shipping-intensify)).
- European gas is near a four-year high.

**Houthis and Saudi Arabia (a new front)**
- 10 Oct: a strike on Riyadh's King Khalid airport killed at least 12; the US blamed the Houthis.
- 13 Oct: Saudi-led strikes on Houthi fuel sites in Sanaa, Hodeidah and Dhamar. The Houthis threatened Aramco.
- Trump said he is considering joining in, and suggested Iran is pushing oil prices up before the midterms.
- Sources: [CBS](https://www.cbsnews.com/live-updates/iran-war-trump-us-elections-saudi-arabia-yemen-houthis/); [GlobalSecurity day 229](https://www.globalsecurity.org/military/ops/iran-war-oprep.htm).
- Iran's foreign minister offered on 11 Oct to mediate between Riyadh and the Houthis ([Al Jazeera](https://www.aljazeera.com/news/2026/10/12/iran-saudi-talks-on-yemens-houthis-whats-in-it-for-tehran)).

**US-Iran**
- Talks are stalled, and Iran called the US response "insufficient" (CBS).
- GlobalSecurity reports an **8 Oct pledge of no US or Israeli strikes on Iran before 3 Nov**. This is unverified against primary reporting.
- **No deal. No reopening of Hormuz.**

**OPEC+**
- On 4 Oct the 7 countries held November output at 31.01mb/d, a second month of pause. Most of the earlier increases were "on paper" because of the war.
- **Next meeting 1 Nov** ([OPEC press release](https://opec.org/pr-detail/1891616-4-october-2026.html); [Nairametrics](https://nairametrics.com/2026/10/05/opec-keeps-november-oil-production-unchanged-at-31-01-million-bpd/)).

**Asymmetry**
- Oil and tankers keep upside from escalation.
- The downside tail is a pre-midterm de-escalation or deal. Trump has a political incentive to lower pump prices before 3 Nov.
- That makes energy a hedge, not a fresh chase.

### 3.4 Metals

**Gold**
- -5.9% since 18 Sep, to about $4,163 (15 Oct). It touched $4,066 on 7 Oct, the lowest since 5 Aug.
- Drivers: real yields at 24-year highs and a firm dollar ([USAGOLD 7 Oct](https://www.usagold.com/daily-precious-metals-market-report-october-7-2026/); [Khaleej Times](https://www.khaleejtimes.com/gold-falls-to-two-week-low-as-rising-treasury-yields-dollar-weigh); [Mettis](https://mettisglobal.news/Gold-dips-to-4122-on-firm-dollar-63985)).
- Gold fell more than 6% in September. Silver fell 15% and gold miners (GDX) 12.7%.
- **The September context of "gold about $4,380" is now stale.**

**Copper**
- COMEX hit a record of about $6.83/lb on 22 Sep, and LME three-month hit records of about $14,700-14,875/t on 8-10 Sep ([Benchmark](https://source.benchmarkminerals.com/article/lme-copper-forward-curve-hits-record-high); [Canadian Mining Report](https://www.canadianminingreport.com/blog/copper-nears-record-highs-as-supply-tightens-can-the-rally-continue)).
- Now 6.54 (-1.1% since 18 Sep). COPX is -7.4%.
- Supply is still tight (treatment charges at zero, LME stocks down about 40% since May), but the miners are de-rating along with growth.

**Lithium**
- Latest benchmark: battery-grade carbonate at $19,750/t CIF Asia on 2 Sep, up from $18,160 on 10 Aug ([Benchmark via axis-intelligence](https://axis-intelligence.com/lithium-price/)).
- No October print; **gap**. LIT -5.8%, ALB -11.7%.

**Uranium**
- The long-term contract price hit a record of about $96/lb, yet the equities are falling. Utilities are reluctant to contract, and reactor developers are hit by rates ([24/7 Wall St 3 Oct](https://247wallst.com/investing/2026/10/03/uranium-prices-just-broke-a-19-year-record-but-nuclear-stocks-are-collapsing-anyway/); [24/7 Wall St 14 Oct](https://247wallst.com/investing/2026/10/14/nuscale-power-falls-7-as-10-year-treasury-yield-climbs-to-5-26-energy-fuels-drops-9-oklo-slides-5)).
- URA -14.7%, NNE -17.3%.

### 3.5 Equities and rotation

**US**
- The S&P 500 made a record close of 7,818.93 on 6 Oct, then fell 1.3% to 14 Oct.
- Breadth is poor: equal-weight is flat, the Russell 2000 is -4.6% and momentum is -1.5%.
- **Q3 earnings (FactSet, 9 Oct):** S&P 500 growth is estimated at **29.6%**, revised *up* from 26.7% on 30 Jun. That would be the third straight quarter above 25%. FactSet's conservative beat-adjusted projection is 35.6%. Guidance is 72 positive against 44 negative. Forward P/E is **19.1** ([FactSet](https://insight.factset.com/sp-500-earnings-season-preview-q3-2026); [Earnings Insight 9 Oct PDF](https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_100926.pdf)).
- So fundamentals for large caps remain strong. The selloff is about the discount rate and financing, not earnings.
- **Banks:** JPM's Q3 (13 Oct) was a miss. Net income was $15.3bn and EPS $5.57 ($5.75 excluding a $658m securities loss) against about $5.90 expected. Revenue was $50.2bn against $51.2bn expected. FICC fell; equities trading was +49% ([SEC 8-K supplement](https://www.sec.gov/Archives/edgar/data/0000019617/000162828026065582/a3q26erfex992supplement.htm); [WealthBriefing](https://www.wealthbriefing.com/html/article.php/net-income-for-third-quarter-2026-rises-at-jp-morgan)). XLF is -2.4%.

**UK and Europe:** the FTSE 100 is +0.7%, helped by energy and defensives. The Euro Stoxx 50 is -1.6%.

**Japan:** the Nikkei is -0.9%. No October BoJ or Japan-specific news was found; **gap**.

**EM**
- EEM is -3.9%, with Korea -11.9% after the memory selloff. Bloomberg calls it EM's worst day since July (13 Oct) ([Bloomberg](https://www.bloomberg.com/news/articles/2026-10-13/ai-selloff-drags-emerging-stocks-down-weighs-on-currency-gauge)).
- **Brazil is +13.5% (EWZ)**:
  - In the first round on 4 Oct, Flávio Bolsonaro took 47.03% against Lula's 45.16%.
  - The Ibovespa rose 7.7% on 5 Oct to a record and 8.8% that week.
  - The **runoff is on 25 Oct** ([Rio Times](https://www.riotimesonline.com/brazil-stocks-real-first-round-2026/); [Trading Economics](https://tradingeconomics.com/brazil/stock-market/news/589584)).

**India**
- The Nifty is -1.4% since 18 Sep and about -13.9% YTD.
- Foreign investors pulled ₹44,166 crore in October to date, and more than ₹3 lakh crore YTD.
- The rupee hit a record low of 96.30/$ on 5 Oct because of oil ([Free Press Journal](https://www.freepressjournal.in/business/fpis-dump-44166-crore-in-october-2026-equity-outflows-cross-3-lakh-crore); [NewsBytes](https://www.newsbytesapp.com/news/business/indian-rupee-slips-to-9630-as-oil-rises-foreign-outflows/tldr)).
- India is an oil importer, so it is hurt by this regime.

**Defence:** ITA is -4.5% and KTOS -17%. No specific catalyst was found (peace or a budget). It looks like a growth and momentum de-rating; **gap**.

### 3.6 AI and semis: why growth names fell 12-15 Oct

The 14 Sep "slow down frontier AI" shock (Amodei, backed by Altman and Musk; [Forklog](https://forklog.com/en/news/chipmaker-stocks-drop-after-altman-and-amodei-call-to-slow-ai-development)) was absorbed. SOXX rallied from 533 (18 Sep) to a high of 589.51 (5 Oct). Then a stack of hits arrived:

1. **12 Oct, Broadcom CEO Hock Tan in Singapore.** He compared many AI investors to casino gamblers with "very extreme expectations". He also warned that **financing could become the biggest limit on AI growth** and questioned loss-making AI labs. SOXX fell about 3% and AVGO about 2% ([investinglive](https://investinglive.com/stocks/broadcom-ceo-likens-ai-boom-to-a-casino-even-as-he-targets-230-billion-in-chip-sales/); [247wallst](https://247wallst.com/investing/2026/10/13/broadcoms-ceo-just-compared-ai-investors-to-gamblers/)).
2. **13 Oct, CXMT.** China's CXMT claimed progress on 4F² DRAM, with a new DDR5 RDIMM expected by year end. SK Hynix fell about 10% and Samsung about 7%, and the Kospi fell about 5.5%. Micron fell too ([Forbes](https://www.forbes.com/sites/siladityaray/2026/10/13/ai-chip-stocks-slide-amid-china-advances-and-ceos-casino-warnings/); [Bloomberg](https://www.bloomberg.com/news/articles/2026-10-13/cracks-grow-across-the-ai-trade-as-memory-chip-stocks-tumble)). This is a roadmap claim, not a product in production.
3. **13 Oct, AI financing worries.**
   - BlackRock's research arm downgraded US tech-driven equities.
   - The Nvidia-backed data-centre operator Firmus withdrew its IPO of up to about $5.5bn.
   - Bond investors demanded wider spreads on tech debt ([Semafor](https://www.semafor.com/article/10/13/2026/tech-stocks-slide-as-investors-fret-ai-overspending); [BGov](https://news.bgov.com/capital-markets/firmus-misfire-casts-shadow-on-data-center-ipos-in-the-pipeline)).
4. **14 Oct, hot CPI.**
   - The October hike is back in play and the 10y is around 5.2%.
   - In one session: CoreWeave -16%, Nebius -11%, Oracle -9%, and AI-pivot miners about 12-13% (TeraWulf -12.6%, Core Scientific, Cipher, IREN).
   - Cointelegraph called it Wall Street's worst selloff since July ([Bloomingbit](https://en.bloomingbit.io/feed/news/122254); [Cointelegraph via Coinspectator](https://coinspectator.com/cointelegraph/2026/10/15/bitcoin-miners-plunge-up-to-13-in-wall-streets-worst-selloff-since-july/)).
   - On 14 Oct the S&P fell 1.11%, the Nasdaq 1.88%, the Russell 2.0% and SOXX 4.5%.

**Diagnosis.** It is the expensive, debt-funded or "second-derivative" AI-infrastructure layer that is breaking: neoclouds, miners turning into data centres, optics and connectivity (CRDO), memory, and power and cooling (VRT). Cash-rich hyperscalers are not: MSFT is +8%, META +11%, NVDA flat. The **hyperscaler capex guidance on 28-29 Oct (MSFT, GOOGL, META, AMZN) is the next decisive test**, then NVDA on 18 Nov.

### 3.7 Crypto

- **Bitcoin** is flat since 18 Sep at about $81.0k on 15 Oct. It peaked at $86.6k on 21 Sep and fell to the low $81k range after CPI. About $1bn of crypto bets were liquidated (15 Oct) ([CoinDesk](https://coindesk.com/markets/2026/10/15/nearly-usd1-billion-in-crypto-bets-liquidated-as-bitcoin-ether-and-xrp-slide); [crypto.news](https://crypto.news/bitcoin-price-drops-below-81k/)).
- One analyst warns that **a clean break below about $80k opens $65-70k**. The September "must hold $80k" test is being retested now.
- **Solana** is -9.4% and led weekly losses among the top 8 (-10.1% on the week, to about $104.6). **BNB** is -5.6% and **ETH** -9.3%.
- **Miners have decoupled badly from BTC.** MARA, RIOT and WULF are -32% to -38% while BTC is flat. Drivers:
  - their AI-hosting pivot makes them AI-infrastructure credit plays;
  - balance sheets are under pressure;
  - MARA sold about $81m of BTC around 10 Oct;
  - aggregate miner BTC treasuries fell to about 1.19m BTC from about 1.9m at the end of 2025 ([Trefis 14 Oct](https://www.trefis.com/articles/618694/why-did-mara-stock-fall/2026-10-14); [24/7 Wall St 8 Oct](https://247wallst.com/investing/2026/10/08/cleanspark-sinks-7-as-mining-stocks-lag-bitcoin-mara-drops-5-strategy-slips/)).
- **COIN** is -11%.
- **Regulation:** the CLARITY Act market-structure bill failed a Senate procedural vote **49-50 on 15 Sep**, over ethics language on presidential crypto income ([bit.com summary](https://www.bit.com/knowledge-hub/clarity-act-senate-vote)). Talks continue, but passage before the 3 Nov midterms looks unlikely. The CFTC and SEC are moving by rulemaking instead, with an SEC comment deadline cited for 20 Oct ([Crowdfund Insider](https://www.crowdfundinsider.com/2026/10/317112-clarity-act-supporter-argues-that-sec-cftc-crypto-rules-fall-short-without-legislation/)).
- **ETF flows:** no October 2026 spot-ETF flow data found; **gap**. IBIT is +0.5%.

### 3.8 GBP/USD

- GBP/USD went from 1.3358 (17 Sep) to 1.3249 (15 Oct), -0.8%. It is down 1.9% from 1.3501 on 14 Sep.
- The fall reflects gilt and fiscal stress ahead of the Budget and a hawkish Fed.
- A weaker pound flatters GBP returns on USD assets: VUAG.L +1.9% against the S&P 500 at +0.9%.
- A Budget that reassures gilt markets, or a BoE hike on 5 Nov, could reverse this.

### 3.9 Hottest trades and whether the asymmetry remains

| Trade | Since 18 Sep | Asymmetry now |
|---|---|---|
| Tankers (FRO) and energy (XLE, XOM) | +5% to +9% | Still positive while Hormuz attacks escalate, but de-escalation risk before the midterms is the tail (8 Oct no-strike pledge to 3 Nov; Trump's political incentive). **Hold, don't chase.** |
| Power and utilities for AI (CEG +9.8%) | Up | Cash-generative and rate-tolerant. Reasonable, but valuation is rich. Earnings on 6 Nov |
| Memory / HBM (MU -10%, Korea -12%) | Reversing | The CXMT claim adds a China-supply risk to a cyclical peak. Asymmetry has worsened |
| AI infrastructure small and mid caps (CRDO, VRT, neoclouds, AI-pivot miners) | -10% to -38% | Cheaper, but the catalysts are binary (capex guidance 28-29 Oct, NVDA 18 Nov) and financing risk is rising. **Asymmetry improving but not yet confirmed.** Wait for hyperscaler capex |
| Gold and gold miners | -6% / -13% | Real yields are the headwind. The hedge value returns if growth cracks or the Fed blinks. Miners are now cheaper than in September |
| Bitcoin at $80k | Flat | Binary at $80k. Below it, analysts flag $65-70k. Hot CPI and a December hike are headwinds |
| Brazil | +13.5% | Event-driven, with the runoff on 25 Oct. Too late to chase for this portfolio |
| Quality mega-caps (MSFT, META, V, ISRG) | +6% to +11% | Defensive growth working. Q3 EPS is strong |

---

## 4. Regime classification of the major developments

**Overall: ESCALATION of the September regime (energy-shock stagflation, with central banks hiking into it), with a growth scare and an AI-financing scare added. Not a reversal.**

| Development | Date | Classification | Why |
|---|---|---|---|
| US 10y and 30y at 24-year highs; UK gilts highest since 2007/1998 | 1-7 Oct | **Regime-level** | Discount-rate shock for all long-duration assets |
| September CPI 3.7% hot; October and December hike pricing | 14 Oct | **Regime-level** | Confirms hiking into the energy shock |
| Payrolls +29k, unemployment 4.2% | 2 Oct | **Regime-level (emerging)** | Adds stagflation or growth-scare risk; may cap the Fed later |
| Record tanker attacks; Houthi-Saudi escalation (Riyadh airport strike) | 28 Sep to 14 Oct | **Regime-level** | Supply shock broadening, not resolving |
| BoE 6-3 split (3 for a hike) | 17 Sep | **Portfolio-level** | Matters for gilts, GBP and the UK ISA ballast |
| Broadcom "casino" and financing warning; Firmus IPO pulled; BlackRock tech downgrade | 12-13 Oct | **Portfolio-level (could become regime-level)** | Hits the AI-infrastructure financing chain. Watch credit spreads and capex guidance |
| CXMT 4F² DRAM claim | 9-13 Oct | **Portfolio-level** | Memory and Korea specific. A roadmap claim |
| Crypto miners -32% to -38% | Through 14 Oct | **Portfolio-level** | Directly affects the venture sleeve |
| Gold -6%, silver -15% | Since 18 Sep | **Portfolio-level** | A real-yield effect, not a change in the gold thesis |
| Uranium equities -15% despite record contract prices | Since 18 Sep | **Portfolio-level** | Nuclear names are trading as long-duration growth |
| Brazil election rally | 4-9 Oct | **Noise** for this portfolio (EM tracker only) | |
| JPM Q3 miss | 13 Oct | **Noise / portfolio-level** for financials ETFs | |
| CLARITY Act failure | 15 Sep | **Portfolio-level** (crypto) | Legislative tailwind delayed until after the midterms |
| UK Budget on 28 Oct (new Chancellor Healey) | Upcoming | **Portfolio-level** (ISA, tax) | |

---

## 5. Event calendar: 2026-10-15 to 2026-11-30

Dates are taken from official pages where marked ✔ (federalreserve.gov, bankofengland.co.uk, ecb.europa.eu, gov.uk, opec.org). The rest come from secondary calendars and should be confirmed.

### Macro, policy and politics

| Date | Event | Source / status |
|---|---|---|
| Tue 20 Oct | UK labour market (Jun-Aug), 07:00 | financecalendar (secondary) |
| Tue 20 Oct | SEC comment deadline on crypto rules (cited) | Crowdfund Insider (secondary) |
| **Wed 21 Oct** | **UK CPI for September**, 07:00 | ONS bulletin "next release" (secondary) |
| **Sun 25 Oct** | Brazil presidential runoff | Rio Times |
| **Tue-Wed 27-28 Oct** | **FOMC**; decision 28 Oct 19:00 UK time. Hike odds about 34-54% | ✔ federalreserve.gov |
| **Wed 28 Oct** | **UK Autumn Budget** (Chancellor John Healey's first) with the OBR forecast | ✔ [gov.uk letter to TSC](https://gov.uk/government/publications/chancellor-letter-to-the-treasury-select-committee-tsc-budget-2026-date) |
| Wed-Thu 28-29 Oct | **ECB**; decision 29 Oct 13:15 UK time (14:15 CET) | ✔ ECB calendar for the date; time from secondary |
| **Thu 29 Oct** | **US PCE for September** (personal income and outlays), 08:30 ET | BEA listing via secondary; one source says 4 Nov |
| Late Oct (unconfirmed) | US Q3 GDP advance estimate | Date not found. **Gap** |
| Thu-Fri 29-30 Oct | BoJ; decision about 30 Oct | Secondary only |
| Fri 30 Oct | Russell December reconstitution rank day (last business day of October) | Channelchek / LSEG |
| **Sun 1 Nov** | **OPEC+ (7-country) monthly meeting** | ✔ opec.org |
| **Tue 3 Nov** | **US midterm elections.** Reported end of the US/Israel "no strikes on Iran" pledge. Prediction markets: Democrats about 85% to win the House, Senate a toss-up | GlobalSecurity (pledge, unverified); DeFi Rate / Newsweek |
| Wed 4 Nov | Russell monitor list released | LSEG FAQ |
| **Thu 5 Nov** | **BoE MPC decision and Monetary Policy Report**, 12:00 | ✔ bankofengland.co.uk |
| **Fri 6 Nov** | **US payrolls for October** | Secondary calendar |
| **Tue 10 Nov** | **US CPI for October**, 08:30 ET | Secondary (cites BLS) |
| Fri 13 Nov | Russell indicative review lists | LSEG FAQ |
| About Wed 18 Nov | FOMC minutes for 27-28 Oct (released three weeks after the meeting by convention) | Inferred, not confirmed |
| Mid/late Nov | UK CPI for October (date not confirmed); UK labour data | **Gap** |
| Mid-Nov | MSCI November semi-annual index review; changes usually effective at the end of November | Date not found. **Gap** |
| Thu 26 Nov | US Thanksgiving, NYSE closed; Fri 27 Nov is a half day | Calendar fact |
| Late Nov | US PCE for October; date not found | **Gap** |
| Outside the window | 4 Dec US payrolls; **8-9 Dec FOMC** (with projections); 10 Dec CPI; 11 Dec Russell reconstitution effective; **17 Dec BoE** and ECB | Mixed |

**UK Budget: tax rumours (none confirmed)**
- **CGT:** possible changes are "under consideration" ([HL](https://www.hl.co.uk/news/autumn-budget-2026-key-changes-rumours-and-what-they-mean-for-your-money); [Which?](https://www.which.co.uk/news/article/autumn-budget-2026-when-is-it-and-what-will-it-contain-aQqC47O24jnl)).
- **Dividends:** platforms are lobbying to reverse the dividend-rate rises made in April 2026 under Reeves.
- **ISA:** reform (the earlier Reeves cash-ISA package) is expected to be laid "broadly as drafted", with possible softening; details unverified.
- **Income tax, NI and VAT rates:** the manifesto pledge is reaffirmed, and threshold freezes run to April 2031.
- **Pressure on the Chancellor:** gilt stress means markets want deficit reduction. Tax rises on wealth or investment income are more likely than not, but nothing is official.
- Assets held inside an ISA are sheltered from CGT and dividend tax, so using the ISA allowance is the robust response.

### US earnings in the window (`earnings_calendar.py`, Nasdaq API; times as given)

| Date | Ticker | Timing | EPS est |
|---|---|---|---|
| 20 Oct | ISRG | after close | $2.13 |
| 21 Oct | **META** | after close | $6.39 (**conflict:** the script also lists META on 4 Nov; confirm on IR) |
| 21 Oct | NEE | before open | $1.18 |
| 21 Oct | QS | after close | -$0.18 |
| 21 Oct | *TSLA* (bellwether) | after close | $0.21 |
| 27 Oct | V | after close | $3.43 |
| 27 Oct | SOFI | before open | $0.17 |
| **28 Oct** | **MSFT** | after close | $4.71 |
| **28 Oct** | **GOOGL** | after close | $2.94 |
| 28 Oct | VRT | n/a | $1.83 |
| **29 Oct** | **AMZN** | n/a | $2.02 |
| 29 Oct | COIN | n/a | -$0.20 |
| 29 Oct | INCY | before open | -$3.87 |
| 29 Oct | RIVN | after close | -$0.86 |
| 29 Oct | RIOT | n/a | -$0.33 |
| 29 Oct | PGY | before open | $0.88 |
| 29 Oct | *LLY* | before open | $7.54 |
| 30 Oct | XOM | n/a | $3.93 |
| 30 Oct | *CCJ* | before open | $0.23 |
| 2 Nov | VRTX | after close | $4.28 |
| 2 Nov | *AAPL, PLTR* | after close | $1.99 / $0.34 |
| 3 Nov | TEM | n/a | -$0.30 |
| 3 Nov | MARA | n/a | -$0.04 |
| 3 Nov | *AMD* | after close | $1.66 |
| 4 Nov | IONQ | n/a | -$0.50 |
| 4 Nov | ALB | after close | $2.44 |
| 4 Nov | ACMR | n/a | $0.41 |
| 4 Nov | (META duplicate) | | |
| 5 Nov | MP | after close | -$0.08 |
| 5 Nov | ACHR | n/a | -$0.36 |
| 5 Nov | INOD | n/a | $0.18 |
| 5 Nov | GPCR | n/a | -$0.51 |
| 5 Nov | *IREN* | n/a | -$0.46 |
| 6 Nov | CEG | n/a | $3.99 |
| 6 Nov | WULF | before open | -$0.09 |
| 6 Nov | **BRK.B** | n/a | $5.91 (found under the "BRK.B" symbol) |
| 9 Nov | RKLB | n/a | -$0.05 |
| 9 Nov | CRSP | n/a | -$1.07 |
| 9 Nov | *CRWV* | n/a | -$1.57 |
| 10 Nov | EVLV | after close | -$0.06 |
| 10 Nov | *OKLO* | n/a | -$0.29 |
| **18 Nov** | ***NVDA*** | n/a | $2.47 |
| 23 Nov | SYM | n/a | $0.07 |
| 24 Nov | NIO | n/a | -$0.03 |
| 25 Nov | DE | before open | $4.07 |

*Italic* tickers are bellwethers added for context.

- **Already reported:** JPM on 13 Oct (see 3.5).
- **No date found in the window:** CRDO, KTOS, NNE, PHR, S, TLRY. CRDO, S and PHR usually report early December, and TLRY reported in early October. **KTOS and NNE usually report in early to mid November but were not found; confirm on IR.** This is historical pattern only, not a confirmed date.

---

## 6. What this means for the portfolios

### The key judgement

The September playbook was to own energy, hard assets and AI leaders, hedge with gold and short duration, and watch the $80k BTC level. **Two of its hedges failed this month: gold and precious-metal miners fell 6-15%, and so did hard-asset miners (copper and uranium equities).** Rising real yields beat them. What worked was **quality cash-flow equities, energy, staples and healthcare, and very short duration (0-1y bills and short gilts)**. Long duration of every kind lost: long bonds, small-cap growth and pre-profit tech.

The next six weeks pack the decisive catalysts into a 10-day cluster:
- 28 Oct: FOMC, the UK Budget, and MSFT/GOOGL earnings;
- 29 Oct: ECB, PCE, and AMZN/COIN/RIOT earnings;
- 1 Nov: OPEC+;
- 3 Nov: the midterms (and the end of the reported Iran no-strike pledge);
- 5 Nov: BoE;
- 6 Nov: payrolls;
- 10 Nov: CPI;
- 18 Nov: NVDA.

That argues for **staging new money (part now, part after 28 Oct to 5 Nov)** rather than deploying everything on 15 Oct.

### (a) eToro venture sleeve (about £4.5k: AI infrastructure, semi-cap, biotech, miners and coins, EV and battery, space, quantum, nuclear, defence; plus the AI copy portfolio)

- **Style headwind is regime-level.** This sleeve is the most rate- and financing-sensitive part of the household. Between 18 Sep and 14 Oct its archetypes fell:
  - miners -32% to -38%;
  - quantum (IONQ) -20%;
  - eVTOL (ACHR) and solid-state batteries (QS) about -22%;
  - small nuclear (NNE) -17%;
  - defence (KTOS) -17%;
  - space (RKLB) -8%;
  - semi-cap (ACMR) -11%;
  - AI infrastructure (VRT) -11%.
- **Tilts within the policy bands:**
  - **Hold new venture money as cash** (or the top of the cash band) until at least the hyperscaler capex prints on 28-29 Oct and the FOMC. Deploy in two or three tranches.
  - **Prefer quality within venture:** names with revenue, positive EPS estimates and catalysts (e.g. VRT, INOD and ACMR have positive EPS estimates), over pre-revenue story stocks (QS, ACHR, NNE, quantum).
  - **Bitcoin miners carry double beta,** to BTC (sitting on $80k) and to AI-financing credit. Do not average down before the RIOT/MARA/WULF prints (29 Oct, 3 Nov, 6 Nov) and the BTC $80k test.
  - **For crypto exposure,** BTC itself has held up far better than miners, SOL or ETH. If any crypto exposure is added, the coin beats the miners in this regime.
  - **Biotech** (INCY, CRSP, TEM, GPCR) is idiosyncratic. GPCR -37% needs a thesis check (not researched here).
  - **AI copy portfolio:** check its exposure to the neocloud and memory layer. That layer is where the cracks are.
- **Asymmetry.** Many venture names are now 15-35% cheaper than at the last run, which improves forward asymmetry *if* the regime stabilises. The catalysts, though, are binary and clustered: capex guidance, the Fed, CPI, NVDA. Keep position sizing small and stagger entries.

### (b) ISA (about £4.6k: mega-caps, thematic ETFs, core trackers, small defensive positions)

**Lean defensive and quality, and keep short-duration ballast at the upper end of its band.**
- **Overweight within bands:**
  - quality mega-caps and World Quality;
  - US staples and healthcare;
  - cybersecurity (+3.9%, software-like cash flows);
  - energy (as an inflation and Hormuz hedge, hold rather than add aggressively given the pre-midterm de-escalation tail);
  - short-dated gilts (0-5y).
- **Why short gilts:** 2y and 5y yields are high, the BoE is closer to hiking than cutting, and a 0-5y fund has limited duration loss if it hikes on 5 Nov. Gilts held in an ISA are tax-free on income too. **Avoid long gilts and long Treasuries.** The 30y gilt is above 6%, but fiscal risk around the 28 Oct Budget is high.
- **Neutral or underweight within bands:**
  - semis and AI thematic ETFs: keep core exposure, but don't add before 28-29 Oct capex and NVDA on 18 Nov;
  - robotics; world small cap (Russell -4.6%; small caps are hurt most by 5%+ yields);
  - financials (JPM miss, XLF -2.4%);
  - India (record foreign outflows, oil importer, rupee at a record low);
  - EM IMI (Korea memory risk; Brazil already rallied).
- **Gold and copper miners:** these failed as hedges this month. They are cheaper now, but the real-yield headwind persists while the Fed is hiking. Hold, no add. They become attractive if the growth scare deepens and the Fed pivots, so watch the 6 Nov payrolls.
- **Defence ETF:** de-rated with growth. Hold.
- **UK Budget (28 Oct):** consider making any planned ISA subscriptions before or around the Budget. Possible CGT or dividend-tax changes make the ISA wrapper relatively more valuable; ISA rules themselves are not expected to change materially, but this is unconfirmed. Avoid crystallising taxable gains outside the ISA before the Budget is clear.
- **FX:** GBP/USD is 1.32-1.33. Unhedged USD assets have flattered GBP returns. A reassuring Budget or a BoE hike could lift sterling and trim GBP returns on US holdings. That is not a reason to hedge at this size, just a source of noise.

### Net tilt recommendation

Moderately more defensive than September:
- higher cash and short-duration ballast (top of band);
- quality over beta in both portfolios;
- add growth in stages after the 28 Oct to 6 Nov catalyst cluster, not before;
- keep energy as a hedge but don't chase it;
- don't treat gold or miners as a reliable hedge while real yields rise.

**Signals that would reverse this tilt (towards more growth):**
- the 10y falls back below about 5%;
- the FOMC holds on 28 Oct with dovish guidance;
- hyperscaler capex is reaffirmed or raised;
- BTC holds $80k;
- a Hormuz or Houthi de-escalation before 3 Nov.

**Signals that would deepen it:**
- the 10y above 5.35%, or the 30y gilt pushing above about 6%;
- a hike plus hawkish guidance;
- capex cuts or AI credit stress (more IPOs pulled, wider spreads);
- BTC below $80k;
- an attack on Aramco or a broader Gulf escalation.

---

## 7. Evidence gaps and caveats

- **Market pricing not found:** BoE (SONIA/OIS) and ECB pricing for the 29 Oct and 5 Nov meetings. The current ECB deposit rate is in conflict (2.00% vs 2.50%).
- **Data not found:**
  - September PPI; October US diesel and gasoline (EIA);
  - October lithium carbonate price; October LME copper settlement;
  - October 2026 spot-BTC ETF flows;
  - a specific cause for the defence-stock selloff;
  - Japan and BoJ news for October 2026;
  - the outcome of the RBI meeting on 7 Oct.
- **Dates not confirmed:** US Q3 GDP advance; October PCE; UK CPI for October; MSCI November review; FOMC minutes (~18 Nov, inferred). September PCE: 29 Oct per BEA via secondary, one source says 4 Nov.
- **Earnings dates:**
  - META is listed twice (21 Oct and 4 Nov).
  - KTOS, NNE, CRDO, S and PHR were not found in the window.
  - Nasdaq API dates are often estimates; confirm on company IR pages.
- **To verify:**
  - Core CPI y/y of 2.6% looks inconsistent with a 3.7% headline; check bls.gov.
  - The 8 Oct "no strikes before 3 Nov" pledge comes from one secondary dashboard (GlobalSecurity).
  - The BlackRock tech downgrade is sourced only via Semafor; no primary source was found.
- **Access limits:** bls.gov, bea.gov and most news sites could not be fetched directly in this environment. Many figures come from search-result summaries of the cited URLs rather than full-page reads.
- **Price timing:** Yahoo prices for 15 Oct (crypto, futures, LSE) are intraday snapshots. US prices are 14 Oct closes.
