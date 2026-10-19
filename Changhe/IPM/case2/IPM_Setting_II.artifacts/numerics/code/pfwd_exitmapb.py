"""BATCHED exit map (2026-10-18T11:45Z): the exact characteristic map T of code/pfwd_exitmap.py applied to B states at once (own datum and own p
each) on one grid, so that an exit-map Jacobian (base + n one-sided perturbations, all re-solved to fixed points) costs a few batched T applications
instead of n single solves.  Orbits: forward RK4 of d lr/dt = V_r/r, d th/dt = V_th/r from every grid point to r_max with the velocity fields prefiltered
as cubic B-splines (PFwdB.eval_bs is batched); (T g)_b(X) = e^{-T_b(X)} r_max^{p_b} A_b(th_exit) / r^{p_b}; optional x-even projection.
solve(): batched Anderson (depth m, ridge-regularised per-state least squares) with a per-state safeguard: a proposal for state b is rejected if its orbits
do not all exit within orbit_cap steps or its rms defect exceeds grow x its best accepted rms; a rejected state takes a damped Picard step
(beta_f halved per consecutive failure) from its last accepted iterate.  Convergence per state: max defect < tol or <= ncell_tol cells above tol with the
rest below tol/10 (located-cell rule, specification v4.6).
"""
import math, time, json
import numpy as np
import torch
torch.set_default_dtype(torch.float64)


class ExitMapB:
    def __init__(self, SB, pB, Afun, dt=0.01, xeven=True, thr=1e-3, orbit_cap=3000):
        self.SB = SB; S = SB.S; self.S = S
        self.pB = pB if torch.is_tensor(pB) else torch.tensor(np.asarray(pB, float), device=SB.dev)
        self.B = int(self.pB.shape[0]); self.Afun = Afun; self.dt = float(dt); self.xeven = bool(xeven); self.thr = float(thr); self.orbit_cap = int(orbit_cap)
        self.dev = SB.dev; Nr, Nth = S.Nr, S.Nth
        self.LR0 = S.lr[:, None].expand(Nr, Nth).reshape(1, -1).expand(self.B, -1).clone()
        self.TH0 = S.th[None, :].expand(Nr, Nth).reshape(1, -1).expand(self.B, -1).clone()
        self.rp = S.r[None, :, None] ** self.pB[:, None, None]                                      # [B, Nr, 1]
        self.scale = ((S.r[None, :] ** 2 / (1.0 + S.r[None, :] ** 2)) ** (1.0 - self.pB[:, None] / 2))[:, :, None]   # [B, Nr, 1]
        j = torch.arange(Nth, device=self.dev); self.flip = torch.remainder(Nth // 2 - j, Nth)

    def project(self, g):
        return 0.5 * (g + g[:, :, self.flip]) if self.xeven else g

    def T(self, g):
        """g [B, Nr, Nth] -> (T g, info dict with per-state orbit counts)."""
        S, SB = self.S, self.SB; B = self.B
        rho = self.rp * g
        Wr, Wt = SB.velocity(rho, self.pB)
        ar = (1.0 / self.pB)[:, None, None] + Wr / S.r[None, :, None]; at = Wt / S.r[None, :, None]
        top = lambda F: F[:, -1:].expand(-1, 2, -1)
        arE = SB.extend(ar, top(ar)); atE = SB.extend(at, top(at)); Car = SB.prefilter(arE); Cat = SB.prefilter(atE)
        LR = self.LR0.clone(); TH = self.TH0.clone(); Tt = torch.zeros_like(LR); live = LR < S.hi - 1e-12; dt = self.dt; it = 0
        def rhs(l_, t_):
            ci = (l_ - S.lo) / S.d; cj = t_ / S.dth
            return SB.eval_bs(Car, arE, ci, cj), SB.eval_bs(Cat, atE, ci, cj)
        while bool(live.any()) and it < self.orbit_cap:
            k1 = rhs(LR, TH); k2 = rhs(LR + 0.5 * dt * k1[0], TH + 0.5 * dt * k1[1]); k3 = rhs(LR + 0.5 * dt * k2[0], TH + 0.5 * dt * k2[1]); k4 = rhs(LR + dt * k3[0], TH + dt * k3[1])
            dl = dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); dth = dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
            over = live & (LR + dl >= S.hi)
            frac = torch.where(over, (S.hi - LR) / torch.clamp(dl, min=1e-300), torch.ones_like(dl))
            LR = torch.where(live, LR + frac * dl, LR); TH = torch.where(live, TH + frac * dth, TH); Tt = torch.where(live, Tt + frac * dt, Tt)
            live = live & ~over; it += 1
        A_exit = self.Afun(TH)                                                                        # [B, N]
        Tg = (torch.exp(-Tt) * torch.exp(self.pB * S.hi)[:, None] * A_exit).reshape(B, S.Nr, S.Nth) / self.rp
        Tg = self.project(Tg)
        return Tg, dict(orbit_its=it, unfinished=live.sum(dim=1).cpu().numpy().tolist())

    def defect(self, g, Tg, tol):
        rowmax = g.max(dim=2, keepdim=True).values
        msk = g > self.thr * rowmax
        d = torch.where(msk, (Tg - g).abs() / rowmax, torch.zeros_like(g))
        cnt = msk.sum(dim=(1, 2)).clamp(min=1)
        dmax = d.amax(dim=(1, 2)); drms = torch.sqrt((d ** 2).sum(dim=(1, 2)) / cnt)
        bad = d > tol; nbad = bad.sum(dim=(1, 2)); drest = torch.sqrt(torch.where(bad, torch.zeros_like(d), d).pow(2).sum(dim=(1, 2)) / cnt)
        return dmax.cpu().numpy(), drms.cpu().numpy(), nbad.cpu().numpy(), drest.cpu().numpy()

    def solve(self, g0, maxit=20, tol=2e-5, m=6, beta=1.0, grow=10.0, ncell_tol=8, log=None):
        B = self.B; S = self.S; N = S.Nr * S.Nth
        g = self.project(g0.clone()); u = (g / self.scale).reshape(B, -1)
        Tg, info = self.T(g); f = (Tg / self.scale).reshape(B, -1) - u
        dmax, drms, nbad, drest = self.defect(g, Tg, tol)
        best = drms.copy(); beta_f = np.full(B, beta); nfail = np.zeros(B, int)
        conv = lambda: (dmax < tol) | ((nbad <= ncell_tol) & (drest < tol / 10))
        hist = [dict(it=0, dmax=dmax.tolist(), drms=drms.tolist(), nbad=nbad.tolist(), unfinished=info['unfinished'], orbit_its=info['orbit_its'])]
        if log: log(json.dumps(hist[-1]))
        X = [u.clone()]; Fh = [f.clone()]
        done = conv(); k = 0; t0 = time.time()
        while k < maxit and not bool(done.all()):
            if len(X) >= 2:
                dF = torch.stack([Fh[i + 1] - Fh[i] for i in range(len(Fh) - 1)], 2)       # [B, N, mk]
                dX = torch.stack([X[i + 1] - X[i] for i in range(len(X) - 1)], 2)
                G = torch.einsum('bnk,bnl->bkl', dF, dF); rhs_ = torch.einsum('bnk,bn->bk', dF, f)
                ridge = 1e-10 * torch.diagonal(G, dim1=1, dim2=2).amax(dim=1).clamp(min=1e-300)
                G = G + ridge[:, None, None] * torch.eye(G.shape[1], device=self.dev)[None]
                gam = torch.linalg.solve(G, rhs_[:, :, None])[:, :, 0]
                u_and = u + beta * f - torch.einsum('bnk,bk->bn', dX + beta * dF, gam)
            else:
                u_and = u + beta * f
            use_picard = torch.tensor(nfail > 0, device=self.dev)
            u_pic = u + torch.tensor(beta_f, device=self.dev)[:, None] * f
            u_new = torch.where(use_picard[:, None], u_pic, u_and)
            u_new = torch.where(torch.tensor(done, device=self.dev)[:, None], u, u_new)       # converged states are frozen
            g_new = self.project((u_new.reshape(B, S.Nr, S.Nth) * self.scale).clamp(min=0.0))
            Tg_new, info = self.T(g_new); k += 1
            dmax_n, drms_n, nbad_n, drest_n = self.defect(g_new, Tg_new, tol)
            unf = np.array(info['unfinished'])
            ok = (unf == 0) & np.isfinite(drms_n) & (drms_n <= grow * best)
            ok = ok | done                                                                     # frozen states keep their values
            okt = torch.tensor(ok, device=self.dev)
            u = torch.where(okt[:, None], u_new, u); g = torch.where(okt[:, None, None], g_new, g); Tg = torch.where(okt[:, None, None], Tg_new, Tg)
            f = (Tg / self.scale).reshape(B, -1) - u
            dmax = np.where(ok, dmax_n, dmax); drms = np.where(ok, drms_n, drms); nbad = np.where(ok, nbad_n, nbad); drest = np.where(ok, drest_n, drest)
            best = np.minimum(best, drms)
            nfail = np.where(ok, 0, nfail + 1); beta_f = np.where(ok, np.minimum(beta, 2 * beta_f), 0.5 * beta_f)
            if (~ok).any():
                # rejected states: reset their Anderson history to the current point (their dX, dF columns vanish -> Picard)
                for i in range(len(X)):
                    X[i] = torch.where(okt[:, None], X[i], u); Fh[i] = torch.where(okt[:, None], Fh[i], f)
            X.append(u.clone()); Fh.append(f.clone())
            if len(X) > m + 1:
                X.pop(0); Fh.pop(0)
            done = conv()
            hist.append(dict(it=k, dmax=[float('%.3g' % v) for v in dmax], drms=[float('%.3g' % v) for v in drms], nbad=nbad.tolist(), accepted=ok.tolist(), unfinished=info['unfinished'],
                             orbit_its=info['orbit_its'], wall=round(time.time() - t0, 1)))
            if log: log(json.dumps(hist[-1]))
        hist.append(dict(final=True, dmax=dmax.tolist(), drms=drms.tolist(), nbad=nbad.tolist(), converged=done.tolist(), wall=round(time.time() - t0, 1)))
        if log: log(json.dumps(hist[-1]))
        return g, Tg, hist


if __name__ == '__main__':
    # timing test: python3 code/pfwd_exitmapb.py state_fp.npz "1,8,35"
    import sys; sys.path.insert(0, 'code')
    from pfwd_batch import PFwdB
    from pfwd_bnewton import BNewton
    d = np.load(sys.argv[1], allow_pickle=True); g0 = d['g']; lr = d['lr']; th = d['th']; a = json.loads(str(d['args'])); p = float(a['p']); coef = np.array(a['par'])
    Nr, Nth = g0.shape; SB = PFwdB(Nr, Nth, float(lr[0]), float(lr[-1]), p)
    BN = BNewton(len(coef), [], Nr=Nr, Nth=Nth, lo=float(lr[0]), hi=float(lr[-1]), lr0=-13.0, log=None, tag='tb')
    for Bs in [int(v) for v in sys.argv[2].split(',')]:
        X = np.repeat(np.concatenate([coef, [p]])[None], Bs, 0)
        for j in range(1, Bs): X[j, (j - 1) % len(coef)] += 0.01
        xB = torch.tensor(X, device='cuda'); pB = xB[:, -1]
        EM = ExitMapB(SB, pB, BN.Afun(xB), dt=0.01, xeven=True)
        g = torch.tensor(g0, device='cuda')[None].expand(Bs, -1, -1).clone()
        torch.cuda.synchronize(); t0 = time.time(); Tg, info = EM.T(g); torch.cuda.synchronize(); t1 = time.time()
        dmax, drms, nbad, drest = EM.defect(g, Tg, 2e-5)
        print('B %d: T wall %.1f s, orbit_its %d, defect_max state0 %.3g (others %.3g..%.3g), mem %.1f GB' % (Bs, t1 - t0, info['orbit_its'], dmax[0], dmax[1:].min() if Bs > 1 else 0, dmax[1:].max() if Bs > 1 else 0, torch.cuda.max_memory_allocated() / 1e9), flush=True)
