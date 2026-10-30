# R1-051 (REVIEWS_v48): exact recomposition of c1-n4's N4-409 (candidate016_angular_tail_bound/verification/
# result_v02.json, prefix 1, 3, ..., 31) and N4-410 (candidate016_reviewed_upper, PROOF sha256 bf8cb48f...50f37ed2) from
# their saved exact endpoints, with the tail formula reviewed in R1-050 (T4-474 at N = 33). No c1-n4, c1-t4 or c1-n3
# code is run; the saved numbers are read and recomposed in exact Fractions.
# Part A: hashes, binding and mode coverage (16 odd modes 1..31 of 160, first omitted 33); comparison of the modes
#   1, 3, 5, 7 with N4-403's endpoints.
# Part B: N4-409, exact: R2 endpoints = squares of the accepted N4-392 rF endpoints; tail endpoints; positive-coefficient
#   and split formulas at m = 33; plain H upper; improvement floors; improved H^2 and E2^2 uppers; strict displays.
# Part C: N4-410, exact: the complete M2 upper, both H squares, both E2 squares, strict displays, the 007 gap, and the
#   relation of its H lower square to N4-396's.
# Part D: comparisons: N4-409 against N4-403 (both outward uppers), the loss bound U^2/33^2, H(016) upper against N4-252's
#   H(007) lower ball (Arb); CONDITIONAL on c1-n3's 30-digit mode Hardy displays: their q_1, q_3 balls against the
#   N4-409 endpoints; FLOAT: c1-n3's complete Hardy display and its CLAIMED H(016) bracket against the enclosure.
# Usage: python3 check_N4409.py (from artifacts/checks). Inputs in data/: N4409_result_v02.json, N4410_result.json,
#   N4410_parameters.json (copies of c1-n4 research/candidate016_angular_tail_bound/verification/result_v02.json and
#   research/candidate016_reviewed_upper/{verification/result.json, source/parameters.json}), N4403_result_v01.json,
#   N4392_comparison.json, N4396_result.json, N4398_result.json, N4252_result.json, N3_016_hdual_m13deep.json; sha256
#   checked.
import hashlib, json, os, sys, time
from fractions import Fraction as Fr
from math import isqrt
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
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
HASH = {'N4409_result_v02.json': '01019cd56639661ace672791a4fbe7f938d90bf02237b93b38f061238bb15b41',
        'N4410_result.json': 'd50ef2bb8868b2eb505933a488e91df979146c269b5b788dad928dfcab7bb7d0',
        'N4410_parameters.json': 'a65ce341175cfaf85d5959a398d38ddd908f66bb233b43f1cb8a654840e3053d',
        'N4403_result_v01.json': '8a6bc15f52acec01664df0e69f47888f6bd422dad3b954962978450d1e59bea1',
        'N4392_comparison.json': 'a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc',
        'N4396_result.json': 'e91c096d6ccb1cb0f9e08e63ae53a2c258875cad720c5ab483b875bfb4a4dffa',
        'N4398_result.json': 'e97891e271837201e3f4a0d18f96732825238604cbad65fc8b31923e36463603',
        'N4252_result.json': 'd94473eb11c0708e25a9529f00b49576628023066e626ed9170bf29b62e22e7c',
        'N3_016_hdual_m13deep.json': 'a32a02e71da636635e3b1d6c3289d5dc478bd8a63cda07f06f8cae98e9a968e5'}
J = {}
for fn, h in HASH.items():
    raw = open(os.path.join(D, fn), 'rb').read()
    ok(hashlib.sha256(raw).hexdigest() == h, 'hash ' + fn)
    J[fn] = json.loads(raw)
R9, R10, P10 = J['N4409_result_v02.json'], J['N4410_result.json'], J['N4410_parameters.json']
R3 = J['N4403_result_v01.json']
NRM = J['N4392_comparison.json']['norms']
RAW = 'a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
ok(R9['raw_sha256'] == R10['raw_sha256'] == P10['raw_sha256'] == R3['raw_sha256'] == RAW, 'one 016 raw file')
ok(R9['candidate'] == R10['candidate'] == 'C1-N1-016-legqs25-quot013', 'candidate id')
ok(P10['dependencies']['research/candidate016_angular_tail_bound/verification/result_v02.json'] == HASH['N4409_result_v02.json'],
   'N4-410 binds this N4-409 result')
for k, fn in (('research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json', 'N4392_comparison.json'),
              ('research/candidate016_dual_lower/verification/result.json', 'N4396_result.json'),
              ('research/candidate016_solenoidal_upper/verification/result.json', 'N4398_result.json')):
    ok(P10['dependencies'][k] == HASH[fn], 'N4-410 binds ' + fn)

# ---- Part A: coverage
ok(R9['complete_field_mode_count'] == 160 and int(R9['prefix']) == 31 and int(R9['smallest_omitted_mode']) == 33,
   '160 odd modes, prefix 31, first omitted 33')
ok([int(m['n']) for m in R9['modes']] == list(range(1, 32, 2)) and int(R9['mode_count_replayed']) == 16,
   'prefix modes 1, 3, ..., 31')
ok(R9['complete_uncomputed_tail_retained'] is True and R9['all160_individual_mode_integrals_replayed'] is False,
   'tail retained, only 16 modes integrated')
q = {int(m['n']): (Fr(m['q_lower_exact']), Fr(m['q_upper_exact'])) for m in R9['modes']}
ok(all(0 < lo <= hi for lo, hi in q.values()), 'positive mode intervals')
q3 = {int(m['n']): (Fr(m['q_lower_exact']), Fr(m['q_upper_exact'])) for m in R3['modes']}
same = all(q3[n] == q[n] for n in q3)
ok(all(max(q3[n][0], q[n][0]) <= min(q3[n][1], q[n][1]) for n in q3), 'modes 1..7 intervals of N4-403 and N4-409 intersect')
print('Part A: 16 modes 1..31 of 160, first omitted 33; modes 1, 3, 5, 7 identical to N4-403:', same, ';', n_ok, 'checks')

# ---- Part B: N4-409
rFu, rFl = Fr(NRM['rF']['accepted_upper_exact']), Fr(NRM['rF']['accepted_lower_exact'])
RL, RU = Fr(R9['full_rF_square_lower_exact']), Fr(R9['full_rF_square_upper_exact'])
ok(RU == rFu ** 2 and RL == rFl ** 2, 'R2 endpoints are the squares of the accepted rF endpoints')
QL, QU = sum(lo for lo, hi in q.values()), sum(hi for lo, hi in q.values())
ok(RL - QU > 0 and Fr(R9['tail_rF_square_lower_exact']) == RL - QU and Fr(R9['tail_rF_square_upper_exact']) == RU - QL,
   'tail endpoints R2 - Q_31 outward, tail lower positive')
m = 33
pos = RU / (m * m) + sum((Fr(1, n * n) - Fr(1, m * m)) * hi for n, (lo, hi) in q.items())
split = sum(hi / (n * n) for n, (lo, hi) in q.items()) + (RU - QL) / (m * m)
ok(pos == Fr(R9['positive_coefficient_formula_upper_exact']) == Fr(R9['M2_upper_exact']), 'positive-coefficient M2 upper (selected)')
ok(split == Fr(R9['split_formula_upper_exact']) and split - pos == (QU - QL) / (m * m) and split > pos, 'split formula larger')
M2lo = sum(lo / (n * n) for n, (lo, hi) in q.items())
ok(M2lo == Fr(R9['M2_lower_exact']), 'M2 lower (prefix only)')
flint.ctx.prec = 2400
fq = lambda z: flint.arb(flint.fmpq(z.numerator, z.denominator))
for key, a, b in (('Q_prefix_ball', QL, QU), ('S_prefix_ball', M2lo, sum(hi / (n * n) for n, (lo, hi) in q.items()))):
    ok(flint.arb(R9[key]).contains(fq(a)) and flint.arb(R9[key]).contains(fq(b)), key + ' contains both exact prefix sums')


def below(z):
    # k with 0 < z < 10^-k (decimal order of a tiny positive Fraction)
    return len(str(z.denominator // z.numerator)) - 1


wmax = max(hi - lo for lo, hi in q.values())
ok(wmax > 0, 'mode intervals have positive width')
Hp = Fr(R9['plain_H_strict_upper_exact'])
ok(Hp * Hp > pos and Hp < Fr(789068, 10 ** 6), 'plain H < 0.789068')
ok([int(x) for x in R9['selected_improvement_modes']] == [1, 3], 'improvements: the distinct modes 1 and 3')
imp = Fr(J['N4398_result.json']['improvement_sum_strict_lower_exact'])
ok(imp == Fr(R9['selected_improvement_sum_lower_exact']), 'N4-398 sum floor')
Hi2 = pos - imp
ok(Hi2 > 0 and Hi2 == Fr(R9['improved_H_square_upper_exact']), 'improved H^2 upper = M2 upper - floor')
Hi = Fr(R9['conditional_improved_H_strict_upper_exact'])
ok(Hi * Hi > Hi2 and Hi < Fr(619652, 10 ** 6), 'improved H < 0.619652')
up = {k: Fr(NRM[k]['accepted_upper_exact']) for k in ('G0', 'G1', 'P2')}
lo4 = {k: Fr(NRM[k]['accepted_lower_exact']) for k in ('G0', 'G1', 'P2')}


def e2sq(c, h2):
    return c['P2'] ** 2 + 2 ** 14 * c['G1'] ** 2 + 2 ** 18 * c['G0'] ** 2 + Fr(20, 21) * 2 ** 18 * h2


E2u2 = e2sq(up, Hi2)
ok(E2u2 == Fr(R9['conditional_E2_upper_square_exact']), 'E2^2 upper from the N4-392 uppers')
E2u = Fr(R9['conditional_E2_strict_upper_exact'])
ok(E2u * E2u > E2u2 and E2u < Fr(629296113, 10 ** 6), 'E2 < 629.296113')
E2plain = e2sq(up, pos)
print('Part B: N4-409: mode interval widths below 1e-%d; M2 <= %s (split larger by less than 1e-%d), plain'
      ' H <= %s < 0.789068; improved H^2 <= %s, H <= %s < 0.619652; E2 <= %s < 629.296113 (without the'
      ' improvement E2 <= %s); %d checks' % (below(wmax), dec_up(pos, 12), below(split - pos), sqrt_up(pos, 9),
                                              dec_up(Hi2, 12), sqrt_up(Hi2, 9), sqrt_up(E2u2, 9), sqrt_up(E2plain, 6),
                                              n_ok))

# ---- Part C: N4-410
ok(Fr(R10['complete_M2_upper_exact']) == pos, 'N4-410 complete M2 upper = N4-409 positive-coefficient upper')
ok(Fr(R10['H_upper_square_exact']) == Hi2, 'N4-410 H^2 upper = M2 upper - N4-398 floor')
ok(Fr(R10['E2_upper_square_exact']) == E2u2, 'N4-410 E2^2 upper')
Hs = Fr(R10['H_strict_upper_exact'])
ok(Hs == Fr(619651337324093367770781451079, 10 ** 30) and Hs * Hs > Hi2 and Hs < Fr(619652, 10 ** 6),
   'H < 0.619651337324093367770781451079 < 0.619652')
Es = Fr(R10['E2_strict_upper_exact'])
ok(Es == Fr(314648056081457, 500000000000) and Es * Es > E2u2 and Es < Fr(629296113, 10 ** 6),
   'E2 < 629.296112162914 < 629.296113')
HL2 = Fr(R10['H_lower_square_exact'])
HL2_396 = Fr(J['N4396_result.json']['H_lower_square_exact'])
ok(HL2 == HL2_396 and HL2 < Hi2, 'N4-410 H lower square = N4-396 lower square, below the upper square')
HLs = Fr(R10['H_strict_lower_exact'])
ok(HLs * HLs < HL2 and HLs > Fr(529469576110, 10 ** 12), 'strict H lower > 0.529469576110')
E2l2 = e2sq(lo4, HL2)
ok(E2l2 == Fr(R10['E2_lower_square_exact']), 'N4-410 E2^2 lower from the N4-392 lowers and its H lower square')
ELs = Fr(R10['E2_strict_lower_exact'])
ok(ELs == Fr(304196192960807, 500000000000) and ELs * ELs < E2l2, 'E2 > 608.392385921614')
U7 = Fr(J['N4252_result.json']['E_upper']['strict_upper_exact'])
ok(U7 == Fr(606820219, 10 ** 6) and ELs - U7 == Fr(786083460807, 500000000000), 'E2(016) - E2(007) > 1.572166921614')
sd = R10['strict_display_bounds']
ok(sd['H_upper'] == P10['H_upper'] == '0.619652' and sd['E2_upper'] == P10['E2_upper'] == '629.296113' and
   sd['gap_lower'] == '1.572166921614', 'displays agree with the parameters')
ok(Fr(dec_dn(ELs, 12)) == ELs and Fr(dec_up(Es, 12)) == Es, 'the two strict E2 bounds are 12-digit decimals')
print('Part C: N4-410: H^2 in [%s, %s], E2 in (%s, %s); H lower square equal to N4-396 (not recomputed'
      ' here); %d checks' % (dec_dn(HL2, 15), dec_up(Hi2, 15), dec_dn(ELs, 12), dec_up(Es, 12), n_ok))

# ---- Part D
pos3 = Fr(R3['M2_upper_exact'])
ok(pos < pos3, 'N4-409 M2 upper below N4-403 M2 upper')
ok(pos - M2lo <= RU / (m * m) and RU / (m * m) < Fr(47, 1000), 'width of the M2 enclosure below U^2/33^2 < 47/1000')
flint.ctx.prec = 600
H7lo = flint.arb(J['N4252_result.json']['H_input_lower_ball'])
ok(flint.arb(flint.fmpq(Hs.numerator, Hs.denominator)) < H7lo, 'H(016) upper below the N4-252 H(007) lower ball')
print('Part D: N4-409 M2 upper %s below N4-403 M2 upper %s; M2 enclosure width <= %s <= U^2/33^2 <= %s;'
      ' H(016) < %s, below the N4-252 H(007) lower ball (about %s)'
      % (dec_up(pos, 12), dec_up(pos3, 12), dec_up(pos - M2lo, 6), dec_up(RU / (m * m), 6), dec_up(Hs, 9),
         H7lo.lower().str(12, radius=False)))
N3 = J['N3_016_hdual_m13deep.json']
for M in N3['modes']:
    n = int(M['n'])
    qq = flint.arb(M['H_n_UB_hardy']) ** 2 * n * n
    lo, hi = q[n]
    ok(qq.contains(flint.arb(flint.fmpq(lo.numerator, lo.denominator))) and
       qq.contains(flint.arb(flint.fmpq(hi.numerator, hi.denominator))),
       'CONDITIONAL: c1-n3 q_%d ball contains the N4-409 endpoints' % n)
Hup = float(N3['H_upper_hardy'].lstrip('[').split()[0][:22])
share = float(QU / RL)
print('  CONDITIONAL on c1-n3 displays: q_1 and q_3 balls contain the N4-409 endpoints. FLOAT: modes 1..31 carry at most'
      ' %.7f of R2; c1-n3 complete Hardy display sqrt(M2) = %.12f vs N4-409 upper %s (true tail beyond 31 about'
      ' %.3e, bound (R2 - Q_31)/33^2 <= %s)' % (share, Hup, sqrt_up(pos, 9), Hup ** 2 - float(M2lo),
                                                 dec_up((RU - QL) / (m * m), 6)))
ok(Hup ** 2 < float(pos) and Hup ** 2 > float(M2lo), 'FLOAT: c1-n3 display inside the N4-409 M2 enclosure')
n3c = (0.6167335007, 0.6189603636)
ok(n3c[0] > float(HLs) and n3c[1] < float(Hs), 'FLOAT: c1-n3 CLAIMED H(016) bracket inside the N4-410 enclosure')
print('  FLOAT: c1-n3 CLAIMED H(016) in [%.10f, %.10f] lies inside (%s, %s); margin to the upper about %.2e'
      % (n3c[0], n3c[1], dec_dn(HLs, 9), dec_up(Hs, 9), float(Hs) - n3c[1]))
print('checks passed', n_ok, '; elapsed %.1f s' % (time.time() - t0))
print('RESULT PASS')
