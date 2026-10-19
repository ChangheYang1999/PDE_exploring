"""Dynamic rescaling on the log-polar grid (lead prototype).  rho_tau = rho - (c_l X + U).grad rho, c_l = (1 + c)/3.
Usage: python3 dr_lp.py --k0 0.6 --Nu 601 --M 24 --dt 0.002 --T 20 --out runs/dr_k06
"""
import argparse, time, sys
import numpy as np
sys.path.insert(0, 'scripts')
from lp_core import LP

ap = argparse.ArgumentParser()
ap.add_argument('--k0', type=float, default=0.6)
ap.add_argument('--Lscale', type=float, default=1.0, help='multiplies the identity-consistent L')
ap.add_argument('--u0', type=float, default=-5.0)
ap.add_argument('--u1', type=float, default=7.0)
ap.add_argument('--Nu', type=int, default=601)
ap.add_argument('--M', type=int, default=24)
ap.add_argument('--dt', type=float, default=0.002)
ap.add_argument('--T', type=float, default=20.0)
ap.add_argument('--every', type=float, default=0.5)
ap.add_argument('--init', type=str, default='')
ap.add_argument('--out', type=str, required=True)
ap.add_argument('--gauge', type=str, default='crho1', help='crho1: c_rho = 1, c_l = (1+c)/3; cld: c_l = cld fixed, c_rho = 3 cld - c')
ap.add_argument('--cld', type=float, default=1.6666667)
a = ap.parse_args()

L = LP(a.u0, a.u1, a.Nu, a.M, a.k0)
r = L.r[:, None]; th = L.th[None, :]
k0 = a.k0
if a.init:
    d = np.load(a.init)
    phi = d['phi']
else:
    Lsq = 4 * (1 - k0) * (3 / k0 - 1) * a.Lscale ** 2
    phi = np.cos(th) ** 2 * np.sin(th) * ((1 + r ** 2 / Lsq) / (1 + r ** 2)) ** ((k0 - 3) / 2)


def state(phi):
    """Returns A, B, c, (effective profile c_l), k, psit, c_rho, transport speed c_l used in A."""
    _, _, c, _ = L.velocity(phi, k0)  # c with provisional tail exponent
    if a.gauge == 'crho1':
        cl = (1 + c) / 3; crho = 1.0; clt = cl
    else:
        crho = 3 * a.cld - c; clt = a.cld; cl = clt / crho if crho > 0 else np.nan
    k = crho / clt
    k = min(max(k, 0.05), 0.98)
    A, B, c, psit = L.fields(phi, clt, k)
    if a.gauge == 'crho1':
        cl = (1 + c) / 3; clt = cl; A = A + (cl - clt)
    else:
        crho = 3 * a.cld - c; cl = clt / crho if crho > 0 else np.nan
    return A, B, c, cl, k, psit, crho, clt


def rhs(phi):
    A, B, c, cl, k, psit, crho, clt = state(phi)
    glo, ghi = L.ghosts(phi, k)
    return crho * phi - L.transport(phi, A, B, glo, ghi), cl


def axis_diag(psit, cl):
    n = L.n[None, :]
    A0 = cl - np.sum(2 * n * psit, axis=1)
    # d_u psit by finite differences of psit (diagnostic only)
    dps = L.du_c(psit)
    mu2 = cl + np.sum(2 * n * (dps + psit), axis=1)
    i = np.where((A0[:-1] < 0) & (A0[1:] >= 0))[0]
    if len(i) == 0:
        return np.nan, np.nan, np.nan
    i = i[0]
    t = -A0[i] / (A0[i + 1] - A0[i])
    us = L.u[i] + t * L.du
    m2 = mu2[i] + t * (mu2[i + 1] - mu2[i])
    mu1 = (A0[i + 1] - A0[i]) / L.du  # d_u A = r d_r (W_1/r) = d_x W_1 - W_1/x = mu1 at P
    return np.exp(us), mu1, m2


t0 = time.time()
tau = 0.0
nsteps = int(round(a.T / a.dt))
ev = int(round(a.every / a.dt))
log = open(a.out + '.log', 'w')
hdr = f"# k0={k0} Lscale={a.Lscale} u=[{a.u0},{a.u1}] Nu={a.Nu} M={a.M} dt={a.dt}"
print(hdr); log.write(hdr + '\n')
for it in range(nsteps + 1):
    if it % ev == 0:
        A, B, c, cl, k, psit, crho, clt = state(phi)
        R, _ = rhs(phi)
        xs, mu1, mu2 = axis_diag(psit, clt)
        if a.gauge != 'crho1':  # report P data in profile normalization: divide rates by c_rho
            mu1, mu2 = mu1 / crho, mu2 / crho
        line = (f"tau={tau:7.3f} cl={cl:.6f} c={c:.6f} crho={crho:.5f} |rhs|/|phi|={np.max(np.abs(R))/np.max(np.abs(phi)):.3e} "
                f"max|phi|={np.max(np.abs(phi)):.4e} min phi={np.min(phi):.3e} x*={xs:.4f} mu1={mu1:.4f} (2cl-1={2*cl-1:.4f}) "
                f"mu2={mu2:.4f} wall={time.time()-t0:.0f}s")
        print(line, flush=True); log.write(line + '\n'); log.flush()
        np.savez(a.out + '.npz', phi=phi, u=L.u, th=L.th, cl=cl, k0=k0, tau=tau)
        if not np.all(np.isfinite(phi)) or np.max(np.abs(phi)) > 1e8:
            break
    if it == nsteps:
        break
    k1, _ = rhs(phi)
    k2, _ = rhs(phi + 0.5 * a.dt * k1)
    k3, _ = rhs(phi + 0.5 * a.dt * k2)
    k4, _ = rhs(phi + a.dt * k3)
    phi = phi + a.dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    tau += a.dt
log.close()
