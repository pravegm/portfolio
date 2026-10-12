# Templates

Templates for the monthly report (Phase 10) and the memory files (Phase 11). Replace bracketed parts. Drop a section only if it truly has nothing in it, and say so in one line.

## Monthly report: `portfolios/<name>/allocations/portfolio-allocation-YYYY-MM-DD.md`

```markdown
# Portfolio Allocation: [Month YYYY] ([Name])

*Research, not financial advice. I'm not a regulated adviser or tax adviser, and I don't know your full financial picture. Verify prices before trading; decisions are yours. Data as of [date]; research was [search-based / search + direct sources].*

---

## Executive summary

**This month's orders**
| # | Broker / account | Action | Instrument | Amount | Order type | Job in the plan |
|---|---|---|---|---|---|---|
| 1 | eToro | Buy (new) | TICKER, Company | £100 | Limit ~$X | New venture shot |
| ... | | | | | | |

**Sells / exits:** [instrument, account, approx £, reason; "None" if none]

**The three things that matter this month**
1. ...
2. ...
3. ...

---

## Dashboard

**Allocation vs policy**
| Portfolio | Bucket | Target | Band | Actual | Drift |
|---|---|---|---|---|---|

**Concentration:** top 5 positions per portfolio with weights; theme exposure (crypto, AI, ...); household overlap flags.

**Stress test:** scenario, estimated £ impact per portfolio, main drivers.

**Scorecard:** picks to date beating benchmark X of Y; median excess return; best and worst categories; what changed in the process because of it.

**Tax and costs:** GIA realized gains this tax year vs £3,000; unrealized losses available; estimated platform/FX costs this month.

**Consolidation progress** (if the profile has a consolidation goal): lines moved / remaining, £ moved / remaining, CGT used this tax year vs £3,000, ISA allowance used vs £20,000, expected finish month. This month's tranche goes in its own orders table in the executive summary.

**Account placement:** which wrapper each venture pick goes in; GIA holdings classified MOVE / KEEP / EXIT / CHECK. If a migration is under way or requested, include the bed-and-ISA plan (lines to move, estimated CGT vs allowance, sequence, ISA allowance check, estimated costs, step-by-step mechanics).

---

## 1. Global market scan
[Rates, energy/commodities, equities, crypto, regions, hot trades, GBP/USD. Lead with any regime change. Dated, sourced.]

**What this means for you:** [how the regime meets this portfolio's shape, and whether it changes tilts within the policy bands]

**Calendar, next 30-45 days:** [date: event: holdings affected]

---

## 2. Portfolio review
Totals: **eToro £X** (N positions, £ cash), **ISA £Y (+Z%)** (N positions, £ cash). Combined **£T**.

**Execution of last month's plan:** ✓ done ... ✗ not done ...

### The central finding
[The one-paragraph story of the month for this portfolio, with evidence.]

### Exceptions: positions worth attention
| Position | P/L | Value | Weight | Verdict | Reasoning |
|---|---|---|---|---|---|

### Full verdict table: everything else
**eToro:** TICKER +x% £v (short note) · ...
**ISA:** TICKER +£x £v · ...

---

## 3. Action list (ranked by money)
1. [Exits, redeployment of proceeds, trims for policy, explicit "do not add" calls, standing decisions noted]

**Tax note:** [CGT effect of any GIA sells; harvesting or bed-and-ISA opportunities; suggest an accountant where material]

---

## 4. Where [Month]'s £[budget] goes

**Slot plan:** [e.g. ISA: 3 core top-ups, 2 quality large-caps, 2 defensive ETFs, 1 satellite; eToro: 1 new shot, 1 follow-on]. [Why, in terms of policy drift, diagnostics and opportunities. If deviating from what the user may expect, say so here.]

### eToro: N slots, £X
| Slot | Recommendation | Entry | Score | Rationale | Key risk / kill criteria |
|---|---|---|---|---|---|

[Rejected moonshot candidates and why, if relevant.]

### ISA equities: N slots, £X
| Slot | Recommendation | Entry | Score | Rationale | Key risk / kill criteria |
|---|---|---|---|---|---|

### ISA ETFs: N slots, £X
| Slot | Recommendation | Entry | Rationale | Fund facts (TER, size, domicile, acc/dist) |
|---|---|---|---|---|

Mark new positions *(new)* and top-ups "top-up". For each new pick, include a one-line bear case. For ETFs, give an alternative if unavailable.

**Execution notes:** [limit prices, timing, FX, stamp duty where relevant]

---

## 5. Notes
- **What I got wrong last month:** ...
- **What worked:** ...
- **The honest summary of your [month]:** ...
- **If [key scenario] happens:** what to expect and what not to do
- **Watchlist for next month:** ...
- **Rejected this month:** name, reason
- **Foundations / policy flags:** [only if something needs attention]
- **Evidence gaps:** holdings or candidates where fresh data couldn't be found
- **Sources:** key dated sources used
```

## History: `portfolios/<name>/portfolio-allocator-history.md`

A compact memory for the next run, not a copy of the report. Replace month-specific sections; append to cumulative ones.

```markdown
# Portfolio Allocator History

## Standing structure
[Rules that apply every month: budget, slot split asked each run, any standing preferences.]

## Holdings as of YYYY-MM-DD
**eToro £X** (N positions, £ cash, invested £, P/L £)
TICKER +x% £v | ...
**ISA £Y (+Z%)** (N positions, £ cash)
TICKER £v | ...

## Executed from [last month] (confirmed via holdings data)
✓ done ... ✗ not done ...

## Picks history
- YYYY-MM-DD: eToro picks; ISA picks; [one-line theme or outcome]
[cumulative: append each run]

## [MONTH YYYY]: [regime headline]
[Key macro facts from this run, compressed.]

## Key insight
[The central finding of this run.]

## [Month] actions
**EXIT:** ... **ADD:** ... **WATCH SIZE:** ... **DON'T ADD:** ...
[Standing user decisions in capitals, with the condition for revisiting.]

## Rejected [month]
- [name and reason]
- Earlier: [cumulative list of past rejections]

## Realized gains log (eToro GIA), tax year YYYY/YY
| Date | Sold | Approx gain/loss £ | Running total vs £3,000 |
|---|---|---|---|

## Conviction notes / lessons
[cumulative: carry forward, add new ones]
```

## Thesis register: `portfolios/<name>/thesis-register.md`

```markdown
# Thesis Register

| Holding | Account | Bucket | Added | Thesis (one line) | Kill criteria | Next catalyst (date) | Review by | Status |
|---|---|---|---|---|---|---|---|---|
| TICKER | eToro | Venture | YYYY-MM-DD | [why it should win] | [observable facts that would break it] | [event] (date) | YYYY-MM | Intact |
```

Status: Intact / Strengthening / Weakening / Broken. Update every run for Tier 1 names; Tier 2 names when something changes.

## Scorecard: `portfolios/<name>/scorecard.md`

```markdown
# Scorecard

Benchmarks: ISA vs [global tracker]; eToro vs [small-cap index]. All returns in GBP. "est." = entry price estimated from screenshots.

| Date | Account | Pick | Type (new/top-up) | Category | Entry tag | Entry price | Price now | Return | Benchmark return | Excess | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Summary (as of YYYY-MM-DD)
- Picks beating benchmark: X of Y (hit rate Z%)
- Median excess return: ...
- By category: new vs top-up; venture vs ISA large-cap vs ETF; by entry tag; by theme
- Process changes made because of this: ...
```
