# Cartesian divergence of U_x = -x phi_z - y q, U_y = -y phi_z + x q, U_z = 2 phi + 2 s phi_s (s = x^2 + y^2), polynomial test.
import sympy as sp
x, y, z, ss = sp.symbols('x y z ss', real=True)
Ps = ss**2*z**3 - 3*ss*z + z**2 + ss**3
Qs = 1 + ss*z
sub = {ss: x**2 + y**2}
P, Q, Pss = Ps.subs(sub), Qs.subs(sub), sp.diff(Ps, ss).subs(sub)
Ux = -x*sp.diff(P, z) - y*Q
Uy = -y*sp.diff(P, z) + x*Q
Uz = 2*P + 2*(x**2 + y**2)*Pss
print('cart_div', sp.expand(sp.diff(Ux, x) + sp.diff(Uy, y) + sp.diff(Uz, z)))
