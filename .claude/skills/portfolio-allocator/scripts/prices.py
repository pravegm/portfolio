#!/usr/bin/env python3
"""Daily closes and returns from Yahoo Finance's chart API (via curl).

Usage:
  python3 -I prices.py SYMBOL [SYMBOL ...] [--from YYYY-MM-DD] [--to YYYY-MM-DD]

Prints, per symbol: currency, first and last close in the window, and the return.
Yahoo symbols: US tickers as-is (CRDO), LSE with .L (VWRP.L), Oslo .OL,
Stockholm .ST, Hong Kong .HK, FX like GBPUSD=X, indices like ^RUT or ^GSPC,
crypto like BTC-USD. Use it for the scorecard (entry date to today, pick vs
benchmark) and for dated prices in the report.
"""
import datetime as dt
import json
import subprocess
import sys

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"


def epoch(d):
    return int(dt.datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=dt.timezone.utc).timestamp())


def closes(sym, start, end):
    url = (f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}"
           f"?period1={epoch(start)}&period2={epoch(end) + 86400}&interval=1d")
    raw = subprocess.run(["curl", "-s", "-m", "25", "-A", UA, url],
                         capture_output=True, text=True).stdout
    res = json.loads(raw)["chart"]["result"][0]
    days = [dt.datetime.fromtimestamp(t, dt.timezone.utc).date().isoformat() for t in res["timestamp"]]
    vals = res["indicators"]["quote"][0]["close"]
    pts = [(d, v) for d, v in zip(days, vals) if v is not None]
    return res["meta"].get("currency", "?"), pts


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    today = dt.date.today().isoformat()
    start = args[args.index("--from") + 1] if "--from" in args else (dt.date.today() - dt.timedelta(days=30)).isoformat()
    end = args[args.index("--to") + 1] if "--to" in args else today
    syms = [a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or args[i - 1] not in ("--from", "--to"))]
    for s in syms:
        try:
            cur, pts = closes(s, start, end)
            (d0, p0), (d1, p1) = pts[0], pts[-1]
            print(f"{s}\t{cur}\t{d0} {p0:.4f}\t{d1} {p1:.4f}\t{(p1 / p0 - 1) * 100:+.2f}%")
        except Exception as e:  # noqa: BLE001 - report and continue with other symbols
            print(f"{s}\tERROR\t{e}")


if __name__ == "__main__":
    main()
