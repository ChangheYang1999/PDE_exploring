# verifier (o17): sign check of D38 (A = 2, L = 2, R12) against the series code: F5/(w H5) and G5 at sample points
import sys
sys.path.insert(0, 'verifier/early_code')
import mpmath as mp
from series_bj import hierarchy, r12
mp.mp.dps = 40
A = mp.mpf(2); L = mp.mpf(2); n = 200
wn, wd, gn, gd = r12(A, L)
sP = hierarchy(wn, wd, gn, gd, A, L, n, 5)
q = mp.mpf(4) / A
for x in [mp.mpf('0.8'), mp.mpf(1), mp.mpf('1.3')]:
    u = x / L
    w = -A * x * (1 - u*u) / (1 + u*u); g = x*x / (1 + u*u)
    H = A**q * g**(5 + q) * abs(w)**(-q)
    r_ser = sP['F5'](x - L) / (w * H)
    r_d38 = (x**2 - 4) * (25*x**4 - 312*x**2 + 1040) / (3840 * x**11)
    G_ser = sP['G5'](x - L)
    G_d38 = x**2 * (11*x**6 + 88*x**4 - 1872*x**2 + 9984) / (90 * (x**2 + 4)**5)
    print('x %s  F5/(wH5): series %s  D38 %s   G5: series %s  D38 %s' % (x, mp.nstr(r_ser, 12), mp.nstr(r_d38, 12), mp.nstr(G_ser, 12), mp.nstr(G_d38, 12)))
