"""V181: noise versus nonlinearity in the finite-difference products of the numerics linear response (column b1 of PL512b,
code/pfwd_parity.py at the DR512 base), for the first Krylov vector V0 = b/|b| of V179. For eps_rel in 1e-5..1e-3 the
forward product F = (T(u + e v) - Tu)/e and the backward product B = (Tu - T(u - e v))/e are formed (scaled variable, plain
l2, e = eps_rel |u|/|v|), with C = (F + B)/2 (second-order consistent) and D = (F - B)/2 (= e T''[v,v]/2 + noise).
A nonlinear error makes |D| grow like eps_rel; noise makes |D| and the spread of C grow like 1/eps_rel. Per band of log r.
The numerics classes are imported read only (no bytecode written)."""
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
print('setup %.1f s; base th12 %.6f %.6f gamma_ok %s unfinished %s' % (time.time() - t0, info0.get('th1_deg', float('nan')), info0.get('th2_deg', float('nan')), info0.get('gamma_ok'), info0.get('unfinished')), flush=True)
Tg0b, info0b = PM.Tp(g)
print('repeat T at base: |T - T| / |T| = %.3e (determinism)' % float(((Tg0b - Tg0) / PM.scale).norm() / (Tg0 / PM.scale).norm()), flush=True)
chi = PM.mode_fn(j, THex); sgn = -1.0 if PM.odd_cols[j] else 1.0
def par(v):
    vm = v.reshape(S.Nr, S.Nth); return (0.5 * (vm + sgn * vm[:, PM.flip])).reshape(-1)
b = par((Tg0 * chi / PM.scale).reshape(-1)); v = b / b.norm(); nu = float(u.norm())
def Tprod(sig, eps_rel):
    e = eps_rel * nu
    Tgp, inf = PM.Tp((u + sig * e * v).reshape(S.Nr, S.Nth) * PM.scale)
    return sig * par(((Tgp / PM.scale).reshape(-1) - Tu0) / e), inf
Cs = {}
for er in (1e-5, 1e-4, 1e-3):
    F, inf_f = Tprod(1.0, er); Bk, inf_b = Tprod(-1.0, er); C = 0.5 * (F + Bk); D = 0.5 * (F - Bk); Cs[er] = C
    cb = bnorm(C); db = bnorm(D)
    print('eps_rel %.0e: th1 + %.4f - %.4f, th2 + %.4f - %.4f; |C| %.4e |D| %.4e |D|/|C| %.3e' % (er, inf_f['th1_deg'], inf_b['th1_deg'], inf_f['th2_deg'], inf_b['th2_deg'], float(C.norm()), float(D.norm()), float(D.norm() / C.norm())), flush=True)
    print('   per band |D|/|C|: %s' % ' '.join('%.1e' % x for x in db / np.maximum(cb, 1e-300)))
    print('   per band |C|: %s' % ' '.join('%.2e' % x for x in cb), flush=True)
for a, c in ((1e-5, 1e-4), (1e-4, 1e-3)):
    d = Cs[a] - Cs[c]; print('|C(%.0e) - C(%.0e)|/|C(%.0e)| = %.3e; per band: %s' % (a, c, c, float(d.norm() / Cs[c].norm()), ' '.join('%.1e' % x for x in bnorm(d) / np.maximum(bnorm(Cs[c]), 1e-300))))
print('total %.1f s' % (time.time() - t0))
