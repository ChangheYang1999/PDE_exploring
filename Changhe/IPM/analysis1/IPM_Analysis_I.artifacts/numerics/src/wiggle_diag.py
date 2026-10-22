"""Floating diagnostic: knot-scale structure of the trial near x_*. (1) eps(r, theta0)/(r sin theta0) on the fine grid of
runs/pdisc/explore_fine.npz (~ eps_y(x, 0)), its oscillation and t-spectrum; (2) the axis trace g(x) = rho~_y(x, 0) minus a smooth
polynomial fit on [x_* - 0.15, x_* + 0.15]: amplitude of the remainder and of its derivatives; spectrum of g''''."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from modal_fit import Trial
XS = 8.600063805157177
d = np.load("runs/pdisc/explore_fine.npz"); t = d["t"]; eps = d["eps"]; r = np.exp(t); N = np.arange(eps.shape[1])
for th0 in [0.002, 0.01, 0.03]:
    e = eps @ np.sin((2 * N + 1) * th0); ey = e / (r * np.sin(th0))
    sel = (r > XS - 0.5) & (r < XS + 0.5)
    print("theta0 = %.3f: eps_y proxy on |s|<0.5: mean %.3e, max %.3e, min %.3e" % (th0, ey[sel].mean(), ey[sel].max(), ey[sel].min()))
    # local oscillation: subtract a running mean over 3 knot spacings (0.0058 in t)
    w = int(0.0058 / (t[1] - t[0]))
    ker = np.ones(w) / w; sm = np.convolve(ey, ker, mode="same")
    osc = ey - sm
    print("   knot-scale oscillation (ey - running mean over 3 knots) on |s|<0.5: rms %.3e, max %.3e" % (np.sqrt((osc[sel] ** 2).mean()), np.abs(osc[sel]).max()))
    # spectrum in t (periodogram) of ey on |s| < 0.5
    seg = ey[sel] - ey[sel].mean(); F = np.abs(np.fft.rfft(seg * np.hanning(len(seg)))); fr = np.fft.rfftfreq(len(seg), d=t[1] - t[0])
    top = np.argsort(F)[::-1][:6]
    print("   dominant t-frequencies (cycles per unit t) and amplitudes:", [(round(float(fr[i]), 1), float("%.2e" % F[i])) for i in top])
    print("   knot frequency 1/0.00194 = %.1f cycles per unit t" % (1 / 0.00194))
# (2) axis trace
T = Trial(np.load("data/trial_v2_h0.008.npz"))
x = np.linspace(XS - 0.15, XS + 0.15, 30001); tt = np.log(x)
g = x ** 2 * T.eval(tt, 0).sum(1)
for deg in [8, 12, 16, 20]:
    c = np.polynomial.chebyshev.chebfit((x - XS) / 0.15, g, deg); rem = g - np.polynomial.chebyshev.chebval((x - XS) / 0.15, c)
    print("axis g minus Chebyshev fit (deg %d): rms %.3e max %.3e (g ~ %.2f)" % (deg, np.sqrt((rem ** 2).mean()), np.abs(rem).max(), g.mean()))
# derivatives of the remainder via the exact representation: g'''' spectrum
St = {4: {1: -6, 2: 11, 3: -6, 4: 1}}
from math import comb
def Gd(t, nu): return sum(comb(nu, l) * 2.0 ** (nu - l) * np.exp(2 * t) * T.eval(t, l).sum(1) for l in range(nu + 1))
g4 = np.exp(-4 * tt) * sum(c * Gd(tt, i) for i, c in St[4].items())
print("g'''' on |s| < 0.15: mean %.2f, rms %.2f, max %.2f" % (g4.mean(), np.sqrt((g4 ** 2).mean()), np.abs(g4).max()))
F = np.abs(np.fft.rfft((g4 - g4.mean()) * np.hanning(len(g4)))); fr = np.fft.rfftfreq(len(g4), d=x[1] - x[0])
top = np.argsort(F)[::-1][:8]
print("dominant x-frequencies of g'''' (cycles per unit x):", [(round(float(fr[i]), 1), float("%.2e" % F[i])) for i in top], "; knot frequency 1/0.0165 = %.1f" % (1 / 0.0165))
# amplitude of the oscillatory part of g implied by g'''' at the knot frequency: a = A4 / (2 pi f)^4
kn = np.exp(T.knots[T.p + 1:-(T.p + 1)]); kn = kn[(kn > XS - 0.15) & (kn < XS + 0.15)]
print("knots (r) in range: %d, mean spacing %.5f" % (len(kn), np.diff(kn).mean()))
# per-knot-interval: mean and range of g''''
for a, b in zip(kn[:-1], kn[1:]):
    m = (x >= a) & (x < b)
    if m.sum() > 10 and abs(0.5 * (a + b) - XS) < 0.06:
        print("  interval [%+.4f, %+.4f]: g'''' min %8.1f max %8.1f mean %8.1f" % (a - XS, b - XS, g4[m].min(), g4[m].max(), g4[m].mean()))
