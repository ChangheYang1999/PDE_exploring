"""V187: per-cell anatomy of the core finite-difference product of the numerics exit map (code/pfwd_parity.py, DR512 base,
limiter as in the numerics runs), x-odd direction V0 = b1/|b1| of V179. Fine scan e = eps_rel |u|, eps_rel log-spaced
from 1e-7 to 1e-3. For the core rows (log r < -8) the exit angle TH, the travel time Tt (recovered from
Tg = exp(-Tt) e^(p hi) A(TH) / r^p) and Tg are stored for every eps, together with th1, th2. The odd part of the product
is then split into the travel-time part and the angular-factor part log A(TH; th1, th2), and the offset delta = TH - th1
(or TH - th2) of each core exit angle from the moving Gamma angle is followed. Numerics classes imported read only."""
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
print("limiter", PM.SB.limiter, flush=True)
S = PM.S; g = g0; lr = S.lr.cpu().numpy(); Nr, Nth = S.Nr, S.Nth
nc = int((lr < -8).sum())
j = PM.K + 0
Tg0, info0, TH0 = PM.T_exit(g); u = (g / PM.scale).reshape(-1)
chi = PM.mode_fn(j, TH0); sgn = -1.0 if PM.odd_cols[j] else 1.0
def par(vm):
    return 0.5 * (vm + sgn * vm[:, PM.flip])
b = par(Tg0 * chi / PM.scale).reshape(-1); v = b / b.norm(); nu = float(u.norm())
rp = (S.r[:, None] ** p)
def unpack(Tg, TH, th12):
    A = PM.Afun(TH, th12)
    Tt = -torch.log(torch.clamp(Tg * rp / (math.exp(p * S.hi) * A), min=1e-300))
    return Tt[:nc].cpu().numpy(), TH[:nc].cpu().numpy(), Tg[:nc].cpu().numpy(), A[:nc].cpu().numpy()
base = unpack(Tg0, TH0, (math.radians(info0['th1_deg']), math.radians(info0['th2_deg'])))
ers = np.logspace(-7, -3, 17)
out = dict(ers=ers, lr=lr[:nc], scale=PM.scale[:nc, 0].cpu().numpy(), v=v.reshape(Nr, Nth)[:nc].cpu().numpy(), nu=nu,
           Tt0=base[0], TH0=base[1], Tg0=base[2], A0=base[3], th10=info0['th1_deg'], th20=info0['th2_deg'], flip=PM.flip.cpu().numpy())
Tts, THs, Tgs, As, th1s, th2s = [], [], [], [], [], []
print('setup %.1f s, core rows %d, |u| %.4e, base th12 %.6f %.6f' % (time.time() - t0, nc, nu, info0['th1_deg'], info0['th2_deg']), flush=True)
for er in ers:
    t1 = time.time()
    Tg, inf, TH = PM.T_exit((u + er * nu * v).reshape(Nr, Nth) * PM.scale)
    th12 = (math.radians(inf['th1_deg']), math.radians(inf['th2_deg']))
    a = unpack(Tg, TH, th12); Tts.append(a[0]); THs.append(a[1]); Tgs.append(a[2]); As.append(a[3]); th1s.append(inf['th1_deg']); th2s.append(inf['th2_deg'])
    print('eps_rel %.3e th1 %.7f th2 %.7f unfinished %d (%.1f s)' % (er, inf['th1_deg'], inf['th2_deg'], inf['unfinished'], time.time() - t1), flush=True)
    out.update(Tt=np.array(Tts), TH=np.array(THs), Tg=np.array(Tgs), A=np.array(As), th1=np.array(th1s), th2=np.array(th2s))
    np.savez_compressed('runs/v187_cells.npz', **out)
print('total %.1f s' % (time.time() - t0))
