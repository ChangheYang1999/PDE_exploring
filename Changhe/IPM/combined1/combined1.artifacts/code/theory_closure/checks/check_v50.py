# REVIEWS_v50 (c1-t1): exact checks for erratum E11 to R1-051 V7 (REVIEWS_v48) and for the radius values of N4-415 used
# in THEORY_FINAL draft 55, section 2.1. No c1-n4 or c1-t4 code is run; saved numbers are read as data.
# Part A: from N4-409's saved exact endpoints (data/N4409_result_v02.json) and the N4-392 accepted rF endpoints, the
#   share of R2 = ||rF||^2 carried by the integrated modes 1, 3, ..., 31. Every ratio of a prefix endpoint to an R2
#   endpoint lies strictly between 0.988805 and 0.988806, so "at most 0.9888" (R1-051 V7) is false and 0.988806 is a
#   rigorous upper.
# Part B: sharpw threshold at s = 1/5184: mu = 201799/648000, A = 576/5, beta(r) = mu - A r. At the selected radius
#   r = 1351/10^6: beta(r) >= 1557/10000 (the tabulated rate), the tabulated threshold 4207/(2 10^7) <= (1557/10000) r,
#   and the exact beta(r) r = 85237452769/405000000000000 > 2.1046e-4 (N4-415); the supremum eta* = mu^2/(4A) at
#   r* = mu/(2A) = 201799/149299200 exceeds beta(r) r by eta* - beta(r) r = A (r - r*)^2.
# Usage: python3 check_v50.py (from artifacts/checks).
import hashlib, json, os
from fractions import Fraction as Fr

n_ok = 0


def ok(cond, msg):
    global n_ok
    assert cond, msg
    n_ok += 1


def dec_up(z, k):
    j = -((-z.numerator * 10 ** k) // z.denominator)
    return '%d.%0*d' % (j // 10 ** k, k, j % 10 ** k)


def dec_dn(z, k):
    j = (z.numerator * 10 ** k) // z.denominator
    return '%d.%0*d' % (j // 10 ** k, k, j % 10 ** k)


D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
HASH = {'N4409_result_v02.json': '01019cd56639661ace672791a4fbe7f938d90bf02237b93b38f061238bb15b41',
        'N4392_comparison.json': 'a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc'}
J = {}
for fn, h in HASH.items():
    raw = open(os.path.join(D, fn), 'rb').read()
    ok(hashlib.sha256(raw).hexdigest() == h, 'hash ' + fn)
    J[fn] = json.loads(raw)
R9, NRM = J['N4409_result_v02.json'], J['N4392_comparison.json']['norms']

# ---- Part A
q = [(Fr(m['q_lower_exact']), Fr(m['q_upper_exact'])) for m in R9['modes']]
ok([int(m['n']) for m in R9['modes']] == list(range(1, 32, 2)), 'modes 1, 3, ..., 31')
QL, QU = sum(a for a, b in q), sum(b for a, b in q)
RL, RU = Fr(R9['full_rF_square_lower_exact']), Fr(R9['full_rF_square_upper_exact'])
ok(RL == Fr(NRM['rF']['accepted_lower_exact']) ** 2 and RU == Fr(NRM['rF']['accepted_upper_exact']) ** 2,
   'R2 endpoints are the squares of the accepted rF endpoints')
lo_b, hi_b = Fr(988805, 10 ** 6), Fr(988806, 10 ** 6)
ratios = {'Q_L/R_U': QL / RU, 'Q_L/R_L': QL / RL, 'Q_U/R_U': QU / RU, 'Q_U/R_L': QU / RL}
for k, z in ratios.items():
    ok(lo_b < z < hi_b, k + ' in (0.988805, 0.988806)')
    ok(z > Fr(9888, 10 ** 4), k + ' > 0.9888')
lo_s, hi_s = QL / RU, QU / RL
ok(lo_s == min(ratios.values()) and hi_s == max(ratios.values()), 'outward share interval [Q_L/R_U, Q_U/R_L]')
print('Part A: modes 1..31 carry a share of R2 in [%s, %s] (outward, from exact endpoints), inside (0.988805, 0.988806);'
      ' every endpoint ratio exceeds 0.9888; %d checks' % (dec_dn(lo_s, 12), dec_up(hi_s, 12), n_ok))

# ---- Part B
mu, A = Fr(97, 250) - 397 * Fr(1, 5184), Fr(8, 5) * 72
ok(mu == Fr(201799, 648000) and A == Fr(576, 5), 'mu = 97/250 - 397/5184 = 201799/648000, A = (8/5)/sqrt(1/5184)')
r = Fr(1351, 10 ** 6)
beta = mu - A * r
ok(beta == Fr(63092119, 405000000) and beta >= Fr(1557, 10000), 'beta(1351/10^6) = 63092119/405000000 >= 1557/10000')
ok(Fr(1557, 10000) * r == Fr(2103507, 10 ** 10) and Fr(4207, 2 * 10 ** 7) <= Fr(1557, 10000) * r,
   'tabulated threshold 2.1035e-4 <= (1557/10000) r = 2.103507e-4')
v = beta * r
ok(v == Fr(85237452769, 405000000000000) and v > Fr(21046, 10 ** 8), 'beta(r) r = 85237452769/405000000000000 > 2.1046e-4')
rs, es = mu / (2 * A), mu * mu / (4 * A)
ok(rs == Fr(201799, 149299200) and es == Fr(40722836401, 193491763200000), 'r* and eta*')
ok(es - v == A * (r - rs) ** 2 and es - v > 0, 'eta* - beta(r) r = A (r - r*)^2 > 0')
ok(Fr(21046, 10 ** 8) < es < Fr(21047, 10 ** 8), '2.1046e-4 < eta* < 2.1047e-4')
print('Part B: at r = 1351/10^6, beta = 63092119/405000000 (>= %s, tabulated 0.1557), beta r = %s (in [%s, %s]);'
      ' eta* - beta r = A (r - r*)^2 = %s (about %.3e); tabulated 4207/(2 10^7) / (beta r) <= %s; %d checks'
      % (dec_dn(beta, 9), v, dec_dn(v, 13), dec_up(v, 13), es - v, float(es - v), dec_up(Fr(4207, 2 * 10 ** 7) / v, 9),
         n_ok))
print('RESULT PASS')
