"""Third computation for the annular distance of the checkpoint (verification topic 39) and the leading-moment
condition of the fixed-tail rigidity theorem (verification topic 40).

Topic 39. The test coefficients a_m = e_m/(1/35 + m^2/630) are rebuilt as exact rationals from the leading residual
sine coefficients e_m, with S0 = sum |a_m|, S1 = sum m |a_m|, Z = S0/16 and C = 91 S0/160 + S1/16. For each recorded
row (T = 2^31, 2^32, 2^35) the signed pairing P_T = pairing - remainder is read from the decimal ball strings of the
audited C9 record and turned into an exact rational interval; then, in mpmath interval arithmetic,
    H_T = 16 (2T)^(1/5), B_T = 104 (2T)^(1/5), V_T = 2 c T + 22 (2T)^(5/9), D_T = 186 T^(-4/9),
    A_T = 3 pi T^2 {H_T [V_T C/T + (2c + 1) Z] + B_T D_T Z},  Q_T = 3 pi T H_T B_T C,
and the largest dyadic q = 2^-k with P_T > A_T q + Q_T q^2 is found by exact comparison of interval endpoints.
The ball radius 5 * 2^-32 of the weighted theorem is tested in the same way.

The same rows are evaluated with the amplitude constants of topics 44 and 45, H_T = (2T)^(1/5)/12 and
B_T = 3 (2T)^(1/5)/16.

Topic 40. For the checkpoint and each of the nine exact references (the eight of topic 40 and d2) the leading
potential moments
sum_k b_(0,m,k) are formed as exact rationals and compared; the references must also share the exact exponent.

Usage: python3 check_p39_p40.py VERIFICATION_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, hashlib
from fractions import Fraction as Q
from decimal import Decimal
from pathlib import Path
from mpmath import iv, mp
sys.set_int_max_str_digits(0)
iv.prec = 400; mp.prec = 400
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
I = lambda q: iv.mpf(Q(q).numerator) / Q(q).denominator


def frac(t):
    """exact value of a raw mpf tuple (sign, mantissa, exponent, bitcount); man_exp alone drops the sign."""
    sign, man, e, bc = t
    if not man:
        assert not e, 'infinite or undefined endpoint'
        return Q(0)
    v = Q(int(man)) * Q(2) ** int(e)
    return -v if sign else v


L = lambda x: frac(x._mpi_[0]); U = lambda x: frac(x._mpi_[1])


def ball(s):
    """'[mid +/- rad]' -> exact rational interval (lo, hi)."""
    s = s.strip()
    assert s[0] == '[' and s[-1] == ']', s
    mid, rad = s[1:-1].split('+/-')
    mid, rad = Q(Decimal(mid.strip())), Q(Decimal(rad.strip()))
    assert rad >= 0
    return mid - rad, mid + rad


c = Q(4076476460239181, 2251799813685248)
out = {'inputs': {}}

# ---------- topic 39 ----------
tailp = ROOT / '05_tails/verification/state131_tail.json'
c9p = ROOT / 'numerics_audit/audit_c9_Q4.json'
recp = ROOT / '39_annular_distance/verification/compute_distance.json'
for p in (tailp, c9p, recp):
    out['inputs'][str(p.relative_to(ROOT))] = sha(p)
td = json.loads(tailp.read_text())
assert Q(td['leading_density_norm_squared_divided_by_pi']) > 0     # Theta is not identically zero
e = {int(m): Q(v) for m, v in td['E_coefficients']['1'].items()}
assert all(m % 2 == 1 and m > 0 for m in e)
am = {m: v / (Q(1, 35) + Q(m * m, 630)) for m, v in e.items()}
S0 = sum((abs(v) for v in am.values()), Q(0)); S1 = sum((m * abs(v) for m, v in am.items()), Q(0))
Z = S0 / 16; C = 91 * S0 / 160 + S1 / 16
rec = json.loads(recp.read_text())
same = (str(S0) == rec['S0'] and str(S1) == rec['S1'] and str(Z) == rec['Z'] and str(C) == rec['C']
        and {str(m): str(v) for m, v in am.items()} == rec['test_coefficients'])
out['test_constants_equal_record'] = same
out['Z_approx'] = float(Z); out['C_approx'] = float(C); out['harmonics'] = len(am)
print('test constants equal record:', same, float(Z), float(C), flush=True)
c9 = json.loads(c9p.read_text())
assert c9['Q'] == 4
rows = []
r0 = Q(5, 2 ** 32)
for row in c9['rows']:
    p = row['R_power']; T = iv.mpf(2) ** p
    pl, ph = ball(row['pairing']); rl, rh = ball(row['remainder'])
    Plo = pl - rh                                       # lower end of pairing - remainder
    assert Plo > 0
    t5 = (2 * T) ** (iv.mpf(1) / 5)
    H = 16 * t5; B = 104 * t5
    H45 = t5 / 12; B45 = 3 * t5 / 16                     # amplitude constants of topics 44 and 45
    V = 2 * I(c) * T + 22 * (2 * T) ** (iv.mpf(5) / 9); D = 186 * T ** (-iv.mpf(4) / 9)
    A = 3 * iv.pi * T * T * (H * (V * I(C) / T + (2 * I(c) + 1) * I(Z)) + B * D * I(Z))
    Qt = 3 * iv.pi * T * H * B * I(C)
    A45 = 3 * iv.pi * T * T * (H45 * (V * I(C) / T + (2 * I(c) + 1) * I(Z)) + B45 * D * I(Z))
    Q45 = 3 * iv.pi * T * H45 * B45 * I(C)
    k45 = next(k for k in range(100) if Plo > U(A45) * Q(1, 2 ** k) + U(Q45) * Q(1, 4 ** k))
    test = lambda q: Plo > U(A) * q + U(Qt) * q * q
    k = next(k for k in range(100) if test(Q(1, 2 ** k)))
    fails_next = not (Plo > L(A) * Q(1, 2 ** (k - 1)) + L(Qt) * Q(1, 2 ** (2 * k - 2)))
    rr = {'T_power': p, 'P_lower_approx': float(Plo), 'A_approx': float(L(A)), 'Q_approx': float(L(Qt)),
          'dyadic_exponent': k, 'next_larger_radius_fails': fails_next, 'excludes_ball_5_2^-32': test(r0),
          'dyadic_exponent_amp44': k45}
    rec_row = next(x for x in rec['rows'] if x['T_power'] == p)
    rr['agrees_with_record'] = (rec_row['dyadic_exponent'] == k and rec_row['excludes_current_ball'] == rr['excludes_ball_5_2^-32'])
    rows.append(rr); print(rr, flush=True)
out['topic39_rows'] = rows
assert same and all(r['agrees_with_record'] and r['dyadic_exponent'] == 22 and r['excludes_ball_5_2^-32'] for r in rows)
out['topic39_radius_2^-22_at_T_2^31_2^32_2^35'] = True
assert [r['dyadic_exponent_amp44'] for r in rows] == [14, 14, 15]
out['topic45_radius_2^-14_at_T_2^31_2^32_and_2^-15_at_T_2^35'] = True

# ---------- topic 40 ----------
def coeffs(name):
    if name == 'state131':
        p = ROOT / 'source_audit/state131_exact.json'
    elif name == 'nb_b6_exact':
        p = ROOT / '36_b6_candidates/verification/nb_b6_exact.audit.json'
    else:
        p = ROOT / f'19_nb_candidates/verification/{name}.audit.json'
    d = json.loads(p.read_text()); out['inputs'][str(p.relative_to(ROOT))] = sha(p)
    cl = d['exact_parameters']['cl'] if name == 'state131' else d['cl']
    mom = {}
    for (j, m, k), v in zip(d['canonical_order'], d['canonical_coefficients']):
        if j == 0:
            mom[m] = mom.get(m, Q(0)) + Q(v)
    return Q(cl), {m: v for m, v in mom.items() if v != 0}


c0, m0 = coeffs('state131')
assert c0 == c and m0
res = {}
for name in ['nb_stableA2_exact', 'nb_stableA3_exact', 'nb_stableA4_exact', 'nb_stableA5_exact', 'nb_Mpen_exact',
             'nb_A6dpen_exact', 'nb_Mpen2_exact', 'nb_b6_exact', 'nb_d2_exact']:
    cn, mn = coeffs(name)
    res[name] = {'same_exponent': cn == c, 'same_leading_moments': mn == m0, 'nonzero_moments': len(mn)}
    print(name, res[name], flush=True)
out['topic40_leading_moments'] = res
out['checkpoint_nonzero_leading_moments'] = len(m0)
assert all(v['same_exponent'] and v['same_leading_moments'] for v in res.values())
out['topic40_all_nine_share_exponent_and_leading_moments'] = True
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE')
