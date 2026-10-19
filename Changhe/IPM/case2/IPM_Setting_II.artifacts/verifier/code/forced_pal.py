"""Pseudo-arclength continuation in h of the lead's forced profile system (see code/forced_char.py), with the far-field
exponent p as an explicit unknown, so that folds of the scalar condition p = 1/c_l are passed smoothly.
Unknowns Z = (v, p, h), z = v wsc = xi on the grid; equations
    F(Z) = (z - T(z; p, h))/wsc = 0,   g(Z) = c_l(z; p, h) p - 1 = 0,
where T(z; p, h) is the marching map with tail exponent p in both the moment functionals (c, b) and W, and
c_l = 1/2 + sqrt(C^2 + B^2), C = h c + (1-h) mu, B = h b. Metric <dZ, dZ> = |dv|^2/nv + dp^2 + dh^2 (nv = v.numel()).
Keller corrector with the hyperplane <t, Z - Z_pred> = 0; every Jacobian-vector product (including d/dp and d/dh) is
exact forward-mode AD through T; GMRES (own) on the bordered (nv + 2)-square system.
Admissibility: T finite, min V_r/r > vrmin on r >= r1, c_l > clmin, 0 < p < pmax.
Start: a converged state runs/NAME_h*.pt of code/forced_char.py (--load). Logs JSON lines to runs/NAME.log."""
import numpy as np, torch, sys, json, time, argparse, math
sys.path.insert(0, 'code')
from forced_char import ForcedSolver, gmres
import torch.autograd.forward_ad as fwAD


class ExtSolver(ForcedSolver):
    def Tp(self, xi, p, h, info=False):
        mu = self.mu
        rho = xi**2
        c, b = self.moments(rho, p)
        cl, l = self.jet(h*c + (1 - h)*mu, h*b)
        W1, W2 = self.velocity(rho, p)
        W1 = h*W1 + (1 - h)*self.E1
        W2 = h*W2 + (1 - h)*self.E2
        Vr = cl*self.R + W1*self.cs + W2*self.sn
        Vt_r = (-W1*self.sn + W2*self.cs)/self.R
        z0 = self.r1*(l[0]*torch.cos(self.th) + l[1]*torch.sin(self.th))
        q, p0 = self.q, self.p0
        new = torch.cat([l[0]*self.X[:p0*q] + l[1]*self.Y[:p0*q], self.march(Vr, Vt_r, z0)], 0)
        g = cl*p - 1
        if info:
            d = dict(c=float(c), b=float(b), cl=float(cl), l=(float(l[0]), float(l[1])), p=float(p), h=float(h),
                     minVr_r=float((Vr[p0*q:]/self.R[p0*q:]).min()))
            return new, g, d
        return new, g


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--name', required=True)
    ap.add_argument('--load', required=True)
    ap.add_argument('--ds', type=float, default=0.01)
    ap.add_argument('--dsmax', type=float, default=0.05)
    ap.add_argument('--dsmin', type=float, default=1e-6)
    ap.add_argument('--steps', type=int, default=400)
    ap.add_argument('--kmax', type=int, default=100)
    ap.add_argument('--gtol', type=float, default=1e-9)
    ap.add_argument('--ctol', type=float, default=1e-9)
    ap.add_argument('--vrmin', type=float, default=0.02)
    ap.add_argument('--clmin', type=float, default=1.0005)
    ap.add_argument('--pmax', type=float, default=0.999)
    ap.add_argument('--dir', type=float, default=1.0)       # initial direction: sign of dh
    ap.add_argument('--maxwall', type=float, default=3000)
    ap.add_argument('--nt_new', type=int, default=0)       # resample the loaded state to this nt (Fourier zero-padding)
    ap.add_argument('--hfix_it', type=int, default=12)     # Newton iterations at fixed h after resampling
    args = ap.parse_args()
    dev = 'cuda'
    D0 = torch.load(args.load, weights_only=False)
    A0 = D0['args']; edges = D0['edges']
    nt_use = args.nt_new if args.nt_new else D0['nt']
    if args.nt_new and args.nt_new != D0['nt']:
        xr = torch.fft.rfft(D0['xi'].to(torch.float64), dim=1)
        D0['xi'] = torch.fft.irfft(xr, n=args.nt_new, dim=1)*(args.nt_new/D0['nt'])
        D0['nt'] = args.nt_new
    S = ExtSolver(edges, D0['q'], nt_use, D0['r1'], dev)
    S.set_forcing(0.0, A0['mu'], A0['LE'])                  # E arrays (mu, LE); h enters Tp explicitly
    R = S.R; rr = (1 + R**2)**0.5
    p_ref = 1.0/max(D0['d']['cl'], 1.0)
    wsc = R/rr*rr**(0.5*min(1.0, p_ref))
    LOG = open(f'runs/{args.name}.log', 'w')
    def log(d):
        LOG.write(json.dumps(d) + '\n'); LOG.flush(); print(json.dumps(d), flush=True)
    log(dict(start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), args=vars(args), load_args=A0, Nr=S.Nr, nt=S.nt))
    shp = D0['xi'].shape; nv = D0['xi'].numel()
    T_ = lambda a: torch.tensor(a, dtype=torch.float64, device=dev)

    def split(Z):
        return Z[:nv].reshape(shp), Z[nv], Z[nv + 1]

    def resid(Z, info=False):
        v, p, h = split(Z)
        z = v*wsc
        out = S.Tp(z, p, h, info=info)
        F = ((z - out[0])/wsc).flatten()
        r = torch.cat([F, out[1].reshape(1)])
        return (r, out[2]) if info else r

    def jvp(Z, dZ):
        with fwAD.dual_level():
            Zd = fwAD.make_dual(Z, dZ)
            r = resid(Zd)
            return fwAD.unpack_dual(r).tangent

    def inner(a, b):        # metric <a, b> = <a_v, b_v>/nv + a_p b_p + a_h b_h
        return float(torch.dot(a[:nv], b[:nv]))/nv + float(a[nv]*b[nv] + a[nv + 1]*b[nv + 1])

    def Mvec(t):            # vector m with dot(m, dZ) = <t, dZ>
        m = t.clone(); m[:nv] = m[:nv]/nv; return m

    def admissible(Z):
        r, d = resid(Z, info=True)
        ok = bool(torch.isfinite(r).all()) and d['minVr_r'] > args.vrmin and d['cl'] > args.clmin and 0 < d['p'] < args.pmax
        return r, d, ok

    def solve_bordered(Z, m, rhs_top, rhs_last):
        """solve [J(Z); m^T] x = [rhs_top; rhs_last] by GMRES on the (nv + 2) system."""
        def A(x):
            return torch.cat([jvp(Z, x), torch.dot(m, x).reshape(1)])
        b = torch.cat([rhs_top, torch.as_tensor(rhs_last, dtype=torch.float64, device=dev).reshape(1)])
        x, gr, kk = gmres(A, b, args.kmax, args.gtol)
        return x, gr, kk

    t0 = time.time()
    Z = torch.cat([(D0['xi'].to(dev)/wsc).flatten(), T_([D0['d']['p'], D0['h']])])
    r, d, ok = admissible(Z)
    log(dict(step=0, **d, res=float(r.abs().max()), ok=ok))
    if args.nt_new:                                        # Newton at fixed h: [J; e_h^T] dZ = [-r; 0]
        eh0 = torch.zeros(nv + 2, dtype=torch.float64, device=dev); eh0[nv + 1] = 1.0
        for it in range(args.hfix_it):
            if float(r.abs().max()) < args.ctol: break
            x, gr, kk = solve_bordered(Z, eh0, -r, 0.0)
            lam = 1.0
            while lam > 1e-3:
                rt, dt_, okt = admissible(Z + lam*x)
                if okt and float(rt.norm()) < float(r.norm()): break
                lam *= 0.5
            Z = Z + lam*x; r, d, ok = rt, dt_, okt
            log(dict(hfix_it=it, lam=lam, kry=kk, gres=gr, **d, res=float(r.abs().max()), ok=ok))
        if float(r.abs().max()) >= args.ctol: log(dict(msg='fixed-h Newton after resampling not converged')); sys.exit(0)
    # initial tangent: [J; e_h] t = [0; dir]
    eh = torch.zeros(nv + 2, dtype=torch.float64, device=dev); eh[nv + 1] = 1.0
    t, gr, kk = solve_bordered(Z, eh, torch.zeros(nv + 1, dtype=torch.float64, device=dev), args.dir)
    t = t/math.sqrt(inner(t, t))
    ds = args.ds
    for step in range(1, args.steps + 1):
        if time.time() - t0 > args.maxwall: log(dict(msg='maxwall')); break
        acc = False
        while ds > args.dsmin:
            Zp = Z + ds*t
            m = Mvec(t)
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
        # new tangent: [J(Zp); m_prev^T] tn = [0; 1]
        tn, gr2, kk2 = solve_bordered(Zp, Mvec(t), torch.zeros(nv + 1, dtype=torch.float64, device=dev), 1.0)
        tn = tn/math.sqrt(inner(tn, tn))
        if inner(tn, t) < 0: tn = -tn
        turned = float(tn[nv + 1])*float(t[nv + 1]) < 0
        Z, t, d = Zp, tn, dp
        v, p, h = split(Z)
        S.h = float(h)
        lhs, rhs, Q, QE = S.qlaw(v*wsc, d)
        log(dict(step=step, ds=ds, kc=kc, kry=kk, turned=turned, dh_ds=float(t[nv + 1]), dp_ds=float(t[nv]), **d,
                 res=rn, qlaw_lhs=lhs, qlaw_rhs=rhs, Q=Q, QE=QE, wall=time.time() - t0))
        if turned or step % 10 == 0:
            torch.save(dict(xi=(v*wsc).cpu(), edges=edges, q=D0['q'], nt=D0['nt'], r1=D0['r1'], args=A0, d=d, h=float(h)),
                       f'runs/{args.name}_s{step:04d}.pt')
        if float(h) >= 1.0 or float(h) <= 0.0:
            log(dict(msg='reached h boundary', h=float(h))); break
        if kc <= 2: ds = min(ds*1.5, args.dsmax)
    log(dict(end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), wall=time.time() - t0))
