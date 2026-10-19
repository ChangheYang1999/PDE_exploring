"""V154: checks of FR Section 9.9 (Propositions 3.6 and 3.14), lead item 17.
Part S (sympy): the axis kernel q, P_x, K_x = d_x d_t P_x, 2 d_t q = -K_x, scaling, Fourier transforms of P_x and K_x,
the k / -k pairing, the convergence integrals, the Step 5 integration (first integral, h, b, sign of b), the
integrated identities and the twice-subtracted pairing.
Part N (numerics, own quadrature, CPU numpy): a manufactured x-even density rho = -Lap G with rho = 0 on the axis,
stream function psi = G_x (so w'(y) = G_xxy(0, y) exactly), and
  N1  w'(y) = -int_0^inf int rho(x, z) K_x(y - z) dz dx   (physical-space quadrature)
  N2  int h w' dy = int_0^inf int rho (K_x * h) dz dx      (Step 3, before Fourier)
  N3  int h w' dy = -(1/pi) int_0^inf int_0^inf k^2 e^{-kx} Im(rho^(x, k) conj h^(k)) dk dx   (Proposition 3.6 formula)
  N4  the same for a density symmetric about a common height y_0: both sides 0
  N5  the canonical once-subtracted law (own polar quadrature) gives the same w'(y) as G_xxy(0, y)
"""
import sys, math
import numpy as np
import sympy as sp

ok = []
def rep(name, cond, extra=''):
    ok.append(bool(cond)); print(('OK   ' if cond else 'FAIL ') + name + (' ' + str(extra) if extra != '' else ''), flush=True)

# ---------------- Part S ----------------
x, t, k, y, a = sp.symbols('x t k y a', real=True)
xp, kp, s = sp.symbols('xp kp s', positive=True)
P = xp/(sp.pi*(xp**2 + t**2))
q = (a**2 - t**2)/(2*sp.pi*(a**2 + t**2)**2)
Kx = 2*t*(3*xp**2 - t**2)/(sp.pi*(xp**2 + t**2)**3)
th = sp.symbols('th', real=True)
K2 = sp.cos(2*th)/(2*sp.pi)   # times |Z|^-2: vertical component of K at Z = (a, t)
rep('S1 q(a, t) = cos(2 th_Z)/(2 pi |Z|^2) at Z = (a, t)', sp.simplify(q - (a**2 - t**2)/(a**2 + t**2)/(2*sp.pi*(a**2 + t**2))) == 0)
rep('S2 q(x, t) = -(1/2) d_x P_x(t)', sp.simplify(q.subs(a, xp) + sp.diff(P, xp)/2) == 0)
rep('S3 K_x = d_x d_t P_x = 2t(3x^2 - t^2)/(pi(x^2 + t^2)^3)', sp.simplify(sp.diff(P, xp, t) - Kx) == 0)
rep('S4 2 d_t q(x, t) = -K_x(t)', sp.simplify(2*sp.diff(q.subs(a, xp), t) + Kx) == 0)
rep('S5 K_x odd, K_x(t) = x^-3 K_1(t/x)', sp.simplify(Kx.subs(t, -t) + Kx) == 0 and sp.simplify(Kx - Kx.subs(xp, 1).subs(t, t/xp)/xp**3) == 0)
K1 = Kx.subs(xp, 1)
L1 = sp.integrate(sp.Abs(K1), (t, -sp.oo, sp.oo)) if False else 2*sp.integrate(K1, (t, 0, sp.sqrt(3))) - 2*sp.integrate(K1, (t, sp.sqrt(3), sp.oo))
rep('S6 ||K_1||_1 finite (sign change at t = 3^{1/2})', L1.is_finite and float(L1) > 0, sp.nsimplify(sp.simplify(L1)))
# Fourier transform of P_x: (2 pi)^-1 int e^{ikt} e^{-x|k|} dk = P_x(t)
FP = (sp.integrate(sp.exp(sp.I*kp*t - xp*kp), (kp, 0, sp.oo), conds='none') + sp.integrate(sp.exp(-sp.I*kp*t - xp*kp), (kp, 0, sp.oo), conds='none'))/(2*sp.pi)
rep('S7 P_x(t) = (2 pi)^-1 int e^{ikt} e^{-x|k|} dk', sp.simplify(FP - P) == 0)
# hat K_x(k) = (ik)(-|k|) e^{-x|k|}: check (2 pi)^-1 int (-ik|k|) e^{-x|k|} e^{ikt} dk = K_x(t)
FK = (sp.integrate(-sp.I*kp*kp*sp.exp(sp.I*kp*t - xp*kp), (kp, 0, sp.oo), conds='none')
      + sp.integrate(sp.I*kp*kp*sp.exp(-sp.I*kp*t - xp*kp), (kp, 0, sp.oo), conds='none'))/(2*sp.pi)
rep('S8 K_x(t) = (2 pi)^-1 int (-ik|k|) e^{-x|k|} e^{ikt} dk', sp.simplify(sp.expand_complex(FK) - Kx) == 0)
# pairing of k and -k: i k|k| e^{-x|k|} A(k) at k and -k with A(-k) = conj A(k)
Ar, Ai = sp.symbols('Ar Ai', real=True); A_ = Ar + sp.I*Ai
pair = sp.I*kp*kp*sp.exp(-xp*kp)*A_ + sp.I*(-kp)*kp*sp.exp(-xp*kp)*sp.conjugate(A_)
rep('S9 k and -k contributions add to -2 k^2 e^{-xk} Im A', sp.simplify(pair + 2*kp**2*sp.exp(-xp*kp)*Ai) == 0)
rep('S10 int_0^inf k e^{-kx} dk = x^-2, int_0^inf k^2 e^{-kx} dk = 2 x^-3',
    sp.simplify(sp.integrate(kp*sp.exp(-kp*xp), (kp, 0, sp.oo)) - xp**-2) == 0 and sp.simplify(sp.integrate(kp**2*sp.exp(-kp*xp), (kp, 0, sp.oo)) - 2*xp**-3) == 0)
gam = sp.symbols('p', positive=True)
rep('S11 int_R (1 + x + |z|)^{p-2} dz = 2 (1 + x)^{p-1}/(1 - p) (p = 1/3 sample)',
    sp.simplify(2*sp.integrate((1 + xp + s)**(sp.Rational(1, 3) - 2), (s, 0, sp.oo)) - 2*(1 + xp)**(sp.Rational(1, 3) - 1)/(1 - sp.Rational(1, 3))) == 0)
# Step 5
l = sp.symbols('l', positive=True); be = 2*l - sp.Rational(1, 2)
B = sp.Function('B')
expr = B(y)*sp.diff(B(y), y, 2) - sp.Rational(3, 2)*sp.diff(B(y), y)**2 + 2*be*sp.diff(B(y), y)
rep('S12 d/dy [b b\'\' - (3/2) b\'^2 + 2 beta b\'] = b b\'\'\' - 2 (b\' - beta) b\'\'',
    sp.simplify(sp.diff(expr, y) - (B(y)*sp.diff(B(y), y, 3) - 2*(sp.diff(B(y), y) - be)*sp.diff(B(y), y, 2))) == 0)
rep('S13 1 - 4l + 2b\' = 2(b\' - beta) and 1 - 4l + 2b\' = 1 - 2l + 2w\' (b\' = l + w\')',
    sp.simplify(1 - 4*l + 2*sp.Symbol('bp') - 2*(sp.Symbol('bp') - be)) == 0 and sp.simplify((1 - 4*l + 2*(l + sp.Symbol('wp'))) - (1 - 2*l + 2*sp.Symbol('wp'))) == 0)
qq = sp.symbols('q')
rep('S14 at y = 0: first integral = beta^2/2; with b\' = beta + q it gives b b\'\' = q(2 beta + 3q)/2',
    sp.simplify(-sp.Rational(3, 2)*be**2 + 2*be*be - be**2/2) == 0 and
    sp.simplify(be**2/2 + sp.Rational(3, 2)*(be + qq)**2 - 2*be*(be + qq) - qq*(2*be + 3*qq)/2) == 0)
hS = 2*be**4/(be + y)**4; bS = be*(be + y)/3 - be**4/(3*(be + y)**2)
rep('S15 h = 2 beta^4/(beta + y)^4, b = beta(beta + y)/3 - beta^4/(3(beta + y)^2): b\'\' = -h, b h\' = 2(b\' - beta) h',
    sp.simplify(sp.diff(bS, y, 2) + hS) == 0 and sp.simplify(bS*sp.diff(hS, y) - 2*(sp.diff(bS, y) - be)*hS) == 0)
rep('S16 b(0) = 0, b\'(0) = beta, h(0) = 2, first integral equals beta^2/2 identically',
    sp.simplify(bS.subs(y, 0)) == 0 and sp.simplify(sp.diff(bS, y).subs(y, 0) - be) == 0 and sp.simplify(hS.subs(y, 0) - 2) == 0 and
    sp.simplify(bS*sp.diff(bS, y, 2) - sp.Rational(3, 2)*sp.diff(bS, y)**2 + 2*be*sp.diff(bS, y) - be**2/2) == 0)
qS = sp.diff(bS, y) - be
rep('S17 h = 2 (1 + 3q/(2 beta))^{4/3}  and  a = (1 + 3q/(2 beta))^{-1/3} = 1 + y/beta',
    sp.simplify((1 + 3*qS/(2*be)) - ((be + y)/be)**-3) == 0)
tt, bP = sp.symbols('tt bP', positive=True)
rep('S18 b = beta (t^3 - beta^3)/(3 t^2), t = beta + y: b < 0 on (-beta, 0), b -> -inf as y -> -beta',
    sp.simplify(bS.subs(y, tt - be) - be*(tt**3 - be**3)/(3*tt**2)) == 0 and
    sp.limit((bP*(tt**3 - bP**3)/(3*tt**2)), tt, 0, '+') == -sp.oo)
okb = True
for lv in [1.01, 1.3, 2.0, 5.0]:
    bev = 2*lv - 0.5
    for yv in np.linspace(-bev*0.999, -1e-6, 400):
        okb &= float(bS.subs({l: lv, y: yv})) < 0 and float(qS.subs({l: lv, y: yv})) > 0
rep('S19 b < 0 and q = b\' - beta > 0 on (-beta, 0) (grid, four l)', okb)
c_ = l - sp.Rational(1, 2); Ih_m, Ih = sp.symbols('Ihm Ih')
rep('S20 l - beta = -c; int_{-inf}^0 g = -c - int_{-inf}^0 h; int_0^inf g = c - int_0^inf h; sum = -int h',
    sp.simplify(l - be + c_) == 0 and sp.simplify((-c_ - Ih_m) + (c_ - (Ih - Ih_m)) + Ih) == 0)
rep('S21 int h (w\' - c) = ((l - 1)/3 - c) int h = -(beta/3) int h', sp.simplify((l - 1)/3 - c_ + be/3) == 0)

if len(sys.argv) > 1 and sys.argv[1] == 'symonly':
    print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok)); sys.exit(0)

# ---------------- Part N ----------------
X, Y = sp.symbols('X Y', real=True)
def manufactured(fexpr, f2=0):
    """G = e^{-X^2} (f + X^2 (f - f''/2)) + X^4 e^{-2 X^2} f2: rho = -Lap G is x-even with rho(0, y) = 0.
    With f2 = 0 every Fourier transform in y is a real multiple of f^(k), so rho(x, .) = mu_x * h (excluded class)."""
    G = sp.exp(-X**2)*(fexpr + X**2*(fexpr - sp.diff(fexpr, Y, 2)/2)) + X**4*sp.exp(-2*X**2)*f2
    rho = sp.simplify(-(sp.diff(G, X, 2) + sp.diff(G, Y, 2)))   # simplify factors out X^2 (no cancellation at small x)
    assert sp.simplify(rho.subs(X, 0)) == 0
    h = sp.simplify(sp.diff(rho, X, 2).subs(X, 0))
    wp = sp.simplify(sp.diff(G, X, 2, Y, 1).subs(X, 0))       # w'(y) = d_y v(0, y), v = G_xx - G_xx(0)
    # the simplified forms contain growing exponentials times decaying ones: evaluate only on |X| <= 20, |Y| <= 40, where both
    # are finite in double precision, and return 0 outside (all functions are below e^{-1000} there)
    def clampXY(fn):
        return lambda XX, YY: np.where((np.abs(XX) <= 20) & (np.abs(YY) <= 40), fn(np.clip(XX, -20, 20), np.clip(YY, -40, 40)), 0.0)
    def clampY(fn):
        return lambda YY: np.where(np.abs(YY) <= 40, fn(np.clip(YY, -40, 40)), 0.0)
    return (clampXY(sp.lambdify((X, Y), rho, 'numpy')), clampY(sp.lambdify(Y, h, 'numpy')), clampY(sp.lambdify(Y, wp, 'numpy')),
            sp.lambdify((X, Y), sp.diff(G, X, 2), 'numpy'))
f_asym = sp.exp(-(Y - sp.Rational(3, 10))**2)*(1 + Y/2 + Y**2/5)
f_sym = sp.exp(-(Y - sp.Rational(3, 10))**2)*(1 + (Y - sp.Rational(3, 10))**2/3)
f_2 = sp.exp(-(Y + sp.Rational(4, 5))**2)*(1 - Y)
gl = np.polynomial.legendre.leggauss(20)
def gl_panels(edges, glw=gl):
    xs, ws = glw; T = []; Wt = []
    for i in range(len(edges) - 1):
        c = 0.5*(edges[i] + edges[i + 1]); hw = 0.5*(edges[i + 1] - edges[i]); T.append(c + hw*xs); Wt.append(hw*ws)
    return np.concatenate(T), np.concatenate(Wt)
xg, xw = gl_panels(np.concatenate([[0.0], np.geomspace(1e-7, 1.0, 36), np.linspace(1.0, 9.0, 33)[1:]]))
tg, tw = gl_panels(np.concatenate([[0.0], np.geomspace(1e-10, 1.0, 50), np.linspace(1.0, 12.0, 45)[1:], np.geomspace(12.0, 1e5, 25)[1:]]))
yg, yw = gl_panels(np.linspace(-12.0, 12.0, 97))
def Kx_np(xx, tt_):
    return 2*tt_*(3*xx**2 - tt_**2)/(math.pi*(xx**2 + tt_**2)**3)
def wprime_kernel(rho_f, yv):
    # -int_0^inf int rho(x, z) K_x(y - z) dz dx, z = y - t, K_x odd: int_0^inf [rho(x, y - t) - rho(x, y + t)] K_x(t) dt
    XX = xg[:, None]; TT = tg[None, :]
    inner = ((rho_f(XX, yv - TT) - rho_f(XX, yv + TT))*Kx_np(XX, TT)*tw[None, :]).sum(axis=1)
    return -(inner*xw).sum()
def run_case(name, fexpr, f2=0, expect_zero=False):
    rho_f, h_f, wp_f, Gxx_f = manufactured(fexpr, f2)
    # N1
    errs = []
    for yv in [-1.3, -0.2, 0.0, 0.7, 2.1]:
        A1 = wprime_kernel(rho_f, yv); A0 = float(wp_f(yv)); errs.append(abs(A1 - A0))
    rep('N1 %s: w\'(y) kernel formula = G_xxy(0, y) at 5 heights' % name, max(errs) < 1e-8, '(max err %.1e)' % max(errs))
    # LHS int h w'
    hy = h_f(yg); lhs = (hy*wp_f(yg)*yw).sum()
    # N2: int_0^inf int rho(x, z) (K_x * h)(z) dz dx, (K_x * h)(z) = int K_x(t) h(z - t) dt = int_0^inf K_x(t)[h(z - t) - h(z + t)] dt
    hdiff = h_f(yg[:, None] - tg[None, :]) - h_f(yg[:, None] + tg[None, :])          # (ny, nt)
    conv = hdiff @ (Kx_np(xg[:, None], tg[None, :])*tw[None, :]).T                     # (ny, nx): (K_x * h)(z)
    tot = ((rho_f(xg[None, :], yg[:, None])*conv*yw[:, None]).sum(axis=0)*xw).sum()
    rep('N2 %s: int h w\' = int_0^inf int rho (K_x * h) dz dx' % name, abs(lhs - tot) < 1e-8*max(1, abs(lhs)), '(%.12f vs %.12f)' % (lhs, tot))
    # N3: Fourier formula
    kg, kw = gl_panels(np.concatenate([[0.0], np.geomspace(1e-4, 1.0, 13)[0:], np.linspace(1.0, 40.0, 79)[1:]]))
    if kg[0] > 0: pass
    E = np.exp(-1j*np.outer(kg, yg))                                   # e^{-iky}
    hhat = E @ (h_f(yg)*yw)
    R = rho_f(xg[:, None], yg[None, :])                                # (nx, ny)
    rhat = (R*yw[None, :]) @ E.T                                       # (nx, nk)
    ImA = np.imag(rhat*np.conj(hhat)[None, :])
    integrand = (kg[None, :]**2*np.exp(-np.outer(xg, kg))*ImA*kw[None, :]).sum(axis=1)
    rhs = -(integrand*xw).sum()/math.pi
    rep('N3 %s: int h w\' = -(1/pi) int int k^2 e^{-kx} Im(rho^ conj h^) dk dx' % name, abs(lhs - rhs) < 1e-7*max(1, abs(lhs)), '(%.12f vs %.12f)' % (lhs, rhs))
    if expect_zero:
        rep('N4 %s: excluded class: both sides 0 and A_x(k) = rho^ conj h^ real' % name, abs(lhs) < 1e-10 and abs(rhs) < 1e-10 and
            np.abs(ImA).max() < 1e-10*np.abs(rhat*np.conj(hhat)[None, :]).max(), '(lhs %.1e, rhs %.1e, max|Im A| %.1e)' % (lhs, rhs, np.abs(ImA).max()))
    else:
        rep('N4 %s: the pairing is nonzero (nontrivial test)' % name, abs(lhs) > 1e-3, '(%.6f)' % lhs)
    return rho_f, wp_f, Gxx_f
rho_a, wp_a, Gxx_a = run_case('generic (f, f2)', f_asym, f2=f_2)
run_case('separable asymmetric (mu_x * h class)', f_asym, expect_zero=True)
run_case('symmetric about y_0 = 0.3', f_sym, f2=f_2 + f_2.subs(Y, sp.Rational(3, 5) - Y), expect_zero=True)

# N5: canonical once-subtracted law on the axis, own polar quadrature with a smooth near/far partition
# (complex form W_2 + i W_1 = (1/2pi) pv int [1/(xi-eta)^2 - 1/eta^2] rho - rho(xi)/2)
def smooth_step(v):
    v = np.clip(v, 0, 1)
    with np.errstate(divide='ignore', over='ignore'):
        A = np.where(v > 0, np.exp(-1/np.maximum(v, 1e-300)), 0.0); B_ = np.where(v < 1, np.exp(-1/np.maximum(1 - v, 1e-300)), 0.0)
    return A/(A + B_)
def phi(u):  # 1 on [0, 1/2], 0 on [1, inf)
    return smooth_step((1 - u)/0.5)
def W_canon(rho_f, X0, Y0, Rmax=40.0, arad=0.5):
    xi = complex(X0, Y0)
    gn = np.polynomial.legendre.leggauss(100)
    sn = 0.5*arad*(gn[0] + 1); swn = 0.5*arad*gn[1]; na = 256; al = 2*math.pi*np.arange(na)/na
    Z = sn[:, None]*np.exp(1j*al[None, :]); eta = xi - Z
    rN = rho_f(eta.real, eta.imag)
    with np.errstate(divide='ignore', invalid='ignore'):
        near = (phi(sn/arad)[:, None]*(rN/Z**2 - np.where(np.abs(eta) > 0, rN/eta**2, 0))*(sn*swn)[:, None]).sum()*(2*math.pi/na)
    rg, rw = gl_panels(np.concatenate([[0.0], np.geomspace(1e-4, 0.0625, 10), np.linspace(0.0625, 4.0, 64)[1:], np.linspace(4.0, Rmax, 145)[1:]]))
    nth = 2048; thv = 2*math.pi*np.arange(nth)/nth
    E = rg[:, None]*np.exp(1j*thv[None, :])
    rr = rho_f(E.real, E.imag); cut = 1 - phi(np.abs(E - xi)/arad)
    with np.errstate(divide='ignore', invalid='ignore'):
        integ = np.where(cut > 0, cut*(1/(xi - E)**2 - 1/E**2)*rr, 0)
    far = (integ*(rg*rw)[:, None]).sum()*(2*math.pi/nth)
    Om = (near + far)/(2*math.pi) - rho_f(X0, Y0)/2
    return Om.imag, Om.real
errs = []; vals = []
for yv in [-1.0, 0.7, 1.6]:
    u0, v0 = W_canon(rho_a, 0.0, yv); vex = float(Gxx_a(0.0, yv) - Gxx_a(0.0, 0.0)); errs.append(max(abs(v0 - vex), abs(u0))); vals.append((v0, vex))
rep('N5 canonical law (own quadrature, generic case) on the axis: u = 0 and v(0, y) = G_xx(0, y) - G_xx(0, 0)',
    max(errs) < 1e-8, '(%s; max err %.1e)' % (', '.join('%.9f/%.9f' % vv for vv in vals), max(errs)))
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
