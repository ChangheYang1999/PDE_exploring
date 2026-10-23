"""q_survey.py -- free-c_l survey in the smooth Q basis from a GRID of starts (lead 17:11Z item 3(b)), with the radial map rebuilt from c_l
at every Gauss-Newton step (src/q_free.py machinery).  Start: rho = a0 y w(r) with b = a0 constant on the Q grid (so a0(start) = a0 and the
far-field gauge gK = a0; w = (1-t)/2 ~ (1/2)(L/r)^(1-1/c_l) at infinity), c_l(start) = c_l.  Unknowns: u and c_l; rows: all-node collocation,
deflated centre row (c_l - 1 + c) gK = 0, gauge row b(1, pi/2) = gK.  Reports per start: end |F|max, |F|_2, c_l, a0, steps, Chebyshev tails,
between-node |R|/N_f by region.  usage: python3 src/q_survey.py N M maxit tag cl1,cl2,... a01,a02,...  (a0 = '4A' allowed)"""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3, ipm3s, ipm3q, ipm3ql, q_free
torch.set_default_dtype(torch.float64); dev = 'cuda'
now = lambda: time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
N, M, maxit, tag = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
cls = [float(v) for v in sys.argv[5].split(',')]; a0s = sys.argv[6].split(',')
q_free.OPT['clmin'] = 1.005
log = open(f'runs/{tag}.log', 'a'); log.write(f"# q_survey {N}x{M} maxit={maxit} cls={cls} a0s={a0s} {now()}\n")
for cl in cls:
    for a0s_ in a0s:
        a0 = 4 * (2 * cl - 1) if a0s_ == '4A' else float(a0s_)
        q0 = q_free.model(N, M, cl, 1.0)
        beta0 = torch.zeros(N + 1, M, device=dev); beta0[:, 0] = a0; u = q0.beta_to_u(beta0); gK = a0
        log.write(f"## start cl={cl} a0={a0} {now()}\n"); t0 = time.time()
        try:
            u2, cl2, info = q_free.gn_free(N, M, u, cl, gK, 1.0, maxit=maxit, log=log)
            q = info['model']; beta = q.beta_full(u2); flds = info['flds']; c = q.psi_xy0(flds).item(); a0e = beta[0, 0].item()
            og = ipm3ql.between_node(q, beta, cl2, flds, 0.0); tail = ipm3ql.cheb_tail(q, u2)
            h = info['hist']; dec = (h[-1][1] / h[max(0, len(h) - 11)][1]) if len(h) > 1 else float('nan')
            m = (f"SURVEY {N}x{M} start (cl={cl}, a0={a0:+.4g}): end cl={cl2:.8f} a0={a0e:+.6f} a0/D={a0e/(cl2-1):.3f} c={c:+.8f} cl+c-1={cl2+c-1:+.2e} "
                 f"|F|max={info['nF']:.2e} |F|2={info['nF2']:.2e} its={info['its']} last10-ratio={dec:.3f} tails={tail[0]:.1e},{tail[1]:.1e} "
                 f"between-node |R|/Nf=[{og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}] ({time.time()-t0:.0f}s)")
            torch.save(dict(beta=beta.cpu(), u=u2.cpu(), cl=cl2, mu=None, gamma=1 / cl2, N=N, M=M, L=1.0, Lf=1.0, gK=gK, p=q.p, rep='QL-free-map',
                            hist=info['hist'], start=(cl, a0)), f'runs/{tag}_cl{cl:g}_a0{a0:+g}.pt')
        except Exception as e:
            m = f"SURVEY {N}x{M} start (cl={cl}, a0={a0:+.4g}): FAILED {type(e).__name__}: {e}"
        print(m, flush=True); log.write(m + "\n"); log.flush()
