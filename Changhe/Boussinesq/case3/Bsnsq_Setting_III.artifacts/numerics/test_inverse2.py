import sys, time, numpy as np, torch, sympy as sp
sys.path.insert(0, '.')
from bq3core import Basis, Geometry, Problem, DT
from test_inverse import make_case, run
x, y = sp.symbols('x y', real=True)
r2 = x**2 + y**2
beta = 3.0
# h ~ r^{1-2/beta} = r^{1/3}: leading x^2 (1+r^2/4)^{-5/6} ~ r^{1/3}; Omega ~ r^{-2/3}
h2 = (1 + y / 2 + x**2 / 5) * (1 + r2 / 4) ** (-sp.Rational(5, 6))
for (Nt, deg, K, Nphi) in [(40, 5, 16, 32), (80, 5, 24, 48), (120, 7, 32, 64), (160, 7, 40, 80)]:
    run(beta, 1.5, Nt, deg, K, Nphi, h2, 'slow2')
