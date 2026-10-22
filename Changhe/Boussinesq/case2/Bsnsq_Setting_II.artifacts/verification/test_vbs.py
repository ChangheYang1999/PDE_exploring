# Manufactured tests for the verifier's modal Biot-Savart evaluator (M1).
import numpy as np, sympy as sp, time, sys
sys.path.insert(0, 'scripts')
from vbs import bs_modal, strain_origin
x, y = sp.symbols('x y', real=True)
def make(Psi):
    Om = sp.simplify(-(sp.diff(Psi, x, 2) + sp.diff(Psi, y, 2)))
    f = {k: sp.lambdify((x, y), e, 'numpy') for k, e in
         dict(Om=Om, Psi=Psi, U1=-sp.diff(Psi, y), U2=sp.diff(Psi, x),
              U1x=-sp.diff(Psi, x, y), U1y=-sp.diff(Psi, y, 2), U2x=sp.diff(Psi, x, 2)).items()}
    pxy0 = sp.limit(sp.limit(sp.diff(Psi, x, y), x, 0), y, 0)
    return f, float(pxy0)
tests = {
 'gauss': x*y*sp.exp(-(x**2+y**2)),
 'alg_a1/3': x*y*(1+x**2+y**2)**sp.Rational(-1, 6),       # Omega ~ r^{-1/3}
 'alg_a1/5': x*y*(x**2-y**2+2*x*y**0)*(1+x**2+y**2)**sp.Rational(-11, 10) if False else
             x*y*(1 + x**2 + 3*y**2)**sp.Rational(-1, 10),  # Omega ~ r^{-1/5}, many modes
 'mix': x*y*(3*x**2 - y**2 + 1)*sp.exp(-(x**2+2*y**2)/2) + x**3*y*(1+x**2+y**2)**sp.Rational(-7, 6),
}
rng = np.random.default_rng(1)
for name, P in tests.items():
    f, pxy0 = make(P)
    Om = lambda X, Y, f=f: f['Om'](X, Y) + 0*X
    # random targets in Q1, log-uniform radius 1e-3..1e3
    nt = 400
    r = 10**rng.uniform(-3, 3, nt); ph = rng.uniform(0, np.pi/2, nt)
    xt, yt = r*np.cos(ph), r*np.sin(ph)
    t0 = time.time()
    o = bs_modal(Om, xt, yt, nphi=256, p=16, second=True)
    dt = time.time()-t0
    sc = np.abs(f['U1'](xt, yt)) + np.abs(f['U2'](xt, yt))
    e1 = np.abs(o['U1']-f['U1'](xt, yt)); e2 = np.abs(o['U2']-f['U2'](xt, yt))
    eg = np.abs(o['U1x']-f['U1x'](xt, yt)) + np.abs(o['U1y']-f['U1y'](xt, yt)) + np.abs(o['U2x']-f['U2x'](xt, yt))
    ep = np.abs(o['Psi']-f['Psi'](xt, yt))
    so = strain_origin(Om)
    print(f"{name:10s} time {dt:5.1f}s  max|dU| {max(e1.max(), e2.max()):.2e}  max rel {np.max((e1+e2)/sc):.2e}"
          f"  max|dDU| {eg.max():.2e}  max|dPsi| {ep.max():.2e}  Psi_xy(0): {so:.14f} exact {pxy0:.14f}")
print('--- with analytic power-law tails ---')
for name, P, a in [('alg_a1/3', tests['alg_a1/3'], [1/3, 1/3+2, 1/3+4]), ('alg_a1/5', tests['alg_a1/5'], [0.2, 2.2, 4.2])]:
    f, pxy0 = make(P)
    Om = lambda X, Y, f=f: f['Om'](X, Y) + 0*X
    nt = 400
    r = 10**rng.uniform(-3, 3, nt); ph = rng.uniform(0, np.pi/2, nt)
    xt, yt = r*np.cos(ph), r*np.sin(ph)
    for xm in [40.0, 80.0]:
        o = bs_modal(Om, xt, yt, nphi=256, p=16, second=True, xi_max=xm, tail_alpha=a)
        e = np.abs(o['U1']-f['U1'](xt, yt)) + np.abs(o['U2']-f['U2'](xt, yt))
        sc = np.abs(f['U1'](xt, yt)) + np.abs(f['U2'](xt, yt))
        print(f"{name} xi_max={xm}: max|dU| {e.max():.2e} max rel {np.max(e/sc):.2e} max|dPsi| {np.abs(o['Psi']-f['Psi'](xt,yt)).max():.2e}")
