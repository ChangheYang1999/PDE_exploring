"""Driver for the verifier's independent solver (code/charsolve.py): Picard or Newton-Krylov on xi = T(xi).
Usage: python3 run_char.py --name NAME [--method picard|newton] [--init gauss|power] [--a 1.5] [--eps 0.0] ...
Writes runs/NAME.log (one JSON line per iteration) and runs/NAME.pt (final xi, grid)."""
import numpy as np, torch, sys, json, time, argparse
sys.path.insert(0, 'code')
from charsolve import CharSolver
ap = argparse.ArgumentParser()
ap.add_argument('--name', required=True)
ap.add_argument('--method', default='picard')
ap.add_argument('--q', type=int, default=8)
ap.add_argument('--nt', type=int, default=64)
ap.add_argument('--r1', type=float, default=1e-6)
ap.add_argument('--L', type=float, default=1e10)
ap.add_argument('--ncore', type=int, default=24)
ap.add_argument('--a', type=float, default=1.5)       # init: xi0 = x (1 + a y + eps*(x - y^2)) f(r)
ap.add_argument('--eps', type=float, default=0.0)     # x-asymmetric part of the initial guess
ap.add_argument('--p0', type=float, default=0.6)
ap.add_argument('--mix', type=float, default=1.0)
ap.add_argument('--maxit', type=int, default=40)
ap.add_argument('--init', default='power')
ap.add_argument('--load', default=None)
ap.add_argument('--ftol', type=float, default=1e-10)
args = ap.parse_args()
dev = 'cuda'
edges = np.concatenate([[0.0], np.geomspace(args.r1, 0.1, 12), np.geomspace(0.1, 10, args.ncore + 1)[1:],
                        np.geomspace(10, args.L, int(round(np.log10(args.L/10)*5)) + 1)[1:]])
S = CharSolver(edges, args.q, args.nt, args.r1, dev)
X, Y, R = S.X, S.Y, S.R
if args.load:
    d = torch.load(args.load)
    from charsolve import CharSolver as _C
    # interpolate old solution onto this grid via its own PolarGrid (Fourier in theta, panel Lagrange in r)
    raise NotImplementedError
else:
    a, e, p0 = args.a, args.eps, args.p0
    if args.init == 'power':
        f = (1 + R**2)**((p0/2 - 2)/2)
        xi = X*(1 + a*Y + e*(X - Y**2/(1+R**2)**0.5))*f
    else:
        xi = X*(1 + a*Y + e*X)*torch.exp(-R**2/2)
log = open(f'runs/{args.name}.log', 'w')
log.write('# ' + time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + ' ' + json.dumps(vars(args)) + f' Nr={S.Nr} nt={S.nt}\n')
log.flush()
wsc = R/(1 + R**2)**((1 - args.p0/2)/2)          # magnitude scale of xi (r near 0, r^{p/2} far)

def diag(xi, it, extra):
    new, d = S.T(xi, info=True)
    Rr, dr = S.residual(xi)
    rho = xi**2
    p = dr['p']
    wR = R**2/(1 + R**2)**(1 - p/2)
    out = dict(it=it, **d, fp=float(((new - xi)/wsc).abs().max()))
    for Rm in (1.0, 10.0, 1e3, 1e8):
        msk = R < Rm
        out[f'Rw<{Rm:g}'] = float((Rr/wR)[msk].abs().max())
    nt = S.nt
    idx = (nt//2 - torch.arange(nt, device=dev)) % nt
    xo = 0.5*(xi + xi[:, idx])        # xi odd in x <=> xi(pi - th) = -xi(th); x-even rho <=> xi odd in x
    out['xodd_frac'] = float((xo/wsc).abs().max()/((xi/wsc).abs().max()))
    out.update(extra)
    log.write(json.dumps(out) + '\n'); log.flush()
    print(json.dumps(out), flush=True)
    return new, out

t0 = time.time()
if args.method == 'picard':
    for it in range(args.maxit):
        new, out = diag(xi, it, dict(t=time.time() - t0))
        if not np.isfinite(out['fp']) or out['cl'] <= 1.0:
            print('stop: non-finite or c_l <= 1', flush=True); break
        xi = (1 - args.mix)*xi + args.mix*new
else:
    from scipy.optimize import newton_krylov
    shape = xi.shape
    def F(v):
        z = torch.tensor(v.reshape(shape), device=dev)*wsc
        return ((z - S.T(z))/wsc).cpu().numpy().ravel()
    it_ = [0]
    def cb(v, f):
        z = torch.tensor(v.reshape(shape), device=dev)*wsc
        diag(z, it_[0], dict(t=time.time() - t0, Fnorm=float(np.abs(f).max())))
        it_[0] += 1
    v0 = (xi/wsc).cpu().numpy().ravel()
    try:
        sol = newton_krylov(F, v0, method='lgmres', f_tol=args.ftol, maxiter=args.maxit, callback=cb, verbose=True,
                            inner_maxiter=60)
        xi = torch.tensor(sol.reshape(shape), device=dev)*wsc
    except Exception as ex:
        print('newton_krylov stopped:', repr(ex), flush=True)
torch.save(dict(xi=xi.cpu(), edges=edges, q=args.q, nt=args.nt, r1=args.r1, args=vars(args)),
           f'runs/{args.name}.pt')
print('wall', time.time() - t0)
