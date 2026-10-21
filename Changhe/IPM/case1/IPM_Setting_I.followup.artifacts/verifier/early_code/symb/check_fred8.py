"""verifier: independent checks of fred8 (lead verifier/fred8/02-axis-functional and 03-source-regularity PROOF.md).
Own derivations and code (the lead's tmp/check_fred8.py was not used).
 (A) family v_d (03 (3)-(6)): Euler identity (sympy, symbolic A, g, lambda), degree, the equivalences
     k > -1 <=> d < (1 + g)/A, lambda < 1 <=> d < A, A lambda = 2 <=> d = 3 - 2/A; inequalities (4) at d = 5/2.
 (B) G_3 on s < 0 of v_d by two independent routes:
     Fourier/ODE route of 03 (7)-(13): c_- from (8), K from (11), coefficient (13);
     physical route: d_y^3 v(s, 0) = int int d_y^3 K_b(s - t, -y') t^(-lambda) k_k(y') dt dy' (absolutely convergent
     for d < 3), K_b = c_b |X|^(2b - 2), k_k = F^{-1}[i sgn eta |eta|^k] = kc sgn y |y|^(-1-k).
     Also the limit d -> 3 - 2/A against fred6 (D14): G_3 |s|^q = 1/(12 sin(pi q)).
 (C) the eta-moments (7) and (10) by quadrature.
 (D) 02 (11)-(14) on R12 data: the original form (1/(3 A^beta)) fp int Q_3' m^(beta-1) and the convergent form
     ((beta-1) A^(1-beta)/3) fp int (Q_3 - Q_3(L)) m^(beta-2)/g against my series B_3 (code/series_bj.py, C4) and the
     closed form C_A (1 - S_A/L^2) (D13 (d)).
 (E) saddle modes: c_j = (-1)^((j-1)/2) j!/prod_{r=1..j}(p + r) for j = 1..11 (polynomial stream function, symbolic p).
"""
import sys
import mpmath as mp
import sympy as sp

sys.path.insert(0, 'verifier/early_code')
mp.mp.dps = 30
out = []
P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))

# ---------------- (A) ----------------
xi, eta, A, g, lam, d = sp.symbols('xi eta A g lambda d', positive=True)
b = g / (2 * (A - 1))
k = 2 * b - 2 - A * lam
M = xi**2 / (xi**2 + eta**2)
lv = (lam - 1) * sp.log(xi) + k * sp.log(eta) - b * sp.log(xi**2 + eta**2)     # log vhat on xi, eta > 0
P('(A) Euler identity residual (symbolic A, g, lambda):', sp.simplify(A * xi * sp.diff(lv, xi) + eta * sp.diff(lv, eta) + (A + 2 + g * M)))
P('(A) isotropic degree + d + 2 with d = 1 + (A-1) lambda:', sp.simplify((lam - 1) + k - 2 * b + 1 + (A - 1) * lam + 2))
lam_d = (d - 1) / (A - 1)
kd = sp.simplify(k.subs(lam, lam_d))
P('(A) k + 1 =', sp.factor(kd + 1), ' ; ((1+g)/A - d) * A/(A-1) =', sp.factor(((1 + g) / A - d) * A / (A - 1)),
  ' ; difference', sp.simplify(kd + 1 - ((1 + g) / A - d) * A / (A - 1)))
P('(A) 1 - lambda =', sp.factor(1 - lam_d), ' ; A lambda - 2 =', sp.factor(A * lam_d - 2), '(zero at d = 3 - 2/A)')
for tag, Av, gv in [('fred8 rounded', '10.1507', '29.749'), ('X3', '10.150725221', '29.7494907')]:
    Av, gv = mp.mpf(Av), mp.mpf(gv)
    bv, beta, lv_ = gv / (2 * (Av - 1)), 2 / Av, mp.mpf(1.5) / (Av - 1)
    kv = 2 * bv - 2 - Av * lv_
    P('(A) %s, d = 5/2: lambda %s beta %s k %s b - A lambda/2 %s A lambda %s (1+g)/A %s 3 - beta %s' % (
        tag, mp.nstr(lv_, 8), mp.nstr(beta, 8), mp.nstr(kv, 8), mp.nstr(bv - Av * lv_ / 2, 8), mp.nstr(Av * lv_, 8),
        mp.nstr((1 + gv) / Av, 8), mp.nstr(3 - beta, 8)),
      '| (4):', 0 < lv_ < beta < 0.5, -1 < kv < 0, bv - Av * lv_ / 2 > 0, 1 < Av * lv_ < 2)


# ---------------- (B), (C) ----------------
def fam(Av, gv, dv):
    Av, gv, dv = mp.mpf(Av), mp.mpf(gv), mp.mpf(dv)
    bv = gv / (2 * (Av - 1))
    lv_ = (dv - 1) / (Av - 1)
    kv = 2 * bv - 2 - Av * lv_
    return Av, gv, dv, bv, lv_, kv


def g3_ode(Av, gv, dv):
    Av, gv, dv, bv, lv_, kv = fam(Av, gv, dv)
    Cb = mp.beta(bv - Av * lv_ / 2, 1 + Av * lv_ / 2) / (2 * mp.pi)
    cm = Cb * mp.gamma(1 - lv_) / mp.gamma(dv + 1) * mp.sin(mp.pi * Av * lv_ / 2) / mp.sin(mp.pi * dv)
    K = (gv / (Av * (dv - 1)) - 1) / 2
    C = -gv * K * cm * dv * (dv - 1) * (dv - 2) / (3 * (Av * (dv - 3) + 2))
    return C, cm, Cb, K


def g3_phys(Av, gv, dv):
    Av, gv, dv, bv, lv_, kv = fam(Av, gv, dv)
    m = 2 * bv - 2
    cb = mp.gamma(1 - bv) / (4**bv * mp.pi * mp.gamma(bv))
    kc = -mp.gamma(1 + kv) * mp.cos(mp.pi * kv / 2) / mp.pi
    f3 = lambda u: m * (m - 2) * u * (1 + u**2)**(m / 2 - 3) * (3 + (m - 1) * u**2)
    Cin = mp.quad(lambda u: u**(-1 - kv) * f3(u), [0, 1, 10, mp.inf])
    return cb * (-2 * kc * Cin) * mp.beta(1 - lv_, 3 - dv) / 6


for tag, Av, gv in [('fred8 rounded', '10.1507', '29.749'), ('X3', '10.150725221', '29.7494907')]:
    C, cm, Cb, K = g3_ode(Av, gv, 2.5)
    Cp = g3_phys(Av, gv, 2.5)
    P('(B) %s d = 5/2: C_b %s c_- %s K %s | G_3 r^(3-d): ODE route %s physical route %s rel diff %s' % (
        tag, mp.nstr(Cb, 12), mp.nstr(cm, 12), mp.nstr(K, 10), mp.nstr(C, 15), mp.nstr(Cp, 15), mp.nstr(abs(C / Cp - 1), 3)))
Av, gv = '10.150725221', '29.7494907'
for dv in ['1.5', '2.2', '2.7', '2.79']:
    C, cm, Cb, K = g3_ode(Av, gv, dv)
    Cp = g3_phys(Av, gv, dv)
    P('(B) X3 d = %s: c_- %s, ODE %s physical %s rel diff %s' % (dv, mp.nstr(cm, 10), mp.nstr(C, 14), mp.nstr(Cp, 14), mp.nstr(abs(C / Cp - 1), 3)))
q = 2 / mp.mpf(Av)
for eps in ['1e-6', '1e-10']:
    dv = 3 - q - mp.mpf(eps)
    C, cm, Cb, K = g3_ode(Av, gv, dv)
    P('(B) X3 d = 3 - 2/A - %s: c_- %s, ODE coefficient %s, physical %s, fred6 1/(12 sin(pi q)) %s' % (
        eps, mp.nstr(cm, 6), mp.nstr(C, 14), mp.nstr(g3_phys(Av, gv, dv), 14), mp.nstr(1 / (12 * mp.sin(mp.pi * q)), 14)))

# (C) eta moments: (7) (1/pi) int_0^inf eta^(k+1) (1 + eta^2)^(-b-1) = C_b; (10) ratio = 2b/(A lambda) = g/(A(d-1))
Av_, gv_, dv_, bv, lv_, kv = fam(Av, gv, 2.5)
m7 = mp.quad(lambda e: e**(kv + 1) * (1 + e**2)**(-bv - 1), [0, 1, mp.inf]) / mp.pi
m10 = mp.quad(lambda e: e**(kv + 1) * (1 + e**2)**(-bv), [0, 1, mp.inf]) / mp.pi
P('(C) X3 d = 5/2: (1/pi) int eta^(k+1)(1+eta^2)^(-b-1) =', mp.nstr(m7, 15), '; C_b =', mp.nstr(g3_ode(Av, gv, 2.5)[2], 15))
P('(C) moment ratio (10):', mp.nstr(m10 / m7, 15), '; g/(A(d-1)) =', mp.nstr(gv_ / (Av_ * (dv_ - 1)), 15))


# ---------------- (D) R12 ----------------
from series_bj import Bj, r12


def rat_series(R, x, N):
    """Taylor coefficients 0..N of a rational function R(x) analytic at 0 (exact)."""
    num, den = sp.fraction(sp.cancel(R))
    nc = sp.Poly(num, x).all_coeffs()[::-1]
    dc = sp.Poly(den, x).all_coeffs()[::-1]
    nc += [0] * (N + 1 - len(nc))
    dc += [0] * (N + 1 - len(dc))
    c = []
    for n in range(N + 1):
        c.append((nc[n] - sum(dc[i] * c[n - i] for i in range(1, n + 1))) / dc[0])
    return c


def r12_forms(Av, Lv, N=60, frac=sp.Rational(1, 4)):
    """Original and convergent forms of B[w] on R12 (exact rational data). fp int_0^L f, f = pref phi(x) x^(-5-beta):
    on [0, x_c] term by term from the Taylor series of phi (exact), on [x_c, L] by quadrature; x_c = frac L."""
    x = sp.symbols('x', positive=True)
    As, Ls = sp.Rational(Av), sp.Rational(Lv)
    be = 2 / As
    u = x / Ls
    w = -As * x * (1 - u**2) / (1 + u**2)
    gg = x**2 / (1 + u**2)
    a2 = (sp.diff(gg, x) - sp.diff(w, x, 2)) / 2
    Q3 = sp.cancel(a2 / gg**3)
    t1 = sp.cancel(w * sp.diff(gg, x) + (As - sp.diff(w, x)) * gg)       # T_1 residual
    kap = Q3.subs(x, Ls)
    Ro = sp.cancel(sp.diff(Q3, x) * x**6)                      # phi_o = Ro (1 - u^2)^(beta - 1)
    Rc = sp.cancel((Q3 - kap) * x**5 * (1 + u**2))             # phi_c = Rc (1 - u^2)^(beta - 2)
    Rc2 = sp.cancel(Rc / (x - Ls))                             # exact: Rc vanishes at L
    bem, Am, Lm = mp.mpf(be.p) / be.q, mp.mpf(As.p) / As.q, mp.mpf(Ls.p) / Ls.q
    xc = Lm * mp.mpf(frac.p) / frac.q
    res = {'t1': t1}
    for name, R, ev, cexp, pref in [
            ('orig', Ro, None, be - 1, 1 / (3 * Am)),
            ('conv', Rc, Rc2, be - 2, (bem - 1) / (3 * Am))]:
        rc = rat_series(R, x, N)
        bc = [0] * (N + 1)
        for n in range(0, N // 2 + 1):
            bc[2 * n] = sp.binomial(cexp, n) * (-1)**n / Ls**(2 * n)
        ph = [sum(rc[i] * bc[n - i] for i in range(n + 1)) for n in range(N + 1)]
        odd = mp.mpf(sp.N(max(abs(ph[n]) for n in range(1, N + 1, 2)), 20))      # conv: from kappa x^5 (odd, integrable)
        phm = [mp.mpf(sp.Rational(c).p) / sp.Rational(c).q for c in ph]
        fp0 = sum(phm[n] * xc**(n - 4 - bem) / (n - 4 - bem) for n in range(0, N + 1))
        tail = abs(phm[N]) * xc**(N - 4 - bem)
        cm1 = mp.mpf(cexp.p) / cexp.q
        # f(t) with tau = L - t passed separately (no cancellation in L - t near L)
        if ev is None:
            Rf = sp.lambdify(x, R, 'mpmath')
            f = lambda t, tau: Rf(t) * (tau * (Lm + t) / Lm**2)**cm1 * t**(-5 - bem)
        else:
            Rf = sp.lambdify(x, ev, 'mpmath')
            f = lambda t, tau: -tau * Rf(t) * (tau * (Lm + t) / Lm**2)**cm1 * t**(-5 - bem)
        # [x_c, L/2] directly; [L/2, L] with tau = sigma^(1/beta), which removes the tau^(beta - 1) endpoint singularity
        I1 = mp.quad(lambda t: f(t, Lm - t), [xc, Lm / 2])
        I1 += mp.quad(lambda sg: f(Lm - sg**(1 / bem), sg**(1 / bem)) * sg**(1 / bem - 1) / bem, [0, (Lm / 4)**bem, (Lm / 2)**bem])
        res[name] = pref * (fp0 + I1)
        res[name + '_odd'] = odd
        res[name + '_tail'] = tail
    return res


CA, Aval = mp.mpf('0.530666623156826'), mp.mpf('10.150725')
SA = 6 * Aval * (4 * Aval - 3) / (8 * Aval - 1)
for Lv in ['6', '8.6', '5.3435753609604']:
    r = r12_forms('10.150725', Lv)
    p3 = 6 + 2 / Aval
    nat = mp.mpf(Lv)**(p3 - 2)
    ser = Bj(*r12(Aval, mp.mpf(Lv)), Aval, mp.mpf(Lv), 120, [mp.mpf(Lv) / 2], jmax=3)[0][3][0]['B']
    P('(D) R12 A = 10.150725 L = %s: T_1 residual %s; nat units: orig %s conv %s series %s closed %s; |orig-conv| %s |conv-series| %s' % (
        Lv, r['t1'], mp.nstr(r['orig'] * nat, 15), mp.nstr(r['conv'] * nat, 15), mp.nstr(ser * nat, 15),
        mp.nstr(CA * (1 - SA / mp.mpf(Lv)**2), 15), mp.nstr(abs(r['orig'] - r['conv']) * nat, 3), mp.nstr(abs(r['conv'] - ser) * nat, 3)))
    P('(D)   odd Taylor coefficients of phi (max): orig %s conv %s; last-term size at x_c: orig %s conv %s' % (
        mp.nstr(r['orig_odd'], 3), mp.nstr(r['conv_odd'], 3), mp.nstr(r['orig_tail'], 3), mp.nstr(r['conv_tail'], 3)))
for Av, Lv in [('4', '3'), ('3', '2.5')]:
    r = r12_forms(Av, Lv)
    Am = mp.mpf(Av)
    ser = Bj(*r12(Am, mp.mpf(Lv)), Am, mp.mpf(Lv), 120, [mp.mpf(Lv) / 2], jmax=3)[0][3][0]['B']
    P('(D) R12 A = %s (beta = %s) L = %s: orig %s conv %s series %s' % (Av, mp.nstr(2 / Am, 6), Lv, mp.nstr(r['orig'], 15), mp.nstr(r['conv'], 15), mp.nstr(ser, 15)))

# ---------------- (E) saddle modes ----------------
x, y, p = sp.symbols('x y p', positive=True)
for j in range(1, 12, 2):
    n = (j - 1) // 2
    al = sp.symbols('a0:%d' % (n + 1))
    psi = sum(al[i] * x**(p + 1 + 2 * i) * y**(j - 2 * i) for i in range(n + 1))
    eq = sp.expand((-(sp.diff(psi, x, 2) + sp.diff(psi, y, 2)) - sp.diff(x**p * y**j, x)) / x**(p - 1))
    sol = sp.solve([eq.coeff(y, j - 2 * i).subs(x, 1) for i in range(n + 1)], al, dict=True)[0]
    U1 = sp.simplify(-sp.diff(psi, y).subs(sol).subs(y, 0) / x**(p + j))
    cj = (-1)**n * sp.factorial(j) / sp.prod([p + r for r in range(1, j + 1)])
    P('(E) j = %d: U_1(x, 0)/x^(p+j) - c_j = %s' % (j, sp.simplify(U1 - cj)))

open('verifier/early_runs/check_fred8.log', 'w').write('\n'.join(out) + '\n')
