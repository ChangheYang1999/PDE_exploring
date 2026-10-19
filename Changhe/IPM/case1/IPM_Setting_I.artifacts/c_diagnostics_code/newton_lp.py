"""Pseudo-transient continuation / Newton for the stationary profile on the log-polar grid (lead prototype).
Unknowns z = (phi[Nu, M], c_l); equations F_phi = phi - (c_l X + U).grad rho / wgt (= DR right-hand side, c_rho = 1),
F_c = 3 c_l - 1 - c[phi]. a(0) = 1 enters through the inflow data below u0 (rho = x^2 y). Far-field tail exponent k = 1/c_l.
Implicit pseudo-time step: (I/dtau - J) dz = F on the phi rows, -J dz = F on the c_l row; dense finite-difference Jacobian.
Usage: python3 newton_lp.py --Nu 201 --M 12 --out runs/nw_test
"""
import argparse, sys, time
import numpy as np
sys.path.insert(0, 'scripts')
from lp_core import LP

ap = argparse.ArgumentParser()
ap.add_argument('--k0', type=float, default=0.6)
ap.add_argument('--u0', type=float, default=-5.0)
ap.add_argument('--u1', type=float, default=7.0)
ap.add_argument('--Nu', type=int, default=201)
ap.add_argument('--M', type=int, default=12)
ap.add_argument('--Lscale', type=float, default=1.0)
ap.add_argument('--init', type=str, default='')
ap.add_argument('--dtau0', type=float, default=0.05)
ap.add_argument('--dtau_max', type=float, default=1e8)
ap.add_argument('--maxit', type=int, default=60)
ap.add_argument('--tol', type=float, default=1e-10)
ap.add_argument('--fdh', type=float, default=1e-7)
ap.add_argument('--out', type=str, required=True)
ap.add_argument('--fixcl', type=float, default=0.0, help='if > 0: c_l fixed, identity dropped (diagnostic F_c reported)')
a = ap.parse_args()

L = LP(a.u0, a.u1, a.Nu, a.M, a.k0)
Nu, M = a.Nu, a.M
r = L.r[:, None]; th = L.th[None, :]
if a.init:
    d = np.load(a.init)
    phi0 = d['phi']
    if phi0.shape != (Nu, M):  # interpolate in u (same theta grid required)
        from scipy.interpolate import CubicSpline
        assert phi0.shape[1] == M
        phi0 = CubicSpline(d['u'], phi0, axis=0)(np.clip(L.u, d['u'][0], d['u'][-1]))
    cl0 = float(d['cl'])
else:
    k0 = a.k0
    Lsq = 4 * (1 - k0) * (3 / k0 - 1) * a.Lscale ** 2
    phi0 = np.cos(th) ** 2 * np.sin(th) * ((1 + r ** 2 / Lsq) / (1 + r ** 2)) ** ((k0 - 3) / 2)
    cl0 = None


def F(z):
    phi = z[:-1].reshape(Nu, M)
    cl = z[-1] if a.fixcl <= 0 else a.fixcl
    k = min(max(1.0 / cl, 0.05), 0.98) if cl > 0 else 0.98
    A, B, c, psit = L.fields(phi, cl, k)
    glo, ghi = L.ghosts(phi, k)
    Fp = phi - L.transport(phi, A, B, glo, ghi)
    return np.concatenate([Fp.ravel(), [3 * cl - 1 - c]]), c, psit


def jac(z, F0):
    N = z.size
    J = np.zeros((N, N))
    if a.fixcl > 0:
        J[-1, -1] = 1.0
    for i in range(N if a.fixcl <= 0 else N - 1):
        zp = z.copy(); zp[i] += a.fdh
        J[:, i] = (F(zp)[0] - F0) / a.fdh
    if a.fixcl > 0:
        J[-1, :] = 0.0
        J[-1, -1] = 1.0
    return J


def axis(psit, cl):
    n = L.n[None, :]
    A0 = cl - np.sum(2 * n * psit, axis=1)
    i = np.where((A0[:-1] < 0) & (A0[1:] >= 0))[0]
    if len(i) == 0:
        return np.nan
    i = i[0]
    return float(np.exp(L.u[i] + (-A0[i] / (A0[i + 1] - A0[i])) * L.du))


z = np.concatenate([phi0.ravel(), [0.0]])
if cl0 is None:
    _, c0, _ = F(np.concatenate([phi0.ravel(), [1.5]]))
    cl0 = (1 + c0) / 3
if a.fixcl > 0:
    cl0 = a.fixcl
z[-1] = cl0
log = open(a.out + '.log', 'w')
def out(s):
    print(s, flush=True); log.write(s + '\n'); log.flush()
out(f"# newton_lp Nu={Nu} M={M} u=[{a.u0},{a.u1}] k0={a.k0} init={a.init or 'analytic'} dtau0={a.dtau0}")
dtau = a.dtau0
F0, c, psit = F(z)
nrm = np.max(np.abs(F0[:-1])) / np.max(np.abs(z[:-1]))
t0 = time.time()
for it in range(a.maxit):
    out(f"it={it:3d} cl={z[-1]:.8f} c={c:.8f} |Fphi|/|phi|={nrm:.3e} |Fc|={abs(F0[-1]):.2e} dtau={dtau:.2e} "
        f"x*={axis(psit, z[-1]):.4f} max|phi|={np.max(np.abs(z[:-1])):.4e} minphi={np.min(z[:-1]):.3e} wall={time.time()-t0:.0f}s")
    np.savez(a.out + '.npz', phi=z[:-1].reshape(Nu, M), cl=z[-1], u=L.u, th=L.th, k0=a.k0, c=c)
    if nrm < a.tol:
        break
    J = jac(z, F0)
    Mx = -J.copy()
    Mx[np.arange(Nu * M), np.arange(Nu * M)] += 1.0 / dtau
    rhs0 = F0.copy()
    if a.fixcl > 0:
        rhs0[-1] = 0.0
    dz = np.linalg.solve(Mx, rhs0)
    # damping: limit relative change
    lam = 1.0
    for _ in range(12):
        zn = z + lam * dz
        if zn[-1] > 0.5:
            Fn, cn, psn = F(zn)
            nn = np.max(np.abs(Fn[:-1])) / np.max(np.abs(zn[:-1]))
            if np.isfinite(nn) and nn < 1.5 * nrm + 1e-14:
                break
        lam *= 0.5
    z = zn; F0, c, psit = Fn, cn, psn
    ratio = nrm / max(nn, 1e-300)
    nrm = nn
    dtau = min(a.dtau_max, dtau * max(0.25, min(ratio, 10.0)) if lam == 1.0 else dtau * 0.5)
log.close()
