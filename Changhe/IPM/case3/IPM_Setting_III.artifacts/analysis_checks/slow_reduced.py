"""Formal small-D (D = c_l - 1 -> 0) reduction of the y-leading profile problem (lead, HEURISTIC).

rho = r [ D h1(sig) sin(th) + D^2 h3(sig) sin(3 th) + ... ],  sig = D log r,  J3 = int_sig^inf h3,
F = 1 - h1/4 + J3  (F = 1 + c_loc/D, c_loc the local strain from all larger scales).
Leading-order system (O(D^2) sin th and O(D^3) sin 3th balances):
   h1' = -h1 F
   F'  =  h1 F/4 - h3
   h3' = -(1 - h1/2) h3 + h1 F (1/2 - F/2 - h1/16)
Unforced profile: (h1, F, h3) -> (alpha, 0, 0) as sig -> -inf, -> (0, 1, 0) as sig -> +inf.
Forced (sheet 1, forcing core at sig = 0): data (alpha, F0 = Delta/D, 0) at sig = 0, shoot F0 so that F(+inf) = 1.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

def rhs(s, z):
    h1, F, h3 = z
    return [-h1*F, h1*F/4 - h3, -(1 - h1/2)*h3 + h1*F*(0.5 - F/2 - h1/16)]

def Finf(alpha, F0, T=400.0):
    def big(s, z): return abs(z[0]) + abs(z[1]) + abs(z[2]) - 1e6
    big.terminal = True
    sol = solve_ivp(rhs, [0, T], [alpha, F0, 0.0], rtol=1e-11, atol=1e-13, events=big)
    h1, F, h3 = sol.y[:, -1]
    return F, h1, h3, sol.status

def eig(alpha):
    tr = 3*alpha/4 - 1; det = alpha*(alpha + 4)/16
    return np.roots([1, -tr, det])

if __name__ == "__main__":
    print("linearization at (alpha,0,0): lambda^2 - (3a/4 - 1) lambda + a(a+4)/16 = 0")
    for a in [1, 4/3, 2, 4, 7.58, 8, 9, 10, 12]:
        print(f"  alpha={a:6.3f}  lambda={eig(a)}")
    print("lattice check: alpha=8 -> {2,3}; alpha=12 -> {2,6}")
    print()
    print("forced reduced sheet: alpha, F0 = Delta/D with F(+inf) = 1")
    rows = []
    for a in [0.1, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 7.5, 8.0, 8.5, 9.0, 10.0, 12.0]:
        g = lambda F0: Finf(a, F0)[0] - 1.0
        grid = np.concatenate([np.logspace(-8, -1, 36), np.linspace(0.11, 1.5, 60)])
        vals = []
        for F0 in grid:
            try:
                vals.append(g(F0))
            except Exception:
                vals.append(np.nan)
        vals = np.array(vals)
        roots = []
        for i in range(len(grid) - 1):
            if np.isfinite(vals[i]) and np.isfinite(vals[i+1]) and vals[i]*vals[i+1] < 0:
                try:
                    roots.append(brentq(g, grid[i], grid[i+1], xtol=1e-14))
                except Exception:
                    pass
        print(f"  alpha={a:6.3f}  F0 roots={['%.6g' % r for r in roots]}")
