"""NUMERICAL: explicit closed-form radial weight derivative mu'(t) (two tanh steps) for the margin hypothesis (H_m)
of Theorem R on the exact-join modal trial; maximizes the grid minimum of m(X) = b0 + mu'(t) q/2 - b_+.
mu'(t) = m0 + (m1 - m0) H((t - ta)/wa) - (m1 - minf) H((t - tb)/wb),  H(z) = (1 + tanh z)/2."""
import numpy as np, json
from scipy.optimize import minimize
d = np.load('field.npz'); t = d['t']; th = d['th']; r = np.exp(t); cl = float(d['cl']); b0 = 1 + cl
bp = (np.hypot(d['rho_x'], d['rho_y']) - d['rho_y']) / 2
c, s = np.cos(th)[None, :], np.sin(th)[None, :]
q = (d['V1'] * c + d['V2'] * s) / r[:, None]
H = lambda z: 0.5 * (1 + np.tanh(z))
def mup(p, tt):
    m0, m1, minf, ta, wa, tb, wb = p
    return m0 + (m1 - m0) * H((tt - ta) / wa) - (m1 - minf) * H((tt - tb) / wb)
def margin(p):
    return b0 + 0.5 * mup(p, t)[:, None] * q - bp
def obj(p):
    m0, m1, minf, ta, wa, tb, wb = p
    pen = 0
    if minf > -0.9: pen += 10 * (minf + 0.9)      # residual r^{2k-1} must be in L^2(e^mu): mu'(inf) < -4k = -0.717
    if wa < 0.05 or wb < 0.05: pen += 10
    M = np.max(np.abs(mup(p, np.linspace(-50, 50, 20001))))
    if M > 1.9: pen += 10 * (M - 1.9)
    return -margin(p).min() + pen
p0 = np.array([0.3, 1.5, -1.5, 1.75, 0.2, 4.5, 1.0])
res = minimize(obj, p0, method='Nelder-Mead', options=dict(maxiter=4000, xatol=1e-4, fatol=1e-5))
p = res.x; m = margin(p); i, j = np.unravel_index(m.argmin(), m.shape)
out = dict(params=dict(zip(['m0', 'm1', 'minf', 'ta', 'wa', 'tb', 'wb'], [float(x) for x in p])),
           grid_min_margin=float(m.min()), argmin_r=float(r[i]), argmin_theta=float(th[j]),
           sup_abs_mup=float(np.max(np.abs(mup(p, np.linspace(-50, 50, 20001))))))
for name, sel in [('r<0.1', r < 0.1), ('0.1<r<5', (r >= 0.1) & (r < 5)), ('5<r<60', (r >= 5) & (r < 60)), ('r>60', r >= 60)]:
    out['min_margin_' + name] = float(m[sel].min())
print(json.dumps(out, indent=1)); json.dump(out, open('mu_explicit.json', 'w'), indent=1)
