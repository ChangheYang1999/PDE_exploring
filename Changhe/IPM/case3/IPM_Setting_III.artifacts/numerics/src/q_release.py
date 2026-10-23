"""Q representation: forced solve at (c_l, gK), then release c_l (unforced Newton) from that smooth near-solution."""
import sys, math, time, numpy as np, torch
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import ipm3, ipm3q
torch.set_default_dtype(torch.float64); dev = 'cuda'
N = int(sys.argv[1]); M = int(sys.argv[2]); cl = float(sys.argv[3]); gK = float(sys.argv[4]); tag = sys.argv[5]
log = open(f'runs/{tag}.log', 'a'); log.write(f"# q_release N={N} M={M} cl={cl} gK={gK} {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n")
q = ipm3q.IPM3Q(N=N, M=M, L=1.0, gamma=1/cl, device=dev)
beta0 = torch.zeros(N+1, M, device=dev); beta0[:, 0] = gK; u0 = q.beta_to_u(beta0)
u, _, mu, info = q.newton(u0, cl, gK, mu=0.0, forced=True, maxit=60, log=log)
beta = q.beta_full(u); c = q.psi_xy0(info['flds']).item()
m1 = f"Q forced N={N} M={M} cl={cl} gK={gK}: |F|={info['nF']:.1e} mu={mu:+.8f} a0={beta[0,0].item():.8f} Delta={cl+c-1:+.6f}"
print(m1, flush=True); log.write(m1+"\n")
u2, cl2, _, info2 = q.newton(u, cl, gK, forced=False, maxit=80, log=log)
beta2 = q.beta_full(u2); c2 = q.psi_xy0(info2['flds']).item(); og = ipm3q.between_node(q, beta2, cl2, info2['flds'], 0.0)
sv = torch.linalg.svdvals(info2['J'])
m2 = f"Q release N={N} M={M} from ({cl},{gK}): |F|={info2['nF']:.1e} its={info2['its']} smin={sv[-1].item():.1e} -> cl={cl2:.8f} a0={beta2[0,0].item():.8f} c={c2:+.8f} cl+c-1={cl2+c2-1:+.1e} between-node |R|/Nf=[{og[0]:.1e} {og[1]:.1e} {og[2]:.1e} {og[3]:.1e}]"
print(m2, flush=True); log.write(m2+"\n")
torch.save(dict(beta=beta2.cpu(), cl=cl2, N=N, M=M, L=1.0, p=q.p, rep='Q'), f'runs/{tag}.pt')
