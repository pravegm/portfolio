---
name: portfolio-allocator
description: Run the monthly investment allocation workflow for one of the people who share this repo (each has their own profile, history and portfolios under portfolios/<name>/; e.g. a high-risk micro-cap moonshot portfolio on eToro and a long-term ISA portfolio of large-caps + ETFs on Revolut). Takes portfolio screenshots, researches current holdings exhaustively, then produces a ranked list of new picks with rationale and entry-point reasoning. Trigger this skill whenever the user mentions adding to their portfolio, picking new stocks, monthly investing, "what should I buy this month", "topping up", "what to add to eToro/ISA/Revolut", running their monthly allocation, or any phrasing that suggests choosing new investments. Trigger aggressively — even casual phrasing like "time to invest again" or "help me pick stocks" should pull this in. Do NOT trigger for one-off stock research without portfolio context, or for portfolio review without an intent to add new positions.
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

The phases below use the micro-cap moonshot (eToro) and ISA (Revolut) setup as the worked example. If the user's profile lists different portfolios or brokers, apply the same steps, rigor and output structure to their portfolios instead.

### Phase 0: Identify the user

Ask who is running this (the folder names under `portfolios/` are the options) unless they have already said so in the conversation. Then read `portfolios/<name>/profile.md`.

If the profile is still a blank template, fill it in with the user before Phase 1: which portfolios they have, the broker for each, the strategy and horizon, the typical amount per position and additions per month, risk posture, and any themes. Save it to their `profile.md`.

### Phase 1: Intake

Ask the user for:
1. Screenshots of each of their portfolios (current positions, sizes, P&L if visible)
2. How many new products they want to add to each portfolio this run
3. For ISA only: the ETF/large-cap split they want this month
4. Any specific themes, sectors, or stocks already on their radar (optional but useful)

Wait for all of this before proceeding. Do not start research with partial inputs.

### Phase 2: History check

Before researching new picks, load the run history if it exists:
- Check for `portfolios/<name>/portfolio-allocator-history.md`, or a history file the user attached
- If it exists, parse it for: current holdings, previously rejected picks, previously considered-but-not-picked candidates, and any conviction notes
- If it doesn't exist, this is the first run — note that and proceed

The history file is the source of truth for what NOT to re-recommend without strong reason. If a previously rejected pick is now compelling, that's fine but the rationale must explicitly address why the prior rejection no longer holds.

### Phase 3: Status quo research

Parse the screenshots to extract current holdings. For each holding, research:
- Current price vs. user's likely entry (estimate from P&L if shown)
- Last 3-6 months price action and what drove it
- Recent material news, earnings, regulatory events
- Analyst coverage shifts (upgrades, downgrades, price target changes)
- Thesis status: is the original investment thesis still intact, weakening, or strengthening?

Use web_search aggressively here. Multiple searches per holding is correct, not excessive. Cross-reference sources. For micro-caps especially, check for dilution events, going-concern flags, or insider activity.

Summarize findings as a brief portfolio health snapshot before moving to new picks. Flag any existing position that warrants attention (not a recommendation to sell, just a flag).

### Phase 4: Candidate generation

Generate candidates separately for each portfolio. Aim for 3x the requested count per portfolio (i.e., if user wants 2 micro-cap picks, research 6 candidates and narrow down).

**For the micro-cap portfolio**, search for:
- Small/micro-caps in emerging themes (look at where existing portfolio is concentrated and consider both deepening and diversifying)
- Companies with asymmetric risk/reward — capped downside (cash on hand, real revenue, real product), uncapped upside (TAM, moat formation, optionality)
- 10x+ pathways must be articulable, not hand-waved
- Avoid pure meme/lottery tickets without a real underlying thesis
- Verify availability on eToro before finalizing

**For the ISA portfolio**, search for:
- ETFs: factor tilts, geographic exposure, sector rotation opportunities, expense ratios, AUM, tracking error
- Large-caps: quality businesses with durable moats, reasonable valuation, dividend or buyback history if relevant
- Honor the ETF/large-cap split the user specified
- Verify availability on Revolut before finalizing

For every candidate, research:
- Past 1Y, 3Y, 5Y price performance (where data exists)
- Current valuation metrics relative to peers and history
- Recent analyst views and price targets
- Forward catalysts and risks
- Entry-point quality: is the current price a good entry, fair entry, or premium entry?

Use the entry-point bias **mix**: surface both undervalued opportunities AND high-conviction picks even if priced full. Tag each candidate as one of:
- `Undervalued entry` — price is below fair value, dip-buying opportunity
- `Fair entry, high conviction` — priced fairly, thesis strong enough to pay up
- `Premium but exceptional` — priced richly but quality justifies it

### Phase 5: Selection and ranking

From candidates, select the requested number per portfolio. Rank by conviction. For each pick, the rationale must cover:
1. **What it is** — one-line business description
2. **Why now** — the catalyst or condition that makes this the right month
3. **Thesis** — 2-3 sentences on why this fits the portfolio's intent
4. **Entry tag** — undervalued / fair / premium
5. **Key risk** — the single biggest thing that could break the thesis
6. **Broker confirmation** — confirmed available on eToro or Revolut

If the user requested 2 picks but only 1 candidate clears the rigor bar, **say so and recommend 1 plus holding cash for the other slot**. Do not pad. The skill's job is to help the user invest well, not to fill a quota.

### Phase 6: Output

Produce a single markdown file: `portfolios/<name>/allocations/portfolio-allocation-YYYY-MM-DD.md`. Use this structure:

```markdown
# Portfolio Allocation — [Month YYYY]

## Status quo snapshot
[Brief health check on existing positions, flagging anything that warrants attention.]

## Micro-cap picks (eToro)
### 1. [TICKER] — [Company name]
- **What it is**: ...
- **Why now**: ...
- **Thesis**: ...
- **Entry**: [Undervalued / Fair / Premium]
- **Key risk**: ...
- **Available on eToro**: Confirmed

### 2. [TICKER] — [Company name]
[same structure]

## ISA picks (Revolut)
### 1. [TICKER] — [Name]
[same structure, with ETF-specific fields where relevant: expense ratio, AUM, tracking method]

## Notes
- [Any flags, caveats, or "if this happens, reconsider" notes]
```

Keep the rationale tight. The user wants picks plus rationale, not a research log. Detail belongs in the working notes, not the deliverable.

### Phase 7: Update history

After producing the deliverable, update (or create) `portfolios/<name>/portfolio-allocator-history.md`:

```markdown
# Portfolio Allocator History

## Holdings as of [YYYY-MM-DD]
### eToro (micro-cap)
- [TICKER] — added [date], thesis [one-liner]
...
### Revolut (ISA)
- [TICKER] — added [date], thesis [one-liner]
...

## Picks this run
- [date]: [tickers picked]

## Rejected/considered candidates
- [TICKER] — considered [date], rejected because [reason]
...
```

Present both files to the user.

## Research rigor checklist

Before producing the deliverable, verify mentally:
- [ ] Did I search for each candidate by ticker AND by company name AND by recent news?
- [ ] Did I check multiple sources (news, analyst, financial data)?
- [ ] Did I check for red flags (dilution, going concern, insider selling, governance)?
- [ ] Did I verify broker availability for every final pick?
- [ ] Did I respect the user's portfolio intent (moonshot vs. compounding)?
- [ ] Did I avoid recommending anything already in the portfolio without a strong thesis-change reason?
- [ ] Did I check the history file for previously rejected names?

If any answer is no or "I'm not sure", do more research before delivering.

## What NOT to do

- Don't generate picks from general knowledge alone. Always research current data.
- Don't recommend a stock without confirming it trades on the relevant broker.
- Don't pad the list to hit the requested count — quality over quantity.
- Don't bury risks in the rationale. State them plainly.
- Don't give financial advice in a regulated sense — present analysis, let the user decide.
- Don't skip the history check, even if the user is in a hurry.

## Reference

For deeper research methodology on specific asset types, see `references/research-methods.md`.
