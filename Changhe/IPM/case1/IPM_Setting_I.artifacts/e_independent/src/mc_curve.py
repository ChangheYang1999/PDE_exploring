"""Fixed-c_l residual curve m(s) = min |F(b)| subject to c_l(b) = s (the referee's recommended nonlinear diagnostic; the lead plans the same
on their basis). Start: construct1 projection + n0 unweighted LSQ iterations at (N, M), R (optional cluster). For each target s: LSQ with the
extra row w_c (c_l(b) - s) (w_c large), its iterations from the common start; report PDE rms (unweighted normalisation), max, near-P shells,
h(P)-1, x*, |c_l - s|. Usage: python3 src/mc_curve.py N M R L "s1,s2,..." [its] [ovs] [p] [cluster:r,w,a] [wc:1e4] [n0:6] [tag]"""
import sys, math, numpy as np, torch
sys.path.insert(0, 'src')
import ipm1disk, ipm1lsq, charac
from scipy.interpolate import RegularGridInterpolator
dev = 'cuda'; base = ''
N, M, R, L = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
targets = [float(v) for v in sys.argv[5].split(',')]
its = int(sys.argv[6]) if len(sys.argv) > 6 else 20; ovs = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0; pmap = float(sys.argv[8]) if len(sys.argv) > 8 else 1.0
cluster = None; wc = 1e4; n0 = 6; tag = f'mc_N{N}M{M}R{int(R)}'
for arg in sys.argv[9:]:
    if arg.startswith('cluster:'):
        rc_, w_, al_ = [float(v) for v in arg[8:].split(',')]; cluster = ipm1disk.RadialDisk.s_for_r(L, R, rc_, w_, al_, p=pmap)
    if arg.startswith('wc:'): wc = float(arg[3:])
    if arg.startswith('n0:'): n0 = int(arg[3:])
    if arg.startswith('tag:'): tag = arg[4:]
cand = np.load('final_candidate.npz', allow_pickle=True)
cl = float(cand['c_l']); rc = cand['r']; thc = cand['theta']; H = cand['H']
m = ipm1disk.IPM1Disk(N=N, M=M, L=L, R=R, gamma=1 / cl, device=dev, p=pmap, cluster=cluster); m.k_tail = 1 / cl
interp = RegularGridInterpolator((np.log(rc), thc), H, method='cubic', bounds_error=False, fill_value=None)
rR = m.rad.rR.cpu().numpy(); thR = m.ang.theta_np
pts = np.array([[math.log(max(r, rc[0])), t] for r in rR[1:] for t in thR]); Hg = interp(pts).reshape(N, M)
b = torch.ones(N + 1, M, device=dev); b[1:] = torch.tensor(np.exp(Hg), device=dev) / m.wR[1:, None]
ls = ipm1lsq.LSQ(m, Qr=int(round(ovs * N)), Qth=2 * M + 1, chunk=256, verbose=False)
cl0, c0, fl0 = ls.cl_of_b(b, cl); ls.set_weights(b, cl0)
b0, cl0, info = ls.solve(b, cl0, maxit=n0, lam=1e-6, svd_at_end=False, rel_stop=1e-9)
print(f"[mc] (N,M)=({N},{M}) R={R} cluster={cluster} wc={wc}: common start after {n0} its: c_l {cl0:.8f}", flush=True)
rq = ls.rq.cpu().numpy(); Xq = ls.rq[:, None] * ls.cq[None, :]; Yq = ls.rq[:, None] * ls.sq[None, :]
def report(bb, cll, label):
    E, q = ls.residual_q(bb, cll); den = ls.denominators(bb, cll, q); rel = (E / den)
    Pi = charac.FieldEval(m, bb, cll).find_P(); dP = torch.sqrt((Xq - Pi['x_star']) ** 2 + Yq ** 2)
    shells = "; ".join(f"[{lo},{hi}) {math.sqrt((rel[(dP>=lo)&(dP<hi)]**2).mean().item()):.1e}/{rel[(dP>=lo)&(dP<hi)].abs().max().item():.1e}" for lo, hi in [(0,0.5),(0.5,1),(1,2),(2,4),(4,8)])
    bands = "; ".join(f"{nm} {math.sqrt((rel[(rq>a_)&(rq<=b_)]**2).mean().item()):.1e}/{rel[(rq>a_)&(rq<=b_)].abs().max().item():.1e}" for nm, (a_, b_) in {'r<=2': (0, 2), '2-10': (2, 10), '10-100': (10, 100), '>100': (100, np.inf)}.items())
    print(f"[mc] {label}: c_l {cll:.8f}, x* {Pi['x_star']:.5f}, h(P)-1 {Pi['h']-1:+.2e}; rms(all) {math.sqrt((rel**2).mean().item()):.3e} max {rel.abs().max().item():.2e}; near-P shells {shells}; bands {bands}", flush=True)
report(b0, cl0, "start")
for s_t in targets:
    ls.extra_rows = [('cfix', wc)]; ls.cfix_target = s_t
    bs, cls, inf = ls.solve(b0, cl0, maxit=its, lam=1e-6, svd_at_end=False, rel_stop=1e-8)
    ls.extra_rows = []
    report(bs, cls, f"s = {s_t:.4f} ({len(inf['hist'])-1} its, |c_l - s| {abs(cls - s_t):.1e})")
    np.savez(base + f'runs/{tag}_s{s_t:.4f}.npz', b=bs.cpu().numpy(), cl=cls, gamma=m.gamma, N=N, M=M, L=L, R=R, disk=True, eps=1.0, lsq=True, Qr=ls.Qr, Qth=ls.Qth, cluster=np.array(cluster if cluster is not None else [], dtype=float), pmap=pmap, cfix=s_t)
