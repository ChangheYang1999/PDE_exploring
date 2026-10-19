# Lead (2026-10-18): scalar checks of referee result 17. (1) explicit axis family L = pi eps (l+n)/(l sqrt(4nl - eps^2));
# (2) far-field even axis velocity e_p[A_e] = -(p+1)/sin(pi p/2) int_0^{pi/2} A_e cos((p+2)th) dth, by solving the quadrant ODE
# P'' + (p+1)^2 P = -p cos A_e + sin A_e', P'(0) = 0, P(pi/2) = 0 and by comparing with the closed form for cos^2 and with the
# far-field w_e / r^p of a computed state. Usage: python3 res17chk.py [state.npz p]
import sys, json
import numpy as np
from scipy.integrate import quad, solve_bvp
out = {}
for (l, n, eps) in ((2.0, 3.5, 1.0), (2.0174, 3.5388, -2.0), (1.3, 2.1, 3.0)):
    bo = lambda r: r * (n + l * r * r) / (1 + r * r); we = lambda r: eps * r * r / (1 + r * r)
    L = n * quad(lambda r: 1 / (bo(r) - we(r)) - 1 / (bo(r) + we(r)), 0, np.inf, limit=400)[0]
    out['L_%g_%g_%g' % (l, n, eps)] = (L, np.pi * eps * (l + n) / (l * np.sqrt(4 * n * l - eps ** 2)))
def ep_formula(Ae, p):
    return -(p + 1) / np.sin(np.pi * p / 2) * quad(lambda t: Ae(t) * np.cos((p + 2) * t), 0, np.pi / 2, limit=200)[0]
def ep_ode(Ae, dAe, p):
    f = lambda t, y: np.vstack([y[1], -(p + 1) ** 2 * y[0] - p * np.cos(t) * Ae(t) + np.sin(t) * dAe(t)])
    bc = lambda ya, yb: np.array([ya[1], yb[0]])
    t = np.linspace(0, np.pi / 2, 400)
    s = solve_bvp(f, bc, t, np.zeros((2, t.size)), tol=1e-10, max_nodes=100000)
    return -s.sol(np.pi / 2)[1]
for p in (0.3, 0.49568063771503623, 0.7):
    Ae = lambda t: np.cos(t) ** 2; dAe = lambda t: -np.sin(2 * t)
    out['cos2_p%g' % p] = (ep_formula(Ae, p), ep_ode(Ae, dAe, p), -2 * (p + 1) / (p * (p + 2) * (p + 4)))
if len(sys.argv) > 2:
    a = [0.23901147232367326, -0.7141202145019341, -0.20965511771424156, 0.1219519748982631, 0.10704951266069528, -0.027048386258850764]
    p = float(sys.argv[2])
    Fo = lambda t: a[0] * np.sin(t) + a[2] * np.sin(3 * t) + a[4] * np.sin(5 * t)
    Fe = lambda t: a[1] * np.cos(2 * t) + a[3] * np.cos(4 * t) + a[5] * np.cos(6 * t)
    Ae = lambda t: np.cos(t) ** 2 * np.exp(Fe(t)) * np.cosh(Fo(t))
    h = 1e-6; dAe = lambda t: (Ae(t + h) - Ae(t - h)) / (2 * h)
    out['N6_ep'] = (ep_formula(Ae, p), ep_ode(Ae, dAe, p))
    sys.path.insert(0, 'explore')
    import pforward as PF
    d = np.load(sys.argv[1]); g, lr, th = d['g'], d['lr'], d['th']; Nth = len(th); r = np.exp(lr)
    wr, wt = PF.velocity_p((r ** p)[:, None] * g, lr, th, p)
    we = 0.5 * (wr[:, Nth // 4] - wr[:, 3 * Nth // 4])
    out['state_we_over_rp'] = {str(L): float(we[np.argmin(np.abs(lr - L))] / np.exp(p * L)) for L in (4, 6, 8, 9, 9.5, 9.9)}
print(json.dumps(out, indent=1))
