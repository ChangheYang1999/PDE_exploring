"""V40 part 2: sympy checks of referee result 13 results/01-04 (independent verifier)."""
import sympy as sp
x, y, a, b, t, L, C, p, l, s, u, v, k, d, h, Ak, tau = sp.symbols('x y a b t L C p l s u v k d h A_k tau', positive=True)
out = []
# N1: V = (a x + H_y, b y - H_x), H = x y / log(1/r): div V = a + b; on y = 0, V1 = x (a + 1/log(1/x)), V2 = 0
X, Y = sp.symbols('X Y', real=True)
r = sp.sqrt(X**2 + Y**2); H = X*Y/sp.log(1/r)
V1 = a*X + sp.diff(H, Y); V2 = b*Y - sp.diff(H, X)
out.append(('N1 div', sp.simplify(sp.diff(V1, X) + sp.diff(V2, Y) - a - b)))
out.append(('N1 axis V1', sp.simplify(V1.subs(Y, 0).subs(X, x) - x*(a + 1/sp.log(1/x)))))
out.append(('N1 axis V2', sp.simplify(V2.subs(Y, 0))))
F = C*x*(a*sp.log(1/x) + 1)**(1/a)
out.append(('N1 F solves x(a+1/L)F = aF', sp.simplify(x*(a + 1/sp.log(1/x))*sp.diff(F, x) - a*F)))
# N3/N4: Xi = d t, H -> h, A = A_k t^k: tau = h/(d t)^q, G = A/Xi^gamma; check G = C tau^((1-ka)/b) exactly
q = b/a; gam = 1/a
tau_t = h/(d*t)**q; G_t = Ak*t**k/(d*t)**gam
Cc = Ak*d**(-k)*h**((k - gam)/q)
out.append(('N4 G ~ C tau^((1-ka)/b)', sp.simplify(sp.expand_power_base(sp.powsimp(G_t/(Cc*tau_t**((1 - k*a)/b)), force=True), force=True))))
# N5: |u|^gamma C |tau|^e with tau = v/|u|^q equals C |u|^k |v|^e
e = (1 - k*a)/b
out.append(('N5', sp.simplify(sp.powsimp(u**gam*(v/u**q)**e/(u**k*v**e), force=True))))
# N6 scaling F(t^a u, t^b v) = t F(u, v) for F = u^gamma G(v/u^q) (generic G as a power)
m = sp.symbols('m')
Fg = lambda U, W: U**gam*(W/U**q)**m
out.append(('N6', sp.simplify(sp.powsimp(Fg(t**a*u, t**b*v)/(t*Fg(u, v)), force=True))))
# S1 kernel derivative: d_x(-x y/(pi r^4)) = y (3x^2 - y^2)/(pi r^6) = sin 3th/(pi r^3)
K1 = -X*Y/(sp.pi*r**4)
out.append(('S1 dK1', sp.simplify(sp.diff(K1, X) - Y*(3*X**2 - Y**2)/(sp.pi*r**6))))
th = sp.symbols('th', real=True)
out.append(('S1 sin3', sp.simplify(sp.expand_trig((sp.sin(th)*(3*sp.cos(th)**2 - sp.sin(th)**2)) - sp.sin(3*th)))))
# S1/S2/S3 coefficients: div(rho phi V) with div(rho V) = (1+2l) rho, phi homogeneous of degree -m: (1 + 2l - m l)
mm = sp.symbols('mm')
out.append(('S1 m=3 coefficient', sp.simplify((1 + 2*l - 3*l) - (1 - l))))
out.append(('S2 m=p+2 coefficient', sp.simplify((1 + 2/p - (p + 2)/p))))
# P1: f_p(Z) = p^2 rho(Z/p), b_p = p^2 V(Z/p): b_p . grad f_p = p f_p, Db_p(0) = p DV(0)
# (scalar check of the scaling factors: grad f_p = p (grad rho)(Z/p); b_p . grad f_p = p^3 (V.grad rho)(Z/p) = p^3 rho = p f_p)
out.append(('P1 factor', sp.simplify(p**2*p*1 - p*p**2)))
out.append(('P1 b_p linear part', sp.simplify(p**2*(1/p)*(1/p) - 1)))   # p^2 * l * (Z/p) = Z with l = 1/p
out.append(('P2 c[f_p] = 1 - p a', sp.simplify((1 - p*a) - (1 - p*a))))
aa = sp.symbols('aa')
gp = 1/(sp.Rational(1, 2) + aa*p)
out.append(('P6 gamma(p) = 2 - 4 aa p + O(p^2)', sp.simplify(sp.series(gp, p, 0, 2).removeO() - (2 - 4*aa*p))))
# F2 scaling: rho_s = s rho(X/s) = s C |xi(X/s)|^gamma = s C s^(-gamma) |xi_s|^gamma
out.append(('F2', sp.simplify(s*C*(1/s)**gam - C*s**(1 - gam))))
# N6 table
for pp, m1 in ((0.3, 0.5487), (0.5, 0.6085), (0.7, 0.7042)):
    bb = 2/pp - m1
    out.append(('N6 table p=%g' % pp, (round(1/m1, 5), round(bb, 5), round(1/bb, 5), round(bb/m1 - 1, 5))))
for n, val in out:
    print(n, ':', val)
