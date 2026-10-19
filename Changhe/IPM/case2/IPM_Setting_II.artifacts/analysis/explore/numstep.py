# Lead: evolve a lead-format state with the numerics' transport scheme (their PFwdB.step, CPU, read-only import), with or
# without their bilinear-hull limiter, to test whether their stationary core differs from the lead one because of the scheme.
# Usage: python3 numstep.py state.npz K nsteps limiter(0/1) out.npz [bs]   (bs: their interp replaced by bspline_torch.interp_bspline)
import sys, time, numpy as np, torch
sys.path.insert(0, '../numerics/code')
sys.path.insert(0, 'explore')
torch.set_default_dtype(torch.float64)
from pfwd_batch import PFwdB
if len(sys.argv) > 6 and sys.argv[6] == 'bs':
    import bspline_torch as BT; BT.patch(PFwdB); print('interp: B-spline (bspline_torch)', flush=True)
import fpeval as FE
d = np.load(sys.argv[1]); K = int(sys.argv[2]); nst = int(sys.argv[3]); lim = bool(int(sys.argv[4])); out = sys.argv[5]
g, lr, th, p, x = d['g'], d['lr'], d['th'], float(d['p']), d['x'][:K]; Nr, Nth = g.shape
S = PFwdB(Nr, Nth, lr[0], lr[-1], p, dev='cpu', limiter=lim)
def Af_np(t):
    t = np.atleast_1d(t).ravel(); return np.cos(t) ** 2 * np.exp(x @ FE.basis(t, K))
def Afun(T):
    sh = T.shape; return torch.tensor(Af_np(T.numpy().ravel()).reshape(sh))
A = torch.tensor(Af_np(th))[None]; G = torch.tensor(g)[None]; pB = torch.tensor([p])
t0 = time.time(); done = 0
while done < nst:
    n = min(100, nst - done); G, dg = S.evolve(G, pB, A, Afun, 0.02, n); done += n
    print('steps', done, 'dg/ds %.2e' % float(dg[0]), 'wall %.0f' % (time.time() - t0), flush=True)
np.savez(out, g=G[0].numpy(), lr=lr, th=th, x=x, p=p, m1=np.nan)
