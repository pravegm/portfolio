#!/usr/bin/env python3
"""Upcoming US earnings dates for given tickers, from Nasdaq's earnings calendar API.

Usage:
  python3 -I earnings_calendar.py TICKER [TICKER ...] [--days 45]

Scans each weekday in the window (one request per day) and prints matches.
Non-US listings won't appear; confirm dates on the company's IR page.
"""
import datetime as dt
import json
import subprocess
import sys

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"


def day(d):
    raw = subprocess.run(["curl", "-s", "-m", "20", "-A", UA,
                          f"https://api.nasdaq.com/api/calendar/earnings?date={d}"],
                         capture_output=True, text=True).stdout
    try:
        return (json.loads(raw).get("data") or {}).get("rows") or []
    except json.JSONDecodeError:
        return []


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    days = int(a[a.index("--days") + 1]) if "--days" in a else 45
    wanted = {t.upper() for i, t in enumerate(a) if not t.startswith("--") and (i == 0 or a[i - 1] != "--days")}
    found = set()
    d = dt.date.today()
    for _ in range(days):
        d += dt.timedelta(days=1)
        if d.weekday() >= 5:
            continue
        for r in day(d.isoformat()):
            if r.get("symbol") in wanted:
                found.add(r["symbol"])
                print(f"{d}\t{r['symbol']}\t{r.get('time', '')}\tEPS est {r.get('epsForecast', '')}\t{r.get('name', '')}")
    missing = sorted(wanted - found)
    if missing:
        print("No date found in window:", ", ".join(missing))


if __name__ == "__main__":
    main()
