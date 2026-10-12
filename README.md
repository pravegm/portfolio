# Portfolio

Monthly investing for Praveg and Shubhi, run with Claude Code and the `portfolio-allocator` skill.

Each of us puts in **£1,000 a month**:
- **£200 to eToro:** 2 micro-cap "venture" picks at £100 each (10-year+ horizon, aiming for a few big winners)
- **£800 to a Stocks & Shares ISA:** 8 slots of £100 across ETFs and large-cap stocks (Praveg on Revolut, Shubhi on Trading 212)

Each month, Claude:
1. checks the portfolio against your investment policy;
2. scores past picks against a benchmark;
3. scans markets and the month ahead;
4. reviews every holding;
5. decides what each £100 slot should do;
6. researches and recommends the picks;
7. writes a report with an orders table.

Everything is saved to this repo so the next month builds on it.

*Research, not regulated financial or tax advice. Decisions are yours.*

---

## Shubhi: your first run (October 2026)

### Before you start (one-time setup)

1. **GitHub access.** Praveg adds your GitHub account as a collaborator on `pravegm/portfolio` with write access (repo Settings > Collaborators). Accept the email invite.
2. **Connect GitHub to Claude.** In your Claude account, connect GitHub at https://claude.ai/connect-github.
3. **Network access for research.** In Claude Code on the web (claude.ai/code), edit your cloud environment: under **Network access**, add every domain listed in section 4 of [`.claude/skills/portfolio-allocator/references/data-sources.md`](.claude/skills/portfolio-allocator/references/data-sources.md) to **Allowed domains**. Keep the package managers box ticked. Steps: https://code.claude.com/docs/en/cloud-environments#network-access. Without this, research falls back to web search only.
4. **Connect eToro to Claude** (once your eToro account exists): on claude.ai, go to Settings > Connectors > eToro > Connect and log in. Claude then reads your eToro holdings directly instead of from screenshots. It never places trades: you always place orders yourself.
5. **eToro.** If you don't have an eToro account yet, open it now: verification can take a day or more. If eToro asks you to fill in a **W-8BEN** form, do it (it cuts US dividend tax to 15%). Don't buy anything yet: the first run will help you decide whether your micro-caps go in eToro's regular account or an **eToro Stocks & Shares ISA** (tax-free gains, but losses can't be used against other gains).

### Have these ready

- **Trading 212 ISA holdings:** a screenshot of the portfolio screen, or a CSV export of your history (more precise). It should show your S&P 500 ETF from September, its value and its name or ticker.
- **eToro:** whether the account is open and verified. If the eToro connector is connected, no screenshot is needed.
- **The £1,000:** £800 ready to go into the Trading 212 ISA, £200 into eToro.
- **Answers to the onboarding questions.** Short answers are fine, and "rather not say" is allowed:
  - Emergency fund of 3-6 months' spending in place?
  - Any high-interest debt?
  - Workplace pension: getting the full employer match?
  - Income tax band (basic or higher rate)?
  - Under 40 and planning to buy a first home? (A Lifetime ISA adds a 25% bonus.)
  - Goals with rough dates. Will any of this money be needed within 5 years?
  - Anything you don't want to invest in, and themes you're excited about for the micro-caps.
  - Whether the proposed investment policy in [`portfolios/shubhi/profile.md`](portfolios/shubhi/profile.md) looks right. The run will walk you through it.
- **This month's split:** how many of the 8 ISA slots go to ETFs and how many to large-cap stocks. You can also say "recommend one".

### Running it

1. Start a new session at claude.ai/code with the `pravegm/portfolio` repo selected.
2. Type something like: **"I'm Shubhi, time to invest for October"**, and attach your screenshots or CSV.
3. Claude asks the onboarding questions in **one message**, each with a recommended default. Reply in one go ("defaults are fine except...").
4. Claude confirms the holdings it read from your screenshots, then researches. This takes a while: markets, your holdings, stock screens, ETF comparisons, and a bear case for every finalist.
5. You get a report in `portfolios/shubhi/allocations/` that opens with a **table of orders to place**. It includes how-to notes for any platform you haven't used before.
6. Claude saves your profile, history, thesis register and scorecard, and pushes them to `main` automatically.

### After the run

- Place the orders from the table (limit orders where it says so).
- Next month, start a new session, say "time to invest", and bring updated screenshots or a CSV. Claude will check what you actually bought.

---

## Praveg

Ongoing since April 2026 (history imported from earlier runs). The October run starts with a short round to confirm the proposed investment policy and financial foundations in [`portfolios/praveg/profile.md`](portfolios/praveg/profile.md), then runs as usual.

---

## Monthly routine (both of us)

1. New session on this repo; say "time to invest" (and who you are).
2. Attach holdings screenshots or CSV exports for both accounts; give the ISA slot split.
3. Read the report; place the orders.
4. In March and April, the run also does a tax-year-end check: ISA allowance, CGT allowance, and moving holdings between us or into an ISA.

## Repo layout

```
.claude/skills/portfolio-allocator/   the skill: SKILL.md, references/ (method), scripts/ (data helpers)
CLAUDE.md                             repo rules for Claude (per-person folders, push to main)
portfolios/
  praveg/  shubhi/
    profile.md                        accounts, budget, investment policy, financial foundations
    portfolio-allocator-history.md    memory of past runs
    thesis-register.md                why each holding is owned and what would make us sell
    scorecard.md                      every pick vs its benchmark
    allocations/                      one report per month
```

Each person's run only reads and writes their own folder. The one exception is a check for overlap between our two portfolios, which reports only what we both hold.
