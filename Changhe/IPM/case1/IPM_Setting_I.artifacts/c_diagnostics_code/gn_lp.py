"""Levenberg-Marquardt on the stationary profile equations, log-polar grid (lead prototype, v2 formulation).

Differences from newton_lp.py:
 - inner boundary: the ghost values below u0 are NOT prescribed x^2 y data. They are the continuation of the solution
   through the saddle at 0 along the linear flow W = (l1 x, l2 y), l1 = c_l - c, l2 = c_l + c (W_1 is odd in x and even
   in y, so W = DW(0) X + O(r^3)): trace the ghost point backward until it exits the disc r = r0 = e^{u0} at angle th_e
   after time t_e; then rho(ghost) = rho(r0, th_e) e^{t_e}. This makes rho = 0 a solution, so the normalization is a
   separate equation;
 - unknowns z = (phi, c_l); residuals R = (F_phi, wc (3c_l - 1 - c), wn (a_est - 1)), a_est = projection of rho(r0, .)
   on x^2 y; LM with a dense finite-difference Jacobian. c_l is kept >= clmin (steps that go below are damped).
"""
import argparse, sys, time
import numpy as np
sys.path.insert(0, 'scripts')
from lp_core import LP

ap = argparse.ArgumentParser()
ap.add_argument('--k0', type=float, default=0.6)
ap.add_argument('--u0', type=float, default=-5.0)
ap.add_argument('--u1', type=float, default=8.0)
ap.add_argument('--Nu', type=int, default=217)
ap.add_argument('--M', type=int, default=12)
ap.add_argument('--Lscale', type=float, default=1.0)
ap.add_argument('--cl0', type=float, default=0.0, help='initial c_l (0: from the analytic guess)')
ap.add_argument('--init', type=str, default='')
ap.add_argument('--maxit', type=int, default=40)
ap.add_argument('--tol', type=float, default=1e-10)
ap.add_argument('--fdh', type=float, default=1e-7)
ap.add_argument('--wc', type=float, default=10.0)
ap.add_argument('--wn', type=float, default=10.0)
ap.add_argument('--clmin', type=float, default=1.05)
ap.add_argument('--mu0', type=float, default=1e-3)
ap.add_argument('--fixcl', type=float, default=0.0, help='if > 0: c_l fixed, identity not imposed (F_c reported)')
ap.add_argument('--out', type=str, required=True)
a = ap.parse_args()

L = LP(a.u0, a.u1, a.Nu, a.M, a.k0)
Nu, M = a.Nu, a.M
h = L.du
r0 = np.exp(L.u[0])
th = L.th
base_rho0 = r0 ** 3 * np.cos(th) ** 2 * np.sin(th)          # x^2 y at r0
base_phi0 = base_rho0 / np.exp(L.lw[0])
rg = r0 * np.exp(-h * np.array([2.0, 1.0]))                   # ghost radii (rows -2, -1)
lwg = 3 * np.log(rg) + 0.5 * (a.k0 - 3) * np.log1p(rg ** 2)


def saddle_ghost(phi_row0, cl, c):
    l1, l2 = cl - c, cl + c
    if not (l1 < 0 < l2):
        return None
    al, be = -l1, l2
    X = rg[:, None] * np.cos(th)[None, :]
    Y = rg[:, None] * np.sin(th)[None, :]
    # solve X^2 e^{2 al t} + Y^2 e^{-2 be t} = r0^2, t > 0 (convex in t, one root); bisection on log scale + Newton
    lo = np.zeros_like(X); hi = np.full_like(X, 1.0)
    f = lambda t: X ** 2 * np.exp(2 * al * t) + Y ** 2 * np.exp(-2 * be * t) - r0 ** 2
    for _ in range(80):
        bad = f(hi) < 0
        if not bad.any():
            break
        hi = np.where(bad, 2 * hi, hi)
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        neg = f(mid) < 0
        lo = np.where(neg, mid, lo); hi = np.where(neg, hi, mid)
    t = 0.5 * (lo + hi)
    xe = X * np.exp(al * t); ye = Y * np.exp(-be * t)
    the = np.arctan2(ye, xe)
    coef = L.Sinv @ phi_row0                                   # odd sine modes of phi(u0, .)
    m = np.arange(M)
    phie = np.sin(np.multiply.outer(the, 2 * m + 1)) @ coef    # phi(u0, th_e)
    rho_g = phie * np.exp(L.lw[0]) * np.exp(t)
    return rho_g / np.exp(lwg)[:, None]


def resid(z):
    phi = z[:-1].reshape(Nu, M)
    cl = z[-1] if a.fixcl <= 0 else a.fixcl
    k = min(max(1.0 / cl, 0.05), 0.97)
    A, B, c, psit = L.fields(phi, cl, k)
    glo = saddle_ghost(phi[0], cl, c)
    if glo is None:
        return None, c, psit
    _, ghi = L.ghosts(phi, k)
    Fp = phi - L.transport(phi, A, B, glo, ghi)
    aest = np.dot(phi[0], base_phi0) / np.dot(base_phi0, base_phi0)
    wc = a.wc if a.fixcl <= 0 else 0.0
    return np.concatenate([Fp.ravel(), [wc * (3 * cl - 1 - c), a.wn * (aest - 1)]]), c, psit


def axis(psit, cl):
    n = L.n[None, :]
    A0 = cl - np.sum(2 * n * psit, axis=1)
    i = np.where((A0[:-1] < 0) & (A0[1:] >= 0))[0]
    if len(i) == 0:
        return np.nan
    i = i[0]
    return float(np.exp(L.u[i] + (-A0[i] / (A0[i + 1] - A0[i])) * L.du))


r = L.r[:, None]
if a.init:
    d = np.load(a.init)
    phi0 = d['phi']
    if phi0.shape != (Nu, M):
        from scipy.interpolate import CubicSpline
        assert phi0.shape[1] == M
        phi0 = CubicSpline(d['u'], phi0, axis=0)(np.clip(L.u, d['u'][0], d['u'][-1]))
    cl0 = float(d['cl'])
else:
    k0 = a.k0
    Lsq = 4 * (1 - k0) * (3 / k0 - 1) * a.Lscale ** 2
    phi0 = np.cos(th)[None, :] ** 2 * np.sin(th)[None, :] * ((1 + r ** 2 / Lsq) / (1 + r ** 2)) ** ((k0 - 3) / 2)
    cl0 = 1 / k0
if a.cl0 > 0:
    cl0 = a.cl0
if a.fixcl > 0:
    cl0 = a.fixcl
z = np.concatenate([phi0.ravel(), [cl0]])
log = open(a.out + '.log', 'w')
def out(s):
    print(s, flush=True); log.write(s + '\n'); log.flush()
out(f"# gn_lp Nu={Nu} M={M} u=[{a.u0},{a.u1}] k0={a.k0} init={a.init or 'analytic'} cl0={cl0} wc={a.wc} wn={a.wn}")
R, c, psit = resid(z)
if R is None:
    out("initial state has no saddle at 0; abort"); sys.exit(1)
mu = a.mu0
t0 = time.time()
for it in range(a.maxit):
    nr = np.linalg.norm(R); nmax = np.max(np.abs(R[:-2])) / np.max(np.abs(z[:-1]))
    imax = np.unravel_index(np.argmax(np.abs(R[:-2])), (Nu, M))
    out(f"it={it:3d} cl={z[-1]:.8f} c={c:.8f} |R|2={nr:.4e} max|Fphi|/max|phi|={nmax:.3e} at u={L.u[imax[0]]:.2f},m={imax[1]} Fc={3*z[-1]-1-c:.2e} "
        f"Fn={R[-1]/a.wn:.2e} mu={mu:.1e} x*={axis(psit, z[-1]):.4f} minphi={np.min(z[:-1]):.3e} wall={time.time()-t0:.0f}s")
    np.savez(a.out + '.npz', phi=z[:-1].reshape(Nu, M), cl=z[-1], u=L.u, th=L.th, k0=a.k0, c=c)
    if nmax < a.tol:
        break
    N = z.size if a.fixcl <= 0 else z.size - 1
    J = np.empty((R.size, N))
    for i in range(N):
        zp = z.copy(); zp[i] += a.fdh
        Rp = resid(zp)[0]
        J[:, i] = (Rp - R) / a.fdh if Rp is not None else 0.0
    JtJ = J.T @ J
    g = J.T @ R
    D = np.diag(JtJ).copy() + 1e-12
    accepted = False
    for _ in range(12):
        dz = -np.linalg.solve(JtJ + mu * np.diag(D), g)
        zn = z.copy(); zn[:N] += dz
        if zn[-1] < a.clmin:
            mu *= 4; continue
        Rn, cn, psn = resid(zn)
        if Rn is not None and np.all(np.isfinite(Rn)) and np.linalg.norm(Rn) < nr:
            accepted = True
            break
        mu *= 4
    if not accepted:
        out("LM: no decrease; stop"); break
    z, R, c, psit = zn, Rn, cn, psn
    mu = max(mu / 5, 1e-10)
log.close()
