"""V182: eps scan of the finite-difference product of the numerics exit map (code/pfwd_parity.py, DR512 base) in the
x-odd direction V0 = b1/|b1| of V179. By the reflection symmetry (u x-even, v x-odd) the odd part of T(u + e v) is odd in
e, so the forward product C(e) = par(T(u + e v) - Tu)/e has error O(e^2) if T is smooth; a smooth map gives band changes
C(e) - C(e') shrinking like e^2. Also splits v = v_core (log r < -8) + v_out and checks additivity of the products, to
see whether the core rows respond to the core part of v or to the rest. Numerics classes imported read only."""
import sys, time
sys.dont_write_bytecode = True
import numpy as np, torch
sys.path.insert(0, 'code')
torch.set_default_dtype(torch.float64)
from pfwd_parity import ParityMap, load_base
t0 = time.time()
fn = 'runs/pfwd/bn/DR512_a2-1.000_it0.npz'
g0, coef, F_odd0, p, lo, hi = load_base(fn, 512)
K = Ko = 16; F_even = np.zeros(K); F_even[:min(K, len(coef))] = coef[:K]; F_odd = np.zeros(Ko)
PM = ParityMap(g0.shape[0], 512, lo, hi, p, F_even, F_odd, xeven=False)
S = PM.S; g = g0; lr = S.lr.cpu().numpy()
bands = [(-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 10.01)]
masks = [torch.tensor((lr >= a) & (lr < b), device=g.device) for a, b in bands]
def bnorm(v):
    vm = v.reshape(S.Nr, S.Nth); return np.array([float(vm[m].norm()) for m in masks])
j = PM.K + 0
Tg0, info0, THex = PM.T_exit(g); u = (g / PM.scale).reshape(-1); Tu0 = (Tg0 / PM.scale).reshape(-1)
chi = PM.mode_fn(j, THex); sgn = -1.0 if PM.odd_cols[j] else 1.0
def par(v):
    vm = v.reshape(S.Nr, S.Nth); return (0.5 * (vm + sgn * vm[:, PM.flip])).reshape(-1)
b = par((Tg0 * chi / PM.scale).reshape(-1)); v = b / b.norm(); nu = float(u.norm())
core = torch.tensor(lr < -8, device=g.device)[:, None].expand(S.Nr, S.Nth).reshape(-1)
v_core = torch.where(core, v, torch.zeros_like(v)); v_out = v - v_core
print('setup %.1f s; |v_core|^2 = %.4f, |v_out|^2 = %.4f' % (time.time() - t0, float(v_core.norm() ** 2), float(v_out.norm() ** 2)), flush=True)
def C(w, e):
    Tgp, inf = PM.Tp((u + e * w).reshape(S.Nr, S.Nth) * PM.scale)
    return par(((Tgp / PM.scale).reshape(-1) - Tu0) / e), inf
Cs = {}; ers = (1e-7, 1e-6, 3e-6, 1e-5, 3e-5, 1e-4, 3e-4, 1e-3)
for er in ers:
    t1 = time.time(); c, inf = C(v, er * nu); Cs[er] = c
    print('eps_rel %.0e: th1 %.6f th2 %.6f |C| %.4e  band |C|: %s  (%.1f s)' % (er, inf['th1_deg'], inf['th2_deg'], float(c.norm()), ' '.join('%.3e' % x for x in bnorm(c)), time.time() - t1), flush=True)
ref = Cs[1e-5]; rb = bnorm(ref)
for er in ers:
    d = Cs[er] - ref
    print('C(%.0e) - C(1e-5): rel %.3e; per band rel. to band of C(1e-5): %s' % (er, float(d.norm() / ref.norm()), ' '.join('%.1e' % x for x in bnorm(d) / np.maximum(rb, 1e-300))))
for a, c2 in zip(ers[:-1], ers[1:]):
    d = Cs[a] - Cs[c2]
    print('C(%.0e) - C(%.0e): per band rel.: %s' % (a, c2, ' '.join('%.1e' % x for x in bnorm(d) / np.maximum(bnorm(Cs[c2]), 1e-300))))
for er in (1e-5, 1e-4):
    cc, _ = C(v_core, er * nu); co, _ = C(v_out, er * nu); s = cc + co; d = s - Cs[er]
    print('eps_rel %.0e split: band |C(v_core)|: %s' % (er, ' '.join('%.2e' % x for x in bnorm(cc))))
    print('eps_rel %.0e split: band |C(v_out)|:  %s' % (er, ' '.join('%.2e' % x for x in bnorm(co))))
    print('eps_rel %.0e additivity |C(core)+C(out)-C(v)| per band rel.: %s' % (er, ' '.join('%.1e' % x for x in bnorm(d) / np.maximum(bnorm(Cs[er]), 1e-300))), flush=True)
print('total %.1f s' % (time.time() - t0))
