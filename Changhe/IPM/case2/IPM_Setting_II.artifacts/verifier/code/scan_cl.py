"""Fixed-c_l Picard iteration xi -> T_cl(xi) of code/charsolve.py (c_l a parameter, p = 1/c_l), reporting the scalar
compatibility defect g(c_l) = c_l - 1/2 - sqrt(c^2 + b^2) at the fixed point (a profile needs g = 0)."""
import numpy as np, torch, sys, json, time, argparse
sys.path.insert(0, 'code')
from charsolve import CharSolver
ap = argparse.ArgumentParser()
ap.add_argument('--cls', default='1.5,2,3')
ap.add_argument('--a', type=float, default=1.5)
ap.add_argument('--eps', type=float, default=0.0)
ap.add_argument('--mix', type=float, default=0.5)
ap.add_argument('--maxit', type=int, default=60)
ap.add_argument('--nt', type=int, default=64)
ap.add_argument('--q', type=int, default=8)
ap.add_argument('--L', type=float, default=1e10)
args = ap.parse_args()
r1 = 1e-6
edges = np.concatenate([[0.0], np.geomspace(r1, 0.1, 12), np.geomspace(0.1, 10, 25)[1:],
                        np.geomspace(10, args.L, int(round(np.log10(args.L/10)*5)) + 1)[1:]])
S = CharSolver(edges, args.q, args.nt, r1, 'cuda')
X, Y, R = S.X, S.Y, S.R
for cl in [float(v) for v in args.cls.split(',')]:
    p = 1/cl
    wsc = R/(1 + R**2)**((1 - p/2)/2)
    xi = X*(1 + args.a*Y/(1 + R**2)**0.5 + args.eps*X/(1+R**2)**0.5)*(1 + R**2)**((p/2 - 1)/2)
    for it in range(args.maxit):
        new, d = S.T(xi, info=True, cl_fixed=cl)
        fp = float(((new - xi)/wsc).abs().max())
        if not np.isfinite(fp): print('cl', cl, 'it', it, 'non-finite', d); break
        xi = (1 - args.mix)*xi + args.mix*new
        if it % 5 == 0 or fp < 1e-11:
            print(json.dumps(dict(cl=cl, it=it, fp=fp, c=d['c'], b=d['b'], g=d['g'], minVr_r=d['minVr_r'])), flush=True)
        if fp < 1e-11: break
