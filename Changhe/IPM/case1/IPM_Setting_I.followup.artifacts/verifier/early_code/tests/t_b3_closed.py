"""verifier: test of the lead's closed form B_3^nat = C_A (1 - S_A / L^2) on R12 (FINAL_REPORT 6.3.2 (a)) with the exact
series values of series_bj (C4): B_3^nat L^2 must be affine in L^2 if the form is exact."""
import sys
sys.path.insert(0, 'verifier/early_code')
from mpmath import mp
import series_bj as SB
mp.dps = 40
A = mp.mpf('10.150725')
Ls = [4, 5, 6, 7, 8.6, 10]
vals = []
for L in Ls:
    L = mp.mpf(L)
    wn, wd, gn, gd = SB.r12(A, L)
    res, _, _ = SB.Bj(wn, wd, gn, gd, A, L, 160, [L * mp.mpf('0.45'), L * mp.mpf('0.55')], jmax=3)
    b = [v['Bnat'] for v in res[3]]
    vals.append((L, b[0]))
    print('L %5s  B3nat %s  (two points differ by %.1e)' % (mp.nstr(L, 4), mp.nstr(b[0], 15), float(abs(b[0] - b[1]))))
# fit C, S from the first two L, predict the others
(L1, B1), (L2, B2) = vals[0], vals[-1]
C = (B1 * L1 ** 2 - B2 * L2 ** 2) / (L1 ** 2 - L2 ** 2)
S = L1 ** 2 * (1 - B1 / C)
print('from L = 4, 10: C %s  S %s' % (mp.nstr(C, 15), mp.nstr(S, 15)))
print('S_A = 6A(4A-3)/(8A-1) = %s; sqrt %s' % (mp.nstr(6 * A * (4 * A - 3) / (8 * A - 1), 15), mp.nstr(mp.sqrt(6 * A * (4 * A - 3) / (8 * A - 1)), 15)))
for L, B in vals:
    print('L %5s: B - C(1 - S/L^2) = %.3e' % (mp.nstr(L, 4), float(B - C * (1 - S / L ** 2))))
