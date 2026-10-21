# (o17): B_5(c_l, w) on the R12 data at the zero of B_3, L^2 = S_A = 6A(4A-3)/(8A-1), with the own series code
# (code/series_bj.py: B_j = (G_j^P - G_j^0)/H_j, both series analytic; valid for j = 5 only when B_3 = 0).
# Checks: B_3 at L^2 = S_A must vanish to working precision; B_5 must agree at several evaluation points x.
import sys, time
sys.path.insert(0, 'verifier/early_code')
import mpmath as mp
from series_bj import Bj, r12
mp.mp.dps = int(sys.argv[2]) if len(sys.argv) > 2 else 40
n = int(sys.argv[3]) if len(sys.argv) > 3 else 200
As = [mp.mpf(a) for a in sys.argv[1].split(',')]
for A in As:
    t0 = time.time()
    SA = 6*A*(4*A - 3)/(8*A - 1)
    L = mp.sqrt(SA)
    wn, wd, gn, gd = r12(A, L)
    xe = [L*mp.mpf(k)/10 for k in (3, 4, 5, 6)]
    res, s0, sP = Bj(wn, wd, gn, gd, A, L, n, xe, jmax=5)
    B3 = [v['B'] for v in res[3]]; B5 = [v['B'] for v in res[5]]; B5n = [v['Bnat'] for v in res[5]]
    p5 = 10 + 4/A
    print('A = %s  L^2 = S_A = %s  p_5 = %s' % (mp.nstr(A, 8), mp.nstr(SA, 20), mp.nstr(p5, 10)))
    print('  B_3 at x/L = 0.3..0.6: ' + ' '.join(mp.nstr(b, 3) for b in B3))
    print('  B_5 (g/x^2 -> 1)     : ' + ' '.join(mp.nstr(b, 20) for b in B5))
    print('  B_5 natural units    : ' + ' '.join(mp.nstr(b, 20) for b in B5n))
    print('  spread of B_5 over x : %s   time %.1f s' % (mp.nstr(max(B5) - min(B5), 3), time.time() - t0), flush=True)
