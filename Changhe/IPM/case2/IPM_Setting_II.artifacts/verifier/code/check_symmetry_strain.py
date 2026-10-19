"""(1) Symmetries of the profile system (sympy, generic functions).
(2) Strain formulas c = psi_xy(0) = (1/pi) int rho sin(3a) s^-2 ds da, b = psi_yy(0) = -(1/pi) int rho cos(3a) s^-2 ds da
    (canonical sublinear law) tested on a manufactured asymmetric growing field."""
import sympy as sp, numpy as np, sys
sys.path.insert(0, 'code')
x, y, cl = sp.symbols('x y c_l', real=True)
rho = sp.Function('rho'); psi = sp.Function('psi')
def ops(r, p):
    U1 = -sp.diff(p, y); U2 = sp.diff(p, x)
    U10 = U1.subs({x: 0, y: 0}); U20 = U2.subs({x: 0, y: 0})
    T = (cl*x + U1 - U10)*sp.diff(r, x) + (cl*y + U2 - U20)*sp.diff(r, y) - r
    P = -sp.diff(p, x, 2) - sp.diff(p, y, 2) - sp.diff(r, x)
    return T, P
T0, P0 = ops(rho(x, y), psi(x, y))
cases = {
  'S_x: rho(-x,y), psi -> -psi(-x,y)': (rho(-x, y), -psi(-x, y), {x: -x}, 1),
  'S_y: -rho(x,-y), psi -> -psi(x,-y)': (-rho(x, -y), -psi(x, -y), {y: -y}, -1),
  'S_xy: -rho(-x,-y), psi -> psi(-x,-y)': (-rho(-x, -y), psi(-x, -y), {x: -x, y: -y}, -1),
  'point refl. rho(-x,-y), psi -> -psi(-x,-y) (not expected)': (rho(-x, -y), -psi(-x, -y), {x: -x, y: -y}, 1),
}
for name, (r, p, sub, sg) in cases.items():
    T, P = ops(r, p)
    # transformed residual should equal sg * (original residual evaluated at reflected point)
    Tr = T0.subs(sub, simultaneous=True).doit(); Pr = P0.subs(sub, simultaneous=True).doit()
    okT = [sgn for sgn in (1, -1) if sp.simplify((T - sgn*Tr).doit()) == 0]
    okP = [sgn for sgn in (1, -1) if sp.simplify((P - sgn*Pr).doit()) == 0]
    print(f'{name}:  transport residual maps to sign {okT} x original;  poisson residual maps to sign {okP} x original')

from polar_inverse import PolarGrid
Q = (x - 0.7)**2 + 2*(y + 0.4)**2 + 0.5*(x - 0.7)*(y + 0.4)
phi = (1 + Q)**sp.Rational(13, 10) + sp.Rational(3, 10)*sp.sin(2*x)*sp.exp(-(x**2 + y**2)/4)
rho_e = -(sp.diff(phi, x, 2) + sp.diff(phi, y, 2))
c_ex = float(sp.diff(phi, x, 2, y, 1).subs({x: 0, y: 0}).evalf())
b_ex = float(sp.diff(phi, x, 1, y, 2).subs({x: 0, y: 0}).evalf())
f = sp.lambdify((x, y), rho_e, 'numpy')
edges = np.concatenate([[0.0], np.linspace(0.25, 8, 30), np.geomspace(8.5, 1e10, 30)])
G = PolarGrid(edges, 20, 256)
R = f(G.X, G.Y)
dth = 2*np.pi/G.nt
c_num = (1/np.pi)*np.sum(G.w[:, None]*dth*R*np.sin(3*G.T)/G.R**2)
b_num = -(1/np.pi)*np.sum(G.w[:, None]*dth*R*np.cos(3*G.T)/G.R**2)
print(f'strain formula test: c exact {c_ex:.15f} quadrature {c_num:.15f};  b exact {b_ex:.15f} quadrature {b_num:.15f}')
rx0 = float(sp.diff(rho_e, x).subs({x: 0, y: 0}).evalf()); ry0 = float(sp.diff(rho_e, y).subs({x: 0, y: 0}).evalf())
print(f'with local terms: c = I_sin - rho_y(0)/4 = {c_num - ry0/4:.15f} (exact {c_ex:.15f});  b = I_cos - rho_x(0)/4 = {b_num - rx0/4:.15f} (exact {b_ex:.15f})')
