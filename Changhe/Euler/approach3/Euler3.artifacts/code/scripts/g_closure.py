#!/usr/bin/env python
"""Angular closure report (SPEC 4.4; lead 2026-10-24T22:40Z (a)): ||G[F]|| of a saved state's leading tail, dist(G[F], carried span)/||G[F]||
for the state's own B/D channel modes, and the same distance for the SPEC-degree span (B up to 2L+3, D up to 2L+2, even m up to 2 M_max) and
for a degree-L span (reference). Usage: g_closure.py <start.pt> [--device cuda:0] [--json out.json]"""
import sys, os, json, argparse, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.bases.solid_harmonics import mode_list
from src.far_field.correction import first_correction, closure_distance
ap = argparse.ArgumentParser(); ap.add_argument("zfile"); ap.add_argument("--device", default="cuda:0" if torch.cuda.is_available() else "cpu")
ap.add_argument("--json", default=None); ap.add_argument("--no-spec", action="store_true")
a = ap.parse_args()
S = torch.load(a.zfile, map_location="cpu", weights_only=False); cfg = S["config"]; z = S["z"].to(a.device)
model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"],
              free_params=S.get("free_params", False), channels=cfg.get("channels"), device=a.device)
prob = Problem(model, formulation="mom")
t0 = time.time()
fc = first_correction(prob, z)
out = dict(zfile=a.zfile, c_l=fc["c_l"], omega=fc["omega"], omega_over_c_l=fc["omega"] / fc["c_l"], alpha=fc["alpha"], F_norm=fc["F_norm"], G_norm=fc["G_norm"], N_norm=fc["N_norm"], gradQ_norm=fc["gradQ_norm"],
           source_resolution=fc["source_resolution"], grid=(fc["ntheta"], fc["nphi"]))
print(f"leading tail: ||F|| {fc['F_norm']:.6f}; ||G[F]|| {fc['G_norm']:.6f} (||N|| {fc['N_norm']:.6f}, ||grad Q|| {fc['gradQ_norm']:.6f}); source top-degree fraction {fc['source_resolution']:.1e}; {time.time()-t0:.1f}s")
own = closure_distance(prob, z, fc=fc)
out["own_channels"] = own
print(f"own channels (B degree {own.get('max_B_degree')}, D degree {own.get('max_D_degree')}, {own['n_columns']} columns, rank {own.get('rank')}): dist/||G|| = {own['dist_rel']:.3e}" + (f"; sigma min/max {own['sigma_min']:.2e}/{own['sigma_max']:.2e}" if own['n_columns'] else ""))
if own.get("carried_mismatch_rel") is not None:
    print(f"carried coefficient (the state's B/D asymptotic amplitudes): ||G_carried|| {own['G_carried_norm']:.4f}, ||G_req - G_carried||/||G_req|| = {own['carried_mismatch_rel']:.3f}, correlation {own['carried_correlation']:.3f} (exact profile: 0 and 1)")
if not a.no_spec:
    L = model.L; Mlead = max(m for (l, m, t) in mode_list(L, model.m_parity, 1))
    for tag, LB, LD in (("degree L", L, L), ("SPEC 2L+3 / 2L+2", 2 * L + 3, 2 * L + 2)):
        mB = [q for q in mode_list(LB, model.m_parity, 1) if q[1] <= max(2 * Mlead, Mlead)]
        mD = [q for q in mode_list(LD, model.m_parity, 1) if q[1] <= max(2 * Mlead, Mlead)]
        t1 = time.time()
        r = closure_distance(prob, z, modes_B=mB, modes_D=mD, fc=fc)
        out[tag] = r
        print(f"{tag}: B {len(mB)} + D {len(mD)} columns, rank {r.get('rank')}, dist/||G|| = {r['dist_rel']:.3e}, sigma min/max {r['sigma_min']:.2e}/{r['sigma_max']:.2e}, |coef| {r['coef_norm']:.3f}; {time.time()-t1:.1f}s")
if a.json:
    json.dump(out, open(a.json, "w"), indent=1, default=str); print("wrote", a.json)
