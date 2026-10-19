"""Many-mode fixed-point Newton for x-even Setting II profiles via the forward evolution, with BATCHED finite-difference Jacobians
(code/pfwd_batch.py).  Unknowns x = (a_1..a_K, b_1..b_nb, p): datum A(th) = cos^2 th exp(sum_j a_j phi_j(th) + sum_i b_i psi_i(th)),
phi_j the x-even Fourier modes (sin th, cos 2th, sin 3th, ...), psi_i Gaussian bumps (in angle) at the zeros 90 / 270 deg with widths
sigma_i (x-even).  Residual F = (wm (m1 - 1/2), c_1..c_{K+nb}) with m1 the CORE-CORRECTED weak node eigenvalue (1/p - c_moment - core)
and c the least-squares coefficients of log Gt(th) on [1, phi, psi] over the exit labels with |cos th| > cut, uniform weight; log Gt =
log A - 2 log|u0| - 2 m1 T from backward orbits with a DEEP inner stop (lr0, V59).  A root (F = 0 with the out-of-span part of log Gt
also small) is an x-even generalized profile with m1 = 1/2 and constant orbit coefficient, i.e. a C^2 node rho = Gt xi^2 (specification M24(a)).
Nothing is imposed on the state: no jet, no square root; the datum is x-even by construction (x-even subspace, specification M23(b)).
Jacobian: one batched evolution of (1 + n) states (base + one-sided perturbations, warm-started from the base state), nsteps_J steps.
Step: Levenberg-Marquardt (JTJ + mu D) dx = -JT F, trial batch over damping factors lam in (1, 0.6, 0.35, 0.2, 0.1), accept the best
decrease of |F|_2 (trial states evolved nsteps_T steps from the base), else mu x 10.  Diagnostics per iterate: D_ax (axis formula),
drifts, D_samp(deep), dips, bulk std, out-of-span rms, singular values of J.
"""
import sys, json, math, time, os
import numpy as np
import torch
sys.path.insert(0, 'code')
from pfwd_batch import PFwdB
from pfwd_diag import axis_D
torch.set_default_dtype(torch.float64)


class BNewton:
    def __init__(self, K, sigmas_deg, Nr=721, Nth=256, lo=-14.0, hi=10.0, ds=0.02, lr0=-13.0, nA=1440, dt=0.01, cut=0.02, wm=3.0,
                 nsteps_J=700, nsteps_T=900, h_a=0.01, h_b=0.01, h_p=0.004, log=None, tag='bn', dev='cuda', wd=0.0, exit=0, exit_maxit=20, exit_tol=2e-5, wD=0.0, dfree=0, fix2=0, exit_safe=1, diag=0, qj=2.0, qfree=0, jac='bs', jac_its=10, broyden_keep=0):
        self.K, self.sig = K, [math.radians(s) for s in sigmas_deg]
        self.nb = 2 * len(self.sig)
        self.dfree, self.fix2 = int(dfree), int(fix2)   # dfree: extra unknown D (specification M27(g): log Gt - mean - D s(th) matched, D free); fix2: a_2 frozen (natural-parameter continuation)
        self.qfree = int(qfree)                        # dual run (notes of the lead analyst 09:55Z (d)): the jet order q is an unknown with the row wm (q m1 - 1) replacing wm (m1 - 1/q); datum |cos|^q e^F
        self.n = K + self.nb + 1 + self.dfree + self.qfree   # unknowns: a_1..a_K, bumps, [D], [q], p (p last; q before p; D before q)
        self.nF = K + self.nb                          # number of datum shape coefficients
        self.Nr, self.Nth, self.lo, self.hi, self.ds, self.lr0, self.nA, self.dt, self.cut, self.wm = Nr, Nth, lo, hi, ds, lr0, nA, dt, cut, wm
        self.nsteps_J, self.nsteps_T, self.h_a, self.h_b, self.h_p = nsteps_J, nsteps_T, h_a, h_b, h_p
        self.log, self.tag, self.dev = log, tag, torch.device(dev)
        self.wd = float(wd)                  # weight of the axis-law drift penalty rows (specification M26(c)); 0 = off
        self.exit, self.exit_maxit, self.exit_tol = int(exit), int(exit_maxit), float(exit_tol)   # exit-map polish of base and accepted iterates (defect correction)
        self.wD = float(wD)                  # weight of the D_ax row (a_div form; specification v4.4 M26(i), notes of the lead analyst 08:30Z); 0 = off
        self.qj = float(qj)                  # jet order q of problem P_q (notes of the lead analyst 09:59Z): datum |cos|^q e^F, m1 target 1/q, Gt_q = A/|Xi|^q, core term 1/(q-1), axis law with exponent q
        self.exit_safe, self.diag = int(exit_safe), int(diag)
        self.broyden_keep = bool(int(broyden_keep)); self.J_broyden = None    # exit mode: Broyden secant updates of J from polished trials (always applied within an iteration; kept across iterations if broyden_keep)
        self.jac, self.jac_its = str(jac), int(jac_its)   # Jacobian source: 'bs' = B-spline FD batch (fast, biased where V_r < 0 lobes exist); 'exit' = one exit-map fixed point per column (safeguarded Anderson, jac_its evaluations each; exact residual differences)   # exit_safe: safeguarded Anderson (solve_safe) for the polish; diag: full_diag (pfwd_diag2) per accepted iterate
        self.SB = None
        self.thA = torch.arange(nA, device=self.dev, dtype=torch.float64) * (2 * math.pi / nA)
        self.g_base = None; self.x_base = None

    # ---------------------------------------------------------------- datum
    def phi(self, th, j):
        """basis function j (0-based): j < K Fourier x-even; then bumps (pairs: 90 deg, 270 deg) per width."""
        if j < self.K:
            n = j + 1
            return torch.sin(n * th) if n % 2 == 1 else torch.cos(n * th)
        k = j - self.K; sig = self.sig[k // 2]; centre = math.pi / 2 if k % 2 == 0 else 3 * math.pi / 2
        dth = torch.remainder(th - centre + math.pi, 2 * math.pi) - math.pi
        return torch.exp(-0.5 * (dth / sig) ** 2)

    def Fexp(self, xB, th):
        """log(A / cos^2) for a batch of unknown vectors xB [B, n] at angles th [B, ...] (broadcast over the batch)."""
        s = torch.zeros(th.shape, device=self.dev, dtype=torch.float64) if th.dim() > 1 else torch.zeros((xB.shape[0],) + th.shape, device=self.dev)
        shp = (xB.shape[0],) + (1,) * (s.dim() - 1)
        for j in range(self.nF):
            s = s + xB[:, j].view(shp) * self.phi(th, j)
        return s

    def qB(self, xB):
        """jet order per state [B]: the unknown x[-2] if qfree else the constant qj."""
        return xB[:, -2] if self.qfree else torch.full((xB.shape[0],), self.qj, device=self.dev, dtype=torch.float64)

    def Afun(self, xB):
        q = self.qB(xB)
        def f(th):                      # th [B, ...]
            shp = (xB.shape[0],) + (1,) * (th.dim() - 1) if th.dim() > 1 else (xB.shape[0],) + (1,) * th.dim()
            return torch.cos(th).abs() ** q.view(shp) * torch.exp(self.Fexp(xB, th))
        return f

    # ---------------------------------------------------------------- batch evaluation
    def ensure(self, p_kernel):
        if self.SB is None or abs(self.SB.pk - p_kernel) > 0.03:
            self.SB = PFwdB(self.Nr, self.Nth, self.lo, self.hi, p_kernel, dev=str(self.dev))

    def evaluate(self, X, nsteps, g_start=None, x_start=None, want_axis=True, g_given=None):
        """X: [B, n] numpy.  Evolves all states (warm start from (g_start, x_start) if given), returns F [B, n] and info list.
        g_given [B, Nr, Nth]: skip the evolution and evaluate the residual of the given states (exit-map fixed points)."""
        X = np.asarray(X, float); B = X.shape[0]
        if self.wd > 0 or self.wD > 0: want_axis = True
        xB = torch.tensor(X, device=self.dev); pB = xB[:, -1]
        self.ensure(float(np.median(X[:, -1])))
        SB = self.SB; S = SB.S
        th_grid = S.th[None, :].expand(B, -1)
        FB = self.Fexp(xB, th_grid)                                     # [B, Nth]
        qB = self.qB(xB)
        A = torch.cos(th_grid).abs() ** qB[:, None] * torch.exp(FB)
        r = S.r
        if g_start is None:
            g = ((r[None, :, None] ** 2 / (1.0 + r[None, :, None] ** 2)) ** (1.0 - pB[:, None, None] / 2)) * A[:, None, :]
        else:
            xs = torch.tensor(np.asarray(x_start, float), device=self.dev)[None]
            Fs = self.Fexp(xs, S.th[None, :])                           # [1, Nth]
            fac = (r[None, :, None] / r[-1]) ** (float(xs[0, -1]) - pB)[:, None, None]
            g = g_start[None] * torch.exp(FB - Fs)[:, None, :] * fac
        t0 = time.time()
        if g_given is not None:
            g = g_given; dg = torch.zeros(B, device=self.dev)
        elif nsteps <= 0:
            dg = torch.zeros(B, device=self.dev)                        # warm start taken as is (g0= option)
        else:
            g, dg = SB.evolve(g, pB, A, self.Afun(xB), self.ds, nsteps)
        t1 = time.time()
        rho = r[None, :, None] ** pB[:, None, None] * g
        Wr, Wt = SB.velocity(rho, pB)
        cm, core = SB.c_moment(rho, pB, A, qj=(qB if self.qfree else self.qj))
        m1 = 1.0 / pB - cm
        T, u0, w0, th0, it, arrived = SB.trace(Wr, Wt, pB, self.thA, self.lr0, dt=self.dt, max_it=8000)   # 8x the normal orbit length; non-arrivals are flagged (arrived_frac)
        Afine = torch.cos(self.thA).abs()[None, :] ** qB[:, None] * torch.exp(self.Fexp(xB, self.thA[None, :].expand(B, -1)))
        logGt = torch.log(torch.clamp(Afine, min=1e-300)) - qB[:, None] * torch.log(torch.clamp(u0.abs(), min=1e-300)) - (qB * m1)[:, None] * T   # Gt_q = A / |Xi|^q
        t2 = time.time()
        # least squares on [1, phi_0..phi_{n-2}] over |cos| > cut (pseudo-inverse with rank protection, computed once)
        msk = (torch.cos(self.thA).abs() > self.cut)
        if getattr(self, '_Phi', None) is None:
            Phi = torch.stack([torch.ones_like(self.thA)] + [self.phi(self.thA, j) for j in range(self.nF)], 1)[msk]   # [M, nF + 1]
            Pn = Phi.cpu().numpy(); svP = np.linalg.svd(Pn, compute_uv=False)
            self._Phi = Phi; self._Pinv = torch.tensor(np.linalg.pinv(Pn, rcond=1e-8), device=self.dev)
            self.emit(dict(lsq_basis=dict(M=int(Pn.shape[0]), n=int(Pn.shape[1]), sv_max=float(svP[0]), sv_min=float(svP[-1]), cond=float(svP[0] / svP[-1]))))
        Phi = self._Phi
        if self.dfree:
            sfun = -0.5 * torch.sin(self.thA)                                                                          # s(-pi/2) - s(pi/2) = 1
            logGt = logGt - xB[:, -2 - self.qfree][:, None] * sfun[None, :]                                               # match log Gt - D s, D the unknown x[-2] (x[-3] if qfree)
        Y = logGt[:, msk].T                                                                                             # [M, B]
        Y = Y - Y.mean(0, keepdim=True)                                                                                 # centre first (referee audit, item 1)
        C = self._Pinv @ Y                                                                                              # [n, B]
        fit = Phi @ C
        rms_un = torch.sqrt(((Y - fit) ** 2).mean(0))
        row_m1 = self.wm * (qB * m1 - 1.0) if self.qfree else self.wm * (m1 - 1.0 / self.qj)
        F = torch.cat([row_m1[None, :], C[1:]], 0).T                                                                    # m1 target 1/q (q m1 = 1 if q is free)                                                   # [B, n]
        Fn = F.cpu().numpy()
        if self.wd > 0:
            Fn = np.concatenate([Fn, np.zeros((B, 2))], 1)                                                              # drift rows filled below
        if self.wD > 0:
            Fn = np.concatenate([Fn, np.zeros((B, 1))], 1)                                                              # D_ax row (a_div) filled below
        lg = (logGt - logGt[:, msk].mean(1, keepdim=True)).cpu().numpy()
        thd = np.degrees(self.thA.cpu().numpy()); at = lambda b, deg: float(lg[b, int(round(deg / 360 * self.nA)) % self.nA])
        bulk = np.abs(np.cos(np.radians(thd))) > 0.3
        infos = []
        for b in range(B):
            d = dict(m1=float(m1[b]), core=float(core[b]), dgds=float(dg[b]), rms_unresolved=float(rms_un[b]), normF=float(np.linalg.norm(Fn[b])),
                     arrived_frac=float(arrived[b].double().mean()),
                     up89=at(b, 89), low269=at(b, 269), D_samp=at(b, 269) - at(b, 89), bulk_std=float(lg[b][bulk].std()),
                     range_cut=float(lg[b][msk.cpu().numpy()].max() - lg[b][msk.cpu().numpy()].min()), gmin=float(g[b].min()))
            d['F_parts'] = dict(m1=float(Fn[b, 0] ** 2), lsq=float((Fn[b, 1:1 + self.nF] ** 2).sum()))      # weighted squared contributions to |F|^2 (D / drift rows added below)
            d['beta1_raw'] = float(Fn[b, 1] - (0.5 * float(xB[b, -2 - self.qfree]) if self.dfree else 0.0))     # raw sin th LSQ coefficient of log Gt (lead 15:02Z metric)
            d['R_reduced'] = float(np.sqrt(Fn[b, 0] ** 2 + (Fn[b, 2:1 + self.nF] ** 2).sum()))                  # physical residual without the sin th row (= min over D of |F| in the dfree form; without axis rows)
            if want_axis:
                try:
                    ax = axis_D(S, g[b], Wr[b], float(pB[b]), float(m1[b]), A=A[b], Wt=Wt[b], qj=float(qB[b]))
                    d.update(D_ax=ax['D_ax_k'], D_ax_res17=ax['D_ax_res17'], drift_up=ax['drift_up'], drift_down=ax['drift_down'],
                             Fp_minus_Fm=ax['Fp_minus_Fm_datum'], e_p=ax['e_p_formula'], a_gap_up=ax.get('a_gap_up'), a_gap_down=ax.get('a_gap_down'),
                             minVr_r=float(((1.0 / pB[b]) + Wr[b] / S.r[:, None]).min()))
                    nextra = (2 if self.wd > 0 else 0) + (1 if self.wD > 0 else 0)
                    if self.wd > 0:
                        j0 = Fn.shape[1] - nextra
                        Fn[b, j0] = self.wd * ax['drift_up']; Fn[b, j0 + 1] = self.wd * ax['drift_down']
                    if self.wD > 0:
                        axd = axis_D(S, g[b], Wr[b], float(pB[b]), float(m1[b]), A=A[b], qj=float(qB[b]), hmode='fd1')          # a_div form, local h (V95)
                        d['D_ax_div'] = axd['D_ax_k']; d['drift_up_div'] = axd['drift_up']
                        Fn[b, -1] = self.wD * axd['D_ax_k']; d['F_parts']['D'] = float(Fn[b, -1] ** 2)
                    if self.wd > 0:
                        d['F_parts']['drift'] = float((Fn[b, j0] ** 2 + Fn[b, j0 + 1] ** 2))
                    if nextra:
                        d['normF'] = float(np.linalg.norm(Fn[b])); d['normF_noExtra'] = float(np.linalg.norm(Fn[b, :-nextra]))
                except Exception as e:
                    d['axis_error'] = str(e)
            infos.append(d)
        timing = dict(evolve=round(t1 - t0, 1), trace=round(t2 - t1, 1), trace_its=it, B=B, nsteps=nsteps)
        return Fn, infos, g, lg, timing

    # ---------------------------------------------------------------- driver
    def emit(self, rec):
        line = json.dumps(rec); print(line, flush=True)
        if self.log: self.log.write(line + '\n'); self.log.flush()

    def save_state(self, x, g, lg, F, info, fn):
        S = self.SB.S
        np.savez(fn, g=g.cpu().numpy(), lr=S.lr.cpu().numpy(), th=S.th.cpu().numpy(), x=np.asarray(x), F=np.asarray(F), logGt=lg, thA=self.thA.cpu().numpy(),
                 hist=json.dumps([info]), args=json.dumps(dict(p=float(x[-1]), kind='bnewton', K=self.K, sigmas=[math.degrees(s) for s in self.sig], par=[float(v) for v in x[:-1]], qj=(float(x[-2]) if self.qfree else self.qj), dfree=self.dfree, qfree=self.qfree)))

    def exit_polish(self, x, g, maxit=None):
        """Exit-map fixed point (code/pfwd_exitmap.py) warm-started from g; returns (g_fp, hist)."""
        maxit = self.exit_maxit if maxit is None else int(maxit)
        from pfwd_exitmap import ExitMap
        xB = torch.tensor(np.asarray(x, float)[None], device=self.dev)
        EM = ExitMap(self.Nr, self.Nth, self.lo, self.hi, float(x[-1]), np.asarray(x[:self.K]), dt=0.01, xeven=True, dev=str(self.dev), qj=float(self.qB(xB)[0]), Afun=self.Afun(xB))   # same datum as the Newton (bumps included; before 10:45Z bump coefficients were read as modes K+1, K+2 by the polish)
        if self.exit_safe:
            g_fp, Tg, hist = EM.solve_safe(g.clone(), maxit=maxit, tol=self.exit_tol, m=6, beta=1.0, log=lambda line: None, orbit_cap=3000, grow=10.0)
        else:
            g_fp, Tg, hist = EM.solve(g.clone(), maxit=maxit, tol=self.exit_tol, m=6, beta=1.0, log=lambda line: None)
        self.emit(dict(polish_hist=[[h.get('kind', 'start')[0], float('%.3g' % h['defect_max']), float('%.3g' % h['defect_rms']), int(h.get('ncells_above_tol', -1)), int(h.get('accepted', True))] for h in hist if not h.get('final')],
                       converged=bool(hist[-1].get('converged', hist[-1]['defect_max'] < self.exit_tol)), ncells=hist[-1].get('ncells_above_tol'), rms_rest=hist[-1].get('rms_rest'), wall=hist[-1]['wall']))
        return g_fp, hist

    def full_diag(self, x, g, it):
        """lead's continuation diagnostics (code/pfwd_diag2.py) on the current base state; emitted as one JSON record."""
        try:
            from pfwd_diag2 import full_diag, summary_line
            xB = torch.tensor(np.asarray(x, float)[None], device=self.dev)
            d = full_diag(self.SB, g, float(x[-1]), np.asarray(x[:self.K]), qj=float(self.qB(xB)[0]), Afun=self.Afun(xB))
            d['it'] = it; d['diag'] = True; d['D_unknown'] = float(x[-2 - self.qfree]) if self.dfree else None; d['q_unknown'] = float(x[-2]) if self.qfree else None
            self.emit(d); print(summary_line(d, '%s_it%d' % (self.tag, it)), flush=True)
        except Exception as e:
            self.emit(dict(it=it, diag_error=str(e)))

    def newton(self, x0, maxit=10, mu0=1e-2, da_max=0.3, dp_max=0.04, tol=1e-4, lams=(1.0, 0.6, 0.35, 0.2, 0.1), nsteps0=1500, outdir='runs/pfwd/bn', g_start=None, x_start=None):
        os.makedirs(outdir, exist_ok=True)
        x = np.asarray(x0, float); mu = mu0
        F, infos, g, lg, tm = self.evaluate(x[None], nsteps0, g_start=g_start, x_start=x_start)
        F = F[0]; g = g[0]; info = infos[0]
        if self.exit:
            g, eh = self.exit_polish(x, g)
            F, infos, gg, lg, tm = self.evaluate(x[None], 0, g_given=g[None]); F = F[0]; info = infos[0]
            info['exit_defect'] = eh[-1]['defect_max']; info['exit_its'] = len(eh)
            self.emit(dict(it=0, exit_polish=True, defect=eh[-1]['defect_max'], its=len(eh), normF=info['normF'], m1=info['m1']))
        self.emit(dict(it=0, x=[round(float(v), 6) for v in x], normF=info['normF'], info=info, timing=tm))
        self.save_state(x, g, lg[0], F, info, '%s/%s_it0.npz' % (outdir, self.tag))
        if self.diag: self.full_diag(x, g, 0)
        for it in range(1, maxit + 1):
            if info['normF'] < tol:
                self.emit(dict(it=it, converged=True)); break
            # Jacobian
            hs = np.array([self.h_a] * self.K + [self.h_b] * self.nb + ([0.02] if self.dfree else []) + ([0.01] if self.qfree else []) + [self.h_p])
            if self.exit and self.broyden_keep and getattr(self, 'J_broyden', None) is not None and self.J_broyden.shape == (len(F), self.n):
                J = self.J_broyden                                             # secant-updated Jacobian of the previous iteration kept (no recomputation)
                self.emit(dict(it=it, jacobian='broyden_kept', sv=[float('%.4g' % v) for v in np.linalg.svd(J, compute_uv=False)]))
            elif self.exit and self.jac == 'exit':
                # exact-residual FD Jacobian: one safeguarded exit-map fixed point per column from the rescaled base (jac_its evaluations each)
                J = np.zeros((len(F), self.n)); tJ = time.time(); colrec = []
                for j in range(self.n):
                    if self.fix2 and j == 1:
                        continue
                    if self.dfree and j == self.n - 2 - self.qfree:
                        J[1, j] = 0.5                                          # D enters only the sin th LSQ row (log Gt - D s, s = -(1/2) sin th): exact
                        continue
                    xj = x.copy(); xj[j] += hs[j]
                    F0j, inf0j, g0j, lg0j, tm0j = self.evaluate(xj[None], 0, g_start=g, x_start=x, want_axis=False)       # rescaled base as the start
                    gj, ehj = self.exit_polish(xj, g0j[0], maxit=self.jac_its)
                    Fj, infj, ggj, lgj, tmj = self.evaluate(xj[None], 0, g_given=gj[None], want_axis=False)
                    J[:, j] = (Fj[0] - F) / hs[j]
                    colrec.append([j, round(float(ehj[-1]['defect_max']), 6), int(ehj[-1].get('ncells_above_tol', -1)), bool(ehj[-1].get('converged', False)), round(float(np.linalg.norm(Fj[0] - F)), 6), round(float(infj[0]['m1'] - info['m1']) / hs[j], 4), float('%.3g' % ehj[-1]['defect_rms'])])   # [col, defect max, ncells, converged, |dF|, dm1/dx, defect rms]
                    self.emit(dict(it=it, jac_col=colrec[-1], wall=round(time.time() - tJ, 1)))
                FJ = None
                self.emit(dict(it=it, jacobian='exit', sv=[float('%.4g' % v) for v in np.linalg.svd(J, compute_uv=False)], cols=colrec, wall=round(time.time() - tJ, 1)))
            else:
                Xp = np.repeat(x[None], self.n + 1, 0)
                for j in range(self.n):
                    Xp[j + 1, j] += hs[j]
                FJ, infJ, gJ, lgJ, tmJ = self.evaluate(Xp, self.nsteps_J, g_start=g, x_start=x, want_axis=False)
                J = (FJ[1:] - FJ[0][None, :]).T / hs[None, :]
                if not self.exit:
                    F = FJ[0]; g = gJ[0]                                       # refreshed base (referee audit, item 2); in exit mode the exact base residual and the fixed point are kept (fix 11:20Z)
                sv = np.linalg.svd(J, compute_uv=False)
                m1cols = [round(float(infJ[j + 1]['m1'] - infJ[0]['m1']) / hs[j], 4) for j in range(self.n)]
                self.emit(dict(it=it, jacobian=True, sv=[float('%.4g' % v) for v in sv], dm1_dx=m1cols, base_m1_J=infJ[0]['m1'], normF_J=infJ[0]['normF'], timing=tmJ,
                               dgds_max=max(d['dgds'] for d in infJ)))
            np.savez('%s/%s_J%d.npz' % (outdir, self.tag, it), J=J, x=x, F=F, hs=hs)
            self.J_broyden = J
            if self.fix2:
                J[:, 1] = 0.0                                                   # a_2 frozen: no step in it (its column is removed from the solve)
            JTJ = J.T @ J; Dm = np.diag(np.maximum(np.diag(JTJ), max(1e-12 * np.diag(JTJ).max(), 1e-14)))
            if self.fix2:
                JTJ[1, 1] = 1.0; Dm[1, 1] = 1.0
            accepted = False
            jD = (self.n - 2 - self.qfree) if self.dfree else None          # index of the D unknown (its Jacobian column is exact: 1/2 on the sin th row, 0 elsewhere)
            def restore_D_column(Jm):
                if jD is not None:
                    Jm[:, jD] = 0.0; Jm[1, jD] = 0.5
                return Jm
            for attempt in range(4):
                J_frozen = J.copy()                                              # the matrix used for this attempt's direction and for the realised / predicted ratio (referee audit, item 4.2)
                dx = -np.linalg.solve(JTJ + mu * Dm, J.T @ F)
                if self.fix2: dx[1] = 0.0
                sc = max(1.0, np.abs(dx[:-1]).max() / da_max, abs(dx[-1]) / dp_max)
                dx = dx / sc
                Xt = np.stack([x + lam * dx for lam in lams] + [x])          # last member: zero-displacement control
                Xt[:, -1] = np.clip(Xt[:, -1], 0.12, 0.9)
                if self.qfree: Xt[:, -2] = np.clip(Xt[:, -2], 1.2, 2.5)
                Ft, inft, gt, lgt, tmt = self.evaluate(Xt, self.nsteps_T, g_start=g, x_start=x)
                norms = [d['normF'] if (np.isfinite(d['normF']) and d['arrived_frac'] > 0.999 and not ((self.wd > 0 or self.wD > 0) and d.get('axis_error') is not None)) else float('inf') for d in inft]   # a failed axis evaluation invalidates a trial whose residual has axis rows (referee audit, item 4.3)
                ctrl = norms[-1]
                pred = [float(np.linalg.norm(F + J @ (Xt[i] - x))) for i in range(len(lams))]
                self.emit(dict(it=it, trial=attempt, mu=mu, step_scale=1 / sc, dx_norm=float(np.linalg.norm(dx)), lams=list(lams), normF_try=[round(v, 6) for v in norms[:-1]],
                               normF_ctrl=round(ctrl, 6), pred=[round(v, 6) for v in pred], m1_try=[round(d['m1'], 5) for d in inft], p_try=[round(float(v), 5) for v in Xt[:, -1]], timing=tmt))
                k = int(np.argmin(norms[:-1]))
                if self.exit:
                    # exact residuals: polish the trials in decreasing lam order until one decreases the exact base residual (each polish ~ exit_maxit T evaluations)
                    ctrl = info['normF']; k = None
                    for kk in range(len(lams)):
                        if not (np.isfinite(norms[kk]) or self.nsteps_T == 0):
                            continue
                        g_fp, eh = self.exit_polish(Xt[kk], gt[kk])
                        Fe, infe, gge, lge, tme = self.evaluate(Xt[kk][None], 0, g_given=g_fp[None])
                        infe[0]['exit_defect'] = eh[-1]['defect_max']; infe[0]['exit_its'] = len(eh); infe[0]['exit_converged'] = bool(eh[-1].get('converged', eh[-1]['defect_max'] < self.exit_tol))
                        self.emit(dict(it=it, exit_polish=True, lam=lams[kk], defect=eh[-1]['defect_max'], its=len(eh), converged=infe[0]['exit_converged'], normF_bs=norms[kk], normF_exit=infe[0]['normF'], m1_bs=inft[kk]['m1'], m1_exit=infe[0]['m1']))
                        Ft[kk] = Fe[0]; gt[kk] = g_fp; inft[kk] = infe[0]; lgt[kk] = lge[0]
                        norms[kk] = infe[0]['normF'] if not ((self.wd > 0 or self.wD > 0) and infe[0].get('axis_error') is not None) else float('inf')
                        # Broyden secant update of the (B-spline) Jacobian with the exact residual pair (Xt[kk] - x, Fe - F)
                        dxk = Xt[kk] - x; nn = float(dxk @ dxk)
                        if nn > 0 and np.all(np.isfinite(Fe[0])) and infe[0].get('axis_error') is None:
                            J = J + np.outer((Fe[0] - F) - J @ dxk, dxk) / nn
                            if self.fix2: J[:, 1] = 0.0
                            J = restore_D_column(J)                                 # Broyden must not touch the exact D column (referee audit, item 4.1)
                            self.J_broyden = J
                        if norms[kk] < ctrl:
                            k = kk; break
                    if k is None:
                        k = int(np.argmin(norms[:-1]))
                        JTJ = J.T @ J; Dm = np.diag(np.maximum(np.diag(JTJ), max(1e-12 * np.diag(JTJ).max(), 1e-14)))
                        if self.fix2: JTJ[1, 1] = 1.0; Dm[1, 1] = 1.0
                if norms[k] < ctrl:
                    pred_dec = ctrl - float(np.linalg.norm(F + J_frozen @ (Xt[k] - x))); real_dec = ctrl - norms[k]       # prediction with the matrix frozen before this trial
                    ratio = real_dec / pred_dec if pred_dec > 0 else float('nan')
                    if self.exit and self.broyden_keep and np.isfinite(ratio) and ratio < 0.3:
                        self.J_broyden = None                                      # realised / predicted decrease below 0.3: recompute the exact Jacobian next iteration (lead 14:21Z)
                    self.emit(dict(it=it, step_quality=dict(predicted_decrease=pred_dec, realised_decrease=real_dec, ratio=ratio, recompute_J=(self.J_broyden is None))))
                    x = Xt[k]; F = Ft[k]; g = gt[k]; info = inft[k]; lgk = lgt[k]
                    mu = max(mu / 3, 1e-6); accepted = True
                    self.emit(dict(it=it, accepted=True, lam=lams[k], x=[round(float(v), 6) for v in x], normF=info['normF'], info=info))
                    self.save_state(x, g, lgk, F, info, '%s/%s_it%d.npz' % (outdir, self.tag, it))
                    if self.diag: self.full_diag(x, g, it)
                    break
                mu *= 10
            if not accepted:
                self.emit(dict(it=it, accepted=False, note='no decrease after 4 LM attempts'))
                break
        self.g_last = g; self.x_last = x; self.info_last = info
        return x, F, info


if __name__ == '__main__':
    # usage: python3 code/pfwd_bnewton.py tag K "sig1,sig2|0" p0 "a1,...,aK[,b...]" [maxit=10] [wm=3] [cut=0.02] [h_a=0.01] [h_p=0.004]
    #        [nsteps_J=700] [nsteps_T=900] [nsteps0=1500] [mu0=0.01] [da_max=0.3] [dp_max=0.04] [lo=-14] [Nr=721] [lr0=-13] [Nth=256] [lincheck=j:h1,h2,...]
    tag = sys.argv[1]; K = int(sys.argv[2]); sig = [float(v) for v in sys.argv[3].split(',')] if sys.argv[3] != '0' else []
    p0 = float(sys.argv[4]); a0 = [float(v) for v in sys.argv[5].split(',')]
    opt = dict(maxit=10, wm=3.0, cut=0.02, h_a=0.01, h_p=0.004, nsteps_J=700, nsteps_T=900, nsteps0=1500, mu0=0.01, da_max=0.3, dp_max=0.04, lo=-14.0, Nr=721, lr0=-13.0, Nth=256, lincheck='', wd=0.0, exit=0, exit_maxit=20, exit_tol=2e-5, lams='1.0,0.6,0.35,0.2,0.1', wD=0.0, dfree=0, fix2=0, D0=0.0, g0='', exit_safe=1, diag=0, qj=2.0, qfree=0, q0=2.0, jac='bs', jac_its=10, broyden_keep=0, J0='')
    for s_ in sys.argv[6:]:
        k, v = s_.split('=', 1); opt[k] = v if k in ('lincheck', 'lams', 'g0', 'jac', 'J0') else (int(v) if k in ('maxit', 'nsteps_J', 'nsteps_T', 'nsteps0', 'Nr', 'Nth', 'exit', 'exit_maxit', 'dfree', 'fix2', 'exit_safe', 'diag', 'qfree', 'jac_its', 'broyden_keep') else float(v))
    os.makedirs('runs/pfwd/bn', exist_ok=True)
    log = open('runs/pfwd/bn/%s.log' % tag, 'a')
    BN = BNewton(K, sig, Nr=opt['Nr'], Nth=opt['Nth'], lo=opt['lo'], lr0=opt['lr0'], cut=opt['cut'], wm=opt['wm'], nsteps_J=opt['nsteps_J'], nsteps_T=opt['nsteps_T'],
                 h_a=opt['h_a'], h_p=opt['h_p'], log=log, tag=tag, wd=opt['wd'], exit=opt['exit'], exit_maxit=opt['exit_maxit'], exit_tol=opt['exit_tol'], wD=opt['wD'], dfree=opt['dfree'], fix2=opt['fix2'], exit_safe=opt['exit_safe'], diag=opt['diag'], qj=opt['qj'], qfree=opt['qfree'], jac=opt['jac'], jac_its=opt['jac_its'], broyden_keep=opt['broyden_keep'])
    n = BN.n
    x0 = np.zeros(n); x0[:len(a0)] = a0; x0[-1] = p0
    if opt['qfree']: x0[-2] = opt['q0']                        # initial jet order for the dual run
    if opt['dfree']: x0[-2 - opt['qfree']] = opt['D0']         # initial guess for the free D (e.g. the measured D_ax of the start)
    BN.emit(dict(tag=tag, K=K, sigmas=sig, n=n, x0=x0.tolist(), opt=opt, start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    if opt['lincheck']:
        j, hs = opt['lincheck'].split(':'); j = int(j); hs = [float(v) for v in hs.split(',')]
        F0, inf0, g0, lg0, tm0 = BN.evaluate(x0[None], opt['nsteps0'])
        X = np.repeat(x0[None], len(hs), 0)
        for i, h in enumerate(hs): X[i, j] += h
        F, infs, g, lg, tm = BN.evaluate(X, opt['nsteps_T'], g_start=g0[0], x_start=x0)
        BN.emit(dict(lincheck=j, base=dict(m1=inf0[0]['m1'], normF=inf0[0]['normF'], D_ax=inf0[0].get('D_ax')), timing=tm))
        for i, h in enumerate(hs):
            BN.emit(dict(h=h, m1=infs[i]['m1'], dm1=infs[i]['m1'] - inf0[0]['m1'], slope=(infs[i]['m1'] - inf0[0]['m1']) / h, D_ax=infs[i].get('D_ax'), dF=[round(float(v), 5) for v in (F[i] - F0[0])], dgds=infs[i]['dgds']))
        sys.exit(0)
    g_start = x_start = None
    if opt['J0']:
        # initial Jacobian from a saved *_J*.npz (rows must match the present residual; a D column of a dfree run is dropped when the present run has dfree=0)
        JJ = np.load(opt['J0'], allow_pickle=True)['J']
        if JJ.shape[1] == n + 1 and not opt['dfree']:
            JJ = np.delete(JJ, JJ.shape[1] - 2, axis=1)                            # drop the D column (second to last) of the dfree Jacobian
        assert JJ.shape[1] == n, (JJ.shape, n)
        BN.J_broyden = JJ; BN.broyden_keep = True
        BN.emit(dict(J0=opt['J0'], shape=list(JJ.shape), sv=[float('%.4g' % v) for v in np.linalg.svd(JJ, compute_uv=False)]))
    if opt['g0']:
        # warm start from a saved state (exit-map _fp.npz / bnewton iterate / bscan member): angular subsampling if its Nth is a multiple of Nth;
        # datum and p rescaled inside evaluate() (g exp(F_new - F_old) (r/r_max)^(p_old - p_new)); nsteps0 B-spline steps (0 = none) then the polish
        dd = np.load(opt['g0'], allow_pickle=True); gsrc = dd['g']; asrc = json.loads(str(dd['args'])); p_src = float(asrc['p'])
        coef_src = np.array(asrc['par']) if 'par' in asrc else dd['x'][:-1]
        if gsrc.shape[1] != opt['Nth']:
            assert gsrc.shape[1] % opt['Nth'] == 0, (gsrc.shape, opt['Nth']); gsrc = gsrc[:, ::gsrc.shape[1] // opt['Nth']]
        assert gsrc.shape[0] == opt['Nr'] and abs(float(dd['lr'][0]) - opt['lo']) < 1e-9, 'radial grid of g0 must match'
        x_start = np.zeros(n); x_start[:min(len(coef_src), K)] = coef_src[:K]; x_start[-1] = p_src
        if opt['dfree']: x_start[-2 - opt['qfree']] = x0[-2 - opt['qfree']]
        if opt['qfree']: x_start[-2] = x0[-2]
        g_start = torch.tensor(gsrc, device='cuda')
        BN.emit(dict(warm_start=opt['g0'], p_src=p_src, coef_src=[float(v) for v in coef_src], Nth_src=int(dd['g'].shape[1]), nsteps0=opt['nsteps0']))
    BN.newton(x0, maxit=opt['maxit'], mu0=opt['mu0'], da_max=opt['da_max'], dp_max=opt['dp_max'], nsteps0=opt['nsteps0'], lams=tuple(float(v) for v in opt['lams'].split(',')), g_start=g_start, x_start=x_start)
    BN.emit(dict(tag=tag, done=True, end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    print("BNEWTON_DONE", flush=True)
