#!/usr/bin/env python3
"""Read-only access to a Trading 212 Invest or Stocks ISA account via its public API.

Usage:
  python3 -I trading212.py cash
  python3 -I trading212.py portfolio
  python3 -I trading212.py orders [--max 200]        filled/cancelled order history
  python3 -I trading212.py dividends [--max 200]
  python3 -I trading212.py transactions [--max 200]   deposits, withdrawals, fees
  python3 -I trading212.py instruments --find TEXT    is an instrument tradeable on this account (ISA check)

Credentials come from environment variables set in the cloud environment's settings:
  T212_API_KEY, T212_API_SECRET   (generate in the Trading 212 app: Settings > API;
                                   grant only read permissions: account data, portfolio, history, metadata)
  T212_ENV                        "live" (default) or "demo"
Never paste keys into chat. This script only sends GET requests; it cannot place or cancel orders.
Endpoint paths follow the beta API (/api/v0) and may change; errors are printed, not hidden.
"""
import base64
import json
import os
import subprocess
import sys

PATHS = {
    "cash": "/equity/account/cash",
    "portfolio": "/equity/portfolio",
    "orders": "/equity/history/orders",
    "dividends": "/history/dividends",
    "transactions": "/history/transactions",
    "instruments": "/equity/metadata/instruments",
}


def get(base, path, auth):
    out = subprocess.run(
        ["curl", "-s", "-m", "30", "-H", f"Authorization: Basic {auth}", "-w", "\n%{http_code}", base + path],
        capture_output=True, text=True,
    ).stdout
    body, _, code = out.rpartition("\n")
    if code.strip() != "200":
        sys.exit(f"HTTP {code.strip()} on {path}: {body[:300]}")
    return json.loads(body)


def main():
    a = sys.argv[1:]
    if not a or a[0] not in PATHS:
        sys.exit(__doc__)
    key, secret = os.environ.get("T212_API_KEY"), os.environ.get("T212_API_SECRET")
    if not key or not secret:
        sys.exit("T212_API_KEY / T212_API_SECRET are not set in this environment. "
                 "Add them in the cloud environment settings and start a new session.")
    base = f"https://{os.environ.get('T212_ENV', 'live')}.trading212.com/api/v0"
    auth = base64.b64encode(f"{key}:{secret}".encode()).decode()
    cmd, limit = a[0], int(a[a.index("--max") + 1]) if "--max" in a else 200

    if cmd in ("orders", "dividends", "transactions"):
        items, path = [], PATHS[cmd] + "?limit=50"
        while path and len(items) < limit:
            page = get(base, path, auth)
            items += page.get("items", [])
            nxt = page.get("nextPagePath")
            path = nxt.replace("/api/v0", "", 1) if nxt else None
        print(json.dumps(items[:limit], indent=1))
    elif cmd == "instruments":
        find = a[a.index("--find") + 1].lower() if "--find" in a else None
        data = get(base, PATHS[cmd], auth)
        if find:
            data = [i for i in data if find in json.dumps(i).lower()]
        print(json.dumps(data[:50], indent=1))
    else:
        print(json.dumps(get(base, PATHS[cmd], auth), indent=1))


if __name__ == "__main__":
    main()
