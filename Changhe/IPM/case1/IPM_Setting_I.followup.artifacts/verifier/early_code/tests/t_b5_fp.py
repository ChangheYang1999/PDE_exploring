"""verifier: cross-check of series_bj (B_j = (G_j^P - G_j^0)/H_j) against the finite-part integral form
B_j = -f.p. int_0^{x*} F_j/(w H_j) on R12 at the zero L* of B_3 (j = 5) and at L = 8.6 (j = 3).
[0, x1]: F_j/(w H_j) = x^(-p_j - 1) E(x), E analytic (series at 0), finite part term by term;
[x1, x*]: mpmath tanh-sinh with F_j from the series at P (G_3 analytic at P)."""
import sys
sys.path.insert(0, 'verifier/early_code')
import mpmath as mp
from series_bj import S, hierarchy, poly_at, r12, Bj
mp.mp.dps = 40
A = mp.mpf('10.150725')
n = 200


def fp_form(L, j, x1f):
    wn, wd, gn, gd = r12(A, L)
    s0 = hierarchy(wn, wd, gn, gd, A, 0, n, j)
    sP = hierarchy(wn, wd, gn, gd, A, L, n, j)
    q = mp.mpf(j - 1) / A
    pj = 2 * j + q
    L2 = mp.mpf(L) ** 2
    # H_j = A^q g^(j+q) |w|^(-q) = x^(p_j) * A^q A^(-q) (1+u^2)^(-(j+q)) ((1-u^2)/(1+u^2))^(-q), u = x/L, on [0, L)
    # so F_j/(w H_j) = x^(-p_j - 1) * [F_j / (w/x)] * (1+u^2)^(j+q) ((1-u^2)/(1+u^2))^q   (series in x at 0)
    u2 = S([0, 0, 1 / L2], n)
    one = S([1], n)
    # power of a series with constant term 1: exp(a log s)
    def spow(s, a):
        # s = 1 + t, log via series of log(1+t) by d/dx: (log s)' = s'/s
        ls_d = s.d().div(s)
        c = [mp.mpf(0)] + [ls_d.c[k] / (k + 1) for k in range(ls_d.n)]
        lgs = S(c, n) * a
        # exp of series with zero constant term: e' = e lgs'
        e = [mp.mpf(1)]
        for k in range(1, n):
            e.append(mp.fsum(i * lgs.c[i] * e[k - i] for i in range(1, k + 1)) / k)
        return S(e, n)
    wx = S(s0['w'].c[1:], n - 1)                     # w/x
    fac = spow(one + u2, j + q) * spow((one - u2).div(one + u2), q)
    E = s0['F%d' % j].div(wx) * fac
    x1 = mp.mpf(x1f) * L
    part0 = mp.fsum(E.c[m] * x1 ** (m - pj) / (m - pj) for m in range(E.n))
    def integrand(x):
        u = x / L
        w = -A * x * (1 - u * u) / (1 + u * u)
        g = x * x / (1 + u * u)
        H = A ** q * g ** (j + q) * abs(w) ** (-q)
        return sP['F%d' % j](x - L) / (w * H)
    part1 = mp.quad(integrand, [x1, (x1 + L) / 2, L - (L - x1) / 64, L], maxdegree=12)
    B = -(part0 + part1)
    return B * mp.mpf(L) ** (pj - j + 1), E.c[-1] * x1 ** (E.n - 1)


Ls = mp.mpf('5.3435753609603999162')
for (L, j) in [(mp.mpf('8.6'), 3), (Ls, 5)]:
    ref = Bj(*r12(A, L), A, L, n, [mp.mpf('0.5') * L], jmax=j)[0][j][0]['Bnat']
    for x1f in ['0.3', '0.5', '0.7']:
        Bn, tail = fp_form(L, j, x1f)
        print('L %s j %d x1/L %s: f.p. form %s   series form %s   diff %s  (last series term %s)' %
              (mp.nstr(L, 10), j, x1f, mp.nstr(Bn, 15), mp.nstr(ref, 15), mp.nstr(Bn - ref, 3), mp.nstr(tail, 3)))
