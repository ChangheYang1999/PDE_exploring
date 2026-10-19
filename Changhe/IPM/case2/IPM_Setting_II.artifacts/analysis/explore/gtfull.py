# Lead: full log Gt(theta_exit) profile of a lead-format state with a GIVEN m1 (e.g. the producer's moment value):
# log Gt = log A - 2 log|e1 . X0| - 2 m1 (T - p lr_max), backward RK4 orbits from the exit circle to lr0 (as dcbroyden.gtrace),
# e1 = weak eigenvector of the ring node matrix. Prints picks relative to the bulk mean (|cos th| > 0.3), the bulk std, and the
# norm of the LSQ coefficients on [1, phi_1..phi_K] over |cos th| > 0.02 (the numerics' F_G form, uniform weight).
# Usage: python3 withpf2.py gtfull.py state.npz m1 [lr0=-12 nA=2048 K=32 kring=20 out=]
import sys, json, time, numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
import pforward as PF
from scipy.interpolate import RectBivariateSpline
s = np.load(sys.argv[1]); m1 = float(sys.argv[2])
o = dict(lr0=-12.0, nA=2048, K=32, kring=20, out='')
for a in sys.argv[3:]:
    k, v = a.split('='); o[k] = v if k == 'out' else (int(v) if k in ('nA', 'K', 'kring') else float(v))
g, lr, th, p, x = s['g'], s['lr'], s['th'], float(s['p']), s['x']; l = 1 / p; r = np.exp(lr); Kx = len(x)
Af = lambda t: np.cos(t) ** 2 * np.exp(x @ FE.basis(np.atleast_1d(t).ravel(), Kx))
t0 = time.time()
rho = (r ** p)[:, None] * g; wr, wt = PF.velocity_p(rho, lr, th, p)
ar = l + wr / r[:, None]; at = wt / r[:, None]
M = PF.node_matrix(ar[o['kring']], at[o['kring']], th); ev, evec = np.linalg.eigh(0.5 * (M + M.T)); e1 = evec[:, 0] * np.sign(evec[0, 0])
pad = 8; thx = np.concatenate([th[-pad:] - 2 * np.pi, th, th[:pad] + 2 * np.pi]); ext = lambda F: np.concatenate([F[:, -pad:], F, F[:, :pad]], axis=1)
Sr = RectBivariateSpline(lr, thx, ext(ar), kx=3, ky=3); St = RectBivariateSpline(lr, thx, ext(at), kx=3, ky=3)
rhs = lambda a, b: (-Sr.ev(a, np.mod(b, 2 * np.pi)), -St.ev(a, np.mod(b, 2 * np.pi)))
nA = o['nA']; dt = 0.01; thA = 2 * np.pi * np.arange(nA) / nA
X = np.full(nA, lr[-1]); T = thA.copy(); tt = np.zeros(nA); live = np.ones(nA, bool); it = 0
while live.any() and it < 200000:
    a, b = X[live], T[live]
    k1 = rhs(a, b); k2 = rhs(a + .5 * dt * k1[0], b + .5 * dt * k1[1]); k3 = rhs(a + .5 * dt * k2[0], b + .5 * dt * k2[1]); k4 = rhs(a + dt * k3[0], b + dt * k3[1])
    X[live] = a + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); T[live] = b + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    tt[live] += dt; live = live & (X > o['lr0']); it += 1
u0 = (np.exp(X)[:, None] * np.stack([np.cos(T), np.sin(T)], 1)) @ e1
lgt = np.log(np.maximum(Af(thA), 1e-300)) - 2 * np.log(np.maximum(np.abs(u0), 1e-300)) - 2 * m1 * (tt - p * lr[-1])
deg = np.degrees(thA); bulkm = np.abs(np.cos(thA)) > 0.3; bulk = float(lgt[bulkm].mean())
msk = (np.abs(np.cos(thA)) > 0.02) & np.isfinite(lgt)
Phi = np.vstack([np.ones_like(thA)[None], FE.basis(thA, o['K'])]).T[msk]
C = np.linalg.lstsq(Phi, lgt[msk] - lgt[msk].mean(), rcond=1e-10)[0]
pk = lambda d: round(float(lgt[np.argmin(np.abs(deg - d))] - bulk), 4)
picks = {str(d): pk(d) for d in (0, 30, 60, 75, 80, 85, 87, 88, 89, 91, 92, 93, 95, 100, 105, 120, 150, 180, 240, 255, 260, 265, 267, 268, 269, 271, 272, 273, 275, 280, 285, 300, 330)}
out = dict(state=sys.argv[1], m1=m1, ring_m1=round(float(ev[0]), 5), lr0=o['lr0'], nA=nA, D_samp=round(pk(269) - pk(89), 4),
           bulk_std=round(float(lgt[bulkm].std()), 4), FG_norm=round(float(np.linalg.norm(C[1:])), 4), rms_unres=round(float(np.std(lgt[msk] - lgt[msk].mean() - Phi @ C)), 4),
           range_cos005=round(float(np.ptp(lgt[np.abs(np.cos(thA)) > 0.05])), 4), picks=picks, nlive=int(live.sum()), steps=it, wall=round(time.time() - t0))
print(json.dumps(out), flush=True)
if o['out']:
    np.savez(o['out'], thA=thA, logGt=lgt, bulk=bulk, m1=m1, T=tt, X0=X, th0=T)
