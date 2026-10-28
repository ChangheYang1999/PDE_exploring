# NUMERICAL (float64 grid data, not a bound): global second moments of the regular-region coefficients after a smooth
# angular cutoff removing the vertical-axis strip |theta - pi/2| < s0 (mod pi), where the singular weight |cos theta|^(-2a)
# lives and the strip estimate (topic 93) replaces Fourier counting. Window t in [-3, 11] as in s2_estimate.py.
import numpy as np, json, sys
exec(open('s2_estimate.py').read().split('out = {}')[0])
eta = 0.1
beta = (np.sqrt(G1**2 + G2**2 + eta**2) - G2) / 2
def bump(x):
    y = np.zeros_like(x); i = (x > 0) & (x < 1)
    with np.errstate(over='ignore'): y[i] = 1 / (1 + np.exp(1 / x[i] - 1 / (1 - x[i])))
    y[x >= 1] = 1; return y
t0, t1, w = -3.0, 11.0, 1.0
m = (t >= t0) & (t <= t1); tt = t[m]
chi = bump((tt - t0) / w) * bump((t1 - tt) / w); ell = tt[-1] - tt[0] + (tt[1] - tt[0])
xi = 2 * np.pi * np.fft.fftfreq(len(tt), d=(tt[1] - tt[0])); nn = np.fft.fftfreq(n_th, d=1.0 / n_th)
Q2 = xi[:, None]**2 + nn[None, :]**2
dist = np.abs(np.abs(np.cos(TH)))   # |cos theta| ~ distance to the vertical axis
out = {}
for s0 in [0.0, 0.05, 0.1, 0.2, 0.3]:
    ang = np.ones_like(TH) if s0 == 0 else bump((dist - s0) / s0)   # 0 for |cos| < s0, 1 for |cos| > 2 s0
    S2 = lambda a: float((Q2 * abs(np.fft.fft2(a[m] * chi[:, None] * ang[None, :]) / (len(tt) * n_th))).sum())
    SB = S2(B11) + S2(B22) + 2 * S2(B12); sb = S2(beta)
    row = dict(S2_B=SB, S2_beta=sb)
    for E in [1.0, 1.5]:
        L2 = (SB + sb) / (2 * (E - eta / 2)); row['E=%g' % E] = dict(Lambda=float(np.sqrt(L2)), N_parity=float(L2 * ell / 8))
    out['s0=%g' % s0] = row
print(json.dumps(out, indent=1))
