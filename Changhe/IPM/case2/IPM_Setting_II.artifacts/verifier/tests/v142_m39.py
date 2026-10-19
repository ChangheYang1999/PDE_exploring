"""V142: checks of specification M39 and a working note (growth classes 1 <= gamma < 2).
Part A (sympy): complex kernel, twice-subtracted remainder, bound integrals, gauge, jet forcing of M, the inequality
gamma lambda_+ >= 1, the polynomial and layered families, the f(x) and f(x) + h(y) nonexistence.
Part B (numerics, own quadrature on the GPU): the twice-subtracted law
    W_2(X) = p.v. int [K(X - Y) - K(-Y) - DK(-Y) X] rho(Y) dY - (rho(X)/2) e_2
evaluated for rho = f(x) (exact W_2 = (0, -f(x))), rho = h(y) (exact W_2 = 0), and, for a non-separable density, the
finite-difference divergence and curl (curl must be -rho_x) and DW_2(0) = 0.
Complex form: K_2 + i K_1 = 1/(2 pi w^2); remainder 1/(xi - eta)^2 - 1/eta^2 - 2 xi/eta^3 = xi^2 (3 eta - 2 xi)/(eta^3 (xi - eta)^2).
"""
import sys, json, math
import numpy as np
import sympy as sp

ok = []
def rep(name, cond, extra=''):
    ok.append(bool(cond)); print(('OK   ' if cond else 'FAIL ') + name + (' ' + str(extra) if extra != '' else ''), flush=True)

# ---------------- Part A ----------------
a, b, x, y, l, g, H, al, gam, e = sp.symbols('a b x y l g H alpha gamma epsilon', real=True)
w = a + sp.I*b
K1 = -2*a*b/(2*sp.pi*(a**2 + b**2)**2); K2 = (a**2 - b**2)/(2*sp.pi*(a**2 + b**2)**2)
rep('A1 K_2 + i K_1 = 1/(2 pi w^2)', sp.simplify(sp.expand_complex(K2 + sp.I*K1 - 1/(2*sp.pi*w**2))) == 0)
xi, eta, ep = sp.symbols('xi eta ep')
rem = 1/(xi - eta)**2 - 1/eta**2 - 2*xi/eta**3
rep('A2 remainder = xi^2 (3 eta - 2 xi)/(eta^3 (xi - eta)^2)', sp.simplify(rem - xi**2*(3*eta - 2*xi)/(eta**3*(xi - eta)**2)) == 0)
rep('A3 DK(-Y)X <-> 2 xi/eta^3', sp.simplify(sp.diff(1/(ep*xi - eta)**2, ep).subs(ep, 0) - 2*xi/eta**3) == 0)
# |rem| <= 16 |xi|^2/|eta|^4 for |eta| >= 2|xi| (|3 eta - 2 xi| <= 4|eta|, |xi - eta| >= |eta|/2); numeric spot check
rng = np.random.default_rng(1); worst = 0.0
for _ in range(20000):
    X = complex(*rng.normal(size=2)); Y = X*complex(*rng.normal(size=2))
    if abs(Y) < 2*abs(X): continue
    r_ = abs(1/(X - Y)**2 - 1/Y**2 - 2*X/Y**3)*abs(Y)**4/abs(X)**2; worst = max(worst, r_)
rep('A4 |rem| |eta|^4/|xi|^2 <= 16 for |eta| >= 2|xi| (sampled max)', worst <= 16, round(worst, 3))
s, r = sp.symbols('s r', positive=True)
rep('A5 near-0 term |2 xi/eta^3| |eta|^2 ~ |eta|^-1 integrable: int_0^1 s^-1 s ds', sp.integrate(1/s*s, (s, 0, 1)) == 1)
I_dk1 = sp.integrate(r*s**(1 - 3)*s, (s, 1, r))
rep('A6 gamma = 1: r int_1^r s^(gamma-3) s ds = r log r', sp.simplify(I_dk1 - r*sp.log(r)) == 0)
I_dk = sp.integrate(r*s**(sp.Rational(3, 2) - 3)*s, (s, 1, r))
rep('A7 gamma = 3/2: r int_1^r s^(gamma-2) ds = 2 r (r^(1/2) - 1) <= 2 r^gamma', sp.simplify(I_dk - 2*r*(sp.sqrt(r) - 1)) == 0)
I_far = sp.integrate(r**2*s**(sp.Rational(3, 2) - 4)*s, (s, 2*r, sp.oo))
rep('A8 far: r^2 int_{2r}^inf s^(gamma-3) ds = O(r^gamma) (gamma = 3/2)', sp.simplify(I_far/r**sp.Rational(3, 2)).is_number, I_far)
# gauge: linear harmonic fields with div = curl = 0
m11, m12, m21, m22 = sp.symbols('m11 m12 m21 m22')
Wl = sp.Matrix([m11*x + m12*y, m21*x + m22*y])
sol = sp.solve([sp.diff(Wl[0], x) + sp.diff(Wl[1], y), sp.diff(Wl[1], x) - sp.diff(Wl[0], y)], [m22, m21], dict=True)[0]
rep('A9 div = curl = 0 for M X  <=>  M symmetric traceless', sol == {m22: -m11, m21: m12}, sol)
# jet forcing: V = l X + M X + O(r^2), rho = x^2 + O(r^3): quadratic part of V.grad rho - rho
Ms = sp.Matrix([[m11, m12], [m12, -m11]]); Vq = (l*sp.eye(2) + Ms)*sp.Matrix([x, y])
q2 = sp.expand(Vq[0]*2*x - x**2)
sj = sp.solve([q2.coeff(x, 2), sp.expand(q2).coeff(x, 1).coeff(y, 1)], [m11, m12], dict=True)[0]
rep('A10 jet forces M = diag(1/2 - l, l - 1/2)', sj == {m11: sp.Rational(1, 2) - l, m12: 0}, sj)
DV0 = (l*sp.eye(2) + Ms.subs(sj))
rep('A11 DV(0) = diag(1/2, 2l - 1/2)', sp.simplify(DV0 - sp.diag(sp.Rational(1, 2), 2*l - sp.Rational(1, 2))) == sp.zeros(2))
# lambda_+ = max eigenvalue of l I + M; gamma lambda_+ >= 1
ok_ineq = True
for gv in [1.0, 1.2, 1.5, 1.9, 1.999]:
    for lv in np.linspace(-2, 3, 501):
        lp = max(0.5, 2*lv - 0.5)
        allowed = gv*lp >= 1 - 1e-12
        pred = lv >= 0.25 + 0.5/gv - 1e-12
        ok_ineq &= (allowed == pred)
rep('A12 gamma lambda_+ >= 1 <=> l >= 1/4 + 1/(2 gamma) for gamma in [1, 2) (grid)', ok_ineq)
rep('A13 1/4 + 1/(2 gamma) ranges over (1/2, 3/4] on [1, 2)', (0.25 + 0.5/1.0 == 0.75) and (0.25 + 0.5/2.0 == 0.5))
# families
psi = -x**3/3 + (l - sp.Rational(1, 2))*x*y; rho = x**2
W = sp.Matrix([-sp.diff(psi, y), sp.diff(psi, x)]); V = l*sp.Matrix([x, y]) + W
rep('A14 rho = x^2, psi = -x^3/3 + (l - 1/2) x y: V.grad rho = rho, -Lap psi = rho_x, W(0) = 0',
    sp.simplify(V[0]*sp.diff(rho, x) + V[1]*sp.diff(rho, y) - rho) == 0 and
    sp.simplify(-sp.diff(psi, x, 2) - sp.diff(psi, y, 2) - sp.diff(rho, x)) == 0 and W.subs({x: 0, y: 0}) == sp.zeros(2, 1))
xp = sp.symbols('xp', positive=True)
rhoL = H*xp**g; psiL = -H*xp**(g + 1)/(g + 1) - a*xp*y; lL = 1/g - a
WL = sp.Matrix([-sp.diff(psiL, y), sp.diff(psiL, xp)]); VL = lL*sp.Matrix([xp, y]) + WL
rep('A15 layered rho = H x^g, psi = -H x^(g+1)/(g+1) - a x y, l = 1/g - a (x > 0)',
    sp.simplify(VL[0]*sp.diff(rhoL, xp) + VL[1]*sp.diff(rhoL, y) - rhoL) == 0 and
    sp.simplify(-sp.diff(psiL, xp, 2) - sp.diff(psiL, y, 2) - sp.diff(rhoL, xp)) == 0)
# f(x): W~ = (0, -f(x)) has div 0, curl -f'; with M forced, V_1 = x/2; (x/2) f' = f
f = sp.Function('f'); h = sp.Function('h')
Wt = sp.Matrix([0, -f(x)])
rep('A16 W~ = (0, -f(x)): div 0, curl = -f\'', sp.diff(Wt[0], x) + sp.diff(Wt[1], y) == 0 and sp.simplify(sp.diff(Wt[1], x) - sp.diff(Wt[0], y) + sp.diff(f(x), x)) == 0)
Vf = l*sp.Matrix([x, y]) + Ms.subs(sj)*sp.Matrix([x, y]) + Wt
rep('A17 V = (x/2, (2l - 1/2) y - f(x))', sp.simplify(Vf - sp.Matrix([x/2, (2*l - sp.Rational(1, 2))*y - f(x)])) == sp.zeros(2, 1))
ode = sp.dsolve(sp.Eq(x/2*sp.diff(f(x), x), f(x)))
rep('A18 (x/2) f\' = f  =>  f = C x^2 on each half-line', sp.simplify(ode.rhs/x**2).free_symbols <= {sp.Symbol('C1')}, ode)
E = sp.expand(Vf[0]*sp.diff(f(x) + h(y), x) + Vf[1]*sp.diff(f(x) + h(y), y) - f(x) - h(y))
Ex = sp.simplify(sp.diff(E, x))
target = x/2*sp.diff(f(x), x, 2) - sp.diff(f(x), x)/2 - sp.diff(f(x), x)*sp.diff(h(y), y)
rep('A19 d_x (V.grad rho - rho) = (x/2) f\'\' - f\'/2 - f\' h\'(y) for rho = f(x) + h(y)', sp.simplify(Ex - target) == 0)
# gauges of higher growth: stream polynomials Re z^k, Im z^k (k = 2..n+1) give harmonic, div/curl-free fields of degree k - 1
z = x + sp.I*y; okg = True
for k in range(2, 6):
    for P in [sp.re(sp.expand(z**k)), sp.im(sp.expand(z**k))]:
        P = sp.expand(P); Wg = sp.Matrix([-sp.diff(P, y), sp.diff(P, x)])
        okg &= sp.simplify(sp.diff(P, x, 2) + sp.diff(P, y, 2)) == 0
        okg &= sp.simplify(sp.diff(Wg[0], x) + sp.diff(Wg[1], y)) == 0 and Wg.subs({x: 0, y: 0}) == sp.zeros(2, 1)
rep('A20 harmonic stream polynomials of degree 2..5: div = curl = 0, W(0) = 0', okg)

if len(sys.argv) > 1 and sys.argv[1] == 'symonly':
    print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok)); sys.exit(0)

# ---------------- Part B ----------------
import torch
NEARGL = 64; PW = 0.0125
dev = 'cuda'; DT = torch.float64
def smooth_step(v):  # 0 for v <= 0, 1 for v >= 1, C^inf
    v = v.clamp(0, 1)
    A = torch.where(v > 0, torch.exp(-1/v.clamp_min(1e-300)), torch.zeros_like(v))
    B = torch.where(v < 1, torch.exp(-1/(1 - v).clamp_min(1e-300)), torch.zeros_like(v))
    return A/(A + B)
def phi(u):  # 1 on [0, 1/2], 0 on [1, inf)
    return smooth_step((1 - u)/0.5)
gl8 = np.polynomial.legendre.leggauss(8); gl12 = np.polynomial.legendre.leggauss(12); gl64 = np.polynomial.legendre.leggauss(NEARGL)
def panels(t0, t1, width, glw):
    n = max(1, int(math.ceil((t1 - t0)/width))); edges = np.linspace(t0, t1, n + 1)
    xs, ws = glw; T = []; Wt = []
    for i in range(n):
        c = 0.5*(edges[i] + edges[i + 1]); hw = 0.5*(edges[i + 1] - edges[i])
        T.append(c + hw*xs); Wt.append(hw*ws)
    return np.concatenate(T), np.concatenate(Wt)
def W2(rho_fn, X, Rmax=1e14, rmin=1e-5, nth=2048, nth_near=256):
    """rho_fn(x, y) torch -> torch. Returns (W2_1, W2_2) at X = (x0, y0)."""
    x0, y0 = X; xi = complex(x0, y0); ax = abs(xi); arad = min(1.0, ax/2)
    # near part, polar about X
    sn = 0.5*arad*(gl64[0] + 1); swn = 0.5*arad*gl64[1]
    al_ = 2*math.pi*np.arange(nth_near)/nth_near
    S_ = torch.tensor(sn, dtype=DT, device=dev)[:, None]; A_ = torch.tensor(al_, dtype=DT, device=dev)[None, :]
    Zr = S_*torch.cos(A_); Zi = S_*torch.sin(A_)
    Z = torch.complex(Zr, Zi); etaN = xi - Z
    rN = rho_fn(etaN.real, etaN.imag)
    integ = phi(S_/arad)*(rN/Z**2 - (1/etaN**2 + 2*xi/etaN**3)*rN)
    near = (integ*(S_*torch.tensor(swn, dtype=DT, device=dev)[:, None])).sum()*(2*math.pi/nth_near)
    # far part, polar about 0, t = log r
    lx = math.log(ax); tmin = math.log(rmin); tmax = math.log(Rmax)
    T1, W1 = panels(tmin, lx - 2, 0.5, gl12); T2, W2_ = panels(lx - 2, lx + 2, PW, gl8); T3, W3 = panels(lx + 2, tmax, 0.5, gl12)
    Tt = np.concatenate([T1, T2, T3]); Wtt = np.concatenate([W1, W2_, W3])
    th = 2*math.pi*np.arange(nth)/nth
    far = torch.zeros((), dtype=torch.complex128, device=dev)
    TH = torch.tensor(th, dtype=DT, device=dev)[None, :]
    for c0 in range(0, len(Tt), 256):
        tt = torch.tensor(Tt[c0:c0 + 256], dtype=DT, device=dev)[:, None]; ww = torch.tensor(Wtt[c0:c0 + 256], dtype=DT, device=dev)[:, None]
        R_ = torch.exp(tt); er = torch.complex(R_*torch.cos(TH), R_*torch.sin(TH))
        rr = rho_fn(er.real, er.imag)
        remk = xi**2*(3*er - 2*xi)/(er**3*(xi - er)**2)
        cut = 1 - phi((er - xi).abs()/arad)
        far = far + (cut*remk*rr*R_**2*ww).sum()*(2*math.pi/nth)
    Om = (near + far)/(2*math.pi) - rho_fn(torch.tensor(x0, dtype=DT, device=dev), torch.tensor(y0, dtype=DT, device=dev))/2
    Om = complex(Om.item())
    return Om.imag, Om.real   # W2_1 = Im Omega, W2_2 = Re Omega
results = {}
pts = [(0.6, 0.4), (2.0, -1.0), (-3.0, 2.5), (7.0, 5.0)]
for gv in [1.0, 1.5]:
    fx = lambda X_, Y_, gv=gv: X_**2*(1 + X_**2)**((gv - 2)/2)
    for P in pts:
        w1, w2 = W2(fx, P)
        ex = -P[0]**2*(1 + P[0]**2)**((gv - 2)/2)
        err = max(abs(w1), abs(w2 - ex)); results['f_g%g_%s' % (gv, P)] = err
        rep('B1 rho = f(x), gamma %g, X = %s: W_2 = (0, -f(x))' % (gv, P), err < 1e-6, '(W2 = %.9f, %.9f; exact 0, %.9f; err %.1e)' % (w1, w2, ex, err))
hy1 = lambda X_, Y_: Y_**3/(1 + Y_**2)
hy2 = lambda X_, Y_: Y_**2*(1 + Y_**2)**(-0.25)
for nm, hf in [('y^3/(1+y^2) (gamma 1)', hy1), ('y^2 (1+y^2)^(-1/4) (gamma 3/2)', hy2)]:
    for P in pts[:3]:
        w1, w2 = W2(hf, P); err = max(abs(w1), abs(w2))
        rep('B2 rho = %s, X = %s: W_2 = 0' % (nm, P), err < 1e-6, '(W2 = %.2e, %.2e)' % (w1, w2))
# non-separable density with gamma = 1.5 and an x-odd, y-odd part
gq = 1.5
def rng2(X_, Y_):
    r2 = X_**2 + Y_**2
    return X_**2*(1 + r2)**((gq - 2)/2) + X_*Y_**2*(1 + r2)**((gq - 3)/2) + 0.5*Y_**3*(1 + r2)**((gq - 3)/2)
def rho_x(X_, Y_):
    Xt = torch.tensor(X_, dtype=DT, device=dev, requires_grad=True); Yt = torch.tensor(Y_, dtype=DT, device=dev)
    v = rng2(Xt, Yt); v.backward(); return Xt.grad.item()
hh = 1e-3
for P in [(1.3, 0.7), (-4.0, 3.0)]:
    Wp = {}
    for dx, dy in [(hh, 0), (-hh, 0), (0, hh), (0, -hh)]:
        Wp[(dx, dy)] = W2(rng2, (P[0] + dx, P[1] + dy))
    div = (Wp[(hh, 0)][0] - Wp[(-hh, 0)][0] + Wp[(0, hh)][1] - Wp[(0, -hh)][1])/(2*hh)
    curl = (Wp[(hh, 0)][1] - Wp[(-hh, 0)][1] - Wp[(0, hh)][0] + Wp[(0, -hh)][0])/(2*hh)
    rx = rho_x(*P)
    rep('B3 non-separable rho, X = %s: div W_2 = 0, curl W_2 = -rho_x' % (P,), abs(div) < 1e-5 and abs(curl + rx) < 1e-5,
        '(div %.1e, curl %.7f, -rho_x %.7f)' % (div, curl, -rx))
# DW_2(0) = 0: W_2(X) = O(|X|^2) near 0
vals = []
for sc in [0.1, 0.05, 0.025]:
    w1, w2 = W2(rng2, (sc*0.8, sc*0.6)); vals.append(math.hypot(w1, w2))
ratios = [vals[0]/vals[1], vals[1]/vals[2]]
rep('B4 non-separable rho: |W_2(X)| ~ |X|^2 near 0 (ratio about 4 per halving)', all(3.3 < q < 4.7 for q in ratios), '(|W_2| %s, ratios %s)' % (['%.3e' % v for v in vals], ['%.3f' % q for q in ratios]))
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
