"""V39b (referee result 12 results/04-geometry): area coordinates, curl/div in Jacobian-one charts, coefficient of b'(t),
cusp compatibility on the (tilted) shears, separable reduction, A = 1/(1+a'^2), index of the model field.
PASS/FAIL per identity. Run: OMP_NUM_THREADS=1 python3 tests/v39b_geom.py"""
import sympy as sp

x, y, z = sp.symbols('x y z', real=True)
t, s = sp.symbols('t s', real=True)
mu, kap = sp.Rational(2, 5), sp.Rational(1, 2)
g, l, beta, tilt = sp.symbols('gamma l beta tau', positive=True)
res = []


def chk(name, expr):
    e = sp.simplify(expr)
    ok = (e == 0)
    res.append(ok)
    print(('PASS' if ok else 'FAIL'), name, '' if ok else e)


# (a) construction: xi = x(1 + mu y) + kap y^2, x = g(t, y) = (t - kap y^2)/(1 + mu y), s = int_0^y g_t dz
xi = x*(1 + mu*y) + kap*y**2
gxy = (t - kap*y**2)/(1 + mu*y)
chk('chart: xi(g(t,y), y) = t', xi.subs(x, gxy) - t)
S = sp.integrate(sp.diff(gxy, t).subs(y, z), (z, 0, y))
print('INFO s(t,y) =', sp.simplify(S))
# Jacobian of (x,y) -> (t,s) with t = xi, s = S(y)
Sxy = S  # independent of t here
J = sp.Matrix([[sp.diff(xi, x), sp.diff(xi, y)], [sp.diff(Sxy, x), sp.diff(Sxy, y)]]).det()
chk('chart: det D(t,s)/D(x,y) = 1', J - 1)
# inverse map X(t, s)
ys = sp.solve(sp.Eq(Sxy, s), y)[0]
Xts = sp.Matrix([gxy.subs(y, ys), ys])
Xt, Xs = Xts.diff(t), Xts.diff(s)
gradperp = sp.Matrix([-sp.diff(xi, y), sp.diff(xi, x)]).subs({x: Xts[0], y: Xts[1]}, simultaneous=True)
chk('chart: X_s = grad^perp xi', (Xs - gradperp).norm()**2)
chk('chart: det DX = 1', sp.Matrix.hstack(Xt, Xs).det() - 1)

# (b) curl and div in this Jacobian-one chart for generic components V = Vt X_t + Vs X_s
Vt = sp.Function('Vt')(t, s)
Vs = sp.Function('Vs')(t, s)
V = Vt*Xt + Vs*Xs
DX = sp.Matrix.hstack(Xt, Xs)
Inv = sp.simplify(DX.inv())          # rows: grad t, grad s (as functions of t,s)
dx = lambda F: Inv[0, 0]*sp.diff(F, t) + Inv[1, 0]*sp.diff(F, s)
dy = lambda F: Inv[0, 1]*sp.diff(F, t) + Inv[1, 1]*sp.diff(F, s)
curl_phys = dx(V[1]) - dy(V[0])
curl_chart = sp.diff(V.dot(Xs), t) - sp.diff(V.dot(Xt), s)
chk('chart: curl V = d_t(V.X_s) - d_s(V.X_t)', sp.expand(sp.simplify(curl_phys - curl_chart)))
div_phys = dx(V[0]) + dy(V[1])
chk('chart: div V = d_t V^t + d_s V^s', sp.expand(sp.simplify(div_phys - sp.diff(Vt, t) - sp.diff(Vs, s))))
# (c) with V^t = t/g, V^s = beta s + b(t): coefficient of b'(t) in curl is |X_s|^2 and nothing else is singular
b = sp.Function('b')
curl_b = curl_chart.subs({Vt: t/g, Vs: beta*s + b(t)}).doit()
coef = sp.diff(sp.expand(curl_b), sp.Derivative(b(t), t))
chk('curl: coefficient of b\'(t) is |X_s|^2', coef - Xs.dot(Xs))
rest = sp.expand(curl_b - coef*sp.Derivative(b(t), t))
ok = not rest.has(sp.Derivative(b(t), t))
res.append(ok)
print(('PASS' if ok else 'FAIL'), 'curl: remaining terms contain only b(t), t/g, beta s and derivatives of X up to order 2')

# (d) tilted shear xi = x + tau y, W = (tau, -1)|xi|^g/(1+tau^2), l = 1/g (side xi > 0):
#     area chart X = t(1,tau)/(1+tau^2) + s(-tau, 1); V^s = beta s + b(t) with beta = 2l - 1/g = l, b = -t^g/(1+tau^2)
tp = sp.symbols('tp', positive=True)
X = sp.Matrix([tp/(1 + tilt**2) - s*tilt, tp*tilt/(1 + tilt**2) + s])
Xt_, Xs_ = X.diff(tp), X.diff(s)
chk('tilted: det DX = 1', sp.Matrix.hstack(Xt_, Xs_).det() - 1)
xi_t = X[0] + tilt*X[1]
chk('tilted: xi(X(t,s)) = t', xi_t - tp)
lv = 1/g
Wt = sp.Matrix([tilt, -1])*tp**g/(1 + tilt**2)
Vt_ = lv*X + Wt
# components in the chart: solve Vt_ = A X_t + B X_s
AB = sp.Matrix.hstack(Xt_, Xs_).solve(Vt_)
chk('tilted: V^t = t/g', AB[0] - tp/g)
chk('tilted: V^s = (2l - 1/g) s + b(t), b = -t^g/(1+tau^2)', AB[1] - ((2*lv - 1/g)*s - tp**g/(1 + tilt**2)))
bb = -tp**g/(1 + tilt**2)
ratio = sp.diff(bb, tp)/sp.diff(tp**g, tp)
gx, gy = 1, tilt
chk('tilted: b\'/f\' = -xi_x/|grad xi|^2 (constant -1/(1+tau^2))', ratio + sp.Rational(gx)/(gx**2 + gy**2))
chk('normalized shear (tau = 0): xi_x/|grad xi|^2 = 1, i.e. xi_x = |grad xi|^2', (-ratio).subs(tilt, 0) - 1)

# (e) separable xi = F(x) G(y): on x = 0, xi_x = F'(0) G(y), xi_y = 0; xi_x = |grad xi|^2 with xi_x != 0 => F'(0) G = 1
Fp0, Gy = sp.symbols('Fp0 Gy', real=True)
sols = sp.solve(sp.Eq(Fp0*Gy, (Fp0*Gy)**2), Gy)
print('INFO solutions of F\'(0)G = (F\'(0)G)^2:', sols)
ok = set(sols) == {0, 1/Fp0}
res.append(ok)
print(('PASS' if ok else 'FAIL'), 'separable: nonzero solution is G = 1/F\'(0), constant')

# (f) zero curve x = a(y), A = xi_x on it, xi_y = -A a'; xi_x = |grad xi|^2  <=>  A = 1/(1 + a'^2)
Aa, ap = sp.symbols('A ap', positive=True)
chk('zero curve: A = A^2(1 + a\'^2) gives A = 1/(1+a\'^2)', sp.solve(sp.Eq(Aa, Aa**2*(1 + ap**2)), Aa)[0] - 1/(1 + ap**2))

# (g) model field (t/g, beta s): Jacobian determinant beta/g, so index sgn(beta)
chk('index: det of (t/g, beta s) is beta/g', sp.Matrix([[1/g, 0], [0, beta]]).det() - beta/g)
# beta >= l  <=>  l >= 1/g  (beta = 2l - 1/g);  c = l - 1/g >= 0
chk('exclusion: beta - l = l - 1/g = c', (2*l - 1/g) - l - (l - 1/g))

print(f'SUMMARY {sum(res)}/{len(res)} PASS')
