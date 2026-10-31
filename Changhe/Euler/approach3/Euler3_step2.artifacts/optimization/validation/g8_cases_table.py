#!/usr/bin/env python
"""Markdown table of the G8 omitted-part sizes (lead 16:19:29Z item 4; information only) from validation/g8_controls_cases_gpu_v1_<case>.json and the
S01_own/manu_a record validation/g8_controls_gpu_v1_v4harness_0757Z.json: per case, control and parameter: the omitted part's norm relative to the column
norm, the minimum G1 error of the omitting copy over the ladder, whether G1 fails (the control is excited) and the largest per-group relative size.
Usage: python validation/g8_cases_table.py [--md]"""
import json, glob, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
files = sorted(glob.glob(os.path.join(ROOT, "validation", "g8_controls_cases_gpu_v1_*.json")))
base = os.path.join(ROOT, "validation", "g8_controls_gpu_v1_v4harness_0757Z.json")
rows = []
def add(d, src):
    for cname, ctr in d["controls"].items():
        for name, r in ctr.items():
            for p, v in r.items():
                opg = v.get("omitted_part_per_group") or {}
                big = max(((g, x.get("rel_to_column", 0.0)) for g, x in opg.items()), key=lambda t: t[1], default=(None, None))
                rows.append((cname, name, p, v["omitted_part_rel_norm"], v["min_error_all"], bool(v["fails_G1"]), big, os.path.basename(src)))
if os.path.exists(base):
    add(json.load(open(base)), base)
for f in files:
    add(json.load(open(f)), f)
print("| case | control | parameter | omitted part / column norm | min G1 error of the omitting copy | G1 fails (control excited) | largest per-group share (group) | record |")
print("|---|---|---|---|---|---|---|---|")
for c, n, p, om, me, fl, big, src in rows:
    print(f"| {c} | {n} | {p} | {om:.1e} | {me:.1e} | {'yes' if fl else 'no'} | {big[1]:.1e} ({big[0]}) | {src} |" if big[0] is not None else f"| {c} | {n} | {p} | {om:.1e} | {me:.1e} | {'yes' if fl else 'no'} | n/a | {src} |")
print(f"\n{len(rows)} rows from {len(files) + (1 if os.path.exists(base) else 0)} records; 'G1 fails' = the omitting copy's whole-column minimum error over the ladder exceeds 1e-4 (100 tau) OR some group's minimum error exceeds 1e-3 (the flag of g8_controls.py); where it does not fail the omitted part is small and its size is the reported limitation (lead 08:16Z item 3; information only).")
