"""Global (Newton) homotopy with pseudo-arclength continuation for the fixed point xi = T(xi) of code/charsolve.py:
    H(v, s) = F(v) - s F(v0) = 0,  F(v) = (z - T(z))/wsc, z = v wsc,
starting at (v0, s = 1). The path is followed through turning points; a profile is a point of the path with s = 0.
Every JVP is exact (forward-mode AD through T). Bordered corrector: two GMRES solves per Newton step.
Admissibility on the path: T finite, min V_r/r > vrmin on r >= r1, c_l > clmin. Logs JSON lines to runs/NAME.log."""
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
ap.add_argument('--a', type=float, default=1.5)
ap.add_argument('--eps', type=float, default=0.0)
ap.add_argument('--p0', type=float, default=0.5)
ap.add_argument('--ds', type=float, default=0.02)       # initial arclength step (in units of |v| ~ |F0|)
ap.add_argument('--dsmax', type=float, default=0.5)
ap.add_argument('--steps', type=int, default=400)
ap.add_argument('--kmax', type=int, default=60)
ap.add_argument('--gtol', type=float, default=1e-6)
ap.add_argument('--vrmin', type=float, default=0.02)
ap.add_argument('--clmin', type=float, default=1.0005)
ap.add_argument('--load', default=None)
ap.add_argument('--ctol', type=float, default=1e-7)   # corrector tolerance |H| < ctol |F(v0)|
ap.add_argument('--maxwall', type=float, default=3.5*3600)
ap.add_argument('--exactp', type=int, default=0)   # 1: exact far-field self-consistency (charsolve.solve_p)
args = ap.parse_args()
dev = 'cuda'
edges = np.concatenate([[0.0], np.geomspace(args.r1, 0.1, 12), np.geomspace(0.1, 10, args.ncore + 1)[1:],
                        np.geomspace(10, args.L, int(round(np.log10(args.L/10)*5)) + 1)[1:]])
S = CharSolver(edges, args.q, args.nt, args.r1, dev)
S.exact_p = bool(args.exactp)
X, Y, R = S.X, S.Y, S.R
rr = (1 + R**2)**0.5
if args.load:
    d0 = torch.load(args.load, weights_only=False); z0 = d0['xi'].to(dev)
else:
    z0 = X*(1 + args.a*Y/rr + args.eps*(X + Y**2/rr)/rr)*rr**(args.p0/2 - 1)
wsc = R/rr*rr**(args.p0/2)
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
    ok = bool(torch.isfinite(F).all()) and d['minVr_r'] > args.vrmin and d['cl'] > args.clmin and d.get('fp', 0.0) < 1e-9
    return F, d, ok

def Jv(v, u):
    with fwAD.dual_level():
        zd = fwAD.make_dual(v*wsc, u*wsc)
        tz = fwAD.unpack_dual(S.T(zd)).tangent
    return u - tz/wsc

def gmres(Av, b, kmax, tol):
    n = b.numel(); beta = float(b.norm())
    if beta == 0: return torch.zeros_like(b), 0.0, 0
    V = torch.zeros((kmax + 1, n), dtype=b.dtype, device=b.device)
    H = np.zeros((kmax + 1, kmax)); cs_, sn_ = np.zeros(kmax), np.zeros(kmax)
    g = np.zeros(kmax + 1); g[0] = beta; V[0] = b.flatten()/beta; k_used = 0
    for k in range(kmax):
        w = Av(V[k].reshape(b.shape)).flatten()
        for j in range(k + 1):
            H[j, k] = float(torch.dot(w, V[j])); w = w - H[j, k]*V[j]
        H[k + 1, k] = float(w.norm())
        if H[k + 1, k] > 0: V[k + 1] = w/H[k + 1, k]
        for j in range(k):
            t = cs_[j]*H[j, k] + sn_[j]*H[j + 1, k]
            H[j + 1, k] = -sn_[j]*H[j, k] + cs_[j]*H[j + 1, k]; H[j, k] = t
        den = math.hypot(H[k, k], H[k + 1, k]); cs_[k], sn_[k] = H[k, k]/den, H[k + 1, k]/den
        H[k, k] = den; H[k + 1, k] = 0.0; g[k + 1] = -sn_[k]*g[k]; g[k] = cs_[k]*g[k]
        k_used = k + 1
        if abs(g[k + 1])/beta < tol: break
    y = np.linalg.solve(np.triu(H[:k_used, :k_used]), g[:k_used])
    x = torch.einsum('k,kn->n', torch.tensor(y, dtype=b.dtype, device=b.device), V[:k_used]).reshape(b.shape)
    return x, abs(g[k_used])/beta, k_used

def Q_over(z, d):
    rho = z**2
    W1, W2 = S.velocity(rho, d['p'])
    Wr = W1*S.cs + W2*S.sn; Wt = -W1*S.sn + W2*S.cs
    g = 3*S.R**-4*(-Wr*torch.sin(3*S.TH) + Wt*torch.cos(3*S.TH))
    Q = float(torch.sum(S.w[:, None]*S.r[:, None]*rho*g)*(2*math.pi/nt))
    return Q/(math.pi*d['c']**2), 1 - 1/(2*d['c'])

t0 = time.time()
v = z0/wsc
F0, d, ok = evalF(v)
nF0 = float(F0.norm())
G = F0/nF0                      # H(v, s) = F(v) - s nF0 G, path parameter s in [0, 1] (s = 1 at v0)
s = 1.0
log(dict(step=0, s=s, nF0=nF0, **d, ok=ok))
if not ok: log(dict(msg='initial state not admissible')); sys.exit(0)
# initial tangent: J tv = G ts; choose ts < 0 (decrease s)
b_, gr, kk = gmres(lambda u: Jv(v, u), G, args.kmax, args.gtol)     # J b = G
def tangent(b_):
    tv = b_*nF0; ts = 1.0                                  # J tv = nF0 G ts
    nrm = math.sqrt(float(tv.norm())**2 + (nF0*ts)**2)
    return tv/nrm, ts/nrm
tv, ts = tangent(b_)
if ts > 0: tv, ts = -tv, -ts
ds = args.ds*nF0
for step in range(1, args.steps + 1):
    if time.time() - t0 > args.maxwall: log(dict(msg='maxwall')); break
    accepted = False
    while ds > 1e-6*nF0:
        vp, sp = v + ds*tv, s + ds*ts                    # predictor
        conv = False
        for kc in range(8):                              # corrector (bordered Newton)
            Fp, dp, okp = evalF(vp)
            if not okp: break
            Hres = Fp - sp*nF0*G
            hn = float(Hres.norm())
            if hn < args.ctol*nF0: conv = True; break
            A = lambda u, vp=vp: Jv(vp, u)
            a_, _, _ = gmres(A, -Hres, args.kmax, args.gtol)
            bb, _, _ = gmres(A, nF0*G, args.kmax, args.gtol)
            # arclength constraint in the metric |dv|^2 + nF0^2 ds^2: <tv, vp - v> + nF0^2 ts (sp - s) = ds;
            # dv = a_ + dsg bb, linearised: <tv, a_ + dsg bb> + nF0^2 ts dsg = -res_arc
            res_arc = float(torch.sum(tv*(vp - v))) + nF0**2*ts*(sp - s) - ds
            den = float(torch.sum(tv*bb)) + nF0**2*ts
            dsg = (-res_arc - float(torch.sum(tv*a_)))/den
            vp = vp + a_ + dsg*bb; sp = sp + dsg
        if conv and okp:
            accepted = True; break
        ds *= 0.5
    if not accepted:
        log(dict(step=step, msg='step size underflow (path leaves admissible set or corrector fails)', s=s, **d)); break
    # new tangent at (vp, sp): J b = G, tv ~ nF0 b, orient along previous tangent
    b_, gr, kk = gmres(lambda u: Jv(vp, u), G, args.kmax, args.gtol)
    tvn, tsn = tangent(b_)
    if float(torch.sum(tvn*tv)) + nF0**2*tsn*ts < 0: tvn, tsn = -tvn, -tsn
    turned = (tsn*ts < 0)
    v, s, d, tv, ts = vp, sp, dp, tvn, tsn
    S.p_start = d['p']                                   # start of the exact p solve at the next point
    out = dict(step=step, s=s, ds=ds/nF0, turned=turned, kc=kc, gm=kk, **d, Finf=float(Fp.abs().max()), wall=time.time() - t0)
    if step % 5 == 0 or turned or abs(s) < 0.05:
        try: out['Qpc2'], out['1-1/2c'] = Q_over(v*wsc, d)
        except Exception: pass
        xo = 0.5*(v*wsc + (v*wsc)[:, idx]); out['xodd_frac'] = float((xo/wsc).abs().max()/((v).abs().max()))
    log(out)
    if s <= 0:
        log(dict(msg='crossed s = 0: candidate fixed point bracket', s=s, **d))
        torch.save(dict(xi=(v*wsc).cpu(), edges=edges, q=args.q, nt=args.nt, r1=args.r1, args=vars(args), d=d, s=s),
                   f'runs/{args.name}_s0.pt')
        break
    if kc <= 2: ds = min(ds*1.5, args.dsmax*nF0)
    if step % 20 == 0:
        torch.save(dict(xi=(v*wsc).cpu(), edges=edges, q=args.q, nt=args.nt, r1=args.r1, args=vars(args), d=d, s=s),
                   f'runs/{args.name}.pt')
log(dict(end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), wall=time.time() - t0))
