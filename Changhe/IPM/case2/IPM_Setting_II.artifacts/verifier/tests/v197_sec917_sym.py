"""V197: independent symbolic checks of Section 9.17 / Proposition 2.1 (frozen candidate 5f37a2bf). Written without
reading the lead's check_917.py. Each check prints its name and True/False."""
import sympy as sp
x, y, s, ph, th = sp.symbols('x y s phi theta', real=True)
R = []
def ok(name, val):
    R.append(bool(val)); print('%-100s %s' % (name, bool(val)), flush=True)
r2 = x**2 + y**2
# kernel from the definition U = grad-perp d_x N, N = -(1/(4 pi)) log(x^2+y^2), away from 0
N = -sp.log(r2) / (4 * sp.pi)
K1 = -sp.diff(N, x, y); K2 = sp.diff(N, x, 2)
ok('K = grad-perp d_x N equals (-sin 2th, cos 2th)/(2 pi r^2)', sp.simplify(K1 + 2 * x * y / r2**2 / (2 * sp.pi)) == 0
   and sp.simplify(K2 - (x**2 - y**2) / r2**2 / (2 * sp.pi)) == 0)
Zb = x - sp.I * y
ok('K1 + i K2 = i/(2 pi Zbar^2)', sp.simplify(K1 + sp.I * K2 - sp.I / (2 * sp.pi * Zb**2)) == 0)
# distributional local term: d_x^2 N + d_y^2 N = -delta, with the p.v. parts cancelling, and the flux of grad d_x N /
# grad d_y N through circles: int_{|Z|=eps} d_x N n_x = -1/2 (so d_xx N = p.v. - delta/2), int d_x N n_y = 0
t = sp.symbols('t', real=True)
cx, cy = sp.cos(t), sp.sin(t)
dxN = sp.diff(N, x).subs({x: cx, y: cy}); 
ok('flux: int_{|Z|=1} d_x N n_x = -1/2 and int d_x N n_y = 0 (local terms -delta/2 for d_xx N, 0 for d_xy N)',
   sp.simplify(sp.integrate(dxN * cx, (t, 0, 2 * sp.pi)) + sp.Rational(1, 2)) == 0 and sp.simplify(sp.integrate(dxN * cy, (t, 0, 2 * sp.pi))) == 0)
# disk potential by matching (independent of K and of the local term): -Lap F = x^2 in r < Rd, F ~ log at infinity
Rd, a0, a2, b0, b2, c0 = sp.symbols('Rd a0 a2 b0 b2 c0', real=True)
rr = sp.symbols('rr', positive=True)
Fin_r = -rr**4 / 32 - rr**4 * sp.cos(2 * th) / 24 + a0 + a2 * rr**2 * sp.cos(2 * th)
Fout_r = b0 * sp.log(rr) + c0 + b2 * rr**-2 * sp.cos(2 * th)
eqs = []
for f_ in (Fin_r - Fout_r, sp.diff(Fin_r - Fout_r, rr)):
    e_ = sp.expand(f_.subs(rr, Rd))
    eqs += [e_.coeff(sp.cos(2 * th)), e_.subs(sp.cos(2 * th), 0)]
sol = sp.solve(eqs, [a0, a2, b0, b2, c0, ], dict=True)
# solve gives one-parameter (c0 free); a2 is what matters
a2v = sol[0][a2]
Fin = -(r2)**2 / 32 - (x**4 - y**4) / 24 + a2v * (x**2 - y**2)
ok('-Lap F_in = x^2', sp.simplify(-sp.diff(Fin, x, 2) - sp.diff(Fin, y, 2) - x**2) == 0)
psi = sp.diff(Fin, x); U = (-sp.diff(psi, y), sp.diff(psi, x))
Wc = (sp.expand(U[0] - U[0].subs({x: 0, y: 0})), sp.expand(U[1] - U[1].subs({x: 0, y: 0})))
ok('disk matching: a2 = R^2/16, centered field of x^2 1_B(0,R) is W_circ = (xy/4, -(7x^2+y^2)/8) for every R',
   sp.simplify(a2v - Rd**2 / 16) == 0 and sp.simplify(Wc[0] - x * y / 4) == 0 and sp.simplify(Wc[1] + (7 * x**2 + y**2) / 8) == 0)
# kernel series (9.17.2)
X_, Y_ = sp.symbols('X Y')
ser = sp.series(sp.I / (2 * sp.pi * (X_ - Y_)**2), X_, 0, 8).removeO()
ok('(9.17.2) i/(2 pi (Xb - Yb)^2) = (i/(2 pi)) sum (k+1) Xb^k Yb^(-k-2) through k = 7',
   sp.simplify(ser - sum(sp.I / (2 * sp.pi) * (k + 1) * X_**k * Y_**(-k - 2) for k in range(8))) == 0)
ok('k-th term majorant: sum (k+1) 2^-k = 4, sum_(j>=0) (j+4) 2^-j = 10',
   sp.summation((sp.Symbol('k') + 1) * sp.Rational(1, 2)**sp.Symbol('k'), (sp.Symbol('k'), 0, sp.oo)) == 4
   and sp.summation((sp.Symbol('j') + 4) * sp.Rational(1, 2)**sp.Symbol('j'), (sp.Symbol('j'), 0, sp.oo)) == 10)
# DK(-Y) X equals the k = 1 term (i/pi) Xbar Ybar^-3 (real check)
y1, y2 = sp.symbols('y1 y2', real=True)
Kf = lambda u, v: (-2 * u * v / (u**2 + v**2)**2 / (2 * sp.pi), (u**2 - v**2) / (u**2 + v**2)**2 / (2 * sp.pi))
Kx = Kf(x - y1, y - y2)
lin = [sp.diff(Kx[j], x).subs({x: 0, y: 0}) * x + sp.diff(Kx[j], y).subs({x: 0, y: 0}) * y for j in range(2)]
pred = sp.I / sp.pi * (x - sp.I * y) * (y1 - sp.I * y2)**-3
ok('DK(-Y) X = (i/pi) Xbar Ybar^-3', sp.simplify(lin[0] + sp.I * lin[1] - pred) == 0)
# real forms
c1, c2, b1, b2_ = sp.symbols('c1 c2 b1 b2', real=True)
cX = sp.expand((c1 + sp.I * c2) * (x - sp.I * y))
ok('c Xbar = (c1 x + c2 y, c2 x - c1 y)', sp.expand(sp.re(cX) - (c1 * x + c2 * y)) == 0 and sp.expand(sp.im(cX) - (c2 * x - c1 * y)) == 0)
bet = b1 + sp.I * b2_
ps3 = sp.re(sp.expand(bet * (x + sp.I * y)**3))
v3 = (-sp.diff(ps3, y), sp.diff(ps3, x)); w3 = sp.expand(3 * sp.I * sp.conjugate(bet) * (x - sp.I * y)**2)
ok('grad-perp Re(beta X^3) = 3i betabar Xbar^2', sp.expand(v3[0] - sp.re(w3)) == 0 and sp.expand(v3[1] - sp.im(w3)) == 0)
l = sp.Symbol('l', real=True)
Q3 = -(x**3 - 3 * x * y**2) / 24; Q2 = (l - sp.Rational(1, 2)) * x * y
gp = lambda f: (-sp.diff(f, y), sp.diff(f, x))
cplx = lambda v: sp.expand(v[0] + sp.I * v[1])
ok('grad-perp Q3 = -(i/8) Xbar^2, grad-perp Q2 = (1/2 - l) Xbar', sp.expand(cplx(gp(Q3)) + sp.I / 8 * (x - sp.I * y)**2) == 0
   and sp.expand(cplx(gp(Q2)) - (sp.Rational(1, 2) - l) * (x - sp.I * y)) == 0)
Wp = (Wc[0] + gp(Q2)[0] + gp(Q3)[0], Wc[1] + gp(Q2)[1] + gp(Q3)[1])
ok('W_circ + gp Q2 + gp Q3 = ((1/2 - l) x, (l - 1/2) y - x^2) = gp(-x^3/3 + (l-1/2)xy)',
   sp.expand(Wp[0] - (sp.Rational(1, 2) - l) * x) == 0 and sp.expand(Wp[1] - ((l - sp.Rational(1, 2)) * y - x**2)) == 0
   and all(sp.expand(Wp[j] - gp(-x**3 / 3 + (l - sp.Rational(1, 2)) * x * y)[j]) == 0 for j in range(2)))
ok('W_circ + gp Q3 = (0, -x^2)', sp.expand(Wc[0] + gp(Q3)[0]) == 0 and sp.expand(Wc[1] + gp(Q3)[1] + x**2) == 0)
# Step 3 Fourier integrals
ip = lambda f: sp.simplify(sp.integrate(sp.expand(f), (ph, 0, 2 * sp.pi)))
E3 = sp.cos(ph)**2 * (sp.cos(3 * ph) + sp.I * sp.sin(3 * ph))
ok('Step 3: int cos^2 e^{3i phi} {1, sin 3phi, cos 3phi} = 0, i pi/2, pi/2',
   ip(E3) == 0 and sp.simplify(ip(E3 * sp.sin(3 * ph)) - sp.I * sp.pi / 2) == 0 and sp.simplify(ip(E3 * sp.cos(3 * ph)) - sp.pi / 2) == 0)
for k in range(1, 7):
    pass
ok('Step 4: int cos^2 phi e^{i(k+2) phi} = 0 for k = 1..8', all(ip(sp.cos(ph)**2 * (sp.cos((k + 2) * ph) + sp.I * sp.sin((k + 2) * ph))) == 0 for k in range(1, 9)))
# polar form of M_k: Y1^2 Ybar^(-k-2) s ds = cos^2 e^{i(k+2)phi} s^(1-k) ds
kk = sp.Symbol('k', positive=True, integer=True)
sP = sp.Symbol('sP', positive=True)
lhs = (sP * sp.cos(ph))**2 * (sP * sp.exp(-sp.I * ph))**(-kk - 2) * sP
ok('M_k integrand in polar coordinates', sp.simplify(lhs - sp.cos(ph)**2 * sp.exp(sp.I * (kk + 2) * ph) * sP**(1 - kk)) == 0)
# Step 4 constants
u = sp.Symbol('u', real=True)
import math
ok('|log(1+u)| <= 2|u| on |u| <= 1/2 (grid of 2001 points and endpoint)', all(abs(math.log1p(v)) <= 2 * abs(v) + 1e-15 for v in [i / 2000 - 0.5 for i in range(2001)]))
ok('|E_R| bound: int_0^{2pi} cos^2 = pi, so the bound is 2 pi S/(mR) <= 4 pi S/(mR)', ip(sp.cos(ph)**2) == sp.pi)
q_ = sp.Symbol('q', positive=True)
tail = sum((k_ + 1) * q_**k_ for k_ in range(3, 400))
ok('sum_(k>=3) (k+1) q^k <= 10 q^3 for q in (0, 1/2] (exact closed form q^3(4 - 3q)/(1-q)^2, increasing)',
   sp.simplify(sp.summation((kk + 1) * q_**kk, (kk, 3, sp.oo)).subs(q_, sp.Rational(1, 2)) - sp.Rational(10, 8)) == 0
   and all(float(tail.subs(q_, v)) <= 10 * v**3 * (1 + 1e-12) for v in [0.01 * i for i in range(1, 51)]))
ok('10 r^2 (L/r)^3 with r = R m/2 equals 20 L^3/(m R)', sp.simplify(10 * (sp.Symbol('R') * sp.Symbol('m') / 2)**2 * (sp.Symbol('L') / (sp.Symbol('R') * sp.Symbol('m') / 2))**3
                                                              - 20 * sp.Symbol('L')**3 / (sp.Symbol('m') * sp.Symbol('R'))) == 0)
# Step 5 moments
a, b, al1, al2 = sp.symbols('a b alpha1 alpha2', real=True)
E4 = sp.cos(ph)**2 * (sp.cos(4 * ph) + sp.I * sp.sin(4 * ph))
ok('Step 5: J for log rho_0 = a cos 4phi + b sin 4phi is (pi/2)(a + ib)', sp.simplify(ip(E4 * (a * sp.cos(4 * ph) + b * sp.sin(4 * ph))) - sp.pi / 2 * (a + sp.I * b)) == 0)
ok('Step 5: I for delta = alpha1 cos + alpha2 sin is (pi/4)(alpha1 + i alpha2)', sp.simplify(ip(E3 * (al1 * sp.cos(ph) + al2 * sp.sin(ph))) - sp.pi / 4 * (al1 + sp.I * al2)) == 0)
ok('Step 5: G = 0 for every mode 4j of rho_0 (j = 0..4, cos and sin)', all(ip(E3 * f_) == 0 for j in range(5) for f_ in (sp.cos(4 * j * ph), sp.sin(4 * j * ph))))
# profile condition
cr, ci, dr, di = sp.symbols('cr ci dr di', real=True)
W1 = x * y / 4 + sp.re(sp.expand((cr + sp.I * ci) * (x - sp.I * y))) + sp.re(sp.expand((dr + sp.I * di) * (x - sp.I * y)**2))
sol = sp.solve(sp.Poly(sp.expand(W1 - (sp.Rational(1, 2) - l) * x), x, y).coeffs(), [cr, ci, dr, di], dict=True)
ok('W^(1) = (1/2 - l) x iff c = 1/2 - l, c\' = -i/8', sol == [{cr: sp.Rational(1, 2) - l, ci: 0, dr: 0, di: -sp.Rational(1, 8)}])
Iv = (sp.Rational(1, 2) - l) * sp.pi / sp.I; Jv = -sp.I / 8 * 2 * sp.pi / (3 * sp.I)
ok('then I = i pi (l - 1/2), J = -pi/12', sp.simplify(Iv - sp.I * sp.pi * (l - sp.Rational(1, 2))) == 0 and sp.simplify(Jv + sp.pi / 12) == 0)
ok('example a = -1/6, alpha2 = 4(l - 1/2): J = -pi/12, I = i pi (l - 1/2)',
   sp.simplify(sp.pi / 2 * (-sp.Rational(1, 6)) + sp.pi / 12) == 0 and sp.simplify(sp.pi / 4 * sp.I * 4 * (l - sp.Rational(1, 2)) - sp.I * sp.pi * (l - sp.Rational(1, 2))) == 0)
ok('V.grad(x^2) = x^2 for V = lX + W with W = ((1/2-l)x, (l-1/2)y - x^2)', sp.expand(2 * x * (l * x + Wp[0]) - x**2) == 0)
# Step 6 ellipse
A_, B_ = sp.symbols('A B', positive=True)
mu = sp.Symbol('mu', real=True)
qv = (B_**2 - A_**2) / (B_**2 + A_**2)
ok('ellipse: cos^2/A^2 + sin^2/B^2 = (1/2)(A^-2 + B^-2)(1 + q cos 2phi)', sp.simplify(sp.expand_trig(sp.cos(ph)**2 / A_**2 + sp.sin(ph)**2 / B_**2
    - (A_**-2 + B_**-2) / 2 * (1 + qv * sp.cos(2 * ph)))) == 0)
ok('|1 + mu e^{2i phi}|^2 = (1 + mu^2)(1 + (2mu/(1+mu^2)) cos 2phi)', sp.simplify(sp.expand((1 + mu * sp.cos(2 * ph))**2 + (mu * sp.sin(2 * ph))**2)
    - (1 + mu**2) * (1 + 2 * mu / (1 + mu**2) * sp.cos(2 * ph))) == 0)
# Fourier coefficients of log rho_0 = -(1/2) log(1 + q cos 2phi) + const via series in mu
f_ser = sp.series(-sp.log(1 + mu * sp.exp(2 * sp.I * ph)), mu, 0, 5).removeO()
ok('-Re log(1 + mu e^{2i phi}) = sum (-mu)^n cos(2n phi)/n through n = 4',
   sp.simplify(sp.expand(sp.re(sp.expand(f_ser, complex=True))) - sum((-mu)**n_ * sp.cos(2 * n_ * ph) / n_ for n_ in range(1, 5))) == 0)
fj = sp.symbols('f0:9', real=True)
fe = sum(fj[j] * sp.cos(j * ph) for j in range(9))
ok('int cos^2 phi e^{4i phi} f = (pi/4)(f2 + 2 f4 + f6) for even f (modes 0..8)', sp.simplify(ip(E4 * fe) - sp.pi / 4 * (fj[2] + 2 * fj[4] + fj[6])) == 0)
Jmu = sp.pi / 4 * (-mu + mu**2 - mu**3 / 3)
ok('J = (pi/4)(-mu + mu^2 - mu^3/3) = (pi/12)((1-mu)^3 - 1)', sp.expand(Jmu - sp.pi / 12 * ((1 - mu)**3 - 1)) == 0)
ok('q = 2mu/(1+mu^2) maps (-1,1) onto (-1,1) increasingly; mu -> 1 as q -> 1',
   sp.simplify(sp.diff(2 * mu / (1 + mu**2), mu) - 2 * (1 - mu**2) / (1 + mu**2)**2) == 0 and sp.limit(2 * mu / (1 + mu**2), mu, 1) == 1)
# Step 3 example
gam = sp.Symbol('gamma', positive=True)
hS = (1 + sP**-2)**((gam - 2) / 2)
ok('rho_gamma polar integrand: s^2 cos^2 (1+s^2)^((g-2)/2) s^-3 s = s^(g-2) h(s)', sp.simplify(sP**2 * (1 + sP**2)**((gam - 2) / 2) * sP**-3 * sP
                                                                                       - sP**(gam - 2) * hS) == 0)
ok('rho_gamma = x^2 + O(r^4): series of (1+r^2)^((g-2)/2) is 1 + O(r^2)', sp.series((1 + sP**2)**((gam - 2) / 2), sP, 0, 2).removeO() == 1)
del_ = sp.Symbol('delta', positive=True); gp1 = sp.Symbol('g1', positive=True); wv = sp.Symbol('w', positive=True)
tR = (sP**gp1 + del_)**(1 / gp1)   # gamma = 1 + g1 > 1
I1 = sp.integrate(wv**(gp1 - 1), (wv, sP, tR))
ok('int_R^{t_R} s^(gamma-2) ds = delta/(gamma - 1) (gamma > 1), and = delta for gamma = 1, t_R = R e^delta',
   sp.simplify(sp.powsimp(sp.simplify(I1), force=True) - del_ / gp1) == 0 and sp.simplify(sp.integrate(1 / wv, (wv, sP, sP * sp.exp(del_))) - del_) == 0)
hh = lambda sv, g: (1 + sv**-2)**((g - 2) / 2)
ok('0 <= 1 - h(s) <= s^-2 for gamma in [1, 2), s >= 1 (grid)', all(0 <= 1 - hh(sv, g) <= sv**-2 + 1e-15 for sv in [1 + 0.05 * i for i in range(400)] for g in [1 + 0.05 * j for j in range(20)]))
ok('Delta for delta = a(1 + sin 3phi) + b(1 + cos 3phi) is (pi/2)(b + i a)', sp.simplify(ip(E3 * (a * (1 + sp.sin(3 * ph)) + b * (1 + sp.cos(3 * ph)))) - sp.pi / 2 * (b + sp.I * a)) == 0)
# reflection parities
ok('K1(x, -y) = -K1(x, y), K2(x, -y) = K2(x, y)', sp.simplify(K1.subs(y, -y) + K1) == 0 and sp.simplify(K2.subs(y, -y) - K2) == 0)
print('ALL', all(R), len(R), flush=True)
