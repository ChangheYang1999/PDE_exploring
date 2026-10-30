import sys, time, json, math; sys.path.insert(0,'RUN_ROOT/numerics_N1N2/numerics/lib')
from ipm_exact import *
nmax = int(sys.argv[1]) if len(sys.argv)>1 else 8
c, terms, rec, raw = load_case4_state('RUN_ROOT/numerics_N1N2/numerics/source_copy/case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json')
E, dens, strm, moments = residual_sectors(c, terms, qmax=2)
gamma=1/c; lam=1-gamma
t=time.time()
alpha, G, Phi, C = stationary_orders(c, dens[gamma], nmax)
print('recursion time', time.time()-t, flush=True)
prev=None; out={}
for n in range(nmax+1):
    nG = quarter_norm(G[n]); nC = max(abs(qfloat(v)) for v in C[n].values())
    pc = poisson_check(G[n], Phi[n], alpha[n])
    ratio = nG/prev if prev else float('nan'); prev=nG
    top = sorted(G[n].items())[:3]
    print(f"n={n:2d} alpha={qfloat(alpha[n]):+.4f} |G_n|={nG:.6g} ratio={ratio:.3f} maxharm={max(G[n])} max|C|={nC:.4g} n(c-1)|G|={n*qfloat(c-1)*nG:.6g} first={[(k,round(qfloat(v),4)) for k,v in top]} poisson_ok={not pc}", flush=True)
    out[n]={'alpha':qstr(alpha[n]),'G':dump_q_dict(G[n]),'Phi':dump_q_dict(Phi[n]),'C':dump_q_dict(C[n])}
json.dump({'cl_exact':qstr(c),'source':'state131 Theta0 (exact), lane c1-n1 ipm_exact.stationary_orders','orders':out}, open(f'RUN_ROOT/numerics_N1N2/numerics/far_field/state131_stationary_orders_exact_0_{nmax}.json','w'))
print('done', flush=True)
