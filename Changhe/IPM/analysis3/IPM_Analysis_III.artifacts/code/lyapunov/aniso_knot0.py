"""NUMERICAL: grid margin for the anisotropic weight w_a = |cos th|^{-2a} e^{mu_a(log r)}, mu_a(t) = -2a t (t < 0),
-(5/4) t (t >= 0). In r < 1 this is exactly |x|^{-2a} (the Theorem O weight with b = 0). Margin
m = b0 + (mu_a'/2) q + a T_ang - b_+, with T_ang = tan(th) V.grad(th) = sin(th) V_2/r - sin(th)^2 V_1/x."""
import numpy as np, json
d = np.load('field.npz'); t = d['t']; th = d['th']; r = np.exp(t); cl = float(d['cl']); b0 = 1 + cl
bp = (np.hypot(d['rho_x'], d['rho_y']) - d['rho_y']) / 2
C, S = np.cos(th)[None, :], np.sin(th)[None, :]
q = (d['V1']*C + d['V2']*S) / r[:, None]; vth = (-d['V1']*S + d['V2']*C) / r[:, None]
J = slice(1, -1); out = {}
for a in (4.1, 4.25, 4.4):
    Tang = np.tan(th[J])[None, :]*vth[:, J]
    mup = np.where(t < 0, -2*a, -1.25)[:, None]
    m = b0 + 0.5*mup*q[:, J] + a*Tang - bp[:, J]
    i0 = np.argmin(np.abs(t)); mk = min((b0 + 0.5*v*q[i0, J] + a*Tang[i0] - bp[i0, J]).min() for v in (-2*a, -1.25))
    i, j = np.unravel_index(m.argmin(), m.shape)
    reg = {lab: float(m[sl].min()) for lab, sl in [('r<0.1', r < 0.1), ('0.1<r<5', (r > 0.1) & (r < 5)),
                                                    ('5<r<60', (r > 5) & (r < 60)), ('r>60', r > 60)]}
    out['%.2f' % a] = dict(min_margin=float(min(m.min(), mk)), at_knot_both_values=float(mk), argmin_r=float(r[i]),
                           argmin_theta=float(th[J][j]), regions=reg, Tang_min=float(Tang.min()), Tang_max=float(Tang.max()))
    print('a=%.2f min %.4f (knot row, both values %.4f) argmin r=%.3g th=%.3f' % (a, min(m.min(), mk), mk, r[i], th[J][j]), reg,
          'T_ang range [%.3f, %.3f]' % (Tang.min(), Tang.max()))
json.dump(out, open('aniso_knot0.json', 'w'), indent=1)
