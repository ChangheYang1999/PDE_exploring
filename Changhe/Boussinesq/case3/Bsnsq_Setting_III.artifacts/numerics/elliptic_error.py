"""elliptic_error.py -- separate numerical elliptic-inversion error E = -Lap Psi - Omega of this lane's modal whole-plane inverse
(fixedsrc.cross_inverse: Psi_k(r), Psi_k'(r) of the sine modes k = 1..K at arbitrary radii, same quadrature as the solver), evaluated
WITHOUT using the modal ODE for Psi_k'': Psi_k'' is obtained by central finite differences of Psi_k' at r (1 +- h) and r (1 +- 2h) (Richardson
combination; the difference of the two estimates is the FD truncation estimate), and
    E_k(r) = -(Psi_k'' + Psi_k'/r - k^2 Psi_k / r^2) - Omega_k(r),   N_k(r) = |Psi_k''| + |Psi_k'/r| + k^2 |Psi_k| / r^2 + |Omega_k|.
Prints max over (k, r) of |E_k| / N_k, the absolute maxima by radial band, and the FD truncation estimate, on log-spaced radii (off the knots).
This measures the quadrature error of the Green formula for the REPRESENTED vorticity x G (the trial source); the Cartesian E(x, y) is
sum_k E_k(r) sin(k phi), so sum_k |E_k| bounds |E| at radius r.  Usage: python3 code/elliptic_error.py state.npz [--rmin 1e-3 --rmax 1e7 --nr 61 --h 1e-3]"""
import sys, os, argparse, json, numpy as np, torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bq3core import Basis, Geometry, DT
from fixedsrc import cross_inverse, omega_modes_at
torch.set_default_dtype(DT)
ap = argparse.ArgumentParser(); ap.add_argument('state'); ap.add_argument('--rmin', type=float, default=1e-3); ap.add_argument('--rmax', type=float, default=1e7)
ap.add_argument('--nr', type=int, default=61); ap.add_argument('--h', type=float, default=1e-3); ap.add_argument('--json', type=str, default='')
a = ap.parse_args(); dev = 'cuda'
d = np.load(a.state)
b = Basis(int(d['Nt']), int(d['deg']), int(d['K']), int(d['Nphi']), ng_coll=int(d['ngc']), m_reg=int(d['mreg']), device=dev, grade=float(d['grade']))
g = Geometry(b, float(d['beta_basis']), float(d['L']), rmap=str(d['rmap']))
cG = torch.tensor(d['cG'], dtype=DT, device=dev); K = b.K
r = torch.tensor(np.logspace(np.log10(a.rmin), np.log10(a.rmax), a.nr) * 1.0137, dtype=DT, device=dev)   # irrational-ish factor: off the knots
h = a.h
fac = torch.tensor([1 - 2 * h, 1 - h, 1.0, 1 + h, 1 + 2 * h], dtype=DT, device=dev)
r_all = (r[None, :] * fac[:, None]).reshape(-1)
Psi, dPsi = cross_inverse(g, cG, r_all)
Psi = Psi.reshape(K, 5, -1); dPsi = dPsi.reshape(K, 5, -1)
d2_h = (dPsi[:, 3] - dPsi[:, 1]) / (2 * h * r[None, :]); d2_2h = (dPsi[:, 4] - dPsi[:, 0]) / (4 * h * r[None, :])
d2 = (4 * d2_h - d2_2h) / 3; trunc = (d2_h - d2_2h).abs() / 3
Om = omega_modes_at(g, cG, g.t_of_r(r), r)                                   # (K, nr)
k = torch.arange(1, K + 1, dtype=DT, device=dev)[:, None]
P0, P1 = Psi[:, 2], dPsi[:, 2]
E = -(d2 + P1 / r[None, :] - k ** 2 * P0 / r[None, :] ** 2) - Om
N = d2.abs() + (P1 / r[None, :]).abs() + (k ** 2 * P0 / r[None, :] ** 2).abs() + Om.abs()
ratio = (E.abs() / N).cpu().numpy(); Ea = E.abs().cpu().numpy(); Na = N.cpu().numpy(); Tr = (trunc / N).cpu().numpy(); rn = r.cpu().numpy()
print(f"# {os.path.basename(a.state)}: K {K} Nt {b.Nt} beta_basis {float(d['beta_basis']):.6f}; {a.nr} radii in [{a.rmin:g}, {a.rmax:g}] x 1.0137; FD step h = {h:g} (Richardson from h, 2h)")
print(f"# max_(k,r) |E_k|/N_k = {ratio.max():.3e} at k = {int(ratio.argmax() // a.nr) + 1}, r = {rn[int(ratio.argmax() % a.nr)]:.3e}; max FD truncation estimate / N = {Tr.max():.3e}")
print(f"# max_(k,r) |E_k| = {Ea.max():.3e} (N there {Na.flatten()[Ea.argmax()]:.3e}); sum_k |E_k| max over r = {Ea.sum(0).max():.3e} at r = {rn[int(Ea.sum(0).argmax())]:.3e}")
bands = [(1e-3, 1e-1), (1e-1, 3), (3, 30), (30, 300), (300, 1e4), (1e4, 1e7)]
rows = []
print("# band                 max ratio   max |E_k|   max sum_k|E_k|   max sum_k|Omega_k|   FD trunc/N")
for lo, hi in bands:
    sel = (rn >= lo) & (rn < hi * 1.0137)
    if not sel.any(): continue
    rows.append(dict(lo=lo, hi=hi, max_ratio=float(ratio[:, sel].max()), max_absE=float(Ea[:, sel].max()), max_sumE=float(Ea[:, sel].sum(0).max()), max_sumOm=float(Om.abs().cpu().numpy()[:, sel].sum(0).max()), max_trunc=float(Tr[:, sel].max())))
    print(f"  [{lo:.0e}, {hi:.0e})   {rows[-1]['max_ratio']:.3e}   {rows[-1]['max_absE']:.3e}   {rows[-1]['max_sumE']:.3e}        {rows[-1]['max_sumOm']:.3e}            {rows[-1]['max_trunc']:.3e}")
if a.json: json.dump(dict(state=a.state, K=K, Nt=b.Nt, h=h, max_ratio=float(ratio.max()), max_trunc=float(Tr.max()), bands=rows), open(a.json, 'w'), indent=1)
