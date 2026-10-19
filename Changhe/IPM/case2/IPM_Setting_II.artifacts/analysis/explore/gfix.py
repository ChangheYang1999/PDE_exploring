# Lead exploration (2026-10-17): fixed-point update of the datum for the forward finite-p evolution.
# Given a stationary state of pforward.py (datum A), compute the node matrix M = DV(0) (ring fit), its weak eigenvalue
# m1 and direction e1, and trace backward orbits (dX/dt = -V) from the inflow ring r_max to a small ring r0. Along
# orbits rho / |xi|^(1/m1) is constant (V xi = m1 xi, xi = e1.X + o(|X|)), so the datum making G constant is
#     A_new(theta) = |xi(r_max, theta)|^(1/m1) / r_max^p = |u0|^(1/m1) e^T / r_max^p     (T = travel time, u0 = e1.X0).
# G(theta) := A(theta) / A_new(theta) is reported (constant iff the state is rho = C |xi|^(1/m1)).
# Usage: python3 gfix.py state.npz out_table.npz [lr0=-9] [nA=1024] [dt=0.01] [omega=1] [kring=20]
import sys, json, numpy as np
from scipy.interpolate import RectBivariateSpline
sys.path.insert(0, '.')
import pforward as PF

state, outf = sys.argv[1], sys.argv[2]
opt = dict(lr0=-9.0, nA=1024, dt=0.01, omega=1.0, kring=20)
for a in sys.argv[3:]:
    k, v = a.split('='); opt[k] = float(v) if k not in ('nA', 'kring') else int(v)
d = np.load(state); g, lr, th = d['g'], d['lr'], d['th']
args = json.loads(str(d['args'])); p = args['p']; l = 1 / p
r = np.exp(lr); Nr, Nth = g.shape
rhoD = (r ** p)[:, None] * g
wr, wt = PF.velocity_p(rhoD, lr, th, p)
ar = l + wr / r[:, None]; at = wt / r[:, None]
M = PF.node_matrix(ar[opt['kring']], at[opt['kring']], th)
ev, evec = np.linalg.eigh(0.5 * (M + M.T)); m1, m2 = ev
e1 = evec[:, 0] * np.sign(evec[0, 0] if abs(evec[0, 0]) > 1e-12 else 1.0); e2 = np.array([-e1[1], e1[0]])
# periodic extension in theta for the splines
pad = 8
thx = np.concatenate([th[-pad:] - 2 * np.pi, th, th[:pad] + 2 * np.pi])
ext = lambda F: np.concatenate([F[:, -pad:], F, F[:, :pad]], axis=1)
Sr = RectBivariateSpline(lr, thx, ext(ar), kx=3, ky=3)
St = RectBivariateSpline(lr, thx, ext(at), kx=3, ky=3)
def rhs(x, t):
    tt = np.mod(t, 2 * np.pi)
    return -Sr.ev(x, tt), -St.ev(x, tt)
nA = opt['nA']; thA = 2 * np.pi * np.arange(nA) / nA
x = np.full(nA, lr[-1]); t = thA.copy(); T = np.zeros(nA); live = np.ones(nA, bool)
dt = opt['dt']; lr0 = opt['lr0']; it = 0
while live.any() and it < 200000:
    xi, ti = x[live], t[live]
    k1 = rhs(xi, ti); k2 = rhs(xi + 0.5 * dt * k1[0], ti + 0.5 * dt * k1[1])
    k3 = rhs(xi + 0.5 * dt * k2[0], ti + 0.5 * dt * k2[1]); k4 = rhs(xi + dt * k3[0], ti + dt * k3[1])
    x[live] = xi + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
    t[live] = ti + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    T[live] += dt
    live = live & (x > lr0); it += 1
X0 = np.exp(x)[:, None] * np.stack([np.cos(t), np.sin(t)], 1)
u0 = X0 @ e1; w0 = X0 @ e2
logAn = np.log(np.abs(u0)) / m1 + T - p * lr[-1]
An = np.exp(logAn - logAn.max())
A_old = PF.datum(thA, args)
G = A_old / np.maximum(An, 1e-300)
mask = A_old > 1e-3 * A_old.max()
Gm = G[mask]
om = opt['omega']
A_up = (1 - om) * A_old / A_old.max() + om * An
np.savez(outf, A=A_up, thA=thA, An=An, A_old=A_old, G=G, T=T, u0=u0, w0=w0, m1=m1, m2=m2, e1=e1, opt=json.dumps(opt))
print(json.dumps(dict(state=state, p=p, m1=round(float(m1), 5), m2=round(float(m2), 5), e1=[round(float(v), 5) for v in e1],
      M=[round(float(v), 5) for v in M.ravel()], iters=it, Tmax=round(float(T.max()), 2),
      G_ratio_on_support=round(float(Gm.max() / Gm.min()), 4), G_rel_std=round(float(Gm.std() / Gm.mean()), 4),
      An_at=[round(float(np.interp(a, thA, An)), 4) for a in np.radians([0, 30, 60, 80, 90, 100, 120, 150, 180, 270])])))
