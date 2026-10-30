# c1-t1 independent check of T4-410 (c1-t4 research/two_weight_velocity_remainder, PROOF sha256 cd2e6f18...), for R1-043.
# Written from the PROOF text, the T4-335 PROOF (research/moment_resolved_tail) and c1-t2 REVIEW_T4_402 section 4 only;
# the c1-t4 check code was not run or read.
# Part A: exact symbolic identities (sympy). Part B: rigorous ball arithmetic (python-flint arb) for the constants of
# (1) at the campaign exponent, the radius r_beta of REVIEW_T4_402 (F1) and lower bounds of the right side of (8).
# Part C: FLOAT diagnostics (mpmath quadrature); they are not part of any proof.
# Run from artifacts/checks: OMP_NUM_THREADS=1 python3 -B check_T4410.py > check_T4410.out
import json
from fractions import Fraction as Fr
import sympy as sp
import mpmath as mp
import flint

res = []


def check(name, ok):
    res.append((name, bool(ok)))
    print('%-4s %s' % ('PASS' if ok else 'FAIL', name))


c = Fr(4076476460239181, 2251799813685248)
qF = 1 / c - 4
dF = 1 - 1 / c
x, y = sp.symbols('x y', real=True)
r, s, t, u = sp.symbols('r s t u', positive=True)
A, B, D, L, k, R0, eta = sp.symbols('A B D L k R0 eta', positive=True)
al = sp.symbols('alpha', positive=True)   # alpha = -a in (3, 5)
ep = sp.symbols('epsilon', positive=True)
a = -al

# ---------------- Part A: exact identities
# A1: kernel. K2 + i K1 = 1/(2 pi z^2); |K| = 1/(2 pi |Z|^2); zero angular mean; f' = -1/(pi z^3), f''' = -12/(pi z^5)
R2 = x ** 2 + y ** 2
K1 = -x * y / (sp.pi * R2 ** 2)
K2 = (x ** 2 - y ** 2) / (2 * sp.pi * R2 ** 2)
z = sp.symbols('z')
f = 1 / (2 * sp.pi * z ** 2)
ok = sp.simplify(sp.expand_complex(K2 + sp.I * K1 - f.subs(z, x + sp.I * y))) == 0
ok = ok and sp.simplify(K1 ** 2 + K2 ** 2 - 1 / (4 * sp.pi ** 2 * R2 ** 2)) == 0
th = sp.symbols('theta', real=True)
pol = {x: sp.cos(th), y: sp.sin(th)}
ok = ok and sp.integrate(K1.subs(pol), (th, 0, 2 * sp.pi)) == 0 and sp.integrate(sp.simplify(K2.subs(pol)), (th, 0, 2 * sp.pi)) == 0
ok = ok and sp.simplify(sp.diff(f, z) + 1 / (sp.pi * z ** 3)) == 0 and sp.simplify(sp.diff(f, z, 3) + 12 / (sp.pi * z ** 5)) == 0
# Taylor remainder bound: (1/3!) 12 |Y|^3/(pi |xi|^5) with |xi| >= r/2 gives 64 |Y|^3/(pi r^5)
ok = ok and sp.simplify(sp.Rational(12, 6) / (r / 2) ** 5 - 64 / r ** 5) == 0
check('A1 K = 1/(2 pi z^2) (v2 + i v1), |K| = 1/(2 pi |Z|^2), zero angular mean, |f\'| = 1/(pi|z|^3), Taylor bound 64|Y|^3/(pi r^5)', ok)

# A2: local term. int_0^(r/2) min(L, 2B/s) ds: = L r/2 if L r/2 <= 2B, else 2B(1 + log(L r/(4B))); and L r/(4B) = k r^eps
s0 = 2 * B / L
I2 = L * s0 + sp.integrate(2 * B / s, (s, s0, r / 2))
ok = sp.simplify(sp.expand_log(I2 - 2 * B * (1 + sp.log(L * r / (4 * B))), force=True)) == 0
q_ = a + ep   # gradient weight q = a + epsilon
Bv = A * (r / 2) ** a
Lv = D * (r / 2) ** (q_ - 1)
kv = D / (2 ** (ep + 1) * A)
ok = ok and sp.simplify(sp.powsimp(sp.powdenest(Lv * r / (4 * Bv) / (kv * r ** ep), force=True), force=True)) == 0 + 1
ok = ok and sp.simplify(sp.powsimp(2 * Bv / (2 ** (1 - a) * A * r ** a), force=True)) == 1
check('A2 local integral of min(L, 2B/s) and L r/(4B) = k r^eps, 2B = 2^(1-a) A r^a', ok)

# A3 annulus, A4 far field, A5 moment replacement, A6 Taylor remainder (integrals with s^a in place of (1+s)^a, a < 0)
ann = 4 * sp.pi * r ** 2 * 2 / (sp.pi * r ** 2) * A * (r / 2) ** a
far = sp.integrate(2 / (sp.pi * s ** 2) * A * s ** a * 2 * sp.pi * s, (s, 2 * r, sp.oo), conds='none')
mom = sp.integrate(s * A * s ** a * 2 * sp.pi * s, (s, r / 2, sp.oo), conds='none') / (sp.pi * r ** 3)
tay = 128 * A / r ** 5 * sp.integrate(s ** (4 + a), (s, 0, r / 2), conds='none')
ok3 = sp.simplify(sp.powsimp(ann / (2 ** (3 - a) * A * r ** a), force=True)) == 1
ok4 = sp.simplify(sp.powsimp(far / (2 ** (a + 2) * A * r ** a / (-a)), force=True)) == 1
ok5 = sp.simplify(sp.powsimp(mom / (2 ** (-a - 2) * A * r ** a / (-a - 3)), force=True)) == 1
ok6 = sp.simplify(sp.powsimp(tay / (2 ** (2 - a) * A * r ** a / (a + 5)), force=True)) == 1
check('A3-A6 annulus 2^(3-a), far 2^(a+2)/(-a), moment 2^(-a-2)/(-a-3), Taylor 2^(2-a)/(a+5) (times A r^a)',
      ok3 and ok4 and ok5 and ok6)

# A7: J'(r) on k r^eps > 1 and the step behind (4)
Ca, La = sp.symbols('C_a L_a', positive=True)
J = A * r ** (-ep) * (Ca + La * (1 + sp.log(k) + ep * sp.log(r)))
dJ = sp.diff(J, r)
ok = sp.simplify(dJ + ep * A * r ** (-ep - 1) * (Ca + La * (sp.log(k) + ep * sp.log(r)))) == 0
X_, l_ = sp.symbols('X l', nonnegative=True)
lhs = sp.exp(-X_ / 2) * (Ca + La * (2 + l_)) - sp.exp(-X_) * (Ca + La * (1 + l_) + La * X_)
rhs = sp.exp(-X_ / 2) * ((Ca + La * (1 + l_)) * (1 - sp.exp(-X_ / 2)) + La * (1 - X_ * sp.exp(-X_ / 2)))
xm = sp.solve(sp.diff(X_ * sp.exp(-X_ / 2), X_), X_)
ok = ok and sp.simplify(lhs - rhs) == 0 and xm == [2] and sp.N(2 / sp.E) < 1
check('A7 J\' = -eps A r^(-eps-1)[C_a + L_a log(k r^eps)] and the e^(-x/2) step of (4) (max of x e^(-x/2) is 2/e < 1)', ok)

# A8: cutoff chi = 3t^2 - 2t^3: C1 at both ends, and |r chi'| = 6 t (1 - t^2) <= 4/sqrt(3) < 3
chi = 3 * t ** 2 - 2 * t ** 3
dchi_dr = sp.diff(chi, t) / R0
rchi = sp.expand((1 + t) * R0 * dchi_dr)
crit = sp.solve(sp.diff(rchi, t), t)
ok = chi.subs(t, 0) == 0 and chi.subs(t, 1) == 1 and sp.diff(chi, t).subs(t, 0) == 0 and sp.diff(chi, t).subs(t, 1) == 0
ok = ok and sp.simplify(rchi - 6 * t * (1 - t ** 2)) == 0 and crit == [1 / sp.sqrt(3)]
ok = ok and sp.simplify(rchi.subs(t, 1 / sp.sqrt(3)) - 4 / sp.sqrt(3)) == 0 and 4 / sp.sqrt(3) < 3
check('A8 cutoff is C1 and sup |r chi\'| = 4/sqrt(3) < 3', ok)

# A9: mode-n Green formula solves A'' + A'/r - n^2 A/r^2 = f (generic f, symbolic n), and its exterior form
n = sp.symbols('n', positive=True)
F = sp.Function('f')
Gr = -(r ** (-n) * sp.Integral(s ** (n + 1) * F(s), (s, 0, r)) + r ** n * sp.Integral(s ** (1 - n) * F(s), (s, r, sp.oo))) / (2 * n)
ode = sp.diff(Gr, r, 2) + sp.diff(Gr, r) / r - n ** 2 * Gr / r ** 2 - F(r)
ok = sp.simplify(ode.doit()) == 0
# exterior r >= L0 with chi = 1 there: int_0^r s^(n+1) chi s^q = r^(n+q+2)/(n+q+2) - J_n, int_r^oo s^(1-n+q) = r^(q+2-n)/(n-q-2)
qq, bn, Jn = sp.symbols('q b_n J_n', real=True)
p = qq + 2
An = -(r ** (-n) * (r ** (n + qq + 2) / (n + qq + 2) - Jn) + r ** n * r ** (qq + 2 - n) / (n - qq - 2)) * bn / (2 * n)
ok = ok and sp.simplify(sp.powsimp(sp.expand(An - (bn * r ** p / (p ** 2 - n ** 2) + bn * Jn * r ** (-n) / (2 * n))), force=True)) == 0
# n = 1: A_1 = -I_inf/(2r) + b_1 r^p/(p^2 - 1) (tails of s^2 f and f beyond r, q in (-5, -3))
Iinf = sp.symbols('I_inf', positive=True)
bq = sp.symbols('beta', positive=True)      # q = -3 - beta
q1 = -3 - bq
A1 = -((Iinf - sp.integrate(s ** (2 + q1), (s, r, sp.oo), conds='none') * bn) / r
       + r * sp.integrate(s ** q1, (s, r, sp.oo), conds='none') * bn) / 2
ok = ok and sp.simplify(sp.powsimp(sp.expand(A1 - (-Iinf / (2 * r) + bn * r ** (q1 + 2) / ((q1 + 2) ** 2 - 1))), force=True)) == 0
check('A9 mode-n Green formula; exterior A_n = b_n r^p/(p^2-n^2) + b_n J_n r^-n/(2n) (n >= 3) and A_1 with the dipole', ok)

# A10: Hessian pair (phi_xy, -phi_xx) of r^-n sin(n theta) has magnitude n(n+1) r^(-n-2), n = 3, 5, 7, 9
ok = True
for nn in (3, 5, 7, 9):
    phi = sp.im(sp.expand((x + sp.I * y) ** nn)) / R2 ** nn
    hx = sp.diff(phi, x, y)
    hxx = sp.diff(phi, x, 2)
    val = sp.simplify(sp.factor(sp.together(hx ** 2 + hxx ** 2)) * R2 ** (nn + 2))
    ok = ok and sp.simplify(val - nn ** 2 * (nn + 1) ** 2) == 0
check('A10 |(phi_xy, -phi_xx)| = n(n+1) r^(-n-2) for phi = r^-n sin(n theta), n = 3, 5, 7, 9 (general n: phi = Re(i z^-n))', ok)

# A11: the per-mode error after division by r^q and its bound by (L0/r)^(q+5)
L0 = sp.symbols('L0', positive=True)
err = bn * (L0 ** (n + qq + 2) / (n + qq + 2)) / (2 * n) * n * (n + 1) * r ** (-n - 2) / r ** qq
ok = sp.simplify(sp.powsimp(err / (bn * (n + 1) / (2 * (n + qq + 2)) * (L0 / r) ** (n + qq + 2)), force=True)) == 1
check('A11 mode-n cutoff error = |b_n|(n+1)/(2(n+q+2)) (L0/r)^(n+q+2), and n+q+2 >= q+5 > 0 for n >= 3', ok)

# A12: polar gradient of h_b = chi(r) r^q b(theta): |grad|^2 = r^(2q-2)[(r chi' + q chi)^2 b^2 + chi^2 b'^2]
#      (checked with the concrete smooth radial factor chi(r) = r^2/(3 + r^2) in place of the cutoff, which enters only
#      through chi and chi'); then |grad h_b| <= r^(q-1)(|r chi'| B0 + sqrt(q^2 b^2 + b'^2)) by the triangle inequality
bb = sp.sin(th) / 3 + sp.Rational(2, 7) * sp.sin(3 * th) - sp.sin(5 * th) / 11
chic = lambda e: e ** 2 / (3 + e ** 2)
ok = True
for qv in (sp.Rational(-7, 2), sp.Rational(-17, 5)):
    rr = sp.sqrt(R2)
    hb = chic(rr) * rr ** qv * bb.subs(th, sp.atan2(y, x))
    g2 = sp.diff(hb, x) ** 2 + sp.diff(hb, y) ** 2
    for (xv, yv) in ((sp.Rational(3, 2), sp.Rational(5, 4)), (sp.Rational(-7, 3), sp.Rational(2, 5))):
        rv = sp.sqrt(xv ** 2 + yv ** 2)
        tv = sp.atan2(yv, xv)
        cv = chic(rv)
        cr = sp.diff(chic(r), r).subs(r, rv)
        rhs_ = rv ** (2 * qv - 2) * ((rv * cr + qv * cv) ** 2 * bb.subs(th, tv) ** 2 + cv ** 2 * sp.diff(bb, th).subs(th, tv) ** 2)
        e = g2.subs({x: xv, y: yv}) - rhs_
        ok = ok and abs(sp.N(e, 50)) < 1e-40
Xs, Ys, Zs = sp.symbols('X Y Z', real=True)
ok = ok and sp.expand((sp.Abs(Xs) + sp.sqrt(Ys ** 2 + Zs ** 2)) ** 2 - ((Xs + Ys) ** 2 + Zs ** 2)
                      - 2 * (sp.Abs(Xs) * sp.sqrt(Ys ** 2 + Zs ** 2) - Xs * Ys)).subs(sp.Abs(Xs) ** 2, Xs ** 2) == 0
check('A12 polar gradient of chi(r) r^q b(theta) at 2 points x 2 exponents (50 digits), and the triangle step', ok)

# A13: lower bounds of the constants for every a in (-5, -3): 2^-a > 8, C_a > 1/2 + 2^(3-a) > 64.5, L_a = 2^(1-a) > 16
check('A13 for -5 < a < -3: 2^(-a) (C_a + L_a) > 8 (1/2 + 64 + 16) = 644 (each term of C_a is positive)', 8 * (Fr(1, 2) + 64 + 16) == 644)

# ---------------- Part B: ball arithmetic (arb)
flint.ctx.prec = 200
arb = flint.arb


def A_(fr):
    return arb(fr.numerator) / fr.denominator


qA, dA = A_(qF), A_(dF)
two = arb(2)


def consts(aa):
    Cv = arb(1) / 2 + two ** (3 - aa) + two ** (aa + 2) / (-aa) + two ** (-aa - 2) / (-aa - 3) + two ** (2 - aa) / (aa + 5)
    Lv_ = two ** (1 - aa)
    return Cv, Lv_


aD = qA - dA
CaD, LaD = consts(aD)
print('     campaign q = %s, delta = 1 - 1/c = %s, a = q - delta = %s' % (qA.str(16), dA.str(16), aD.str(16)))
print('     at a = q - delta: C_a = %s, L_a = %s, C_a + L_a = %s, 2^(-a)(C_a + L_a) = %s' % (
    CaD.str(10), LaD.str(10), (CaD + LaD).str(10), (two ** (-aD) * (CaD + LaD)).str(10)))
check('B1 at a = q - delta: 200 < C_a + L_a < 210 and 2^(-a)(C_a + L_a) > 3000',
      (CaD + LaD) > 200 and (CaD + LaD) < 210 and two ** (-aD) * (CaD + LaD) > 3000)

# B2: r_beta of REVIEW_T4_402 (F1): r_beta = (B0/(beta sqrt(-2q-2)))^(1/(-q-1)), B0 the angular projection bound of the
#     T4-380 inputs (upper end); sharpw ceiling 28496/10^10 and TB ceiling 3793/10^9
inp = json.load(open('data/T4380_inputs.json'))
assert Fr(inp['q']) == qF and Fr(inp['delta']) == dF


def arbint(sv):
    body = sv.strip()[1:-1]
    mid, rad = body.split('+/-')
    return Fr(mid.strip()) - Fr(rad.strip()), Fr(mid.strip()) + Fr(rad.strip())


# targets: sharpw and TB family ceilings, graded ceiling, fixed sharpw ball (the smallest beta, so the largest r_beta)
BETAS = (('sharpw', Fr(28496, 10 ** 10)), ('TB', Fr(3793, 10 ** 9)), ('graded', Fr(25, 54684)),
         ('fixed', Fr(1351, 1024000000)))
rbeta, kcrit, ratio = {}, {}, {}
DdA = A_(Fr(inp['D']))
s2pi = (2 * arb.pi()).sqrt()
Hlo = None
for row in inp['rows']:
    Bhi = A_(arbint(row['B'])[1])
    Blo = A_(arbint(row['B'])[0])
    g0 = A_(Fr(row['G_lower_exact']))
    hl = arbint(row['H_point'])[0]
    Hlo = hl if Hlo is None else min(Hlo, hl)
    for bn_, bv in BETAS:
        rb = (Bhi / (A_(bv) * (-2 * qA - 2).sqrt())) ** (1 / (-qA - 1))
        rbeta[(row['candidate'], bn_)] = rb
        kcrit[(row['candidate'], bn_)] = DdA * Bhi * rb ** dA / (s2pi * g0)
        # Kcrit/(B0/sqrt(2 pi)) with B0 at its lower end in the denominator: an upper bound of the allowed factor
        ratio[(row['candidate'], bn_)] = DdA * rb ** dA / g0 * Bhi / Blo
        print('     %s %-6s r_beta <= %s, Kcrit <= %s, Kcrit/(B0/sqrt(2 pi)) <= %s' % (
            row['candidate'], bn_, (rb + rb.rad()).str(12, radius=False),
            (kcrit[(row['candidate'], bn_)] + kcrit[(row['candidate'], bn_)].rad()).str(10, radius=False),
            (ratio[(row['candidate'], bn_)] + ratio[(row['candidate'], bn_)].rad()).str(8, radius=False)))
check('B2 r_beta and Kcrit (sharpw) agree with REVIEW_T4_402 (13761.47 / 13761.57 / 13761.43; 681750.9 / 681765.5 / '
      '681745.1, to 0.1) and are smaller at TB',
      all(abs(rbeta[(cn, 'sharpw')] - arb(v)) < arb('0.01') for cn, v in (('007', '13761.47'), ('013', '13761.57'),
                                                                        ('014', '13761.43')))
      and all(abs(kcrit[(cn, 'sharpw')] - arb(v)) < arb('0.1') for cn, v in (('007', '681750.9'), ('013', '681765.5'),
                                                                           ('014', '681745.1')))
      and all(rbeta[(cn, 'TB')] < rbeta[(cn, 'sharpw')] and kcrit[(cn, 'TB')] < kcrit[(cn, 'sharpw')]
              for cn in ('007', '013', '014')))
Rs = arb(1376158) / 100
Rm = arb(1886000) / 100
Km = arb(6817656) / 10
check('B2b sharpw and TB: every r_beta < 13761.58 and every Kcrit < 681765.6; all four targets: every r_beta < 18860',
      all(rbeta[(cn, bn_)] < Rs and kcrit[(cn, bn_)] < Km for cn in ('007', '013', '014') for bn_ in ('sharpw', 'TB'))
      and all(v < Rm for v in rbeta.values()))

# Lower bound of the constant for every exponent a = q - eps with 0 < eps <= delta (so -q < -a <= -q + delta): each term
# of C_a is positive and 2^(3-a) + 2^(1-a) = 5 2^(1-a) > 5 2^(1-q), so C_a + L_a > lam1 = 1/2 + 5 2^(1-q) and
# 2^(-a)(C_a + L_a) > lam2 = 2^(-q) lam1
lam1 = arb(1) / 2 + 5 * two ** (1 - qA)
lam2 = two ** (-qA) * lam1
print('     lam1 = 1/2 + 5 2^(1-q) = %s; lam2 = 2^(-q) lam1 = %s' % (lam1.str(10), lam2.str(10)))
check('B3a lam1 > 109 and lam2 > 1190', lam1 > 109 and lam2 > 1190)

# B3 (obstruction through A_in). If (6) is T4-335 (7), its list contains the exponent delta, so eps <= delta. With
#    R0 >= 2 (L0 >= 4) and L0 <= r <= Rm: by (1) and (5) at the radius r itself the T4-410 bound is J(r) + B_b(L0/r)^(q+5)
#    >= J(r) >= A_in r^-eps (C_a + L_a) >= H ((1 + L0)/r)^eps lam1 >= H (5/Rm)^delta lam1, since 5/r < 1 and
#    0 < eps <= delta give (5/r)^eps >= (5/r)^delta when r >= 5, and ((1 + L0)/r)^eps >= 1 when r <= 5
lowS = (5 / Rs) ** dA * lam1
low = (5 / Rm) ** dA * lam1
print('     B3: T4-410 bound/H >= %s at every r in [L0, 13761.58] and >= %s at every r in [L0, 18860] (eps <= delta)' % (
    (lowS - lowS.rad()).str(8, radius=False), (low - low.rad()).str(8, radius=False)))
kH = Km / A_(Hlo)
print('     Kcrit/H <= Kcrit_max/H_point_min < %s' % (kH + kH.rad()).str(8, radius=False))
check('B3 the T4-410 remainder bound exceeds 3.1 H on [L0, 13761.58] (sharpw, TB) and 2.7 H on [L0, 18860] (all four '
      'targets): above the audited universal constant 1.747261 (T4-411), above Kcrit/H (< 0.682) and above every room',
      lowS > arb('3.1') and low > arb('2.7') and low > arb('1.747261') and kH < arb('0.682'))

# B4 radius at which the A_in lower bound of B3 falls to a given room: r >= 5 (lam1/room)^(1/delta).
#    Rooms: 0.09893906 (REVIEW_T4_402 (F2), Eprof = 583/1000, cutoff test); with Eprof = 93/250 (T4-415, OPEN) and the
#    full-integral E bounds of T4-414 (OPEN): 0.527596 - 0.372, 0.458292 - 0.372, 0.434940 - 0.372; and the margin
#    1.747261 - 0.372 below the universal constant
okB4 = True
for nm, rm_ in (('F2 cutoff room, 583/1000', '0.09893906'), ('fixed sharpw, 93/250', '0.155596'),
                ('sharpw family, 93/250', '0.086292'), ('TB, 93/250', '0.06294'), ('universal margin', '1.375261')):
    rn = 5 * (lam1 / arb(rm_)) ** (1 / dA)
    print('     B4: room %-10s (%s): the A_in lower bound reaches it only for r >= %s' % (rm_, nm, (rn - rn.rad()).str(6, radius=False)))
    okB4 = okB4 and rn > 4 * Rm
RneedD = 5 * ((CaD + LaD) / arb('0.09893906')) ** (1 / dA)
print('     B4: with the constants at eps = delta the (F2) room needs r >= %s' % (RneedD - RneedD.rad()).str(6, radius=False))
check('B4 every listed room is reached by the A_in lower bound only beyond 4 times the largest r_beta (> 75000)', okB4)

# B5 (obstruction through A_out, independent of H, E, V and t). The T4-335 (7) term C3 r^(q-delta) with
#    C3 = H(V + E G)/D_delta >= H E g0/D_delta satisfies C3 R^-delta >= B0/sqrt(2 pi) for R <= r_grad (definition of
#    r_grad, REVIEW_T4_375 (c), REVIEW_T4_402 section 4). With eps <= delta and L0 <= R:
#    A R^-eps >= A_out R^-eps >= 2^-a C3 L0^(eps-delta) R^-eps >= 2^-a C3 R^-delta, so J(R) >= lam2 B0/sqrt(2 pi).
#    Kcrit = (B0/sqrt(2 pi)) D_delta r_beta^delta/g0. So J(R)/Kcrit >= lam2/ratio.
mins = min((lam2 / v) for v in ratio.values())
mins1 = min((lam1 / v) for v in ratio.values())
print('     B5: for L0 <= R <= r_grad, J(R)/Kcrit >= lam2 g0/(D_delta r_beta^delta) >= %s' % (mins - mins.rad()).str(6, radius=False))
print('         with the sharper factor (1 + 1/L0)^(-a) >= 1 in place of 2^(-a): J(R)/Kcrit >= %s' % (
    (mins1 - mins1.rad()).str(6, radius=False)))
check('B5 J(R) > 50 Kcrit for every L0 <= R <= r_grad (all three candidates, all four targets), and > 4.7 Kcrit even with '
      'the factor 2^(-a) of A_out removed', mins > 50 and mins1 > 4.7)
mx = max(ratio.values(), key=lambda v: float(v.mid()))
print('     any remainder bound of the form lam (C0 tail term at R) certifies (F3) only if lam < %s (kappa >= 0, V >= 0)' %
      (mx + mx.rad()).str(6, radius=False))
check('B6 the factor allowed by (F3) is below 23.2 (upper bound over candidates and the four targets)', mx < arb('23.2'))

# B7 radius-dependent use inside the T4-335 transport integral. T4-335 bounds e by integrating
#    c r^(gamma+1) d/dr(r^-gamma e) = forcing from r to infinity, gamma = 1/c. A velocity coefficient E(s) (|w(s)| <=
#    E(s) H s^q) gives the term (H G/c) r^gamma int_r^oo E(s) s^(q-delta-gamma-1) ds = H G r^(q-delta) Eeff(r)/D_delta with
#    Eeff(r) = kap r^kap int_r^oo E(s) s^(-kap-1) ds, kap = gamma + delta - q = 5 - 1/c, D_delta = c kap (checked exactly).
#    (CI) is positive at r only if Eeff(r) < (r/r_beta)^delta Kcrit/H <= Kcrit/H for r <= r_beta.
#    (i) E(s) >= T4-410 bound/H >= lam1 (5/s)^delta gives Eeff(r) >= lam1 (5/r)^delta kap/(kap + delta).
#    (ii) E(s) = min(1.747261, T4-410 bound/H) >= 1.747261 on s <= r_u = 5 (lam1/1.747261)^(1/delta), so
#         Eeff(r) >= 1.747261 (1 - (r/r_u)^kap).
gam = 1 / c
kapF = gam + dF - qF
check('B7a kap = 5 - 1/c, D_delta = c kap, q - delta - gamma = -kap (exact)',
      kapF == 5 - 1 / c and Fr(inp['D']) == c * kapF and qF - dF - gam == -kapF)
kapA = A_(kapF)
ss_, rr_, kk_, dd_ = sp.symbols('s r kappa d', positive=True)
okI = sp.simplify(kk_ * rr_ ** kk_ * sp.integrate(ss_ ** (-dd_ - kk_ - 1), (ss_, rr_, sp.oo), conds='none')
                  - kk_ / (kk_ + dd_) * rr_ ** (-dd_)) == 0
eeff1 = lam1 * (5 / Rm) ** dA * kapA / (kapA + dA)
ru = 5 * (lam1 / arb('1.747261')) ** (1 / dA)
eeff2 = arb('1.747261') * (1 - (Rm / ru) ** kapA)
kHf = max(kcrit.values(), key=lambda v: float(v.mid())) / A_(Hlo)
print('     B7: kap = %s; for r <= 18860: Eeff >= %s (T4-410 alone), >= %s (minimum with 1.747261, r_u >= %s); '
      'Kcrit/H <= %s' % (kapA.str(10), (eeff1 - eeff1.rad()).str(6, radius=False), (eeff2 - eeff2.rad()).str(6, radius=False),
                          (ru - ru.rad()).str(6, radius=False), (kHf + kHf.rad()).str(6, radius=False)))
check('B7 radius-dependent use: Eeff(r) > 2.49 (T4-410 alone) and > 1.72 (minimum with the universal constant) for '
      'every r <= 18860, above Kcrit/H < 0.7851 (all four targets)', okI and eeff1 > arb('2.49') and eeff2 > arb('1.72')
      and kHf < arb('0.7851'))

# ---------------- Part C: FLOAT diagnostics
mp.mp.dps = 30
# C1: the cutoff model (5) for q = campaign q, R0 = 2, b = sin/3 + (2/7) sin 3 - sin 5/11: velocity from the mode Green
#     formula by quadrature; compare r^-q |U + DK M - r^q V_q[b]| with B_b (L0/r)^(q+5)
qm = mp.mpf(qF.numerator) / qF.denominator
R0m = mp.mpf(2)
L0m = 2 * R0m
bcoef = {1: mp.mpf(1) / 3, 3: mp.mpf(2) / 7, 5: -mp.mpf(1) / 11}


def chim(rv):
    if rv <= R0m:
        return mp.mpf(0)
    if rv >= L0m:
        return mp.mpf(1)
    tt = rv / R0m - 1
    return 3 * tt ** 2 - 2 * tt ** 3


def mode(nn, rv):
    fn = lambda sv: chim(sv) * sv ** qm * bcoef[nn]
    I = mp.quad(lambda sv: sv ** (nn + 1) * fn(sv), [0, R0m, L0m] + ([rv] if rv > L0m else []))
    Jt = mp.quad(lambda sv: sv ** (1 - nn) * fn(sv), [rv, 10 * rv, mp.inf])
    A0 = -(rv ** (-nn) * I + rv ** nn * Jt) / (2 * nn)
    A1v = (rv ** (-nn - 1) * I - rv ** (nn - 1) * Jt) / 2
    A2v = fn(rv) - A1v / rv + nn ** 2 * A0 / rv ** 2
    return A0, A1v, A2v, I


def hess_vel(rv, ph, modes):
    hxy = mp.mpf(0)
    hxx = mp.mpf(0)
    for nn in bcoef:
        A0, A1v, A2v, _ = modes[nn]
        S, C = mp.sin(nn * ph), mp.cos(nn * ph)
        prr, pr, ptt, prt, pt = A2v * S, A1v * S, -nn ** 2 * A0 * S, nn * A1v * C, nn * A0 * C
        cp, sp_ = mp.cos(ph), mp.sin(ph)
        hxx += cp ** 2 * prr + sp_ ** 2 * (pr / rv + ptt / rv ** 2) - 2 * sp_ * cp * (prt / rv - pt / rv ** 2)
        hxy += sp_ * cp * (prr - pr / rv - ptt / rv ** 2) + (cp ** 2 - sp_ ** 2) * (prt / rv - pt / rv ** 2)
    return hxy, -hxx


def Vq(ph):
    # Hessian pair of r^p sum b_n sin(n theta)/(p^2 - n^2) at r = 1
    pm = qm + 2
    hxy = mp.mpf(0)
    hxx = mp.mpf(0)
    for nn, bv in bcoef.items():
        cf = bv / (pm ** 2 - nn ** 2)
        S, C = mp.sin(nn * ph), mp.cos(nn * ph)
        A0, A1v, A2v = cf, cf * pm, cf * pm * (pm - 1)
        prr, pr, ptt, prt, pt = A2v * S, A1v * S, -nn ** 2 * A0 * S, nn * A1v * C, nn * A0 * C
        cp, sp_ = mp.cos(ph), mp.sin(ph)
        hxx += cp ** 2 * prr + sp_ ** 2 * (pr + ptt) - 2 * sp_ * cp * (prt - pt)
        hxy += sp_ * cp * (prr - pr - ptt) + (cp ** 2 - sp_ ** 2) * (prt - pt)
    return hxy, -hxx


Bb = sum(abs(bv) * (nn + 1) / (2 * (nn + qm + 2)) for nn, bv in bcoef.items() if nn >= 3)
okC = True
for rv in (mp.mpf(4), mp.mpf(8), mp.mpf(40), mp.mpf(400)):
    worst = mp.mpf(0)
    modes = {nn: mode(nn, rv) for nn in bcoef}
    m_ = mp.pi * modes[1][3] + mp.pi * mp.quad(lambda sv: sv ** 2 * sv ** qm * bcoef[1], [rv, 10 * rv, mp.inf])
    for j in range(24):
        ph = (j + mp.mpf(1) / 3) * mp.pi / 12
        U1, U2 = hess_vel(rv, ph, modes)
        # DK(X)(0, m) = -(cos 3 theta, sin 3 theta) m/(pi r^3) (T4-335 section 2: -partial_y K = (cos3, sin3)/(pi r^3))
        dk1, dk2 = -m_ * mp.cos(3 * ph) / (mp.pi * rv ** 3), -m_ * mp.sin(3 * ph) / (mp.pi * rv ** 3)
        V1, V2 = Vq(ph)
        e1 = U1 + dk1 - rv ** qm * V1
        e2 = U2 + dk2 - rv ** qm * V2
        worst = max(worst, mp.sqrt(e1 ** 2 + e2 ** 2) / rv ** qm)
    bound = Bb * (L0m / rv) ** (qm + 5)
    print('     r = %s: max over 24 angles of r^-q|U + DK M - r^q V_q[b]| = %s, B_b (L0/r)^(q+5) = %s' % (
        mp.nstr(rv, 4), mp.nstr(worst, 8), mp.nstr(bound, 8)))
    okC = okC and worst <= bound * (1 + mp.mpf('1e-12'))
check('C1 FLOAT: the cutoff model error is below the bound (5) at r = 4, 8, 40, 400 (24 angles)', okC)

# C2: with eps free in (0, q + 5) (a tail expansion beyond T4-335 (7)), the A_in part of (8) alone at L0 = 4 and
#     R = 13761.58 or 18860: min over eps of (5/R)^eps (C_(q-eps) + L_(q-eps)) (FLOAT grid of 2000 points)
bests = []
for Rf in (mp.mpf('13761.58'), mp.mpf(18860)):
    best = None
    for j in range(1, 2000):
        e_ = (qm + 5) * j / 2000
        aa = qm - e_
        Cv = mp.mpf(1) / 2 + 2 ** (3 - aa) + 2 ** (aa + 2) / (-aa) + 2 ** (-aa - 2) / (-aa - 3) + 2 ** (2 - aa) / (aa + 5)
        v_ = (5 / Rf) ** e_ * (Cv + 2 ** (1 - aa))
        if best is None or v_ < best[1]:
            best = (e_, v_)
    bests.append(best)
    print('     FLOAT: with eps free, min of the A_in part of (8)/H at R = %s is %s at eps = %s' % (
        mp.nstr(Rf, 8), mp.nstr(best[1], 6), mp.nstr(best[0], 6)))
check('C2 FLOAT diagnostic computed', len(bests) == 2)

npass = sum(1 for _, o in res if o)
print('%d checks, %s' % (len(res), 'ALL PASS' if npass == len(res) else '%d FAIL' % (len(res) - npass)))
