"""V179: band distribution and finite-difference consistency of the first Krylov vectors of the numerics linear-response
column b1 (code/pfwd_parity.py linear_column, PL512b settings: analytic RHS, podd = 1, eps_rel = 1e-3) at the DR512 base.
The numerics classes are imported read only (no bytecode written); every product is rebuilt here with the same formulas:
b = par(Tg0 chi_j(th_exit)/scale), Lv(v) = v - par((T(u + e v)/scale - Tu0)/e), e = eps_rel |u|/|v| (plain l2).
Reported per band of log r: share of |V_k|^2, the local relative step eps_rel |u| |V_k,band| / |u_band|, and the relative
difference of the products at eps_rel = 1e-4, 1e-3, 1e-2 (linearity)."""
import sys, json, time, math
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
j = PM.K + 0                                                     # column b1
Tg0, info0, THex = PM.T_exit(g); u = (g / PM.scale).reshape(-1); Tu0 = (Tg0 / PM.scale).reshape(-1)
print('setup + T_exit %.1f s; th_exit range %.4f..%.4f' % (time.time() - t0, float(THex.min()), float(THex.max())), flush=True)
chi = PM.mode_fn(j, THex); sgn = -1.0 if PM.odd_cols[j] else 1.0
def par(v):
    vm = v.reshape(S.Nr, S.Nth); return (0.5 * (vm + sgn * vm[:, PM.flip])).reshape(-1)
b = (Tg0 * chi / PM.scale).reshape(-1); print('b even fraction %.3e' % float((b - par(b)).norm() / b.norm())); b = par(b)
nu = float(u.norm()); ub = bnorm(u)
print('|u| %.4e; band |u|: %s' % (nu, ' '.join('%.3e' % x for x in ub)))
def Lv(v, eps_rel):
    e = eps_rel * nu / max(float(v.norm()), 1e-300)
    gp = (u + e * v).reshape(S.Nr, S.Nth) * PM.scale
    Tgp, inf = PM.Tp(gp)
    return v - par(((Tgp / PM.scale).reshape(-1) - Tu0) / e), inf
def report(name, v):
    bn = bnorm(v); n = float(v.norm())
    print('%s |v| %.4e  share of |v|^2 per band: %s' % (name, n, ' '.join('%.3e' % x for x in (bn / n) ** 2)))
    print('%s local relative step (eps_rel 1e-3): %s' % (name, ' '.join('%.2e' % x for x in 1e-3 * nu * (bn / n) / ub)))
V = [b / b.norm()]; report('V0', V[0]); res = {}
for k in range(2):
    ws = {}
    for er in (1e-4, 1e-3, 1e-2):
        t1 = time.time(); w, inf = Lv(V[k], er); ws[er] = w
        print('k %d eps_rel %.0e: |Lv| %.4e  unfinished %s  gamma_ok %s  th12 %.4f %.4f  (%.1f s)' % (k, er, float(w.norm()), inf.get('unfinished'), inf.get('gamma_ok'), inf.get('th1_deg', float('nan')), inf.get('th2_deg', float('nan')), time.time() - t1), flush=True)
    ref = ws[1e-3]; rb = bnorm(ref)
    for er in (1e-4, 1e-2):
        d = ws[er] - ref; db = bnorm(d)
        print('k %d |L(%.0e) - L(1e-3)|/|L(1e-3)| = %.3e ; per band (rel. to band of L(1e-3)): %s' % (k, er, float(d.norm() / ref.norm()), ' '.join('%.1e' % x for x in db / np.maximum(rb, 1e-300))))
    report('Lv%d' % k, ref)
    w = ref.clone()
    for _ in range(2):
        for Vi in V: w = w - torch.dot(Vi, w) * Vi
    V.append(w / w.norm()); report('V%d' % (k + 1), V[-1])
    if k == 1: break
print('total %.1f s' % (time.time() - t0))
