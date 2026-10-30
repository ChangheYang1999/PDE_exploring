# c1-t1 R1-018: exact checks for T4-153 (research/weighted_third_origin/PROOF.md).
# (a) q = 3 boundary values alpha_v = 2 - c, alpha_h = 5c - 4 - a, B = alpha_h - alpha_v, and B <= c - 2 <= 0 under (2);
# (b) the zero profile exp(alpha_v v/(2c - 2)) (1 + e^(2v))^(B/(4c - 4)) solves the conjugated zero equation, with
#     log-slopes alpha_v/d0 at -oo and alpha_h/d0 at +oo;
# (c) scaling exponents of E_eps f = eps^2 f(X/eps) in R^2: hat(E_eps f)(xi) = eps^4 hat f(eps xi), so
#     ||E_eps f||_(dot H^s)^2 = eps^(6 - 2s) ||f||_(dot H^s)^2 and a degree-d homogeneous linear functional scales as
#     eps^(2 - d); exact Gaussian-type example for the unweighted ||D^k E_eps f||_2^2 = eps^(6 - 2k) ||D^k f||_2^2;
# (d) R_eps of (7): L E_eps w - E_eps L0 w = E_eps R_eps for a generic linear-plus-quadratic V and grad rho jet;
# (e) a positive-quadrant imaginary bump gives c[g] = d_y U2[g](0) > 0 (sign of the multiplier).
# Run from artifacts/checks: OMP_NUM_THREADS=1 python3 -B check_T4153.py > check_T4153.out
import sympy as sp

ok = []


def rep(name, cond):
    ok.append(bool(cond))
    print('%-86s %s' % (name, 'OK' if cond else 'FAIL'))


c, a, v, q, eps = sp.symbols('c a v q epsilon', positive=True)
d0 = 2 * c - 2
av = q - c - 1
ah = q * (2 * c - 1) - c - 1 - a
B = 2 * q * (c - 1) - a
rep('(a) q = 3: alpha_v = 2 - c, alpha_h = 5c - 4 - a, B = alpha_h - alpha_v',
    sp.simplify(av.subs(q, 3) - (2 - c)) == 0 and sp.simplify(ah.subs(q, 3) - (5 * c - 4 - a)) == 0 and
    sp.simplify(B.subs(q, 3) - (ah - av).subs(q, 3)) == 0)
rep('(a) at a = 5c - 4: B = c - 2 (and B decreases in a), so B <= c - 2 <= 0 for c <= 2',
    sp.simplify(B.subs(q, 3).subs(a, 5 * c - 4) - (c - 2)) == 0 and sp.diff(B, a) == -1)
p = sp.exp(2 * v) / (1 + sp.exp(2 * v))
phi = sp.exp(av.subs(q, 3) * v / d0) * (1 + sp.exp(2 * v)) ** (B.subs(q, 3) / (4 * c - 4))
rep('(b) -d0 phi\' + (alpha_v + B p) phi = 0 at q = 3',
    sp.simplify((-d0 * sp.diff(phi, v) + (av + B * p).subs(q, 3) * phi) / phi) == 0)
sl = sp.simplify(sp.diff(sp.log(phi), v))
num = {c: sp.Rational(9, 5), a: 10}
rep('(b) log-slopes alpha_v/d0 at -oo, alpha_h/d0 at +oo (c = 9/5, a = 10)',
    sp.limit(sl.subs(num), v, -sp.oo) == (av.subs(q, 3) / d0).subs(num) and
    sp.limit(sl.subs(num), v, sp.oo) == (ah.subs(q, 3) / d0).subs(num))
# (c) power counting on the Fourier side
s_, dd = sp.symbols('s d', real=True)
# int |xi|^(2s) eps^8 |fhat(eps xi)|^2 dxi, substitute eta = eps xi: |xi|^(2s) = eps^(-2s)|eta|^(2s), dxi = eps^-2 deta
expo_norm = 8 - 2 * s_ - 2
rep('(c) ||E_eps f||_(dot H^s)^2 scales as eps^(6 - 2s): s = 3 -> 1, s = -1 -> eps^8, s = k -> eps^(6 - 2k)',
    sp.expand(expo_norm - (6 - 2 * s_)) == 0 and expo_norm.subs(s_, 3) == 0 and expo_norm.subs(s_, -1) == 8)
expo_fun = 4 - 2 - dd
rep('(c) degree-d functional: eps^(2 - d); c[.] has d = 1, so c[E_eps w] = eps c[w]', expo_fun.subs(dd, 1) == 1)
x, y, X, Y = sp.symbols('x y X Y', real=True)
f = y * sp.exp(-x ** 2 - 2 * y ** 2)  # S1: even in x, odd in y
Ef = eps ** 2 * f.subs({x: x / eps, y: y / eps})


def dk2(g, k):
    tot = 0
    for i in range(k + 1):
        tot += sp.binomial(k, i) * sp.integrate(sp.diff(g, x, i, y, k - i) ** 2, (x, -sp.oo, sp.oo), (y, -sp.oo, sp.oo))
    return sp.simplify(tot)


rep('(c) exact example: ||D^k E_eps f||_2^2 = eps^(6 - 2k) ||D^k f||_2^2 for k = 0, 1, 2, 3 (Frobenius count)',
    all(sp.simplify(dk2(Ef, k) - eps ** (6 - 2 * k) * dk2(f, k)) == 0 for k in range(4)))
# (d) R_eps identity for the local (transport + coupling) part: with U homogeneous of degree 0, U[E_eps w] = E_eps U[w]
w = sp.Function('w')(X, Y)
W1, W2 = sp.Function('W1')(X, Y), sp.Function('W2')(X, Y)  # U[w] components
k1, k2, k3, r1, r2, r3 = sp.symbols('k1 k2 k3 r1 r2 r3', real=True)
V1 = lambda X_, Y_: (2 * c - 1) * X_ + k1 * X_ * Y_ ** 2 + k3 * X_ ** 3
V2 = lambda X_, Y_: Y_ + k2 * X_ ** 2 * Y_
rx = lambda X_, Y_: r1 * X_ * Y_
ry = lambda X_, Y_: a + r2 * X_ ** 2 + r3 * Y_ ** 2
# left: L(E_eps w)(eps X, eps Y) / eps^2 with E_eps w(x, y) = eps^2 w(x/eps, y/eps); derivatives d_x = (1/eps) d_X
lhs = (V1(eps * X, eps * Y) * sp.diff(w, X) / eps + V2(eps * X, eps * Y) * sp.diff(w, Y) / eps - w
       + W1 * rx(eps * X, eps * Y) + W2 * ry(eps * X, eps * Y))
L0 = (2 * c - 1) * X * sp.diff(w, X) + Y * sp.diff(w, Y) - w + a * W2   # -a Q w = a U2[w]
Reps = ((V1(eps * X, eps * Y) / eps - (2 * c - 1) * X) * sp.diff(w, X) + (V2(eps * X, eps * Y) / eps - Y) * sp.diff(w, Y)
        + rx(eps * X, eps * Y) * W1 + (ry(eps * X, eps * Y) - a) * W2)
rep('(d) (7): L E_eps w - E_eps L0 w = E_eps R_eps (generic odd/even jet)', sp.simplify(lhs - L0 - Reps) == 0)
rep('(d) R_eps -> 0 pointwise as eps -> 0 (coefficients O(eps |X|^2) and O(eps^2 |X|^2))',
    sp.limit(sp.expand(Reps), eps, 0) == 0)
# (e) sign of c[g]: c[g] = int (i xi_y)(-xi_x^2/|xi|^2) hat g, hat g = i sgn(xi_y) beta >= 0 (real S1 g)
xi1, xi2 = sp.symbols('xi1 xi2', real=True)
integrand = (sp.I * xi2) * (-xi1 ** 2 / (xi1 ** 2 + xi2 ** 2)) * (sp.I * sp.sign(xi2))
rep('(e) multiplier of c[g] against i sgn(xi_y) beta is |xi_y| xi_x^2/|xi|^2 >= 0',
    sp.simplify(integrand - sp.Abs(xi2) * xi1 ** 2 / (xi1 ** 2 + xi2 ** 2)) == 0)
print('all checks', 'PASS' if all(ok) else 'FAIL', '(%d of %d)' % (sum(ok), len(ok)))
