"""Release c_l from a forced state (free Newton, unforced), rescale the result to the canonical representative
L_can = 1 (SPEC 5.4) on a grid with L = 1, and refine over a list of resolutions; full diagnostics at each level."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
start = sys.argv[1]; tag = sys.argv[2]; pairs = [tuple(int(v) for v in s.split('x')) for s in sys.argv[3].split(',')]
Lgrid = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0      # grid scale relative to L_can
log = open(f'runs/{tag}.log', 'a'); log.write(f"# release+refine from {start} pairs {pairs} Lgrid={Lgrid} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
def cheb_coeffs(mdl, f):
    t = mdl.rad.tR_np; V = np.cos(np.outer(np.arccos(t), np.arange(mdl.N + 1))); return np.linalg.lstsq(V, f, rcond=None)[0]
def K_Lcan(mdl, b, cl):
    bhat = mdl.ang.to_coef(b, 'EE'); M = mdl.M
    bK = ((mdl.rad.ext1_R @ bhat)[0]*torch.cos(math.pi*torch.arange(M, device=dev, dtype=torch.float64))).sum().item()
    K = mdl.L**(1-1/cl)*bK; a0 = b[0,0].item(); return K, (K/a0)**(cl/(cl-1)) if K/a0 > 0 else float('nan')
def diag(mdl, b, cl, flds, label):
    c = mdl.psi_xy0(flds).item(); a0 = b[0,0].item(); K, Lcan = K_Lcan(mdl, b, cl); N, M = mdl.N, mdl.M
    tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1]+tR[1:]); th = mdl.ang.theta_np; thm = np.concatenate([[0.5*th[0]], 0.5*(th[:-1]+th[1:]), [0.5*(th[-1]+np.pi/2)]])
    rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(b, cl, flds, RR, TT); qf = np.abs(ev['R'])/ev['Nf']; qv = np.abs(ev['R'])/ev['Nv']
    regs = [(0,0.1),(0.1,1),(1,10),(10,100),(100,1e4),(1e4,1e30)]
    og = [(qf[(RR>=lo)&(RR<hi)].max(), qv[(RR>=lo)&(RR<hi)].max(), np.abs(ev['R'])[(RR>=lo)&(RR<hi)].max()) if ((RR>=lo)&(RR<hi)).any() else (float('nan'),)*3 for lo,hi in regs]
    bhat = mdl.ang.to_coef(b, 'EE'); ck0 = cheb_coeffs(mdl, bhat[:,0].cpu().numpy()); ck1 = cheb_coeffs(mdl, bhat[:,1].cpu().numpy())
    n = np.arange(N+1); tail = slice(N//2, N-2); s0 = ((-1.0)**n*ck0)[tail]
    rr = np.logspace(-4, -1, 7); tt = mdl.rad.t_of_r(rr)
    P = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, tt, mdl.rad.wR_np), device=dev); bk = (P @ bhat).cpu().numpy()
    d0 = bk[:,0]-a0; ls0 = np.diff(np.log(np.abs(d0)))/np.diff(np.log(rr)); ls1 = np.diff(np.log(np.abs(bk[:,1])))/np.diff(np.log(rr))
    far = bhat[-1].abs().cpu().numpy()
    msg = (f"{label} N={N} M={M} L={mdl.L}: cl={cl:.12f} c={c:+.12f} cl+c-1={cl+c-1:+.1e} a0={a0:.10f} K={K:.8f} Lcan={Lcan:.8f}\n"
           f"    between-node max|R|/Nf, max|R|/Nv, max|R| by region r in [0,.1),[.1,1),[1,10),[10,100),[100,1e4),[1e4,inf): "
           + " ".join(f"({a:.1e},{bb:.1e},{cc:.1e})" for a,bb,cc in og) + "\n"
           f"    cheb coeffs beta0: |c_N/4|={abs(ck0[N//4]):.1e} |c_N/2|={abs(ck0[N//2]):.1e} |c_3N/4|={abs(ck0[3*N//4]):.1e} |c_N-3|={abs(ck0[N-3]):.1e} tail sign frac(+)={(s0>0).mean():.2f};  beta1: |c_N/2|={abs(ck1[N//2]):.1e} |c_N-3|={abs(ck1[N-3]):.1e}\n"
           f"    far-field angular coefs (row N, k=0..7): {np.array2string(far[:8], precision=4, max_line_width=200)};  near-0 slopes b0-a0 {np.array2string(ls0, precision=2)} b1 {np.array2string(ls1, precision=2)}")
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
    return dict(cl=cl, c=c, a0=a0, K=K, Lcan=Lcan, og=og)
def rescale_regrid(mdl_old, b_old, lam, mdl_new):
    """b_new(r) for rho_lam(X) = lam rho(X/lam): b_new(r,th) = w_old(r/lam)/w_new(r) b_old(r/lam, th)."""
    r_new = mdl_new.rad.rR.cpu().numpy(); t_old = mdl_old.rad.t_of_r(r_new/lam)
    P = torch.tensor(ipm3.interp_matrix(mdl_old.rad.tR_np, t_old, mdl_old.rad.wR_np), device=dev)
    bi = P @ b_old
    if mdl_new.M != mdl_old.M:
        C = mdl_old.ang.to_coef(bi, 'EE'); C2 = torch.zeros(C.shape[0], mdl_new.M, device=dev); m = min(mdl_new.M, mdl_old.M); C2[:, :m] = C[:, :m]
        bi = mdl_new.ang.to_val(C2, 'EE')
    w_old = mdl_old.rad.w_of_t(torch.tensor(t_old, device=dev), mdl_old.gamma)
    return (w_old/mdl_new.wR)[:, None]*bi
st = torch.load(start)
N0, M0 = st['N'], st['M']
mdl = ipm3.IPM3(N=N0, M=M0, L=st['L'], gamma=st['gamma'], p=st['p'], device=dev, couple_gamma=True); mdl.gauge = 'inf'
b = st['b'].to(dev); cl = st['cl']; beta = (mdl.rad.ext1_R @ b).mean().item()
b, cl, info = ipm3.newton(mdl, b, cl, gauge_value=beta, maxit=80, tol=1e-12, verbose=False, log=log)
m = f"RELEASE from {start}: |F|={info['nF']:.1e} it={len(info['hist'])}"; print(m); log.write(m+"\n")
d = diag(mdl, b, cl, info['flds'], "RELEASED")
torch.save(dict(b=b.cpu(), cl=cl, gamma=mdl.gamma, N=N0, M=M0, L=st['L'], p=mdl.p), f'runs/{tag}_released.pt')
# canonical rescaling: lam = Lgrid/Lcan so that L_can(new) = Lgrid (grid L = 1)
lam = Lgrid/d['Lcan']
mdl_old, b_old = mdl, b
for (N, M) in pairs:
    mdl_new = ipm3.IPM3(N=N, M=M, L=1.0, gamma=1/cl, device=dev, couple_gamma=True); mdl_new.gauge = 'inf'
    bg = rescale_regrid(mdl_old, b_old, lam, mdl_new)
    beta_new = (mdl_new.rad.ext1_R @ bg).mean().item()
    t0 = time.time()
    b2, cl2, info2 = ipm3.newton(mdl_new, bg, cl, gauge_value=beta_new, maxit=80, tol=1e-12, verbose=False, log=log)
    m = f"REFINE N={N} M={M}: start |F|={info2['hist'][0][0]:.1e} -> |F|={info2['nF']:.1e} it={len(info2['hist'])} beta={beta_new:.6f} time {time.time()-t0:.1f}s"; print(m, flush=True); log.write(m+"\n")
    d2 = diag(mdl_new, b2, cl2, info2['flds'], "CANDIDATE")
    torch.save(dict(b=b2.cpu(), cl=cl2, gamma=mdl_new.gamma, N=N, M=M, L=1.0, p=mdl_new.p), f'runs/{tag}_N{N}M{M}.pt')
    if info2['nF'] < 1e-8:
        mdl_old, b_old, cl, lam = mdl_new, b2, cl2, 1.0
        # keep the canonical scale exactly: re-normalise lam so that L_can = Lgrid at the next level
        lam = Lgrid/d2['Lcan']
