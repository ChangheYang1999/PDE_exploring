"""Reduced (2-mode, small D) forced sheet: roots F0(alpha) of F_inf(alpha, F0) = 1 (lead, HEURISTIC; see ANALYSIS O)."""
import numpy as np, sys
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
sys.path.insert(0, 'code')
from slow_reduced import rhs

def g(alpha, F0, T=60.0):
    sol = solve_ivp(rhs, [0, T], [alpha, F0, 0.0], method='LSODA', rtol=1e-10, atol=1e-12)
    return sol.y[1, -1] - 1.0

grid = np.concatenate([np.logspace(-6, -1.3, 25), np.linspace(0.05, 1.2, 70)])
for a in [0.25, 0.5, 1, 2, 3, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 7.6, 7.8, 8]:
    vals = np.array([g(a, f) for f in grid])
    roots = []
    for i in range(len(grid) - 1):
        if vals[i] * vals[i + 1] < 0 and abs(vals[i]) < 5 and abs(vals[i + 1]) < 5:
            roots.append(brentq(lambda f: g(a, f), grid[i], grid[i + 1], xtol=1e-12))
    print(f"alpha={a:5.2f} roots F0={['%.4f' % r for r in roots]}  min(F_inf-1)={vals.min():.3g}", flush=True)
