"""Pointwise test of the sufficient condition H_- for B_3 > 0 (A > 2) on sampled axis traces:
   R(x) = Q(x) - P(m(x)) - Q(x*) <= 0 on (0, x*),  Q = (g' - w'')/(2 g^3),  m = -w/g,
P(m) = q5 m^5 + q3 m^3 + q1 m the divergent part of Q at m -> infinity (Q - P = O(1/m)). g, g', Q(x*) by the run-1
machinery (vb3ibp.build: reconstruction of g with the near-x* regularization A_g). P is obtained by fitting Q/m^5 as a
polynomial in m^-2 on [xlo, xc] (the subtraction is characterized by Q - P = O(1/m); no separate fit of d3, d5, d7).
Natural units: R_nat = x*^5 R. Also B_3^nat from the convergent formula B_3 = (beta-1)/(3 A^beta) int R m^(beta-2) dm,
dm = -(A_g/g) dx, as a consistency check of the subtraction.
Usage: python3 hminus.py r12 L | python3 hminus.py trace name1,name2,... [wppkey]"""
import sys, json, itertools
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dcode'))
from vb3ibp import build

D = os.environ.get('TRACE_DIR', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'traces')) + os.sep


def analyse(x, w, wp, wpp, cl, label):
    d = build(x, w, wp, wpp, cl)
    xs, be, A = d['xs'], d['be'], d['A']
    g, a2 = d['g'], d['a2']
    Q = a2 / g ** 3
    Qs = d['kappa']
    m = -w / g
    Ag = A + (d['mu1'] - A) * (x / xs) ** 2
    ok = d['keep'] & (x < xs) & (x > 0)
    rows = []
    for xlof, xcf, K in itertools.product((0.02, 0.04), (0.2, 0.3), (4, 5, 6)):
        sel = ok & (x >= xlof * xs) & (x <= xcf * xs)
        z = m[sel] ** -2; zc = z.max()
        c = np.polyfit(z / zc, Q[sel] / m[sel] ** 5, K)[::-1]   # c[0] + c[1] z + c[2] z^2 + ... (scaled variable)
        c = c / zc ** np.arange(len(c))
        P = c[0] * m ** 5 + c[1] * m ** 3 + c[2] * m
        R = (Q - P - Qs) * xs ** 5
        u = x / xs
        # max over u in [0.06, 0.999]: below 0.06 the fit's truncation error is amplified by m^5 (on exact R12 data a
        # K = 4 fit on [0.02, 0.3] gives a spurious +4 at u = 0.02); there R = -Q* + c3/m + ... is reported instead
        band = ok & (u >= 0.06) & (u < 0.999)
        Rb = R[band]
        # B_3 from (8): below xlo use R = -Qs + r1/m with r1 = c[3] (Q - P = c3/m + ...)
        f = (R / xs ** 5) * m ** (be - 2) * Ag / g
        s = ok & (x >= xlof * xs) & (u < 0.995)
        sp = CubicSpline(np.log(x[s]), f[s] * x[s])
        I_mid = float(sp.integrate(np.log(x[s][0]), np.log(x[s][-1])))
        x0 = x[s][0]
        mf = CubicSpline(np.log(x[s]), np.log(m[s]))
        I_lo = quad(lambda t: (-Qs + c[3] / (A / t)) * (A / t) ** (be - 2) * A / t ** 2, 0, x0, limit=200)[0]
        # tail (0.995 x*, x*): R ~ R(u_e) (m/m_e)^1 (linear in m), integrate in m exactly
        me = m[s][-1]; Re = R[s][-1] / xs ** 5
        I_hi = Re / me * me ** be / be
        B3 = (be - 1) / (3 * A ** be) * (I_lo + I_mid + I_hi) * xs ** (4 + be)
        imax = np.argmax(Rb)
        rows.append(dict(xlo=xlof, xc=xcf, K=K, q5A5=float(c[0] * A ** 5), Rmax=float(Rb.max()), u_at_max=float(u[band][imax]),
                         frac_pos=float((Rb > 0).mean()), R_origin_model_u006=float((-Qs + c[3] * (0.06 * xs) / A) * xs ** 5), R_u=[float(np.interp(v, u[band], Rb)) for v in (0.1, 0.3, 0.5, 0.7, 0.9, 0.98)],
                         B3_formula8=float(B3)))
    Rm = np.array([r['Rmax'] for r in rows]); Bm = np.array([r['B3_formula8'] for r in rows])
    out = dict(label=label, c_l=cl, A=A, x_star=xs, minus_Qs_nat=float(-Qs * xs ** 5), mu1_rel=float((d['mu1'] - A) / A),
               Rmax_min=float(Rm.min()), Rmax_max=float(Rm.max()), Rmax_median=float(np.median(Rm)),
               B3_formula8_median=float(np.median(Bm)), B3_formula8_range=[float(Bm.min()), float(Bm.max())],
               R_u_median=[float(np.median([r['R_u'][i] for r in rows])) for i in range(6)], rows=rows)
    print('%s: c_l %.7f x* %.5f -Q* nat %.5e | max R_nat over windows [%.3e, %.3e] (median %.3e, u_at_max %s) | R_nat at '
          'u=.1,.3,.5,.7,.9,.98: %s | B3 by (8): median %.4f range [%.4f, %.4f]' % (
              label, cl, xs, out['minus_Qs_nat'], Rm.min(), Rm.max(), np.median(Rm),
              sorted(set(round(r['u_at_max'], 3) for r in rows))[:4], ['%.3e' % v for v in out['R_u_median']],
              out['B3_formula8_median'], Bm.min(), Bm.max()), flush=True)
    return out


if __name__ == '__main__':
    mode = sys.argv[1]
    res = []
    if mode == 'r12':
        Lv = float(sys.argv[2]); cl = 5.5753626; A = 2 * cl - 1
        z = np.load(D + 'c6g_traces.npz', allow_pickle=True)
        x = z['x'] * (Lv / 8.6000638)
        u = x / Lv
        import sympy as sp
        t = sp.symbols('t', positive=True)
        wS = -A * t * (1 - (t / Lv) ** 2) / (1 + (t / Lv) ** 2)
        w, wp, wpp = [sp.lambdify(t, sp.diff(wS, t, j), 'numpy')(x) for j in range(3)]
        k = A / Lv ** 2
        ex = lambda v: (1 - 6 * k) * (v ** 5 - 1) + (1 + 2 * k) * (v ** 3 - 1)
        print('R12 L=%.6f exact R_nat at u=.1,.3,.5,.7,.9,.98: %s ; exact max %.3e' % (
            Lv, ['%.3e' % ex(v) for v in (0.1, 0.3, 0.5, 0.7, 0.9, 0.98)], ex(np.linspace(1e-3, 0.999, 9999)).max()))
        res.append(analyse(x, w, wp, wpp, cl, 'R12 L=%.4f' % Lv))
        tag = 'r12_%.4f' % Lv
    else:
        key = sys.argv[3] if len(sys.argv) > 3 else 'wpp_ode'
        for nm in sys.argv[2].split(','):
            z = np.load(D + nm + '_traces.npz', allow_pickle=True)
            res.append(analyse(z['x'], z['w'], z['wp'], z[key], float(z['c_l']), nm + ':' + key))
        tag = 'traces_' + key
    json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out_%s.json' % tag), 'w'), indent=1)
