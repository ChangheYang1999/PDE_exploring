"""Checks for the A.3.34 non-profile test and the local transport models (rep4 item 15).

rho = a y (1 + r^2)^(-1/4) (1 - 2 x^2/(1 + r^2)) + 4 tau x^2 y exp(-r^2), tau = -2 + 5a/2, a = +-1, c_l = 2.
Exact: modal form (sin th and sin 3th only), strain c = -1, Theta0, Phi0, limit of U.grad rho on th = pi/4.
Numerical: canonical stream function from the modal Green formulas (1D quadratures), then R, N_v, N_f on th = pi/4.
Models: resonant linear model and flat model satisfy div W = 2 c_l and W.grad rho = rho.
"""
import sympy as sp
import mpmath as mp

x, y, r, th, s = sp.symbols('x y r theta s', real=True)
rp = sp.symbols('rp', positive=True)
cl = 2
p = sp.Rational(1, 2)

for a in (1, -1):
    tau = -2 + sp.Rational(5, 2) * a
    rho = a * y * (1 + x**2 + y**2)**sp.Rational(-1, 4) * (1 - 2 * x**2 / (1 + x**2 + y**2)) \
        + 4 * tau * x**2 * y * sp.exp(-(x**2 + y**2))
    g1 = a * rp * (1 + rp**2)**sp.Rational(-1, 4) * (1 - rp**2 / (2 * (1 + rp**2))) + tau * rp**3 * sp.exp(-rp**2)
    g3 = -sp.Rational(1, 2) * a * rp**3 * (1 + rp**2)**sp.Rational(-5, 4) + tau * rp**3 * sp.exp(-rp**2)
    pol = rho.subs({x: rp * sp.cos(th), y: rp * sp.sin(th)})
    diff = sp.simplify(sp.expand_trig(pol - g1 * sp.sin(th) - g3 * sp.sin(3 * th)))
    a0 = sp.diff(rho, y).subs({x: 0, y: 0})
    strain = sp.simplify(-a0 / 4 + sp.integrate(g3 / rp**2, (rp, 0, sp.oo)))
    print(f'a = {a}: tau = {tau}, modal form exact: {diff == 0}, a0 = {a0}, c = -a0/4 + int rho3 s^-2 = {strain}')
    modal = g1 * sp.sin(th) + g3 * sp.sin(3 * th)
    Theta0 = sp.limit(g1 / rp**p, rp, sp.oo) * sp.sin(th) + sp.limit(g3 / rp**p, rp, sp.oo) * sp.sin(3 * th)
    print('   Theta0 =', sp.simplify(Theta0), ' check a sin th (1 - 2cos^2 th):',
          sp.simplify(Theta0 - a * sp.sin(th) * (1 - 2 * sp.cos(th)**2)) == 0)
    src = sp.simplify(sp.expand_trig(p * sp.cos(th) * Theta0 - sp.sin(th) * sp.diff(Theta0, th)))
    b2 = sp.simplify(sp.integrate(src * sp.sin(2 * th), (th, 0, 2 * sp.pi)) / sp.pi)
    b4 = sp.simplify(sp.integrate(src * sp.sin(4 * th), (th, 0, 2 * sp.pi)) / sp.pi)
    print('   angular source = %s sin 2th + %s sin 4th; remainder %s' %
          (b2, b4, sp.simplify(sp.expand_trig(src - b2 * sp.sin(2 * th) - b4 * sp.sin(4 * th)))))
    Phi0 = b2 / (4 - (p + 1)**2) * sp.sin(2 * th) + b4 / (16 - (p + 1)**2) * sp.sin(4 * th)
    print('   Phi0 =', Phi0, ' ODE residual:',
          sp.simplify(-sp.diff(Phi0, th, 2) - (p + 1)**2 * Phi0 - src))
    lim = sp.simplify(((p + 1) * Phi0 * sp.diff(Theta0, th)).subs(th, sp.pi / 4))
    print('   Theta0\'(pi/4) =', sp.simplify(sp.diff(Theta0, th).subs(th, sp.pi / 4)),
          ' u0th(pi/4) =', sp.simplify(((p + 1) * Phi0).subs(th, sp.pi / 4)),
          ' limit of U.grad rho on th = pi/4:', lim, '=', sp.N(lim))
    # linear residual c_l X.grad rho - rho on the ray, exact asymptotics
    pol = modal
    lin = sp.simplify(cl * rp * sp.diff(pol, rp) - pol)
    linray = sp.simplify(lin.subs(th, sp.pi / 4))
    print('   linear residual on ray ~', sp.simplify(sp.limit(linray * rp**sp.Rational(3, 2), rp, sp.oo)), '* r^(-3/2)')

    # numerical canonical inverse
    F2 = sp.simplify((sp.diff(g1, rp) - g1 / rp) / 2 + sp.diff(g3, rp) / 2 + 3 * g3 / (2 * rp))
    F4 = sp.simplify(sp.diff(g3, rp) / 2 - 3 * g3 / (2 * rp))
    F2f = sp.lambdify(rp, F2, 'mpmath')
    F4f = sp.lambdify(rp, F4, 'mpmath')
    mp.mp.dps = 30

    def modes(R0):
        out = {}
        for m, F in ((2, F2f), (4, F4f)):
            brk = [0, 0.5, 1, 2, 4, 8]
            inner = mp.quad(lambda v: v**(m + 1) * F(v), [b for b in brk if b < R0] + [R0])
            outer = mp.quad(lambda v: v**(1 - m) * F(v), [R0] + [b for b in brk + [16, 64, 256] if b > R0] + [mp.inf])
            P = (R0**(-m) * inner + R0**m * outer) / (2 * m)
            dP = (-R0**(-m - 1) * inner + R0**(m - 1) * outer) / 2
            out[m] = (P, dP)
        return out
    cnum = mp.quad(lambda v: F2f(v) / v, [0, 1, 4, 16, 64, mp.inf]) / 2
    print('   numerical strain psi_xy(0) = (1/2) int F2/s ds =', mp.nstr(cnum, 15))
    grad_r = sp.lambdify((rp, th), sp.diff(pol, rp), 'mpmath')
    grad_t = sp.lambdify((rp, th), sp.diff(pol, th) / rp, 'mpmath')
    rhof = sp.lambdify((rp, th), pol, 'mpmath')
    t0 = mp.pi / 4
    for R0 in (10, 100, 1000, 10000, 100000):
        R0 = mp.mpf(R0)
        md = modes(R0)
        psi_th = 2 * md[2][0] * mp.cos(2 * t0) + 4 * md[4][0] * mp.cos(4 * t0)
        psi_r = md[2][1] * mp.sin(2 * t0) + md[4][1] * mp.sin(4 * t0)
        Ur, Ut = -psi_th / R0, psi_r
        dr_, dt_ = grad_r(R0, t0), grad_t(R0, t0)
        rh = rhof(R0, t0)
        Ugr = Ur * dr_ + Ut * dt_
        linres = cl * R0 * dr_ - rh
        Rres = linres + Ugr
        # Cartesian components for N_f
        ex = (mp.cos(t0), mp.sin(t0)); et = (-mp.sin(t0), mp.cos(t0))
        rx = dr_ * ex[0] + dt_ * et[0]; ry = dr_ * ex[1] + dt_ * et[1]
        U1 = Ur * ex[0] + Ut * et[0]; U2 = Ur * ex[1] + Ut * et[1]
        X1, X2 = R0 * ex[0], R0 * ex[1]
        Nf = abs((cl * X1 + U1) * rx) + abs((cl * X2 + U2) * ry) + abs(rh)
        Nv = abs(rh) + abs(R0 * dr_) + abs(Ugr)
        print('   r=%-8s U.grad rho=%s  lin.res*r^1.5=%s  R=%s  N_v=%s  |R|/N_v=%s  N_f/r^0.5=%s' % (
            mp.nstr(R0, 6), mp.nstr(Ugr, 10), mp.nstr(linres * R0**1.5, 8), mp.nstr(Rres, 10), mp.nstr(Nv, 10),
            mp.nstr(abs(Rres) / Nv, 10), mp.nstr(Nf / mp.sqrt(R0), 10)))
    print('   -6 sqrt2/7 =', mp.nstr(-6 * mp.sqrt(2) / 7, 12), ' predicted N_f/r^0.5 -> c_l |Theta0\'(pi/4)| =',
          mp.nstr(cl * mp.sqrt(2), 10))

# local transport models
S, Nn, C, l, k, lp, lm, c_l = sp.symbols('s n C l k lambda_p lambda_m c_l', positive=True)
W = ((2 * c_l + 3 * C * Nn**2) * S, -C * Nn**3)
rho = S**l * Nn**(3 * l) * sp.exp(-(2 * c_l * l - 1) / (2 * C * Nn**2))
div = sp.simplify(sp.diff(W[0], S) + sp.diff(W[1], Nn))
tr = sp.simplify((W[0] * sp.diff(rho, S) + W[1] * sp.diff(rho, Nn)) / rho)
print('flat model: div W =', div, ', W.grad rho / rho =', tr)
Wl = (lp * S, lm * Nn)
rl = S**l * Nn**k
print('resonant model: div =', sp.simplify(sp.diff(Wl[0], S) + sp.diff(Wl[1], Nn)),
      ', W.grad rho/rho =', sp.simplify((Wl[0] * sp.diff(rl, S) + Wl[1] * sp.diff(rl, Nn)) / rl))
lmv = (1 - 2 * l * c_l) / (k - l)
print('resonance solved: lambda_- =', lmv, ' k lambda_- + l lambda_+ =', sp.simplify(k * lmv + l * (2 * c_l - lmv)))
# item (i): |DU(q)|_op = c_l - lambda_- and the lower bound
kk, ll = sp.symbols('k l', positive=True)
val = c_l - (1 - 2 * ll * c_l) / (kk - ll)
print('|DU(q)| - [c_l + (2 c_l l - 1)/(k - l)] =', sp.simplify(val - (c_l + (2 * c_l * ll - 1) / (kk - ll))))
print('d/dl of (2 c_l l - 1)/(k - l) =', sp.simplify(sp.diff((2 * c_l * ll - 1) / (kk - ll), ll)))
print('value at l = 1 minus c_l - A/(k-1):', sp.simplify(val.subs(ll, 1) - (c_l + (2 * c_l - 1) / (kk - 1))))
