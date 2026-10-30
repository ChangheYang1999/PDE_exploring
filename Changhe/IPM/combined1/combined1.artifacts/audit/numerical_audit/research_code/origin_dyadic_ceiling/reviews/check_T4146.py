# c1-t1 R1-017: checks for T4-145 (origin_spectral_line) and T4-146 (origin_dyadic_inverse) with APPLICATION_007.
# Part 1 (exact, sympy): the log-frequency conjugation (9) of T4-145, the interior profile phi_sigma, |symbol U|^2 = p,
#   the origin derivative (L h)_y(0) = a0 c[h] for a generic S1 jet, and the critical point equation of H(d).
# Part 2 (mpmath interval, 300 digits): s_star, H(c - 1), H(c - 1) < 57/50, and the seven 007 cell ratios
#   5^((l-2)/2) N13(e) / (H (1 + c - c l)/(1 + l)) from the stored mode norms (data/T4127_combined_cover.json, the
#   T4-127 data CONFIRMED by N4-113), with the exact H and with the T4 bound 57/50.
# Run from artifacts/checks: OMP_NUM_THREADS=1 python3 -B check_T4146.py > check_T4146.out
import json, hashlib, re
import sympy as sp
from mpmath import mp, iv, mpf

ok = []


def rep(name, cond):
    ok.append(bool(cond))
    print('%-78s %s' % (name, 'OK' if cond else 'FAIL'))


# ---- Part 1 ----
u, v, q, c, a0, sig, tau = sp.symbols('u v q c a0 sigma tau', real=True)
d0 = 2 * c - 2
p = sp.exp(2 * v) / (1 + sp.exp(2 * v))
omega = 2 * sp.exp((q + 1) * u + v / 2) * (1 + sp.exp(2 * v)) ** (q / 2)
g = sp.Function('g')(u, v)
w_hat = g / omega
# Fourier side of L0: -(D xi).grad_xi w_hat - (2c + 1) w_hat - a0 p w_hat, with (D xi).grad_xi = d_u + d0 d_v
L0w = -(sp.diff(w_hat, u) + d0 * sp.diff(w_hat, v)) - (2 * c + 1) * w_hat - a0 * p * w_hat
conj = sp.simplify(sp.expand(omega * L0w))
alpha_v = q - c - 1
B = 2 * q * (c - 1) - a0
target = -sp.diff(g, u) - d0 * sp.diff(g, v) + (alpha_v + B * p) * g
rep('T4-145 (9): W L0 W^-1 g = -g_u - d0 g_v + (alpha_v + B p(v)) g', sp.simplify(conj - target) == 0)
# (D xi).grad_xi in log coordinates: xi_y = e^u, xi_x = e^(u+v)
X1, X2 = sp.symbols('xi_x xi_y', positive=True)
F = sp.Function('F')
expr = (2 * c - 1) * X1 * sp.diff(F(sp.log(X2), sp.log(X1 / X2)), X1) + X2 * sp.diff(F(sp.log(X2), sp.log(X1 / X2)), X2)
U_, V_ = sp.symbols('U_ V_')
expr2 = sp.simplify(expr.doit())
uu, vv = sp.log(X2), sp.log(X1 / X2)
chk = sp.simplify(expr2 - (sp.Subs(sp.Derivative(F(U_, V_), U_), (U_, V_), (uu, vv))
                           + d0 * sp.Subs(sp.Derivative(F(U_, V_), V_), (U_, V_), (uu, vv))).doit())
rep('(D xi).grad_xi = d_u + (2c - 2) d_v in u = log xi_y, v = log(xi_x/xi_y)', chk == 0)
# Jacobian and weight of the unitary map (8)
J = sp.Matrix([[sp.exp(u + v), sp.exp(u + v)], [sp.exp(u), 0]]).det()
# |xi|^2 = exp(2u)(1 + exp(2v)) with both factors positive, so |xi|^(2q) = exp(2qu)(1 + exp(2v))^q
rep('|Jacobian| = exp(2u + v); |xi|^2 = exp(2u)(1 + exp(2v))',
    sp.simplify(J + sp.exp(2 * u + v)) == 0 and
    sp.simplify(sp.exp(2 * (u + v)) + sp.exp(2 * u) - sp.exp(2 * u) * (1 + sp.exp(2 * v))) == 0)
rep('4 |xi|^(2q) Jacobian = omega^2 (factor 2 for four quadrants)',
    sp.simplify(4 * sp.exp(2 * q * u) * (1 + sp.exp(2 * v)) ** q * sp.exp(2 * u + v) - omega ** 2) == 0)
phi = sp.exp((alpha_v - sig) * v / d0) * (1 + sp.exp(2 * v)) ** (B / (2 * d0))
rep('T4-145 (11): -d0 phi\' + (alpha_v + B p) phi = sigma phi',
    sp.simplify((-d0 * sp.diff(phi, v) + (alpha_v + B * p) * phi - sig * phi) / phi) == 0)
rep('phi rates: (alpha_v - sigma)/d0 at -oo and (alpha_v + B - sigma)/d0 at +oo',
    sp.simplify(sp.limit(sp.diff(sp.log(phi), v).subs({q: 3, c: sp.Rational(3, 2), a0: 7, sig: -1}), v, -sp.oo)
                - ((alpha_v - sig) / d0).subs({q: 3, c: sp.Rational(3, 2), a0: 7, sig: -1})) == 0 and
    sp.simplify(sp.limit(sp.diff(sp.log(phi), v).subs({q: 3, c: sp.Rational(3, 2), a0: 7, sig: -1}), v, sp.oo)
                - ((alpha_v + B - sig) / d0).subs({q: 3, c: sp.Rational(3, 2), a0: 7, sig: -1})) == 0)
# |symbol of U|^2 = p: U = (-R1 R2, R1^2), R_j -> i xi_j/|xi|
x1, x2 = sp.symbols('x1 x2', real=True)
n2 = x1 ** 2 + x2 ** 2
s1 = -(sp.I * x1) * (sp.I * x2) / n2
s2 = (sp.I * x1) ** 2 / n2
rep('T4-146 (7): |symbol U|^2 = xi_x^2/|xi|^2 in [0, 1]', sp.simplify(sp.Abs(s1) ** 2 + sp.Abs(s2) ** 2 - x1 ** 2 / n2) == 0)
# (L h)_y(0) = a0 c[h] for S1 jets: V = (V1, V2) with V(0) = 0, DV(0) = diag(2c-1, 1); h, U2 odd in y, U1 odd in x.
X, Yv = sp.symbols('X Y', real=True)
hy, h3, h4, u2y, rxy, ryy, k1, k2 = sp.symbols('h_y h3 h4 u2y rxy ryy k1 k2', real=True)
h = hy * Yv + h3 * X ** 2 * Yv + h4 * Yv ** 3                      # S1 jet: even in X, odd in Y
U1 = sp.Symbol('m1') * X                                            # U1 odd in X, even in Y: linear part m1 X
U2 = u2y * Yv                                                       # U2 even in X, odd in Y: linear part c[h] Y
V1 = (2 * c - 1) * X + k1 * X * Yv ** 2                             # S1-compatible, DV(0) = diag(2c - 1, 1)
V2 = Yv + k2 * X ** 2 * Yv
rho_x = rxy * X * Yv                                                # rho_x odd-odd, rho_y even-even with rho_y(0) = a0
rho_y = a0 + ryy * X ** 2
Lh = V1 * sp.diff(h, X) + V2 * sp.diff(h, Yv) - h + U1 * rho_x + U2 * rho_y
rep('T4-146 (16): (L h)_y(0) = a0 c[h] with c[h] = d_y U2[h](0)',
    sp.simplify(sp.diff(Lh, Yv).subs({X: 0, Yv: 0}) - a0 * u2y) == 0)
# H(d): d/ds [(d - s)^2 s (1 + s)] = (d - s)(-4 s^2 + (2d - 3) s + d)
s, dd = sp.symbols('s d', positive=True)
rep('T4-146 (19): critical point polynomial of (d - s)^2 s(1 + s)',
    sp.expand(sp.diff((dd - s) ** 2 * s * (1 + s), s) - (dd - s) * (-4 * s ** 2 + (2 * dd - 3) * s + dd)) == 0)
rep('ceiling slope: d/da (1 + c - c a)/(1 + a) = -(1 + 2c)/(1 + a)^2',
    sp.simplify(sp.diff((1 + c - c * sp.Symbol('a')) / (1 + sp.Symbol('a')), sp.Symbol('a'))
                + (1 + 2 * c) / (1 + sp.Symbol('a')) ** 2) == 0)

# ---- Part 2 ----
mp.dps = 300
iv.dps = 300
C = iv.mpf(4076476460239181) / iv.mpf(2) ** 51
D = C - 1
sq = iv.sqrt((2 * D - 3) ** 2 + 16 * D)
sstar = (2 * D - 3 + sq) / 8
H = (D - sstar) * iv.sqrt(4 * iv.pi * sstar * (1 + sstar))
print('s_star in [%s, %s]' % (mp.nstr(mpf(sstar.a), 25), mp.nstr(mpf(sstar.b), 25)))
print('H(c - 1) in [%s, %s]' % (mp.nstr(mpf(H.a), 25), mp.nstr(mpf(H.b), 25)))
rep('s_star in (0, c - 1) and quadratic changes sign on (0, c - 1) (unique interior maximum)',
    sstar.a > 0 and sstar.b < D.a and D.a > 0 and (-2 * D * D - 2 * D).b < 0)
rep('H(c - 1) < 57/50 (outward)', H.b < iv.mpf(57) / 50)
# grid sanity check of the maximum (FLOAT)
dm = mpf(4076476460239181) / mpf(2) ** 51 - 1
grid = max(((dm - t) * mp.sqrt(4 * mp.pi * t * (1 + t)) for t in [dm * k / 20000 for k in range(1, 20000)]))
rep('grid maximum of (d - s) sqrt(4 pi s(1 + s)) below the formula value', grid <= mpf(H.b))
print('grid maximum (FLOAT) %s' % mp.nstr(grid, 15))
PATH = 'data/T4127_combined_cover.json'
raw = open(PATH, 'rb').read()
print('input %s sha256 %s' % (PATH, hashlib.sha256(raw).hexdigest()))
dat = json.loads(raw)


def ball(sx):
    m = re.match(r'\[([0-9.eE+-]+) \+/- ([0-9.eE+-]+)\]', sx)
    mid, rad = iv.mpf(m.group(1)), iv.mpf(m.group(2))
    return iv.mpf([mpf((mid - rad).a), mpf((mid + rad).b)])


fr = lambda t: sp.Rational(t)
N13 = {fr(r['a']): ball(r['modes_1_3_norm']) for r in dat['rows']}
A = sp.Rational(6328276273924429, 4076476460239181)
rep('A = 1 + 1/c exactly and A < 7/4', A == 1 + 1 / (sp.Rational(4076476460239181, 2 ** 51)) and A < sp.Rational(7, 4))
cells = [(0, sp.Rational(1, 4), sp.Rational(1, 4)), (sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(1, 2)),
         (sp.Rational(1, 2), sp.Rational(3, 4), sp.Rational(3, 4)), (sp.Rational(3, 4), 1, 1),
         (1, sp.Rational(5, 4), sp.Rational(5, 4)), (sp.Rational(5, 4), sp.Rational(3, 2), sp.Rational(3, 2)),
         (sp.Rational(3, 2), A, sp.Rational(7, 4))]
q2 = lambda r: iv.mpf(int(sp.Rational(r).p)) / iv.mpf(int(sp.Rational(r).q))
mins = []
print('cell [l, h], e: ratio with exact H (outward lower end), ratio with 57/50, old ratio with B(l) (sqrt(8 pi) beta^2/(1+l))')
for (l, hgh, e) in cells:
    L5 = iv.mpf(5) ** ((q2(l) - 2) / 2)
    lhs = L5 * N13[sp.Rational(e)]
    beta = 1 + C - C * q2(l)
    rH = lhs / (H * beta / (1 + q2(l)))
    r57 = lhs / ((iv.mpf(57) / 50) * beta / (1 + q2(l)))
    rB = lhs / (iv.sqrt(8 * iv.pi) * beta ** 2 / (1 + q2(l)))
    mins.append(mpf(rH.a))
    print('  [%s, %s], e = %s: %s  %s  %s' % (l, hgh if hgh != A else 'A', e, mp.nstr(mpf(rH.a), 15),
                                            mp.nstr(mpf(r57.a), 15), mp.nstr(mpf(rB.a), 6)))
    rep('    cell [%s, %s] fails the ceiling (ratio > 1, outward)' % (l, hgh if hgh != A else 'A'), rH.a > 1 and r57.a > 1)
print('minimum ratio (exact H) %s' % mp.nstr(min(mins), 15))
print('all checks', 'PASS' if all(ok) else 'FAIL', '(%d of %d)' % (sum(ok), len(ok)))
