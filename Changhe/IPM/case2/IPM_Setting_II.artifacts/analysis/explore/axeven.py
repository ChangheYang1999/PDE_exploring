# Lead (2026-10-18): even / odd parts of the axis velocity of an x-even forward state and their share in
# log(kappa_+/kappa_-). Vr_+-(r) = |V_2(0, +-r)| = l r +- w_e(r) + w_o(r); exact log k_+ - log k_- vs the first-order
# form 2 m2 int_0^r w_e / Vr_o^2 ds + 2 w_e/Vr_o. Usage: python3 axeven.py state.npz p m1
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import pforward as PF
d = np.load(sys.argv[1]); p = float(sys.argv[2]); m1 = float(sys.argv[3]); l = 1 / p; m2 = 2 * l - m1
g, lr, th = d['g'], d['lr'], d['th']; Nth = len(th); r = np.exp(lr)
rho = (r ** p)[:, None] * g
wr, wt = PF.velocity_p(rho, lr, th, p)
wu, wd = wr[:, Nth // 4], wr[:, 3 * Nth // 4]          # W_2(0, r) and -W_2(0, -r)
we, wo = 0.5 * (wu - wd), 0.5 * (wu + wd)
Vp, Vm, Vo = l * r + wu, l * r + wd, l * r + wo
def logk(V):
    a = 2 * l - np.gradient(V, r); f = -(a - m1) / V
    return np.concatenate([[0], np.cumsum(0.5 * (f[1:] + f[:-1]) * np.diff(r))])
ex = logk(Vp) - logk(Vm)
integ = we / Vo ** 2
fo = 2 * m2 * np.concatenate([[0], np.cumsum(0.5 * (integ[1:] + integ[:-1]) * np.diff(r))]) + 2 * we / Vo - 2 * we[0] / Vo[0]
for L in (-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 9.5):
    i = int(np.argmin(np.abs(lr - L)))
    print(json.dumps(dict(lr=round(float(lr[i]), 2), we_over_r=float('%.4g' % (we[i] / r[i])), wo_over_r=float('%.4g' % (wo[i] / r[i])),
                          we_over_rp=float('%.4g' % (we[i] / r[i] ** p)), exact=round(float(ex[i]), 4), first_order=round(float(fo[i]), 4))))
# where does the integral come from (share per unit lr)
dens = 2 * m2 * integ * r
print(json.dumps(dict(share_lr_lt_m4=float(np.trapz(dens[lr < -4], lr[lr < -4])), share_m4_2=float(np.trapz(dens[(lr >= -4) & (lr < 2)], lr[(lr >= -4) & (lr < 2)])),
                      share_gt_2=float(np.trapz(dens[lr >= 2], lr[lr >= 2])), min_we=float(we.min()), sign_changes=int(np.sum(np.diff(np.sign(we)) != 0)))))
