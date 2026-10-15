# Venture sleeve: micro/small-cap candidates, 2026-10-15

Goal: 2 new venture picks (£100 each), bought in a Revolut Stocks & Shares ISA (NYSE/Nasdaq/LSE/AIM only).
Bar (raised after the scorecard lesson): real revenue with strong growth and gross margin; profitable or 6+ quarters of runway; share count growth under 15% a year; no going-concern language; market cap $50M-$3B; ADV over $1M; price over $2. Avoid crowded themes (crypto, EV/battery, quantum, nuclear, space, defence) and pure AI.

Data date: prices and multiples are from Finviz and stockanalysis.com as of the 2026-10-14 close (fetched 2026-10-15) unless stated. Quarterly figures come from company releases and 8-Ks via stockanalysis.com and SEC EDGAR.

**Process limits (evidence gaps):**
- The web-search budget ran out partway through. Later checks used SEC EDGAR, stockanalysis.com, Finviz and ClinicalTrials.gov only.
- UK/AIM names were not screened, because Finviz covers US listings only and the search budget was gone.
- Short-report searches for the finalists were not possible.
- Underwriter overlap was checked from the IPO prospectuses (424B4) on EDGAR.

---

## 1. Idea generation

| Source | Filter / query | Matches | Notes |
|---|---|---|---|
| Preset `microcap-quality-growth` | cap<$2B, US, ADV>200K, price>$2, sales q/q>20%, GM>35%, current ratio>1.5, D/E<0.5 | 50 | Mostly biotech, crypto-treasury names and royalty companies |
| Preset `microcap-insider-buying` | cap<$2B, ADV>200K, price>$2, latest insider buys | 1,394 (top 60 by cap shown) | Too broad; used the custom insider screen below |
| Preset `biotech-cash-runway` | cap<$2B biotech, current ratio>5, D/E<0.1 | 138 | Pre-revenue; excluded by the raised bar |
| Custom 1 | cap<$2B, sales 5y>20%, sales q/q>25%, GM>50%, positive op margin, D/E<0.5 | 12 | |
| Custom 2 | cap<$2B, sales q/q>20%, EPS q/q>20%, GM>40%, ROE>15%, above SMA200 | 10 | |
| Custom 3 (insider) | cap<$2B, insider transactions >+10% (6m), sales q/q>15%, GM>30% | 6 | ALKT, PAR, RCEL, TNXP, TGS, HRZN |
| Custom 4 | cap<$2B, sales q/q>25%, sales 5y>15%, GM>40%, current ratio>1.5, net margin>0 | 26 | |
| Custom 5 | $300M-$2B, sales q/q>30%, GM>45%, D/E<0.5, current ratio>1.5 | 31 | |
| Custom 6 | $300M-$2B, sales q/q>20%, sales 5y>15%, GM>40%, op margin>0, D/E<0.5 | 13 | |
| Custom 7 | $2-10B (ascending), sales q/q>20%, GM>40%, D/E<0.5 | 70 (lowest 30 reviewed) | For the $2-3B band |
| Custom 8 | cap<$2B and $2-10B, sales q/q>20%, GM>50%, fwd P/E<20 | 24 + 51 | Cheap high-margin growers |
| WebSearch | Insider cluster buys Oct 2026; small-cap estimate revisions; 2026 spin-offs and uplistings | n/a | Nothing usable for October 2026 (results were older or large-cap) |

Names carried into the gates (about 60, from the screens above): RDVT, PAYS, CXDO, DSP, MNTN, EVER, OPRA, ATEX, CSTL, CBLL, BBNX, KMTS, OMDA, STAA, MASS, DCTH, ZVRA, CRMD, ETON, ANIP, BWAY, HAPN, AIP, AMBQ, MRAM, INTT, ALKT, PAR, RCEL, LMAT, AXGN, VCEL, CALX, FLYW, TLS, PRE, HSAI, FEIM, KOPN, QTRX, OABI, EVTC, PRCH, ASTH, MQ, AMPL, URGN, ARDX, PHAT, TREE, GRND, EZPW, BCRX, HRMY, UPWK, LQDA, PGEN, COUR, STUB, plus the pre-revenue biotech, crypto-treasury and royalty names from the presets.

---

## 2. Hard gates: rejected names

Source for the figures: Finviz quote snapshots, 2026-10-14. Share-count changes are from stockanalysis.com quarterly balance sheets. Where "Shares Change YoY" on the statistics page was inflated by IPO weighting, I used period-end counts.

| Ticker | Gate failed | Evidence (2026-10-14) |
|---|---|---|
| AGIO, VIR, SEPN, FDMT, ARVN, ASMB, ABEO, XFOR, TNXP, ADRX, TRVI, STOK etc. | Pre-revenue or early biotech (raised bar) | Biotech preset; no meaningful product revenue |
| SBET, HSDT (Solana Co), TONX | Crowded theme (crypto treasuries) | |
| ELE, VOXR, MTA, ASM, GROY, TRX | Thesis depends on gold and silver prices, not business quality; poor 10x fit | Royalty and miner names |
| HAPN (Happen, formerly LendingClub) | Overlaps with held fintech lenders (SOFI, PGY); a 10x path for a bank is implausible | Renamed June 2026 ([stockanalysis](https://stockanalysis.com/stocks/hapn/)) |
| ATEX | Not real revenue at scale | Sales $7.0M, EV/S 215 |
| KMTS | Heavy losses | Op margin -134% |
| CBLL | Pre-profit | Op loss about $20M/qtr (Q2-26); cash about $129M; consensus 2026 EPS -1.96 |
| BBNX | Pre-profit | Op margin -70% |
| QTRX | Pre-profit, broken trend | Op margin -64%; -48% over 1Y |
| OABI | Pre-profit, AI drug discovery | Op margin -126% |
| AMBQ, AIP | AI semis/IP (AI fully allocated) and losses | Op margins -43% and -44% |
| PRE | Losses; bitcoin-treasury exposure | Op margin -35% |
| HSAI | Crowded theme (EV/auto lidar); China ADR | |
| HAWK, FEIM, KOPN, TLS, AIRO, POWW | Crowded theme (defence/space). Also: KOPN revenue -7% TTM, FEIM growth 6% TTM, TLS GM 37% with losses | |
| CSTL, MASS, INTT, RCEL, LMAT, EVTC, UPWK, STUB | Growth under 20% TTM | 3%, 0.7%, 5%, 1%, 12%, 12%, 2%, 8% TTM |
| ALKT | Growth slowing (Q2-26 +16% YoY); GAAP losses; Sell downgrade ($24 to $14) on 2026-09-24 | Insider buying noted, but the quality gate fails |
| PAR | Growth 19%; GAAP losses; -57% over 1Y | |
| ASTH, MQ | Gross margin too low | 8.8% and 16.4% |
| AMPL | GAAP losses (op margin -27%); current ratio 0.95 | |
| URGN | Runway | TTM FCF -$159M vs cash $108M and debt $196M; Altman Z -3.2. Zusduri ramp is strong (Q2 rev $72.5M vs $24.2M) but the balance sheet fails the gate |
| CRMD | Dilution and declining revenue | Shares +40% YoY (Melinta deal); revenue $127.4M (Q1-26) then $101.9M (Q2-26); Q3 EPS estimate -$0.05; short float 21.6% |
| ETON, PAYS | Timing rule (no buying after a 50%+ run) | ETON +182% 1Y with EV/S 14. PAYS +74% in 3 months and +170% 1Y. Fundamentals are strong (sales +47%, GM 52%, P/FCF 12.6), so keep on the watchlist for a pullback |
| ANIP, ARDX, TREE, PGEN, BCRX | Leverage | D/E 1.02, 1.72, 1.36 and 2.26; BCRX profit margin -41%. TREE is also -58% 1Y with revenue down QoQ |
| PHAT | Losses plus debt; -41% 1Y | |
| LQDA | Above the $3B cap | $3.04B |
| GRND | 10x implausible at $2.62B; net debt $383M; 74% insider-controlled | |
| EZPW, HRMY | 10x implausible: pawn lender, and single-drug pharma facing a patent cliff | |
| COUR | Growth is merger-driven; GAAP losses; -53% 1Y | |
| STAA | Growth is a rebound in China distributor orders, not steady growth; consensus Hold-leaning (Recom 2.6) | Revenue $57.8M (Q4-25), $93.5M (Q1-26), $93.5M (Q2-26) |
| PRCH | Growth 16%; short float 18% | |
| TGS, HRZN, CTRI etc. | Not venture-type (Argentine gas utility, BDC, utility contractor) | |

---

## 3. Scoring the survivors (micro-cap rubric, 100 points)

Columns: A = asymmetry/10x path (20), Q = quality/traction (20), F = financial strength/dilution (15), M = management (10), V = valuation vs growth (15), R = revisions/trend (10), C = catalyst (10).

| Rank | Ticker | A | Q | F | M | V | R | C | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | MNTN | 15 | 16 | 14 | 4 | 14 | 3 | 6 | **72** |
| 2 | OMDA | 13 | 17 | 13 | 4 | 14 | 5 | 5 | **71** |
| 3 | DCTH | 14 | 14 | 13 | 7 | 10 | 7 | 5 | **70** |
| 4 | ZVRA | 11 | 15 | 14 | 4 | 13 | 4 | 7 | **68** |
| 5 | BWAY | 10 | 17 | 13 | 5 | 8 | 6 | 5 | **64** |
| 6 | RDVT | 8 | 16 | 15 | 6 | 5 | 8 | 5 | **63** |
| 7 | CALX | 6 | 15 | 15 | 6 | 12 | 4 | 5 | 63 |
| 8 | EVER | 8 | 13 | 15 | 4 | 14 | 3 | 5 | 62 |
| 9 | DSP | 10 | 11 | 13 | 6 | 11 | 6 | 5 | 62 |
| 10 | OPRA | 7 | 14 | 14 | 3 | 13 | 5 | 5 | 61 |
| 11 | AXGN | 9 | 14 | 12 | 5 | 7 | 7 | 6 | 60 |
| 12 | CXDO | 10 | 12 | 11 | 5 | 12 | 2 | 5 | 57 |
| 13 | VCEL | 8 | 13 | 14 | 5 | 6 | 5 | 5 | 56 |

Why the survivors ranked 7-13 stopped:
- **CALX:** $2.27B cap makes 10x implausible; -39% over 1Y.
- **EVER:** growth slowing (2027 consensus +10%); short float 26.5%; revenue flat QoQ.
- **DSP:** GAAP operating losses in H1-26; GM 44%; founder-controlled; overlaps MNTN.
- **OPRA:** controlled by Kunlun; low float; 10x implausible.
- **AXGN:** +121% over 1Y; GAAP losses; fwd P/E 51.
- **CXDO:** organic growth unclear (acquisition); CTO sold 25K shares on 2026-09-01; -51% from its 52-week high.
- **VCEL:** fwd P/E 46 for 23% growth.

---

## 4. Deep dives (top 6)

### 4.1 MNTN, Inc. (NYSE: MNTN): performance CTV advertising platform for SMB and mid-market brands

- **Price and cap (2026-10-14):** $9.40; market cap $703M; EV $466M; 74.8M shares.
- **ADV:** 935K shares (about $8.8M).
- **1Y:** -40.8% (from $15.88). 52-week range $7.67-$18.60. SMA50 -18.6%, SMA200 -7.1%.
- **Last quarters, revenue (all quarters below from stockanalysis.com quarterly data / 8-K):**

| Quarter | Revenue | YoY | Gross margin | Op income |
|---|---|---|---|---|
| Q2-25 | $68.5M | | 77% | $3.7M |
| Q3-25 | $70.0M | | 79% | $7.5M |
| Q4-25 | $87.1M | | 82% | $20.5M |
| Q1-26 | $73.7M | +25% adjusted / +14% GAAP | 81% | $9.6M |
| Q2-26 | $82.5M | +21% | 81% | $8.6M |

  Q2-26 net income was $6.7M, against a $26.2M loss in Q2-25 ([8-K](https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm)).
- **Guidance:**
  - Q3-26 revenue $86-89M (about +25% at the midpoint); adj. EBITDA $22-25M.
  - FY26 revenue $347-357M reiterated (over +24% excluding the Maximum Effort divestiture); adj. EBITDA $96-101M ([BusinessWire](https://www.businesswire.com/news/home/20260804192898/en/)).
  - Consensus revenue: 2026 $352M (+21%), 2027 $417M (+18%) ([stockanalysis](https://stockanalysis.com/stocks/mntn/forecast/)).
- **Traction:** active Performance TV customers 4,225 (+40% YoY); expansion rate "well north of 115%" (call summaries via [Quartr](https://quartr.com/events/mntn-inc-mntn-q2-2026_F6njEL7H)).
- **Cash, dilution and buyback:**
  - Cash $237.3M, no borrowings (30 Jun 2026). TTM FCF $72.9M.
  - SBC $12.6M in H1-26, against $21.7M in H1-25 (8-K cash-flow statement).
  - Shares 72.6M (Q2-25) to 74.8M (Q2-26), +3.0%.
  - $100M buyback authorised through 2027-08-05, about 14% of market cap.
- **Insiders:**
  - No open-market buying.
  - Baroda Ventures (VC holder) sold about 336K shares at $12.53-12.75 on 2026-08-17/20.
  - Director Hadi Partovi sold about 447K shares at $13.39-13.46 on 2025-12-03.
  - Remaining Form 4s are director stock awards. Source: [EDGAR Form 4s](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=1891027&type=4).
- **Governance:** dual-class. Class B carries 10 votes and held about 86.4% of voting power at IPO; founder-CEO Mark Douglas held about 16.7% ([424B4](https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm)). Insider ownership 12% (stockanalysis); Finviz shows 50.9% (class definitions differ).
- **Short interest:** 10.8% of float, 4.3 days to cover (Finviz); 9.96% (stockanalysis).
- **Analysts:**
  - 10 analysts, consensus Buy, average target $18.10 (range $13-$22).
  - Targets were cut after Q2: $26→$22, $17→$16 and $18→$16 (Hold) on 2026-08-10/13.
  - IPO bookrunners Morgan Stanley, Citigroup and Evercore ISI (plus Citizens, Needham, Raymond James, Susquehanna, Loop and Tigress) are underwriter-conflicted, so discount the Buy consensus.
- **Valuation vs peers (Finviz, 2026-10-14):**

| Company | EV/sales | Sales growth TTM |
|---|---|---|
| MNTN | 1.49 | +21% |
| TTD | 1.57 | +12% |
| DSP | 2.25 | +22% |
| PUBM | 2.44 | -1% |
| MGNI | 4.73 | +8% |

  MNTN's EV/FCF is about 6.4 (15.6% FCF yield) and its forward P/E is about 9.6.
- **10x path:**
  - 2026 revenue of about $352M compounding at 20% for 8 years gives about $1.5B.
  - A 25% FCF margin then gives about $375M FCF; at 20x that is about $7.5B plus cash, roughly 10-11x today's $703M.
  - Base case: 15% CAGR and a 22% margin at 15x is about $3.6B, roughly 5x.
  - Downside cushion: net cash is 34% of market cap and the business is FCF-positive.
- **Next catalyst:** Q3-26 results on 2026-11-03 (earnings calendar). The guide implies about +25% YoY; buyback execution is also observable.
- **Entry tag: Undervalued.** It trades at EV/S 1.5 and EV/FCF 6.4 with 20%+ growth and 80% GM. The price is 49% below its 52-week high, and the drawdown came from a guidance miss (May 2026: -22.5% on a soft Q2 guide, [Tickeron](https://tickeron.com/blogs/mntn-inc-mntn-shares-drop-22-after-earnings-miss-and-soft-q2-guidance-13218/)), not from a broken thesis.
- **Bear case:**
  - The whole adtech group has de-rated: TTD now has a $5.8B cap at EV/S 1.6, which suggests a structural concern (Amazon DSP fee pressure, walled-garden CTV, AI-driven buying).
  - SMB ad budgets are cyclical, and an oil shock plus rate hikes hit SMB spend first.
  - Dual-class control.
  - VC holders are still selling.
  - Growth slowed from 36% (Q4-25) to 21% (Q2-26).
- **Pre-mortem (down 60% in 2 years):**
  1. Amazon, Roku or Google self-serve CTV tools commoditise performance CTV and growth falls under 10%.
  2. A recession cuts SMB ad spend and customer churn spikes.
  3. Management spends the cash on a large dilutive acquisition.
- **Kill criteria:**
  - Two consecutive quarters of YoY revenue growth under 12%.
  - Active customers fall YoY.
  - Expansion rate disclosed under 100%.
  - TTM FCF turns negative.
  - Net cash falls below $150M without a stated value-creating use.
  - Any equity raise.

### 4.2 Omada Health (Nasdaq: OMDA): virtual chronic-care (diabetes, hypertension, GLP-1 support, MSK) sold to employers and health plans

- **Price and cap (2026-10-14):** $18.22; market cap $1.12B; EV $894M; 61.2M shares.
- **ADV:** 1.39M shares (about $25M).
- **1Y:** -25.7%. 52-week range $10.28-$26.92. Quarter -23%. SMA200 +4.1%.
- **Last quarters:**

| Quarter | Revenue | YoY | Gross margin | Op income |
|---|---|---|---|---|
| Q2-25 | $61.4M | | 66% | -$4.3M |
| Q3-25 | $68.0M | | 66% | -$2.5M |
| Q4-25 | $75.9M | | 71% | +$3.3M |
| Q1-26 | $78.1M | | 62% | -$4.8M |
| Q2-26 | $87.8M | +43% | 73% | +$3.6M |

  Q2-26 net income was $5.3M ([8-K](https://www.sec.gov/Archives/edgar/data/0001611115/000162828026054266/q2fy26pressrelease.htm)).
- **Traction and guidance:**
  - Members about 1.1M (+45%).
  - FY26 revenue guidance raised to $334-340M (+28-31%); adj. EBITDA $21-27M.
  - Consensus revenue: 2026 $339M (+30%), 2027 $408M (+20%).
- **Cash, dilution and leadership:**
  - Net cash $221.7M, no debt. TTM FCF $22.7M.
  - Shares 57.6M (Q2-25) to 61.2M (Q2-26), +6.3%.
  - CEO transition: President Wei-Li Shao becomes CEO on 2027-01-01; co-founder Sean Duffy becomes Executive Chair.
- **Insiders:** steady 10b5-1 sales by the CEO, CFO and President (Sept-Oct 2026, about $20.6-22.6); no buying.
- **Short interest:** 15.0% of float (Finviz), 5.4 days to cover.
- **Analysts:**
  - 12 analysts, consensus Buy, average target $28.42 (range $22-$35).
  - Latest: Hold $22 (2026-10-14), Buy $30 (2026-10-13).
  - Coverage is dominated by IPO underwriters (Morgan Stanley, Goldman Sachs, J.P. Morgan, Barclays, Evercore ISI, Canaccord, Needham; [424B4](https://www.sec.gov/Archives/edgar/data/1611115/000119312525137394/d785770d424b4.htm)), so discount it.
- **Valuation vs peers (Finviz):**

| Company | EV/sales | Growth | Note |
|---|---|---|---|
| OMDA | 2.9 TTM / about 2.6 on 2026 guidance | +48% TTM | |
| HNGE (Hinge Health), closest peer | 11.2 | +50% | |
| TDOC | 0.5 | -2% | |
| LFST | 3.2 | +20% | GM 30% |

- **10x path:**
  - Revenue compounding at 25% for 8 years gives about $2.0B.
  - At a 15% EBIT margin and 25x EBIT that is about $7.5B, roughly 7x.
  - Getting to 10x needs either a Hinge-like 5x sales multiple on $2B, or GLP-1 programmes taking growth above 30%.
  - Downside: net cash is 20% of market cap, GAAP profitable in Q2, and the members are real.
- **Next catalyst:** Q3-26 results on 2026-11-05 after hours; then 2027 employer selling-season wins and the CEO handover on 2027-01-01.
- **Entry tag: Undervalued** relative to its closest peer at a similar growth rate.
- **Bear case:**
  - GLP-1 refresh cycle may not be durable, and pricing per member may fall as competition grows ([Public.com analyst summary](https://public.com/stocks/omda/forecast-price-target)).
  - Employer and health-plan budgets are under pressure.
  - Q1-26 gross margin dipped to 62%.
  - CEO transition.
  - Constant insider selling and short interest of 15%.
- **Pre-mortem:**
  1. Payers bundle GLP-1 support themselves, or drug makers offer free coaching, and growth collapses to single digits.
  2. A large channel partner (PBM or health plan) drops Omada.
  3. The new CEO resets guidance lower.
- **Kill criteria:**
  - Revenue growth under 15% YoY for two quarters.
  - Member growth under 15%.
  - Loss of a top channel partner.
  - Return to GAAP operating losses for two consecutive quarters with net cash under $150M.
  - Any equity raise.

### 4.3 Delcath Systems (Nasdaq: DCTH): HEPZATO KIT (liver-directed melphalan perfusion) for uveal melanoma liver metastases; Phase 2 trials in colorectal and breast liver metastases

- **Price and cap (2026-10-14):** $14.72; market cap $511M; EV $417M; 34.7M shares.
- **ADV:** 472K shares (about $6.9M).
- **1Y:** +29.5%. 52-week range $8.12-$17.42. SMA200 +21.8%; SMA50 -8.5%.
- **Last quarters:**

| Quarter | Revenue | Gross margin | Op income |
|---|---|---|---|
| Q2-25 | $24.2M | | $2.6M |
| Q3-25 | $20.6M | | -$0.4M |
| Q4-25 | $20.7M | | -$2.2M |
| Q1-26 | $25.0M | | -$1.6M |
| Q2-26 | $29.1M (+21% YoY; HEPZATO $27.1M, CHEMOSAT $2.0M) | 90% | $2.4M |

  Revenue stalled through H2-25 and re-accelerated in H1-26. Source: [8-K](https://www.sec.gov/Archives/edgar/data/0000872912/000162828026053902/dcth-q22026erex991.htm).
- **Guidance and footprint:**
  - FY26 revenue raised to $104-108M, assuming HEPZATO volume up at least 28%; GM 86-89%; positive adj. EBITDA.
  - 31 active centers, with 37 targeted by year-end.
  - Consensus revenue: 2026 $106M (+25%), 2027 $132M (+24%).
- **Cash and dilution:**
  - Cash and investments $95.9M, debt $2.5M. TTM FCF $17.5M.
  - Period-end shares 35.0M (Q2-25) to 34.7M (Q2-26), roughly flat. Over 2 years 28.0M to 34.7M, about +11% a year. The 3-year rate was higher because of the 2023 warrant financing.
  - An S-8 for an equity-plan increase was filed 2026-08-14.
- **Insiders:** open-market purchases by the CEO (Gerard Michel, 11,200 shares at $8.96 on 2026-03-03) and the CFO (Sandra Pennell, 5,533 shares at $9.04 on 2026-03-06). The amounts are small, but they are real buys at about 60% of today's price.
- **Short interest:** 6.1% of float.
- **Analysts:** 5 analysts, Strong Buy, average target $24 (range $21-$32); one raise from $18 to $24 on 2026-08-07.
- **Pipeline (ClinicalTrials.gov):**
  - mCRC Phase 2 ([NCT06607458](https://clinicaltrials.gov/study/NCT06607458)): 90 patients; primary completion estimated 2026-12.
  - Breast Phase 2 ([NCT06875128](https://clinicaltrials.gov/study/NCT06875128)): primary completion 2029-05.
  - HEPZATO + Opdualag Phase 1/2: starts 2026-10.
- **Valuation:** EV/S 4.4 TTM (about 3.9 on 2026 guidance) for 25% growth and 90% GM.
- **10x path:**
  - Uveal melanoma alone is a niche, so 10x needs a colorectal liver-metastasis label.
  - With one, revenue of $600M-$1B by the mid-2030s at a 30% op margin and 20x EBIT gives $3.6-6B, roughly 7-12x.
  - This depends on the trial and probably needs a Phase 3.
- **Next catalyst:** Q3-26 results on 2026-11-03; mCRC Phase 2 primary completion (estimated Dec 2026), so data likely in 2027.
- **Entry tag: Fair.**
- **Bear case:**
  - Single product in a niche indication.
  - Systemic therapies such as IDEAYA's darovasertib+crizotinib (background knowledge, not verified this run) could shrink the uveal melanoma liver-metastasis market.
  - The procedure is complex and capacity-limited per center.
  - Revenue stalled for two quarters in 2025.
  - Melphalan toxicity and REMS.
- **Pre-mortem:**
  1. mCRC Phase 2 data are unconvincing and the platform story dies.
  2. A systemic drug approval erodes HEPZATO volumes.
  3. Center growth stalls and revenue plateaus around $100M.
- **Kill criteria:**
  - HEPZATO revenue down YoY for two quarters.
  - mCRC trial reported negative or deprioritised.
  - Cash under $50M or any equity raise.
  - FDA safety action.

### 4.4 Zevra Therapeutics (Nasdaq: ZVRA): rare disease; MIPLYFFA (arimoclomol) for Niemann-Pick type C

- **Price and cap (2026-10-14):** $10.23; market cap $608M; EV $387M.
- **ADV:** 1.08M shares (about $11M).
- **1Y:** -2.5%. 52-week range $8.01-$15.03. Quarter -19.8%.
- **Last quarters:**

| Quarter | Revenue | Op income |
|---|---|---|
| Q2-25 | $25.9M | -$12.3M |
| Q3-25 | $26.1M | $4.1M |
| Q4-25 | $34.1M | $9.3M |
| Q1-26 | $36.2M | $8.8M |
| Q2-26 | $39.7M (+53% YoY; MIPLYFFA US $30.2M, +40% YoY) | $16.8M |

  GM is about 96%. Source: [8-K](https://www.sec.gov/Archives/edgar/data/0001434647/000143464726000067/zvra-20260805xex991earnings.htm).
- **Patients:** 14 new enrollment forms in Q2 (184 since launch); payer access covers 69% of lives.
- **Cash and dilution:** cash and investments $260.2M; debt $1.5M; TTM FCF $32.6M. Shares 56.1M to 59.4M, +5.8% YoY.
- **Insiders and short interest:** only 10b5-1 sales (CEO sold 20K at $11.25 on 2026-10-13; CLO sold); insiders own 1.2%. Short float 12.2%.
- **Analysts:** 9 analysts, Strong Buy, average target $25 (range $20-$35). Guggenheim cut from $24 to $23 on 2026-08-07. 2026 EPS consensus $1.17 (-13.6%).
- **Valuation:** EV/TTM op income about 10x; fwd P/E about 11-12.
- **Revenue outlook:** consensus 2026 $153M (+44%), 2027 $178M (+16%), so growth decelerates sharply.
- **10x path:** weak. NPC is a small market; the EU CHMP opinion was negative on 2026-07-24 and is under re-examination; the celiprolol (vEDS) Phase 3 primary completion is 2029-03 ([NCT05432466](https://clinicaltrials.gov/study/NCT05432466)). The realistic bull case is about 3x. Downside is well cushioned: net cash is 36% of market cap and the business is profitable.
- **Catalysts:** Q3 results on 2026-11-04; CHMP re-examination outcome in Q4-26 (binary EU upside).
- **Entry tag: Undervalued.**
- **Bear case:** competitor AQNEURSA in NPC; OLPRUVA scaled back; growth decelerating; CFO transition.
- **Kill criteria:** MIPLYFFA revenue down QoQ two quarters in a row; enrollments under 5 per quarter; value-destroying M&A.

### 4.5 BrainsWay (Nasdaq ADR: BWAY): Deep TMS systems for depression and OCD

- **Price and cap (2026-10-14):** $11.51; market cap $469M; EV $416M.
- **ADV:** about 122K ADS (about $1.4M, so it passes, just).
- **1Y:** +52%, but -22% over the quarter and 17% below SMA200.
- **Q2-26:**
  - Revenue $17.1M (+35%); 125 systems shipped (+42%); installed base about 1,950; RPO $80.4M (+30%).
  - Op income $2.4M; 12th straight profitable quarter.
  - FY26 guidance raised to $68-70M revenue and $13-14M adj. EBITDA.
  - Debt-free, cash $62.4M. Source: [6-K](https://www.sec.gov/Archives/edgar/data/0001505065/000117184326005440/exh_991.htm).
- **Shares:** +6.2% YoY.
- **Analysts:** 3, average target $19.27.
- **Valuation:** EV/S 6.9 and fwd P/E about 32, so a full price.
- **10x path:** limited by the size of the TMS market. **Entry tag: Fair.**
- **Kill criteria:** growth under 15%; return to losses.

### 4.6 Red Violet (Nasdaq: RDVT): identity and data-fusion analytics (idiCORE, FOREWARN)

- **Price and cap (2026-10-14):** $75.96; market cap $1.22B; EV $1.17B.
- **1Y:** +43.9%; half-year +95%.
- **Q2-26:** revenue $26.7M (+23% YoY); op income $6.1M.
- **Gross margin:** the two sources disagree, 73.5% (Finviz) vs about 86% (stockanalysis GP line), because of how cost of revenue is classified.
- **Balance sheet and shares:** net cash, D/E 0.02; shares flat (+0.2%).
- **Valuation:** EV/S 11.8; fwd P/E 46. **Entry tag: Premium.** It is near its 52-week high of $81.79.
- **Next catalyst:** Q3 results on 2026-11-04.
- **Why it ranks low:** valuation leaves little room for a 10x from $1.2B.

---

## 5. Recommendation

**Picks (rubric 70+, no unresolved red flag):**

1. **MNTN (72), Undervalued.**
   - Cheapest quality growth in the funnel: EV/FCF 6.4, net cash 34% of market cap, GAAP profitable, 80% GM, 20%+ growth, and a buyback worth 14% of the market cap.
   - Adds a new, diversifying theme (CTV advertising); there is no adtech in the book.
   - Least exposed to the rate and duration selloff because the cash flow is current.
   - Accepted risks: dual-class control and VC selling are governance negatives; the adtech de-rating is a real, partly answered bear case.
2. **OMDA (71), Undervalued vs peer.**
   - 43% growth, GAAP profitable in Q2, net cash 20% of market cap.
   - Trades at about a quarter of Hinge Health's EV/sales at similar growth.
   - Adds chronic-care and GLP-1 services exposure that is not AI and not biotech binary.
   - Risks to watch: CEO transition, insider 10b5-1 selling, 15% short interest.

**Alternates:**
- **DCTH (70).** Fair price; profitable single-product oncology device; insider buys; mCRC data likely in 2027. It is the 3rd choice because of single-product risk and the 2025 revenue stall.
- **ZVRA (68).** Below the 70 bar, so only if a pick is unavailable or after a positive CHMP re-examination. It has the strongest downside protection in the funnel but a weak 10x path.

**Timing note:** both picks report within about 3 weeks (MNTN 2026-11-03, OMDA 2026-11-05). Use limit orders. If you buy before earnings, accept the gap risk, or split the purchase around the print.

**Watchlist:**
- PAYS: re-check after its run cools (it failed only the 50%-in-3-months rule).
- URGN: re-check if Zusduri cash flow turns FCF-positive.
- ALKT: re-check if growth stays above 15% and the insider buying continues.

---

## 6. Sources

- Finviz screens and quote snapshots via `finviz.py` (2026-10-14 close)
- stockanalysis.com statistics, quarterly financials and forecast pages for each ticker, e.g. [MNTN forecast](https://stockanalysis.com/stocks/mntn/forecast/), [OMDA forecast](https://stockanalysis.com/stocks/omda/forecast/), [DCTH balance sheet](https://stockanalysis.com/stocks/dcth/financials/balance-sheet/?p=quarterly)
- MNTN Q2-26 8-K: https://www.sec.gov/Archives/edgar/data/0001891027/000189102726000070/mntnearningsrelease2026-q2.htm ; IPO 424B4: https://www.sec.gov/Archives/edgar/data/1891027/000110465925052048/tm2413466-25_424b4.htm ; BusinessWire: https://www.businesswire.com/news/home/20260804192898/en/ ; May-26 drop: https://tickeron.com/blogs/mntn-inc-mntn-shares-drop-22-after-earnings-miss-and-soft-q2-guidance-13218/ ; Quartr summary: https://quartr.com/events/mntn-inc-mntn-q2-2026_F6njEL7H
- OMDA Q2-26 8-K: https://www.sec.gov/Archives/edgar/data/0001611115/000162828026054266/q2fy26pressrelease.htm ; 424B4: https://www.sec.gov/Archives/edgar/data/1611115/000119312525137394/d785770d424b4.htm ; bear view: https://public.com/stocks/omda/forecast-price-target ; MarketBeat call highlights: https://www.marketbeat.com/instant-alerts/omada-health-q2-earnings-call-highlights-2026-08-07/
- DCTH Q2-26 8-K: https://www.sec.gov/Archives/edgar/data/0000872912/000162828026053902/dcth-q22026erex991.htm ; trials: https://clinicaltrials.gov/study/NCT06607458 , https://clinicaltrials.gov/study/NCT06875128
- ZVRA Q2-26 8-K: https://www.sec.gov/Archives/edgar/data/0001434647/000143464726000067/zvra-20260805xex991earnings.htm ; CHMP: https://www.biospace.com/press-releases/zevra-therapeutics-provides-update-on-regulatory-submission-for-arimoclomol-for-the-treatment-of-niemann-pick-disease-type-c-npc-in-the-european-union ; celiprolol trial: https://clinicaltrials.gov/study/NCT05432466
- BWAY Q2-26 6-K: https://www.sec.gov/Archives/edgar/data/0001505065/000117184326005440/exh_991.htm ; https://www.marketbeat.com/instant-alerts/brainsway-q2-earnings-call-highlights-2026-08-13/
- HAPN rename: https://stockanalysis.com/stocks/hapn/
- Form 4s: SEC EDGAR via `sec_filings.py` and the raw Form 4 XML (MNTN CIK 1891027, DCTH 872912, ZVRA 1434647, OMDA 1611115, EVER, CXDO)
- Earnings dates: `earnings_calendar.py` (Nasdaq calendar), fetched 2026-10-15
