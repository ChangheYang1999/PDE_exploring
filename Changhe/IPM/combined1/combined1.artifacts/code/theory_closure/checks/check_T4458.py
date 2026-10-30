# R1-046 (REVIEWS_v44): independent review of T4-458 (candidate C1-N1-001 has no stationary correction in its affine L^2
# class, c1-t4 research/candidate001_affine_exclusion, PROOF sha256 771ad6b4...789a3e), written from the PROOF text and
# the raw generator file only. No c1-t4 or c1-n4 code is run; the c1-t4 coefficient table is read only for comparison.
# Part A, exact sympy: the polar formulas (3), (4) and (6) of the PROOF against Cartesian differentiation, for a
#   symbolic radial exponent d and sample frequencies.
# Part B, exact rationals: the leading profiles of C1-N1-001 by a different method (direct Cartesian differentiation
#   of the homogeneous functions r^p F(theta), F a Laurent polynomial in w = e^(i theta)); the leading
#   residual coefficient E at q = 2 gamma - 1 (linear part of branch 1 plus u_0 . grad rho_0); comparison with the
#   c1-t4 table; E nonzero; the exponent bookkeeping (q > 0, q < gamma, every other label below q).
# Usage: python3 check_T4458.py (from artifacts/checks). Inputs: data/C1-N1-001_raw.json (copy of
# c1-t4/research/candidate001_affine_exclusion/source/raw.json, sha256 8077f130...dc355c7, the immutable snapshot
# generator file) and data/T4458_leading_coefficients.json (copy of that topic's data/leading_coefficients.json).
import hashlib, json, os, time
from fractions import Fraction as Fr
import sympy as sp

t0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'data', 'C1-N1-001_raw.json')
T4C = os.path.join(HERE, 'data', 'T4458_leading_coefficients.json')
n_ok = 0


def ok(cond, msg):
    global n_ok
    assert cond, msg
    n_ok += 1


ok(hashlib.sha256(open(RAW, 'rb').read()).hexdigest() ==
   '8077f1305e5403264831de280689bb9334628bd1aa1233ce4dec58017dc355c7', 'raw hash')
x, y = sp.symbols('x y', real=True)
w, d = sp.symbols('w d')
R2 = x**2 + y**2


def lap(f):
    return sp.diff(f, x, 2) + sp.diff(f, y, 2)


def on_circle(f):
    # value on r = 1 as a Laurent polynomial in w = e^(i theta); every power of R2 is replaced by 1
    f = f.replace(lambda e: e.is_Pow and e.base == R2, lambda e: sp.Integer(1))
    f = f.subs({x: (w + 1 / w) / 2, y: (w - 1 / w) / (2 * sp.I)}, simultaneous=True)
    return sp.Poly(sp.expand(f * w**60), w)


def sine_coeffs(P):
    # f = sum_k c_k w^k with real f; returns {n: b_n} for f = sum b_n sin(n theta) + cosine part, and the cosine part
    c = {}
    for (k,), v in P.terms():
        c[k - 60] = v
    b, a = {}, {}
    for n in range(0, 61):
        cp, cm = c.get(n, 0), c.get(-n, 0)
        bn = sp.expand(sp.I * (cp - cm))      # b_n = i (c_n - c_-n)
        an = sp.expand(cp + cm) if n else sp.expand(cp)
        if bn != 0:
            b[n] = bn
        if an != 0:
            a[n] = an
    return b, a


# ---- Part A: formulas (3), (4), (6), compared exactly as Laurent polynomials on the unit circle
def re_n(n):
    return sp.expand(sp.re(sp.expand((x + sp.I * y)**n)))


def im_n(n):
    return sp.expand(sp.im(sp.expand((x + sp.I * y)**n)))


def sine_of(n, coef):
    # sin(n theta) times coef, as a Laurent polynomial expression in w
    return coef * (w**n - w**(-n)) / (2 * sp.I)


for n in [0, 2, 4, 6]:
    chi = R2**((d - n) / 2) * re_n(n)
    rho = on_circle(-sp.diff(lap(chi), y)).as_expr()
    psi = on_circle(sp.diff(chi, x, y)).as_expr()
    r3 = sine_of(n + 1, -(d**2 - n**2) * (d - 2 - n) / 2) + sine_of(n - 1, (d**2 - n**2) * (d - 2 + n) / 2)
    r4 = sine_of(n + 2, (d - n) * (d - n - 2) / 4) + sine_of(n - 2, -(d + n) * (d + n - 2) / 4)
    ok(sp.expand(rho - sp.expand(r3 * w**60)) == 0, 'formula (3) n=%d' % n)
    ok(sp.expand(psi - sp.expand(r4 * w**60)) == 0, 'formula (4) n=%d' % n)
# (6): stream A r^(g+1) sin(m theta), density B r^g sin(n theta), u = (-psi_y, psi_x), symbolic g
g = sp.symbols('g')
for (m, n) in [(1, 2), (3, 1), (2, 5), (4, 4), (5, 2)]:
    psi = R2**((g + 1 - m) / 2) * im_n(m)
    rho = R2**((g - n) / 2) * im_n(n)
    prod = on_circle(-sp.diff(psi, y) * sp.diff(rho, x) + sp.diff(psi, x) * sp.diff(rho, y)).as_expr()
    r6 = sine_of(n + m, (-g * m + (g + 1) * n) / 2) + sine_of(n - m, (-g * m - (g + 1) * n) / 2)
    ok(sp.expand(prod - sp.expand(r6 * w**60)) == 0, 'formula (6) m=%d n=%d' % (m, n))
print('Part A: formulas (3), (4), (6) agree exactly with Cartesian differentiation;', n_ok, 'checks so far')

# ---- Part B: leading profiles of C1-N1-001, by direct Cartesian differentiation of homogeneous functions
# A homogeneous function r^p F(theta) is stored as (p, F) with F a Laurent polynomial in w = e^(i theta) whose
# coefficients are exact Gaussian rationals; d/dx (r^p F) = r^(p-1) (p cos F - sin F'), d/dy (r^p F) =
# r^(p-1) (p sin F + cos F'), F' = dF/dtheta. This does not use the polar formulas (3) to (6) of the PROOF.


class C:
    __slots__ = ('a', 'b')

    def __init__(self, a, b=Fr(0)):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        return C(self.a + o.a, self.b + o.b)

    def __mul__(self, o):
        return C(self.a * o.a - self.b * o.b, self.a * o.b + self.b * o.a)

    def iszero(self):
        return self.a == 0 and self.b == 0


def padd(P, Q):
    R = dict(P)
    for k, v in Q.items():
        R[k] = R[k] + v if k in R else v
    return {k: v for k, v in R.items() if not v.iszero()}


def pmul(P, Q):
    R = {}
    for k1, v1 in P.items():
        for k2, v2 in Q.items():
            k = k1 + k2
            R[k] = R[k] + v1 * v2 if k in R else v1 * v2
    return {k: v for k, v in R.items() if not v.iszero()}


def pscal(s, P):
    return {k: v * s for k, v in P.items() if not (v * s).iszero()}


COS = {1: C(Fr(1, 2)), -1: C(Fr(1, 2))}
SIN = {1: C(0, Fr(-1, 2)), -1: C(0, Fr(1, 2))}


def dtheta(P):
    return {k: v * C(0, k) for k, v in P.items() if k != 0}


def ddx(f):
    p, F = f
    return (p - 1, padd(pmul(pscal(C(p), COS), F), pscal(C(-1), pmul(SIN, dtheta(F)))))


def ddy(f):
    p, F = f
    return (p - 1, padd(pmul(pscal(C(p), SIN), F), pmul(COS, dtheta(F))))


def hadd(f, g):
    assert f[0] == g[0], 'degrees differ'
    return (f[0], padd(f[1], g[1]))


def hneg(f):
    return (f[0], pscal(C(-1), f[1]))


def lap(f):
    return hadd(ddx(ddx(f)), ddy(ddy(f)))


def sine_cos(P):
    b, a = {}, {}
    n_max = max(abs(k) for k in P) if P else 0
    for n in range(0, n_max + 1):
        cp, cm = P.get(n, C(0)), P.get(-n, C(0))
        bn = C(0, 1) * (cp + cm * C(-1))
        an = (cp + cm) if n else cp
        if not bn.iszero():
            b[n] = bn
        if not an.iszero():
            a[n] = an
    return b, a


def partB(raw, T4, ok):
    c0 = Fr(raw['cl_exact'])
    gam = 1 / c0
    dlt = 1 - gam
    q = 2 * gam - 1
    a = {}
    for G in raw['generators']:
        a[(G['j'], G['m'])] = a.get((G['j'], G['m']), Fr(0)) + Fr(G['coef'])
    out = {}
    for j in (0, 1):
        dj = 3 + gam - j * dlt
        chi = (dj, {})
        for m in range(0, 10):
            A = a.get((j, m), Fr(0))
            if A == 0:
                continue
            # chi_jm = (x^2+y^2)^((d_j-2m)/2) Re (x+iy)^(2m) = r^(d_j) cos(2 m theta)
            F = {2 * m: C(A / 2), -2 * m: C(A / 2)} if m else {0: C(A)}
            chi = hadd(chi, (dj, F))
        rho = hneg(ddy(lap(chi)))
        psi = ddx(ddy(chi))
        out[j] = dict(rho=rho, psi=psi, u1=hneg(ddy(psi)), u2=ddx(psi), rx=ddx(rho), ry=ddy(rho))
    f0, f1 = out[0], out[1]
    ok(f0['rho'][0] == gam and f1['rho'][0] == q, 'density degrees gamma and q')
    ok(f0['u1'][0] + f0['rx'][0] == q, 'u_0 . grad rho_0 has degree q')
    QU = padd(pmul(f0['u1'][1], f0['rx'][1]), pmul(f0['u2'][1], f0['ry'][1]))
    E = padd(pscal(C(c0 * q - 1), f1['rho'][1]), QU)
    bG0, aG0 = sine_cos(f0['rho'][1])
    bG1, aG1 = sine_cos(f1['rho'][1])
    bE, aE = sine_cos(E)
    ok(all(v.b == 0 for v in list(bG0.values()) + list(bG1.values()) + list(bE.values())), 'real sine coefficients')
    ok(len(bG0) > 0 and not aG0, 'G_0 nonzero, pure sine')
    ok(not aG1 and not aE, 'G_1 and E pure sine (density odd in y)')
    ok(len(bE) > 0, 'E nonzero')
    ok(Fr(T4['q_exact']) == q and Fr(T4['c_exact']) == c0, 'T4 table exponents')
    mine = {n: v.a for n, v in bE.items()}
    theirs = {int(n): Fr(v) for n, v in T4['E10'].items() if Fr(v) != 0}
    ok(mine == theirs, 'E sine coefficients equal the c1-t4 table exactly (modes %s)' % sorted(mine))
    dens0 = {int(n): Fr(v) for n, v in T4['density']['0'].items() if Fr(v) != 0}
    dens1 = {int(n): Fr(v) for n, v in T4['density']['1'].items() if Fr(v) != 0}
    ok({n: v.a for n, v in bG0.items()} == dens0, 'G_0 equals the c1-t4 density table')
    ok({n: v.a for n, v in bG1.items()} == dens1, 'G_1 equals the c1-t4 density table')
    ssq = sum(v * v for v in mine.values())
    ok(ssq == Fr(T4['E10_sum_squares_exact']), 'sum of squares equals the c1-t4 value')
    return dict(c0=c0, gam=gam, q=q, mine=mine, ssq=ssq, bG0=bG0, bG1=bG1)

raw = json.load(open(RAW))
gens = raw['generators']
ok(len(gens) == 860, '860 generators')
c0 = Fr(raw['cl_exact'])
gam = 1 / c0
dlt = 1 - gam
q = 2 * gam - 1
ok(c0 == Fr(4076476460239181, 2251799813685248), 'c0')
ok(q == Fr(427123167131315, 4076476460239181) and 0 < q < gam < 1 and dlt > 0, 'q exact, 0 < q < gamma < 1')
ok(q == gam - dlt, 'q = gamma - delta (label (1,0))')
# every other label gamma - h delta - 2k with (h,k) != (0,0),(1,0) is below q
ok(gam - 2 * dlt < q and gam - 2 < q, 'labels h >= 2 or k >= 1 lie below q')
# T(1) = 1: t^h at t = 1, and t^w P_n(2t - 1) at t = 1 with P_n(1) = 1 (checked with sympy for every n used)
for G in gens:
    sp_ = G['spec']
    if sp_[0] == 'mono':
        ok(len(sp_) == 2 and int(sp_[1]) >= 0, 'mono spec')
    else:
        ok(sp_[0] == 'leg' and len(sp_) == 3 and min(int(sp_[1]), int(sp_[2])) >= 0, 'leg spec')
for n in sorted({int(G['spec'][1]) for G in gens if G['spec'][0] == 'leg'} |
                {int(G['spec'][2]) for G in gens if G['spec'][0] == 'leg'}):
    ok(sp.legendre(n, 1) == 1, 'P_n(1) = 1')
ok(all(G['j'] in (0, 1, 2, 3) and 0 <= G['m'] <= 9 for G in gens), 'branch and m indices')
T4 = json.load(open(T4C))
res = partB(raw, T4, ok)
mine, ssq = res['mine'], res['ssq']
print('Part B: E has sine modes', sorted(mine), '; lowest', min(mine), 'coefficient', float(mine[min(mine)]))
print('  sum of squared sine coefficients of E =', float(ssq), '(exact rational; int E^2 dtheta = pi times this)')
print('  G_0 sine modes', sorted(res['bG0']), '; G_1 sine modes', sorted(res['bG1']))
print('  q =', q, '=', float(q), '; gamma =', float(gam), '; c0 q - 1 =', float(c0 * q - 1))
print('checks passed', n_ok)
print('RESULT PASS')
