#!/usr/bin/env python
"""Gate G1 T09 (aliasing) for the ranking diagnostics: holdout SPEC diagnostics on the standard holdout grid and on a holdout grid with 1.5x
the angular resolution (same Gauss radii), plus 2x the radial Gauss points per shell. Reports the relative change of rho_u^max, rho_nl^max,
sigma_u^max, a_max and the worst per-shell rho_u change. Usage: t09_aliasing.py <start.pt> [--device cuda:0] [--json out]"""
import sys, os, json, argparse, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.validation.spec_diagnostics import spec_diagnostics
from src.validation.holdout import HoldoutGrid
ap = argparse.ArgumentParser(); ap.add_argument("zfile"); ap.add_argument("--device", default="cuda:0" if torch.cuda.is_available() else "cpu"); ap.add_argument("--json", default=None)
a = ap.parse_args()
S = torch.load(a.zfile, map_location="cpu", weights_only=False); cfg = S["config"]; z = S["z"].to(a.device)
model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"],
              free_params=S.get("free_params", False), channels=cfg.get("channels"), device=a.device)
prob = Problem(model, formulation="mom")
Lx = getattr(model, "L_ext", model.L)
t0 = time.time()
hg0 = HoldoutGrid(model, r_core=model.R0)
hg1 = HoldoutGrid(model, r_core=model.R0, ntheta=int(round(1.5 * (2 * Lx + 12))), nphi=int(round(1.5 * (4 * Lx + 18))))
hg2 = HoldoutGrid(model, r_core=model.R0, n_per_shell=12)
d0 = spec_diagnostics(prob, z, holdout=hg0, extras=False); d1 = spec_diagnostics(prob, z, holdout=hg1, extras=False); d2 = spec_diagnostics(prob, z, holdout=hg2, extras=False)
def rel(x, y):
    return abs(x - y) / max(abs(x), 1e-300)
out = dict(zfile=a.zfile, L=model.L, L_ext=Lx, grids=dict(standard=(hg0.model.ntheta, hg0.model.nphi, 6), angular_x1_5=(hg1.model.ntheta, hg1.model.nphi, 6), radial_x2=(hg2.model.ntheta, hg2.model.nphi, 12)))
for name, d in (("angular_x1_5", d1), ("radial_x2", d2)):
    g0, g = d0["global_"], d["global_"]
    res = {k: rel(g0[k], g[k]) for k in ("rho_u_max", "rho_nl_max", "sigma_u_max", "a_max", "rho_lin_max", "rho_Om_max")}
    res["worst_shell_rho_u"] = max(rel(x, y) for x, y in zip(d0["rho_u"], d["rho_u"]) if x is not None and y is not None)
    res["values"] = {k: (g0[k], g[k]) for k in ("rho_u_max", "rho_nl_max", "sigma_u_max", "a_max")}
    out[name] = res
    print(f"[{name}] relative changes: " + ", ".join(f"{k} {v:.2e}" for k, v in res.items() if k != "values") + f"; rho_u_max {g0['rho_u_max']:.5f} -> {g['rho_u_max']:.5f}")
print(f"done in {time.time()-t0:.0f}s")
if a.json:
    json.dump(out, open(a.json, "w"), indent=1, default=str)
