#!/usr/bin/env python
"""8.5 long-budget rule helper (lead 13:56:28Z item 4 (2), 16:19:29Z item 6): from a run's worker.log, the O1 fall over the LAST hour of the segment (and over the whole
segment) in per cent per hour, from the accepted-iteration lines 'YYYY-MM-DDTHH:MM:SSZ   LM it  N cost C ...'. Reading only. Usage: python scripts/segment_rate.py <run dir> [window_min=60]"""
import sys, re, datetime as dt
run = sys.argv[1]; win = float(sys.argv[2]) if len(sys.argv) > 2 else 60.0
pat = re.compile(r"^(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\s+LM it\s+(\d+)\s+cost\s+([0-9.eE+-]+)")
pts = []
for line in open(run.rstrip("/") + "/worker.log"):
    m = pat.match(line)
    if m:
        pts.append((dt.datetime.strptime(m.group(1), "%Y-%m-%dT%H:%M:%SZ"), int(m.group(2)), float(m.group(3))))
if len(pts) < 2:
    raise SystemExit("fewer than two accepted iterations in the log")
t_end, it_end, c_end = pts[-1]
first = pts[0]
cands = [p for p in pts if (t_end - p[0]).total_seconds() >= win * 60]
ref = cands[-1] if cands else first
hours = (t_end - ref[0]).total_seconds() / 3600
rate = (ref[2] - c_end) / ref[2] / hours * 100 if hours > 0 else float("nan")
hours_all = (t_end - first[0]).total_seconds() / 3600
rate_all = (first[2] - c_end) / first[2] / hours_all * 100 if hours_all > 0 else float("nan")
print(f"run {run}: last accepted {t_end:%Y-%m-%dT%H:%M:%SZ} it {it_end} cost {c_end:.6e}; reference for the last {win:.0f} min: {ref[0]:%H:%M:%SZ} it {ref[1]} cost {ref[2]:.6e} -> {rate:.2f} per cent per hour over {hours:.2f} h; whole segment (from {first[0]:%H:%M:%SZ} it {first[1]} cost {first[2]:.6e}): {rate_all:.2f} per cent per hour over {hours_all:.2f} h; 8.5 rule (> 1 per cent per hour over the last hour): {'MET' if rate > 1.0 else 'NOT MET'}")
