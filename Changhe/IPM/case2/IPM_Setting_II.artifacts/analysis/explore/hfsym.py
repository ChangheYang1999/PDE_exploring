# Lead exploration (2026-10-18): high-frequency symbol of the forward fixed-point map (heuristic, unverified).
# For an angular perturbation delta log A of high frequency, the forward state changes by delta rho constant-in-phase along
# orbits; the IPM velocity of a stripe pattern is tangent to the stripes (U = -n_1 n^perp delta rho), so delta V = alpha V
# with alpha = -V_2 delta rho / |V|^2: orbits keep their shape and are only re-timed. Then (along the orbit ending at theta)
#     delta rho / rho = delta log A * exp(-int_t^{t_e} q),  q = rho V_2 / |V|^2,
#     delta log |Xi| = delta m1 * (...) + m1 (1 - exp(-Q(theta))) delta log A,  Q = int_{-inf}^{t_e} q dt,
# so the Jacobian J = dc/da of the Gt residual has principal symbol  s(theta) = 1 - 2 m1 (1 - exp(-Q(theta))).
# At m1 = 1/2, s = exp(-Q) > 0. This script computes Q(theta) on a converged state and the predicted J matrix
# (LSQ projection of s phi_j on 1, phi_1..phi_N over |cos| > cut) for comparison with finite-difference columns.
# Usage: python3 hfsym.py state.npz p N [datum a1,..,aN | 0] [nA=1024]
import sys, json
import numpy as np
from scipy.interpolate import RectBivariateSpline
sys.path.insert(0, 'explore')
import pforward as PF
import fpeval as FE

st = np.load(sys.argv[1]); p = float(sys.argv[2]); N = int(sys.argv[3])
a = np.array([float(v) for v in sys.argv[4].split(',')]) if len(sys.argv) > 4 and sys.argv[4] != '0' else np.zeros(N)
nA = int(sys.argv[5]) if len(sys.argv) > 5 else 1024
g, lr, th = st['g'], st['lr'], st['th']
l = 1.0 / p; r = np.exp(lr)
wr, wt = PF.velocity_p((r ** p)[:, None] * g, lr, th, p)
ar = l + wr / r[:, None]; at = wt / r[:, None]
M = PF.node_matrix(ar[20], at[20], th)
m1 = np.linalg.eigvalsh(0.5 * (M + M.T))[0]
pad = 8
thx = np.concatenate([th[-pad:] - 2 * np.pi, th, th[:pad] + 2 * np.pi])
ext = lambda F: np.concatenate([F[:, -pad:], F, F[:, :pad]], axis=1)
Sr = RectBivariateSpline(lr, thx, ext(ar), kx=3, ky=3)
St = RectBivariateSpline(lr, thx, ext(at), kx=3, ky=3)
Sg = RectBivariateSpline(lr, thx, ext(g), kx=3, ky=3)
def rhs(x, t):
    tt = np.mod(t, 2 * np.pi)
    return -Sr.ev(x, tt), -St.ev(x, tt)
def qf(x, t):
    tt = np.mod(t, 2 * np.pi); A_ = Sr.ev(x, tt); B_ = St.ev(x, tt)
    return np.exp((p - 1) * x) * Sg.ev(x, tt) * (A_ * np.sin(tt) + B_ * np.cos(tt)) / (A_ ** 2 + B_ ** 2)
thA = 2 * np.pi * np.arange(nA) / nA
x = np.full(nA, lr[-1]); t = thA.copy(); Q = np.zeros(nA); live = np.ones(nA, bool); dt = 0.01; it = 0
lr0 = -9.0
while live.any() and it < 200000:
    xi, ti = x[live], t[live]
    q1 = qf(xi, ti)
    k1 = rhs(xi, ti); k2 = rhs(xi + 0.5 * dt * k1[0], ti + 0.5 * dt * k1[1])
    k3 = rhs(xi + 0.5 * dt * k2[0], ti + 0.5 * dt * k2[1]); k4 = rhs(xi + dt * k3[0], ti + dt * k3[1])
    xn = xi + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); tn = ti + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    Q[live] += 0.5 * dt * (q1 + qf(xn, tn))
    x[live] = xn; t[live] = tn
    live = live & (x > lr0); it += 1
s = 1 - 2 * m1 * (1 - np.exp(-Q))
cut = 0.05
w = np.abs(np.cos(thA)) > cut
B = FE.basis(thA, N)
X = np.vstack([np.ones_like(thA), B]).T[w]
Jp = np.zeros((N, N))
for j in range(N):
    Jp[:, j] = np.linalg.lstsq(X, (s * B[j])[w], rcond=None)[0][1:]
out = dict(m1=float(m1), Q_minmax=[float(Q.min()), float(Q.max())], s_minmax=[float(s[w].min()), float(s[w].max())],
           Q_deg={str(d): float(Q[int(round(d / 360 * nA)) % nA]) for d in (0, 30, 60, 80, 89, 91, 100, 120, 150, 180, 210, 240, 260, 269, 271, 280, 300, 330)})
print(json.dumps(out))
np.set_printoptions(precision=3, suppress=True, linewidth=150)
print('predicted J (columns = modes):'); print(Jp)
np.savez(sys.argv[1].replace('.npz', '_hfsym.npz'), thA=thA, Q=Q, s=s, Jp=Jp, m1=m1)
