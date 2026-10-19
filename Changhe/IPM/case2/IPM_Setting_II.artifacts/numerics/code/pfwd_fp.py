"""Fixed-point Newton for Setting II profiles via the forward evolution (notes of the lead analyst 2026-10-17T23:55Z, specification M23(b)), GPU version.

Unknowns: a = (a_1..a_N) in the x-even datum A(th) = cos^2 th exp(sum_j a_j phi_j(th)), phi = sin th, cos 2th, sin 3th, cos 4th, ...
          and p (c_l = 1/p).
Residual: F_0 = m1 - 1/2 (weak node eigenvalue from the moment, m1 = c_l - psi_xy(0), x-even states);
          F_j = weighted projection of log Gt(th) - mean on phi_j, j = 1..N, where Gt is the lead's orbit invariant
                log Gt(th) = log A(th) - 2 log|u0(th)| - 2 m1 T(th)   (+ const),
          obtained by tracing the backward orbit (dX/dt = -V) from (r_max, th) to the inner ring r_0 = e^{lr0}: X0 = arrival point,
          u0 = X0 . e1 (weak eigenvector), T = travel time.  Gt constant (and m1 = 1/2) means rho = Gt xi^2 with xi the slow coordinate:
          a C^2 node with the Setting II jet (after the scaling normalisation).  Gt varies across the weak-axis layer otherwise.
Each residual evaluation = one steady state of the forward evolution (warm start) + the tracer.
"""
import sys, json, math, time
import numpy as np, torch
sys.path.insert(0, 'code')
from pfwd import PFwd, datum
torch.set_default_dtype(torch.float64)


BUMPS = dict(Nf=None, sigma_deg=8.0)        # if Nf is set, basis index j >= Nf are x-even bumps: j = Nf -> at 90 deg, Nf+1 -> at 270 deg,
                                            # Nf+2 -> cos-modulated bump at 90, Nf+3 -> at 270 (second shape), ...


def basis(th, j):
    Nf = BUMPS['Nf']
    if Nf is not None and j >= Nf:
        k = j - Nf; centre = math.pi / 2 if k % 2 == 0 else 3 * math.pi / 2
        sig = math.radians(BUMPS['sigma_deg']) * (1.0 if k < 2 else 2.0)
        dth = torch.remainder(th - centre + math.pi, 2 * math.pi) - math.pi
        return torch.exp(-0.5 * (dth / sig) ** 2)
    n = j + 1
    return torch.sin(n * th) if n % 2 == 1 else torch.cos(n * th)


class FixedPoint:
    def __init__(self, p, N, Nr=661, Nth=256, lo=-12.0, hi=10.0, ds=0.02, nsteps=700, lr0=-9.0, nA=512, dt=0.02, dev='cuda', log=None, wmode='A'):
        self.wmode = wmode
        self.p, self.N, self.Nr, self.Nth, self.lo, self.hi, self.ds, self.nsteps, self.lr0, self.nA, self.dt = p, N, Nr, Nth, lo, hi, ds, nsteps, lr0, nA, dt
        self.dev = dev
        self.S = PFwd(Nr, Nth, lo, hi, p, dev=dev)
        self.g = None; self.A_old = None; self.p_old = p
        self.log = log
        self.thA = torch.arange(nA, device=dev, dtype=torch.float64) * (2 * math.pi / nA)

    def Afun(self, a):
        def f(th):
            s = torch.zeros_like(th)
            for j in range(len(a)):
                s = s + float(a[j]) * basis(th, j)
            return torch.cos(th) ** 2 * torch.exp(s)
        return f

    def steady(self, a, p):
        S = self.S
        if abs(p - S.p) > 1e-15:
            S.p = float(p); S.cl = 1.0 / p; S._build_kernels()
        Af = self.Afun(a); A = Af(S.th)
        if self.g is None:
            g = ((S.r ** 2 / (1.0 + S.r ** 2)) ** (1.0 - p / 2))[:, None] * A[None, :]
        else:
            fac = (S.r[:, None] / S.r[-1]) ** (self.p_old - p)
            g = self.g * fac * (A[None, :] / torch.clamp(self.A_old[None, :], min=1e-12))
            g = torch.where(self.A_old[None, :] > 1e-6, g, ((S.r[:, None] ** 2 / (1 + S.r[:, None] ** 2)) ** (1 - p / 2)) * A[None, :])
        for n in range(self.nsteps):
            gn, (Wr, Wt) = S.step(g, self.ds, A, Af)
            if n == self.nsteps - 1:
                dg = float((gn - g).abs().max()) / self.ds
            g = gn
        ok = math.isfinite(dg) and dg < 1e-3
        if ok:
            self.g = g; self.A_old = A; self.p_old = p
        d = S.diagnostics(g, Wr, Wt, krings=(20,))
        return g, Wr, Wt, d, dg, ok

    def trace(self, Wr, Wt, e1):
        """Backward orbits dX/dt = -V from (r_max, thA) to lr0.  Returns T (travel time), u0 = X0.e1, w0 = X0.e2, th0."""
        S = self.S
        ar = S.cl + Wr / S.r[:, None]; at = Wt / S.r[:, None]
        top = lambda F: F[-1:].expand(2, -1)
        def rhs(lr, th):
            ci = (lr - S.lo) / S.d; cj = th / S.dth - S.thshift
            return -S.interp(ar, ci, cj, top(ar)), -S.interp(at, ci, cj, top(at))
        lr = torch.full((self.nA,), S.hi - 1e-9, device=self.dev); th = self.thA.clone()
        T = torch.zeros(self.nA, device=self.dev); live = torch.ones(self.nA, dtype=torch.bool, device=self.dev)
        lr_prev = lr.clone(); th_prev = th.clone()
        dt = self.dt; it = 0
        while bool(live.any()) and it < 200000:
            k1 = rhs(lr, th); k2 = rhs(lr + 0.5 * dt * k1[0], th + 0.5 * dt * k1[1])
            k3 = rhs(lr + 0.5 * dt * k2[0], th + 0.5 * dt * k2[1]); k4 = rhs(lr + dt * k3[0], th + dt * k3[1])
            lr_n = lr + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); th_n = th + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
            # orbits crossing lr0 in this step: linear interpolation of the crossing (time and angle)
            cross = live & (lr_n <= self.lr0)
            frac = torch.where(cross, (lr - self.lr0) / torch.clamp(lr - lr_n, min=1e-300), torch.zeros_like(lr))
            T = torch.where(live, T + dt * torch.where(cross, frac, torch.ones_like(frac)), T)
            th_c = th + frac * (th_n - th)
            lr = torch.where(live & ~cross, lr_n, torch.where(cross, torch.full_like(lr, self.lr0), lr))
            th = torch.where(live & ~cross, th_n, torch.where(cross, th_c, th))
            live = live & ~cross
            it += 1
        r0 = math.exp(self.lr0)
        X0 = torch.stack([r0 * torch.cos(th), r0 * torch.sin(th)], 1)
        e1t = torch.tensor(e1, device=self.dev, dtype=torch.float64); e2t = torch.tensor([-e1[1], e1[0]], device=self.dev, dtype=torch.float64)
        return T, X0 @ e1t, X0 @ e2t, th, it

    def trace_from(self, Wr, Wt, lr_start, th_start, e1, lr0=None, dt=None):
        """Backward orbits dX/dt = -V from arbitrary points (lr_start, th_start) to lr0.  Returns T, u0 = X0.e1, w0, th0."""
        S = self.S; lr0 = self.lr0 if lr0 is None else lr0; dt = self.dt if dt is None else dt
        ar = S.cl + Wr / S.r[:, None]; at = Wt / S.r[:, None]
        top = lambda F: F[-1:].expand(2, -1)
        def rhs(lr, th):
            ci = (lr - S.lo) / S.d; cj = th / S.dth - S.thshift
            return -S.interp(ar, ci, cj, top(ar)), -S.interp(at, ci, cj, top(at))
        lr = lr_start.clone(); th = th_start.clone()
        T = torch.zeros_like(lr); live = lr > lr0
        it = 0
        while bool(live.any()) and it < 400000:
            k1 = rhs(lr, th); k2 = rhs(lr + 0.5 * dt * k1[0], th + 0.5 * dt * k1[1])
            k3 = rhs(lr + 0.5 * dt * k2[0], th + 0.5 * dt * k2[1]); k4 = rhs(lr + dt * k3[0], th + dt * k3[1])
            lr_n = lr + dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); th_n = th + dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
            cross = live & (lr_n <= lr0)
            frac = torch.where(cross, (lr - lr0) / torch.clamp(lr - lr_n, min=1e-300), torch.zeros_like(lr))
            T = torch.where(live, T + dt * torch.where(cross, frac, torch.ones_like(frac)), T)
            th_c = th + frac * (th_n - th)
            lr = torch.where(live & ~cross, lr_n, torch.where(cross, torch.full_like(lr, lr0), lr))
            th = torch.where(live & ~cross, th_n, torch.where(cross, th_c, th))
            live = live & ~cross
            it += 1
        r0 = math.exp(lr0)
        X0 = torch.stack([r0 * torch.cos(th), r0 * torch.sin(th)], 1)
        e1t = torch.tensor(e1, device=self.dev, dtype=torch.float64); e2t = torch.tensor([-e1[1], e1[0]], device=self.dev, dtype=torch.float64)
        return T, X0 @ e1t, X0 @ e2t, th, it

    def residual(self, x, return_all=False):
        a = list(x[:-1]); p = float(x[-1])
        t0 = time.time()
        g, Wr, Wt, d, dg, ok = self.steady(a, p)
        Wr, Wt = self.S.velocity(self.S.r[:, None] ** p * g)          # velocity of the FINAL density (the step's velocity is one step stale)
        d = self.S.diagnostics(g, Wr, Wt, krings=(20,))
        cl = 1.0 / p
        m1 = cl - d['c_moment']
        if not ok:
            Fpen = np.full(self.N + 1, 10.0)
            rec = dict(x=[round(float(v), 6) for v in x], F='PENALTY (steady state not converged, dg/ds %.1e)' % dg, ok=False)
            line = json.dumps(rec); print(line, flush=True)
            if self.log: self.log.write(line + '\n'); self.log.flush()
            return (Fpen, None) if return_all else Fpen
        r20 = d['ring20']
        ang = math.radians(r20['e1_deg']); e1 = (math.cos(ang), math.sin(ang))
        T, u0, w0, th0, it = self.trace(Wr, Wt, e1)
        A = self.Afun(a)(self.thA)
        logGt = torch.log(torch.clamp(A, min=1e-300)) - 2 * torch.log(torch.clamp(u0.abs(), min=1e-300)) - 2 * m1 * T
        if self.wmode == 'A':
            w = A / A.max()                                    # weight: the datum itself (vanishes at the zeros of A where Gt is ill-conditioned)
        else:                                                  # 'flat': uniform weight, only the strong-axis traces (|cos th| < 0.02) excluded
            w = (torch.cos(self.thA).abs() > 0.02).double()
        mean = float((w * logGt).sum() / w.sum())
        dev_ = logGt - mean
        F = [m1 - 0.5]
        for j in range(self.N):
            phi = basis(self.thA, j)
            F.append(float((w * dev_ * phi).sum() / w.sum()))
        F = np.array(F)
        std = float(torch.sqrt((w * dev_ ** 2).sum() / w.sum()))
        gmax = float(dev_[w > 1e-2].max()); gmin = float(dev_[w > 1e-2].min())
        rec = dict(x=[round(float(v), 6) for v in x], F=[round(float(v), 6) for v in F], m1=round(m1, 6), m1_ring=r20['m1'], e1=r20['e1_deg'],
                   logGt_std=round(std, 5), logGt_range=[round(gmin, 4), round(gmax, 4)], dgds='%.1e' % dg, ok=ok, trace_steps=it, wall=round(time.time() - t0, 1))
        line = json.dumps(rec); print(line, flush=True)
        if self.log: self.log.write(line + '\n'); self.log.flush()
        if return_all:
            return F, dict(rec=rec, logGt=logGt.cpu().numpy(), thA=self.thA.cpu().numpy(), T=T.cpu().numpy(), u0=u0.cpu().numpy(), w0=w0.cpu().numpy(), th0=th0.cpu().numpy(), g=g, d=d)
        return F

    def newton(self, x0, maxit=12, h_a=0.02, h_p=0.01, tol=1e-4, save=None, mu0=1e-2, da_max=0.5, dp_max=0.1):
        """Damped Gauss-Newton (Levenberg-Marquardt scaling) with a finite-difference Jacobian; steps clipped (|da| <= 0.5, |dp| <= 0.1)."""
        x = np.array(x0, dtype=float); F = self.residual(x); mu = mu0
        for it in range(maxit):
            nF = np.abs(F).max()
            print("NEWTON it %d |F|_inf = %.3e |F|_2 = %.3e mu = %.1e x = %s" % (it, nF, np.linalg.norm(F), mu, np.round(x, 5).tolist()), flush=True)
            if save: np.savez(save, x=x, F=F)
            if nF < tol: break
            J = np.zeros((len(F), len(x)))
            base = (self.g.clone(), self.A_old.clone(), self.p_old)
            for j in range(len(x)):
                self.g, self.A_old, self.p_old = base[0].clone(), base[1].clone(), base[2]      # every column starts from the base state
                xp = x.copy(); hh = h_p if j == len(x) - 1 else h_a; xp[j] += hh
                J[:, j] = (self.residual(xp) - F) / hh
            self.g, self.A_old, self.p_old = base[0].clone(), base[1].clone(), base[2]
            sv = np.linalg.svd(J, compute_uv=False)
            print("NEWTON   singular values of J: %s" % np.round(sv, 5).tolist(), flush=True)
            JTJ = J.T @ J; D = np.diag(np.maximum(np.diag(JTJ), 1e-12 * np.diag(JTJ).max()))
            accepted = False
            for attempt in range(6):
                dx = -np.linalg.solve(JTJ + mu * D, J.T @ F)
                sc = max(1.0, np.abs(dx[:-1]).max() / da_max, abs(dx[-1]) / dp_max)
                dx = dx / sc
                xn = x + dx
                if xn[-1] <= 0.05 or xn[-1] >= 0.95:
                    mu *= 10; continue
                Fn = self.residual(xn)
                if np.linalg.norm(Fn) < np.linalg.norm(F):
                    x, F = xn, Fn; mu = max(mu / 3, 1e-6); accepted = True; break
                mu *= 10
            if not accepted:
                print("NEWTON   no decrease after 6 damped attempts; stopping", flush=True); break
        return x, F


if __name__ == '__main__':
    # usage: python3 code/pfwd_fp.py N tag p a1,a2,...,aN [maxit=12] [nsteps=700] [Nth=256]
    N = int(sys.argv[1]); tag = sys.argv[2]; p0 = float(sys.argv[3]); a0 = [float(v) for v in sys.argv[4].split(',')]
    opt = dict(maxit=12, nsteps=700, Nth=256, Nr=661, dp_max=0.1, da_max=0.5, mu0=1e-2, h_a=0.02, wmode='A', Nf=0, sigma_deg=8.0)
    for s_ in sys.argv[5:]:
        k, v = s_.split('='); opt[k] = v if k == 'wmode' else (int(v) if k in ('maxit', 'nsteps', 'Nth', 'Nr', 'Nf') else float(v))
    if opt['Nf'] > 0:
        BUMPS['Nf'] = opt['Nf']; BUMPS['sigma_deg'] = opt['sigma_deg']
    assert len(a0) == N
    log = open('runs/pfwd/fp_%s.log' % tag, 'a')
    FP = FixedPoint(p0, N, Nr=opt['Nr'], Nth=opt['Nth'], nsteps=opt['nsteps'], log=log, wmode=opt['wmode'])
    x, F = FP.newton(a0 + [p0], maxit=opt['maxit'], save='runs/pfwd/fp_%s_x.npz' % tag, mu0=opt['mu0'], da_max=opt['da_max'], dp_max=opt['dp_max'], h_a=opt['h_a'])
    Fall, info = FP.residual(x, return_all=True)
    np.savez('runs/pfwd/fp_%s_state.npz' % tag, g=info['g'].cpu().numpy(), lr=FP.S.lr.cpu().numpy(), th=FP.S.th.cpu().numpy(),
             hist=json.dumps([info['rec']]), args=json.dumps(dict(p=float(x[-1]), kind='expf', par=[float(v) for v in x[:-1]], N=N)),
             logGt=info['logGt'], thA=info['thA'], T=info['T'], u0=info['u0'])
    print("FP_RESULT", json.dumps(dict(tag=tag, N=N, x=x.tolist(), F=Fall.tolist(), rec=info['rec'])), flush=True)
