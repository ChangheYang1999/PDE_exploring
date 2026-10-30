# R1-054 (REVIEWS_v54): exact recomposition of c1-n4's N4-427 and N4-428 (candidate 016, Hardy prefix 1, 3, ..., 47)
# and N4-430 and N4-431 (prefix 1, 3, ..., 63) from their saved exact endpoints. No c1-n4, c1-t4 or c1-n3 code is run;
# the saved numbers are recomposed in exact Fractions. The mode integrals (708 and 920 group intervals) and the 2130
# group intervals behind the 16 dual and solenoidal floors are not recomputed.
# Part A: hashes and bindings (each multimode result binds its angular-tail result; both bind the N4-392 components).
# Part B, for P = 47 and P = 63: coverage, mode intervals (modes 1..31 equal to N4-417's), R2 endpoints, tail endpoints,
#   M2 lower and the positive-coefficient M2 upper R_U/N^2 + sum_(n <= P) (1/n^2 - 1/N^2) U_n at N = P + 2.
# Part C, for P = 47 and P = 63: U2 = M2 upper - J with the N4-418 floors, per-mode consistency, strict H and E2
#   endpoints by exact squaring, E2 from the N4-392 component uppers, the gaps over 007 (N4-252), c1-n4's displays.
# Part D: nesting P = 63 inside P = 47 inside N4-418; the width split; FLOAT positions of c1-n3's CLAIMED values.
# Part E (only when R6/c1-n4 is readable): the four source files have the recorded sha256 and the extract fields equal
#   their source fields.
# Usage: python3 check_N4427.py (from artifacts/checks). Inputs in data/: N4427_extract.json (written by
#   make_N4427_extract.py), N4418_result_v01.json, N4417_result_v03.json, N4392_comparison.json, N4252_result.json.
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
    j = -((-z.numerator * 10 ** k) // z.denominator)
    return '%s%d.%0*d' % ('-' if j < 0 else '', abs(j) // 10 ** k, k, abs(j) % 10 ** k)


def dec_dn(z, k):
    j = (z.numerator * 10 ** k) // z.denominator
    return '%d.%0*d' % (j // 10 ** k, k, j % 10 ** k)


sha = lambda b: hashlib.sha256(b).hexdigest()
hx = lambda z: sha(str(z).encode())
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
HASH = {'N4427_extract.json': '611a8febe1f823f04fd32047bba49f647452f713349f3aa0cb34898465427cac',
        'N4418_result_v01.json': '8eec600612f7719a1c0cbcb408d1665659b8d2c06d861f032a102651953c3728',
        'N4417_result_v03.json': '285dac39d93e32574c214d00cef9764087c0718c19b4042398c7ec728b530840',
        'N4392_comparison.json': 'a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc',
        'N4252_result.json': 'd94473eb11c0708e25a9529f00b49576628023066e626ed9170bf29b62e22e7c'}
J = {}
for fn, h in HASH.items():
    raw = open(os.path.join(D, fn), 'rb').read()
    ok(sha(raw) == h, 'hash ' + fn)
    J[fn] = json.loads(raw)
X, R18, R17 = J['N4427_extract.json'], J['N4418_result_v01.json'], J['N4417_result_v03.json']
REC, SRC = X['records'], X['sources']
NRM = J['N4392_comparison.json']['norms']
RAW = 'a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42'
SRCH = {'tail_v04': 'd1d90c2295662dd1288a3a77d100b0b9cc3cdfbfb8a8345399145c7cba3f0bff',
        'tail_v05': 'dc1dfe24d70ba74c405e317864391dcb01e0a8188bbf8eb97edaefbe11ef9066',
        'multi_v02': '42e43b1b5240309fad4ab3d7579dfe557ae15a89ead61b9a4991da18a4950513',
        'multi_v03': '6c5f02dc951d92cff7df788228594d2137e5f41b5bdea58b17b8505cb40cd3ee'}
CASES = ((47, 'tail_v04', 'multi_v02', 3017, 4438), (63, 'tail_v05', 'multi_v03', 3921, 4446))

# ---- Part A: bindings
for k, h in SRCH.items():
    ok(SRC[k]['sha256'] == h, 'extract source hash ' + k)
for P, kt, km, ct, cm in CASES:
    t, m = REC[kt], REC[km]
    ok(t['raw_sha256'] == m['raw_sha256'] == R18['raw_sha256'] == RAW, 'one 016 raw file, P=%d' % P)
    ok(t['candidate'] == m['candidate'] == 'C1-N1-016-legqs25-quot013', 'candidate id, P=%d' % P)
    ok(m['inputs'][SRC[kt]['path']] == SRC[kt]['sha256'], 'multimode result binds its tail result, P=%d' % P)
    cp = 'research/candidate016_scaled_norm_peer/verification/comparison_G0_rF_G1_P2_v01.json'
    ok(t['inputs'][cp] == m['inputs'][cp] == HASH['N4392_comparison.json'], 'both bind N4-392, P=%d' % P)
    ok(m['inputs']['research/negative_norm_forcing_assembly/verification/result.json'] == HASH['N4252_result.json'],
       'multimode binds N4-252, P=%d' % P)
    ok(t['checks_all_true'] and t['checks_len'] == t['check_count'] == ct and m['checks_all_true'] and
       m['checks_len'] == m['check_count'] == cm, 'recorded checks all true (%d and %d), P=%d' % (ct, cm, P))
print('Part A: 4 c1-n4 results bound (prefix 47: N4-427 %s..., N4-428 %s...; prefix 63: N4-430 %s..., N4-431 %s...);'
      ' %d checks' % (SRCH['tail_v04'][:8], SRCH['multi_v02'][:8], SRCH['tail_v05'][:8], SRCH['multi_v03'][:8], n_ok))

# common data
qall = {int(n): (Fr(lo), Fr(lo) + Fr(w)) for n, lo, w in X['q_modes_tail_v05']}
q17 = {int(mm['n']): (Fr(mm['q_lower_exact']), Fr(mm['q_upper_exact'])) for mm in R17['modes']}
RL, RU = Fr(R17['full_rF_square_lower_exact']), Fr(R17['full_rF_square_upper_exact'])
rFu, rFl = Fr(NRM['rF']['accepted_upper_exact']), Fr(NRM['rF']['accepted_lower_exact'])
ok(RU == rFu ** 2 and RL == rFl ** 2, 'R2 endpoints are the squares of the accepted N4-392 rF endpoints')
sel = R18['selected_modes']
Ln = {int(s['n']): Fr(s['selected_lower']) for s in sel}
Jn = {int(s['n']): Fr(s['selected_improvement']) for s in sel}
L2, Jt = sum(v * v for v in Ln.values()), sum(Jn.values())
ok(L2 == Fr(R18['H_lower_square_exact']) and Jt == Fr(R18['selected_improvement_sum_lower_exact']),
   'N4-418 L2 and J recomputed from its 16 selected floors')
up = {k: Fr(NRM[k]['accepted_upper_exact']) for k in ('G0', 'G1', 'P2')}
lo4 = {k: Fr(NRM[k]['accepted_lower_exact']) for k in ('G0', 'G1', 'P2')}


def e2sq(c, h2):
    return c['P2'] ** 2 + 2 ** 14 * c['G1'] ** 2 + 2 ** 18 * c['G0'] ** 2 + Fr(20, 21) * 2 ** 18 * h2


HL, EL = Fr(R18['H_strict_lower_exact']), Fr(R18['E2_strict_lower_exact'])
U7 = Fr(J['N4252_result.json']['E_upper']['strict_upper_exact'])
ok(U7 == Fr(606820219, 10 ** 6), 'E2(007) < 606.820219 (N4-252)')
b7 = J['N4252_result.json']['H_input_lower_ball'].strip('[]').split()
ok(b7[1] == '+/-', 'N4-252 H(007) lower ball format')
h7lo = Fr(b7[0]) - Fr(b7[2])
flint.ctx.prec = 600
H7lo = flint.arb(J['N4252_result.json']['H_input_lower_ball'])
fq = lambda z: flint.arb(flint.fmpq(z.numerator, z.denominator))
res = {}
for P, kt, km, ct, cm in CASES:
    t, m = REC[kt], REC[km]
    N = P + 2
    # ---- Part B
    ok(int(t['prefix']) == int(m['prefix']) == P and int(t['smallest_omitted_mode']) == N and
       t['mode_count_replayed'] == (P + 1) // 2 == m['individually_integrated_Hardy_modes'],
       'prefix %d, first omitted %d, %d modes integrated' % (P, N, (P + 1) // 2))
    ok(t['complete_field_mode_count'] == 160 and t['complete_field_component_count'] == 1360 and
       t['complete_uncomputed_tail_retained'] is True and t['all160_individual_mode_integrals_replayed'] is False and
       m['all160_source_modes_covered'] is True, '160 odd modes, 1360 components, tail retained, P=%d' % P)
    mr = t['mode_records']
    ok([r[0] for r in mr] == list(range(1, P + 1, 2)), 'mode records 1..%d' % P)
    for n, rec, h, gc, bits, c1, c2 in mr:
        # c1 and c2 record whether the replay ball and the saved mode ball contain one another; the proof asks only
        # that they agree (the recorded n<n>_production_consistency checks), so they are not required here
        ok(rec.endswith('mode_%03d.json' % n) and t['inputs'][rec] == h and bits > 150,
           'mode %d record bound, more than 150 accuracy bits, P=%d' % (n, P))
    q = {n: qall[n] for n in range(1, P + 1, 2)}
    ok(all(0 < lo < hi and hi - lo < Fr(1, 10 ** 510) for lo, hi in q.values()), 'all intervals positive, width < 1e-510')
    ok(all(q[n] == q17[n] for n in range(1, 32, 2)), 'modes 1..31 equal to N4-417 (R1-052), P=%d' % P)
    ok(Fr(t['full_rF_square_lower_exact']) == RL and Fr(t['full_rF_square_upper_exact']) == RU, 'R2 endpoints, P=%d' % P)
    QL, QU = sum(lo for lo, hi in q.values()), sum(hi for lo, hi in q.values())
    ok(hx(RL - QU) == t['tail_rF_square_lower_exact_sha256'] and hx(RU - QL) == t['tail_rF_square_upper_exact_sha256']
       and RL - QU > 0, 'tail endpoints R_L - Q_U > 0 and R_U - Q_L, P=%d' % P)
    pos = RU / (N * N) + sum((Fr(1, n * n) - Fr(1, N * N)) * hi for n, (lo, hi) in q.items())
    ok(hx(pos) == t['M2_upper_exact_sha256'] == t['positive_coefficient_formula_upper_exact_sha256'] ==
       m['complete_M2_upper_exact_sha256'], 'M2 upper = R_U/%d^2 + sum (1/n^2 - 1/%d^2) U_n' % (N, N))
    split = sum(hi / (n * n) for n, (lo, hi) in q.items()) + (RU - QL) / (N * N)
    spl_eq = hx(split) == t['split_formula_upper_exact_sha256']
    ok(spl_eq or t['split_formula_upper_exact_sha256'] == t['M2_upper_exact_sha256'],
       'stored split formula value: own split form, or equal to the positive-coefficient upper, P=%d' % P)
    ok(split - pos == sum(hi - lo for lo, hi in q.values()) / (N * N), 'split - positive = sum (U_n - L_n)/N^2')
    m2lo = sum(lo / (n * n) for n, (lo, hi) in q.items())
    ok(hx(m2lo) == t['M2_lower_exact_sha256'], 'M2 lower = sum L_n/n^2, P=%d' % P)
    pH = Fr(t['plain_H_strict_upper_exact'])
    ok(pH * pH > pos, 'plain H strict upper by exact squaring, P=%d' % P)
    print('Part B, P = %d: %d modes, first omitted %d; tail R2 in [%s, %s]; M2 in [%s, %s]; plain H(016) < %s;'
          ' %d checks' % (P, len(q), N, dec_dn(RL - QU, 9), dec_up(RU - QL, 9), dec_dn(m2lo, 12), dec_up(pos, 12),
                          dec_up(pH, 9), n_ok))
    if not spl_eq:
        print('  the stored split_formula_upper_exact equals the positive-coefficient value; the split form'
              ' sum U_n/n^2 + (R_U - Q_L)/N^2 exceeds it by sum (U_n - L_n)/N^2 < 1e-510')
    # ---- Part C
    ok(t['selected_improvement_modes'] == list(range(1, 32, 2)) and m['selected_modes_equal_N4418'] is True and
       m['trial_mode_count'] == 16 and m['pairing_group_count'] == 2130, '16 distinct floors, those of N4-418, P=%d' % P)
    ok(Fr(t['selected_improvement_sum_lower_exact']) == Fr(m['selected_improvement_sum_lower_exact']) == Jt and
       Fr(t['H_lower_square_exact']) == Fr(m['H_lower_square_exact']) == L2, 'J and L2 unchanged, P=%d' % P)
    U2 = pos - Jt
    ok(hx(U2) == t['improved_H_square_upper_exact_sha256'] == m['H_upper_square_exact_sha256'], 'U2 = M2 upper - J')
    ok(L2 < U2, 'the H^2 enclosure is not empty, P=%d' % P)
    gap = {n: q[n][1] / (n * n) - Jn[n] - Ln[n] ** 2 for n in Ln}
    ok(all(g > 0 for g in gap.values()), 'per-mode L_n^2 < U_n/n^2 - J_n for n = 1..31, P=%d' % P)
    hiP = sum((Fr(1, n * n) - Fr(1, N * N)) * q[n][1] for n in range(33, P + 1, 2))
    tailterm = (RU - sum(q[n][1] for n in range(1, 32, 2))) / (N * N) + hiP
    ok(U2 - L2 == sum(gap.values()) + tailterm and tailterm > 0,
       'width split: U2 - L2 = sum of the 16 mode gaps + (R_U - Q_U(1..31))/N^2 + sum_(33..P) (1/n^2 - 1/N^2) U_n')
    HU = Fr(m['H_strict_upper_exact'])
    ok(HU == Fr(t['conditional_improved_H_strict_upper_exact']) and Fr(m['H_strict_lower_exact']) ==
       Fr(t['H_strict_lower_exact']) == HL, 'strict H fractions agree, P=%d' % P)
    ok(HL * HL < L2 and HU * HU > U2, 'strict H endpoints by exact squaring, P=%d' % P)
    EU2 = e2sq(up, U2)
    ok(hx(EU2) == t['conditional_E2_upper_square_exact_sha256'] == m['E2_upper_square_exact_sha256'],
       'E2^2 upper from the N4-392 uppers and U2, P=%d' % P)
    ok(Fr(t['E2_lower_square_exact']) == Fr(m['E2_lower_square_exact']) == e2sq(lo4, L2), 'E2^2 lower unchanged')
    EU = Fr(m['E2_strict_upper_exact'])
    ok(EU == Fr(t['conditional_E2_strict_upper_exact']) and Fr(m['E2_strict_lower_exact']) == EL and EU * EU > EU2,
       'strict E2 upper by exact squaring, P=%d' % P)
    hgap = Fr(m['H007_minus_H016_strict_lower_exact'])
    ok(hgap == h7lo - HU and hgap > 0 and fq(HU) < H7lo, 'H gap = (lower end of the N4-252 H(007) ball) - HU, P=%d' % P)
    egap = Fr(m['E2016_minus_E2007_strict_lower_exact'])
    ok(egap == EL - U7 == Fr(21759869526341, 10 ** 12), 'E2 gap = 21.759869526341, P=%d' % P)
    db = {k: Fr(v) for k, v in m['display_bounds_exact'].items()}
    ok(db['H_lower'] < HL and HU < db['H_upper'] and db['E2_lower'] < EL and EU < db['E2_upper'] and
       db['H007_minus_H016_lower'] < hgap and db['E2016_minus_E2007_lower'] < egap, 'c1-n4 displays implied, P=%d' % P)
    res[P] = dict(HU=HU, EU=EU, U2=U2, pos=pos, hgap=hgap, gap=gap, tail=tailterm, hiP=hiP)
    print('Part C, P = %d: U2 = %s; %s < H(016) < %s; %s < E2(016) < %s; H(007) - H(016) > %s;'
          ' E2(016) - E2(007) > %s; %d checks' % (P, dec_up(U2, 12), dec_dn(HL, 12), dec_up(HU, 12), dec_dn(EL, 9),
                                                   dec_up(EU, 9), dec_dn(hgap, 15), dec_dn(egap, 12), n_ok))
    print('  exact: H(016) < %s; E2(016) < %s' % (m['H_strict_upper_exact'], m['E2_strict_upper_exact']))

# ---- Part D
HU18, EU18 = Fr(R18['H_strict_upper_exact']), Fr(R18['E2_strict_upper_exact'])
ok(res[63]['HU'] < res[47]['HU'] < HU18 and res[63]['EU'] < res[47]['EU'] < EU18, 'nested: P63 inside P47 inside N4-418')
ok(res[63]['U2'] < res[47]['U2'] < Fr(R18['H_upper_square_exact']), 'U2 decreases with the prefix')
ok(Fr(617899376, 10 ** 9) > res[47]['HU'] and Fr(628865882, 10 ** 6) > res[47]['EU'] and
   Fr(617897369, 10 ** 9) > res[63]['HU'] and Fr(628865389, 10 ** 6) > res[63]['EU'], 'decimal uppers implied')
ok(res[47]['hgap'] > Fr(17625000525836, 10 ** 15) and res[63]['hgap'] > Fr(17627007636152781, 10 ** 18),
   'decimal H gaps implied')
print('Part D: H upper %s (N4-418) > %s (P = 47) > %s (P = 63); E2 upper %s > %s > %s'
      % (dec_up(HU18, 9), dec_up(res[47]['HU'], 9), dec_up(res[63]['HU'], 9), dec_up(EU18, 6), dec_up(res[47]['EU'], 6),
         dec_up(res[63]['EU'], 6)))
for P in (47, 63):
    r = res[P]
    print('  P = %d: width U2 - L2 <= %s; FLOAT shares: 16 mode gaps (n <= 31) %.3f, modes 33..%d and tail %.3f'
          % (P, dec_up(r['U2'] - L2, 9), float(sum(r['gap'].values()) / (r['U2'] - L2)), P,
             float(r['tail'] / (r['U2'] - L2))))
n3H, n3E = (0.6167335007, 0.6189603636), (628.5800885, 629.1263188)
n3H2, n3E2 = 0.6167972322, 628.5957005
ok(float(HL) < n3H2 < float(res[63]['HU']) and float(EL) < n3E2 < float(res[63]['EU']),
   'FLOAT: c1-n3 later CLAIMED lowers lie inside the P = 63 enclosure')
print('  FLOAT: c1-n3 CLAIMED H(016) >= %.10f lies %.2e below the P = 63 upper; c1-n3 CLAIMED upper %.10f is above it'
      ' by %.2e' % (n3H2, float(res[63]['HU']) - n3H2, n3H[1], n3H[1] - float(res[63]['HU'])))

# ---- Part E: source files, when readable
N4R = 'RUN_ROOT/numerics_audit_N4'
if all(os.path.exists(os.path.join(N4R, v['path'])) for v in SRC.values()):
    for k, v in SRC.items():
        b = open(os.path.join(N4R, v['path']), 'rb').read()
        ok(sha(b) == v['sha256'], 'source hash ' + k)
        s = json.loads(b)
        for key, val in REC[k].items():
            if key.endswith('_exact_sha256'):
                ok(sha(s[key[:-7]].encode()) == val, 'source field %s %s' % (k, key[:-7]))
            elif key in s and key not in ('inputs', 'display_bounds_exact'):
                ok(s[key] == val, 'source field %s %s' % (k, key))
        if k.startswith('tail'):
            ok([[int(mm['n']), mm['record'], mm['sha256'], mm['group_count'], mm['accuracy_bits'],
                 mm['replay_contains_source_final'], mm['source_final_contains_replay']] for mm in s['modes']] ==
               REC[k]['mode_records'], 'mode records ' + k)
            ok(all(qall[int(mm['n'])] == (Fr(mm['q_lower_exact']), Fr(mm['q_upper_exact'])) for mm in s['modes']),
               'mode endpoints ' + k)
            ok(all(s['inputs'][p] == h for p, h in REC[k]['inputs'].items()), 'inputs ' + k)
        else:
            ok(s['selected_modes'] == R18['selected_modes'] and s['display_bounds_exact'] == REC[k]['display_bounds_exact']
               and all(s['inputs'][p] == h for p, h in REC[k]['inputs'].items()), 'selected modes, displays, inputs ' + k)
    print('Part E: the four c1-n4 source files are readable; the extract equals their fields')
else:
    print('Part E: c1-n4 source files not readable; skipped')
print('checks passed', n_ok, '; elapsed %.1f s' % (time.time() - t0))
print('RESULT PASS')
