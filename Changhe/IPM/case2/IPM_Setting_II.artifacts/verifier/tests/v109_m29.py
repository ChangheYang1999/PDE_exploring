"""V109 (notes of the lead analyst 10:35Z item (h)): symbolic checks of specification v4.13 M29 (a), (b), (d) and the proposed report Section 4.15(f).
(a) curl V in the coordinates (t, y), x = chi(t, y), t = xi, with V_1 = (t/q) chi_t + chi_y v, V_2 = v, against referee audit 16's formula;
    transport V.grad xi = xi/q and the divergence identity chi_t v = b(t) + beta S - (t/q) S_t with S = int_0^y chi_t.
(b) the two leading orders of the formal C^{2,q-1} root xi = a x + d x^{1+q} (x > 0) in the local equations.
(d) the (q, p) = (1, 1) layer and its angular pair; the invariant y/x + H log x."""
import sympy as sp
t, y, q, H, l, x, th, z = sp.symbols('t y q H l x theta z', real=True)
chi = sp.Function('chi')(t, y); v = sp.Function('v')(t, y)
V1 = (t/q)*sp.diff(chi, t) + sp.diff(chi, y)*v; V2 = v
dx = lambda F: sp.diff(F, t)/sp.diff(chi, t)                       # d/dx at fixed y
dy = lambda F: sp.diff(F, y) - sp.diff(F, t)*sp.diff(chi, y)/sp.diff(chi, t)   # d/dy at fixed x
curl = sp.simplify(dx(V2) - dy(V1))
ct, cy, cty, ctt, cyy = [sp.diff(chi, *a) for a in ((t,), (y,), (t, y), (t, t), (y, y))]
aud = (1 + cy**2)/ct*sp.diff(v, t) - cy*sp.diff(v, y) + (cy*cty/ct - cyy)*v + cy/q + (t/q)*(cy*ctt/ct - cty)
print('(a) curl - referee audit 16 formula =', sp.simplify(curl - aud))
# transport: V.grad t with grad t from the inverse: t_x = 1/chi_t, t_y = -chi_y/chi_t
print('(a) V.grad xi - xi/q =', sp.simplify(V1/ct + V2*(-cy/ct) - t/q))
# divergence: div V = d_x V1 + d_y V2 must equal 2l; with chi_t v = b + beta S - (t/q) S_t, S_y = chi_t
S = sp.Function('S')(t, y); b = sp.Function('b')(t); beta = 2*l - 1/q
vS = (b + beta*S - (t/q)*sp.diff(S, t))/ct
div = dx(V1.subs(v, vS)) + dy(vS)
div = div.subs(sp.Derivative(S, y), ct).subs(sp.Derivative(S, t, y), ctt).subs(sp.Derivative(S, y, t), ctt)
print('(a) div V - 2l =', sp.simplify(sp.expand(div.doit()).subs(sp.Derivative(S, y), ct) - 2*l))
# (b) x > 0: xi = a x + d x^(1+q); V1 = A x + E x^(1+q); V2 = B + F x^q + G x^2, at q = 3/2 (x = u^2) and q = 5/4 (x = u^4)
u = sp.symbols('u', positive=True)
for qq, k in ((sp.Rational(3, 2), 2), (sp.Rational(5, 4), 4)):
    a, d, A, B, E, F, G = [sp.Function(n)(y) for n in 'adABEFG']
    X = u**k; xq = u**int(qq*k)
    du = lambda f: sp.diff(f, u)/sp.diff(X, u)
    xi = a*X + d*X*xq; V1b = A*X + E*X*xq; V2b = B + F*xq + G*X**2
    rho = H*a**qq*xq*(1 + qq*(d/a)*xq)
    Esol = H*sp.diff(a**qq, y)/(qq + 1); Fsol = -H*a**qq
    sub = lambda f: sp.expand(f.subs(E, Esol).subs(F, Fsol).doit())
    curlres = sub(du(V2b) - sp.diff(V1b, y) + du(rho))
    divres = sub(du(V1b) + sp.diff(V2b, y) - 2*l)
    tr = sub(V1b*du(xi) + V2b*sp.diff(xi, y) - xi/qq)
    lead = int((qq - 1)*k)
    print('(b) q =', qq, ': curl coefficient of x^(q-1):', sp.simplify(curlres.coeff(u, lead)),
          '; div x^0:', sp.simplify(divres.coeff(u, 0)), ' x^q:', sp.simplify(divres.coeff(u, int(qq*k))))
    print('    transport x^1:', sp.simplify(tr.coeff(u, k) - (A*a + B*sp.diff(a, y) - a/qq)),
          ' (difference from M29); x^(1+q) minus M29 law:',
          sp.simplify(tr.coeff(u, k + int(qq*k)) - (B*sp.diff(d, y) + ((qq + 1)*A - 1/qq)*d - H*a**qq*sp.diff(a, y)/(qq + 1))),
          '; lowest powers of u present in transport:', sorted(set(m.as_coeff_exponent(u)[1] for m in sp.Add.make_args(tr)))[:4])
# (d) layer at (1, 1): rho = H|x|, V = (x, y - H|x|); on x > 0
psi = -H*x**2/2
Vd = (x, y - H*x)
print('(d) Delta psi + rho_x =', sp.simplify(sp.diff(psi, x, 2) + H), '; W = (-psi_y, psi_x) =', (0, sp.diff(psi, x)))
print('(d) V.grad rho - rho =', sp.simplify(Vd[0]*H - H*x), '; div V =', sp.diff(Vd[0], x) + sp.diff(Vd[1], y))
inv = y/x + H*sp.log(x)
print('(d) V.grad (y/x + H log x) =', sp.simplify(Vd[0]*sp.diff(inv, x) + Vd[1]*sp.diff(inv, y)))
Aang = H*sp.cos(th); Psi = -(H/2)*sp.cos(th)**2                    # on |th| < pi/2
print('(d) Psi\'\' + 4 Psi + cos A - sin A\' =', sp.simplify(sp.diff(Psi, th, 2) + 4*Psi + sp.cos(th)*Aang - sp.sin(th)*sp.diff(Aang, th)),
      '; 2 Psi A\' - Psi\' A =', sp.simplify(2*Psi*sp.diff(Aang, th) - sp.diff(Psi, th)*Aang))
print('(d) psi/r^2 = -(H/2) cos|cos| on x > 0:', sp.simplify((psi/(x**2 + y**2)).subs({x: sp.cos(th), y: sp.sin(th)}) - Psi))
# 4.15(f) present text at g < 1 and the layer: V = (x/g, (2l - 1/g) y - H|x|^g) solves the local equations for any l
g = sp.symbols('g', positive=True)
Vg = (x/g, (2*l - 1/g)*y - H*x**g)
print('(a) local layer any l: div - 2l =', sp.simplify(sp.diff(Vg[0], x) + sp.diff(Vg[1], y) - 2*l),
      '; curl + rho_x =', sp.simplify(sp.diff(Vg[1], x) - sp.diff(Vg[0], y) + sp.diff(H*x**g, x)),
      '; V.grad xi - xi/g =', sp.simplify(Vg[0] - x/g))
