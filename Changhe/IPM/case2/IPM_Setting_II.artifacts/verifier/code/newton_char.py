"""Damped Newton-GMRES (own implementation, torch, float64) for the fixed point xi = T(xi) of code/charsolve.py.
F(v) = (z - T(z))/wsc, z = v*wsc. Jacobian-vector products by central finite differences of T. Backtracking line
search on |F|_2; a trial state is admissible only if T is finite, min V_r/r > vrmin on r >= r1 and c_l > clmin
(class S needs c_l > 1). Logs one JSON line per Newton step (and per rejected trial) to runs/NAME.log.
Usage: python3 newton_char.py --name NAME [--a 1.5 --p0 0.5 --eps 0 --nt 64 --L 1e10 --maxit 30 ...]"""
import numpy as np, torch, sys, json, time, argparse, math
sys.path.insert(0, 'code')
from charsolve import CharSolver
import torch.autograd.forward_ad as fwAD
ap = argparse.ArgumentParser()
ap.add_argument('--name', required=True)
ap.add_argument('--q', type=int, default=8)
ap.add_argument('--nt', type=int, default=64)
ap.add_argument('--r1', type=float, default=1e-6)
ap.add_argument('--L', type=float, default=1e10)
ap.add_argument('--ncore', type=int, default=24)
ap.add_argument('--a', type=float, default=1.5)     # zeta0 = x (1 + a y/<r> + eps (x + y^2/<r>)/<r>) <r>^{p0/2 - 1}
ap.add_argument('--eps', type=float, default=0.0)
ap.add_argument('--p0', type=float, default=0.5)
ap.add_argument('--maxit', type=int, default=30)
ap.add_argument('--kmax', type=int, default=60)     # GMRES Krylov dimension (no restart)
ap.add_argument('--gtol', type=float, default=1e-3) # relative GMRES tolerance (inexact Newton)
ap.add_argument('--fd', type=float, default=1e-6)
ap.add_argument('--vrmin', type=float, default=0.02)
ap.add_argument('--clmin', type=float, default=1.0005)
ap.add_argument('--ftol', type=float, default=1e-9)
ap.add_argument('--load', default=None)
ap.add_argument('--jvp', default='ad')              # 'ad' (forward-mode AD through T) or 'fd' (central differences)
args = ap.parse_args()
dev = 'cuda'
edges = np.concatenate([[0.0], np.geomspace(args.r1, 0.1, 12), np.geomspace(0.1, 10, args.ncore + 1)[1:],
                        np.geomspace(10, args.L, int(round(np.log10(args.L/10)*5)) + 1)[1:]])
S = CharSolver(edges, args.q, args.nt, args.r1, dev)
X, Y, R = S.X, S.Y, S.R
rr = (1 + R**2)**0.5
if args.load:
    d = torch.load(args.load)
    assert np.allclose(d['edges'], edges) and d['nt'] == args.nt and d['q'] == args.q, 'grid mismatch'
    z0 = d['xi'].to(dev)
else:
    z0 = X*(1 + args.a*Y/rr + args.eps*(X + Y**2/rr)/rr)*rr**(args.p0/2 - 1)
wsc = R/rr*rr**(args.p0/2)               # ~ r near 0, r^{p0/2} far
LOG = open(f'runs/{args.name}.log', 'w')
def log(d):
    LOG.write(json.dumps(d) + '\n'); LOG.flush(); print(json.dumps(d), flush=True)
log(dict(start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), args=vars(args), Nr=S.Nr, nt=S.nt))
nt = S.nt
idx = (nt//2 - torch.arange(nt, device=dev)) % nt

def evalF(v):
    z = v*wsc
    new, d = S.T(z, info=True)
    F = (z - new)/wsc
    ok = bool(torch.isfinite(F).all()) and d['minVr_r'] > args.vrmin and d['cl'] > args.clmin
    return F, d, ok

def Q_over(z, d):
    """Q/(pi c^2) and 1 - 1/(2c) (lead's necessary condition, V13(b))."""
    rho = z**2
    W1, W2 = S.velocity(rho, d['p'])
    Wr = W1*S.cs + W2*S.sn; Wt = -W1*S.sn + W2*S.cs
    g = 3*S.R**-4*(-Wr*torch.sin(3*S.TH) + Wt*torch.cos(3*S.TH))
    Q = float(torch.sum(S.w[:, None]*S.r[:, None]*rho*g)*(2*math.pi/nt))
    c = d['c']
    return Q/(math.pi*c*c), 1 - 1/(2*c)

def diag(v, F, d, it, extra):
    z = v*wsc
    Rr, dr = S.residual(z)
    wR = R**2/(1 + R**2)**(1 - dr['p']/2)
    out = dict(it=it, **d, Finf=float(F.abs().max()), F2=float(F.norm()))
    for Rm in (1.0, 10.0, 1e3, 1e8):
        msk = R < Rm
        out[f'Rw<{Rm:g}'] = float((Rr/wR)[msk].abs().max())
    xo = 0.5*(z + z[:, idx])
    out['xodd_frac'] = float((xo/wsc).abs().max()/((z/wsc).abs().max()))
    try:
        out['Qpc2'], out['1-1/2c'] = Q_over(z, d)
    except Exception:
        pass
    out.update(extra); out['wall'] = time.time() - t0
    log(out)

def gmres(Av, b, kmax, tol):
    """plain GMRES (modified Gram-Schmidt, Givens), x0 = 0. Returns x, relative residual, iterations."""
    n = b.numel(); beta = float(b.norm())
    V = torch.zeros((kmax + 1, n), dtype=b.dtype, device=b.device)
    H = np.zeros((kmax + 1, kmax))
    V[0] = b.flatten()/beta
    cs_, sn_ = np.zeros(kmax), np.zeros(kmax)
    g = np.zeros(kmax + 1); g[0] = beta
    k_used = 0
    for k in range(kmax):
        w = Av(V[k].reshape(b.shape)).flatten()
        for j in range(k + 1):
            H[j, k] = float(torch.dot(w, V[j])); w = w - H[j, k]*V[j]
        H[k + 1, k] = float(w.norm())
        if H[k + 1, k] > 0: V[k + 1] = w/H[k + 1, k]
        for j in range(k):
            t = cs_[j]*H[j, k] + sn_[j]*H[j + 1, k]
            H[j + 1, k] = -sn_[j]*H[j, k] + cs_[j]*H[j + 1, k]; H[j, k] = t
        den = math.hypot(H[k, k], H[k + 1, k])
        cs_[k], sn_[k] = H[k, k]/den, H[k + 1, k]/den
        H[k, k] = den; H[k + 1, k] = 0.0
        g[k + 1] = -sn_[k]*g[k]; g[k] = cs_[k]*g[k]
        k_used = k + 1
        if abs(g[k + 1])/beta < tol: break
    y = np.linalg.solve(np.triu(H[:k_used, :k_used]), g[:k_used])
    x = torch.einsum('k,kn->n', torch.tensor(y, dtype=b.dtype, device=b.device), V[:k_used]).reshape(b.shape)
    return x, abs(g[k_used])/beta, k_used

t0 = time.time()
v = z0/wsc
F, d, ok = evalF(v)
diag(v, F, d, 0, dict(ok=ok))
if not ok:
    log(dict(msg='initial state not admissible')); sys.exit(0)
for it in range(1, args.maxit + 1):
    fn = float(F.norm())
    def Av(u):
        if args.jvp == 'ad':
            with fwAD.dual_level():
                zd = fwAD.make_dual(v*wsc, u*wsc)
                tz = fwAD.unpack_dual(S.T(zd)).tangent
            return u - tz/wsc
        un = float(u.norm()); h = args.fd*(1 + float(v.norm()))/max(un, 1e-300)
        Fp, _, _ = evalF(v + h*u); Fm, _, _ = evalF(v - h*u)
        return (Fp - Fm)/(2*h)
    dv, gres, kk = gmres(Av, -F, args.kmax, args.gtol)
    lam = 1.0; acc = False
    while lam > 1e-4:
        vt = v + lam*dv
        Ft, dt_, okt = evalF(vt)
        if okt and float(Ft.norm()) < (1 - 1e-4*lam)*fn:
            acc = True; break
        log(dict(it=it, reject=lam, ok=okt, F2=float(Ft.norm()) if okt else None, cl=dt_['cl'], minVr_r=dt_['minVr_r']))
        lam *= 0.5
    if not acc:
        log(dict(it=it, msg='line search failed', gmres_res=gres, kry=kk)); break
    v, F, d = vt, Ft, dt_
    diag(v, F, d, it, dict(lam=lam, gmres_res=gres, kry=kk))
    torch.save(dict(xi=(v*wsc).cpu(), edges=edges, q=args.q, nt=args.nt, r1=args.r1, args=vars(args), d=d),
               f'runs/{args.name}.pt')
    if float(F.abs().max()) < args.ftol:
        log(dict(msg='converged')); break
log(dict(end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), wall=time.time() - t0))
