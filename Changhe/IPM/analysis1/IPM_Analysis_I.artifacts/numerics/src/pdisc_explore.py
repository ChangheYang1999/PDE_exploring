"""Floating exploration (evidence only): residual modes eps_N(t) of the trial on a fine log-radial grid around the source radius
x_*, to locate the fine structure of eps~ (scale in t and in theta) before the H^s norm computation.
Usage: python3 pdisc_explore.py trial.npz t_lo t_hi dt out.npz
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from modal_fit import Trial
from trial_green import TrialGreen

path, tlo, thi, dt, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
T = Trial(np.load(path)); G = TrialGreen(T)
t0 = time.time(); G.build(); print("build %.1fs" % (time.time() - t0), flush=True)
t = np.arange(tlo, thi + 0.5 * dt, dt)
t1 = time.time(); A, B = G.AB_at(t); print("AB_at at %d radii: %.1fs" % (len(t), time.time() - t1), flush=True)
t1 = time.time(); eps = G.residual_modes(t); print("residual_modes: %.1fs" % (time.time() - t1), flush=True)
np.savez_compressed(out, t=t, eps=eps)
r = np.exp(t); W = np.abs(eps).sum(1)
# knots of the trial in this range
kn = T.knots[T.p + 1:-(T.p + 1)]; kn = kn[(kn > tlo) & (kn < thi)]
print("knots in range (t):", np.round(kn, 5))
print("knot spacing in t: min %.4g max %.4g" % (np.diff(kn).min(), np.diff(kn).max()))
# mode decay at the W peak
i = np.argmax(W); print("W peak %.3e at r = %.5f (t = %.6f)" % (W[i], r[i], t[i]))
N = np.arange(eps.shape[1])
for Nc in [10, 20, 40, 80, 160, 320]:
    print("  sum_{N>=%d} |eps_N| at peak: %.3e" % (Nc, np.abs(eps[i, Nc:]).sum()))
# derivative structure by finite differences in t (float evidence)
d1 = np.gradient(eps, dt, axis=0); d2 = np.gradient(d1, dt, axis=0)
print("sup_t sum_N|d_t eps_N| = %.3e ; sum_N|d_t^2 eps_N| = %.3e" % (np.abs(d1).sum(1).max(), np.abs(d2).sum(1).max()))
# sup over theta on a dense grid, and the theta location of the max, at a few radii around the peak
th = np.linspace(0, np.pi / 2, 4001); S = np.sin((2 * N[:, None] + 1) * th[None, :])
for rr in [8.55, 8.58, 8.60, 8.62, 8.65, 8.70, 8.75, 8.79, 8.85, 8.9, 9.0]:
    j = np.argmin(np.abs(r - rr)); E = eps[j] @ S; kk = np.argmax(np.abs(E))
    print("  r = %.3f: W = %.3e sup_theta|eps| = %.3e at theta = %.4f ; eps(theta=0.01) = %.3e" % (r[j], W[j], np.abs(E).max(), th[kk], eps[j] @ np.sin((2 * N + 1) * 0.01)))
