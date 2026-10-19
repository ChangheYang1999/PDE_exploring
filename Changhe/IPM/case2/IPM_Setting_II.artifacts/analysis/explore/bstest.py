# Lead: check bspline_torch.interp_bspline against the lead interpolant (p0_forward2.interp_qm, scipy) on a lead state.
# Usage: python3 bstest.py state.npz
import sys, types, numpy as np, torch
sys.path.insert(0, 'explore')
torch.set_default_dtype(torch.float64)
import bspline_torch as BT, p0_forward2 as P2
d = np.load(sys.argv[1]); g = d['g']; Nr, Nth = g.shape
rng = np.random.default_rng(1)
ci = np.arange(Nr)[:, None] + rng.uniform(0, 1.5, (Nr, Nth)); cj = np.arange(Nth)[None, :] + rng.uniform(-1, 1, (Nr, Nth))
ref = P2.interp_qm(g, ci, cj, Nth)
S = types.SimpleNamespace(Nr=Nr, Nth=Nth, limiter=True)
G = torch.tensor(g)[None]
out = BT.interp_bspline(S, G, torch.tensor(ci)[None], torch.tensor(cj)[None], G[:, -1:].expand(-1, 2, -1))[0].numpy()
sc = np.abs(g).max(axis=1, keepdims=True)
for a, b in [(0, 30), (30, Nr - 40), (Nr - 40, Nr - 2)]:
    print('rows %d..%d max |diff| / ring max %.2e' % (a, b, (np.abs(out - ref) / sc)[a:b].max()))
c2 = np.cos(d['th']) ** 2; ok = c2 > 1e-10
rel = np.abs(out - ref)[30:Nr - 40][:, ok] / (sc[30:Nr - 40] * c2[ok])
print('interior, relative to ring max * cos^2: %.2e' % rel.max())
