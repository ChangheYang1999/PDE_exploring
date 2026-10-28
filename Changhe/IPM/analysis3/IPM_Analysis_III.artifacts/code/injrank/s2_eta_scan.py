# NUMERICAL (float64 grid data, not a bound): eta dependence of S2(b_eta) on the window [-3, 11] of s2_estimate.py,
# and the resulting global second-order cutoff Lambda^2 = [sum S2(B_ij) + S2(b_eta)] / [2 (E - eta/2)].
import numpy as np, json, sys
exec(open('s2_estimate.py').read().split('out = {}')[0])
t0, t1, w = -3.0, 11.0, 1.0
m = (t >= t0) & (t <= t1); tt = t[m]
def bump(x):
    y = np.zeros_like(x); i = (x > 0) & (x < 1)
    y[i] = 1 / (1 + np.exp(1 / x[i] - 1 / (1 - x[i]))); y[x >= 1] = 1; return y
chi = bump((tt - t0) / w) * bump((t1 - tt) / w); ell = tt[-1] - tt[0] + (tt[1] - tt[0])
xi = 2 * np.pi * np.fft.fftfreq(len(tt), d=(tt[1] - tt[0])); nn = np.fft.fftfreq(n_th, d=1.0 / n_th)
Q2 = xi[:, None]**2 + nn[None, :]**2
S2 = lambda a: float((Q2 * abs(np.fft.fft2(a[m] * chi[:, None]) / (len(tt) * n_th))).sum())
SB = S2(B11) + S2(B22) + 2 * S2(B12)
out = dict(S2_B_sum=SB, rows=[])
for eta in [0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5]:
    sb = S2((np.sqrt(G1**2 + G2**2 + eta**2) - G2) / 2)
    row = dict(eta=eta, S2_beta=sb)
    for E in [1.0, 1.25, 1.5]:
        if E > eta / 2:
            L2 = (SB + sb) / (2 * (E - eta / 2)); row['E=%g' % E] = dict(Lambda=float(np.sqrt(L2)), N_parity=float(L2 * ell / 8))
    out['rows'].append(row)
print(json.dumps(out, indent=1))
