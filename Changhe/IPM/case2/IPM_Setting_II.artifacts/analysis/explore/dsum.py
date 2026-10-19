# Lead (2026-10-18): one-line axis summary of a forward x-even state (lead or numerics npz with g, lr, th; rho = r^p g).
# Fp - Fm = log(h_+/h_-) r^{2-p} at the outer ring (h = rho_xx on the half-axes, -> 2 e^{F(+-pi/2)} r^{p-2});
# twoL = 2 log(kappa_+/kappa_-) from the k ODE (k' = -(a - m1) k / Vr, a = 2l - Vr'), paired, at the outer ring;
# D_ax = log(h/k^2)_down - log(h/k^2)_up at the outer ring minus the law difference (axcheck.py, M25(g)); shares of 2L by lr range.
# Usage: python3 dsum.py state.npz p m1 [tag]
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import pforward as PF
d = np.load(sys.argv[1]); p = float(sys.argv[2]); m1 = float(sys.argv[3]); l = 1 / p; m2 = 2 * l - m1
tag = sys.argv[4] if len(sys.argv) > 4 else sys.argv[1]
g, lr, th = d['g'], d['lr'], d['th']; Nth = len(th); r = np.exp(lr)
rho = (r ** p)[:, None] * g
wr, wt = PF.velocity_p(rho, lr, th, p)
kk = np.fft.rfftfreq(Nth, 1.0 / Nth)
gtt = np.fft.irfft(-(kk ** 2) * np.fft.rfft(g, axis=1), Nth, axis=1)
res = {}
for name, j in (('up', Nth // 4), ('down', 3 * Nth // 4)):
    h = r ** (p - 2) * gtt[:, j]; Vr = l * r + wr[:, j]
    a = 2 * l - np.gradient(Vr, r); f = -(a - m1) / Vr
    logk = np.concatenate([[0], np.cumsum(0.5 * (f[1:] + f[:-1]) * np.diff(r))])
    law = np.concatenate([[0], np.cumsum(0.5 * ((1 - 2 * m1) / Vr[1:] + (1 - 2 * m1) / Vr[:-1]) * np.diff(r))])
    res[name] = dict(logh_out=float(np.log(abs(h[-1]) * r[-1] ** (2 - p) / 2)), q=float(np.log(abs(h[-1])) - 2 * logk[-1] - law[-1]), logk=logk, Vr=Vr)
we = 0.5 * (wr[:, Nth // 4] - wr[:, 3 * Nth // 4]); Vo = l * r + 0.5 * (wr[:, Nth // 4] + wr[:, 3 * Nth // 4])
dens = 4 * m2 * we / (Vo ** 2 - we ** 2) * r
sh = lambda lo, hi: float(np.trapezoid(dens[(lr >= lo) & (lr < hi)], lr[(lr >= lo) & (lr < hi)]))
out = dict(tag=tag, p=p, Fp_minus_Fm=round(res['up']['logh_out'] - res['down']['logh_out'], 4),
           twoL=round(float(2 * (res['up']['logk'][-1] - res['down']['logk'][-1])), 4),
           D_ax=round(res['down']['q'] - res['up']['q'], 4),
           twoL_res17=round(float(np.trapezoid(dens, lr)), 4),
           share_lt_m4=round(sh(-99, -4), 4), share_m4_2=round(sh(-4, 2), 4), share_gt_2=round(sh(2, 99), 4),
           we_over_r_m6=float('%.4g' % (we[np.argmin(np.abs(lr + 6))] / np.exp(-6))), we_far_over_rp=float('%.4g' % (we[-1] / r[-1] ** p)),
           lr_min=float(lr[0]), lr_max=float(lr[-1]), Nth=Nth)
print(json.dumps(out))
