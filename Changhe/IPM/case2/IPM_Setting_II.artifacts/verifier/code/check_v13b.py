"""V13 follow-up: (i) L-dependence of the defect of int R phi = pi c(c-1/2) - Q for the asymmetric growing density
(expected truncation of int_{r<L} R phi ~ L^{p-1}); (ii) nt = 128 for the numerics' one-step map c1."""
import numpy as np, torch, sys, math
sys.path.insert(0, 'code')
from check_v13 import make, integ, Qfun, Rphi
for L in (1e6, 1e8, 1e10, 1e12, 1e14):
    S = make(L=L, nt=32)
    X, Y, R = S.X, S.Y, S.R
    pp = 0.6
    rho = (X*(1 + 1.2*Y/(1 + R**2)**0.5) + 0.5*X**2/(1 + R**2)**0.5 + 0.4*Y**2/(1+R**2)**0.5)**2*(1 + R**2)**((pp - 2)/2)
    c, b = S.moments(rho, pp); c = float(c)
    Q, W1, W2 = Qfun(S, rho, pp)
    lhs = Rphi(S, rho, pp, W1, W2, c)
    d = lhs - (math.pi*c*(c-0.5) - Q)
    print(f'L={L:.0e}: c={c:.12f} Q={Q:.12f} diff={d:.4e} diff*L^0.4={d*L**0.4:.6f}', flush=True)
for nt in (128,):
    S = make(nt=nt)
    X, Y, R = S.X, S.Y, S.R
    for a in (1.5, 3.0):
        zeta = X*(1 + a*Y/(1 + R**2)**0.5)*(1 + R**2)**(-3/8)
        new, d = S.T(zeta, p_tail=0.5, info=True)
        c1, b1 = S.moments(new**2, 1/d['cl'])
        print(f'nt={nt} a={a}: cl={d["cl"]:.8f} c1={float(c1):.6f} b1={float(b1):.1e}', flush=True)
