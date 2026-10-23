"""Checks for the completed parts of A.3.25(ii), A.3.25(v) and A.3.26(iii) (rep4 item 8).

(A) Angular system of the frozen equation for H = r^d Theta(th), stream chi = r^{d+1} Phi(th):
    residue matrices at th = 0 and th = pi/2, equivariance under the two reflections, the Theta = 0 obstruction,
    the lattice solution, and a numerical matching (boundary conditions Phi(0+) = Phi(pi/2-) = 0) at two
    non-lattice parameter sets.
(B) Order eps^s of the rescaled forced equation with generic F, G, and the scaling of the cubic relation.
(C) The commutator identity L h_T = -(1/T) zeta'(s) h + a0 d_x g, -Lap g = f_T, for the cut-off lattice mode.
"""
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

th, d, A, a0, t = sp.symbols('theta d A a0 t', real=True)
Th, Ph, Pp = sp.symbols('Theta Phi Phip')

# transport: (A-1) sin cos Theta' = (d - 1 + (A-1) d cos^2) Theta + a0 ((d+1) cos Phi - sin Phi')
# Poisson:   Phi'' + (d+1)^2 Phi = -(d cos Theta - sin Theta')
N = (d - 1 + (A - 1) * d * sp.cos(th)**2) * Th + a0 * ((d + 1) * sp.cos(th) * Ph - sp.sin(th) * Pp)
dTh = N / ((A - 1) * sp.sin(th) * sp.cos(th))
dPp = -(d + 1)**2 * Ph - d * sp.cos(th) * Th + sp.sin(th) * dTh
rhs = [dTh, Pp, dPp]
Y = [Th, Ph, Pp]
M = sp.Matrix([[sp.diff(f, v) for v in Y] for f in rhs])
R0 = sp.simplify((th * M).applyfunc(lambda e: sp.limit(e, th, 0)))
R1 = sp.simplify(((th - sp.pi / 2) * M).applyfunc(lambda e: sp.limit(e, th, sp.pi / 2)))
print('(A) residue at 0:', R0.tolist())
print('    eigenvalues:', {sp.simplify(k): v for k, v in R0.eigenvals().items()}, ' rank:', R0.rank())
print('    residue at pi/2:', R1.tolist())
print('    eigenvalues:', {sp.simplify(k): v for k, v in R1.eigenvals().items()}, ' rank:', R1.rank(),
      ' R1 (1,0,1) - kappa_y (1,0,1):',
      sp.simplify(R1 * sp.Matrix([1, 0, 1]) - (a0 - d + 1) / (A - 1) * sp.Matrix([1, 0, 1])).T)
print('    regular parts: th*M - R0 and (th - pi/2)*M - R1 vanish at the points:',
      sp.simplify((th * M - R0).applyfunc(lambda e: sp.limit(e, th, 0))) == sp.zeros(3),
      sp.simplify(((th - sp.pi / 2) * M - R1).applyfunc(lambda e: sp.limit(e, th, sp.pi / 2))) == sp.zeros(3))

# equivariance: S (th -> -th, Theta, Phi odd) and T (th -> pi - th, Theta even, Phi odd)
fT, fP = sp.Function('fT'), sp.Function('fP')
def residuals(TT, PP):
    e1 = (A - 1) * sp.sin(th) * sp.cos(th) * sp.diff(TT, th) - (d - 1 + (A - 1) * d * sp.cos(th)**2) * TT \
        - a0 * ((d + 1) * sp.cos(th) * PP - sp.sin(th) * sp.diff(PP, th))
    e2 = sp.diff(PP, th, 2) + (d + 1)**2 * PP + d * sp.cos(th) * TT - sp.sin(th) * sp.diff(TT, th)
    return e1, e2
b1, b2 = residuals(fT(th), fP(th))
for name, (TT, PP), sub in (('S', (-fT(-th), -fP(-th)), -th), ('T', (fT(sp.pi - th), -fP(sp.pi - th)), sp.pi - th)):
    e1, e2 = residuals(TT, PP)
    ok = []
    for e, b in ((e1, b1), (e2, b2)):
        bb = b.subs(th, sub).doit()
        ok.append(sp.simplify(e.doit() - bb) == 0 or sp.simplify(e.doit() + bb) == 0)
    print('    equivariance under', name, ':', ok)

# Theta = 0 obstruction
C = sp.symbols('C')
Phi0 = C * sp.sin(th)**(d + 1)
print('    Theta = 0: transport residual of C sin^{d+1}:',
      sp.simplify((d + 1) * sp.cos(th) * Phi0 - sp.sin(th) * sp.diff(Phi0, th)),
      ' Poisson residual:', sp.simplify(sp.diff(Phi0, th, 2) + (d + 1)**2 * Phi0))

# lattice solution
lat = {A: sp.Rational(3, 2), d: sp.Rational(3, 2), a0: sp.Rational(9, 4)}
e1, e2 = residuals(sp.sin(th), -sp.sin(2 * th) / 9)
print('    lattice (sin th, -sin 2th/9) at A = d = 3/2, a0 = 9/4:',
      sp.simplify(e1.subs(lat)), sp.simplify(e2.subs(lat)))
# Cartesian form of the lattice pair
x, y = sp.symbols('x y', real=True)
r = sp.sqrt(x**2 + y**2)
H = y * sp.sqrt(r)
chi = -sp.Rational(2, 9) * x * y * sp.sqrt(r)
print('    Cartesian: frozen eq', sp.simplify(sp.Rational(3, 2) * x * sp.diff(H, x) + y * sp.diff(H, y) - H
                                         + sp.Rational(9, 4) * sp.diff(chi, x)),
      ' Poisson', sp.simplify(-sp.diff(chi, x, 2) - sp.diff(chi, y, 2) - sp.diff(H, x)))

# numerical matching
fnum = sp.lambdify((th, Th, Ph, Pp, A, a0, d), rhs, 'numpy')
for (Av, a0v, dv, alpha) in ((1.5, 3.0, 1.7, 0.2), (1.25, 2.0, 1.55, 0.2)):
    q0 = 1 + alpha
    kx = (Av * dv - 1) / (Av - 1)
    ky = (a0v - dv + 1) / (Av - 1)
    lo, hi = q0, min(2, a0v + 1 - (Av - 1) * q0)
    def f(s, Yv):
        return fnum(s, Yv[0], Yv[1], Yv[2], Av, a0v, dv)
    e0 = 1e-6
    L0, L1 = np.zeros(3), np.zeros(3)
    for k in range(3):
        Y0 = np.eye(3)[k]
        s0 = solve_ivp(f, (np.pi / 4, e0), Y0, method='Radau', rtol=1e-12, atol=1e-15)
        s1 = solve_ivp(f, (np.pi / 4, np.pi / 2 - e0), Y0, method='Radau', rtol=1e-12, atol=1e-15)
        # Phi(0+) and Phi(pi/2-) by first-order extrapolation from the end points
        L0[k] = s0.y[1, -1] - e0 * s0.y[2, -1]
        L1[k] = s1.y[1, -1] + e0 * s1.y[2, -1]
    Ym = np.cross(L0, L1)
    Ym /= np.linalg.norm(Ym)
    near0 = [1e-1, 1e-2, 1e-3, 1e-4]
    sa = solve_ivp(f, (np.pi / 4, e0), Ym, method='Radau', rtol=1e-12, atol=1e-15, t_eval=near0 + [e0])
    nearh = [np.pi / 2 - v for v in near0]
    sb = solve_ivp(f, (np.pi / 4, np.pi / 2 - e0), Ym, method='Radau', rtol=1e-12, atol=1e-15, t_eval=nearh + [np.pi / 2 - e0])
    grid = np.linspace(0.05, np.pi / 2 - 0.05, 7)
    sg = solve_ivp(f, (np.pi / 4, 0.05), Ym, method='Radau', rtol=1e-12, atol=1e-15, t_eval=grid[grid < np.pi / 4][::-1])
    sh = solve_ivp(f, (np.pi / 4, np.pi / 2 - 0.05), Ym, method='Radau', rtol=1e-12, atol=1e-15, t_eval=grid[grid > np.pi / 4])
    Thv = list(sg.y[0][::-1]) + list(sh.y[0])
    print(f'    numeric (A, a0, d) = ({Av}, {a0v}, {dv}): d-range ({lo}, {hi:.3f}), kappa_x = {kx:.4f}, '
          f'kappa_y = {ky:.4f}, rank of (l0, l1) = {np.linalg.matrix_rank(np.vstack([L0, L1]), tol=1e-8)}')
    print('      Theta at 6 interior angles (pi/4 excluded):', ' '.join(f'{v:.4f}' for v in Thv))
    print('      near 0, Theta/(th Phi\'), predicted -a0 d/(A (d - 1)) =', f'{-a0v * dv / (Av * (dv - 1)):.6f}:',
          ' '.join(f'{T / (tt * Pd):.6f}' for tt, T, Pd in zip(sa.t[:-1], sa.y[0][:-1], sa.y[2][:-1])),
          ' Phi(0+) ~', f'{sa.y[1, -1] - e0 * sa.y[2, -1]:.1e}')
    print('      near pi/2, Theta\' ~', ' '.join(f'{f(tt, Yv)[0]:.2e}' for tt, Yv in zip(sb.t[:-1], sb.y.T[:-1])),
          ' a0 Phi\'/((d - 1) Theta):', ' '.join(f'{a0v * Pd / ((dv - 1) * T):.6f}'
                                               for T, Pd in zip(sb.y[0][:-1], sb.y[2][:-1])),
          ' Phi(pi/2-) ~', f'{sb.y[1, -1] + e0 * sb.y[2, -1]:.1e}')

# (B) order eps^s of the rescaled equation with generic F, G
Z1, Z2, e, Cc, a, cl, mu = sp.symbols('Z1 Z2 e C a c_l mu', real=True)
F = sp.Function('F')(Z1, Z2)
G = sp.Function('G')(Z1, Z2)
c = 1 - cl
rt = a * Z2 + Cc * e * F
pt = c * Z1 * Z2 + Cc * e * G
U1, U2 = -sp.diff(pt, Z2), sp.diff(pt, Z1)
lhs = (cl * Z1 + U1) * sp.diff(rt, Z1) + (cl * Z2 + U2) * sp.diff(rt, Z2) - rt
ser = sp.expand(lhs)
c0 = ser.coeff(e, 0)
c1 = ser.coeff(e, 1)
target = Cc * ((2 * cl - 1) * Z1 * sp.diff(F, Z1) + Z2 * sp.diff(F, Z2) - F + a * sp.diff(G, Z1))
print('(B) order e^0:', sp.simplify(c0), '; order e^1 minus C[(A Z1 d1 + Z2 d2 - 1) F + a G_1]:',
      sp.simplify(c1 - target), '; order e^2 is C^2 (grad^perp G . grad F):',
      sp.simplify(ser.coeff(e, 2) - Cc**2 * (-sp.diff(G, Z2) * sp.diff(F, Z1) + sp.diff(G, Z1) * sp.diff(F, Z2))))
print('    Poisson: -Lap pt - d1 rt =', sp.simplify(-sp.diff(pt, Z1, 2) - sp.diff(pt, Z2, 2) - sp.diff(rt, Z1)),
      '(should be C e (-Lap G - F_1))')
# cubic relation b (a0 - 4A + 2 Delta) = 3 a0 H + 4 mu/eps^2 with the scalings
ep, s_, bF, HF, cF, Av_ = sp.symbols('epsilon s b_F H_F c_F A', positive=True)
b_eps = Cc * bF * ep**(s_ - 2)
H_eps = Cc * HF * ep**(s_ - 2)
Delta = Cc * cF * ep**s_
mu_eps = a * Delta
rel = b_eps * (a - 4 * Av_ + 2 * Delta) - 3 * a * H_eps - 4 * mu_eps / ep**2
lead = sp.simplify(sp.expand(rel * ep**(2 - s_) / Cc))
print('    cubic relation times eps^(2-s)/C:', sp.collect(sp.expand(lead), ep),
      ' -> at eps = 0 (s > 0):', sp.simplify(sp.expand(lead).subs(ep, 0)))

# (C) commutator identity for the cut-off lattice mode at A = d, a0 = (d - 1)(d + 3)
dd, T = sp.symbols('d T', positive=True)
X, Yc = sp.symbols('X Y', real=True)
R = sp.sqrt(X**2 + Yc**2)
ch = sp.Function('zeta')
sv = -sp.log(R) / T
cT = ch(sv)
h = Yc * R**(dd - 1)
k = -X * Yc * R**(dd - 1) / (dd + 3)
Ad, a0d = dd, (dd - 1) * (dd + 3)
frozen = sp.simplify(Ad * X * sp.diff(h, X) + Yc * sp.diff(h, Yc) - h + a0d * sp.diff(k, X))
pois = sp.simplify(-sp.diff(k, X, 2) - sp.diff(k, Yc, 2) - sp.diff(h, X))
print('(C) lattice mode: frozen residual', frozen, ', Poisson residual', pois)
hT = cT * h
explicit = Ad * X * sp.diff(hT, X) + Yc * sp.diff(hT, Yc) - hT + a0d * sp.diff(cT * k, X)
u = sp.symbols('u')
chi1 = sp.Subs(sp.Derivative(ch(u), u), u, sv)
chi2 = sp.Subs(sp.Derivative(ch(u), u, 2), u, sv)
claim = -(1 / T) * chi1 * h
print('    (A x d_x + y d_y - 1) h_T + a0 d_x (zeta(s) chi) + (1/T) zeta\'(s) h =',
      sp.simplify((explicit - claim).doit()))
fT_ = sp.diff(hT, X) + sp.diff(cT * k, X, 2) + sp.diff(cT * k, Yc, 2)
fclaim = (1 / T) * X * Yc * R**(dd - 3) * ((dd - 1) / (dd + 3) * chi1 - chi2 / (T * (dd + 3)))
print('    f_T := d_x h_T + Lap(zeta(s) chi) minus (1/T) x y r^(d-3) [((d-1)/(d+3)) zeta\' - zeta\'\'/(T (d+3))] =',
      sp.simplify((fT_ - fclaim).doit()))
