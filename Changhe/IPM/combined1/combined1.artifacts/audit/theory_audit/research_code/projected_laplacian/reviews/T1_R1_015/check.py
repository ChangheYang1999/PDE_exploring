# c1-t1 check of the T4-127 selected-mode data for C1-N1-007 (FW-T-DYADIC-Y-v1 test NC-T-DYADIC-LAP).
# Input: data/T4127_combined_cover.json (copy of c1-t4 research/projected_laplacian/verification/combined_cover.json,
# sha256 bd5a33163064e077c0b145f27837c853762651dfe0f3ab85dedf35dfa6a6e0f1).
# Part 1 recomputes the four T4-127 cell ratios 5^((l-2)/2) J_S(h) / B(l), S = {1, 3}, from the stored mode norms.
# Part 2 prints the pointwise ratios 5^((a-2)/2) J(a) / B(a) for S = {1,3} and S = {1,...,15} on the stored grid.
# Ratios use the ball midpoints (ball radii are below 1e-80); the printed values are FLOAT diagnostics, except that
# part 1 compares with the T4 interval values.
import json, hashlib
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 60
PATH = 'data/T4127_combined_cover.json'
raw = open(PATH, 'rb').read()
print('input sha256', hashlib.sha256(raw).hexdigest())
d = json.loads(raw)
c = mp.mpf(4076476460239181) / mp.mpf(2) ** 51
A = 1 + 1 / c


def mid(s):
    return mp.mpf(s.strip('[').split()[0])


def frac(s):
    return Fraction(s)


def B(a):
    return mp.sqrt(8 * mp.pi) * (1 + c - c * a) ** 2 / (1 + a)


rows = {}
for r in d['rows']:
    rows[frac(r['a'])] = (mid(r['modes_1_3_norm']), mid(r['modes_1_to_15_norm']))

print('part 1: T4-127 cells, S = {1,3}')
for cell in d['cells']:
    l = frac(cell['left'])
    h = frac(cell['norm_evaluation_at'])
    lm = mp.mpf(l.numerator) / l.denominator
    J = rows[h][0]
    ratio = mp.power(5, (lm - 2) / 2) * J / B(lm)
    print(' cell', cell['left'], cell['right'], 'J at', cell['norm_evaluation_at'], 'ratio', mp.nstr(ratio, 15),
          'T4', cell['ratio'][:20], 'passed', cell['passed'])

print('part 2: pointwise ratios (FLOAT), ratio >= 1 means the necessary test fails at that a')
for a in sorted(rows):
    am = mp.mpf(a.numerator) / a.denominator
    if am >= A:
        print(' a', a, 'outside the window a < 1 + 1/c')
        continue
    f = mp.power(5, (am - 2) / 2)
    n13, n115 = rows[a]
    print(' a', str(a).ljust(4), 'N ceiling', mp.nstr(B(am) / f, 8), 'J13', mp.nstr(n13, 8), 'J1..15', mp.nstr(n115, 8),
          'ratio13', mp.nstr(f * n13 / B(am), 6), 'ratio1..15', mp.nstr(f * n115 / B(am), 6))
