"""V185 (diagnostic for V181): the numerics exit map integrates every grid orbit with fixed-step RK4 and ends it with a
linear fraction of the last step (pfwd_gnewton._orbits), so T is only piecewise smooth: its derivative jumps where an
orbit's step count changes. Count, per band of log r, the orbits whose step count ceil(Tt/dt) differs between the base u
and u + e V0 (V0 of V179), and the exit-fraction distribution. Numerics classes imported read only (no bytecode)."""
import sys, time, math
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
S = PM.S; lr = S.lr.cpu().numpy(); dt = PM.dt
bands = [(-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 10.01)]
def orbits(g):
    Wr, Wt, rho = PM.velocity(g); rhs = PM._fields(Wr, Wt)
    LR, TH, Tt, live, it = PM._orbits(rhs, PM.LR.clone(), PM.TH.clone(), PM.orbit_cap)
    k = torch.ceil(Tt / dt - 1e-9).reshape(S.Nr, S.Nth).cpu().numpy(); return k, Tt.reshape(S.Nr, S.Nth).cpu().numpy(), it
Tg0, info0, THex = PM.T_exit(g0); u = (g0 / PM.scale).reshape(-1)
chi = PM.mode_fn(PM.K, THex); sgn = -1.0 if PM.odd_cols[PM.K] else 1.0
def par(v):
    vm = v.reshape(S.Nr, S.Nth); return (0.5 * (vm + sgn * vm[:, PM.flip])).reshape(-1)
b = par((Tg0 * chi / PM.scale).reshape(-1)); v = b / b.norm(); nu = float(u.norm())
k0, Tt0, it0 = orbits(g0)
print('dt %.4g, max steps %d; setup %.1f s' % (dt, it0, time.time() - t0))
print('base: median step count per band: %s' % ' '.join('%d' % np.median(k0[(lr >= a) & (lr < b_)]) for a, b_ in bands))
frac = Tt0 / dt - (k0 - 1)
print('base: exit fraction within 1e-3 of a step boundary, per band: %s' % ' '.join('%.1e' % ((np.minimum(frac, 1 - frac)[(lr >= a) & (lr < b_)] < 1e-3).mean()) for a, b_ in bands), flush=True)
for er in (1e-6, 1e-5, 1e-4, 1e-3):
    gp = (u + er * nu * v).reshape(S.Nr, S.Nth) * PM.scale
    k1, Tt1, it1 = orbits(gp); ch = k1 != k0
    print('eps_rel %.0e: orbits with a changed step count per band (fraction): %s; total %d' % (er, ' '.join('%.1e' % ch[(lr >= a) & (lr < b_)].mean() for a, b_ in bands), int(ch.sum())), flush=True)
print('total %.1f s' % (time.time() - t0))
