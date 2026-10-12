---
name: portfolio-allocator
description: Run the monthly investment allocation for one of the people who share this repo (each has their own profile, investment policy, history and portfolios under portfolios/<name>/; typically a venture-style micro-cap portfolio on eToro and a long-term ISA of large-caps and ETFs on the ISA broker named in their profile, such as Revolut or Trading 212). Works like a wealth manager - checks the portfolio against its investment policy and the household's tax position, scores past picks against benchmarks, scans markets and the month ahead, reviews every holding with exit/add/hold verdicts, decides top-down what each slot of the month's budget should do, then fills slots with researched new picks or top-ups. Trigger this skill whenever the user mentions adding to their portfolio, picking new stocks, monthly investing, "what should I buy this month", "topping up", "what to add to eToro/ISA/Revolut/Trading 212", running their monthly allocation, or any phrasing that suggests choosing new investments. Trigger aggressively - even casual phrasing like "time to invest again" or "help me pick stocks" should pull this in. Do NOT trigger for one-off stock research without portfolio context, or for portfolio review without an intent to add new positions.
---

# Portfolio Allocator

Monthly allocation run, done the way a good wealth manager would do it for a client they know well. The non-negotiable principle: **research is exhaustive before any recommendation lands**. A weak recommendation is worse than no recommendation.

## Operating principles

1. **Policy first, picks second.** Every run starts from the person's investment policy (targets, bands, limits) in their profile. Picks serve the policy; market views only tilt within its bands.
2. **Every pound has a job.** Decide top-down what each slot must do this month (fill a gap, rebalance toward target, follow on into a winner, take a new shot) before searching for names.
3. **Costs and taxes are certain; returns are not.** Wrapper, FX, spread and tax effects are checked on every action.
4. **Sell on thesis or policy, not on price.** Exits need a broken thesis, a kill criterion hit, or a policy breach. A falling price with improving operating numbers is a valuation story.
5. **Boring is allowed.** If nothing new clears the bar, the right answer is a core top-up or cash. Never pad.
6. **Keep score honestly.** Every past pick is measured against a benchmark from its entry date. Lessons change the process.
7. **Household, not just individual.** Praveg and Shubhi are a married couple: allowances, concentration and transfers are judged at household level, while each person's report stays about their own portfolios.

## Files

Each person has a folder under `portfolios/<name>/` at the repo root:

- `profile.md`: portfolios, brokers, budget, **investment policy** (targets, bands, limits, benchmarks) and **financial foundations**.
- `portfolio-allocator-history.md`: compact memory of past runs (holdings snapshot, picks history, regime notes, standing decisions, rejections, lessons, realized-gains log).
- `thesis-register.md`: one entry per holding: thesis, kill criteria, next catalyst, review date.
- `scorecard.md`: every past pick with entry date and return versus benchmark.
- `allocations/`: one report per run.

Create any missing file on the run that first needs it (templates in `references/report-template.md`). Never put one person's holdings or picks into the other person's files or report; the only cross-read allowed is the household overlap check in Phase 5.

**Never trade.** The eToro connector can place real orders. This skill only reads: never call `place-trade`, `place-close`, `prepare-trade`, `prepare-close` or `execute-write`, and never change watchlists, alerts or copy settings. Recommendations go in the report; the user places every order themselves. If the user explicitly asks Claude to place an order, that is outside this skill: show the exact order and get their approval for that one order first.

**Broker availability is a hard constraint.** Picks that aren't tradeable on the relevant platform (and ISA-eligible, for ISA picks) are useless. Verify every recommendation.

## References (read when the phase calls for them)

- `references/wealth-management-framework.md`: investment policy, core-satellite, bands, rebalancing with cash flows, sizing, venture sleeve rules, diagnostics, stress scenarios, benchmarks, behavioural guardrails.
- `references/uk-tax-and-wrappers.md`: ISA and GIA rules, CGT, dividends, spouse transfers, bed-and-ISA, asset location, withholding tax, stamp duty, platform costs, tax-year checklist.
- `references/research-methods.md`: evidence standards, materiality tiers, deep-dive checks by asset type, micro-cap gates, red team, entry-point rubric.
- `references/stock-selection.md`: the selection funnel, idea sources, screen recipes, scoring rubrics, how to read analyst ratings, insider/institutional/short signals, forensic scores, valuation by company type, sector KPIs, timing.
- `references/data-sources.md`: the data access check, the helper scripts, the Alpha Vantage budget, the source map by need, source reliability tiers, and what to ask the user for.
- `references/report-template.md`: the report, history, thesis register and scorecard templates.
- `references/onboarding.md`: a person's first run: the one-round onboarding questions, files to create, and what changes in each phase.

## Workflow

Run these phases in order. Do not skip ahead even if the user seems impatient; the value of this skill is the rigor. Where the phases say "ISA broker", use the one named in the profile. If the profile lists different portfolios or brokers, apply the same steps to those.

If a subagent tool is available, research holdings and candidates in parallel batches (e.g. one agent per 8-10 holdings) and merge the findings; the main thread owns the policy, allocation and final judgement.

### Phase 0: Identify the user and load the policy

1. Ask who is running this (folder names under `portfolios/`) unless they already said so. Read their `profile.md`.
2. `git fetch origin main` and make sure the working branch includes it, so the latest files are used.
3. **Data access check** (`references/data-sources.md`): run `scripts/check_access.sh` and plan research around what works. Use the helper scripts in `scripts/` (prices, Finviz quotes and screens, SEC filings, earnings calendar, page text) for reachable sources, web search for the rest, Alpha Vantage as a backup. If an important source is blocked, tell the user once in one line and carry on.
4. **First run** (no runs yet in the history, or the profile has PROPOSED or "confirm" sections): follow `references/onboarding.md`. Ask its questions in one message with recommended defaults, save the answers to `profile.md` (remove the PROPOSED marker, set "Policy last reviewed"), and apply its first-run differences in the later phases.
5. **Annual review.** If "Policy last reviewed" is over 12 months old, or this is the first run in March or April since it was last reviewed (UK tax year ends 5 April), also re-confirm the policy and financial foundations and run the tax-year checklist in `references/uk-tax-and-wrappers.md`.

### Phase 1: Intake

Ask the user for:
1. **Holdings data** for each portfolio. If the eToro connector is connected, pull eToro holdings, cash and trades from it (`references/data-sources.md` section 1b) and don't ask for eToro screenshots. For a Trading 212 ISA with API keys set, use `scripts/trading212.py` (section 1c). For other brokers, CSV exports or statements are best (exact cost basis, needed for CGT); screenshots are fine. Include cash balances.
2. **Slot split** for this month: micro-cap slots (eToro) and ISA slots split between large-caps and ETFs. The budget is in the profile; never assume the split.
3. **Anything that changed**: income, big upcoming expenses, a goal date moving, a view they want tested (optional themes or names).

Then parse the holdings into a table (ticker, value, P&L, weight) and show the user the totals and anything unreadable. Proceed unless they correct it. Wait for all inputs before research.

### Phase 2: Memory and execution check

Load the history, thesis register and scorecard.

- **Execution:** compare holdings (and, with the eToro connector, closed trades since the last run) with last month's action list. Record what was and wasn't done; don't re-litigate skipped items without new information.
- **Standing decisions are final** (e.g. "keep X, do not recommend trimming again"). Respect them unless the condition they name for revisiting has been met.
- **Rejected names** need an explicit reason the rejection no longer holds before they can return.
- **Lessons** from earlier runs apply now; list the ones relevant to this month in working notes.

### Phase 3: Scorecard (the learning loop)

Before any new research, update `scorecard.md`: for every past pick and top-up, return since entry versus the benchmark over the same period (benchmarks are in the profile). Use `scripts/prices.py` for exact closes on the entry date and today, for the pick, the benchmark and GBPUSD. From it, compute hit rate, average excess return, and which kinds of picks have worked (e.g. de-rated quality vs momentum, themes, top-ups vs new names). Be explicit where entry prices are estimated.

Use the results: if a category of pick keeps losing to its benchmark, raise its bar this month and say so in the report. If the ISA satellites as a whole trail the core tracker, that argues for more slots into the core.

### Phase 4: Market and calendar scan

Research what moved markets since the last run, from current data only, with dates and sources:
- Rates, central banks, inflation, jobs; energy and commodities; equities and sector rotation; crypto; regions (US, UK, Europe, Japan, EM) with earnings expectations and positioning; the hottest trades and whether the asymmetry is still there; GBP/USD.

Then build the **next 30-45 days calendar** for this portfolio (`scripts/earnings_calendar.py` for US earnings dates): earnings dates for holdings and candidates, FOMC and Bank of England meetings, CPI prints, drug approval (PDUFA) dates and trial readouts, lock-up expiries, index rebalances, ex-dividend dates, and UK tax-year deadlines.

Classify each development as **regime-level** (changes the policy's tilts), **portfolio-level** (changes a holding's thesis), or **noise**. Monthly news should only move tactical tilts within policy bands. If the regime has genuinely changed, say so first.

### Phase 5: Portfolio diagnostics

Run the diagnostics in `references/wealth-management-framework.md` and produce a short dashboard:
- **Allocation vs policy:** each bucket's weight vs target and band (core, quality large-caps, thematic ETFs, defensives/fixed income, venture sleeve). Underweight buckets are the main input to Phase 7.
- **Concentration:** largest positions, theme exposure (count crypto coins, miners and exchanges together; count AI across direct names, ETFs and baskets), ETF look-through overlap with direct holdings.
- **Exposures:** sector, region, currency (GBP vs USD and others), style (long-duration growth vs value/defensive), position count and line items too small to matter.
- **Mandate drift:** venture-sleeve holdings that are no longer small caps; ISA satellites that have grown core-sized.
- **Household overlap:** read the other person's latest holdings snapshot (their history file) for aggregate overlap only: the same names, themes or ETFs held by both, and combined concentration. Report only the overlap, never their positions or values.
- **Tax position:** for the GIA (eToro), unrealized gains and losses, realized gains so far this tax year vs the CGT allowance (from eToro trading history since 6 April when connected, converted to GBP), and harvesting opportunities (mind the 30-day rule). Asset location: anything better held in an ISA.
- **Costs:** FX fees, spreads and fund charges in the current setup.
- **Stress test:** estimate the portfolio's move in 3-4 scenarios relevant now (e.g. rates +100bp, equity bear market -30%, crypto -50%, a named geopolitical reversal, GBP +10%), using rough betas. The point is to spot fragility, not precision.

### Phase 6: Holding review

Research every holding, tiered by materiality so effort goes where money is. Start with `scripts/finviz.py quote` for all US-listed holdings (one call gives valuation, growth, ownership, short interest, trend and analyst data) and `scripts/sec_filings.py` for Tier 1 US names:
- **Tier 1 (deep):** positions over 3% of their portfolio, anything that moved more than 20% since last run, anything with a calendar event in the next 45 days, anything near a kill criterion, and every candidate for a top-up or exit.
- **Tier 2 (sweep):** everything else gets a news, filings and earnings check.

For each: price action and its driver, latest operating numbers (revenue, orders, backlog, margins, cash, burn) and the sector KPIs that matter, material news, analyst signals read as `references/stock-selection.md` describes (revisions and rating changes over rating levels), insider activity, and for micro-caps dilution filings, going-concern language and cash runway. **Check operating numbers before calling a thesis broken.**

Update the thesis register (thesis, kill criteria, next catalyst, review date) and give every holding a verdict:
- `EXIT`: thesis broken, a kill criterion hit, or a dead line item
- `ADD`: thesis intact or strengthening and the entry is good now (a candidate for a slot)
- `HOLD`
- `HOLD, watch size`: big enough to matter, or above a policy limit
- `HOLD, tight leash`: thesis weak; name what would break it

Check every GIA sell for CGT impact; ISA sells are tax-free, so policy rebalancing is easiest there.

### Phase 7: Allocation plan (top-down, before any names)

Decide what each slot of this month's budget must do, using in priority order:
1. **Financial foundations** from the profile (an emergency fund gap or high-interest debt are flagged once, plainly; the user decides).
2. **Policy drift:** direct new money to underweight buckets first (cash-flow rebalancing; see the framework). This keeps the ISA aligned without selling.
3. **Diagnostics:** fragility or gaps found in Phase 5 (e.g. no fixed income in a rate shock, concentration in one theme).
4. **Opportunities:** `ADD` verdicts from Phase 6 and tactical tilts from Phase 4, within bands.

Write a slot plan, for example: "ISA: 3 core top-ups, 2 quality large-caps (one new, one top-up), 2 ETFs for the defensive gap, 1 satellite; eToro: 1 new shot, 1 follow-on." Honour the user's large-cap/ETF split; within it, the plan decides new vs top-up. Say plainly if the plan departs from what the user might expect, and why.

### Phase 8: Candidate generation and screening

Generate candidates only for slots the plan says need a new name or a choice between holdings. Run the funnel in `references/stock-selection.md`: wide idea generation from its idea sources and screen recipes (`scripts/finviz.py preset ...` runs them; 20-40 names per slot type), hard gates, rubric scoring, then deep research on the top ~3x the number of such slots. Record every name that reached scoring and why it stopped.

**Micro-cap sleeve (eToro):** apply the screen in `references/research-methods.md` (market-cap band, liquidity, exchange, cash runway, dilution, insider activity, quality). A 10x+ path must be articulable: capped downside (cash, real revenue, real product, strategic value) and uncapped upside (TAM, moat formation, optionality). Avoid meme names and buying after a huge run into a binary catalyst. Respect themes the history marks as fully allocated. Follow-ons go to holdings whose operating numbers are proving the thesis, not by default to the biggest losers.

**ISA:** core slots use the policy's chosen core funds. Large-caps: durable moats, reasonable valuation, capital allocation record. ETFs: the ETF screen (cost, size, domicile, replication, accumulating, index method, look-through overlap). Thematic ETFs face a higher bar: fewer than one in ten survive and beat a global index over 15 years, so they must earn their place and stay within the thematic cap. Check ISA eligibility on the user's ISA broker.

For every candidate: 1Y/3Y/5Y performance, valuation vs peers and history, analyst target spread, catalysts and risks, and an entry tag (`Undervalued`, `Fair` / `Fair, high conviction`, `Premium but exceptional`). **Apply the same entry-timing discipline to top-ups as to new picks.**

**Portfolio fit test:** does it add to an already crowded theme, factor or currency? Does it overlap an ETF already held? Does it duplicate a household position?

**Red team the finalists.** For each, write the strongest bear case and a pre-mortem ("it's down 60% in two years; what happened?"). If the bear case can't be answered with evidence, drop it.

**Pick threshold:** a rubric score of 70+ and no unresolved red flag. Show the score in the report.

### Phase 9: Selection and execution plan

Fill the slots in conviction order (£100 per slot unless the profile says otherwise). Each recommendation states: what it is, why now, thesis, entry tag, key risk, kill criteria, broker and ISA-eligibility confirmation, and its job in the slot plan.

- **Don't pad.** If nothing clears the bar for a slot, use it for a qualifying core top-up or hold cash, and say so.
- **Name the rejections**, especially the hot trade everyone is talking about.
- **eToro check:** run `get-instruments-overview` on every eToro finalist and top-up in one batch: confirm `allowOpenPosition`, note whole-unit-only instruments (adjust the amount to whole shares) and the spread.
- **Execution notes:** limit orders for small caps and anything with a wide spread; trade US names in US hours, away from the open and close; FX cost on non-GBP purchases; prefer GBP-traded lines of UCITS ETFs where equivalent; UK shares carry 0.5% stamp duty (ETFs and AIM shares don't).
- **Priority order:** if the user only does three things this month, which three.
- **Arithmetic check:** slots add up to the budget, sells and redeployments reconcile, every figure has a date.

### Phase 10: Output

Write `portfolios/<name>/allocations/portfolio-allocation-YYYY-MM-DD.md` using the template in `references/report-template.md`. It opens with an executive summary (this month's orders, sells, the three things that matter) and a dashboard (allocation vs policy, concentration, scorecard), then the market scan, portfolio review, action list, slot-by-slot allocation, and notes. Be specific with numbers and sources; state risks plainly; keep each rationale tight.

### Phase 11: Update memory, commit, push

Update the history (compact, per the template), thesis register, scorecard and, if anything changed, the profile. Present the report to the user. Then commit and push as the repo's CLAUDE.md says (straight to `main`).

## Research rigor checklist

Before delivering, verify:
- [ ] Data access checked; research planned around what works; gaps disclosed.
- [ ] Policy loaded and drift computed; the slot plan follows from it.
- [ ] Scorecard updated before new picks; lessons applied.
- [ ] Every holding reviewed (Tier 1 deep, Tier 2 swept); operating numbers checked before any thesis is called broken.
- [ ] Calendar built for the next 30-45 days.
- [ ] Concentration, look-through, household overlap, currency and stress test done.
- [ ] Funnel run: idea sources and screens used, gates applied, rubric scores recorded.
- [ ] Each candidate searched by ticker, company name and recent news, from multiple dated sources (Tier A, or two Tier B).
- [ ] Analyst signals read as revisions and changes, not just rating levels; underwriter coverage discounted.
- [ ] Red flags checked (dilution, going concern, insider selling, governance, liquidity).
- [ ] Bear case and pre-mortem written for every finalist.
- [ ] Broker availability and ISA eligibility verified for every pick (eToro picks via `get-instruments-overview`, including whole-unit constraints).
- [ ] No trading tool was called.
- [ ] Tax effect checked for every GIA sell; wrapper and FX costs considered.
- [ ] Standing decisions and prior rejections respected.
- [ ] Numbers add up; every figure dated.

If any answer is no or "I'm not sure", do more work before delivering.

## What NOT to do

- Don't generate picks or verdicts from general knowledge alone. Always research current data.
- Don't let one month's headlines move the portfolio outside its policy bands.
- Don't recommend anything without confirming it trades (and is ISA-eligible where relevant) on the right broker.
- Don't pad slots to hit the count.
- Don't call a thesis broken on price alone, or average down on a name whose thesis is weakening.
- Don't re-raise a decision the user recorded as final.
- Don't bury risks. State them plainly.
- Don't present this as regulated financial or tax advice. Present analysis; the user decides.
- Don't skip the history, scorecard or policy steps, even if the user is in a hurry.
