"""Global (Newton) homotopy for the unforced profile system with the far-field exponent p as an explicit unknown
(replaces code/homotopy_char.py --exactp 1, whose inner scalar solve of p = 1/c_l(p) stalls where that scalar
equation has a double root). Unknowns Z = (v, p, s), z = v wsc; with ExtSolver.Tp at h = 1 (= the unforced map of
code/charsolve.py with tail exponent p in both the moment functionals and W):
    F(v, p) = (z - T(z; p))/wsc,  g(v, p) = c_l(z; p) p - 1,
    H(Z) = (F(v, p) - s F(v0, p0),  g(v, p) - s g(v0, p0)) = 0,   s = 1 at the seed, s = 0 a profile with p = 1/c_l.
Metric |dv|^2/nv + dp^2 + ds^2; Keller corrector, exact forward-AD JVPs, bordered GMRES (code/forced_char.gmres).
Admissibility: T finite, min V_r/r > vrmin on r >= r1, c_l > clmin, 0 < p < pmax. Logs JSON lines to runs/NAME.log."""
import numpy as np, torch, sys, json, time, argparse, math
sys.path.insert(0, 'code')
from forced_char import gmres
from forced_pal import ExtSolver
import torch.autograd.forward_ad as fwAD

ap = argparse.ArgumentParser()
ap.add_argument('--name', required=True)
ap.add_argument('--q', type=int, default=8)
ap.add_argument('--nt', type=int, default=64)
ap.add_argument('--r1', type=float, default=1e-6)
ap.add_argument('--L', type=float, default=1e4)
ap.add_argument('--ncore', type=int, default=24)
ap.add_argument('--a', type=float, default=1.5)
ap.add_argument('--eps', type=float, default=0.0)
ap.add_argument('--p0', type=float, default=0.5)
ap.add_argument('--ds', type=float, default=0.01)
ap.add_argument('--dsmax', type=float, default=0.2)
ap.add_argument('--dsmin', type=float, default=1e-7)
ap.add_argument('--steps', type=int, default=1500)
ap.add_argument('--kmax', type=int, default=100)
ap.add_argument('--gtol', type=float, default=1e-9)
ap.add_argument('--ctol', type=float, default=1e-9)
ap.add_argument('--vrmin', type=float, default=0.02)
ap.add_argument('--clmin', type=float, default=1.0005)
ap.add_argument('--pmax', type=float, default=0.999)
ap.add_argument('--maxwall', type=float, default=3000)
args = ap.parse_args()
dev = 'cuda'
edges = np.concatenate([[0.0], np.geomspace(args.r1, 0.1, 12), np.geomspace(0.1, 10, args.ncore + 1)[1:],
                        np.geomspace(10, args.L, int(round(np.log10(args.L/10)*5)) + 1)[1:]])
S = ExtSolver(edges, args.q, args.nt, args.r1, dev)
S.set_forcing(1.0, 0.0, 2.0)                      # h = 1: no forcing (E = 0)
X, Y, R = S.X, S.Y, S.R
rr = (1 + R**2)**0.5
z0 = X*(1 + args.a*Y/rr + args.eps*(X + Y**2/rr)/rr)*rr**(args.p0/2 - 1)
wsc = R/rr*rr**(args.p0/2)
LOG = open(f'runs/{args.name}.log', 'w')
def log(d):
    LOG.write(json.dumps(d) + '\n'); LOG.flush(); print(json.dumps(d), flush=True)
log(dict(start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), args=vars(args), Nr=S.Nr, nt=S.nt))
shp = z0.shape; nv = z0.numel(); nt = S.nt
idx = (nt//2 - torch.arange(nt, device=dev)) % nt
one = torch.tensor(1.0, dtype=torch.float64, device=dev)

def split(Z):
    return Z[:nv].reshape(shp), Z[nv], Z[nv + 1]

def base(v, p, info=False):
    z = v*wsc
    out = S.Tp(z, p, one, info=info)
    r = torch.cat([((z - out[0])/wsc).flatten(), out[1].reshape(1)])
    return (r, out[2]) if info else r

Z0 = torch.cat([(z0/wsc).flatten(), torch.tensor([args.p0, 1.0], dtype=torch.float64, device=dev)])
r0, d0 = base(Z0[:nv].reshape(shp), Z0[nv], info=True)
r0 = r0.detach()

def resid(Z, info=False):
    v, p, s = split(Z)
    out = base(v, p, info)
    if info: return out[0] - s*r0, out[1]
    return out - s*r0

def jvp(Z, dZ):
    with fwAD.dual_level():
        r = resid(fwAD.make_dual(Z, dZ))
        return fwAD.unpack_dual(r).tangent

def inner(a, b):
    return float(torch.dot(a[:nv], b[:nv]))/nv + float(a[nv]*b[nv] + a[nv + 1]*b[nv + 1])

def Mvec(t):
    m = t.clone(); m[:nv] = m[:nv]/nv; return m

def admissible(Z):
    r, d = resid(Z, info=True)
    ok = bool(torch.isfinite(r).all()) and d['minVr_r'] > args.vrmin and d['cl'] > args.clmin and 0 < d['p'] < args.pmax
    return r, d, ok

def solve_bordered(Z, m, rhs_top, rhs_last):
    A = lambda x: torch.cat([jvp(Z, x), torch.dot(m, x).reshape(1)])
    b = torch.cat([rhs_top, torch.as_tensor(rhs_last, dtype=torch.float64, device=dev).reshape(1)])
    return gmres(A, b, args.kmax, args.gtol)

def save(tag, Z, d):
    v, p, s = split(Z)
    torch.save(dict(xi=(v*wsc).cpu(), edges=edges, q=args.q, nt=args.nt, r1=args.r1, args=vars(args), d=d, s=float(s),
                    h=1.0), f'runs/{args.name}_{tag}.pt')

t0 = time.time()
Z = Z0.clone()
r, d, ok = admissible(Z)
log(dict(step=0, **d, s=1.0, nF0=float(r0.norm()), g0=float(r0[-1]), res=float(r.abs().max()), ok=ok))
if not ok: log(dict(msg='seed not admissible')); sys.exit(0)
es = torch.zeros(nv + 2, dtype=torch.float64, device=dev); es[nv + 1] = 1.0
t, _, _ = solve_bordered(Z, es, torch.zeros(nv + 1, dtype=torch.float64, device=dev), -1.0)   # ds/dsigma < 0
t = t/math.sqrt(inner(t, t))
ds = args.ds
for step in range(1, args.steps + 1):
    if time.time() - t0 > args.maxwall: log(dict(msg='maxwall')); break
    acc = False
    while ds > args.dsmin:
        Zp = Z + ds*t; m = Mvec(t)
        conv = False; okp = False
        for kc in range(8):
            rp, dp, okp = admissible(Zp)
            if not okp: break
            rn = float(rp.abs().max())
            cons = float(torch.dot(m, Zp - Z)) - ds
            if rn < args.ctol and abs(cons) < 1e-8*ds: conv = True; break
            x, gr, kk = solve_bordered(Zp, m, -rp, -cons)
            Zp = Zp + x
        if conv and okp: acc = True; break
        ds *= 0.5
    if not acc:
        log(dict(step=step, msg='step size underflow (path leaves admissible set or corrector fails)', **d)); break
    tn, _, kk2 = solve_bordered(Zp, Mvec(t), torch.zeros(nv + 1, dtype=torch.float64, device=dev), 1.0)
    tn = tn/math.sqrt(inner(tn, tn))
    if inner(tn, t) < 0: tn = -tn
    turned = float(tn[nv + 1])*float(t[nv + 1]) < 0
    Z, t, d = Zp, tn, dp
    v, p, s = split(Z)
    z = v*wsc
    xo = 0.5*(z + z[:, idx])
    log(dict(step=step, s=float(s), ds=ds, kc=kc, kry=kk2, turned=turned, ds_dsig=float(t[nv + 1]), dp_dsig=float(t[nv]),
             **d, res=rn, Finf_true=float((rp + s*r0)[:nv].abs().max()), xodd_frac=float((xo/wsc).abs().max()/(v.abs().max())),
             wall=time.time() - t0))
    if turned: save(f'turn{step:04d}', Z, d)
    if step % 20 == 0: save('last', Z, d)
    if float(s) <= 0:
        log(dict(msg='crossed s = 0: profile bracket', s=float(s), **d)); save('s0', Z, d); break
    if kc <= 2: ds = min(ds*1.5, args.dsmax)
log(dict(end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), wall=time.time() - t0))
