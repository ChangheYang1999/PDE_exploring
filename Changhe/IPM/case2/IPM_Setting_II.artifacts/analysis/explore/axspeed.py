# Lead: axis speeds of an x-even lead-format state and the band split of the 5.8(v) formula
# D = F(-pi/2) - F(pi/2) + 2 n int (1/beta_- - 1/beta_+) dt, beta_+-(t) = B_+-(r)/r (outward speed / r on the upper / lower
# half-axis), t = log r, n = 2l - m1 (exact only at m1 = 1/2). Usage: python3 withpf2.py axspeed.py state.npz [m1=0.5] [K]
# (K: number of datum modes; numerics exit-map npz files carry x = (modes, p), so pass K = len(x) - 1 for them)
import sys, json, numpy as np
sys.path.insert(0, 'explore')
import fpeval as FE
import pforward as PF
s = np.load(sys.argv[1]); m1 = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5
g, lr, th, p = s['g'], s['lr'], s['th'], float(s['p']); K = int(sys.argv[3]) if len(sys.argv) > 3 else len(s['x'])
x = s['x'][:K]; l = 1 / p; r = np.exp(lr); N = len(th)
rho = (r ** p)[:, None] * g; wr, wt = PF.velocity_p(rho, lr, th, p)
ju, jd = N // 4, 3 * N // 4
assert abs(th[ju] - np.pi / 2) < 1e-9 and abs(th[jd] - 3 * np.pi / 2) < 1e-9
bu = l + wr[:, ju] / r; bd = l + wr[:, jd] / r; n = 2 * l - m1
F = lambda t: float(x @ FE.basis(np.atleast_1d(t), K).ravel())
dF = F(-np.pi / 2) - F(np.pi / 2)
f = 1 / bd - 1 / bu
bands = {}
for lo, hi in [(-14, -8), (-8, -4), (-4, 0), (0, 4), (4, 10)]:
    m = (lr >= lo) & (lr <= hi); bands['%d..%d' % (lo, hi)] = round(float(2 * n * np.trapz(f[m], lr[m])), 4)
k = np.argmin(bu); kd = np.argmin(bd)
out = dict(state=sys.argv[1], p=p, m1_used=m1, n=round(n, 4), dF=round(dF, 4), twoL=round(float(2 * n * np.trapz(f, lr)), 4),
           D_formula=round(float(dF + 2 * n * np.trapz(f, lr)), 4), twoL_bands=bands,
           min_beta_up=[round(float(bu[k]), 4), round(float(lr[k]), 2)], min_beta_down=[round(float(bd[kd]), 4), round(float(lr[kd]), 2)],
           beta_up_at_t={int(t): round(float(np.interp(t, lr, bu)), 3) for t in range(-14, 11, 2)},
           beta_down_at_t={int(t): round(float(np.interp(t, lr, bd)), 3) for t in range(-14, 11, 2)})
print(json.dumps(out))
