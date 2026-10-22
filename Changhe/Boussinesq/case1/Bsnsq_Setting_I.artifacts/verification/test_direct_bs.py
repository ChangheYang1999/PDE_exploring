import numpy as np, sympy as sp, sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from direct_bs import direct_velocity
from bs_modal import ModalBS
X, Y = sp.symbols('x y', real=True)
Psi = X * Y * sp.exp(-(X**2 + 2 * Y**2)) * (1 + X**2 - Y**4 / 3)
Om = sp.lambdify((X, Y), sp.simplify(-(sp.diff(Psi, X, 2) + sp.diff(Psi, Y, 2))), 'numpy')
U1f = sp.lambdify((X, Y), -sp.diff(Psi, Y), 'numpy'); U2f = sp.lambdify((X, Y), sp.diff(Psi, X), 'numpy')
pts = np.array([[0.3, 0.2], [1.1, -0.7], [-2.0, 0.5], [0.05, 1.3], [3.0, 3.0]])
for Na, npan in [(256, 120), (512, 200)]:
    U = direct_velocity(Om, pts, rho_max=40, npan=npan, Na=Na)
    Ue = np.stack([U1f(pts[:, 0], pts[:, 1]), U2f(pts[:, 0], pts[:, 1])], 1)
    print('direct, Na', Na, 'max abs err', np.abs(U - Ue).max())
# algebraic tail with smooth cutoff, compared with the modal inverse of the same cut-off field
Psi2 = X * Y * (1 + X**2 + Y**2) ** sp.Rational(-1, 5)
Om2 = sp.lambdify((X, Y), sp.simplify(-(sp.diff(Psi2, X, 2) + sp.diff(Psi2, Y, 2))), 'numpy')
R = 30.0
chi = lambda x, y: np.exp(-((x**2 + y**2) / R**2) ** 4)
Omc = lambda x, y: Om2(x, y) * chi(x, y)
U = direct_velocity(Omc, pts, rho_max=200, npan=240, Na=512)
r = np.hypot(pts[:, 0], pts[:, 1]); ph = np.arctan2(pts[:, 1], pts[:, 0])
br = np.unique(np.concatenate([np.geomspace(1e-7, 300, 301), r]))
bs = ModalBS(br, npg=16, M=256); bs.set_omega_func(Omc); bs.solve()
ib = np.searchsorted(br, r)
U1m, U2m, _ = bs.velocity(ib, ph)
print('cut-off algebraic field: direct vs modal max abs diff', np.abs(U - np.stack([U1m, U2m], 1)).max(), ' |U| ~', np.abs(U).max())
