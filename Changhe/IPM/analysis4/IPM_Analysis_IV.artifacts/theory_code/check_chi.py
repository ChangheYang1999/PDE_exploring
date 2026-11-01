"""Lead's low-order consistency check: recurrence (B),(R) versus direct substitution into the chi equation.

Exact rational c_l, sympy. Builds f_n, g_n from (B),(R), reconstructs C_n from f_n (SPEC section 7),
then forms chi_N = sum r^{q_n} C_n, computes rho = -d_y Lap chi and u = (-chi_xyy, chi_xxy) in Cartesian
coordinates, and checks that the residual of (c_l X + u).grad rho - rho vanishes through order p_N.
"""
import sympy as sp
from fractions import Fraction as Fr

def recurrence(cl, a1, N):
    """a1: dict k -> coefficient of sin((2k+1)th). Returns lists of dicts f[n], g[n] (n = 1..N)."""
    gam = 1 / cl
    dl = 1 - gam
    p = lambda n: 1 - n * dl
    f = {1: dict(a1)}
    g = {}

    def poisson(n):
        P = p(n) + 1
        a = f[n]
        K = max(a) if a else -1
        b = {}
        for j in range(1, K + 2):
            num = (p(n) - 2 * j + 1) * a.get(j - 1, 0) + (p(n) + 2 * j + 1) * a.get(j, 0)
            den = 2 * (4 * j * j - P * P)
            if num != 0:
                b[j] = num / den
        return b

    g[1] = poisson(1)
    for n in range(2, N + 1):
        acc = {}  # coefficient of sin(m th), m odd
        for i in range(1, n):
            j = n - i
            gi, fj = g[i], f[j]
            Pi = p(i) + 1
            pj = p(j)
            for mu, b in gi.items():
                # g_i' = 2mu b cos(2mu th); f_j = a sin(m th); f_j' = m a cos(m th)
                for k, a in fj.items():
                    m = 2 * k + 1
                    # term1: -p_j g_i' f_j = -p_j 2mu b a cos(2mu th) sin(m th)
                    c1 = -pj * 2 * mu * b * a
                    # term2: (p_i+1) g_i f_j' = Pi b m a sin(2mu th) cos(m th)
                    c2 = Pi * b * m * a
                    # cos(A) sin(B) = (sin(B+A) + sin(B-A))/2 ; sin(A) cos(B) = (sin(A+B) + sin(A-B))/2
                    for (mm, c) in ((m + 2 * mu, c1 / 2), (m - 2 * mu, c1 / 2), (2 * mu + m, c2 / 2), (2 * mu - m, c2 / 2)):
                        if mm < 0:
                            mm, c = -mm, -c
                        acc[mm] = acc.get(mm, 0) + c
        fac = 1 / ((n - 1) * (cl - 1))
        f[n] = {(mm - 1) // 2: fac * c for mm, c in acc.items() if c != 0}
        g[n] = poisson(n)
    return f, g, p


def chi_coeffs(fn, pn):
    """C(th) = sum_k c_k cos(2k th) with rho = -d_y Lap(r^{p+3} C)."""
    q = pn + 3
    K = max(fn) if fn else -1
    d = {}
    # a_m = (m - (p+1)/2) d_m + (m+1+(p+1)/2) d_{m+1} (m>=1); a_0 = -(p+1) d_0 + ((p+3)/2) d_1
    d[K + 1] = 0
    for m in range(K, 0, -1):
        d[m] = (fn.get(m, 0) - (m + 1 + (pn + 1) / 2) * d[m + 1]) / (m - (pn + 1) / 2)
    d[0] = (fn.get(0, 0) - ((pn + 3) / 2) * d[1]) / (-(pn + 1))
    c = {k: d[k] / (q * q - 4 * k * k) for k in d if d[k] != 0}
    return c


def main():
    cl = sp.Rational(5, 3)
    N = 4
    a1 = {0: sp.Integer(1), 1: sp.Rational(1, 2)}
    f, g, p = recurrence(cl, a1, N)
    for n in range(1, N + 1):
        print('n', n, 'p_n', p(n), 'f_n', f[n])
        print('     g_n', g[n])
    x, y = sp.symbols('x y', positive=True)  # check in the open first quadrant
    r = sp.sqrt(x * x + y * y)
    th = sp.atan2(y, x)
    chi = 0
    for n in range(1, N + 1):
        C = chi_coeffs(f[n], p(n))
        # cos(2k th) = T_{2k}(x/r)
        Cexpr = sum(ck * sp.chebyshevt(2 * k, x / r) for k, ck in C.items())
        chi += r ** (p(n) + 3) * Cexpr
    rho = -sp.diff(sp.diff(chi, x, 2) + sp.diff(chi, y, 2), y)
    ux = -sp.diff(chi, x, y, y)
    uy = sp.diff(chi, x, x, y)
    res = (cl * x + ux) * sp.diff(rho, x) + (cl * y + uy) * sp.diff(rho, y) - rho
    # check rho reproduces the f_n at sample points, and the residual size at increasing radii
    import mpmath as mp
    mp.mp.dps = 60
    fres = sp.lambdify((x, y), res, 'mpmath')
    frho = sp.lambdify((x, y), rho, 'mpmath')
    t0 = mp.mpf('0.7')
    for R in [mp.mpf(10) ** 2, mp.mpf(10) ** 4, mp.mpf(10) ** 6]:
        X, Y = R * mp.cos(t0), R * mp.sin(t0)
        rho_ser = sum(R ** (mp.mpf(p(n).p) / p(n).q) *
                      sum(mp.mpf(a.p) / a.q * mp.sin((2 * k + 1) * t0) for k, a in f[n].items()) for n in range(1, N + 1))
        rr = frho(X, Y)
        rv = fres(X, Y)
        pN1 = mp.mpf(p(N + 1).p) / p(N + 1).q
        print('R=%s  rho-series diff %s  residual %s  residual/R^p_{N+1} %s' % (
            mp.nstr(R, 3), mp.nstr(rr - rho_ser, 5), mp.nstr(rv, 8), mp.nstr(rv / R ** pN1, 12)))
    # predicted leading residual coefficient: -(N)(c_l-1) f_{N+1}^{(partial)}: compute F_{N+1} from (R) without the f_{N+1} term
    f2, g2, _ = recurrence(cl, a1, N + 1)
    lead = N * (mp.mpf(cl.p) / cl.q - 1) * sum(mp.mpf(a.p) / a.q * mp.sin((2 * k + 1) * t0) for k, a in f2[N + 1].items())
    print('predicted residual coefficient N (c_l-1) f_{N+1}(t0):', mp.nstr(lead, 12))


if __name__ == '__main__':
    main()
