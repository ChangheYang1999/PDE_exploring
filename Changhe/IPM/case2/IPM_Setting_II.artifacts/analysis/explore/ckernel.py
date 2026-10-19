# Lead: frozen-velocity sensitivity of c = l - m1 to the datum, by exit angle. With V from the state (frozen), integrate the
# forward orbit of every grid point with lr <= lrcut to r_max (as exactT.py), record its exit angle phi, and bin the cell
# contributions dc = (1/pi) e^{(p-1) lr} g sin 3th dlr dth by phi (1 deg bins) and by band of lr. Since rho = e^{-T} r_max^p A(phi)
# on orbits, the binned sum is d c / d log A(phi) at frozen velocity (per bin). Also records T. Usage:
# python3 withpf2.py ckernel.py state.npz K out.npz [lrcut=-2 dt=0.01]
import sys, json, time, numpy as np
sys.path.insert(0, 'explore')
import pforward as PF
from scipy.interpolate import RectBivariateSpline
s = np.load(sys.argv[1], allow_pickle=True); K = int(sys.argv[2]); outf = sys.argv[3]
o = dict(lrcut=-2.0, dt=0.01)
for a in sys.argv[4:]:
    k, v = a.split('='); o[k] = float(v)
g, lr, th, p = s['g'], s['lr'], s['th'], float(s['p']); l = 1 / p; r = np.exp(lr); N = len(th)
t0 = time.time()
rho = (r ** p)[:, None] * g; wr, wt = PF.velocity_p(rho, lr, th, p)
ar = l + wr / r[:, None]; at = wt / r[:, None]
pad = 8; thx = np.concatenate([th[-pad:] - 2 * np.pi, th, th[:pad] + 2 * np.pi]); ext = lambda F: np.concatenate([F[:, -pad:], F, F[:, :pad]], axis=1)
Sr = RectBivariateSpline(lr, thx, ext(ar), kx=3, ky=3); St = RectBivariateSpline(lr, thx, ext(at), kx=3, ky=3)
ii = np.where(lr <= o['lrcut'])[0]
L0, J0 = np.meshgrid(ii, np.arange(N), indexing='ij'); X = lr[L0].ravel().copy(); T = th[J0].ravel().copy(); tt = np.zeros_like(X)
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
phi = np.mod(T, 2 * np.pi).reshape(L0.shape)
dlr = lr[1] - lr[0]; dth = 2 * np.pi / N
w = np.ones(len(ii)); w[0] = 0.5                                        # trapezoid end weight at lr[0]
dc = (1 / np.pi) * (np.exp((p - 1) * lr[ii]) * w)[:, None] * g[ii] * np.sin(3 * th)[None, :] * dlr * dth
bins = np.linspace(0, 2 * np.pi, 361); kb = np.clip(np.digitize(phi, bins) - 1, 0, 359)
bands = [(-14.5, -10), (-10, -6), (-6, -4), (-4, o['lrcut'] + 1e-9)]
Kc = np.zeros((len(bands), 360))
for bi, (lo, hi) in enumerate(bands):
    m = (lr[ii] >= lo) & (lr[ii] < hi)
    np.add.at(Kc[bi], kb[m].ravel(), dc[m].ravel())
np.savez(outf, Kc=Kc, bands=np.array(bands), phi=phi.astype(np.float32), T=tt.reshape(L0.shape).astype(np.float32), rows=ii, p=p, lrcut=o['lrcut'])
deg = np.arange(360) + 0.5
summ = {}
for bi, (lo, hi) in enumerate(bands):
    k = Kc[bi]; tot = k.sum()
    win = lambda a, b: float(k[(deg >= a) & (deg < b)].sum())
    summ['%g..%g' % (lo, hi)] = dict(total=round(float(tot), 4), w80_100=round(win(80, 100), 4), w260_280=round(win(260, 280), 4),
                                     q0_80=round(win(0, 80) + win(280, 360), 4), q100_260=round(win(100, 260), 4))
print(json.dumps(dict(state=sys.argv[1], p=p, steps=nst, wall=round(time.time() - t0), bands=summ)), flush=True)
