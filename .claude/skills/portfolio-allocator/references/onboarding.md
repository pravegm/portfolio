# First Run (Onboarding)

Use this when a person has no history file, or their profile still has PROPOSED or "confirm" sections. The goal is to settle everything in **one round of questions**, so the rest of the run can proceed like any other month.

## 1. One onboarding message

Send a single message with numbered questions, each with a recommended default, so the user can answer "defaults are fine except 3 and 7". Don't start research until it's answered.

**A. Accounts and money**
1. Which accounts are open and funded? (ISA broker; eToro; anything else, e.g. a workplace pension or SIPP)
2. eToro: if not yet open, they need it opened and verified before buying micro-caps (verification can take a day or more). If eToro asks for a W-8BEN form, they should complete it (it lowers US dividend withholding to 15%).
3. **Wrapper for the venture sleeve** (decide before the first micro-cap purchase; it's hardest to change later): eToro's regular account (taxable; losses can offset gains) or an eToro Stocks & Shares ISA (gains tax-free; losses unusable; check the specific stocks are available in it). Explain the trade-off from `uk-tax-and-wrappers.md` (asset location) and recommend the ISA for a venture sleeve whose purpose is large gains, provided the stocks are eligible. Both ISAs share the £20,000 allowance; at £9,600 a year in total, there's room.
4. This month's slot split: how many of the ISA slots go to ETFs vs large-caps (or "recommend one").

**B. Investment policy** (show the PROPOSED table from their profile)
5. Confirm or adjust targets and limits. Note what the current holdings mean for it (e.g. an ISA that is 100% one S&P 500 tracker is already over the core target and is US-only).
6. Benchmarks: confirm defaults.
7. Exclusions or preferences (sectors, ethics, themes they care about or want to avoid).
8. Themes of interest for the venture sleeve.

**C. Financial foundations** (short answers are fine; "rather not say" is allowed)
9. Emergency fund of 3-6 months' spending in place?
10. Any high-interest debt?
11. Workplace pension: taking the full employer match? Salary sacrifice available?
12. Income tax band.
13. Under 40 and planning to buy a first home? (Lifetime ISA)
14. Goals with rough dates; any of this money needed within 5 years?

## 2. After the answers

- Write the answers into `profile.md`: remove the PROPOSED marker, set "Policy last reviewed" to today, record the wrapper decision for the venture sleeve.
- Create or complete `portfolio-allocator-history.md` (from `report-template.md`), seeded with current holdings and any pre-skill purchases in "Picks history", marked as made before the skill.
- Create `thesis-register.md` with an entry per holding (for a core index fund the thesis is "market exposure at low cost"; kill criteria are things like a cheaper equivalent fund or a policy change).
- Create `scorecard.md` with benchmarks and, if there were pre-skill purchases, a baseline row each (marked "pre-skill"; not counted in the hit rate).

## 3. First-run differences in the workflow

- **Phase 2:** no execution check (nothing was recommended last month).
- **Phase 3:** scorecard starts now; there's nothing to learn from yet, so say so in one line.
- **Phase 5:** run all diagnostics on whatever is held, plus the household overlap check against the partner's latest holdings. A brand-new venture sleeve has no concentration yet; the first picks should start it across different themes rather than doubling up on one, and should not duplicate the partner's venture names unless deliberately chosen.
- **Phase 7:** for a new or concentrated ISA, the slot plan is mostly about building the policy's buckets from scratch. Explain the plan in plain terms, since this is the first time they see it.
- **Phase 10:** add a short "How to place these orders" note to the report for each platform the user hasn't used before (order type, where to find the ISA vs the regular account, FX shown at checkout).
- Keep the report as thorough as any other month, but put a two-line "what this report is and how to read it" at the top.
