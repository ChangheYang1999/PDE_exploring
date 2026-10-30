# R1-052 (REVIEWS_v51): exact recomposition of c1-n4's N4-417 (candidate016_angular_tail_bound/verification/
# result_v03.json, prefix 1, 3, ..., 31 with all 16 corrected modes) and N4-418 (candidate016_multimode_complete_bounds,
# PROOF sha256 967c25cd...0dac568) from their saved exact endpoints. No c1-n4, c1-t4 or c1-n3 code is run; the saved
# numbers are read and recomposed in exact Fractions. The 2130 group intervals behind the 16 dual and solenoidal floors
# (N4-416, replayed in T4-486) are not recomputed.
# Part A: hashes, binding and coverage; the 16 prefix intervals and R2 endpoints of result_v03 equal those of
#   result_v02 (R1-051), so the complete M2 upper is unchanged.
# Part B: L2 = sum L_n^2 and J = sum J_n from the 16 selected floors; U2 = M2 upper - J; per-mode consistency
#   L_n^2 < U_n/n^2 - J_n; the width of [L2, U2] split into the 16 modes and the tail term (R_U - Q_U)/33^2.
# Part C: strict H and E2 endpoints by exact squaring, E2 from the N4-392 component bounds, the gaps over 007 (N4-252),
#   the c1-n4 and T4-486 displays.
# Part D: comparison with N4-410 (nested), with N4-398's two-mode floor, and FLOAT positions of c1-n3's CLAIMED values
#   (matrix v154 rows near lines 1994 and 2217). Since REVIEWS_v52 (erratum E13, T4-493) the distance of c1-n3's H lower
#   0.6167335007 below HL is checked and printed as an exact interval, not as a rounded FLOAT.
# Usage: python3 check_N4418.py (from artifacts/checks). Inputs in data/: N4418_result_v01.json, N4417_result_v03.json
#   (copies of c1-n4 research/candidate016_multimode_complete_bounds/verification/result_v01.json and
#   research/candidate016_angular_tail_bound/verification/result_v03.json), N4409_result_v02.json, N4410_result.json,
#   N4392_comparison.json, N4398_result.json, N4252_result.json; sha256 checked.
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
HASH = {'N4418_result_v01.json': '8eec600612f7719a1c0cbcb408d1665659b8d2c06d861f032a102651953c3728',
        'N4417_result_v03.json': '285dac39d93e32574c214d00cef9764087c0718c19b4042398c7ec728b530840',
        'N4409_result_v02.json': '01019cd56639661ace672791a4fbe7f938d90bf02237b93b38f061238bb15b41',
        'N4410_result.json': 'd50ef2bb8868b2eb505933a488e91df979146c269b5b788dad928dfcab7bb7d0',
        'N4392_comparison.json': 'a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc',
        'N4398_result.json': 'e97891e271837201e3f4a0d18f96732825238604cbad65fc8b31923e36463603',
        'N4252_result.json': 'd94473eb11c0708e25a9529f00b49576628023066e626ed9170bf29b62e22e7c'}
J = {}
for fn, h in HASH.items():
    raw = open(os.path.join(D, fn), 'rb').read()
    ok(hashlib.sha256(raw).hexdigest() == h, 'hash ' + fn)
    J[fn] = json.loads(raw)
R18, R17, R9, R10 = J['N4418_result_v01.json'], J['N4417_result_v03.json'], J['N4409_result_v02.json'], J['N4410_result.json']
NRM = J['N4392_comparison.json']['norms']
RAW = 'a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
ok(R18['raw_sha256'] == R17['raw_sha256'] == R9['raw_sha256'] == R10['raw_sha256'] == RAW, 'one 016 raw file')
ok(R18['candidate'] == R17['candidate'] == 'C1-N1-016-legqs25-quot013', 'candidate id')
IN = R18['inputs']
for k, fn in (('research/candidate016_angular_tail_bound/verification/result_v03.json', 'N4417_result_v03.json'),
              ('research/candidate016_angular_tail_bound/verification/result_v02.json', 'N4409_result_v02.json'),
              ('research/candidate016_reviewed_upper/verification/result.json', 'N4410_result.json'),
              ('research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json', 'N4392_comparison.json'),
              ('research/negative_norm_forcing_assembly/verification/result.json', 'N4252_result.json')):
    ok(IN[k] == HASH[fn], 'N4-418 binds ' + fn)
ok(all(R18['checks'].values()) and len(R18['checks']) == R18['check_count'] == 4430, 'N4-418: 4430 recorded checks true')
ok(all(R17['checks'].values()) and len(R17['checks']) == R17['check_count'] == 2065, 'N4-417: 2065 recorded checks true')

# ---- Part A: coverage
ok(R17['complete_field_mode_count'] == 160 and int(R17['prefix']) == 31 and int(R17['smallest_omitted_mode']) == 33,
   '160 odd modes, prefix 31, first omitted 33')
ok(int(R18['prefix']) == 31 and R18['trial_mode_count'] == 16 and R18['pairing_group_count'] == 2130,
   'N4-418: prefix 31, 16 trial modes, 2130 pairing groups')
ok(R17['complete_uncomputed_tail_retained'] is True and R17['all160_individual_mode_integrals_replayed'] is False and
   R18['all160_source_modes_covered'] is True and R18['individually_integrated_Hardy_modes'] == 16,
   'tail retained, 16 modes integrated, all 160 covered')
q = {int(m['n']): (Fr(m['q_lower_exact']), Fr(m['q_upper_exact'])) for m in R17['modes']}
q9 = {int(m['n']): (Fr(m['q_lower_exact']), Fr(m['q_upper_exact'])) for m in R9['modes']}
ok(sorted(q) == list(range(1, 32, 2)) and q == q9, 'the 16 prefix intervals of result_v03 equal those of result_v02')
for k in ('full_rF_square_lower_exact', 'full_rF_square_upper_exact', 'M2_lower_exact', 'M2_upper_exact',
          'positive_coefficient_formula_upper_exact', 'plain_H_strict_upper_exact'):
    ok(Fr(R17[k]) == Fr(R9[k]), 'result_v03 %s = result_v02' % k)
RL, RU = Fr(R17['full_rF_square_lower_exact']), Fr(R17['full_rF_square_upper_exact'])
rFu, rFl = Fr(NRM['rF']['accepted_upper_exact']), Fr(NRM['rF']['accepted_lower_exact'])
ok(RU == rFu ** 2 and RL == rFl ** 2, 'R2 endpoints are the squares of the accepted N4-392 rF endpoints')
QL, QU = sum(lo for lo, hi in q.values()), sum(hi for lo, hi in q.values())
m = 33
pos = RU / (m * m) + sum((Fr(1, n * n) - Fr(1, m * m)) * hi for n, (lo, hi) in q.items())
ok(pos == Fr(R17['M2_upper_exact']) == Fr(R18['complete_M2_upper_exact']), 'complete M2 upper (T4-474 (4) at N = 33)')
print('Part A: 16 modes 1..31 of 160, first omitted 33; result_v03 prefix data and M2 upper equal to result_v02;'
      ' M2 <= %s; %d checks' % (dec_up(pos, 12), n_ok))

# ---- Part B: selected floors
sel = R18['selected_modes']
ok([int(s['n']) for s in sel] == list(range(1, 32, 2)), 'one selected trial for each of the 16 distinct frequencies')
ok([int(x) for x in R17['selected_improvement_modes']] == list(range(1, 32, 2)), 'N4-417 improvement modes 1..31')
for s in sel:
    ok(IN[s['record']] == s['sha256'] and s['record'].endswith('mode_%03d.json' % int(s['n'])),
       'selected record bound in N4-418 inputs, n=%s' % s['n'])
Ln = {int(s['n']): Fr(s['selected_lower']) for s in sel}
Jn = {int(s['n']): Fr(s['selected_improvement']) for s in sel}
ok(all(v > 0 for v in Ln.values()) and all(v > 0 for v in Jn.values()), 'positive floors')
L2 = sum(v * v for v in Ln.values())
Jt = sum(Jn.values())
ok(L2 == Fr(R18['H_lower_square_exact']) == Fr(R17['H_lower_square_exact']), 'L2 = sum L_n^2')
ok(Jt == Fr(R18['selected_improvement_sum_lower_exact']) == Fr(R17['selected_improvement_sum_lower_exact']) ==
   Fr(60190270781084901078904854514861671131, 25 * 10 ** 37), 'J = sum J_n = 60190270781084901078904854514861671131/(2.5 10^38)')
U2 = pos - Jt
ok(U2 == Fr(R18['H_upper_square_exact']) == Fr(R17['improved_H_square_upper_exact']), 'U2 = M2 upper - J')
ok(L2 < U2, 'L2 < U2: the H^2 enclosure is not empty')
# per-mode: the dual norm splits over frequencies, L_n^2 <= H_n^2 <= q_n/n^2 - b_n^2/a_n < U_n/n^2 - J_n
gap = {}
for n in Ln:
    gap[n] = q[n][1] / (n * n) - Jn[n] - Ln[n] ** 2
    ok(gap[n] > 0, 'per-mode consistency L_n^2 < U_n/n^2 - J_n, n=%d' % n)
tailterm = (RU - QU) / (m * m)
ok(U2 - L2 == sum(gap.values()) + tailterm and tailterm > 0, 'width = sum of mode gaps + (R_U - Q_U)/33^2')
print('Part B: L2 = %s, J = %s, U2 = %s (rounded outward); width U2 - L2 <= %s = modes %s + tail %s; %d checks'
      % (dec_dn(L2, 12), dec_dn(Jt, 12), dec_up(U2, 12), dec_up(U2 - L2, 9), dec_up(sum(gap.values()), 9),
         dec_up(tailterm, 9), n_ok))
print('  FLOAT, per-mode gaps U_n/n^2 - J_n - L_n^2 (exact positive, shown about): ' +
      ', '.join('%d: %.2e' % (n, float(g)) for n, g in gap.items()))
print('  modes 1..15 together <= %s; modes 17..31 together <= %s' % (dec_up(sum(gap[n] for n in range(1, 16, 2)), 9),
                                                                    dec_up(sum(gap[n] for n in range(17, 32, 2)), 9)))

# ---- Part C: strict endpoints, E2, gaps
HL, HU = Fr(R18['H_strict_lower_exact']), Fr(R18['H_strict_upper_exact'])
ok(HL == Fr(R17['H_strict_lower_exact']) == Fr(308366750368225240013184170643, 5 * 10 ** 29), 'H lower fraction')
ok(HU == Fr(R17['conditional_improved_H_strict_upper_exact']) == Fr(154488238463271634620877708271, 25 * 10 ** 28),
   'H upper fraction')
ok(HL > 0 and HL * HL < L2 and HU * HU > U2, 'strict H endpoints by exact squaring')


def e2sq(c, h2):
    return c['P2'] ** 2 + 2 ** 14 * c['G1'] ** 2 + 2 ** 18 * c['G0'] ** 2 + Fr(20, 21) * 2 ** 18 * h2


up = {k: Fr(NRM[k]['accepted_upper_exact']) for k in ('G0', 'G1', 'P2')}
lo4 = {k: Fr(NRM[k]['accepted_lower_exact']) for k in ('G0', 'G1', 'P2')}
EL2, EU2 = e2sq(lo4, L2), e2sq(up, U2)
ok(EL2 == Fr(R18['E2_lower_square_exact']) == Fr(R17['E2_lower_square_exact']), 'E2^2 lower from the N4-392 lowers and L2')
ok(EU2 == Fr(R18['E2_upper_square_exact']) == Fr(R17['conditional_E2_upper_square_exact']), 'E2^2 upper from the uppers and U2')
EL, EU = Fr(R18['E2_strict_lower_exact']), Fr(R18['E2_strict_upper_exact'])
ok(EL == Fr(R17['E2_strict_lower_exact']) == Fr(628580088526341, 10 ** 12) and
   EU == Fr(R17['conditional_E2_strict_upper_exact']) == Fr(314439512374259, 5 * 10 ** 11), 'E2 fractions')
ok(EL * EL < EL2 and EU * EU > EU2, 'strict E2 endpoints by exact squaring')
U7 = Fr(J['N4252_result.json']['E_upper']['strict_upper_exact'])
ok(U7 == Fr(606820219, 10 ** 6), 'E2(007) < 606.820219 (N4-252)')
egap = EL - U7
ok(egap == Fr(R18['E2016_minus_E2007_strict_lower_exact']) == Fr(21759869526341, 10 ** 12), 'E2 gap = 21.759869526341')
hgap = Fr(R18['H007_minus_H016_strict_lower_exact'])
flint.ctx.prec = 600
H7lo = flint.arb(J['N4252_result.json']['H_input_lower_ball'])
fq = lambda z: flint.arb(flint.fmpq(z.numerator, z.denominator))
# the H(007) lower ball as a decimal interval [mid - rad, mid + rad]; H(007) >= mid - rad, H(016) < HU strictly
b7 = J['N4252_result.json']['H_input_lower_ball'].strip('[]').split()
h7lo = Fr(b7[0]) - Fr(b7[2])
ok(b7[1] == '+/-' and hgap == h7lo - HU and hgap > 0, 'H gap = (lower end of the N4-252 H(007) lower ball) - HU, exact')
ok(not (fq(h7lo) > H7lo) and fq(HU) < H7lo, 'Arb: the ball parsed at 600 bits agrees; HU below the ball')
# T4-486 directed displays and c1-n4 displays
T486 = {'H_lower': Fr(616733500735, 10 ** 12), 'H_upper': Fr(617952953855, 10 ** 12),
        'E2_lower': Fr(628580088525, 10 ** 9), 'E2_upper': Fr(628879024750, 10 ** 9),
        'H_gap': Fr(17571422145091, 10 ** 15), 'E2_gap': Fr(21759869525, 10 ** 9)}
ok(T486['H_lower'] < HL and HU < T486['H_upper'] and T486['E2_lower'] < EL and EU < T486['E2_upper'] and
   T486['H_gap'] < hgap and T486['E2_gap'] < egap, 'T4-486 displays are implied')
db = {k: Fr(v) for k, v in R18['display_bounds_exact'].items()}
ok(db['H_lower'] < HL and HU < db['H_upper'] and db['E2_lower'] < EL and EU < db['E2_upper'] and
   db['H007_minus_H016_lower'] < hgap and db['E2016_minus_E2007_lower'] < egap, 'N4-418 displays are implied')
print('Part C: %s < H(016) < %s; %s < E2(016) < %s; H(007) - H(016) > %s; E2(016) - E2(007) > %s; %d checks'
      % (dec_dn(HL, 12), dec_up(HU, 12), dec_dn(EL, 9), dec_up(EU, 9), dec_dn(hgap, 15), dec_dn(egap, 12), n_ok))
print('  H(007) lower ball about %s; E2 width <= %s, H width <= %s'
      % (H7lo.lower().str(12, radius=False), dec_up(EU - EL, 9), dec_up(HU - HL, 9)))

# ---- Part D: comparisons
HL10, HU10 = Fr(R10['H_strict_lower_exact']), Fr(R10['H_strict_upper_exact'])
EL10, EU10 = Fr(R10['E2_strict_lower_exact']), Fr(R10['E2_strict_upper_exact'])
ok(HL10 < HL and HU < HU10 and EL10 < EL and EU < EU10, 'N4-418 enclosure strictly inside N4-410')
ok(L2 > Fr(R10['H_lower_square_exact']) and U2 < Fr(R10['H_upper_square_exact']), 'both squares improve N4-410')
imp398 = Fr(J['N4398_result.json']['improvement_sum_strict_lower_exact'])
ok(Jt > imp398, 'J above the N4-398 two-mode floor')
ok(Jn[1] + Jn[3] == imp398, 'J_1 + J_3 equals the N4-398 two-mode floor exactly')
print('Part D: nested in N4-410 ((%s, %s) for H, (%s, %s) for E2); J - N4-398 floor >= %s, all from modes 5..31'
      ' (J_1 + J_3 equals the N4-398 floor exactly)'
      % (dec_dn(HL10, 9), dec_up(HU10, 9), dec_dn(EL10, 9), dec_up(EU10, 9), dec_dn(Jt - imp398, 9)))
n3H = (0.6167335007, 0.6189603636)
n3E = (628.5800885, 629.1263188)
ok(abs(n3H[0] - float(HL)) < 1e-10 and n3H[1] > float(HU), 'FLOAT: c1-n3 H lower agrees to 1e-10, its upper is above HU')
ok(n3E[1] > float(EU) and abs(n3E[0] - float(EL)) < 1e-6, 'FLOAT: c1-n3 E2 upper above EU, lower agrees to 1e-6')
dH = HL - Fr('0.6167335007')
ok(dH == Fr(18225240013184170643, 5 * 10 ** 29) and Fr(364, 10 ** 13) < dH < Fr(365, 10 ** 13),
   'exact: HL - 0.6167335007 = 18225240013184170643/(5 10^29), in (3.64e-11, 3.65e-11)')
print('  FLOAT: c1-n3 CLAIMED H(016) in [%.10f, %.10f]: lower below HL by %s (exact, in (%s, %s)), upper %.2e above HU;'
      ' CLAIMED E2(016) in [%.7f, %.7f]: upper %.4f above EU'
      % (n3H[0], n3H[1], dH, dec_dn(dH, 13), dec_up(dH, 13), n3H[1] - float(HU), n3E[0], n3E[1], n3E[1] - float(EU)))
# c1-n3 notes 16:30Z and 16:37Z (with dual tests in modes 33 to 63): H(016) >= 0.6167972322, E2(016) >= 628.5957005
n3H2, n3E2 = 0.6167972322, 628.5957005
ok(float(HL) < n3H2 < float(HU) and float(EL) < n3E2 < float(EU), 'FLOAT: c1-n3 later CLAIMED lowers inside the enclosure')
print('  FLOAT: c1-n3 later CLAIMED H(016) >= %.10f and E2(016) >= %.7f lie inside, %.2e and %.4f above HL and EL'
      % (n3H2, n3E2, n3H2 - float(HL), n3E2 - float(EL)))
print('  FLOAT: modes 17..31 share of the width %.3f; tail term share %.3f' % (float(sum(gap[n] for n in range(17, 32, 2)) / (U2 - L2)),
                                                                          float(tailterm / (U2 - L2))))
print('checks passed', n_ok, '; elapsed %.1f s' % (time.time() - t0))
print('RESULT PASS')
