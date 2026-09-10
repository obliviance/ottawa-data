#!/usr/bin/env python3
"""Grab a *small* sample of a source's data without building its full parser.

For sources that need a bespoke parser (see ROADMAP.md), this saves enough to
(a) prove the data is reachable and (b) show what a full parser would face:

  samples/<source-id>/
    page.html / *.pdf        the raw artifact(s)
    sample.csv               first --rows of the first HTML table, if any
    api.json                 --api response, if given
    README.md                what was found + what a full parser needs

Where a table or API sample parses, it's also registered in the warehouse
(shape="html" / "json-api", suffix "__sample") so it shows in catalog/INDEX.md.

    python3 tools/sample.py office-expenses
    python3 tools/sample.py devapps --api "https://devapps-restapi.ottawa.ca/devapps/apptype/all?authKey=KEY"
    python3 tools/sample.py budget-documents --pdfs 3
    python3 tools/sample.py committee-of-adjustment --render      # via headless Chromium
"""
from __future__ import annotations

import argparse
import io
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import warehouse  # noqa: E402
from _http import download, get  # noqa: E402

REPO = pathlib.Path(__file__).parent.parent
SAMPLES = REPO / "samples"
DATA_LINK = re.compile(r'href=["\']([^"\']+\.(?:csv|xlsx?|pdf|json|geojson|zip|xml))["\']', re.I)


def src(sid: str) -> dict:
    for s in json.loads((REPO / "sources.json").read_text())["sources"]:
        if s["id"] == sid:
            return s
    sys.exit(f"no such source id: {sid}")


def render(url: str) -> tuple[str, list[str]]:
    """(visible text or html, discovered data links) via the CDP Chromium."""
    import os
    import socket
    import urllib.request as ur
    from playwright.sync_api import sync_playwright
    host = os.environ.get("CHROMIUM_CDP_URL", "http://chromium:9222")
    ip = socket.gethostbyname(host.split("//")[1].split(":")[0])
    ver = json.loads(ur.urlopen(ur.Request(f"http://{ip}:9222/json/version",
                                           headers={"Host": "localhost:9222"}), timeout=10).read())
    ws = re.sub(r"//(localhost|127\.0\.0\.1)(:\d+)?/", f"//{ip}:9222/", ver["webSocketDebuggerUrl"])
    with sync_playwright() as p:
        b = p.chromium.connect_over_cdp(ws)
        pg = b.new_context().new_page()
        pg.goto(url, wait_until="domcontentloaded", timeout=45000)
        try:
            pg.wait_for_load_state("networkidle", timeout=15000)
        except Exception:
            pass
        pg.wait_for_timeout(2000)
        html = pg.content()
        b.close()
    return html, DATA_LINK.findall(html)


def first_table(html: str, rows: int):
    import pandas as pd
    try:
        tables = pd.read_html(io.StringIO(html))
    except Exception:
        return None
    tables = [t for t in tables if t.shape[0] >= 2 and t.shape[1] >= 2]
    return tables[0].head(rows) if tables else None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source_id")
    ap.add_argument("--rows", type=int, default=10)
    ap.add_argument("--pdfs", type=int, default=0, help="download up to N linked PDFs")
    ap.add_argument("--api", help="fetch this endpoint and save the JSON")
    ap.add_argument("--render", action="store_true", help="use the headless browser instead of raw fetch")
    ap.add_argument("--url", help="override the source's primary URL")
    a = ap.parse_args()

    s = src(a.source_id)
    url = a.url or s["urls"][0]
    out = SAMPLES / a.source_id
    out.mkdir(parents=True, exist_ok=True)
    notes = [f"# sample: {s['name']}", "",
             f"- source id: `{a.source_id}` · access `{s['access']}`",
             f"- url: <{url}>", ""]
    got_table = got_api = None
    links: list[str] = []

    if a.api:
        j = json.loads(get(a.api))
        (out / "api.json").write_text(json.dumps(j, indent=2, ensure_ascii=False)[:200_000])
        import pandas as pd
        rec = j if isinstance(j, list) else next((v for v in (j.values() if isinstance(j, dict) else [])
                                                  if isinstance(v, list)), None)
        if rec:
            df = pd.json_normalize(rec).head(max(a.rows, 50))
            warehouse.register(f"{a.source_id}__sample", df, source_id=a.source_id, shape="json-api",
                               title=f"{s['name']} — API sample", origin_url=a.api.split("?")[0],
                               notes=f"first {len(df)} of {len(rec)} records")
            got_api = len(df)
        notes.append(f"**API** `{a.api.split('?')[0]}` → {'list of ' + str(len(rec)) if rec else 'non-list JSON'}; "
                     f"saved `api.json`" + (f", {got_api} rows → warehouse" if got_api else ""))

    elif url.lower().split("?")[0].endswith(".pdf") or a.pdfs:
        pass  # handled below

    if not a.api:
        if a.render:
            html, links = render(url)
            (out / "page.html").write_text(html[:2_000_000])
            notes.append(f"rendered in headless Chromium → `page.html` ({len(html):,} bytes)")
        else:
            raw = get(url)
            (out / "page.html").write_text(raw.decode("utf-8", "replace")[:2_000_000])
            html = raw.decode("utf-8", "replace")
            links = DATA_LINK.findall(html)
            notes.append(f"raw fetch → `page.html` ({len(raw):,} bytes)")

        tbl = first_table(html, a.rows)
        if tbl is not None:
            tbl.to_csv(out / "sample.csv", index=False)
            warehouse.register(f"{a.source_id}__sample", tbl, source_id=a.source_id, shape="html",
                               title=f"{s['name']} — table sample", origin_url=url,
                               notes=f"first {len(tbl)} rows of the first HTML table")
            got_table = len(tbl)
            notes.append(f"first HTML table: {got_table} rows × {tbl.shape[1]} cols → `sample.csv` + warehouse")

        if links:
            uniq = sorted(set(links))[:20]
            (out / "data_links.txt").write_text("\n".join(uniq))
            notes.append(f"{len(uniq)} data-file link(s) on the page → `data_links.txt`")
            for i, ln in enumerate([x for x in uniq if x.lower().endswith(".pdf")][: a.pdfs]):
                full = ln if ln.startswith("http") else re.sub(r"(https?://[^/]+).*", r"\1", url) + ln
                try:
                    download(full, out / f"doc_{i}.pdf", max_bytes=40_000_000)
                    notes.append(f"  downloaded `doc_{i}.pdf`  ({ln})")
                except Exception as e:  # noqa: BLE001
                    notes.append(f"  PDF {ln} failed: {e}")

    notes += ["", "## What a full parser needs", "",
              "- _TODO: describe the pagination / form / document structure a real ingester must handle_"]
    (out / "README.md").write_text("\n".join(notes) + "\n")
    print(f"samples/{a.source_id}/ — " +
          ", ".join(x for x in (f"{got_table} table rows" if got_table else "",
                                f"{got_api} api rows" if got_api else "",
                                f"{len(links)} links" if links else "", "page.html") if x))


if __name__ == "__main__":
    main()
