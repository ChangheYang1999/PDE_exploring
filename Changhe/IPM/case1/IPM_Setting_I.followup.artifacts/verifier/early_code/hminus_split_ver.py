"""verifier: lead notes S-18 (b), the amplitude split of B_3 (lead request (m)), own code (functions of hminus_ver.py).
At fixed w, Q = Q0 + Q1, Q0 = g'/(2 g^3), Q1 = -w''/(2 g^3); g -> mu g keeps the axis law (linear in g), Q0 -> mu^-2 Q0,
Q1 -> mu^-3 Q1, m -> m/mu, so B_3(mu) = mu^(-1-beta) (b0 + b1/mu) and B_3(mu) = 0 at mu_0 = -b1/b0.
b_i by the m-form (8) with Q_i, its own divergent part P_i and Q_i* = Q_i(x*).  P_i = the part of P of weight L^-5 (i = 0)
and L^-7 (i = 1) under x -> L u at fixed shape (d_n of weight L^(1-n)):
  P0 = m^5/A^5 + 3 d3 m^3/A^4 + (10 A d5 + 21 d3^2) m/(8 A^3),
  P1 = -3 d3 m^5/A^5 - (10 A d5 + 12 d3^2) m^3/A^4 - (168 A^2 d7 + 324 A d3 d5 + 144 d3^3) m/(8 A^3).
The series route checks that x^5 (Q_i - P_i) = O(x^6) separately (printed).
Exact on R12 (fixed shape in u, Q0 ~ L^-5, Q1 ~ L^-7): mu_0 = S_A/L^2, and (H_-) at mu iff mu >= 3A/L^2.
Usage: hminus_split_ver.py r12 | hminus_split_ver.py traces name1,name2,... [wppkey]"""
import sys
import json
import math
import numpy as np
from numpy.polynomial import legendre as Lg
from scipy.special import roots_jacobi
sys.path.insert(0, 'verifier/early_code')
from trace_axis import TraceAxis
from hminus_ver import N, mul, inv, sexp, spow, der, integ, down, up, ev, fit_w

D = 'first-run-records/ver/runs/gen4/'


def pcoef(d3, d5, d7, A):
    P0 = (1 / A ** 5, 3 * d3 / A ** 4, (10 * A * d5 + 21 * d3 ** 2) / (8 * A ** 3))
    P1 = (-3 * d3 / A ** 5, -(10 * A * d5 + 12 * d3 ** 2) / A ** 4, -(168 * A ** 2 * d7 + 324 * A * d3 * d5 + 144 * d3 ** 3) / (8 * A ** 3))
    return P0, P1


def series_split(wcoef, A, dAg):
    w = np.zeros(N + 1)
    w[:len(wcoef)] = wcoef[:N + 1]
    wt = down(w)
    Ag = np.zeros(N + 1)
    Ag[0], Ag[2] = A, dAg
    r = mul(der(w) - Ag, inv(wt))
    r[0] = 0.0
    gh = sexp(integ(down(r)))
    g = up(up(gh))
    ig3 = inv(2 * mul(gh, mul(gh, gh)))
    qt = [mul(down(der(g)), ig3), mul(-down(der(der(w))), ig3)]
    mm = mul(-wt, inv(gh))
    m3 = mul(mm, mul(mm, mm))
    Ps = pcoef(w[3], w[5], w[7], A)
    difs = []
    for qti, (q5, q3, q1) in zip(qt, Ps):
        difs.append(qti - (q5 * mul(m3, mul(mm, mm)) + q3 * up(up(m3)) + q1 * up(up(up(up(mm))))))
    return Ps, difs, mm, gh, Ag


def parts01(ad, x):
    W, G = ad.interp('w', x), ad.interp('g', x)
    w, wpp, g, gp = W[0], 2 * W[2], G[0], G[1]
    return gp / (2 * g ** 3), -wpp / (2 * g ** 3), -w / g, g


def b3_part(ad, i, qs, Qs, dif, mm, gh, Agser, A, be, dAg, xs):
    q5, q3, q1 = qs
    x1, x2 = 0.06 * xs, 0.97 * xs
    Rser = np.concatenate([dif[5:], np.zeros(5)])
    Rser[0] -= Qs
    Sx = mul(mul(Rser, spow(mm, be - 2)), mul(Agser, inv(gh)))
    n = np.arange(N - 8)
    I0 = float(np.sum(Sx[n] * x1 ** (n + 1 - be) / (n + 1 - be)))

    def Rfun(xx):
        Q0, Q1, m, g = parts01(ad, xx)
        Q = (Q0, Q1)[i]
        return Q - (q5 * m ** 5 + q3 * m ** 3 + q1 * m) - Qs, m, g
    tb = np.linspace(math.log(x1), math.log(x2), 41)
    gx, gw = Lg.leggauss(20)
    I1 = 0.0
    for a, b in zip(tb[:-1], tb[1:]):
        xx = np.exp(a + (gx + 1) * (b - a) / 2)
        R, m, g = Rfun(xx)
        I1 += np.sum(gw * (b - a) / 2 * R * m ** (be - 2) * (A + dAg * xx ** 2) / g * xx)
    d = xs - x2
    sg = 0.01 + 0.99 * (np.cos(np.pi * (np.arange(120) + 0.5) / 120) + 1) / 2
    R, m, g = Rfun(xs - d * sg)
    tau = d * sg
    cr = np.polynomial.chebyshev.Chebyshev.fit(sg, R / tau, 8, domain=[0, 1])
    cm = np.polynomial.chebyshev.Chebyshev.fit(sg, m / tau, 8, domain=[0, 1])
    cg = np.polynomial.chebyshev.Chebyshev.fit(sg, g, 8, domain=[0, 1])
    zj, wj = roots_jacobi(30, be - 1, 0.0)
    s2 = (1 - zj) / 2
    f = cr(s2) * cm(s2) ** (be - 2) * (A + dAg * (xs - d * s2) ** 2) / cg(s2)
    I2 = float(d ** be * np.sum(wj * f) / 2 ** be)
    return float((be - 1) / (3 * A ** be) * (I0 + I1 + I2) * xs ** (4 + be))


def analyse(path, label, kw):
    ad = TraceAxis(path, reg='Ag', **kw)
    xs, mu1 = ad.xs, ad.mu1
    A = 2 * ad.c_l_file - 1
    be = 2 / A
    dAg = (mu1 - A) / xs ** 2
    z = np.load(path, allow_pickle=True)
    xd, wd = np.asarray(z['x']), np.asarray(z['w'])
    Q0s, Q1s, _, _ = parts01(ad, np.array([xs]))
    rows = []
    for xf, deg in [(2.0, 8), (2.0, 10), (2.6, 10)]:
        wc, res = fit_w(xd, wd, A, xf, deg)
        Ps, difs, mm, gh, Agser = series_split(wc, A, dAg)
        low = [float(np.abs(dd[:6]).max()) for dd in difs]
        b = [b3_part(ad, i, Ps[i], (Q0s, Q1s)[i][0], difs[i], mm, gh, Agser, A, be, dAg, xs) for i in (0, 1)]
        # R0, R1 in natural units at a few u (pointwise), and the (H_-) threshold in mu: R0 + R1/mu <= 0
        uu = np.linspace(0.06, 0.9995, 2000)
        Q0, Q1, m, g = parts01(ad, uu * xs)
        Rp = [((Q0, Q1)[i] - (Ps[i][0] * m ** 5 + Ps[i][1] * m ** 3 + Ps[i][2] * m) - (Q0s, Q1s)[i][0]) * xs ** 5 for i in (0, 1)]
        pos = Rp[1] > 0
        mu_H = float(np.max(-Rp[1][pos] / Rp[0][pos])) if pos.any() else 0.0     # R0 < 0 assumed (checked below)
        rows.append(dict(xf=xf, deg=deg, low=low, b0=b[0], b1=b[1], mu0=-b[1] / b[0], B3=b[0] + b[1], mu_H=mu_H,
                         R0max=float(Rp[0].max()), R0_u=[float(np.interp(v, uu, Rp[0])) for v in (0.1, 0.5, 0.9, 0.98)],
                         R1_u=[float(np.interp(v, uu, Rp[1])) for v in (0.1, 0.5, 0.7, 0.9, 0.98)]))
    return dict(label=label, A=A, x_star=xs, rows=rows)


if __name__ == '__main__':
    VAR = {'near3': dict(near_frac=0.03), 'ls24n3': dict(fit01=(24, 11), fit2=(24, 11), near_frac=0.03)}
    res = []
    if sys.argv[1] == 'r12':
        A, Lv = 10.150725, 8.6
        SA = 6 * A * (4 * A - 3) / (8 * A - 1)
        print('R12 L = 8.6: exact mu_0 = S_A/L^2 = %.6f, (H_-) threshold 3A/L^2 = %.6f, B_3^nat = %.10f' % (
            SA / Lv ** 2, 3 * A / Lv ** 2, 0.530666623156826 * (1 - SA / Lv ** 2)))
        for vn in VAR:
            res.append(analyse('verifier/early_data/traces/r12_L8.6_n0.npz', 'R12 ' + vn, VAR[vn]))
        tag = 'r12'
    else:
        key = sys.argv[3] if len(sys.argv) > 3 else 'wpp_ode'
        for nm in sys.argv[2].split(','):
            for vn in VAR:
                res.append(analyse(D + nm + '_traces.npz', nm + ':' + key + ':' + vn, dict(VAR[vn], wppkey=key)))
        tag = 'traces_' + key
    for r in res:
        print(r['label'], 'x* %.5f' % r['x_star'])
        for row in r['rows']:
            print('   xf %.1f deg %d: low coeffs %.0e %.0e | b0 %.5f b1 %.5f B3 %.5f mu_0 %.4f | (H_-) for mu >= %.4f | max R0 %.3e,'
                  ' R0(u=.1,.5,.9,.98) %s, R1(u=.1,.5,.7,.9,.98) %s' % (
                      row['xf'], row['deg'], row['low'][0], row['low'][1], row['b0'], row['b1'], row['B3'], row['mu0'], row['mu_H'],
                      row['R0max'], ' '.join('%+.4f' % v for v in row['R0_u']), ' '.join('%+.4f' % v for v in row['R1_u'])), flush=True)
    json.dump(res, open('verifier/early_data/hminus_split_ver_%s.json' % tag, 'w'), indent=1)
