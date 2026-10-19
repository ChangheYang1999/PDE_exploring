"""V157: checks of FR Section 9.10 (Proposition 3.17, axis identity in S^+_even) and of the 4.2 test-density numbers
(lead item 20, candidate FR_cand_910 c5758fc8).
Part S (sympy): wall equation on the lower half-axis, the logarithmic derivative of E_+-, the exponent identity,
B_+ B_- = b_o^2 - w_e^2 and 1/B_- - 1/B_+ = 2 w_e/(b_o^2 - w_e^2), d_1 Xi(0, z), A'' = 2 e^F at +-pi/2 for
A = cos^2 th e^F, E'(0) formula.
Part N: (N1) synthetic axis data (not a profile): h from the wall ODE by direct quadrature, H_+- by its own limit,
against the FR formula (2 l^2/beta^2) exp(-2 beta J_+-) and the identity log(H_-/H_+) = -4 beta int w_e/(B_+ B_-);
(N2) the canonical axis velocity of x^2 P(y) e^{-r^2} by an own Fourier route (U_2^ = -xi_1^2/|xi|^2 rho^, heat-kernel
representation of 1/|xi|^2, closed forms in sympy) and, independently, by a real-space polar quadrature (mpmath);
w_e(1), w_e(10), c, w''(0), E'(0) for rho_* = x^2 (1 + 6y + 10y^2) e^{-r^2};
(N3) int_0^inf w_f/s^2 ds in closed form (Fourier), I_M for L = 1/100, l = 2, M = 0, 3, and the stated error bound;
(N4) the bound |DW| <= (1/4 pi^2) int |xi_1| |rho^| dxi against 37 sqrt(pi)/2 (times L).
"""
import sys, math
import sympy as sp
import mpmath as mp

ok = []
def rep(name, cond, extra=''):
    ok.append(bool(cond)); print(('OK   ' if cond else 'FAIL ') + name + (' ' + str(extra) if extra != '' else ''), flush=True)

# ---------------- Part S ----------------
r, y, z, s, t = sp.symbols('r y z s t', real=True)
l = sp.symbols('l', positive=True); p = 1/l; be = 2*l - sp.Rational(1, 2)
b = sp.Function('b'); h = sp.Function('h')
Bm = -b(-r); hm = h(-r)
lhs = Bm*sp.diff(hm, r) - 2*(sp.diff(Bm, r) - be)*hm
wall_at = (b(y)*sp.diff(h(y), y) - 2*(sp.diff(b(y), y) - be)*h(y)).subs(y, -r)
rep('S1 lower half-axis: B_- h_-\' - 2(B_-\' - beta) h_- = [b h\' - 2(b\' - beta) h](-r)', sp.simplify(sp.expand(lhs - wall_at.doit())) == 0)
rep('S1b 1 - 4l = -2 beta', sp.simplify(1 - 4*l + 2*be) == 0)
B = sp.Function('B')
E = 2*(B(r)/(be*r))**2*sp.exp(-2*be*sp.Integral(1/B(s) - 1/(be*s), (s, 0, r)))
dlogE = sp.simplify(sp.diff(sp.log(E), r).doit())
rep('S2 (log E)\' = 2 B\'/B - 2 beta/B, the same as (log h)\' from B h\' = 2(B\' - beta) h', sp.simplify(dlogE - (2*sp.diff(B(r), r)/B(r) - 2*be/B(r))) == 0)
rep('S3 -2 beta (1/l - 1/beta) = p - 2', sp.simplify(-2*be*(1/l - 1/be) - (p - 2)) == 0)
Bp, Bmm = sp.symbols('Bp Bm', positive=True)
bo = (Bp + Bmm)/2; we = (Bp - Bmm)/2
rep('S4 B_+ B_- = b_o^2 - w_e^2 and 1/B_- - 1/B_+ = 2 w_e/(b_o^2 - w_e^2)', sp.simplify(Bp*Bmm - (bo**2 - we**2)) == 0 and sp.simplify(1/Bmm - 1/Bp - 2*we/(bo**2 - we**2)) == 0)
wf = sp.Function('w')
rep('S4b B_+ - B_- = w(r) + w(-r) for B_+ = l r + w(r), B_- = -(l(-r) + w(-r))', sp.simplify((l*r + wf(r)) - (-(l*(-r) + wf(-r))) - (wf(r) + wf(-r))) == 0)
Y1, Y2 = sp.symbols('Y1 Y2', real=True); zp = sp.symbols('zp', positive=True)
Bf = sp.Function('Bf')
Xi = (Y1**2 + Y2**2)**(p/4)*Bf(sp.atan2(Y2, Y1))
d1 = sp.diff(Xi, Y1)
d1_up = sp.simplify(d1.subs({Y1: 0, Y2: zp}).subs(Bf(sp.pi/2), 0))
d1_dn = sp.simplify(d1.subs({Y1: 0, Y2: -zp}).subs(Bf(-sp.pi/2), 0))
Bp_up = sp.Subs(sp.Derivative(Bf(s), s), s, sp.pi/2).doit(); Bp_dn = sp.Subs(sp.Derivative(Bf(s), s), s, -sp.pi/2).doit()
c_up = sp.simplify(d1_up/(-(zp**(p/2 - 1))))
c_dn = sp.simplify(d1_dn/((zp**(p/2 - 1))))
print('   d_1 Xi(0, z), z > 0:', d1_up, ' z < 0:', d1_dn)
rep('S5 d_1 Xi(0, z) = -sgn(z) |z|^{p/2-1} B\'(sgn(z) pi/2) when B(+-pi/2) = 0',
    sp.simplify(c_up - Bp_up) == 0 and sp.simplify(c_dn - Bp_dn) == 0, (c_up, c_dn))
th = sp.symbols('th', real=True); F = sp.Function('F')
A = sp.cos(th)**2*sp.exp(F(th))
rep('S6 A = cos^2 th e^F: A\'\'(+-pi/2) = 2 e^{F(+-pi/2)}', all(sp.simplify(sp.diff(A, th, 2).subs(th, v).doit() - 2*sp.exp(F(v))) == 0 for v in [sp.pi/2, -sp.pi/2]))
Bs = sp.sin(th - sp.pi/2)*(2 + sp.cos(th))   # sample C^inf root with a simple zero at pi/2
rep('S6b A = B^2 with B(th_0) = 0: A\'\'(th_0) = 2 B\'(th_0)^2; B/cos th -> -B\'(th_0)/sin th_0',
    sp.simplify(sp.diff(Bs**2, th, 2).subs(th, sp.pi/2) - 2*sp.diff(Bs, th).subs(th, sp.pi/2)**2) == 0 and
    sp.simplify(sp.limit(Bs/sp.cos(th), th, sp.pi/2) + sp.diff(Bs, th).subs(th, sp.pi/2)/sp.sin(sp.pi/2)) == 0)
ww = sp.Function('ww'); hh = sp.Function('hh'); lv = sp.Rational(5, 4); bev = 2*lv - sp.Rational(1, 2)
bb = lv*y + ww(y)
Ef = bb*sp.diff(hh(y), y) - 2*(sp.diff(bb, y) - bev)*hh(y)
Ep0 = sp.diff(Ef, y).subs(y, 0).doit()
Ep0 = Ep0.subs({ww(0): 0}).subs(sp.Subs(sp.Derivative(ww(y), y), y, 0), sp.Rational(3, 4))
Ep0 = sp.simplify(Ep0.doit().subs(sp.Derivative(ww(y), y).subs(y, 0), sp.Rational(3, 4)))
print('   E\'(0) =', Ep0)

if len(sys.argv) > 1 and sys.argv[1] == 'symonly':
    print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok)); sys.exit(0)

# ---------------- Part N1: synthetic axis data ----------------
mp.mp.dps = 30
L1 = mp.mpf('1.6'); P1 = 1/L1; BE1 = 2*L1 - mp.mpf('0.5'); C1 = L1 - mp.mpf('0.5'); D1 = mp.mpf('0.3')
def w1(yv): return C1*yv*(1 + yv**2)**((P1 - 1)/2) + D1*yv**2*(1 + yv**2)**(P1/2 - 1) + mp.mpf('0.2')*yv**3*mp.exp(-yv**2)
def w1p(yv): return mp.diff(w1, yv)
def b1(yv): return L1*yv + w1(yv)
def b1p(yv): return L1 + w1p(yv)
okb = all(b1p(mp.mpf(v)) > 0 for v in [-50, -10, -3, -1.5, -1, -0.5, -0.2, 0, 0.2, 0.5, 1, 1.5, 3, 10, 50])
def logh_rate(tv):   # (log h)' = 2 (b' - beta)/b, regular at 0
    if abs(tv) < mp.mpf('1e-12'):
        return 2*mp.diff(b1, 0, 2)/BE1
    return 2*(b1p(tv) - BE1)/b1(tv)
def logH(sign):
    f0 = mp.quad(lambda u: sign*logh_rate(sign*u), [0, 0.5, 1])           # d/du log h(sign u) = sign (log h)'(sign u)
    f1 = mp.quad(lambda u: sign*logh_rate(sign*u) + (2 - P1)/u, [1, 10, 100, mp.inf])
    return mp.log(2) + f0 + f1
lHp = logH(1); lHm = logH(-1)
def Bpm(sign, rv): return b1(rv) if sign > 0 else -b1(-rv)
def J(sign): return mp.quad(lambda u: 1/Bpm(sign, u) - 1/(BE1*u), [0, 0.5, 1]) + mp.quad(lambda u: 1/Bpm(sign, u) - 1/(L1*u), [1, 10, 100, mp.inf])
lHp_fr = mp.log(2*L1**2/BE1**2) - 2*BE1*J(1); lHm_fr = mp.log(2*L1**2/BE1**2) - 2*BE1*J(-1)
we_int = mp.quad(lambda u: ((w1(u) + w1(-u))/2)/(Bpm(1, u)*Bpm(-1, u)), [0, 0.5, 1, 10, 100, mp.inf])
rep('N1a synthetic b (b\' > 0 sampled): log H_+- by direct ODE quadrature = log(2 l^2/beta^2) - 2 beta J_+-',
    okb and abs(lHp - lHp_fr) < mp.mpf('1e-11') and abs(lHm - lHm_fr) < mp.mpf('1e-11'),
    '(%s vs %s; %s vs %s)' % (mp.nstr(lHp, 15), mp.nstr(lHp_fr, 15), mp.nstr(lHm, 15), mp.nstr(lHm_fr, 15)))
rep('N1b log(H_-/H_+) + 4 beta int w_e/(B_+ B_-) = 0 on the same data (h = H_+- |y|^{p-2}(1 + o(1)))',
    abs(lHm - lHp + 4*BE1*we_int) < mp.mpf('1e-11'), '(log ratio %s, 4 beta int %s)' % (mp.nstr(lHm - lHp, 15), mp.nstr(4*BE1*we_int, 15)))
# direct check of the limit: h(Y) Y^{2-p} at Y = 1e8 against H_+ (relative error O(Y^{p-1}))
d6 = mp.log(2) + mp.quad(lambda u: logh_rate(u), [0, 0.5, 1, 10, 100, 1e4, 1e6]) + (2 - P1)*mp.log(1e6) - lHp
d8 = mp.log(2) + mp.quad(lambda u: logh_rate(u), [0, 0.5, 1, 10, 100, 1e4, 1e6, 1e8]) + (2 - P1)*mp.log(1e8) - lHp
rep('N1c log(h(Y) Y^{2-p}) - log H_+ at Y = 1e6, 1e8: ratio about 100^{1-p} (rate O(Y^{p-1}))', abs(d6/d8/mp.mpf(100)**(1 - P1) - 1) < 0.1,
    '(%s, %s, ratio %s, 100^{1-p} = %s)' % (mp.nstr(d6, 5), mp.nstr(d8, 5), mp.nstr(d6/d8, 5), mp.nstr(mp.mpf(100)**(1 - P1), 5)))

# ---------------- Part N2: rho = x^2 P(y) e^{-r^2}: canonical axis velocity ----------------
X1, X2, u, v, k = sp.symbols('xi1 xi2 u v k', real=True); up = sp.symbols('up', positive=True); sP = sp.symbols('sP', positive=True)
Mv = sp.symbols('M', real=True)
g1 = sp.sqrt(sp.pi)*(sp.Rational(1, 2) - X1**2/4)*sp.exp(-X1**2/4)           # FT of x^2 e^{-x^2}
assert sp.simplify(sp.integrate(sp.exp(-sp.I*X1*s)*s**2*sp.exp(-s**2), (s, -sp.oo, sp.oo)) - g1) == 0
g2e = lambda M: sp.sqrt(sp.pi)*(1 + M*(sp.Rational(1, 2) - X2**2/4))*sp.exp(-X2**2/4)   # FT of (1 + M y^2) e^{-y^2}
g2o = -sp.I*(X2/2)*sp.sqrt(sp.pi)*sp.exp(-X2**2/4)                         # FT of y e^{-y^2}
assert sp.simplify(sp.integrate(sp.exp(-sp.I*X2*s)*s*sp.exp(-s**2), (s, -sp.oo, sp.oo)) - g2o) == 0
# U_2^ = -xi_1^2/|xi|^2 rho^, 1/|xi|^2 = int_0^inf e^{-t |xi|^2} dt; u = t + 1/4 > 1/4
T1 = sp.simplify(sp.integrate(X1**2*sp.exp(-t*X1**2)*g1, (X1, -sp.oo, sp.oo), conds='none'))
def w_even_closed(M):
    # w(y) = U_2(0, y) - U_2(0, 0) = -(1/4 pi^2) int_0^inf T1(t) T2(t, y) dt, T2 = int e^{-t xi2^2} g2e (cos(xi2 y) - 1) dxi2
    T2 = sp.simplify(sp.integrate(sp.exp(-t*X2**2)*g2e(M)*(sp.cos(X2*sP) - 1), (X2, -sp.oo, sp.oo), conds='none'))
    integrand = sp.simplify(T1*T2)
    return integrand
Ie = w_even_closed(10)
print('   integrand (M = 10):', sp.simplify(Ie.subs(t, up - sp.Rational(1, 4))))
def w_even_num(M, yv):
    f = sp.lambdify((t, sP), w_even_closed(M), 'mpmath')
    return -mp.quad(lambda tv: f(tv, yv), [0, 1, 10, mp.inf])/(4*mp.pi**2)
we1 = w_even_num(10, mp.mpf(1)); we10 = w_even_num(10, mp.mpf(10))
target = mp.mpf(293)/8 - mp.mpf(395)/(4*mp.e)
rep('N2a rho_*: w_e(1) = 293/8 - 395/(4e) > 0 (Fourier route)', abs(we1 - target) < mp.mpf('1e-20') and we1 > 0, '(%s vs %s)' % (mp.nstr(we1, 22), mp.nstr(target, 22)))
rep('N2b rho_*: w_e(10) < 0 (Fourier route)', we10 < 0, mp.nstr(we10, 12))
# closed form of w_e(y): t-integral exactly
try:
    wcl = sp.simplify(-sp.integrate(sp.expand(Ie.subs(t, up - sp.Rational(1, 4))), (up, sp.Rational(1, 4), sp.oo), conds='none')/(4*sp.pi**2))
    print('   closed form w_e(y) for x^2 (1 + 10 y^2) e^{-r^2}:', wcl)
    rep('N2c closed form at y = 1 equals 293/8 - 395/(4e)', sp.simplify(wcl.subs(sP, 1) - (sp.Rational(293, 8) - sp.Rational(395, 4)/sp.E)) == 0, sp.nsimplify(wcl.subs(sP, 1)))
except Exception as ex:
    print('   closed form not obtained:', ex)
# real-space polar quadrature (independent): w(y) = 2 (I(y) - I(0)),
# I(y) = int_{-pi/2}^{pi/2} int_0^inf cos(2 phi) cos^2(phi) s e^{-s^2 cos^2 phi} g(y + s sin phi) ds dphi / (2 pi), g = P e^{-z^2}
def I_polar(gfun, yv):
    def inner(ph):
        cph = mp.cos(ph); sph = mp.sin(ph)
        return mp.cos(2*ph)*cph**2*mp.quad(lambda sv: sv*mp.exp(-sv**2*cph**2)*gfun(yv + sv*sph), [0, 2, 6, 15, mp.inf])
    return mp.quad(inner, [-mp.pi/2, -mp.pi/4, 0, mp.pi/4, mp.pi/2])/(2*mp.pi)
mp.mp.dps = 20
gstar = lambda zz: (1 + 6*zz + 10*zz**2)*mp.exp(-zz**2)
I0 = I_polar(gstar, 0)
wp1 = 2*(I_polar(gstar, 1) - I0); wm1 = 2*(I_polar(gstar, -1) - I0)
rep('N2d real-space polar quadrature: (w(1) + w(-1))/2 = 293/8 - 395/(4e)', abs((wp1 + wm1)/2 - target) < mp.mpf('1e-12'), '(%s; w(1) %s, w(-1) %s)' % (mp.nstr((wp1 + wm1)/2, 15), mp.nstr(wp1, 10), mp.nstr(wm1, 10)))
# c = w'(0) and w''(0): differentiate g under the integral (z = y + t substitution)
zs = sp.symbols('zs', real=True); gs_expr = (1 + 6*zs + 10*zs**2)*sp.exp(-zs**2)
gp = sp.lambdify(zs, sp.diff(gs_expr, zs), 'mpmath'); gpp = sp.lambdify(zs, sp.diff(gs_expr, zs, 2), 'mpmath')
c_num = 2*I_polar(gp, 0); w2_num = 2*I_polar(gpp, 0)
Ep0n = 24 - 4*w2_num    # E'(0) = beta h'(0) - 2 w''(0) h(0), h(0) = 2, h'(0) = 12, beta = 2 (b'(0) = beta needs c = 3/4)
rep('N2e rho_*: c = w\'(0) = 3/4, w\'\'(0) = 13/8, E\'(0) = 24 - 4 w\'\'(0) = 35/2', abs(c_num - mp.mpf(3)/4) < 1e-12 and abs(Ep0n - mp.mpf(35)/2) < 1e-11,
    '(c %s, w\'\'(0) %s, E\'(0) %s)' % (mp.nstr(c_num, 14), mp.nstr(w2_num, 14), mp.nstr(Ep0n, 14)))
mp.mp.dps = 30

# ---------------- Part N3: int_0^inf w_f/s^2 and I_M ----------------
# int_0^inf w/y^2 dy = (1/(8 pi)) int xi_1^2 |xi_2| / |xi|^2 rho^ dxi  (int_0^inf (cos ky - 1)/y^2 dy = -pi |k|/2)
th2 = sp.symbols('th2', real=True)
rh = (g1*g2e(Mv)).subs({X1: k*sp.cos(th2), X2: k*sp.sin(th2)})
integ = sp.integrate(sp.integrate(sp.expand(k*sp.cos(th2)**2*sp.Abs(sp.sin(th2))*rh*k).subs(sp.Abs(sp.sin(th2)), sp.sin(th2)), (th2, 0, sp.pi)), (k, 0, sp.oo))
Iw = sp.simplify(2*integ/(8*sp.pi))     # the th2 in (pi, 2 pi) half equals the (0, pi) half by symmetry
rep('N3a int_0^inf w_f(s)/s^2 ds = sqrt(pi)(5M - 14)/105 (Fourier, exact)', sp.simplify(Iw - sp.sqrt(sp.pi)*(5*Mv - 14)/105) == 0, Iw)
Lr = mp.mpf(1)/100; lr = mp.mpf(2)
for M in [0, 3]:
    f = sp.lambdify((t, sP), w_even_closed(M), 'mpmath')
    wfun = lambda sv: -mp.quad(lambda tv: f(tv, sv), [0, 1, 10, mp.inf])/(4*mp.pi**2)
    mp.mp.dps = 20
    IM = Lr*mp.quad(lambda sv: wfun(sv)/(lr**2*sv**2 - Lr**2*wfun(sv)**2), [0, 0.5, 1, 2, 4, 8, 20, mp.inf])
    IM0 = (Lr/lr**2)*mp.sqrt(mp.pi)*(5*M - 14)/105
    chk0 = Lr/lr**2*mp.quad(lambda sv: wfun(sv)/sv**2, [0, 0.5, 1, 2, 4, 8, 20, mp.inf])
    mp.mp.dps = 30
    rep('N3b M = %d: I_M = %s, I_M^0 = %s, |I_M - I_M^0|/|I_M^0| = %s < 3/9999' % (M, mp.nstr(IM, 8), mp.nstr(IM0, 8), mp.nstr(abs(IM - IM0)/abs(IM0), 4)),
        abs(IM - IM0) < mp.mpf(3)/9999*abs(IM0) and abs(chk0 - IM0) < 1e-15 and ((M == 0 and IM < 0) or (M == 3 and IM > 0)))

# ---------------- Part N4: |DW| bound ----------------
# DU^(xi) = i xi (x) (xi_1 xi_2, -xi_1^2) rho^/|xi|^2 has operator norm |xi_1| |rho^|, so |DW(X)| <= (1/4 pi^2) int |xi_1| |rho^| dxi
# rho_f^ = g1(xi_1) g2e(xi_2) factorizes; integrate |.| with breakpoints at the zeros (xi_1^2 = 2, xi_2^2 = 2 + 4/M)
a1 = sp.lambdify(X1, g1, 'mpmath')
int1 = 2*mp.quad(lambda q: q*abs(a1(q)), [0, mp.sqrt(2), 6, 20, mp.inf])
for M in [0, 3]:
    a2 = sp.lambdify(X2, g2e(M), 'mpmath')
    br = [0, mp.sqrt(2 + mp.mpf(4)/M), 8, 20, mp.inf] if M > 0 else [0, 8, 20, mp.inf]
    int2 = 2*mp.quad(lambda q: abs(a2(q)), br)
    bnd = int1*int2/(4*mp.pi**2)
    rep('N4 M = %d: (1/4 pi^2) int |xi_1| |rho_f^| = %s <= 37 sqrt(pi)/2 = %s (so |DW| <= L times it < l = 2)' % (M, mp.nstr(bnd, 10), mp.nstr(37*mp.sqrt(mp.pi)/2, 10)),
        bnd <= 37*mp.sqrt(mp.pi)/2 and Lr*bnd < lr)
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
