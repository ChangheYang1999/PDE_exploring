"""Numerical checks of lead proofs/structure_v1.md:
 (B) Thm 5(c) kernel formula w'(y) = psi_xy(0,y) = (1/pi) int rho(a,z) (z-y)(3a^2-(z-y)^2)/(a^2+(z-y)^2)^3 da dz
     (no contact term when rho = grad rho = 0 on the axis) vs d/dy of U_2(0,y) from the independent Cartesian
     Ewald inverse (code/bs_cartesian.py), for rho = x^2 (1 + a y)^2 exp(-r^2).
 (A) Thm 3(ii) Theta'(a) = R V_r(R e_a) / (l L(a)^2) on a manufactured flow V = l X + curl^perp psi,
     psi = k (1+r^2)^{(p-1)/2} (al x^2 + be x y + ga y^2 + de x^3/<r>), div V = 2 l exactly, |W| = O(r^p)."""
import numpy as np, torch, sys, math
sys.path.insert(0, 'code')
from bs_cartesian import CartesianBS, dev, DT
from scipy.integrate import solve_ivp
# ---------------- (B) ----------------
aa = 1.0
rho_fn = lambda X, Y: X**2*(1 + aa*Y)**2*torch.exp(-(X**2 + Y**2))
S = CartesianBS(12.0, 0.025, 7.0, 11.0, sigma=4*0.025)
msk, U1, U2, rg, f = S.velocity(rho_fn, region=3.0)
Xt, Yt = S.X[msk], S.Y[msk]
ax = (Xt.abs() < 1e-14)
ys = Yt[ax].cpu().numpy(); u2 = U2[ax].cpu().numpy(); o = np.argsort(ys); ys, u2 = ys[o], u2[o]
h = S.h
# 8th-order central differences
cfd = np.array([1/280, -4/105, 1/5, -4/5, 0, 4/5, -1/5, 4/105, -1/280])
xg, wg = np.polynomial.legendre.leggauss(40)
def kernel_formula(y0):
    # polar quadrature centred at (0, y0): (1/pi) int rho(Y0 + r e_th) r^{-3} sin 3th r dr dth
    edges = np.concatenate([[0], np.geomspace(1e-3, 12, 30)])
    rr = np.concatenate([a + (b - a)*(xg + 1)/2 for a, b in zip(edges[:-1], edges[1:])])
    ww = np.concatenate([wg*(b - a)/2 for a, b in zip(edges[:-1], edges[1:])])
    nth = 256; th = 2*np.pi*np.arange(nth)/nth
    Rr, Tt = np.meshgrid(rr, th, indexing='ij')
    Xa = Rr*np.cos(Tt); Za = y0 + Rr*np.sin(Tt)
    rho = Xa**2*(1 + aa*Za)**2*np.exp(-(Xa**2 + Za**2))
    return float(np.sum(ww[:, None]*rho*Rr**-2*np.sin(3*Tt))*(2*np.pi/nth)/np.pi)
print('(B) y0, d/dy U2(0,y) [Cartesian Ewald inverse, FD8], lead kernel formula, difference')
for y0 in [-1.5, -0.6, 0.0, 0.3, 1.0, 2.0]:
    i = np.argmin(abs(ys - y0)); y0 = ys[i]
    d = float(np.dot(cfd, u2[i - 4:i + 5]))/h
    kf = kernel_formula(y0)
    print(f'  y0={y0:+.3f}  {d:+.12f}  {kf:+.12f}  {d - kf:+.2e}')
# ---------------- (A) ----------------
l, p, k = 1.7, 1/1.7, 0.35
al, be, ga, de = 0.4, -0.7, 0.25, 0.5
def W(x, y):
    # psi = k (1+r^2)^{(p-1)/2} P(x,y), P = al x^2 + be x y + ga y^2 + de x^3/(1+r^2)^{1/2}
    r2 = x*x + y*y; s = 1 + r2; e = (p - 1)/2
    P = al*x*x + be*x*y + ga*y*y + de*x**3/np.sqrt(s)
    Px = 2*al*x + be*y + de*(3*x*x/np.sqrt(s) - x**4/s**1.5)
    Py = be*x + 2*ga*y - de*x**3*y/s**1.5
    f = s**e; fx = 2*e*x*s**(e - 1); fy = 2*e*y*s**(e - 1)
    psx = k*(fx*P + f*Px); psy = k*(fy*P + f*Py)
    return -psy, psx
def rhs(s, z):
    u, th = z; r = math.exp(u); x, y = r*math.cos(th), r*math.sin(th)
    w1, w2 = W(x, y)
    vr = l*r + w1*math.cos(th) + w2*math.sin(th); vt = -w1*math.sin(th) + w2*math.cos(th)
    return [vr/r, vt/r]
Rst = 6.0
# check V_r >= l r/2 on |X| >= Rst
tt = np.linspace(0, 2*np.pi, 721); vrmin = 1e9
for rr_ in np.geomspace(Rst, 1e8, 200):
    w1, w2 = W(rr_*np.cos(tt), rr_*np.sin(tt)); vr = l*rr_ + w1*np.cos(tt) + w2*np.sin(tt); vrmin = min(vrmin, (vr/rr_).min())
print(f'(A) l={l} p={p:.4f}; min V_r/r on {Rst} <= r <= 1e8: {vrmin:.4f} (needs >= l/2 = {l/2})')
Smax = 75.0
def LT(a):
    sol = solve_ivp(rhs, [0, Smax], [math.log(Rst), a], method='DOP853', rtol=1e-13, atol=1e-13)
    u, th = sol.y[:, -1]
    return math.exp(u - l*Smax), th
for a in [0.3, 1.2, 2.5, 4.0, 5.5]:
    hh = 1e-5
    Lp, Tp = LT(a + hh); Lm, Tm = LT(a - hh); L0, T0 = LT(a)
    dT = (Tp - Tm)/(2*hh)
    x, y = Rst*math.cos(a), Rst*math.sin(a); w1, w2 = W(x, y)
    vr = l*Rst + w1*math.cos(a) + w2*math.sin(a)
    formula = Rst*vr/(l*L0**2)
    print(f'  a={a:.2f}  L={L0:.10f}  Theta={T0:.10f}  Theta_fd={dT:.10f}  formula={formula:.10f}  diff={dT - formula:+.2e}')
# convergence in Smax of L (tail error ~ e^{-(1-p) l s})
for Sm in [40.0, 60.0, 75.0]:
    sol = solve_ivp(rhs, [0, Sm], [math.log(Rst), 1.2], method='DOP853', rtol=1e-13, atol=1e-13)
    print(f'  Smax={Sm}: L(1.2) = {math.exp(sol.y[0, -1] - l*Sm):.13f}, Theta = {sol.y[1, -1]:.13f}')
