"""(n4) second test density, phi = (1 + x^2) e^{-(x^2 + 2 y^2)}, rho = (1/2) d_y Lap phi.
(n4): kernel representation of Q on the axis.
Claim (FINAL_REPORT 6.4): (g' - w'')/2 = g'/4 - (12/pi) I(x), i.e. w'' = g'/2 + (24/pi) I(x), where
I(x) = lim_{eps->0} int over the quadrant minus the half-disk (u-x)^2+v^2<=eps^2 of
[J(x-u,v) + J(x+u,v)] rho(u,v), J(t,v) = t v (t^2-v^2)/(t^2+v^2)^4.
Test density rho = v (8 - 4(u^2+v^2)) e^{-(u^2+v^2)} = (1/2) d_y Lap e^{-r^2}; then (canonical law
U_1^ = xi1 xi2/|xi|^2 rho^) U_1 = (1/2) d_x d_y^2 e^{-r^2} in closed form, so w'' = d_x^2 U_1(x,0) exactly.
I(x): own quadrature, polar coordinates about (x,0) on the half-disk of radius delta (angular pairing a, pi-a),
polar outside with the quadrant cut, plain tensor Gauss-Legendre for the J(x+u,v) term; delta varied.
"""
import numpy as np, sympy as sp
X, Y = sp.symbols('x y', real=True)
E = sp.exp(-(X**2 + 2*Y**2))*(1 + X**2)
rho_s = sp.Rational(1, 2)*sp.diff(sp.diff(E, X, 2) + sp.diff(E, Y, 2), Y)
assert sp.simplify(rho_s - sp.Rational(1, 2)*sp.diff(sp.diff(E, X, 2) + sp.diff(E, Y, 2), Y)) == 0
U1 = sp.Rational(1, 2)*sp.diff(E, X, 1, Y, 2)
# check the velocity law in physical space: U = (-psi_y, psi_x), -Lap psi = d_x rho  =>  psi = -(1/2) d_x d_y e^{-r^2}... verify
psi = -sp.Rational(1, 2)*sp.diff(E, X, 1, Y, 1)
assert sp.simplify(-(sp.diff(psi, X, 2) + sp.diff(psi, Y, 2)) - sp.diff(rho_s, X)) == 0
assert sp.simplify(-sp.diff(psi, Y) - U1) == 0
wpp = sp.lambdify(X, sp.diff(U1, X, 2).subs(Y, 0), 'numpy')
g = sp.diff(rho_s, Y).subs(Y, 0)
gp = sp.lambdify(X, sp.diff(g, X), 'numpy')
rho = sp.lambdify((X, Y), rho_s, 'numpy')

def J(t, v):
    r2 = t*t + v*v
    return t*v*(t*t - v*v)/r2**4

def gl(n, a, b):
    z, w = np.polynomial.legendre.leggauss(n)
    return 0.5*(b - a)*z + 0.5*(b + a), 0.5*(b - a)*w

def I_of(x, delta, n=200, R=12.0):
    # (1) half-disk s < delta about (x,0): pair a and pi - a (J odd in t)
    s, ws = gl(n, 0.0, delta)
    a, wa = gl(n, 0.0, np.pi/2)
    S, A = np.meshgrid(s, a, indexing='ij')
    c, sn = np.cos(A), np.sin(A)
    # point (u,v) = (x + s cos a, s sin a): t = x - u = -s cos a
    f = J(-S*c, S*sn)*(rho(x + S*c, S*sn) - rho(x - S*c, S*sn))*S
    I1 = np.einsum('i,j,ij->', ws, wa, f)
    # (2) outside: s > delta, a in (0, pi), u = x + s cos a > 0
    a2, wa2 = gl(2*n, 0.0, np.pi)
    I2 = 0.0
    for ai, wai in zip(a2, wa2):
        ca, sa = np.cos(ai), np.sin(ai)
        smax = R if ca >= 0 else min(R, x/(-ca))
        if smax <= delta:
            continue
        # split [delta, smax] in panels to resolve the Gaussian
        edges = np.linspace(delta, smax, 9)
        for lo, hi in zip(edges[:-1], edges[1:]):
            ss, wss = gl(60, lo, hi)
            I2 += wai*np.sum(wss*J(-ss*ca, ss*sa)*rho(x + ss*ca, ss*sa)*ss)
    # (3) J(x+u, v) over the quadrant: regular (singularity at (-x,0))
    I3 = 0.0
    ue = np.linspace(0, R, 25)
    for lo, hi in zip(ue[:-1], ue[1:]):
        uu, wu = gl(40, lo, hi)
        for lo2, hi2 in zip(ue[:-1], ue[1:]):
            vv, wv = gl(40, lo2, hi2)
            U, V = np.meshgrid(uu, vv, indexing='ij')
            I3 += np.einsum('i,j,ij->', wu, wv, J(x + U, V)*rho(U, V))
    return I1 + I2 + I3

print('x   delta   w_exact''   g\'/2 + (24/pi) I   diff')
for x in [0.3, 0.7, 1.0, 1.5, 2.2, 3.0]:
    for delta in [0.1*x, 0.5*x]:
        I = I_of(x, delta)
        lhs = wpp(x)
        rhs = gp(x)/2 + 24/np.pi*I
        print(f'{x:4.1f} {delta:6.3f} {lhs: .15e} {rhs: .15e} {lhs-rhs: .2e}')
    # alternative local coefficient check: what local term would be needed
    print(f'      needed local/g\' = {(wpp(x) - 24/np.pi*I)/gp(x): .12f}')
