"""v38b: checks for referee result 11 03-jets: strain identities, moment family, critical flux, far field relation,
homogeneous-tail exclusion asymptotics, l->1 sign conflict, large-l rescaling, explicit solutions,
vertical-axis integral."""
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp, quad, dblquad

res = []
def rep(ok, name, extra=""):
    res.append(bool(ok)); print(("PASS" if ok else "FAIL"), name, extra)
def chk(name, expr):
    e = sp.simplify(expr); rep(e == 0, name, "" if e == 0 else str(e))

x, y = sp.symbols('x y', real=True)
r, th = sp.symbols('r theta', positive=True)
l, g, m, p = sp.symbols('ell gamma m p', positive=True)
r2 = x**2 + y**2
K2 = (x**2 - y**2)/(2*sp.pi*r2**2)
K1 = -2*x*y/(2*sp.pi*r2**2)
s3 = y*(3*x**2 - y**2)/r2**3          # r^-3 sin 3 th
c3 = x*(x**2 - 3*y**2)/r2**3          # r^-3 cos 3 th

# (1) kernel derivatives; no delta part (zero circle averages of K_i n_j); oddness
chk("03 d_y K2 = -sin3th/(pi r^3)", sp.diff(K2, y) + s3/sp.pi)
chk("03 d_x K2 = -cos3th/(pi r^3)", sp.diff(K2, x) + c3/sp.pi)
for nm, Ki in [("K1", -sp.sin(2*th)), ("K2", sp.cos(2*th))]:
    for nn, nj in [("n_x", sp.cos(th)), ("n_y", sp.sin(th))]:
        chk(f"03 no delta in derivative of pv {nm}: circle mean of {nm} {nn}", sp.integrate(Ki*nj, (th, 0, 2*sp.pi)))

# (2) strain identities checked independently through the Fourier form of the Darcy law
#     psi^ = i k1 R^/|k|^2 ;  psi_xy(0) = (1/4pi^2) int (ik1)(ik2) psi^ ;  psi_xx(0) = (1/4pi^2) int (ik1)^2 psi^
k1, k2, kap, ph = sp.symbols('k1 k2 kappa phi', real=True)
G0 = sp.pi*sp.exp(-(k1**2 + k2**2)/4)        # FT of exp(-r^2), convention f^ = int f e^{-ik.x}
def FT_mono(a_, b_):
    e = G0
    for _ in range(a_): e = sp.I*sp.diff(e, k1)
    for _ in range(b_): e = sp.I*sp.diff(e, k2)
    return e
poly = {(2, 1): 1, (3, 0): sp.Rational(3, 10), (0, 3): sp.Rational(-1, 5), (1, 2): sp.Rational(1, 2)}
Rhat = sum(cf*FT_mono(a_, b_) for (a_, b_), cf in poly.items())
Rphys = sum(cf*x**a_*y**b_ for (a_, b_), cf in poly.items())*sp.exp(-r2)
psihat = sp.I*k1*Rhat/(k1**2 + k2**2)
def fourier_int(expr):
    e = sp.simplify(expr.subs({k1: kap*sp.cos(ph), k2: kap*sp.sin(ph)})*kap)
    f = sp.lambdify((kap, ph), e, 'numpy')
    val = dblquad(lambda kk, pp_: complex(f(kk, pp_)).real, 0, 2*np.pi, 0, 40, epsabs=1e-12)[0]
    return val/(4*np.pi**2)
psixy0 = fourier_int((sp.I*k1)*(sp.I*k2)*psihat)
psixx0 = fourier_int((sp.I*k1)**2*psihat)
Rpol = sp.simplify(Rphys.subs({x: r*sp.cos(th), y: r*sp.sin(th)}))
fs = sp.lambdify((r, th), Rpol*sp.sin(3*th)/r**2, 'numpy')
fc = sp.lambdify((r, th), Rpol*sp.cos(3*th)/r**2, 'numpy')
Is = dblquad(lambda rr, tt: fs(rr, tt), 0, 2*np.pi, 1e-12, 12)[0]/np.pi
Ic = dblquad(lambda rr, tt: fc(rr, tt), 0, 2*np.pi, 1e-12, 12)[0]/np.pi
rep(abs(psixy0 - Is) < 1e-8, "03 strain identity psi_xy(0) = (1/pi) int R r^-3 sin3th (Fourier check)", f"{psixy0:.10f} vs {Is:.10f}")
rep(abs(psixx0 - Ic) < 1e-8, "03 identity psi_xx(0) = (1/pi) int R r^-3 cos3th (Fourier check)", f"{psixx0:.10f} vs {Ic:.10f}")

# (3) DV(0) from V xi = alpha xi, D xi(0) = e1, curl V(0) = 0, div = 2 ell
d11, d12, d21, d22, alpha = sp.symbols('d11 d12 d21 d22 alpha')
sol = sp.solve([d11 - alpha, d12, d21 - d12, d11 + d22 - 2*l], [d11, d12, d21, d22], dict=True)[0]
chk("03 DV(0) = diag(alpha, 2l - alpha)", (sp.Matrix([[sol[d11], sol[d12]], [sol[d21], sol[d22]]]) - sp.diag(alpha, 2*l - alpha)).norm())

# (4) moment family: pointwise identity in polar form with generic functions
Rf = sp.Function('R')(r, th); Wr = sp.Function('Wr')(r, th); Wt = sp.Function('Wt')(r, th)
Phi = sp.Function('Phi')(th)
phi = r**(-m)*Phi
Vr = l*r + Wr; Vt = Wt
div = lambda Fr, Ft: sp.diff(r*Fr, r)/r + sp.diff(Ft, th)/r
dot_grad = lambda Fr, Ft, f: Fr*sp.diff(f, r) + Ft*sp.diff(f, th)/r
lhs = div(Rf*phi*Vr, Rf*phi*Vt)
rhs = (1 + 2*l - m*l)*Rf*phi + Rf*dot_grad(Wr, Wt, phi) + phi*(dot_grad(Vr, Vt, Rf) - Rf) + Rf*phi*div(Wr, Wt)
chk("03 div(R phi V) = (1+2l-ml) R phi + R W.grad phi + phi (VR - R) + R phi div W", sp.expand(lhs - rhs))
chk("03 critical exponent coefficient 1+2l-(p+2)l = 0 at p = 1/l", (1 + 2*l - (1/l + 2)*l))
chk("03 Phi=1: W.grad r^-(p+2) = -(p+2) r^-(p+3) W_r", dot_grad(Wr, Wt, r**(-p - 2)) + (p + 2)*r**(-p - 3)*Wr)
chk("03 m=3: Q = (l-1) pi c with c = l - 1/g", sp.expand(-(1 + 2*l - 3*l)*sp.pi*(l - 1/g) - sp.pi*(l - 1)*(l - 1/g)))

# (5) integrated moment identity on an annulus for an exact transport solution
#     (linear field V = (x/g, (2l-1/g) y), R = |x|^g, W = V - l X), including both boundary fluxes
for gv, lv_, mv in [(2.0, 1.4, 2.9), (4.5, 1.2, 3.3)]:
    av = 1/gv; bv = 2*lv_ - av; cv = lv_ - av
    Phif = lambda t_: np.sin(3*t_) + 0.3*np.cos(t_) + 0.2
    dPhif = lambda t_: 3*np.cos(3*t_) - 0.3*np.sin(t_)
    def integrand(rr, tt):
        R_ = (rr*abs(np.cos(tt)))**gv
        ph_ = rr**(-mv)*Phif(tt)
        Wr_ = rr*(-cv*np.cos(tt)**2 + cv*np.sin(tt)**2)
        Wt_ = rr*(2*cv*np.cos(tt)*np.sin(tt))
        gr = -mv*rr**(-mv - 1)*Phif(tt); gt = rr**(-mv - 1)*dPhif(tt)
        return ((1 + 2*lv_ - mv*lv_)*R_*ph_ + R_*(Wr_*gr + Wt_*gt))*rr
    def flux(rr):
        f = lambda tt: (rr*abs(np.cos(tt)))**gv*rr**(-mv)*Phif(tt)*rr*(av*np.cos(tt)**2 + bv*np.sin(tt)**2)*rr
        return quad(f, 0, 2*np.pi, limit=200)[0]
    eps, Lr = 0.3, 2.5
    vol = dblquad(integrand, 0, 2*np.pi, eps, Lr, epsabs=1e-11, epsrel=1e-11)[0]
    fl = flux(Lr) - flux(eps)
    rep(abs(vol - fl) < 1e-8*max(1, abs(fl)), f"03 annulus divergence identity (g={gv}, l={lv_}, m={mv})", f"{vol:.10f} vs {fl:.10f}")
# outer flux limit at the critical exponent: R ~ L^p A, V_r ~ l L  ->  l int A Phi
chk("03 critical outer flux power L^p * L^-(p+2) * L * L = L^0", sp.simplify(p - (p + 2) + 2))

# (6) far field: angular Poisson equation, polar velocity, J_p, correction coefficient
A = sp.Function('A'); Ps = sp.Function('Psi')
TH = sp.atan2(y, x); RR = sp.sqrt(r2)
psi = RR**(p + 1)*Ps(TH)
F = RR**p*A(TH)
lap = sp.diff(psi, x, 2) + sp.diff(psi, y, 2)
tosub = {x: r*sp.cos(th), y: r*sp.sin(th)}
def topolar(e):   # substitute polar coordinates and reduce atan2(r sin th, r cos th) -> th (valid for th in (-pi, pi))
    return e.subs(tosub).replace(sp.atan2, lambda a_, b_: th).doit()
e1 = sp.simplify(topolar(lap + sp.diff(F, x)))
target = r**(p - 1)*(sp.diff(Ps(th), th, 2) + (p + 1)**2*Ps(th) + p*sp.cos(th)*A(th) - sp.sin(th)*sp.diff(A(th), th))
chk("03 -Lap(r^(p+1)Psi) = d_x(r^p A)  <=>  Psi''+(p+1)^2 Psi = -p cos A + sin A'", sp.simplify(e1.doit() - target))
U1 = -sp.diff(psi, y); U2 = sp.diff(psi, x)
Ur = sp.simplify(topolar((U1*x + U2*y)/RR))
Ut = sp.simplify(topolar((-U1*y + U2*x)/RR))
chk("03 H_r = -r^p Psi'", sp.simplify(Ur + r**p*sp.diff(Ps(th), th)))
chk("03 H_th = (p+1) r^p Psi", sp.simplify(Ut - (p + 1)*r**p*Ps(th)))
Fp = r**p*A(th)
Jexpr = sp.simplify((-r**p*sp.diff(Ps(th), th))*sp.diff(Fp, r) + (p + 1)*r**p*Ps(th)*sp.diff(Fp, th)/r)
chk("03 H.grad(r^p A) = r^(2p-1) J_p, J_p = (p+1) Psi A' - p Psi' A",
    sp.simplify(Jexpr - r**(2*p - 1)*((p + 1)*Ps(th)*sp.diff(A(th), th) - p*sp.diff(Ps(th), th)*A(th))))
chk("03 correction coefficient: l(2p-1)-1 = -(l-1) at p=1/l", l*(2/l - 1) - 1 + (l - 1))
Cc = sp.symbols('C')
Psi_c = Cc*A(th)**((p + 1)/p)
chk("03 Psi = C A^((p+1)/p) gives J_p = 0", sp.simplify((p + 1)*Psi_c*sp.diff(A(th), th) - p*sp.diff(Psi_c, th)*A(th)))
chk("03 vanishing order k = g + g/p exceeds g+2 iff g > 2p", sp.simplify((g + g/p) - (g + 2) - (g - 2*p)/p))

# (7) local asymptotics of Psi at a zero of A (Psi(th0)=Psi'(th0)=0), numeric ODE vs the claimed coefficients
def psi_ratio(gv, pv, th0, side=+1, tmax=2e-3, aa=1.3):
    Af = lambda t_: aa*t_**gv*(1 + 0.4*t_)
    dAf = lambda t_: aa*(gv*t_**(gv - 1)*(1 + 0.4*t_) + 0.4*t_**gv)
    def rhs_(t_, Y):
        thv = th0 + side*t_
        Ath = side*dAf(t_)          # dA/dtheta
        f = -pv*np.cos(thv)*Af(t_) + np.sin(thv)*Ath
        return [Y[1], f - (pv + 1)**2*Y[0]]      # d^2/dt^2 = d^2/dth^2
    so = solve_ivp(rhs_, (0, tmax), [0, 0], rtol=1e-12, atol=1e-40)
    return so.y[0, -1], tmax
for gv, pv in [(2.0, 0.7), (4.5, 0.55)]:
    th0 = 0.8
    val, tm = psi_ratio(gv, pv, th0)
    pred = 1.3*np.sin(th0)/(gv + 1)*tm**(gv + 1)
    rep(abs(val/pred - 1) < 5e-3, f"03 Psi ~ a sin(th0) t^(g+1)/(g+1), g={gv}, p={pv}", f"ratio {val/pred:.5f}")
    val, tm = psi_ratio(gv, pv, 0.0)
    pred = 1.3*(gv - pv)/((gv + 1)*(gv + 2))*tm**(gv + 2)
    rep(abs(val/pred - 1) < 5e-3, f"03 Psi ~ a(g-p)cos(th0) t^(g+2)/((g+1)(g+2)) at th0=0, g={gv}, p={pv}", f"ratio {val/pred:.5f}")
# (8) l -> 1+, g = 2, zeros at 0 and pi: the constant C in Psi = C A^2 has opposite signs at the two ends
t_ = sp.symbols('t', positive=True); a0, api = sp.symbols('a0 api', positive=True)
def lead_psi(rhs_series):
    return sp.integrate(sp.integrate(rhs_series, (t_, 0, t_)), (t_, 0, t_))
rhs0 = sp.series(-sp.cos(t_)*a0*t_**2 + sp.sin(t_)*sp.diff(a0*t_**2, t_), t_, 0, 3).removeO()       # th = t
rhspi = sp.series(-sp.cos(sp.pi - t_)*api*t_**2 + sp.sin(sp.pi - t_)*(-sp.diff(api*t_**2, t_)), t_, 0, 3).removeO()  # th = pi - t
C0 = sp.simplify(lead_psi(rhs0)/(a0**2*t_**4)); Cpi = sp.simplify(lead_psi(rhspi)/(api**2*t_**4))
chk("03 l->1: C = 1/(12 a_0) at th=0", C0 - 1/(12*a0))
chk("03 l->1: C = -1/(12 a_pi) at th=pi (opposite sign)", Cpi + 1/(12*api))

# (9) large-l rescaling (explicit non-solution test functions R, W, xi on R^2)
pv_, gv_ = sp.Rational(1, 3), sp.Rational(9, 2)
lv_ = 1/pv_; d = pv_**(1/(gv_ - 1)); k = pv_**(gv_/(gv_ - 1))
chk("03 k/d = p", sp.simplify(k/d - pv_)); chk("03 k d^-g = 1", sp.simplify(k*d**(-gv_) - 1)); chk("03 k = p d", sp.simplify(k - pv_*d))
Y1, Y2 = sp.symbols('Y1 Y2', real=True)
Rt = sp.sin(Y1) + Y2**3 + Y1*Y2; Wt1 = sp.cos(Y1*Y2); Wt2 = Y1**2 - Y2; xit = Y1 + sp.sin(Y2)**2
sub = {Y1: x/d, Y2: y/d}
f_p = k*Rt.subs(sub); b1 = x + k*Wt1.subs(sub); b2 = y + k*Wt2.subs(sub); chi = d*xit.subs(sub)
VR = (lv_*Y1 + Wt1)*sp.diff(Rt, Y1) + (lv_*Y2 + Wt2)*sp.diff(Rt, Y2)
Vxi = (lv_*Y1 + Wt1)*sp.diff(xit, Y1) + (lv_*Y2 + Wt2)*sp.diff(xit, Y2)
chk("03 b.grad f - p f = p k (VR - R)(Z/d)", sp.simplify(b1*sp.diff(f_p, x) + b2*sp.diff(f_p, y) - pv_*f_p - pv_*k*(VR - Rt).subs(sub)))
chk("03 b.grad chi - (p/g) chi = p d (V xi - xi/g)(Z/d)", sp.simplify(b1*sp.diff(chi, x) + b2*sp.diff(chi, y) - pv_/gv_*chi - pv_*d*(Vxi - xit/gv_).subs(sub)))
divW = sp.diff(Wt1, Y1) + sp.diff(Wt2, Y2); curlW = sp.diff(Wt2, Y1) - sp.diff(Wt1, Y2)
chk("03 div b = 2 + p div W(Z/d)", sp.simplify(sp.diff(b1, x) + sp.diff(b2, y) - 2 - pv_*divW.subs(sub)))
chk("03 curl b + (f_p)_x = p (curl W + R_x)(Z/d)", sp.simplify(sp.diff(b2, x) - sp.diff(b1, y) + sp.diff(f_p, x) - pv_*(curlW + sp.diff(Rt, Y1)).subs(sub)))
chk("03 c[f_p] = p c[R] = 1 - p/g", sp.simplify(pv_*(lv_ - 1/gv_) - (1 - pv_/gv_)))
chk("03 Q[f_p] = p^2 Q[R] = pi(1-p)(1-p/g)", sp.simplify(pv_**2*(lv_ - 1)*(lv_ - 1/gv_) - (1 - pv_)*(1 - pv_/gv_)))
chk("03 scaling of c: k d^-3 d^2 = p", sp.simplify(k*d**(-3)*d**2 - pv_))
chk("03 scaling of Q: k^2 d^-4 d^2 = p^2", sp.simplify(k**2*d**(-4)*d**2 - pv_**2))

# (10) explicit local (non-canonical) solution and rough canonical branch; both sides of x = 0
s = sp.symbols('s', positive=True)
for sgn in [1, -1]:
    X = sgn*s                       # x = X, |x| = s, d/dx = sgn d/ds
    dx = lambda f: sgn*sp.diff(f, s)
    cc = l - 1/g
    Rl = s**g
    psil = cc*X*y - X*s**g/(g + 1)
    lap_l = dx(dx(psil)) + sp.diff(psil, y, 2)
    chk(f"03 local sol Poisson -Lap psi = R_x (side {sgn})", sp.simplify(-lap_l - dx(Rl)))
    V1 = l*X - sp.diff(psil, y); V2 = l*y + dx(psil)
    chk(f"03 local sol transport (side {sgn})", sp.simplify(V1*dx(Rl) + V2*sp.diff(Rl, y) - Rl))
    chk(f"03 local sol V = (x/g, (2l-1/g) y - |x|^g) (side {sgn})", sp.simplify(V1 - X/g) + sp.simplify(V2 - ((2*l - 1/g)*y - s**g)))
    # rough canonical branch, 0<g<1, l = 1/g
    Rr = s**g; W1 = sp.Integer(0); W2 = -s**g
    chk(f"03 rough branch div W = 0 (side {sgn})", dx(W1) + sp.diff(W2, y))
    chk(f"03 rough branch curl W = -R_x (side {sgn})", dx(W2) - sp.diff(W1, y) + dx(Rr))
    chk(f"03 rough branch transport with l g = 1 (side {sgn})", sp.simplify(((1/g)*X + W1)*dx(Rr) + ((1/g)*y + W2)*sp.diff(Rr, y) - Rr))

# (11) moment ratio Q/(pi c^2) = (l-1)/(l-1/g) in (0,1) on admissible exponents
vals = [(lv - 1)/(lv - 1/gv) for lv in np.linspace(1.001, 50, 400) for gv in [2.0] + list(np.linspace(3.001, 60, 100))]
rep(0 < min(vals) and max(vals) < 1, "03 moment ratio in (0,1)", f"[{min(vals):.4f},{max(vals):.4f}]")

# (12) vertical-axis integral: b h' = (1 - 2 g l + g b') h  =>  int h w' = ((g-1)l-1)/(g+1) int h
def axis_check(gv, lv, cdist):
    pv = 1/lv; cv = lv - 1/gv
    w = lambda yy: cv*yy*(1 + yy*yy)**((pv - 1)/2) + cdist*yy*yy*(1 + yy*yy)**((pv - 2)/2)
    def wp(yy):
        return (cv*((1 + yy*yy)**((pv - 1)/2) + yy*yy*(pv - 1)*(1 + yy*yy)**((pv - 3)/2))
                + cdist*(2*yy*(1 + yy*yy)**((pv - 2)/2) + yy**3*(pv - 2)*(1 + yy*yy)**((pv - 4)/2)))
    b = lambda yy: lv*yy + w(yy); bp = lambda yy: lv + wp(yy)
    tot = {}
    for side in [1, -1]:
        y0 = 1e-7
        # integrate in u = log|y| ; state: log h, int h dy, int h w' dy ; start log h(y0) ~ 0
        def rhs_(u_, Y):
            yy = side*np.exp(u_)
            dlogh_dy = (1 - 2*gv*lv + gv*bp(yy))/b(yy)
            h = np.exp(Y[0]); jac = np.exp(u_)
            return [dlogh_dy*side*jac, h*jac, h*wp(yy)*jac]
        so = solve_ivp(rhs_, (np.log(y0), 80.0), [0.0, 0.0, 0.0], rtol=1e-11, atol=1e-14, method='DOP853')
        tot[side] = so.y[:, -1]
    Ih = tot[1][1] + tot[-1][1]; Ihw = tot[1][2] + tot[-1][2]
    Kc = ((gv - 1)*lv - 1)/(gv + 1)
    # tail exponent check: h ~ |y|^(p-g)
    return Ihw/Ih, Kc
for gv, lv, cd in [(2.0, 1.5, 0.15), (4.5, 1.25, -0.1), (2.0, 3.0, 0.3)]:
    ratio, Kc = axis_check(gv, lv, cd)
    rep(abs(ratio - Kc) < 1e-6, f"03 vertical-axis identity, g={gv}, l={lv}, asym={cd}", f"{ratio:.9f} vs {Kc:.9f}")
chk("03 axis coefficient algebra", sp.simplify((2*g*l - 1)/(g + 1) - l - ((g - 1)*l - 1)/(g + 1)))
chk("03 escaping branch exponent h ~ r^(p-g)", sp.simplify(p*(1 - 2*g/p) + g - (p - g)))

print("SUMMARY: %d/%d PASS" % (sum(res), len(res)))
