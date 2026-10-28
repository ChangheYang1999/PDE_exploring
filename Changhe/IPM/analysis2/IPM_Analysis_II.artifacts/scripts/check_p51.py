"""Third computation for verification topic 51 (exterior transfer of the annular negative-norm witnesses).

1. The weight identity. For a = w_T/w_R with w_R = (1 + z/R^2)^(-q), z = |X|^2, the radial Laplacian is
   Delta a = 4 (z a'' + a'); the script differentiates symbolically (sympy) and checks
   Delta a/a = 4 q D0 [z^2 + q D0 z - T^2 R^2]/[(T^2 + z)^2 (R^2 + z)^2], D0 = R^2 - T^2, and the decomposition
   z^2 + q D0 z - T^2 R^2 = (z - T^2)(z + T^2 + q D0) + (q - 1) T^2 D0.
2. The Dirichlet energy of phi = chi(r/T) sum a_m sin(m theta), chi = (t - 1)^2 (2 - t)^2 on [1, 2], is
   ||D phi||^2 = pi sum a_m^2 (int_1^2 chi'^2 t dt + m^2 int_1^2 chi^2/t dt); both integrals are formed exactly
   (the second as a rational plus a rational multiple of log 2) and enclosed in interval arithmetic.
3. With P_T = pairing - remainder (lower end) from the audited C9 rows, l_T = P_T/||D phi|| and
   N_(s,R)(F) > 2^(53/2) l_T/(1 + 2^-12 C_T), C_T = 41/(5T) + 17/T^2 + 327/(5T^3) + 1309/(10T^4) + 924/(5T^5),
   for all R >= T. The recorded integers of topic 51 are compared with these enclosures (each must be below the lower end),
   and the gap over 2^-30 is formed.

Usage: python3 check_p51.py VERIFICATION_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, hashlib
from fractions import Fraction as Q
from decimal import Decimal
from pathlib import Path
import sympy as sp
from mpmath import iv
sys.set_int_max_str_digits(0)
iv.prec = 400
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
I = lambda q: iv.mpf(Q(q).numerator) / Q(q).denominator


def frac(t):
    sign, man, e, bc = t
    if not man:
        assert not e
        return Q(0)
    v = Q(int(man)) * Q(2) ** int(e)
    return -v if sign else v


lo = lambda x: frac(x._mpi_[0]); hi = lambda x: frac(x._mpi_[1])


def ball(s):
    s = s.strip(); assert s[0] == '[' and s[-1] == ']', s
    mid, rad = s[1:-1].split('+/-')
    mid, rad = Q(Decimal(mid.strip())), Q(Decimal(rad.strip())); assert rad >= 0
    return mid - rad, mid + rad


out = {'inputs': {}}
# 1. weight identity
z, T, R, q = sp.symbols('z T R q', positive=True)
a = ((1 + z / R ** 2) / (1 + z / T ** 2)) ** q
lap = 4 * (z * sp.diff(a, z, 2) + sp.diff(a, z))
D0 = R ** 2 - T ** 2
claim = 4 * q * D0 * (z ** 2 + q * D0 * z - T ** 2 * R ** 2) / ((T ** 2 + z) ** 2 * (R ** 2 + z) ** 2)
out['laplacian_formula'] = sp.simplify(lap / a - claim) == 0
out['bracket_decomposition'] = sp.expand(z ** 2 + q * D0 * z - T ** 2 * R ** 2
                                         - ((z - T ** 2) * (z + T ** 2 + q * D0) + (q - 1) * T ** 2 * D0)) == 0
out['ratio_at_most_one_for_R>=T'] = True    # (1 + z/R^2) <= (1 + z/T^2) and q > 0
print(out, flush=True)
assert out['laplacian_formula'] and out['bracket_decomposition']

# 2. Dirichlet energy
t = sp.symbols('t', positive=True)
chi = (t - 1) ** 2 * (2 - t) ** 2
J1 = sp.integrate(sp.expand(sp.diff(chi, t) ** 2 * t), (t, 1, 2))
J2 = sp.integrate(sp.expand(chi ** 2) / t, (t, 1, 2))
J2 = sp.nsimplify(sp.expand(J2))
assert J1 == sp.Rational(1, 35)
J2r = J2.subs(sp.log(2), 0); J2l = sp.expand((J2 - J2r) / sp.log(2))
assert J2r.is_Rational and J2l.is_Rational
out['int_chi_prime^2_t'] = str(J1); out['int_chi^2/t'] = f'{J2r} + ({J2l}) log 2'
tailp = ROOT / '05_tails/verification/state131_tail.json'
c9p = ROOT / 'numerics_audit/audit_c9_Q4.json'
for p in (tailp, c9p):
    out['inputs'][str(p.relative_to(ROOT))] = sha(p)
td = json.loads(tailp.read_text())
e = {int(m): Q(v) for m, v in td['E_coefficients']['1'].items()}
am = {m: v / (Q(1, 35) + Q(m * m, 630)) for m, v in e.items()}
I2 = I(Q(int(J2r.p), int(J2r.q))) + I(Q(int(J2l.p), int(J2l.q))) * iv.log(2)
E = iv.pi * sum((I(v * v) * (I(Q(1, 35)) + m * m * I2) for m, v in am.items()), iv.mpf(0))
G = iv.sqrt(E)
c9 = json.loads(c9p.read_text())
gl, gh = ball(c9['gradient_norm'])
out['gradient_norm'] = [float(lo(G)), float(hi(G))]
out['gradient_norm_overlaps_record'] = lo(G) <= gh and gl <= hi(G)
print('gradient norm', out['gradient_norm'], out['gradient_norm_overlaps_record'], flush=True)
assert out['gradient_norm_overlaps_record']

# 3. bounds
REC = {31: 35350195123380074757524496, 32: 152106025974381578784015837, 35: 12111707934138297389397188825}
REC_L = {31: 372474829674258475, 32: 1602697408584840334, 35: 127617579877087467912}
REC_GAP = {31: 114, 32: 116, 35: 123}
rows = []
for row in c9['rows']:
    p = int(row['R_power']); Tv = Q(2) ** p
    pl, ph = ball(row['pairing']); rl, rh = ball(row['remainder']); P = pl - rh; assert P > 0
    l = I(P) / G
    CT = Q(41, 5) / Tv + 17 / Tv ** 2 + Q(327, 5) / Tv ** 3 + Q(1309, 10) / Tv ** 4 + Q(924, 5) / Tv ** 5
    Nl = iv.sqrt(iv.mpf(2) ** 53) * l / (1 + I(CT) / 4096)
    gap = max(k for k in range(0, 200) if lo(Nl) > Q(2) ** (k - 30))
    rr = {'T_power': p, 'P_lower': float(P), 'l_lower': float(lo(l)), 'N_lower': float(lo(Nl)),
          'record_l_below': Q(REC_L[p]) < lo(l), 'record_N_below': Q(REC[p]) < lo(Nl),
          'record_N_tight': lo(Nl) - REC[p] < 1, 'gap_power_over_2^-30': gap, 'gap_agrees': gap == REC_GAP[p]}
    rows.append(rr); print(rr, flush=True)
out['rows'] = rows
assert all(r['record_l_below'] and r['record_N_below'] and r['gap_agrees'] for r in rows)
out['all_pass'] = True
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE')
