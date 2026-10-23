"""Faster driver for code/slow_reduced.py (same ODE; lead, HEURISTIC). Prints with flush."""
import numpy as np, sys
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
sys.path.insert(0, 'code')
from slow_reduced import rhs, eig

def Finf(alpha, F0, T=80.0):
    def big(s, z): return abs(z[0]) + abs(z[1]) + abs(z[2]) - 1e4
    big.terminal = True
    sol = solve_ivp(rhs, [0, T], [alpha, F0, 0.0], method='LSODA', rtol=1e-10, atol=1e-12, events=big)
    return sol.y[1, -1], sol.y[0, -1], sol.y[2, -1], sol.status

for a in [1, 4/3, 2, 4, 6, 7, 7.58, 8, 9, 10, 12]:
    print(f"alpha={a:6.3f} lambda={np.round(eig(a), 4)}", flush=True)
print("F(+inf) - 1 on a grid of F0 (columns) for each alpha", flush=True)
F0s = [1e-6, 1e-4, 1e-2, 0.05, 0.1, 0.2, 0.4, 0.7, 1.0]
print("alpha  " + " ".join(f"{f:9.2g}" for f in F0s), flush=True)
for a in [0.5, 1, 2, 3, 4, 5, 6, 7, 7.5, 8, 9, 10, 12]:
    row = []
    for F0 in F0s:
        Fi, h1, h3, st = Finf(a, F0)
        row.append(Fi - 1 if st == 0 else np.nan)
    print(f"{a:5.2f}  " + " ".join(f"{v:9.3g}" for v in row), flush=True)
