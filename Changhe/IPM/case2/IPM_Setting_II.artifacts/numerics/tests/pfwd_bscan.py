"""Batched scan of forward x-even states: evaluate a family of data in ONE batched evolution (code/pfwd_bnewton.py evaluate()).
Family: base unknown vector x = (a_1..a_K, [bumps], p) and up to two sweep directions "j:v1,v2,..." (component j set to each value;
j = -1 is p; 'c13', 'c51' sweep the compensator amplitude along sin th + sin 3th resp. sin 5th - sin th).  Product of the two sweeps.
Prints m1 (core-corrected), D_ax, drifts, D_samp(deep), dips, bulk std, out-of-span rms, |F| per state.
Usage: python3 tests/pfwd_bscan.py tag K "sig|0" "x1,...,xK[,b..],p" "sweep1" ["sweep2"] [nsteps=1200] [lo=-14] [Nr=721] [lr0=-13] [Nth=256] [cold=0]
       cold=0: warm start from a converged base state (evolved nsteps0 first); cold=1: all from the cold start."""
import sys, json, math, time, os; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_bnewton import BNewton
torch.set_default_dtype(torch.float64)
tag = sys.argv[1]; K = int(sys.argv[2]); sig = [float(v) for v in sys.argv[3].split(',')] if sys.argv[3] != '0' else []
x0 = np.array([float(v) for v in sys.argv[4].split(',')])
sweeps = []; opt = dict(nsteps=1200, nsteps0=1500, lo=-14.0, hi=10.0, Nr=721, lr0=-13.0, Nth=256, cold=0, cut=0.02)
for s_ in sys.argv[5:]:
    if ':' in s_ and '=' not in s_.split(':')[0]:
        j, vals = s_.split(':'); sweeps.append((j, [float(v) for v in vals.split(',')]))
    else:
        k, v = s_.split('='); opt[k] = int(v) if k in ('nsteps', 'nsteps0', 'Nr', 'Nth', 'cold') else float(v)
os.makedirs('runs/pfwd/bscan', exist_ok=True)
log = open('runs/pfwd/bscan/%s.log' % tag, 'a')
BN = BNewton(K, sig, Nr=opt['Nr'], Nth=opt['Nth'], lo=opt['lo'], hi=opt['hi'], lr0=opt['lr0'], cut=opt['cut'], log=log, tag=tag)
assert len(x0) == BN.n, (len(x0), BN.n)
DIR = dict(c13=np.array([1, 0, 1, 0, 0, 0]), c51=np.array([-1, 0, 0, 0, 1, 0]))
def apply(x, j, v):
    x = x.copy()
    if j in DIR:
        x[:6] += v * DIR[j]
    else:
        jj = int(j); x[jj if jj >= 0 else len(x) - 1] = v
    return x
X = [x0.copy()]; labels = [('base', None, None)]
if len(sweeps) == 1:
    for v in sweeps[0][1]: X.append(apply(x0, sweeps[0][0], v)); labels.append((sweeps[0][0], v, None))
elif len(sweeps) == 2:
    for v in sweeps[0][1]:
        for u in sweeps[1][1]:
            X.append(apply(apply(x0, sweeps[0][0], v), sweeps[1][0], u)); labels.append((sweeps[0][0], v, u))
X = np.array(X)
BN.emit(dict(tag=tag, K=K, sigmas=sig, x0=x0.tolist(), sweeps=sweeps, opt=opt, B=len(X), start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
t0 = time.time()
if opt['cold']:
    F, infos, g, lg, tm = BN.evaluate(X, opt['nsteps'])
else:
    F0, inf0, g0, lg0, tm0 = BN.evaluate(x0[None], opt['nsteps0'])
    F, infos, g, lg, tm = BN.evaluate(X, opt['nsteps'], g_start=g0[0], x_start=x0)
    BN.emit(dict(base_first_pass=inf0[0], timing=tm0))
BN.emit(dict(timing=tm, wall=round(time.time() - t0, 1)))
print("%-6s %-9s %-9s | %-8s %-8s %-8s | %-7s %-6s %-6s | %-7s %-7s %-7s %-6s %-6s | %-7s %-7s %-7s" % ('sweep', 'v', 'u', 'm1', 'p', 'normF', 'D_ax', 'drU', 'drD', 'D_samp', 'up89', 'low269', 'bulk', 'rmsun', 'e_p', 'Fp-Fm', 'dgds'))
for (j, v, u), xi, d in zip(labels, X, infos):
    print("%-6s %-9s %-9s | %-8.5f %-8.5f %-8.4f | %-7.3f %-6.3f %-6.3f | %-7.3f %-7.3f %-7.3f %-6.3f %-6.4f | %-7.3f %-7.3f %-7.1e" % (
        j, '' if v is None else '%.4g' % v, '' if u is None else '%.4g' % u, d['m1'], xi[-1], d['normF'], d.get('D_ax', float('nan')), d.get('drift_up', float('nan')),
        d.get('drift_down', float('nan')), d['D_samp'], d['up89'], d['low269'], d['bulk_std'], d['rms_unresolved'], d.get('e_p', float('nan')), d.get('Fp_minus_Fm', float('nan')), d['dgds']))
    BN.emit(dict(sweep=j, v=v, u=u, x=[round(float(t), 6) for t in xi], info=d))
np.savez('runs/pfwd/bscan/%s_states.npz' % tag, X=X, g=g.cpu().numpy(), lr=BN.SB.S.lr.cpu().numpy(), th=BN.SB.S.th.cpu().numpy(), logGt=lg, thA=BN.thA.cpu().numpy(), labels=json.dumps(labels))
print("BSCAN_DONE", flush=True)
