"""verifier: evaluate a stored trial (PUBLISHED_REPORT 4.2 format) with the independent pipeline.
usage: python3 run_eval.py path.npz p hmax Nth tmin_log10 tmax_log10 tag
Prints residual maxima by region at the nodes and at off-node points, c identities, x*, h(P), velocity at center,
far-field growth; saves axis data and modes to verifier/early_data/<tag>_eval.npz."""
import sys, math, time, json
from pathlib import Path
sys.path.insert(0, 'verifier/early_code')
import numpy as np, torch
from vgen import Trial
from vnum import NumTrial
from vres import Evaluation, TrialDensity, theta_grid, synth, analyse_sin
from scipy.optimize import brentq

path, p, hmax, Nth = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
tmin, tmax = math.log(10 ** float(sys.argv[5])), math.log(10 ** float(sys.argv[6]))
tag = sys.argv[7]
nmax_arg = int(sys.argv[8]) if len(sys.argv) > 8 else None
dev = 'cuda'
_files = np.load(path, allow_pickle=True).files
NUM = 'b' in _files and 'z' not in _files               # numerics-lane state (vnum) or published trial (vgen)
tr = NumTrial(path, dev) if NUM else Trial(path, dev)
k = tr.k
print('trial %s: k %.15f c_l %.15f (file %.15f) p3 %.12f L %.12f' % (path, k, tr.c_l, tr.c_l_file, tr.p3, tr.L))
kn = np.log(tr.interior_knots_r())
b = np.unique(np.concatenate([[tmin, tmax], kn[(kn > tmin) & (kn < tmax)]]))
bb = [b[0]]
for i in range(len(b) - 1):
    m = int(math.ceil((b[i + 1] - b[i]) / hmax))
    bb.extend(list(b[i] + (b[i + 1] - b[i]) * np.arange(1, m + 1) / m))
breaks = np.array(bb)
mu_r = [k + 1, 2 * k, 3 * k - 1, 4 * k - 2, 5 * k - 3]
if NUM:   # far field of r^3 w(r) b(q): exponents k + 1 + n (k - 1) - 2 l; add the l = 1, n = 0 term
    mu_r = [k + 1, 2 * k, 3 * k - 1, k - 1, 4 * k - 2, 5 * k - 3]
dens = TrialDensity(tr)
ev = Evaluation(dens, breaks, p, Nth, c_l=tr.c_l, mu_right=mu_r, nmax=nmax_arg)
out = dict(path=path, p=p, hmax=hmax, Nth=Nth, tmin=tmin, tmax=tmax, N=int(ev.pan.N), panels=int(ev.pan.P),
           nmax=int(ev.ns[-1]))
out['parity'] = ev.parity
out['tail_fit_relres_mode1'] = float(ev.tail['right_fit_relres'][0])
# c identities
c = 3 * tr.c_l - 1
out['c_from_cl'] = c
out['c_int'], out['c_psi'], out['c_rho'] = float(ev.c_int), float(ev.c_psi), float(ev.c_rho)
out['cl_identity_int'] = (1 + ev.c_int) / 3
out['cl_identity_rho'] = (1 + ev.c_rho) / 3
# x*, h(P)
w, P1 = ev.axis_w()
pan = ev.pan
P1n = (2 * ev.ns[None, :] * ev.psi_modes)           # (N, nmax)
S1 = P1n.sum(1)                                       # r P1 = sum 2n psi_n


def P1f(x, d=0):
    t = math.log(x)
    s = pan.interp(S1, [t], 0)[0]
    if d == 0:
        return s / x
    s1 = pan.interp(S1, [t], 1)[0]           # d/dt
    return (s1 - s) / x ** 2                  # d/dx (s/x) = (s_t/x - s)/x^2 ... s_t = x s_x


def wf(x):
    return tr.c_l * x - P1f(x)


i0 = np.where(np.diff(np.sign(w)) != 0)[0]
roots = []
for i in i0:
    if pan.r[i] > 1e-3:
        roots.append(brentq(wf, pan.r[i], pan.r[i + 1], xtol=1e-15, rtol=1e-15))
out['w_zeros'] = roots
if roots:
    xs = roots[0]
    hP = tr.c_l + P1f(xs, 1)
    out['xstar'] = xs
    out['hP_minus_1'] = hP - 1
# velocity at the center: U1/(-x) and U2/y at the smallest radius
i = 0
th = ev.th
U1, U2 = ev.U1[i], ev.U2[i]
xx = pan.r[i] * torch.cos(th)
yy = pan.r[i] * torch.sin(th)
out['center_rmin'] = float(pan.r[0])
out['center_U1_over_minus_x_minus_c'] = float((U1 / (-xx) - c).abs().max())
out['center_U2_over_y_minus_c'] = float((U2 / yy - c).abs().max())
# far-field growth of U
for rq in [1e3, 1e6, 1e9]:
    j = np.argmin(np.abs(pan.r - rq))
    Um = float(torch.sqrt(ev.U1[j] ** 2 + ev.U2[j] ** 2).max())
    out['Umax_over_r_at_%g' % rq] = Um / pan.r[j]
# residual maxima at nodes by region
xs = out.get('xstar', 8.6)
regions = {
    'all': lambda r, t: torch.ones_like(r * t, dtype=torch.bool),
    'nearP_r<0.5': lambda r, t: (r * torch.cos(t) - xs) ** 2 + (r * torch.sin(t)) ** 2 < 0.25,
    'nearP_r<2': lambda r, t: (r * torch.cos(t) - xs) ** 2 + (r * torch.sin(t)) ** 2 < 4.0,
    'r<1e-3': lambda r, t: (r < 1e-3) & (t == t),
    '1e-3<r<1': lambda r, t: (r >= 1e-3) & (r < 1) & (t == t),
    '1<r<30': lambda r, t: (r >= 1) & (r < 30) & (t == t),
    '30<r<1e3': lambda r, t: (r >= 30) & (r < 1e3) & (t == t),
    '1e3<r<1e6': lambda r, t: (r >= 1e3) & (r < 1e6) & (t == t),
    'r>1e6': lambda r, t: (r >= 1e6) & (t == t),
    'near_x_axis_|sin|<0.01': lambda r, t: (torch.sin(t).abs() < 0.01) & (r > 0),
    'near_y_axis_|cos|<0.01': lambda r, t: (torch.cos(t).abs() < 0.01) & (r > 0),
}
res = {}
for nm, fn in regions.items():
    res[nm] = dict(Nf=ev.region_max(fn, 'f'), Nv=ev.region_max(fn, 'v'))
out['nodes'] = res
print(json.dumps(out, indent=1, default=float), flush=True)

# ---- off-node evaluation: radial midpoints between nodes (inside panels), angles shifted by a quarter cell
rng = np.random.default_rng(1)
tq = []
for jp in range(pan.P):
    # two points per panel at random positions
    tq.extend(list(pan.b[jp] + pan.h[jp] * rng.uniform(0.05, 0.95, 2)))
tq = np.array(tq)
rq = np.exp(tq)
thq = (torch.arange(Nth, dtype=torch.float64, device=dev) + 0.25) * 2 * math.pi / Nth
psi_q = pan.interp(ev.psi_modes, tq, 0)          # (Nq, nmax)
dpsi_q = pan.interp(ev.psi_modes, tq, 1)
d2psi_q = pan.interp(ev.psi_modes, tq, 2)
kmax = Nth // 2 - 2
nmax = ev.ns[-1]
nn = torch.as_tensor(ev.ns, dtype=torch.float64, device=dev)
A = torch.zeros((len(tq), kmax + 1), dtype=torch.float64, device=dev)
B = torch.zeros_like(A)
C2 = torch.zeros_like(A)
Z = torch.zeros_like(A)
A[:, 2:2 * nmax + 1:2] = 2 * nn[None, :] * torch.as_tensor(psi_q, device=dev)
B[:, 2:2 * nmax + 1:2] = torch.as_tensor(dpsi_q, device=dev)
C2[:, 2:2 * nmax + 1:2] = torch.as_tensor(d2psi_q, device=dev) - 4 * nn[None, :] ** 2 * torch.as_tensor(psi_q, device=dev)
psith = synth(A, Z, thq, Nth)
rpsir = synth(Z, B, thq, Nth)
lap_r2 = synth(Z, C2, thq, Nth)                     # r^2 Laplace psi
rt = torch.as_tensor(rq, dtype=torch.float64, device=dev)[:, None]
Ur, Uth = -psith / rt, rpsir / rt
co, si = torch.cos(thq)[None, :], torch.sin(thq)[None, :]
U1q, U2q = Ur * co - Uth * si, Ur * si + Uth * co
rho, rr, rth = dens.eval(rq, thq)
rx = co * rr - si * rth / rt
ry = si * rr + co * rth / rt
x, y = rt * co, rt * si
W1, W2 = tr.c_l * x + U1q, tr.c_l * y + U2q
R = W1 * rx + W2 * ry - rho
Nf = (W1 * rx).abs() + (W2 * ry).abs() + rho.abs()
Nv = rho.abs() + (x * rx + y * ry).abs() + (U1q * rx + U2q * ry).abs()
E = -lap_r2 / rt ** 2 - rx
# normalization: ring maximum of |d_x rho| plus the sum of the magnitudes of the modal terms of Laplace psi
magL = (torch.as_tensor(np.abs(d2psi_q) + 4 * ev.ns[None, :] ** 2 * np.abs(psi_q), device=dev).sum(1)) / rt[:, 0] ** 2
E_rel_ring = E.abs().max(1).values / (rx.abs().max(1).values + magL)
E_rel_ring_dx = E.abs().max(1).values / rx.abs().max(1).values
offres = {}
for nm, fn in regions.items():
    m = fn(rt, thq[None, :])
    qf = torch.where(m, (R.abs() / Nf), torch.zeros_like(R))
    qv = torch.where(m, (R.abs() / Nv), torch.zeros_like(R))
    mr = m.any(1)
    er = float(E_rel_ring[mr].max()) if bool(mr.any()) else float('nan')
    er2 = float(E_rel_ring_dx[mr].max()) if bool(mr.any()) else float('nan')
    idx = int(torch.argmax(qf))
    offres[nm] = dict(Nf=float(qf.max()), Nv=float(qv.max()), at_r=float(rq[idx // Nth]),
                      at_th=float(thq[idx % Nth]), E_ring_rel=er, E_ring_rel_dxrho_only=er2)
print('OFF-NODE', json.dumps(offres, indent=1), flush=True)
output_path = Path('verifier/early_data') / ('%s_eval.npz' % tag)
output_path.parent.mkdir(parents=True, exist_ok=True)
np.savez(output_path, breaks=breaks, p=p, t=pan.t, r=pan.r,
         S1=S1, w=w, P1=P1, psi_modes=ev.psi_modes.astype(np.float64), f_modes=ev.f_modes, ns=ev.ns, c_l=tr.c_l,
         summary=json.dumps(out, default=float), offnode=json.dumps(offres))
print('saved')
