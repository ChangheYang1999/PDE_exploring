"""Check: (i) H = N g^{3+2/A} |w|^{-2/A}, N = A^{2/A}/g0^{3+2/A}; (ii) with the exact axis constraints
a2 = (g' - w'')/2, b3 = -a2'/3, h = 2c_l - w', B_3 depends only on (w, c_l):
   B_3 = (1/(3N)) f.p. int_0^{x*} (a2/g^3)' (|w|/g)^{2/A-1} dx.
Compatible data built from w alone at c_l = 1.3 and 2.2 (g from w g' = (w' - A) g, g(x*) = 1)."""
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from b3_diag import AxisData

X = sp.symbols('x')
for cl in (1.3, 2.2):
    A = 2 * cl - 1
    ws = -A * X * (1 - X**2) / (1 + X**2) * (1 + 0.3 * X**2 * (1 - X**2))  # keeps w'(0) = -A, w'(1) = A
    wd = [sp.lambdify(X, sp.diff(ws, X, k), 'numpy') for k in range(4)]
    # g: log g' = (w'-A)/w; regular parts: (w'-A)/w = 2/x - 0 ... integrate numerically from x* side with series
    # use ln g(x) = -int_x^{1} (w'-A)/w dt, integrand regular at t=1 (w'(1) = A)
    lg_rhs = lambda t: (wd[1](t) - A) / wd[0](t)
    xs_grid = np.linspace(-0.5, 0.999999, 1)  # placeholder
    sol = solve_ivp(lambda t, y: [lg_rhs(t) if abs(t) > 1e-12 else 0.0], [1 - 1e-7, 1e-3], [0.0],
                    method='DOP853', rtol=1e-13, atol=1e-15, dense_output=True)
    # extend to x<0 by evenness; near 0 g ~ g0 x^2: ln g - 2 ln x is regular
    def g(x):
        x = np.abs(np.asarray(x, float))
        return np.exp(sol.sol(np.clip(x, 1e-3, 1 - 1e-7))[0])
    # symbolic-free derivatives via the ODE
    def gp(x):
        x = np.asarray(x, float)
        return g(x) * (wd[1](x) - A) / wd[0](x)
    def gpp(x):
        x = np.asarray(x, float)
        w, w1, w2 = wd[0](x), wd[1](x), wd[2](x)
        return gp(x) * (w1 - A) / w + g(x) * (w2 * w - (w1 - A) * w1) / w**2
    a2 = lambda x: (gp(x) - wd[2](x)) / 2
    a2p = lambda x: (gpp(x) - wd[3](x)) / 2
    b3 = lambda x: -a2p(x) / 3
    h = lambda x: 2 * cl - wd[1](x)
    print(f"c_l={cl}: g ODE residual check at 0.5:", gp(0.5) * wd[0](0.5) - (wd[1](0.5) - A) * g(0.5))
    # g0 = lim g/x^2
    g0 = g(1e-3) / 1e-6
    d = AxisData(wd[0], h, a2, b3, g, gp, cl, 1.0)
    N = A**(2 / A) / g0**(3 + 2 / A)
    xx = np.array([0.05, 0.2, 0.5, 0.8, 0.95])
    print('   H / (N g^{3+2/A}|w|^{-2/A}) - 1 =', d.H(xx) / (N * g(xx)**(3 + 2 / A) * np.abs(wd[0](xx))**(-2 / A)) - 1)
    bfp, info = d.b3_fp()
    # w-only formula: integrand (1/(3N)) (a2/g^3)' (|w|/g)^{2/A-1} equals -F3/(wH) pointwise
    t = np.array([0.1, 0.3, 0.6, 0.9])
    q = a2(t) / g(t)**3
    qp = (a2p(t) - 3 * a2(t) * gp(t) / g(t)) / g(t)**3
    lhs = (1 / (3 * N)) * qp * (np.abs(wd[0](t)) / g(t))**(2 / A - 1)
    rhs = -d.F3(t) / (wd[0](t) * d.H(t))
    print('   integrand ratio (w-only / direct) - 1 =', lhs / rhs - 1, '   fp B3 =', bfp, ' odd_rel', info['odd_rel'])
