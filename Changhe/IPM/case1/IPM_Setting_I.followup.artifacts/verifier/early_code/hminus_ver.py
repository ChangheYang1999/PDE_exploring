"""verifier: (H_-) and B_3 by the convergent m-form (8) on the stored fixed-c_l gen4 traces (lead request (l3)), own code.
  R(x) = Q(x) - P(m(x)) - Q*,  Q = (g' - w'')/(2 g^3),  m = -w/g,  Q* = Q(x*),  P(m) = q5 m^5 + q3 m^3 + q1 m,
  (H_-): R <= 0 on (0, x*);  B_3 = ((beta - 1)/(3 A^beta)) int_0^x* R m^(beta-2) (A_g/g) dx   (dm = -(A_g/g) dx).
Data: TraceAxis (code/trace_axis.py) with reg = 'Ag' (A_g = A + (mu1 - A)(x/x*)^2, A = 2 c_l - 1 of the file, so that
g ~ x^2 at 0 and h = 1 at x*).  Natural units: R_nat = x*^5 R, B_3^nat = x*^(4+beta) B_3.
P by two independent routes:
 (S) from w alone: least squares of (w/x + A)/x^2 as a polynomial in x^2 on [x0, xf]; power-series arithmetic of the
     fitted w (with the A_g of the regularization) gives the series of x^5 Q and x m, and q5, q3, q1 by matching the
     x^0, x^2, x^4 coefficients (= fred11 03 (4) when A_g = A; the difference is printed); the series also gives R near 0
     (Q - P = O(x), no cancellation).
 (M) the subtraction characterised by Q - P = O(1/m): least squares of Q/m^5 as a polynomial in m^-2 on [xlo, xc]
     (TraceAxis Q, m); this is the idea of the lead's hminus.py, implemented here independently.
R pointwise from TraceAxis on [0.06, 0.9995] x*; on (0, 0.06 x*) the series of (S).
B_3 by (8): [0, 0.06 x*] series term by term (integrand x^(-beta) S(x)); [0.06, 0.97] x* Gauss-Legendre panels in log x;
[0.97 x*, x*]: R = tau r(tau), m = tau mu(tau), tau = x* - x, r and mu Chebyshev least-squares fits, Gauss-Jacobi weight
tau^(beta-1).
Usage: hminus_ver.py r12                     (exact R12 data, L = 8.6: validation against the closed forms)
       hminus_ver.py traces name1,name2,... [wppkey]"""
import sys
import json
import math
import numpy as np
from numpy.polynomial import legendre as Lg
from scipy.special import roots_jacobi
sys.path.insert(0, 'verifier/early_code')
from trace_axis import TraceAxis, _parts

D = 'first-run-records/ver/runs/gen4/'
N = 40
UL = (0.06, 0.1, 0.3, 0.5, 0.7, 0.9, 0.98, 0.995)


# ---- truncated power series in x (float64, length N + 1) ----
def mul(a, b):
    return np.convolve(a, b)[:N + 1]


def inv(a):
    c = np.zeros(N + 1)
    c[0] = 1 / a[0]
    for n in range(1, N + 1):
        c[n] = -np.dot(a[1:n + 1], c[n - 1::-1][:n]) / a[0]
    return c


def sexp(a):
    f = np.zeros(N + 1)
    f[0] = 1.0
    for n in range(1, N + 1):
        k = np.arange(1, n + 1)
        f[n] = np.dot(k * a[k], f[n - k]) / n
    return f


def spow(a, p):
    f = np.zeros(N + 1)
    f[0] = a[0] ** p
    for n in range(1, N + 1):
        k = np.arange(1, n + 1)
        f[n] = np.dot((k * p - n + k) * a[k], f[n - k]) / (n * a[0])
    return f


der = lambda a: np.concatenate([np.arange(1, N + 1) * a[1:], [0.0]])
integ = lambda a: np.concatenate([[0.0], a[:N] / np.arange(1, N + 1)])
down = lambda a: np.concatenate([a[1:], [0.0]])
up = lambda a: np.concatenate([[0.0], a[:N]])
ev = lambda a, x: np.polynomial.polynomial.polyval(x, a)


def qcoef(d3, d5, d7, A):
    return ((1 - 3 * d3) / A ** 5, -(10 * A * d5 + 12 * d3 ** 2 - 3 * d3) / A ** 4,
            -(168 * A ** 2 * d7 + 324 * A * d3 * d5 - 10 * A * d5 + 144 * d3 ** 3 - 21 * d3 ** 2) / (8 * A ** 3))


def series_route(wcoef, A, dAg, be):
    """wcoef: odd Taylor coefficients of w (array, index = power). dAg: A_g = A + dAg x^2.
    Returns q's (from (4)), the series of x^5 (Q - P) (low coefficients printed as a check), of x m, g/x^2, A_g."""
    w = np.zeros(N + 1)
    w[:len(wcoef)] = wcoef[:N + 1]
    wt = down(w)
    Ag = np.zeros(N + 1)
    Ag[0], Ag[2] = A, dAg
    r = mul(der(w) - Ag, inv(wt))
    assert abs(r[0] - 2) < 1e-10, r[0]
    r[0] = 0.0
    gh = sexp(integ(down(r)))
    g = up(up(gh))
    qt = mul(down(der(g) - der(der(w))), inv(2 * mul(gh, mul(gh, gh))))     # x^5 Q
    mm = mul(-wt, inv(gh))                                                   # x m
    q4 = qcoef(w[3], w[5], w[7], A)
    m3 = mul(mm, mul(mm, mm))
    M5, M3, M1 = mul(m3, mul(mm, mm)), m3, mm
    # q's by matching the x^0, x^2, x^4 coefficients of x^5 Q exactly (this includes the A_g term, which (4) omits)
    q5 = qt[0] / M5[0]
    q3 = (qt[2] - q5 * M5[2]) / M3[0]
    q1 = (qt[4] - q5 * M5[4] - q3 * M3[2]) / M1[0]
    x5P = q5 * M5 + q3 * up(up(M3)) + q1 * up(up(up(up(M1))))
    dif = qt - x5P
    return dict(q=(q5, q3, q1), q4=q4, dif=dif, mm=mm, gh=gh, Ag=Ag, qt=qt)


def fit_w(x, w, A, xf, deg, x0=0.02):
    # w/x = c0 + d3 x^2 + ...; c0 is fitted (free), not forced to -A: on the traces w/x(0) + A = 2.4e-11, and forcing it
    # biases d3, d5, d7 (relative residual 2.3e-7 of (w/x + A)/x^2 at x = 0.02); the series then uses w'(0) = -A
    s = (x >= x0) & (x <= xf)
    y = w[s] / x[s]
    z = (x[s] / xf) ** 2
    c = np.polynomial.polynomial.polyfit(z, y, deg + 1)
    res = float(np.abs(np.polynomial.polynomial.polyval(z, c) - y).max() / np.abs(y + A).max())
    wc = np.zeros(2 * deg + 4)
    wc[1] = -A
    wc[3::2] = c[1:] / xf ** (2 * np.arange(1, deg + 2))
    return wc, res


def fit_M(Q, m, deg):
    z = m ** -2
    zc = z.max()
    c = np.polynomial.polynomial.polyfit(z / zc, Q / m ** 5, deg)
    c = c / zc ** np.arange(deg + 1)
    return c[0], c[1], c[2]


def analyse(path, label, kw, Bex=None, Rex=None):
    ad = TraceAxis(path, reg='Ag', **kw)
    xs, mu1 = ad.xs, ad.mu1
    A = 2 * ad.c_l_file - 1
    be = 2 / A
    dAg = (mu1 - A) / xs ** 2
    z = np.load(path, allow_pickle=True)
    xd, wd = np.asarray(z['x']), np.asarray(z['w'])
    # pointwise data
    u = np.concatenate([np.geomspace(0.003, 0.06, 120)[:-1], np.linspace(0.06, 0.98, 900)[:-1], 1 - np.geomspace(0.02, 5e-4, 200)])
    x = u * xs
    pp = _parts(ad, x)
    Q, m, g = pp['Q'], pp['m'], pp['g']
    Qs = float(_parts(ad, np.array([xs]))['Q'][0])
    Ag = A + dAg * x ** 2
    out = dict(label=label, kw=str(kw), c_l=ad.c_l_file, A=A, x_star=xs, hP_minus_1=ad.hP_file - 1,
               minus_Qs_nat=-Qs * xs ** 5, routes={})
    # routes
    P_list = {}
    for xf, deg in [(1.5, 8), (2.0, 8), (2.0, 10), (2.6, 10), (2.6, 12)]:
        wc, res = fit_w(xd, wd, A, xf, deg)
        S = series_route(wc, A, dAg, be)
        P_list['S xf%.1f d%d' % (xf, deg)] = (S['q'], S, res)
    for xlo, xc, deg in [(0.02, 0.2, 4), (0.02, 0.3, 5), (0.04, 0.3, 6)]:
        sel = (u >= xlo) & (u <= xc)
        P_list['M %.2f-%.1f K%d' % (xlo, xc, deg)] = (fit_M(Q[sel], m[sel], deg), None, None)
    Sref = P_list['S xf2.0 d10'][1]
    for key, (qs, S, res) in P_list.items():
        q5, q3, q1 = qs
        R = Q - (q5 * m ** 5 + q3 * m ** 3 + q1 * m) - Qs
        Rn = R * xs ** 5
        band = (u >= 0.06) & (u <= 0.9995)
        Ru = [float(np.interp(v, u, Rn)) for v in UL]
        near = u > 0.995
        slope = float(np.polyfit(1 - u[near], Rn[near], 2)[1])    # R_nat = -slope (1 - u) + ...
        row = dict(q5A5=q5 * A ** 5, Rmax=float(Rn[band].max()), u_at_max=float(u[band][np.argmax(Rn[band])]),
                   R_u=Ru, slope_u1=-slope)
        if S is not None:
            row['fit_res'] = res
            row['low_coeffs'] = float(np.abs(S['dif'][:6]).max())
            row['q_matched_minus_q4_nat'] = [float((a - b) * A ** n) for a, b, n in zip(S['q'], S['q4'], (5, 3, 1))]
            # series R near 0 and its agreement with the pointwise R where both are valid
            QmP = S['dif'][5:]
            RS = lambda xx: ev(QmP, xx) - Qs
            lo = (u >= 0.02) & (u <= 0.2)
            row['series_vs_pointwise_0.02_0.2'] = float(np.abs((RS(x[lo]) - R[lo]) * xs ** 5).max())
            row['R_series_u'] = [float(RS(v * xs) * xs ** 5) for v in (0.003, 0.01, 0.03, 0.06)]
            row['Rmax_series_0_0.06'] = float(max(RS(v * xs) * xs ** 5 for v in np.linspace(0, 0.06, 61)))
            row['B3nat_8'] = b3_form8(ad, S, qs, Qs, A, be, dAg, xs)
        if Rex is not None:
            row['err_vs_exact_band'] = float(np.abs(Rn[band] - Rex(u[band])).max())
        out['routes'][key] = row
    out['d_fit'] = [float(v) for v in Sref['q']]
    return out


def b3_form8(ad, S, qs, Qs, A, be, dAg, xs):
    q5, q3, q1 = qs
    x1, x2 = 0.06 * xs, 0.97 * xs
    # [0, x1]: integrand = R (xm)^(be-2) A_g / gh * x^(-be), R = -Qs + series
    Rser = np.concatenate([S['dif'][5:], np.zeros(5)])
    Rser[0] -= Qs
    Sx = mul(mul(Rser, spow(S['mm'], be - 2)), mul(S['Ag'], inv(S['gh'])))
    n = np.arange(N - 8)
    I0 = float(np.sum(Sx[n] * x1 ** (n + 1 - be) / (n + 1 - be)))
    tail = abs(Sx[N - 9] * x1 ** (N - 8))

    def Rfun(xx):
        pp = _parts(ad, xx)
        return pp['Q'] - (q5 * pp['m'] ** 5 + q3 * pp['m'] ** 3 + q1 * pp['m']) - Qs, pp['m'], pp['g']
    # [x1, x2]: panels in log x
    tb = np.linspace(math.log(x1), math.log(x2), 41)
    gx, gw = Lg.leggauss(20)
    I1 = 0.0
    for a, b in zip(tb[:-1], tb[1:]):
        t = a + (gx + 1) * (b - a) / 2
        xx = np.exp(t)
        R, m, g = Rfun(xx)
        I1 += np.sum(gw * (b - a) / 2 * R * m ** (be - 2) * (A + dAg * xx ** 2) / g * xx)
    # [x2, x*]
    d = xs - x2
    sg = 0.01 + 0.99 * (np.cos(np.pi * (np.arange(120) + 0.5) / 120) + 1) / 2
    R, m, g = Rfun(xs - d * sg)
    tau = d * sg
    cr = np.polynomial.chebyshev.Chebyshev.fit(sg, R / tau, 8, domain=[0, 1])
    cm = np.polynomial.chebyshev.Chebyshev.fit(sg, m / tau, 8, domain=[0, 1])
    cg = np.polynomial.chebyshev.Chebyshev.fit(sg, g, 8, domain=[0, 1])
    zj, wj = roots_jacobi(30, be - 1, 0.0)            # weight (1 - z)^(be-1) on [-1, 1]; sigma = (1 + z)/2 ... use 1 - z
    s2 = (1 - zj) / 2                                  # sigma in (0, 1), weight sigma^(be-1) (2)^(1-be)... see below
    f = cr(s2) * cm(s2) ** (be - 2) * (A + dAg * (xs - d * s2) ** 2) / cg(s2)
    # int_0^d tau^(be-1) F d tau = d^be int_0^1 s^(be-1) F ds; int_{-1}^1 (1-z)^(be-1) F dz = 2^be int_0^1 s^(be-1) F ds
    I2 = float(d ** be * np.sum(wj * f) / 2 ** be)
    B = (be - 1) / (3 * A ** be) * (I0 + I1 + I2)
    return dict(Bnat=float(B * xs ** (4 + be)), I0=I0 * xs ** (4 + be) * (be - 1) / (3 * A ** be), series_tail=float(tail),
                end_fit_res=float(np.abs(cr(sg) - R / tau).max() / np.abs(R / tau).max()))


if __name__ == '__main__':
    mode = sys.argv[1]
    res = []
    VAR = {'near3': dict(near_frac=0.03), 'ls24n3': dict(fit01=(24, 11), fit2=(24, 11), near_frac=0.03)}
    if mode == 'r12':
        Lv = 8.6
        A = 10.150725
        k = A / Lv ** 2
        Rex = lambda uu: (1 - 6 * k) * (uu ** 5 - 1) + (1 + 2 * k) * (uu ** 3 - 1)
        SA = 6 * A * (4 * A - 3) / (8 * A - 1)
        Bex = 0.530666623156826 * (1 - SA / Lv ** 2)
        uu = np.linspace(1e-3, 0.9995, 20000)
        print('R12 L = 8.6: exact R_nat at u = %s: %s; exact max on [0.06, 0.9995] %.4e; slope at u = 1: %.6f; B_3^nat %.10f' % (
            UL, ['%.4e' % Rex(v) for v in UL], Rex(uu[uu >= 0.06]).max(), 8 - 24 * k, Bex))
        for vn in VAR:
            r = analyse('verifier/early_data/traces/r12_L8.6_n0.npz', 'R12 ' + vn, VAR[vn], Bex, Rex)
            r['Bex'] = Bex
            res.append(r)
        tag = 'r12'
    else:
        key = sys.argv[3] if len(sys.argv) > 3 else 'wpp_ode'
        for nm in sys.argv[2].split(','):
            for vn in VAR:
                res.append(analyse(D + nm + '_traces.npz', nm + ':' + key + ':' + vn, dict(VAR[vn], wppkey=key)))
        tag = sys.argv[4] if len(sys.argv) > 4 else 'traces_' + key
    for r in res:
        print('%s: c_l %.7f x* %.5f h(P)-1 %+.1e -Q*_nat %.5e' % (r['label'], r['c_l'], r['x_star'], r['hP_minus_1'], r['minus_Qs_nat']))
        for k2, row in r['routes'].items():
            s = '   %-16s q5A5 %.10f max R_nat [0.06,0.9995] %+.3e at u %.4f, slope %.4f, R_nat(u=%s) %s' % (
                k2, row['q5A5'], row['Rmax'], row['u_at_max'], row['slope_u1'], UL, ' '.join('%+.4f' % v for v in row['R_u']))
            if 'fit_res' in row:
                s += '\n                    q-q(4) (x A^n) %s,' % ' '.join('%.1e' % v for v in row['q_matched_minus_q4_nat'])
                s += ' fit res %.1e, low coeffs %.1e, series-pointwise %.1e, R_series(u=.003,.01,.03,.06) %s, max_series[0,.06] %+.4f, B3nat(8) %.5f (I0 %.4f, tail %.0e, end res %.0e)' % (
                    row['fit_res'], row['low_coeffs'], row['series_vs_pointwise_0.02_0.2'], ' '.join('%+.4f' % v for v in row['R_series_u']),
                    row['Rmax_series_0_0.06'], row['B3nat_8']['Bnat'], row['B3nat_8']['I0'], row['B3nat_8']['series_tail'], row['B3nat_8']['end_fit_res'])
            if 'err_vs_exact_band' in row:
                s += '\n                    max |R_nat - exact| on band %.1e' % row['err_vs_exact_band'] + (
                    ', B3nat - exact %+.1e' % (row['B3nat_8']['Bnat'] - r['Bex']) if 'B3nat_8' in row else '')
            print(s, flush=True)
    json.dump(res, open('verifier/early_data/hminus_ver_%s.json' % tag, 'w'), indent=1)
