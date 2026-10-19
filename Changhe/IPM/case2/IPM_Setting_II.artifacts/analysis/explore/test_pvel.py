# Lead check: velocity_p (pforward.py) against direct once-subtracted kernel quadrature for a smooth density with
# growth r^p: rho = x^2 (1 + r^2)^((p-2)/2) (1 + 0.3 y / sqrt(1 + r^2)).
import numpy as np, sys
from scipy import integrate
sys.path.insert(0, '.')
import pforward as PF, p0_forward as P1
p = 0.5
def rho_f(x, y):
    r2 = x*x + y*y
    return x*x*(1 + r2)**((p - 2)/2)*(1 + 0.3*y/np.sqrt(1 + r2))
def part(cx, cy, R=1e7):
    # int over |Y - C| < R of K(C - Y) rho(Y) dY, p.v. at C; K(Z) = (-sin2t, cos2t)/(2 pi |Z|^2), K even
    def ang(t):
        f = lambda u: rho_f(cx + np.exp(u)*np.cos(t), cy + np.exp(u)*np.sin(t))   # s ds / s^2 = du
        v = integrate.quad(f, -40, np.log(R), limit=500)[0]
        return v
    tt = np.linspace(0, 2*np.pi, 401)[:-1] + np.pi/400
    vals = np.array([ang(t) for t in tt])
    k = np.stack([-np.sin(2*tt), np.cos(2*tt)])/(2*np.pi)
    # p.v.: subtract the angular mean of the integrand's leading behaviour automatically by symmetry of K (mean zero)
    return (k*vals).mean(axis=1)*2*np.pi
lr, th = P1.make_grid(481, 256, -6, 12)
r = np.exp(lr)
Xg = r[:, None]*np.cos(th)[None, :]; Yg = r[:, None]*np.sin(th)[None, :]
wr, wt = PF.velocity_p(rho_f(Xg, Yg), lr, th, p)
for (k, j) in [(np.searchsorted(r, 0.7), 32), (np.searchsorted(r, 3.0), 150)]:
    X, Y = Xg[k, j], Yg[k, j]
    W = part(X, Y) - part(0.0, 0.0)
    W = W - (rho_f(X, Y) - rho_f(0, 0))/2*np.array([0, 1])
    c, s = np.cos(th[j]), np.sin(th[j])
    Wr_ex = W[0]*c + W[1]*s; Wt_ex = -W[0]*s + W[1]*c
    print('X=(%.3f,%.3f): grid (W_r, W_th) = (%.5f, %.5f), quadrature (%.5f, %.5f)' % (X, Y, wr[k, j], wt[k, j], Wr_ex, Wt_ex))
