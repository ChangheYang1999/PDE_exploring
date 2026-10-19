"""Batched GPU forward self-similar IPM evolution: B states (own datum and own p each) on one grid, evolved together.
Same discretisation as code/pfwd.py (semi-Lagrangian RK2 feet, periodic cubic Lagrange interpolation, bilinear-hull limiter,
per-mode Green kernels with exact exponential product integration, one-term r^{p-1} tail with a per-state tail correction when
p differs from the kernel's p).  Purpose: finite-difference Jacobians of the fixed-point residual in ONE batched evolution.
Validated against PFwd (tests/pfwd_batch_check.py): identical to roundoff for equal p; tail correction tested at p +- 0.01.
"""
import math, time
import numpy as np
import torch
import sys
sys.path.insert(0, 'code')
from pfwd import PFwd, fd_dlr
torch.set_default_dtype(torch.float64)


class PFwdB:
    def __init__(self, Nr, Nth, lo, hi, p_kernel, dev='cuda', limiter=True, bspline=True, pad=12):
        self.S = PFwd(Nr, Nth, lo, hi, p_kernel, dev=dev, limiter=limiter)
        S = self.S
        self.bspline = bool(bspline); self.pad = int(pad)
        # cubic B-spline prefilter along lr on the extended axis [pad rows of row 0 | g rows 0..Nr-1 | 2 inflow rows | pad rows of inflow]
        Next = Nr + 2 + 2 * self.pad; self.Next = Next
        T = np.zeros((Next, Next)); idx = np.arange(Next)
        T[idx, idx] = 4.0 / 6; T[idx[:-1], idx[:-1] + 1] = 1.0 / 6; T[idx[1:], idx[1:] - 1] = 1.0 / 6
        self.Minv = torch.tensor(np.linalg.inv(T), device=dev)
        k = torch.arange(Nth // 2 + 1, device=dev, dtype=torch.float64)
        self.lam_th = (4.0 + 2.0 * torch.cos(2 * math.pi * k / Nth)) / 6.0            # periodic prefilter symbol in theta
        self.dev = S.dev; self.Nr, self.Nth, self.lo, self.hi, self.d, self.dth = Nr, Nth, S.lo, S.hi, S.d, S.dth
        self.lr, self.r, self.th, self.cos, self.sin, self.m, self.Mm = S.lr, S.r, S.th, S.cos, S.sin, S.m, S.Mm
        self.pk = float(p_kernel)
        self.limiter = limiter
        self.ii = S.ii[None]                   # [1, Nr, 1]
        self.jj = S.jj[None]                   # [1, 1, Nth]
        # decay factors for the tail correction: e^{-|m| (hi - lr)}
        self.decay = torch.exp(-self.m[:, None] * (self.hi - self.lr)[None, :])      # [Mm, Nr]

    # ------------------------------------------------------------------------------------------------------------
    def dx_rho(self, rho):                     # rho [B, Nr, Nth]
        rho_r = fd_dlr(rho.permute(1, 0, 2), self.d).permute(1, 0, 2) / self.r[None, :, None]
        F = torch.fft.rfft(rho, dim=2)
        k = torch.arange(self.Nth // 2 + 1, device=self.dev, dtype=torch.float64)
        F = F * (1j * k)[None, None, :]; F[..., -1] = 0.0
        rho_t = torch.fft.irfft(F, n=self.Nth, dim=2) / self.r[None, :, None]
        return self.cos[None, None, :] * rho_r - self.sin[None, None, :] * rho_t

    def velocity(self, rho, p):
        """rho [B, Nr, Nth], p [B] -> W_r, W_th [B, Nr, Nth]."""
        S = self.S; B = rho.shape[0]
        f = self.dx_rho(rho)
        F = torch.fft.rfft(f, dim=2)[..., :self.Mm] / self.Nth          # [B, Nr, Mm]
        F = F.permute(2, 1, 0).contiguous()                              # [Mm, Nr, B]
        e2 = torch.exp(2 * self.lr)
        h = F * e2[None, :, None]
        def mm(K, v):
            return torch.matmul(K, v.real) + 1j * torch.matmul(K, v.imag)
        Al = mm(S.Kin, h)
        Ag = mm(S.Kout, h)
        # per-state tail correction (one-term tail h_last/(|m| - 1 - p) built into Kout at p_kernel)
        a = self.m
        big = (a >= 2)
        dp = p - self.pk                                                   # [B]
        if bool((dp.abs() > 1e-15).any()):
            h0 = h[:, -1, :]                                               # [Mm, B]
            c_k = torch.where(big, 1.0 / torch.clamp(a - 1.0 - self.pk, min=1e-12), torch.zeros_like(a))[:, None]
            c_p = torch.where(big[:, None], 1.0 / torch.clamp(a[:, None] - 1.0 - p[None, :], min=1e-12), torch.zeros_like(h0.real))
            Ag = Ag + self.decay[:, :, None] * (h0 * (c_p - c_k))[:, None, :]
        hq = F[1] * self.r[:, None]                                        # [Nr, B]
        I1 = (S.K1 @ hq.real) + 1j * (S.K1 @ hq.imag)
        Ag = Ag.clone(); Ag[1] = -self.r[:, None] * I1
        mpos = self.m.clone(); mpos[0] = 1.0
        psi = (Al + Ag) / (2.0 * mpos[:, None, None])
        dpsi = (-Al + Ag) / (2.0 * self.r[None, :, None])
        Wr = -1j * self.m[:, None, None] * psi / self.r[None, :, None]
        Wt = dpsi.clone()
        Wr[0] = 0.0
        Wt[0] = -Al[0] / self.r[:, None]
        def to_phys(cm):                                                   # [Mm, Nr, B] -> [B, Nr, Nth]
            full = torch.zeros(B, self.Nr, self.Nth // 2 + 1, dtype=torch.complex128, device=self.dev)
            full[:, :, :self.Mm] = cm.permute(2, 1, 0)
            return torch.fft.irfft(full, n=self.Nth, dim=2) * self.Nth
        return to_phys(Wr), to_phys(Wt)

    # ------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------------- cubic B-spline interpolation (lead recipe, notes 06:47Z)
    def extend(self, F, top_rows):
        """[B, Nr, Nth] -> extended [B, Next, Nth]: pad rows of row 0, the field, two inflow rows, pad rows of the last inflow row."""
        P = self.pad
        return torch.cat([F[:, :1].expand(-1, P, -1), F, top_rows, top_rows[:, -1:].expand(-1, P, -1)], 1)

    def prefilter(self, Fext):
        """B-spline coefficients c with (c[i-1] + 4 c[i] + c[i+1])/6 = F[i] in both directions (FFT in theta, dense inverse in lr)."""
        Fh = torch.fft.rfft(Fext, dim=2) / self.lam_th[None, None, :]
        Ft = torch.fft.irfft(Fh, n=self.Nth, dim=2)
        return torch.einsum('ij,bjk->bik', self.Minv, Ft)

    def eval_bs(self, C, Fext, ci, cj):
        """Evaluate the B-spline with coefficients C [B, Next, Nth] at fractional grid indices (ci, cj) [B, ...]; clip to the hull of the
        four surrounding grid values of Fext (not of C)."""
        Nth, P, Next = self.Nth, self.pad, self.Next
        B = C.shape[0]
        bidx = torch.arange(B, device=self.dev).view((B,) + (1,) * (ci.dim() - 1))
        i0 = torch.floor(ci); t = ci - i0; i0 = i0.long() + P
        j0 = torch.floor(cj); u = cj - j0; j0 = j0.long()
        def wts(t):
            return ((1 - t) ** 3 / 6, (3 * t ** 3 - 6 * t ** 2 + 4) / 6, (-3 * t ** 3 + 3 * t ** 2 + 3 * t + 1) / 6, t ** 3 / 6)
        wi = wts(t); wj = wts(u)
        out = torch.zeros_like(ci)
        for a in range(4):
            ia = (i0 + (a - 1)).clamp(0, Next - 1)
            rowv = torch.zeros_like(ci)
            for bb in range(4):
                jb = torch.remainder(j0 + (bb - 1), Nth)
                rowv = rowv + wj[bb] * C[bidx, ia, jb]
            out = out + wi[a] * rowv
        if self.limiter:
            ia0 = i0.clamp(0, Next - 1); ia1 = (i0 + 1).clamp(0, Next - 1)
            ja0 = torch.remainder(j0, Nth); ja1 = torch.remainder(j0 + 1, Nth)
            c00 = Fext[bidx, ia0, ja0]; c01 = Fext[bidx, ia0, ja1]; c10 = Fext[bidx, ia1, ja0]; c11 = Fext[bidx, ia1, ja1]
            lo = torch.minimum(torch.minimum(c00, c01), torch.minimum(c10, c11))
            hi = torch.maximum(torch.maximum(c00, c01), torch.maximum(c10, c11))
            out = torch.minimum(torch.maximum(out, lo), hi)
        return out

    def interp(self, F, ci, cj, top_rows):
        if self.bspline:
            Fext = self.extend(F, top_rows)
            return self.eval_bs(self.prefilter(Fext), Fext, ci, cj)
        return self.interp_lagrange(F, ci, cj, top_rows)

    def interp_lagrange(self, F, ci, cj, top_rows):
        """F [B, Nr, Nth]; ci, cj [B, ...] fractional indices; top_rows [B, 2, Nth].  Local cubic Lagrange (the pre-07:00Z scheme)."""
        Nr, Nth = self.Nr, self.Nth
        B = F.shape[0]
        Fp = torch.cat([F[:, :1], F, top_rows], 1)                        # [B, Nr+3, Nth]: rows -1 .. Nr+1 -> +1
        bidx = torch.arange(B, device=self.dev).view((B,) + (1,) * (ci.dim() - 1))
        i0 = torch.floor(ci); i0 = i0.long()
        j0 = torch.floor(cj); u = cj - j0; j0 = j0.long()
        i0 = torch.clamp(i0, 0, Nr)
        t = torch.where((ci - i0.double()) > 1.0, torch.ones_like(ci), ci - i0.double())
        def lw(t):
            return (-t * (t - 1) * (t - 2) / 6, (t + 1) * (t - 1) * (t - 2) / 2, -(t + 1) * t * (t - 2) / 2, (t + 1) * t * (t - 1) / 6)
        wi = lw(t); wj = lw(u)
        out = torch.zeros_like(ci)
        for a in range(4):
            ia = (i0 + (a - 1) + 1).clamp(0, Nr + 2)
            rowv = torch.zeros_like(ci)
            for b in range(4):
                jb = torch.remainder(j0 + (b - 1), Nth)
                rowv = rowv + wj[b] * Fp[bidx, ia, jb]
            out = out + wi[a] * rowv
        if self.limiter:
            ia0 = (i0 + 1).clamp(0, Nr + 2); ia1 = (i0 + 2).clamp(0, Nr + 2)
            ja0 = torch.remainder(j0, Nth); ja1 = torch.remainder(j0 + 1, Nth)
            c00 = Fp[bidx, ia0, ja0]; c01 = Fp[bidx, ia0, ja1]; c10 = Fp[bidx, ia1, ja0]; c11 = Fp[bidx, ia1, ja1]
            lo = torch.minimum(torch.minimum(c00, c01), torch.minimum(c10, c11))
            hi = torch.maximum(torch.maximum(c00, c01), torch.maximum(c10, c11))
            out = torch.minimum(torch.maximum(out, lo), hi)
        return out

    def step(self, g, ds, p, A, Afun):
        """g [B, Nr, Nth]; p [B]; A [B, Nth] datum on the grid; Afun(th [B, ...]) -> datum values per state."""
        cl = 1.0 / p
        rho = self.r[None, :, None] ** p[:, None, None] * g
        Wr, Wt = self.velocity(rho, p)
        ar = cl[:, None, None] + Wr / self.r[None, :, None]
        at = Wt / self.r[None, :, None]
        src = p[:, None, None] * Wr / self.r[None, :, None]
        top2 = lambda X: X[:, -1:].expand(-1, 2, -1)
        ci0 = self.ii + 0.5 * ds * ar / self.d
        cj0 = self.jj + 0.5 * ds * at / self.dth
        arm = self.interp(ar, ci0, cj0, top2(ar)); atm = self.interp(at, ci0, cj0, top2(at)); srm = self.interp(src, ci0, cj0, top2(src))
        ci = self.ii + ds * arm / self.d
        cj = self.jj + ds * atm / self.dth
        gn = self.interp(g, ci, cj, A[:, None, :].expand(-1, 2, -1)) * torch.exp(ds * srm)
        out = ci > self.Nr - 1
        if bool(out.any()):
            gn = torch.where(out, Afun(cj * self.dth), gn)
        return gn, (Wr, Wt)

    def evolve(self, g, p, A, Afun, ds, nsteps):
        for n in range(nsteps):
            gn, WW = self.step(g, ds, p, A, Afun)
            if n == nsteps - 1:
                dg = (gn - g).abs().amax(dim=(1, 2)) / ds
            g = gn
        return g, dg

    # ------------------------------------------------------------------------------------------------------------
    def c_moment(self, rho, p, A, qj=2.0):
        """strain moment c = psi_xy(0) = (1/pi) int rho r^-3 sin 3th dX, grid + outer tail + core term (specification M25(f)) -> [B].
        qj: jet order of the core continuation (rho ~ (r/r_min)^qj rho(r_min, th) below r_min): core term x 1/(qj - 1) (P_q, notes of the lead analyst 09:59Z)."""
        wl = torch.full((self.Nr,), self.d, device=self.dev); wl[0] = 0.5 * self.d; wl[-1] = 0.5 * self.d      # trapezoid in lr
        w = (self.r ** (-1) * wl)[None, :, None] * self.dth / math.pi
        s3 = torch.sin(3 * self.th)[None, None, :]
        c_grid = (rho * s3 * w).sum(dim=(1, 2))
        a3s = (A * torch.sin(3 * self.th)[None, :]).sum(dim=1) * self.dth / math.pi
        rmax = float(self.r[-1]); tail = rmax ** (p - 1) / (1 - p)
        r0 = float(self.r[0])
        qm1 = (qj - 1.0) if torch.is_tensor(qj) else (float(qj) - 1.0)                      # scalar or per-state tensor [B]
        core = r0 / math.pi * ((rho[:, 0, :] / r0 ** 2) * torch.sin(3 * self.th)[None, :]).sum(dim=1) * self.dth / qm1
        return c_grid + a3s * tail + core, core

    def trace(self, Wr, Wt, p, thA, lr0, dt=0.01, e1=(1.0, 0.0), max_it=40000):
        """Backward orbits dX/dt = -V from (r_max, thA) to lr0 for all B states.  Returns T, u0, w0, th0 [B, nA]."""
        B = Wr.shape[0]; nA = thA.shape[0]
        cl = 1.0 / p
        ar = cl[:, None, None] + Wr / self.r[None, :, None]; at = Wt / self.r[None, :, None]
        top = lambda F: F[:, -1:].expand(-1, 2, -1)
        if self.bspline:
            arE = self.extend(ar, top(ar)); atE = self.extend(at, top(at)); Car = self.prefilter(arE); Cat = self.prefilter(atE)
            def rhs(lr, th):
                ci = (lr - self.lo) / self.d; cj = th / self.dth
                return -self.eval_bs(Car, arE, ci, cj), -self.eval_bs(Cat, atE, ci, cj)
        else:
            def rhs(lr, th):
                ci = (lr - self.lo) / self.d; cj = th / self.dth
                return -self.interp(ar, ci, cj, top(ar)), -self.interp(at, ci, cj, top(at))
        lr = torch.full((B, nA), self.hi - 1e-9, device=self.dev); th = thA[None, :].expand(B, -1).clone()
        T = torch.zeros(B, nA, device=self.dev); live = torch.ones(B, nA, dtype=torch.bool, device=self.dev)
        it = 0
        while bool(live.any()) and it < max_it:
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
        X0 = torch.stack([r0 * torch.cos(th), r0 * torch.sin(th)], 2)
        e1t = torch.tensor(e1, device=self.dev, dtype=torch.float64); e2t = torch.tensor([-e1[1], e1[0]], device=self.dev, dtype=torch.float64)
        arrived = (~live) & torch.isfinite(th) & torch.isfinite(T)
        return T, X0 @ e1t, X0 @ e2t, th, it, arrived
