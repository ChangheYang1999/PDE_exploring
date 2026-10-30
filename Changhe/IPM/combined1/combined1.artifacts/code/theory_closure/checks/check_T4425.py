# c1-t1 check for R1-045 (REVIEWS_v43): review of c1-t4 T4-425 (research/radial_averaged_remainder_obstruction,
# PROOF 4d13c623...), written from the PROOF text only. No other lane's code is run or imported.
# Part A: exact sympy identities. Part B: python-flint arb at 200 bits, with the T4-380 inputs of
# data/T4380_inputs.json (as in check_T4410 and check_R1044). No FLOAT step.
# Run from artifacts/checks: OMP_NUM_THREADS=1 python3 -B check_T4425.py > check_T4425.out
import json
import math
from fractions import Fraction as Fr
import sympy as sp
import flint

flint.ctx.prec = 200
arb = flint.arb
RES = []


def check(name, ok):
    RES.append((name, bool(ok)))
    print('%s %s' % ('PASS' if ok else 'FAIL', name))


def A_(fr):
    return arb(fr.numerator) / fr.denominator


def arbint(sv):
    body = sv.strip()[1:-1]
    mid, rad = body.split('+/-')
    return Fr(mid.strip()) - Fr(rad.strip()), Fr(mid.strip()) + Fr(rad.strip())


def lo(x, n=10):
    # printed lower bound: the ball's lower endpoint, decreased by one unit in the last printed place
    v = x - x.rad()
    e = arb(10) ** (math.floor(math.log10(abs(float(v.mid())))) - n + 1)
    return (v - e).str(n, radius=False)


def hi(x, n=10):
    v = x + x.rad()
    e = arb(10) ** (math.floor(math.log10(abs(float(v.mid())))) - n + 1)
    return (v + e).str(n, radius=False)


# ---------------- Part A: exact identities ----------------
c, r, s, rho, H, G, m = sp.symbols('c r s rho H G m', positive=True)
gam = 1 / c
q = gam - 4
dl = 1 - gam
kap = 1 - q
D = c * kap
check('A1 kappa = 1 - q = 5 - gamma = 4 + delta and D = c kappa = 5c - 1 (symbolic c)',
      sp.simplify(kap - (5 - gam)) == 0 and sp.simplify(kap - (4 + dl)) == 0 and sp.simplify(D - (5 * c - 1)) == 0)

cF = Fr(4076476460239181, 2251799813685248)
qF = 1 / cF - 4
EminF = (-qF - 1) / (2 * (-qF) * (-qF - 3))
EtestF = Fr(40673572058993602044748051350395, 51288398112310268946308133030216)   # check_T4381 A14
check('A2 Emin = (-q-1)/(2(-q)(-q-3)) at the campaign c equals Etest of T4-381 exactly (check_T4381 A14)',
      EminF == EtestF)

check('A3 2^(3-q) + 2^(1-q) = 5 2^(1-q) (symbolic q)',
      sp.simplify(2 ** (3 - q) + 2 ** (1 - q) - 5 * 2 ** (1 - q)) == 0)

# A4: integration of c r dh/dr - h = f from r to infinity: h(r) = -(r^gamma/c) int_r^inf s^(-gamma-1) f(s) ds
f = sp.Function('f')
Fint = sp.Function('Fint')        # Fint(r) = int_r^inf s^(-gamma-1) f(s) ds, so Fint' = -r^(-gamma-1) f(r)
hh = -(r ** gam / c) * Fint(r)
expr = c * r * sp.diff(hh, r) - hh
expr = expr.subs(sp.Derivative(Fint(r), r), -r ** (-gam - 1) * f(r))
check('A4 h = -(r^gamma/c) int_r^inf s^(-gamma-1) f ds solves c r h_r - h = f (generic f)',
      sp.simplify(expr - f(r)) == 0)

# A5: the two forms of (4) agree: (HG/c) r^gamma s^(q-2) = (HG/D) r^(q-delta) kappa r^kappa s^(-kappa-1)
lhs = (H * G / c) * r ** gam * s ** (q - 2)
rhs = (H * G / D) * r ** (q - dl) * kap * r ** kap * s ** (-kap - 1)
check('A5 the two forms of the averaging formula (4) agree (forcing power s^(q+gamma-1) times s^(-gamma-1))',
      sp.simplify(sp.powsimp(lhs / rhs, force=True)) == 1
      and sp.simplify((q + gam - 1) + (-gam - 1) - (q - 2)) == 0)

# A6: constant E is reproduced, and the T4-335 (7) denominator: kappa r^kappa int_r^inf s^(-kappa-1) ds = 1
k_, d_, Em, la, ru = sp.symbols('kappa delta Emin lambda r_u', positive=True)
Tc = k_ * r ** k_ * sp.integrate(s ** (-k_ - 1), (s, r, sp.oo))
check('A6 the averaging operator maps a constant to itself, and int_r^inf s^(q-2) ds = r^(q-1)/kappa',
      sp.simplify(Tc) == 1 and sp.simplify(sp.integrate(s ** (-k_ - 1), (s, r, sp.oo)) - r ** (-k_) / k_) == 0)

# A7: formula (5). e_min(s) = Emin for s <= r_u and lambda (5/s)^delta for s >= r_u, with lambda (5/r_u)^delta = Emin.
lam_expr = Em * (ru / 5) ** d_         # lambda expressed through r_u
T_lo = k_ * r ** k_ * (Em * sp.integrate(s ** (-k_ - 1), (s, r, ru))
                       + lam_expr * 5 ** d_ * sp.integrate(s ** (-d_ - k_ - 1), (s, ru, sp.oo)))
T_hi = k_ * r ** k_ * lam_expr * 5 ** d_ * sp.integrate(s ** (-d_ - k_ - 1), (s, r, sp.oo))
f5lo = Em * (1 - d_ / (k_ + d_) * (r / ru) ** k_)
f5hi = lam_expr * (5 / r) ** d_ * k_ / (k_ + d_)
okA7 = (sp.simplify(sp.powsimp(sp.expand(T_lo - f5lo), force=True)) == 0
        and sp.simplify(sp.powsimp(sp.expand(T_hi - f5hi), force=True)) == 0
        and sp.simplify(f5lo.subs(r, ru) - f5hi.subs(r, ru)) == 0
        and sp.simplify(sp.diff(f5lo, r) + Em * d_ * k_ / (k_ + d_) * r ** (k_ - 1) / ru ** k_) == 0)
check('A7 formula (5): both branches of T[e_min] by direct integration, equal at r_u, decreasing (d/dr < 0)', okA7)

# A8: case analysis behind (2), for the record: for 0 < eps <= delta, x = (1+L0)/s and s >= 5,
#     x >= 1 gives x^eps >= 1 >= (5/s)^delta; x < 1 gives x >= 5/s (as 1 + L0 >= 5) and x^eps >= x^delta >= (5/s)^delta.
x, e_ = sp.symbols('x epsilon', positive=True)
okA8 = sp.simplify(sp.diff(x ** e_, e_) - x ** e_ * sp.log(x)) == 0     # x^eps is nonincreasing in eps for x < 1
check('A8 (2): d/d eps of x^eps = x^eps log x, which is <= 0 for x < 1 (the case analysis is in R1-045)', okA8)

# ---------------- Part B: arb ----------------
inp = json.load(open('data/T4380_inputs.json'))
qA, dA, DA = A_(Fr(inp['q'])), A_(Fr(inp['delta'])), A_(Fr(inp['D']))
check('B0 inputs: q = 1/c - 4, delta = 1 - 1/c, D = 5c - 1 (exact, data/T4380_inputs.json)',
      Fr(inp['q']) == qF and Fr(inp['delta']) == 1 - 1 / cF and Fr(inp['D']) == 5 * cF - 1)
two = arb(2)
kapA = 1 - qA
lam = arb(1) / 2 + 5 * two ** (1 - qA)
Emin = A_(EminF)
print('     Emin = %s; lambda = %s; kappa = %s; delta/(kappa+delta) = %s' % (
    Emin.str(25), lam.str(15), kapA.str(15), (dA / (kapA + dA)).str(15)))
check('B1 lambda > Emin > 0.79303', lam > Emin and Emin > arb('0.79303'))
ruA = 5 * (lam / Emin) ** (1 / dA)
print('     r_u = 5 (lambda/Emin)^(1/delta) = %s' % ruA.str(16))
check('B2 r_u > 18860 and r_u agrees with the stated 302748.4007664045 to 1e-9',
      ruA > 18860 and abs(ruA - arb('302748.4007664045')) < arb('1e-9'))


def Tlo(Eu_, ru_, r_):
    return Eu_ * (1 - dA / (kapA + dA) * (r_ / ru_) ** kapA)


T18860 = Tlo(Emin, ruA, arb(18860))
print('     T[e_min](18860) = %s' % T18860.str(25))
check('B3 T[e_min](18860) > 0.79303 and agrees with the stated 0.7930361911778637328405552269 to 1e-25',
      T18860 > arb('0.79303') and abs(T18860 - arb('0.7930361911778637328405552269')) < arb('1e-25'))

BETAS = (('sharpw', Fr(28496, 10 ** 10)), ('TB', Fr(3793, 10 ** 9)), ('graded', Fr(25, 54684)),
         ('fixed', Fr(1351, 1024000000)))
s2pi = (2 * arb.pi()).sqrt()
ok4 = ok7 = True
kmax = rbmax = rbmin = None
lamAout = None
for row in inp['rows']:
    Blo, Bhi = (A_(v) for v in arbint(row['B']))
    Plo = A_(arbint(row['H_point'])[0])
    g0 = A_(Fr(row['G_lower_exact']))
    for bn_, bv in BETAS:
        rbh = (Bhi / (A_(bv) * (-2 * qA - 2).sqrt())) ** (1 / (-qA - 1))
        rbl = (Blo / (A_(bv) * (-2 * qA - 2).sqrt())) ** (1 / (-qA - 1))
        KP = DA * Bhi * rbh ** dA / (s2pi * g0 * Plo)          # >= Kcrit/Phi
        ok4 = ok4 and rbl > 5 and rbh < 18860 and KP < arb('0.785064') and T18860 > KP
        kmax = KP if kmax is None or KP > kmax else kmax
        rbmax = rbh if rbmax is None or rbh > rbmax else rbmax
        rbmin = rbl if rbmin is None or rbl < rbmin else rbmin
        # B7 (extension, R1-044): with A_out only, J(s)/H >= lam E g0 s^-delta / D (E = list constant >= Emin);
        #     envelope min(Emin, c_out s^-delta), c_out = lam Emin g0 / D; average at r <= r_beta.
        cout = lam * Emin * g0 / DA
        ruo = (cout / Emin) ** (1 / dA)
        Tout = Tlo(Emin, ruo, rbh)
        ok7 = ok7 and ruo > rbh and Tout > KP
        lamAout = Tout if lamAout is None or Tout < lamAout else lamAout
print('     over 12 pairs: r_beta in [%s, %s]; Kcrit/Phi <= %s' % (lo(rbmin, 7), hi(rbmax, 7), hi(kmax, 8)))
check('B4 for all 12 (reference, target) pairs: 5 < r_beta < 18860, Kcrit/Phi < 0.785064 < T[e_min](18860)', ok4)
check('B5 hence on R <= r <= r_beta the CI integrand vanishes: Eeff(r) >= T[e_min](r) >= T[e_min](18860) > Kcrit/Phi',
      ok4 and T18860 > kmax)

U1 = arb('1.747261')
ru1 = 5 * (lam / U1) ** (1 / dA)
T1 = Tlo(U1, ru1, arb(18860))
T1c = U1 * (1 - (arb(18860) / ru1) ** kapA)
print('     universal 1.747261: r_u = %s, exact-envelope average at 18860 = %s, coarse R1-043 bound = %s' % (
    ru1.str(12), T1.str(12), T1c.str(12)))
check('B6 the 1.747261 case: averages 1.745480614 (exact envelope) and 1.727790118 (R1-043 coarse) to 1e-9',
      abs(T1 - arb('1.745480614')) < arb('1e-9') and abs(T1c - arb('1.727790118')) < arb('1e-9'))
print('     A_out-only extension (R1-044): min over 12 pairs of the averaged floor at r_beta = %s' % lo(lamAout, 8))
check('B7 extension: with A_out only (R1-044 (R44.1)), the envelope min(Emin, lam Emin g0 s^-delta/D) averages above '
      'Kcrit/Phi at every r <= r_beta, for all 12 pairs', ok7)
print('ALL PASS' if all(o for _, o in RES) else 'SOME FAIL', '(%d checks)' % len(RES))
