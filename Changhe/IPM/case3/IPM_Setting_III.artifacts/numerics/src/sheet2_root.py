"""Root-find mu(c_l) = 0 on a forced sheet (secant in c_l) at a sequence of resolutions, starting from a saved forced
state. At each resolution: regrid the start, forced-solve at c_l_a and c_l_b, secant until |mu| < tol, then diagnostics
of the (unforced) residual between nodes, Chebyshev tails, far-field angular coefficients, near-origin slopes, K, L_can."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3
torch.set_default_dtype(torch.float64)
dev = 'cuda'
start = sys.argv[1]; tag = sys.argv[2]; pairs = [tuple(int(v) for v in s.split('x')) for s in sys.argv[3].split(',')]
beta = float(sys.argv[4]); L = float(sys.argv[5]) if len(sys.argv) > 5 else 1.0
log = open(f'runs/{tag}.log', 'a'); log.write(f"# sheet2 root from {start} pairs {pairs} beta={beta} L={L} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
def cheb_coeffs(mdl, f):
    t = mdl.rad.tR_np; V = np.cos(np.outer(np.arccos(t), np.arange(mdl.N + 1))); return np.linalg.lstsq(V, f, rcond=None)[0]
def diag(mdl, b, cl, flds, mu, label):
    c = mdl.psi_xy0(flds).item(); a0 = b[0,0].item(); N, M = mdl.N, mdl.M; gamma = 1/cl
    bhat = mdl.ang.to_coef(b, 'EE')
    bK = ((mdl.rad.ext1_R @ bhat)[0]*torch.cos(math.pi*torch.arange(M, device=dev, dtype=torch.float64))).sum().item()
    K = mdl.L**(1-gamma)*bK; Lcan = (K/a0)**(cl/(cl-1)) if K/a0 > 0 else float('nan')
    tR = mdl.rad.tR_np; tm = 0.5*(tR[:-1]+tR[1:]); th = mdl.ang.theta_np; thm = np.concatenate([[0.5*th[0]], 0.5*(th[:-1]+th[1:]), [0.5*(th[-1]+np.pi/2)]])
    rm = mdl.rad.rmap(torch.tensor(tm)).numpy(); RR, TT = np.meshgrid(rm, thm, indexing='ij')
    ev = mdl.evaluate(b, cl, flds, RR, TT); qf = np.abs(ev['R'])/ev['Nf']; qv = np.abs(ev['R'])/ev['Nv']
    regs = [(0,0.1),(0.1,1),(1,10),(10,100),(100,1e4),(1e4,1e30)]
    og = [(qf[m].max(), qv[m].max(), np.abs(ev['R'])[m].max()) if (m := (RR>=lo)&(RR<hi)).any() else (float('nan'),)*3 for lo,hi in regs]
    ck0 = cheb_coeffs(mdl, bhat[:,0].cpu().numpy()); ck1 = cheb_coeffs(mdl, bhat[:,1].cpu().numpy())
    rr = np.logspace(-4, -1, 7)*mdl.L; tt = mdl.rad.t_of_r(rr)
    P = torch.tensor(ipm3.interp_matrix(mdl.rad.tR_np, tt, mdl.rad.wR_np), device=dev); bk = (P @ bhat).cpu().numpy()
    d0 = bk[:,0]-a0; ls0 = np.diff(np.log(np.abs(d0)))/np.diff(np.log(rr)); ls1 = np.diff(np.log(np.abs(bk[:,1])))/np.diff(np.log(rr))
    far = bhat[-1].abs().cpu().numpy(); mid = bhat[N//2].abs().cpu().numpy()
    msg = (f"{label} N={N} M={M} L={mdl.L} beta={beta}: cl={cl:.12f} mu={mu:+.3e} c={c:+.12f} a0={a0:.10f} K={K:.8f} Lcan={Lcan:.8f}\n"
           f"    between-node (unforced) max|R|/Nf, max|R|/Nv, max|R| for r in [0,.1),[.1,1),[1,10),[10,100),[100,1e4),[1e4,inf): "
           + " ".join(f"({a:.1e},{bb:.1e},{cc:.1e})" for a,bb,cc in og) + "\n"
           f"    radial cheb coeffs beta0: |c_N/4|={abs(ck0[N//4]):.1e} |c_N/2|={abs(ck0[N//2]):.1e} |c_3N/4|={abs(ck0[3*N//4]):.1e} |c_N-3|={abs(ck0[N-3]):.1e};  beta1: |c_N/2|={abs(ck1[N//2]):.1e} |c_N-3|={abs(ck1[N-3]):.1e}\n"
           f"    angular coefs |b_k| at r=inf (k=0,1,2,4,8,16,M-1): {np.array2string(far[[0,1,2,4,8,min(16,M-1),M-1]], precision=3, max_line_width=200)}; at mid radius r={mdl.rad.rR[N//2].item():.3g}: {np.array2string(mid[[0,1,2,4,8,min(16,M-1),M-1]], precision=3, max_line_width=200)}\n"
           f"    near-0 slopes b0-a0 {np.array2string(ls0, precision=2)} b1 {np.array2string(ls1, precision=2)}")
    print(msg, flush=True); log.write(msg+"\n"); log.flush()
    return dict(cl=cl, c=c, a0=a0, K=K, Lcan=Lcan)
def fsolve(mdl, bg, cl, mu0):
    b, _, info = ipm3.newton(mdl, bg, cl, gauge_value=beta, maxit=80, tol=1e-12, verbose=False, log=log, mu=mu0, forced=True)
    return b, info
st = torch.load(start)
mdl_prev = ipm3.IPM3(N=st['N'], M=st['M'], L=st['L'], gamma=st['gamma'], p=st['p'], device=dev); mdl_prev.gauge = 'inf'
b_prev = st['b'].to(dev); cl_prev = st['cl']; mu_prev = st.get('mu', 0.0)
for (N, M) in pairs:
    t0 = time.time()
    def solve_at(cl, mdl_from, b_from, mu_from):
        mdl = ipm3.IPM3(N=N, M=M, L=L, gamma=1/cl, device=dev); mdl.gauge = 'inf'
        bg = ipm3.regrid(mdl_from, b_from, mdl); bg = bg*(beta/(mdl.rad.ext1_R @ bg).mean().item())
        b, info = fsolve(mdl, bg, cl, mu_from)
        return mdl, b, info
    # two points for the secant
    cl_a = cl_prev; mdl_a, b_a, info_a = solve_at(cl_a, mdl_prev, b_prev, mu_prev); mu_a = info_a['mu']
    m = f"  [{N}x{M}] cl={cl_a:.10f} mu={mu_a:+.6e} |F|={info_a['nF']:.1e} it={len(info_a['hist'])}"; print(m, flush=True); log.write(m+"\n")
    cl_b = cl_a + (0.02 if mu_a < 0 else -0.02); mdl_b, b_b, info_b = solve_at(cl_b, mdl_a, b_a, mu_a); mu_b = info_b['mu']
    m = f"  [{N}x{M}] cl={cl_b:.10f} mu={mu_b:+.6e} |F|={info_b['nF']:.1e} it={len(info_b['hist'])}"; print(m, flush=True); log.write(m+"\n")
    for it in range(12):
        if abs(mu_b) < 1e-10 or abs(mu_b - mu_a) < 1e-14: break
        cl_c = cl_b - mu_b*(cl_b - cl_a)/(mu_b - mu_a)
        mdl_c, b_c, info_c = solve_at(cl_c, mdl_b, b_b, mu_b); mu_c = info_c['mu']
        m = f"  [{N}x{M}] secant {it}: cl={cl_c:.12f} mu={mu_c:+.6e} |F|={info_c['nF']:.1e} it={len(info_c['hist'])} a0={b_c[0,0].item():.8f}"; print(m, flush=True); log.write(m+"\n")
        if info_c['nF'] > 1e-8:
            print("   not converged; stop secant", flush=True); break
        cl_a, mu_a, cl_b, mu_b, mdl_b, b_b, info_b = cl_b, mu_b, cl_c, mu_c, mdl_c, b_c, info_c
    d = diag(mdl_b, b_b, cl_b, info_b['flds'], mu_b, f"ROOT")
    torch.save(dict(b=b_b.cpu(), cl=cl_b, gamma=1/cl_b, N=N, M=M, L=L, p=mdl_b.p, mu=mu_b, beta=beta), f'runs/{tag}_N{N}M{M}.pt')
    log.write(f"  time {time.time()-t0:.1f}s\n"); log.flush()
    mdl_prev, b_prev, cl_prev, mu_prev = mdl_b, b_b, cl_b, mu_b
