# Failure factors at candidate 007 of the failed tests for specified certificates in theory_v08 section 1.
# Each row is an inequality "proved quantity < threshold" that a specified certificate needs. The script takes a cited
# LOWER bound p for the quantity that is proved for 007 and a cited UPPER bound t for the threshold, both as exact
# decimals, and prints p/t rounded down at the displayed precision, 10^(-k) floor(10^k p/t) with k = 4 (k = 2 for
# ratios of 100 or more). Since p <= quantity and threshold <= t, the true ratio quantity/threshold is at least p/t,
# so every printed factor is a lower bound. Revision 2 (after c1-t4 T4-437): S2 uses the sharp norm lower comparison
# 516.9717852723 (N4-180/N4-181, accepted in T4-238), not the sharpw value 756.5312630768; K rows cite T4-425 s2.
# Exact rational arithmetic (fractions); no FLOAT step. The cited bounds are the sources' printed outward roundings.
from fractions import Fraction as F
from math import floor

ROWS = [
    # (label, p = lower bound of the proved quantity, source of p, t = upper bound of the threshold, source of t)
    ('D1 NC-T-DIST, TB-sharp family ceiling', '0.004769166867', 'T4-185 (R1-022)',
     '3.7930e-6', 'FW-T-TB-sharp-v1 ceiling, T4-028'),
    ('D2 NC-T-DIST, sharpw family ceiling', '0.004769166867', 'T4-185 (R1-022)',
     '2.8496e-6', 'FW-T-T4L2-sharpw-v1 ceiling'),
    ('D3 NC-T-DIST, sharp family ceiling', '0.004769166867', 'T4-185 (R1-022)',
     '3.0927e-6', 'FW-T-T4L2-sharp-v1 ceiling'),
    ('D4 NC-T-DIST, fixed sharpw ball radius', '0.004769166867', 'T4-185 (R1-022)',
     '1351/1024000000', 'fixed ball r/sqrt(w2), T4-262'),
    ('D5 NC-T-DIST, graded ceiling', '0.004769166867', 'T4-185 (R1-022)',
     '25/54684', 'graded ceiling < 25/54684, T4-277'),
    ('S1 :H6 smallness, sharpw', '756.5312630768', 'T4-238, N4-180', '2.1035e-4', 'sharpw eta'),
    ('S2 :H6 smallness, sharp', '516.9717852723', 'T4-238, N4-180, sharp lower comparison', '7.6219e-5', 'sharp eta'),
    ('O1 NC-T-ORIGIN-INV, min over seven cells', '1.23427738878510651005', 'T4-147 (R1-017)', '1', 'ratio test'),
    ('U1 NC-T-UNIV-E, fixed sharpw ball', '0.793036506422514088', 'T4-381 Etest',
     '0.785064', 'T4-380 (3), T4-399, T4-424'),
    ('U2 NC-T-UNIV-E, sharpw ceiling', '0.793036506422514088', 'T4-381 Etest', '0.6819391', 'T2 AU3, T4-404'),
    ('U3 NC-T-UNIV-E, TB-sharp ceiling', '0.793036506422514088', 'T4-381 Etest', '0.6471910', 'T2 AU3, T4-404'),
    ('U4 NC-T-UNIV-E, graded ceiling', '0.793036506422514088', 'T4-381 Etest', '0.2694314', 'T2 AU3, T4-404'),
    ('P1 profile coefficient 93/250, graded (zero remainder)', '93/250', 'T4-415', '0.1810598671', 'REVIEW_T4_415 s6'),
    ('P2 any N/G certificate, graded (zero remainder)', '0.3714757', 'REVIEW_T4_415 s4', '0.1810598671',
     'REVIEW_T4_415 s6'),
    ('P3 profile coefficient 583/1000, fixed sharpw ball', '583/1000', 'T4-402', '0.5275684020', 'REVIEW_T4_415 s6'),
    ('P4 profile coefficient 583/1000, sharpw ceiling', '583/1000', 'T4-402', '0.4582680410', 'REVIEW_T4_415 s6'),
    ('P5 profile coefficient 583/1000, TB ceiling', '583/1000', 'T4-402', '0.4349170868', 'REVIEW_T4_415 s6'),
    ('R1 T4-410 remainder / room for 93/250, fixed sharpw', '3.452825', 'REVIEW_T4_415 s7', '0.1555681',
     'REVIEW_T4_415 s6'),
    ('R2 T4-410 remainder / room for 93/250, sharpw', '3.974970', 'REVIEW_T4_415 s7', '0.08626771', 'REVIEW_T4_415 s6'),
    ('R3 T4-410 remainder / room for 93/250, TB', '4.188388', 'REVIEW_T4_415 s7', '0.06291677', 'REVIEW_T4_415 s6'),
    ('A1 radial average Eeff / Kcrit/Phi (T4-425)', '0.79303', 'T4-425 (7)', '0.785064', 'T4-425 (7)'),
    ('K1 kernel constant Lam, fixed sharpw (with fallback)', '109.6024', 'T4-425 s2 lambda', '14.41', 'R1-044 3(c)'),
    ('K2 kernel constant Lam, sharpw', '109.6024', 'T4-425 s2 lambda', '8.647', 'R1-044 3(c)'),
    ('K3 kernel constant Lam, TB', '109.6024', 'T4-425 s2 lambda', '7.287', 'R1-044 3(c)'),
]


def q(s):
    return F(s)


def down(x, nd):
    s = F(10) ** nd
    return F(floor(x * s), s)


fails = 0
for lab, p, ps, t, ts in ROWS:
    r = q(p) / q(t)
    nd = 4 if r < 100 else 2
    d = down(r, nd)
    assert d <= r
    ok = r > 1
    fails += ok
    print(f'{lab}: p = {p} ({ps}), t = {t} ({ts}), factor >= {float(d):.{nd}f} {"FAILS" if ok else "passes"}')
# rows with no room: the threshold for the graded target is below 93/250 (P1), so the remainder room is negative and
# no remainder bound helps (REVIEW_T4_415 s6, room <= -0.1909308 for 007/013/014).
print(f'rows {len(ROWS)}, failing for 007: {fails}')
assert fails == len(ROWS)
print('ALL ROWS FAIL FOR 007 (each factor is a lower bound)')
