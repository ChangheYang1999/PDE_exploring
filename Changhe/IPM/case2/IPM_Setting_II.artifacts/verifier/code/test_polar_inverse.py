"""Manufactured tests for code/polar_inverse.py: rho = -Lap phi, exact U = grad^perp d_x phi - (same at 0)."""
import numpy as np, sympy as sp, sys, time
sys.path.insert(0, 'code')
from polar_inverse import PolarGrid

x, y = sp.symbols('x y', real=True)
def manufactured(phi):
    rho = -(sp.diff(phi, x, 2) + sp.diff(phi, y, 2))
    U1 = -sp.diff(phi, x, y); U2 = sp.diff(phi, x, 2)
    f = [sp.lambdify((x, y), e, "numpy") for e in (rho, U1, U2)]
    return f

def run(name, phi, edges, q, nt, ren=(2,)):
    frho, fU1, fU2 = manufactured(phi)
    G = PolarGrid(edges, q, nt)
    rho = frho(G.X, G.Y) * np.ones_like(G.X)
    t0 = time.time()
    U1, U2 = G.velocity(rho, ren_modes=ren, rho0=float(frho(0.0, 0.0)))
    dt = time.time() - t0
    E1 = U1 - (fU1(G.X, G.Y) - fU1(0.0, 0.0)); E2 = U2 - (fU2(G.X, G.Y) - fU2(0.0, 0.0))
    for Rm in (2, 5, 10):
        msk = G.R < Rm
        err = max(np.abs(E1[msk]).max(), np.abs(E2[msk]).max())
        sc = max(np.abs(U1[msk]).max(), np.abs(U2[msk]).max())
        print(f'{name:28s} q={q} P={G.P} nt={nt}  |X|<{Rm:3d}: max|U-Uex| = {err:.3e}  (max|U| {sc:.2e})  t={dt:.2f}s')

geo = lambda r0, L, n: np.concatenate([[0.0], np.geomspace(r0, L, n)])
Q = (x - 0.7)**2 + 2*(y + 0.4)**2 + 0.5*(x - 0.7)*(y + 0.4)
tests = {
  'C: localized exp(-Q)': sp.exp(-Q),
  'A: decay (1+Q)^0.5': (1 + Q)**sp.Rational(1, 2),
  'B: growth k=0.6 (1+Q)^1.3': (1 + Q)**sp.Rational(13, 10),
  'D: growth + oscillation': (1 + Q)**sp.Rational(13, 10) + sp.Rational(3, 10)*sp.sin(2*x)*sp.exp(-(x**2 + y**2)/4),
}
for name, phi in tests.items():
    for (q, P, nt, L) in [(12, 30, 128, 1e6), (16, 40, 256, 1e8), (20, 60, 256, 1e10)]:
        edges = np.concatenate([[0.0], np.linspace(0.25, 8, P // 2), np.geomspace(8.5, L, P // 2)])
        run(name, phi, edges, q, nt)
