# c1-t1 independent check of T4-372 (c1-t4 research/sharp_amplitude_moment, PROOF sha256 6283be5d...), for R1-039.
# Written from the PROOF text only; the c1-t4 check code was not run or copied.
# Part A: exact symbolic identities in d > 0 (sympy). Part B: the constants at the campaign d in interval arithmetic
# (mpmath iv, 60 digits). Part C: FLOAT calibrations (mpmath quadrature) of the extremizer integrals and of the
# inequality on test functions; these are diagnostics, not part of the proof.
# Run from artifacts/checks: OMP_NUM_THREADS=1 python3 -B check_T4372.py > check_T4372.out
from fractions import Fraction as Fr
import sympy as sp
import mpmath as mp
from mpmath import iv

res = []


def check(name, ok):
    res.append((name, bool(ok)))
    print('%-4s %s' % ('PASS' if ok else 'FAIL', name))


# ---------------- Part A: symbolic identities
d, lam, b, H, R, beta = sp.symbols('d lambda b H R beta', positive=True)
a = d + 3
theta = d / (d + 2)
nu = 2 * (d + 2) / (d + 4)
check('A1 nu = 2 - 4/(a+1)', sp.simplify(nu - (2 - 4 / (a + 1))) == 0)
check('A2 1/4 + 1/(2a-2) = (d+4)/(4(d+2))', sp.simplify(sp.Rational(1, 4) + 1 / (2 * a - 2) - (d + 4) / (4 * (d + 2))) == 0)
check('A3 1/4 + 1/(a-3) = (d+4)/(4d)', sp.simplify(sp.Rational(1, 4) + 1 / (a - 3) - (d + 4) / (4 * d)) == 0)
# crossing radius R_phi = (H/(lam b))^(1/(a+1)); radial integrals with H = lam b R^(a+1) substituted
Hc = lam * b * R ** (a + 1)
r = sp.symbols('r', positive=True)
for dv in (sp.Rational(1, 2), sp.Rational(1824676646553933, 4076476460239181), sp.Integer(2)):
    av = dv + 3
    Hv = lam * b * R ** (av + 1)
    I2 = sp.integrate(lam ** 2 * b ** 2 * r ** 3, (r, 0, R)) + sp.integrate(Hv ** 2 * r ** (1 - 2 * av), (r, R, sp.oo))
    I1 = sp.integrate(b * lam * b * r ** 3, (r, 0, R)) + sp.integrate(b * Hv * r ** (2 - av), (r, R, sp.oo))
    ok2 = sp.simplify(I2 - lam ** 2 * b ** 2 * R ** 4 * (sp.Rational(1, 4) + 1 / (2 * av - 2))) == 0
    ok1 = sp.simplify(I1 - lam * b ** 2 * R ** 4 * (sp.Rational(1, 4) + 1 / (av - 3))) == 0
    check('A4 radial integrals of |h|^2 r and |y h| r at d = %s' % dv, ok2 and ok1)
# powers after substituting R^4 = (H/(lam b))^(4/(a+1)): norm^2 ~ H^(4/(d+4)) lam^nu b^nu, moment ~ lam^(d/(d+4))
Rp = (H / (lam * b)) ** (1 / (a + 1))
e_norm = sp.simplify(sp.expand_power_base(sp.powsimp(lam ** 2 * b ** 2 * Rp ** 4, force=True), force=True))
e_mom = sp.simplify(sp.expand_power_base(sp.powsimp(lam * b ** 2 * Rp ** 4, force=True), force=True))
check('A5 lam^2 b^2 R^4 = H^(4/(d+4)) lam^nu b^nu',
      sp.simplify(sp.log(e_norm) - sp.log(H ** (4 / (d + 4)) * lam ** nu * b ** nu)).equals(0)
      or sp.simplify(sp.expand_log(sp.log(e_norm), force=True)
                     - sp.expand_log(sp.log(H ** (4 / (d + 4)) * lam ** nu * b ** nu), force=True)) == 0)
check('A6 lam b^2 R^4 = H^(4/(d+4)) lam^(d/(d+4)) b^nu',
      sp.simplify(sp.expand_log(sp.log(e_mom), force=True)
                  - sp.expand_log(sp.log(H ** (4 / (d + 4)) * lam ** (d / (d + 4)) * b ** nu), force=True)) == 0)
# elimination: lam^nu = beta^2/(C0 H^(4/(d+4))); moment = D0 H^(4/(d+4)) lam^(d/(d+4))
C0, J = sp.symbols('C0 J', positive=True)
lam_e = (beta ** 2 / (C0 * H ** (4 / (d + 4)))) ** (1 / nu)
D0 = (d + 2) * C0 / d
mom = D0 * H ** (4 / (d + 4)) * lam_e ** (d / (d + 4))
target = (d + 2) / d * C0 ** ((d + 4) / (2 * (d + 2))) * beta ** theta * H ** (1 - theta)
check('A7 eliminated moment = Csharp beta^theta H^(1-theta)',
      sp.simplify(sp.expand_log(sp.log(mom), force=True) - sp.expand_log(sp.log(target), force=True)) == 0)
check('A8 D0 = (d+4)J/(4d) equals (d+2)/d C0 with C0 = (d+4)J/(4(d+2))',
      sp.simplify((d + 4) * J / (4 * d) - (d + 2) / d * ((d + 4) * J / (4 * (d + 2)))) == 0)
# split bound: disk sqrt(pi) beta R^2/2, exterior 4 H R^-d/d; minimize over R
A_, B_ = sp.sqrt(sp.pi) * beta / 2, 4 * H / d
Rs = (d * B_ / (2 * A_)) ** (1 / (d + 2))
fmin = A_ * Rs ** 2 + B_ * Rs ** (-d)
Csplit = (d + 2) / (2 * d) * sp.pi ** (theta / 2) * 4 ** (1 - theta)
Rv = sp.symbols('Rv', positive=True)
fR = A_ * Rv ** 2 + B_ * Rv ** (-d)
ok_crit = sp.simplify(sp.powsimp(sp.powdenest(sp.diff(fR, Rv).subs(Rv, Rs), force=True), force=True)) == 0
ok_conv = sp.simplify(sp.diff(fR, Rv, 2) - (2 * A_ + d * (d + 1) * B_ * Rv ** (-d - 2))) == 0
qq = fmin / (Csplit * beta ** theta * H ** (1 - theta))
ok_val = sp.simplify(sp.expand(sp.expand_log(sp.log(sp.powsimp(sp.powdenest(qq, force=True), force=True)),
                                             force=True))) == 0
ok_num = all(abs(sp.N(qq.subs({d: dv, beta: sp.Rational(3, 7), H: sp.Rational(5, 2)}), 50) - 1) < sp.Float('1e-45')
             for dv in (sp.Rational(1, 2), sp.Rational(7, 3), sp.Rational(1824676646553933, 4076476460239181)))
check('A9 split bound A R^2 + B R^-d: critical point, convexity, min = Csplit beta^theta H^(1-theta)',
      ok_crit and ok_conv and ok_val and ok_num)
# disk and exterior pieces themselves
rr, ph = sp.symbols('rr ph', positive=True)
check('A10 int_disk y^2 = pi R^4/4', sp.simplify(sp.integrate(sp.integrate(rr ** 3 * sp.sin(ph) ** 2, (ph, 0, 2 * sp.pi)),
                                                              (rr, 0, R)) - sp.pi * R ** 4 / 4) == 0)
check('A11 int_0^(2pi) |sin| = 4 and int_R^oo r^(2-a) dr = R^-d/d at d = 1/2',
      sp.integrate(sp.Abs(sp.sin(ph)), (ph, 0, 2 * sp.pi)) == 4
      and sp.simplify(sp.integrate(rr ** (2 - sp.Rational(7, 2)), (rr, R, sp.oo)) - R ** sp.Rational(-1, 2) / sp.Rational(1, 2)) == 0)
# pointwise maximizer: argmax of y t - t^2/(2 lam) on [-M, M] is sign(y) min(lam |y|, M)
yv, M, t = sp.symbols('y M t', real=True)
ok = True
for (yy, MM, ll) in [(sp.Rational(3, 2), sp.Rational(1, 5), 2), (sp.Rational(-1, 7), 5, 3), (sp.Rational(2, 3), 1, sp.Rational(1, 4))]:
    f = yy * t - t ** 2 / (2 * ll)
    cand = sp.sign(yy) * sp.Min(ll * abs(yy), MM)
    grid = [sp.Rational(k, 400) * MM for k in range(-400, 401)]
    ok = ok and all(f.subs(t, g) <= f.subs(t, cand) for g in grid)
check('A12 pointwise maximizer on [-M, M] (exact, grid of 801 rational points per case, 3 cases)', ok)

# ---------------- Part B: constants at the campaign d (intervals)
iv.dps = 60
c = Fr(4076476460239181, 2251799813685248)
dq = 1 - 1 / c
check('B1 d = 1 - 1/c = 1824676646553933/4076476460239181', dq == Fr(1824676646553933, 4076476460239181))
th_q = dq / (dq + 2)
nu_q = 2 * (dq + 2) / (dq + 4)
print('  theta =', th_q, ' nu =', nu_q)
dI = iv.mpf(dq.numerator) / dq.denominator
nuI = iv.mpf(nu_q.numerator) / nu_q.denominator
thI = iv.mpf(th_q.numerator) / th_q.denominator
JI = 2 * iv.sqrt(iv.pi) * iv.gamma((nuI + 1) / 2) / iv.gamma((nuI + 2) / 2)
C0I = (dI + 4) * JI / (4 * (dI + 2))
CsI = (dI + 2) / dI * iv.exp((dI + 4) / (2 * (dI + 2)) * iv.log(C0I))
CspI = (dI + 2) / (2 * dI) * iv.exp(thI / 2 * iv.log(iv.pi)) * iv.exp((1 - thI) * iv.log(iv.mpf(4)))
ratio = CsI / CspI


def frac(x):
    m, e = x.man_exp
    return Fr(m) * Fr(2) ** e


def dec(f, n, up):
    # decimal string of the Fraction f > 0 rounded down (up = False) or up (up = True) to n digits after the point
    k = f * 10 ** n
    q = k.numerator // k.denominator
    if up and q * k.denominator != k.numerator:
        q += 1
    return '%d.%0*d' % (q // 10 ** n, n, q % 10 ** n)


ends = {}
for n, v in [('Jnu', JI), ('C0', C0I), ('Csharp', CsI), ('Csplit', CspI), ('Csharp/Csplit', ratio)]:
    lo, hi = frac(mp.make_mpf(v._mpi_[0])), frac(mp.make_mpf(v._mpi_[1]))
    ends[n] = (lo, hi)
    print('  %-14s in [%s, %s], width < %s' % (n, dec(lo, 24, False), dec(hi, 24, True), mp.nstr(mp.mpf(float(hi - lo)), 3)))


def inside(n, lo, hi):
    return Fr(lo) < ends[n][0] and ends[n][1] < Fr(hi)


check('B2 Jnu in (3.881723940658062035679, 3.881723940658062035680)',
      inside('Jnu', '3.881723940658062035679', '3.881723940658062035680'))
check('B3 C0 in (1.763392688289059058889, 1.763392688289059058890)',
      inside('C0', '1.763392688289059058889', '1.763392688289059058890'))
check('B4 Csharp in (9.155134741153639269902, 9.155134741153639269903) (T4-372 digits)',
      inside('Csharp', '9.155134741153639269902', '9.155134741153639269903'))
check('B5 Csplit in (9.423825890966201403965, 9.423825890966201403966) (T4-371 digits)',
      inside('Csplit', '9.423825890966201403965', '9.423825890966201403966'))
check('B6 Csharp/Csplit in (0.971488103354059961363, 0.971488103354059961364), so Csharp < Csplit',
      inside('Csharp/Csplit', '0.971488103354059961363', '0.971488103354059961364') and ends['Csharp/Csplit'][1] < 1)
mp.mp.dps = 30
nuF = mp.mpf(nu_q.numerator) / nu_q.denominator
Jq = mp.quad(lambda p: abs(mp.sin(p)) ** nuF, [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi])
check('B7 Jnu Gamma formula agrees with direct quadrature of |sin|^nu (FLOAT, 1e-20)',
      abs(Jq - mp.mpf(ends['Jnu'][0].numerator) / ends['Jnu'][0].denominator) < mp.mpf('1e-20'))
# moment constant of T4-351 for comparison: mu = 8/((-q-1)(-q-2)(-q-3)), q = -d-3
mu = Fr(8) / ((dq + 2) * (dq + 1) * dq)
print('  mu = 8/((d+2)(d+1)d) =', float(mu))
check('B8 mu < 5.04423 (T4-351 value)', mu < Fr(504423, 100000))

# ---------------- Part C: FLOAT calibrations
mp.mp.dps = 25


def extremizer_integrals(dd, HH, bb):
    aa = dd + 3
    nuv = 2 * (dd + 2) / (dd + 4)
    Jv = 2 * mp.sqrt(mp.pi) * mp.gamma((nuv + 1) / 2) / mp.gamma((nuv + 2) / 2)
    C0v = (dd + 4) * Jv / (4 * (dd + 2))
    lamv = (bb ** 2 / (C0v * HH ** (4 / (dd + 4)))) ** (1 / nuv)

    def radial(ph, k):
        s = abs(mp.sin(ph))
        Rph = (HH / (lamv * s)) ** (1 / (aa + 1))
        if k == 2:
            f = lambda rr: min(lamv * s * rr, HH * rr ** (-aa)) ** 2 * rr
        else:
            f = lambda rr: rr * s * min(lamv * s * rr, HH * rr ** (-aa)) * rr
        return mp.quad(f, [0, Rph, 2 * Rph, mp.inf])
    n2 = 4 * mp.quad(lambda ph: radial(ph, 2), [0, mp.pi / 2])
    m1 = 4 * mp.quad(lambda ph: radial(ph, 1), [0, mp.pi / 2])
    Cs = (dd + 2) / dd * C0v ** ((dd + 4) / (2 * (dd + 2)))
    return n2, m1, Cs * bb ** (dd / (dd + 2)) * HH ** (2 / (dd + 2))


for dd, HH, bb in [(mp.mpf(dq.numerator) / dq.denominator, mp.mpf(1), mp.mpf('1e-3')),
                   (mp.mpf('0.5'), mp.mpf(3), mp.mpf('0.2')), (mp.mpf(2), mp.mpf('0.7'), mp.mpf(1))]:
    n2, m1, rhs = extremizer_integrals(dd, HH, bb)
    print('  d=%s H=%s beta=%s: ||h||^2/beta^2 = %s, moment/(Csharp beta^theta H^(1-theta)) = %s'
          % (mp.nstr(dd, 6), HH, bb, mp.nstr(n2 / bb ** 2, 12), mp.nstr(m1 / rhs, 12)))
    check('C1 extremizer norm and moment by 2D quadrature at d = %s (FLOAT, 1e-8)' % mp.nstr(dd, 6),
          abs(n2 / bb ** 2 - 1) < 1e-8 and abs(m1 / rhs - 1) < 1e-8)


# test functions h = k y exp(-r^2/s^2) scaled to the largest k with |h| <= H r^-a; the ratio must be <= 1
def gauss_ratio(dd, s):
    aa = dd + 3
    # sup over r of r^(1+a) exp(-r^2/s^2) at r^2 = (1+a) s^2/2
    rm = mp.sqrt((1 + aa) / 2) * s
    k = 1 / (rm ** (1 + aa) * mp.exp(-rm ** 2 / s ** 2))  # then |h| <= k r exp(-r^2/s^2) <= r^-a (H = 1)
    n2 = k ** 2 * mp.quad(lambda rr: rr ** 3 * mp.exp(-2 * rr ** 2 / s ** 2), [0, mp.inf]) * mp.pi
    mom = k * mp.quad(lambda rr: rr ** 3 * mp.exp(-rr ** 2 / s ** 2), [0, mp.inf]) * mp.pi
    nuv = 2 * (dd + 2) / (dd + 4)
    Jv = 2 * mp.sqrt(mp.pi) * mp.gamma((nuv + 1) / 2) / mp.gamma((nuv + 2) / 2)
    C0v = (dd + 4) * Jv / (4 * (dd + 2))
    Cs = (dd + 2) / dd * C0v ** ((dd + 4) / (2 * (dd + 2)))
    return mom / (Cs * mp.sqrt(n2) ** (dd / (dd + 2)))


dQ = mp.mpf(dq.numerator) / dq.denominator
rats = [gauss_ratio(dQ, mp.mpf(s)) for s in ('0.1', '1', '10', '1000')]
print('  Gaussian test ratios at the campaign d:', [mp.nstr(x, 8) for x in rats])
check('C2 Gaussian test functions satisfy (1) with ratio < 1 (FLOAT diagnostic)', all(x < 1 for x in rats))

print('summary: %d checks, %s' % (len(res), 'ALL PASS' if all(o for _, o in res) else 'FAILURES: %s' % [n for n, o in res if not o]))
