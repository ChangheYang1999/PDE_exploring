"""Adversarial search for the Setting II node: maximise the central strain c[A] of the forward-evolution steady state (equivalently
minimise m1 - 1/2 = c_l - 1/2 - c) over a positive datum family with two quadratic zeros at +-90 deg,
      A(theta) = cos^2(theta) exp( x_1 sin th + x_2 cos 2th + x_3 sin 3th + x_4 cos 4th + ... )  (x-even basis, K terms),
by Nelder-Mead (scipy).  Each evaluation runs the evolution (warm start from the previous steady state) to a steady state and
returns the deficit c_target - c_moment (penalty if the evolution does not converge).  Also reports m1 from the ring fit.
Usage: python3 tests/pfwd_opt.py p K tag [nsteps=800] [Nr=661] [Nth=256] [x0=comma list]"""
import sys, json, math, time; sys.path.insert(0, 'code')
import numpy as np, torch
from scipy.optimize import minimize
from pfwd import PFwd
torch.set_default_dtype(torch.float64)
p = float(sys.argv[1]); K = int(sys.argv[2]); tag = sys.argv[3]
opt = dict(nsteps=800, Nr=661, Nth=256, x0='', lo=-12.0, hi=10.0, ds=0.02, maxfev=150)
for a in sys.argv[4:]:
    k, v = a.split('='); opt[k] = v if k == 'x0' else (int(v) if k in ('nsteps', 'Nr', 'Nth', 'maxfev') else float(v))
S = PFwd(opt['Nr'], opt['Nth'], opt['lo'], opt['hi'], p, dev='cuda')
# x-even basis (invariant under theta -> pi - theta): sin th, cos 2th, sin 3th, cos 4th, sin 5th, ...  (K terms, K parameters)
def basis(th, k):
    n = k + 1
    return torch.sin(n * th) if n % 2 == 1 else torch.cos(n * th)
def Afun_of(x):
    def Afun(th):
        f = torch.zeros_like(th)
        for k in range(K):
            f = f + x[k] * basis(th, k)
        return torch.cos(th) ** 2 * torch.exp(f)
    return Afun
state = {'g': None, 'best': (1e9, None), 'n': 0}
log = open('runs/pfwd/opt_%s.log' % tag, 'a')
def evaluate(x):
    Afun = Afun_of(x); A = Afun(S.th)
    if state['g'] is None:
        g = ((S.r ** 2 / (1.0 + S.r ** 2)) ** (1.0 - p / 2))[:, None] * A[None, :]
    else:
        g = state['g'] * (A[None, :] / torch.clamp(state['A'], min=1e-12))  # rescale the far field to the new datum
        g = torch.where(state['A'][None, :] > 1e-6, g, (S.r[:, None] ** 2 / (1 + S.r[:, None] ** 2)) ** (1 - p / 2) * A[None, :])
    t0 = time.time(); dg = 1.0
    for n in range(opt['nsteps']):
        gn, (Wr, Wt) = S.step(g, opt['ds'], A, Afun)
        if n % 50 == 49:
            dg = float((gn - g).abs().max()) / opt['ds']
            if not math.isfinite(dg) or dg > 1e3:
                break
        g = gn
    ok = math.isfinite(dg) and dg < 1e-4
    if ok:
        d = S.diagnostics(g, Wr, Wt, krings=(20,))
        deficit = d['c_target'] - d['c_moment']; m1 = d['ring20']['m1']; e1 = d['ring20']['e1_deg']
        state['g'] = g; state['A'] = A
    else:
        deficit = 10.0; m1 = float('nan'); e1 = float('nan')
    state['n'] += 1
    rec = dict(n=state['n'], x=[round(float(v), 5) for v in x], deficit=round(deficit, 6), m1=round(m1, 6) if ok else None, e1=e1 if ok else None,
               dgds='%.1e' % dg, wall=round(time.time() - t0, 1))
    if ok and deficit < state['best'][0]:
        state['best'] = (deficit, list(map(float, x)))
        np.savez('runs/pfwd/opt_%s_best.npz' % tag, g=g.cpu().numpy(), lr=S.lr.cpu().numpy(), th=S.th.cpu().numpy(),
                 hist=json.dumps([rec]), args=json.dumps(dict(p=p, kind='expfourier', par=list(map(float, x)), K=K)))
    print(json.dumps(rec), flush=True); log.write(json.dumps(rec) + '\n'); log.flush()
    return deficit
x0 = np.zeros(K) if not opt['x0'] else np.array([float(v) for v in opt['x0'].split(',')])
res = minimize(evaluate, x0, method='Nelder-Mead', options=dict(maxfev=opt['maxfev'], xatol=1e-3, fatol=1e-4, initial_simplex=np.vstack([x0] + [x0 + 0.3 * np.eye(K)[i] for i in range(K)])))
print("RESULT", json.dumps(dict(p=p, K=K, best_deficit=state['best'][0], best_x=state['best'][1], nfev=res.nfev, msg=str(res.message))), flush=True)
log.write("RESULT " + json.dumps(dict(p=p, K=K, best_deficit=state['best'][0], best_x=state['best'][1], nfev=res.nfev)) + '\n'); log.close()
