# Lead: scale-invariant concentration Q = log(G_up a_*^{1/(1-p)}) (a_* = max_th g at the outer radius), effective
# mismatch length L_eff = c_{lr<-6} / (K (G_up - G_lo)) at lr -9 in units of l_* = a_*^{1/(1-p)}, transition radius
# r_c = (a_*/G_up)^{1/(2-p)} (log, and in units of l_*), cumulative strain c_<R at lr = -12 .. 2 (referee result 18 / specification M27(g)).
# Lead-format npz (g, lr, th, p); no core term below lr[0]. Usage: python3 cq.py state.npz [...]
import sys, numpy as np
K = 14 / (15 * np.pi)
print('%-30s %6s %6s %7s %7s %8s %8s %8s | c_<R at lr -12 -10 -8 -6 -4 -2 0 2' % ('state', 'p', 'c', 'Q', 'lnr_c', 'r_c/l*', 'Leff/l*', 'lD(-9)'))
for f in sys.argv[1:]:
    s = np.load(f, allow_pickle=True); g, lr, th, p = s['g'], s['lr'], s['th'], float(s['p']); r = np.exp(lr)
    up = np.sin(th) > 0; sel = np.abs(np.cos(th)) > 0.5
    rho = (r ** p)[:, None] * g; q = rho / np.maximum((r[:, None] * np.cos(th)[None, :]) ** 2, 1e-300)
    Gu = np.array([np.median(q[i][sel & up]) for i in range(len(lr))]); Gl = np.array([np.median(q[i][sel & ~up]) for i in range(len(lr))])
    net = 2 * (np.exp((p - 1) * lr)[:, None] * g * np.sin(3 * th)[None, :]).mean(axis=1)
    cum = np.concatenate([[0], np.cumsum(0.5 * (net[1:] + net[:-1]) * np.diff(lr))])
    astar = g[-1].max(); lstar = astar ** (1 / (1 - p))
    i11 = np.argmin(abs(lr + 11)); i9 = np.argmin(abs(lr + 9)); i6 = np.argmin(abs(lr + 6))
    Q = np.log(Gu[i11] * lstar); rc = (astar / Gu[i11]) ** (1 / (2 - p))
    Leff = cum[i6] / (K * (Gu[i9] - Gl[i9]))
    cs = ' '.join('%6.3f' % cum[np.argmin(abs(lr - t))] for t in [-12, -10, -8, -6, -4, -2, 0, 2])
    print('%-30s %6.4f %6.3f %7.3f %7.3f %8.3g %8.3g %8.3f | %s' % (f.split('/')[-1][:30], p, cum[-1], Q, np.log(rc), rc / lstar, Leff / lstar, np.log(Gl[i9] / Gu[i9]), cs))
