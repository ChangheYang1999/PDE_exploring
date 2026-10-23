"""For each c_l: forced beta-scan up to beta_max, release c_l (free Newton), then diagnostics of the valley state:
Chebyshev tail of beta_0 (sign fraction, slope), near-origin slopes, off-grid residual, K, Lcan, a0."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
N = int(sys.argv[1]); M = int(sys.argv[2]); L = 1.0; tag = sys.argv[3]
cls = [float(v) for v in sys.argv[4].split(',')]; betas = [float(v) for v in sys.argv[5].split(',')]
log = open(f'runs/{tag}.log', 'a'); log.write(f"# valley chain N={N} M={M} cls={cls} betas={betas} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
def cheb_coeffs(mdl, f):
    t = mdl.rad.tR_np; V = np.cos(np.outer(np.arccos(t), np.arange(mdl.N + 1))); return np.linalg.lstsq(V, f, rcond=None)[0]
def diagnostics(mdl, b, cl, flds, label):
    c = mdl.psi_xy0(flds).item(); a0 = b[0,0].item(); gamma = 1/cl
    bhat = mdl.ang.to_coef(b, 'EE')
    bK = ((mdl.rad.ext1_R @ bhat)[0]*torch.cos(math.pi*torch.arange(M, device=dev, dtype=torch.float64))).sum().item()
    K = L**(1-gamma)*bK; Lcan = (K/a0)**(cl/(cl-1)) if K/a0 > 0 else float('nan')
    tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1]+tR[1:]); th = mdl.ang.theta_np; thm = 0.5*(th[:-1]+th[1:])
    rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(b, cl, flds, RR, TT); q = np.abs(ev['R'])/ev['Nf']
    og = [q[(RR>=lo)&(RR<hi)].max() for lo,hi in [(0,1),(1,100),(100,1e4),(1e4,1e30)]]
    ck0 = cheb_coeffs(mdl, bhat[:,0].cpu().numpy()); n = np.arange(N+1); tail = slice(N//2, N-2)
    s0 = ((-1.0)**n*ck0)[tail]; x = np.log(n[tail]); y = np.log(np.abs(s0)+1e-300)
    sl = np.linalg.lstsq(np.vstack([x, np.ones_like(x)]).T, y, rcond=None)[0][0]
    rr = np.logspace(-4, -1, 7); tt = mdl.rad.t_of_r(rr)
    P = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, tt, mdl.rad.wR_np), device=dev); bk = (P @ bhat).cpu().numpy()
    d0 = bk[:,0]-a0; ls0 = np.diff(np.log(np.abs(d0)))/np.diff(np.log(rr)); ls1 = np.diff(np.log(np.abs(bk[:,1])))/np.diff(np.log(rr))
    msg = (f"{label} cl={cl:.8f} a0={a0:.8f} c={c:+.8f} cl+c-1={cl+c-1:+.1e} K={K:.5f} Lcan={Lcan:.4g} offgrid|R|/Nf={og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e} "
           f"tail beta0: frac(+)={(s0>0).mean():.2f} slope={sl:+.2f} (-> d-1 ~ {(-sl-1)/2:.2f}) |c_N/2|={abs(ck0[N//2]):.1e} |c_N-3|={abs(ck0[N-3]):.1e} mean(s0)={s0.mean():+.2e}  "
           f"near-0 slopes b0-a0 {np.array2string(ls0, precision=2)} b1 {np.array2string(ls1, precision=2)}")
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
for cl in cls:
    mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdl.gauge = 'inf'
    b = betas[0]*torch.ones(N+1, M, device=dev); mu = 0.0; ok = False
    for beta in betas:
        bt = b*(beta/(mdl.rad.ext1_R @ b).mean().item())
        bn, _, info = ipm3.newton(mdl, bt, cl, gauge_value=beta, maxit=80, tol=1e-12, verbose=False, log=log, mu=mu, forced=True)
        m = f"  forced cl={cl} beta={beta}: mu={info['mu']:+.6f} a0={bn[0,0].item():.6f} c={mdl.psi_xy0(info['flds']).item():+.6f} |F|={info['nF']:.1e} it={len(info['hist'])}"
        print(m, flush=True); log.write(m+"\n")
        if info['nF'] < 1e-8: b, mu, ok = bn, info['mu'], True
        else: break
    # release c_l
    mdl2 = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev, couple_gamma=True); mdl2.gauge = 'inf'
    beta_rel = (mdl2.rad.ext1_R @ b).mean().item()
    b2, cl2, info2 = ipm3.newton(mdl2, b, cl, gauge_value=beta_rel, maxit=80, tol=1e-12, verbose=False, log=log)
    m = f"  release cl={cl} -> cl={cl2:.10f} |F|={info2['nF']:.1e} it={len(info2['hist'])} beta={beta_rel}"
    print(m, flush=True); log.write(m+"\n")
    diagnostics(mdl2, b2, cl2, info2['flds'], f"VALLEY[{tag}]")
    torch.save(dict(b=b2.cpu(), cl=cl2, gamma=mdl2.gamma, N=N, M=M, L=L, p=mdl2.p, mu_release_from=mu, beta=beta_rel), f'runs/{tag}_cl{cl:.3f}.pt')
