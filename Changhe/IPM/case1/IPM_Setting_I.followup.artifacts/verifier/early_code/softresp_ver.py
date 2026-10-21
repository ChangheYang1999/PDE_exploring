"""verifier: response of this lane's residual (own exact inverse, vres.Evaluation) along the numerics lane's stored soft
right singular vectors (runs/<tag>_softvecs.pt; scaled coordinates, c_l entry per 1/400, packing z = [b[1:].ravel(), c_l, C],
b[0] = 1), and along random comparison directions.  For each direction v (unit in the scaled coordinates) and s in S:
states z +- s v are written to data/tmp_softresp.npz and evaluated on one fixed panel set (that of the base state);
reported per unit step: max |dR/ds| over the off-node grid (R = W.grad rho - rho), the same relative to the base
normalization max Nf, the scale-free ratio max|dR/ds| / max(|W1 d_x drho| + |W2 d_y drho| + |drho|), d h(P)/ds and
d(3 c_l - 1 - psi_xy(0))/ds.  C (the numerics lane's auxiliary unknown) does not enter this lane's residual.
usage: python3 softresp_ver.py state.npz softvecs.pt nvec"""
import sys, math, json, time
sys.path.insert(0, 'verifier/early_code')
import numpy as np, torch
from vnum import NumTrial
from vres import Evaluation, TrialDensity, synth
from scipy.optimize import brentq

spath, vpath, nvec = sys.argv[1], sys.argv[2], int(sys.argv[3])
dev = 'cuda'
p, hmax, Nth = 12, 0.25, 4096
tmin, tmax = math.log(1e-5), math.log(1e12)
S = (0.05, 0.2)
TMP = 'verifier/early_data/tmp_softresp.npz'
d0 = dict(np.load(spath, allow_pickle=True))
N, M = int(d0['N']), int(d0['M'])
b0 = np.asarray(d0['b'], float); cl0 = float(d0['c_l']); C0 = float(d0['C'])
z0 = np.concatenate([b0[1:].ravel(), [cl0, C0]])
scale = np.ones(z0.size); scale[-2] = 1.0 / 400.0
Sv = torch.load(vpath, map_location='cpu'); V = Sv['Vsoft'].numpy(); ss = Sv['ssoft'].numpy()
assert V.shape[0] == z0.size, (V.shape, z0.size)

breaks = np.arange(tmin, tmax + 1e-12, hmax)
rng = np.random.default_rng(1)
tq = []
for jp in range(len(breaks) - 1):
    tq.extend(list(breaks[jp] + (breaks[jp + 1] - breaks[jp]) * rng.uniform(0.05, 0.95, 2)))
tq = np.array(tq); rq = np.exp(tq)
thq = (torch.arange(Nth, dtype=torch.float64, device=dev) + 0.25) * 2 * math.pi / Nth
rt = torch.as_tensor(rq, dtype=torch.float64, device=dev)[:, None]
co, si = torch.cos(thq)[None, :], torch.sin(thq)[None, :]


def write_state(z):
    d = dict(d0)
    b = b0.copy(); b[1:] = z[:N * M].reshape(N, M)
    d['b'] = b; d['c_l'] = np.float64(z[-2]); d['C'] = np.float64(z[-1])
    np.savez(TMP, **d)
    return TMP


def evaluate(path):
    tr = NumTrial(path, dev)
    k = tr.k
    mu_r = [k + 1, 2 * k, 3 * k - 1, k - 1, 4 * k - 2, 5 * k - 3]
    dens = TrialDensity(tr)
    ev = Evaluation(dens, breaks, p, Nth, c_l=tr.c_l, mu_right=mu_r)
    pan = ev.pan
    S1 = (2 * ev.ns[None, :] * ev.psi_modes).sum(1)
    def P1f(x, dd=0):
        t = math.log(x); s = pan.interp(S1, [t], 0)[0]
        if dd == 0:
            return s / x
        return (pan.interp(S1, [t], 1)[0] - s) / x ** 2
    w, _ = ev.axis_w()
    i0 = np.where(np.diff(np.sign(w)) != 0)[0]
    roots = [brentq(lambda x: tr.c_l * x - P1f(x), pan.r[i], pan.r[i + 1], xtol=1e-15, rtol=1e-15) for i in i0 if pan.r[i] > 1e-3]
    xs = roots[0]
    hP = tr.c_l + P1f(xs, 1)
    nmax = ev.ns[-1]; kmax = Nth // 2 - 2
    nn = torch.as_tensor(ev.ns, dtype=torch.float64, device=dev)
    psi_q = pan.interp(ev.psi_modes, tq, 0); dpsi_q = pan.interp(ev.psi_modes, tq, 1)
    Aa = torch.zeros((len(tq), kmax + 1), dtype=torch.float64, device=dev); Bb = torch.zeros_like(Aa); Z = torch.zeros_like(Aa)
    Aa[:, 2:2 * nmax + 1:2] = 2 * nn[None, :] * torch.as_tensor(psi_q, device=dev)
    Bb[:, 2:2 * nmax + 1:2] = torch.as_tensor(dpsi_q, device=dev)
    psith = synth(Aa, Z, thq, Nth); rpsir = synth(Z, Bb, thq, Nth)
    Ur, Uth = -psith / rt, rpsir / rt
    U1q, U2q = Ur * co - Uth * si, Ur * si + Uth * co
    rho, rr, rth = dens.eval(rq, thq)
    rx = co * rr - si * rth / rt; ry = si * rr + co * rth / rt
    x, y = rt * co, rt * si
    W1, W2 = tr.c_l * x + U1q, tr.c_l * y + U2q
    R = W1 * rx + W2 * ry - rho
    Nf = (W1 * rx).abs() + (W2 * ry).abs() + rho.abs()
    return dict(R=R, Nf=Nf, rho=rho, rx=rx, ry=ry, W1=W1, W2=W2, hP=hP - 1, xs=xs,
                ident=3 * tr.c_l - 1 - float(ev.c_int), cl=tr.c_l)


t0 = time.time()
E0 = evaluate(write_state(z0))
Nf0 = float(E0['Nf'].max())
relR0 = float((E0['R'].abs() / E0['Nf'].clamp_min(1e-300)).max())
print(f'base {spath}: c_l {cl0:.12f} x* {E0["xs"]:.9f} h(P)-1 {E0["hP"]:+.4e} ident {E0["ident"]:+.4e} '
      f'max|R| {float(E0["R"].abs().max()):.3e} max Nf {Nf0:.3e} max |R|/Nf {relR0:.3e}  ({time.time() - t0:.1f}s)', flush=True)
farm = (rt >= 100) & (thq[None, :] * 180 / math.pi >= 80) & (thq[None, :] * 180 / math.pi <= 100)
dirs = []
for i in range(min(nvec, V.shape[1])):
    v = scale * V[:, i]; dirs.append((f'soft{i} sigma {ss[i]:.3e}', v / np.linalg.norm(v)))
g = np.random.default_rng(7)
v = g.standard_normal(z0.size); v[-1] = 0.0; dirs.append(('random (all nodes)', v / np.linalg.norm(v)))
with np.errstate(divide='ignore'):   # q = 1 - (1 + u^2)^(-(1-k)/2), so 1 + u^2 = (1 - q)^(-2/(1-k))
    r_nodes = (1.0 - np.asarray(d0['q'], float)[1:]) ** (-2.0 / (1.0 - 1.0 / cl0))
r_nodes = float(d0['L']) * np.sqrt(np.maximum(r_nodes - 1.0, 0.0))
thd = np.asarray(d0['theta'], float) * 180 / math.pi
mask = (r_nodes[:, None] >= 100) & (thd[None, :] >= 80)
v = g.standard_normal((N, M)) * mask; v = np.concatenate([v.ravel(), [0.0, 0.0]]); dirs.append(('random (r>100, theta>80)', v / np.linalg.norm(v)))
rows = []
for name, v in dirs:
    out = dict(name=name, dcl=float(v[-2]), dC=float(v[-1]))
    for s in S:
        Ep = evaluate(write_state(z0 + s * v)); Em = evaluate(write_state(z0 - s * v))
        dR = (Ep['R'] - Em['R']) / (2 * s)
        drho = (Ep['rho'] - Em['rho']) / (2 * s); drx = (Ep['rx'] - Em['rx']) / (2 * s); dry = (Ep['ry'] - Em['ry']) / (2 * s)
        Nd = (E0['W1'] * drx).abs() + (E0['W2'] * dry).abs() + drho.abs()
        o = dict(maxdR=float(dR.abs().max()), maxdR_rel=float(dR.abs().max()) / Nf0, ratio=float(dR.abs().max() / Nd.max()),
                 ratio_far=float(dR[farm].abs().max() / Nd[farm].max()) if bool(farm.any()) else float('nan'),
                 l2ratio=float(dR.norm() / Nd.norm()),
                 dhP=(Ep['hP'] - Em['hP']) / (2 * s), dident=(Ep['ident'] - Em['ident']) / (2 * s))
        out[str(s)] = o
        print(f'  {name:28s} s {s:4.2f}: max|dR/ds| {o["maxdR"]:.3e} (/max Nf {o["maxdR_rel"]:.3e}) ratio {o["ratio"]:.3e} '
              f'(far {o["ratio_far"]:.3e}, l2 {o["l2ratio"]:.3e}) dh(P)/ds {o["dhP"]:+.3e} dident/ds {o["dident"]:+.3e} dc_l {out["dcl"]:+.2e}', flush=True)
    rows.append(out)
json.dump(dict(state=spath, vecs=vpath, base=dict(hP=E0['hP'], ident=E0['ident'], xs=E0['xs'], relR0=relR0, Nf0=Nf0), rows=rows),
          open('verifier/early_runs/softresp_ver_%s.json' % spath.split('/')[-1].replace('.npz', ''), 'w'),
          indent=1, default=float)
print('done %.1fs' % (time.time() - t0))
