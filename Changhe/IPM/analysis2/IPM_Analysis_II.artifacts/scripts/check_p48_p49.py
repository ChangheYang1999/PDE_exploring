"""Third computation for verification topics 48 and 49, and for the selected centered square tests of topics 46, 47
and 48.

Part 1 (exact rational arithmetic). The constants of topic 48: d_h = a2 + (11/5) a1 + (15/2) a0,
d_u = (9/5) a2 + (33/10) a1 + 20 a0, the twelfth powers C_h^12 = (11/10)^4 d_h^8/(27 2^116) < 1000^-12 and
C_u^12 = (13/3)^4 (11/10)^4 d_u^8/(27 2^116) < 400^-12, and sigma^2 (1 + (sigma + 1)^2) < 225/4. The cubes of the
weighted L2 constants of topic 49, ell^2 d_h < 190000^-3 and (13/3)^2 ell^2 d_u < 60000^-3 with
ell^2 = 121/(100 2^53). The test-norm identity of topic 47, (2 I2 I0 + 2 I1^2)/(16/15)^4 = 2025/49.

Part 2. The test of topic 49, zeta_T = b(r/T) chi(r/T) sum a_m sin(m theta), b = (1 + t^2)^(-11/10),
chi = (t - 1)^2 (2 - t)^2, a_m = 630 e_m/(18 + m^2). The polynomial identities behind |chi| <= 1/16, |chi'| <= 1/2,
|chi''| <= 2 are checked exactly; |b| <= 1, |b'| <= 11/10, |b''| <= 231/100 on [1, 2] are checked by interval
evaluation of the closed forms on 256 subintervals; then |B'| <= 91/160 and |B''| <= 5191/1600, and
Z = S0/16, C1 = 91 S0/160 + S1/16, C2 = 6101 S0/1600 + 303 S1/320 + S2/16 are rebuilt and compared with the record.

Part 3. Annular comparisons from the audited C9 rows (P_T = pairing - remainder, lower end):
topic 48: g = (2T)^(1/5), W = (1 + 4T^2/R_min^2)^(11/10), H = min(2g/25, W/1000), B = min(11g/60, W/400),
    A = 3 pi T^2 [H (V C1/T + (2c + 1) Z) + B D Z], Q = 3 pi T H B C1, for R_min = 1 and 2^31;
topic 49 (R_min = 2^31): k = (11/5) T/(R_min^2 + T^2), V = 2cT + 22 (2T)^(5/9), V1 = sqrt(2) c + 22 T^(-4/9),
    D = 186 T^(-4/9), D1 = 186 T^(-13/9), m = 2c + 1,
    A_h = ell W sqrt(3 pi) [(V/T) C2 + (V1 + m + k V) C1 + k m T Z], A_u = (13/3) ell W sqrt(3 pi) [(D1 + k D) T Z + D C1],
    Q = W^2 C1/(190000 * 60000 T).
The largest dyadic q with P_T > A q + Q q^2 is found by exact comparison of interval endpoints.

Part 4. Point residual bounds of topic 48, N(F) >= 1000 w_R(X) |F(X)|, at the 93 points of topic 45, with
w_R(X) >= (1 + r^2)^(-11/10) for R >= 1 and w_R(X) >= (1 + r^2/2^62)^(-11/10) for R >= 2^31; F(X) is enclosed by the
bivariate interval jets of check_jet_distance.py.

Part 5. Centered square tests. On the square S of center X0 and half side delta, sup |V|, sup |DV|_F, sup |D rho|,
sup |D2 rho|_F and K = sup |D3 F|_F are bounded by Taylor expansion from the center jets with a box remainder of order 6
(the box jets enclose the order-6 coefficients on all of S); f = |F(X0) + delta^2 (F_xx + F_yy)(X0)/14|
- (sqrt(2)/21) delta^3 K. With the constants of topics 46, 47, 48 (see square_test below), the strict comparison
f > A q + Q q^2 is checked at the recorded radius and the largest dyadic radius is reported.

Usage: python3 check_p48_p49.py VERIFICATION_RESEARCH_DIR [OUTPUT_JSON]
"""
import json, sys, hashlib, time
from fractions import Fraction as Q
from decimal import Decimal
from math import comb, factorial
from pathlib import Path
ROOT = Path(sys.argv[1])
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(__file__).with_suffix('.json')
sys.argv = [sys.argv[0], str(ROOT)]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_jet_distance as cj                      # jets, sources and exact endpoint helpers
from mpmath import iv
sys.set_int_max_str_digits(0)
iv.prec = 320
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
I, lo, hi, mag, mig = cj.I, cj.lo, cj.hi, cj.mag, cj.mig
out = {'inputs': {}}
t_start = time.monotonic()


def ball(s):
    s = s.strip(); assert s[0] == '[' and s[-1] == ']', s
    mid, rad = s[1:-1].split('+/-')
    mid, rad = Q(Decimal(mid.strip())), Q(Decimal(rad.strip())); assert rad >= 0
    return mid - rad, mid + rad


def dyadic(test, rng=range(-80, 80)):
    """largest p in rng with test(2^p), assuming monotonicity; also returns whether 2^(p+1) fails."""
    ok = [p for p in rng if test(Q(2) ** p)]
    p = max(ok)
    return p, not test(Q(2) ** (p + 1))


# ---------- part 1: exact constants ----------
a0, a1, a2 = Q(2051, 4194304), Q(1025, 2097152), Q(1025, 1024)
d_h = a2 + Q(11, 5) * a1 + Q(15, 2) * a0
d_u = Q(9, 5) * a2 + Q(33, 10) * a1 + 20 * a0
assert d_h == Q(8436585, 8388608) and d_u == Q(7604905, 4194304)
Ch12 = Q(11, 10) ** 4 * d_h ** 8 / (27 * Q(2) ** 116)
Cu12 = Q(13, 3) ** 4 * Q(11, 10) ** 4 * d_u ** 8 / (27 * Q(2) ** 116)
sig = Q(11, 5)
p1 = {'d_h': str(d_h), 'd_u': str(d_u),
      'C_h^12<1000^-12': Ch12 < Q(1, 1000 ** 12), 'C_u^12<400^-12': Cu12 < Q(1, 400 ** 12),
      'C_h_approx': float(Ch12) ** (1 / 12), 'C_u_approx': float(Cu12) ** (1 / 12),
      'sigma^2(1+(sigma+1)^2)': str(sig ** 2 * (1 + (sig + 1) ** 2)),
      'hessian_weight_bound_15/2': sig ** 2 * (1 + (sig + 1) ** 2) < Q(225, 4)}
ell2 = Q(121, 100 * 2 ** 53)
bh3 = ell2 * d_h; bu3 = Q(13, 3) ** 2 * ell2 * d_u
p1.update({'ell^2 d_h<190000^-3': bh3 < Q(1, 190000 ** 3), '(13/3)^2 ell^2 d_u<60000^-3': bu3 < Q(1, 60000 ** 3),
           'b_h_approx': float(bh3) ** (1 / 3), 'b_u_approx': float(bu3) ** (1 / 3),
           'b_h_ratio_to_1/190000': float(bh3 * 190000 ** 3) ** (1 / 3), 'b_u_ratio_to_1/60000': float(bu3 * 60000 ** 3) ** (1 / 3)})


def pint(coef, lo_, hi_):
    """exact integral of the polynomial with coefficient list coef (ascending) over [lo_, hi_]."""
    return sum((cf * (Q(hi_) ** (k + 1) - Q(lo_) ** (k + 1)) / (k + 1) for k, cf in enumerate(coef)), Q(0))


def pmul(p, q):
    r = [Q(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i + j] += x * y
    return r


pder = lambda p: [k * p[k] for k in range(1, len(p))]
phi = [Q(1), Q(0), Q(-2), Q(0), Q(1)]                      # (1 - t^2)^2
I0 = pint(pmul(phi, phi), -1, 1); I1 = pint(pmul(pder(phi), pder(phi)), -1, 1)
I2 = pint(pmul(pder(pder(phi)), pder(pder(phi))), -1, 1)
assert (pint(phi, -1, 1), I0, I1, I2) == (Q(16, 15), Q(256, 315), Q(256, 105), Q(128, 5))
p1['topic47_d3_identity'] = (2 * I2 * I0 + 2 * I1 ** 2) / Q(16, 15) ** 4 == Q(2025, 49)
p1['topic46_second_moment'] = pint(pmul([Q(0), Q(0), Q(1)], phi), -1, 1) == Q(16, 105)
out['part1_constants'] = p1
print('part 1', p1, flush=True)
assert all(v for k, v in p1.items() if isinstance(v, bool))

# ---------- part 2: the test of topic 49 ----------
tailp = ROOT / '05_tails/verification/state131_tail.json'
c9p = ROOT / 'numerics_audit/audit_c9_Q4.json'
r49p = ROOT / '49_negative_annular_distance/verification/compute.json'
r48p = ROOT / '48_negative_energy_amplitudes/verification/residual_annular.json'
for p in (tailp, c9p, r49p, r48p):
    out['inputs'][str(p.relative_to(ROOT))] = sha(p)
td = json.loads(tailp.read_text())
e = {int(m): Q(v) for m, v in td['E_coefficients']['1'].items()}
am = {m: 630 * v / (18 + m * m) for m, v in e.items()}
S0 = sum((abs(v) for v in am.values()), Q(0)); S1 = sum((m * abs(v) for m, v in am.items()), Q(0))
S2 = sum((m * m * abs(v) for m, v in am.items()), Q(0))
Z = S0 / 16; C1 = Q(91, 160) * S0 + S1 / 16; C2 = Q(6101, 1600) * S0 + Q(303, 320) * S1 + S2 / 16
# chi = (t-1)^2 (2-t)^2 = (1/4 - u^2)^2 with u = t - 3/2: check the identities chi' = 4u^3 - u, chi'' = 12u^2 - 1
chi_t = pmul(pmul([Q(-1), Q(1)], [Q(-1), Q(1)]), pmul([Q(2), Q(-1)], [Q(2), Q(-1)]))
def compose_shift(p, s):                                    # coefficients of p(u + s) in u
    r = [Q(0)] * len(p)
    for k, cf in enumerate(p):
        for i in range(k + 1):
            r[i] += cf * comb(k, i) * s ** (k - i)
    return r
chi_u = compose_shift(chi_t, Q(3, 2))
p2 = {'chi_is_(1/4-u^2)^2': chi_u == [Q(1, 16), Q(0), Q(-1, 2), Q(0), Q(1)],
      'chi_prime_is_4u^3-u': compose_shift(pder(chi_t), Q(3, 2)) == [Q(0), Q(-1), Q(0), Q(4)],
      'chi_second_is_12u^2-1': compose_shift(pder(pder(chi_t)), Q(3, 2)) == [Q(-1), Q(0), Q(12)]}
# |chi| <= 1/16 since 0 <= 1/4 - u^2 <= 1/4; |chi'| = 4|u|(1/4 - u^2) <= 4 (1/2)(1/4) = 1/2; chi'' in [-1, 2].
bmax = [Q(0)] * 3
for j in range(256):
    t = iv.mpf([I(1 + Q(j, 256)), I(1 + Q(j + 1, 256))])
    w = 1 + t * t
    vals = [w ** (-iv.mpf(11) / 10), I(Q(11, 5)) * t * w ** (-iv.mpf(21) / 10),
            I(Q(11, 5)) * w ** (-iv.mpf(31) / 10) * (I(Q(16, 5)) * t * t - 1)]
    bmax = [max(bm, mag(v)) for bm, v in zip(bmax, vals)]
p2.update({'b_sup_upper': float(bmax[0]), 'b1_sup_upper': float(bmax[1]), 'b2_sup_upper': float(bmax[2]),
           '|b|<=1': bmax[0] <= 1, '|b_prime|<=11/10': bmax[1] <= Q(11, 10), '|b_second|<=231/100': bmax[2] <= Q(231, 100)})
Bp = Q(11, 10) * Q(1, 16) + 1 * Q(1, 2); Bpp = Q(231, 100) * Q(1, 16) + 2 * Q(11, 10) * Q(1, 2) + 1 * 2
p2['B_prime_bound'] = str(Bp); p2['B_second_bound'] = str(Bpp)
assert Bp == Q(91, 160) and Bpp == Q(5191, 1600)
# Hessian: T^2 |H|_F <= |B''| S0 + (3/2)(|B'| + |B|) S1 + |B'| S0 + |B| S2 on 1 <= t <= 2
assert C2 == Bpp * S0 + Q(3, 2) * (Bp + Q(1, 16)) * S1 + Bp * S0 + Q(1, 16) * S2 and C1 == Bp * S0 + Q(1, 16) * S1
r49 = json.loads(r49p.read_text())
p2['S012_equal_record'] = [str(S0), str(S1), str(S2)] == r49['S012_exact']
p2['Z_C1_C2_equal_record'] = [str(Z), str(C1), str(C2)] == r49['Z_C1_C2_exact']
p2['coefficients_equal_record'] = {str(m): str(v) for m, v in am.items()} == r49['test_coefficients']
p2.update({'S0': float(S0), 'S1': float(S1), 'S2': float(S2), 'Z': float(Z), 'C1': float(C1), 'C2': float(C2), 'harmonics': len(am)})
out['part2_test'] = p2
print('part 2', p2, flush=True)
assert all(v for k, v in p2.items() if isinstance(v, bool))

# ---------- part 3: annular comparisons ----------
c = Q(4076476460239181, 2251799813685248)
c9 = json.loads(c9p.read_text()); assert c9['Q'] == 4
r48 = json.loads(r48p.read_text())
ell = I(Q(11, 10)) / iv.sqrt(iv.mpf(2) ** 53)
rows48, rows49 = [], []
for row in c9['rows']:
    p = row['R_power']; T = iv.mpf(2) ** p
    pl, ph = ball(row['pairing']); rl, rh = ball(row['remainder']); P = pl - rh; assert P > 0
    V = 2 * I(c) * T + 22 * (2 * T) ** (iv.mpf(5) / 9); D = 186 * T ** (-iv.mpf(4) / 9)
    g = (2 * T) ** (iv.mpf(1) / 5)
    for rp in (0, 31):
        Rm = iv.mpf(2) ** rp; W = (1 + 4 * T * T / (Rm * Rm)) ** (iv.mpf(11) / 10)
        H = min(hi(2 * g / 25), hi(W / 1000)); B = min(hi(11 * g / 60), hi(W / 400))
        A = hi(3 * iv.pi * T * T * (I(H) * (V * I(C1) / T + (2 * I(c) + 1) * I(Z)) + I(B) * D * I(Z)))
        Qc = hi(3 * iv.pi * T * I(H) * I(B) * I(C1))
        k, nxt = dyadic(lambda q: P > A * q + Qc * q * q)
        rec = next(x for x in r48['annular'] if x['R_min_power'] == rp and x['T_power'] == p)
        rr = {'R_min_power': rp, 'T_power': p, 'P_lower': float(P), 'A_upper': float(A), 'Q_upper': float(Qc),
              'largest_dyadic_power': k, 'next_fails': nxt, 'record_exclusion_power': rec['exclusion_power'],
              'agrees': -k == rec['exclusion_power']}
        rows48.append(rr); print('topic48', rr, flush=True)
    rp = 31; Rm = iv.mpf(2) ** rp; assert p >= rp
    W = (1 + 4 * T * T / (Rm * Rm)) ** (iv.mpf(11) / 10); kk = I(Q(11, 5)) * T / (Rm * Rm + T * T)
    V1 = iv.sqrt(2) * I(c) + 22 * T ** (-iv.mpf(4) / 9); D1 = 186 * T ** (-iv.mpf(13) / 9); m = 2 * I(c) + 1
    s3p = iv.sqrt(3 * iv.pi)
    Ah = ell * W * s3p * ((V / T) * I(C2) + (V1 + m + kk * V) * I(C1) + kk * m * T * I(Z))
    Au = I(Q(13, 3)) * ell * W * s3p * ((D1 + kk * D) * T * I(Z) + D * I(C1))
    A = hi(Ah + Au); Qc = hi(W * W * I(C1) / (190000 * 60000 * T))
    k, nxt = dyadic(lambda q: P > A * q + Qc * q * q)
    rec = next(x for x in r49['rows'] if x['T_power'] == p)
    Ar, Qr = ball(rec['A']), ball(rec['Q'])
    rr = {'T_power': p, 'P_lower': float(P), 'A_h': float(hi(Ah)), 'A_u': float(hi(Au)), 'A_upper': float(A), 'Q_upper': float(Qc),
          'largest_dyadic_power': k, 'next_fails': nxt, 'record_power': rec['excluded_radius_power_positive'],
          'A_rel_diff_vs_record': float((A - Ar[1]) / Ar[1]), 'Q_rel_diff_vs_record': float((Qc - Qr[1]) / Qr[1]),
          'margin_at_record_radius': float(P - A * Q(2) ** rec['excluded_radius_power_positive']
                                           - Qc * Q(4) ** rec['excluded_radius_power_positive'])}
    rr['agrees'] = k == rec['excluded_radius_power_positive'] and rr['margin_at_record_radius'] > 0
    rows49.append(rr); print('topic49', rr, flush=True)
out['part3_topic48_annular'] = rows48; out['part3_topic49_annular'] = rows49
assert all(r['agrees'] for r in rows48 + rows49)
assert [r['largest_dyadic_power'] for r in rows49] == [57, 57, 55]
assert next(r for r in rows48 if r['R_min_power'] == 31 and r['T_power'] == 31)['largest_dyadic_power'] == -4

# ---------- part 4: point residual bounds of topic 48 ----------
TABLE48 = {'nb_A6dpen_exact': ('19.21489524', '185.70839626', 37), 'nb_Mpen2_exact': ('12.66133139', '123.57090072', 36),
           'nb_Mpen_exact': ('39.61351415', '451.71368471', 38), 'nb_b6_exact': ('1380.06796500', '5849.14554848', 42),
           'nb_stableA2_exact': ('5195.00167319', '26524.52060617', 44), 'nb_stableA3_exact': ('2850.12811221', '14449.35922962', 43),
           'nb_stableA4_exact': ('309.38916628', '2308.46168280', 41), 'nb_stableA5_exact': ('40.58323789', '516.41867227', 39),
           'state131': ('0.04750770', '3.58780259', 31), 'nb_d2_exact': ('5.47963704', '16.71364365', 34)}
part4 = {}; npts = 0
for name in cj.NAMES:
    pth, shs, cc, a0rec, terms = cj.source(name); out['inputs'][str(pth.relative_to(ROOT))] = shs
    best = [Q(0), Q(0)]; bestpt = [None, None]
    for xs, ys in cj.POINTS + cj.EXTRA_POINTS.get(name, []):
        X, Y = I(Q(xs)), I(Q(ys)); J = cj.Jets(4)
        F = cj.fields(J, cj.chi_jet(J, terms, cc, X, Y), cc, X, Y)['F'][0]
        r2 = Q(xs) ** 2 + Q(ys) ** 2
        for j, w in enumerate([(1 + I(r2)) ** (-iv.mpf(11) / 10), (1 + I(r2) / iv.mpf(2) ** 62) ** (-iv.mpf(11) / 10)]):
            Nl = 1000 * mig(F) * lo(w)
            if Nl > best[j]: best[j], bestpt[j] = Nl, [xs, ys]
        npts += 1
    t1, t31, gap = TABLE48[name]
    g31 = max(k for k in range(-40, 90) if best[1] > Q(2) ** (k - 30))
    part4[name] = {'R>=1_lower': float(best[0]), 'R>=1_point': bestpt[0], 'R>=2^31_lower': float(best[1]),
                   'R>=2^31_point': bestpt[1], 'gap_power_R>=2^31': g31,
                   'exceeds_record_R>=1': best[0] > Q(Decimal(t1)), 'exceeds_record_R>=2^31': best[1] > Q(Decimal(t31)),
                   'record_within_1e-8_relative': abs(best[0] - Q(Decimal(t1))) < Q(1, 10 ** 8) * best[0] + Q(1, 10 ** 8)
                   and abs(best[1] - Q(Decimal(t31))) < Q(1, 10 ** 8) * best[1] + Q(1, 10 ** 8),
                   'gap_agrees': g31 == gap}
    print('topic48 points', name, part4[name], flush=True)
out['part4_topic48_points'] = part4; out['part4_points_tested'] = npts
assert npts == 93 and all(v['exceeds_record_R>=1'] and v['exceeds_record_R>=2^31'] and v['gap_agrees'] for v in part4.values())


# ---------- part 5: centered square tests ----------
KT = 6


def sup_partial(Jx, uc, ub, beta, dl):
    """upper bound of sup_S |d^beta u|: Taylor from the center, order-KT coefficients enclosed on the box S."""
    bx, by = beta; nb = bx + by; tot = Q(0)
    for n in range(KT - nb + 1):
        for i in range(n + 1):
            ax, ay = i, n - i
            kpos = Jx.pos[ax + bx, ay + by]
            mult = (factorial(ax + bx) // factorial(ax)) * (factorial(ay + by) // factorial(ay))
            tot += mult * (mag(uc[kpos]) if n < KT - nb else mag(ub[kpos])) * dl ** n
    return tot


def sup_frob(Jx, comps, n, dl):
    s = Q(0)
    for uc, ub in comps:
        for i in range(n + 1):
            s += comb(n, i) * sup_partial(Jx, uc, ub, (i, n - i), dl) ** 2
    return hi(iv.sqrt(I(s)))


def square_test(name, xs, ys, dl, mode, qpow):
    pth, shs, cc, a0rec, terms = cj.source(name)
    x0, y0 = Q(xs), Q(ys); N = KT + 4
    t0 = (x0 * x0 + y0 * y0) / (1 + x0 * x0 + y0 * y0)
    Jt = cj.Jets(N); ft = cj.fields(Jt, cj.chi_jet(Jt, terms, cc, I(x0), I(y0), t0), cc, I(x0), I(y0))
    BX = iv.mpf([I(x0 - dl), I(x0 + dl)]); BY = iv.mpf([I(y0 - dl), I(y0 + dl)])
    Jb = cj.Jets(N); fb = cj.fields(Jb, cj.chi_jet(Jb, terms, cc, BX, BY, t0), cc, BX, BY)
    JM, J1 = ft['J'], ft['J1']; assert JM.N >= KT and J1.N == KT
    Vs = sup_frob(JM, [(ft['V1'], fb['V1']), (ft['V2'], fb['V2'])], 0, dl)
    V1s = sup_frob(JM, [(ft['V1'], fb['V1']), (ft['V2'], fb['V2'])], 1, dl)
    Ds = sup_frob(JM, [(ft['rho'], fb['rho'])], 1, dl)
    D1s = sup_frob(JM, [(ft['rho'], fb['rho'])], 2, dl)
    K3 = sup_frob(J1, [(ft['F'], fb['F'])], 3, dl)
    F = ft['F']; Tc = F[0] + I(dl * dl / 14) * 2 * (F[J1.pos[2, 0]] + F[J1.pos[0, 2]])
    f = mig(Tc) - hi(iv.sqrt(2) / 21 * I(dl ** 3) * I(K3))
    rm2 = (abs(x0) + dl) ** 2 + (abs(y0) + dl) ** 2
    gS = I(1) if rm2 <= 1 else I(rm2) ** (iv.mpf(1) / 10)
    W46 = (1 + I(rm2)) ** (iv.mpf(3) / 5); W47 = (1 + I(rm2)) ** (iv.mpf(11) / 10)
    a = I(Q(2051, 4194304)); m = abs(2 * I(cc) + 1); kk = I(Q(11, 10))
    d1 = I(Q(15, 4) / dl); d2 = 5 * iv.sqrt(6) / (7 * I(dl * dl)); e2 = I(Q(5, 7) / dl)
    dinf = 25 * iv.sqrt(6) / (32 * I(dl ** 3)); d3 = I(Q(45, 7) / dl ** 3)
    V, V1, D, D1 = I(Vs), I(V1s), I(Ds), I(D1s)
    H = hi(2 * gS / 25); B = hi(11 * gS / 60)
    if mode == '48':
        H = min(H, hi(W47 / 1000)); B = min(B, hi(W47 / 400))
    H, B = I(H), I(B)
    up = lambda x: hi(x)
    lin12 = min(up(H * V * d1), up(a * W46 * V * d2)) + min(up(H * m), up(a * W46 * m * e2))
    lin3 = min(up(B * D), up(I(Q(8, 3)) * a * W46 * D * e2))
    if mode == '46':
        A = lin12 + lin3
    else:
        Ah47 = up(ell * W47 * (V * d3 + (V1 + m + kk * V) * d2 + kk * m * e2))
        Au47 = up(I(Q(13, 3)) * ell * W47 * ((D1 + kk * D) * e2 + D * d2))
        A = min(lin12, Ah47) + min(lin3, Au47)
    Qc = min(up(H * B * d1), up(a * W46 * B * d2), up(I(Q(8, 3)) * a * W46 * H * d2),
             up(I(Q(8, 3)) * a * a * W46 * W46 * dinf))
    q = Q(2) ** qpow
    margin = f - A * q - Qc * q * q
    k, nxt = dyadic(lambda qq: f > A * qq + Qc * qq * qq, range(-60, 10))
    return {'reference': name, 'mode': mode, 'center': [xs, ys], 'half_side': str(dl), 'f_lower': float(f), 'A_upper': float(A),
            'Q_upper': float(Qc), 'sup_V': float(Vs), 'sup_DV': float(V1s), 'sup_Drho': float(Ds), 'sup_D2rho': float(D1s),
            'sup_D3F': float(K3), 'F_center': float(lo(F[0])), 'radius_power': qpow, 'margin_at_radius': float(margin),
            'excludes_radius': margin > 0, 'largest_dyadic_power': k, 'next_fails': nxt}


CLAIMS = [('nb_Mpen2_exact', '0', '4/5', Q(1, 1024), '46', -14), ('nb_d2_exact', '0', '2/5', Q(1, 1024), '46', -15),
          ('nb_Mpen2_exact', '0', '2/5', Q(5, 2048), '47', -11), ('nb_d2_exact', '0', '2/5', Q(1, 512), '47', -12),
          ('nb_Mpen2_exact', '0', '2/5', Q(1, 512), '48', -9), ('nb_d2_exact', '0', '2/5', Q(3, 2048), '48', -9)]
sq = []
for name, xs, ys, dl, mode, qp in CLAIMS:
    rr = square_test(name, xs, ys, dl, mode, qp); sq.append(rr); print('square', rr, flush=True)
out['part5_squares'] = sq
assert all(r['excludes_radius'] for r in sq)
out['all_pass'] = True
out['seconds'] = round(time.monotonic() - t_start, 1)
out['code_sha256'] = sha(Path(__file__))
OUT.write_text(json.dumps(out, indent=2) + '\n'); print('DONE')
