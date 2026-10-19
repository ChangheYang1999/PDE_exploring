"""V125: symbolic checks of the identities used in referee result 25 (Theorems 3.2, 3.3, 3.13). Own derivations, sympy."""
import sympy as sp
ok = []
def chk(name, expr):
    e = sp.simplify(expr); ok.append((name, e == 0)); print(name, 'OK' if e == 0 else 'FAIL: %s' % e)
x, y, t, a, l, s, c, R = sp.symbols('x y t a l s c R', real=True)
p = 1/l
# (4.8): second x-derivative of V1 rho_x + V2 rho_y - rho
V1, V2, rho = [sp.Function(n)(x, y) for n in ('V1', 'V2', 'rho')]
E = V1*rho.diff(x) + V2*rho.diff(y) - rho
lhs = E.diff(x, 2)
rhs = (V1*rho.diff(x, 3) + 2*V1.diff(x)*rho.diff(x, 2) + V1.diff(x, 2)*rho.diff(x) + V2*rho.diff(x, 2, y)
       + 2*V2.diff(x)*rho.diff(x, y) + V2.diff(x, 2)*rho.diff(y) - rho.diff(x, 2))
chk('(4.8)', lhs - rhs)
# reduction on the axis with parity: rho = x^2 h(y) + x^4 k(y), V1 = x f1(y) + x^3 f3(y), V2 = b(y) + x^2 g2(y), div V = 2l
h, k, f3, b, g2 = [sp.Function(n)(y) for n in ('h', 'k', 'f3', 'b', 'g2')]
f1 = 2*l - b.diff(y)                       # div V = 2l at x = 0
rr = x**2*h/2*2/2 + x**4*k                  # rho_xx(0,y) = h  <=> rho = x^2 h/2 + ...
rr = x**2*h/2 + x**4*k
VV1 = x*f1 + x**3*f3; VV2 = b + x**2*g2
EE = VV1*rr.diff(x) + VV2*rr.diff(y) - rr
red = sp.expand(EE.diff(x, 2).subs(x, 0))
chk('(4.9) b h\' = (1 - 4l + 2b\') h', red - (b*h.diff(y) - (1 - 4*l + 2*b.diff(y))*h))
# (4.11): with b = l y + w, h'/h = (1 - 4l + 2b')/b; minus k/y with k = p - 2
w = sp.Function('w')(y)
bb = l*y + w
hp_over_h = (1 - 4*l + 2*bb.diff(y))/bb
chk('(4.11)', hp_over_h - (p - 2)/y - (2*y*w.diff(y) - (p - 2)*w)/(y*(l*y + w)))
chk('l k = 1 - 2l', l*(p - 2) - (1 - 2*l))
# (bh)' = (1 - l + 3w') h using (4.9)
hh = sp.Function('h')(y)
bh_prime = bb.diff(y)*hh + (1 - 4*l + 2*bb.diff(y))*hh
chk("(bh)' = (1 - l + 3w')h", bh_prime - (1 - l + 3*w.diff(y))*hh)
# (2.3), (2.5): A(Theta(a)) = L^-p q^2 at a zero of q
L, q, Th = [sp.Function(n)(a) for n in ('L', 'q', 'Th')]
A = sp.Function('A')
G = L**(-p)*q**2
d1 = sp.diff(A(Th), a); d2 = sp.diff(A(Th), a, 2)
a0 = sp.Symbol('a0'); q0p, A1, A2 = sp.symbols('q0p A1 A2')
Q1, Q2 = sp.symbols('Q1 Q2')
def atzero(e):  # evaluate at a zero of q: replace q'', q', then q
    return e.subs(q.diff(a, 2), Q2).subs(q.diff(a), Q1).subs(q, 0)
G1 = atzero(G.diff(a)); chk('(2.2) first derivative vanishes at a zero of q', G1)
G2 = atzero(G.diff(a, 2))
chk('(2.3) second derivative = 2 L^-p q\'^2', G2 - 2*L**(-p)*Q1**2)
B = L**(-p/2)*q
chk('(2.4) B^2 = L^-p q^2', B**2 - G)
chk('(2.5) d_a B at zero = L^-p/2 q\'', atzero(B.diff(a)) - L**(-p/2)*Q1)
# (3.2): u^{1-p}' <= lambda u^{1-p} + (1-p)C, lambda = l - 1: (1-p) l = lambda and (1-p)C/lambda = C/l
C = sp.Symbol('C', positive=True)
chk('(1-p) l = l - 1', (1 - p)*l - (l - 1)); chk('(1-p)C/lambda = C/l', (1 - p)*C/(l - 1) - C/l)
chk('lambda/(1-p) = l', (l - 1)/(1 - p) - l)
# integrand bound e^{-ls} (e^{ls})^p = e^{-(l-1)s}
chk('e^{-ls} e^{pls} = e^{-lambda s}', sp.exp(-l*s)*sp.exp(p*l*s) - sp.exp(-(l - 1)*s))
# (3.14) with X = P(a,s): |S| = e^{ls} L, rho = e^s q^2, xi = e^{s/2} q
Ls, qs = sp.symbols('Ls qs', positive=True)
chk('(3.14) rho', (sp.exp(l*s)*Ls)**p*Ls**(-p)*qs**2 - sp.exp(s)*qs**2)
chk('(3.14) xi', (sp.exp(l*s)*Ls)**(p/2)*Ls**(-p/2)*qs - sp.exp(s/2)*qs)
# (3.16): |Phi_t X|^{p-1} with |Phi_t X| >= (r/2) e^{lt}: exponent (p-1) l t = -lambda t
chk('(p-1) l = -lambda', (p - 1)*l + (l - 1))
# (3.18): beta - l = l - 1/2; beta - 2 alpha = 2l - 3/2
beta = 2*l - sp.Rational(1, 2); alpha = sp.Rational(1, 2)
chk('beta - l', beta - l - (l - sp.Rational(1, 2))); chk('beta - 2alpha', beta - 2*alpha - (2*l - sp.Rational(3, 2)))
# (1.5): det(R J e_a, V) = -R V_r
V1s, V2s = sp.symbols('V1s V2s')
ea = sp.Matrix([sp.cos(a), sp.sin(a)]); Jea = sp.Matrix([-sp.sin(a), sp.cos(a)])
chk('det(RJe_a, V) = -R V_r', sp.Matrix.hstack(R*Jea, sp.Matrix([V1s, V2s])).det() + R*(V1s*sp.cos(a) + V2s*sp.sin(a)))
# (4.1): K(RZ) = R K(Z), K = (-2 Z1 Z2, Z1^2 - Z2^2)/(2 pi |Z|^4)
Z1, Z2 = sp.symbols('Z1 Z2', real=True)
K = lambda u, v: sp.Matrix([-2*u*v, u**2 - v**2])/(2*sp.pi*(u**2 + v**2)**2)
Rm = sp.diag(-1, 1)
chk('K(RZ) = R K(Z)', (K(-Z1, Z2) - Rm*K(Z1, Z2)).norm()**2)
# K = (d_12 G, -d_11 G) = -J grad(d_1 G), G = log|Z|/(2 pi): the distributional kernel is p.v. K - (0, 1/2) delta
# (d_11 G = p.v. + delta/2), which is the -rho e_2/2 term; then W = J grad psi with Lap psi = -rho_x
G0 = sp.log(Z1**2 + Z2**2)/(4*sp.pi)
Kc = sp.Matrix([sp.diff(G0, Z1, Z2), -sp.diff(G0, Z1, Z1)])
chk('K = (d_12 G, -d_11 G), G = log|Z|/(2 pi)', (Kc - K(Z1, Z2)).applyfunc(sp.simplify).norm()**2)
# (4.15): A/cos^2 at a vertical zero -> A''/2: cos^2(pi/2 + t)/t^2 -> 1
chk('cos^2(pi/2+t)/t^2 -> 1', sp.limit(sp.cos(sp.pi/2 + t)**2/t**2, t, 0) - 1)
# (4.17)-(4.18): |y| < r/2 => |x| > sqrt(3) r / 2
chk('x^2 = r^2 - y^2 > 3r^2/4 at |y| = r/2', (R**2 - (R/2)**2) - sp.Rational(3, 4)*R**2)
# (5.5) chart: Dg(0,0) = (0, beta) when V2_x(0) = 0, V2_y(0) = beta, chi_v(0) = 0, chi_u(0) = 1
u_, v_ = sp.symbols('u v'); V2f = sp.Function('V2'); chi = sp.Function('chi')(u_, v_)
g = V2f(chi, v_)
gu = sp.diff(g, u_); gv = sp.diff(g, v_)
print('g_u =', gu, '\ng_v =', gv)
# referee result 23 Section 7 (V124(b)): d_x(|Z| cos 3th) = 2 cos 2th - cos 4th, angular mean of cos 2th times it = 1
th, rr_ = sp.symbols('th rr', positive=True)
f = sp.sqrt(Z1**2 + Z2**2)*sp.cos(3*sp.atan2(Z2, Z1))
fx = sp.diff(sp.expand_trig(sp.sqrt(Z1**2 + Z2**2)*(4*(Z1/sp.sqrt(Z1**2 + Z2**2))**3 - 3*Z1/sp.sqrt(Z1**2 + Z2**2))), Z1)
fx_pol = sp.simplify(fx.subs({Z1: rr_*sp.cos(th), Z2: rr_*sp.sin(th)}))
chk('d_x(|Z| cos 3th) = 2cos2th - cos4th', sp.simplify(sp.expand_trig(fx_pol - (2*sp.cos(2*th) - sp.cos(4*th)))))
chk('mean cos2th (2cos2th - cos4th) = 1', sp.integrate(sp.cos(2*th)*(2*sp.cos(2*th) - sp.cos(4*th)), (th, 0, 2*sp.pi))/(2*sp.pi) - 1)
print('ALL OK' if all(v for _, v in ok) else 'SOME FAILED', len(ok))
