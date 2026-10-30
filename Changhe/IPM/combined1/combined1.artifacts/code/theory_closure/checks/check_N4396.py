# R1-048 (REVIEWS_v46): independent review of N4-396 (c1-n4 research/candidate016_dual_lower, PROOF sha256
# 4a98af09...7eabca): the two-mode dual lower bound H(F) >= sqrt(sum_n p_n^2/d_n) for the exact candidate 016 and the
# ordering E2(007) < E2(016). No c1-n4, c1-n3 or c1-t4 code is run; their saved numbers are read for comparison.
# Part A, exact: admissibility of all 663 test coefficients (beta > 3/2, k >= -1, 3 + 2k >= n, 3 + 2k - n even).
# Part B, exact rationals: the gradient energies d_n/pi by a third method, Beta integrals in r (each basis function is
#   r^(3+2k) (1+r^2)^(-beta-k) sin(n theta); every pair integral is a rational Beta value B(N, beta_i + beta_j - 3) with
#   integer N); comparison with c1-n3's and c1-n4's exact rationals.
# Part C, Arb balls: |p_n|/sqrt(d_n) from c1-n4's final pairing ball and the exact d_n of Part B; the strict floors l_n
#   lie below it and below c1-n3's and c1-n4's quotient balls.
# Part D, exact rationals: H^2 >= l_1^2 + l_3^2, the strict H floor, the E2 floor from the accepted N4-392 component
#   lower bounds, and the comparison with the accepted 007 upper bound 606820219/10^6 (N4-252), same E2 definition.
# Part E, FLOAT arithmetic only: E2 from the rounded MID 32 displays of numerics_v15 section 5 (not a bound).
# Usage: python3 check_N4396.py (from artifacts/checks). Inputs in data/: N3_016_hdual_m13deep.json (c1-n3's exact
# vectors, copy of c1-n4 source/N3_exact_vectors.json), N4396_mode_001.json, N4396_mode_003.json, N4396_result.json
# (c1-n4 verification/), N4392_comparison.json (c1-n4 candidate016_scaled_norm_peer/verification/
# comparison_G0_rF_G1_P2_v01.json), N4252_result.json (c1-n4 negative_norm_forcing_assembly/verification/result.json).
import hashlib, json, os, sys, time
from fractions import Fraction as Fr
from math import factorial
import flint

sys.set_int_max_str_digits(0)
t0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, 'data')
flint.ctx.prec = 1200
n_ok = 0


def ok(cond, msg):
    global n_ok
    assert cond, msg
    n_ok += 1


HASH = {'N3_016_hdual_m13deep.json': 'a32a02e71da636635e3b1d6c3289d5dc478bd8a63cda07f06f8cae98e9a968e5',
        'N4396_mode_001.json': '4291bb11104879c7821a888c52ad666d1700065d6cf365540250dd0080b34cda',
        'N4396_mode_003.json': 'e57ce8e56dcd9e613afdb17b7f2d6f8c74252480be65502efe9065938036aab9',
        'N4396_result.json': 'e91c096d6ccb1cb0f9e08e63ae53a2c258875cad720c5ab483b875bfb4a4dffa',
        'N4392_comparison.json': 'a2f68954828f60a7dc8983ecb69e8e30ddcd8e868ec0d1b58ce56faa27eeaedc',
        'N4252_result.json': 'd94473eb11c0708e25a9529f00b49576628023066e626ed9170bf29b62e22e7c'}
J = {}
for f, h in HASH.items():
    b = open(os.path.join(D, f), 'rb').read()
    ok(hashlib.sha256(b).hexdigest() == h, 'hash ' + f)
    J[f] = json.loads(b)
N3 = J['N3_016_hdual_m13deep.json']
RES = J['N4396_result.json']
ok(N3['source_sha256'] == RES['raw_sha256'] == 'a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42',
   'both records bind the 016 raw file')
ok(N3['id'] == RES['candidate'] == 'C1-N1-016-legqs25-quot013', 'candidate id')


def beta_int(N, z):
    # B(N, z) = (N-1)! / (z (z+1) ... (z+N-1)) for integer N >= 1 and rational z > 0
    den = Fr(1)
    for i in range(N):
        den *= z + i
    return Fr(factorial(N - 1)) / den


def grad_energy_over_pi(n, basis):
    # basis: list of (x, beta, k). psi = sum x r^(3+2k) (1+r^2)^(-(beta+k)) sin(n theta) =: R(r) sin(n theta).
    # ||grad psi||^2 / pi = int_0^inf (R'^2 + n^2 R^2 / r^2) r dr. With a = 3+2k, s = beta+k:
    # g' = a r^(a-1) (1+r^2)^(-s) - 2 s r^(a+1) (1+r^2)^(-s-1), and int_0^inf r^(2N-1) (1+r^2)^(-S) dr = B(N, S-N)/2.
    W = {}
    m = len(basis)
    for i in range(m):
        xi, bi, ki = basis[i]
        for j in range(i, m):
            xj, bj, kj = basis[j]
            key = (ki, bi, kj, bj) if (ki, bi) <= (kj, bj) else (kj, bj, ki, bi)
            W[key] = W.get(key, 0) + (1 if i == j else 2) * xi * xj
    tot = Fr(0)
    for (ki, bi, kj, bj), w in W.items():
        ai, si, aj, sj = 3 + 2 * ki, bi + ki, 3 + 2 * kj, bj + kj
        A = (ai + aj) // 2              # r^(ai+aj-1) = r^(2A-1)
        z = bi + bj - 3                 # S - A with S = si + sj
        B0, B1, B2 = beta_int(A, z), beta_int(A + 1, z), beta_int(A + 2, z)
        v = ((ai * aj + n * n) * B0 - 2 * (ai * sj + aj * si) * B1 + 4 * si * sj * B2) / 2
        tot += w * v
    return tot


modes = {}
for M in N3['modes']:
    n = int(M['n'])
    basis = []
    for key, val in M['x_rational'].items():
        bs, ks = key.split(',')
        b, k = Fr(bs), int(ks)
        # Part A: admissibility
        ok(b > Fr(3, 2), 'beta > 3/2')
        ok(k >= -1 and 3 + 2 * k >= n and (3 + 2 * k - n) % 2 == 0, 'origin regularity')
        basis.append((Fr(val), b, k))
    ok(len(basis) == int(M['basis_size']), 'basis size mode %d' % n)
    ok(len({(b, k) for _, b, k in basis}) == len(basis), 'distinct labels mode %d' % n)
    modes[n] = dict(M=M, basis=basis)
ok(sorted(modes) == [1, 3], 'modes 1 and 3')
ok(sum(len(v['basis']) for v in modes.values()) == 663, '663 coefficients')
print('Part A: 663 coefficients admissible (beta > 3/2, k >= -1, 3 + 2k >= n, 3 + 2k - n even);', n_ok, 'checks')

# Part B
for n in (1, 3):
    t1 = time.time()
    d = grad_energy_over_pi(n, modes[n]['basis'])
    modes[n]['d_over_pi'] = d
    ok(d > 0, 'positive gradient energy mode %d' % n)
    ok(d == Fr(modes[n]['M']['grad_psi_sq_over_pi_exact']), 'equals c1-n3 exact energy mode %d' % n)
    rec = J['N4396_mode_%03d.json' % n]
    ok(int(rec['n']) == n and d == Fr(rec['gradient_energy_over_pi_exact']), 'equals c1-n4 exact energy mode %d' % n)
    print('Part B: mode %d, d_n/pi = %.15e exactly equal to c1-n3 and c1-n4 (%.1f s; numerator %d digits)'
          % (n, float(d), time.time() - t1, len(str(d.numerator))))

# Part C
PI = flint.arb.pi()
floors = {int(k): Fr(v) for k, v in RES['mode_strict_floors'].items()}
for n in (1, 3):
    rec = J['N4396_mode_%03d.json' % n]
    p = flint.arb(rec['pairing_ball'])
    d = flint.arb(flint.fmpq(modes[n]['d_over_pi'].numerator, modes[n]['d_over_pi'].denominator)) * PI
    q = abs(p) / d.sqrt()
    l = floors[n]
    lq = flint.arb(flint.fmpq(l.numerator, l.denominator))
    ok(l > 0 and lq < q, 'strict floor below own quotient mode %d' % n)
    ok(lq < flint.arb(rec['quotient_ball']), 'floor below c1-n4 quotient ball mode %d' % n)
    ok(lq < flint.arb(modes[n]['M']['LB']), 'floor below c1-n3 quotient ball mode %d' % n)
    ok(q.overlaps(flint.arb(rec['quotient_ball'])), 'own quotient overlaps c1-n4 quotient mode %d' % n)
    ok(p.overlaps(flint.arb(modes[n]['M']['F_psi'])), 'c1-n4 pairing inside c1-n3 display mode %d' % n)
    print('Part C: mode %d, |p|/sqrt(d) = %s, strict floor %s (gap %.3e); p/d - 1 = %s'
          % (n, q.str(25), float(l), float((q - lq).mid()), (p / d - 1).str(5)))

# Part D
H2 = floors[1] ** 2 + floors[3] ** 2
ok(H2 == Fr(RES['H_lower_square_exact']), 'H^2 floor equals c1-n4 exact')
Hs = Fr(RES['H_strict_lower_exact'])
ok(Hs > 0 and Hs ** 2 < H2, 'strict H floor')
ok(Hs == Fr(529469576110512066428681, 10 ** 24), 'H floor value 0.529469576110512066428681')
NRM = J['N4392_comparison.json']
ok(NRM['raw_sha256'] == RES['raw_sha256'], 'N4-392 record binds the same raw file')
G0, G1, P2 = (Fr(NRM['norms'][k]['accepted_lower_exact']) for k in ('G0', 'G1', 'P2'))
ok(min(G0, G1, P2) > 0, 'component lower bounds positive')
E2sq = P2 ** 2 + 2 ** 14 * G1 ** 2 + 2 ** 18 * G0 ** 2 + Fr(20, 21) * 2 ** 18 * H2
ok(E2sq == Fr(RES['E2_lower_square_exact']), 'E2^2 floor equals c1-n4 exact (same four components)')
E2s = Fr(RES['E2_strict_lower_exact'])
ok(E2s == Fr(304196192960807, 500000000000) and E2s ** 2 < E2sq, 'strict E2 floor 608.392385921614')
U7 = Fr(J['N4252_result.json']['E_upper']['strict_upper_exact'])
ok(U7 == Fr(606820219, 10 ** 6) and Fr(RES['baseline007_E2_strict_upper_exact']) == U7, '007 strict upper 606.820219')
ok(J['N4252_result.json']['E_upper']['strict_bounds_verified'] is True, '007 bound verified flag')
ok(E2s > U7 and E2s - U7 == Fr(RES['strict_E2_separation_exact']) == Fr(786083460807, 500000000000),
   'separation 1.572166921614')
# the H component alone: without it the floor is below the 007 upper, so the dual bound is needed for the ordering
E2noH = P2 ** 2 + 2 ** 14 * G1 ** 2 + 2 ** 18 * G0 ** 2
ok(E2noH < U7 ** 2, 'without the H term the 016 floor is below the 007 upper bound')
Hneed = (U7 ** 2 - E2noH) / (Fr(20, 21) * 2 ** 18)
def dec(q, k):
    # q rounded down to k decimals, as a string (exact)
    s = str(q.numerator * 10 ** k // q.denominator).rjust(k + 1, '0')
    return s[:-k] + '.' + s[-k:]


print('Part D: H^2 >= %s, H > %s; E2(016)^2 >= %s, E2(016) > %s > %s >= E2(007)'
      % (dec(H2, 24), dec(Hs, 24), dec(E2sq, 9), dec(E2s, 12), dec(U7, 6)))
print('  without H: E2 floor %.6f < %.6f; the ordering needs H(016) > %.9f (floor %.9f, margin %.4f in H^2)'
      % (float(E2noH) ** 0.5, float(U7), float(Hneed) ** 0.5, float(Hs), float(H2 - Hneed)))

# Part E (FLOAT): rounded MID 32 displays of numerics_v15 section 5 (G0, G1, P2, H)
V15 = {'007': (0.3767, 3.439, 190.8, 0.6355), '013': (0.3722, 3.441, 191.2, 0.6313), '016': (0.3089, 3.727, 218.1, 0.6178),
       '017': (0.3209, 3.538, 200.5, 0.6153), '018': (0.3127, 3.856, 223.6, 0.6153), '019': (0.3251, 3.587, 202.2, 0.6142),
       '020': (0.3201, 3.913, 226.9, 0.6113), '021': (0.2996, 3.489, 203.5, 0.6096), '022': (0.2816, 3.554, 206.9, 0.6119),
       '023': (0.3228, 3.939, 247.9, 0.6121), '024': (0.3275, 3.680, 209.6, 0.6187), '025': (0.3051, 4.067, 245.1, 0.6251),
       '026': (0.2788, 3.627, 223.5, 0.6115), '027': (0.2762, 3.426, 199.7, 0.6101), '028': (0.2442, 3.260, 197.1, 0.6104)}
e2f = {k: (P2 ** 2 + 2 ** 14 * G1 ** 2 + 2 ** 18 * G0 ** 2 + (20 / 21) * 2 ** 18 * H ** 2) ** 0.5
       for k, (G0, G1, P2, H) in V15.items()}
below = sorted(k for k in e2f if k != '007' and e2f[k] < e2f['007'])
print('Part E (FLOAT, display arithmetic, not bounds): E2 =', ', '.join('%s %.2f' % (k, v) for k, v in e2f.items()))
print('  FLOAT E2 below 007\'s FLOAT value for:', ', '.join(below))
ok(below == ['013', '017', '021', '022', '027', '028'], 'FLOAT list')
print('checks passed', n_ok, '; elapsed %.1f s' % (time.time() - t0))
print('RESULT PASS')
