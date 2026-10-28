# Independent auditor replay for topic241 (Gaussian strain-one test direction).
# Written from PROOF.md (1)-(4) and SPEC.md S1.1, S2, S3; does not import or run the verifier's check.py.
# Every field is (polynomial) * exp(-x^2-y^2); strip() returns that polynomial exactly.
import time
import sympy as S
import mpmath as mp

T0 = time.time()
x, y = S.symbols('x y', real=True)
r, th, eps = S.symbols('r theta epsilon', positive=True)
z = S.symbols('z')
E = S.exp(-x**2 - y**2)
out = []
def ok(name, cond):
    out.append((name, bool(cond)))
    print(('PASS ' if cond else 'FAIL ') + name + '   [%.1fs]' % (time.time() - T0), flush=True)
def strip(f, w=x**2 + y**2):
    return S.expand(S.powsimp(S.expand(f * S.exp(w))))

# (1): potential, built from the definitions in PROOF.md
g = -(y**3 / 6) * S.exp(-y**2)
gd = lambda n: S.diff(g, y, n)
a_g = 2*g - gd(2)
b_g = gd(4) - 12*gd(2) + 12*g
W = g + x**2/2*a_g + x**4/24*b_g
v = S.exp(-x**2) * W

# (4): v = exp(-x^2) W; exp(-x^2) = 1 - x^2 + x^4/2 + O(x^6) is exact through x^4
Wp = S.expand(strip(W, y**2))                       # polynomial in x, y
vser = S.expand(Wp * (1 - x**2 + x**4/2))
gp = lambda n: S.expand(strip(gd(n), y**2))
ok('(4): x^0, x^2, x^4 coefficients of v are g, -g\'\'/2, g\'\'\'\'/24',
   S.expand(vser.coeff(x, 0) - gp(0)) == 0 and S.expand(vser.coeff(x, 2) + gp(2)/2) == 0
   and S.expand(vser.coeff(x, 4) - gp(4)/24) == 0)
# x-expansion of Delta v from (4): x^0 coefficient -g''+g'', x^2 coefficient g''''/2-g''''/2
c0 = 2*(-gp(2)/2) + gp(2)
c2 = 12*gp(4)/24 + S.expand(strip(S.diff(-gd(2)/2, y, 2), y**2))
ok('x^0 and x^2 coefficients of Delta v from (4) vanish', S.expand(c0) == 0 and S.expand(c2) == 0)

# (2): polynomial factor of d = -Delta v
d = -(S.diff(v, x, 2) + S.diff(v, y, 2))
Dp = strip(d)
ok('d exp(r^2) is a polynomial with rational coefficients',
   Dp.is_polynomial(x, y) and all(cf.is_Rational for cf in S.Poly(Dp, x, y).coeffs()))
print('d exp(r^2) =', Dp)
qq, rem = S.div(S.Poly(Dp, x, y), S.Poly(x**4*y, x, y))
ok('exact divisibility by x^4 y', rem.is_zero)
P = qq.as_expr()
print('P =', S.factor(P), '; P(0,0) =', P.subs({x: 0, y: 0}))
ok('P has only even powers', all(i % 2 == 0 and j % 2 == 0 for (i, j) in S.Poly(P, x, y).monoms()))
ok('P(0,0) != 0: inner quotient rate exactly r^(1/5)', P.subs({x: 0, y: 0}) != 0)
ok('parity: d even in x, odd in y', S.expand(Dp.subs(x, -x) - Dp) == 0 and S.expand(Dp.subs(y, -y) + Dp) == 0)
ok('d nonzero', Dp != 0)
ok('lowest total degree 5 (d=O(r^5), J[d]=0)', min(i + j for (i, j) in S.Poly(Dp, x, y).monoms()) == 5)

# (3): SPEC S1.1  -Lap psi = d_x rho, U = (-psi_y, psi_x)
psi = S.diff(v, x)
ok('-Delta psi = d_x d', strip(-(S.diff(psi, x, 2) + S.diff(psi, y, 2)) - S.diff(d, x)) == 0)
Pp = strip(psi)
ok('psi odd-odd (SPEC S2.3 canonical class; Schwartz hence o(r^2))',
   S.expand(Pp.subs(x, -x) + Pp) == 0 and S.expand(Pp.subs(y, -y) + Pp) == 0)
U1 = -S.diff(psi, y); U2 = S.diff(psi, x)
ok('U = (-v_xy, v_xx)', strip(U1 + S.diff(v, x, y)) == 0 and strip(U2 - S.diff(v, x, 2)) == 0)
ok('div U = 0', strip(S.diff(U1, x) + S.diff(U2, y)) == 0)
cp = S.diff(psi, x, y).subs({x: 0, y: 0}); c2_ = S.diff(U2, y).subs({x: 0, y: 0}); c1_ = -S.diff(U1, x).subs({x: 0, y: 0})
print('psi_xy(0), d_yU2(0), -d_xU1(0) =', cp, c2_, c1_)
ok('c[d] = 1 in SPEC S3.1 convention (all three forms)', cp == 1 and c2_ == 1 and c1_ == 1)

# Kernel formula SPEC S3.2, exact: angular integral via constant Laurent coefficient, radial via sympy
cs = (z + 1/z)/2; sn = (z - 1/z)/(2*S.I); s3 = (z**3 - z**-3)/(2*S.I)
cker = 0
for (i, j), cf in S.Poly(Dp, x, y).terms():
    lau = S.expand(s3 * cs**i * sn**j * z**40)
    ang = 2*S.pi*S.Poly(lau, z).coeff_monomial(z**40)
    rad = S.integrate(r**(i + j - 2) * S.exp(-r**2), (r, 0, S.oo))
    cker += cf * ang * rad
cker = S.simplify(cker / S.pi)
print('kernel strain (exact) =', cker)
ok('kernel strain (1/pi) int sin(3theta) r^-3 d dX = 1', cker == 1)
fd = S.lambdify((r, th), S.sin(3*th) * r**-2 * (Dp.subs({x: r*S.cos(th), y: r*S.sin(th)})) * S.exp(-r**2), 'mpmath')
mp.mp.dps = 16
num = mp.quad(fd, [0, 1.5, 4, 9], [0, mp.pi, 2*mp.pi]) / mp.pi
print('kernel strain (quadrature) =', num)
ok('quadrature within 1e-12 of 1', abs(num - 1) < 1e-12)

# Origin Taylor of U: polynomial part times exp(-r^2) truncated through degree 4
expt = 1 - (x**2 + y**2) + (x**2 + y**2)**2/2
def jet(f, n=5):
    s = S.expand((strip(f) * expt).subs({x: eps*x, y: eps*y}))
    return [S.expand(s.coeff(eps, m)) for m in range(n)]
j1 = jet(U1); j2 = jet(U2)
print('U1 degrees 0..4:', j1); print('U2 degrees 0..4:', j2)
ok('U[d] = (-x, y) + O(r^3)', j1[:3] == [0, -x, 0] and j2[:3] == [0, y, 0])
# cubic cancellation with rho0 = x^2 y + O(r^5), H0 = x^2 y + O(r^5), c[d] = 1
canc = U1*2*x*y + U2*x**2 + cp*x**2*y*E          # c H0 jet: x^2 y exp(-r^2) has same jet through deg 4 as x^2 y
jc = jet(canc)
print('U.grad(x^2y)+c x^2y, degrees 0..4:', jc)
ok('cubic part of U[d].grad rho0 is -x^2 y and cancels c[d]H0 (degree<=4 part zero)',
   all(t == 0 for t in jc) and S.expand(j1[1]*2*x*y + j2[1]*x**2 + x**2*y) == 0)

# Generic tangent field V1 = x A, V2 = B (A, B arbitrary): V.grad(x^4 y Q) - x^4 y Q
A = S.Function('A')(x, y); B = S.Function('B')(x, y); Q = S.Function('Q')(x, y)
dd = x**4*y*Q
Td = S.expand(x*A*S.diff(dd, x) + B*S.diff(dd, y) - dd)
def xpow(tm):
    e = 0
    for f in S.Mul.make_args(tm):
        if f == x: e += 1
        elif f.is_Pow and f.base == x: e += f.exp
    return e
ok('generic transport image keeps the factor x^4', all(xpow(tm) >= 4 for tm in S.Add.make_args(Td)))
ok('generic transport cofactor /(x^2 y) vanishes on x=0', S.expand(Td/(x**2*y)).subs(x, 0) == 0)

# Inner cylinder quotients: b = r^(24/5), p = cos^2 sin
pol = {x: r*S.cos(th), y: r*S.sin(th)}
Dpol = S.expand(Dp.subs(pol))
lead = S.expand(Dpol / r**5).subs(r, 0)
print('d/(r^5 e^{-r^2}) at r=0:', S.factor(lead))
cofq = S.expand(P.subs(pol) * r**2 * S.cos(th)**2)       # = d/(x^2 y) * e^{r^2}
ok('d/(b p) = r^(1/5) cos^2(theta) P e^{-r^2}: identity and zero vertical trace',
   S.expand(cofq * r**3 * S.cos(th)**2 * S.sin(th) - Dpol) == 0 and cofq.subs(th, S.pi/2) == 0 and cofq.subs(th, 3*S.pi/2) == 0)
t = S.symbols('t', real=True)
ok('e^{t/5} is L2 on (-oo,-1]', S.integrate(S.exp(2*t/5), (t, -S.oo, -1)).is_finite)

print('SUMMARY:', 'ALL PASS' if all(c for _, c in out) else 'SOME FAIL', len(out), 'checks, %.1fs' % (time.time() - T0))
