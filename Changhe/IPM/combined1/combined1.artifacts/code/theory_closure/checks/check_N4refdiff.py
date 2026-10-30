# c1-t1 independent check of the c1-n4 lemma research/reference_difference/PROOF.md (sha256 6f2d3685...), for R1-041.
# Written from the PROOF text only; the c1-n4 code was not run or copied. Part A: exact identities (sympy) and exact
# exponent inequalities at the campaign delta. Part B: FLOAT checks (mpmath, 30 digits) of the Euler primitive J_k and
# its recursion, and of a synthetic pair satisfying (P): decay rates, finite L2 norm, and V = U[g] through the mode-1
# Green formula. Part B is a diagnostic; it is not part of any proof.
# Run from artifacts/checks: OMP_NUM_THREADS=1 python3 -B check_N4refdiff.py > check_N4refdiff.out
from fractions import Fraction as Fr
import sympy as sp
import mpmath as mp

res = []


def check(name, ok):
    res.append((name, bool(ok)))
    print('%-4s %s' % ('PASS' if ok else 'FAIL', name))


c = Fr(4076476460239181, 2251799813685248)
dF = 1 - 1 / c
# ---------------- Part A
check('A1 exact delta = %s/%s: 2/5 < delta < 1/2, so 4-5delta > 2-delta and 1-5delta < -1' % (dF.numerator, dF.denominator),
      Fr(2, 5) < dF < Fr(1, 2) and 4 - 5 * dF > 2 - dF and 1 - 5 * dF < -1)
# A2: omitted density exponents 1 - l delta - 2k (l >= 5 or k >= 1, l >= 1) are < -1; the four kept ones are > -1
okA2 = all(1 - l * dF - 2 * k < -1 for l in range(1, 40) for k in range(0, 6) if l >= 5 or k >= 1)
okA2 = okA2 and all(1 - l * dF > -1 for l in range(1, 5))
check('A2 density exponents: 1-l delta > -1 for l <= 4; 1-l delta-2k < -1 when l >= 5 or k >= 1 (l < 40, k < 6)', okA2)
x, y = sp.symbols('x y', real=True)
chi = sp.Function('chi')(x, y)
lap = lambda f: sp.diff(f, x, 2) + sp.diff(f, y, 2)
g = -sp.diff(lap(chi), y)
V = (-sp.diff(chi, x, y, y), sp.diff(chi, x, x, y))
psi = -sp.diff(chi, y)
okA3 = sp.simplify(lap(psi) - g) == 0 and sp.simplify(V[0] - sp.diff(psi, x, y)) == 0 and sp.simplify(V[1] + sp.diff(psi, x, 2)) == 0
okA3 = okA3 and sp.simplify(lap(V[0]) - sp.diff(g, x, y)) == 0 and sp.simplify(lap(V[1]) + sp.diff(g, x, 2)) == 0
okA3 = okA3 and sp.simplify(sp.diff(V[0], x) + sp.diff(V[1], y)) == 0
check('A3 u = (-chi_xyy, chi_xxy) = (psi_xy, -psi_xx) with Lap psi = rho; Lap V1 = g_xy, Lap V2 = -g_xx, div V = 0', okA3)
# A4: Fourier symbols. With Lap psi = g, psi^ = -g^/|xi|^2, so (psi_xy, -psi_xx)^ = (xi1 xi2, -xi1^2) g^/|xi|^2, which is
#     (-R1 R2, R1^2) for R_j with symbol i xi_j/|xi|; the vector symbol has norm |xi1|/|xi| <= 1
k1, k2 = sp.symbols('xi1 xi2', real=True)
n2 = k1 ** 2 + k2 ** 2
s_psi = -1 / n2
sym = ((sp.I * k1) * (sp.I * k2) * s_psi, -(sp.I * k1) ** 2 * s_psi)
Rj = (sp.I * k1 / sp.sqrt(n2), sp.I * k2 / sp.sqrt(n2))
okA4 = sp.simplify(sym[0] - (-Rj[0] * Rj[1])) == 0 and sp.simplify(sym[1] - Rj[0] ** 2) == 0
okA4 = okA4 and sp.simplify(sym[0] ** 2 + sym[1] ** 2 - k1 ** 2 / n2) == 0
check('A4 symbols (xi1 xi2, -xi1^2)/|xi|^2 = (-R1R2, R1^2); squared vector symbol xi1^2/|xi|^2 <= 1', okA4)
# A5: div form of the equation: (cX + W).grad rho - rho = div((cX + W) rho) - (2c+1) rho when div W = 0
cs = sp.symbols('c', positive=True)
rho = sp.Function('rho')(x, y)
phi = sp.Function('phi')(x, y)
W = (sp.diff(phi, y), -sp.diff(phi, x))  # a generic divergence-free field
lhs = (cs * x + W[0]) * sp.diff(rho, x) + (cs * y + W[1]) * sp.diff(rho, y) - rho
rhs = sp.diff((cs * x + W[0]) * rho, x) + sp.diff((cs * y + W[1]) * rho, y) - (2 * cs + 1) * rho
check('A5 (cX+W).grad rho - rho = div((cX+W) rho) - (2c+1) rho for div W = 0', sp.simplify(lhs - rhs) == 0)
# A6: generator leading coefficients. With z = r^-2: t = 1/(1+z), tau_R = 1/(1+R^2 z), 1 - tau_R = R^2 z/(1+R^2 z),
#     (1+r^2)^(2-l delta/2) = r^(4-l delta)(1+z)^(2-l delta/2); the z^0 coefficient is P_n(1) = 1 when q = 0, else 0
z = sp.symbols('z', positive=True)
de = sp.Rational(dF.numerator, dF.denominator)
okA6 = True
for (l, m, w, n, q, R) in ((1, 0, 0, 0, 0, 1), (3, 2, 1, 2, 0, 25), (4, 1, 2, 3, 0, 100), (2, 1, 1, 1, 1, 10), (1, 3, 0, 4, 2, 50)):
    tR = 1 / (1 + R ** 2 * z)
    gen = (1 + z) ** (2 - l * de / 2) * (1 / (1 + z)) ** m * tR ** w * (1 - tR) ** q * sp.legendre(n, 2 * tR - 1)
    lead = sp.limit(gen, z, 0)
    okA6 = okA6 and lead == (1 if q == 0 else 0)
check('A6 leading coefficient of five sample generators is 1 for q = 0 and 0 for q > 0 (any m, w, n, R)', okA6)
# A7: tau_R = t/(1+(R^2-1)v), v = 1 - t = 1/(1+r^2); r dr = dt/(2 v^2); r^2 = t/v
r, Rs = sp.symbols('r R', positive=True)
t = r ** 2 / (1 + r ** 2)
v = 1 - t
okA7 = sp.simplify(r ** 2 / (Rs ** 2 + r ** 2) - t / (1 + (Rs ** 2 - 1) * v)) == 0
okA7 = okA7 and sp.simplify(sp.diff(t, r) / (2 * v ** 2) - r) == 0 and sp.simplify(r ** 2 - t / v) == 0
okA7 = okA7 and all(R ** 2 - 1 == a for R, a in ((10, 99), (25, 624), (50, 2499), (100, 9999)))
check('A7 tau_R = t/(1+(R^2-1)v); r dr = dt/(2v^2); r^2 = t/v; poles a = 99, 624, 2499, 9999', okA7)
# A8: recursion (k-1) J_k = (1+a)^(1-k) - (b-k+2) J_(k-1) from d/dv[v^(b+1)(1+av)^(1-k)]
vv, a, b = sp.symbols('v a b', positive=True)
kk = sp.symbols('k', positive=True)
dd = sp.diff(vv ** (b + 1) * (1 + a * vv) ** (1 - kk), vv)
# the claim is dd = (b-k+2) v^b (1+av)^(1-k) + (k-1) v^b (1+av)^(-k), integrated over [0, 1]
cl = (b - kk + 2) * vv ** b * (1 + a * vv) ** (1 - kk) + (kk - 1) * vv ** b * (1 + a * vv) ** (-kk)
check('A8 derivative identity behind the J_k recursion', sp.simplify(sp.powsimp(sp.expand((dd - cl) / vv ** b * (1 + a * vv) ** kk), force=True)) == 0)

# ---------------- Part B: FLOAT diagnostics
mp.mp.dps = 30


def Jq(k, bb, aa):
    # v = u^(1/(b+1)) removes the endpoint power: J_k = (1/(b+1)) int_0^1 (1 + a u^(1/(b+1)))^(-k) du
    p = 1 / (bb + 1)
    pts = [0] + [mp.mpf(10) ** (-e) for e in range(12, 0, -1)] + [1]
    return mp.quad(lambda u: (1 + aa * u ** p) ** (-k), pts) * p


def Jrec(bb, aa, kmax):
    aa = mp.mpf(aa)  # an int a would make (1+a)^(1-k) a double-precision float
    out = [mp.hyp2f1(1, bb + 1, bb + 2, -aa) / (bb + 1)]
    for k in range(2, kmax + 1):
        out.append(((1 + aa) ** (1 - k) - (bb - k + 2) * out[-1]) / (k - 1))
    return out


dM = mp.mpf(dF.numerator) / dF.denominator
worst = 0
loss = 0
for bb in (dM - 1, 3 * dM - 2, 5 * dM - 3, mp.mpf(2)):
    for aa in (99, 624, 2499, 9999):
        with mp.workdps(60):
            Jhi = Jrec(mp.mpf(bb), aa, 5)
        with mp.workdps(40):
            for k in range(1, 6):
                worst = max(worst, abs(Jhi[k - 1] - Jq(k, mp.mpf(bb), aa)) / abs(Jhi[k - 1]))
        with mp.workdps(30):
            Jlo = Jrec(mp.mpf(bb), aa, 5)
        loss = max(loss, max(abs(Jlo[i] - Jhi[i]) / abs(Jhi[i]) for i in range(5)))
check('B1 FLOAT: J_1 = 2F1(1,b+1;b+2;-a)/(b+1) and the recursion to k = 5 (60 digits) match quadrature (40 digits); '
      'max rel. diff %s' % mp.nstr(worst, 3), worst < mp.mpf('1e-25'))
print('     forward recursion run at 30 digits: max relative error %s (the recursion is used inside outward balls by c1-n4)' % mp.nstr(loss, 3))
mp.mp.dps = 30
# B2: synthetic pair with (P): chi = (1+r^2)^(2-delta/2) [l = 1, m = 0, q = 0, R = 1] and chi' = chi tau_10 [w = 1, R = 10].
#     Both have leading coefficient 1 in sector (1, 0). Radial chi_d = chi' - chi = -100 (1+r^2)^(2-delta/2)/(100+r^2).
#     g = -d_y Lap chi_d = f(r) sin(theta), f = -(Lap chi_d)'; psi = -d_y chi_d = P(r) sin(theta), P = -chi_d'.
rr = sp.symbols('r', positive=True)
chi1 = (1 + rr ** 2) ** (2 - de / 2)
chid = -100 * chi1 / (100 + rr ** 2)
radlap = lambda F: sp.diff(F, rr, 2) + sp.diff(F, rr) / rr
f_d = sp.lambdify(rr, -sp.diff(radlap(chid), rr), 'mpmath')
f_1 = sp.lambdify(rr, -sp.diff(radlap(chi1), rr), 'mpmath')
P_d = sp.lambdify(rr, -sp.diff(chid, rr), 'mpmath')
lim_d = -100 * dM * (2 - dM) ** 2
lim_1 = -(4 - dM) ** 2 * (2 - dM)
rows = []
for R_ in (mp.mpf(10) ** 3, mp.mpf(10) ** 5, mp.mpf(10) ** 7):
    rows.append((f_d(R_) * R_ ** (1 + dM) / lim_d, f_1(R_) * R_ ** (dM - 1) / lim_1))
print('     ratios f_d r^(1+delta)/(-100 delta (2-delta)^2) and f_1 r^(delta-1)/(-(4-delta)^2(2-delta)) at r = 1e3, 1e5, 1e7:')
for u1, u2 in rows:
    print('       %s  %s' % (mp.nstr(u1, 12), mp.nstr(u2, 12)))
check('B2 FLOAT: difference density decays like r^(-1-delta) (L2), single generator like r^(1-delta) (not L2)',
      abs(rows[-1][0] - 1) < 1e-6 and abs(rows[-1][1] - 1) < 1e-6 and 2 * (-1 - dM) + 1 < -1 < 2 * (1 - dM) + 1)
nrm2 = mp.pi * mp.quad(lambda s: f_d(s) ** 2 * s, [0, 1, 10, 100, 1000, mp.inf])
print('     ||g||_2^2 = pi int f_d^2 r dr = %s' % mp.nstr(nrm2, 20))
# B3: V = U[g]. The canonical L2 velocity is the Hessian velocity of the mode-1 Green potential
#     Pg = -(1/2)[r^-1 int_0^r s^2 f + r int_r^oo f] (decaying, regular). V comes from P; (P - Pg)/r must be constant
#     (the mode-1 harmonic A r sin(theta) = A y, whose Hessian velocity is zero; B sin(theta)/r is excluded by regularity).
Itot = mp.quad(lambda s: s ** 2 * f_d(s), [0, 1, 10, 100])


def Pg(R_):
    I_ = mp.quad(lambda s: s ** 2 * f_d(s), [0, min(R_, 1), R_]) if R_ > 0 else 0
    J_ = mp.quad(f_d, [R_, 10 * R_, 100 * R_, mp.inf])
    return -(I_ / R_ + R_ * J_) / 2


vals = [(P_d(R_) - Pg(R_)) / R_ for R_ in (mp.mpf('0.5'), mp.mpf(2), mp.mpf(20), mp.mpf(200))]
print('     (P - Pg)/r at r = 0.5, 2, 20, 200: %s' % ', '.join(mp.nstr(u, 15) for u in vals))
spread = max(vals) - min(vals)
check('B3 FLOAT: P - Pg = A r with A = %s (spread %s), so V = U[g] in this example' % (mp.nstr(vals[0], 12), mp.nstr(spread, 3)),
      spread < mp.mpf('1e-15') * max(1, abs(vals[0])))

npass = sum(1 for _, o in res if o)
print('%d checks, %s' % (len(res), 'ALL PASS' if npass == len(res) else '%d FAIL' % (len(res) - npass)))
