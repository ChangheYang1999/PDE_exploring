import numpy as np, sympy as sp, sys
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from bs_modal import ModalBS

X, Y = sp.symbols('x y', real=True)
def make(Psi):
    Om = -(sp.diff(Psi, X, 2) + sp.diff(Psi, Y, 2))
    U1 = -sp.diff(Psi, Y); U2 = sp.diff(Psi, X)
    f = lambda e: sp.lambdify((X, Y), e, 'numpy')
    return f(sp.simplify(Om)), f(U1), f(U2), float(sp.diff(Psi, X, Y).subs({X: 0, Y: 0}))

tests = {
  'gauss': X * Y * sp.exp(-(X**2 + Y**2)),
  'aniso': X * Y * sp.exp(-(X**2 + 2 * Y**2)) * (1 + X**2 - Y**4 / 3),
  'alg_p0.2': X * Y * (1 + X**2 + Y**2) ** sp.Rational(-1, 5),
}
for name, Psi in tests.items():
    Omf, U1f, U2f, c0 = make(Psi)
    for (npg, M, Rmax, npan) in [(12, 64, 1e3, 120), (16, 128, 1e4, 200), (20, 256, 1e6, 300)]:
        breaks = np.geomspace(1e-6, Rmax, npan + 1)
        bs = ModalBS(breaks, npg=npg, M=M)
        bs.set_omega_func(Omf)
        tail = None
        if name.startswith('alg'):
            p = 0.2
            # exact tail for mode 1 only, w_1 ~ (r^2/2) g(r^2) with Omega = xy g ; leading: w_1 ~ 2p(2-p) rho^-2p (1+O(rho^-2))
            def tail(k, R, p=p):
                out = np.zeros(len(k)); al = 2 * p
                out[0] = 2 * p * (2 - p) * R ** (1 - al) / (al) # int_R^inf (R/rho) c rho^-al drho = c R^(1-al)/al
                return out
        bs.solve(tail=tail)
        ib = np.arange(0, npan + 1, max(1, npan // 40))
        ib = ib[(breaks[ib] > 1e-3) & (breaks[ib] < min(Rmax, 50))]
        rng = np.random.default_rng(0)
        phi = rng.uniform(0, 2 * np.pi, size=ib.shape)
        U1, U2, Psi_ = bs.velocity(ib, phi)
        r = breaks[ib]
        U1e = U1f(r * np.cos(phi), r * np.sin(phi)); U2e = U2f(r * np.cos(phi), r * np.sin(phi))
        err = np.max(np.hypot(U1 - U1e, U2 - U2e) / (1e-300 + np.maximum(1, np.hypot(U1e, U2e))))
        print(f'{name:9s} npg={npg} M={M} Rmax={Rmax:.0e}: max rel vel err {err:.2e}; Psi_xy(0) {bs.strain0():.12f} exact {c0:.12f}')
