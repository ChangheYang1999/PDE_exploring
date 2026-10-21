# Mode-level test of the spectral-element inverse against direct quadrature of the Green's function.
import sys, numpy as np
sys.path.insert(0, '.')
from vinv import Panels, solve_modes
from scipy.integrate import quad
def phi_f(t, n):
    r = np.exp(t)
    return r**4 / (1 + r**2)**(1.41) * (1 + 0.3*np.cos(3*t)/(1+r**2))   # ~ r^4 at 0, r^1.18 at inf
mu_r = [1.18, -0.82, -2.82]
for p, hmax in [(8, 0.5), (12, 0.25), (16, 0.25)]:
    br = np.arange(-12, 30 + 1e-9, hmax)
    pan = Panels(br, p)
    ns = [1, 2, 5, 40]
    phi = np.stack([phi_f(pan.t, n) for n in ns], 1)
    psi, dpsi, tail = solve_modes(pan, phi, ns, mu_left=(4.0,), mu_right=mu_r)
    errs = []
    for jn, n in enumerate(ns):
        e = 0
        for tt in [-3.0, 0.0, 0.7, 2.2, 8.0, 15.0]:
            i = np.argmin(np.abs(pan.t - tt)); t0 = pan.t[i]
            f1 = lambda s: np.exp(-2*n*abs(t0 - s)) * phi_f(s, n)
            # exact canonical value
            v = (quad(f1, -60, t0, limit=400, epsabs=0, epsrel=1e-13)[0] + quad(f1, t0, t0+40/n+40, limit=400, epsabs=0, epsrel=1e-13)[0]) / (4*n)
            dv = (-quad(f1, -60, t0, limit=400, epsabs=0, epsrel=1e-13)[0] + quad(f1, t0, t0+40/n+40, limit=400, epsabs=0, epsrel=1e-13)[0]) / 2
            e = max(e, abs(psi[i, jn] - v)/abs(v), abs(dpsi[i, jn] - dv)/abs(dv))
        errs.append(e)
    print(p, hmax, pan.N, 'max rel err psi, dpsi per mode', ['%.2e' % e for e in errs], 'tail fit', tail['right_fit_relres'])
