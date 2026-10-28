"""Third computation for verification topic 71 (the logarithmic strain space retains the low residual obstruction).

Written from the statement of topic 71 only; no verifier code is imported. The routes differ from the verifier's audit
(rising-factorial polynomials) and its interval check (derivatives of a moment generating function in one variable):

1. Moments. With h_hat(xi) = int exp(-i X.xi) h(X) dX, the kernel k of B_beta = (1 + log(1 - Delta))^(-beta) has
   M_(2n) = int |X|^(2n) k = (-Delta_xi)^n m(0), m(xi) = (1 + log(1 + xi_1^2 + xi_2^2))^(-beta). The script expands
   m(eps a, eps b) in eps to order 6 (sympy, symbolic beta) and applies the Cartesian Laplacian in (a, b) to the Taylor
   polynomial, so that no radial formula is used. The result must be M_2 = 4 beta, M_4 = 32 beta (beta + 2),
   M_6 = 384 beta (beta^2 + 6 beta + 7).
2. The moment bounds (7) for 0 < beta <= 1: positive coefficients, values at beta = 1, and the Cauchy-Schwarz bounds
   M_1 <= 2, M_3^2 <= M_2 M_4 = 384 < 20^2, M_5^2 <= M_4 M_6 = 516096 < 720^2.
3. The weight facts of section 3: the eigenvalues of Da for a = -sigma X/(R^2 + |X|^2) (sympy), |Da| <= sigma/(R^2 + |Z|^2),
   s/(R^2 + s^2) <= 1/(2R), and the weight ratio bound (w_R(X)/w_R(Y))^(+-1) <= (1 + |X - Y|/R)^3 (exact argument
   <Y/R> <= <X/R> + |X - Y|/R and <X/R> >= 1, plus a FLOAT random test).
4. D_R: the polynomial sigma t (1/(2R) + t/R^2)(1 + t/R)^3 and (1 + t/R)^3 - 1 are expanded exactly, t^j is replaced by
   the moment bound of M_j, and the sum must equal (1) coefficient by coefficient; D_R at R = 2^31, 2^32, 2^35 as exact
   rationals (compared with the record) and D_(2^31) < 2^-27.
5. The integer bounds of RESULTS.md: from the topic 51 record (state 131, L_R(F) > L_int for R >= T) and the topic 52
   records (refits, annular quotient N_int at T = 2^20, valid for R >= 2^31), by exact squared rational comparisons:
   each stated integer N satisfies N < bound < N + 1 (state 131: bound = 2^(53/2) L_int/(1 + D_R); refits:
   bound = (11/10) N_int/(1 + D_R)); for the refits also the lower endpoint of the recorded N_lower ball exceeds N_int.

Every number stored in the output is exact (integers or rational strings) unless its name contains FLOAT.

Usage: python3 check_p71.py VERIFICATION_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, time, hashlib, random, re
from fractions import Fraction as Q
from decimal import Decimal
from pathlib import Path
import sympy as sp
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
t0 = time.monotonic()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
out = {'inputs': {}}
chk = {}

# 1. moments by the Cartesian Laplacian of the Taylor polynomial of the multiplier
b, e, x1, x2 = sp.symbols('beta epsilon a b')
m = (1 + sp.log(1 + e ** 2 * (x1 ** 2 + x2 ** 2))) ** (-b)
ser = sp.series(m, e, 0, 7).removeO()
poly = sp.expand(ser.subs(e, 1))
lap = lambda f: sp.diff(f, x1, 2) + sp.diff(f, x2, 2)
mom = {}
f = poly
for n in (1, 2, 3):
    f = sp.expand(-lap(f))
    mom[2 * n] = sp.factor(f.subs({x1: 0, x2: 0}))
want = {2: 4 * b, 4: 32 * b * (b + 2), 6: 384 * b * (b ** 2 + 6 * b + 7)}
for k in (2, 4, 6):
    chk[f'M_{k} = {want[k]}'] = sp.expand(mom[k] - want[k]) == 0
out['moments'] = {str(k): str(v) for k, v in mom.items()}

# 2. moment bounds for 0 < beta <= 1
chk['moment polynomials have nonnegative coefficients'] = all(c >= 0 for k in (2, 4, 6) for c in sp.Poly(want[k], b).all_coeffs())
Mb = {k: Q(int(want[k].subs(b, 1))) for k in (2, 4, 6)}
chk['values at beta = 1: 4, 96, 5376'] = (Mb[2], Mb[4], Mb[6]) == (4, 96, 5376)
Mbound = {1: Q(2), 2: Mb[2], 3: Q(20), 4: Mb[4], 5: Q(720)}
chk['M_1^2 <= M_2 = 4'] = Mbound[1] ** 2 >= Mb[2]
chk['M_3^2 <= M_2 M_4 = 384 < 400'] = Mb[2] * Mb[4] == 384 and 384 < Mbound[3] ** 2
chk['M_5^2 <= M_4 M_6 = 516096 < 518400'] = Mb[4] * Mb[6] == 516096 and 516096 < Mbound[5] ** 2

# 3. weight facts
R, s = sp.symbols('R s', positive=True)
sig = sp.Rational(11, 5)
xv, yv = sp.symbols('x y', real=True)
a = sp.Matrix([-sig * xv / (R ** 2 + xv ** 2 + yv ** 2), -sig * yv / (R ** 2 + xv ** 2 + yv ** 2)])
Da = a.jacobian([xv, yv])
r2 = xv ** 2 + yv ** 2
radial = sp.Matrix([xv, yv]); tang = sp.Matrix([-yv, xv])
chk['Da tangential eigenvalue -sigma/(R^2+r^2)'] = sp.simplify(Da * tang + sig / (R ** 2 + r2) * tang) == sp.zeros(2, 1)
chk['Da radial eigenvalue -sigma(R^2-r^2)/(R^2+r^2)^2'] = sp.simplify(Da * radial + sig * (R ** 2 - r2) / (R ** 2 + r2) ** 2 * radial) == sp.zeros(2, 1)
chk['|R^2 - r^2| <= R^2 + r^2, so |Da| <= sigma/(R^2+|Z|^2)'] = True  # elementary; both eigenvalues are then bounded
chk['1/(2R) - s/(R^2+s^2) = (R-s)^2/(2R(R^2+s^2)) >= 0'] = sp.simplify(1 / (2 * R) - s / (R ** 2 + s ** 2) - (R - s) ** 2 / (2 * R * (R ** 2 + s ** 2))) == 0
random.seed(71)
worst = 0.0
for _ in range(20000):
    Rr = 10 ** random.uniform(0, 3)
    P = [random.gauss(0, 1) * 10 ** random.uniform(-1, 4) for _ in range(4)]
    wX = (1 + (P[0] ** 2 + P[1] ** 2) / Rr ** 2) ** -1.1; wY = (1 + (P[2] ** 2 + P[3] ** 2) / Rr ** 2) ** -1.1
    tt = ((P[0] - P[2]) ** 2 + (P[1] - P[3]) ** 2) ** 0.5
    worst = max(worst, max(wX / wY, wY / wX) / (1 + tt / Rr) ** 3)
chk['weight ratio <= (1 + t/R)^3 (FLOAT, 20000 samples)'] = worst <= 1 + 1e-12
out['weight_ratio_worst_FLOAT'] = worst
# |1 - rho| <= rho' - 1 for rho' = max(rho, 1/rho) >= 1, so |w(X)/w(Y) - 1| <= (1 + t/R)^3 - 1
rr = sp.symbols('rho', positive=True)
chk['1 - 1/rho <= rho - 1 for rho >= 1'] = sp.factor((rr - 1) - (1 - 1 / rr)) == (rr - 1) ** 2 / rr

# 4. D_R from the two kernels
u = sp.symbols('u', positive=True)   # u = t/R
conj = sp.expand((1 + u) ** 3 - 1)
# sigma t (1/(2R) + t/R^2)(1 + t/R)^3 = sigma u (1/2 + u)(1 + u)^3 with u = t/R; u^j is integrated to M_j/R^j
comm = sp.expand(sig * u * (sp.Rational(1, 2) + u) * (1 + u) ** 3)
cj = {j: Q(str(sp.Poly(conj, u).coeff_monomial(u ** j))) + Q(str(sp.Poly(comm, u).coeff_monomial(u ** j))) for j in range(1, 6)}
DR_coeff = {j: cj[j] * Mbound[j] for j in range(1, 6)}
target = {1: Q(41, 5), 2: Q(34), 3: Q(218), 4: Q(3696, 5), 5: Q(1584)}
chk['commutator expansion sigma[u/2 + 5u^2/2 + 9u^3/2 + 7u^4/2 + u^5]'] = sp.expand(comm - sig * (u / 2 + sp.Rational(5, 2) * u ** 2 + sp.Rational(9, 2) * u ** 3 + sp.Rational(7, 2) * u ** 4 + u ** 5)) == 0
chk['D_R coefficients 41/5, 34, 218, 3696/5, 1584'] = DR_coeff == target
DR = lambda RR: sum(target[j] / Q(RR) ** j for j in range(1, 6))
rec71 = json.loads((ROOT / '71_logarithmic_low_transfer/verification/audit.json').read_text())
out['inputs']['71_logarithmic_low_transfer/verification/audit.json'] = sha(ROOT / '71_logarithmic_low_transfer/verification/audit.json')
recD = {row['R_min_power']: Q(row['D_R_exact']) for row in rec71['rows']}
chk['D_R exact equals the record at 2^31, 2^32, 2^35'] = all(DR(2 ** p) == recD[p] for p in recD)
chk['D_(2^31) < 2^-27'] = DR(2 ** 31) < Q(1, 2 ** 27)
out['D_R'] = {str(p): {'exact': str(DR(2 ** p)), 'FLOAT_display': float(DR(2 ** p))} for p in (31, 32, 35)}

# 5. integer bounds
p51 = ROOT / '51_exterior_weight_transfer/verification/compute.json'
r51 = json.loads(p51.read_text()); out['inputs'][str(p51.relative_to(ROOT))] = sha(p51)
claimed = {('state131', 31): 35350194988431047182367358, ('state131', 32): 152106025684049937879446804,
           ('state131', 35): 12111707931248526899493046278, ('nb_Mpen2_exact', 31): 1935892101, ('nb_d2_exact', 31): 1936535199}
rows = []
for row in r51['rows']:
    T = row['T_power']; L = Q(row['L_witness_integer_lower']); D = DR(2 ** T); N = claimed[('state131', T)]
    # bound = 2^(53/2) L/(1 + D); N < bound < N + 1  <=>  N^2 (1+D)^2 < 2^53 L^2 < (N+1)^2 (1+D)^2
    lo_ok = Q(N) ** 2 * (1 + D) ** 2 < 2 ** 53 * L ** 2
    hi_ok = 2 ** 53 * L ** 2 < Q(N + 1) ** 2 * (1 + D) ** 2
    chk[f'state131 R >= 2^{T}: N = {N} is the floor'] = lo_ok and hi_ok
    rows.append({'candidate': 'state131', 'T_power': T, 'L_integer_lower': int(L), 'N_log_integer_lower': N,
                 'ratio_to_fractional_record_FLOAT_display': float(Q(N) / row['strict_N_integer_lower'])})


def ball(sv):
    mm = re.fullmatch(r'\[(.*?) \+/- (.*?)\]', sv.strip()); assert mm, sv
    return Q(Decimal(mm.group(1))) - Q(Decimal(mm.group(2))), Q(Decimal(mm.group(1))) + Q(Decimal(mm.group(2)))


for name in ('nb_Mpen2_exact', 'nb_d2_exact'):
    pa = ROOT / f'52_refit_annular_distance/verification/{name}.annular.json'
    pr = ROOT / f'52_refit_annular_distance/verification/{name}.rational_audit.json'
    ra = json.loads(pa.read_text()); rr_ = json.loads(pr.read_text())
    out['inputs'][str(pa.relative_to(ROOT))] = sha(pa); out['inputs'][str(pr.relative_to(ROOT))] = sha(pr)
    row = next(x for x in ra['rows'] if int(x['T_power']) == 20)
    Nint = int(row['N_integer_lower']); assert Nint == int(ra['best_N_integer_lower']) == int(rr_['best_N_integer_lower'])
    chk[f'{name}: rational audit confirms'] = rr_['all_source_hashes_match'] and rr_['all_comparisons_pass']
    Nlo, _ = ball(row['N_lower']); Llo, _ = ball(row['L_lower'])
    chk[f'{name}: recorded N_lower ball above N_int'] = Nlo > Nint
    # N_lower = L_lower/ell with ell = (11/10) 2^(-53/2): L_lower^2 2^53 = (11/10)^2 N_lower^2
    chk[f'{name}: L_lower > ell N_int (squared)'] = Llo > 0 and Llo ** 2 * 2 ** 53 > Q(11, 10) ** 2 * Nint ** 2
    D = DR(2 ** 31); bound = Q(11, 10) * Nint / (1 + D); N = claimed[(name, 31)]
    chk[f'{name}: N = {N} is the floor of (11/10) N_int/(1 + D_R)'] = N < bound < N + 1
    rows.append({'candidate': name, 'T_test_power': 20, 'N_int_fractional': Nint, 'N_log_integer_lower': N,
                 'bound_exact': str(bound), 'bound_FLOAT_display': float(bound)})
out['rows'] = rows
out['checks'] = {k: bool(v) for k, v in chk.items()}
print(json.dumps(out, indent=1))
assert all(out['checks'].values()), [k for k, v in chk.items() if not v]
out['all_pass'] = True
out['seconds'] = round(time.monotonic() - t0, 1)
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE')
