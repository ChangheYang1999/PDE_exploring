# Lead: characteristic check of a lead-format state in the core. With V computed from the state itself, trace FORWARD
# orbits (d lr/dt = V_r/r, d th/dt = V_th/r) from points (lr0, th) to r_max and compare g_char = e^{-T} r_max^p A(th_exit) / r^p with the
# grid value g. Usage: python3 withpf2.py charcore.py state.npz K [lr list] [deg list]   (datum = cos^2 exp(x @ basis_K), x from the file)
import sys, numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
import pforward as PF
from scipy.interpolate import RectBivariateSpline
s = np.load(sys.argv[1]); K = int(sys.argv[2])
lrs = [float(v) for v in sys.argv[3].split(',')] if len(sys.argv) > 3 else [-12, -11, -10, -9, -8, -6, -4]
degs = [float(v) for v in sys.argv[4].split(',')] if len(sys.argv) > 4 else [0, 30, 60, 75, 85, 88, 92, 105, 150, 180, 240, 265, 268, 272, 285]
g, lr, th, p, x = s['g'], s['lr'], s['th'], float(s['p']), s['x'][:K]; l = 1 / p; r = np.exp(lr); N = len(th)
Af = lambda t: np.cos(t) ** 2 * np.exp(x @ FE.basis(np.atleast_1d(t).ravel(), K))
rho = (r ** p)[:, None] * g; wr, wt = PF.velocity_p(rho, lr, th, p)
ar = l + wr / r[:, None]; at = wt / r[:, None]
pad = 8; thx = np.concatenate([th[-pad:] - 2 * np.pi, th, th[:pad] + 2 * np.pi]); ext = lambda F: np.concatenate([F[:, -pad:], F, F[:, :pad]], axis=1)
Sr = RectBivariateSpline(lr, thx, ext(ar), kx=3, ky=3); St = RectBivariateSpline(lr, thx, ext(at), kx=3, ky=3)
c2 = np.maximum(np.cos(th) ** 2, 1e-30)[None, :]; Sg = RectBivariateSpline(lr, thx, ext(np.log(np.maximum(g / c2, 1e-300))), kx=3, ky=3)
ii = np.array([np.argmin(np.abs(lr - v)) for v in lrs]); jj = np.array([np.argmin(np.abs(np.degrees(th) - v)) for v in degs])
lrs = list(lr[ii]); degs = list(np.degrees(th[jj]))
L0, D0 = np.meshgrid(np.array(lrs, float), np.array(degs, float), indexing="ij"); X = L0.ravel().copy(); T = np.radians(D0.ravel()).copy(); tt = np.zeros_like(X)
X0, T0 = X.copy(), T.copy()
def f(a, b):
    b = np.mod(b, 2 * np.pi); return Sr.ev(a, b), St.ev(a, b)
dt = 0.005; live = X < lr[-1]
while live.any():
    a, b = X[live], T[live]
    k1 = f(a, b); k2 = f(a + .5 * dt * k1[0], b + .5 * dt * k1[1]); k3 = f(a + .5 * dt * k2[0], b + .5 * dt * k2[1]); k4 = f(a + dt * k3[0], b + dt * k3[1])
    da = dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); db = dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    an = a + da; over = an >= lr[-1]
    # last partial step: linear fraction to land on lr[-1]
    fr = np.where(over, (lr[-1] - a) / np.maximum(da, 1e-300), 1.0)
    X[live] = a + fr * da; T[live] = b + fr * db; tt[live] += fr * dt
    live = X < lr[-1] - 1e-12
logg_char = -tt + p * lr[-1] + np.log(np.maximum(Af(np.mod(T, 2 * np.pi)), 1e-300)) - p * X0
logg_grid = np.log(np.maximum(g[np.ix_(ii, jj)], 1e-300)).ravel()
d = (logg_grid - logg_char).reshape(L0.shape)
print('state', sys.argv[1], 'Nth', N, 'p %.5f' % p)
print('log(g_grid / g_char) at grid points, by lr (rows) and angle (cols):', ' '.join('%6.1f' % v for v in degs))
for i, L in enumerate(lrs):
    print('lr %6.2f   ' % L + ' '.join('%6.3f' % v for v in d[i]))
