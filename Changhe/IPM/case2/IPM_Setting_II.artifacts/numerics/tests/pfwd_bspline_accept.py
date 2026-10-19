"""Acceptance test of the B-spline transport (notes of the lead analyst 06:47Z item 3): evolve the lead's 512-angle state runs/ev_k64it5_512.npz (lead format:
g (721, 512), lr in [-14, 10], th, x (64,), p) with PFwdB (bspline) and the datum cos^2 exp(sum x_j phi_j); m1 (moment + core) must stay at
0.558-0.560 and the lead's characteristic check (charcore.py) must give < 0.1.  Also runs the Lagrange scheme for comparison.
Usage: python3 tests/pfwd_bspline_accept.py [nsteps=900] [scheme=bs|lag|both] [state=<lead npz>]"""
import sys, json, math, time, os; sys.path.insert(0, 'code')
import numpy as np, torch
from pfwd_batch import PFwdB
torch.set_default_dtype(torch.float64)
opt = dict(nsteps=900, scheme='both', state='runs/ev_k64it5_512.npz', every=300)
for s_ in sys.argv[1:]:
    k, v = s_.split('='); opt[k] = int(v) if k in ('nsteps', 'every') else v
d = np.load(opt['state']); g0 = d['g']; lr = d['lr']; th = d['th']; x = d['x']; p = float(d['p']); Nr, Nth = g0.shape
K = len(x)
def Afun(t):                                    # t [B, ...]
    F = torch.zeros_like(t)
    for j in range(K):
        n = j + 1; F = F + float(x[j]) * (torch.sin(n * t) if n % 2 == 1 else torch.cos(n * t))
    return torch.cos(t) ** 2 * torch.exp(F)
os.makedirs('runs/pfwd/bs', exist_ok=True)
for scheme in (['bs', 'lag'] if opt['scheme'] == 'both' else [opt['scheme']]):
    SB = PFwdB(Nr, Nth, float(lr[0]), float(lr[-1]), p, bspline=(scheme == 'bs')); S = SB.S
    assert abs(float(S.th[1]) - th[1]) < 1e-12 and abs(float(S.lr[0]) - lr[0]) < 1e-12
    g = torch.tensor(g0, device='cuda')[None]; pB = torch.tensor([p], device='cuda'); A = Afun(S.th[None, :])
    rho = S.r[None, :, None] ** p * g; cm, core = SB.c_moment(rho, pB, A)
    print('%s step 0: m1 = %.5f (lead file m1 %s)' % (scheme, 1 / p - float(cm[0]), str(d['m1']) if 'm1' in d.files else '-'), flush=True)
    t0 = time.time(); done = 0
    while done < opt['nsteps']:
        n = min(opt['every'], opt['nsteps'] - done)
        g, dg = SB.evolve(g, pB, A, Afun, 0.02, n); done += n
        rho = S.r[None, :, None] ** p * g; cm, core = SB.c_moment(rho, pB, A)
        print('%s step %d: m1 = %.5f  core %.5f  dg/ds %.1e  (%.0f s)' % (scheme, done, 1 / p - float(cm[0]), float(core[0]), float(dg[0]), time.time() - t0), flush=True)
    fn = 'runs/pfwd/bs/accept_%s_%d.npz' % (scheme, Nth)
    np.savez(fn, g=g[0].cpu().numpy(), lr=lr, th=th, x=x, p=p, m1=1 / p - float(cm[0]))
    print('saved', fn, flush=True)
print('ACCEPT_DONE', flush=True)
