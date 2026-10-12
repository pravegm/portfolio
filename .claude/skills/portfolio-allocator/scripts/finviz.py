#!/usr/bin/env python3
"""Finviz quote snapshots and screens (US-listed stocks), via curl.

Usage:
  python3 -I finviz.py quote TICKER [TICKER ...]
  python3 -I finviz.py screen FILTERS [--order -marketcap] [--max 60]
  python3 -I finviz.py preset NAME [--max 60]

quote: key metrics (market cap, EV, valuation, growth, margins, cash, debt,
  insider/institutional ownership and transactions, short float, SMA distances,
  performance, analyst recommendation 1=Strong Buy..5=Sell, target price, earnings date).
screen: Finviz filter codes, comma-separated (as in a finviz.com/screener.ashx URL "f=").
preset: named screens matching the recipes in references/stock-selection.md.
Data is delayed and Finviz's; cross-check figures that drive a verdict.
"""
import html
import re
import subprocess
import sys

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"

PRESETS = {
    # A. Micro-cap quality growth
    "microcap-quality-growth": "cap_smallunder,geo_usa,sh_avgvol_o200,sh_price_o2,fa_salesqoq_o20,"
                               "fa_grossmargin_o35,fa_curratio_o1.5,fa_debteq_u0.5",
    # B. Micro-cap insider conviction (recent insider buying)
    "microcap-insider-buying": "cap_smallunder,sh_avgvol_o200,sh_price_o2,it_latestbuys",
    # C. Quality on sale (large caps)
    "quality-on-sale": "cap_largeover,fa_roe_o15,fa_opermargin_o15,fa_debteq_u1,fa_fpe_u25,ta_highlow52w_b20h",
    # D. Estimate revision / earnings momentum (large caps)
    "large-earnings-momentum": "cap_largeover,fa_epsqoq_o20,fa_salesqoq_o10,fa_estltgrowth_o10,an_recom_buybetter,ta_sma200_pa",
    # E. Pre-revenue / early biotech with cash support
    "biotech-cash-runway": "cap_smallunder,sec_healthcare,ind_biotechnology,sh_avgvol_o200,fa_curratio_o5,fa_debteq_u0.1",
}


def get(url):
    return subprocess.run(["curl", "-sL", "-m", "25", "-A", UA, url],
                          capture_output=True, text=True, errors="replace").stdout


def clean(cell):
    return html.unescape(re.sub(r"<[^>]+>", "", cell)).strip()


def quote(ticker):
    page = get(f"https://finviz.com/quote.ashx?t={ticker}")
    cells = [clean(c) for c in re.findall(r"<td[^>]*snapshot-td2[^>]*>(.*?)</td>", page, re.S)]
    if not cells:
        print(f"{ticker}: no data (not US-listed on Finviz?)")
        return
    pairs = list(zip(cells[0::2], cells[1::2]))
    print(f"== {ticker}")
    print(" | ".join(f"{k}: {v}" for k, v in pairs if v not in ("", "-")))


def screen(filters, order="-marketcap", limit=60):
    rows, start = [], 1
    while len(rows) < limit:
        page = get(f"https://finviz.com/screener.ashx?v=111&f={filters}&o={order}&r={start}")
        found = 0
        for seg in page.split("</tr>"):
            tr = seg[seg.rfind("<tr"):]  # innermost row; the results table is nested
            tick = re.search(r'(?:stock|quote\.ashx)\?t=([A-Z0-9.\-]+)', tr)
            if not tick:
                continue
            tds = [clean(td) for td in re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)]
            if len(tds) >= 10 and tds[0].isdigit():
                tds[1] = tick.group(1)  # the ticker cell also holds a logo letter
                rows.append(tds)
                found += 1
        total = re.search(r"#\d+ / (\d+)", page)
        if found == 0 or (total and start + 20 > int(total.group(1))):
            break
        start += 20
    total_txt = total.group(1) if total else "?"
    print(f"Filters: {filters}  (matches: {total_txt}, showing {min(len(rows), limit)})")
    print("No\tTicker\tCompany\tSector\tIndustry\tCountry\tMktCap\tP/E\tPrice\tChange\tVolume")
    for r in rows[:limit]:
        print("\t".join(r[:11]))


def main():
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    limit = int(a[a.index("--max") + 1]) if "--max" in a else 60
    if a[0] == "quote":
        for t in [x for x in a[1:] if not x.startswith("--")]:
            quote(t.upper())
    elif a[0] == "screen":
        order = a[a.index("--order") + 1] if "--order" in a else "-marketcap"
        screen(a[1], order, limit)
    elif a[0] == "preset":
        if len(a) < 2 or a[1] not in PRESETS:
            sys.exit("presets: " + ", ".join(PRESETS))
        screen(PRESETS[a[1]], "-marketcap", limit)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
