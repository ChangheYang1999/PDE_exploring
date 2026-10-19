"""V151: independent checks of the candidate FR Section 9.8 (working draft, sha 32af3977).
S1  Step 1 on a manufactured density: G = P(x, y) e^{-r^2/2}, rho = -Lap G, psi = G_x (so -Lap psi = rho_x, W = J grad psi
    is the canonical velocity since W(0) = 0 and W decays). P is chosen so that rho(0) = 0, grad rho(0) = 0,
    grad psi(0) = 0, with a generic Hessian of rho at 0 and c, b != 0. Checks int rho phi = pi c,
    int rho r^-3 cos 3th = -pi b, and int (V_s.grad rho - rho) phi = (s - 1) pi c - Q for several s (own quadrature).
S2  Step 2: rescaling exponents (numerically, L = 2), kappa, the quadratic part of the evolution, dc/ds.
S3  Step 3: divergence identity, the m = 2 + p coefficient and the flux limit (sympy).
S4  Step 4: H = J grad(r^{p+1} Psi), div, curl, H.grad F, (Psi A^-k)', the Taylor coefficients, and a direct
    quadrature of the once-subtracted kernel law for F = r^p A compared with H (A with quadratic zeros).
S5  Step 5: translation of the kernel law (contact term rho(P)/2 e_2), M^T H + H M = H, degenerate-zero weights.
S6  Step 6: eigenstructure, covariance, Darcy sign, the f = pi/2 counterexample.
"""
import sys, math
import numpy as np
import sympy as sp

ok = []
def rep(name, cond, extra=''):
    ok.append(bool(cond)); print(('OK   ' if cond else 'FAIL ') + name + (' ' + str(extra) if extra != '' else ''), flush=True)

x, y = sp.symbols('x y', real=True)
r, th = sp.symbols('r theta', positive=True)
# ---------------- S1 ----------------
coef = {}
P = 0
for i in range(5):
    for j in range(5 - i):
        coef[(i, j)] = sp.Symbol('p%d%d' % (i, j)); P += coef[(i, j)]*x**i*y**j
G = P*sp.exp(-(x**2 + y**2)/2)
def d0(expr, i, j):
    return sp.diff(expr, x, i, y, j).subs({x: 0, y: 0}) if (i + j) > 0 else expr.subs({x: 0, y: 0})
LapG = sp.diff(G, x, 2) + sp.diff(G, y, 2)
cons = [d0(LapG, 0, 0), d0(LapG, 1, 0), d0(LapG, 0, 1), d0(G, 1, 0), d0(G, 2, 0), d0(G, 1, 1)]
cons = [sp.simplify(cc) for cc in cons]
sol = sp.solve(cons, [coef[(0, 0)], coef[(1, 0)], coef[(0, 1)], coef[(0, 2)], coef[(1, 1)], coef[(1, 2)]], dict=True)
rep('S1a jet constraints solvable (6 linear conditions)', len(sol) == 1, sol)
vals = {coef[k]: sp.Rational(v) for k, v in zip(sorted(coef), ['0', '3/7', '-2/5', '5/11', '-1/3', '2/9', '7/13', '-3/8', '1/6', '4/9', '-5/7', '3/5', '-1/4', '2/3', '1/2'])}
s0 = {k: v.subs(vals) for k, v in sol[0].items()}
vals.update(s0)
Gn = G.subs(vals)
rho = sp.expand(-(sp.diff(Gn, x, 2) + sp.diff(Gn, y, 2)))
psi = sp.diff(Gn, x)
c_ = d0(psi, 1, 1); b_ = d0(psi, 0, 2)
H0 = sp.Matrix([[d0(rho, 2, 0), d0(rho, 1, 1)], [d0(rho, 1, 1), d0(rho, 0, 2)]])
rep('S1b manufactured rho: rho(0) = 0, grad rho(0) = 0, W(0) = 0, psi_xx(0) = -b',
    d0(rho, 0, 0) == 0 and d0(rho, 1, 0) == 0 and d0(rho, 0, 1) == 0 and d0(psi, 1, 0) == 0 and d0(psi, 0, 1) == 0
    and sp.simplify(d0(psi, 2, 0) + b_) == 0, '(c = %s, b = %s, D2 rho(0) = %s)' % (c_, b_, list(H0)))
rep('S1c generic Hessian (rank 2, off-diagonal != 0) and c, b != 0', H0.det() != 0 and H0[0, 1] != 0 and c_ != 0 and b_ != 0)
W = sp.Matrix([-sp.diff(psi, y), sp.diff(psi, x)])
rep('S1d -Lap psi = rho_x', sp.simplify(-(sp.diff(psi, x, 2) + sp.diff(psi, y, 2)) - sp.diff(rho, x)) == 0)
fr = sp.lambdify((x, y), rho, 'numpy'); frx = sp.lambdify((x, y), sp.diff(rho, x), 'numpy'); fry = sp.lambdify((x, y), sp.diff(rho, y), 'numpy')
fW1 = sp.lambdify((x, y), W[0], 'numpy'); fW2 = sp.lambdify((x, y), W[1], 'numpy')
NR, NT, RMAX = 400, 64, 16.0
gx, gw = np.polynomial.legendre.leggauss(NR)
# panels in r to resolve smoothly
edges = np.linspace(0, RMAX, 9); RR = []; WR = []
for a0, a1 in zip(edges[:-1], edges[1:]):
    RR.append(0.5*(a0 + a1) + 0.5*(a1 - a0)*gx[:80]*0 + 0.5*(a1 - a0)*np.polynomial.legendre.leggauss(80)[0]); WR.append(0.5*(a1 - a0)*np.polynomial.legendre.leggauss(80)[1])
RR = np.concatenate(RR); WR = np.concatenate(WR)
TT = 2*np.pi*np.arange(NT)/NT
Rg, Tg = np.meshgrid(RR, TT, indexing='ij'); Xg = Rg*np.cos(Tg); Yg = Rg*np.sin(Tg)
wA = (WR[:, None]*Rg)*(2*np.pi/NT)   # r dr dth
def integ(F): return float(np.sum(F*wA))
rh = fr(Xg, Yg); rx = frx(Xg, Yg); ry = fry(Xg, Yg); W1 = fW1(Xg, Yg); W2 = fW2(Xg, Yg)
phi = Rg**-3*np.sin(3*Tg)
# grad phi in Cartesian: phi = Im(1/zbar^3)?  use polar: d_r phi = -3 r^-4 sin3th, (1/r) d_th phi = 3 r^-4 cos3th
er = np.stack([np.cos(Tg), np.sin(Tg)]); et = np.stack([-np.sin(Tg), np.cos(Tg)])
gphi = (-3*Rg**-4*np.sin(3*Tg))*er + (3*Rg**-4*np.cos(3*Tg))*et
I = integ(rh*phi); cn = float(c_)
rep('S1e int rho phi = pi c', abs(I - math.pi*cn) < 1e-11, '(I = %.15f, pi c = %.15f)' % (I, math.pi*cn))
I3 = integ(rh*Rg**-3*np.cos(3*Tg)); bn = float(b_)
rep('S1f int rho r^-3 cos 3th = -pi b', abs(I3 + math.pi*bn) < 1e-11, '(%.15f vs %.15f)' % (I3, -math.pi*bn))
Q = integ(rh*(W1*gphi[0] + W2*gphi[1]))
worst = 0.0
for s in [-1.3, 0.0, 0.5 + cn, 2.7]:
    V1 = s*Xg + W1; V2 = s*Yg + W2
    lhs = integ((V1*rx + V2*ry - rh)*phi); rhs = (s - 1)*math.pi*cn - Q
    worst = max(worst, abs(lhs - rhs))
rep('S1g int (V_s.grad rho - rho) phi = (s - 1) pi c - Q for s in {-1.3, 0, 1/2 + c, 2.7}', worst < 1e-10, '(Q = %.12f, max err %.1e)' % (Q, worst))
# check that the inner Green terms are -pi c and +pi c separately (eps -> 0) with psi_2
eps = sp.Symbol('eps', positive=True)
psi2 = (r**2/2)*(c_*sp.sin(2*th) - b_*sp.cos(2*th))
hpol = r**-2*sp.sin(2*th)
t1 = sp.integrate((hpol*(-sp.diff(psi2, r))*r).subs(r, eps), (th, 0, 2*sp.pi))
t2 = sp.integrate((psi2*(-sp.diff(hpol, r))*r).subs(r, eps), (th, 0, 2*sp.pi))
rep('S1h inner Green terms: oint h d_n psi_2 = -pi c, oint psi_2 d_n h = +pi c (n = -e_r)', sp.simplify(t1 + sp.pi*c_) == 0 and sp.simplify(t2 - sp.pi*c_) == 0, (t1, t2))
# full inner boundary terms with the true psi at small eps, numerically
def inner_terms(e):
    tt = 2*np.pi*np.arange(256)/256; X_ = e*np.cos(tt); Y_ = e*np.sin(tt)
    fpx = sp.lambdify((x, y), sp.diff(psi, x), 'numpy'); fpy = sp.lambdify((x, y), sp.diff(psi, y), 'numpy'); fp = sp.lambdify((x, y), psi, 'numpy')
    dnpsi = -(np.cos(tt)*fpx(X_, Y_) + np.sin(tt)*fpy(X_, Y_)); hh = e**-2*np.sin(2*tt); dnh = 2*e**-3*np.sin(2*tt)
    A1 = np.sum(hh*dnpsi)*e*2*np.pi/256; A2 = np.sum(fp(X_, Y_)*dnh)*e*2*np.pi/256
    A0 = np.sum(fr(X_, Y_)*hh*(-np.cos(tt)))*e*2*np.pi/256
    return A0, A1, A2
A0, A1, A2 = inner_terms(1e-4)
rep('S1i true psi at eps = 1e-4: density term ~ 0, oint h d_n psi -> -pi c, oint psi d_n h -> pi c',
    abs(A0) < 1e-3 and abs(A1 + math.pi*cn) < 1e-3 and abs(A2 - math.pi*cn) < 1e-3, '(%.2e, %.6f, %.6f; pi c = %.6f)' % (A0, A1, A2, math.pi*cn))
# ---------------- S2 ----------------
L = 2.0
rhL = L**2*fr(Xg/L, Yg/L); W1L = L**2*fW1(Xg/L, Yg/L); W2L = L**2*fW2(Xg/L, Yg/L)
QL = integ(rhL*(W1L*gphi[0] + W2L*gphi[1])); IL = integ(rhL*phi)
Ls = sp.Integer(2); psiL = Ls**3*psi.subs({x: x/Ls, y: y/Ls})
rep('S2a rescaling L = 2: psi_L = L^3 psi(X/L) solves -Lap psi_L = d_x rho_L, c_L = L c', sp.simplify(-(sp.diff(psiL, x, 2) + sp.diff(psiL, y, 2)) - sp.diff(Ls**2*rho.subs({x: x/Ls, y: y/Ls}), x)) == 0
    and sp.simplify(d0(psiL, 1, 1) - Ls*c_) == 0)
rep('S2b Q_L = L^2 Q and I_L = pi c_L (numerical; RMAX 16 covers the support at L = 2)', abs(QL - L**2*Q) < 1e-9*abs(Q)*10 and abs(IL - math.pi*L*cn) < 1e-9, '(Q_L/Q = %.12f)' % (QL/Q))
pp, cc, ll, bb, kk = sp.symbols('p c l b k', positive=True)
kap = 1 - 1/(2*cc)
rep('S2c kappa = 1 - 1/(2c) = 2(1 - p)/(2 - p) at c = 1/p - 1/2', sp.simplify(kap.subs(cc, 1/pp - sp.Rational(1, 2)) - 2*(1 - pp)/(2 - pp)) == 0)
Qp = sp.pi*cc*(cc - sp.Rational(1, 2))
rep('S2d (s - 1) pi c - Q = 0 at s = l = c + 1/2 gives Q = pi c (c - 1/2)', sp.simplify((cc + sp.Rational(1, 2) - 1)*sp.pi*cc - Qp) == 0)
bs = sp.Symbol('b', real=True)
M0 = (sp.Rational(1, 2) + cc)*sp.eye(2) + sp.Matrix([[-cc, -bs], [-bs, cc]])
Vq = M0*sp.Matrix([x, y]); r2 = x**2
quad = sp.expand(r2 - (Vq[0]*sp.diff(r2, x) + Vq[1]*sp.diff(r2, y)))
rep('S2e quadratic part of rho - V.grad rho for the jet x^2: 2 b x y, i.e. d_s D^2 rho(0) = [[0, 2b], [2b, 0]]',
    sp.simplify(quad - 2*bs*x*y) == 0 and sp.hessian(quad, (x, y)) == sp.Matrix([[0, 2*bs], [2*bs, 0]]))
Qs = sp.Symbol('Q')
dc = -((sp.Rational(1, 2) + cc - 1)*sp.pi*cc - Qs)/sp.pi
rep('S2f dc/ds = -(1/pi)[(s - 1) pi c - Q] at s = 1/2 + c equals c(1/2 - c) + Q/pi', sp.simplify(dc - (cc*(sp.Rational(1, 2) - cc) + Qs/sp.pi)) == 0)
# ---------------- S3 ----------------
m, lsym = sp.symbols('m l', positive=True)
Phi = sp.Function('Phi')
fm = r**(-m)*Phi(th)
# l X.grad f_m = l r d_r f_m
rep('S3a l X.grad f_m = -m l f_m, so div(rho V f_m) = (1 + 2l - m l) rho f_m + rho W.grad f_m', sp.simplify(lsym*r*sp.diff(fm, r) + m*lsym*fm) == 0)
rep('S3b coefficient vanishes at m = 2 + p, p = 1/l', sp.simplify((1 + 2*lsym - m*lsym).subs(m, 2 + 1/lsym)) == 0)
Rr = sp.Symbol('R', positive=True); Afun = sp.Function('A'); Wr = sp.Function('W_r')
Bm = (r**(-(2 + pp))*(lsym*r + Wr(th))*r**pp*Afun(th)*r).subs(r, Rr)   # rho = R^p A on the circle (leading), f = R^{-2-p}, V.e_r = l R + W_r, ds = R dth
rep('S3c flux density on |X| = R at m = 2 + p: l A + R^{-1} W_r A (so -> l int A Phi when W_r = O(R^p))', sp.simplify(Bm - (lsym*Afun(th) + Wr(th)*Afun(th)/Rr)) == 0)
gradf = sp.diff(r**(-(2 + pp)), r)
rep('S3d Phi = 1: W.grad r^{-2-p} = -(2 + p) W_r r^{-3-p}, so int rho W_r r^{-3-p} = -(l/(2 + p)) int A', sp.simplify(gradf + (2 + pp)*r**(-3 - pp)) == 0)
rep('S3e m = 3, Phi = sin 3th: coefficient 1 + 2l - 3l = 1 - l, giving (1 - l) pi c + Q = 0', sp.simplify((1 + 2*lsym - 3*lsym) - (1 - lsym)) == 0)
# ---------------- S4 ----------------
Psi = sp.Function('Psi'); A = sp.Function('A')
lam = pp + 1
fpot = r**lam*Psi(th)
grad_pol = lambda f: (sp.diff(f, r), sp.diff(f, th)/r)          # (e_r, e_th) components
Jg = lambda g: (-g[1], g[0])                                      # J e_r = e_th, J e_th = -e_r
Hh = Jg(grad_pol(fpot))
rep('S4a J grad(r^{p+1} Psi) = r^p(-Psi\' e_r + lambda Psi e_th)', sp.simplify(Hh[0] + r**pp*sp.diff(Psi(th), th)) == 0 and sp.simplify(Hh[1] - lam*r**pp*Psi(th)) == 0)
divH = sp.diff(r*Hh[0], r)/r + sp.diff(Hh[1], th)/r
curlH = sp.diff(r*Hh[1], r)/r - sp.diff(Hh[0], th)/r
rep('S4b div H = 0, curl H = r^{p-1}(Psi\'\' + lambda^2 Psi)', sp.simplify(divH) == 0 and sp.simplify(curlH - r**(pp - 1)*(sp.diff(Psi(th), th, 2) + lam**2*Psi(th))) == 0)
F = r**pp*A(th)
dxF = sp.cos(th)*sp.diff(F, r) - sp.sin(th)/r*sp.diff(F, th)
qq = sp.sin(th)*sp.diff(A(th), th) - pp*sp.cos(th)*A(th)
rep('S4c -d_x F = r^{p-1} q, q = sin th A\' - p cos th A', sp.simplify(-dxF - r**(pp - 1)*qq) == 0)
gF = grad_pol(F)
HgF = sp.simplify(Hh[0]*gF[0] + Hh[1]*gF[1])
Jp = lam*Psi(th)*sp.diff(A(th), th) - pp*sp.diff(Psi(th), th)*A(th)
rep('S4d H.grad F = r^{2p-1} J_p, J_p = lambda Psi A\' - p Psi\' A', sp.simplify(HgF - r**(2*pp - 1)*Jp) == 0)
kq = lam/pp
dd = sp.diff(Psi(th)*A(th)**(-kq), th)
rep('S4e (Psi A^-k)\' = -(1/p) A^{-k-1} J_p, k = (p + 1)/p', sp.simplify(dd + A(th)**(-kq - 1)*Jp/pp) == 0)
rep('S4f k = (p + 1)/p > 2 for 0 < p < 1, so 2k > 4', sp.simplify(kq - 2 - (1 - pp)/pp) == 0)
tt, uu, aa, beta = sp.symbols('t u a beta', real=True)
lamn = sp.Rational(3, 2)  # p = 1/2 for the Taylor check; general p below via series
for (bet, label) in [(sp.pi/3, 'sin beta != 0'), (sp.Integer(0), 'sin beta = 0 (beta = 0)'), (sp.pi, 'sin beta = 0 (beta = pi)')]:
    pass
# general p: q(beta + u) with A(beta + u) = a u^2 + a3 u^3 (C^3 model; the o(u^2) part does not enter the stated orders)
a3 = sp.Symbol('a3', real=True)
Aloc = aa*uu**2 + a3*uu**3
qloc = sp.sin(beta + uu)*sp.diff(Aloc, uu) - pp*sp.cos(beta + uu)*Aloc
Psi0 = sp.integrate(sp.series(sp.sin(lam*(tt - uu))*qloc, uu, 0, 5).removeO().subs(uu, uu), (uu, 0, tt))/lam
Psi0s = sp.series(sp.expand(Psi0), tt, 0, 5).removeO()
c3 = sp.simplify(sp.expand(Psi0s).coeff(tt, 3)); c4_0 = sp.simplify(sp.expand(Psi0s).coeff(tt, 4).subs(beta, 0)); c4_pi = sp.simplify(sp.expand(Psi0s).coeff(tt, 4).subs(beta, sp.pi))
rep('S4g Psi(beta + t) = (a sin beta/3) t^3 + O(t^4)', sp.simplify(c3 - aa*sp.sin(beta)/3) == 0, c3)
rep('S4h sin beta = 0: t^3 coefficient 0 and t^4 coefficient (2 - p) a cos beta/12 (beta = 0, pi)',
    sp.simplify(c3.subs(beta, 0)) == 0 and sp.simplify(c4_0 - (2 - pp)*aa/12) == 0 and sp.simplify(c4_pi + (2 - pp)*aa/12) == 0, (c4_0, c4_pi))
rep('S4i det(I - T) = 2 - 2 cos 2 pi lambda for the rotation monodromy', sp.simplify((sp.Matrix([[1, 0], [0, 1]]) - sp.Matrix([[sp.cos(2*sp.pi*lam), sp.sin(2*sp.pi*lam)], [-sp.sin(2*sp.pi*lam), sp.cos(2*sp.pi*lam)]])).det() - (2 - 2*sp.cos(2*sp.pi*lam))) == 0)
# exterior: W - H = B_0 + T_g -> B_0.grad F = r^{p-1} B_0.(p A e_r + A' e_th)
B1, B2 = sp.symbols('B1 B2', real=True)
Br = B1*sp.cos(th) + B2*sp.sin(th); Bt = -B1*sp.sin(th) + B2*sp.cos(th)
rep('S4j B_0.grad F = r^{p-1} (B_0.e_r p A + B_0.e_th A\'), lower order than r^{2p-1} since p > 0', sp.simplify(Br*gF[0] + Bt*gF[1] - r**(pp - 1)*(Br*pp*A(th) + Bt*sp.diff(A(th), th))) == 0)
rep('S4k l X.grad F = F for p = 1/l', sp.simplify((1/pp)*r*sp.diff(F, r) - F) == 0)

if len(sys.argv) > 1 and sys.argv[1] == 'symonly':
    print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok)); sys.exit(0)

# ---------------- S4 numerics: kernel law for F = r^p A versus H ----------------
def smooth_step(v):
    v = np.clip(v, 0, 1)
    with np.errstate(divide='ignore', over='ignore'):
        Aa = np.where(v > 0, np.exp(-1/np.maximum(v, 1e-300)), 0.0); Bb = np.where(v < 1, np.exp(-1/np.maximum(1 - v, 1e-300)), 0.0)
    return Aa/(Aa + Bb)
def cutphi(u): return smooth_step((1 - u)/0.5)     # 1 on [0, 1/2], 0 on [1, inf)
glS = np.polynomial.legendre.leggauss(64); gl8 = np.polynomial.legendre.leggauss(8); gl12 = np.polynomial.legendre.leggauss(12)
def panels(t0, t1, width, glw):
    n = max(1, int(math.ceil((t1 - t0)/width))); e_ = np.linspace(t0, t1, n + 1); T_ = []; W_ = []
    for i in range(n):
        cm = 0.5*(e_[i] + e_[i + 1]); hw = 0.5*(e_[i + 1] - e_[i]); T_.append(cm + hw*glw[0]); W_.append(hw*glw[1])
    return np.concatenate(T_), np.concatenate(W_)
def kernel_law(dens, X, Rmax=1e6, tmin=-69.0, nth=2048, nth_near=512, tail=None):
    """Once-subtracted law W(X) = p.v. int [K(X - Y) - K(-Y)] dens(Y) dY - dens(X)/2 e_2, complex form
    W_2 + i W_1 = (1/2 pi) p.v. int [1/(xi - eta)^2 - 1/eta^2] dens - dens(X)/2.  tail(xi, Rmax) adds |eta| > Rmax."""
    xi = complex(*X); ax = abs(xi); arad = min(1.0, ax/2)
    sn = 0.5*arad*(glS[0] + 1); swn = 0.5*arad*glS[1]; al_ = 2*np.pi*np.arange(nth_near)/nth_near
    Z = sn[:, None]*np.exp(1j*al_[None, :]); eta = xi - Z
    dN = dens(eta.real, eta.imag)
    near = np.sum(cutphi(sn[:, None]/arad)*(dN/Z**2 - dN/eta**2)*(sn*swn)[:, None])*(2*np.pi/nth_near)
    lx = math.log(ax)
    T1, W1_ = panels(tmin, lx - 2, 0.5, gl12); T2, W2_ = panels(lx - 2, lx + 2, 0.0125, gl8); T3, W3_ = panels(lx + 2, math.log(Rmax), 0.5, gl12)
    Tt = np.concatenate([T1, T2, T3]); Wt = np.concatenate([W1_, W2_, W3_]); thg = 2*np.pi*np.arange(nth)/nth
    far = 0j
    for c0 in range(0, len(Tt), 128):
        R_ = np.exp(Tt[c0:c0 + 128])[:, None]; ww = Wt[c0:c0 + 128][:, None]
        e_ = R_*np.exp(1j*thg[None, :]); dd_ = dens(e_.real, e_.imag)
        ker = 1/(xi - e_)**2 - 1/e_**2
        cut = 1 - cutphi(np.abs(e_ - xi)/arad)
        far += np.sum(cut*ker*dd_*R_**2*ww)*(2*np.pi/nth)
    Om = (near + far)/(2*np.pi) - dens(np.array(X[0]), np.array(X[1]))/2
    if tail is not None: Om += tail(xi, Rmax)
    return float(np.imag(Om)), float(np.real(Om))
pn = 0.5; lamn = pn + 1
Afn = lambda T: np.cos(T)**2*(1 + 0.4*np.sin(T) + 0.2*np.cos(T))
NF = 64; thF = 2*np.pi*np.arange(NF)/NF; Ahat = np.fft.fft(Afn(thF))/NF        # A = sum Ahat_m e^{i m th}
def Fdens(X_, Y_):
    R_ = np.hypot(X_, Y_); T_ = np.arctan2(Y_, X_); return R_**pn*Afn(T_)
def Fdiff(T):  # A' via the Fourier series
    m_ = np.fft.fftfreq(NF, 1/NF); return np.real(sum(Ahat[k]*1j*m_[k]*np.exp(1j*m_[k]*T) for k in range(NF)))
m_ = np.fft.fftfreq(NF, 1/NF)
qv = np.sin(thF)*Fdiff(thF) - pn*np.cos(thF)*Afn(thF); qhat = np.fft.fft(qv)/NF
Psihat = qhat/(lamn**2 - m_**2)
Psi_ = lambda T: np.real(sum(Psihat[k]*np.exp(1j*m_[k]*T) for k in range(NF)))
dPsi_ = lambda T: np.real(sum(Psihat[k]*1j*m_[k]*np.exp(1j*m_[k]*T) for k in range(NF)))
def Hfield(X):
    R_ = math.hypot(*X); T_ = math.atan2(X[1], X[0]); er_ = np.array([math.cos(T_), math.sin(T_)]); et_ = np.array([-math.sin(T_), math.cos(T_)])
    return R_**pn*(-dPsi_(T_)*er_ + lamn*Psi_(T_)*et_)
A3 = Ahat[3]
rep('S4l A = cos^2 th (1 + 0.4 sin th + 0.2 cos th): modes |m| <= 3, quadratic zeros at pi/2, 3pi/2',
    max(abs(Ahat[k]) for k in range(NF) if abs(m_[k]) > 3) < 1e-14 and abs(Afn(np.pi/2)) < 1e-15)
tailF = lambda xi, R: 2*xi*A3*R**(pn - 1)/(1 - pn)
worst = 0.0; lines = []
for X in [(0.7, 0.3), (-1.5, 2.0), (2.5, -0.8), (0.1, -3.0)]:
    w1, w2 = kernel_law(Fdens, X, tail=tailF); Hv = Hfield(X)
    err = max(abs(w1 - Hv[0]), abs(w2 - Hv[1])); worst = max(worst, err)
    lines.append('X = %s: kernel (%.10f, %.10f), H (%.10f, %.10f)' % (X, w1, w2, Hv[0], Hv[1]))
for ln in lines: print('     ' + ln)
rep('S4m once-subtracted kernel law for F = r^p A (p = 1/2) equals H_p[A] at four points', worst < 1e-7, '(max err %.1e)' % worst)
# J_p not identically 0 on either side of the zero pi/2 for this A
tn = np.linspace(-0.2, 0.2, 401); tn = tn[tn != 0]
Jn = lamn*Psi_(np.pi/2 + tn)*Fdiff(np.pi/2 + tn) - pn*dPsi_(np.pi/2 + tn)*Afn(np.pi/2 + tn)
rep('S4n J_p[A] != 0 on both sides of beta = pi/2 for this A', np.max(np.abs(Jn[tn < 0])) > 1e-6 and np.max(np.abs(Jn[tn > 0])) > 1e-6,
    '(max |J_p| left %.3e, right %.3e)' % (np.max(np.abs(Jn[tn < 0])), np.max(np.abs(Jn[tn > 0]))))
# ---------------- S5 ----------------
# translation and the contact term, on the S1 density (exact U = J grad G_x)
Gxn = sp.diff(Gn, x); U1 = sp.lambdify((x, y), -sp.diff(Gxn, y), 'numpy'); U2 = sp.lambdify((x, y), sp.diff(Gxn, x), 'numpy')
Pp = (0.9, -0.4); rhoP = float(fr(*Pp))
fdens = lambda X_, Y_: fr(X_ + Pp[0], Y_ + Pp[1])
worst = 0.0
for z in [(0.5, 0.2), (-0.7, 1.1)]:
    w1, w2 = kernel_law(fdens, z, Rmax=40.0)
    e1 = U1(Pp[0] + z[0], Pp[1] + z[1]) - U1(*Pp); e2 = U2(Pp[0] + z[0], Pp[1] + z[1]) - U2(*Pp) - rhoP/2
    worst = max(worst, abs(w1 - e1), abs(w2 - e2))
rep('S5a kernel law of f = rho(P + .) equals W(P + z) - W(P) - (rho(P)/2) e_2 (rho(P) = %.4f != 0)' % rhoP, worst < 1e-8, '(max err %.1e)' % worst)
rng = np.random.default_rng(7); okM = True
for _ in range(200):
    lam_m, lam_p = sorted(rng.uniform(-2, 4, 2)); Q_, _r = np.linalg.qr(rng.normal(size=(2, 2)))
    Mm = Q_ @ np.diag([lam_m, lam_p]) @ Q_.T
    # solve M^T H + H M = H for symmetric H: linear system in (H11, H12, H22)
    Lmat = []
    for E in [np.array([[1., 0], [0, 0]]), np.array([[0, 1.], [1, 0]]), np.array([[0, 0], [0, 1.]])]:
        Rm = Mm.T @ E + E @ Mm - E; Lmat.append([Rm[0, 0], Rm[0, 1], Rm[1, 1]])
    Lmat = np.array(Lmat).T; sv = np.linalg.svd(Lmat, compute_uv=False)
    nnull = int(np.sum(sv < 1e-10))
    expect = sum(1 for (a_, b_) in [(lam_m, lam_m), (lam_m, lam_p), (lam_p, lam_p)] if abs(a_ + b_ - 1) < 1e-10)
    okM &= (nnull == expect)
rep('S5b M^T H + H M = H for symmetric M has a nonzero symmetric solution only if lambda_i + lambda_j = 1 (200 random M)', okM)
ls_, Ms_ = sp.symbols('l m', positive=True)
lam_minus = sp.Rational(1, 2)
Hs = sp.Matrix([[sp.Symbol('h11'), sp.Symbol('h12')], [sp.Symbol('h12'), sp.Symbol('h22')]])
Md = sp.diag(lam_minus, 2*ls_ - lam_minus)
eqs = sp.simplify(Md.T*Hs + Hs*Md - Hs)
rep('S5c with eigenvalues 1/2 and 2l - 1/2 (l > 1): H12 = H22 = 0, H11 free', sp.solve([eqs[0, 1], eqs[1, 1]], [sp.Symbol('h12'), sp.Symbol('h22')]) == {sp.Symbol('h12'): 0, sp.Symbol('h22'): 0} and eqs[0, 0] == 0)
u_, v_ = sp.symbols('u v', real=True); nn = 5
fnn = sum(sp.Symbol('a%d' % j)*u_**(nn - j)*v_**j for j in range(nn + 1))
eqd = sp.expand(2*ls_*v_*sp.diff(fnn, v_) - fnn)
rep('S5d degenerate zero: 2l v d_v f_n - f_n = sum (2lj - 1) a_j u^{n-j} v^j (n = 5)', all(sp.simplify(eqd.coeff(u_, nn - j).coeff(v_, j) - (2*ls_*j - 1)*sp.Symbol('a%d' % j)) == 0 for j in range(nn + 1)))
okj = all(abs(2*lv*j - 1) > 1e-12 for lv in np.linspace(1.0001, 50, 2000) for j in range(0, 12))
rep('S5e 2lj - 1 != 0 for every integer j >= 0 when l > 1 (grid)', okj)
# ---------------- S6 ----------------
fa = sp.Symbol('f', real=True)
e = sp.Matrix([sp.cos(fa), sp.sin(fa)]); Je = sp.Matrix([-sp.sin(fa), sp.cos(fa)]); kk_ = ls_ - sp.Rational(1, 2)
cf = kk_*sp.cos(2*fa); bf = kk_*sp.sin(2*fa)
Mf = ls_*sp.eye(2) + sp.Matrix([[-cf, -bf], [-bf, cf]])
rep('S6a c = k cos 2f, b = k sin 2f give M e = e/2 and M Je = (2l - 1/2) Je', sp.simplify(Mf*e - e/2) == sp.zeros(2, 1) and sp.simplify(Mf*Je - (2*ls_ - sp.Rational(1, 2))*Je) == sp.zeros(2, 1))
rep('S6b DW(0) = k (I - 2 e e^T)', sp.simplify(sp.Matrix([[-cf, -bf], [-bf, cf]]) - kk_*(sp.eye(2) - 2*e*e.T)) == sp.zeros(2))
cg, bg = sp.symbols('cg bg', real=True)
Mg = ls_*sp.eye(2) + sp.Matrix([[-cg, -bg], [-bg, cg]])
Xv = sp.Matrix([x, y]); eX = (e.T*Xv)[0]
qd = sp.expand(sp.expand_trig(2*eX*(e.T*Mg*Xv)[0] - eX**2))
solcb = sp.solve([qd.coeff(x, 2), qd.coeff(x, 1).coeff(y, 1)], [cg, bg], dict=True)
rep('S6c conversely the quadratic equation 2 (e.X)(e.MX) = (e.X)^2 forces c = k cos 2f, b = k sin 2f', len(solcb) == 1 and sp.simplify(solcb[0][cg] - cf) == 0 and sp.simplify(solcb[0][bg] - bf) == 0
    and sp.simplify(qd.subs(solcb[0])) == 0, solcb)
# covariance on the manufactured density, f = 0.7
fv = 0.7; Rf = sp.Matrix([[sp.cos(fv), -sp.sin(fv)], [sp.sin(fv), sp.cos(fv)]])
zz = Rf*sp.Matrix([x, y])
rt = rho.subs({x: zz[0], y: zz[1]}, simultaneous=True); pt = psi.subs({x: zz[0], y: zz[1]}, simultaneous=True)
lhs = -(sp.diff(pt, x, 2) + sp.diff(pt, y, 2)); rhs = math.cos(fv)*sp.diff(rt, x) - math.sin(fv)*sp.diff(rt, y)
fl = sp.lambdify((x, y), lhs - rhs, 'numpy')
Wt_ = sp.Matrix([-sp.diff(pt, y), sp.diff(pt, x)]); Wrot = Rf.T*W.subs({x: zz[0], y: zz[1]}, simultaneous=True)
fw = sp.lambdify((x, y), list(Wt_ - Wrot), 'numpy')
pts_ = rng.normal(size=(20, 2))*1.5
e_cov = max(abs(fl(*pq)) for pq in pts_); e_w = max(max(abs(np.array(fw(*pq)))) for pq in pts_)
rep('S6d -Lap psi~ = cos f d_1 rho~ - sin f d_2 rho~ and J grad psi~ = R_{-f} W(R_f z) (f = 0.7, 20 points)', e_cov < 1e-9 and e_w < 1e-9, '(%.1e, %.1e)' % (e_cov, e_w))
q1, q2 = sp.symbols('q1 q2', real=True); Pf = sp.Function('Pr')(x, y); rf_ = sp.Function('rho')(x, y)
Ud = sp.Matrix([-sp.diff(Pf, x) - rf_*q1, -sp.diff(Pf, y) - rf_*q2])
curlU = sp.diff(Ud[1], x) - sp.diff(Ud[0], y)
Jm = sp.Matrix([[0, -1], [1, 0]]); mJq = -Jm*sp.Matrix([q1, q2])
rep('S6e Darcy U = -grad P - rho q, U = J grad psi: -Lap psi = -curl U = (-J q).grad rho', sp.simplify(-curlU - (mJq[0]*sp.diff(rf_, x) + mJq[1]*sp.diff(rf_, y))) == 0)
qrot = sp.Matrix([[sp.cos(-fa), -sp.sin(-fa)], [sp.sin(-fa), sp.cos(-fa)]])*sp.Matrix([0, 1])
rep('S6f q = e_2 gives -Lap psi = rho_x; q = R_{-f} e_2 gives -J q = (cos f, -sin f) = R_{-f} e_1', sp.simplify(-Jm*sp.Matrix([0, 1]) - sp.Matrix([1, 0])) == sp.zeros(2, 1) and sp.simplify(-Jm*qrot - sp.Matrix([sp.cos(fa), -sp.sin(fa)])) == sp.zeros(2, 1))
R90 = sp.Matrix([[0, -1], [1, 0]]); zr = R90*sp.Matrix([u_, v_])
rt2 = (x**2).subs({x: zr[0], y: zr[1]}, simultaneous=True)
rep('S6g f = pi/2: rho = x^2 gives rho~ = v^2, -d_v rho~ = -2v while d_u rho~ = 0', sp.simplify(rt2 - v_**2) == 0 and sp.diff(rt2, u_) == 0 and -sp.diff(rt2, v_) == -2*v_)
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
