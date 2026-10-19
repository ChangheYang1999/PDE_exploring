# Local angular frequency of the near-axis residual R/N_f at fixed r (verifier, verifier).
# Usage: python3 strip_freq.py tag [r_lo r_hi thmax]
import sys, numpy as np
t = sys.argv[1]
rlo, rhi, thmax = (float(v) for v in sys.argv[2:5]) if len(sys.argv) > 4 else (8.2, 8.6, 0.15)
d = np.load('runs/audit/%s_resmap.npz' % t); r, th, R, Nf = d['r'], d['th'], d['R'], d['Nf']
with np.errstate(all='ignore'): X = np.where(Nf > 0, R / Nf, 0.0)
jj = (th > 1e-6) & (th <= thmax)
T = th[jj]
ns = np.arange(20, 900, 2.0)
win = np.sin(np.pi * T / thmax) ** 2
for i in np.where((r >= rlo) & (r <= rhi))[0][::3]:
    f = X[i, jj]
    zc = np.where(np.sign(f[1:]) != np.sign(f[:-1]))[0]
    zt = T[zc] + (T[zc+1]-T[zc]) * f[zc] / (f[zc] - f[zc+1])
    half = np.diff(zt)
    nzc = np.pi / np.median(half) if len(half) > 1 else np.nan
    P = np.array([abs(np.sum(f * win * np.exp(1j * n * T))) for n in ns])
    k = np.argmax(P)
    print('%s r %.3f max|R/Nf| %.2e  zero-crossing freq %.0f  periodogram peak n %.0f  (sin(n theta); cos(2m theta) m = n/2)' % (t, r[i], abs(f).max(), nzc, ns[k]))
