"""Exit-map fixed-point solver (notes of the lead analyst 2026-10-18T07:50Z; specification M26(h)): the reference stationary solver of the forward problem.
Given the far-field datum A (x-even, cos^2 exp(sum a_j phi_j)) and p, iterate rho <- T[rho], where T is the exact characteristic map of the
velocity computed from the current state: for every grid point integrate the forward orbit (d lr/dt = V_r/r, d th/dt = V_th/r; velocity fields
prefiltered as cubic B-splines) to r_max and set  (T g)(X) = e^{-T(X)} r_max^p A(th_exit(X)) / r^p.  A fixed point is a stationary state whose
density is consistent with its own characteristics by construction (no semi-Lagrangian time stepping, no interpolation of the transported
field).  Anderson acceleration (depth m) on the scaled variable u = g / s(r), s = (r^2/(1+r^2))^{1-p/2}; optional x-even projection
g(th) <- (g(th) + g(pi - th))/2.  Warm start from a saved forward state.
"""
import sys, json, math, time, os
import numpy as np
import torch
sys.path.insert(0, 'code')
from pfwd_batch import PFwdB
torch.set_default_dtype(torch.float64)


class ExitMap:
    def __init__(self, Nr, Nth, lo, hi, p, coef, dt=0.01, xeven=True, thr=1e-3, dev='cuda', max_it=30000, qj=2.0, Afun=None):
        self.qj = float(qj)                                                                      # jet order of the datum zero (P_q)
        if Afun is not None: self.Afun = Afun                                                    # external datum function (e.g. BNewton.Afun with window bumps)
        self.SB = PFwdB(Nr, Nth, lo, hi, p, dev=dev); S = self.SB.S
        self.S, self.p, self.dt, self.xeven, self.thr, self.dev, self.max_it = S, float(p), float(dt), bool(xeven), float(thr), dev, int(max_it)
        self.coef = np.asarray(coef, float); self.K = len(self.coef)
        self.pB = torch.tensor([self.p], device=dev)
        self.A = self.Afun(S.th[None, :])                                                     # [1, Nth]
        self.LR = S.lr[:, None].expand(Nr, Nth).reshape(1, -1).clone(); self.TH = S.th[None, :].expand(Nr, Nth).reshape(1, -1).clone()
        self.scale = ((S.r ** 2 / (1.0 + S.r ** 2)) ** (1.0 - self.p / 2))[:, None]          # [Nr, 1]
        j = torch.arange(Nth, device=dev); self.flip = torch.remainder(Nth // 2 - j, Nth)       # th -> pi - th

    def Afun(self, t):
        F = torch.zeros_like(t)
        for j in range(self.K):
            n = j + 1; F = F + float(self.coef[j]) * (torch.sin(n * t) if n % 2 == 1 else torch.cos(n * t))
        return torch.cos(t).abs() ** self.qj * torch.exp(F)

    def project(self, g):
        return 0.5 * (g + g[:, self.flip]) if self.xeven else g

    def velocity(self, g):
        rho = self.S.r[:, None] ** self.p * g
        Wr, Wt = self.SB.velocity(rho[None], self.pB)
        return Wr, Wt, rho

    def T(self, g, return_vel=False):
        """One exit-map application on g [Nr, Nth]."""
        S, SB = self.S, self.SB
        Wr, Wt, rho = self.velocity(g)
        ar = (1 / self.p) + Wr / S.r[None, :, None]; at = Wt / S.r[None, :, None]
        top = lambda F: F[:, -1:].expand(-1, 2, -1)
        arE = SB.extend(ar, top(ar)); atE = SB.extend(at, top(at)); Car = SB.prefilter(arE); Cat = SB.prefilter(atE)
        LR = self.LR.clone(); TH = self.TH.clone(); Tt = torch.zeros_like(LR); live = LR < S.hi - 1e-12; dt = self.dt; it = 0
        def rhs(l_, t_):
            ci = (l_ - S.lo) / S.d; cj = t_ / S.dth
            return SB.eval_bs(Car, arE, ci, cj), SB.eval_bs(Cat, atE, ci, cj)
        while bool(live.any()) and it < self.max_it:
            k1 = rhs(LR, TH); k2 = rhs(LR + 0.5 * dt * k1[0], TH + 0.5 * dt * k1[1]); k3 = rhs(LR + 0.5 * dt * k2[0], TH + 0.5 * dt * k2[1]); k4 = rhs(LR + dt * k3[0], TH + dt * k3[1])
            dl = dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); dth = dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
            over = live & (LR + dl >= S.hi)
            frac = torch.where(over, (S.hi - LR) / torch.clamp(dl, min=1e-300), torch.ones_like(dl))
            LR = torch.where(live, LR + frac * dl, LR); TH = torch.where(live, TH + frac * dth, TH); Tt = torch.where(live, Tt + frac * dt, Tt)
            live = live & ~over; it += 1
        Tg = (torch.exp(-Tt) * math.exp(self.p * S.hi) * self.Afun(TH)).reshape(S.Nr, S.Nth) / S.r[:, None] ** self.p
        Tg = self.project(Tg)
        info = dict(orbit_its=it, unfinished=int(live.sum()))
        if return_vel:
            return Tg, info, (Wr, Wt)
        return Tg, info

    def defect(self, g, Tg, tol=None):
        rowmax = g.max(dim=1, keepdim=True).values
        msk = g > self.thr * rowmax
        d = torch.where(msk, (Tg - g).abs() / rowmax, torch.zeros_like(g))
        if tol is None:
            return float(d.max()), float(torch.sqrt((d ** 2).sum() / msk.sum()))
        bad = d > tol
        d2 = torch.where(bad, torch.zeros_like(d), d)
        return float(d.max()), float(torch.sqrt((d ** 2).sum() / msk.sum())), int(bad.sum()), float(torch.sqrt((d2 ** 2).sum() / msk.sum()))

    def solve(self, g0, maxit=30, tol=1e-5, m=6, beta=1.0, log=print):
        """Anderson-accelerated fixed-point iteration on u = g / scale.  Returns g, Tg, history."""
        g = self.project(g0.clone()); hist = []
        X = []; Fh = []
        u = (g / self.scale).reshape(-1)
        t0 = time.time()
        for k in range(maxit):
            Tg, info = self.T(g)
            dmax, drms = self.defect(g, Tg)
            Tu = (Tg / self.scale).reshape(-1); f = Tu - u
            rec = dict(it=k, defect_max=dmax, defect_rms=drms, orbit_its=info['orbit_its'], unfinished=info['unfinished'], wall=round(time.time() - t0, 1))
            hist.append(rec); log(json.dumps(rec))
            if dmax < tol:
                break
            X.append(u.clone()); Fh.append(f.clone())
            if len(X) > m + 1:
                X.pop(0); Fh.pop(0)
            if len(X) >= 2:
                dF = torch.stack([Fh[i + 1] - Fh[i] for i in range(len(Fh) - 1)], 1)       # [N, mk]
                dX = torch.stack([X[i + 1] - X[i] for i in range(len(X) - 1)], 1)
                gam = torch.linalg.lstsq(dF, f[:, None]).solution[:, 0]
                u_new = u + beta * f - (dX + beta * dF) @ gam
            else:
                u_new = u + beta * f
            u = u_new
            g = self.project((u.reshape(self.S.Nr, self.S.Nth) * self.scale).clamp(min=0.0))
        Tg, info = self.T(g)
        dmax, drms = self.defect(g, Tg)
        hist.append(dict(it=len(hist), defect_max=dmax, defect_rms=drms, final=True, wall=round(time.time() - t0, 1)))
        log(json.dumps(hist[-1]))
        return g, Tg, hist

    def solve_safe(self, g0, maxit=30, tol=1e-5, m=6, beta=1.0, log=print, orbit_cap=3000, grow=10.0, beta_min=1.0 / 64, grow_picard=2.0, ncell_tol=8, rms_rest_tol=None):
        """Safeguarded Anderson (2026-10-18T10:30Z): every proposed iterate is accepted only if all orbits exit within orbit_cap RK4
        steps and the rms defect does not exceed grow x the best accepted rms so far (Anderson is not monotone; grow 10 allows its excursions) and,
        for a damped Picard step, grow_picard x the current rms; otherwise the proposal is discarded, the Anderson history is
        cleared and a damped Picard step u + beta_f f from the last accepted iterate is taken, beta_f halved per consecutive failure (verifier's
        PG strategy).  On acceptance beta_f is doubled back toward beta.  Returns g, Tg, history (one record per T evaluation, accepted flag)."""
        max_it_saved = self.max_it; self.max_it = int(orbit_cap)
        g = self.project(g0.clone()); hist = []; X = []; Fh = []
        u = (g / self.scale).reshape(-1); t0 = time.time()
        rms_rest_tol = tol / 10 if rms_rest_tol is None else rms_rest_tol
        Tg, info = self.T(g); dmax, drms, nbad, drest = self.defect(g, Tg, tol); Tu = (Tg / self.scale).reshape(-1); f = Tu - u
        rec = dict(it=0, defect_max=dmax, defect_rms=drms, ncells_above_tol=nbad, rms_rest=drest, orbit_its=info['orbit_its'], unfinished=info['unfinished'], accepted=True, beta_f=beta, wall=round(time.time() - t0, 1))
        hist.append(rec); log(json.dumps(rec))
        conv = lambda dm, nb, dr: (dm < tol) or (nb <= ncell_tol and dr < rms_rest_tol)   # converged: max defect below tol, or at most ncell_tol cells above tol (exit-window flips on the separatrix) with the rest below rms_rest_tol
        if info['unfinished'] > 0 or not np.isfinite(dmax):
            log(json.dumps(dict(warning='start state has unfinished orbits or a non-finite defect; no fallback possible', unfinished=info['unfinished'])))
        beta_f = beta; nfail = 0; nacc = 0; k = 0; drms_best = drms if np.isfinite(drms) else float('inf')
        while k < maxit and not conv(dmax, nbad, drest):
            X.append(u.clone()); Fh.append(f.clone())
            if len(X) > m + 1:
                X.pop(0); Fh.pop(0)
            if len(X) >= 2 and nfail == 0:
                dF = torch.stack([Fh[i + 1] - Fh[i] for i in range(len(Fh) - 1)], 1); dX = torch.stack([X[i + 1] - X[i] for i in range(len(X) - 1)], 1)
                gam = torch.linalg.lstsq(dF, f[:, None]).solution[:, 0]
                u_new = u + beta * f - (dX + beta * dF) @ gam; kind = 'anderson'
            else:
                u_new = u + beta_f * f; kind = 'picard'
            g_new = self.project((u_new.reshape(self.S.Nr, self.S.Nth) * self.scale).clamp(min=0.0))
            Tg_new, info = self.T(g_new); dmax_new, drms_new, nbad_new, drest_new = self.defect(g_new, Tg_new, tol); k += 1
            ok = (info['unfinished'] == 0) and np.isfinite(dmax_new) and (drms_new <= grow * drms_best) and (kind == 'anderson' or drms_new <= grow_picard * drms)
            rec = dict(it=k, kind=kind, defect_max=dmax_new, defect_rms=drms_new, ncells_above_tol=nbad_new, rms_rest=drest_new, orbit_its=info['orbit_its'], unfinished=info['unfinished'], accepted=bool(ok), beta_f=beta_f, nfail=nfail, wall=round(time.time() - t0, 1))
            hist.append(rec); log(json.dumps(rec))
            if ok:
                u = u_new; g = g_new; Tg = Tg_new; dmax, drms, nbad, drest = dmax_new, drms_new, nbad_new, drest_new; f = (Tg / self.scale).reshape(-1) - u
                nacc += 1; drms_best = min(drms_best, drms)
                if nfail > 0:
                    nfail = 0; beta_f = min(beta, 2 * beta_f)
                elif beta_f < beta:
                    beta_f = min(beta, 2 * beta_f)
            else:
                X.clear(); Fh.clear(); nfail += 1; beta_f *= 0.5
                if beta_f < beta_min:
                    log(json.dumps(dict(giveup=True, beta_f=beta_f, note='damping below beta_min; returning the last accepted iterate'))); break
        self.max_it = max_it_saved
        hist.append(dict(it=len(hist), defect_max=dmax, defect_rms=drms, ncells_above_tol=nbad, rms_rest=drest, converged=bool(conv(dmax, nbad, drest)), final=True, accepted_steps=nacc, wall=round(time.time() - t0, 1)))
        log(json.dumps(hist[-1]))
        return g, Tg, hist


if __name__ == '__main__':
    # usage: python3 code/pfwd_exitmap.py state.npz [K=32] [maxit=30] [tol=1e-5] [m=6] [beta=1.0] [dt=0.01] [xeven=1] [tag=em] [cold=0]
    #        state.npz: bnewton iterate (g, x, args) or bscan-style single state (g, x, args) or any (g, lr, th, args with p and par)
    sys.path.insert(0, 'code')
    from pfwd_bnewton import BNewton
    fn = sys.argv[1]; opt = dict(K=32, maxit=30, tol=1e-5, m=6, beta=1.0, dt=0.01, xeven=1, tag='em', cold=0, Nth=0, safe=0, orbit_cap=3000, grow=10.0, sub=1, qj=0.0)
    for s_ in sys.argv[2:]:
        k, v = s_.split('='); opt[k] = v if k == 'tag' else (int(v) if k in ('K', 'maxit', 'm', 'xeven', 'cold', 'Nth', 'safe', 'orbit_cap', 'sub') else float(v))
    d = np.load(fn, allow_pickle=True); g0 = d['g']; lr = d['lr']; th = d['th']
    if 'x' in d.files and 'args' in d.files:
        x = d['x']; a = json.loads(str(d['args'])); p = float(a['p']); coef = x[:-1] if len(x) == len(a.get('par', x[:-1])) + 1 else np.array(a['par'])
    else:
        a = json.loads(str(d['args'])); p = float(a['p']); coef = np.array(a['par'])
    if opt['sub'] > 1:                                        # angular subsampling of the start state (uniform grid, thshift 0): g[:, ::sub]
        g0 = g0[:, ::opt['sub']]; th = th[::opt['sub']]
    Nr, Nth = g0.shape
    os.makedirs('runs/pfwd/em', exist_ok=True); logf = open('runs/pfwd/em/%s.log' % opt['tag'], 'a')
    def log(line):
        print(line, flush=True); logf.write(line + '\n'); logf.flush()
    log(json.dumps(dict(tag=opt['tag'], state=fn, p=p, K=len(coef), Nr=Nr, Nth=Nth, opt=opt, start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))))
    qj = opt['qj'] if opt['qj'] > 0 else float(a.get('qj', 2.0))
    EM = ExitMap(Nr, Nth, float(lr[0]), float(lr[-1]), p, coef, dt=opt['dt'], xeven=bool(opt['xeven']), qj=qj)
    g_init = torch.tensor(g0, device='cuda') if not opt['cold'] else (EM.scale * EM.A)
    if opt['safe']:
        g, Tg, hist = EM.solve_safe(g_init, maxit=opt['maxit'], tol=opt['tol'], m=opt['m'], beta=opt['beta'], log=log, orbit_cap=opt['orbit_cap'], grow=opt['grow'])
    else:
        g, Tg, hist = EM.solve(g_init, maxit=opt['maxit'], tol=opt['tol'], m=opt['m'], beta=opt['beta'], log=log)
    # diagnostics of the fixed point via the Newton residual machinery (no evolution)
    BN = BNewton(len(coef), [], Nr=Nr, Nth=Nth, lo=float(lr[0]), hi=float(lr[-1]), lr0=-13.0 if lr[0] <= -13.5 else float(lr[0]) + 1.0, cut=0.02, wm=3.0, log=None, tag=opt['tag'], qj=qj)
    xfull = np.concatenate([coef, [p]])
    F, infos, gg, lg, tm = BN.evaluate(xfull[None], 0, g_given=g[None])
    info = infos[0]; info['F0_m1'] = float(F[0][0]); info['normF_noM1'] = float(np.linalg.norm(F[0][1:]))
    # specification v4.3: D_ax in the a_div form with a_dir next to it; min |V|/r and min V_r/r with locations
    from pfwd_diag import axis_D
    Wr, Wt, rho = EM.velocity(g)
    axd = axis_D(EM.S, g, Wr[0], p, info['m1'], A=EM.A[0], qj=qj)                 # a_div form
    axr = axis_D(EM.S, g, Wr[0], p, info['m1'], A=EM.A[0], Wt=Wt[0], qj=qj)       # a_dir form
    Vr_r = (1 / p) + Wr[0] / EM.S.r[:, None]; Vt_r = Wt[0] / EM.S.r[:, None]; Vabs = torch.sqrt(Vr_r ** 2 + Vt_r ** 2)
    lrn = EM.S.lr.cpu().numpy(); thd = np.degrees(EM.S.th.cpu().numpy())
    i, j = np.unravel_index(int(Vabs.argmin()), Vabs.shape); i2, j2 = np.unravel_index(int(Vr_r.argmin()), Vr_r.shape)
    info.update(D_ax_div=axd['D_ax_k'], drift_up_div=axd['drift_up'], drift_down_div=axd['drift_down'], D_ax_dir=axr['D_ax_k'], drift_up_dir=axr['drift_up'],
                drift_down_dir=axr['drift_down'], D_res17=axd['D_ax_res17'], minVabs_r=float(Vabs.min()), minVabs_at=[float(lrn[i]), float(thd[j])],
                minVr_r=float(Vr_r.min()), minVr_at=[float(lrn[i2]), float(thd[j2])], Fp_minus_Fm=axd['Fp_minus_Fm_datum'])
    log(json.dumps(dict(fixed_point=True, m1=info['m1'], core=info['core'], normF=info['normF'], D_ax_div=info['D_ax_div'], drift_div=[info['drift_up_div'], info['drift_down_div']],
                        D_ax_dir=info['D_ax_dir'], drift_dir=[info['drift_up_dir'], info['drift_down_dir']], D_res17=info['D_res17'], Fp_minus_Fm=info['Fp_minus_Fm'],
                        up89=info['up89'], low269=info['low269'], D_samp=info['D_samp'], bulk_std=info['bulk_std'], rms_unresolved=info['rms_unresolved'],
                        minVabs_r=info['minVabs_r'], minVabs_at=info['minVabs_at'], minVr_r=info['minVr_r'], minVr_at=info['minVr_at'],
                        defect_max=hist[-1]['defect_max'], defect_rms=hist[-1]['defect_rms'])))
    np.savez('runs/pfwd/em/%s_fp.npz' % opt['tag'], g=g.cpu().numpy(), Tg=Tg.cpu().numpy(), lr=lr, th=th, x=xfull, p=p, hist=json.dumps(hist), info=json.dumps(info),
             args=json.dumps(dict(p=p, kind='expf', par=[float(v) for v in coef], exitmap=True, qj=qj)), logGt=lg[0], thA=BN.thA.cpu().numpy())
    log("EXITMAP_DONE")
