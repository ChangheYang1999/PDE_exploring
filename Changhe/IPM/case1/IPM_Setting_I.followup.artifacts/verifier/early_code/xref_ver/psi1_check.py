# Psi(1) and G(1) of bnat against the referee's closed form (41) and against Gauss-Legendre panels, per reference
import sys, json
sys.path.insert(0, '.')
import mpmath as mp
from bnat import Ref, gl_nodes
mp.mp.dps = 40
for K in [int(k) for k in sys.argv[1].split(',')]:
    d = json.load(open('lead/b3_functional/xref/ref_c6g_K%d.json' % K))
    A = mp.mpf(repr(d['A'])); q = d['q_monomial']
    R = Ref(repr(d['A']), 1/mp.mpf(repr(d['x_star']))**2, q, dps=40)
    qf = lambda t: mp.fsum(mp.mpf(c)*t**k for k, c in enumerate(q))
    T1 = mp.quad(lambda t: (1 + t)**2*qf(t)/(A - t*(1 - t**2)*qf(t)), mp.linspace(0, 1, 9))/2
    xs, ws = gl_nodes(40)
    P_gl = mp.fsum(mp.fsum(wk*R.psi((i + xk)/mp.mpf(64)) for xk, wk in zip(xs, ws))/64 for i in range(64))
    print('K=%d: Psi1 (mp.quad, bnat) %s; GL 64x40 minus bnat %s; (41): T(1) - log 2 minus bnat %s; G(1) = %s' %
          (K, mp.nstr(R.Psi1, 25), mp.nstr(P_gl - R.Psi1, 3), mp.nstr(T1 - mp.log(2) - R.Psi1, 3), mp.nstr(R.G1, 22)), flush=True)
