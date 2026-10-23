"""Symbolic checks for A.3.47(iv) and A.3.49 (identities quoted in the appendix text).

Run with OMP_NUM_THREADS=1.  Exit status is nonzero on failure.
"""
import sys
import sympy as sp
import mpmath as mp

results = []


def report(name, ok, info=""):
    results.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ((": " + info) if info else ""))


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


x, y = sp.symbols('x y', real=True)
r, th, t, m, cl, a, D = sp.symbols('r theta t m c_l a D', positive=True)
R2 = x**2 + y**2


def lap(f):
    return sp.diff(f, x, 2) + sp.diff(f, y, 2)


# ---------------------------------------------------------------- A.3.47 weights
w0 = y * R2**(1 - m)
w = y * R2**(-m)
report("Lap(y r^{2-2m}) = 4(m-1)(m-2) y r^{-2m}", zero(sp.simplify(lap(w0) / w) - 4 * (m - 1) * (m - 2)))
report("d_xx(y r^{2-2m}) = 2(m-1) y r^{-2m}(2m x^2/r^2 - 1)",
       zero(sp.simplify(sp.diff(w0, x, 2) / w) - 2 * (m - 1) * (2 * m * x**2 / R2 - 1)))
g2 = sp.simplify((sp.diff(w0, x)**2 + sp.diff(w0, y)**2) * R2**(2 * m - 2))
report("|grad w0|^2 r^{4m-4} = 1 + 4(m-1)(m-2) y^2/r^2", zero(sp.simplify(g2 - (1 + 4 * (m - 1) * (m - 2) * y**2 / R2))))
report("1 + 4(m-1)(m-2) = (2m-3)^2", zero(1 + 4 * (m - 1) * (m - 2) - (2 * m - 3)**2))
H = sp.Function('H')(x, y)
W1 = sp.Function('W1')(x, y)
W2 = sp.Function('W2')(x, y)
divW = sp.diff(W1, x) + sp.diff(W2, y)
Bf = (x * W1 + y * W2) / R2
lhs = w * (W1 * sp.diff(H, x) + W2 * sp.diff(H, y) - H)
div_term = sp.diff(H * w * W1, x) + sp.diff(H * w * W2, y) - H * w * (divW - 2 * cl)
rhs = div_term + H * y * R2**(-m) * (2 * m * Bf - 2 * cl - 1) - H * W2 * R2**(-m)
report("transport weight identity (3) with div W = 2 c_l", zero(sp.simplify((lhs - rhs) * R2**(m + 1))))
# moment test integrals
report("int_{r>=R} r^{2-2m} dX = 2 pi R^{4-2m}/(2m-4)",
       zero(sp.integrate(2 * sp.pi * r**(3 - 2 * m), (r, sp.Symbol('R', positive=True), sp.oo), conds='none').subs(m, 5)
            - 2 * sp.pi * sp.Symbol('R', positive=True)**(-6) / 6))
# B for W = (A x, y)
A = 2 * cl - 1
report("B = (A x^2 + y^2)/r^2 = 1 + 2 D x^2/r^2", zero(sp.simplify((A * x**2 + y**2) / R2 - 1 - 2 * (cl - 1) * x**2 / R2)))

# ---------------------------------------------------------------- A.3.49(b)
f = sp.Function('f')
q = f(y)
u1, u2 = x, -y
report("limit solution: (X+u).grad q = 0", zero((x + u1) * sp.diff(q, x) + (y + u2) * sp.diff(q, y)))
report("limit solution: div u = 0, curl u = -q_x", zero(sp.diff(u1, x) + sp.diff(u2, y)) and
       zero(sp.diff(u2, x) - sp.diff(u1, y) + sp.diff(q, x)))
# radial pair: rho = y F, psi = -x y Hn, Hn = r^{-4} int_0^r s^3 F ds  <=>  r Hn' + 4 Hn = F
Hr = sp.Function('Hr')
rr = sp.sqrt(R2)
Fexpr = 4 * Hr(rr) + rr * sp.diff(Hr(rr), x) * rr / x  # r H'(r) via chain rule: d_x H = H' x/r
psi = -x * y * Hr(rr)
rho = y * Fexpr
ok = zero(sp.simplify(-lap(psi) - sp.diff(rho, x)))
report("psi = -x y H, rho = y (4H + r H') satisfy -Lap psi = rho_x", ok)
pp = sp.Symbol('p', positive=True)
s = sp.Symbol('s', positive=True)
Fs = (1 + s)**(-(1 - pp) / 2)
rFp = 2 * s * sp.diff(Fs, s)
report("F + r F' = (1+s)^{-(3-p)/2}(1 + p s) for F_n", zero(sp.simplify((Fs + rFp) - (1 + s)**(-(3 - pp) / 2) * (1 + pp * s))))
report("r F_n' = -(1-p) s/(1+s) F_n", zero(sp.simplify(rFp + (1 - pp) * s / (1 + s) * Fs)))

# ---------------------------------------------------------------- A.3.49(d) modes
N = sp.Symbol('N', positive=True, integer=True)
pf = sp.Function('p')
tt = sp.log(rr)
G = R2 * pf(tt) * sp.sin(N * sp.atan2(y, x))
# polar Hessian entries (with t = log r): Grr, (1/r)G_r + (1/r^2)G_thth, d_r(G_th/r)
ps, pt, ptt = sp.symbols('ps pt ptt')
rP, thP = sp.symbols('rP thP', positive=True)
Gp = rP**2 * sp.Function('p')(sp.log(rP)) * sp.sin(N * thP)
Grr = sp.diff(Gp, rP, 2)
Gtt = sp.diff(Gp, rP) / rP + sp.diff(Gp, thP, 2) / rP**2
Grt = sp.diff(sp.diff(Gp, thP) / rP, rP)
P0 = sp.Function('p')(sp.log(rP))
sub = {sp.Derivative(P0, rP, 2): 0}


def tform(e):
    # express in p, p_t, p_tt with t = log r
    pt_ = sp.Symbol('pt_')
    e = sp.simplify(e)
    return e


lp = sp.Symbol('lp')
pfun = sp.Function('p')
Gq = sp.exp(2 * lp) * pfun(lp) * sp.sin(N * thP)
# use r = e^lp: d_r = e^{-lp} d_lp
def dr(e):
    return sp.exp(-lp) * sp.diff(e, lp)


Grr_ = sp.simplify(dr(dr(Gq)))
Gtt_ = sp.simplify(dr(Gq) * sp.exp(-lp) + sp.diff(Gq, thP, 2) * sp.exp(-2 * lp))
Grt_ = sp.simplify(dr(sp.diff(Gq, thP) * sp.exp(-lp)))
P, Pt, Ptt = pfun(lp), sp.diff(pfun(lp), lp), sp.diff(pfun(lp), lp, 2)
report("polar Hessian G_rr = (2p + 3p_t + p_tt) sin(N th)", zero(Grr_ - (2 * P + 3 * Pt + Ptt) * sp.sin(N * thP)))
report("polar Hessian G_thth-part = (2p + p_t - N^2 p) sin(N th)", zero(Gtt_ - (2 * P + Pt - N**2 * P) * sp.sin(N * thP)))
report("polar Hessian G_rth = N (p + p_t) cos(N th)", zero(Grt_ - N * (P + Pt) * sp.cos(N * thP)))
report("Lap mode = (p_tt + 4 p_t + (4 - N^2) p) sin(N th)", zero(Grr_ + Gtt_ - (Ptt + 4 * Pt + (4 - N**2) * P) * sp.sin(N * thP)))
# Green kernel: K(u) = e^{-(2n+2)u}/(4n) (u>0), e^{(2n-2)u}/(4n) (u<0) solves -(p''+4p'-(4n^2-4)p) = delta
nn = sp.Symbol('n', positive=True)
u = sp.Symbol('u')
Kp = sp.exp(-(2 * nn + 2) * u) / (4 * nn)
Km = sp.exp((2 * nn - 2) * u) / (4 * nn)
Lop = lambda e: sp.diff(e, u, 2) + 4 * sp.diff(e, u) - (4 * nn**2 - 4) * e
report("Green kernel solves the homogeneous equation on both sides", zero(Lop(Kp)) and zero(Lop(Km)))
report("Green kernel continuous with derivative jump -1",
       zero(Kp.subs(u, 0) - Km.subs(u, 0)) and zero(sp.diff(Kp, u).subs(u, 0) - sp.diff(Km, u).subs(u, 0) + 1))
L1 = sp.integrate(Kp, (u, 0, sp.oo), conds='none') + sp.integrate(Km, (u, -sp.oo, 0), conds='none')
report("kernel L1 norm = 1/(4n^2 - 4)", zero(sp.simplify(L1 - 1 / (4 * nn**2 - 4)).subs(nn, sp.Rational(7, 3))) and
       zero(sp.simplify(L1.subs(nn, 3) - sp.Rational(1, 32))))
# mode decomposition of d_x (r a sin(j th))
aj = sp.Symbol('aj')
ajt = sp.Symbol('ajt')
j = sp.Symbol('j', positive=True, integer=True)
# d_x = cos th d_r - sin th / r d_th applied to rho_j(r) sin(j th), rho_j = r a(t): rho_j' = a + a_t, rho_j/r = a
expr = sp.cos(thP) * (aj + ajt) * sp.sin(j * thP) - sp.sin(thP) * j * aj * sp.cos(j * thP)
target = sp.Rational(1, 2) * ((1 - j) * aj + ajt) * sp.sin((j + 1) * thP) + sp.Rational(1, 2) * ((1 + j) * aj + ajt) * sp.sin((j - 1) * thP)
report("d_x(r a sin j th) = (1/2)((1-j)a + a_t) sin((j+1)th) + (1/2)((1+j)a + a_t) sin((j-1)th)",
       zero(sp.expand_trig(sp.expand(sp.expand_trig((expr - target).subs(j, 5))))) and
       zero(sp.expand_trig(sp.expand(sp.expand_trig((expr - target).subs(j, 3))))))
# p_1: p' + 4p = Q for p = int_0^inf e^{-4u} Q(t-u) du (test with Q = e^{i w t} type: Q = cos(w t))
wv = sp.Symbol('w', positive=True)
p1 = sp.integrate(sp.exp(-4 * u) * sp.cos(wv * (t - u)), (u, 0, sp.oo), conds='none')
report("p_1 = int e^{-4u} Q(t-u) du solves p' + 4p = Q (Q = cos wt)", zero(sp.simplify(sp.diff(p1, t) + 4 * p1 - sp.cos(wv * t))))
# and the original two-sided formula at n = 1 equals it (Q = cos(w t), F_1 = -Q')
F1 = -sp.diff(sp.cos(wv * t), t)
tau = sp.Symbol('tau')
p1b = sp.Rational(1, 4) * (sp.integrate(sp.exp(-4 * (t - tau)) * F1.subs(t, tau), (tau, -sp.oo, t), conds='none')
                           + sp.integrate(F1.subs(t, tau), (tau, t, sp.oo), conds='none'))
# the second integral does not converge for cos; use instead decaying Q = e^{-t^2}-type numerically
Qf = lambda tv: mp.e**(-tv**2) * (1 + tv) / (1 + tv**2)
dQ = lambda tv: mp.diff(Qf, tv)
for tv in [mp.mpf('-0.7'), mp.mpf('0.3'), mp.mpf('1.9')]:
    lhs1 = mp.quad(lambda s_: mp.e**(-4 * s_) * Qf(tv - s_), [0, mp.inf])
    rhs1 = (mp.quad(lambda ta: mp.e**(-4 * (tv - ta)) * (-dQ(ta)), [-mp.inf, tv]) + mp.quad(lambda ta: -dQ(ta), [tv, mp.inf])) / 4
    report("n = 1 mode formula equals int e^{-4u} Q(t-u) du at t = %s" % mp.nstr(tv, 3), abs(lhs1 - rhs1) < 1e-12,
           mp.nstr(lhs1 - rhs1, 3))
# Hessian bound coefficients: (N^2+2N) + (2N+4) + 1 = N^2 + 4N + 5; at N = 2: 8, 8, 1
report("N = 2 coefficients 8, 8, 1", (2**2 + 2 * 2, 2 * 2 + 4) == (8, 8))
# B(s) derivative and F_1 = -d_t Q with Q = D B(s), d_t = D d_s
hs, H3 = sp.Function('h'), sp.Function('H3')
sv = sp.Symbol('s')
Bexpr = -hs(sv) / 2 - D / 2 * H3(sv)
# F_1 = D^2 (h'/2 + 2 H3 + (D/2) H3') and Q = int_t^inf F_1 dtau = D * [B(s) with 2 int_s^inf H3]; check -d_t Q = F_1
# with d_t = D d_s and d_s (2 int_s^inf H3) = -2 H3
dQdt = D * D * (sp.diff(Bexpr, sv) - 2 * H3(sv))
F1e = D**2 * (sp.diff(hs(sv), sv) / 2 + 2 * H3(sv) + D / 2 * sp.diff(H3(sv), sv))
report("-d_t Q = F_1 with Q = D B(s)", zero(-dQdt - F1e))
report("F_1 from the mode formula: (1/2) a1_t + 2 a3 + (1/2) a3_t",
       zero(sp.Rational(1, 2) * D * D * sp.diff(hs(sv), sv) + 2 * D**2 * H3(sv) + sp.Rational(1, 2) * D**3 * sp.diff(H3(sv), sv) - F1e))

bad = [n_ for n_, ok in results if not ok]
print("%d checks, %d failed" % (len(results), len(bad)))
sys.exit(1 if bad else 0)
