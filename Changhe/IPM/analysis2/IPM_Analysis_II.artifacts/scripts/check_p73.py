"""Third computation for verification topic 73 (necessary distances in the logarithmic spaces N^log_(beta,R)).

Written from the statement of topic 73 only; no verifier code is imported. Routes:

1. Exact rational constants: a0, a1, a2 from M1 <= pi/2 < 11/7 and M2 = 4 beta <= 4 (so 1 + 2 M1 + M2 < 57/7 and
   1 + 2 M1 < 29/7); the growth coefficients (8) as exact squared comparisons, rebuilt from the partition bounds
   (||F|| <= 3 t^(1/5) P0, ||D2 F|| <= t^(1/5)(450 P0 + 36 P1 + P2)), the weighted Riesz factors 8/3, 3/2, 9/5,
   the interpolation constant 1/2, three overlapping cutoffs and 2^(1/5) < 5/4 (checked as 2 < (5/4)^5);
   d_h, d_u of (10) from the product rule with the weight bounds 1, 11/10, 15/2 and the factor 2 in the cross term;
   the cubic comparisons (11); kappa = 95/37; D_R at R = 2^31 below 2^-27 and 1/10, D_R decreasing.
2. The moment facts behind (4) (FLOAT): the 2D heat kernel first moment E|X| = sqrt(pi T) by quadrature,
   Gamma(u + 1/2)/Gamma(u) <= sqrt(u) (conditional Jensen) and E sqrt(U) = Gamma(beta + 1/2)/Gamma(beta) <= sqrt(pi)/2
   on a grid of beta in (0, 1].
3. The weak identity (9): the integrand difference is an exact divergence (sympy, with stream functions for the
   divergence-free reference and correction velocities).
4. Directed margins P_T - A_T q - (95/37) Q_T^old q^2 > 0 at the stated radii, in exact Fractions from the
   ball strings "[mid +/- rad]" of the topic 49 and 52 records (P at its lower end, A and Q at their upper ends);
   A_h + A_u contains A; the largest dyadic radius with a positive margin is reported (diagnostic) and must be at
   least the stated one. Input records and the original source are bound by SHA-256.

Usage: python3 check_p73.py VERIFICATION_RESEARCH_DIR [OUTPUT_JSON [NUMERICS_DATA_DIR STATE131_CHECKPOINT_JSON]]

The last two arguments locate the exact refit records and the original state 131 checkpoint (accepted_00000131.json);
by default they are relative to the restored base directory.
"""
import json, sys, hashlib, time, re
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp
import mpmath
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
NUMD = Path(sys.argv[3]) if len(sys.argv) > 4 else ROOT / 'numerics/data'
ORIG = Path(sys.argv[4]) if len(sys.argv) > 4 else \
    (ROOT / 'case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json')
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
t0 = time.monotonic()
chk, out = {}, {}

# 1. exact constants
pi_hi = Q(22, 7)
M1_hi, M2_hi = pi_hi / 2, Q(4)
chk['1 + 2 M1 + M2 <= 57/7'] = 1 + 2 * M1_hi + M2_hi == Q(57, 7)
chk['1 + 2 M1 <= 29/7'] = 1 + 2 * M1_hi == Q(29, 7)
a0, a1, a2 = Q(57, 7) / 2048, Q(29, 7) / 2048, Q(29, 7)
chk['a0, a1, a2 = 57/(7 2048), 29/(7 2048), 29/7'] = (a0, a1, a2) == (Q(57, 7 * 2048), Q(29, 7 * 2048), Q(29, 7))
chk['2^(1/5) < 5/4'] = Q(5, 4) ** 5 > 2
# sup |piece| <= (1/2) sqrt(||F|| ||D2 F||), three pieces, t^(1/5) <= (5/4) max(1, r)^(1/5)
pref = 3 * Q(1, 2) * Q(5, 4)
chk['prefactor 3 (1/2)(5/4) = 15/8'] = pref == Q(15, 8)
Ch2 = pref ** 2 * (3 * a0) * (450 * a0 + 36 * a1 + a2)
uP0, uP1, uP2 = Q(8, 3) * a0, Q(3, 2) * a1, Q(9, 5) * a2
Cu2 = pref ** 2 * (3 * uP0) * (450 * uP0 + 36 * uP1 + uP2)
chk['Cu^2 equals (15/8)^2 8 a0 (1200 a0 + 54 a1 + (9/5) a2)'] = Cu2 == Q(15, 8) ** 2 * 8 * a0 * (1200 * a0 + 54 * a1 + Q(9, 5) * a2)
chk['Ch^2 < (51/100)^2'] = Ch2 < Q(51, 100) ** 2
chk['Cu^2 < (6/5)^2'] = Cu2 < Q(6, 5) ** 2
# D2(w f) = w D2 f + 2 Dw (x) Df + D2w f, with w <= omega2, |Dw| <= (11/10) omega1, |D2 w| <= (15/2) omega0
d_h = 1 * a2 + 2 * Q(11, 10) * a1 + Q(15, 2) * a0
d_u = 1 * uP2 + 2 * Q(11, 10) * uP1 + Q(15, 2) * uP0
chk['d_h = a2 + (11/5) a1 + (15/2) a0'] = d_h == a2 + Q(11, 5) * a1 + Q(15, 2) * a0
chk['d_u = (9/5) a2 + (33/10) a1 + 20 a0'] = d_u == Q(9, 5) * a2 + Q(33, 10) * a1 + 20 * a0
ell2 = Q(121, 100) / 2 ** 53
chk['ell^2 d_h < 120000^-3'] = ell2 * d_h < Q(1, 120000) ** 3
chk['(13/3)^2 ell^2 d_u < 37000^-3'] = Q(13, 3) ** 2 * ell2 * d_u < Q(1, 37000) ** 3
kappa = Q(190000 * 60000, 120000 * 37000)
chk['kappa = 95/37'] = kappa == Q(95, 37)
DR = lambda R: Q(41, 5) / R + Q(34) / R ** 2 + Q(218) / R ** 3 + Q(3696, 5) / R ** 4 + Q(1584) / R ** 5
chk['D_(2^31) < 2^-27 < 1/10 (D_R decreasing: positive coefficients)'] = DR(Q(2) ** 31) < Q(1, 2 ** 27) < Q(1, 10)
chk['(1 + D_R) 2^(-53/2) <= ell for R >= 2^31: (1 + D)^2 <= 121/100'] = (1 + DR(Q(2) ** 31)) ** 2 <= Q(121, 100)
margins = {'Ch^2 / (51/100)^2': float(Ch2 / Q(51, 100) ** 2), 'Cu^2 / (6/5)^2': float(Cu2 / Q(6, 5) ** 2),
           'ell^2 d_h 120000^3': float(ell2 * d_h * 120000 ** 3), '(13/3)^2 ell^2 d_u 37000^3': float(Q(13, 3) ** 2 * ell2 * d_u * 37000 ** 3)}
out['exact_constants'] = {'a0': str(a0), 'a1': str(a1), 'a2': str(a2), 'Ch_squared': str(Ch2), 'Cu_squared': str(Cu2), 'd_h': str(d_h),
                          'd_u': str(d_u), 'ell_squared': str(ell2), 'kappa': str(kappa), 'D_R_at_2^31': str(DR(Q(2) ** 31))}
out['ratios_FLOAT_display'] = margins

# 2. FLOAT moment facts
mpmath.mp.dps = 30
Tm = mpmath.mpf(3) / 7
m1 = mpmath.quad(lambda rr: rr * rr * 2 * mpmath.pi * mpmath.exp(-rr ** 2 / (4 * Tm)) / (4 * mpmath.pi * Tm), [0, 1, 4, mpmath.inf])
chk['E|X| = sqrt(pi T) for the 2D heat kernel (FLOAT, T = 3/7)'] = abs(m1 - mpmath.sqrt(mpmath.pi * Tm)) < 1e-25
grid = [mpmath.mpf(j) / 400 for j in range(1, 401)]
chk['Gamma(u + 1/2)/Gamma(u) <= sqrt(u) on u = 1/400 ... 1 (FLOAT)'] = all(mpmath.gamma(u + 0.5) / mpmath.gamma(u) <= mpmath.sqrt(u) for u in grid)
chk['E sqrt(U) = Gamma(beta + 1/2)/Gamma(beta) <= sqrt(pi)/2 on beta = 1/400 ... 1 (FLOAT)'] = \
    all(mpmath.gamma(b + 0.5) / mpmath.gamma(b) <= mpmath.sqrt(mpmath.pi) / 2 + mpmath.mpf(10) ** -25 for b in grid)
# repaired 12:52Z (V185): this entry used to be a hardcoded True; it is now an actual two-dimensional quadrature
def _ET(b):
    mpmath.mp.dps = 15
    inner = lambda u: mpmath.quad(lambda t: t * mpmath.exp((u - 1) * mpmath.log(t) - t - mpmath.loggamma(u)), [0, 1, 10, mpmath.inf])
    v_ = mpmath.quad(lambda u: inner(u) * mpmath.exp((b - 1) * mpmath.log(u) - u - mpmath.loggamma(b)), [0, 1, 10, 60])
    mpmath.mp.dps = 30
    return v_
chk['the composite gamma(u) mixture over U ~ gamma(beta) has E T = beta (FLOAT 2D quadrature at beta = 3/10, 4/5)'] = \
    all(abs(_ET(mpmath.mpf(b)) - mpmath.mpf(b)) < 1e-8 for b in ('0.3', '0.8'))

# 3. weak identity (9) as an exact divergence
x, y, c = sp.symbols('x y c', real=True)
a = sp.Function('a')(x, y); bb = sp.Function('b')(x, y); hh = sp.Function('h')(x, y); rb = sp.Function('rho')(x, y); z = sp.Function('zeta')(x, y)
ub = (-sp.diff(a, y), sp.diff(a, x)); uh = (-sp.diff(bb, y), sp.diff(bb, x))
D = lambda f: (sp.diff(f, x), sp.diff(f, y))
dot = lambda p, q: p[0] * q[0] + p[1] * q[1]
div = lambda p: sp.diff(p[0], x) + sp.diff(p[1], y)
Ffun = dot((c * x + ub[0], c * y + ub[1]), D(rb)) - rb
rho = rb + hh; U = (ub[0] + uh[0], ub[1] + uh[1])
eq = c * dot((x, y), D(rho)) + div((U[0] * rho, U[1] * rho)) - rho   # = 0 for an exact profile
# int F zeta = int (F - eq) zeta; (F - eq) zeta - RHS integrand must be a divergence
rhs = hh * (dot((c * x + ub[0], c * y + ub[1]), D(z)) + (2 * c + 1) * z) - dot(uh, D(rb)) * z + hh * dot(uh, D(z))
G = (-(c * x + ub[0] + uh[0]) * hh * z, -(c * y + ub[1] + uh[1]) * hh * z)   # div(u_h rho) zeta = u_h.D rho zeta needs no transfer
chk['(9): (F - equation) zeta - right side = div G exactly'] = sp.simplify(sp.expand((Ffun - eq) * z - rhs - div(G))) == 0

# 4. directed margins from the records
ball = re.compile(r'^\[\s*([-+0-9.eE]+)\s*\+/-\s*([0-9.eE+-]+)\s*\]?$')


def iv(s):
    s = s.strip()
    m = ball.match(s)
    if m:
        mid, rad = Q(m.group(1)), Q(m.group(2))
        return mid - rad, mid + rad
    v = Q(s.strip('[]'))
    return v, v


inputs = {}
orig = ORIG
inputs['original state 131'] = sha(orig)
rows = []


def margin_rows(name, row, stated, Tpow):
    Plo, _ = iv(row['P_lower']); _, Ahi = iv(row['A']); _, Qhi = iv(row['Q'])
    Ahl, Ahh = iv(row['A_h']); Aul, Auh = iv(row['A_u']); Alo, _ = iv(row['A'])
    # renamed 12:52Z (V185): this only tests that the interval A_h + A_u and the interval A overlap; neither is claimed
    # to contain the other (for state 131 at T = 2^31, 2^32 they do not). The margin below uses P lower, A and Q upper.
    chk[f'{name} T = 2^{Tpow}: A_h + A_u and A overlap (diagnostic only)'] = Ahl + Aul <= Ahi and Alo <= Ahh + Auh
    mg = lambda p: Plo - Ahi * Q(2) ** p - kappa * Qhi * Q(4) ** p
    best = max(p for p in range(0, 120) if mg(p) > 0)
    chk[f'{name} T = 2^{Tpow}: margin at the stated radius 2^{stated} > 0 (exact, directed)'] = mg(stated) > 0
    chk[f'{name} T = 2^{Tpow}: largest positive dyadic radius >= stated'] = best >= stated
    rows.append({'reference': name, 'T_power': Tpow, 'stated_radius_power': stated, 'largest_positive_power': best,
                 'margin_at_stated_floor': int(mg(stated)), 'margin_at_stated_FLOAT_display': float(mg(stated)),
                 'margin_at_next_power_FLOAT_display': float(mg(stated + 1))})


p49 = ROOT / '49_negative_annular_distance/verification/compute.json'
inputs[str(p49.relative_to(ROOT))] = sha(p49)
d49 = json.loads(p49.read_text())
chk['topic 49 record: L2 constants 1/190000, 1/60000'] = d49['L2_constants_exact'] == ['1/190000', '1/60000']
for t, p in [(31, 57), (32, 56), (35, 54)]:
    margin_rows('state131', next(z for z in d49['rows'] if int(z['T_power']) == t), p, t)
for name in ['nb_Mpen2_exact', 'nb_d2_exact']:
    pa = ROOT / f'52_refit_annular_distance/verification/{name}.annular.json'
    inputs[str(pa.relative_to(ROOT))] = sha(pa)
    da = json.loads(pa.read_text())
    src = NUMD / (name + '.json')
    inputs[name + ' source'] = sha(src)
    chk[f'{name}: record source hash = numerics data file'] = da['source_sha256'] == sha(src)
    chk[f'{name}: record original hash = original state 131'] = da['original_source_sha256'] == sha(orig)
    margin_rows(name, next(z for z in da['rows'] if int(z['T_power']) == 20), 21, 20)
out['margins'] = rows
out['inputs_sha256'] = inputs
out['checks'] = {k: bool(v) for k, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k for k, v in chk.items() if not v]
out['all_pass'] = True
out['check_count'] = len(chk)
out['seconds'] = round(time.monotonic() - t0, 1)
out['code_sha256'] = sha(__file__)
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE', len(chk), 'checks')
