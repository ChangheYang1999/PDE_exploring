#!/usr/bin/env python
"""Deliverable B (PROMPT 11.B): parameter evolution of a FREE lineage from the worker logs of its segments: accepted iteration (cumulative), O1, rms, c_l, omega,
omega/c_l, |gD|/|r| (the complete-gradient ratio printed by the worker). Writes a CSV and prints a summary (initial, final, min, max of c_l and omega, the total
fall of O1). Reading only. Usage: python scripts/param_evolution.py <lineage name> <run dir> [<run dir> ...]  (segments in order) -> validation/param_evolution_<lineage>.csv"""
import sys, os, re, csv
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
name = sys.argv[1]; runs = sys.argv[2:]
pat = re.compile(r"^(\S+Z)\s+LM it\s+(\d+)\s+cost\s+([0-9.eE+-]+)\s+rms\s+([0-9.eE+-]+)\s+lam\s+([0-9.eE+-]+)\s+\|gD\|/\|r\|\s+([0-9.eE+-]+)\s+acc\((\d+) trials\).*?c_l\s+([0-9.]+)\s+omega\s+([0-9.]+)")
rows = []
for run in runs:
    seg_it0 = None
    for line in open(os.path.join(run, "worker.log")):
        m0 = re.search(r"resuming at iteration (\d+)", line)
        if m0:
            seg_it0 = int(m0.group(1))
        m = pat.match(line)
        if m:
            it_seg = int(m.group(2)); it_cum = (seg_it0 or 0) + it_seg + 1 if seg_it0 is not None else it_seg + 1
            c_l = float(m.group(8)); om = float(m.group(9))
            rows.append(dict(segment=os.path.basename(run), ts=m.group(1), it_cum=it_cum, it_segment=it_seg, O1=float(m.group(3)), rms=float(m.group(4)), lam=float(m.group(5)), gD_over_r=float(m.group(6)), trials=int(m.group(7)), c_l=c_l, omega=om, omega_over_cl=om / c_l))
out = os.path.join(ROOT, "validation", f"param_evolution_{name}.csv")
with open(out, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
cl = [r["c_l"] for r in rows]; om = [r["omega"] for r in rows]
print(f"{name}: {len(rows)} accepted iterations over {len(runs)} segment(s); O1 {rows[0]['O1']:.6e} -> {rows[-1]['O1']:.6e} ({(1 - rows[-1]['O1'] / rows[0]['O1']) * 100:.1f} per cent lower); c_l {cl[0]:.6f} -> {cl[-1]:.6f} (min {min(cl):.6f}, max {max(cl):.6f}); omega {om[0]:.6f} -> {om[-1]:.6f} (min {min(om):.6f}, max {max(om):.6f}); omega/c_l {rows[0]['omega_over_cl']:.4f} -> {rows[-1]['omega_over_cl']:.4f}; |gD|/|r| last {rows[-1]['gD_over_r']:.2e}; written {out}")
