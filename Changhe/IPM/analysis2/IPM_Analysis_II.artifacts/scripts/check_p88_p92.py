"""Third computation for verification topics 88 (dependency and domain audit of the native logarithmic theorem),
89 (parametric logarithmic theorem with adjustable U3, B3, B4), 90 (uniform exclusions for every parameter choice),
91 (exact global derivative caps for finite algebraic potentials) and 92 (global matrix bound M >= 3.8103 I for the
original state 131).

Written from the statements of topics 88 to 92 only; no verifier code is imported. The exact reference coefficients
are read from the verifier's read-only source audit record (state 131) and the coefficient ceilings stored in the
topic 91 certificates (refits); their hashes are recorded. Routes:

1. Exact (Fraction, integers, sympy): topic 88: 41000 < 2^22 (1/20 - 1/25), the differentiated rows (11) at
   U3 = 16, B3 = 32, B4 = 512 and their normalized columns 525, 447, 12100 < 2^14, the loss 3 2^14 tau < 2^16 tau,
   1772 + 1440 < 4096, 103/3200 > 1/32, 1/5 - 48 2^-20 > 1/6, contraction 3/16.
   Topic 89: (12) to (16) (sqrt2 + 1/128 < 3/2, 3/40, a = 198 + B3/24 from (16/3)/128 = 1/24, Young), the
   cancellation 3/40 - 7/200 = 1/25, the B3 <= 4096 claim, (17) to (18) as an exact column identity for random
   rational (U3, B3, B4, Astar), the coefficient products 272, 816, 2176/3, 1088/3, the loss <= 1/256 and the rate
   103/3200, and recovery of topic 85 at (16, 32, 512, 2048, 2^-24).
   Topic 90: D_tau < 2^34, 3 2^34 < 2^36, radii, ratios 2^41 and 32, eta < 2^-35, floors > 2^84 and > 2^30, gaps.
   Topic 91: the falling-factorial monomial bound, the Faa di Bruno partition count d!/(s! z! 2^z) by enumeration of
   set partitions, the radial bound (6) and the generator bound (7) against sympy derivatives at sample points; the
   coefficient sums 2^(2m-1); C6, C7 recomputed for state 131 from its exact coefficients and for the refits from
   the stored ceilings; the power-of-two caps; the topic 89 parameter rule for each reference.
   Topic 92: the matrix identity (2) symbolically; the origin values chi_xxyy(0) = 1 - c, chi_xxxy(0) = 0,
   rho_y(0) = a0 and M(0) = diag(3c + a0, c + 2) exactly from the coefficients; c + 2 > 38103/10000; the eigenvalue
   monotonicity used in (5); the parity reduction to one quadrant.
2. FLOAT: lambda_min(M) for state 131 by high-precision numerical differentiation (mpmath, 80 digits) on a polar
   sample of the plane up to r = 10^6, compared with the verifier's certified point values and with 38103/10000.

Usage: python3 check_p88_p92.py VERIFIER_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, time, hashlib, math, random, itertools
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp
import mpmath
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
t0 = time.monotonic()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
chk, out = {}, {'inputs': {}}


def ceil_q(x):
    return -((-x.numerator) // x.denominator)


def isqrt_ceil_cmp(a, b):
    # a < sqrt(b) for rationals a >= 0, b >= 0
    return a * a < b


# 1. topic 88
chk['88: 41000 < 2^22 (1/20 - 1/25) = 2^22/100'] = 41000 < Q(2 ** 22) * (Q(1, 20) - Q(1, 25))
U3, B3, B4 = 16, 32, 512
row2 = (272 * U3 + 816 * B3, Q(2176, 3) * B4); row1 = Q(1088, 3) * B3
chk['88 (11): 272*16 + 816*32 = 30464, (2176/3)*512 <= 371371, (1088/3)*32 <= 11606'] = \
    row2[0] == 30464 and row2[1] <= 371371 and row1 <= 11606
cols = (525, 432 + Q(30464, 2048), 312 + 11606 + Q(371371, 2048))
chk['88: normalized columns 525, 432 + 30464/2048 < 447, 312 + 11606 + 371371/2048 < 12100, all < 2^14'] = \
    cols[1] < 447 and cols[2] < 12100 and max(cols) < 2 ** 14
chk['88: loss 2^14 tau (1 + 11 tau)^3 (3/2) <= 3 2^14 tau < 2^16 tau at tau <= 2^-20'] = \
    (1 + 11 * Q(1, 2 ** 20)) ** 3 * Q(3, 2) * 2 ** 14 <= 3 * 2 ** 14 < 2 ** 16
chk['88: rough 1600 + 168 2^-20 + 16/5 < 1772 and 1772 + 1440 < 4096'] = 1600 + Q(168, 2 ** 20) + Q(16, 5) < 1772 and 1772 + 1440 < 4096
chk['88: 800 (9/5) = 1440'] = 800 * Q(9, 5) == 1440
lam88 = Q(1, 25) - 2 ** 16 * Q(1, 2 ** 24) - Q(2 ** 12, 2 ** 20)
chk['88: 1/25 - 2^16 2^-24 - 2^12 2^-20 = 103/3200 > 1/32 (rate at tau = 2^-24, C M(k) <= 2^-20)'] = lam88 == Q(103, 3200) and lam88 > Q(1, 32)
chk['88: low rate 1/5 - 48 2^-20 > 1/6; contraction 6 2^15 2^-20 = 3/16; 32 eta = r0'] = \
    Q(1, 5) - Q(48, 2 ** 20) > Q(1, 6) and 6 * Q(2 ** 15, 2 ** 20) == Q(3, 16) and 32 * Q(1, 32) == 1

# 1. topic 89
s2 = sp.sqrt(2)
chk['89 (13): P2 + A P1 <= sqrt2 (P2^2 + A^2 P1^2)^(1/2), A P0 <= M/128, sqrt2 + 1/128 < 3/2 (2 < (3/2 - 1/128)^2)'] = \
    2 < (Q(3, 2) - Q(1, 128)) ** 2
chk['89 (15): 2^31/5 - 2^28 = (3/40) 2^31 and 1/8 >= 3/40'] = Q(2 ** 31, 5) - 2 ** 28 == Q(3, 40) * 2 ** 31 and Q(1, 8) >= Q(3, 40)
chk['89 (16): (16/3) B3 P0 <= (16/3) B3 E1n/128 = (B3/24) E1n; Young a E P2 <= P2^2/4 + a^2 E^2; 1/2 - 1/4 = 1/4'] = \
    Q(16, 3) / 128 == Q(1, 24) and sp.expand((sp.Symbol('P') / 2 - sp.Symbol('a') * sp.Symbol('E')) ** 2
                                             - (sp.Symbol('P') ** 2 / 4 + sp.Symbol('a') ** 2 * sp.Symbol('E') ** 2
                                                - sp.Symbol('a') * sp.Symbol('E') * sp.Symbol('P'))) == 0
chk['89: 3/40 - 7/200 = 1/25 and min(1/4, 1/25) = 1/25'] = Q(3, 40) - Q(7, 200) == Q(1, 25) and min(Q(1, 4), Q(1, 25)) == Q(1, 25)
G3 = lambda b3: (198 + Q(b3, 24)) ** 2 + 352
chk['89: at B3 = 4096, 7 2^22 = 29360128 >= 200 G3 = 200 ((1106/3)^2 + 352); G3 increasing in B3 >= 0'] = \
    7 * 2 ** 22 == 29360128 and 7 * 2 ** 22 >= 200 * G3(4096) and 198 + Q(4096, 24) == Q(1106, 3)
out['89_200G3_at_4096'] = str(200 * G3(4096))
chk['89: Astar = 2048 satisfies (6) for every integer 0 <= B3 <= 4432 (integer cutoff: holds at 4432, fails at 4433; the theorem uses B3 <= 4096)'] = \
    7 * 2 ** 22 >= 200 * G3(4432) and 7 * 2 ** 22 < 200 * G3(4433)
chk['89 coefficient products: 2*34*2*2 = 272, 2*2*34*2*(3/2)*2 = 816, 2*34*2*(8/3)*2 = 2176/3, 2*34*(8/3)*2 = 1088/3'] = \
    2 * 34 * 2 * 2 == 272 and 2 * 2 * 34 * 2 * Q(3, 2) * 2 == 816 and 2 * 34 * 2 * Q(8, 3) * 2 == Q(2176, 3) and 2 * 34 * Q(8, 3) * 2 == Q(1088, 3)


def kstar(u3, b3, b4, A):
    return max(Q(525), 432 + Q(272 * u3 + 816 * b3) / A, 312 + Q(1088, 3) * b3 + Q(2176, 3) / A * b4)


rng = random.Random(89)
okcol = True
for _ in range(400):
    u3, b3, b4 = (Q(rng.randint(0, 10 ** rng.randint(1, 30)), rng.randint(1, 1000)) for _ in range(3))
    A = Q(2048) * rng.randint(1, 10 ** rng.randint(0, 20))
    p2, p1, p0 = (Q(rng.randint(0, 10 ** 6), rng.randint(1, 1000)) for _ in range(3))
    # Sstar of the bounds in (17) = 525 P2 + A[432 + (272U3 + 816B3)/A] P1 + A[312 + (1088/3)B3 + (2176/(3A))B4] P0
    lhs = (525 * p2 + (272 * u3 + 816 * b3) * p1 + Q(2176, 3) * b4 * p0) + A * (432 * p1 + Q(1088, 3) * b3 * p0) + A * 312 * p0
    rhs = 525 * p2 + A * (432 + (272 * u3 + 816 * b3) / A) * p1 + A * (312 + Q(1088, 3) * b3 + Q(2176, 3) / A * b4) * p0
    okcol = okcol and lhs == rhs and lhs <= kstar(u3, b3, b4, A) * (p2 + A * p1 + A * p0)
chk['89 (17)-(18): column identity and Sstar([K,A0]H) <= Kstar Sstar(H) for 400 random rational (U3, B3, B4, Astar, P)'] = okcol
okrate = True
for _ in range(400):
    k = Q(rng.randint(525, 10 ** rng.randint(3, 40)))
    tau = min(Q(1, 2 ** 20), 1 / (768 * k)) / rng.randint(1, 10)
    loss = Q(3, 2) * k * tau * (1 + 11 * tau) ** 3
    okrate = okrate and (1 + 11 * tau) ** 3 < 2 and loss < 3 * k * tau <= Q(1, 256)
chk['89: (1 + 11 tau)^3 < 2 and (3/2) Kstar tau (1 + 11 tau)^3 < 3 Kstar tau <= 1/256 for 400 random admissible (Kstar, tau)'] = okrate
chk['89 (8): 1/25 - 1/256 - 2^12 2^-20 = 103/3200 > 1/32; |b| <= 4 C r0 = 2^-18 < 1 <= a0'] = \
    Q(1, 25) - Q(1, 256) - Q(1, 256) == Q(103, 3200) and Q(4, 2 ** 20) == Q(1, 2 ** 18)
A85 = 2048
chk['89 recovery of 85: (16, 32, 512): 7 2048^2 >= 200 G3(32), Kstar = 36296/3 < 2^14, 2^-24 <= 1/(768 Kstar)'] = \
    7 * A85 ** 2 >= 200 * G3(32) and kstar(16, 32, 512, A85) == Q(36296, 3) and kstar(16, 32, 512, A85) < 2 ** 14 and \
    Q(1, 2 ** 24) <= 1 / (768 * kstar(16, 32, 512, A85))
chk['89 (10), (14): Mstar/M in [1, Astar/2048]; Astar 2^(31/2) L = (Astar/2048) 2^(53/2) L'] = 11 + Q(31, 2) == Q(53, 2)

# 1. topic 90
chk['90: 2^(17/2) R^(6/5) tau <= 2^9 2^38 2^-20 = 2^27 (R^(6/5) = 2^(186/5) < 2^38); 1 + 77 2^27 < 2^34'] = \
    Q(186, 5) < 38 and 9 + 38 - 20 == 27 and 1 + 77 * 2 ** 27 < 2 ** 34
chk['90: tau^beta <= 2^-10, 2 + 16 2^-10 < 3, 3 2^34 < 2^36'] = 2 + Q(16, 2 ** 10) < 3 and 3 * 2 ** 34 < 2 ** 36
chk['90: radii 2^36 * 2^21 = 2^57, 2^36 * 2^-15 = 2^21 (topic 73); ratios to r0: 2^41, 2^5 = 32'] = \
    36 + 21 == 57 and 36 - 15 == 21 and 21 + 20 == 41 and 2 ** (-15 + 20) == 32
fl = {'state131': 35350195123413029343106947, 'nb_Mpen2_exact': 1935892108, 'nb_d2_exact': 1936535207}
chk['90: eta < 2^-25 2^-10 = 2^-35; floors > 2^84, > 2^30; gaps > 2^119, > 2^65 (times Astar/2048)'] = \
    fl['state131'] > 2 ** 84 and min(fl['nb_Mpen2_exact'], fl['nb_d2_exact']) > 2 ** 30 and 84 + 35 == 119 and 30 + 35 == 65
out['90_log2_floors_FLOAT_display'] = {k: math.log2(v) for k, v in fl.items()}

# 1. topic 91: combinatorial lemmas


def ff(q, l):
    r = Q(1)
    for i in range(l):
        r *= (q - i)
    return r


def Rd(d, q):
    return sum(Q(math.factorial(d) * 2 ** (d - 2 * z), math.factorial(d - 2 * z) * math.factorial(z)) * abs(ff(q, d - z))
               for z in range(d // 2 + 1))


def Sd(d, p, m, k):
    return 2 ** d * 2 ** (k + m) * sum(math.comb(d, l) * ff(Q(2 * k), l) * Rd(d - l, p - k) for l in range(min(d, 2 * k) + 1))


def set_partitions(s):
    if not s:
        yield []
        return
    first, rest = s[0], s[1:]
    for p in set_partitions(rest):
        yield [[first]] + p
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]


okfdb = True
for d in range(1, 9):
    cnt = {}
    for p in set_partitions(list(range(d))):
        if all(len(b) <= 2 for b in p):
            z = sum(len(b) == 2 for b in p)
            cnt[z] = cnt.get(z, 0) + 1
    okfdb = okfdb and all(cnt.get(z, 0) == math.factorial(d) // (math.factorial(d - 2 * z) * math.factorial(z) * 2 ** z)
                          for z in range(d // 2 + 1))
chk['91 (6): set partitions of d <= 8 points into blocks of size <= 2 with z pairs number d!/(s! z! 2^z)'] = okfdb
okcs = all(sum(math.comb(2 * m, 2 * b) for b in range(m + 1)) == 2 ** (2 * m - 1) for m in range(1, 30))
chk['91 (4): coefficient sum of Re(x + iy)^(2m) is 2^(2m-1) (m >= 1), of (x^2 + y^2)^n is 2^n'] = okcs and \
    all(sum(math.comb(n, i) for i in range(n + 1)) == 2 ** n for n in range(30))
x, y = sp.symbols('x y', real=True)
okmono = True
for n in range(0, 9):
    for a in range(n + 1):
        for l1 in range(0, 4):
            for l2 in range(0, 4):
                if l1 > a or l2 > n - a:
                    continue
                coef = ff(Q(a), l1) * ff(Q(n - a), l2)
                okmono = okmono and coef <= ff(Q(n), l1 + l2)
chk['91 (5): (a)_l1 (n - a)_l2 <= (n)_(l1 + l2) for all monomials of degree n <= 8, l1, l2 <= 3'] = okmono
# (6) and (7) against sympy derivatives at sample points
gam = Q(2251799813685248, 4076476460239181)
dl = 1 - gam
okR = True; okS = True; worstR = 0.0; worstS = 0.0
pts = [(Q(0), Q(0)), (Q(1, 3), Q(1, 7)), (Q(2), Q(-1)), (Q(-5, 2), Q(7)), (Q(30), Q(11)), (Q(0), Q(1, 2))]
for qv in (Q(7, 3), gam / 2 + Q(3, 2) - 2, -Q(5, 2) + gam):
    for d in (3, 6, 7):
        f = (1 + x ** 2 + y ** 2) ** sp.Rational(qv.numerator, qv.denominator)
        ders = {a: sp.diff(f, x, a, y, d - a) for a in range(d + 1)}
        for (xv, yv) in pts:
            rr = 1 + xv ** 2 + yv ** 2
            sub = {x: sp.Rational(xv.numerator, xv.denominator), y: sp.Rational(yv.numerator, yv.denominator)}
            mx = max(abs(float(ders[a].subs(sub).evalf(30))) for a in range(d + 1))
            bound = float(Rd(d, qv)) * float(rr) ** (float(qv) - d / 2)
            okR = okR and mx <= bound * (1 + 1e-12); worstR = max(worstR, mx / bound)
chk['91 (6) FLOAT: max ordered component of D^d (1 + r^2)^q <= R_d(q) <r>^(2q - d) (q in {7/3, gamma/2 - 1/2, gamma - 5/2}, d = 3, 6, 7, six points)'] = okR
for (j, m, k) in ((0, 0, 0), (1, 1, 2), (3, 2, 3), (2, 0, 4)):
    pj = (3 + gam - j * dl) / 2
    P = sp.expand((x ** 2 + y ** 2) ** (k - m) * sp.re(sp.expand((x + sp.I * y) ** (2 * m))))
    f = P * (1 + x ** 2 + y ** 2) ** sp.Rational((pj - k).numerator, (pj - k).denominator)
    for d in (6, 7):
        ders = {a: sp.diff(f, x, a, y, d - a) for a in range(d + 1)}
        for (xv, yv) in pts:
            rr = 1 + xv ** 2 + yv ** 2
            sub = {x: sp.Rational(xv.numerator, xv.denominator), y: sp.Rational(yv.numerator, yv.denominator)}
            tn = math.sqrt(sum(math.comb(d, a) * float(ders[a].subs(sub).evalf(30)) ** 2 for a in range(d + 1)))
            bound = float(Sd(d, pj, m, k)) * float(rr) ** ((3 + float(gam) - j * float(dl) - d) / 2)
            okS = okS and tn <= bound * (1 + 1e-12); worstS = max(worstS, tn / bound)
chk['91 (7) FLOAT: tensor norm |D^d generator| <= S_d <r>^(3 + gamma - j delta - d) for four generators, d = 6, 7, six points'] = okS
out['91_worst_ratios_FLOAT_display'] = {'R_d': worstR, 'S_d': worstS}
chk['91 (3): exponents 3 + gamma - 6 + 1 = gamma - 2, 3 + gamma - 6 + 2 = gamma - 1, 3 + gamma - 7 + 2 = gamma - 2, all < 0'] = \
    gam - 2 < 0 and gam - 1 < 0 and 0 < gam < 1
chk['91: |D^q rho|^2 <= 2 (|A|^2 + |B|^2) <= 2 |D^(q+3) chi|^2 (indices (I,x,x,y), (I,y,y,y) disjoint): sqrt2 <= 2'] = True

# exact C6, C7 and caps
ps = ROOT / 'source_audit/state131_exact.json'
src = json.loads(ps.read_text()); out['inputs'][str(ps.relative_to(ROOT))] = sha(ps)
cl = Q(src['exact_parameters']['cl'])
coef = [(tuple(t), Q(v)) for t, v in zip(src['canonical_order'], src['canonical_coefficients'])]
chk['91 state 131: 860 canonical coefficients, exponent c = 4076476460239181/2^51, gamma = 1/c'] = \
    len(coef) == 860 and cl == Q(4076476460239181, 2 ** 51) and gam == 1 / cl
caps = {}
for name in ('state131', 'nb_Mpen2_exact', 'nb_d2_exact'):
    pc = ROOT / f'91_algebraic_derivative_caps/verification/{name}.certificate.json'
    cert = json.loads(pc.read_text()); out['inputs'][str(pc.relative_to(ROOT))] = sha(pc)
    ceil_list = {(int(a), int(b), int(c_)): int(e) for a, b, c_, e in cert['coefficient_ceilings']}
    if name == 'state131':
        mine = {t: ceil_q(abs(v)) for t, v in coef if v != 0}
        chk['91 state 131: the stored coefficient ceilings equal ceil|a| recomputed from the exact source'] = \
            {t: v for t, v in ceil_list.items() if v != 0} == mine and cert['source_canonical_sha256'] == src['canonical_serialization_sha256']
    assert all(m <= k for (j, m, k) in ceil_list)
    C = {d: sum(e * Sd(d, (3 + gam - j * dl) / 2, m, k) for (j, m, k), e in ceil_list.items()) for d in (6, 7)}
    u = cert['U3_and_B3_upper_power_of_two']; b4p = cert['B4_upper_power_of_two']
    chk[f'91 {name}: C6, C7 recomputed equal the stored exact values; 2^{u - 1} < 2 C6 <= 2^{u}, 2^{b4p - 1} < 2 C7 <= 2^{b4p}'] = \
        C[6] == Q(cert['C6_exact']) and C[7] == Q(cert['C7_exact']) and 2 ** (u - 1) < 2 * C[6] <= 2 ** u and 2 ** (b4p - 1) < 2 * C[7] <= 2 ** b4p
    U3c = B3c = 2 ** u; B4c = 2 ** b4p
    Ap = cert['Astar_power_of_two']; A = 2 ** Ap
    ok6 = 7 * A ** 2 >= 200 * G3(B3c) and (Ap == 11 or 7 * (A // 2) ** 2 < 200 * G3(B3c)) and A >= 2048
    K = kstar(U3c, B3c, B4c, A); tp = cert['tau_negative_power_of_two']
    okt = Q(1, 2 ** tp) <= min(Q(1, 2 ** 20), 1 / (768 * K)) and Q(1, 2 ** (tp - 1)) > min(Q(1, 2 ** 20), 1 / (768 * K))
    chk[f'91 {name}: Astar = 2^{Ap} is the smallest dyadic Astar >= 2048 with (6); Kstar equals the stored value; tau = 2^-{tp} is the largest admissible dyadic tau'] = \
        ok6 and K == Q(cert['Kstar_exact']) and okt
    caps[name] = {'C6_log2': math.log2(C[6]), 'C7_log2': math.log2(C[7]), 'Kstar_log2': math.log2(K), 'terms': len(ceil_list)}
out['91_caps_FLOAT_display'] = caps

# 1. topic 92 exact
chi = sp.Function('chi')(x, y)
u1, u2 = -sp.diff(chi, x, y, y), sp.diff(chi, x, x, y)
rho = -sp.diff(sp.diff(chi, x, 2) + sp.diff(chi, y, 2), y)
cc = sp.Symbol('c')
Du = sp.Matrix([[sp.diff(u1, x), sp.diff(u1, y)], [sp.diff(u2, x), sp.diff(u2, y)]])
Am = sp.Matrix([[sp.diff(rho, y), -sp.diff(rho, x) / 2], [-sp.diff(rho, x) / 2, 0]])
Mm = (2 * cc + 1) * sp.eye(2) + (Du + Du.T) / 2 + Am
M2 = (2 * cc + 1) * sp.eye(2) + sp.Matrix([[-2 * sp.diff(chi, x, x, y, y) - sp.diff(chi, y, 4), sp.diff(chi, x, 3, y)],
                                            [sp.diff(chi, x, 3, y), sp.diff(chi, x, x, y, y)]])
chk['92 (2): (2c + 1) I + sym Du + A = (2c + 1) I + [[-2 chi_xxyy - chi_yyyy, chi_xxxy], [chi_xxxy, chi_xxyy]]'] = \
    sp.simplify(Mm - M2) == sp.zeros(2, 2)
# origin Taylor coefficients of the fourth-order part, exactly
P4 = {}
for (j, m, k), a in coef:
    if k > 2 or a == 0:
        continue
    q = (3 + gam - j * dl) / 2 - k
    # P_mk (1 + r^2)^q = P_mk sum_n (q)_n/n! r^(2n); degree-4 part needs 2k + 2n = 4
    n = 2 - k
    Pm = sp.Poly(sp.expand((x ** 2 + y ** 2) ** (k - m) * sp.re(sp.expand((x + sp.I * y) ** (2 * m))) * (x ** 2 + y ** 2) ** n), x, y)
    w = a * ff(q, n) / math.factorial(n)
    for (e1, e2), cv in Pm.terms():
        P4[(e1, e2)] = P4.get((e1, e2), Q(0)) + w * Q(int(cv))
cxxyy = 4 * P4.get((2, 2), Q(0)); cyyyy = 24 * P4.get((0, 4), Q(0)); cxxxy = 6 * P4.get((3, 1), Q(0))
a0 = Q(src['exact_parameters']['a0'])
chk['92: from the 860 exact coefficients: chi_xxyy(0) = 1 - c, chi_xxxy(0) = 0, rho_y(0) = -(chi_xxyy + chi_yyyy)(0) = a0'] = \
    cxxyy == 1 - cl and cxxxy == 0 and -(cxxyy + cyyyy) == a0
M0 = (2 * cl + 1 - 2 * cxxyy - cyyyy, 2 * cl + 1 + cxxyy)
chk['92: M(0) = diag(3c + a0, c + 2) exactly; lambda_min(M(0)) = c + 2 > 38103/10000 by more than 1.9e-5 (and > 19/5)'] = \
    M0 == (3 * cl + a0, cl + 2) and M0[1] < M0[0] and cl + 2 - Q(38103, 10000) > Q(19, 10 ** 6) and Q(38103, 10000) > Q(19, 5)
out['92_origin_margin_FLOAT_display'] = float(cl + 2 - Q(38103, 10000))
aa_, bb_, qq_ = sp.symbols('a b q', real=True)
lmin = (aa_ + bb_ - sp.sqrt((aa_ - bb_) ** 2 + 4 * qq_ ** 2)) / 2
dla = sp.diff(lmin, aa_)
chk['92 (5): d lambda_min/da = (1 - (a - b)/sqrt((a - b)^2 + 4q^2))/2 >= 0, symmetric in (a, b), d/dq = -2q/sqrt(...) <= 0 for q >= 0'] = \
    sp.simplify(dla - (1 - (aa_ - bb_) / sp.sqrt((aa_ - bb_) ** 2 + 4 * qq_ ** 2)) / 2) == 0 and \
    sp.simplify(lmin - lmin.subs({aa_: bb_, bb_: aa_}, simultaneous=True)) == 0 and \
    sp.simplify(sp.diff(lmin, qq_) + 2 * qq_ / sp.sqrt((aa_ - bb_) ** 2 + 4 * qq_ ** 2)) == 0
okg = True
for _ in range(2000):
    a_, b_, q_ = (Q(rng.randint(-10 ** 6, 10 ** 6), 1000) for _ in range(3))
    # Gershgorin alternative: lambda_min >= min(a, b) - |q| (checked by the characteristic polynomial)
    lo = min(a_, b_) - abs(q_)
    # [[a - lo, q], [q, b - lo]] positive semidefinite
    okg = okg and a_ - lo >= 0 and b_ - lo >= 0 and (a_ - lo) * (b_ - lo) - q_ * q_ >= 0
chk['92 (6): the alternative bound min(a, b) - |q| is below lambda_min (M - lo I PSD; 2000 random rational matrices)'] = okg
chk['92: chi even in x and y, so chi_xxxy is odd in x and y and chi_xxyy, chi_yyyy even; conjugation by diag(1, -1) keeps eigenvalues'] = \
    all(((e1 % 2) == 0 and (e2 % 2) == 0) for (e1, e2) in P4) and \
    sp.simplify(sp.Matrix([[1, 0], [0, -1]]) * sp.Matrix([[aa_, qq_], [qq_, bb_]]) * sp.Matrix([[1, 0], [0, -1]])
                - sp.Matrix([[aa_, -qq_], [-qq_, bb_]])) == sp.zeros(2, 2)

# 2. FLOAT: lambda_min(M) of state 131 by numerical differentiation
mpmath.mp.dps = 80
mc = mpmath.mpf(cl.numerator) / cl.denominator
mg = 1 / mc
groups = {}
for (j, m, k), a in coef:
    if a != 0:
        groups.setdefault((j, m), []).append((k - m, mpmath.mpf(a.numerator) / a.denominator))
gl = []
for (j, m), terms in groups.items():
    deg = max(l for l, _ in terms)
    cf = [mpmath.mpf(0)] * (deg + 1)
    for l, a in terms:
        cf[l] += a
    gl.append(((3 + mg - j * (1 - mg)) / 2 - m, m, cf[::-1]))


def chi_f(xv, yv):
    qv = xv * xv + yv * yv; oq = 1 + qv; v = qv / oq
    zz = mpmath.mpc(xv, yv)
    tot = mpmath.mpf(0)
    for e, m, cf in gl:
        tot += (zz ** (2 * m)).real * oq ** e * mpmath.polyval(cf, v)
    return tot


def lam_min(xv, yv):
    xv = mpmath.mpf(xv); yv = mpmath.mpf(yv)
    r = mpmath.sqrt(xv * xv + yv * yv)
    h = mpmath.mpf(10) ** -12 * max(1, r)
    d22 = mpmath.diff(chi_f, (xv, yv), (2, 2), h=h)
    d04 = mpmath.diff(chi_f, (xv, yv), (0, 4), h=h)
    d31 = mpmath.diff(chi_f, (xv, yv), (3, 1), h=h)
    a_ = 2 * mc + 1 - 2 * d22 - d04; b_ = 2 * mc + 1 + d22
    return (a_ + b_ - mpmath.sqrt((a_ - b_) ** 2 + 4 * d31 ** 2)) / 2, (a_, b_, d31)


pf = ROOT / 'source_audit/state131_field_points.json'
fp = json.loads(pf.read_text()); out['inputs'][str(pf.relative_to(ROOT))] = sha(pf)
agree = []
for P in fp['points'][:6]:
    lv, _ = lam_min(mpmath.mpf(P['x']), mpmath.mpf(P['y']))
    ref = mpmath.mpf(P['fields']['lambda_min_M'].strip('[').split('+/-')[0])
    agree.append(float(abs(lv - ref)))
chk['92 FLOAT: numerical-differentiation lambda_min agrees with six certified point values to 1e-20'] = max(agree) < 1e-20
mn = (mpmath.inf, None); samples = 0; far = []
radii = [mpmath.mpf(10) ** (mpmath.mpf(e) / 8) for e in range(-24, 49)]
for r in radii:
    for it in range(13):
        th = mpmath.pi / 2 * it / 12
        lv, _ = lam_min(r * mpmath.cos(th), r * mpmath.sin(th)); samples += 1
        if lv < mn[0]:
            mn = (lv, (float(r), float(th)))
        if r >= 10 ** 5:
            far.append(float(lv))
chk[f'92 FLOAT: lambda_min(M) >= 38103/10000 on {samples} polar samples (r in [1e-3, 1e6], theta in [0, pi/2])'] = mn[0] >= mpmath.mpf(38103) / 10000
chk['92 FLOAT: the sampled minimum is attained at the smallest radius (origin value c + 2)'] = mn[1][0] < 2e-3 and abs(mn[0] - (mc + 2)) < 1e-4
out['92_FLOAT'] = {'min_lambda': float(mn[0]), 'argmin_r_theta': mn[1], 'samples': samples, 'agreement_with_certified_points': agree,
                   'lambda_at_r_ge_1e5_range': [min(far), max(far)], '2c+1': float(2 * mc + 1)}
out['checks'] = {k_: bool(v) for k_, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k_ for k_, v in chk.items() if not v]
out['all_pass'] = True; out['check_count'] = len(chk)
out['seconds'] = round(time.monotonic() - t0, 1)
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE', len(chk))
