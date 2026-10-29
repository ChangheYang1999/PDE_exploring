# Lead check of the 5D Green representation used for the S1 moment identities:
#   phi(0, z1)   = (1/4) int_0^inf int_R r^3 eta / rho^3 dz dr,
#   phi_z(0, z1) = (3/4) int_0^inf int_R (z - z1) r^3 eta / rho^5 dz dr,   rho^2 = r^2 + (z - z1)^2,
# for a decaying phi with eta = -Delta_5 phi. Test field: phi = (z + 0.3) / (1 + r^2 + (z - 0.2)^2)^k.
import numpy as np, sympy as S
from scipy import integrate
r, z = S.symbols('r z', positive=True)
k = S.Rational(3, 2)
phi = (z + S.Rational(3, 10)) / (1 + r**2 + (z - S.Rational(1, 5))**2)**k
eta = S.simplify(-(S.diff(phi, r, 2) + 3*S.diff(phi, r)/r + S.diff(phi, z, 2)))
fe = S.lambdify((r, z), eta, 'numpy')
fphi = S.lambdify((r, z), phi, 'numpy'); fphiz = S.lambdify((r, z), S.diff(phi, z), 'numpy')
for z1 in (0.0, 0.7, -1.3):
    # polar coordinates about (0, z1): r = rho sin t, z - z1 = rho cos t, dr dz = rho drho dt
    g0 = lambda t, p: (p*np.sin(t))**3 * fe(p*np.sin(t), z1 + p*np.cos(t)) / p**3 * p
    g1 = lambda t, p: np.cos(t) * (p*np.sin(t))**3 * fe(p*np.sin(t), z1 + p*np.cos(t)) / p**4 * p
    opts = dict(epsabs=1e-11, epsrel=1e-11, limit=400)
    I0 = sum(integrate.dblquad(g0, a, b, 0, np.pi, epsabs=1e-12, epsrel=1e-12)[0] for a, b in ((0, 1), (1, 10), (10, 100), (100, 1e4)))
    I1 = sum(integrate.dblquad(g1, a, b, 0, np.pi, epsabs=1e-12, epsrel=1e-12)[0] for a, b in ((0, 1), (1, 10), (10, 100), (100, 1e4)))
    print(f'z1={z1:+.2f}  phi: {0.25*I0:.10f} vs {float(fphi(0.0, z1)):.10f}   phi_z: {0.75*I1:.10f} vs {float(fphiz(1e-300, z1)):.10f}')
