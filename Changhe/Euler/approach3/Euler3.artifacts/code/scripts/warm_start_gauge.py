#!/usr/bin/env python
"""Warm-start dilation-gauge check (lead d128 DU rule, 2026-10-26T07:37:10Z): before launching a warm start across a parameter change, evaluate the
start state's coefficients at the TARGET (c_l, omega) with the worker's own model and tail_norm2 and report ||F|| - 1 (the dilation gauge is
int_S2 |F|^2 = 1; the twisted-potential construction of F carries omega/c_l and alpha factors, so the gauge is not preserved across the jump).
Rule: abs(||F|| - 1) > 0.05 -> do not launch (record 'not launched under the registered warm-start gauge rule'); 0.02-0.05 -> launch and record the
value and the gauge block (0.5 (gauge_weight (||F|| - 1))^2) in the arm reading; below 0.02 -> launch. CPU, about 20-60 s per target at L6.
Usage: CUDA_VISIBLE_DEVICES=-1 OMP_NUM_THREADS=4 .venv/bin/python scripts/warm_start_gauge.py <start .pt> --c_l 0.44 [--omega 0.3] [--json out.json]
       (several targets: --c_l 0.42,0.44 --omega 0.3,0.5 evaluates every pair)"""
import sys, os, json, math, argparse
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "scripts"))
import torch
torch.set_default_dtype(torch.float64)
ap = argparse.ArgumentParser(); ap.add_argument("start"); ap.add_argument("--c_l", default=None); ap.add_argument("--omega", default=None); ap.add_argument("--json", default=None)
a = ap.parse_args()
import importlib.util
spec = importlib.util.spec_from_file_location("worker", os.path.join(ROOT, "scripts", "worker.py")); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W)
S = torch.load(a.start, map_location="cpu", weights_only=False); cfg0 = dict(S["config"])
cls = [float(v) for v in a.c_l.split(",")] if a.c_l else [float(cfg0["c_l"])]
oms = [float(v) for v in a.omega.split(",")] if a.omega else [float(cfg0["omega"])]
out = dict(start=os.path.relpath(os.path.abspath(a.start), ROOT), source_c_l=cfg0["c_l"], source_omega=cfg0["omega"], rule="lead d128 DU: abs(||F||-1) > 0.05 do not launch; 0.02-0.05 launch and record", results=[])
for cl in cls:
    for om in oms:
        cfg = dict(cfg0); cfg["c_l"] = cl; cfg["omega"] = om
        for k in ("core_pin", "nonaxi_pin", "balance_lambda", "radial_lambda_w", "fsw", "efrac", "nu", "pin_c_l"): cfg.pop(k, None)
        cfg["closure_lambda"] = 0.0
        model, prob = W.build(cfg, "cpu")
        with torch.no_grad():
            aT, aS, _, _ = model.unpack(S["z"].clone())
            n2 = float(prob.tail_norm2(aT, aS, torch.tensor(cl), torch.tensor(om)))
        dev = math.sqrt(n2) - 1.0; gc = 0.5 * (prob.gauge_weight * dev) ** 2
        verdict = "launch" if abs(dev) <= 0.02 else ("launch and record" if abs(dev) <= 0.05 else "DO NOT LAUNCH (gauge)")
        out["results"].append(dict(c_l=cl, omega=om, omega_over_c_l=om / cl, F_norm2=n2, F_norm_minus_1=dev, gauge_row_cost=gc, gauge_weight=prob.gauge_weight, verdict=verdict))
        print(f"{out['start']} at c_l {cl}, omega {om} (omega/c_l {om/cl:.4f}): ||F||^2 {n2:.6f}, ||F|| - 1 = {dev:+.4f}, gauge-row cost {gc:.4e} -> {verdict}", flush=True)
if a.json:
    json.dump(out, open(a.json, "w"), indent=1); print("wrote", a.json)
