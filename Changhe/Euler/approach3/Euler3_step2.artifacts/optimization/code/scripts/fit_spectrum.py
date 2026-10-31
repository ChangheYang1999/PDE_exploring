#!/usr/bin/env python
"""Singular-value spectrum of the (weighted, column-scaled) transfer-fit matrix and the fit residual against the truncation rcond, for the
verifier's exported field. Usage: fit_spectrum.py <export_dir> L Nk Nr [--NkE 4] [--no-tc]"""
import sys, os, json, argparse, math, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
DT = torch.float64
from src.equations.fields import Model, alpha_of
from src.optimization.tail_constraints import TailConstraints
from src.optimization.lm import jacobian_fwd
ap = argparse.ArgumentParser(); ap.add_argument("export_dir"); ap.add_argument("L", type=int); ap.add_argument("Nk", type=int); ap.add_argument("Nr", type=int)
ap.add_argument("--NkB", type=int, default=4); ap.add_argument("--NkD", type=int, default=4); ap.add_argument("--NkE", type=int, default=4); ap.add_argument("--no-tc", action="store_true")
ap.add_argument("--device", default="cuda:0")
a = ap.parse_args(); dev = a.device
sys.argv = [sys.argv[0]]
meta = json.load(open(os.path.join(a.export_dir, "meta.json"))); c_l = meta["c_l"]; omega = meta["omega"]; R0 = meta["R0"]; alpha = alpha_of(c_l)
S = np.load(os.path.join(a.export_dir, "samples.npz"))
# their field at our grid points via their BASIS (same code path as eval_transfer: re-use its functions by exec of the relevant part is heavy;
# use their U_grid samples instead: fit on THEIR tensor grid (radii x theta x phi), which is a legitimate target set)
y = torch.tensor(S["y_grid"].reshape(-1, 3), dtype=DT, device=dev); U = torch.tensor(S["U_grid"].reshape(-1, 3), dtype=DT, device=dev)
sel = torch.arange(0, len(y), 37, device=dev)                 # subsample for speed (about 5800 points)
y = y[sel]; U = U[sel]
model = Model(L=a.L, Nk=a.Nk, m_parity="even", R0=R0, Nr=a.Nr, device=dev, c_l=c_l, omega=omega, channels=dict(NkB=a.NkB, NkD=a.NkD, NkE=a.NkE))
tc = None if a.no_tc else TailConstraints(model)
n = model.n_coef if tc is None else tc.n_red
def field_flat(zc):
    z = tc.expand(zc) if tc is not None else zc
    return model.fields_points(z, y, need_vort=False)["U"].T.reshape(-1)
t0 = time.time(); J = jacobian_fwd(field_flat, torch.zeros(n, dtype=DT, device=dev), chunk=48)
w = ((1 + (y ** 2).sum(-1) / R0 ** 2) ** alpha).sqrt()[:, None].expand(-1, 3).reshape(-1)
Jw = J * w[:, None]; bw = U.reshape(-1) * w
cs = Jw.norm(dim=0); nz = cs > 0
print(f"L {a.L} Nk {a.Nk} channels B{a.NkB}/D{a.NkD}/E{a.NkE} tc {tc is not None}: {J.shape[0]} rows, {n} columns, {int((~nz).sum())} exactly zero columns; Jacobian {time.time()-t0:.1f}s")
Js = Jw[:, nz] / cs[nz][None, :]
Uq, sv, Vh = torch.linalg.svd(Js.cpu(), full_matrices=False)
print("singular values (scaled columns): max %.3e; quantiles 10%% %.3e 50%% %.3e 90%% %.3e; smallest 8: %s" % (sv[0], sv[int(0.1*len(sv))], sv[len(sv)//2], sv[int(0.9*len(sv))], " ".join(f"{v:.1e}" for v in sv[-8:])))
b = bw.cpu(); c = Uq.T @ b
for rc in (1e-6, 1e-8, 1e-10, 1e-12, 1e-14, 0.0):
    keep = sv >= rc * sv[0]
    r = b - Uq[:, keep] @ c[keep]
    print(f"  rcond {rc:.0e}: rank {int(keep.sum())} / {len(sv)}, relative fit residual {float(r.norm() / b.norm()):.3e}")
