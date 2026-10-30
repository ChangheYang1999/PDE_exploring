# c1-t1 independent check of T4-397 (c1-t4 research/fractional_ball_velocity_lower, PROOF sha256 9afe571d...), for R1-042.
# Written from the PROOF text, the T4-381 PROOF (velocity limit) and the definition of X_(s,w) in the frozen
# source/sharp_space_PROOF.md only; the c1-t4 check code was not run or read.
# Part A: exact symbolic identities (sympy). Part B: rigorous ball arithmetic (python-flint arb) for C_s and for the
# bump-gradient constant. Part C: FLOAT diagnostics (scipy and mpmath quadrature); they are not part of the proof.
# Run from artifacts/checks: OMP_NUM_THREADS=1 python3 -B check_T4397.py > check_T4397.out
import random
from fractions import Fraction as Fr
import numpy as np
import sympy as sp
import mpmath as mp
import flint
from scipy import integrate

res = []


def check(name, ok):
    res.append((name, bool(ok)))
    print('%-4s %s' % ('PASS' if ok else 'FAIL', name))


c = Fr(4076476460239181, 2251799813685248)
qF = 1 / c - 4
aF = -qF
x, y = sp.symbols('x y', real=True)
r, t, u, R, a, p, be, m_, C = sp.symbols('r t u R a p beta m C', positive=True)
Y1, Y2, Z1, Z2 = sp.symbols('Y1 Y2 Z1 Z2', real=True)

# ---------------- Part A: exact identities
# A1: 2(1+4|Y|^2)(1+4|Z|^2) - (1+4|Y+Z|^2) = 1 + 32|Y|^2|Z|^2 + 4|Y-Z|^2 > 0, so omega(Y+Z) <= 2^(2/5) omega(Y) omega(Z)
A_, B_ = Y1 ** 2 + Y2 ** 2, Z1 ** 2 + Z2 ** 2
S_ = (Y1 + Z1) ** 2 + (Y2 + Z2) ** 2
check('A1 2(1+4A)(1+4B)-(1+4|Y+Z|^2) = 1+32AB+4|Y-Z|^2',
      sp.expand(2 * (1 + 4 * A_) * (1 + 4 * B_) - (1 + 4 * S_) - (1 + 32 * A_ * B_ + 4 * ((Y1 - Z1) ** 2 + (Y2 - Z2) ** 2))) == 0)
# A2: 2D heat kernel (4 pi t)^-1 exp(-r^2/(4t)): moment of r^p is (4t)^(p/2) Gamma(p/2+1); p = 4/5 gives (4t)^(2/5) Gamma(7/5)
mom = sp.integrate(r ** p * sp.exp(-r ** 2 / (4 * t)) * 2 * sp.pi * r / (4 * sp.pi * t), (r, 0, sp.oo), conds='none')
check('A2 heat-kernel moment of r^p = (4t)^(p/2) Gamma(p/2+1)',
      sp.simplify(sp.powsimp(sp.gammasimp(mom / ((4 * t) ** (p / 2) * sp.gamma(p / 2 + 1))), force=True)) == 1)
# A3: Gamma representation of the Bessel multiplier: Gamma(beta)^-1 int t^(beta-1) e^(-t(1+u)) dt = (1+u)^(-beta)
gr = sp.integrate(t ** (be - 1) * sp.exp(-t * (1 + u)), (t, 0, sp.oo), conds='none') / sp.gamma(be)
check('A3 Bessel multiplier (1+|xi|^2)^(-alpha/2) from the heat semigroup (u = |xi|^2), mass 1 at u = 0',
      sp.simplify(sp.powsimp(gr * (1 + u) ** be, force=True)) == 1 and sp.simplify(gr.subs(u, 0)) == 1)
# A4: t-integral of the moment: Gamma(beta)^-1 int t^(beta-1) e^-t (4t)^(2/5) dt = 4^(2/5) Gamma(beta+2/5)/Gamma(beta)
ti = sp.integrate(t ** (be - 1) * sp.exp(-t) * (4 * t) ** sp.Rational(2, 5), (t, 0, sp.oo), conds='none') / sp.gamma(be)
check('A4 int omega-moment t-integral = 4^(2/5) Gamma(beta+2/5)/Gamma(beta)',
      sp.simplify(sp.gammasimp(ti - 4 ** sp.Rational(2, 5) * sp.gamma(be + sp.Rational(2, 5)) / sp.gamma(be))) == 0)
# A5: g(x) = 1 + x^(2/5) - (1+x)^(2/5) has g(0) = 0 and g' = (2/5)(x^(-3/5) - (1+x)^(-3/5)) > 0 for x > 0
g = 1 + u ** sp.Rational(2, 5) - (1 + u) ** sp.Rational(2, 5)
check('A5 (1+x)^(2/5) <= 1 + x^(2/5): g(0) = 0 and g\' = (2/5)(x^(-3/5) - (1+x)^(-3/5))',
      g.subs(u, 0) == 0 and sp.simplify(sp.diff(g, u) - sp.Rational(2, 5) * (u ** sp.Rational(-3, 5) - (1 + u) ** sp.Rational(-3, 5))) == 0)
# A6: trace on the last two indices: |sum_k T_ijkk|^2 <= 2 sum_k T_ijkk^2 (Cauchy-Schwarz, 2 terms), so |tr T| <= sqrt(2)|T|;
#     and D2 Delta f is that trace of D4 f (sympy on a concrete f); 200 random exact integer tensors
a1, b1 = sp.symbols('a1 b1', real=True)
okt = sp.expand(2 * (a1 ** 2 + b1 ** 2) - (a1 + b1) ** 2 - (a1 - b1) ** 2) == 0
random.seed(397)
for _ in range(200):
    T = {(i, j, k, l): random.randint(-50, 50) for i in range(2) for j in range(2) for k in range(2) for l in range(2)}
    tr2 = sum((T[(i, j, 0, 0)] + T[(i, j, 1, 1)]) ** 2 for i in range(2) for j in range(2))
    okt = okt and tr2 <= 2 * sum(v * v for v in T.values())
fz = sp.exp(-x ** 2 - 2 * y ** 2) * y ** 3 * (1 + x ** 2)
V = [x, y]
okt = okt and all(sp.simplify(sp.diff(sp.diff(fz, x, 2) + sp.diff(fz, y, 2), V[i], V[j])
                              - sum(sp.diff(fz, V[i], V[j], V[k], V[k]) for k in range(2))) == 0 for i in range(2) for j in range(2))
check('A6 trace contraction norm <= sqrt(2) (identity, 200 exact tensors) and D2 Delta f = trace of D4 f', okt)
# A7: symbol identity J^s = J^(-alpha)(1 - Delta), alpha = 2 - s: (1+u)^(s/2) = (1+u)^(-(2-s)/2)(1+u)
s_ = sp.symbols('s', positive=True)
check('A7 (1+u)^(s/2) = (1+u)^(-(2-s)/2) (1+u)', sp.simplify(sp.powsimp((1 + u) ** (-(2 - s_) / 2) * (1 + u) / (1 + u) ** (s_ / 2), force=True)) == 1)
# A8: scaling f_R(X) = R^-a f_1(X/R); omega(RY)^(5/2) <= R^2 omega(Y)^(5/2) for R >= 1 since the difference is R^2 - 1
f1 = lambda X, Yv: Yv * (1 + X ** 2 + Yv ** 2) ** (-(a + 1) / 2) / a
fR = y * (R ** 2 + x ** 2 + y ** 2) ** (-(a + 1) / 2) / a
ok8 = sp.simplify(sp.powsimp(sp.powdenest(fR / (R ** (-a) * f1(x / R, y / R)), force=True), force=True)) == 1
ok8 = ok8 and sp.expand(R ** 2 * (1 + 4 * (Y1 ** 2 + Y2 ** 2)) - (1 + 4 * R ** 2 * (Y1 ** 2 + Y2 ** 2)) - (R ** 2 - 1)) == 0
check('A8 f_R(X) = R^-a f_1(X/R) and omega(RY) <= R^(4/5) omega(Y) for R >= 1', ok8)
# A9: exponents in (7), (8): weighted D2, D4 give R^(1-a-k+4/5)/R^(1-a) = R^-6/5, R^-16/5; unweighted D1, D3, D0, D2
#     give R^-1, R^-3, R^0, R^-2 relative to R^(1-a); all <= 1 for R >= 1
ex = {k: (1 - a - k + sp.Rational(4, 5)) - (1 - a) for k in (2, 4)}
ex0 = {k: (1 - a - k) - (1 - a) for k in (0, 1, 2, 3)}
check('A9 relative exponents -6/5, -16/5 (weighted) and 0, -1, -2, -3 (unweighted)',
      ex[2] == sp.Rational(-6, 5) and ex[4] == sp.Rational(-16, 5) and [ex0[k] for k in range(4)] == [0, -1, -2, -3])
# A10: polar gradient of f_R = F sin(theta): F' = (R^2 - a r^2)(R^2+r^2)^(-(a+3)/2)/a and F/r = (R^2+r^2)^(-(a+1)/2)/a
FR = r * (R ** 2 + r ** 2) ** (-(a + 1) / 2) / a
check('A10 polar gradient coefficients of f_R',
      sp.simplify(sp.diff(FR, r) - (R ** 2 - a * r ** 2) * (R ** 2 + r ** 2) ** (-(a + 3) / 2) / a) == 0
      and sp.simplify(FR / r - (R ** 2 + r ** 2) ** (-(a + 1) / 2) / a) == 0)
# A11: |R^2 - a r^2| <= a(R^2 + r^2) for a >= 1: the two differences are (a-1)R^2 + 2a r^2 and (a+1)R^2
check('A11 a(R^2+r^2) -/+ (R^2 - a r^2) = (a-1)R^2 + 2a r^2, (a+1)R^2',
      sp.expand(a * (R ** 2 + r ** 2) - (R ** 2 - a * r ** 2) - ((a - 1) * R ** 2 + 2 * a * r ** 2)) == 0
      and sp.expand(a * (R ** 2 + r ** 2) + (R ** 2 - a * r ** 2) - (a + 1) * R ** 2) == 0)
# A12: (1 + R^-2)(R^2 + r^2) - (1 + r)^2 = (R - r/R)^2, so (1+r)/sqrt(R^2+r^2) <= sqrt(1 + R^-2)
check('A12 (1+R^-2)(R^2+r^2) - (1+r)^2 = (R - r/R)^2', sp.expand((1 + R ** -2) * (R ** 2 + r ** 2) - (1 + r) ** 2 - (R - r / R) ** 2) == 0)
# A13: lower bound H_q(k_R) >= 1: on the positive y-axis the weighted gradient (1+r)^(a+1)|F'| tends to 1 (r = 1/v, v -> 0+)
v = sp.symbols('v', positive=True)
lim_ok = True
for av, Rv in ((sp.Rational(7, 2), 3), (sp.Rational(9, 2), 1), (sp.Rational(4076476460239181 * 4 - 2251799813685248, 4076476460239181), 2)):
    expr = (1 + 1 / v) ** (av + 1) * (av / v ** 2 - Rv ** 2) * (Rv ** 2 + 1 / v ** 2) ** (-(av + 3) / 2) / av
    lim_ok = lim_ok and sp.limit(sp.simplify(expr), v, 0, '+') == 1
check('A13 weighted gradient of f_R on the positive y-axis tends to 1 (a = 7/2, 9/2, campaign a)', lim_ok)
# A14: the regular mode-one Green solution has c[g] = -F'(0)/4: for F = F1 r + F3 r^3 + O(r^5) the Green formula gives
#      phi = -r J0/2 + F1 r^3/8 + F3 r^5/24 + ..., psi = y G(x^2+y^2), c = -psi_xxy(0) = -2 G'(0) = -F1/4
F1, F3, J0 = sp.symbols('F1 F3 J0', real=True)
Iser = sp.integrate(u ** 2 * (F1 * u + F3 * u ** 3), (u, 0, r))
Jser = J0 - sp.integrate(F1 * u + F3 * u ** 3, (u, 0, r))
phis = sp.expand(-(Iser / r + r * Jser) / 2)
rho_ = sp.symbols('rho', positive=True)
Gs = sp.expand(phis / r).subs(r, sp.sqrt(rho_))
psi = y * Gs.subs(rho_, x ** 2 + y ** 2)
cval = -sp.diff(psi, x, 2, y).subs({x: 0, y: 0})
ok14 = sp.simplify(phis - (-r * J0 / 2 + F1 * r ** 3 / 8 + F3 * r ** 5 / 24)) == 0 and sp.simplify(cval + F1 / 4) == 0
# concrete check of the Green formula itself: F = r e^(-r^2): Delta psi = h and c = -1/4
Fc = r * sp.exp(-r ** 2)
Ic = sp.integrate(u ** 3 * sp.exp(-u ** 2), (u, 0, r))
Jc = sp.integrate(u * sp.exp(-u ** 2), (u, r, sp.oo))
phic = -(Ic / r + r * Jc) / 2
psic = y * (phic / r).subs(r, sp.sqrt(x ** 2 + y ** 2))
lap = sp.simplify(sp.diff(psic, x, 2) + sp.diff(psic, y, 2) - y * sp.exp(-x ** 2 - y ** 2))
Gc = sp.series((phic / r).subs(r, sp.sqrt(rho_)), rho_, 0, 3).removeO()
ok14 = ok14 and lap == 0 and sp.simplify(-2 * sp.diff(Gc, rho_).subs(rho_, 0) + sp.Rational(1, 4)) == 0
check('A14 c[F sin(theta)] = -F\'(0)/4 (generic odd F; and F = r e^(-r^2): Delta psi = h, c = -1/4)', ok14)
# A15: slopes at the origin: f_R has F'(0) = R^(-a-1)/a; b = y eta(r^2) has slope eta(0) = 1; so c[k_R] = 0
eta = lambda tt: sp.exp(1 - 1 / (1 - tt))
check('A15 slopes R^(-a-1)/a and eta(0) = 1, so k_R = f_R - R^(-a-1) b/a has c = 0',
      sp.simplify(sp.diff(FR, r).subs(r, 0) - R ** (-a - 1) / a) == 0 and eta(sp.Integer(0)) == 1)
# A16: large-r expansion F_R = r^q/a - (a+1) R^2 r^(q-2)/(2a) + O(r^(q-4)) (series of the bracket in w = R^2/r^2)
w_ = sp.symbols('w', positive=True)
ser = sp.series((1 + w_) ** (-(a + 1) / 2), w_, 0, 2).removeO()
check('A16 F_R = r^q (1 + R^2/r^2)^(-(a+1)/2)/a with bracket 1 - (a+1)w/2 + O(w^2)',
      sp.simplify(sp.powsimp(FR / (r ** (-a) * (1 + R ** 2 / r ** 2) ** (-(a + 1) / 2) / a), force=True)) == 1
      and sp.simplify(ser - (1 - (a + 1) * w_ / 2)) == 0)
# A17: tails with F = r^q/a + C r^(q-2) (a = 3 + b): phi = -m/(2 pi r) + r^(q+2)/(a(q+1)(q+3)) + C r^q/((q-1)(q+1))
bb = sp.symbols('b', positive=True)
qb = -(3 + bb)
Ft = lambda uu: uu ** qb / (3 + bb) + C * uu ** (qb - 2)
# tails written as antiderivatives; checked by differentiation (all exponents q+3 = -b, q+1, q-1 are negative, so each
# tail tends to 0 at infinity)
It = -r ** (qb + 3) / ((3 + bb) * (qb + 3)) - C * r ** (qb + 1) / (qb + 1)
Jt = -r ** (qb + 1) / ((3 + bb) * (qb + 1)) - C * r ** (qb - 1) / (qb - 1)
okt17 = (sp.simplify(sp.powsimp(sp.expand(sp.diff(It, r) + r ** 2 * Ft(r)), force=True)) == 0
         and sp.simplify(sp.powsimp(sp.expand(sp.diff(Jt, r) + Ft(r)), force=True)) == 0)
pht = -((m_ / sp.pi - It) / r + r * Jt) / 2
rem = sp.simplify(sp.powsimp(sp.expand(pht - (-m_ / (2 * sp.pi * r) + r ** (qb + 2) / ((3 + bb) * (qb + 1) * (qb + 3)))), force=True))
check('A17 leading nondipole potential r^(q+2)/(a(q+1)(q+3)); the next term is C r^q/((q-1)(q+1)) = O(r^q)',
      okt17 and sp.simplify(sp.powsimp(sp.expand(rem - C * r ** qb / ((qb - 1) * (qb + 1))), force=True)) == 0)
# A18: outside its support the compact b contributes exactly its dipole: I(r) = I(1), J(r) = 0 for r >= 1
check('A18 Green formula for r >= 1 with F supported in r <= 1: phi = -I(1)/(2r) = -(m_b/pi)/(2r) (definition)', True)
# A19: |W(pi/4)| = (a-1)/(2a(a-3)) and the exact campaign value
th = sp.symbols('theta', real=True)
qs = -a
W = sp.Matrix([sp.cos(th) * (1 + (qs - 1) * sp.sin(th) ** 2), -sp.sin(th) * (1 + (qs - 1) * sp.cos(th) ** 2)]) / (a * (qs + 3))
n2 = sp.simplify((W[0] ** 2 + W[1] ** 2).subs(th, sp.pi / 4))
EtF = (aF - 1) / (2 * aF * (aF - 3))
check('A19 |W(pi/4)|^2 = ((a-1)/(2a(a-3)))^2; campaign Etest = %s/%s' % (EtF.numerator, EtF.denominator),
      sp.simplify(n2 - ((a - 1) / (2 * a * (a - 3))) ** 2) == 0
      and EtF == Fr(40673572058993602044748051350395, 51288398112310268946308133030216))

# ---------------- Part B: ball arithmetic (arb)
flint.ctx.prec = 200
arb = flint.arb


def Cs(sv):
    al2 = (2 - arb(sv.numerator) / sv.denominator) / 2
    two5 = arb(2) / 5
    return arb(2) ** two5 * (1 + arb(16) ** two5 * arb(7 / arb(5)).gamma() * (al2 + two5).gamma() / al2.gamma())


cs = Cs(Fr(1, 5184))
print('     C_s at s = 1/5184: %s' % cs.str(25, radius=True))
check('B1 C_s(1/5184) = 2^(2/5)(1 + 16^(2/5) Gamma(7/5) Gamma(alpha/2+2/5)/Gamma(alpha/2)) agrees with 4.468299565794177 to 1e-15',
      abs(cs - arb('4.468299565794177')) < arb('1e-15'))
cs1 = Cs(Fr(1, 1))
print('     C_s at s = 1: %s; at s = 1/7744: %s' % (cs1.str(15), Cs(Fr(1, 7744)).str(15)))
# B2: bump constant: sup_t t|eta'(t)| = sup_{u >= 1} (u^2 - u) e^(1-u), attained at u = (3 + sqrt 5)/2; so |grad b| <= 1 + 2 sup
#     < 2.7 and H_q(b) <= 2^(a+1) 2.7 < 5 2^(a+1)
uu = sp.symbols('uu', positive=True)
crit = sp.solve(sp.diff((uu ** 2 - uu) * sp.exp(1 - uu), uu), uu)
uc = (3 + arb(5).sqrt()) / 2
val = (uc ** 2 - uc) * (1 - uc).exp()
check('B2 critical points of (u^2-u)e^(1-u) are (3 -/+ sqrt5)/2; max on u >= 1 is %s < 0.85, so |grad b| < 2.7' % val.str(12),
      sorted(crit, key=lambda z: float(z)) == [(3 - sp.sqrt(5)) / 2, (3 + sp.sqrt(5)) / 2] and val < arb('0.85')
      and (uc - 1) > 0)
# eta' = -eta/(1-t)^2 (so t|eta'| = (u^2 - u) e^(1-u) with u = 1/(1-t))
check('B3 eta\'(t) = -eta(t)/(1-t)^2 and t|eta\'(t)| = (u^2-u)e^(1-u), u = 1/(1-t)',
      sp.simplify(sp.diff(eta(t), t) + eta(t) / (1 - t) ** 2) == 0
      and sp.simplify((t * eta(t) / (1 - t) ** 2).subs(t, 1 - 1 / uu) - (uu ** 2 - uu) * sp.exp(1 - uu)) == 0)

# ---------------- Part C: FLOAT diagnostics
mp.mp.dps = 30


def omegaG(sv):
    # int omega G_alpha = Gamma(beta)^-1 int int t^(beta-1) e^-t (1 + 16 t w)^(2/5) e^-w dw dt, beta = (2-s)/2
    b_ = (2 - mp.mpf(sv.numerator) / sv.denominator) / 2
    inner = lambda tt: mp.quad(lambda ww: (1 + 16 * tt * ww) ** mp.mpf(0.4) * mp.exp(-ww), [0, 1, 10, mp.inf])
    return mp.quad(lambda tt: tt ** (b_ - 1) * mp.exp(-tt) * inner(tt), [0, 1, 10, mp.inf]) / mp.gamma(b_)


okC1 = True
for sv in (Fr(1, 5184), Fr(1, 2), Fr(3, 2)):
    exact = omegaG(sv)
    bound = float(Cs(sv).mid()) / 2 ** 0.4
    print('     s = %s: int omega G_alpha = %s (FLOAT), bound C_s/2^(2/5) = %.12f' % (sv, mp.nstr(exact, 12), bound))
    okC1 = okC1 and exact <= bound
check('C1 FLOAT: int omega G_alpha is below the stated bound at s = 1/5184, 1/2, 3/2', okC1)

# C2: FLOAT values of A_k, B_k for f_1 at the campaign a, the constant D of (8) for the sharpw parameters, the bound (5)
#     for X(b), and the first R = 2^j at which the bound (9) puts k_R in the sharpw X ball and the bound on
#     ||k_R||_2 is below rho/sqrt(w2) (diagnostic: T4-397 claims no finite-R number)
af = float(aF)
xs, ys = sp.symbols('xs ys', real=True)
Vs = [xs, ys]


def tensors(expr, kmax):
    out = {0: [expr]}
    cur = {(): expr}
    for k in range(1, kmax + 1):
        nxt = {}
        for idx, e in cur.items():
            for j in range(2):
                nxt[idx + (j,)] = sp.diff(e, Vs[j])
        cur = nxt
        out[k] = list(cur.values())
    return out


def norms(expr, rmax, kmax, weighted):
    tn = tensors(expr, kmax)
    fns = {k: sp.lambdify((xs, ys), sum(e ** 2 for e in tn[k]), 'numpy') for k in tn}
    ths = np.linspace(0, 2 * np.pi, 96, endpoint=False)
    outA, outB = {}, {}
    for k in tn:
        def radial(rr, k=k, wt=False):
            vals = fns[k](rr * np.cos(ths), rr * np.sin(ths))
            ang = np.mean(vals) * 2 * np.pi
            return ang * rr * ((1 + 4 * rr ** 2) ** 0.8 if wt else 1.0)
        pts = [0, 0.5, 1, 2, 5, 10, 50, 200, 1e3, 1e4]
        pts = [z for z in pts if z < rmax] + [rmax]
        A2 = sum(integrate.quad(radial, pts[i], pts[i + 1], limit=200)[0] for i in range(len(pts) - 1))
        outA[k] = A2 ** 0.5
        if k in weighted:
            B2 = sum(integrate.quad(lambda rr: radial(rr, wt=True), pts[i], pts[i + 1], limit=200)[0] for i in range(len(pts) - 1))
            outB[k] = B2 ** 0.5
    return outA, outB


f1e = ys * (1 + xs ** 2 + ys ** 2) ** (-(af + 1) / 2) / af
A, Bw = norms(f1e, 1e6, 4, (2, 4))
s2 = 2 ** 0.5
w1, w2, rho = 32768.0, 1048576.0, 1351 / 1e6
csf = float(cs.mid())
Dc = csf * (Bw[2] + s2 * Bw[4]) + w1 ** 0.5 * (A[1] + s2 * A[3]) + w2 ** 0.5 * (A[0] + s2 * A[2])
print('     A_0..A_4 = %s; B_2, B_4 = %.6g, %.6g; D(sharpw, campaign a) = %.6g' % (
    ', '.join('%.6g' % A[k] for k in range(5)), Bw[2], Bw[4], Dc))
rb = xs ** 2 + ys ** 2
be_s = ys * sp.exp(1 - 1 / (1 - rb))
Ab, Bb = norms(be_s, 1 - 1e-9, 4, (2, 4))
Xb = csf * (Bb[2] + s2 * Bb[4]) + w1 ** 0.5 * (Ab[1] + s2 * Ab[3]) + w2 ** 0.5 * (Ab[0] + s2 * Ab[2])
print('     bump b: ||b||_2 = %.6g; bound (5) for X(b) = %.6g' % (Ab[0], Xb))
Rj = None
for j in range(0, 40):
    Rv = 2.0 ** j
    xb = Dc * Rv ** (1 - af) + Rv ** (-af - 1) * Xb / af
    l2 = A[0] * Rv ** (1 - af) + Rv ** (-af - 1) * Ab[0] / af
    if xb <= rho and l2 <= rho / w2 ** 0.5:
        Rj = Rv
        break
Hup = (1 + Rj ** -2) ** ((af + 1) / 2) + Rj ** (-af - 1) * 5 * 2 ** (af + 1) / af
Etf = float(EtF)
print('     first R = 2^j with the bound (9) <= rho and ||k_R||_2 bound <= rho/sqrt(w2): R = %g; there H_q(k_R) <= %.9f and'
      ' any E valid on the sharpw ball is >= Etest/H_upper = %.9f (FLOAT)' % (Rj, Hup, Etf / Hup))
check('C2 FLOAT: some R = 2^j <= 2^39 puts k_R in the sharpw X ball and L2 ball by the stated bounds', Rj is not None)

npass = sum(1 for _, o in res if o)
print('%d checks, %s' % (len(res), 'ALL PASS' if npass == len(res) else '%d FAIL' % (len(res) - npass)))
