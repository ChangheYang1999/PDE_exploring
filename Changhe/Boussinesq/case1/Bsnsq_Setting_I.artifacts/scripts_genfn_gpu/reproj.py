# copy of scripts_genfn_cpu/reproj.py (CPU), used with this folder's device-aware jets/model (CPU tensors stay on the CPU)
"""Re-project a generating-function state onto another basis (J, Kw, alpha, se): least-squares fit of the jets
G_x, G_x eta (= A) and G_xx (= B0) of the old state at the collocation-type points of both bases (relative weights),
with the H(0,0) = 1 row. Usage: python3 reproj.py old.npz new.npz J Kw alpha se [gam]"""
import sys, numpy as np, torch
torch.set_num_threads(1)
from jets import monos, DT
from model import Model, ts_to_xeta
d = dict(np.load(sys.argv[1])); d['files'] = list(d.keys()); out = sys.argv[2]
J, Kw, alpha, se = int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6])
gam = float(sys.argv[7]) if len(sys.argv) > 7 and not sys.argv[7].startswith('--') else 0.0
lsc = float(sys.argv[sys.argv.index('--scale') + 1]) if '--scale' in sys.argv else 1.0   # dilation X -> l X: G_l(x, eta) = l^2 G(x/l, eta/l)
J0, K0 = int(d['J']), int(d['Kw']); a0_ = float(d['alpha']) if 'alpha' in d['files'] else 0.0; s0 = float(d['se']) if 'se' in d['files'] else 1.0; g0 = float(d['gam']) if 'gam' in d['files'] else 0.0
m_ = int(d['m']) if 'm' in d['files'] else 3
mn_ = int(sys.argv[sys.argv.index('--m') + 1]) if '--m' in sys.argv else m_      # new m (beta = 2m/(m-1)); fit only r < rfit if given
rfit = float(sys.argv[sys.argv.index('--rfit') + 1]) if '--rfit' in sys.argv else None
old = Model(J0, K0, m=m_, alpha=a0_, se=s0, gam=g0); new = Model(J, Kw, m=mn_, alpha=alpha, se=se, gam=gam)
def pts(Nt, Ns, tmin, alpha, se, shift, gam, m_):
    it = (np.arange(Nt) + 0.5 + shift) / Nt; is_ = (np.arange(Ns) + 0.5 + shift) / Ns
    tau = 0.5 * (1 - np.cos(np.pi * it)); t = tau if alpha <= 0 else 1 - (np.exp(alpha * (1 - tau)) - 1) / (np.exp(alpha) - 1)
    t = tmin + (1 - tmin) * t; s = 0.5 * (1 - np.cos(np.pi * is_))
    T, S = np.meshgrid(t, s, indexing='ij'); T = T.ravel(); S = S.ravel()
    S = S if gam <= 0 else (np.exp(gam * S) - 1) / (np.exp(gam) - 1)
    x, eta = ts_to_xeta(T, S, m_, se); k = (x > 1e-12) & (eta > 1e-12)
    return x[k], eta[k]
xa, ea = pts(3 * J + 10, 3 * Kw + 10, 0.008 ** (3.0 / mn_), alpha, se, 0.0, gam, mn_)
xb, eb = pts(3 * J0 + 10, 3 * K0 + 10, 0.008 ** (3.0 / m_), a0_, s0, 0.21, g0, m_); xb, eb = lsc * xb, lsc * eb
x = torch.tensor(np.concatenate([xa, xb])); e = torch.tensor(np.concatenate([ea, eb]))
if rfit is not None:
    gx = torch.cat([lsc * (old.basis_matrix(x[ch] / lsc, e[ch] / lsc, p=1)[monos(1)[1][(1, 0)]] @ torch.tensor(d['c'])) for ch in torch.split(torch.arange(x.shape[0]), 1500)])
    keep = torch.hypot(x, gx) < rfit; x, e = x[keep], e[keep]; print('rfit %g: %d points' % (rfit, int(keep.sum())))
L, ix = monos(2)
rows = []; rhs = []
co = torch.tensor(d['c'])
for ch in torch.split(torch.arange(x.shape[0]), 1500):
    Bo = old.basis_matrix(x[ch] / lsc, e[ch] / lsc, p=2) @ co; Bo[ix[(1, 0)]] *= lsc; Bo[ix[(0, 0)]] *= lsc ** 2; Bn = new.basis_matrix(x[ch], e[ch], p=2)
    for key in [(1, 0), (1, 1), (2, 0)]:
        tgt = Bo[ix[key]]
        sc = 1.0 / (tgt.abs() + 1e-3 * Bo[ix[(1, 1)]].abs() * (1 + x[ch]))
        rows.append((Bn[ix[key]] * sc[:, None]).numpy()); rhs.append((tgt * sc).numpy())
Aw = np.vstack(rows + [1e6 * new.h00_row()[None, :]]); bw = np.concatenate(rhs + [[1e6]])
ridge = float(sys.argv[sys.argv.index('--ridge') + 1]) if '--ridge' in sys.argv else 0.0   # Tikhonov weight on c (unscaled)
nfit = Aw.shape[0]
if ridge > 0:
    Aw = np.vstack([Aw, ridge * np.eye(Aw.shape[1])]); bw = np.concatenate([bw, np.zeros(Aw.shape[1])])
scn = np.linalg.norm(Aw, axis=0); scn[scn == 0] = 1
sol, *_ = np.linalg.lstsq(Aw / scn, bw, rcond=1e-15)
c = sol / scn
res = (Aw @ c - bw)[:nfit - 1]
print('max |c| %.3e  |c|_2 %.3e' % (np.abs(c).max(), np.linalg.norm(c)))
nR = x.shape[0]
Gx_old = np.concatenate([lsc * (old.basis_matrix(x[ch] / lsc, e[ch] / lsc, p=1)[monos(1)[1][(1, 0)]] @ co).numpy() for ch in torch.split(torch.arange(nR), 1500)])
rad = np.hypot(x.numpy(), Gx_old); phd = np.degrees(np.arctan2(Gx_old, x.numpy()))
rk = np.abs(res).reshape(-1)
# rows are stacked per chunk as (Gx, A, B0) blocks; recover per-point max over the three rows
per = np.zeros(nR); pos = 0
for ch in torch.split(torch.arange(nR), 1500):
    n = len(ch)
    blk = rk[pos:pos + 3 * n].reshape(3, n); per[ch.numpy()] = blk.max(0); pos += 3 * n
for lo, hi in [(0, 0.1), (0.1, 1), (1, 10), (10, 1e3), (1e3, 1e5), (1e5, 1e12)]:
    for plo, phi_ in [(0, 45), (45, 85), (85, 90.1)]:
        m = (rad >= lo) & (rad < hi) & (phd >= plo) & (phd < phi_)
        if m.any(): print('  r [%g,%g) phi [%g,%g): max rel err %.2e (%d pts)' % (lo, hi, plo, phi_, per[m].max(), m.sum()))
print('reproj %s -> J %d Kw %d alpha %g se %g gam %g: rms rel %.2e max rel %.2e  H00 %.12f' % (sys.argv[1], J, Kw, alpha, se, gam,
      np.sqrt(np.mean(res ** 2)), np.abs(res).max(), new.h00_row() @ c))
np.savez(out, c=c, a0=float(d['a0']), J=J, Kw=Kw, m=mn_, beta=new.beta, l=float(d['l']) if 'l' in d['files'] else 1.0, src=sys.argv[1],
         alpha=alpha, se=se, gam=gam)
