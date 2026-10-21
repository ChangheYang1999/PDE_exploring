# Own symbolic checks of the algebra in fred27 (answer.md 10:46): (1.9)-(1.11), (3.3), (3.5), (3.13), (3.15),
# the antiderivative in the proof of (3.22), (3.23) boundary exponents, (3.26) and p_5.
import sympy as sp
x, y, eps, A = sp.symbols('x y epsilon A', real=True)
a = sp.Function('a')(x, y); b = sp.Function('b')(x, y); f = sp.Function('f')(x, y); z = sp.Function('z')(x, y)
B = sp.Function('B')(x, y)
lap = lambda u: sp.diff(u, x, 2) + sp.diff(u, y, 2)
D = lambda u: a*sp.diff(u, x) + b*sp.diff(u, y)
# (1.10): [Lap, W.grad] z = 2 d_i((d_i W_j) d_j z) - (Lap W_j) d_j z
W = [a, b]; X = [x, y]
lhs = lap(D(z)) - D(lap(z))
rhs = sum(2*sp.diff(sp.diff(W[j], X[i])*sp.diff(z, X[j]), X[i]) for i in range(2) for j in range(2)) \
      - sum(lap(W[j])*sp.diff(z, X[j]) for j in range(2))
print('(1.10)', sp.simplify(sp.expand(lhs - rhs)) == 0)
# (1.11): [Lap, B] z = d_i((d_i B) z) + (d_i B) d_i z
lhs = lap(B*z) - B*lap(z)
rhs = sum(sp.diff(sp.diff(B, X[i])*z, X[i]) + sp.diff(B, X[i])*sp.diff(z, X[i]) for i in range(2))
print('(1.11)', sp.simplify(sp.expand(lhs - rhs)) == 0)
# (1.9) with symbols: P J = J P - eps^2 J [Lap,P] J  <=>  (1 - eps^2 Lap) P J u = P u - eps^2 [Lap,P] J u (u = (1-eps^2 Lap) J u)
# operator identity: (1 - e Lap) P v = P (1 - e Lap) v - e [Lap, P] v for any v
v = z; e = eps**2
P = lambda u: D(u) + B*u
lhs = (P(v) - e*lap(P(v))) - (P(v - e*lap(v)) - e*(lap(P(v)) - P(lap(v))))
print('(1.9)', sp.simplify(sp.expand(lhs)) == 0)
# (3.3)
fx, fy = sp.diff(f, x), sp.diff(f, y)
K = sp.diff(f, y, 2) - fy/a*sp.diff(a, y)
by = sp.diff(b, y); ay = sp.diff(a, y); ax = sp.diff(a, x); ayy = sp.diff(a, y, 2)
F = (ay**2/a - ayy)*(fx + b*fy/a) - 2*ay*sp.diff(f, x, y) + (ax - by)*(fy/a)*ay
E = a*fx + b*fy - f
lhs = D(K) + (2*by - 1)*K - F
rhs = sp.diff(E, y, 2) - ay/a*sp.diff(E, y) - fy*sp.diff(ax + by, y)
print('(3.3)', sp.simplify(sp.expand(lhs - rhs)) == 0)
# (3.5): series in y with generic coefficients (no equation used); parities: a even, b odd, f odd in y
w, a2, a4, h, b3, g, G3 = [sp.Function(n)(x) for n in ('w', 'a2', 'a4', 'h', 'b3', 'g', 'G3')]
aS = w + a2*y**2 + a4*y**4; bS = h*y + b3*y**3; fS = g*y + G3*y**3
FS = (sp.diff(aS, y)**2/aS - sp.diff(aS, y, 2))*(sp.diff(fS, x) + bS*sp.diff(fS, y)/aS) - 2*sp.diff(aS, y)*sp.diff(fS, x, y) \
     + (sp.diff(aS, x) - sp.diff(bS, y))*(sp.diff(fS, y)/aS)*sp.diff(aS, y)
Llim = sp.limit(sp.simplify(FS/y), y, 0)
L = -6*a2*sp.diff(g, x) + 2*a2*g/w*(sp.diff(w, x) - 2*h)
print('(3.5)', sp.simplify(Llim - L) == 0)
# (3.13): M = 6 G3 - 2 g a2/w solves w M' + (3h - 1) M = L  <=>  w G3' + (3h - 1) G3 = -a2 g' + g a2'/3, using w g' = (w' - A) g, h = A + 1 - w'
M = 6*G3 - 2*g*a2/w
expr = w*sp.diff(M, x) + (3*h - 1)*M - L - 6*(w*sp.diff(G3, x) + (3*h - 1)*G3 - (-a2*sp.diff(g, x) + g*sp.diff(a2, x)/3))
sub = {h: A + 1 - sp.diff(w, x)}
expr = sp.expand(expr.subs(sub).doit())
expr = expr.subs(sp.Derivative(g, x), (sp.diff(w, x) - A)*g/w)
print('(3.13)', sp.simplify(expr) == 0)
# (3.15): m = -w/g, m' = -A/g, F3 = g^4 Q'/3, Z' = -(A^-beta/3) m^(beta-1) Q' with H = A^beta g^3 m^-beta, Z = G3/H
beta = 2/A
m = -w/g; Q = a2/g**3; H = A**beta*g**3*m**(-beta)
gp = (sp.diff(w, x) - A)*g/w
def red(e):
    e = e.doit().subs(sp.Derivative(g, x), gp)
    return sp.simplify(e)
print("m' = -A/g", red(sp.diff(m, x) + A/g) == 0)
F3 = -a2*sp.diff(g, x) + g*sp.diff(a2, x)/3
print("F3 = g^4 Q'/3", red(F3 - g**4*sp.diff(Q, x)/3) == 0)
# H homogeneous: w H' + (3h - 1) H = 0
print('H homogeneous', red((w*sp.diff(H, x) + (3*(A + 1 - sp.diff(w, x)) - 1)*H)/H) == 0)
# Z' = F3/(w H) (from w G3' + (3h-1) G3 = F3 and H homogeneous) equals -(A^-beta/3) m^(beta-1) Q'
print("Z' formula", red(F3/(w*H) + A**(-beta)/3*m**(beta - 1)*sp.diff(Q, x)) == 0)
# (3.22) antiderivative
mm, t, bb = sp.symbols('m t b', positive=True)
zf = sp.Function('zf')
Phi = -3*A**bb*(mm**(1 - bb)*zf(mm) - (1 - bb)*sp.Integral(t**(-bb)*zf(t), (t, 0, mm)))
print('(3.22) derivative', sp.simplify(sp.diff(Phi, mm) - (-3*A**bb*mm**(1 - bb)*sp.diff(zf(mm), mm))) == 0)
# (3.23) integration by parts constant: (A^-beta/3) * [-(beta-1) int (Q-Q*) m^(beta-2) m' dx], m' = -A/g
print('(3.23) constant: (A^-b/3)(b-1)A = (b-1)A^(1-b)/3 ->', sp.simplify(A**(-bb)/3*(bb - 1)*A - (bb - 1)*A**(1 - bb)/3) == 0)
# boundary exponents at 0: Q m^(b-1) ~ x^(-5+1-b+2j), Q* m^(b-1) ~ x^(1-b+2j); zero for 0<b<2 only if b = 2j-4 or b = 2j+1
for jj in range(0, 6):
    s1 = sp.solve(sp.Eq(-4 - bb + 2*jj, 0), bb); s2 = sp.solve(sp.Eq(1 - bb + 2*jj, 0), bb)
    print('  j', jj, 'roots', s1, s2)
# (3.26) from the hierarchy: a f_x + b f_y = f, div: a_x + b_y = A + 1, coefficient of y^5
G5, b5 = sp.Function('G5')(x), sp.Function('b5')(x)
aS = w + a2*y**2 + a4*y**4; bS = h*y + b3*y**3 + b5*y**5; fS = g*y + G3*y**3 + G5*y**5
eq = sp.expand(aS*sp.diff(fS, x) + bS*sp.diff(fS, y) - fS)
c5 = eq.coeff(y, 5)
F5 = -a2*sp.diff(G3, x) - 3*b3*G3 - a4*sp.diff(g, x) - b5*g
print('(3.26)', sp.simplify(c5 - (w*sp.diff(G5, x) + (5*h - 1)*G5 - F5)) == 0)
c3 = eq.coeff(y, 3)
print('j=3 eq', sp.simplify(c3 - (w*sp.diff(G3, x) + (3*h - 1)*G3 + a2*sp.diff(g, x) + b3*g)) == 0)
dv = sp.expand(sp.diff(aS, x) + sp.diff(bS, y))
print('div y^2 coeff a2 + 3 b3:', dv.coeff(y, 2))
# p_5 = 2*5 + 4/A even integer for A > 1 only at A = 2
print('p5 even-integer A in (1, inf):', [sp.Rational(4, k - 10) for k in (12, 14) if sp.Rational(4, k - 10) > 1])
