#!/usr/bin/env python3
"""Build the decision timeline spine.

  spine_meetings  — every Council / committee / board meeting. Full history from the
                    eScribe calendar endpoint (2012→now); enriched where howtheyvoted
                    has processed the agenda.
  spine_motions   — one row per motion (from howtheyvoted, 2022→now): date, meeting,
                    agenda item, mover/seconder, result, for/against counts, summary.

Needs the howtheyvoted tables in the warehouse (tools/ingest/howtheyvoted.py).

    python3 spine/timeline.py
    python3 spine/timeline.py --calendar-from 2012-01
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys
import time
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent / "tools"))
import warehouse  # noqa: E402

CAL = "https://pub-ottawa.escribemeetings.com/MeetingsCalendarView.aspx/GetCalendarMeetings"


def calendar_month(year: int, month: int) -> list[dict]:
    start = dt.date(year, month, 1)
    end = (start.replace(day=28) + dt.timedelta(days=4)).replace(day=1) - dt.timedelta(days=1)
    body = json.dumps({"calendarStartDate": start.strftime("%Y/%m/%d"),
                       "calendarEndDate": end.strftime("%Y/%m/%d")}).encode()
    req = urllib.request.Request(CAL, data=body, method="POST",
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": "ottawa-data/0.1"})
    r = json.loads(urllib.request.urlopen(req, timeout=30).read())
    return r.get("d", r) or []


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--calendar-from", default="2018-01", help="YYYY-MM (default 2018-01; eScribe starts 2012-06)")
    ap.add_argument("--delay", type=float, default=0.4)
    a = ap.parse_args()
    import pandas as pd

    c = warehouse.con()
    have = {r[0] for r in c.execute("SELECT table_name FROM information_schema.tables").fetchall()}
    if "d_htv_motions" not in have:
        c.close()
        sys.exit("need htv_motions — run tools/ingest/howtheyvoted.py first")

    # --- spine_motions: straight from howtheyvoted, lightly cleaned ---
    motions = c.execute("""
        SELECT meeting_date::DATE                AS date,
               meeting_name, agenda_item_number, agenda_item_title,
               motion_id, motion_text, motion_moved_by, motion_seconded_by,
               nullif(motion_result,'')          AS result,
               for_count, against_count, vote_kind, summary
        FROM d_htv_motions
    """).df()
    warehouse.register("spine_motions", motions, shape="spine",
                       title="spine — council/committee motions (2022→)",
                       origin_url="https://howtheyvoted.ca/",
                       notes="from howtheyvoted; site terms, not open data")

    # --- spine_meetings: eScribe calendar history, enriched from howtheyvoted ---
    y0, m0 = map(int, a.calendar_from.split("-"))
    today = dt.date.today()
    seen, meetings = set(), []
    ym = (y0, m0)
    while (ym[0], ym[1]) <= (today.year, today.month):
        try:
            for mtg in calendar_month(*ym):
                mid = mtg.get("ID")
                if mid in seen:
                    continue
                seen.add(mid)
                meetings.append({
                    "meeting_id": mid,
                    "meeting_name": mtg.get("MeetingName"),
                    "start": mtg.get("StartDate"),
                    "location": (mtg.get("Location") or "").strip(),
                    "url": mtg.get("MeetingUrl") or mtg.get("AgendaUrl"),
                })
        except Exception as e:  # noqa: BLE001
            print(f"  {ym[0]}-{ym[1]:02d}  FAIL {e}")
        ym = (ym[0] + 1, 1) if ym[1] == 12 else (ym[0], ym[1] + 1)
        time.sleep(a.delay)

    mdf = pd.DataFrame(meetings)
    if not mdf.empty:
        mdf["start"] = pd.to_datetime(mdf["start"], errors="coerce")
        mdf["date"] = mdf["start"].dt.date
        htv = c.execute("SELECT DISTINCT meeting_id, TRUE AS in_howtheyvoted FROM d_htv_meetings").df()
        mdf = mdf.merge(htv, on="meeting_id", how="left")
        mdf["in_howtheyvoted"] = mdf["in_howtheyvoted"].fillna(False)
    warehouse.register("spine_meetings", mdf, shape="spine",
                       title="spine — meetings (eScribe calendar)",
                       origin_url="https://pub-ottawa.escribemeetings.com/",
                       notes="eScribe calendar; in_howtheyvoted flags meetings with a parsed agenda")
    c.close()
    print(f"\nspine_motions: {len(motions)} · spine_meetings: {len(mdf)} "
          f"({int(mdf['in_howtheyvoted'].sum()) if not mdf.empty else 0} with votes parsed)")
    print("next: spine/entities.py")


if __name__ == "__main__":
    main()
