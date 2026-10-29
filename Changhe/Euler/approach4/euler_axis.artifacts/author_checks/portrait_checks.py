# Lead re-check (independent code) of the referee's axis-chain counterexamples and the ring-source seed polynomial.
import sympy as sp
s, z, c, K = sp.symbols('s z c K', real=True)
r = sp.symbols('r', positive=True)
out = []
def lap5(f):  # Delta_5 in (s, z)
    return 4*s*sp.diff(f, s, 2) + 8*sp.diff(f, s) + sp.diff(f, z, 2)
def residuals(phi, q, cc):
    eta = -lap5(phi)
    Wr_over = 2*s*(cc - sp.diff(phi, z))          # W_m . grad = Wr_over d_s + Wz d_z
    Wz = cc*z + 2*phi + 2*s*sp.diff(phi, s)
    Rq = q + Wr_over*sp.diff(q, s) + Wz*sp.diff(q, z) - 2*sp.diff(phi, z)*q
    Reta = (1 + cc)*eta + Wr_over*sp.diff(eta, s) + Wz*sp.diff(eta, z) - sp.diff(q**2, z)
    return sp.expand(eta), sp.expand(Rq), sp.expand(Reta)
# (13) ring-source seed
nu = (1 + c)/2; E = 2*K**2/(3*c)
q = K*s*z
phi = z*(c + nu*(1 - s)) + sp.Rational(4, 3)*nu*z**3 - E/6*s**2*z**3 + E/5*s*z**5 - sp.Rational(4, 105)*E*z**7
eta, Rq, Reta = residuals(phi, q, c)
out.append(('eta - E s^2 z', sp.simplify(eta - E*s**2*z)))
# lowest z-order in residuals
for name, R in (('Rq', Rq), ('Reta', Reta)):
    P = sp.Poly(R, z)
    low = min(m[0] for m in P.monoms())
    out.append((name + ' lowest z power', low))
# eigenvalues at origin and at ring (r=1, z=0)
Wr = r*(c - sp.diff(phi, z)).subs(s, r**2)
Wz = (c*z + 2*phi + 2*s*sp.diff(phi, s)).subs(s, r**2)
J = sp.Matrix([[sp.diff(Wr, r), sp.diff(Wr, z)], [sp.diff(Wz, r), sp.diff(Wz, z)]])
J0 = sp.simplify(J.subs({r: 0, z: 0})); J1 = sp.simplify(J.subs({r: 1, z: 0}))
out.append(('J at origin', J0)); out.append(('J at ring', J1))
out.append(('v at origin', sp.simplify(-sp.diff(phi, z).subs({s: 0, z: 0}))))
# (5) degenerate counterexample at c = 3/5 on z > 0 (q = Q there), and the first-integral form for z < 0
cc = sp.Rational(3, 5); d = 1 + cc; t = z**2
wd = cc*z**3*(t - 1)/(t**2 - t/2 + sp.Rational(1, 4))
zp = sp.symbols('zp', positive=True)
Qd = 3*sp.exp(sp.Rational(1, 3))*zp**sp.Rational(7, 3)*sp.exp(-1/(3*zp**2))/(4*zp**4 - 2*zp**2 + 1)
wdp = wd.subs(z, zp); a = d - sp.diff(wdp, zp)
out.append(('(5) swirl eq z>0', sp.simplify(wdp*sp.diff(Qd, zp) + a*Qd)))
etad = 2*Qd*(Qd - 1)/wdp
out.append(('(5) eta eq z>0', sp.simplify(wdp*sp.diff(etad, zp) + d*etad - 2*Qd*sp.diff(Qd, zp))))
out.append(('(5) Q(1), wd(1), wd\'(1), wd\'(0)', (sp.simplify(Qd.subs(zp, 1)), wd.subs(z, 1), sp.diff(wd, z).subs(z, 1), sp.diff(wd, z).subs(z, 0))))
out.append(('(5) wd - c z at infinity', sp.limit((wd - cc*z)*z, z, sp.oo)))
# (6) simple-zero example
we = cc*z*(t - 1)*(t + 2)/(t**2 + t/2 + sp.Rational(3, 4))
Qe = 9*z**2*((z**2 + 2)/3)**sp.Rational(1, 6)/(4*z**4 + 2*z**2 + 3)
a = d - sp.diff(we, z)
out.append(('(6) swirl eq', sp.simplify(we*sp.diff(Qe, z) + a*Qe)))
etae = 2*Qe*(Qe - 1)/we
out.append(('(6) eta eq', sp.simplify(we*sp.diff(etae, z) + d*etae - 2*Qe*sp.diff(Qe, z))))
out.append(('(6) Qe(1), we\'(0), we\'(1)', (sp.simplify(Qe.subs(z, 1)), sp.diff(we, z).subs(z, 0), sp.diff(we, z).subs(z, 1))))
out.append(('(6) k at 0 = 1 + d/mu', 1 + d/(-sp.diff(we, z).subs(z, 0))))
for k_, v_ in out:
    print(k_, ':', v_)
