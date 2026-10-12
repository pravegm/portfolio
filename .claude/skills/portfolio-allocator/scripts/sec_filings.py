#!/usr/bin/env python3
"""Recent SEC filings for a US ticker (via data.sec.gov), optionally filtered by form.

Usage:
  python3 -I sec_filings.py TICKER [--forms 4,8-K,S-3,424B5,10-Q] [--n 20]

Useful forms: 4 (insider trades), 144 (planned insider sales), 8-K (material events),
S-1/S-3/424B* (offerings, dilution), 10-Q/10-K, SC 13D/13G (large holders).
Each line has a link to the filing index. Read a Form 4 with fetch_text.py to see
whether it is an open-market buy (code P), sale (S), or option exercise (M).
"""
import json
import os
import subprocess
import sys

UA = os.environ.get("SEC_USER_AGENT", "portfolio-allocator research contact@example.org")


def get(url):
    return json.loads(subprocess.run(["curl", "-s", "-m", "25", "-A", UA, url],
                                     capture_output=True, text=True).stdout)


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    ticker = args[0].upper()
    forms = set(args[args.index("--forms") + 1].split(",")) if "--forms" in args else None
    n = int(args[args.index("--n") + 1]) if "--n" in args else 20
    tickers = get("https://www.sec.gov/files/company_tickers.json")
    cik = next((v["cik_str"] for v in tickers.values() if v["ticker"] == ticker), None)
    if cik is None:
        sys.exit(f"{ticker}: not found in SEC ticker list (foreign or non-US listing?)")
    d = get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json")
    r = d["filings"]["recent"]
    print(f"{d['name']} (CIK {cik})")
    shown = 0
    for form, date, acc, doc in zip(r["form"], r["filingDate"], r["accessionNumber"], r["primaryDocument"]):
        if forms and form not in forms:
            continue
        link = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/{doc}"
        print(f"{date}\t{form}\t{link}")
        shown += 1
        if shown >= n:
            break


if __name__ == "__main__":
    main()
