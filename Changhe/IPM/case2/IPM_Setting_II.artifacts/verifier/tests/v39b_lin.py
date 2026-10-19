"""V39b (referee result 12 results/02-linearization): operator (L), Laplacian identity (P), 1D kernel, Fourier form (F),
polynomial (analytic) kernel. Prints PASS/FAIL. Run: OMP_NUM_THREADS=1 python3 tests/v39b_lin.py"""
import itertools
import sympy as sp

x = sp.symbols('x', positive=True)          # work on the side x > 0, f = x^g
y, eps, a, k = sp.symbols('y epsilon a k', real=True)
g = sp.symbols('gamma', positive=True)
res = []


def chk(name, expr):
    e = sp.simplify(expr)
    ok = (e == 0)
    res.append(ok)
    print(('PASS' if ok else 'FAIL'), name, '' if ok else e)


h = sp.Function('h')(x, y)
tau = sp.Function('tau')(x, y)     # T(f'h) = first component of the velocity of the density perturbation
sig = sp.Function('sigma')(x, y)   # second component (enters only at second order)
f = x**g
fp = sp.diff(f, x)

# (a) first-order expansion of V.grad xi - xi/g with xi = x + eps h, l = 1/g + eps a, W = (0,-f) + eps (tau, sig)
xi = x + eps*h
lv = 1/g + eps*a
V1 = lv*x + eps*tau
V2 = lv*y - f + eps*sig
F = V1*sp.diff(xi, x) + V2*sp.diff(xi, y) - xi/g
F0 = F.subs(eps, 0)
F1 = sp.diff(F, eps).subs(eps, 0)
L = (x*sp.diff(h, x) + y*sp.diff(h, y) - h)/g - f*sp.diff(h, y) + tau + a*x
chk('(L): zeroth order vanishes (shear is a gamma-profile)', F0)
chk('(L): first order equals L_gamma h + T(f\'h) + a x', F1 - L)
# density perturbation is f'(x) h: d/deps |x + eps h|^g at eps = 0 (x > 0 side)
chk('(L): d/deps (x+eps h)^g = f\' h', sp.diff((x + eps*h)**g, eps).subs(eps, 0) - fp*h)

# (b) tilted-shear direction h = y: T(f' y) is the eps-derivative of W1 of the tilted shear |x + eps y|^g
tt = sp.symbols('t', real=True)
W1tilt = tt/(1 + tt**2)*(x + tt*y)**g            # W1 = (a1 a2/|a|^2) f(s), a = (1, t)
Tfy = sp.diff(W1tilt, tt).subs(tt, 0)
chk('(b) T(f\'y) = |x|^g from the tilted family', Tfy - f)
Lb = (x*0 + y*1 - y)/g - f*1 + Tfy
chk('(b) h = y, a = 0 solves (L) (unnormalized direction)', Lb)

# (c) Laplacian of (L) on x > 0 with Lap tau = (f'h)_xy gives (P)
lap = lambda u: sp.diff(u, x, 2) + sp.diff(u, y, 2)
z = lap(h)
LapL = lap((x*sp.diff(h, x) + y*sp.diff(h, y) - h)/g - f*sp.diff(h, y)) + sp.diff(fp*h, x, y)
P = (x*sp.diff(z, x) + y*sp.diff(z, y) + z)/g - f*sp.diff(z, y) - fp*sp.diff(h, x, y)
chk('(c) Lap(L) = (P) (a x and harmonic residual removed)', sp.expand(LapL - P))
chk('(c) Lap((X.grad - 1)h) = (X.grad + 1) Lap h', sp.expand(lap(x*sp.diff(h, x) + y*sp.diff(h, y) - h)
                                                          - (x*sp.diff(z, x) + y*sp.diff(z, y) + z)))
# Lap W1 = rho_xy: W1 = -psi_y, -Lap psi = rho_x gives Lap W1 = d_y(-Lap psi) = rho_xy (by hand)

# (d) trace step: with h_xy(0,y) = 0, Taylor h_xy = x h_xxy(0,y) + ..., f'h_xy/x^g -> g h_xxy(0,y)
H3 = sp.Function('H3')(y)
hxy_model = x*H3 + x**2*sp.Function('H4')(y)
chk('(d) f\' h_xy / x^g -> g h_xxy(0,y)', sp.limit(sp.simplify(fp*hxy_model/x**g), x, 0) - g*H3)
# limit equation y Z' + Z = 0  =>  Z = C/y on each half line; continuity at 0 => C = 0
Z = sp.Function('Z')
solZ = sp.dsolve(sp.Eq(y*Z(y).diff(y) + Z(y), 0), Z(y))
chk('(d) y Z\' + Z = 0 has solution C/y only', solZ.rhs.subs(sp.Symbol('C1'), 1) - 1/y)
# H'' = -A, H(0) = H'(0) = 0 => H = -A y^2/2
A = sp.symbols('A', real=True)
Hf = sp.Function('Hf')
solH = sp.dsolve(sp.Eq(Hf(y).diff(y, 2), -A), Hf(y), ics={Hf(0): 0, Hf(y).diff(y).subs(y, 0): 0})
chk('(d) H\'\' = -A, H(0)=H\'(0)=0 gives H = -A y^2/2', solH.rhs + A*y**2/2)

# (e) 1D sector: x h' - h = -g a x  => h = x (C - g a log x)
C = sp.symbols('C', real=True)
h1 = x*(C - g*a*sp.log(x))
chk('(e) x h\' - h = -g a x for h = x(C - g a log|x|)', x*sp.diff(h1, x) - h1 + g*a*x)
hh = sp.Function('hh')
sol1 = sp.dsolve(sp.Eq(x*hh(x).diff(x) - hh(x), -g*a*x), hh(x))
print('INFO 1D kernel ODE general solution:', sol1)
chk('(e) h1\' = C - g a - g a log x', sp.diff(h1, x) - (C - g*a - g*a*sp.log(x)))
for av in (1, -1):
    lv0 = sp.limit(sp.diff(h1, x).subs({a: av, g: sp.Rational(1, 2), C: 0}), x, 0, '+')
    ok = lv0 in (sp.oo, -sp.oo)
    res.append(ok)
    print(('PASS' if ok else 'FAIL'), f'(e) a = {av}: lim_(x->0+) h1\'(x) = {lv0} (not C^1, so a = 0)')

# (f) Fourier in y: F[y h_y](k) = -(1 + k d_k) F[h](k), checked on h = exp(-(y-1)^2) (x frozen)
hy = sp.exp(-(y - 1)**2)
FT = lambda u: sp.integrate(sp.exp(-sp.I*k*y)*u, (y, -sp.oo, sp.oo))
Fh = sp.simplify(FT(hy))
lhs = sp.simplify(FT(y*sp.diff(hy, y)))
chk('(f) F[y h_y] = -(1 + k d_k) F[h]', sp.simplify(lhs + Fh + k*sp.diff(Fh, k)))
chk('(f) F[h_y] = i k F[h]', sp.simplify(FT(sp.diff(hy, y)) - sp.I*k*Fh))
# Green kernel: T^ = (ik/2) int sgn(x-z) e^{-|k||x-z|} q(z) dz satisfies (d_x^2 - k^2) T^ = i k q'(x)
kk = sp.symbols('kk', positive=True)  # |k|
xs, zz = sp.symbols('xs zz', real=True)
q = sp.Function('q')
Im = sp.Integral(sp.exp(-kk*(xs - zz))*q(zz), (zz, -sp.oo, xs))
Ip = sp.Integral(sp.exp(-kk*(zz - xs))*q(zz), (zz, xs, sp.oo))
That = sp.I*k/2*(Im - Ip)
expr = sp.diff(That, xs, 2) - kk**2*That - sp.I*k*sp.diff(q(xs), xs)
expr = sp.simplify(sp.expand(expr.doit()))
chk('(f) (d_x^2 - k^2) T^ = i k q\' (Green kernel of (F))', expr)

# (g) analytic class: generic polynomial h of degree <= 8 with h(0)=0, Dh(0)=0; (P) on x>0 splits into
#     integer-power part (X.grad + 1) z = 0 and x^(g-1) part  x z_y + g h_xy = 0
N = 8
cs = {}
hp = 0
for i, j in itertools.product(range(N + 1), repeat=2):
    if 2 <= i + j <= N:
        cs[(i, j)] = sp.Symbol(f'c{i}_{j}')
        hp += cs[(i, j)]*x**i*y**j
zp = lap(hp)
eq1 = sp.expand(x*sp.diff(zp, x) + y*sp.diff(zp, y) + zp)
eq2 = sp.expand(x*sp.diff(zp, y) + g*sp.diff(hp, x, y))
eqs = sp.Poly(eq1, x, y).coeffs() + sp.Poly(eq2, x, y).coeffs()
solc = sp.solve(eqs, list(cs.values()), dict=True)
hsol = sp.expand(hp.subs(solc[0]))
free = sorted(hsol.free_symbols - {x, y, g}, key=str)
print('INFO polynomial solutions of the two split equations:', hsol, ' free:', free)
ok = (len(free) == 1) and sp.simplify(hsol - free[0]*(x**2 - y**2)) == 0
res.append(ok)
print(('PASS' if ok else 'FAIL'), '(g) split system forces h = A (x^2 - y^2); trace h(0,y)=0 then gives A = 0')
print(f'SUMMARY {sum(res)}/{len(res)} PASS')
