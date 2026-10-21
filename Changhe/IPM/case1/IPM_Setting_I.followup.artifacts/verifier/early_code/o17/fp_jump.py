# verifier (o17): finite-part form of B_5 on R12 at L^2 = S_A near the resonance A = 2 (p_5 = 12), with the
# contribution of the near-resonant Laurent term m = 12 of E (F_5/(w H_5) = x^(-p_5-1) E(x)) shown separately.
# fp_form follows code/tests/t_b5_fp.py (own code) with A as a parameter.
import sys
sys.path.insert(0, 'verifier/early_code')
import mpmath as mp
from series_bj import S, hierarchy, r12, Bj
mp.mp.dps = 40
n = 160


def spow(s, a):
    ls_d = s.d().div(s)
    c = [mp.mpf(0)] + [ls_d.c[k] / (k + 1) for k in range(ls_d.n)]
    lgs = S(c, n) * a
    e = [mp.mpf(1)]
    for k in range(1, n):
        e.append(mp.fsum(i * lgs.c[i] * e[k - i] for i in range(1, k + 1)) / k)
    return S(e, n)


def fp_form(A, L, j, x1f):
    wn, wd, gn, gd = r12(A, L)
    s0 = hierarchy(wn, wd, gn, gd, A, 0, n, j)
    sP = hierarchy(wn, wd, gn, gd, A, L, n, j)
    q = mp.mpf(j - 1) / A
    pj = 2 * j + q
    L2 = mp.mpf(L) ** 2
    u2 = S([0, 0, 1 / L2], n)
    one = S([1], n)
    wx = S(s0['w'].c[1:], n - 1)
    fac = spow(one + u2, j + q) * spow((one - u2).div(one + u2), q)
    E = s0['F%d' % j].div(wx) * fac
    x1 = mp.mpf(x1f) * L
    terms = [E.c[m] * x1 ** (m - pj) / (m - pj) for m in range(E.n)]
    part0 = mp.fsum(terms)

    def integrand(x):
        u = x / L
        w = -A * x * (1 - u * u) / (1 + u * u)
        g = x * x / (1 + u * u)
        H = A ** q * g ** (j + q) * abs(w) ** (-q)
        return sP['F%d' % j](x - L) / (w * H)
    part1 = mp.quad(integrand, [x1, (x1 + L) / 2, L - (L - x1) / 64, L], maxdegree=12)
    return -(part0 + part1), E, pj, terms


for As in sys.argv[1].split(','):
    A = mp.mpf(As)
    L = mp.sqrt(6 * A * (4 * A - 3) / (8 * A - 1))
    ref = Bj(*r12(A, L), A, L, n, [mp.mpf('0.5') * L], jmax=5)[0][5][0]['B']
    for x1f in ['0.3', '0.6']:
        B, E, pj, terms = fp_form(A, L, 5, x1f)
        print('A %s x1/L %s: B5 f.p. form %s  series %s  diff %s | E_12 %s  12 - p5 %s  term m=12 (-) %s  B5 without it %s' %
              (As, x1f, mp.nstr(B, 12), mp.nstr(ref, 12), mp.nstr(B - ref, 3), mp.nstr(E.c[12], 6), mp.nstr(12 - pj, 6),
               mp.nstr(-terms[12], 10), mp.nstr(B + terms[12], 12)), flush=True)
print('11/1474560 =', mp.nstr(mp.mpf(11) / 1474560, 12))
