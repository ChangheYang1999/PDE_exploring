"""2D manufactured test of the full pipeline (FFT in theta, modal solve, synthesis of U, c identities).
Phi = Im(z^3) (1+r^2)^(-b) + 0.5 x^4 y (1+r^2)^(-b-1), rho = -Laplace Phi (even in x, odd in y, O(r^3) at 0),
canonical psi = Phi_x (grows like r^(2-2b) = o(r^2)), U = (-Phi_xy, Phi_xx), c = psi_xy(0) = 6."""
import sys, math, time
sys.path.insert(0, 'verifier/early_code')
import numpy as np, torch, sympy as sp
from vres import Evaluation, theta_grid

b = 0.41
x, y = sp.symbols('x y', real=True)
r2 = x ** 2 + y ** 2
Phi = (3 * x ** 2 * y - y ** 3) * (1 + r2) ** (-b) + sp.Rational(1, 2) * x ** 4 * y * (1 + r2) ** (-b - 1)
rho = -(sp.diff(Phi, x, 2) + sp.diff(Phi, y, 2))
exprs = [rho, sp.diff(rho, x), sp.diff(rho, y), -sp.diff(Phi, x, y), sp.diff(Phi, x, 2), sp.diff(Phi, x)]
fns = [sp.lambdify((x, y), e, 'numpy') for e in exprs]


class Dens:
    def eval(self, r, th):
        r = np.asarray(r)[:, None]
        th_ = th.cpu().numpy()[None, :]
        X, Y = r * np.cos(th_), r * np.sin(th_)
        a, ax, ay = [torch.as_tensor(f(X, Y)) .cuda() for f in fns[:3]]
        co, si = torch.cos(th)[None, :], torch.sin(th)[None, :]
        rr = torch.as_tensor(r).cuda()
        return a, co * ax + si * ay, rr * (-si * ax + co * ay)


mu_r = [2 - 2 * b, -2 * b, -2 - 2 * b, -4 - 2 * b, -6 - 2 * b]
for p, hmax, Nth, tmin, tmax in [(8, 0.5, 512, math.log(1e-4), math.log(1e8)),
                                (12, 0.25, 1024, math.log(1e-5), math.log(1e10)),
                                (16, 0.25, 1024, math.log(1e-5), math.log(1e10))]:
    nb = int(math.ceil((tmax - tmin) / hmax))
    breaks = np.linspace(tmin, tmax, nb + 1)
    ev = Evaluation(Dens(), breaks, p, Nth, c_l=1.0, mu_right=mu_r)
    th = ev.th.cpu().numpy()[None, :]
    r = ev.pan.r[:, None]
    X, Y = r * np.cos(th), r * np.sin(th)
    U1x, U2x, psix = fns[3](X, Y), fns[4](X, Y), fns[5](X, Y)
    U1, U2 = ev.U1.cpu().numpy(), ev.U2.cpu().numpy()
    sc = np.abs(U1x) + np.abs(U2x) + 1e-300
    e1 = np.abs(U1 - U1x) / sc
    e2 = np.abs(U2 - U2x) / sc
    # psi on axis-free points via modes
    print('p %d hmax %.2f Nth %d N %d: max rel err U1 %.2e U2 %.2e; tail fit relres %.1e; parity %s' %
          (p, hmax, Nth, ev.pan.N, e1.max(), e2.max(), ev.tail['right_fit_relres'].max(), ev.parity))
    for rr_ in [1e-3, 0.1, 1.0, 10.0, 1e3, 1e6]:
        i = np.argmin(np.abs(ev.pan.r - rr_))
        print('   r %.3g: rel err U %.2e' % (ev.pan.r[i], max(e1[i].max(), e2[i].max())))
    print('   c: int %.15f (parts %s)  psi %.12f  rho %.15f  (exact 6)' % (ev.c_int, ev.c_int_parts, ev.c_psi, ev.c_rho))
