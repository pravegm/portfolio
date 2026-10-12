# Portfolio repo

This repo is the shared home for the `portfolio-allocator` skill (`.claude/skills/portfolio-allocator/`). It is used by Praveg and Shubhi, each from their own Claude account.

## Layout

```
portfolios/
  praveg/
    profile.md                        # portfolios, brokers, budget, investment policy, financial foundations
    portfolio-allocator-history.md    # run history (holdings, picks, rejections, lessons, realized gains)
    thesis-register.md                # thesis, kill criteria, next catalyst per holding (created on first run)
    scorecard.md                      # every pick vs benchmark (created on first run)
    allocations/                      # one portfolio-allocation-YYYY-MM-DD.md per run
  shubhi/
    (same structure)
```

Only read and write the folder of the person running the session. Never mix their holdings, history or picks.

## Trading

Connected broker tools (e.g. eToro) can place real trades. Use them read-only. Never place, close or modify orders, positions, copy settings, watchlists or alerts unless the account owner explicitly asks in that session and approves each individual order.

## Keeping history across sessions

Cloud sessions run in throwaway containers and new sessions start from `main`, so a run's files only count once they are on `main`.

- At the start of a run, `git fetch origin main` and make sure the working branch includes it, so the latest history is used.
- **Push to `main` directly, every time, without asking.** This is the repo owner's standing instruction. At the end of a run (and after any change to the skill, profiles or history), commit, push the session branch, then push the same commit to `main` (`git push origin HEAD:main`). If `main` has moved on, merge `origin/main` in first (never force-push `main`). Do not open pull requests for this.
