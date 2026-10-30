# c1-t1 independent check of T4-381 (c1-t4 research/universal_velocity_lower, PROOF sha256 ca0e008a...), for R1-040.
# Written from the PROOF text and from T4-335 section 1 only; the c1-t4 check code was not run or copied.
# Part A: exact symbolic identities (sympy) in a = -q > 3 or at the exact campaign q. Part B: interval arithmetic
# (mpmath iv, 60 digits) for Etest, the T4-380 thresholds and the two caps, from data/T4380_inputs.json (fields copied
# from the T4-380 result; source sha256 inside). Part C: FLOAT diagnostics (mpmath quadrature at 40 digits) of the
# exact velocity remainder of the test function along theta = pi/4; they are not part of the proof.
# Run from artifacts/checks: OMP_NUM_THREADS=1 python3 -B check_T4381.py > check_T4381.out
import json
from fractions import Fraction as Fr
import sympy as sp
import mpmath as mp
from mpmath import iv

res = []


def check(name, ok):
    res.append((name, bool(ok)))
    print('%-4s %s' % ('PASS' if ok else 'FAIL', name))


c = Fr(4076476460239181, 2251799813685248)
qF = 1 / c - 4
dF = 1 - 1 / c
DF = 1 - c * (qF - dF)

# ---------------- Part A: symbolic identities
x, y = sp.symbols('x y', real=True)
r, s, a, th = sp.symbols('r s a theta', positive=True)
q = -a
R = sp.sqrt(x ** 2 + y ** 2)
h = y * (1 + R) ** (q - 1) / a
# A1: weighted gradient norm^2 equals (1/a^2)[((1+qr)/(1+r))^2 sin^2 + cos^2]
pol = {x: r * sp.cos(th), y: r * sp.sin(th)}
# exact: h = y w(R) with w = (1+R)^(q-1)/a, so grad h = (0, w) + y w'(R) X/R; evaluate on X = r(cos, sin), R = r
w = (1 + r) ** (q - 1) / a
w1 = sp.diff(w, r)
gx = r * sp.sin(th) * w1 * sp.cos(th)
gy = w + r * sp.sin(th) * w1 * sp.sin(th)
wg2 = (gx ** 2 + gy ** 2) * (1 + r) ** (2 - 2 * q)
claim = (((1 + q * r) / (1 + r)) ** 2 * sp.sin(th) ** 2 + sp.cos(th) ** 2) / a ** 2
ok = sp.simplify(sp.powsimp(sp.expand(sp.powsimp((wg2 - claim) * a ** 2 * (1 + r) ** 2, force=True)), force=True)) == 0
# cross-check the chain rule against sympy's Cartesian derivatives at three points (50 digits)
gxc, gyc = sp.diff(h, x), sp.diff(h, y)
for av, xv, yv in ((sp.Rational(7, 2), sp.Rational(3, 10), sp.Rational(5, 7)), (sp.Rational(10, 3), sp.Integer(4), sp.Rational(-1, 3))):
    rv = sp.sqrt(xv ** 2 + yv ** 2)
    tv = sp.atan2(yv, xv)
    e1 = (gxc.subs({a: av, x: xv, y: yv}) - gx.subs({a: av, r: rv, th: tv}))
    e2 = (gyc.subs({a: av, x: xv, y: yv}) - gy.subs({a: av, r: rv, th: tv}))
    ok = ok and abs(sp.N(e1, 50)) < 1e-40 and abs(sp.N(e2, 50)) < 1e-40
check('A1 weighted gradient norm^2 of h = y(1+r)^(q-1)/a', ok)
# A2: a^2 (1+r)^2 - (1 - a r)^2 = (a+1)(a-1+2ar) >= 0, so |(1+qr)/(1+r)| <= a and the weighted gradient is <= 1
check('A2 (a(1+r))^2-(1-ar)^2 = (a+1)(a-1+2ar)', sp.expand(a ** 2 * (1 + r) ** 2 - (1 - a * r) ** 2 - (a + 1) * (a - 1 + 2 * a * r)) == 0)
# A3: weighted amplitude r/(1+r)|sin|/a <= 1/a < 1; weighted gradient at theta = pi/2 tends to |q|/a = 1, so H_q = 1
lim = sp.limit(sp.sqrt(claim.subs(th, sp.pi / 2)), r, sp.oo)
amp = sp.simplify(((1 + R) ** (-q) * h).subs(pol) - r / (1 + r) * sp.sin(th) / a)
check('A3 amplitude part r/(1+r) sin/a and gradient limit 1 at theta = pi/2', amp == 0 and sp.simplify(lim - 1) == 0)
# A4: m = pi int_0^oo r^2 f, f = r(1+r)^(q-1)/a, equals 6 pi/(a^2(a-1)(a-2)(a-3)); Beta(4, a-3)/a
mB = sp.pi * sp.gamma(4) * sp.gamma(a - 3) / sp.gamma(a + 1) / a
check('A4 moment = pi B(4,a-3)/a = 6pi/(a^2(a-1)(a-2)(a-3))',
      sp.simplify(sp.gammasimp(mB - 6 * sp.pi / (a ** 2 * (a - 1) * (a - 2) * (a - 3)))) == 0)
aval = -qF
mp.mp.dps = 40
aM = mp.mpf(aval.numerator) / aval.denominator
# t = u/(1-u): pi int_0^1 u^3 (1-u)^(a-4) du / a; on [1/2, 1] put v = 1 - u so the endpoint power sits at v = 0
# (tanh-sinh at 40 digits gives only about 20 correct digits for the power v^(a-4); 60 digits give about 28)
mp.mp.dps = 60
aM = mp.mpf(aval.numerator) / aval.denominator
mq = mp.pi * (mp.quad(lambda u: u ** 3 * (1 - u) ** (aM - 4), [0, mp.mpf(1) / 2])
              + mp.quad(lambda v: (1 - v) ** 3 * v ** (aM - 4), [0, mp.mpf(1) / 2])) / aM
mc = 6 * mp.pi / (aM ** 2 * (aM - 1) * (aM - 2) * (aM - 3))
check('A5 FLOAT: moment at campaign q, quadrature %s, formula %s, T4-381 0.99992906777388050028655 (agree to 1e-22)' % (
    mp.nstr(mq, 24), mp.nstr(mc, 24)), abs(mq - mc) < mp.mpf('1e-22') and abs(mc - mp.mpf('0.99992906777388050028655')) < 1e-22)
mp.mp.dps = 40
aM = mp.mpf(aval.numerator) / aval.denominator
# A6: mode-1 Green formula phi = -(1/2)[r^-1 I + r J], I = int_0^r s^2 f, J = int_r^oo f, solves
#     phi'' + phi'/r - phi/r^2 = f (Leibniz rule with a generic f)
F = sp.Function('f')
I = sp.Integral(s ** 2 * F(s), (s, 0, r))
J = sp.Integral(F(s), (s, r, sp.oo))
phi = -(I / r + r * J) / 2
ode = sp.diff(phi, r, 2) + sp.diff(phi, r) / r - phi / r ** 2 - F(r)
check('A6 Green formula solves the mode-1 equation', sp.simplify(ode.doit()) == 0)
# A7: tails with f = r^q/a: phi = -(m/pi)/(2r) + r^(q+2)/(a(q+1)(q+3)) for the homogeneous part
m_ = sp.symbols('m', positive=True)
bb = sp.symbols('b', positive=True)  # a = 3 + b, b > 0, so both tails converge
Itail = sp.integrate(s ** (2 - (3 + bb)) / (3 + bb), (s, r, sp.oo))
Jtail = sp.integrate(s ** (-(3 + bb)) / (3 + bb), (s, r, sp.oo))
phi_h = -((m_ / sp.pi - Itail) / r + r * Jtail) / 2
qb = -(3 + bb)
check('A7 two tails give -m/(2 pi r) + r^(q+2)/(a(q+1)(q+3))',
      sp.simplify(sp.powsimp(phi_h - (-m_ / (2 * sp.pi * r) + r ** (qb + 2) / ((3 + bb) * (qb + 1) * (qb + 3))), force=True)) == 0)
# A8: Hessian velocity (psi_xy, -psi_xx) of psi = C y r^(q+1), C = 1/(a(q+1)(q+3)), equals (6)
psi2 = y * R ** (q + 1) / (a * (q + 1) * (q + 3))
W = sp.Matrix([sp.diff(psi2, x, y), -sp.diff(psi2, x, 2)])
W6 = sp.Matrix([sp.cos(th) * (1 + (q - 1) * sp.sin(th) ** 2), -sp.sin(th) * (1 + (q - 1) * sp.cos(th) ** 2)]) / (a * (q + 3))
Wp = (W.subs(pol) / r ** q).applyfunc(lambda e: sp.simplify(sp.powsimp(e, force=True)))
check('A8 Hessian velocity of C y r^(q+1) is r^q times (6)', all(sp.simplify(Wp[i] - W6[i]) == 0 for i in range(2)))
# A9: dipole: Hessian velocity of -m y/(2 pi r^2) equals -DK(X)(0, m), K = (-z1 z2, (z1^2 - z2^2)/2)/(pi |Z|^4)
K = sp.Matrix([-x * y, (x ** 2 - y ** 2) / 2]) / (sp.pi * R ** 4)
DKM = K.jacobian([x, y]) * sp.Matrix([0, m_])
psid = -m_ * y / (2 * sp.pi * R ** 2)
Ud = sp.Matrix([sp.diff(psid, x, y), -sp.diff(psid, x, 2)])
check('A9 Hessian velocity of the dipole potential is -DK(X)M', all(sp.simplify(Ud[i] + DKM[i]) == 0 for i in range(2)))
# A10: K is the Hessian velocity of the Newtonian kernel log|Z|/(2 pi) (so U = (psi_xy, -psi_xx) with Laplace psi = h)
G = sp.log(R) / (2 * sp.pi)
check('A10 K = (G_xy, -G_xx) for G = log|Z|/(2 pi)',
      sp.simplify(sp.diff(G, x, y) - K[0]) == 0 and sp.simplify(-sp.diff(G, x, 2) - K[1]) == 0)
# A11: |(6)|^2 = (1 + (q-1)(q+3) sin^2 cos^2)/(a(q+3))^2; at pi/4 the norm is (-q-1)/(2a(-q-3)); max at pi/4 for q < -3
n2 = sp.simplify(sp.expand_trig((W6[0] ** 2 + W6[1] ** 2) * (a * (q + 3)) ** 2))
okn = sp.simplify(n2 - (1 + (q - 1) * (q + 3) * sp.sin(th) ** 2 * sp.cos(th) ** 2)) == 0
Et = (-q - 1) / (2 * a * (-q - 3))
v4 = sp.simplify((n2.subs(th, sp.pi / 4)) / (a * (q + 3)) ** 2 - Et ** 2)
check('A11 |(6)|^2 identity and |(6)| = Etest at theta = pi/4', okn and v4 == 0)
# A12: cap_delta factor: int_1^oo (1 - s^-delta)^2 s^(2q+1) ds = 1/al - 2/(al+de) + 1/(al+2de) = 2de^2/(al(al+de)(al+2de))
al, de = sp.symbols('alpha delta', positive=True)
ex = 1 / al - 2 / (al + de) + 1 / (al + 2 * de)
check('A12 shape-integral identity', sp.simplify(ex - 2 * de ** 2 / (al * (al + de) * (al + 2 * de))) == 0)
qs = sp.Rational(qF.numerator, qF.denominator)
dS = sp.Rational(dF.numerator, dF.denominator)
In = sum(sp.integrate(t, (s, 1, sp.oo)) for t in sp.Add.make_args(sp.expand((1 - s ** (-dS)) ** 2 * s ** (2 * qs + 1))))
check('A13 shape integral at the campaign q, delta', sp.simplify(In - ex.subs({al: -2 * qs - 2, de: dS})) == 0)
# A14: Etest exact rational at campaign q equals the T4-381 value
EtF = (-qF - 1) / (2 * (-qF) * (-qF - 3))
check('A14 Etest exact = %s/%s matches T4-381' % (EtF.numerator, EtF.denominator),
      EtF == Fr(40673572058993602044748051350395, 51288398112310268946308133030216))
check('A15 D = 5c - 1 and alpha = -2q - 2 > 0, delta > 0', DF == 5 * c - 1 and -2 * qF - 2 > 0 and dF > 0)

# ---------------- Part B: interval arithmetic
iv.dps = 60


def dec(f, n, up):
    # decimal string of the Fraction f > 0 rounded down (up = False) or up (up = True) to n digits after the point
    k = f * 10 ** n
    qq = k.numerator // k.denominator
    if up and qq * k.denominator != k.numerator:
        qq += 1
    return '%d.%0*d' % (qq // 10 ** n, n, qq % 10 ** n)


def sci(f, n):
    # upper decimal bound of the Fraction f > 0 in the form m.mmm...e-k
    e = 0
    while f * 10 ** e < 1:
        e += 1
    return '%se-%d' % (dec(f * 10 ** e, n, True), e)


def ivF(f):
    return iv.mpf(f.numerator) / f.denominator


def arb(sv):
    # '[mid +/- rad]' -> exact Fraction interval [mid - rad, mid + rad]
    body = sv.strip()[1:-1]
    mid, rad = body.split('+/-')
    return Fr(mid.strip()) - Fr(rad.strip()), Fr(mid.strip()) + Fr(rad.strip())


def frac(x):
    m, e = x.man_exp
    return Fr(m) * Fr(2) ** e


def hi(v):
    return frac(mp.make_mpf(v._mpi_[1]))


def lo(v):
    return frac(mp.make_mpf(v._mpi_[0]))


inp = json.load(open('data/T4380_inputs.json'))
assert Fr(inp['q']) == qF and Fr(inp['delta']) == dF and Fr(inp['D']) == DF
q_ = ivF(qF)
de_ = ivF(dF)
D_ = ivF(DF)
al_ = -2 * q_ - 2
Et_ = ivF(EtF)
check('B1 Etest in [%s, %s]' % (dec(lo(Et_), 21, False), dec(hi(Et_), 21, True)),
      lo(Et_) > Fr('0.79303650642251408835') and hi(Et_) < Fr('0.79303650642251408836'))
betas = {'sharpw_rounded_ceiling': Fr(28496, 10 ** 10), 'TB_sharp_rounded_ceiling': Fr(3793, 10 ** 9),
         'original_graded_ceiling': Fr(25, 54684), 'fixed_sharpw_ball': Fr(1351, 1024000000)}
s2pi = iv.sqrt(2 * iv.pi)
worst = {}
mine = {}
for row in inp['rows']:
    Blo, Bhi = arb(row['B'])
    Hlo, Hhi = arb(row['H_point'])
    g0 = Fr(row['G_lower_exact'])
    v0 = Fr(row['V_lower_exact'])
    H_ = ivF(Hlo)
    for vname, vv in (('V=0', Fr(0)), ('v0', v0)):
        # T4-380 (3): reaching beta needs E <= [D B/(sqrt(2 pi) H0) (B/(beta sqrt(alpha)))^(delta/(-q-1)) - v0]/g0;
        # upper bound uses B upper end and H0 lower end (the bound increases in B, decreases in H0)
        for bn, bv in betas.items():
            Bu = ivF(Bhi)
            Ec = (D_ * Bu / (s2pi * H_) * (Bu / (ivF(bv) * iv.sqrt(al_))) ** (de_ / (-q_ - 1)) - ivF(vv)) / ivF(g0)
            worst[(vname, bn)] = max(worst.get((vname, bn), Fr(0)), hi(Ec))
            mine[(row['candidate'], vname, bn)] = hi(Ec)
        # caps with E = Etest (any admissible universal E >= Etest gives a smaller cap)
        Bu = ivF(Bhi)
        r0 = (s2pi * H_ * (ivF(vv) + Et_ * ivF(g0)) / (D_ * Bu)) ** (1 / de_)
        crude = Bu * r0 ** (q_ + 1) / iv.sqrt(al_)
        shape = crude * iv.sqrt(2 * de_ ** 2 / ((al_ + de_) * (al_ + 2 * de_)))
        worst[(vname, 'crude')] = max(worst.get((vname, 'crude'), Fr(0)), hi(crude))
        worst[(vname, 'shape')] = max(worst.get((vname, 'shape'), Fr(0)), hi(shape))
        print('     %s %-3s r0 > %s, crude cap < %s, shape cap < %s' % (
            row['candidate'], vname, dec(lo(r0), 4, False), sci(hi(crude), 6), sci(hi(shape), 6)))
for vname in ('V=0', 'v0'):
    for bn in betas:
        print('     %-3s %-24s: largest T4-380 E threshold over 007, 013, 014 < %s' % (vname, bn, dec(worst[(vname, bn)], 8, True)))
check('B2 V=0: Etest exceeds the T4-380 threshold for the fixed sharpw ball (all three) and it is < 0.785064',
      lo(Et_) > worst[('V=0', 'fixed_sharpw_ball')] and worst[('V=0', 'fixed_sharpw_ball')] < Fr('0.785064'))
check('B3 V=0: Etest exceeds every family-ceiling threshold (< 0.682, 0.648, 0.27)',
      worst[('V=0', 'sharpw_rounded_ceiling')] < Fr('0.682') and worst[('V=0', 'TB_sharp_rounded_ceiling')] < Fr('0.648')
      and worst[('V=0', 'original_graded_ceiling')] < Fr('0.27') and lo(Et_) > Fr('0.682'))
check('B4 V=0: crude cap < 1.2485e-6 < 1351/1024000000 = 1.3193359375e-6',
      worst[('V=0', 'crude')] < Fr('1.2485e-6') < Fr(1351, 1024000000))
check('B5 V=0: shape cap < 1.421e-7', worst[('V=0', 'shape')] < Fr('1.421e-7'))
check('B6 with v0: crude cap < 9.88e-7 and shape cap < 1.124e-7',
      worst[('v0', 'crude')] < Fr('9.88e-7') and worst[('v0', 'shape')] < Fr('1.124e-7'))
for row in inp['rows']:
    e = arb(row['Ecrit_without_velocity_asymptotic']['fixed_sharpw_ball'])
    print('     %s T4-380 stored threshold (fixed sharpw, V=0) < %s' % (row['candidate'], dec(e[1], 12, True)))
okB7 = True
for rw in inp['rows']:
    for vname, key in (('V=0', 'Ecrit_without_velocity_asymptotic'), ('v0', 'Ecrit_with_velocity_asymptotic')):
        for bn in betas:
            okB7 = okB7 and abs(arb(rw[key][bn])[1] - mine[(rw['candidate'], vname, bn)]) < Fr('1e-40')
check('B7 my 24 thresholds agree with the stored T4-380 values to 1e-40', okB7)

# B8: consistency with R1-038 (c) (ii): with V = 0 the T4-380 threshold is Emax(b) B/(sqrt(2 pi) H0), Emax(b) with
#     B in place of 85020; so it is below the R1-038 upper bounds of Emax(b) times B_hi/(sqrt(2 pi) H0_lo)
emax = {'TB_sharp_rounded_ceiling': Fr('19.076327'), 'sharpw_rounded_ceiling': Fr('20.100578'),
        'original_graded_ceiling': Fr('7.9416068')}
okB8 = True
for rw in inp['rows']:
    Bhi_ = arb(rw['B'])[1]
    H0lo = arb(rw['H_point'])[0]
    fac = ivF(Bhi_) / (s2pi * ivF(H0lo))
    for bn, em in emax.items():
        okB8 = okB8 and mine[(rw['candidate'], 'V=0', bn)] < hi(ivF(em) * fac)
    print('     %s sqrt(2 pi) H0/B > %s' % (rw['candidate'], dec(lo(1 / fac), 6, False)))
check('B8 T4-380 thresholds (V = 0) are below the R1-038 Emax(b) bounds divided by sqrt(2 pi) H0/B', okB8)

# B9: dependence on T4-375. With only the T4-351 bound H0 = B/sqrt(2 pi), r0 = (Etest g0/D)^(1/delta) and the crude cap
#     is B r0^(q+1)/sqrt(alpha); a lower value of it (B lower end) shows that this cap alone then decides nothing
okB9 = True
for rw in inp['rows']:
    Blo_ = arb(rw['B'])[0]
    r0 = (Et_ * ivF(Fr(rw['G_lower_exact'])) / D_) ** (1 / de_)
    cap351 = ivF(Blo_) * r0 ** (q_ + 1) / iv.sqrt(al_)
    print('     %s with the T4-351 H0 only: r0 < %s, crude cap > %s' % (rw['candidate'], dec(hi(r0), 4, True), dec(lo(cap351), 2, False)))
    okB9 = okB9 and lo(cap351) > Fr(100)
check('B9 with the T4-351 lower bound alone the crude cap exceeds 100 (the obstruction needs the T4-375 H0)', okB9)

# ---------------- Part C: FLOAT diagnostics of the exact remainder along theta = pi/4
mp.mp.dps = 40
fq = lambda t: t * (1 + t) ** (-aM - 1) / aM
mtot = mp.quad(lambda t: t ** 2 * fq(t), [0, 1, 10, 100, 1000, mp.inf])


def remainder(rr):
    Ir = mtot - mp.quad(lambda t: t ** 2 * fq(t), [rr, 10 * rr, mp.inf])
    Jr = mp.quad(fq, [rr, 10 * rr, mp.inf])
    ph = -(Ir / rr + rr * Jr) / 2
    ph1 = -(Jr - Ir / rr ** 2) / 2
    ph2 = fq(rr) - Ir / rr ** 3
    # subtract the dipole: phi_dip = -mtot/(2 r) (m = pi mtot, phi = m/(2 pi r) form)
    ph -= -mtot / (2 * rr)
    ph1 -= mtot / (2 * rr ** 2)
    ph2 -= -mtot / rr ** 3
    g = ph / rr
    g1 = ph1 / rr - ph / rr ** 2
    g2 = ph2 / rr - 2 * ph1 / rr ** 2 + 2 * ph / rr ** 3
    X, Y = rr / mp.sqrt(2), rr / mp.sqrt(2)
    psixy = X * (g2 * Y ** 2 / rr ** 2 + g1 / rr - g1 * Y ** 2 / rr ** 3)
    psixx = Y * (g2 * X ** 2 / rr ** 2 + g1 / rr - g1 * X ** 2 / rr ** 3)
    return mp.sqrt(psixy ** 2 + psixx ** 2) / rr ** (-aM)


Etm = (aM - 1) / (2 * aM * (aM - 3))
prev = None
okC = True
for rr in (mp.mpf(10) ** 3, mp.mpf(10) ** 4, mp.mpf(10) ** 5, mp.mpf(10) ** 6):
    v = remainder(rr)
    print('     r = %s: |U + DK M| / (H_q r^q) = %s (Etest %s, difference %s)' % (
        mp.nstr(rr, 3), mp.nstr(v, 15), mp.nstr(Etm, 15), mp.nstr(v - Etm, 5)))
    if prev is not None:
        okC = okC and abs(v - Etm) < abs(prev - Etm)
    prev = v
check('C1 FLOAT: the remainder ratio tends to Etest with error decreasing in r (diagnostic)', okC and abs(prev - Etm) < 1e-4)

npass = sum(1 for _, o in res if o)
print('%d checks, %s' % (len(res), 'ALL PASS' if npass == len(res) else '%d FAIL' % (len(res) - npass)))
