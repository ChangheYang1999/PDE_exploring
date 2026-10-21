import sys, time, json
sys.path.insert(0, '.')
import mpmath as mp
from bnat import Ref, B_value
d = json.load(open('lead/b3_functional/xref/ref_c6g_K4.json'))
A = repr(d['A']); xs = mp.mpf(repr(d['x_star']))
mp.mp.dps = 40
e = 1/xs**2
R = Ref(A, e, [], dps=40)
b = R.beta; Am = R.A
CA = (16 - b)/(3*Am*(4 + b))*mp.beta(2 - b/2, b)
SA = 6*Am*(4*Am - 3)/(8*Am - 1)
print('closed C_A (1 - S_A e) =', CA*(1 - SA*e), ' lead 0.325791726307172')
t0 = time.time()
R.series0(40)
print('series built %.1fs' % (time.time() - t0)); sys.stdout.flush()
for which in ['II', 'I']:
    for delta in [mp.mpf('0.15'), mp.mpf('0.3')]:
        t0 = time.time()
        v, parts = B_value(R, which, delta)
        print(which, 'delta', delta, ':', mp.nstr(v, 25), ' diff to closed', mp.nstr(v - CA*(1 - SA*e), 3), ' %.0fs' % (time.time() - t0)); sys.stdout.flush()
