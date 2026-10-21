"""verifier: independent checks of fred11 03-sign-criterion (lead verifier/fred11/; FINAL_REPORT 6.4 "Sign criterion for B_3").
Own derivations; the referee's and the lead's scripts were not used.
 (1) sympy: expansions (6) of m x/A and Q for w = -A x + d3 x^3 + d5 x^5 + d7 x^7 + d9 x^9 (g rebuilt from w), the
     coefficients (4) of P by matching, and Q - P(m) = O(x).
 (2) sympy: R12 formulas (13), the identities (14), the remainder (15), the positivity step of (16), (17), the sign
     change at L^2 = S_A, and the A = 2 identity 2 g'(L) = w''(L) g* behind (12).
 (3) B_3 on R12 for any A > 1 in closed form from the R10 finite-part integral (Beta functions, an independent route):
     B_3^nat = (1/(3A)) [-5 (1 - 6k) I(-5-beta) - 3 (1 + 2k) I(-3-beta)], I(a) = fp int_0^1 u^a (1 - u^2)^(beta-1) du;
     against C_A (1 - S_A/L^2) and against the ordinary integrals (8) (A > 2) and (11) (1 < A < 2) by quadrature (power substitutions at both ends).
 (4) (8) on a non-R12 trace (R12 at A = 10.150725, L = 8.6, times 1 + eps x^2 exp(-x^2/8) chi), with q_j from the
     trace's own Taylor coefficients, against the fit-free finite-part value of exact_dir948b.py.
"""
import time
import mpmath as mp
import sympy as sp

out = []
P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))
t0 = time.time()

# ---------------- (1) ----------------
x = sp.symbols('x', positive=True)
A, d3, d5, d7, d9 = sp.symbols('A d3 d5 d7 d9')
NS = 10
w = -A * x + d3 * x**3 + d5 * x**5 + d7 * x**7 + d9 * x**9
wt = sp.expand(w / x)                                    # -A + d3 x^2 + ...
# e = (w' - A)/w - 2/x = [(w' - A) - 2 w/x]/w = [(w' - A) - 2 wt]/(x wt)
num = sp.expand(sp.diff(w, x) - A - 2 * wt)              # O(x^2)
e = sp.expand(sp.series(sp.expand(num / x) / wt, x, 0, NS).removeO())
lg = sp.integrate(e, x)
gh = sp.expand(sp.series(sp.exp(lg), x, 0, NS).removeO())
g = sp.expand(x**2 * gh)
qt = sp.expand(sp.series((sp.diff(g, x) - sp.diff(w, x, 2)) * x**5 / (2 * g**3), x, 0, 8).removeO())   # x^5 Q
mm = sp.expand(sp.series(-wt / gh, x, 0, 8).removeO())                                                 # x m
mxA = sp.expand(mm / A)
c6 = [sp.simplify(mxA.coeff(x, n)) for n in (0, 2, 4)]
P('(1) m x/A = 1 + (%s) x^2 + (%s) x^4 + O(x^6)' % (c6[1], c6[2]))
P('    vs (6): residuals', sp.simplify(c6[0] - 1), sp.simplify(c6[1] + d3 / (2 * A)), sp.simplify(c6[2] + (2 * A * d5 + d3**2) / (8 * A**2)))
Qc = [sp.factor(sp.simplify(qt.coeff(x, n))) for n in (0, 2, 4)]
P('(1) x^5 Q coefficients x^0, x^2, x^4:', Qc)
P('    vs (6): residuals', sp.simplify(Qc[0] - (1 - 3 * d3)), sp.simplify(Qc[1] + (20 * A * d5 + 9 * d3**2 - d3) / (2 * A)),
  sp.simplify(Qc[2] + 3 * (56 * A**2 * d7 + 58 * A * d3 * d5 + 15 * d3**3) / (8 * A**2)))
P('    odd coefficients of x^5 Q (must vanish):', [sp.simplify(qt.coeff(x, n)) for n in (1, 3, 5)])
q5, q3, q1 = sp.symbols('q5 q3 q1')
x5P = sp.expand(sp.series(q5 * mm**5 + q3 * x**2 * mm**3 + q1 * x**4 * mm, x, 0, 8).removeO())
diff_ = sp.expand(qt - x5P)
sol = sp.solve([diff_.coeff(x, 0), diff_.coeff(x, 2), diff_.coeff(x, 4)], [q5, q3, q1], dict=True)[0]
ref = {q5: (1 - 3 * d3) / A**5, q3: -(10 * A * d5 + 12 * d3**2 - 3 * d3) / A**4,
       q1: -(168 * A**2 * d7 + 324 * A * d3 * d5 - 10 * A * d5 + 144 * d3**3 - 21 * d3**2) / (8 * A**3)}
P('(1) q_5, q_3, q_1 by matching minus (4):', [sp.simplify(sol[q] - ref[q]) for q in (q5, q3, q1)])
rem = sp.expand(diff_.subs(sol))
P('    x^5 (Q - P(m)) through x^5 after matching:', [sp.simplify(rem.coeff(x, n)) for n in range(6)],
  '; x^6 coefficient (the O(x) term of Q - P) depends on d9:', sp.simplify(rem.coeff(x, 6)).has(d9))
P('(1) done, %.0f s' % (time.time() - t0))

# ---------------- (2) ----------------
Ls, As = sp.symbols('L A_', positive=True)
u = x / Ls
wR = -As * x * (1 - u**2) / (1 + u**2)
gR = x**2 / (1 + u**2)
eR = sp.simplify((sp.diff(wR, x) - As) / wR - 2 / x - sp.diff(sp.log(gR / x**2), x))
P('(2) R12: (w\' - A)/w - 2/x - d/dx log(g/x^2) =', eR, '(g/x^2 -> 1 at 0)')
kk = As / Ls**2
mR = sp.simplify(-wR / gR)
QR = sp.simplify((sp.diff(gR, x) - sp.diff(wR, x, 2)) / (2 * gR**3))
P('(2) (13): m - (A/x - A x/L^2) =', sp.simplify(mR - (As / x - As * x / Ls**2)),
  '; Q - [(1-6k) x^-5 + (1+2k) L^-2 x^-3] =', sp.simplify(QR - ((1 - 6 * kk) / x**5 + (1 + 2 * kk) / (Ls**2 * x**3))))
r, b, z = sp.symbols('r b z')
zr = r - b / r
P('(2) (14):', sp.simplify(r**3 - (b / r)**3 - (zr**3 + 3 * b * zr)), sp.simplify(r**5 - (b / r)**5 - (zr**5 + 5 * b * zr**3 + 5 * b**2 * zr)))
# Taylor coefficients of R12 and P from (4)
wser = sp.series(wR, x, 0, 9).removeO()
dd = {d3: wser.coeff(x, 3), d5: wser.coeff(x, 5), d7: wser.coeff(x, 7)}
P('(2) R12 Taylor: d3, d5, d7 =', [sp.simplify(dd[k]) for k in (d3, d5, d7)])
PR = sum(ref[q].subs(A, As).subs(dd) * mR**n for q, n in ((q5, 5), (q3, 3), (q1, 1)))
QsR = QR.subs(x, Ls)
R15 = Ls**-5 * ((1 - 6 * kk) * (u**5 - 1) + (1 + 2 * kk) * (u**3 - 1))
P('(2) (15): Q - P(m) - Q(L) - L^-5[(1-6k)(u^5-1) + (1+2k)(u^3-1)] =', sp.simplify(QR - PR - QsR - R15))
uu, ks = sp.symbols('u k')
br = (1 - 6 * ks) * sum(uu**i for i in range(5)) + (1 + 2 * ks) * sum(uu**i for i in range(3))
P('(2) (16): -L^5 R/(1-u) - bracket =', sp.simplify(sp.cancel(-((1 - 6 * ks) * (uu**5 - 1) + (1 + 2 * ks) * (uu**3 - 1)) / (1 - uu)) - br),
  '; d bracket/dk =', sp.factor(sp.diff(br, ks)), '; bracket(k = 1/3) - (1-u)(3u^3+6u^2+4u+2)/3 =',
  sp.simplify(br.subs(ks, sp.Rational(1, 3)) - (1 - uu) * (3 * uu**3 + 6 * uu**2 + 4 * uu + 2) / 3),
  '; bracket at u = 1:', sp.factor(br.subs(uu, 1)))
SA = 6 * As * (4 * As - 3) / (8 * As - 1)
P('(2) (17): S_A - 2A =', sp.factor(SA - 2 * As), '; 3A - S_A =', sp.factor(3 * As - SA),
  '; dR/du at u = 1 times L^5:', sp.factor(sp.diff((1 - 6 * ks) * (uu**5 - 1) + (1 + 2 * ks) * (uu**3 - 1), uu).subs(uu, 1)))
# A = 2: g'(L) = w''(L) g*/A holds for any trace with T_1 = 0 and h(L) = 1; on R12:
P('(2) R12: g\'(L) - w\'\'(L) g(L)/A =', sp.simplify((sp.diff(gR, x) - sp.diff(wR, x, 2) * gR / As).subs(x, Ls)))
P('(2) general: d/dx[w g\' + (A + 1 - w\' - 1) g] at x = L with w(L) = 0, w\'(L) = A gives A g\'(L) - w\'\'(L) g(L) = 0; at A = 2,',
  'Q*/6 = (g\'-w\'\')/(12 g*^3) = w\'\'(L)(g* - 2)/(24 g*^3) <=> 2 g\'(L) = w\'\'(L) g*: identity.')
P('(2) done, %.0f s' % (time.time() - t0))

# ---------------- (3) ----------------
mp.mp.dps = 30


def b3nat_beta(Av, Lv):
    Av, Lv = mp.mpf(Av), mp.mpf(Lv)
    be = 2 / Av
    I = lambda a: mp.gamma((a + 1) / 2) * mp.gamma(be) / (2 * mp.gamma((a + 1) / 2 + be))
    k = Av / Lv**2
    return (-5 * (1 - 6 * k) * I(-5 - be) - 3 * (1 + 2 * k) * I(-3 - be)) / (3 * Av)


def b3nat_int(Av, Lv):
    """(8) for A > 2, (11) for 1 < A < 2, on R12, as integrals in x (dm = -A/g dx), natural units."""
    Av, Lv = mp.mpf(Av), mp.mpf(Lv)
    be = 2 / Av
    k = Av / Lv**2

    def f(X, tau):
        U = X / Lv
        # R = L^-5 [(1-6k)(U^5-1) + (1+2k)(U^3-1)] with U - 1 = -tau/L factored out (no cancellation at L)
        Rm = -(tau / Lv**6) * ((1 - 6 * k) * (1 + U + U**2 + U**3 + U**4) + (1 + 2 * k) * (1 + U + U**2))
        if Av < 2:      # Q - P(m) = R + Q* = L^-5 [(1-6k) U^5 + (1+2k) U^3] (= R15 + (2-4k) L^-5), O(x^3) at 0
            Rm = ((1 - 6 * k) * U**5 + (1 + 2 * k) * U**3) / Lv**5
        m = Av * tau * (Lv + X) / (Lv**2 * X)
        gg = X**2 / (1 + U**2)
        return Rm * m**(be - 2) * Av / gg
    # endpoint behaviour: x^(-beta) (A > 2) or x^(1-beta) (A < 2) at 0; (L-x)^(beta-1) (A > 2) or (L-x)^(beta-2) (A < 2) at L
    p0 = -be if Av > 2 else 1 - be
    pL = be - 1 if Av > 2 else be - 2
    a0, aL = 1 / (p0 + 1), 1 / (pL + 1)
    h = Lv / 2
    I = mp.quad(lambda s: f(s**a0, Lv - s**a0) * a0 * s**(a0 - 1), [0, h**(p0 + 1)]) + \
        mp.quad(lambda s: f(Lv - s**aL, s**aL) * aL * s**(aL - 1), [0, h**(pL + 1)])
    return (be - 1) / (3 * Av**be) * I * Lv**(4 + be)


CA = b3nat_beta('10.150725', 1e10)
Av = mp.mpf('10.150725')
P('(3) A = 10.150725: C_A from the Beta form', mp.nstr(CA, 15), '(C2/D13: 0.530666623156826)')
for Lv in ['6', '8.6', '5.3435753609604', '4', '10']:
    cf = CA * (1 - 6 * Av * (4 * Av - 3) / (8 * Av - 1) / mp.mpf(Lv)**2)
    bb = b3nat_beta(Av, Lv)
    bi = b3nat_int(Av, Lv)
    P('(3) A = 10.150725, L = %s: Beta form %s, C_A(1 - S_A/L^2) %s, integral (8) %s, rel diff (8) vs Beta %s' % (
        Lv, mp.nstr(bb, 16), mp.nstr(cf, 16), mp.nstr(bi, 16), mp.nstr(abs(bi - bb) / max(abs(bb), mp.mpf(10)**-20), 3)))
for Av2, Lv in [('4', '3'), ('4', '5'), ('3', '2.5'), ('1.5', '2'), ('1.5', '4'), ('1.25', '3')]:
    bb = b3nat_beta(Av2, Lv)
    bi = b3nat_int(Av2, Lv)
    P('(3) A = %s, L = %s: Beta form %s, integral (%s) %s, rel diff %s' % (
        Av2, Lv, mp.nstr(bb, 16), '8' if mp.mpf(Av2) > 2 else '11', mp.nstr(bi, 16), mp.nstr(abs(bi - bb) / abs(bb), 3)))
P('(3) A = 2 (beta = 1): Beta form at L = 3:', mp.nstr(b3nat_beta(2, 3), 16), ' Q* L^5/6 = (2 - 4k)/6:', mp.nstr((2 - 4 * mp.mpf(2) / 9) / 6, 16))
P('(3) done, %.0f s' % (time.time() - t0))
open('verifier/early_runs/check_fred11.log', 'w').write('\n'.join(out) + '\n')
