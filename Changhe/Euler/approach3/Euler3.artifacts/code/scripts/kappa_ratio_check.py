#!/usr/bin/env python
"""kappa(R) remainder check (lead d128 BN item 3, 2026-10-26T03:10Z; numerics account WORKLOG 02:38Z): for a finished job's arm reading
(reports/arm_reading_<job>.json, written by arm_reading.py --json) take the finite-radius energy-coefficient estimates kappa at the three far
radii 2^12, 2^14, 2^16 R0, subtract the direct coefficient ratio K_E = K_carried / K_required, and compare the successive ratios of the
deviations with the rate 4^(-(2 - alpha)) predicted for the first unconstrained correction (rate alpha + 3 content), alpha = (1 - c_l)/c_l.
This is a primary-reported consistency check of one rate on three radii: it fixes one amplitude and tests one rate with two ratios and does
not exclude other finite-radius contributions (verifier 02:34Z, 02:46Z, 02:53Z: endpoint residues, an oscillating quadrupole term r^(2 alpha - 3),
third-order terms r^(alpha - 2), subtraction errors). Usage: kappa_ratio_check.py <job_id> [...]"""
import sys, os, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
for job in sys.argv[1:]:
    p = os.path.join(ROOT, "reports", f"arm_reading_{job}.json")
    if not os.path.exists(p):
        print(f"## {job}: no arm reading at {p}"); continue
    d = json.load(open(p)); row = d["row"]
    c_l = float(row["c_l"]); alpha = (1.0 - c_l) / c_l; rate = 4.0 ** (-(2.0 - alpha))
    K = row.get("K_ratio_direct"); kap = row.get("kappa_far_finite_radius") or {}
    keys = sorted(kap.keys(), key=lambda s: int(s.split("^")[1]))
    print(f"## {job}: c_l {c_l}, omega {row.get('omega')}, omega/c_l {float(row.get('omega'))/c_l:.4f}, alpha {alpha:.6f}, 2 - alpha {2-alpha:.6f}, predicted ratio 4^(-(2-alpha)) = {rate:.4f}")
    if K is None or len(keys) < 3:
        print("   K_E ratio or kappa values missing; no check"); continue
    print(f"   direct K_E ratio {K:.6f}; kappa: " + ", ".join(f"{k} R0: {kap[k]:+.4f}" for k in keys))
    dev = [kap[k] - K for k in keys]
    print("   deviations kappa - K_E: " + ", ".join(f"{x:+.4f}" for x in dev))
    for i in range(1, len(dev)):
        r = dev[i] / dev[i-1] if dev[i-1] != 0 else float("nan")
        print(f"   ratio dev({keys[i]}) / dev({keys[i-1]}) = {r:+.4f} (predicted {rate:.4f}; relative difference {(r-rate)/rate:+.3f})")
    # extrapolation of the next two radii under the single-rate model (a consistency statement, not a measurement)
    if dev[-1] != 0:
        print(f"   single-rate extrapolation (not a measurement): kappa at 2^18 R0 {K + dev[-1]*rate:+.4f}, at 2^20 R0 {K + dev[-1]*rate*rate:+.4f}")
