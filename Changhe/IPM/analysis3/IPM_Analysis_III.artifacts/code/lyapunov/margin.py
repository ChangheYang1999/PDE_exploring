"""NUMERICAL: pointwise Garding-Lyapunov margin m(X) = b0 + (1/2) mu'(t) V.X/r^2 - b_+(X) for a radial weight
w = e^{mu(log r)} on the exact-join modal trial. b_+ = (|grad rho| - rho_y)/2 is the coupling cost of the square identity."""
import numpy as np, sys
d = np.load(sys.argv[1] if len(sys.argv) > 1 else 'field.npz'); t = d['t']; th = d['th']; r = np.exp(t)
cl = float(d['cl']); b0 = 1 + cl
rx, ry, V1, V2 = d['rho_x'], d['rho_y'], d['V1'], d['V2']
bp = (np.hypot(rx, ry) - ry) / 2
c, s = np.cos(th)[None, :], np.sin(th)[None, :]
q = (V1 * c + V2 * s) / r[:, None]
def best_delta(gam):
    # maximize delta s.t. exists mu'(t) with mu' q >= 2(bp - b0 + delta) for all theta, and mu' = -2 gam for t >= tf
    lo_d, hi_d = 0.0, b0
    for _ in range(40):
        dm = 0.5 * (lo_d + hi_d); rho = 2 * (bp - b0 + dm)
        ok = True
        for i in range(len(t)):
            pos = q[i] > 1e-12; neg = q[i] < -1e-12
            L = (rho[i, pos] / q[i, pos]).max() if pos.any() else -np.inf
            H = (rho[i, neg] / q[i, neg]).min() if neg.any() else np.inf
            if L > H: ok = False; break
        if ok: lo_d = dm
        else: hi_d = dm
    return lo_d
dstar = best_delta(0.9)
print('best delta with free radial mu (grid):', dstar)
# explicit smooth choice: mu'(t) = midpoint-ish of the window for delta = 0.5, joined to -2 gam
gam = 0.9; dl = 0.5; rho = 2 * (bp - b0 + dl)
lo = np.array([(rho[i, q[i] > 0] / q[i, q[i] > 0]).max() if (q[i] > 0).any() else -np.inf for i in range(len(t))])
hi = np.array([(rho[i, q[i] < 0] / q[i, q[i] < 0]).min() if (q[i] < 0).any() else np.inf for i in range(len(t))])
mup = np.maximum(lo + 0.25, -2 * gam); mup = np.minimum(mup, hi - 0.25)
# smooth with a Gaussian in t (width 0.3) and re-check
dt = t[1] - t[0]; ker = np.exp(-0.5 * (np.arange(-60, 61) * dt / 0.3) ** 2); ker /= ker.sum()
pad = np.r_[np.full(60, mup[0]), mup, np.full(60, mup[-1])]
mus = np.convolve(pad, ker, mode='valid')
m = b0 + 0.5 * mus[:, None] * q - bp
i, j = np.unravel_index(m.argmin(), m.shape)
print('explicit smoothed mu\': min margin %.4f at r=%.4g th=%.4f; mu\' range [%.3f, %.3f]; mu\'(end)=%.3f' %
      (m.min(), r[i], th[j], mus.min(), mus.max(), mus[-1]))
mu = np.cumsum(mus) * dt; print('total variation of mu over grid: %.3f (weight ratio e^mu: %.3g)' % (mu.max() - mu.min(), np.exp(mu.max() - mu.min())))
np.savez('mu_choice.npz', t=t, mup=mus, margin_min=m.min())
