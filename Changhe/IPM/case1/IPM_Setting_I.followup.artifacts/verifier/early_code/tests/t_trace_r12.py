"""verifier: TraceAxis + vaxis.B3 (F2b, F2a) and fp_ibp on exact R12 data sampled on the first-run trace grid;
compare with the closed form B_3^nat = C_A (1 - S_A/L^2) (D13 (d)).  Optional relative noise on w''."""
import sys, math
sys.path.insert(0, 'verifier/early_code')
import numpy as np
import sympy as sp
from trace_axis import TraceAxis, b3_trace, b3_ibp_full
from vaxis import B3

A = 10.150725
c_l = (A + 1) / 2
L = float(sys.argv[1]) if len(sys.argv) > 1 else 8.6
noise = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
X = sp.symbols('x')
wexpr = -A * X * (L ** 2 - X ** 2) / (L ** 2 + X ** 2)
fs = [sp.lambdify(X, sp.diff(wexpr, X, k), 'numpy') for k in range(4)]
z = np.load('first-run-records/ver/runs/gen4/fxn24g_traces.npz', allow_pickle=True)
x = z['x']
rng = np.random.default_rng(1)
wpp = fs[2](x) * (1 + noise * rng.standard_normal(len(x)))
path = 'verifier/early_data/traces/r12_L%g_n%g.npz' % (L, noise)
np.savez(path, x=x, w=fs[0](x), wp=fs[1](x), wpp_ode=wpp, wpp_fd=wpp, c_l=c_l)
CA = 0.530666623156826
SA = 6 * A * (4 * A - 3) / (8 * A - 1)
Bex = CA * (1 - SA / L ** 2)
WINS = [(0.17, 2.0), (0.34, 2.6), (0.5, 3.5)]
for kw in [dict(), dict(near_frac=0.03), dict(near_frac=0.03, near_fit=(40, 8)), dict(reg='Ag'), dict(reg=None)]:
    ad = TraceAxis(path, **kw)
    errs = [np.abs(ad.wj['w'][k] - fs[k](ad.x) / math.factorial(k)).max() / np.abs(fs[k](ad.x)).max() * math.factorial(k)
            for k in range(4)]
    b = B3(ad)
    s = []
    for xlo, xc in WINS:
        for deg in (8, 12):
            s.append('%+.1e/%+.1e/%+.1e/%+.1e' % (b.fp('F2b', xlo, xc, deg=deg)['Bnat'] - Bex,
                                            b3_ibp_full(b, xlo, xc, deg=deg)['Bnat'] - Bex,
                                            b3_trace(b, 'F2b', xlo, xc, deg=deg)['Bnat'] - Bex,
                                            b3_trace(b, 'ibp', xlo, xc, deg=deg)['Bnat'] - Bex))
    print('L %g noise %.0e %s: x* - L %.1e, h(P)-1 %+.1e, jet errs %s' % (L, noise, kw, ad.xs - L, ad.hP_file - 1,
          ' '.join('%.0e' % v for v in errs)))
    print('   F2b(GJ)/ibp_full/F2b(fit)/ibp(fit) - exact (windows x deg):', ' '.join(s), flush=True)
