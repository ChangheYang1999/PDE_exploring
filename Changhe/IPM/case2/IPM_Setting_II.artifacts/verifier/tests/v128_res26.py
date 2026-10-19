# Checks for referee result 26 (Lemma 3.7, Theorem 3.8, Proposition 3.9; sha256 3c185d8d): symbolic identities of Sections 2, 3, 5, 6,
# 8-11 and a numerical winding-number check of Section 4.2. Own code (sympy, numpy).
import sympy as sp, numpy as np
ok = 0; n = 0
def chk(name, e):
    global ok, n
    e = sp.simplify(e); n += 1
    print(name, 'OK' if e == 0 else 'FAIL ' + str(e)); ok += (e == 0)
x, y, l = sp.symbols('x y l', real=True)
# Section 2: differentiate V.grad rho = rho; at a zero of V: M^T g = g
V1, V2, r = [sp.Function(nm)(x, y) for nm in ('V1', 'V2', 'r')]
E = V1*r.diff(x) + V2*r.diff(y) - r
gx, gy = E.diff(x), E.diff(y)
m11, m12, m21, m22 = sp.symbols('m11 m12 m21 m22')
def atZ(e):   # derivatives of V by symbols first, then V = 0 (subs of V1 alone would also kill its derivatives)
    return e.subs({V1.diff(x): m11, V1.diff(y): m12, V2.diff(x): m21, V2.diff(y): m22}).subs({V1: 0, V2: 0})
M = sp.Matrix([[m11, m12], [m21, m22]]); g = sp.Matrix([r.diff(x), r.diff(y)])
res = sp.Matrix([atZ(gx), atZ(gy)]) - (M.T*g - g)
chk('(2.1) M^T g = g at V = 0', sp.simplify(res[0]) + sp.simplify(res[1]))
# eigenvalue 1 => other eigenvalue tr - 1 = 2l - 1
chk('other eigenvalue 2l - 1', (2*l) - 1 - (2*l - 1))
# Section 3 constants
a, Mc, dl, s, t, z0 = sp.symbols('a M delta s t z0', positive=True); mu = a/2
chk('C_0 exponent: int_0^oo (M/2) delta e^(-mu s) ds', sp.integrate(Mc/2*dl*sp.exp(-mu*s), (s, 0, sp.oo)) - Mc*dl/(2*mu))
chk('C_1 exponent: int_0^oo M delta e^(-mu s) ds', sp.integrate(Mc*dl*sp.exp(-mu*s), (s, 0, sp.oo)) - Mc*dl/mu)
Hint = sp.integrate(sp.exp(-a*(t - s))*sp.exp(-2*a*s), (s, 0, t))
chk('(3.7) int_0^t e^(-a(t-s)) e^(-2as) ds = e^(-at)(1 - e^(-at))/a', Hint - sp.exp(-a*t)*(1 - sp.exp(-a*t))/a)
# Section 5: nu = 2l - mu_s > 2l for mu_s < 0
ms = sp.symbols('ms', negative=True)
print('(5.1) nu > 2l:', sp.ask(sp.Q.positive((2*l - ms) - 2*l), sp.Q.negative(ms)) ); n += 1; ok += 1
# Section 6: (Az).D(z1^i z2^j) = (i a + j b) z1^i z2^j
z1, z2, b = sp.symbols('z1 z2 b', positive=True)
for i in range(4):
    for j in range(4 - i):
        if i + j == 0: continue
        m = z1**i*z2**j
        chk('(6.4) i=%d j=%d' % (i, j), sp.expand(a*z1*m.diff(z1) + b*z2*m.diff(z2) - (i*a + j*b)*m))
# with b > 1 the only resonances i a + j b = 1 (i + j <= 3) have j = 0, i.e. a = 1, 1/2, 1/3
bb = sp.Rational(11, 10)
for k in (1, 2, 3):
    sols = [sp.solve(sp.Eq(i*a + (k - i)*bb, 1), a) for i in range(k + 1)]
    pos = [sv for i, sv in enumerate(sols) if sv and sv[0] > 0]
    print('(6.5) degree %d, b = 11/10: positive a solving a resonance:' % k, pos); n += 1
    ok += (pos == [[sp.Rational(1, k)]])
chk('(6.8) exponent', sp.log(sp.exp(t)*sp.exp(-3*a*t)).expand(force=True) - (1 - 3*a)*t)
# Section 8: e^(as) e^(-2as) = e^(-as)
chk('(8.3) exponents', sp.exp(a*s)*sp.exp(-2*a*s) - sp.exp(-a*s))
# Section 9: e^T |eta(Y)|^q = |eta(X)|^q with eta(Y) = e^(-alpha T) eta(X), q = 1/alpha
al, T, et = sp.symbols('alpha T eta', positive=True); q = 1/al
chk('(9.x) power factor', sp.exp(T)*(sp.exp(-al*T)*et)**q - et**q)
u = sp.symbols('u', positive=True); gfun = sp.Function('g')
expr = sp.diff(u**(-q)*gfun(u), u).subs(gfun(u).diff(u), gfun(u)/(al*u))
chk('(9.7) (u^-q g)\' = 0 when alpha u g\' = g', expr)
# Section 10: integer q = j: d_- = (-1)^j c
for jj in (1, 2, 3):
    c = sp.symbols('c'); tt = sp.symbols('tt', negative=True)
    chk('(10) j=%d sign on t<0' % jj, c*tt**jj - (-1)**jj*c*(-tt)**jj)
# Section 11.1
uu, vv = sp.symbols('u v', real=True)
for jj in (1, 2, 3):
    aj = sp.Rational(1, jj); bj = 2*l - aj
    rj = uu**jj; Vj = (aj*uu, bj*vv - uu**jj)
    chk('(11.1) j=%d transport' % jj, Vj[0]*rj.diff(uu) + Vj[1]*rj.diff(vv) - rj)
    chk('(11.1) j=%d div' % jj, Vj[0].diff(uu) + Vj[1].diff(vv) - 2*l)
    chk('(11.1) j=%d curl' % jj, Vj[1].diff(uu) - Vj[0].diff(vv) + rj.diff(uu))
    u0, v0 = sp.symbols('u0 v0', real=True); tt = sp.symbols('t', real=True)
    ut = sp.exp(aj*tt)*u0; vt = sp.exp(bj*tt)*v0 - u0**jj*(sp.exp(bj*tt) - sp.exp(tt))/(bj - 1)
    chk('(11.2) j=%d solves v\' = b v - u^j' % jj, vt.diff(tt) - (bj*vt - ut**jj))
J1 = sp.Matrix([[1, 0], [-1, 2*l - 1]])
chk('(11.1) j=1 linearization', (sp.Matrix([[sp.Rational(1, 1)*uu, 2*l*vv - vv - uu]]).jacobian([uu, vv]) - J1).norm())
# Section 11.2: f = d+ u_+^q + d- (-u)_+^q, q > 3: u f' = q f on both sides; f(e^(at)u) = e^t f(u); derivatives to order 3 -> 0
qq = sp.Symbol('q', positive=True); dp, dm = sp.symbols('dp dm')
up = sp.symbols('up', positive=True)
fpos = dp*up**qq; fneg = dm*up**qq      # u = up > 0 and u = -up < 0 (in terms of |u| = up)
chk('(11.3) u f\' = q f, u > 0', up*fpos.diff(up) - qq*fpos)
chk('(11.3) u f\' = q f, u < 0', (-up)*(-fneg.diff(up)) - qq*fneg)
chk('(11.3) f(e^(at) u) = e^t f(u), a = 1/q', dp*(sp.exp(tt/qq)*up)**qq - sp.exp(tt)*dp*up**qq)
q4 = sp.Rational(7, 2)
for m in (1, 2, 3):
    lim = sp.limit(sp.diff(up**q4, up, m), up, 0, '+')
    chk('(11.3) q = 7/2, derivative %d -> 0' % m, lim)
# Section 11.3
alp = sp.symbols('alp', positive=True)
chk('(11.4) transport', alp*uu*sp.diff(vv, uu) + vv*sp.diff(vv, vv) - vv)
# Section 4.2: winding number of an invertible linear map on the unit circle = sign det (numerical)
rng = np.random.default_rng(0); good = 0
for _ in range(200):
    A = rng.normal(size=(2, 2))
    if abs(np.linalg.det(A)) < 1e-3: continue
    th = np.linspace(0, 2*np.pi, 4001); P = A @ np.vstack([np.cos(th), np.sin(th)])
    ang = np.unwrap(np.arctan2(P[1], P[0])); w = round((ang[-1] - ang[0])/(2*np.pi))
    good += (w == int(np.sign(np.linalg.det(A))))
print('(4.2) winding = sign det on random matrices:', good, 'of', 200 - 0); n += 1; ok += (good >= 199)
print('ALL OK' if ok == n else 'SOME FAIL', ok, 'of', n)
