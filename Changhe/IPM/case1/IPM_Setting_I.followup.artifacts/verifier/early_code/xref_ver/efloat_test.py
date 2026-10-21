# (o6) offset test: B (II) on ref_c6g_K<K> with e = the stored float e instead of 1/x*^2 (40 digits)
import sys, time, json
sys.path.insert(0, '.')
import mpmath as mp
from bnat import Ref, B_value
for K in [int(k) for k in sys.argv[1].split(',')]:
    d = json.load(open('lead/b3_functional/xref/ref_c6g_K%d.json' % K))
    mp.mp.dps = 40
    A = repr(d['A']); xs = mp.mpf(repr(d['x_star']))
    e_x = 1/xs**2; e_f = mp.mpf(repr(d['e']))
    R = Ref(A, e_f, d['q_monomial'], dps=40)
    R.series0(80)
    t0 = time.time()
    v, parts = B_value(R, 'II', mp.mpf('0.25'))
    print('K=%d: e_float - 1/x*^2 = %s; B (II, e float) = %s; minus lead %s (%.0fs)'
          % (K, mp.nstr(e_f - e_x, 5), mp.nstr(v, 22), mp.nstr(v - mp.mpf(d['B']), 3), time.time() - t0), flush=True)
