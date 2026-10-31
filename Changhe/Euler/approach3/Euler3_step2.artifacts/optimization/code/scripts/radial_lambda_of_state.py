#!/usr/bin/env python
"""S12 / R13 helper: the worker's RADIAL LAMBDA diagnostics (d93, training grid) for a saved state that predates the battery line (e.g. the nest6 starts of the
S12 arms): share of the weighted squared momentum residual along lambda(r) U, pointwise along-U share, lambda max and its radius, negative-pairing fraction,
octaves with lambda < 0 and lambda by octave of r/R0. Same objects as the worker (build, pivot, pressure, nonlinear weights refreshed at the state; pin, closure,
balance and S12 rows removed so that only the momentum residual enters). Primary-reported diagnostics, never acceptance criteria.
Usage: radial_lambda_of_state.py <start .pt> [--device cpu|cuda:0] [--json out.json]"""
import sys, os, json, argparse
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "scripts"))
import torch
torch.set_default_dtype(torch.float64)
ap = argparse.ArgumentParser(); ap.add_argument("start"); ap.add_argument("--device", default="cpu"); ap.add_argument("--json", default=None)
a = ap.parse_args()
import importlib.util
spec = importlib.util.spec_from_file_location("worker", os.path.join(ROOT, "scripts", "worker.py")); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W)
S = torch.load(a.start, map_location="cpu", weights_only=False)
cfg = dict(S["config"])
for k in ("core_pin", "nonaxi_pin", "balance_lambda", "radial_lambda_w", "fsw", "efrac", "nu", "pin_c_l"):
    cfg.pop(k, None)
cfg["closure_lambda"] = 0.0
model, prob = W.build(cfg, a.device)
z = S["z"].to(a.device)
prob.pivot = S.get("pivot") if S.get("pivot") is not None else prob.choose_pivot(z)
prob.maybe_rebuild_pressure(z); prob.update_nl_weights(z)
with torch.no_grad():
    rl = prob.radial_lambda_diagnostics(z)
out = dict(start=os.path.relpath(os.path.abspath(a.start), ROOT), c_l=cfg["c_l"], omega=cfg["omega"], L=cfg["L"], Nk=cfg["Nk"], device=a.device,
           radial_lambda_share=rl["radial_lambda_share"], pointwise_along_U_share=rl["pointwise_along_U_share"], lambda_max=rl["lambda_max"], r_at_lambda_max=rl["r_at_lambda_max"],
           negative_pairing_fraction=rl["negative_pairing_fraction"], n_octaves_negative=rl["n_octaves_negative"], lambda_by_octave={k: float(v) for k, v in rl["lambda_by_octave"].items()})
print(f"RADIAL LAMBDA (d93, training grid) of {out['start']} (c_l {cfg['c_l']}, omega {cfg['omega']}, L {cfg['L']} Nk {cfg['Nk']}): share {rl['radial_lambda_share']:.3f} "
      f"(pointwise along-U share {rl['pointwise_along_U_share']:.3f}); lambda max {rl['lambda_max']:.3f} at r {rl['r_at_lambda_max']:.3g}; negative-pairing fraction {rl['negative_pairing_fraction']:.2e}; "
      f"octaves with lambda < 0: {rl['n_octaves_negative']} of {len(rl['lambda_by_octave'])}; lambda by octave of r/R0: " + " ".join(f"{k}:{float(v):+.3f}" for k, v in rl["lambda_by_octave"].items()))
if a.json:
    json.dump(out, open(a.json, "w"), indent=1); print("wrote", a.json)
