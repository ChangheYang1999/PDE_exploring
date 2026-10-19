# Lead (2026-10-18): y-axis check of a forward x-even state. h(r) = rho_xx(0, +-r) from the angular second
# derivative of g at 90/270 deg (spectral), b = V_2 on the axis, a = 2l - dV_r/dr, k from b k' + (a - m1) k = 0 (k(0) = 1),
# and the axis law b (log h/k^2)' = 1 - 2 m1. Prints h, k, h/k^2 on both half-axes at selected r.
# Usage: python3 axcheck.py state.npz p m1
import sys, json
import numpy as np
sys.path.insert(0, 'explore')
import pforward as PF
d = np.load(sys.argv[1]); p = float(sys.argv[2]); m1 = float(sys.argv[3]); l = 1 / p
g, lr, th = d['g'], d['lr'], d['th']; Nth = len(th); r = np.exp(lr)
rho = (r ** p)[:, None] * g
wr, wt = PF.velocity_p(rho, lr, th, p)
kk = np.fft.rfftfreq(Nth, 1.0 / Nth)
gtt = np.fft.irfft(-(kk ** 2) * np.fft.rfft(g, axis=1), Nth, axis=1)
out = {}
for name, j in (('up', Nth // 4), ('down', 3 * Nth // 4)):
    h = r ** (p - 2) * gtt[:, j]          # rho_xx(0, y) = (1/r^2) d^2 rho/d th^2 on the axis
    Vr = l * r + wr[:, j]                 # radial velocity on the half-axis (= |b|)
    dVr = np.gradient(Vr, r)
    a = 2 * l - dVr
    # k: dk/dr = -(a - m1) k / Vr, integrate from the innermost point (k = 1 there)
    f = -(a - m1) / Vr
    logk = np.concatenate([[0], np.cumsum(0.5 * (f[1:] + f[:-1]) * np.diff(r))])
    q = np.log(np.abs(h)) - 2 * logk
    law = np.concatenate([[0], np.cumsum(0.5 * ((1 - 2 * m1) / Vr[1:] + (1 - 2 * m1) / Vr[:-1]) * np.diff(r))])
    sel = [int(np.argmin(np.abs(lr - L))) for L in (-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 9.5)]
    out[name] = [dict(lr=round(float(lr[i]), 2), h=float('%.4g' % h[i]), a=round(float(a[i]), 4), Vr_over_r=round(float(Vr[i] / r[i]), 4),
                      logk=round(float(logk[i]), 4), log_h_over_k2=round(float(q[i]), 4), law=round(float(law[i]), 4),
                      h_r2mp=float('%.4g' % (h[i] * r[i] ** (2 - p)))) for i in sel]
for k_, v in out.items():
    print(k_)
    for row in v: print(json.dumps(row))
