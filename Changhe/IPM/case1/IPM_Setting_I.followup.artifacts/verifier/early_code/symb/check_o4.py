"""verifier: lead request (o4) items 1-3, symbolic checks.
1. Pair 6.3.1 (c) at A = 2: g* = g(P), w''(P), compatibility, and the A = 2 formula B_3 = Q(x*)/6 = w''(P)(g* - 2)/(24 g*^3)
   (g'(x*) = w''(x*) g*/A from w g' = (w' - A) g).
2. Family of 6.3.1 (g): lambda = (d-1)/(A-1), k = 2b - 2 - A lambda; ranges, and the example A = 2.1, g* = 4.3, d = 2.5.
3. A = 4 (beta = 1/2): w = w_R12(L=4) + e x^(7+beta); first order in e, leading term of delta Q at 0 and in the variable m."""
import sympy as sp
x, t, e = sp.symbols('x t e', positive=True)
# 1
A = 2; k = sp.sqrt(sp.Rational(2, A)); cl = sp.Rational(A + 1, 2)
w = -(A/k)*sp.sin(k*x); g = A*(1 - sp.cos(k*x)); P = sp.pi/k
print('1. A=2 pair: compat residual', sp.simplify(w*sp.diff(g, x) - (sp.diff(w, x) - A)*g), ' P =', P,
      ' g* =', g.subs(x, P), ' w\'\'(P) =', sp.diff(w, x, 2).subs(x, P), " w'(P) =", sp.diff(w, x).subs(x, P),
      ' Q(P) =', sp.simplify(((sp.diff(g, x) - sp.diff(w, x, 2))/(2*g**3)).subs(x, P)))
Ag, W2, gs = sp.symbols('A w2 g_s', positive=True)
gp = W2*gs/Ag                       # g'(x*) by l'Hopital in g' = (w' - A) g / w
Qs = (gp - W2)/(2*gs**3)
print('   B_3 = Q*/6 at A=2 minus w\'\'(g*-2)/(24 g*^3):', sp.simplify((Qs/6).subs(Ag, 2) - W2*(gs - 2)/(24*gs**3)))
# 2
Aa, gg, d = sp.symbols('A g d', positive=True)
b = gg/(2*(Aa - 1)); lam = (d - 1)/(Aa - 1); kk = 2*b - 2 - Aa*lam
print('2. k + 1 =', sp.factor(sp.simplify(kk + 1)), ';  1 - lambda =', sp.factor(1 - lam))
for (Av, gv, dv) in [(sp.Rational(21, 10), sp.Rational(43, 10), sp.Rational(5, 2)), (sp.Rational('10.150725'), sp.Rational('29.74949'), sp.Rational(5, 2))]:
    print('   A=%s g*=%s d=%s: (1+g*)/A = %s, lambda = %s, k = %s' % (Av, gv, dv, sp.N((1 + gv)/Av, 6), sp.N(lam.subs({Aa: Av, d: dv}), 6), sp.N(kk.subs({Aa: Av, gg: gv, d: dv}), 6)))
# 3  x = t^2, beta = 1/2, A = 4, L = 4
A = 4; be = sp.Rational(1, 2); N = 22
wR = -A*x*(1 - x**2/16)/(1 + x**2/16)
wt = (wR + e*x**(7 + be)).subs(x, t**2)
z = sp.expand(sp.series(-wt/(A*t**2), t, 0, N).removeO())
# E(x) = int_0^x (1/z - 1)/x dx = int_0^t (1/z - 1) * 2/t dt
integ = sp.expand(sp.series((1/z - 1)*2/t, t, 0, N).removeO())
integ = sp.expand(integ.subs(e**2, 0))
E = sp.integrate(integ, t)
gt = sp.expand(sp.series(t**4*z*sp.exp(E), t, 0, N + 4).removeO())
gt = sp.expand(sum(gt.coeff(e, j)*e**j for j in (0, 1)))
dx = lambda f: sp.diff(f, t)/(2*t)
Q = (dx(gt) - dx(dx(wt)))/(2*gt**3)
Qs = sp.expand(sp.series(Q, t, 0, 6).removeO())
dQ = sp.expand(Qs.coeff(e, 1))
print('3. delta Q / e, leading terms in t = sqrt(x):', sp.series(dQ, t, 0, 4))
print('   predicted -(7+beta)(6+beta)/2 x^(beta-1) =', -(7 + be)*(6 + be)/2, '* t^-1')
