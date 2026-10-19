# Lead: specification M26(h)(i) exact-T test on a lead-format state. With V computed from the state itself (frozen), replace g on
# every grid point with lr <= lrcut by g_char = e^{-T} r_max^p A(th_exit) / r^p from the FORWARD orbit (as charcore.py, all angles),
# keep g above lrcut, and report the moment m1 (m1mom.py formula) of the state and of its exact image, plus max |log g - log g_char|
# on lr <= -8 (M26(h)(ii)), by band. Usage: python3 withpf2.py exactT.py state.npz K [lrcut=-4 dt=0.01 thin=1]
import sys, json, time, numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
import pforward as PF
from scipy.interpolate import RectBivariateSpline
s = np.load(sys.argv[1]); K = int(sys.argv[2])
o = dict(lrcut=-4.0, dt=0.01, thin=1)
for a in sys.argv[3:]:
    k, v = a.split('='); o[k] = int(v) if k == 'thin' else float(v)
g, lr, th, p, x = s['g'], s['lr'], s['th'], float(s['p']), s['x'][:K]; l = 1 / p; r = np.exp(lr); N = len(th)
Af = lambda t: np.cos(t) ** 2 * np.exp(x @ FE.basis(np.atleast_1d(t).ravel(), K))
t0 = time.time()
rho = (r ** p)[:, None] * g; wr, wt = PF.velocity_p(rho, lr, th, p)
ar = l + wr / r[:, None]; at = wt / r[:, None]
pad = 8; thx = np.concatenate([th[-pad:] - 2 * np.pi, th, th[:pad] + 2 * np.pi]); ext = lambda F: np.concatenate([F[:, -pad:], F, F[:, :pad]], axis=1)
Sr = RectBivariateSpline(lr, thx, ext(ar), kx=3, ky=3); St = RectBivariateSpline(lr, thx, ext(at), kx=3, ky=3)
ii = np.where(lr <= o['lrcut'])[0][::o['thin']]
L0, J0 = np.meshgrid(ii, np.arange(N), indexing='ij'); X = lr[L0].ravel().copy(); T = th[J0].ravel().copy(); tt = np.zeros_like(X); X0 = X.copy()
def f(a, b):
    b = np.mod(b, 2 * np.pi); return Sr.ev(a, b), St.ev(a, b)
dt = o['dt']; live = X < lr[-1]; nst = 0
while live.any() and nst < 100000:
    a, b = X[live], T[live]
    k1 = f(a, b); k2 = f(a + .5 * dt * k1[0], b + .5 * dt * k1[1]); k3 = f(a + .5 * dt * k2[0], b + .5 * dt * k2[1]); k4 = f(a + dt * k3[0], b + dt * k3[1])
    da = dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); db = dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    an = a + da; over = an >= lr[-1]
    fr = np.where(over, (lr[-1] - a) / np.maximum(da, 1e-300), 1.0)
    X[live] = a + fr * da; T[live] = b + fr * db; tt[live] += fr * dt
    live = X < lr[-1] - 1e-12; nst += 1
gc = np.exp(-tt + p * lr[-1] - p * X0) * Af(np.mod(T, 2 * np.pi))
gT = g.copy(); gT[L0, J0] = gc.reshape(L0.shape)


def m1mom(G):
    w = np.exp((p - 1) * lr)[:, None] * G * np.sin(3 * th)[None, :]
    ang = w.mean(axis=1) * 2
    return 1 / p - np.trapz(ang, lr) - ang[-1] / (1 - p), ang


m0, a0 = m1mom(g); mT, aT = m1mom(gT)
rows = lr[ii]; lg = np.log(np.maximum(g[ii], 1e-300)); lc = np.log(np.maximum(gT[ii], 1e-300))
sig = g[ii] > 1e-3 * g[ii].max(axis=1, keepdims=True)
dd = np.where(sig, np.abs(lg - lc), 0.0)
offax = (np.abs(np.sin(th)) >= np.sin(np.radians(6.0)))[None, :]             # specification M26(h) v4.1: weak-axis sectors reported separately
bands = {}
for lo, hi in [(-14.5, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4)]:
    m = (rows >= lo) & (rows < hi)
    if m.any():
        dm = -np.trapz(np.where((lr >= lo) & (lr < hi), aT - a0, 0.0), lr)
        sub = dd[m]; k = np.unravel_index(np.argmax(sub), sub.shape)
        bands['%g..%g' % (lo, hi)] = dict(maxdev=round(float(sub.max()), 4), at=[round(float(rows[m][k[0]]), 2), round(float(np.degrees(th[k[1]])), 1)],
                                         p99=round(float(np.percentile(sub[sig[m]], 99)), 4), dm1=round(float(dm), 5))
out = dict(state=sys.argv[1], Nth=N, p=round(p, 6), m1=round(float(m0), 5), m1_exactT=round(float(mT), 5), dm1=round(float(mT - m0), 5),
           maxdev_lr_m12_m8=round(float(dd[(rows >= -12) & (rows <= -8)].max()), 4),
           maxdev_offaxis_le_m8=round(float(np.where(offax, dd, 0.0)[rows <= -8].max()), 4),
           maxdev_axis_le_m8=round(float(np.where(offax, 0.0, dd)[rows <= -8].max()), 4), bands=bands, rows=len(ii), steps=nst, dt=dt, wall=round(time.time() - t0))
print(json.dumps(out), flush=True)
