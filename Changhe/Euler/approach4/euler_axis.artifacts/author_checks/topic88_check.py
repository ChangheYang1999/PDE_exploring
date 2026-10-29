# Lead cross-check of the verifier's topic 88 plateau algebra (smooth stagnation segment at c_l = 1/2).
import sympy as sp
r, z, x, y = sp.symbols('r z x y', real=True)
s = r**2
cl = sp.Rational(1, 2)
phi = z*(sp.Rational(5, 4) - sp.Rational(3, 4)*s)
q = sp.Integer(1)
Ur = -r*sp.diff(phi, z)
Uth = r*q
Uz = 2*phi + r*sp.diff(phi, r)
div = sp.simplify(sp.diff(Ur, r) + Ur/r + sp.diff(Uz, z))
Wr = sp.factor(cl*r + Ur)
Wz = sp.factor(cl*z + Uz)
eta = sp.simplify(-(sp.diff(phi, r, 2) + 3/r*sp.diff(phi, r) + sp.diff(phi, z, 2)))
# eta from the azimuthal vorticity: Omega_theta = d_z U^r - d_r U^z, eta = Omega_theta / r
eta_curl = sp.simplify((sp.diff(Ur, z) - sp.diff(Uz, r))/r)
Reta = sp.simplify((1 + cl)*eta + Wr*sp.diff(eta, r) + Wz*sp.diff(eta, z) - sp.diff(q**2, z))
Rq = sp.simplify(q + Wr*sp.diff(q, r) + Wz*sp.diff(q, z) + 2*(Ur/r)*q)
out = {
    'div': div, 'Wr': Wr, 'Wz': Wz, 'eta': eta, 'eta_curl_equal': sp.simplify(eta - eta_curl) == 0,
    'Reta_on_r1': sp.simplify(Reta.subs(r, 1)), 'Rq': sp.factor(Rq), 'Uth_at_r1': Uth.subs(r, 1),
}
# Cartesian divergence: see checks/topic88_cart.py (polynomial test in s = x^2 + y^2).
for k, v in out.items():
    print(k, v)
