---
name: portfolio-allocator
description: Run the monthly investment allocation workflow for one of the people who share this repo (each has their own profile, history and portfolios under portfolios/<name>/; typically a high-risk micro-cap moonshot portfolio on eToro and a long-term ISA portfolio of large-caps + ETFs on the ISA broker named in their profile, such as Revolut or Trading 212). Takes portfolio screenshots, scans global markets, reviews every holding (with exit/add/hold verdicts), then allocates the month's budget across new picks and top-ups with rationale and entry-point reasoning. Trigger this skill whenever the user mentions adding to their portfolio, picking new stocks, monthly investing, "what should I buy this month", "topping up", "what to add to eToro/ISA/Revolut/Trading 212", running their monthly allocation, or any phrasing that suggests choosing new investments. Trigger aggressively — even casual phrasing like "time to invest again" or "help me pick stocks" should pull this in. Do NOT trigger for one-off stock research without portfolio context, or for portfolio review without an intent to add new positions.
---

# Portfolio Allocator

Monthly allocation workflow for the user's portfolios, as described in their profile. The non-negotiable principle: **research is exhaustive before any recommendation lands**. A weak recommendation is worse than no recommendation.

## Portfolio context

This skill is shared by more than one person. Each person has their own folder under `portfolios/<name>/` at the repo root:

- `profile.md`: their portfolios, brokers, strategies and risk posture. This is the portfolio context for the run.
- `portfolio-allocator-history.md`: their run history.
- `allocations/`: their past allocation reports.

Never mix one person's holdings, history or picks into another person's run.

**Broker availability is a hard constraint.** Picks that aren't tradeable on the relevant platform are useless. Verify every recommendation.

## Workflow

Run these phases in order. Do not skip ahead even if the user seems impatient — the value of this skill is the rigor.

The phases below assume the standard setup: a micro-cap moonshot portfolio on eToro and an ISA portfolio. Wherever they say "ISA broker", use the one named in the user's profile (e.g. Revolut, Trading 212). If the profile lists different portfolios or brokers, apply the same steps, rigor and output structure to their portfolios instead.

### Phase 0: Identify the user

Ask who is running this (the folder names under `portfolios/` are the options) unless they have already said so in the conversation. Then read `portfolios/<name>/profile.md`.

If the profile is still a blank template or has gaps marked "confirm on first run", fill it in with the user before Phase 1: which portfolios they have, the broker for each, the strategy and horizon, the typical amount per position and additions per month, risk posture, and any themes. Save it to their `profile.md`.

### Phase 1: Intake

Ask the user for:
1. Screenshots of each of their portfolios (current positions, values, P&L, cash)
2. The slot counts for this month: how many micro-cap slots (eToro) and how many ISA slots go to large-caps vs ETFs. The budget is in their profile; never assume the split.
3. Any specific themes, sectors, or stocks already on their radar (optional but useful)

Wait for all of this before proceeding. Do not start research with partial inputs.

### Phase 2: History check

Load `portfolios/<name>/portfolio-allocator-history.md` (or a history file the user attached). If it doesn't exist, this is the first run: note that and proceed.

Parse it for: standing structure and rules, last month's holdings and recommendations, picks history, regime context, rejected candidates, standing user decisions, and conviction notes/lessons.

- **Standing user decisions are final.** If the history records that the user has decided something (e.g. "keep X, do not recommend trimming again"), respect it and do not re-raise it unless the condition it names for revisiting has been met.
- **Rejected names** need an explicit reason why the prior rejection no longer holds before they can be recommended.
- **Lessons** from earlier runs (e.g. entry-timing discipline on top-ups) apply to this run.

### Phase 3: Global market scan

Research what moved markets since the last run, using current data only:
- **Rates and central banks**: policy moves, 10-year yields, inflation prints, jobs data
- **Energy and commodities**: oil, gas, gold, industrial metals, and what is driving them
- **Equities**: index levels, sector rotation, notable single-day moves and their causes
- **Crypto**: BTC and majors, regulatory developments, key levels
- **Regions**: US, Europe, Japan, EM, UK; earnings growth expectations and fund positioning
- **Hot trades**: what has run hardest this year, and whether the asymmetry is still there

End with **"What this means for you"**: how the regime interacts with the shape of the user's portfolio (duration, concentration, gaps such as no fixed income or no defensives).

If the regime has changed (e.g. first hike in years, a supply shock), say so up front. It is the most important fact in the report.

### Phase 4: Portfolio review

Parse the screenshots to extract every holding with value and P&L. First check **execution of last month's recommendations**: compare the screenshots with last month's action list and record what was and wasn't done.

Then research every holding:
- Price action since last run and what drove it
- Latest earnings and operating numbers (revenue, orders, backlog, cash, burn)
- Material news, regulatory events, analyst target changes
- For micro-caps: dilution filings, going-concern language, insider activity, cash runway

**Separate multiple compression from thesis breaks.** A falling price with improving operating numbers is a valuation story; slipping milestones, rising burn, or a product that keeps not shipping is a thesis break. Check the operating numbers before calling anything broken.

Give every holding a verdict:
- `EXIT`: the thesis is genuinely broken, or it is a dead line item
- `ADD`: thesis intact or strengthening and the entry is good now (a candidate for a slot)
- `HOLD`: thesis intact, no action
- `HOLD, watch size`: position has grown large enough to matter
- `HOLD, tight leash`: thesis intact but weak; name what would break it

Also assess concentration (largest positions as % of each portfolio) and structural gaps (missing asset classes, sectors or regions).

Use web search aggressively. Multiple searches per holding is correct, not excessive. Where fresh data can't be found, say so in the evidence gaps note rather than guessing.

### Phase 5: Candidate generation

Slots can be filled by **new positions or top-ups of existing holdings** marked `ADD`. Research about 3x the slot count per portfolio and narrow down.

**For the micro-cap portfolio (eToro)**:
- Small/micro-caps in emerging themes (look at where existing portfolio is concentrated and consider both deepening and diversifying)
- Asymmetric risk/reward: capped downside (cash on hand, real revenue, real product), uncapped upside (TAM, moat formation, optionality)
- 10x+ pathways must be articulable, not hand-waved
- Avoid pure meme/lottery tickets and buying after a huge run into a binary catalyst
- Respect themes the history marks as fully allocated
- Verify availability on eToro

**For the ISA (large-caps and ETFs)**:
- ETFs: factor tilts, geographic exposure, sector rotation, filling structural gaps (e.g. short-duration fixed income, staples) when the regime calls for it; check expense ratio, AUM, domicile, replication, accumulating vs distributing
- Large-caps: quality businesses with durable moats and reasonable valuation, including direct beneficiaries of the current regime
- Honor the large-cap/ETF slot split the user gave
- Verify availability on the user's ISA broker, and that it is ISA-eligible there

For every candidate, research:
- Past 1Y, 3Y, 5Y price performance (where data exists)
- Current valuation relative to peers and history
- Recent analyst views and price target spread
- Forward catalysts and risks
- Entry-point quality. **Apply the same entry-timing discipline to top-ups as to new picks**: don't top up right after a run.

Tag each candidate:
- `Undervalued`: below fair value, recent drawdown not thesis-breaking
- `Fair` / `Fair, high conviction`: near fair value, thesis strong enough to pay it
- `Premium but exceptional`: use rarely

### Phase 6: Selection

Fill the requested slots, ranked by conviction, at £100 per slot unless the profile says otherwise. Each slot's rationale covers: what it is (for new names), why now, the thesis, the entry tag, the key risk, and broker confirmation.

- **Don't pad.** If nothing clears the bar for a slot, say so and either use it for a top-up that does clear it, or recommend holding cash.
- **Deviating is allowed, but explicit.** If the regime makes the requested mix unwise (e.g. eight new speculative names into a rate shock), recommend the better allocation and state plainly why you are deviating. Keep the slot structure the user asked for.
- **Rejections are part of the output.** Name the obvious candidates you rejected and why, especially the hot trade everyone is talking about.

### Phase 7: Output

Produce `portfolios/<name>/allocations/portfolio-allocation-YYYY-MM-DD.md` with this structure:

```markdown
# Portfolio Allocation — [Month YYYY]

*Research, not financial advice. I'm not a regulated adviser or tax adviser, and I don't know your full financial picture. Verify prices before trading; decisions are yours.*

---

## 1. Global market scan
[Rates, energy/commodities, equities, crypto, regions, hot trades. Lead with the regime change if there is one.]

**What this means for you:** [how the regime meets this portfolio's shape]

---

## 2. Portfolio review
Totals: **eToro £X** (N positions, £ cash), **ISA £Y (+Z%)** (N positions, £ cash). Combined **£T**.

### The central finding
[The one-paragraph story of the month for this portfolio, with the evidence.]

### Exceptions: positions worth attention
| Position | P/L | Value | Verdict | Reasoning |
|---|---|---|---|---|

### Full verdict table: everything else
**eToro (holds):** TICKER +x% £v (short note) · ...
**ISA (all HOLD):** TICKER +£x £v · ...

[Concentration and structural gaps.]

---

## 3. Action list (ranked by money)
1. [Exits, redeployment of proceeds, explicit "do not add" calls, standing decisions noted]

**Tax note:** [eToro is taxable: losses can offset gains against the CGT allowance. Suggest an accountant.]

---

## 4. Where [Month]'s £[budget] goes
[If deviating from the requested mix, say so and why, first.]

### eToro — N slots, £X
| Slot | Recommendation | Entry | Rationale |
|---|---|---|---|

[Rejected moonshot candidates and why, if no new name cleared the bar.]

### ISA equities — N slots, £X
| Slot | Recommendation | Entry | Rationale |
|---|---|---|---|

### ISA ETFs — N slots, £X
| Slot | Recommendation | Entry | Rationale |
|---|---|---|---|

Mark new positions *(new)*; top-ups say "top-up". ETFs name the full fund, and an alternative if unavailable.

---

## 5. Notes
- **What I got wrong last month:** [honest review of last month's picks]
- **What worked:** [...]
- **The honest summary of your [month]:** [...]
- **If [key scenario] happens:** [what to expect and what not to do]
- **Watchlist for next month:** [...]
- **Rejected this month:** [name, reason]
- **Evidence gaps:** [holdings or candidates where fresh data couldn't be found]
```

Be specific with numbers and sources; state risks plainly. Keep each rationale tight.

### Phase 8: Update history

Update (or create) `portfolios/<name>/portfolio-allocator-history.md`. It is a compact memory for the next run, not a copy of the report. Keep these sections, replacing the month-specific ones and appending to the cumulative ones:

```markdown
# Portfolio Allocator History

## Standing structure
[Rules that apply every month, e.g. ask for the slot split each run. Budget.]

## Holdings as of YYYY-MM-DD
**eToro £X** (N positions, £ cash, invested £, P/L £)
TICKER +x% £v | ...
**ISA £Y (+Z%)** (N positions, £ cash)
TICKER £v | ...

## Executed from [last month] (confirmed via screenshots)
✓ done ... ✗ not done ...

## Picks history
- YYYY-MM-DD: eToro picks; ISA picks — [one-line outcome or theme]
[cumulative: append this run's line]

## [MONTH YYYY] — [regime headline]
[Key macro facts from this run's market scan, compressed.]

## Key insight
[The central finding of this run.]

## [Month] actions
**EXIT:** ... **ADD:** ... **WATCH SIZE:** ... **DON'T ADD:** ...
[Standing user decisions recorded here, in capitals, so later runs respect them.]

## Rejected [month]
- [name and reason; keep the cumulative "Earlier:" list of past rejections]

## Conviction notes / lessons
[cumulative: carry forward, add new lessons]
```

Present both files to the user. Then commit and push them as described in the repo's CLAUDE.md.

## Research rigor checklist

Before producing the deliverable, verify:
- [ ] Did I research every holding, not just the big movers?
- [ ] Did I check operating numbers before calling any thesis broken?
- [ ] Did I check execution of last month's recommendations?
- [ ] Did I search for each candidate by ticker AND by company name AND by recent news?
- [ ] Did I check multiple sources (news, analyst, financial data)?
- [ ] Did I check for red flags (dilution, going concern, insider selling, governance)?
- [ ] Did I verify broker availability (and ISA eligibility) for every final pick?
- [ ] Did I apply entry-timing discipline to top-ups as well as new picks?
- [ ] Did I respect the user's portfolio intent (moonshot vs. compounding)?
- [ ] Did I respect standing user decisions and previously rejected names in the history?

If any answer is no or "I'm not sure", do more research before delivering.

## What NOT to do

- Don't generate picks or verdicts from general knowledge alone. Always research current data.
- Don't recommend anything without confirming it trades on the relevant broker.
- Don't pad slots to hit the requested count. Quality over quantity.
- Don't call a thesis broken on price alone.
- Don't re-raise a decision the user has recorded as final.
- Don't bury risks in the rationale. State them plainly.
- Don't give financial advice in a regulated sense. Present analysis, let the user decide.
- Don't skip the history check, even if the user is in a hurry.

## Reference

For deeper research methodology on specific asset types, see `references/research-methods.md`.
