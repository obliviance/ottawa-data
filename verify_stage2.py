#!/usr/bin/env python3
"""Stage 2 verification: render the JavaScript-only sources in a real browser.

Stage 0-1 (verify.py) marks a source `needs_browser` when the URL loads but the body
is a JavaScript shell with no content. This script drives a headless Chromium over the
Chrome DevTools Protocol, renders each of those pages for real, and records:

  - the text and structure that actually appear,
  - every XHR / fetch the page makes (this is where the real backing API hides -
    devapps talks to devapps-restapi.ottawa.ca, Engage Ottawa to an EngagementHQ API),
  - a screenshot, saved outside the repo as evidence,
  - a revised outcome: `machine-readable` if a clean JSON endpoint turned up,
    otherwise `reachable_html` (the content is there, it just needs a renderer).

It needs a Chromium reachable over CDP. In this environment that is the service at
$CHROMIUM_CDP_URL (default http://chromium:9222); the endpoint enforces Chrome's
Host-header check, so we fetch /json/version with Host: localhost and rewrite the
returned websocket URL to the container's IP.

    pip install playwright          # the browser binary is remote; no `playwright install`
    python3 verify_stage2.py                       # the needs_browser/blocked set + curated extras
    python3 verify_stage2.py --only devapps engage-ottawa
    python3 verify_stage2.py --cdp http://localhost:9222

Output: verification_stage2.json  (screenshots -> --shots-dir, default a temp dir).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import socket
import sys
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).parent
STAGE01 = ROOT / "verification.json"
OUT = ROOT / "verification_stage2.json"

NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
CDP_DEFAULT = os.environ.get("CHROMIUM_CDP_URL", "http://chromium:9222")

# reachable_html in stage 0-1, but really interactive apps worth a browser look
STAGE2_EXTRA = ["devapps", "lobbyist-registry", "engage-ottawa", "escribe",
                "committee-of-adjustment", "social-housing-registry"]

# an XHR is a promising *data* endpoint if its URL matches this ...
DATA_RE = re.compile(
    r"(/rest/services/|/FeatureServer|/MapServer|hub\.arcgis|/api/3/action/|/api/search/|"
    r"/api/feed/|/datasets?/|/devapps/|GetCalendarMeetings|/data/[a-z-]+/(index|dates)|"
    r"/records?/|/query\?|/collections/|graphql|/odata|/api/v\d)", re.I)
# ... and is NOT one of these (framework plumbing, CMS chrome, analytics, bot sensors)
NOISE_RE = re.compile(
    r"(nationbuilderthemes|datadoghq|px-cloud|px\.net|pxebumdlwe|perimeterx|/rum\b|"
    r"visit_token|/locales?/|lang_[a-z]{2}\.json|/common\.json|manifest\.json|config\.json|"
    r"sharing/rest/portals/self|/api/gateway/|/api/alerts/|/api/footer/|/api/menu/|"
    r"google|gtag|analytics|doubleclick|hotjar|segment\.|sentry|facebook|linkedin|"
    r"cloudflareinsights|clarity|/cookie|/consent|recaptcha|hcaptcha|\?d=[\w.-]+$)", re.I)
ASSET_RE = re.compile(r"\.(png|jpe?g|gif|svg|woff2?|ttf|css|js|ico|mp4|webp|map|html?)(\?|$)", re.I)
# query params that carry a credential - redact the value before it is written to disk
SECRET_PARAM_RE = re.compile(
    r"((?:access_?token|auth_?key|api_?key|apikey|key|token|sig|signature|client_?secret|"
    r"password|pw|secret)=)([^&#]+)", re.I)
SECRET_TOKEN_RE = re.compile(r"\b(pk|sk)\.[A-Za-z0-9._-]{20,}")


def redact(url: str) -> str:
    url = SECRET_PARAM_RE.sub(r"\1<redacted>", url)
    url = SECRET_TOKEN_RE.sub(r"\1.<redacted>", url)
    return url


def cdp_ws(cdp_http: str) -> str:
    """Resolve the browser websocket endpoint, working around the Host-header check."""
    host = urllib.parse.urlparse(cdp_http).hostname
    port = urllib.parse.urlparse(cdp_http).port or 9222
    ip = socket.gethostbyname(host)
    req = urllib.request.Request(f"http://{ip}:{port}/json/version",
                                 headers={"Host": f"localhost:{port}"})
    ver = json.loads(urllib.request.urlopen(req, timeout=10).read())
    ws = ver["webSocketDebuggerUrl"]
    ws = re.sub(r"//(localhost|127\.0\.0\.1)(:\d+)?/", f"//{ip}:{port}/", ws)
    return ws, ver.get("Browser", "?")


def classify_xhr(calls: list[dict]) -> tuple[list[dict], list[dict]]:
    """Split XHR/fetch calls into (data endpoints, other same-origin JSON)."""
    data, other, seen = [], [], set()
    for c in calls:
        u = c["url"]
        if ASSET_RE.search(u) or NOISE_RE.search(u):
            continue
        key = u.split("?")[0]
        if key in seen:
            continue
        seen.add(key)
        c = {**c, "url": redact(u)}
        rec = {k: c[k] for k in ("method", "url", "status", "content_type") if k in c}
        is_json = "json" in (c.get("content_type") or "") or c.get("content_type") == ""
        if DATA_RE.search(u) and is_json:
            data.append(rec)
        elif is_json:
            other.append(rec)
    return data[:20], other[:12]


def render(page, url: str, shots_dir: pathlib.Path, sid: str, i: int) -> dict:
    calls: list[dict] = []
    resp_meta: dict[str, dict] = {}

    def on_request(r):
        if r.resource_type in ("xhr", "fetch"):
            calls.append({"method": r.method, "url": r.url, "resource_type": r.resource_type})

    def on_response(r):
        if r.request.resource_type in ("xhr", "fetch"):
            resp_meta[r.url] = {"status": r.status,
                                "content_type": (r.headers or {}).get("content-type", "")}

    page.on("request", on_request)
    page.on("response", on_response)

    err = None
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=45000)
        try:
            page.wait_for_load_state("networkidle", timeout=20000)
        except Exception:
            pass
        page.wait_for_timeout(2500)
    except Exception as e:
        err = f"{type(e).__name__}: {str(e)[:200]}"

    for c in calls:
        c.update(resp_meta.get(c["url"], {}))

    shot = ""
    try:
        shots_dir.mkdir(parents=True, exist_ok=True)
        name = f"{sid}-{i}.png"
        page.screenshot(path=str(shots_dir / name), full_page=False)
        shot = name
    except Exception:
        pass

    text = ""
    try:
        text = page.evaluate("document.body ? document.body.innerText : ''")
    except Exception:
        pass
    text = redact(re.sub(r"\n{3,}", "\n\n", text).strip())

    links = tables = 0
    try:
        links = page.evaluate("document.querySelectorAll('a[href]').length")
        tables = page.evaluate("document.querySelectorAll('table, [role=table], .table').length")
    except Exception:
        pass

    apis, other_json = classify_xhr(calls)
    if err and len(text) < 200:
        outcome = "needs_browser"  # still couldn't get anything
    elif apis:
        outcome = "machine-readable"  # a real data endpoint turned up
    elif len(text) > 300:
        outcome = "reachable_html"  # renders fine; a headless scrape works
    else:
        outcome = "needs_browser"

    return {
        "url": url,
        "final_url": redact(page.url),
        "title": (page.title() or "")[:160],
        "rendered_text_chars": len(text),
        "rendered_text_sample": text[:1500],
        "link_count": links,
        "table_count": tables,
        "xhr_total": len(calls),
        "discovered_apis": apis,
        "other_json_xhr": other_json,
        "screenshot": shot,
        "new_outcome": outcome,
        "error": err,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", nargs="+", metavar="ID", help="only these source ids")
    ap.add_argument("--cdp", default=CDP_DEFAULT, help=f"CDP http endpoint (default {CDP_DEFAULT})")
    ap.add_argument("--shots-dir", default="", help="screenshot dir (default: a scratch temp dir)")
    args = ap.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit("playwright not installed - `pip install playwright` (browser binary is remote)")

    data = json.loads((ROOT / "sources.json").read_text())
    by_id = {s["id"]: s for s in data["sources"]}
    stage01 = json.loads(STAGE01.read_text())

    if args.only:
        targets = args.only
    else:
        targets = [sid for sid, s in stage01["sources"].items()
                   if s["rollup"] in ("needs_browser", "blocked")]
        targets += [sid for sid in STAGE2_EXTRA if sid not in targets]

    shots_dir = pathlib.Path(args.shots_dir) if args.shots_dir else \
        pathlib.Path(os.environ.get("TMPDIR", "/tmp")) / "ottawa-stage2-shots"

    ws, browser_ver = cdp_ws(args.cdp)
    print(f"CDP {args.cdp} -> {browser_ver}\nrendering {len(targets)} sources -> screenshots in {shots_dir}\n")

    results: dict[str, dict] = {}
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(ws)
        for sid in targets:
            src = by_id.get(sid)
            if not src:
                print(f"  ?? {sid}: not in sources.json"); continue
            urls = src["urls"][:2]  # first couple; enough to characterise
            url_results = []
            for i, url in enumerate(urls):
                ctx = browser.new_context(viewport={"width": 1280, "height": 900},
                                          user_agent="Mozilla/5.0 ottawa-data-verify/0.2")
                page = ctx.new_page()
                r = render(page, url, shots_dir, sid, i)
                ctx.close()
                url_results.append(r)
                api = f" · {len(r['discovered_apis'])} API-ish XHR" if r["discovered_apis"] else ""
                print(f"  {r['new_outcome']:16} {sid:24} {r['rendered_text_chars']:>6} chars{api}  {url}")
            results[sid] = {
                "name": src["name"],
                "claimed_access": src["access"],
                "url_results": url_results,
                "rollup": _rollup([u["new_outcome"] for u in url_results]),
            }
        browser.close()

    out = {
        "generated_at": NOW.isoformat(),
        "tool": "verify_stage2.py 0.1 (headless Chromium over CDP)",
        "browser": browser_ver,
        "screenshots_dir": str(shots_dir),
        "note": "Rendered the JavaScript-only sources. discovered_apis lists the XHR/fetch "
                "calls that look like a real data endpoint - promote to sources.json and "
                "re-run verify.py to fingerprint them.",
        "sources": results,
    }
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")

    print(f"\nwrote {OUT.name}")
    promoted = {sid: [a["url"] for a in u["discovered_apis"]]
                for sid, s in results.items() for u in s["url_results"] if u["discovered_apis"]}
    if promoted:
        print("\ncandidate APIs to add to sources.json:")
        for sid, apis in promoted.items():
            for a in apis[:4]:
                print(f"  {sid}: {a}")


def _rollup(outcomes: list[str]) -> str:
    rank = ["needs_browser", "reachable_html", "machine-readable"]
    return max(outcomes, key=rank.index) if outcomes else "needs_browser"


if __name__ == "__main__":
    main()
