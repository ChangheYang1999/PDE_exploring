"""Independent cross-check of the lead's forced homotopy (lead explore/dynhom.py), with the verifier's own
marching map (code/charsolve.py) and Newton-GMRES instead of dynamic rescaling.
Forced profile system (lead, notes 19:07Z item 2):
    V_h = c_l X + h W[rho] + (1-h) E,   E = (-d_y psi_E, d_x psi_E),  psi_E = mu x y exp(-r^2/LE^2)  (E = mu(-x, y) near 0),
    jet x^2:  total strain at 0 is [[-C, -B], [-B, C]] with C = h c[rho] + (1-h) mu, B = h b[rho]; c_l = 1/2 + sqrt(C^2 + B^2)
    (= 1/2 + h c + (1-h) mu when B = 0 and C > 0), jet direction = slow eigenvector.
h = 0: T does not depend on xi (linear transport by c_l X + E). Natural continuation in h with Newton at each h.
Forced moment law at a fixed point (from div(rho phi V_h), phi = r^-3 sin 3th):
    (c_l - 1) pi c = h Q[rho] + (1-h) Q_E,   Q = int rho W.grad phi,  Q_E = int rho E.grad phi.
Logs JSON lines to runs/NAME.log, saves runs/NAME_h{h}.pt."""
import numpy as np, torch, sys, json, time, argparse, math
sys.path.insert(0, 'code')
from charsolve import CharSolver
import torch.autograd.forward_ad as fwAD


class ForcedSolver(CharSolver):
    def set_forcing(self, h, mu, LE):
        self.h, self.mu, self.LE = float(h), float(mu), float(LE)
        X, Y = self.X, self.Y
        chi = torch.exp(-(X**2 + Y**2)/LE**2)
        self.E1 = -mu*X*chi*(1 - 2*Y**2/LE**2)
        self.E2 = mu*Y*chi*(1 - 2*X**2/LE**2)

    def T(self, xi, info=False):
        h, mu = self.h, self.mu
        rho = xi**2
        if getattr(self, 'exact_p', True):          # exact scalar solve of p = 1/c_l(p) (charsolve.solve_p)
            c, b, cl, l, p, self.last_dp = self.solve_p(rho, h, mu, getattr(self, 'p_start', 0.5))
        else:                                        # old fixed-count loop (inconsistent near p -> 1; kept for reference)
            p = getattr(self, 'p_start', 0.5)
            for _ in range(getattr(self, 'np_iter', 3)):
                c, b = self.moments(rho, p)
                cl, l = self.jet(h*c + (1 - h)*mu, h*b)
                p_old, p = p, torch.clamp(1.0/cl, max=0.999)
            self.last_dp = abs(float(p) - float(p_old))
        W1, W2 = self.velocity(rho, p)
        W1 = h*W1 + (1 - h)*self.E1
        W2 = h*W2 + (1 - h)*self.E2
        Vr = cl*self.R + W1*self.cs + W2*self.sn
        Vt_r = (-W1*self.sn + W2*self.cs)/self.R
        z0 = self.r1*(l[0]*torch.cos(self.th) + l[1]*torch.sin(self.th))
        q, p0 = self.q, self.p0
        new = torch.cat([l[0]*self.X[:p0*q] + l[1]*self.Y[:p0*q], self.march(Vr, Vt_r, z0)], 0)
        if info:
            d = dict(c=float(c), b=float(b), cl=float(cl), l=(float(l[0]), float(l[1])), p=float(p), dp=self.last_dp,
                     minVr_r=float((Vr[p0*q:]/self.R[p0*q:]).min()))
            return new, d
        return new

    def qlaw(self, xi, d):
        """returns (c_l - 1) pi c, h Q + (1-h) Q_E."""
        rho = xi**2
        W1, W2 = self.velocity(rho, d['p'])
        g1 = 3*self.R**-4*(-torch.sin(3*self.TH)*self.cs - torch.cos(3*self.TH)*self.sn)   # grad phi, cartesian
        g2 = 3*self.R**-4*(-torch.sin(3*self.TH)*self.sn + torch.cos(3*self.TH)*self.cs)
        wq = self.w[:, None]*self.r[:, None]*(2*math.pi/self.nt)
        Q = float(torch.sum(wq*rho*(W1*g1 + W2*g2)))
        QE = float(torch.sum(wq*rho*(self.E1*g1 + self.E2*g2)))
        return (d['cl'] - 1)*math.pi*d['c'], self.h*Q + (1 - self.h)*QE, Q, QE


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


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--name', required=True)
    ap.add_argument('--q', type=int, default=8)
    ap.add_argument('--nt', type=int, default=64)
    ap.add_argument('--r1', type=float, default=1e-6)
    ap.add_argument('--L', type=float, default=1e4)
    ap.add_argument('--ncore', type=int, default=24)
    ap.add_argument('--mu', type=float, default=1.0)
    ap.add_argument('--LE', type=float, default=2.0)
    ap.add_argument('--hs', default='0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0')
    ap.add_argument('--maxit', type=int, default=25)
    ap.add_argument('--kmax', type=int, default=80)
    ap.add_argument('--gtol', type=float, default=1e-8)
    ap.add_argument('--ftol', type=float, default=1e-9)
    ap.add_argument('--vrmin', type=float, default=0.02)
    ap.add_argument('--clmin', type=float, default=1.0005)
    ap.add_argument('--npit', type=int, default=8)
    ap.add_argument('--exactp', type=int, default=1)
    args = ap.parse_args()
    dev = 'cuda'
    edges = np.concatenate([[0.0], np.geomspace(args.r1, 0.1, 12), np.geomspace(0.1, 10, args.ncore + 1)[1:],
                            np.geomspace(10, args.L, int(round(np.log10(args.L/10)*5)) + 1)[1:]])
    S = ForcedSolver(edges, args.q, args.nt, args.r1, dev)
    R = S.R; rr = (1 + R**2)**0.5
    LOG = open(f'runs/{args.name}.log', 'w')
    def log(d):
        LOG.write(json.dumps(d) + '\n'); LOG.flush(); print(json.dumps(d), flush=True)
    log(dict(start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), args=vars(args), Nr=S.Nr, nt=S.nt))
    nt = S.nt
    idx = (nt//2 - torch.arange(nt, device=dev)) % nt
    t0 = time.time()
    xi = None
    for hs in args.hs.split(','):
        h = float(hs)
        S.set_forcing(h, args.mu, args.LE)
        S.np_iter = args.npit; S.exact_p = bool(args.exactp)
        if xi is not None: S.p_start = d['p']    # previous converged far-field exponent
        if xi is None:
            xi, d = S.T(S.X, info=True)            # h = 0 (or any h): first iterate from xi = x
        wsc = R/rr*rr**(0.5*min(1.0, 1.0/max(d['cl'], 1.0)))
        v = xi/wsc
        def evalF(v):
            z = v*wsc
            new, dd = S.T(z, info=True)
            F = (z - new)/wsc
            ok = bool(torch.isfinite(F).all()) and dd['minVr_r'] > args.vrmin and dd['cl'] > args.clmin and dd['dp'] < 1e-9
            return F, dd, ok
        F, d, ok = evalF(v)
        conv = False
        for it in range(args.maxit):
            fn = float(F.norm())
            if float(F.abs().max()) < args.ftol: conv = True; break
            def Av(u):
                with fwAD.dual_level():
                    zd = fwAD.make_dual(v*wsc, u*wsc)
                    tz = fwAD.unpack_dual(S.T(zd)).tangent
                return u - tz/wsc
            dv, gres, kk = gmres(Av, -F, args.kmax, args.gtol)
            lam = 1.0; acc = False
            while lam > 1e-4:
                Ft, dt_, okt = evalF(v + lam*dv)
                if okt and float(Ft.norm()) < (1 - 1e-4*lam)*fn: acc = True; break
                lam *= 0.5
            if not acc:
                log(dict(h=h, it=it, msg='line search failed', F2=fn, **d)); break
            v, F, d = v + lam*dv, Ft, dt_
            log(dict(h=h, it=it, lam=lam, gres=gres, kry=kk, F2=float(F.norm()), Finf=float(F.abs().max()),
                     c=d['c'], b=d['b'], cl=d['cl'], minVr_r=d['minVr_r'], wall=time.time() - t0))
        xi = v*wsc
        lhs, rhs, Q, QE = S.qlaw(xi, d)
        xo = 0.5*(xi + xi[:, idx])
        out = dict(h=h, summary=True, conv=conv, **d, Finf=float(F.abs().max()), qlaw_lhs=lhs, qlaw_rhs=rhs, Q=Q, QE=QE,
                   xodd_frac=float((xo/wsc).abs().max()/((xi/wsc).abs().max())), wall=time.time() - t0)
        log(out)
        torch.save(dict(xi=xi.cpu(), edges=edges, q=args.q, nt=args.nt, r1=args.r1, args=vars(args), d=d, h=h),
                   f'runs/{args.name}_h{h:.3f}.pt')
        if not conv:
            log(dict(msg='not converged at this h; stop', h=h)); break
    log(dict(end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), wall=time.time() - t0))
