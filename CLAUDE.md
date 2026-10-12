# Portfolio repo

This repo is the shared home for the `portfolio-allocator` skill (`.claude/skills/portfolio-allocator/`). It is used by Praveg and Shubhi, each from their own Claude account.

## Layout

```
portfolios/
  praveg/
    profile.md                        # portfolios, brokers, strategy
    portfolio-allocator-history.md    # run history (holdings, picks, rejections)
    allocations/                      # one portfolio-allocation-YYYY-MM-DD.md per run
  shubhi/
    (same structure)
```

Only read and write the folder of the person running the session. Never mix their holdings, history or picks.

## Keeping history across sessions

Cloud sessions run in throwaway containers and new sessions start from `main`, so a run's files only count once they are on `main`.

- At the start of a run, `git fetch origin main` and make sure the working branch includes it, so the latest history is used.
- At the end of a run, commit the new allocation report and updated history, push, then ask the user whether to open a pull request and merge it into `main`, so the next run sees it.
