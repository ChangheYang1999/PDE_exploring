"""x-odd (asymmetric) forward test with MOVABLE ZEROS at high angular resolution (PROMPT section 5: asymmetry must not be excluded by the
ansatz; specification M25(e): x-odd data need the zeros as free parameters because the strong-orbit exits b+- must coincide with the zeros).
Datum (lead chart, explore/fpfull.py):  A(th) = 4 S(th)^2 exp(F(th)),  S = (cos(Dz/2) - cos(th - sig))/2, zeros z+ = sig - Dz/2, z- = sig + Dz/2
(sig = 180 deg, Dz = 180 deg: 4 S^2 = cos^2 th, the x-even zeros +-90 deg; dsig rotates both zeros, dDz moves them apart).  F = x-even N = 6 part (sin th, cos 2th, sin 3th, cos 4th, sin 5th, cos 6th) + x-odd
part e_1 cos th + e_2 sin 2th + e_3 cos 3th.  Batched over (sig shift, Dz shift, e_1, e_2, e_3) rows given on the command line.
Outputs per state: m1, m2 and the weak eigenvector angle e1 (ring fit at r = e^lr_ring), psi_xy(0) = c and psi_yy(0) = -d (strain moments:
c = (1/pi) int rho r^-3 sin 3th, d = psi_xx(0) = (1/pi) int rho r^-3 cos 3th; Setting II orientation needs d = 0), the strong-orbit exits b+-
(sign changes of u0 = X0.e1 on the exit circle) against the datum zeros z+-, the regular tracer residual Fr = log A - 2 log|Xi| - 2 log|S_z|
+ 2 log|S_b| (its std over |S_z|, |S_b| > cut), and the raw log Gt range.  Nothing is imposed on the state.
Usage: python3 tests/pfwd_xodd.py tag p "a1,..,a6" "dsig,dDz,e1,e2,e3;dsig,dDz,e1,e2,e3;..." [Nth=1024] [nsteps=1500] [lo=-14] [Nr=721] [lr0=-13] [ring=-11]"""
import sys, json, math, time, os; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_batch import PFwdB
torch.set_default_dtype(torch.float64)
tag = sys.argv[1]; p = float(sys.argv[2]); a6 = [float(v) for v in sys.argv[3].split(',')]
rows = [[float(v) for v in r.split(',')] for r in sys.argv[4].split(';')]
opt = dict(Nth=1024, nsteps=1500, lo=-14.0, Nr=721, lr0=-13.0, ring=-11.0, ds=0.02, nA=2880, cut=0.03, max_it=8000)
for s_ in sys.argv[5:]:
    k, v = s_.split('='); opt[k] = int(v) if k in ('Nth', 'nsteps', 'Nr', 'nA', 'max_it') else float(v)
dev = 'cuda'; B = len(rows)
P = torch.tensor(rows, device=dev)                       # [B, 5]: dsig (deg), dDz (deg), e1, e2, e3
sig = math.pi + torch.deg2rad(P[:, 0]); Dz = math.pi + torch.deg2rad(P[:, 1])      # sig = 180 deg, Dz = 180 deg: S = cos(th)/2, zeros +-90 deg
zp = sig - Dz / 2; zm = sig + Dz / 2                     # datum zeros
def S_of(th, sigv, Dzv):
    return 0.5 * (torch.cos(Dzv / 2) - torch.cos(th - sigv))
def Afun(th):                                            # th [B, ...]
    shp = (B,) + (1,) * (th.dim() - 1)
    F = torch.zeros_like(th)
    for j, aj in enumerate(a6):
        n = j + 1; F = F + aj * (torch.sin(n * th) if n % 2 == 1 else torch.cos(n * th))
    F = F + P[:, 2].view(shp) * torch.cos(th) + P[:, 3].view(shp) * torch.sin(2 * th) + P[:, 4].view(shp) * torch.cos(3 * th)
    return 4 * S_of(th, sig.view(shp), Dz.view(shp)) ** 2 * torch.exp(F)
SB = PFwdB(opt['Nr'], opt['Nth'], opt['lo'], 10.0, p, dev=dev); S = SB.S
pB = torch.full((B,), p, device=dev)
A = Afun(S.th[None, :].expand(B, -1))
g = ((S.r[None, :, None] ** 2 / (1.0 + S.r[None, :, None] ** 2)) ** (1.0 - p / 2)) * A[:, None, :]
os.makedirs('runs/pfwd/xodd', exist_ok=True); log = open('runs/pfwd/xodd/%s.log' % tag, 'a')
def emit(rec):
    line = json.dumps(rec); print(line, flush=True); log.write(line + '\n'); log.flush()
emit(dict(tag=tag, p=p, a6=a6, rows=rows, opt=opt, start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
t0 = time.time()
g, dg = SB.evolve(g, pB, A, Afun, opt['ds'], opt['nsteps'])
rho = S.r[None, :, None] ** p * g
Wr, Wt = SB.velocity(rho, pB)
# strain moments c (sin 3th) and d (cos 3th), with core terms and outer tails
wl = torch.full((S.Nr,), S.d, device=dev); wl[0] = 0.5 * S.d; wl[-1] = 0.5 * S.d
w = (S.r ** (-1) * wl)[None, :, None] * S.dth / math.pi
rmax = float(S.r[-1]); tail = rmax ** (p - 1) / (1 - p); r0 = float(S.r[0])
def moment(trig):
    grid = (rho * trig[None, None, :] * w).sum(dim=(1, 2))
    a3 = (A * trig[None, :]).sum(dim=1) * S.dth / math.pi
    core = r0 / math.pi * ((rho[:, 0, :] / r0 ** 2) * trig[None, :]).sum(dim=1) * S.dth
    return grid + a3 * tail + core
c = moment(torch.sin(3 * S.th)); d = moment(torch.cos(3 * S.th))
m1_mom = 1.0 / p - c
# ring fit of DV(0) at r = e^ring
k = int(np.argmin(np.abs(S.lr.cpu().numpy() - opt['ring'])))
ar = (1.0 / p) + Wr[:, k, :] / S.r[k]; at = Wt[:, k, :] / S.r[k]
rings = []
for b in range(B):
    M = S.node_matrix(ar[b], at[b]); Ms = 0.5 * (M + M.T); ev, evec = torch.linalg.eigh(Ms)
    e1 = evec[:, 0]; ang = math.degrees(math.atan2(float(e1[1]), float(e1[0])))
    if ang > 90: ang -= 180
    if ang <= -90: ang += 180
    rings.append((float(ev[0]), float(ev[1]), ang, float(M[1, 0] - M[0, 1]), M))
# tracer with e1 = ring weak eigenvector per state
thA = torch.arange(opt['nA'], device=dev, dtype=torch.float64) * (2 * math.pi / opt['nA'])
T, u0x, w0x, th0, it, arrived = SB.trace(Wr, Wt, pB, thA, opt["lr0"], dt=0.01, max_it=int(opt.get("max_it", 8000)), e1=(1.0, 0.0))
Afine = Afun(thA[None, :].expand(B, -1))
emit(dict(timing=dict(total=round(time.time() - t0, 1), trace_its=it), arrived=[round(float(a.double().mean()), 4) for a in arrived]))
print("%-26s | %-8s %-8s %-7s %-8s %-8s | %-9s %-9s %-9s %-9s | %-7s %-7s %-7s | %-7s" % ('row (dsig,dDz,e1,e2,e3)', 'm1_mom', 'm1_ring', 'm2_ring', 'e1_deg', 'd=psixx', 'z+ (deg)', 'b+ (deg)', 'z- (deg)', 'b- (deg)', 'Fr_std', 'Gt_rng', 'bulk', 'dgds'))
for b in range(B):
    m1r, m2r, ang, asym, M = rings[b]
    e1v = torch.tensor([math.cos(math.radians(ang)), math.sin(math.radians(ang))], device=dev)
    r0s = math.exp(opt['lr0']); X0 = torch.stack([r0s * torch.cos(th0[b]), r0s * torch.sin(th0[b])], 1)
    u0 = X0 @ e1v
    logXi = torch.log(torch.clamp(u0.abs(), min=1e-300)) + m1r * T[b]          # weak eigenvalue of the (symmetrised) ring matrix, not 1/p - c (referee audit)
    Xs = (torch.sign(u0) * torch.exp(logXi - logXi.max())).cpu().numpy()
    thn = thA.cpu().numpy()
    sc = np.nonzero(Xs * np.roll(Xs, -1) < 0)[0]
    bz = []
    for i in sc:
        j = (i + 1) % len(thn); t0_ = thn[i]; t1_ = thn[j] if j > i else thn[j] + 2 * math.pi
        bz.append(np.degrees(np.mod(t0_ + (t1_ - t0_) * Xs[i] / (Xs[i] - Xs[j]), 2 * math.pi)))
    zpd, zmd = math.degrees(float(zp[b])) % 360, math.degrees(float(zm[b])) % 360
    bp = min(bz, key=lambda v: abs((v - zpd + 180) % 360 - 180)) if bz else float('nan')
    bm = min(bz, key=lambda v: abs((v - zmd + 180) % 360 - 180)) if bz else float('nan')
    Sz = S_of(thA, sig[b], Dz[b]).cpu().numpy()
    Sb = 0.5 * (np.cos(np.radians(bm - bp) / 2) - np.cos(thn - np.radians((bp + bm) / 2))) if bz else Sz
    lgA = np.log(np.maximum(Afine[b].cpu().numpy(), 1e-300))
    Fr = lgA - 2 * logXi.cpu().numpy() - 2 * np.log(np.abs(Sz) + 1e-300) + 2 * np.log(np.abs(Sb) + 1e-300)
    wmask = (np.abs(Sz) > opt['cut']) & (np.abs(Sb) > opt['cut']) & np.isfinite(Fr)
    logGt = lgA - 2 * logXi.cpu().numpy()
    i11 = int(np.argmin(np.abs(S.lr.cpu().numpy() + 11))); i13 = int(np.argmin(np.abs(S.lr.cpu().numpy() + 13)))
    rb = rho[b].cpu().numpy(); core_slope = float(np.median(np.log(np.maximum(rb[i11], 1e-300)) - np.log(np.maximum(rb[i13], 1e-300))) / 2)
    rec = dict(row=rows[b], core_logslope=core_slope, m1_mom=float(m1_mom[b]), c=float(c[b]), d_psixx=float(d[b]), m1_ring=m1r, m2_ring=m2r, e1_deg=ang, antisym=asym,
               zp=zpd, zm=zmd, bz=[round(v, 3) for v in bz], bp=bp, bm=bm, Fr_std=float(Fr[wmask].std()), Fr_range=float(Fr[wmask].max() - Fr[wmask].min()),
               Gt_range=float(logGt[wmask].max() - logGt[wmask].min()), bulk_std=float(logGt[np.abs(Sz) > 0.3].std()), dgds=float(dg[b]), arrived=float(arrived[b].double().mean()),
               minVr_r=float(((1.0 / p) + Wr[b] / S.r[:, None]).min()), nzeros=len(bz))
    emit(rec)
    print("%-26s | %-8.5f %-8.5f %-7.4f %-8.3f %-8.5f | %-9.3f %-9.3f %-9.3f %-9.3f | %-7.4f %-7.3f %-7.3f | %-7.1e" % (str(rows[b]), rec['m1_mom'], m1r, m2r, ang, rec['d_psixx'], zpd, bp, zmd, bm, rec['Fr_std'], rec['Gt_range'], rec['bulk_std'], rec['dgds']))
np.savez('runs/pfwd/xodd/%s_states.npz' % tag, g=g.cpu().numpy(), lr=S.lr.cpu().numpy(), th=S.th.cpu().numpy(), rows=np.array(rows), p=p, a6=np.array(a6))
print("XODD_DONE", flush=True)
