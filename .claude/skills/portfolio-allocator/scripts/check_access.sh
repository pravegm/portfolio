#!/usr/bin/env bash
# Data access check for Phase 0: prints HTTP status per source host.
# 200/301/302 = reachable; 403 = the site's bot protection (use web search);
# 000 = blocked by the network policy (add the host to allowed domains) or refused by the site.
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
for u in \
  https://stockanalysis.com/ https://finviz.com/ https://query1.finance.yahoo.com/v8/finance/chart/SPY \
  https://data.sec.gov/submissions/CIK0000320193.json https://api.nasdaq.com/api/calendar/earnings \
  https://companiesmarketcap.com/ https://clinicaltrials.gov/api/v2/version \
  https://www.justetf.com/uk/ https://www.ishares.com/uk https://www.marketbeat.com/ https://www.tipranks.com/ \
  https://www.zacks.com/ https://www.macrotrends.net/ https://www.morningstar.co.uk/ https://www.londonstockexchange.com/ \
  https://www.investegate.co.uk/ https://www.bankofengland.co.uk/ https://www.federalreserve.gov/ https://www.gov.uk/ \
  https://www.coingecko.com/ https://www.biopharmcatalyst.com/ https://fred.stlouisfed.org/ https://openinsider.com/ \
  https://www.etoro.com/ https://www.trading212.com/ https://www.revolut.com/; do
  ua="$UA"; [[ "$u" == *sec.gov* ]] && ua="${SEC_USER_AGENT:-portfolio-allocator research contact@example.org}"
  printf "%s %s\n" "$(curl -s -o /dev/null -m 12 -A "$ua" -w '%{http_code}' "$u")" "$u"
done
