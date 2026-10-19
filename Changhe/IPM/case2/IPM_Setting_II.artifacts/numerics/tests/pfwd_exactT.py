"""specification M26(h) exact-characteristic test (notes of the lead analyst 07:24Z item 3) on a saved forward state (bnewton iterate or bscan/xodd-style npz with g, lr, th,
and the datum coefficients): with the velocity frozen (computed from the state), integrate the FORWARD orbit of every grid point with
g > 1e-3 x (row max) to r_max and form T_exact g = e^{-T} r_max^p A(th_exit) / r^p.  Report: m1(moment + core) of T_exact g minus m1 of the
state (lead criterion < 1e-3), max |log g - log T_exact g| on lr <= -8 and on lr <= -4, and (option ds2=1) the change of m1 when the state is
re-evolved for the same pseudo-time with ds / 2.  Usage: python3 tests/pfwd_exactT.py state.npz [K=32] [ds2=0] [dt=0.005]"""
import sys, json, math, time; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_batch import PFwdB
torch.set_default_dtype(torch.float64)
fn = sys.argv[1]; opt = dict(K=32, ds2=0, dt=0.005, thr=1e-3)
for s_ in sys.argv[2:]:
    k, v = s_.split('='); opt[k] = int(v) if k in ('K', 'ds2') else float(v)
d = np.load(fn, allow_pickle=True); g0 = d['g']; lr = d['lr']; th = d['th']
if 'x' in d.files and 'args' in d.files:
    x = d['x']; a = json.loads(str(d['args'])); p = float(a['p']); coef = x[:-1]
elif 'x' in d.files:
    x = d['x']; p = float(d['p']); coef = x
else:
    a = json.loads(str(d['args'])); p = float(a['p']); coef = np.array(a['par'])
K = len(coef); Nr, Nth = g0.shape; dev = 'cuda'
def Afun(t):
    F = torch.zeros_like(t)
    for j in range(K):
        n = j + 1; F = F + float(coef[j]) * (torch.sin(n * t) if n % 2 == 1 else torch.cos(n * t))
    return torch.cos(t) ** 2 * torch.exp(F)
SB = PFwdB(Nr, Nth, float(lr[0]), float(lr[-1]), p); S = SB.S
g = torch.tensor(g0, device=dev)[None]; pB = torch.tensor([p], device=dev); A = Afun(S.th[None, :])
rho = S.r[None, :, None] ** p * g; Wr, Wt = SB.velocity(rho, pB)
cm, core = SB.c_moment(rho, pB, A); m1_state = 1 / p - float(cm[0])
# forward orbits from all grid points (lr_i, th_j): d lr/dt = V_r/r, d th/dt = V_th/r, until lr >= hi
ar = (1 / p) + Wr / S.r[None, :, None]; at = Wt / S.r[None, :, None]
top = lambda F: F[:, -1:].expand(-1, 2, -1)
arE = SB.extend(ar, top(ar)); atE = SB.extend(at, top(at)); Car = SB.prefilter(arE); Cat = SB.prefilter(atE)
LR = S.lr[:, None].expand(Nr, Nth).reshape(1, -1).clone(); TH = S.th[None, :].expand(Nr, Nth).reshape(1, -1).clone()
T = torch.zeros_like(LR); live = LR < S.hi - 1e-12; dt = opt['dt']; it = 0; t0 = time.time()
def rhs(l_, t_):
    ci = (l_ - S.lo) / S.d; cj = t_ / S.dth
    return SB.eval_bs(Car, arE, ci, cj), SB.eval_bs(Cat, atE, ci, cj)
while bool(live.any()) and it < 400000:
    k1 = rhs(LR, TH); k2 = rhs(LR + 0.5 * dt * k1[0], TH + 0.5 * dt * k1[1]); k3 = rhs(LR + 0.5 * dt * k2[0], TH + 0.5 * dt * k2[1]); k4 = rhs(LR + dt * k3[0], TH + dt * k3[1])
    dl = dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); dth = dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
    over = live & (LR + dl >= S.hi)
    frac = torch.where(over, (S.hi - LR) / torch.clamp(dl, min=1e-300), torch.ones_like(dl))
    LR = torch.where(live, LR + frac * dl, LR); TH = torch.where(live, TH + frac * dth, TH); T = torch.where(live, T + frac * dt, T)
    live = live & ~over; it += 1
Tg = (torch.exp(-T) * math.exp(p * S.hi) * Afun(TH)).reshape(Nr, Nth) / S.r[:, None] ** p
gn = g[0]; rowmax = gn.max(dim=1, keepdim=True).values
msk = gn > opt['thr'] * rowmax
Tg_full = torch.where(msk, Tg, gn)                     # outside the mask keep the state (zeros of A)
rhoT = (S.r[:, None] ** p * Tg_full)[None]; cmT, coreT = SB.c_moment(rhoT, pB, A); m1_T = 1 / p - float(cmT[0])
dlog = (torch.log(torch.clamp(gn, min=1e-300)) - torch.log(torch.clamp(Tg, min=1e-300))).abs()
dlog = torch.where(msk, dlog, torch.zeros_like(dlog)).cpu().numpy(); lrn = lr
out = dict(state=fn, p=p, m1_state=m1_state, m1_Tg=m1_T, dm1=m1_T - m1_state, maxdlog_le_m8=float(dlog[lrn <= -8].max()), maxdlog_le_m4=float(dlog[lrn <= -4].max()),
           maxdlog_all=float(dlog.max()), argmax=[float(lrn[int(np.unravel_index(dlog.argmax(), dlog.shape)[0])]), float(np.degrees(th[int(np.unravel_index(dlog.argmax(), dlog.shape)[1])]))],
           orbit_its=it, orbit_wall=round(time.time() - t0, 1), unfinished=int(live.sum()))
for L in (-12, -10, -8, -6, -4):
    i = int(np.argmin(np.abs(lrn - L))); out['row_lr%d_max' % L] = float(dlog[i].max()); out['row_lr%d_argdeg' % L] = float(np.degrees(th[int(dlog[i].argmax())]))
for lo_, hi_ in ((-12, -8), (-12, -4), (-10, -4)):
    band = (lrn >= lo_ - 1e-9) & (lrn <= hi_ + 1e-9); sub = dlog[band]
    ii, jj = np.unravel_index(sub.argmax(), sub.shape)
    out['band_%d_%d_max' % (lo_, hi_)] = float(sub.max()); out['band_%d_%d_arg' % (lo_, hi_)] = [float(lrn[band][ii]), float(np.degrees(th[jj]))]
print(json.dumps({k: (round(v, 5) if isinstance(v, float) else v) for k, v in out.items()}), flush=True)
if opt['ds2']:
    for ds, n in ((0.02, 600), (0.01, 1200)):
        g2, dg = SB.evolve(g.clone(), pB, A, Afun, ds, n)
        rho2 = S.r[None, :, None] ** p * g2; cm2, _ = SB.c_moment(rho2, pB, A)
        print(json.dumps(dict(ds=ds, steps=n, m1=1 / p - float(cm2[0]), dm1_vs_state=1 / p - float(cm2[0]) - m1_state, dgds=float(dg[0]))), flush=True)
print("EXACTT_DONE", flush=True)
