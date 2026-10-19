"""Check specification identity I3 in its off-shell form (valid for any rho, not only solutions):
   for phi homogeneous of degree -m (2+p < m < 4), R = (c_l X + W).grad rho - rho,
   (1 + 2 c_l - m c_l) int rho phi + int rho W.grad phi = - int R phi.
Uses the independent polar inverse (code/polar_inverse.py) for W and exact gradients of rho."""
import numpy as np, sympy as sp, sys
sys.path.insert(0, 'code')
from polar_inverse import PolarGrid
x, y = sp.symbols('x y', real=True)
r2 = x**2 + y**2
fields = {
 'localized': (x**2 + 0.3*x*y + 0.2*y**3 - 0.1*x**3)*sp.exp(-(x**2 + 2*y**2)/3),
 'growth p=0.6': (x**2 + 0.3*x*y - 0.4*x*y**2 + 0.25*y**3)*(1 + r2 + 0.3*x*y)**sp.Rational(-6, 5) + 0.2*x**2*sp.exp(-r2),
}
edges = np.concatenate([[0.0], np.geomspace(1e-3, 0.25, 12), np.linspace(0.3, 8, 30), np.geomspace(8.5, 1e10, 40)])
G = PolarGrid(edges, 20, 256)
dth = 2*np.pi/G.nt
integ = lambda F: np.sum(G.w[:, None]*dth*G.R*F)
for name, re in fields.items():
    f = sp.lambdify((x, y), re, 'numpy')
    fx = sp.lambdify((x, y), sp.diff(re, x), 'numpy'); fy = sp.lambdify((x, y), sp.diff(re, y), 'numpy')
    rho = f(G.X, G.Y); rx = fx(G.X, G.Y); ry = fy(G.X, G.Y)
    W1, W2 = G.velocity(rho)
    for cl in (1.3, 1.7):
        R = (cl*G.X + W1)*rx + (cl*G.Y + W2)*ry - rho
        for m, Phi, dPhi in [(3, np.sin(3*G.T), 3*np.cos(3*G.T)), (3, np.cos(3*G.T), -3*np.sin(3*G.T)),
                             (3.5, np.sin(3*G.T) + 0.4*np.cos(G.T), 3*np.cos(3*G.T) - 0.4*np.sin(G.T))]:
            ph = G.R**(-m)*Phi
            # grad phi in Cartesian: e_r * (-m) r^{-m-1} Phi + e_th * r^{-m-1} Phi'
            gr = -m*G.R**(-m-1)*Phi; gt = G.R**(-m-1)*dPhi
            c, s = np.cos(G.T), np.sin(G.T)
            gx = c*gr - s*gt; gy = s*gr + c*gt
            lhs = (1 + 2*cl - m*cl)*integ(rho*ph) + integ(rho*(W1*gx + W2*gy))
            rhs = -integ(R*ph)
            print(f'{name:14s} c_l={cl} m={m}: lhs {lhs:+.14e}  -int R phi {rhs:+.14e}  diff {lhs-rhs:.2e}')
