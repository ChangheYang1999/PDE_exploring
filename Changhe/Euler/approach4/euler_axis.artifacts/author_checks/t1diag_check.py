"""Lead check of the source-jet closure identities and the source strain kernel
used by the independent referee's T1 diagnostic (t1diag).

(1) Axis swirl equation (c z + 2 phi) q_z + (1 - 2 phi_z) q = 0 at a source z0 with
    c z0 + 2 phi(z0) = 0, phi_z(z0) = 1/2, q(z0) = K gives q_z = 2 K phi_zz / (1 + c).
(2) Axis vorticity equation (1 + c) eta + W.grad eta = d_z(q^2) at the source (W = 0)
    gives eta_K = 4 K^2 phi_zz / (1 + c)^2.
(3) eta_phi = -Delta_5 phi on the axis equals -(4 phi_rr + phi_zz).
(4) Newton kernel: phi_z at the 5D centre equals
    (3/4) int_0^inf dR int_{-1}^{1} mu (1 - mu^2) eta dmu   (R = e^x gives the e^x dx form),
    tested on phi = z exp(-R^2), phi = z (1 + z^2) exp(-R^2) and phi = z exp(-r^2 - 2 z^2).
"""
import json, sympy as sp
from mpmath import mp, quad, mpf
mp.dps = 30
c, K, z, z0, r, s = sp.symbols('c K z z0 r s', real=True)
out = {}
# (1), (2): generic jets at the source
p1, p2, p3, q1, q2 = sp.symbols('p1 p2 p3 q1 q2')
phi = sp.Rational(-1, 2) * c * z0 + sp.Rational(1, 2) * (z - z0) + p2 * (z - z0)**2 / 2 + p3 * (z - z0)**3 / 6
q = K + q1 * (z - z0) + q2 * (z - z0)**2 / 2
E = (c * z + 2 * phi) * sp.diff(q, z) + (1 - 2 * sp.diff(phi, z)) * q
assert sp.simplify(E.subs(z, z0)) == 0
sol = sp.solve(sp.diff(E, z).subs(z, z0), q1)[0]
out['qz_at_source'] = str(sp.simplify(sol))
assert sp.simplify(sol - 2 * K * p2 / (1 + c)) == 0
eta_src = sp.simplify(2 * K * sol / (1 + c))
out['eta_at_source'] = str(eta_src)
assert sp.simplify(eta_src - 4 * K**2 * p2 / (1 + c)**2) == 0
# (3) axis Laplacian in s = r^2
f = sp.Function('f')
phi_rs = f(r**2, z)
lap5_r = sp.diff(phi_rs, r, 2) + 3 / r * sp.diff(phi_rs, r) + sp.diff(phi_rs, z, 2)
a0, a1, a2, b1 = sp.symbols('a0 a1 a2 b1')
test = a0 + a1 * r**2 + a2 * r**4 + b1 * z * r**2 + z**3
lap = sp.simplify(sp.diff(test, r, 2) + 3 / r * sp.diff(test, r) + sp.diff(test, z, 2))
ax = sp.simplify(-(4 * sp.diff(test, r, 2) + sp.diff(test, z, 2)).subs(r, 0) + lap.subs(r, 0))
out['axis_laplacian_identity_residual'] = str(ax)
assert ax == 0
# (4) kernel tests
R, mu = sp.symbols('R mu', positive=True)
res = []
for name, ph in [('z exp(-R^2)', z * sp.exp(-r**2 - z**2)),
                 ('z (1+z^2) exp(-R^2)', z * (1 + z**2) * sp.exp(-r**2 - z**2)),
                 ('z exp(-r^2-2z^2)', z * sp.exp(-r**2 - 2 * z**2))]:
    eta = -(sp.diff(ph, r, 2) + 3 / r * sp.diff(ph, r) + sp.diff(ph, z, 2))
    eta = sp.simplify(eta)
    etaP = sp.simplify(eta.subs({r: R * sp.sqrt(1 - mu**2), z: R * mu}))
    fnum = sp.lambdify((R, mu), sp.Rational(3, 4) * mu * (1 - mu**2) * etaP, 'mpmath')
    val = quad(lambda RR: quad(lambda m: fnum(RR, m), [-1, 0, 1]), [0, 1, 3, mp.inf])
    target = sp.diff(ph, z).subs({r: 0, z: 0})
    res.append({'phi': name, 'kernel': float(val), 'phi_z_at_0': float(target)})
    assert abs(val - mpf(float(target))) < 1e-20
out['kernel_tests'] = res
print(json.dumps(out, indent=1))
json.dump(out, open('checks/t1diag_check_output.json', 'w'), indent=1)
