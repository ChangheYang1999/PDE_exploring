"""Damped Picard on the FULL angular datum (no basis truncation) for the fixed-point problem (specification M23(b)):
   log A <- log A - omega (log Gt - mean)  on the far-field angles (A kept as cos^2 exp F, F updated), and p adjusted by a secant step so
   that m1 = 1/2.  Each iteration = one forward steady state (warm start) + the backward tracer.  Reports the Gt defect per iteration.
Usage: python3 tests/pfwd_picardA.py tag p0 "a1,a2,..." [omega=0.3] [iters=30] [nA=1024] [nsteps=700] [Nth=256]"""
import sys, json, math, time; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd import PFwd
from pfwd_fp import FixedPoint
torch.set_default_dtype(torch.float64)
tag = sys.argv[1]; p = float(sys.argv[2]); a0 = [float(v) for v in sys.argv[3].split(',')]
opt = dict(omega=0.3, iters=30, nA=1024, nsteps=700, Nth=256, Nr=661)
for s_ in sys.argv[4:]:
    k, v = s_.split('='); opt[k] = int(v) if k in ('iters', 'nA', 'nsteps', 'Nth', 'Nr') else float(v)
FP = FixedPoint(p, len(a0), Nr=opt['Nr'], Nth=opt['Nth'], nsteps=opt['nsteps'], nA=opt['nA'])
S = FP.S
thA = FP.thA; thA_np = thA.cpu().numpy()
F = torch.zeros_like(thA)
for j, aj in enumerate(a0):
    n = j + 1; F = F + aj * (torch.sin(n * thA) if n % 2 == 1 else torch.cos(n * thA))
mask = (torch.cos(thA).abs() > 0.02)
log = open('runs/pfwd/picA_%s.log' % tag, 'a'); g = None; A_old = None; p_old = p
dm1dp = None; m1_prev = None; p_prev = None
def Afun_from(Ftab):
    Fn = Ftab.cpu().numpy()
    def f(th):
        thn = torch.remainder(th, 2 * math.pi).cpu().numpy()
        Fi = np.interp(thn, thA_np, Fn, period=2 * math.pi)
        return torch.cos(th) ** 2 * torch.exp(torch.tensor(Fi, device=th.device))
    return f
for it in range(opt['iters']):
    t0 = time.time()
    if abs(p - S.p) > 1e-15:
        S.p = p; S.cl = 1 / p; S._build_kernels()
    Af = Afun_from(F); A = Af(S.th)
    if g is None:
        g = ((S.r ** 2 / (1 + S.r ** 2)) ** (1 - p / 2))[:, None] * A[None, :]
    else:
        g = g * (S.r[:, None] / S.r[-1]) ** (p_old - p) * (A[None, :] / torch.clamp(A_old[None, :], min=1e-12))
    for n in range(opt['nsteps']):
        gn, (Wr, Wt) = S.step(g, S_ds := 0.02, A, Af)
        if n == opt['nsteps'] - 1: dg = float((gn - g).abs().max()) / 0.02
        g = gn
    A_old = A; p_old = p
    d = S.diagnostics(g, Wr, Wt, krings=(20,)); m1 = 1 / p - d['c_moment']
    T, u0, w0, th0, nst = FP.trace(Wr, Wt, (1.0, 0.0))
    AA = torch.cos(thA) ** 2 * torch.exp(F)
    logGt = torch.log(torch.clamp(AA, min=1e-300)) - 2 * torch.log(torch.clamp(u0.abs(), min=1e-300)) - 2 * m1 * T
    mean = float(logGt[mask].mean()); dev = (logGt - mean)
    std = float(dev[mask].std()); rng = [float(dev[mask].min()), float(dev[mask].max())]
    def at(deg): return float(dev[int(round(deg / 360 * opt['nA'])) % opt['nA']])
    rec = dict(it=it, p=round(p, 6), m1=round(m1, 6), std=round(std, 5), range=[round(v, 4) for v in rng], at=[round(at(x), 3) for x in (0, 45, 85, 89, 180, 265, 269)], dgds='%.1e' % dg, wall=round(time.time() - t0, 1))
    print(json.dumps(rec), flush=True); log.write(json.dumps(rec) + '\n'); log.flush()
    if std < 2e-3 and abs(m1 - 0.5) < 2e-4:
        break
    # update: F <- F - omega * dev on the masked angles (smooth across the excluded zeros by linear fill)
    dev_np = dev.cpu().numpy().copy(); m_np = mask.cpu().numpy()
    dev_np[~m_np] = np.interp(thA_np[~m_np], thA_np[m_np], dev_np[m_np], period=2 * math.pi)
    F = F - opt['omega'] * torch.tensor(dev_np, device=thA.device)
    # p update (secant on m1 - 1/2; first step uses the slope estimate dm1/dp ~ 0.6 from the Newton Jacobians)
    if m1_prev is not None and abs(p - p_prev) > 1e-6 and abs(m1 - m1_prev) > 1e-6:
        dm1dp = (m1 - m1_prev) / (p - p_prev)
    slope = dm1dp if (dm1dp is not None and abs(dm1dp) > 0.05) else 0.6
    m1_prev, p_prev = m1, p
    p = float(np.clip(p - opt['omega'] * (m1 - 0.5) / slope, 0.2, 0.8))
np.savez('runs/pfwd/picA_%s_state.npz' % tag, g=g.cpu().numpy(), lr=S.lr.cpu().numpy(), th=S.th.cpu().numpy(), hist=json.dumps([rec]),
         args=json.dumps(dict(p=p_old, kind='table', Afile='runs/pfwd/picA_%s_A.npz' % tag)), F=F.cpu().numpy(), thA=thA_np)
np.savez('runs/pfwd/picA_%s_A.npz' % tag, thA=thA_np, A=(np.cos(thA_np) ** 2 * np.exp(F.cpu().numpy())))
print("PICARD_DONE", json.dumps(rec), flush=True)
