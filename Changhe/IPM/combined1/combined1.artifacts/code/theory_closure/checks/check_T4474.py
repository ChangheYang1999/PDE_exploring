# R1-050 (REVIEWS_v47): independent review of T4-474 (c1-t4 research/partial_mode_hardy_certificate, PROOF sha256
# afd349a7...189aa9414) and of the tail step of N4-403 (c1-n4 research/candidate016_angular_tail_bound, PROOF sha256
# c459a7b9...285a9bf0cb), written from the two PROOF texts only. No c1-t4 or c1-n4 code is run; their saved numbers are
# read for comparison.
# Part A, exact sympy: the parity argument (even in x, odd in y gives only odd sine modes); the tangential field
#   A_F = -e_theta r f cos(n theta)/n has div A_F = f sin(n theta) and is orthogonal to every radial gradient (the
#   cutoff step); angular Parseval for the weight r^2; on the manufactured fixture F = -Delta(psi_1 + psi_3) the identity
#   int A_F . grad phi = -int F phi for two rational test functions, by exact integration.
# Part B, exact rationals: the prefix lemma for symbolic nonnegative energy lists (B_N - M2 identity, the bound
#   (3), monotonicity in N, equality of T4-474's B_(N+2) with N4-403's S_N + (R2 - Q_N)/(N+2)^2, the outward formula
#   (4) and the split formula of N4-403 and their difference), on T4-474's four fixture lists and on 200 pseudo-random
#   rational lists; the omission counterexamples; the known-solution fixture (B_3 = M2, B_3 - a_1 - a_3 = H^2).
# Part C, exact rationals: candidate 016. From N4-403's saved exact endpoints of q_1, q_3, q_5, q_7 and of R2 = ||rF||^2:
#   both complete M2 uppers, the plain H upper, the improved H and E2 uppers with the N4-398 sum floor and the N4-392
#   component uppers, the lower bounds, and the T4-474 loss bounds S/N^2 for N = 1, 3, 5, 9, 17, 33, 65.
# Part D, Arb balls, CONDITIONAL on c1-n3's 30-digit mode Hardy displays: q_1 = H_1^2 and q_3 = 9 H_3^2 against
#   N4-403's exact endpoints, and the FLOAT size of the true tail sum_(n>=9) q_n/n^2 against the bound (R2 - Q_7)/81.
# Usage: python3 check_T4474.py (from artifacts/checks). Inputs in data/: N4403_result_v01.json (copy of c1-n4
#   research/candidate016_angular_tail_bound/verification/result_v01.json), T4474_parameters.json (copy of c1-t4
#   research/partial_mode_hardy_certificate/data/parameters.json), N4392_comparison.json, N4396_result.json,
#   N4398_result.json, N3_016_hdual_m13deep.json; sha256 checked.
import hashlib, json, os, random, sys, time
from fractions import Fraction as Fr
from math import isqrt
import sympy as sp
import flint

sys.set_int_max_str_digits(0)
t0 = time.time()
n_ok = 0


def ok(cond, msg):
    global n_ok
    assert cond, msg
    n_ok += 1


def dec_up(z, k):
    # smallest multiple of 10^-k that is >= z, as a decimal string (exact)
    j = -((-z.numerator * 10 ** k) // z.denominator)
    return '%s%d.%0*d' % ('-' if j < 0 else '', abs(j) // 10 ** k, k, abs(j) % 10 ** k)


def dec_dn(z, k):
    j = (z.numerator * 10 ** k) // z.denominator
    return '%d.%0*d' % (j // 10 ** k, k, j % 10 ** k)


def sqrt_up(z, k):
    # smallest d = j/10^k with d^2 >= z (z >= 0), exact
    t = z * 10 ** (2 * k)
    j = isqrt(t.numerator // t.denominator)
    while j * j < t:
        j += 1
    return '%d.%0*d' % (j // 10 ** k, k, j % 10 ** k)


def sqrt_dn(z, k):
    t = z * 10 ** (2 * k)
    j = isqrt(t.numerator // t.denominator)
    return '%d.%0*d' % (j // 10 ** k, k, j % 10 ** k)


# displays: uppers rounded up and lowers rounded down from the exact values (dec_up, sqrt_up, dec_dn, sqrt_dn)
# ---- Part A
r, th = sp.symbols('r theta', positive=True)
x, y = sp.symbols('x y', real=True)
# parity: theta -> -theta is y -> -y, theta -> pi - theta is x -> -x
for n in range(1, 12):
    s_odd_y = sp.simplify(sp.sin(n * (-th)) + sp.sin(n * th)) == 0
    c_odd_y = sp.simplify(sp.cos(n * (-th)) + sp.cos(n * th)) == 0
    s_even_x = sp.simplify(sp.sin(n * (sp.pi - th)) - sp.sin(n * th)) == 0
    ok(s_odd_y and not c_odd_y, 'odd in y: sine modes only, n=%d' % n)
    ok(s_even_x == (n % 2 == 1), 'sin(n theta) even in x exactly for odd n, n=%d' % n)
f = sp.Function('f')
nn = sp.symbols('n', positive=True, integer=True)
Ath = -r * f(r) * sp.cos(nn * th) / nn
ok(sp.simplify(sp.diff(Ath, th) / r - f(r) * sp.sin(nn * th)) == 0, 'div A_F = f sin(n theta)')
chi = sp.Function('chi')
# grad chi(r) = chi'(r) e_r; A_F = A_theta e_theta; e_r . e_theta = 0
er = sp.Matrix([sp.cos(th), sp.sin(th)])
et = sp.Matrix([-sp.sin(th), sp.cos(th)])
ok(sp.simplify((sp.diff(chi(r), r) * er).dot(Ath * et)) == 0, 'radial cutoff gradient orthogonal to A_F')
# Parseval with weight r^2: int |r f_n sin(n th) + r f_m sin(m th)|^2 = pi int r^3 (f_n^2 + f_m^2) dr for n != m
for (n1, n2) in [(1, 3), (3, 5), (1, 7)]:
    I = sp.integrate((sp.sin(n1 * th) + 2 * sp.sin(n2 * th)) ** 2, (th, 0, 2 * sp.pi))
    ok(I == 5 * sp.pi, 'angular Parseval %d %d' % (n1, n2))
# fixture: psi_1 = r sin th/(1+r^2)^(3/2), psi_3 = r^3 sin 3th/(1+r^2)^3, F = -Delta(psi_1 + psi_3)
u = {1: r / (1 + r ** 2) ** sp.Rational(3, 2), 3: r ** 3 / (1 + r ** 2) ** 3}
fF = {n: sp.simplify(-(sp.diff(un, r, 2) + sp.diff(un, r) / r - n ** 2 * un / r ** 2)) for n, un in u.items()}
S = {n: sp.integrate(sp.simplify(sp.pi * r ** 3 * fF[n] ** 2), (r, 0, sp.oo)) for n in (1, 3)}
ok(S[1] == sp.Rational(3, 4) * sp.pi and S[3] == sp.Rational(64, 35) * sp.pi, 'fixture S_1/pi = 3/4, S_3/pi = 64/35')
Ffull = fF[1] * sp.sin(th) + fF[3] * sp.sin(3 * th)
Afull = -r * (fF[1] * sp.cos(th) / 1 + fF[3] * sp.cos(3 * th) / 3)
# A_F . grad phi = A_theta (1/r) d_theta phi; after the exact angular integration the two radial densities cancel
# pointwise in r (so the radial integrals, which converge for these rational phi, agree)
for phi in (r * sp.sin(th) / (1 + r ** 2) ** 3, r ** 3 * sp.sin(3 * th) / (1 + r ** 2) ** 5 + r * sp.sin(th) / (1 + r ** 2) ** 4):
    lhs = sp.integrate(sp.expand(Afull * sp.diff(phi, th) / r * r), (th, 0, 2 * sp.pi))
    rhs = sp.integrate(sp.expand(Ffull * phi * r), (th, 0, 2 * sp.pi))
    ok(sp.simplify(lhs + rhs) == 0 and sp.simplify(rhs) != 0, 'int A_F . grad phi = -int F phi on the fixture')
print('Part A: parity, div A_F = F, cutoff orthogonality, Parseval, fixture S_n and the distributional identity;',
      n_ok, 'checks')

# ---- Part B
odd = list(range(1, 2 * 12, 2))           # modes 1, 3, ..., 23
Ssym = {n: sp.Symbol('S%d' % n, nonnegative=True) for n in odd}
Stot = sum(Ssym.values())
M2s = sum(Ssym[n] / sp.Integer(n) ** 2 for n in odd)


def B(N, Sv, St):
    # T4-474 (1): every mode n < N included, S = St the complete weighted energy
    return St / sp.Integer(N) ** 2 + sum((1 / sp.Integer(n) ** 2 - 1 / sp.Integer(N) ** 2) * Sv[n] for n in Sv if n < N)


for N in odd:
    d = sp.expand(B(N, Ssym, Stot) - M2s)
    ok(sp.expand(d - sum((1 / sp.Integer(N) ** 2 - 1 / sp.Integer(n) ** 2) * Ssym[n] for n in odd if n >= N)) == 0,
       'B_N - M2 identity N=%d' % N)
    # every coefficient of d is nonnegative and at most 1/N^2: 0 <= B_N - M2 <= S/N^2
    co = [d.coeff(Ssym[n]) for n in odd]
    ok(all(0 <= c_ <= sp.Rational(1, N ** 2) for c_ in co), 'bound (3) coefficientwise N=%d' % N)
    if N + 2 <= odd[-1]:
        dd = sp.expand(B(N + 2, Ssym, Stot) - B(N, Ssym, Stot))
        ok(sp.expand(dd - (sp.Rational(1, (N + 2) ** 2) - sp.Rational(1, N ** 2)) *
                     (Stot - sum(Ssym[n] for n in odd if n <= N))) == 0, 'B_(N+2) - B_N identity N=%d' % N)
        # N4-403 (1) with last included mode N and m = N + 2 equals T4-474 B_(N+2)
        n403 = sum(Ssym[n] / sp.Integer(n) ** 2 for n in odd if n <= N) + \
            (Stot - sum(Ssym[n] for n in odd if n <= N)) / sp.Integer(N + 2) ** 2
        ok(sp.expand(n403 - B(N + 2, Ssym, Stot)) == 0, 'N4-403 (1) = T4-474 B_(N+2), N=%d' % N)


def Bq(N, Sv, St):
    return St / Fr(N * N) + sum((Fr(1, n * n) - Fr(1, N * N)) * Sv[n] for n in Sv if n < N)


P = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'T4474_parameters.json')))
random.seed(474)
lists = [{int(k): Fr(v) for k, v in fx['energies'].items()} for fx in P['fixtures']]
for _ in range(200):
    K = random.choice([3, 5, 8, 12])
    lists.append({2 * i + 1: Fr(random.randint(0, 50), random.randint(1, 30)) for i in range(K)})
for Sv in lists:
    St = sum(Sv.values())
    M2 = sum(v / (n * n) for n, v in Sv.items())
    top = max(Sv) + 2
    prev = None
    for N in range(1, top + 1, 2):
        b = Bq(N, Sv, St)
        ok(M2 <= b and b - M2 <= St / (N * N), '(2), (3) on a list')
        if prev is not None:
            ok(b <= prev, 'monotone in N')
        prev = b
        # outward (4) with upper data U >= S, U_n >= S_n, and N4-403's split formula with lower data L_n <= S_n
        U = St + Fr(1, 97)
        Un = {n: v + Fr(1, 89) for n, v in Sv.items()}
        Ln = {n: max(v - Fr(1, 83), Fr(0)) for n, v in Sv.items()}
        pos = U / (N * N) + sum((Fr(1, n * n) - Fr(1, N * N)) * Un[n] for n in Sv if n < N)
        split = sum(Un[n] / (n * n) for n in Sv if n < N) + (U - sum(Ln[n] for n in Sv if n < N)) / (N * N)
        ok(b <= pos <= split and split - pos == sum(Un[n] - Ln[n] for n in Sv if n < N) / (N * N),
           'outward formulas and their difference')
    ok(prev == M2, 'B_N = M2 once every nonzero mode is below N')
# omission counterexamples: (i) dropping the tail term; (ii) leaving a lower mode out of the prefix
hi = {1: Fr(0), 3: Fr(0), 5: Fr(1)}
ok(sum(hi[n] / (n * n) for n in (1, 3)) < sum(v / (n * n) for n, v in hi.items()), 'tail cannot be replaced by zero')
mx = lists[2]
St = sum(mx.values())
wrong = St / 49 + sum((Fr(1, n * n) - Fr(1, 49)) * mx[n] for n in (3, 5))     # mode 1 omitted from the prefix
ok(wrong < sum(v / (n * n) for n, v in mx.items()), 'an omitted lower mode breaks the bound')
# known solution: S_1 = 3/4, S_3 = 64/35 (units of pi), a_1 = 3/8, a_3 = 2/63, H^2 = 153/280
ks = {1: Fr(3, 4), 3: Fr(64, 35)}
b3 = Bq(3, ks, sum(ks.values()))
ok(b3 == Fr(1201, 1260) == sum(v / (n * n) for n, v in ks.items()), 'B_3 = M2 = 1201/1260')
ok(b3 - Fr(3, 8) - Fr(2, 63) == Fr(153, 280), 'B_3 - a_1 - a_3 = H^2 = 153/280')
ok(Bq(1, ks, sum(ks.values())) == Fr(3, 4) + Fr(64, 35) and Bq(1, ks, sum(ks.values())) > b3, 'B_1 = S (plain Hardy)')
print('Part B: prefix lemma symbolic for modes 1..23, N4-403 (1) = T4-474 B_(N+2), outward formulas,',
      len(lists), 'lists, omission counterexamples, known solution;', n_ok, 'checks')

# ---- Part C: candidate 016
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
HASH = {'N4403_result_v01.json': '8a6bc15f52acec01664df0e69f47888f6bd422dad3b954962978450d1e59bea1',
        'T4474_parameters.json': '659210cd3824e5367dd5eea0d8b8a649c8242a78cebc415f6d8301dc8040ed05',
        'N4392_comparison.json': 'a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc',
        'N4396_result.json': 'e91c096d6ccb1cb0f9e08e63ae53a2c258875cad720c5ab483b875bfb4a4dffa',
        'N4398_result.json': 'e97891e271837201e3f4a0d18f96732825238604cbad65fc8b31923e36463603',
        'N3_016_hdual_m13deep.json': 'a32a02e71da636635e3b1d6c3289d5dc478bd8a63cda07f06f8cae98e9a968e5'}
J = {}
for fn, h in HASH.items():
    raw = open(os.path.join(D, fn), 'rb').read()
    ok(hashlib.sha256(raw).hexdigest() == h, 'hash ' + fn)
    J[fn] = json.loads(raw)
R = J['N4403_result_v01.json']
NRM = J['N4392_comparison.json']['norms']
RAW = 'a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
ok(R['raw_sha256'] == J['N4392_comparison.json']['raw_sha256'] == J['N4396_result.json']['raw_sha256'] ==
   J['N4398_result.json']['raw_sha256'] == J['N3_016_hdual_m13deep.json']['source_sha256'] == RAW, 'one 016 raw file')
ok(R['complete_field_mode_count'] == 160 and int(R['prefix']) == 7 and int(R['smallest_omitted_mode']) == 9,
   '160 odd modes 1..319, prefix 7, first omitted 9')
ok([int(m['n']) for m in R['modes']] == [1, 3, 5, 7], 'prefix modes 1, 3, 5, 7')
q = {int(m['n']): (Fr(m['q_lower_exact']), Fr(m['q_upper_exact'])) for m in R['modes']}
ok(all(0 < lo <= hi_ for lo, hi_ in q.values()), 'positive mode intervals')
rFu = Fr(NRM['rF']['accepted_upper_exact'])
rFl = Fr(NRM['rF']['accepted_lower_exact'])
RL, RU = Fr(R['full_rF_square_lower_exact']), Fr(R['full_rF_square_upper_exact'])
ok(rFu == Fr(P['rF_upper']), 'T4-474 rF upper = N4-392 accepted upper')
ok(RU == rFu ** 2 and RL == rFl ** 2 and RL > 0, 'R2 endpoints are the squares of the accepted rF endpoints')
QL = sum(lo for lo, hi_ in q.values())
ok(RL - sum(hi_ for lo, hi_ in q.values()) > 0, 'tail energy positive: R2 lower exceeds Q_7 upper')
ok(Fr(R['tail_rF_square_lower_exact']) == RL - sum(hi_ for lo, hi_ in q.values()) and
   Fr(R['tail_rF_square_upper_exact']) == RU - QL, 'tail endpoints equal R2 - Q_7 outward')
m = 9
pos = RU / (m * m) + sum((Fr(1, n * n) - Fr(1, m * m)) * hi_ for n, (lo, hi_) in q.items())
split = sum(hi_ / (n * n) for n, (lo, hi_) in q.items()) + (RU - QL) / (m * m)
ok(pos == Fr(R['positive_coefficient_formula_upper_exact']) == Fr(R['M2_upper_exact']), 'positive-coefficient M2 upper')
ok(split == Fr(R['split_formula_upper_exact']) and split - pos == sum(h - l for l, h in q.values()) / 81, 'split formula')
ok(pos < Fr(1129996, 10 ** 6), 'M2 < 1.129996')
M2lo = sum(lo / (n * n) for n, (lo, hi_) in q.items())
ok(M2lo == Fr(R['M2_lower_exact']), 'M2 lower (prefix only)')
Hp = Fr(R['plain_H_strict_upper_exact'])
ok(Hp * Hp > pos and Hp < Fr(1063013, 10 ** 6), 'plain H < 1.063013')
imp = Fr(J['N4398_result.json']['improvement_sum_strict_lower_exact'])
ok(imp == Fr(R['selected_improvement_sum_lower_exact']) == Fr(P['cross_improvement_lower']), 'N4-398 sum floor')
Hi2 = pos - imp
ok(Hi2 == Fr(R['improved_H_square_upper_exact']), 'improved H^2 upper = M2 upper - sum floor')
Hi = Fr(R['conditional_improved_H_strict_upper_exact'])
ok(Hi * Hi > Hi2 and Hi < Fr(944107, 10 ** 6), 'improved H < 0.944107')
Hl = Fr(J['N4396_result.json']['H_strict_lower_exact'])
ok(Hl * Hl < Hi2 and Fr(R['H_strict_lower_exact']) >= Hl, 'two-sided: H lower square below improved upper')
up = {k: Fr(NRM[k]['accepted_upper_exact']) for k in ('G0', 'G1', 'P2')}
E2u2 = up['P2'] ** 2 + 2 ** 14 * up['G1'] ** 2 + 2 ** 18 * up['G0'] ** 2 + Fr(20, 21) * 2 ** 18 * Hi2
ok(E2u2 == Fr(R['conditional_E2_upper_square_exact']), 'E2^2 upper from the N4-392 uppers and the improved H^2 upper')
E2u = Fr(R['conditional_E2_strict_upper_exact'])
ok(E2u * E2u > E2u2 and E2u < Fr(722968760, 10 ** 6), 'E2 < 722.968760')
E2noimp = up['P2'] ** 2 + 2 ** 14 * up['G1'] ** 2 + 2 ** 18 * up['G0'] ** 2 + Fr(20, 21) * 2 ** 18 * pos
# T4-474 loss bounds S/N^2 with S < rF upper squared
loss = {N: rFu ** 2 / (N * N) for N in P['odd_cuts']}
ok(loss[33] < Fr(P['tail_loss_upper_N33']), 'T4-474: loss for N = 33 below 47/1000')
print('Part C: R2 in [%s, %s], Q_7 lower %s, tail (R2 - Q_7) <= %s; M2 <= %s (split <= %s)'
      % (dec_dn(RL, 15), dec_up(RU, 15), dec_dn(QL, 12), dec_up(RU - QL, 12), dec_up(pos, 9), dec_up(split, 9)))
print('  plain H <= %s < 1.063013; improved H^2 <= %s, H <= %s < 0.944107; E2 <= %s (without the'
      ' improvement E2 <= %s); H lower %s' % (sqrt_up(pos, 9), dec_up(Hi2, 9), sqrt_up(Hi2, 9), sqrt_up(E2u2, 6),
                                              sqrt_up(E2noimp, 6), dec_dn(Hl, 9)))
print('  modes 1, 3, 5, 7: Q_7 upper / R2 lower = %.7f (FLOAT ratio of exact numbers)'
      % float(sum(hi_ for lo, hi_ in q.values()) / RL))
print('  T4-474 loss bounds S/N^2 (rounded up):', ', '.join('N=%d %s' % (N, dec_up(v, 6)) for N, v in loss.items()))

# ---- Part D (CONDITIONAL on c1-n3's displays)
flint.ctx.prec = 600
N3 = J['N3_016_hdual_m13deep.json']
for M in N3['modes']:
    n = int(M['n'])
    h = flint.arb(M['H_n_UB_hardy'])
    qq = h * h * n * n
    lo, hi_ = q[n]
    Lb, Hb = flint.arb(flint.fmpq(lo.numerator, lo.denominator)), flint.arb(flint.fmpq(hi_.numerator, hi_.denominator))
    ok(qq.contains(Lb) and qq.contains(Hb) and qq.rad() < flint.arb(10) ** -29,
       'the c1-n3 30-digit ball for q_%d contains both N4-403 endpoints' % n)
    w = hi_ - lo
    kw = len(str(w.denominator // w.numerator)) - 1 if w > 0 else None     # w < 10^-kw
    print('Part D: n=%d, c1-n3 n^2 H_n^2 = %s (radius %s) contains N4-403 q_n in [%s, %s] (width below 1e-%s)'
          % (n, qq.str(32, radius=False), qq.rad().str(3, radius=False), Lb.str(32, radius=False),
             Hb.str(32, radius=False), kw))
Hup = float(N3['H_upper_hardy'].lstrip('[').split()[0][:22])
pre = float(M2lo)
print('  FLOAT, CONDITIONAL on the c1-n3 complete Hardy display sqrt(M2) = %.12f: true tail sum_(n>=9) q_n/n^2 about'
      ' %.6f, bound (R2 - Q_7)/81 <= %s (ratio about %.2f); M2 display minus the N4-398 floor gives H about %.6f'
      % (Hup, Hup ** 2 - pre, dec_up((RU - QL) / 81, 6), float((RU - QL) / 81) / (Hup ** 2 - pre),
         (Hup ** 2 - float(imp)) ** 0.5))
print('checks passed', n_ok, '; elapsed %.1f s' % (time.time() - t0))
print('RESULT PASS')
