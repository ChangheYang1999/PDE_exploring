#!/usr/bin/env python
"""Odd-azimuthal-mode content of a saved all-m state (CPU). Zeroes the even-m coefficients of every channel (A, C, B, D, E) and evaluates
the odd-m part of the field on the training grid (far anchor radii excluded): RMS ratios ||U_odd|| / ||U||, ||Omega_odd|| / ||Omega||,
||DU_odd|| / ||DU|| over all grid points and by radius bin ([0, 0.125), [0.125, 0.5), [0.5, 2), [2, 8), >= 8 in y units), the energy
fractions ||U_odd||^2 / ||U||^2 (all, r < 0.125, r >= 8) and the odd coefficient-norm fraction ||z_odd|| / ||z||. The RAY by |m| worker line
prints ENERGY fractions at two decimals, so an order-0.1 amplitude admixture prints as 0.00 there; this script gives both amplitude and
energy. Plain (unweighted) RMS over the product grid, as in the WORKLOG 2026-10-26T11:26Z and 14:28Z readings. Usage:
  CUDA_VISIBLE_DEVICES=-1 OMP_NUM_THREADS=4 .venv/bin/python scripts/odd_m_fraction.py <start.pt> [--json out.json]"""
import sys, os, json, argparse, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
ap = argparse.ArgumentParser(); ap.add_argument("start"); ap.add_argument("--json", default=None)
a = ap.parse_args()
st = torch.load(a.start, map_location="cpu", weights_only=False)
cfg = st["config"]; z = st["z"].detach().clone().double()
model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"],
              free_params=cfg.get("free_params", False), device="cpu", channels=cfg.get("channels"), extra_r=None)
assert model.n_z == z.numel(), (model.n_z, z.numel())
d = model.unpack_all(z)
odd = (model.m_arr % 2 == 1)
extra = {}
for name, n in model.layout:
    arr = d[name].clone(); arr[:, ~odd] = 0.0
    if name in ("A", "C"): d[name + "_odd"] = arr
    else: extra[name] = arr
z_odd = model.pack(d["A_odd"], d["C_odd"], d["c_l"], d["omega"], extra=extra)
with torch.no_grad():
    f = model.fields_grid(z); fo = model.fields_grid(z_odd)
r = torch.sqrt((model.y ** 2).sum(-1))                       # (Nr, Na)
def rms(x, mask=None):
    x2 = (x ** 2).sum(0) if x.dim() == 3 else (x ** 2).sum((0, 1))   # (Nr, Na)
    if mask is not None: x2 = x2[mask]
    return float(torch.sqrt(x2.mean()))
out = dict(start=a.start, c_l=float(cfg["c_l"]), omega=float(cfg["omega"]), L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity"), n_modes=int(model.Nq), n_odd_modes=int(odd.sum()),
           coef_norm_fraction_odd=float(z_odd.norm() / z.norm()), grid=dict(Nr=int(r.shape[0]), Na=int(r.shape[1]), r_min=float(r.min()), r_max=float(r.max())))
out["ratio_all"] = dict(U=rms(fo["U"]) / rms(f["U"]), Omega=rms(fo["Om"]) / rms(f["Om"]), DU=rms(fo["GU"]) / rms(f["GU"]))
edges = [0.0, 0.125, 0.5, 2.0, 8.0, float("inf")]
out["ratio_by_radius"] = []
for lo, hi in zip(edges[:-1], edges[1:]):
    m = (r >= lo) & (r < hi)
    if int(m.sum()) == 0: continue
    out["ratio_by_radius"].append(dict(bin=[lo, hi], n=int(m.sum()), U=rms(fo["U"], m) / rms(f["U"], m), Omega=rms(fo["Om"], m) / rms(f["Om"], m), DU=rms(fo["GU"], m) / rms(f["GU"], m)))
def efrac(mask=None):
    e = (fo["U"] ** 2).sum(0); E = (f["U"] ** 2).sum(0)
    if mask is not None: e, E = e[mask], E[mask]
    return float(e.sum() / E.sum())
out["energy_fraction_odd"] = dict(all=efrac(), core_r_lt_0p125=efrac(r < 0.125), tail_r_ge_8=efrac(r >= 8.0))
print(f"odd-m content of {a.start} (c_l {out['c_l']}, omega {out['omega']}, L {out['L']}, Nk {out['Nk']}, {out['n_odd_modes']} odd of {out['n_modes']} modes; training grid Nr {out['grid']['Nr']} x Na {out['grid']['Na']}, r {out['grid']['r_min']:.3g} to {out['grid']['r_max']:.3g})")
print(f"  RMS ratios (odd part / full): ||U_odd||/||U|| {out['ratio_all']['U']:.3e}, ||Omega_odd||/||Omega|| {out['ratio_all']['Omega']:.3e}, ||DU_odd||/||DU|| {out['ratio_all']['DU']:.3e}")
for b in out["ratio_by_radius"]:
    print(f"  r in [{b['bin'][0]}, {b['bin'][1]}): n {b['n']}, U {b['U']:.3e}, Omega {b['Omega']:.3e}, DU {b['DU']:.3e}")
print(f"  energy fractions of the odd part: all {out['energy_fraction_odd']['all']:.3e}, core r < 0.125 {out['energy_fraction_odd']['core_r_lt_0p125']:.3e}, tail r >= 8 {out['energy_fraction_odd']['tail_r_ge_8']:.3e}; odd coefficient-norm fraction {out['coef_norm_fraction_odd']:.3f}")
if a.json:
    json.dump(out, open(a.json, "w"), indent=1); print("written", a.json)
