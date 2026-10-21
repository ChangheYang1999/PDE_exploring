"""verifier: fred11 03-sign-criterion formulas (8) (A > 2), (11) (1 < A < 2) and (12) (A = 2) on traces that are NOT R12:
w = w_R12 (1 + eps x^2 exp(-x^2/8) chi), L = 8.6, chi the cutoff of exact_dir948b.py (1 on x <= 0.8 L, 0 on x >= 0.95 L),
finite eps. Reference: the R10 finite-part value of exact_dir948b.py (code reused by exec; A replaced by text).
Formula side, own code:
  R = Q - P(m) - Q* (A > 2), R = Q - P(m) (A < 2), P from (4) with the trace's own d3, d5, d7, Q* = Q(L) = Q(L; K).
  B_3 = ((beta - 1)/(3 A^beta)) int_0^L R m^(beta-2) (A/g) dx      (dm = -(A/g) dx, from w g' = (w' - A) g)
  [0, x_c]: power series; x^5 (Q - P(m)) has zero coefficients through x^5 (printed: a check of (4) on this trace), and
            the integrand is x^(-beta) S(x), integrated term by term.
  [x_c, 0.95 L]: the Gauss-Legendre panels of exact_dir948b.py.  [0.95 L, L]: w = w_R12, g = K g_R12, R/(L - x) exact
            rational in (x, K) (sympy), tau = L - x = sigma^(1/(beta-1+1)) or sigma^(1/(beta-2+1)) removes the endpoint power.
  A = 2: B_3 = Q*/6 and B_3 = w''(L)(g* - 2)/(24 g*^3) with g* = g(L).
Usage: check_fred11b.py A eps [eps ...]
"""
import sys
import time
import mpmath as mp
import sympy as sp

Aarg = sys.argv[1]
src = open('verifier/early_code/symb/exact_dir948b.py').read().split('\nnat = L**')[0]
src = src.replace("'10.150725'", "'%s'" % Aarg)
src = src.replace("fp = mp.fsum(ph[n] * xc**(n - 4 - be) / (n - 4 - be) for n in range(N + 1))",
                  "fp = mp.fsum(ph[n] * xc**(n - 4 - be) / (n - 4 - be) for n in range(N + 1) if n - 4 - be != 0)\n"
                  "    assert be != 1 or abs(ph[5]) < mp.mpf(10)**-25")
exec(src)
assert A == mp.mpf(Aarg)
outb = []
PB = lambda *a: (print(*a, flush=True), outb.append(' '.join(str(x) for x in a)))
nat = L**(4 + be)


def qcoef(d3, d5, d7):
    return ((1 - 3 * d3) / A**5, -(10 * A * d5 + 12 * d3**2 - 3 * d3) / A**4,
            -(168 * A**2 * d7 + 324 * A * d3 * d5 - 10 * A * d5 + 144 * d3**3 - 21 * d3**2) / (8 * A**3))


def series_part(eps, Qst):
    num, den = zeros(), zeros()
    num[1], num[3] = -A, A / L**2
    den[0], den[2] = mp.mpf(1), 1 / L**2
    wR = mul(num, inv(den))
    bq = zeros()
    bq[2] = mp.mpf(-1) / 8
    b = up(up(sexp(bq)))
    one = zeros()
    one[0] = mp.mpf(1)
    w = mul(wR, add(one, scal(eps, b)))
    wt = down(w)
    r = mul(add(der(w), scal(-A, one)), inv(wt))
    r[0] = mp.mpf(0)
    lg = integ(down(r))
    gh = sexp(lg)
    g = up(up(gh))
    qt = mul(down(add(der(g), scal(-1, der(der(w))))), inv(scal(2, mul(gh, mul(gh, gh)))))
    mm = mul(scal(-1, wt), inv(gh))
    q5, q3, q1 = qcoef(w[3], w[5], w[7])
    m3 = mul(mm, mul(mm, mm))
    x5P = add(scal(q5, mul(m3, mul(mm, mm))), add(scal(q3, up(up(m3))), scal(q1, up(up(up(up(mm)))))))
    dif = add(qt, scal(-1, x5P))
    low = max(abs(dif[n]) for n in range(6))
    QmP = dif
    for _ in range(5):
        QmP = down(QmP)
    Rs = add(QmP, scal(-Qst, one)) if A > 2 else QmP
    S = mul(scal(A, mul(Rs, spow(mm, be - 2))), inv(gh))
    I0 = mp.fsum(S[n] * xc**(n + 1 - be) / (n + 1 - be) for n in range(N - 5) if n + 1 - be != 0)
    return I0, low, (w[3], w[5], w[7]), (q5, q3, q1), abs(dif[6])


def mid_part(eps, qs, Qst):
    q5, q3, q1 = qs

    def Rint(t, lgh):
        W = WD[reg_of(t)]
        w0, w1, w2 = [W[k](t, eps) for k in range(3)]
        g = t**2 * mp.exp(lgh)
        g1 = (w1 - A) * g / w0
        Q = (g1 - w2) / (2 * g**3)
        m = -w0 / g
        R = Q - (q5 * m**5 + q3 * m**3 + q1 * m) - (Qst if A > 2 else 0)
        return R * m**(be - 2) * A / g
    lg0, I = origin(eps)[1], mp.mpf(0)
    for a, b in zip(BR[:-1], BR[1:]):
        h = (b - a) / 2
        for z, wgt in zip(GX, GW):
            t = a + h * (z + 1)
            I += h * wgt * Rint(t, lg0 + gl(lambda s: efun(s, eps), a, t))
        lg0 += gl(lambda s: efun(s, eps), a, b)
    return I


xs, Ks, Qss, q5s, q3s, q1s = sp.symbols('x K Qs q5 q3 q1')
uR = xs / Ls
wR12 = -As * xs * (1 - uR**2) / (1 + uR**2)
gK = Ks * xs**2 / (1 + uR**2)
QK = (sp.diff(gK, xs) - sp.diff(wR12, xs, 2)) / (2 * gK**3)
mK = sp.cancel(-wR12 / gK)
QstK = sp.simplify(QK.subs(xs, Ls))
Rsym = QK - (q5s * mK**5 + q3s * mK**3 + q1s * mK) - (QstK if A > 2 else 0)
Rt = sp.cancel(sp.together(Rsym) / (Ls - xs))
if A > 2:
    assert sp.fraction(Rt)[1].subs(xs, Ls) != 0
Rtf = sp.lambdify((xs, Ks, q5s, q3s, q1s), Rt if A > 2 else Rsym, 'mpmath')
Qstf = sp.lambdify(Ks, QstK, 'mpmath')


def end_part2(K, qs):
    pL = be - 1 if A > 2 else be - 2         # integrand ~ tau^pL at L
    aL = 1 / (pL + 1)

    def f(s):
        tau = s**aL
        xx = L - tau
        mfac = A * (L + xx) / (K * L**2 * xx)         # m = tau * mfac
        gg = K * xx**2 / (1 + (xx / L)**2)
        if A > 2:
            return Rtf(xx, K, *qs) * mfac**(be - 2) * A / gg / (pL + 1)     # R m^(be-2) dtau = Rt tau^(be-1) ... dtau
        return Rtf(xx, K, *qs) * mfac**(be - 2) * A / gg / (pL + 1)         # (Q - P) tau^(be-2) dtau
    return mp.quad(f, [0, (L - a2)**(pL + 1) / 4, (L - a2)**(pL + 1)])


PB('A = %s, beta = %s, L = %s, x_c = %s, N = %d, NG = %d, %d panels' % (Aarg, mp.nstr(be, 10), L, xc, N, NG, len(BR) - 1))
t0 = time.time()
for e in sys.argv[2:]:
    eps = mp.mpf(e)
    Bfp, tail, K = B3(eps)
    Qst = Qstf(K)
    I0, low, ds, qs, c6 = series_part(eps, Qst)
    I1, I2 = (mid_part(eps, qs, Qst), end_part2(K, qs)) if A != 2 else (0, 0)
    if A != 2:
        Bf = (be - 1) / (3 * A**be) * (I0 + I1 + I2)
        PB('eps = %s: K - 1 = %s, d3, d5, d7 = %s; max |coeff x^0..x^5 of x^5 (Q - P(m))| = %s (x^6: %s);'
           ' B_3^nat f.p. (R10) %s, formula (%s) %s, diff %s, %.0f s' % (
               e, mp.nstr(K - 1, 6), [mp.nstr(d, 12) for d in ds], mp.nstr(low, 3), mp.nstr(c6, 6), mp.nstr(Bfp * nat, 20),
               '8' if A > 2 else '11', mp.nstr(Bf * nat, 20), mp.nstr((Bf - Bfp) * nat, 3), time.time() - t0))
    else:
        gs = K * L**2 / 2
        w2L = sp.lambdify(xs, sp.diff(wR12, xs, 2), 'mpmath')(L)
        B12 = w2L * (gs - 2) / (24 * gs**3)
        PB('eps = %s: K - 1 = %s; max |coeff x^0..x^5 of x^5 (Q - P(m))| = %s; B_3 f.p. (R10) %s, Q*/6 %s, w\'\'(L)(g*-2)/(24 g*^3) %s,'
           ' diffs %s %s, %.0f s' % (e, mp.nstr(K - 1, 6), mp.nstr(low, 3), mp.nstr(Bfp, 20), mp.nstr(Qst / 6, 20), mp.nstr(B12, 20),
                                    mp.nstr(Qst / 6 - Bfp, 3), mp.nstr(B12 - Bfp, 3), time.time() - t0))
open('verifier/early_runs/check_fred11b_A%s.log' % Aarg, 'w').write('\n'.join(outb) + '\n')
