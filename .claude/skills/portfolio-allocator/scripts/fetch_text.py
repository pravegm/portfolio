#!/usr/bin/env python3
"""Fetch a web page through the session proxy (via curl) and print readable text.

Usage:
  python3 -I fetch_text.py URL [--find WORD] [--chars N]

--find prints the text around each occurrence of WORD (case-insensitive).
--chars limits output length (default 6000).
SEC hosts get the declared User-Agent SEC requires.
"""
import html
import os
import re
import subprocess
import sys

BROWSER_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
SEC_UA = os.environ.get("SEC_USER_AGENT", "portfolio-allocator research contact@example.org")


def fetch(url):
    ua = SEC_UA if "sec.gov" in url else BROWSER_UA
    out = subprocess.run(
        ["curl", "-sL", "-m", "25", "-A", ua, "-w", "\n%{http_code}", url],
        capture_output=True, text=True, errors="replace",
    ).stdout
    body, _, code = out.rpartition("\n")
    return code.strip(), body


def to_text(body):
    body = re.sub(r"<(script|style|noscript)\b.*?</\1>", " ", body, flags=re.S | re.I)
    body = re.sub(r"<br\s*/?>|</(p|div|tr|li|h\d)>", "\n", body, flags=re.I)
    text = html.unescape(re.sub(r"<[^>]+>", " ", body))
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n\s*\n+", "\n", text).strip()


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    url, find, chars = args[0], None, 6000
    if "--find" in args:
        find = args[args.index("--find") + 1]
    if "--chars" in args:
        chars = int(args[args.index("--chars") + 1])
    code, body = fetch(url)
    print(f"[HTTP {code}] {url}")
    if code != "200":
        sys.exit(1)
    text = body if body.lstrip().startswith(("{", "[")) else to_text(body)
    if find:
        hits = [m.start() for m in re.finditer(re.escape(find), text, re.I)]
        for h in hits[:8]:
            print("...", text[max(0, h - 300):h + 700].replace("\n", " "), "...\n")
        if not hits:
            print(f"'{find}' not found")
    else:
        print(text[:chars])


if __name__ == "__main__":
    main()
