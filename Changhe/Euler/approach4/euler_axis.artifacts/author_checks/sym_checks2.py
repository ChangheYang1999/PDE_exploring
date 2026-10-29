"""Lead symbolic checks, part 2: 5D integral identities, energy-flux divergence form, Green's formula per mode."""
import sympy as sp, json
out = {}
r, z, c = sp.symbols('r z c', positive=True)
phi = sp.Function('phi')(r, z); q = sp.Function('q')(r, z); P = sp.Function('P')(r, z)
Ur = -r*sp.diff(phi, z); Uz = 2*phi + r*sp.diff(phi, r); Ut = r*q
Wr = c*r + Ur; Wz = c*z + Uz
div5 = lambda Fr, Fz: sp.diff(Fr, r) + 3*Fr/r + sp.diff(Fz, z)
out['div5_Wm'] = sp.simplify(div5(Wr, Wz) - (5*c + 2*Ur/r)) == 0
lap5 = sp.diff(phi, r, 2) + 3/r*sp.diff(phi, r) + sp.diff(phi, z, 2)
# d_z phi * Delta_5 phi = div_5(d_z phi grad phi) - d_z(|grad phi|^2/2)
gr = sp.diff(phi, r); gz = sp.diff(phi, z)
lhs = gz*lap5
rhs = div5(gz*gr, gz*gz) - sp.diff((gr**2 + gz**2)/2, z)
out['dzphi_lap5phi_is_divergence'] = sp.simplify(sp.expand(lhs - rhs)) == 0
# (U^r/r) eta = d_z phi * Delta_5 phi
eta = -lap5
out['Ur_over_r_eta'] = sp.simplify(sp.expand((Ur/r)*eta - gz*lap5)) == 0
# 5D integrated eta equation: (1+c) eta + W.grad eta - d_z q^2 = div5(W eta) + (1+c - 5c - 2Ur/r) eta - d_z(q^2)
Reta = (1+c)*eta + Wr*sp.diff(eta, r) + Wz*sp.diff(eta, z) - sp.diff(q**2, z)
form = div5(Wr*eta, Wz*eta) + (1 - 4*c)*eta - 2*(Ur/r)*eta - sp.diff(q**2, z)
out['eta_eq_conservative_5D'] = sp.simplify(sp.expand(Reta - form)) == 0
# energy flux: U.M = (2-5c)/2 |U|^2 + div3(W |U|^2/2 + U P)
div3 = lambda Fr, Fz: sp.diff(Fr, r) + Fr/r + sp.diff(Fz, z)
D = lambda f: Wr*sp.diff(f, r) + Wz*sp.diff(f, z)
Mr = (1-c)*Ur + D(Ur) - Ut**2/r + sp.diff(P, r)
Mt = (1-c)*Ut + D(Ut) + Ur*Ut/r
Mz = (1-c)*Uz + D(Uz) + sp.diff(P, z)
U2 = Ur**2 + Ut**2 + Uz**2
lhs = Ur*Mr + Ut*Mt + Uz*Mz
rhs = (2 - 5*c)/2*U2 + div3(Wr*U2/2 + Ur*P, Wz*U2/2 + Uz*P)
out['energy_flux_divergence_form'] = sp.simplify(sp.expand(lhs - rhs)) == 0
# circulation conservative form: div3(W Gamma) = (5c-1) Gamma + [(1-2c)Gamma + W.grad Gamma]
G = r**2*q
out['Gamma_conservative'] = sp.simplify(sp.expand(div3(Wr*G, Wz*G) - (5*c - 1)*G - ((1 - 2*c)*G + D(G)))) == 0
# Green's function per Legendre mode
R, s, l = sp.symbols('R s l', positive=True)
f = sp.Function('f')
for lv in range(0, 4):
    Pl = (R**(-lv-1)*sp.Integral(s**(lv+2)*f(s), (s, 0, R)) + R**lv*sp.Integral(s**(1-lv)*f(s), (s, R, sp.oo)))/(2*lv+1)
    ode = -sp.diff(R**2*sp.diff(Pl, R), R)/R**2 + lv*(lv+1)*Pl/R**2 - f(R)
    out[f'green_mode_{lv}'] = sp.simplify(ode.doit()) == 0
print(out)
json.dump({k: bool(v) for k, v in out.items()}, open('author_checks/sym_checks2_result.json', 'w'), indent=1)
