#!/usr/bin/env python3
"""Browser check that the S3 /index.html link-fix restores links quarto-nav.js strips.

Serves the rendered site (site/_site) over a local HTTP server and opens a few
pages with a real browser (Playwright/Chromium). For every link whose
data-original-href ends in /index.html (i.e. one quarto-nav.js stripped to a
folder path), it asserts the live href was restored to end in /index.html.

Usage:  python scripts/check-s3-links.py [path-to-_site]
Requires: playwright + chromium (python -m playwright install chromium).
Exit 0 = OK, 1 = FAIL.
"""
import http.server
import os
import sys
import threading

from playwright.sync_api import sync_playwright


def main() -> int:
    base = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(__file__), "..", "site", "_site"
    )
    base = os.path.abspath(base)
    if not os.path.isdir(base):
        print(f"NOT A DIR: {base}", file=sys.stderr)
        return 2
    os.chdir(base)
    srv = http.server.ThreadingHTTPServer(
        ("127.0.0.1", 0), http.server.SimpleHTTPRequestHandler
    )
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    fail = False
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for rel in [
            "index.html",  # depth 0 — was 404 for the old ../src external fix
            "framework/index.html",  # depth 1
            "framework/introduction.html",  # depth 2 — was 404 for the old ../src fix
            "framework/vs-01.html",  # depth 2
        ]:
            if not os.path.exists(rel):
                continue
            page.goto(f"http://127.0.0.1:{port}/{rel}")
            page.wait_for_load_state("load")
            links = page.eval_on_selector_all(
                "a",
                "ls => ls.map(x => ({o: x.getAttribute('data-original-href'), h: x.href}))",
            )
            stripped = [l for l in links if l["o"] and l["o"].endswith("index.html")]
            bad = [l for l in stripped if not l["h"].endswith("index.html")]
            status = "OK" if (stripped and not bad) else ("FAIL(no-links)" if not stripped else "FAIL")
            if status != "OK":
                fail = True
            print(f"{rel}: stripped={len(stripped)} bad={len(bad)} -> {status}")
            for l in (stripped + bad)[:3]:
                print(f"    {l['o']}  ->  {l['h']}")
        browser.close()

    print("S3_LINK_FIX_OK" if not fail else "S3_LINK_FIX_FAIL")
    return 0 if not fail else 1


if __name__ == "__main__":
    raise SystemExit(main())
