"""V160: checks of FR 4.16 and Section 9.11 (lead item 24, snapshot d733c084).
Part S (sympy, exact unless stated): the homogeneous field H, its divergence, curl and pressure P_H; the material
identity; the radial-graph identity and the two leading coefficients; the Reynolds and pressure integrands; E_A > 0
at either location of a quadratic zero; the band, Tonelli, power and zero-curve formulas (with numerical
quadrature for the test angular densities); the integration by parts of (c); the test densities rho_M (jet, growth,
tail, Fourier data, Psi_0, Psi_*, the three rationals, (rho_0)_x, residual 3x^2, zeros of A_M); kernel symmetries
and scaling.
Part N (numerics, own quadrature on the GPU, float64): the canonical once-subtracted law
    W_2 + i W_1 = (1/2 pi) p.v. int [1/(xi - eta)^2 - 1/eta^2] rho(eta) d eta - rho(xi)/2
for the homogeneous F_M (must equal H_M on the unit circle) and for rho_M itself (W_1 on both axes, W = O(r^2) at 0,
W_2(x, 0) - (3/2) x^{1/2} Psi_M(0) bounded, and psi_M(x, 0) = int_0^x W_2 with its r^{3/2} Psi_M(0) asymptotic and
sign) for M = 0 and M = 100.
"""
import sys, math
import numpy as np
import sympy as sp

ok = []
def rep(name, cond, extra=''):
    ok.append(bool(cond)); print(('OK   ' if cond else 'FAIL ') + name + (' ' + str(extra) if extra != '' else ''), flush=True)

th, t, s, u = sp.symbols('theta t s u', real=True)
r, R, a, l = sp.symbols('r R a l', positive=True)
x, y = sp.symbols('x y', real=True)
p = sp.symbols('p', positive=True)
half = sp.Rational(1, 2)

# ---------------- Part S ----------------
# S1-S3: concrete A_0, A_* and the stated Psi_0, Psi_* (p = 1/2), in Cartesian coordinates
A0 = sp.cos(th)**2
Ast = sp.cos(th)**2*sp.sin(th)**6
Ast_four = sp.Rational(5, 128) - sp.cos(2*th)/32 - sp.cos(4*th)/32 + sp.cos(6*th)/32 - sp.cos(8*th)/128
rep('S0 A_* = cos^2 sin^6 = 5/128 - cos2/32 - cos4/32 + cos6/32 - cos8/128',
    sp.simplify(sp.expand(sp.expand_trig(Ast - Ast_four))) == 0)
Psi0 = -sp.Rational(7, 10)*sp.cos(th) - sp.cos(3*th)/18
Psist = sp.cos(th)/64 - sp.cos(3*th)/144 + 5*sp.cos(5*th)/728 - 61*sp.cos(7*th)/23936 + sp.cos(9*th)/2688
def ang_res(Ps, A, pv):
    return sp.simplify(sp.expand(sp.expand_trig(sp.diff(Ps, th, 2) + (pv + 1)**2*Ps - (sp.sin(th)*sp.diff(A, th) - pv*sp.cos(th)*A))))
rep('S1 Psi_0 solves Psi\'\' + (9/4) Psi = sin A_0\' - (1/2) cos A_0', ang_res(Psi0, A0, half) == 0)
rep('S2 Psi_* solves the same equation with A_*', ang_res(Psist, Ast, half) == 0)
# independent: Fourier projection of the forcing and division by 9/4 - n^2
def psi_by_projection(A):
    """exact Fourier coefficients in z = e^{i theta}; mode n divided by 9/4 - n^2"""
    zz = sp.symbols('zz')
    f = sp.sin(th)*sp.diff(A, th) - half*sp.cos(th)*A
    fz = sp.expand(f.rewrite(sp.exp).subs(th, -sp.I*sp.log(zz)))
    out = 0
    for term in sp.Add.make_args(fz):
        cf, n = term.as_coeff_exponent(zz)
        assert cf.free_symbols == set()
        out += cf*zz**n/(sp.Rational(9, 4) - n**2)
    return sp.expand(out.subs(zz, sp.exp(sp.I*th)).rewrite(sp.cos))
P0p = psi_by_projection(A0); Pstp = psi_by_projection(Ast)
rep('S3 exact Fourier (Laurent) coefficients of the forcing divided by 9/4 - n^2 reproduce Psi_0 and Psi_*',
    sp.simplify(sp.expand(sp.expand_trig(P0p - Psi0))) == 0 and sp.simplify(sp.expand(sp.expand_trig(Pstp - Psist))) == 0)
v0 = Psi0.subs(th, 0); vst = Psist.subs(th, 0); v100 = v0 + 100*vst
rep('S4 Psi_0(0) = -34/45, Psi_*(0) = 2048/153153, Psi_100(0) = 148474/255255',
    v0 == sp.Rational(-34, 45) and vst == sp.Rational(2048, 153153) and v100 == sp.Rational(148474, 255255), (v0, vst, v100))
# mode coupling
n_, an = sp.symbols('n a_n', positive=True)
forc = sp.expand(sp.sin(th)*sp.diff(an*sp.cos(n_*th), th) - p*sp.cos(th)*an*sp.cos(n_*th))
claim = -(n_ + p)*an*sp.cos((n_ - 1)*th)/2 + (n_ - p)*an*sp.cos((n_ + 1)*th)/2
rep('S5 forcing of a_n cos(n th): -(n + p) a_n cos((n-1)th)/2 + (n - p) a_n cos((n+1)th)/2; a_0 gives -p a_0 cos th',
    sp.simplify(sp.expand_trig(sp.expand(sp.expand_trig(forc - claim).rewrite(sp.exp)))) == 0 and
    sp.simplify(sp.sin(th)*sp.diff(an, th) - p*sp.cos(th)*an + p*an*sp.cos(th)) == 0)
rep('S6 the angular operator sends cos(n th) to (9/4 - n^2) cos(n th); 3/2 not an integer (periodic solution unique)',
    sp.simplify(sp.diff(sp.cos(n_*th), th, 2) + sp.Rational(9, 4)*sp.cos(n_*th) - (sp.Rational(9, 4) - n_**2)*sp.cos(n_*th)) == 0)

# Cartesian checks of H, div H, curl H, pressure
def cart_checks(Ps, A, pv):
    rr = sp.sqrt(x**2 + y**2); c = x/rr; sn = y/rr
    def ang(expr):  # expression in theta -> Cartesian via Chebyshev expansion in cos, sin
        e = sp.expand(sp.expand_trig(expr))
        return e.subs({sp.cos(th): c, sp.sin(th): sn})
    Pc = ang(Ps); Pdc = ang(sp.diff(Ps, th)); Ac = ang(A)
    Hr = -rr**pv*Pdc; Ht = (pv + 1)*rr**pv*Pc
    H1 = Hr*c - Ht*sn; H2 = Hr*sn + Ht*c
    F = rr**pv*Ac
    div = sp.diff(H1, x) + sp.diff(H2, y); curl = sp.diff(H2, x) - sp.diff(H1, y)
    qH = ang((sp.diff(Ps, th) - A*sp.sin(th))/(pv + 1)); PH = rr**(pv + 1)*qH
    e1 = H1 + sp.diff(PH, x); e2 = H2 + sp.diff(PH, y) + F
    pts = [(0.7, 0.3), (-1.3, 2.2), (0.2, -0.9), (3.1, 1.7)]
    f = sp.lambdify((x, y), [div, curl + sp.diff(F, x), e1, e2, x*H1 + y*H2 - (-x*sp.diff(PH, x) - y*sp.diff(PH, y) - y*F),
                             x*H1 + y*H2 + rr**(pv + 1)*Pdc], 'mpmath')
    import mpmath as mp
    mp.mp.dps = 30
    worst = max(abs(v) for P_ in pts for v in f(mp.mpf(P_[0]), mp.mpf(P_[1])))
    return worst
for nm, Ps, A in [('A_0, Psi_0', Psi0, A0), ('A_*, Psi_*', Psist, Ast)]:
    w = cart_checks(Ps, A, half)
    rep('S7 %s (Cartesian, 4 points, 30 digits): div H = 0, curl H = -F_x, H = -grad P_H - F e_2, X.H = -X.grad P_H - y F = -r^{p+1} Psi\'' % nm,
        w < 1e-25, '(max %.1e)' % float(w))
# generic polar: q_H' identity
Psi = sp.Function('Psi'); Af = sp.Function('A')
qH = (Psi(th).diff(th) - Af(th)*sp.sin(th))/(p + 1)
ode_rhs = sp.sin(th)*Af(th).diff(th) - p*sp.cos(th)*Af(th) - (p + 1)**2*Psi(th)
qHp = sp.diff(qH, th).subs(Psi(th).diff(th, 2), ode_rhs)
rep('S8 q_H\' = -(p+1) Psi - A cos(theta) (generic A, p)', sp.simplify(qHp + (p + 1)*Psi(th) + Af(th)*sp.cos(th)) == 0)
# generic polar components of -grad P_H - F e_2 (e_2 = sin e_r + cos e_th)
PH = r**(p + 1)*qH
radial = -sp.diff(PH, r) - r**p*Af(th)*sp.sin(th)
angular = -sp.diff(PH, th)/r - r**p*Af(th)*sp.cos(th)
angular = angular.subs(Psi(th).diff(th, 2), ode_rhs)
rep('S9 generic: (-grad P_H - F e_2)_r = -r^p Psi\', (...)_th = (p+1) r^p Psi',
    sp.simplify(radial + r**p*Psi(th).diff(th)) == 0 and sp.simplify(angular - (p + 1)*r**p*Psi(th)) == 0)
# generic polar div/curl of H
Hr = -r**p*Psi(th).diff(th); Ht = (p + 1)*r**p*Psi(th)
divH = sp.diff(r*Hr, r)/r + sp.diff(Ht, th)/r
curlH = sp.diff(r*Ht, r)/r - sp.diff(Hr, th)/r
mFx = -(sp.cos(th)*sp.diff(r**p*Af(th), r) - sp.sin(th)*sp.diff(r**p*Af(th), th)/r)
rep('S10 generic: div H = 0 and curl H = r^{p-1}(Psi\'\' + (p+1)^2 Psi) = -F_x <=> the angular equation',
    sp.simplify(divH) == 0 and sp.simplify(curlH - r**(p - 1)*(Psi(th).diff(th, 2) + (p + 1)**2*Psi(th))) == 0 and
    sp.simplify(curlH.subs(Psi(th).diff(th, 2), ode_rhs) - mFx) == 0)

# S11: material identity and coefficients
E, Jf, Qf = sp.symbols('E_A J Q')
lp = 1/l
J_ = E*R**(2*lp + 2)/(l - 1)**2; Q_ = -E*R**(2*lp + 2)/(l - 1)
rep('S11 l(2p+2) = 4l - 2(l-1) with p = 1/l; l R J\' = 4l J + 2Q holds exactly for the leading terms',
    sp.simplify(l*(2*lp + 2) - (4*l - 2*(l - 1))) == 0 and sp.simplify(l*R*sp.diff(J_, R) - 4*l*J_ - 2*Q_) == 0)
If = sp.Function('I')
rep('S12 (I/R^4)\' = (l R I\' - 4 l I)/(l R^5) = 2Q/(l R^5) when l R I\' = 4l I + 2Q',
    sp.simplify(sp.diff(If(R)/R**4, R) - (l*R*If(R).diff(R) - 4*l*If(R))/(l*R**5)) == 0)
rep('S13 with I = pi R^4/2 + J: l R J\' = 4 l J + 2Q (the pi R^4/2 part cancels)',
    sp.simplify(l*R*sp.diff(sp.pi*R**4/2, R) - 4*l*sp.pi*R**4/2) == 0)
# S14: radial-graph identity on an explicit star-shaped domain
b1, b2, b3 = sp.Rational(3, 10), sp.Rational(1, 7), sp.Rational(-1, 5)
g = b1*sp.cos(th) + b2*sp.sin(2*th) + b3*sp.cos(3*th)
k = sp.symbols('k', positive=True)
sR = R*(k + g)
ksol = [kk for kk in sp.solve(sp.integrate(sp.expand(sR**2), (th, 0, 2*sp.pi)) - 2*sp.pi*R**2, k) if kk.is_positive][0]
sR = sR.subs(k, ksol)
area = sp.integrate(sp.expand(sR**2), (th, 0, 2*sp.pi))/2
Ival = sp.integrate(sp.expand(sR**4), (th, 0, 2*sp.pi))/4
rhs = sp.integrate(sp.expand((sR**2 - R**2)**2), (th, 0, 2*sp.pi))/4
rep('S14 explicit star domain with |D| = pi R^2: I - pi R^4/2 = (1/4) int (s^2 - R^2)^2 > 0 (exact)',
    sp.simplify(area - sp.pi*R**2) == 0 and sp.simplify(Ival - sp.pi*R**4/2 - rhs) == 0 and float(rhs.subs(R, 1)) > 0)
# S15: leading coefficient of (1/4) int (s^2 - R^2)^2 and of the work integral, for s = R + R^p Psi'/(l-1)
ep = sp.symbols('epsilon', positive=True)  # epsilon = R^{p-1}
Pd = sp.Function('Pd')(th)                   # Psi'(theta)
sn = R*(1 + ep*Pd/(l - 1))
lead = sp.series(((sn**2 - R**2)**2/4)/R**4, ep, 0, 3).removeO()
rep('S15 (s^2 - R^2)^2/4 = R^{2p+2} Psi\'^2/(l-1)^2 + higher order in R^{p-1}',
    sp.simplify(lead.coeff(ep, 2) - Pd**2/(l - 1)**2) == 0 and lead.coeff(ep, 1) == 0 and lead.coeff(ep, 0) == 0)
work = sp.integrate(-(R**(2))*ep*R*Pd, (r, R, sn))/R**4    # r^2 W_r ~ -R^2 R^p Psi', R^p = ep R
rep('S16 int_R^{s_R} r^2 W_r dr with r^2 W_r = -R^{p+2} Psi\': -R^{2p+2} Psi\'^2/(l-1)',
    sp.simplify(work - (-(ep**2)*Pd**2/(l - 1))) == 0)
# S17: Reynolds integrand, pressure integration by parts (generic)
psi = sp.Function('psi')(x, y); P = sp.Function('P')(x, y); rho = sp.Function('rho')(x, y)
W1, W2 = -sp.diff(psi, y), sp.diff(psi, x)
V1, V2 = l*x + W1, l*y + W2
Xsq = x**2 + y**2
rey = sp.diff(Xsq*V1, x) + sp.diff(Xsq*V2, y)
rep('S17 div(|X|^2 V) = V.grad|X|^2 + |X|^2 div V = 4l|X|^2 + 2X.W for V = lX + grad-perp psi',
    sp.simplify(rey - (4*l*Xsq + 2*(x*W1 + y*W2))) == 0)
Wp1, Wp2 = -sp.diff(P, x), -sp.diff(P, y) - rho
rep('S18 curl(W + rho e_2) = 0 for W = -grad P - rho e_2; X.W = -div(P X) + 2P - y rho',
    sp.simplify(sp.diff(Wp2 + rho, x) - sp.diff(Wp1, y)) == 0 and
    sp.simplify(x*Wp1 + y*Wp2 - (-(sp.diff(P*x, x) + sp.diff(P*y, y)) + 2*P - y*rho)) == 0)
rep('S19 a constant in P changes 2 int_D P - int_{bd D} P X.n by 2|D| - int_D div X = 0', sp.simplify(2 - (sp.diff(x, x) + sp.diff(y, y))) == 0)
# S20: E_A > 0: local forms at a quadratic zero
be, a3 = sp.symbols('beta a3', real=True)
Aloc = a*t**2 + a3*t**3
qloc = sp.sin(be + t)*sp.diff(Aloc, t) - p*sp.cos(be + t)*Aloc
ser = sp.series(qloc, t, 0, 3).removeO()
rep('S20 sin(theta)A\' - p cos(theta)A at beta + t: 2a sin(beta) t + O(t^2); at sin(beta) = 0: a(2-p)cos(beta) t^2 + O(t^3)',
    sp.simplify(ser.coeff(t, 1) - 2*a*sp.sin(be)) == 0 and sp.simplify(ser.coeff(t, 0)) == 0 and
    all(sp.simplify(ser.subs(be, b0).coeff(t, 2) - a*(2 - p)*sp.cos(b0)) == 0 and ser.subs(be, b0).coeff(t, 1) == 0 for b0 in [0, sp.pi]))
# S21: Tonelli substitution and the power formula
tt = sp.symbols('tt', positive=True); Av = sp.symbols('Av', positive=True)
rr_t = (tt/Av)**(1/p)
rep('S21 t = r^p A: r dr = (1/p) A^{-2/p} t^{2/p - 1} dt', sp.simplify(rr_t*sp.diff(rr_t, tt) - Av**(-2/p)*tt**(2/p - 1)/p) == 0)
q = sp.symbols('q', real=True)
rep('S22 int_0^R r^{1+pq} dr = R^{2+pq}/(2+pq) for 2 + pq > 0; q > -1/2, p < 1 gives 2 + pq > 3/2',
    sp.simplify(sp.integrate(r**(sp.Rational(1, 3)*sp.Rational(-2, 5) + 1), (r, 0, R)) - R**(2 + sp.Rational(1, 3)*sp.Rational(-2, 5))/(2 + sp.Rational(1, 3)*sp.Rational(-2, 5))) == 0)
rep('S23 int_0^1 s^{2q} ds finite iff q > -1/2 (q = -2/5 finite, q = -1/2 infinite); A^{-2/p} ~ s^{-4/p}, 4/p > 4',
    sp.integrate(s**sp.Rational(-4, 5), (s, 0, 1)).is_finite and sp.integrate(s**-1, (s, 0, 1)) == sp.oo)
# S24: zero-curve weighted length for the homogeneous model: B^2 = A, B(beta) = 0 => B'(beta)^2 = A''(beta)/2 = a
B0_, B1_, B2_ = sp.symbols('B0 B1 B2', real=True)   # B, B', B'' at the zero
rel = (2*B1_**2 + 2*B0_*B2_).subs(B0_, 0)                   # (B^2)'' = 2B'^2 + 2BB''
rep('S24 (B^2)\'\' = 2B\'^2 at a zero of B: |grad Xi| = r^{p/2-1} a^{1/2} on a zero ray; int_0^R r^{1-p/2} dr = R^{2-p/2}/(2-p/2)',
    sp.simplify(sp.diff(sp.Function('B')(th)**2, th, 2) - 2*sp.Function('B')(th).diff(th)**2 - 2*sp.Function('B')(th)*sp.Function('B')(th).diff(th, 2)) == 0 and rel == 2*B1_**2 and
    sp.simplify(sp.integrate(r**(1 - sp.Rational(1, 4)), (r, 0, R)) - R**(2 - sp.Rational(1, 4))/(2 - sp.Rational(1, 4))) == 0)
# S25: integration by parts of (c) in polar coordinates, numerically (A_0, Psi_0, p = 1/2)
import mpmath as mp
mp.mp.dps = 20
zeta = lambda rr_, tq: (mp.exp(-1/((rr_ - 1)*(3 - rr_))) if 1 < rr_ < 3 else 0)*(1 + mp.mpf('0.3')*mp.sin(tq) + mp.mpf('0.2')*mp.sin(2*tq) + mp.mpf('0.15')*mp.cos(tq) + mp.mpf('0.1')*mp.sin(3*tq))
Gf = lambda v: mp.sin(v) + v**2; Gp = lambda v: mp.cos(v) + 2*v
A0f = sp.lambdify(th, A0, 'mpmath'); A0d = sp.lambdify(th, sp.diff(A0, th), 'mpmath')
P0f = sp.lambdify(th, Psi0, 'mpmath'); P0d = sp.lambdify(th, sp.diff(Psi0, th), 'mpmath')
def lhs_int(rr_, tq):  # zeta G'(F) H.grad F r
    F = mp.sqrt(rr_)*A0f(tq)
    Hr_ = -mp.sqrt(rr_)*P0d(tq); Ht_ = mp.mpf(3)/2*mp.sqrt(rr_)*P0f(tq)
    Fr = A0f(tq)/(2*mp.sqrt(rr_)); Ft = A0d(tq)/mp.sqrt(rr_)
    return zeta(rr_, tq)*Gp(F)*(Hr_*Fr + Ht_*Ft)*rr_
def rhs_int(rr_, tq):  # -G(F) H.grad zeta r
    F = mp.sqrt(rr_)*A0f(tq)
    Hr_ = -mp.sqrt(rr_)*P0d(tq); Ht_ = mp.mpf(3)/2*mp.sqrt(rr_)*P0f(tq)
    zr = mp.diff(lambda z: zeta(z, tq), rr_); zt = mp.diff(lambda z: zeta(rr_, z), tq)/rr_
    return -Gf(F)*(Hr_*zr + Ht_*zt)*rr_
mp.mp.dps = 15
I1 = mp.quad(lhs_int, [1, 2, 3], [0, mp.pi/2, mp.pi, 3*mp.pi/2, 2*mp.pi])
I2 = mp.quad(rhs_int, [1, 2, 3], [0, mp.pi/2, mp.pi, 3*mp.pi/2, 2*mp.pi])
rep('S25 (c): int zeta G\'(F) H.grad F = -int G(F) H.grad zeta (A_0, G = sin t + t^2, angular zeta; quadrature)',
    abs(I1 - I2) < 1e-8*max(1, abs(I1)) and abs(I1) > 1e-3, '(%s vs %s)' % (mp.nstr(I1, 12), mp.nstr(I2, 12)))

# S26-S31: the test densities
M = sp.symbols('M', nonnegative=True)
rhoM = x**2*(1 + x**2 + y**2)**sp.Rational(-3, 4)*(1 + M*y**6/(1 + x**2 + y**2)**3)
lam = sp.symbols('lambda', positive=True)
jet = sp.series(rhoM.subs({x: lam*sp.cos(th), y: lam*sp.sin(th)}), lam, 0, 4).removeO()
rep('S26 rho_M = x^2 + O(r^4) (series in r along a generic ray)', sp.simplify(jet - lam**2*sp.cos(th)**2) == 0)
AM = sp.cos(th)**2*(1 + M*sp.sin(th)**6)
w_ = sp.symbols('w', positive=True)   # w = 1/r
rho_ray = rhoM.subs({x: sp.cos(th)/w_, y: sp.sin(th)/w_})
dser = sp.series(rho_ray - w_**sp.Rational(-1, 2)*AM, w_, 0, 3)
d_lead = sp.simplify(dser.removeO())
rep('S27 rho_M - r^{1/2} A_M = O(r^{-3/2}) along every ray (leading term c(theta) r^{-3/2})',
    sp.simplify(sp.limit((rho_ray - w_**sp.Rational(-1, 2)*AM)/w_**sp.Rational(3, 2), w_, 0) -
                sp.limit((rho_ray - w_**sp.Rational(-1, 2)*AM)/w_**sp.Rational(3, 2), w_, 0)) == 0 and
    sp.limit((rho_ray - w_**sp.Rational(-1, 2)*AM)/w_**sp.Rational(3, 2), w_, 0).is_finite)
# gradient of d at large r: d_x and d_y along a sample ray, decay exponent 5/2
dx_ = sp.diff(rhoM - (x**2 + y**2)**sp.Rational(1, 4)*AM.subs({sp.cos(th): x/sp.sqrt(x**2 + y**2), sp.sin(th): y/sp.sqrt(x**2 + y**2)}), x)
dxf = sp.lambdify((x, y, M), dx_, 'mpmath')
mp.mp.dps = 40
ratios = [abs(dxf(mp.mpf(10)**k*mp.mpf('0.6'), mp.mpf(10)**k*mp.mpf('0.8'), 3))*mp.mpf(10)**(k*mp.mpf(5)/2) for k in [3, 4, 5]]
rep('S28 |d_x d| r^{5/2} bounded along a ray (r = 1e3, 1e4, 1e5; M = 3)', max(ratios)/min(ratios) < 1.01, [mp.nstr(v, 6) for v in ratios])
rho0x = sp.diff(rhoM.subs(M, 0), x)
rep('S29 (rho_0)_x = x(1+r^2)^{-7/4}[2 + x^2/2 + 2y^2]',
    sp.simplify(rho0x - x*(1 + x**2 + y**2)**sp.Rational(-7, 4)*(2 + x**2/2 + 2*y**2)) == 0)
# residual with W = O(r^2): general quadratic W
w = sp.symbols('w1:7', real=True)
Wq1 = w[0]*x**2 + w[1]*x*y + w[2]*y**2; Wq2 = w[3]*x**2 + w[4]*x*y + w[5]*y**2
res = (2*x + Wq1)*sp.diff(rhoM, x) + (2*y + Wq2)*sp.diff(rhoM, y) - rhoM
rser = sp.series(res.subs({x: lam*sp.cos(th), y: lam*sp.sin(th)}), lam, 0, 3).removeO()
rep('S30 (2X + W).grad rho_M - rho_M = 3x^2 + O(r^3) for any W = O(r^2)', sp.simplify(rser - 3*lam**2*sp.cos(th)**2) == 0)
AMd2 = sp.diff(AM, th, 2)
rep('S31 A_M = cos^2[1 + M sin^6]: zeros exactly +-pi/2 (bracket >= 1), A_M\'\'/2 = 1 + M there',
    all(sp.simplify(AM.subs(th, z0)) == 0 and sp.simplify(AMd2.subs(th, z0)/2 - (1 + M)) == 0 for z0 in [sp.pi/2, -sp.pi/2]))
rep('S32 A_M = A_0 + M A_* (so Psi_M = Psi_0 + M Psi_*)', sp.simplify(AM - A0 - M*Ast) == 0)
# kernel symmetries: K = (-sin 2t, cos 2t)/(2 pi |Z|^2) <-> K_2 + i K_1 = 1/(2 pi Z^2)
a_, b_ = sp.symbols('a b', real=True)
K = sp.Matrix([-2*a_*b_, a_**2 - b_**2])/(2*sp.pi*(a_**2 + b_**2)**2)
Rx = sp.diag(-1, 1); Ry = sp.diag(1, -1)
rep('S33 K(RZ) = R K(Z) for R = reflection in x; K(R\'Z) = -R\'K(Z) for R\' = reflection in y; R e_2 = e_2, R\' e_2 = -e_2',
    sp.simplify(K.subs({a_: -a_}, simultaneous=True) - Rx*K) == sp.zeros(2, 1) and
    sp.simplify(K.subs({b_: -b_}, simultaneous=True) + Ry*K) == sp.zeros(2, 1))
# scaling
L_ = sp.symbols('L', positive=True)
rep('S34 K homogeneous of degree -2 (W[L^2 rho(./L)](X) = L^2 W[rho](X/L)); grad-perp(L^3 psi(X/L)) = L^2 (grad-perp psi)(X/L)',
    sp.simplify(K.subs({a_: L_*a_, b_: L_*b_}, simultaneous=True) - K/L_**2) == sp.zeros(2, 1) and
    sp.simplify(sp.diff(L_**3*sp.Function('f')(x/L_, y/L_), x) - L_**2*sp.Subs(sp.Derivative(sp.Function('f')(u, s), u), (u, s), (x/L_, y/L_)).doit()) == 0)
rep('S35 grad rho_M in L^q iff q > 4 (int_1^inf r^{-q/2} r dr); K in L^{q\'}(|Z| > 1) iff q\' > 1; outer boundary R^{-2} R^{1/2} R = R^{-1/2}',
    sp.integrate(r**(-sp.Rational(9, 2)/2 + 1), (r, 1, sp.oo)).is_finite and sp.integrate(r**(-2 + 1), (r, 1, sp.oo)) == sp.oo and
    sp.integrate(r**(-2*sp.Rational(11, 10) + 1), (r, 1, sp.oo)).is_finite)
# numeric: m(t)/sqrt(t) -> 2 C_A, band formula, J(0), for A_M, p = 1/2
pnum = 0.5
for Mv in [0.0, 100.0]:
    thg = (np.arange(400000) + 0.5)*2*np.pi/400000
    Ag = np.cos(thg)**2*(1 + Mv*np.sin(thg)**6)
    CA = 2/np.sqrt(1 + Mv)
    m_ = lambda tv: (Ag[None, :] < np.atleast_1d(tv)[:, None]).sum(axis=1)*2*np.pi/len(thg)
    from scipy.optimize import brentq
    gfun = lambda s_, tv: math.sin(s_)**2*(1 + Mv*math.cos(s_)**6) - tv
    def m_small(tv):  # t <= 1e-2: two symmetric intervals |s| < s*(t) about +-pi/2 (A_M(pi/2 + s) = sin^2 s (1 + M cos^6 s), increasing on [0, 0.2])
        return 4*brentq(gfun, 0.0, 0.2, args=(tv,), xtol=1e-16, rtol=1e-15)
    assert all(gfun(0.2, 1e-2) > 0 for _ in [0]) and np.all(np.cos(thg[np.abs(np.abs(thg - np.pi) - np.pi/2) >= 0.2])**2 >= 1e-2)   # g increasing on [0, pi/6)
    tsm = np.array([1e-4, 1e-6, 1e-8])
    mr = np.array([m_small(tv) for tv in tsm])/np.sqrt(tsm)
    # band area in B_R via int_0^R r [m(b/r^p) - m(a/r^p)] dr, a = 0.5, b = 2, R = 1e8
    av, bv, Rv = 0.5, 2.0, 1e8
    rgl, wgl = np.polynomial.legendre.leggauss(40)
    edges = np.concatenate([[0], np.geomspace(1e-2, Rv, 60)])
    tot = 0.0
    for i in range(len(edges) - 1):
        rc = 0.5*(edges[i] + edges[i + 1]) + 0.5*(edges[i + 1] - edges[i])*rgl; wc = 0.5*(edges[i + 1] - edges[i])*wgl
        tot += (wc*rc*(m_(bv/rc**pnum) - m_(av/rc**pnum))).sum()
    pred = 2*CA*(np.sqrt(bv) - np.sqrt(av))*Rv**(2 - pnum/2)/(2 - pnum/2)
    # J(0): |{0 < F < t} in B_R|/(2 sqrt t), t -> 0, R = 1
    tz = 1e-8
    totJ = 0.0
    edgesJ = np.concatenate([[0.0], np.geomspace(1e-12, 1.0, 40)])
    for i in range(len(edgesJ) - 1):
        rc = 0.5*(edgesJ[i] + edgesJ[i + 1]) + 0.5*(edgesJ[i + 1] - edgesJ[i])*rgl; wc = 0.5*(edgesJ[i + 1] - edgesJ[i])*wgl
        mv = np.array([m_small(tz/rv**pnum) if tz/rv**pnum <= 1e-2 else m_(tz/rv**pnum)[0] for rv in rc])
        totJ += (wc*rc*mv).sum()
    totJ /= 2*np.sqrt(tz)
    predJ = CA/(2 - pnum/2)
    rep('S36 M = %g: m(t)/sqrt(t) -> 2C_A = %.8f (t = 1e-4, 1e-6, 1e-8: %s); band area (a,b) = (1/2, 2), R = 1e8 vs formula (rel %.1e); J(0) at R = 1 vs C_A R^{2-p/2}/(2-p/2) (rel %.1e)'
        % (Mv, 2*CA, np.round(mr, 8), abs(tot/pred - 1), abs(totJ/predJ - 1)),
        abs(mr[-1]/(2*CA) - 1) < 1e-6 and abs(tot/pred - 1) < 2e-2 and abs(totJ/predJ - 1) < 1e-5)

if len(sys.argv) > 1 and sys.argv[1] == 'symonly':
    print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok)); sys.exit(0)

# ---------------- Part N ----------------
import torch
dev = 'cuda'; DT = torch.float64
def smooth_step(v):
    v = v.clamp(0, 1)
    A_ = torch.where(v > 0, torch.exp(-1/v.clamp_min(1e-300)), torch.zeros_like(v))
    B_ = torch.where(v < 1, torch.exp(-1/(1 - v).clamp_min(1e-300)), torch.zeros_like(v))
    return A_/(A_ + B_)
def phi(z):  # 1 on [0, 1/2], 0 on [1, inf)
    return smooth_step((1 - z)/0.5)
gl8 = np.polynomial.legendre.leggauss(8); gl12 = np.polynomial.legendre.leggauss(12); gl64 = np.polynomial.legendre.leggauss(64)
def panels(t0, t1, width, glw):
    n = max(1, int(math.ceil((t1 - t0)/width))); edges = np.linspace(t0, t1, n + 1)
    xs, ws = glw; T = []; Wt = []
    for i in range(n):
        c = 0.5*(edges[i] + edges[i + 1]); hw = 0.5*(edges[i + 1] - edges[i]); T.append(c + hw*xs); Wt.append(hw*ws)
    return np.concatenate(T), np.concatenate(Wt)
def make_rho(Mv, homog=False):
    def f(X_, Y_):
        r2 = X_**2 + Y_**2
        if homog:   # F_M = r^{1/2} A_M
            rr_ = torch.sqrt(r2)
            c2 = torch.where(rr_ > 0, X_**2/r2.clamp_min(1e-300), torch.zeros_like(rr_)); s2 = 1 - c2
            return torch.sqrt(rr_)*c2*(1 + Mv*s2**3)
        return X_**2*(1 + r2)**(-0.75)*(1 + Mv*Y_**6/(1 + r2)**3)
    return f
def Wcanon(rho_fn, X0, Y0, nth=2048, nth_near=256):
    xi = complex(X0, Y0); ax = abs(xi); arad = ax/2
    sn_ = 0.5*arad*(gl64[0] + 1); swn = 0.5*arad*gl64[1]
    al_ = 2*math.pi*np.arange(nth_near)/nth_near
    S_ = torch.tensor(sn_, dtype=DT, device=dev)[:, None]; A_ = torch.tensor(al_, dtype=DT, device=dev)[None, :]
    Z = torch.complex(S_*torch.cos(A_), S_*torch.sin(A_)); etaN = xi - Z
    rN = rho_fn(etaN.real, etaN.imag)
    near = (phi(S_/arad)*(rN/Z**2 - rN/etaN**2)*(S_*torch.tensor(swn, dtype=DT, device=dev)[:, None])).sum()*(2*math.pi/nth_near)
    lx = math.log(ax); tmin = math.log(1e-30); tmax = math.log(1e30)
    T1, W1_ = panels(tmin, lx - 2, 0.5, gl12); T2, W2_ = panels(lx - 2, lx + 2, 0.05, gl8); T3, W3_ = panels(lx + 2, tmax, 0.5, gl12)
    Tt = np.concatenate([T1, T2, T3]); Wtt = np.concatenate([W1_, W2_, W3_])
    TH = torch.tensor(2*math.pi*np.arange(nth)/nth, dtype=DT, device=dev)[None, :]
    far = torch.zeros((), dtype=torch.complex128, device=dev)
    for c0 in range(0, len(Tt), 256):
        tt_ = torch.tensor(Tt[c0:c0 + 256], dtype=DT, device=dev)[:, None]; ww = torch.tensor(Wtt[c0:c0 + 256], dtype=DT, device=dev)[:, None]
        R_ = torch.exp(tt_); er = torch.complex(R_*torch.cos(TH), R_*torch.sin(TH))
        rr = rho_fn(er.real, er.imag)
        kern = xi*(2*er - xi)/(er**2*(xi - er)**2)          # = 1/(xi - eta)^2 - 1/eta^2, no cancellation at large |eta|
        cut = 1 - phi((er - xi).abs()/arad)
        far = far + (cut*kern*rr*R_**2*ww).sum()*(2*math.pi/nth)
    Om = (near + far)/(2*math.pi) - rho_fn(torch.tensor(X0, dtype=DT, device=dev), torch.tensor(Y0, dtype=DT, device=dev))/2
    Om = complex(Om.item())
    return Om.imag, Om.real
rep('N0 kernel identity 1/(xi - eta)^2 - 1/eta^2 = xi(2 eta - xi)/(eta^2 (xi - eta)^2)',
    sp.simplify(1/(sp.Symbol('X') - sp.Symbol('E'))**2 - 1/sp.Symbol('E')**2 - sp.Symbol('X')*(2*sp.Symbol('E') - sp.Symbol('X'))/(sp.Symbol('E')**2*(sp.Symbol('X') - sp.Symbol('E'))**2)) == 0)
Psi_f = {0: (sp.lambdify(th, Psi0), sp.lambdify(th, sp.diff(Psi0, th))),
         100: (sp.lambdify(th, Psi0 + 100*Psist), sp.lambdify(th, sp.diff(Psi0 + 100*Psist, th)))}
for Mv in [0, 100]:
    Fh = make_rho(float(Mv), homog=True); errs = []
    for tq in [0.0, 0.4, 1.1, 2.0, -2.7]:
        w1, w2 = Wcanon(Fh, math.cos(tq), math.sin(tq))
        Wr = w1*math.cos(tq) + w2*math.sin(tq); Wt = -w1*math.sin(tq) + w2*math.cos(tq)
        errs.append(max(abs(Wr + Psi_f[Mv][1](tq)), abs(Wt - 1.5*Psi_f[Mv][0](tq))))
    w1, w2 = Wcanon(Fh, 1.0, 0.0)
    rep('N1 M = %d: canonical law of F_M on the unit circle = H_M (5 angles); W_2(1, 0)/(3/2) = %.10f vs Psi_M(0) = %.10f' % (Mv, w2/1.5, Psi_f[Mv][0](0.0)),
        max(errs) < 1e-7, '(max err %.1e)' % max(errs))
# rho_M: axes, small-r behaviour, stream along the positive x-axis
glp = np.polynomial.legendre.leggauss(10)
edges = np.concatenate([[0.0], 2.0**np.arange(-6, 15)])
for Mv in [0, 100]:
    rh = make_rho(float(Mv)); P0 = float(Psi_f[Mv][0](0.0))
    sym = max(max(abs(Wcanon(rh, 0.0, yv)[0]) for yv in [0.7, -3.0, 40.0]), max(abs(Wcanon(rh, xv, 0.0)[0]) for xv in [0.7, 3.0, 40.0]))
    rep('N2 M = %d: W_1(0, y) = 0 and W_1(x, 0) = 0 (three points each)' % Mv, sym < 1e-9, '(max %.1e)' % sym)
    vals = [math.hypot(*Wcanon(rh, sc*0.6, sc*0.8)) for sc in [0.1, 0.05, 0.025]]
    rat = [vals[0]/vals[1], vals[1]/vals[2]]
    rep('N3 M = %d: |W(X)| ~ |X|^2 at 0 (ratios per halving %s), consistent with W(0) = 0, DW(0) = 0' % (Mv, np.round(rat, 3)), all(3.6 < q_ < 4.4 for q_ in rat))
    psi_acc = 0.0; out = []; dev2 = []
    for i in range(len(edges) - 1):
        a0, a1 = edges[i], edges[i + 1]
        xs = 0.5*(a0 + a1) + 0.5*(a1 - a0)*glp[0]; ws = 0.5*(a1 - a0)*glp[1]
        w2s = np.array([Wcanon(rh, float(xv), 0.0)[1] for xv in xs])
        psi_acc += (w2s*ws).sum()
        dev2.extend(list(w2s - 1.5*np.sqrt(xs)*P0))
        out.append((a1, psi_acc))
    tail = [(xv, ps, (ps - P0*xv**1.5)/xv) for xv, ps in out if xv >= 64]
    for xv, ps, d_ in tail[::2]:
        print('   M = %d: x = %8.0f  psi_M(x, 0) = %.8e  psi/x^{3/2} = %.6f  (psi - Psi_M(0) x^{3/2})/x = %.5f' % (Mv, xv, ps, ps/xv**1.5, d_), flush=True)
    dd = [d_ for _, _, d_ in tail]
    inc = [abs(dd[i + 1] - dd[i]) for i in range(len(dd) - 1)]
    signok = all((ps < 0) if Mv == 0 else (ps > 0) for xv, ps, _ in tail)
    dW = np.abs(np.array(dev2))
    rep('N4 M = %d: psi_M(x, 0) = Psi_M(0) x^{3/2} + O(x): d(x) = (psi - Psi_M(0) x^{3/2})/x at x = 2^6..2^14 = %s, increments per doubling %s (contracting); sign %s for x >= 64; |W_2 - (3/2) x^{1/2} Psi_M(0)| max %.4f on [0, 2^14], %.4f on [2^13, 2^14]'
        % (Mv, np.round(dd, 4), np.round(inc, 4), 'negative' if Mv == 0 else 'positive', dW.max(), dW[-10:].max()),
        signok and all(inc[i + 1] <= 0.8*inc[i] + 1e-6 for i in range(len(inc) - 1)))
    # leading coefficient without presupposing Psi_M(0): fit psi = a x^{3/2} + b x + c x^{1/2} + e at x = 2^11..2^14
    # (run 1 used |psi/x^{3/2} - Psi_M(0)| < 5 % at 2^14 instead; for M = 100 the O(x) term, -4.69 x, makes that 6.3 %)
    xf = np.array([xv for xv, _, _ in tail[-4:]]); yf = np.array([ps for _, ps, _ in tail[-4:]])
    cf = np.linalg.solve(np.stack([xf**1.5, xf, xf**0.5, np.ones_like(xf)], 1), yf)
    rep('N4b M = %d: free fit at x = 2^11..2^14: a = %.8f (Psi_M(0) = %.8f, rel %.1e), b = %.5f' % (Mv, cf[0], P0, abs(cf[0] - P0)/abs(P0), cf[1]),
        abs(cf[0] - P0) < 1e-3*abs(P0))
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
