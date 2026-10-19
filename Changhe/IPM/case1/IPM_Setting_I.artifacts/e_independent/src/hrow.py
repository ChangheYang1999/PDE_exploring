"""Lead request 21:49Z: (a) derivative of h(P) along the smallest right singular vector of the Jacobian (x* re-solved);
(b) re-solve with the extra row w_h (h(P) - 1) = 0 (c_l free, least squares via reduced LM), report c_l, x*, h(P), smin and
its c_l component with and without the row.  Usage: python3 src/hrow.py <state.npz> <tag> [lm_its] [w_h]"""
import sys, time, math, numpy as np, torch
sys.path.insert(0, 'src')
import diag, solve, charac, batchmap, consistency
dev = 'cuda'; base = ''
path, tag = sys.argv[1], sys.argv[2]; lmit = int(sys.argv[3]) if len(sys.argv) > 3 else 80; w_h = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0
m, b, cl, d = diag.load(path, device=dev); m.k_tail = 1 / cl
N, M = m.N, m.M; n = (N + 1) * M; R = float(d['R'])
nw = solve.Newton(m, verbose=False, chunk=512)

XSTAR0 = [None]
def hP_batch(Bb, cls):
    """h(P) and x* for a batch of states (B, N+1, M) with per-column c_l, x* re-solved by batched bisection (local bracket)."""
    fe = batchmap.BatchFieldEval(m, Bb, cls)
    if XSTAR0[0] is None:
        xs_, mu1, hP, has = fe.find_P()
        XSTAR0[0] = xs_[0].item()
    else:
        xs_, mu1, hP, has = fe.find_P(bracket=(0.8 * XSTAR0[0], 1.25 * XSTAR0[0]), npts=40)
    return hP, xs_, mu1, has

def hP_single(bb, cc):
    h, xs_, mu1, has = hP_batch(bb[None], torch.tensor([cc], device=dev))
    return h[0].item(), xs_[0].item(), mu1[0].item()

def smallest_sv(J):
    U_, S_, Vh = torch.linalg.svd(J)
    return S_[0].item(), S_[-3:].cpu().numpy(), Vh[-1].clone(), U_[:, -1].clone()

t0 = time.time()
F, fl = nw.residual_full(b, cl); J = nw.jacobian(b, cl, fl)
smax, s3, v, u = smallest_sv(J)
h0, xs0, mu10 = hP_single(b, cl)
print(f"[hrow] state {path}: N={N} M={M} R={R} c_l={cl:.10f} x*={xs0:.8f} h(P)-1={h0-1:+.3e}; |F|_inf={F.abs().max().item():.2e}; smax={smax:.3e} smallest sv {s3}; v c_l comp {v[-1].item():+.3e} ({time.time()-t0:.0f}s)", flush=True)
# (a) derivative of h(P) along v (unit vector in the discrete norm), with x* re-solved
for eps in [1e-4, 1e-3, 1e-2]:
    bp = b + eps * v[:-1].reshape(N + 1, M); clp = cl + eps * v[-1].item()
    bm = b - eps * v[:-1].reshape(N + 1, M); clm = cl - eps * v[-1].item()
    hp, xp, _ = hP_single(bp, clp); hm, xm, _ = hP_single(bm, clm)
    print(f"[hrow] (a) eps={eps:.0e}: d h(P)/d s along v = {(hp-hm)/(2*eps):+.4e}, d x*/d s = {(xp-xm)/(2*eps):+.4e}, d c_l/d s = {v[-1].item():+.4e}  -> d h(P)/d c_l along the mode = {(hp-hm)/(2*eps)/v[-1].item():+.4e}", flush=True)
# residual change along v for reference
Fp, _ = nw.residual_full(b + 1e-3 * v[:-1].reshape(N + 1, M), cl + 1e-3 * v[-1].item())
print(f"[hrow] (a) |F(b + 1e-3 v) - F(b)|_2 = {(Fp - F).norm().item():.3e} (= sigma_min * 1e-3 expected {s3[-1]*1e-3:.3e})", flush=True)
# (b) augmented reduced LM: residual = [F[keep]; w_h (h(P) - 1)], Jacobian rows: J[keep][:, keep] and w_h grad h by batched FD
keep = torch.arange(M, n + 1, device=dev); nf = len(keep)
def aug_res(bb, cc):
    Fv, flv = nw.residual_full(bb, cc); hh, xs_, _ = hP_single(bb, cc)
    return torch.cat([Fv[keep], torch.tensor([w_h * (hh - 1.0)], device=dev)]), flv, hh, xs_
def grad_h(bb, cc, chunk=48):
    """row vector d h(P)/d(b_free, c_l) by batched central FD (x* re-solved)."""
    g = torch.zeros(nf, device=dev); bf = bb.reshape(-1)
    base_h, _, _ = hP_single(bb, cc)
    for s in range(0, nf - 1, chunk):
        e = min(nf - 1, s + chunk); idxs = keep[s:e]
        Bb = bf[None, :].repeat(e - s, 1); epsv = 1e-6 * torch.maximum(torch.ones(e - s, device=dev), bf[idxs].abs())
        Bb[torch.arange(e - s), idxs] += epsv
        hB, _, _, _ = hP_batch(Bb.reshape(e - s, N + 1, M), torch.full((e - s,), cc, device=dev))
        g[s:e] = (hB - base_h) / epsv
    hc, _, _ = hP_single(bb, cc + 1e-6); g[-1] = (hc - base_h) / 1e-6
    return g
bb, cc = b.clone(), cl; lam = 1e-6
r, flv, hh, xs_ = aug_res(bb, cc); nrm2 = (r ** 2).sum().item()
print(f"[hrow] (b) augmented LM start: |r|_inf={r.abs().max().item():.3e} (h-row {w_h*(hh-1):+.2e})", flush=True)
gh = None
for it in range(1, lmit + 1):
    Jr = nw.jacobian(bb, cc, flv)[keep][:, keep]
    if gh is None or (it - 1) % 5 == 0:
        tg = time.time(); gh = grad_h(bb, cc); print(f"[hrow] (b) grad h recomputed ({time.time()-tg:.0f}s), |grad_h|={gh.norm().item():.3e}, d h/d c_l = {gh[-1].item():+.3e}", flush=True)
    Ja = torch.cat([Jr, (w_h * gh)[None, :]], 0)
    JtJ = Ja.T @ Ja; g = Ja.T @ r; D = torch.diag(JtJ).clamp_min(1e-30)
    accepted = False
    for _ in range(14):
        dlt = torch.linalg.solve(JtJ + lam * torch.diag(D), -g)
        bt = bb.clone(); bt.reshape(-1)[M:] += dlt[:-1]; ct = cc + dlt[-1].item()
        rt, flt, ht, xt = aug_res(bt, ct); n2 = (rt ** 2).sum().item()
        if n2 < nrm2:
            bb, cc, r, flv, hh, xs_, nrm2 = bt, ct, rt, flt, ht, xt, n2; lam = max(lam / 3, 1e-16); accepted = True; break
        lam *= 4
    if True:
        print(f"[hrow] (b) it {it:3d} |r|_inf={r.abs().max().item():.3e} |r|_2={math.sqrt(nrm2):.3e} c_l={cc:.10f} x*={xs_:.8f} h(P)-1={hh-1:+.3e} lam={lam:.1e} accepted={accepted}", flush=True)
    if not accepted: break
F2, fl2 = nw.residual_full(bb, cc); J2 = nw.jacobian(bb, cc, fl2)
smax2, s32, v2, u2 = smallest_sv(J2)
gh2 = grad_h(bb, cc); Ja2 = torch.cat([J2[keep][:, keep], (w_h * gh2)[None, :]], 0)
sa = torch.linalg.svdvals(Ja2)
print(f"[hrow] (b) RESULT with h-row: c_l = {cc:.10f} (before {cl:.10f}), x* = {xs_:.8f} (before {xs0:.8f}), h(P)-1 = {hh-1:+.3e} (before {h0-1:+.3e}), equation residual max|E| = {m.residual(bb, cc, fl2)[1:].abs().max().item():.3e}, identity {F2[-1].item():+.2e}", flush=True)
print(f"[hrow] (b) Jacobian WITHOUT h-row at the new state: smallest sv {s32}, c_l component of v {v2[-1].item():+.3e}; augmented (with h-row) smallest singular values {sa[-3:].cpu().numpy()} (smax {sa[0].item():.3e}); consistency {abs(consistency.c_quadrature(m, bb, cc) - m.psi_xy0(fl2).item())/m.psi_xy0(fl2).item():.2e}", flush=True)
np.savez(base + f'runs/{tag}.npz', b=bb.cpu().numpy(), cl=cc, gamma=m.gamma, N=N, M=M, L=m.L, R=R, disk=True, eps=1.0, x_star=xs_, h_row=True)
print(f"[hrow] saved runs/{tag}.npz ({time.time()-t0:.0f}s)", flush=True)
