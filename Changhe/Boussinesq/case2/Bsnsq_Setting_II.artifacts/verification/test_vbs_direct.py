import numpy as np, sympy as sp, time, sys
sys.path.insert(0, 'scripts')
from vbs import bs_modal
from vbs_direct import bs_direct
x, y = sp.symbols('x y', real=True)
def make(Psi):
    Om = -(sp.diff(Psi, x, 2) + sp.diff(Psi, y, 2))
    return {k: sp.lambdify((x, y), e, 'numpy') for k, e in
            dict(Om=Om, U1=-sp.diff(Psi, y), U2=sp.diff(Psi, x)).items()}
rng = np.random.default_rng(2)
for name, P in [('gauss', x*y*sp.exp(-(x**2+y**2))),
                ('alg4', x*y*(3*x**2-y**2+1)*(1+x**2+y**2)**(-4)),
                ('aniso', x*y*sp.exp(-(4*x**2+y**2/4)) * (1+x*y))]:
    f = make(P)
    Om = lambda X, Y, f=f: f['Om'](X, Y) + 0*X
    nt = 24
    r = 10**rng.uniform(-1.5, 1.2, nt); ph = rng.uniform(0, np.pi/2, nt)
    ph[:3] = [0, np.pi/2, 1e-3]
    xt, yt = r*np.cos(ph), r*np.sin(ph)
    t0 = time.time()
    U1, U2 = bs_direct(Om, xt, yt)
    t1 = time.time()
    o = bs_modal(Om, xt, yt, nphi=256)
    e_d = np.abs(U1-f['U1'](xt, yt)) + np.abs(U2-f['U2'](xt, yt))
    e_m = np.abs(o['U1']-f['U1'](xt, yt)) + np.abs(o['U2']-f['U2'](xt, yt))
    print(f"{name}: direct {t1-t0:.1f}s max err {e_d.max():.2e}; modal max err {e_m.max():.2e}; |U|max {np.max(np.abs(f['U1'](xt,yt))+np.abs(f['U2'](xt,yt))):.2e}")
