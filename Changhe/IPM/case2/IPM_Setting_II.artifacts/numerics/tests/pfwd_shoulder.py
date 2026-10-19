"""Referee suggestion (question 3): the shoulder family
   A_{H,q,s}(th) = cos^2 th (1 + H chi(th)) [1 + tanh(s sin th + q sin th chi(th))],
   chi = exp(1 - 1/(1 - z^2)) for |z| < 1 (0 otherwise), z = 10 (sin^2 th - 5/8): a smooth bump on the shoulders 46.4-58.4 deg (all four
   quadrants), where sin 3th > 0 and cos((p+2) th) < 0 for every p in (0, 1).  Exactly: A_e = cos^2 (1 + H chi), F(pi/2) - F(-pi/2) = 2s.
   q moves mass from the lower to the upper shoulders (positive strain contribution) without changing A_e or the endpoint data; H > H_*(p)
   makes e_p > 0 (H_* = 8.37 at p 0.5, 11.71 at p 0.35).  Test: at s = 0 shoot in q for m1 = 1/2 and read D_ax (if w_e >= 0 everywhere then
   D = T > 0 rigorously).  Batched over (H, q) in one evolution.
Usage: python3 tests/pfwd_shoulder.py tag p "H1,H2" "q1,q2,..." [s=0] [Nth=256] [nsteps=1500] [lo=-14] [Nr=721] [lr0=-13]"""
import sys, json, math, time, os; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_batch import PFwdB
from pfwd_diag import axis_D
torch.set_default_dtype(torch.float64)
tag = sys.argv[1]; p = float(sys.argv[2]); Hs = [float(v) for v in sys.argv[3].split(',')]; qs = [float(v) for v in sys.argv[4].split(',')]
opt = dict(s=0.0, Nth=256, nsteps=1500, lo=-14.0, Nr=721, lr0=-13.0, ds=0.02, nA=1440)
for s_ in sys.argv[5:]:
    k, v = s_.split('='); opt[k] = int(v) if k in ('Nth', 'nsteps', 'Nr', 'nA') else float(v)
dev = 'cuda'
par = [(H, q) for H in Hs for q in qs]; B = len(par)
Ht = torch.tensor([u[0] for u in par], device=dev); qt = torch.tensor([u[1] for u in par], device=dev); s0 = opt['s']
def chi(th):
    z = 10.0 * (torch.sin(th) ** 2 - 0.625)
    inside = z.abs() < 1
    zz = torch.where(inside, z, torch.zeros_like(z))
    return torch.where(inside, torch.exp(1.0 - 1.0 / torch.clamp(1.0 - zz ** 2, min=1e-300)), torch.zeros_like(z))
def Afun(th):                     # th [B, ...]
    shp = (B,) + (1,) * (th.dim() - 1)
    c = chi(th)
    return torch.cos(th) ** 2 * (1 + Ht.view(shp) * c) * (1 + torch.tanh(s0 * torch.sin(th) + qt.view(shp) * torch.sin(th) * c))
SB = PFwdB(opt['Nr'], opt['Nth'], opt['lo'], 10.0, p, dev=dev); S = SB.S
pB = torch.full((B,), p, device=dev)
A = Afun(S.th[None, :].expand(B, -1))
g = ((S.r[None, :, None] ** 2 / (1.0 + S.r[None, :, None] ** 2)) ** (1.0 - p / 2)) * A[:, None, :]
os.makedirs('runs/pfwd/shoulder', exist_ok=True); log = open('runs/pfwd/shoulder/%s.log' % tag, 'a')
def emit(rec):
    line = json.dumps(rec); print(line, flush=True); log.write(line + '\n'); log.flush()
emit(dict(tag=tag, p=p, Hs=Hs, qs=qs, opt=opt, start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
t0 = time.time()
g, dg = SB.evolve(g, pB, A, Afun, opt['ds'], opt['nsteps'])
rho = S.r[None, :, None] ** p * g
Wr, Wt = SB.velocity(rho, pB)
cm, core = SB.c_moment(rho, pB, A)
m1 = 1.0 / p - cm
thA = torch.arange(opt['nA'], device=dev, dtype=torch.float64) * (2 * math.pi / opt['nA'])
T, u0, w0, th0, it, arrived = SB.trace(Wr, Wt, pB, thA, opt['lr0'], dt=0.01, max_it=20000)
emit(dict(trace_its=it, arrived_frac=[round(float(a.double().mean()), 4) for a in arrived]))
Afine = Afun(thA[None, :].expand(B, -1))
logGt = (torch.log(torch.clamp(Afine, min=1e-300)) - 2 * torch.log(torch.clamp(u0.abs(), min=1e-300)) - 2 * m1[:, None] * T).cpu().numpy()
thd = np.degrees(thA.cpu().numpy()); msk = np.abs(np.cos(np.radians(thd))) > 0.05; bulk = np.abs(np.cos(np.radians(thd))) > 0.3
emit(dict(timing=dict(evolve_and_trace=round(time.time() - t0, 1), trace_its=it, B=B)))
print("%-6s %-6s | %-8s %-8s | %-7s %-6s %-6s | %-7s %-7s %-7s %-6s | %-7s %-7s %-7s %-7s %-7s" % ('H', 'q', 'm1', 'core', 'D_ax', 'drU', 'drD', 'D_samp', 'up89', 'low269', 'bulk', 'e_p', 'e_p_ms', 'we_m6', 'Fp-Fm', 'dgds'))
rows = []
for b, (H, q) in enumerate(par):
    lg = logGt[b] - logGt[b][msk].mean(); at = lambda deg: float(lg[int(round(deg / 360 * opt['nA'])) % opt['nA']])
    ax = axis_D(S, g[b], Wr[b], p, float(m1[b]), A=A[b])
    # sign of w_e along the axis: fraction of lr where w_e < 0, and its min/max over r
    Nth = S.Nth; we = 0.5 * (Wr[b, :, Nth // 4] - Wr[b, :, 3 * Nth // 4]).cpu().numpy()
    rec = dict(H=H, q=q, m1=float(m1[b]), core=float(core[b]), D_ax=ax['D_ax_k'], D_ax_res17=ax['D_ax_res17'], drift_up=ax['drift_up'], drift_down=ax['drift_down'],
               D_samp=at(269) - at(89), up89=at(89), low269=at(269), bulk_std=float(lg[bulk].std()), e_p=ax['e_p_formula'], e_p_meas=ax['e_p_measured'],
               we_m6=ax['we_over_r_m6'], Fp_minus_Fm=ax['Fp_minus_Fm_datum'], twoL=ax['twoL_k'], we_neg_frac=float((we < 0).mean()), dgds=float(dg[b]), arrived=float(arrived[b].double().mean()))
    rows.append(rec); emit(rec)
    print("%-6.2f %-6.2f | %-8.5f %-8.5f | %-7.3f %-6.3f %-6.3f | %-7.3f %-7.3f %-7.3f %-6.3f | %-7.3f %-7.3f %-7.3f %-7.3f %-7.1e" % (H, q, rec['m1'], rec['core'], rec['D_ax'], rec['drift_up'], rec['drift_down'], rec['D_samp'], rec['up89'], rec['low269'], rec['bulk_std'], rec['e_p'], rec['e_p_meas'], rec['we_m6'], rec['Fp_minus_Fm'], rec['dgds']))
np.savez('runs/pfwd/shoulder/%s_states.npz' % tag, g=g.cpu().numpy(), lr=S.lr.cpu().numpy(), th=S.th.cpu().numpy(), par=np.array(par), p=p, s=s0, logGt=logGt, thA=thA.cpu().numpy())
print("SHOULDER_DONE", flush=True)
