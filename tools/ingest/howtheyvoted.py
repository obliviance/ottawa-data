#!/usr/bin/env python3
"""Ingest the howtheyvoted.ca compiled Ottawa council voting record (JSON) into the
warehouse as flat tables: councillors, meetings, motions, votes.

    python3 tools/ingest/howtheyvoted.py            # all dates in the index
    python3 tools/ingest/howtheyvoted.py --since 2026-01-01
    python3 tools/ingest/howtheyvoted.py --limit 20

Source: https://howtheyvoted.ca/data/ottawa/index.json  (independent; site terms, not
open data — a secondary source for the "recorded votes aren't published as data" gap).
"""
from __future__ import annotations

import argparse
import pathlib
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
import warehouse  # noqa: E402
from _http import get_json  # noqa: E402

BASE = "https://howtheyvoted.ca/data/ottawa"
ORIGIN = "https://howtheyvoted.ca/"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since", default="", help="only dates >= YYYY-MM-DD")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--delay", type=float, default=0.6)
    a = ap.parse_args()
    import pandas as pd

    idx = get_json(f"{BASE}/index.json")
    warehouse.register("htv_councillors", pd.DataFrame(idx["councillors"]),
                       source_id="howtheyvoted", shape="json-api",
                       title="howtheyvoted — councillors", origin_url=ORIGIN)

    dates = sorted(d for d in idx["dates"] if d >= a.since)
    dates = dates[-a.limit:] if a.limit else dates
    print(f"{len(dates)} meeting-dates ({dates[0]} … {dates[-1]})\n")

    meetings, motions, votes, attendance = [], [], [], []
    for i, date in enumerate(dates, 1):
        try:
            day = get_json(f"{BASE}/dates/{date}.json")
        except Exception as e:  # noqa: BLE001
            print(f"  [{i}/{len(dates)}] {date}  FAIL {e}")
            continue
        for m in day.get("meetings", []):
            mid = m["meeting_id"]
            meetings.append({k: m.get(k) for k in
                             ("meeting_id", "meeting_name", "meeting_number", "meeting_date",
                              "start_time", "location", "source_url")})
            for att in m.get("attendance", []):
                attendance.append({"meeting_id": mid, **att})
            for item in m.get("agenda_items", []):
                for mo in item.get("motions", []):
                    motions.append({
                        "meeting_id": mid, "meeting_name": m.get("meeting_name"),
                        "meeting_date": m.get("meeting_date"),
                        "agenda_item_number": item.get("agenda_item_number"),
                        "agenda_item_title": item.get("title"),
                        **{k: mo.get(k) for k in
                           ("motion_id", "motion_number", "motion_text", "motion_moved_by",
                            "motion_seconded_by", "motion_result", "for_count", "against_count",
                            "vote_kind", "summary")}})
                    for v in mo.get("votes", []):
                        votes.append({"motion_id": mo["motion_id"], "meeting_id": mid,
                                      "meeting_date": m.get("meeting_date"), **v})
        if i % 25 == 0:
            print(f"  [{i}/{len(dates)}] {date}")
        time.sleep(a.delay)

    for name, rows in (("meetings", meetings), ("motions", motions),
                       ("votes", votes), ("attendance", attendance)):
        warehouse.register(f"htv_{name}", pd.DataFrame(rows), source_id="howtheyvoted",
                           shape="json-api", title=f"howtheyvoted — {name}", origin_url=ORIGIN)
    print(f"\n{len(meetings)} meetings · {len(motions)} motions · {len(votes)} councillor-votes")


if __name__ == "__main__":
    main()
