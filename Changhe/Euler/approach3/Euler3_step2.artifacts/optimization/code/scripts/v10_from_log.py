#!/usr/bin/env python
"""V10 stationarity (SPEC 11c v1.18) from a worker log: relative decrease of the LM cost over the last tenth of the logged iterations of the
last start. Usage: v10_from_log.py <run_dir> [...]"""
import sys, os, re
for rd in sys.argv[1:]:
    lines = open(os.path.join(rd, "worker.log")).read().splitlines()
    costs = []
    for ln in lines:
        m = re.search(r"LM it\s+(\d+) cost ([0-9.e+-]+)", ln)
        if m:
            it, c = int(m.group(1)), float(m.group(2))
            if it == 0: costs = []
            costs.append((it, c))
    if len(costs) < 3:
        print(f"{os.path.basename(rd)}: no LM history"); continue
    N = costs[-1][0]; target = N - max(1, N // 10)
    c_last = costs[-1][1]; c_tenth = min(costs, key=lambda t: abs(t[0] - target))
    dec = (c_tenth[1] - c_last) / abs(c_tenth[1])
    print(f"{os.path.basename(rd)}: iterations {N}, cost {c_tenth[1]:.4e} (it {c_tenth[0]}) -> {c_last:.4e} (it {N}): relative decrease over the last tenth {dec:.3e} -> {'GN-stationary' if dec <= 1e-3 else 'NOT stationary'} (threshold 1e-3)")
