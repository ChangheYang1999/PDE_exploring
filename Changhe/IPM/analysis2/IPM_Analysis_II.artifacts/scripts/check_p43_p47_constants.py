"""Third computation for the exact constants of verification topics 43 (smooth commutator), 44 (amplitudes),
46 (centered tests) and 47 (weighted Bessel bound).

Exact rational arithmetic for every assembled constant; the Bessel and heat moments are evaluated in mpmath interval
arithmetic from the closed forms
    K_j = (s/2) 2^j Gamma(1+j/2) Gamma((j-s)/2) / Gamma(1-s/2),   M_j = 2^j Gamma(1+j/2) Gamma((j+s)/2) / Gamma(s/2),
    int r^j |D^2 J^-2| <= 2^j Gamma(1+j/2) (2+j/2) Gamma(j/2),     int r^j G = 2^j Gamma(1+j/2)^2,
on a grid of s in (0, 1/16] including both ends of the range (a check of the stated inequalities, not a proof of them
for every s; the proofs are the gamma-density arguments, reviewed by hand).

Usage: python3 check_p43_p47_constants.py [OUTPUT_JSON]
"""
import json, sys, hashlib
from fractions import Fraction as Q
from pathlib import Path
from mpmath import iv, mp
iv.prec = 200; mp.prec = 200
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_suffix('.json')
out = {}
ok = {}

# ---------- topic 43, section 2: moment tables on a grid ----------
def K(j, s):
    s = iv.mpf(s)
    return (s / 2) * 2 ** j * iv.gamma(1 + iv.mpf(j) / 2) * iv.gamma((j - s) / 2) / iv.gamma(1 - s / 2)
def M(j, s):
    s = iv.mpf(s)
    return 2 ** j * iv.gamma(1 + iv.mpf(j) / 2) * iv.gamma((j + s) / 2) / iv.gamma(s / 2)
grid = [Q(1, 16), Q(1, 32), Q(1, 64), Q(1, 4096), Q(3, 2 ** 21), Q(3, 2 ** 31), Q(1, 2 ** 40)]
Kb = {1: 2, 2: 2, 3: 6, 4: 16, 5: 81}; Mb = {1: 2, 2: 2, 3: 6, 4: 17, 5: 84}
rows = []
for s in grid:
    si = iv.mpf(s.numerator) / s.denominator
    r = {'s': str(s)}
    for j in Kb:
        kj = K(j, si) / si; r[f'K{j}/s'] = float(kj.b)
        assert kj.b <= Kb[j] if j != 2 else (kj.a <= 2 <= kj.b), (j, s, kj)
    for j in Mb:
        mj = M(j, si) / si; r[f'M{j}/s'] = float(mj.b)
        assert mj.b <= Mb[j] if j != 2 else (mj.a <= 2 <= mj.b), (j, s, mj)
    # (4) of topic 43
    r['int r(1+2r)kappa/s'] = float(((K(1, si) + 2 * K(2, si)) / si).b)
    r['int r(1+2r)^2kappa/s'] = float(((K(1, si) + 4 * K(2, si) + 4 * K(3, si)) / si).b)
    r['int r^2(1+2r)|Dkappa|/s'] = float(((3 * K(1, si) + 8 * K(2, si)) / si).b)
    assert r['int r(1+2r)kappa/s'] <= 6 and r['int r(1+2r)^2kappa/s'] <= 34 and r['int r^2(1+2r)|Dkappa|/s'] <= 22
    rows.append(r)
out['topic43_moment_grid'] = rows
ok['topic43_moment_tables_on_grid'] = True

# heat tensor kernel moments (10) and the 1 + 5 pi < 17 and (11) checks
qmom = {j: 2 ** j * iv.gamma(1 + iv.mpf(j) / 2) * (2 + iv.mpf(j) / 2) * iv.gamma(iv.mpf(j) / 2) for j in (1, 2, 3, 4)}
claimed = {1: 5 * iv.pi / 2, 2: iv.mpf(12), 3: 21 * iv.pi / 2, 4: iv.mpf(128)}
ok['topic43_(10)_tensor_moments_exact'] = all(abs(qmom[j] - claimed[j]).b < iv.mpf(10) ** -50 for j in qmom)
ok['topic43_1+5pi<17'] = bool((1 + 5 * iv.pi).b < 17)
eps = iv.mpf(1) / 2 ** 31
mcoef = [1, 1 + 3 * eps, 3 * eps + 3 * eps ** 2, 3 * eps ** 2 + eps ** 3, eps ** 3]   # m_eps - 1 = sum_{j>=1} c_j r^j
lhs11 = 1 + sum(mcoef[j] * qmom[j] for j in (1, 2, 3, 4))
ok['topic43_(11)_<9'] = bool(lhs11.b < 9); out['topic43_(11)_value'] = float(lhs11.b)
Gm = {j: 2 ** j * iv.gamma(1 + iv.mpf(j) / 2) ** 2 for j in range(5)}
lhsG = Gm[0] + sum(mcoef[j] * Gm[j] for j in (1, 2, 3, 4))
ok['topic43_J^-2_m-weighted_<3'] = bool(lhsG.b < 3)
ok['topic43_1+pi<5'] = bool((1 + iv.pi).b < 5)
# (9) at s = 2^-12 and s = 1/16 is not needed; check at s = 2^-12 (the range used)
for s in (Q(1, 4096), Q(3, 2 ** 21)):
    si = iv.mpf(s.numerator) / s.denominator
    mb = 1 + sum(mcoef[j] * M(j, si) for j in (1, 2, 3, 4))
    rk = K(1, si) + mcoef[1] * K(2, si) + mcoef[2] * K(3, si) + mcoef[3] * K(4, si) + mcoef[4] * K(5, si)
    rd = (3 * K(1, si) + mcoef[1] * 4 * K(2, si) + mcoef[2] * 5 * K(3, si) + mcoef[3] * 6 * K(4, si)
          + mcoef[4] * 7 * K(5, si))
    ok[f'topic43_(9)_at_s={s}'] = bool((mb - 1).b <= 3 * si.a and rk.b <= iv.mpf(17) / 4 * si.a and rd.b <= 15 * si.a)

# ---------- topic 43, sections 3-6: exact assembly ----------
D1, D2 = Q(14, 5), Q(3); CT = 17 * D1 + 22 * D2
ok['topic43_C_T=568/5'] = CT == Q(568, 5)
ok['topic43_(15/2)(4099/4096)<8'] = Q(15, 2) * Q(4099, 4096) < 8
ok['topic43_(17/4)(4099/4096)<5'] = Q(17, 4) * Q(4099, 4096) < 5
p2 = CT + 2 * 6 * 3 * 2 + 6 * 3 * Q(9, 5) * 2
p2_1 = 34 * 32 * 2 + 2 * 34 * 64 * Q(3, 2) * 2
p2_0 = 34 * 1024 * Q(8, 3) * 2
top = p2 + (p2_1 + p2_0) / 2048
p1 = CT + 6 * 3 * 2 + 6 * 3 * Q(3, 2) * 2
p1_0 = 34 * 32 * Q(8, 3) * 2
mid = 2048 * (p1 / 2048 + p1_0 / 2048)
low = Q(27, 5) * (9 * D1 + 8 * D2) + Q(16, 5) * (5 * D2) + 5 * (Q(27, 5) * 3 + 32) * Q(13, 3)
cx = 2 * 12 + 2 * (1 + Q(81, 5))
total = top + mid + low + cx
out['topic43_components'] = {'top': str(top), 'mid': str(mid), 'low': str(low), 'cX': str(cx), 'total': str(total)}
ok['topic43_top=83641/240'] = top == Q(83641, 240)
ok['topic43_mid=90094/15'] = mid == Q(90094, 15)
ok['topic43_low=101851/75'] = low == Q(101851, 75)
ok['topic43_total=9325421/1200<8192'] = total == Q(9325421, 1200) and total < 8192
# weight ratio bounds of section 6: (1+4r^2)^(2/5) <= 4^(2/5) <r>^(4/5) and 4^(2/5) < 2
ok['topic43_4^(2/5)<2'] = Q(4) ** 2 < Q(2) ** 5
# section 7 parameters
s7 = iv.mpf(3) / 2 ** 21; r0 = iv.mpf(5) / 2 ** 27; eta = iv.mpf(1) / 2 ** 30
rate = iv.mpf(1) / 20 - 2 ** 13 * s7 - 400 * r0 / iv.sqrt(s7)
ok['topic43_high_rate>6283/245760>1/40'] = bool(rate.a > iv.mpf(6283) / 245760 and Q(6283, 245760) > Q(1, 40))
ok['topic43_40eta=r0'] = Q(40, 2 ** 30) == Q(5, 2 ** 27)
contr = 6 * 2048 * r0 / iv.sqrt(s7)
ok['topic43_contraction<15/(16sqrt6)+<2/5'] = bool(contr.b < iv.mpf(2) / 5 and abs(contr - 15 / (16 * iv.sqrt(6))).b < 1e-40)
ok['topic43_slope_4r0/sqrt(s)<2^-12'] = bool((4 * r0 / iv.sqrt(s7)).b < iv.mpf(1) / 4096)
ok['topic43_40*146/sqrt(s)<2^23'] = bool((40 * 146 / iv.sqrt(s7)).b < 2 ** 23)
out['topic43_rate_lower'] = float(rate.a); out['topic43_contraction_upper'] = float(contr.b)
out['topic43_output_constant_upper'] = float((40 * 146 / iv.sqrt(s7)).b)
# same ratios as Theorem D_w
sw = iv.mpf(3) / 2 ** 31; rw = iv.mpf(5) / 2 ** 32
ok['topic43_ratios_equal_D_w'] = bool(abs(2 ** 13 * s7 - 2 ** 23 * sw).b < 1e-50 and abs(r0 / iv.sqrt(s7) - rw / iv.sqrt(sw)).b < 1e-50)

# ---------- topic 44 ----------
a0, a1, a2 = Q(2051, 4194304), Q(1025, 2097152), Q(1025, 1024)
Ch2 = Q(15, 8) ** 2 * 3 * a0 * (450 * a0 + 36 * a1 + a2)
CU2 = Q(15, 8) ** 2 * 8 * a0 * (1200 * a0 + 54 * a1 + Q(9, 5) * a2)
ok['topic44_Ch^2=3596147769375/562949953421312<1/144'] = Ch2 == Q(3596147769375, 562949953421312) and Ch2 < Q(1, 144)
ok['topic44_CU^2=1168572376125/35184372088832<9/256'] = CU2 == Q(1168572376125, 35184372088832) and CU2 < Q(9, 256)
ok['topic44_a0=(1+6/4096)/2048'] = a0 == (1 + Q(6, 4096)) / 2048 and a1 == (1 + Q(4, 4096)) / 2048 and a2 == 1 + Q(4, 4096)
# C_U: L2 factor 3 (8/3) a0, Hessian factor 450 (8/3) a0 + 36 (3/2) a1 + (9/5) a2
lhs = 3 * Q(8, 3) * a0 * (450 * Q(8, 3) * a0 + 36 * Q(3, 2) * a1 + Q(9, 5) * a2)
ok['topic44_U_coeffs'] = lhs == 8 * a0 * (1200 * a0 + 54 * a1 + Q(9, 5) * a2)
ok['topic44_5^(3/5)<3_5^(1/10)<2_2^(1/5)<5/4'] = Q(5) ** 3 < Q(3) ** 5 and Q(5) < Q(2) ** 10 and Q(2) * 4 ** 5 < 5 ** 5

# ---------- topic 46 ----------
ok['topic46_2/25_11/60'] = Ch2 < Q(4, 625) and CU2 < Q(121, 3600)
ok['topic46_t^2phi=16/105'] = 2 * (Q(1, 3) - Q(2, 5) + Q(1, 7)) == Q(16, 105)
I0, I1, I2 = Q(256, 315), Q(256, 105), Q(128, 5)
ok['topic46_I0'] = 2 * (1 - Q(4, 3) + Q(6, 5) - Q(4, 7) + Q(1, 9)) == I0
ok['topic46_I1'] = 16 * Q(16, 105) == I1
ok['topic46_I2'] = 144 * Q(2, 5) - 96 * Q(2, 3) + 32 == I2
Mm = Q(16, 15) ** 2
ok['topic46_d2^2=150/49'] = 2 * I0 * I1 / Mm ** 2 == Q(150, 49)     # (5 sqrt 6/7)^2
ok['topic46_e2=5/7'] = I0 / Mm == Q(5, 7)
ok['topic46_dinf^2'] = (Q(64, 27) * 2) / Mm ** 2 == Q(625 * 6, 1024)  # (8 sqrt2/(3 sqrt3))^2 / M^2 = (25 sqrt6/32)^2
ok['topic46_d1'] = 4 * Q(16, 15) / Mm == Q(15, 4)
# ---------- topic 47 ----------
ok['topic47_d3^2=2025/49'] = (2 * I2 * I0 + 2 * I1 ** 2) / Mm ** 2 == Q(2025, 49)
sig = Q(11, 5)
CR = [3 * 2 + sig * 2 / 2, 3 * 2 + sig * Q(5, 2) * 2, 6 + sig * Q(9, 2) * 6, sig * Q(7, 2) * 17, sig * 84]
ok['topic47_C_R_coeffs'] = CR == [Q(41, 5), Q(17), Q(327, 5), Q(1309, 10), Q(924, 5)]
ok['topic47_sum=4063/10'] = sum(CR) == Q(4063, 10) and 1 + sum(CR) / 4096 < Q(11, 10)
ok['topic47_M5_bound'] = (54 * Q(49, 32)) ** 2 * Q(33, 32) < 84 ** 2
# expansion sigma t (1/(2R) + t/R^2)(1+t/R)^3 -> coefficients (1/2, 5/2, 9/2, 7/2, 1) of t^k/R^k
poly = [Q(0)] * 6
for i, ci in enumerate([Q(1, 2), Q(1)]):          # t/(2R) and t^2/R^2  (powers 1 and 2)
    for j, cj in enumerate([1, 3, 3, 1]):
        poly[1 + i + j] += ci * cj
ok['topic47_expansion'] = poly[1:] == [Q(1, 2), Q(5, 2), Q(9, 2), Q(7, 2), Q(1)]
# quadratic coefficients quoted in topic 47: H B d1 with H = 2/25, B = 11/60
ok['topic47_Q=22.528_and_28.16'] = Q(2, 25) * Q(11, 60) * Q(15, 4) * Q(2048, 5) == Q(22528, 1000) and \
    Q(2, 25) * Q(11, 60) * Q(15, 4) * 512 == Q(2816, 100)
out['checks'] = {k: bool(v) for k, v in ok.items()}
out['all_pass'] = all(ok.values())
out['code_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(out, indent=2) + '\n')
for k, v in ok.items():
    print(k, bool(v))
print('ALL PASS' if out['all_pass'] else 'FAILURES'); print('DONE')
