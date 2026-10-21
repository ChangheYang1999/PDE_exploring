# convergence of the own (II) value in the quadrature parameters and in the working precision, per reference
import sys, time, json
sys.path.insert(0, '.')
import mpmath as mp
from bnat import Ref, B_value
K = int(sys.argv[1])
d = json.load(open('lead/b3_functional/xref/ref_c6g_K%d.json' % K))
for dps, N, kw in [(40, 80, dict()), (40, 80, dict(nmid=40, wmid=mp.mpf(1)/40, ns=40, levels=14)),
                   (40, 80, dict(t1=mp.mpf('0.35'))), (50, 100, dict(nmid=40, ns=40))]:
    mp.mp.dps = dps
    t0 = time.time()
    R = Ref(repr(d['A']), 1/mp.mpf(repr(d['x_star']))**2, d['q_monomial'], dps=dps); R.series0(N)
    v, parts = B_value(R, 'II', mp.mpf('0.25'), **kw)
    print('K=%d dps %d N %d %s: B (II) = %s, minus lead %s (%.0fs)' % (K, dps, N, {k: mp.nstr(x, 4) for k, x in kw.items()},
          mp.nstr(v, 24), mp.nstr(v - mp.mpf(d['B']), 3), time.time() - t0), flush=True)
