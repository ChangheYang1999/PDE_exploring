"""Transport-consistency check along characteristics (independent of the collocation residual).
For sample points X0, integrate dX/ds = -W(X) backward (RK4) until |X| < eps, then
   Theta_char(X0) = exp((beta-2) s) Theta_state(X_end),
   Omega_char(X0) = exp(-s) Omega_state(X_end) + int_0^s exp(-(s-sig)) Theta_x(X(sig)) dsig   (forward form),
and compare with the state's own Theta(X0), Omega(X0).  W, Theta, Theta_x, Omega are evaluated from the stored
representation through cubic Hermite interpolation of the radial profiles on a fine q-grid (interpolation error
is reported by halving the grid)."""
import sys, math, argparse, json, numpy as np, torch
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from polarlib import *; from evalfields import load_coefs, radial_profiles

ap = argparse.ArgumentParser(); ap.add_argument('npz'); ap.add_argument('--Nfine', type=int, default=6000)
ap.add_argument('--eps', type=float, default=1e-3); ap.add_argument('--ds', type=float, default=0.01)
ap.add_argument('--rmax', type=float, default=1e3); ap.add_argument('--json', default=None)
args = ap.parse_args()
device = dev()
P, cT, cO, NT, NO, K = load_coefs(args.npz); beta = P.beta

class Interp:
    """Cubic Hermite interpolation of radial profiles (value + derivative) on a fine q grid."""
    def __init__(self, Nfine):
        qmax = P.q_of_u(torch.tensor(1e7, dtype=DT)).item()
        q = torch.linspace(0, qmax, Nfine + 1, dtype=DT, device=device)[1:]
        r = P.u_of_q(q) * P.L
        r = torch.cat([torch.logspace(-7, math.log10(float(r[0]) * 0.999), 200, dtype=DT, device=device), r])
        self.r = r
        self.prof = radial_profiles(P, cT, cO, r, NT, NO, K)
    def __call__(self, rq):
        r = self.r
        idx = torch.searchsorted(r, rq).clamp(1, r.shape[0] - 1)
        r0 = r[idx - 1]; r1 = r[idx]; h = r1 - r0; t = ((rq - r0) / h).clamp(0, 1)
        h00 = 2 * t ** 3 - 3 * t ** 2 + 1; h10 = t ** 3 - 2 * t ** 2 + t; h01 = -2 * t ** 3 + 3 * t ** 2; h11 = t ** 3 - t ** 2
        out = {}
        for key, dkey in (('f', 'df'), ('g', 'dg'), ('psi', 'dpsi')):
            v = self.prof[key]; d = self.prof[dkey]
            out[key] = h00 * v[:, idx - 1] + h10 * h * d[:, idx - 1] + h01 * v[:, idx] + h11 * h * d[:, idx]
            # derivative of the Hermite cubic
            dh00 = (6 * t ** 2 - 6 * t) / h; dh10 = (3 * t ** 2 - 4 * t + 1); dh01 = (-6 * t ** 2 + 6 * t) / h; dh11 = (3 * t ** 2 - 2 * t)
            out[dkey] = dh00 * v[:, idx - 1] + dh10 * d[:, idx - 1] + dh01 * v[:, idx] + dh11 * d[:, idx]
        return out

def fields(itp, X):
    x, y = X[:, 0], X[:, 1]
    r = torch.sqrt(x * x + y * y); th = torch.atan2(y, x)
    pr = itp(r)
    Th = torch.zeros_like(r); Thr = torch.zeros_like(r); Thth_r = torch.zeros_like(r)
    for n in range(NT):
        m = 2 * n + 1
        Th += pr['f'][n] * torch.sin(m * th); Thr += pr['df'][n] * torch.sin(m * th); Thth_r += m * pr['f'][n] / r * torch.cos(m * th)
    Om = torch.zeros_like(r); Psir = torch.zeros_like(r); Psith_r = torch.zeros_like(r)
    for n in range(1, NO + 1):
        m = 2 * n
        Om += pr['g'][n - 1] * torch.sin(m * th)
        Psir += pr['dpsi'][n - 1] * torch.sin(m * th); Psith_r += m * pr['psi'][n - 1] / r * torch.cos(m * th)
    cs, sn = torch.cos(th), torch.sin(th)
    Thx = cs * Thr - sn * Thth_r
    U1 = -(sn * Psir + cs * Psith_r); U2 = cs * Psir - sn * Psith_r
    W = torch.stack([beta * x + U1, beta * y + U2], 1)
    return dict(Th=Th, Thx=Thx, Om=Om, W=W)

def run(Nfine):
    itp = Interp(Nfine)
    # sample points: log-spaced radii, interior angles
    rs = torch.logspace(-2, math.log10(args.rmax), 25, dtype=DT, device=device)
    ths = (torch.arange(12, dtype=DT, device=device) + 0.5) / 12 * (math.pi / 2)
    R, TH = torch.meshgrid(rs, ths, indexing='ij'); R = R.reshape(-1); TH = TH.reshape(-1)
    X0 = torch.stack([R * torch.cos(TH), R * torch.sin(TH)], 1)
    F0 = fields(itp, X0)
    X = X0.clone(); s = torch.zeros(X.shape[0], dtype=DT, device=device)
    active = torch.ones(X.shape[0], dtype=torch.bool, device=device)
    # forward-form Omega integral accumulated backward: I = int_0^s e^{-(s-sig)} Theta_x dsig ; backward variable tau = s - sig
    # Omega_char(X0) = e^{-s} Om(X_end) + int_0^s e^{-tau} Theta_x(X(tau)) dtau where X(tau) is the backward path (tau = 0 at X0)
    I = torch.zeros_like(s)
    ds = args.ds
    for it in range(200000):
        if not active.any(): break
        Xa = X[active]
        def rhs(Xc): return -fields(itp, Xc)['W']
        k1 = rhs(Xa); k2 = rhs(Xa + 0.5 * ds * k1); k3 = rhs(Xa + 0.5 * ds * k2); k4 = rhs(Xa + ds * k3)
        Xn = Xa + ds / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        # Simpson for the Omega integral on [tau, tau+ds]
        ta = s[active]
        thx_a = fields(itp, Xa)['Thx']; thx_m = fields(itp, Xa + 0.5 * ds * k1)['Thx']; thx_b = fields(itp, Xn)['Thx']
        I[active] = I[active] + ds / 6 * (torch.exp(-ta) * thx_a + 4 * torch.exp(-(ta + 0.5 * ds)) * thx_m + torch.exp(-(ta + ds)) * thx_b)
        X[active] = Xn; s[active] = ta + ds
        rn = torch.sqrt((Xn ** 2).sum(1))
        done = rn < args.eps
        idx = torch.nonzero(active)[:, 0]
        active[idx[done]] = False
        if (s > 400).any():
            active[s > 400] = False
    Fe = fields(itp, X)
    Th_char = torch.exp((beta - 2) * s) * Fe['Th']
    Om_char = torch.exp(-s) * Fe['Om'] + I
    return dict(R=R, TH=TH, s=s, Th0=F0['Th'], Th_char=Th_char, Om0=F0['Om'], Om_char=Om_char, Xend=X)

out = run(args.Nfine); out2 = run(args.Nfine // 2)
relT = ((out['Th_char'] - out['Th0']).abs() / out['Th0'].abs())
Omscale = out['Om0'].abs().reshape(25, 12).max(1, keepdim=True).values.expand(25, 12).reshape(-1)
relO = ((out['Om_char'] - out['Om0']).abs() / (out['Om0'].abs() + 0.1 * Omscale))
interpT = ((out['Th_char'] - out2['Th_char']).abs() / out['Th0'].abs()).max().item()
interpO = ((out['Om_char'] - out2['Om_char']).abs() / (out['Om0'].abs() + 0.1 * Omscale)).max().item()
print('max s (backward time to reach eps):', out['s'].max().item(), ' points not reaching eps:', int((torch.sqrt((out['Xend'] ** 2).sum(1)) >= args.eps).sum()))
print('interpolation sensitivity (Nfine vs Nfine/2): Theta %.2e  Omega %.2e' % (interpT, interpO))
R = out['R'].cpu().numpy(); TH = out['TH'].cpu().numpy(); relT = relT.cpu().numpy(); relO = relO.cpu().numpy()
print('relative |Theta_char - Theta| by radius (max over angles), and same for Omega:')
rows = []
for rv in np.unique(R):
    m = R == rv
    rows.append((float(rv), float(relT[m].max()), float(TH[m][relT[m].argmax()] * 180 / math.pi), float(relO[m].max()), float(TH[m][relO[m].argmax()] * 180 / math.pi)))
    print('   r=%9.4g  Theta: %.3e (at %5.1f deg)   Omega: %.3e (at %5.1f deg)' % rows[-1])
if args.json:
    json.dump(dict(file=args.npz, beta=beta, rows=rows, interpT=interpT, interpO=interpO), open(args.json, 'w'), indent=1)
