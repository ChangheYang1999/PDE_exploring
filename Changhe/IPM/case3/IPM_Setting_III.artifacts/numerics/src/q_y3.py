"""q_y3.py -- SECONDARY branch (PROMPT section 1: rho_y(0) = 0 but rho(0, y) not identically 0, y^3-leading), exploratory, in the smooth Q basis with
the radial map rebuilt from c_l (q_free machinery).  Centre row: a0 = beta_0(-1) = 0 (replaces the y-leading strain identity; the cubic identity
3(c_l + c) = 1 for the y^3 coefficient, and rho_xxy(0) = 0 for c_l > 1, then follow from the near-centre collocation rows, see NUM_REPORT 4N).
Start: b = g0 sigma [1/2 - (1/2) cos 2th] (pure y^3 at cubic order), gauge gK = b(1, pi/2) = g0.  The printed r^2 "coefficients" are coefficients
in sigma; physical cubic coefficients are kappa (d0 +- d1 - a0) with kappa = 2^(2p)/L^2 (huge for c_l near 1).
usage: python3 src/q_y3.py N M maxit tag cl1,cl2,... g01,g02,..."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3, ipm3s, ipm3q, ipm3ql, q_free
torch.set_default_dtype(torch.float64); dev = 'cuda'
now = lambda: time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
N, M, maxit, tag = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
cls = [float(v) for v in sys.argv[5].split(',')]; g0s = [float(v) for v in sys.argv[6].split(',')]
q_free.OPT['clmin'] = 1.005; q_free.OPT['y3'] = True
flags = sys.argv[7:]                                                   # shift 3: 'id' = centre row 3(c_l + c) - 1 = 0 (y^3 identity) instead of a0 = 0; 'fine' = oversampled rows M2 = 3M
if 'id' in flags: q_free.OPT['y3'] = 'id'
if 'fine' in flags: q_free.OPT['fine'] = True; q_free.OPT['M2'] = 3 * M
log = open(f'runs/{tag}.log', 'a'); log.write(f"# q_y3 {N}x{M} maxit={maxit} cls={cls} g0s={g0s} {now()}\n")
for cl in cls:
    for g0 in g0s:
        q0 = q_free.model(N, M, cl, 1.0); sig = q0.rad.sigR
        beta0 = torch.zeros(N + 1, M, device=dev); beta0[:, 0] = 0.5 * g0 * sig; beta0[:, 1] = -0.5 * g0   # pure y^3: y^3 = y r^2 (1 - cos 2th)/2 (the earlier 3/4, -1/4 start was x^2 y/2 + y^3; referee (e2) item 17)
        gK = g0                                                                   # b(1, pi/2) = beta_0(1) - beta_1(1) = g0
        u = q0.beta_to_u(beta0)
        log.write(f"## start cl={cl} g0={g0} {now()}\n"); t0 = time.time()
        try:
            u2, cl2, info = q_free.gn_free(N, M, u, cl, gK, 1.0, maxit=maxit, log=log)
            q = info['model']; beta = q.beta_full(u2); flds = info['flds']; c = q.psi_xy0(flds).item(); a0e = beta[0, 0].item()
            og = ipm3ql.between_node(q, beta, cl2, flds, 0.0); tail = ipm3ql.cheb_tail(q, u2)
            # cubic data: b_0 ~ 2 beta_0'(-1) sigma, b_1 ~ beta_1(-1) sigma  ->  (b + e)/2 and (b - e)/2 coefficients of r^2 (up to the map factor)
            d0 = (q.rad.DR @ beta[:, 0])[0].item() * 2; d1 = beta[0, 1].item()
            m = (f"Y3{'ID' if q_free.OPT['y3'] == 'id' else ''}{'F' if q_free.OPT['fine'] else ''} {N}x{M} start (cl={cl}, g0={g0:+g}): end cl={cl2:.8f} a0={a0e:+.2e} c={c:+.8f} 3(cl+c)-1={3*(cl2+c)-1:+.3e} (y^3 identity) "
                 f"r^2-coeffs mode0={d0:+.5g} mode1={d1:+.5g} (rho_xxy(0)=0 needs mode0 + mode1 = 0: {d0+d1:+.2e}) |F|max={info['nF']:.2e} |F|2={info['nF2']:.2e} "
                 f"its={info['its']} tails={tail[0]:.1e},{tail[1]:.1e} between-node |R|/Nf=[{og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}] ({time.time()-t0:.0f}s)")
            torch.save(dict(beta=beta.cpu(), u=u2.cpu(), cl=cl2, mu=None, gamma=1 / cl2, N=N, M=M, L=1.0, Lf=1.0, gK=gK, p=q.p, rep='QL-y3',
                            hist=info['hist'], start=(cl, g0)), f'runs/{tag}_cl{cl:g}_g0{g0:+g}.pt')
        except Exception as e:
            m = f"Y3 {N}x{M} start (cl={cl}, g0={g0:+g}): FAILED {type(e).__name__}: {e}"
        print(m, flush=True); log.write(m + "\n"); log.flush()
