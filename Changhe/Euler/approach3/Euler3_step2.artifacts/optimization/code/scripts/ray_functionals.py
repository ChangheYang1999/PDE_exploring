#!/usr/bin/env python
"""SPEC v1.22 tau_F and delta_G of a saved state (lead 03:21Z item 5). Usage: ray_functionals.py <start.pt> [--device cuda:0] [--json out] [--per_octave 16]"""
import sys, os, json, argparse, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.far_field.ray_functional import ray_functionals
ap = argparse.ArgumentParser(); ap.add_argument("zfile"); ap.add_argument("--device", default="cuda:0" if torch.cuda.is_available() else "cpu"); ap.add_argument("--json", default=None)
ap.add_argument("--per_octave", type=int, default=16)
a = ap.parse_args()
S = torch.load(a.zfile, map_location="cpu", weights_only=False); cfg = S["config"]; z = S["z"].to(a.device)
model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"],
              free_params=S.get("free_params", False), channels=cfg.get("channels"), device=a.device)
prob = Problem(model, formulation="mom")
ys = None; ae = None
crit = S.get("critical") or {}
if crit.get("local_maxima"):
    ys = crit["local_maxima"][0].get("y"); ae = None
t0 = time.time()
out = ray_functionals(prob, z, n_per_octave=a.per_octave)
out2 = ray_functionals(prob, z, n_per_octave=max(4, a.per_octave // 2))
out["quadrature_error_tau_F"] = {k: abs(out["tau_F"][k] - out2["tau_F"].get(k, out["tau_F"][k])) for k in out["tau_F"]}
print(f"tau_F(R) = {out['tau_F']} (||F_U|| from the tail {out['F_norm_from_tail']:.4f}); half-resolution differences {out['quadrature_error_tau_F']}")
print(f"self-check F^(R)[L U] vs R^alpha U(R) (relative): {out['selfcheck_FR_LU_vs_RalphaU']}; G[L U] = U relative error {out['G_identity_rel']:.2e}")
print(f"delta_G: core ball {out['delta_G_core_ball']:.3f}, max over shells {out['delta_G_max']:.3f}; per shell: " + " ".join(f"{v:.2f}" if v is not None else "n/a" for v in out['delta_G_shells']['delta_G']))
print(f"done in {time.time()-t0:.0f}s")
if a.json:
    json.dump(out, open(a.json, "w"), indent=1, default=str)
