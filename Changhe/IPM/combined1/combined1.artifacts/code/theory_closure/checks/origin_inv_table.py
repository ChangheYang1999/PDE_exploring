# c1-t1 theory_v03 section 5 (NC-T-ORIGIN-INV): directed values of the T4-146 ceilings.
# Ceiling on Y(F) from (18): H(c - 1) beta_inf(a)/(1 + a); on N_a(F): 5^((2-a)/2) times that; the T4-097 ceiling
# B(a) = sqrt(8 pi) beta_inf(a)^2/(1 + a); the combined N_a ceiling 5^((2-a)/2) min(...); M floor 1/(c - 1 - s*) at
# the maximizing s* (the bound M >= 1/(c - 1 - s) holds for each s). Ceilings rounded up, floors rounded down, 7 digits.
# Cell rule: on [l, h] the scheme is ruled out if a lower bound of N_h(F) is at least the N_a ceiling printed at a = l.
# Run from artifacts/checks: OMP_NUM_THREADS=1 python3 -B origin_inv_table.py > origin_inv_table.out
from mpmath import mp, iv, mpf
import math

mp.dps = 60
iv.dps = 60
C = iv.mpf(4076476460239181) / iv.mpf(2) ** 51
D = C - 1
sstar = ((2 * D - 3) + iv.sqrt((2 * D - 3) ** 2 + 16 * D)) / 8
H = (D - sstar) * iv.sqrt(4 * iv.pi * sstar * (1 + sstar))


def up(x, k=7):
    x = mpf(x.b)
    e = math.floor(math.log10(x)) - k + 1
    return mp.nstr(mp.ceil(x / mpf(10) ** e) * mpf(10) ** e, k + 2)


def dn(x, k=7):
    x = mpf(x.a)
    e = math.floor(math.log10(x)) - k + 1
    return mp.nstr(mp.floor(x / mpf(10) ** e) * mpf(10) ** e, k + 2)


print('H(c - 1) in [%s, %s]; s* in [%s, %s]' % (mp.nstr(mpf(H.a), 20), mp.nstr(mpf(H.b), 20),
                                               mp.nstr(mpf(sstar.a), 17), mp.nstr(mpf(sstar.b), 17)))
print('M floor at s*: 1/(c - 1 - s*) >= %s' % dn(1 / (D - sstar)))
print('crossover: H/sqrt(8 pi) = %s (FLOAT), beta_inf(a) = that at a = %s (FLOAT)'
      % (mp.nstr(mpf((H / iv.sqrt(8 * iv.pi)).a), 8),
         mp.nstr(mpf(((1 + C - H / iv.sqrt(8 * iv.pi)) / C).a), 8)))
print('a | Y ceiling (18) | B(a) (T4-097) | N_a ceiling from (18) | N_a ceiling combined')
for num, den in [(0, 1), (1, 4), (1, 2), (3, 4), (4, 5), (1, 1), (6, 5), (5, 4), (13, 10), (7, 5), (3, 2)]:
    a = iv.mpf(num) / den
    beta = 1 + C - C * a
    yc = H * beta / (1 + a)
    bc = iv.sqrt(8 * iv.pi) * beta ** 2 / (1 + a)
    f5 = iv.mpf(5) ** ((2 - a) / 2)
    nc = f5 * yc
    nb = f5 * bc
    comb = nc if nc.b < nb.a else (nb if nb.b < nc.a else None)
    print('%s/%s | %s | %s | %s | %s' % (num, den, up(yc), up(bc), up(nc), up(comb) if comb is not None else 'tie'))
