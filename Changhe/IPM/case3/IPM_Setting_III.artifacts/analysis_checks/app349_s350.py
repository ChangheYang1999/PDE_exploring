"""Symbolic checks for A.3.50 (identities quoted in the appendix text).

Run with OMP_NUM_THREADS=1.  Exit status is nonzero on failure.
"""
import sys
import sympy as sp
import mpmath as mp

results = []


def report(name, ok, info=""):
    results.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + ((": " + info) if info else ""))


def zero(e):
    return sp.simplify(sp.expand(e)) == 0


x, y = sp.symbols('x y', real=True)
r, th, s, z, t, tau = sp.symbols('r theta s z t tau', positive=True)
a, cl, k, A_, D_ = sp.symbols('a c_l k A D', positive=True)
R2 = x**2 + y**2
rr = sp.sqrt(R2)


def lap(f):
    return sp.diff(f, x, 2) + sp.diff(f, y, 2)


# ------------------------------------------------------------ radial formulas
Hf = sp.Function('H')
Hr = Hf(r)
H1, H2 = sp.diff(Hr, r), sp.diff(Hr, r, 2)
f_r = 4 * Hr + r * H1
fp_r = sp.diff(f_r, r)
# psi = -a x y H(r) in polar coordinates; compute Cartesian second derivatives via chain rule
xr, yr = r * sp.cos(th), r * sp.sin(th)
P = sp.Function('P')
psi_c = -a * x * y * Hf(rr)
d = {}
for (i, j) in [(2, 0), (1, 1), (0, 2), (1, 0), (0, 1)]:
    e = psi_c
    if i:
        e = sp.diff(e, x, i)
    if j:
        e = sp.diff(e, y, j)
    d[(i, j)] = e
sub_pol = {x: xr, y: yr}


def topolar(e):
    e = e.subs(sub_pol)
    e = e.subs(sp.sqrt(r**2 * sp.cos(th)**2 + r**2 * sp.sin(th)**2), r)
    e = sp.simplify(e)
    return e


S11 = topolar(-d[(1, 1)])
S12 = topolar((d[(2, 0)] - d[(0, 2)]) / 2)
# replace derivatives of H at r
Kq = 2 * f_r + r * fp_r
Qq = r * fp_r + 24 * Hr - 6 * f_r


def clean(e):
    e = e.replace(lambda u: isinstance(u, sp.Subs), lambda u: u.doit())
    return sp.simplify(e)


S11c = clean(S11)
S12c = clean(S12)
ok1 = zero(sp.expand(sp.expand_trig(S11c - a / 8 * (Kq - Qq * sp.cos(4 * th)))))
ok2 = zero(sp.expand(sp.expand_trig(S12c + a / 8 * Qq * sp.sin(4 * th))))
report("radial strain S11 = (a/8)(K - Q cos 4th)", ok1)
report("radial strain S12 = -(a/8) Q sin 4th", ok2)
report("K = 8H + 7rH' + r^2H'', Q = r^2H'' - rH'",
       zero(Kq - (8 * Hr + 7 * r * H1 + r**2 * H2)) and zero(Qq - (r**2 * H2 - r * H1)))
# max over theta of |S|^2 = (a/8)^2 (K^2 - 2KQ cos4th + Q^2)
report("|S|_op^2 = S11^2 + S12^2 = (a/8)^2 (K^2 - 2 K Q cos 4th + Q^2)",
       zero(sp.expand_trig(sp.expand((a / 8)**2 * ((Kq - Qq * sp.cos(4 * th))**2 + Qq**2 * sp.sin(4 * th)**2)
                                     - (a / 8)**2 * (Kq**2 - 2 * Kq * Qq * sp.cos(4 * th) + Qq**2)))))
# t = log r form
Ht = sp.Function('h')
T = sp.Symbol('T')
He = Ht(sp.log(r))
Kt = (8 * He + 7 * r * sp.diff(He, r) + r**2 * sp.diff(He, r, 2))
Qt = (r**2 * sp.diff(He, r, 2) - r * sp.diff(He, r))
h0, h1, h2 = sp.symbols('h0 h1 h2')
def tsub(e):
    e = sp.expand(e)
    e = e.subs(sp.Derivative(Ht(sp.log(r)), sp.log(r), 2), h2)
    return e
# direct: r d/dr = d/dt, r^2 d^2/dr^2 = d^2/dt^2 - d/dt
lam = sp.Symbol('lam')
He2 = sp.exp(lam * sp.log(r))
Kt2 = sp.simplify((8 * He2 + 7 * r * sp.diff(He2, r) + r**2 * sp.diff(He2, r, 2)) / He2)
Qt2 = sp.simplify((r**2 * sp.diff(He2, r, 2) - r * sp.diff(He2, r)) / He2)
report("t-form: K + Q = 8H + 4H_t + 2H_tt and K - Q = 8H + 8H_t (tested on H = e^{lam t})",
       zero(Kt2 + Qt2 - (8 + 4 * lam + 2 * lam**2)) and zero(Kt2 - Qt2 - (8 + 8 * lam)))
# transport residual for rho = a y f(r), psi = -a x y H, W = c_l X + U, U = (-psi_y, psi_x)
fF = sp.Function('f')
rho = a * y * (4 * Hf(rr) + rr * sp.diff(Hf(rr), x) * rr / x)
rho = sp.simplify(rho)
U1 = -sp.diff(psi_c, y)
U2 = sp.diff(psi_c, x)
Fres = (cl * x + U1) * sp.diff(rho, x) + (cl * y + U2) * sp.diff(rho, y) - rho
Fp = clean(topolar(Fres / (a * y)))
fr, fpr, Hpr = f_r, fp_r, H1
target = cl * r * fpr + (cl - 1) * fr - a * Hr * fr - a * r * Hr * fpr + sp.cos(th)**2 * a * r * (2 * Hr * fpr - Hpr * fr)
report("radial residual F/(a y) = c_l r f' + D f - a H f - a r H f' + cos^2 th a r (2 H f' - H' f)",
       zero(sp.expand(sp.expand_trig(Fp - target))))
# H = (1/(2S^2)) int_0^S s F(s) ds solves 4H + r H' = f with S = r^2 (checked on F = s^n)
nn = sp.Symbol('n', positive=True)
Sv = r**2
Hs = sp.integrate(s * s**nn, (s, 0, Sv)) / (2 * Sv**2)
report("H = (1/(2 S^2)) int_0^S s F ds gives 4H + rH' = F (F = s^n)", zero(sp.simplify(4 * Hs + r * sp.diff(Hs, r) - Sv**nn)))
# radial velocity formula
Hn = Hf(rr)
Ucheck1 = -sp.diff(psi_c, y) - a * x * (Hn + y**2 * sp.diff(Hn, y) / y / rr * rr) * 1
report("U = a (x (H + y^2 H'/r), -y (H + x^2 H'/r))",
       zero(sp.simplify((-sp.diff(psi_c, y) - a * x * (Hn + y * sp.diff(Hn, y))).subs(sub_pol))) and
       zero(sp.simplify((sp.diff(psi_c, x) + a * y * (Hn + x * sp.diff(Hn, x))).subs(sub_pol))))
# |grad(y f)|^2 = cos^2 f^2 + sin^2 (f + r f')^2
ff = fF(rr)
g2 = sp.diff(y * ff, x)**2 + sp.diff(y * ff, y)**2
f0s, f1s = sp.symbols('f0 f1')
g2p = clean(topolar(g2))
F0, F1 = fF(r), sp.diff(fF(r), r)
report("|grad(y f)|^2 = cos^2 th f^2 + sin^2 th (f + r f')^2",
       zero(sp.expand(sp.expand_trig(g2p - (sp.cos(th)**2 * F0**2 + sp.sin(th)**2 * (F0 + r * F1)**2)))))

# ------------------------------------------------------------ 3.50(a)
fb = (1 + s)**sp.Rational(-1, 4)
rfb = 2 * s * sp.diff(fb, s)
report("base: r f' = -(s/2)(1+s)^{-5/4}", zero(sp.simplify(rfb + s / 2 * (1 + s)**sp.Rational(-5, 4))))
report("base: f + r f' = (1+s)^{-5/4}(1 + s/2)", zero(sp.simplify(fb + rfb - (1 + s)**sp.Rational(-5, 4) * (1 + s / 2))))
report("base: 2f - rf' <= 2 reduces to 1 + 5s/4 <= (1+s)^{5/4}",
       zero(sp.simplify((2 * fb - rfb) - (1 + s)**sp.Rational(-5, 4) * (2 + 5 * s / 2))))
report("base: f + rf'/2 = (3/4)u^{-1/4} + (1/4)u^{-5/4}, u = 1+s",
       zero(sp.simplify(fb + rfb / 2 - (sp.Rational(3, 4) * (1 + s)**sp.Rational(-1, 4) + sp.Rational(1, 4) * (1 + s)**sp.Rational(-5, 4)))))
report("base: (3/4)2^{-1/4} + (1/4)2^{-5/4} = (7/4) 2^{-5/4}",
       zero(sp.Rational(3, 4) * 2**sp.Rational(-1, 4) + sp.Rational(1, 4) * 2**sp.Rational(-5, 4) - sp.Rational(7, 4) * 2**sp.Rational(-5, 4)))
report("base: 2X.grad(y f) - y f = y (1+r^2)^{-5/4}", zero(sp.simplify(y * (fb + 2 * rfb) - y * (1 + s)**sp.Rational(-5, 4))))
# chord / tangent bounds for convex F on [0,S]
Fs = sp.Function('F')
Sx = sp.Symbol('S', positive=True)
F0s, F1s = sp.symbols('F0 FS')
chord = sp.integrate(s * (1 - (1 - F1s) * s / Sx), (s, 0, Sx)) / (2 * Sx**2)
report("chord bound: H <= 1/12 + F(S)/6", zero(chord - (sp.Rational(1, 12) + F1s / 6)))
Fp_ = sp.Symbol('FpS')
tang = sp.integrate(s * (F1s + Fp_ * (s - Sx)), (s, 0, Sx)) / (2 * Sx**2)
report("tangent bound: H >= F/4 - S F'(S)/12 = F/4 - r f'/24", zero(tang - (F1s / 4 - Sx * Fp_ / 12)))
# H for f = (1+s)^{-1/4} at large r: (1/(2S^2)) int s^{3/4} = (2/7) S^{-1/4}
report("int_0^S s^{3/4} ds/(2S^2) = (2/7) S^{-1/4}", zero(sp.integrate(s**sp.Rational(3, 4), (s, 0, Sx)) / (2 * Sx**2) - sp.Rational(2, 7) * Sx**sp.Rational(-1, 4)))
# Fourier data of the Gaussian strain
xi1, xi2, L, B, u = sp.symbols('xi1 xi2 L B u', positive=True)
psihat = sp.Symbol('psihat')
M = sp.Matrix([[xi1 * xi2, (xi2**2 - xi1**2) / 2], [(xi2**2 - xi1**2) / 2, -xi1 * xi2]])
report("|hat S|_op: (xi1 xi2)^2 + ((xi2^2 - xi1^2)/2)^2 = |xi|^4/4",
       zero((xi1 * xi2)**2 + ((xi2**2 - xi1**2) / 2)**2 - (xi1**2 + xi2**2)**2 / 4))
# transforms: hat of exp(-x^2/L^2) and y exp(-y^2)
X_ = sp.Symbol('X', real=True)
w_ = sp.Symbol('w', real=True)
ft1 = sp.integrate(sp.exp(-X_**2 / L**2) * sp.exp(-sp.I * X_ * w_), (X_, -sp.oo, sp.oo))
report("hat exp(-x^2/L^2) = sqrt(pi) L exp(-L^2 xi^2/4)", zero(sp.simplify(ft1 - sp.sqrt(sp.pi) * L * sp.exp(-L**2 * w_**2 / 4))))
ft2 = sp.integrate(X_ * sp.exp(-X_**2) * sp.exp(-sp.I * X_ * w_), (X_, -sp.oo, sp.oo))
report("hat y exp(-y^2) = -i sqrt(pi)(xi/2) exp(-xi^2/4)", zero(sp.simplify(ft2 + sp.I * sp.sqrt(sp.pi) * w_ / 2 * sp.exp(-w_**2 / 4))))
cc = sp.Symbol('c', positive=True)
m1 = sp.integrate(2 * xi1 * sp.exp(-cc * xi1**2), (xi1, 0, sp.oo))
m3 = sp.integrate(2 * xi1**3 * sp.exp(-cc * xi1**2), (xi1, 0, sp.oo))
report("int |xi| e^{-c xi^2} = 1/c and int |xi|^3 e^{-c xi^2} = 1/c^2", zero(m1 - 1 / cc) and zero(m3 - 1 / cc**2))
report("moments at c = L^2/4 and c = 1/4: 4/L^2, 16/L^4, 4, 16",
       zero((1 / cc).subs(cc, L**2 / 4) - 4 / L**2) and zero((1 / cc**2).subs(cc, L**2 / 4) - 16 / L**4) and
       (1 / cc).subs(cc, sp.Rational(1, 4)) == 4 and (1 / cc**2).subs(cc, sp.Rational(1, 4)) == 16)
# sup bound and difference bound constants
supS = (2 * sp.pi)**-2 * (B * sp.pi * L / 4) * (4 / L**2) * 4
report("(2pi)^{-2} int |hat S| = B/(pi L)", zero(supS - B / (sp.pi * L)))
diffS1 = (2 * sp.pi)**-2 * sp.Rational(1, 2) * (B * sp.pi * L / 4) * (16 / L**4) * 4
diffS2 = (2 * sp.pi)**-2 * sp.Rational(1, 2) * (B * sp.pi * L / 4) * (4 / L**2) * 16
report("difference coefficients 2B/(pi L^3) (x^2) and 2B/(pi L) (y^2)",
       zero(diffS1 - 2 * B / (sp.pi * L**3)) and zero(diffS2 - 2 * B / (sp.pi * L)))
aa, bb = sp.symbols('alpha beta', positive=True)
uint = sp.integrate((aa + u)**sp.Rational(-3, 2) * (bb + u)**sp.Rational(-3, 2), (u, 0, sp.oo))
target_u = 2 / (sp.sqrt(aa * bb) * (sp.sqrt(aa) + sp.sqrt(bb))**2)
okU = all(abs(float((uint - target_u).subs({aa: av, bb: bv}))) < 1e-12 for av, bv in [(1, 2), (sp.Rational(9, 4), sp.Rational(1, 4)), (5, sp.Rational(1, 7))])
report("int_0^inf (a+u)^{-3/2}(b+u)^{-3/2} du = 2/(sqrt(ab)(sqrt a + sqrt b)^2)", okU)
# derivative check of the antiderivative to make it exact
Fanti = -2 * (2 * u + aa + bb) / ((aa - bb)**2 * sp.sqrt((aa + u) * (bb + u)))
report("antiderivative of (a+u)^{-3/2}(b+u)^{-3/2} is -2(2u+a+b)/((a-b)^2 sqrt((a+u)(b+u)))",
       zero(sp.simplify(sp.diff(Fanti, u) - (aa + u)**sp.Rational(-3, 2) * (bb + u)**sp.Rational(-3, 2))))
val0 = sp.simplify(sp.limit(Fanti, u, sp.oo) - Fanti.subs(u, 0))
report("value at u = 0 equals 2/(sqrt(ab)(sqrt a + sqrt b)^2)",
       all(abs(float((val0 - target_u).subs({aa: av, bb: bv}))) < 1e-13 for av, bv in [(3, 1), (sp.Rational(25, 4), sp.Rational(1, 4))]))
S110 = (2 * sp.pi)**-2 * (B * sp.pi * L / 2) * (sp.pi / 4) * target_u.subs({aa: L**2 / 4, bb: sp.Rational(1, 4)})
report("S_g,11(0) = B/(L+1)^2", zero(sp.simplify(S110 - B / (L + 1)**2)))
# numeric confirmation of S11(0) for L = 3, B = 1 by direct 2D quadrature
Lv = 3
val = mp.quad(lambda p, q: (1 * mp.pi * Lv / 2) * p**2 * q**2 / (p**2 + q**2) * mp.e**(-Lv**2 * p**2 / 4 - q**2 / 4),
              [-mp.inf, 0, mp.inf], [-mp.inf, 0, mp.inf]) / (2 * mp.pi)**2
report("numeric S_g,11(0) at L = 3, B = 1 equals 1/16", abs(val - mp.mpf(1) / 16) < 1e-10, mp.nstr(val, 15))
# Gaussian gradient in scaled coordinates
w = sp.Symbol('w', positive=True)
report("(2w-1)e^{-w} has derivative (3-2w)e^{-w}", zero(sp.diff((2 * w - 1) * sp.exp(-w), w) - (3 - 2 * w) * sp.exp(-w)))
# rho_y(0,1) for the base: 4(1-delta)(f + r f')(r = 1) = 6 (1-delta) 2^{-5/4}
report("base y-derivative at (0,1): 4 (f + r f')(s=1) = 6 * 2^{-5/4}",
       zero(sp.simplify(4 * (fb + rfb).subs(s, 1) - 6 * 2**sp.Rational(-5, 4))))

# ------------------------------------------------------------ 3.50(b)
g = sp.exp(-z)
# with z = 1/r^2: r d/dr = -2 z d/dz
rd = lambda e: -2 * z * sp.diff(e, z)
E1 = sp.expint(1, z)
Hg = ((1 - z) * g + z**2 * E1) / 4
report("H_g = ((1-z)e^{-z} + z^2 E_1(z))/4 satisfies 4H + rH' = e^{-z}", zero(sp.simplify(4 * Hg + rd(Hg) - g)))
report("H_g = (z^2/2) int_z^inf w^{-3} e^{-w} dw", zero(sp.simplify(sp.diff(Hg / (z**2 / 2), z) + z**-3 * sp.exp(-z))))
Hgn = lambda zz: ((1 - zz) * mp.e**(-zz) + zz**2 * mp.e1(zz)) / 4
report("H_g -> 0 as z -> inf and H_g -> 1/4 as z -> 0 (numeric), and 0 < H_g <= e^{-z}/4",
       abs(Hgn(mp.mpf(200))) < 1e-80 and abs(Hgn(mp.mpf('1e-12')) - 0.25) < 1e-10 and
       all(0 < Hgn(zz) <= mp.e**(-zz) / 4 for zz in [mp.mpf('0.001'), mp.mpf('0.3'), 1, 3, 10, 50]))
f1 = 1 - g
H1b = sp.Rational(1, 4) - Hg
K1 = 2 * f1 + rd(f1)
Q1 = rd(f1) + 24 * H1b - 6 * f1
report("K = 2[1 - (1+z) e^{-z}]", zero(sp.simplify(K1 - 2 * (1 - (1 + z) * g))))
report("K - Q = 2 - 8 e^{-z} + 24 H_g", zero(sp.simplify(K1 - Q1 - (2 - 8 * g + 24 * Hg))))
report("K + Q = 2 + 4(1-z) e^{-z} - 24 H_g", zero(sp.simplify(K1 + Q1 - (2 + 4 * (1 - z) * g - 24 * Hg))))
report("4(1-z)e^{-z} - 24 H_g = -2(1-z)e^{-z} - 6 z^2 E_1(z)",
       zero(sp.simplify(4 * (1 - z) * g - 24 * Hg - (-2 * (1 - z) * g - 6 * z**2 * E1))))
okE = all(mp.e1(zz) > mp.e**(-zz) / (1 + zz) for zz in [mp.mpf('0.01'), mp.mpf('0.5'), 1, 2, 5, 20, 80])
report("numeric spot check E_1(z) > e^{-z}/(1+z)", okE)
bet = sp.Symbol('beta', positive=True)
Dd = sp.Symbol('D', positive=True)
report("1 - 2 beta = 1/c_l for beta = D/(2(1+D))", zero(1 - 2 * Dd / (2 * (1 + Dd)) - 1 / (1 + Dd)))
# binomial weights: sum_{j>=1} w_j (1 - g^j) = (1-g)^beta, check by series to order 8
gg = sp.Symbol('g')
bv = sp.Rational(3, 10)
ser = sp.series((1 - gg)**bv, gg, 0, 9).removeO()
wsum = sum(((-1)**(j - 1) * sp.binomial(bv, j)) * (1 - gg**j) for j in range(1, 9))
tail = sum(((-1)**(j - 1) * sp.binomial(bv, j)) for j in range(1, 9))
report("(1-g)^beta = 1 - sum w_j g^j through order 8 (beta = 3/10), w_j > 0",
       zero(sp.expand(ser - (1 - sum(((-1)**(j - 1) * sp.binomial(bv, j)) * gg**j for j in range(1, 9))))) and
       all(((-1)**(j - 1) * sp.binomial(bv, j)) > 0 for j in range(1, 30)))
# not a profile: cos^2 coefficient zero => H = f^2/4 => f = 1
fq = sp.Function('f')
report("H = f^2/4 and f = 4H + rH' give r f' = 2(1 - f) when f != 0",
       zero(sp.expand(4 * (fq(r)**2 / 4) + r * sp.diff(fq(r)**2 / 4, r) - fq(r) - fq(r) / 2 * (2 * fq(r) + r * sp.diff(fq(r), r) - 2))))

# ------------------------------------------------------------ 3.50(c)
A = 2 * cl - 1
rho_c = A * y * (1 + sp.cos(k * x))
psi_cc = y * (cl * x - A / k * sp.sin(k * x))
report("(c): -Lap psi = rho_x", zero(-lap(psi_cc) - sp.diff(rho_c, x)))
U1c, U2c = -sp.diff(psi_cc, y), sp.diff(psi_cc, x)
W1c, W2c = cl * x + U1c, cl * y + U2c
report("(c): W = ((A/k) sin kx, y (2 c_l - A cos kx))", zero(W1c - A / k * sp.sin(k * x)) and zero(W2c - y * (2 * cl - A * sp.cos(k * x))))
report("(c): W . grad rho = rho", zero(sp.expand(sp.expand_trig(W1c * sp.diff(rho_c, x) + W2c * sp.diff(rho_c, y) - rho_c))))
S11c_ = -sp.diff(psi_cc, x, y)
S12c_ = (sp.diff(psi_cc, x, 2) - sp.diff(psi_cc, y, 2)) / 2
wv = 1 - sp.cos(k * x)
Dc = cl - 1
fact = A * wv * (-2 * Dc + A * wv + A * k**2 * y**2 / 4 * (1 + sp.cos(k * x)))
report("(c): |S|_op^2 - D^2 = A w [-2D + A w + (A k^2 y^2/4)(1 + cos kx)]",
       zero(sp.expand(sp.expand_trig(S11c_**2 + S12c_**2 - Dc**2 - fact)).rewrite(sp.cos).subs(sp.sin(k * x)**2, 1 - sp.cos(k * x)**2)))
report("(c): U(0) = 0, a0 = 2A, psi_xy(0) = -D",
       zero(U1c.subs({x: 0, y: 0})) and zero(U2c.subs({x: 0, y: 0})) and zero(sp.diff(rho_c, y).subs({x: 0, y: 0}) - 2 * A)
       and zero(sp.diff(psi_cc, x, y).subs({x: 0, y: 0}) + Dc))
hc = rho_c - 2 * A * y
lamv = sp.Symbol('lam')
hser = sp.series(hc.subs({x: lamv * x, y: lamv * y}), lamv, 0, 5).removeO()
report("(c): h = -(A k^2/2) x^2 y + O(r^5)", zero(sp.expand(hser - lamv**3 * (-(A * k**2 / 2) * x**2 * y))))
report("(c): bracket bound -2D + A k^2 r^2/2 <= 0 iff r <= (2/k)(D/A)^{1/2}",
       zero((-2 * Dc + A * k**2 * ((2 / k) * sp.sqrt(Dc / A))**2 / 2)))

# ------------------------------------------------------------ 3.50(d)
al = sp.Symbol('alpha', positive=True)
H0 = (sp.exp(-al * tau) - al * sp.exp(-tau)) / (1 - al)
report("(d): H0(0+) = 1, H0'(0+) = 0, H0''(0+) = -alpha",
       zero(H0.subs(tau, 0) - 1) and zero(sp.diff(H0, tau).subs(tau, 0)) and zero(sp.diff(H0, tau, 2).subs(tau, 0) + al))
report("(d): H0 + H0' = e^{-alpha tau}", zero(sp.simplify(H0 + sp.diff(H0, tau) - sp.exp(-al * tau))))
G0 = H0 + sp.diff(H0, tau) / 2 + sp.diff(H0, tau, 2) / 4
G0f = (sp.exp(-al * tau) * (1 - al / 2 + al**2 / 4) - 3 * al / 4 * sp.exp(-tau)) / (1 - al)
report("(d): G0 formula", zero(sp.simplify(G0 - G0f)))
report("(d): G0(0+) = 1 - alpha/4", zero(sp.simplify(G0f.subs(tau, 0) - (1 - al / 4))))
report("(d): G0 - e^{-alpha tau}(1 - alpha/4) = (3 alpha/4)(e^{-alpha tau} - e^{-tau})/(1 - alpha)",
       zero(sp.simplify(G0f - sp.exp(-al * tau) * (1 - al / 4) - 3 * al / 4 * (sp.exp(-al * tau) - sp.exp(-tau)) / (1 - al))))
report("(d): G0' = [-alpha e^{-alpha tau}(1 - alpha/2 + alpha^2/4) + (3 alpha/4) e^{-tau}]/(1-alpha)",
       zero(sp.simplify(sp.diff(G0f, tau) - (-al * sp.exp(-al * tau) * (1 - al / 2 + al**2 / 4) + 3 * al / 4 * sp.exp(-tau)) / (1 - al))))
report("(d): 1 - alpha/2 + alpha^2/4 = 3/4 + (1 - alpha)^2/4", zero(1 - al / 2 + al**2 / 4 - sp.Rational(3, 4) - (1 - al)**2 / 4))
# linear part of the residual kills e^{-alpha t}: c_l r f' + D f with f = e^{-alpha t}, alpha = D/c_l
report("(d): c_l (-alpha) + D = 0 for alpha = D/c_l, and 1 - alpha = 1/c_l",
       zero(cl * (-(cl - 1) / cl) + (cl - 1)) and zero(1 - (cl - 1) / cl - 1 / cl))
# remote pair
fs, gfun, Ks = sp.Function('fs'), sp.Function('g'), sp.Function('Ks')
b_ = sp.Symbol('b', positive=True)
Phi = Ks(x / L)                       # Phi(x) = K_*(x/L), K_*' = f_*
psi_r = b_ * sp.diff(Phi, x) * gfun(y)  # = (b/L) f_*(x/L) g(y)
rho_r = -b_ * sp.diff(Phi, x, 2) * gfun(y) - b_ * Phi * sp.diff(gfun(y), y, 2)  # = -(b/L^2) f_*' g - b K_* g''
report("(d): remote pair -Lap psi_r = d_x rho_r (with K_*' = f_*)", zero(-lap(psi_r) - sp.diff(rho_r, x)))
psi_r_f = b_ / L * fs(x / L) * gfun(y)
xs = sp.Symbol('xs')
S11r = -sp.diff(psi_r_f, x, y)
S12r = (sp.diff(psi_r_f, x, 2) - sp.diff(psi_r_f, y, 2)) / 2
report("(d): S_r,11 = -(b/L^2) f_*'(x/L) g'(y)",
       zero(sp.simplify(S11r + b_ / L**2 * sp.Subs(sp.Derivative(fs(xs), xs), xs, x / L).doit() * sp.diff(gfun(y), y))))
report("(d): S_r,12 = (b/(2L)) (f_*''(x/L) g/L^2 - f_*(x/L) g'')",
       zero(sp.simplify(S12r - b_ / (2 * L) * (sp.Subs(sp.Derivative(fs(xs), xs, 2), xs, x / L).doit() * gfun(y) / L**2
                                                   - fs(x / L) * sp.diff(gfun(y), y, 2)))))
# remote density on |x| < L: f_* = 0 there, K_* = -1, so rho_r = b g''
gy = y**3 / 6
report("(d): g = y^3/6 gives g'' = y, g'(1) = 1/2", zero(sp.diff(gy, y, 2) - y) and sp.diff(gy, y).subs(y, 1) == sp.Rational(1, 2))

# ------------------------------------------------------------ 3.50(e)
E = sp.exp(-x**2 / L**2 - y**2)
report("(e): d_y(y E) = (1 - 2y^2) E and x d_x(yE) = -2 x^2 y E/L^2",
       zero(sp.diff(y * E, y) - (1 - 2 * y**2) * E) and zero(x * sp.diff(y * E, x) + 2 * x**2 * y * E / L**2))
report("(e): X . grad(y E) = y E (1 - 2x^2/L^2 - 2y^2)",
       zero(sp.simplify(x * sp.diff(y * E, x) + y * sp.diff(y * E, y) - y * E * (1 - 2 * x**2 / L**2 - 2 * y**2))))
J3 = sp.integrate((1 - sp.exp(-s))**2 / s**2, (s, 0, sp.oo))
report("(e): J_3 = int_0^inf s^{-2}(1 - e^{-s})^2 ds = 2 log 2", zero(sp.simplify(J3 - 2 * sp.log(2))), str(J3))
mm = sp.Symbol('m', positive=True)
cm = sp.integrate((1 + u**2)**(-3), (u, -sp.oo, sp.oo))
report("(e): int (1+u^2)^{-m} du at m = 3 equals sqrt(pi) Gamma(5/2)/Gamma(3) = 3 pi/8",
       zero(cm - sp.sqrt(sp.pi) * sp.gamma(sp.Rational(5, 2)) / sp.gamma(3)) and zero(cm - 3 * sp.pi / 8))
I3 = 4 * sp.integrate(sp.exp(-2 * s), (s, sp.Rational(1, 2), sp.oo))
report("(e): 4 int_{1/2}^inf e^{-2s} ds = 2/e, so R_3^2 >= (2/e)/(2 log 2) = 1/(e log 2)",
       zero(I3 - 2 * sp.exp(-1)) and zero(I3 / (2 * sp.log(2)) - 1 / (sp.E * sp.log(2))))
# polar reduction ||y g(y)||_m^2 = c_m int |y|^{3-2m} g^2 dy, substitution s = y^2
yv = sp.Symbol('yv', positive=True)
report("(e): s = y^2: 2 int_0^inf y^{-3}(1 - e^{-y^2})^2 dy = int_0^inf s^{-2}(1 - e^{-s})^2 ds = 2 log 2",
       zero(sp.simplify(2 * sp.integrate(yv**-3 * (1 - sp.exp(-yv**2))**2, (yv, 0, sp.oo)) - 2 * sp.log(2))))
# ||h||_3 bound integral
report("(e): int_0^1 r dr + int_1^inf r^{-3} dr = 1",
       zero(sp.integrate(r, (r, 0, 1)) + sp.integrate(r**-3, (r, 1, sp.oo)) - 1))
# leading m -> 2 term: int_{r>=1} a0^2 y^2 r^{-2m} dX = pi a0^2/(2(m-2))
a0s = sp.Symbol('a0')
lead = a0s**2 * sp.pi * sp.integrate(r**(3 - 2 * mm), (r, 1, sp.oo), conds='none')
report("(e): int_{r>=1} a0^2 y^2 r^{-2m} dX = pi a0^2/(2(m-2))", zero(sp.simplify(lead.subs(mm, sp.Rational(5, 2)) - sp.pi * a0s**2 / 1)))

bad = [n_ for n_, ok in results if not ok]
print("%d checks, %d failed" % (len(results), len(bad)))
sys.exit(1 if bad else 0)
