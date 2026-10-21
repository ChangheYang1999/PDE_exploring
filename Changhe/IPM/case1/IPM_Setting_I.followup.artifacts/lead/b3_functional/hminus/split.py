"""Amplitude split of the sign criterion. At fixed axis velocity w, Q = (g' - w'')/(2 g^3) = Q0 + Q1 with
Q0 = g'/(2 g^3), Q1 = -w''/(2 g^3). Under g -> mu g (density amplitude on the axis, a(0) -> mu a(0)), Q0 -> mu^-2 Q0,
Q1 -> mu^-3 Q1, m -> m/mu, so with b_i = ((beta-1)/(3 A^beta)) int (Q_i - P_i(m) - Q_i(x*)) m^(beta-2) dm (P_i the divergent
part of Q_i) one has B_3(mu) = mu^(-1-beta) (b0 + b1/mu): B_3 = 0 at mu_0 = -b1/b0, and (H_-) holds iff
R0 + R1/mu <= 0 on (0, x*), R_i = x*^5 (Q_i - P_i - Q_i(x*)). Reports mu_0 and the (H_-) range of mu.
Same fit windows and quadrature as hminus.py. R12 check: mu_0 = S_A/L^2, (H_-) iff mu >= 3A/L^2.
Usage: python3 split.py r12 L | python3 split.py trace name1,name2,... [wppkey]"""
import sys, json, itertools
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dcode'))
from vb3ibp import build

D = os.environ.get('TRACE_DIR', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'traces')) + os.sep


def part(x, Q, Qs, m, g, Ag, ok, xs, be, A, xlof, xcf, K):
    sel = ok & (x >= xlof * xs) & (x <= xcf * xs)
    z = m[sel] ** -2; zc = z.max()
    c = np.polyfit(z / zc, Q[sel] / m[sel] ** 5, K)[::-1]
    c = c / zc ** np.arange(len(c))
    P = c[0] * m ** 5 + c[1] * m ** 3 + c[2] * m
    R = (Q - P - Qs) * xs ** 5
    f = (R / xs ** 5) * m ** (be - 2) * Ag / g
    s = ok & (x >= xlof * xs) & (x / xs < 0.995)
    sp = CubicSpline(np.log(x[s]), f[s] * x[s])
    I_mid = float(sp.integrate(np.log(x[s][0]), np.log(x[s][-1])))
    x0 = x[s][0]
    I_lo = quad(lambda t: (-Qs + c[3] / (A / t)) * (A / t) ** (be - 2) * A / t ** 2, 0, x0, limit=200)[0]
    me = m[s][-1]; Re = R[s][-1] / xs ** 5
    I_hi = Re / me * me ** be / be
    B = (be - 1) / (3 * A ** be) * (I_lo + I_mid + I_hi) * xs ** (4 + be)
    return R, float(B), c


def analyse(x, w, wp, wpp, cl, label):
    d = build(x, w, wp, wpp, cl)
    xs, be, A = d['xs'], d['be'], d['A']
    g, a2 = d['g'], d['a2']
    u = np.log(x)
    gp = a2 * 2 + wpp                       # g' as rebuilt by build (a2 = (g' - w'')/2)
    gps, gs, wpps = CubicSpline(u, gp), CubicSpline(u, g), CubicSpline(u, wpp)
    gst = float(gs(np.log(xs)))
    Q0, Q1 = gp / (2 * g ** 3), -wpp / (2 * g ** 3)
    Q0s, Q1s = float(gps(np.log(xs))) / (2 * gst ** 3), -float(wpps(np.log(xs))) / (2 * gst ** 3)
    m = -w / g
    Ag = A + (d['mu1'] - A) * (x / xs) ** 2
    ok = d['keep'] & (x < xs) & (x > 0)
    uu = x / xs
    band = ok & (uu >= 0.06) & (uu < 0.999)
    rows = []
    mus = np.geomspace(0.05, 20, 4001)
    for xlof, xcf, K in itertools.product((0.02, 0.04), (0.2, 0.3), (4, 5, 6)):
        R0, b0, c0 = part(x, Q0, Q0s, m, g, Ag, ok, xs, be, A, xlof, xcf, K)
        R1, b1, c1 = part(x, Q1, Q1s, m, g, Ag, ok, xs, be, A, xlof, xcf, K)
        Rt, bt, _ = part(x, Q0 + Q1, Q0s + Q1s, m, g, Ag, ok, xs, be, A, xlof, xcf, K)
        r0, r1 = R0[band], R1[band]
        hold = np.array([np.all(r0 + r1 / mu <= 0) for mu in mus])
        rows.append(dict(xlo=xlof, xc=xcf, K=K, b0=b0, b1=b1, b_total=bt, mu0=-b1 / b0,
                         muH_min=float(mus[hold].min()) if hold.any() else None,
                         muH_max=float(mus[hold].max()) if hold.any() else None,
                         R0_u=[float(np.interp(v, uu[band], r0)) for v in (0.1, 0.3, 0.5, 0.7, 0.9, 0.98)],
                         R1_u=[float(np.interp(v, uu[band], r1)) for v in (0.1, 0.3, 0.5, 0.7, 0.9, 0.98)],
                         q5A5_0=float(c0[0] * A ** 5), q5A5_1=float(c1[0] * A ** 5)))
    med = lambda k: float(np.median([r[k] for r in rows if r[k] is not None]))
    out = dict(label=label, c_l=cl, A=A, x_star=xs, g_star=gst, w2_star=float(wpps(np.log(xs))),
               Q0s_nat=Q0s * xs ** 5, Q1s_nat=Q1s * xs ** 5,
               b0_median=med('b0'), b1_median=med('b1'), b_total_median=med('b_total'), mu0_median=med('mu0'),
               mu0_range=[min(r['mu0'] for r in rows), max(r['mu0'] for r in rows)],
               muH_min_median=med('muH_min'), muH_min_range=[min(r['muH_min'] for r in rows if r['muH_min']),
                                                             max(r['muH_min'] for r in rows if r['muH_min'])],
               R0_u_median=[float(np.median([r['R0_u'][i] for r in rows])) for i in range(6)],
               R1_u_median=[float(np.median([r['R1_u'][i] for r in rows])) for i in range(6)], rows=rows)
    print('%s: x* %.5f g* %.4f w''(x*) %.4e | Q0* nat %.4e Q1* nat %.4e | b0 %.4f b1 %.4f (sum %.4f, direct %.4f) | '
          'mu0 = -b1/b0 median %.4f range [%.4f, %.4f] | (H_-) for mu >= %.4f (range [%.4f, %.4f]) | R0 at u=.1..0.98 %s '
          '| R1 %s' % (label, xs, gst, out['w2_star'], out['Q0s_nat'], out['Q1s_nat'], out['b0_median'], out['b1_median'],
                       out['b0_median'] + out['b1_median'], out['b_total_median'], out['mu0_median'], *out['mu0_range'],
                       out['muH_min_median'], *out['muH_min_range'], ['%.3f' % v for v in out['R0_u_median']],
                       ['%.3f' % v for v in out['R1_u_median']]), flush=True)
    return out


if __name__ == '__main__':
    mode = sys.argv[1]
    res = []
    if mode == 'r12':
        Lv = float(sys.argv[2]); cl = 5.5753626; A = 2 * cl - 1
        z = np.load(D + 'c6g_traces.npz', allow_pickle=True)
        x = z['x'] * (Lv / 8.6000638)
        import sympy as sp
        t = sp.symbols('t', positive=True)
        wS = -A * t * (1 - (t / Lv) ** 2) / (1 + (t / Lv) ** 2)
        w, wp, wpp = [sp.lambdify(t, sp.diff(wS, t, j), 'numpy')(x) for j in range(3)]
        SA = 6 * A * (4 * A - 3) / (8 * A - 1)
        print('R12 L=%.4f expected mu0 = S_A/L^2 = %.6f, (H_-) iff mu >= 3A/L^2 = %.6f' % (Lv, SA / Lv ** 2, 3 * A / Lv ** 2))
        res.append(analyse(x, w, wp, wpp, cl, 'R12 L=%.4f' % Lv))
        tag = 'r12_%.4f' % Lv
    else:
        key = sys.argv[3] if len(sys.argv) > 3 else 'wpp_ode'
        for nm in sys.argv[2].split(','):
            z = np.load(D + nm + '_traces.npz', allow_pickle=True)
            res.append(analyse(z['x'], z['w'], z['wp'], z[key], float(z['c_l']), nm + ':' + key))
        tag = 'traces_' + key
    json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'split_%s.json' % tag), 'w'), indent=1)
