"""Parity-free profile search (notes of the lead analyst 2026-10-18T16:05Z; PROMPT numerical program item 4).
Datum with BOTH parities and Gamma-slaved zeros (code/pfwd_gnewton.GammaMap):
    A(th) = 4 sin^2((th - th_1)/2) sin^2((th - th_2)/2) exp(F(th)),   F = sum_j a_j phi_j (x-even modes) + sum_j b_j chi_j (x-odd modes),
    phi: sin(n th) (n odd), cos(n th) (n even);  chi: cos(n th) (n odd), sin(n th) (n even);  th_1, th_2 = exit angles of the strong unstable
    manifold of the current velocity (so A vanishes exactly where Gamma reaches infinity: the necessary Gamma matching of R19(f)).
    At b = 0 and th_1, th_2 = 90 / 270 deg this is the x-even datum cos^2 th e^F of the DR runs.
State solver: UNPROJECTED safeguarded Anderson iteration of the Gamma-slaved exit map (no parity projection of the state; optional
    projection only for the consistency test against the x-even solver).
Unknowns x = (a_1..a_K, b_1..b_Ko, p).  Rows (weighted):
    wm (m1 - 1/2)                       m1 = 1/p - c, c = psi_xy(0) by the sin 3th moment with the core term (as in the x-even runs)
    even LSQ (K)                        least-squares coefficients of log Gt - mean on phi_1..phi_K over the exit labels off the zero windows
    odd LSQ (Ko)                        the same on chi_1..chi_Ko (vanish identically at x-even states)
    wD D_ax                             axis-formula up/down mismatch (a_div form, y-axis columns; exact for x-even states, an O(b^2)-biased proxy otherwise)
    wM M_up, wM M_dn                    x-odd matching rows at the two strong exits: mean of log Gt - mean over the band (th_z + 0.5 .. 2.5 deg) minus the
                                        band (th_z - 2.5 .. -0.5 deg) of exit labels; a sampled proxy for G(th_z+) - G(th_z-) (one-sided window limits)
    wO psi_yy(0)                        orientation: psi_yy(0) = -(1/pi) int rho r^-3 cos 3th dX (grid + tail + core term), x-odd; psi_xx(0) = -psi_yy(0)
                                        by the Poisson equation at the origin (rho_x(0) = 0 for these states); ring estimates DW(0) at lr -12 / -10 reported.
log Gt = log A(th) - 2 log|u0| - 2 m1 T from backward orbits (r_max, th) -> lr0 (u0 = x coordinate at arrival, as in the x-even runs).
Jacobian: one unprojected fixed point per column (warm start = base state rescaled by exp(dF) (r/r_max)^(dp), jac_its evaluations).
LM search with trial polishes and Broyden updates as in code/pfwd_bnewton.py.
"""
import sys, json, math, time, os
import numpy as np
import torch
sys.path.insert(0, 'code')
from pfwd_batch import PFwdB
from pfwd_gnewton import GammaMap
from pfwd_diag import axis_D
torch.set_default_dtype(torch.float64)


class ParityMap(GammaMap):
    def __init__(self, Nr, Nth, lo, hi, p, F_even, F_odd, dt=0.01, dev='cuda', orbit_cap=3000, lr_g=-12.0, xeven=False, nA=1440, lr0=-13.0, cut=0.02,
                 band=(0.5, 2.5), wm=50.0, wD=5.0, wM=5.0, wO=50.0, thr=1e-3, slave=True, wG=50.0):
        super().__init__(Nr, Nth, lo, hi, p, F_even, F_odd, dt=dt, dev=dev, orbit_cap=orbit_cap, lr_g=lr_g)
        self.slave = bool(slave); self.wG = float(wG); self.dth12 = np.zeros(2)     # slave=False: datum zeros th_1 = pi/2 + dth12[0], th_2 = 3pi/2 + dth12[1] are UNKNOWNS, Gamma matching = two rows wG (th_exit,z - th_z)
        self.xeven = bool(xeven); self.nA = int(nA); self.lr0 = float(lr0); self.cut = float(cut); self.band = band; self.thr = float(thr)
        self.band_offsets = [0.75, 1.25, 1.75, 2.25]                                # degrees from each zero: paired traced labels th_z +- delta for the band rows
        self.wm, self.wD, self.wM, self.wO = float(wm), float(wD), float(wM), float(wO); self.safe = True
        self.solver = 'anderson'; self.newton_steps = 2; self.newton_kmax = 25; self.resp = {}        # resp: linear state responses dg/dx_j (torch [Nr, Nth]) for warm starts
        self.thA = torch.arange(self.nA, device=dev, dtype=torch.float64) * (2 * math.pi / self.nA)
        self.K = len(self.F_even); self.Ko = len(self.F_odd); nz = 0 if self.slave else 2
        self.n = self.K + self.Ko + nz + 1
        self.nrows = 1 + self.K + self.Ko + 4 + nz
        self.row_names = ['m1'] + ['a%d' % (j + 1) for j in range(self.K)] + ['b%d' % (j + 1) for j in range(self.Ko)] + ['D_ax', 'M_up', 'M_dn', 'psi_yy0'] + (['G_up', 'G_dn'] if nz else [])
        self.col_names = ['a%d' % (j + 1) for j in range(self.K)] + ['b%d' % (j + 1) for j in range(self.Ko)] + (['t1', 't2'] if nz else []) + ['p']
        self.odd_rows = np.array([False] + [False] * self.K + [True] * self.Ko + [False, True, True, True] + [True] * nz)
        self.odd_cols = np.array([False] * self.K + [True] * self.Ko + [True] * nz + [False])

    # ---------------------------------------------------------------- datum / parameters
    def zeros(self):
        return (math.pi / 2 + float(self.dth12[0]), 3 * math.pi / 2 + float(self.dth12[1]))

    def set_x(self, x):
        x = np.asarray(x, float); self.F_even = x[:self.K].copy(); self.F_odd = x[self.K:self.K + self.Ko].copy(); p = float(x[-1])
        if not self.slave: self.dth12 = x[self.K + self.Ko:self.K + self.Ko + 2].copy(); self.th12 = self.zeros()
        if abs(p - self.p) > 0:
            self.p = p; self.pB = torch.tensor([p], device=self.dev); self.scale = ((self.S.r ** 2 / (1.0 + self.S.r ** 2)) ** (1.0 - p / 2))[:, None]
        if abs(p - self.SB.pk) > 0.03:                                            # kernel p (per-state tail correction validated at +-0.01)
            self.SB = PFwdB(self.S.Nr, self.S.Nth, self.S.lo, self.S.hi, p, dev=str(self.dev)); self.S = self.SB.S
    def get_x(self):
        return np.concatenate([self.F_even, self.F_odd, ([] if self.slave else self.dth12), [self.p]])

    def T(self, g, return_all=False):
        """exit map: datum zeros slaved to the strong-manifold exits (slave=True, GammaMap.T) or FIXED at the datum's own zeros (slave=False; the exits are still computed
        and reported for the Gamma rows)."""
        if self.slave:
            return GammaMap.T(self, g, return_all=return_all)
        S = self.S
        Wr, Wt, rho = self.velocity(g); rhs = self._fields(Wr, Wt)
        the1, the2, ok = self.gamma_angles(rhs)
        LR, TH, Tt, live, it = self._orbits(rhs, self.LR.clone(), self.TH.clone(), self.orbit_cap)
        th1, th2 = self.zeros()
        Tg = (torch.exp(-Tt) * math.exp(self.p * S.hi) * self.Afun(TH, (th1, th2))).reshape(S.Nr, S.Nth) / S.r[:, None] ** self.p
        info = dict(th1_deg=math.degrees(th1), th2_deg=math.degrees(th2), exit1_deg=math.degrees(the1), exit2_deg=math.degrees(the2), gamma_ok=ok, orbit_its=it, unfinished=int(live.sum()))
        if return_all:
            return Tg, info, Wr, Wt, rho
        return Tg, info

    def project(self, g):
        return 0.5 * (g + g[:, self.flip]) if self.xeven else g

    def Tp(self, g):
        Tg, info = self.T(g)
        return self.project(Tg), info

    def defect(self, g, Tg, tol=None):
        rowmax = g.max(dim=1, keepdim=True).values
        msk = (g > self.thr * rowmax) | (Tg > self.thr * rowmax)                   # cells where g OR Tg is significant (referee audit, item 6: old zeros must not hide a wrong image)
        d = torch.where(msk, (Tg - g).abs() / rowmax, torch.zeros_like(g))
        if tol is None:
            return float(d.max()), float(torch.sqrt((d ** 2).sum() / msk.sum()))
        bad = d > tol; d2 = torch.where(bad, torch.zeros_like(d), d)
        return float(d.max()), float(torch.sqrt((d ** 2).sum() / msk.sum())), int(bad.sum()), float(torch.sqrt((d2 ** 2).sum() / msk.sum()))

    def warm_start(self, g, x_old, x_new):
        """base state rescaled to the new datum: g exp(F_new - F_old) (r/r_max)^(p_old - p_new) (zero factors untouched)."""
        xo = np.asarray(x_old, float); xn = np.asarray(x_new, float)
        Fo_e, Fo_o = self.F_even, self.F_odd
        self.F_even, self.F_odd = xo[:self.K], xo[self.K:self.K + self.Ko]; Fo = self.Fexp(self.S.th[None, :])
        self.F_even, self.F_odd = xn[:self.K], xn[self.K:self.K + self.Ko]; Fn = self.Fexp(self.S.th[None, :])
        self.F_even, self.F_odd = Fo_e, Fo_o
        fac = (self.S.r / self.S.r[-1]) ** (float(xo[-1]) - float(xn[-1]))
        if self.resp:                                                                # unknowns with a TOTAL linear state response: no datum rescaling for them (referee audit: double counting otherwise)
            xn2 = np.asarray(xn, float).copy()
            for j in self.resp:
                if j < self.K + self.Ko: xn2[j] = xo[j]
            self.F_even, self.F_odd = xn2[:self.K], xn2[self.K:self.K + self.Ko]; Fn = self.Fexp(self.S.th[None, :])
            self.F_even, self.F_odd = Fo_e, Fo_o
        g_ws = g * torch.exp(Fn - Fo) * fac[:, None]
        for j, dg in self.resp.items():                                              # first-order state responses (from the linear-response columns) for the unknowns that have them
            d = float(xn[j] - xo[j])
            if d != 0.0:
                g_ws = g_ws + d * dg
        return g_ws.clamp(min=0.0)

    # ---------------------------------------------------------------- state solver (safeguarded Anderson, unprojected)
    def solve_safe(self, g0, maxit=30, tol=1e-5, m=6, beta=1.0, log=None, grow=10.0, beta_min=1.0 / 64, grow_picard=2.0, ncell_tol=8, rms_rest_tol=None):
        log = log or (lambda s: None)
        g = self.project(g0.clone()); hist = []; X = []; Fh = []
        u = (g / self.scale).reshape(-1); t0 = time.time()
        rms_rest_tol = tol / 10 if rms_rest_tol is None else rms_rest_tol
        Tg, info = self.Tp(g); dmax, drms, nbad, drest = self.defect(g, Tg, tol); f = (Tg / self.scale).reshape(-1) - u
        rec = dict(it=0, defect_max=dmax, defect_rms=drms, ncells_above_tol=nbad, rms_rest=drest, unfinished=info['unfinished'], th12=[round(info['th1_deg'], 4), round(info['th2_deg'], 4)], accepted=True, beta_f=beta, wall=round(time.time() - t0, 1))
        hist.append(rec); log(json.dumps(rec))
        conv = lambda dm, nb, dr: (dm < tol) or (nb <= ncell_tol and dr < rms_rest_tol)
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
            Tg_new, info = self.Tp(g_new); dmax_new, drms_new, nbad_new, drest_new = self.defect(g_new, Tg_new, tol); k += 1
            ok = (info['unfinished'] == 0) and info.get('gamma_ok', True) and np.isfinite(dmax_new) and (drms_new <= grow * drms_best) and (kind == 'anderson' or drms_new <= grow_picard * drms)
            rec = dict(it=k, kind=kind, defect_max=dmax_new, defect_rms=drms_new, ncells_above_tol=nbad_new, rms_rest=drest_new, unfinished=info['unfinished'], th12=[round(info['th1_deg'], 4), round(info['th2_deg'], 4)], accepted=bool(ok), beta_f=beta_f, nfail=nfail, wall=round(time.time() - t0, 1))
            hist.append(rec); log(json.dumps(rec))
            if ok:
                u = u_new; g = g_new; Tg = Tg_new; dmax, drms, nbad, drest = dmax_new, drms_new, nbad_new, drest_new; f = (Tg / self.scale).reshape(-1) - u
                nacc += 1; drms_best = min(drms_best, drms)
                if nfail > 0: nfail = 0; beta_f = min(beta, 2 * beta_f)
                elif beta_f < beta: beta_f = min(beta, 2 * beta_f)
            else:
                X.clear(); Fh.clear(); nfail += 1; beta_f *= 0.5
                if beta_f < beta_min:
                    log(json.dumps(dict(giveup=True, beta_f=beta_f))); break
        hist.append(dict(it=len(hist), defect_max=dmax, defect_rms=drms, ncells_above_tol=nbad, rms_rest=drest, converged=bool(conv(dmax, nbad, drest)), final=True, accepted_steps=nacc, evaluations=k + 1, wall=round(time.time() - t0, 1)))
        log(json.dumps(hist[-1]))
        return g, Tg, hist


    def solve_plain(self, g0, maxit=30, tol=1e-5, m=6, beta=1.0, log=None):
        """Plain Anderson (no growth safeguards; orbit cap only), as ExitMap.solve, unprojected unless self.xeven."""
        log = log or (lambda s_: None)
        g = self.project(g0.clone()); hist = []; X = []; Fh = []
        u = (g / self.scale).reshape(-1); t0 = time.time()
        for k in range(maxit):
            Tg, info = self.Tp(g); dmax, drms, nbad, drest = self.defect(g, Tg, tol); Tu = (Tg / self.scale).reshape(-1); f = Tu - u
            rec = dict(it=k, defect_max=dmax, defect_rms=drms, ncells_above_tol=nbad, rms_rest=drest, unfinished=info['unfinished'], th12=[round(info['th1_deg'], 4), round(info['th2_deg'], 4)], godd=float(torch.sqrt(((g - g[:, self.flip]) ** 2).mean() / (g ** 2).mean())), wall=round(time.time() - t0, 1))
            hist.append(rec); log(json.dumps(rec))
            if (dmax < tol) or (nbad <= 8 and drest < tol / 10) or not np.isfinite(dmax):
                break
            X.append(u.clone()); Fh.append(f.clone())
            if len(X) > m + 1:
                X.pop(0); Fh.pop(0)
            if len(X) >= 2:
                dF = torch.stack([Fh[i + 1] - Fh[i] for i in range(len(Fh) - 1)], 1); dX = torch.stack([X[i + 1] - X[i] for i in range(len(X) - 1)], 1)
                gam = torch.linalg.lstsq(dF, f[:, None]).solution[:, 0]
                u = u + beta * f - (dX + beta * dF) @ gam
            else:
                u = u + beta * f
            g = self.project((u.reshape(self.S.Nr, self.S.Nth) * self.scale).clamp(min=0.0))
        Tg, info = self.Tp(g); dmax, drms, nbad, drest = self.defect(g, Tg, tol)
        hist.append(dict(it=len(hist), defect_max=dmax, defect_rms=drms, ncells_above_tol=nbad, rms_rest=drest, converged=bool((dmax < tol) or (nbad <= 8 and drest < tol / 10)), final=True, evaluations=len(hist) + 1, unfinished=info['unfinished'], wall=round(time.time() - t0, 1)))
        log(json.dumps(hist[-1]))
        return g, Tg, hist

    def solve(self, g0, maxit=30, tol=1e-5, log=None):
        if getattr(self, 'solver', 'anderson') == 'newton':
            return self.solve_newton(g0, maxit=self.newton_steps, kmax=self.newton_kmax, tol=tol, log=log)
        if getattr(self, 'solver', 'anderson') == 'newtonm':
            return self.solve_newton_masked(g0, maxit=self.newton_steps, kmax=self.newton_kmax, tol=tol, log=log, **getattr(self, 'nm_opts', {}))
        return self.solve_safe(g0, maxit=maxit, tol=tol, log=log) if self.safe else self.solve_plain(g0, maxit=maxit, tol=tol, log=log)

    def solve_newton(self, g0, maxit=2, kmax=25, tol=1e-5, log=None, eps_rel=1e-3):
        """Newton-GMRES on R(u) = u - T(u)/scale (unprojected, matrix-free, backtracking line search), as pfwd_gnewton.newton_gmres but returning the
        (g, Tg, hist) triple of the other solvers; hist records per Newton step the defect (located-cell criterion as in solve_safe)."""
        log = log or (lambda s_: None)
        S = self.S; g = g0.clone(); u = (g / self.scale).reshape(-1); t0 = time.time(); hist = []; nT = 0
        def R_of(u_, clip=True):
            g_ = (u_.reshape(S.Nr, S.Nth) * self.scale)
            if clip: g_ = g_.clamp(min=0.0)
            Tg_, info_ = self.Tp(g_)
            return u_ - (Tg_ / self.scale).reshape(-1), g_, Tg_, info_
        R, g, Tg, info = R_of(u); nT += 1
        conv = lambda dm, nb, dr: (dm < tol) or (nb <= 8 and dr < tol / 10)
        dmax, drms, nbad, drest = self.defect(g, Tg, tol)
        rec = dict(it=0, kind='newton', defect_max=dmax, defect_rms=drms, ncells_above_tol=nbad, rms_rest=drest, unfinished=info['unfinished'], th12=[round(info['th1_deg'], 4), round(info['th2_deg'], 4)], R2=float(R.norm()), accepted=True, wall=round(time.time() - t0, 1))
        hist.append(rec); log(json.dumps(rec))
        for it in range(1, maxit + 1):
            if conv(dmax, nbad, drest):
                break
            b = -R; beta = float(b.norm()); V = [b / beta]; H = np.zeros((kmax + 1, kmax)); kk = 0; rres_hist = []
            for k in range(kmax):
                v = V[k]; e = eps_rel * float(u.norm()) / max(float(v.norm()), 1e-300)
                Rp, _, _, _ = R_of(u + e * v, clip=False); nT += 1                      # no clipping inside the finite-difference products
                w = (Rp - R) / e
                for i in range(k + 1):
                    H[i, k] = float(torch.dot(V[i], w)); w = w - H[i, k] * V[i]
                for i in range(k + 1):                                                   # second orthogonalisation pass
                    h2 = float(torch.dot(V[i], w)); w = w - h2 * V[i]; H[i, k] += h2
                H[k + 1, k] = float(w.norm()); kk = k + 1
                y, *_ = np.linalg.lstsq(H[:kk + 1, :kk], np.concatenate([[beta], np.zeros(kk)]), rcond=None)
                rres = float(np.linalg.norm(H[:kk + 1, :kk] @ y - np.concatenate([[beta], np.zeros(kk)]))) / beta; rres_hist.append(round(rres, 5))
                if H[k + 1, k] < 1e-14 or rres < 1e-3:
                    break
                V.append(w / H[k + 1, k])
            Hk = H[:kk + 1, :kk]; y, *_ = np.linalg.lstsq(Hk, np.concatenate([[beta], np.zeros(kk)]), rcond=None)
            d = sum(float(y[i]) * V[i] for i in range(kk))
            accepted = False
            for fac in (1.0, 0.5, 0.25):
                Rn, gn, Tgn, infon = R_of(u + fac * d); nT += 1
                if float(Rn.norm()) < float(R.norm()) and infon['unfinished'] == 0 and infon.get('gamma_ok', True):
                    u = u + fac * d; R, g, Tg, info = Rn, gn, Tgn, infon; accepted = True; break
            dmax, drms, nbad, drest = self.defect(g, Tg, tol)
            rec = dict(it=it, kind='newton', gmres_k=kk, gmres_resid=rres_hist[-1] if rres_hist else None, step_fac=(fac if accepted else None), defect_max=dmax, defect_rms=drms, ncells_above_tol=nbad, rms_rest=drest,
                       unfinished=info['unfinished'], th12=[round(info['th1_deg'], 4), round(info['th2_deg'], 4)], R2=float(R.norm()), accepted=accepted, nT=nT, wall=round(time.time() - t0, 1))
            hist.append(rec); log(json.dumps(rec))
            if not accepted:
                break
        hist.append(dict(it=len(hist), defect_max=dmax, defect_rms=drms, ncells_above_tol=nbad, rms_rest=drest, converged=bool(conv(dmax, nbad, drest)), final=True, evaluations=nT, unfinished=info['unfinished'], wall=round(time.time() - t0, 1)))
        log(json.dumps(hist[-1]))
        return g, Tg, hist

    def mask_lr(self, lrcut, lrw=1.0):
        """smoothstep mask M(lr) over [lrcut - lrw/2, lrcut + lrw/2] as a flat [Nr*Nth] tensor (None if lrcut is None)."""
        if lrcut is None: return None
        S = self.S; s_ = ((S.lr - (lrcut - 0.5 * lrw)) / lrw).clamp(0.0, 1.0); Mr = s_ * s_ * (3.0 - 2.0 * s_)
        return Mr[:, None].expand(S.Nr, S.Nth).reshape(-1).contiguous()

    def solve_newton_masked(self, g0, maxit=3, kmax=25, tol=1e-5, log=None, eps_rel=3e-6, smooth=1, kang=32, sig_lr=0.5, lrcut=-8.0, lrw=1.0, core_sweeps=2, tsvd=0.0, gm_tol=0.02, merit_tol=None):
        """Newton-GMRES on the OUTER state in the smooth class (lead analyst, 18:18Z measurement).  R(u) = u - T(u)/scale.  Per step: solve M (I - S DT) M w = -M S R
        by GMRES (matrix-free finite-difference products at eps_rel, smoothing S = angular modes |k| <= kang + Gaussian of width sig_lr in lr, smoothstep mask M over
        [lrcut - lrw/2, lrcut + lrw/2]; optional TSVD of the Hessenberg problem), step d = M w with backtracking on the merit |M S R|; then core_sweeps Picard sweeps of
        the core alone, u <- u - (1 - M) R, with the outer state fixed (the core density's effect on the outer velocity is O(r_core^2)).  No parity projection (the
        state at b != 0 has none).  Convergence: located-cell defect criterion as in solve_safe, or merit below merit_tol."""
        log = log or (lambda s_: None)
        S = self.S; g = g0.clone(); u = (g / self.scale).reshape(-1); t0 = time.time(); hist = []; nT = 0
        Sm = self.smoother(kang, sig_lr) if smooth else (lambda v_: v_)
        Mmask = self.mask_lr(lrcut, lrw); Mk = (lambda v_: v_ * Mmask) if Mmask is not None else (lambda v_: v_)
        Cm = (1.0 - Mmask) if Mmask is not None else None
        def R_of(u_, clip=True):
            g_ = (u_.reshape(S.Nr, S.Nth) * self.scale)
            if clip: g_ = g_.clamp(min=0.0); u_ = (g_ / self.scale).reshape(-1)       # the state kept is the CLIPPED one (u and g synchronised; referee audit, item 4)
            Tg_, info_ = self.Tp(g_)
            return u_ - (Tg_ / self.scale).reshape(-1), g_, Tg_, info_, u_
        def merit(R_): return float(Mk(Sm(R_)).norm())                              # merit = |M S R| (the residual of the regularised problem G(u) = M S R(u) = 0)
        def outer(R_): return float(Mk(R_).norm())                                  # unsmoothed outer residual |M R| (reported, not minimised)
        R, g, Tg, info, u = R_of(u); nT += 1
        conv = lambda dm, nb, dr: (dm < tol) or (nb <= 8 and dr < tol / 10)
        dmax, drms, nbad, drest = self.defect(g, Tg, tol); mer = merit(R)
        rec = dict(it=0, kind='newtonm', defect_max=dmax, defect_rms=drms, ncells_above_tol=nbad, rms_rest=drest, unfinished=info['unfinished'], th12=[round(info['th1_deg'], 4), round(info['th2_deg'], 4)],
                   R2=float(R.norm()), R2_core=(float((R * Cm).norm()) if Cm is not None else None), R2_outer=outer(R), merit=mer, accepted=True, wall=round(time.time() - t0, 1))
        hist.append(rec); log(json.dumps(rec))
        for it in range(1, maxit + 1):
            if conv(dmax, nbad, drest) or (merit_tol is not None and mer < merit_tol):
                break
            b = -Mk(Sm(R)); beta = float(b.norm()); V = [b / beta]; H = np.zeros((kmax + 1, kmax)); kk = 0; rres_hist = []
            def Lv(w_):                                                                  # consistent Jacobian of G(u) = M S R(u) along the trial direction v = M w: M S DR (M w) (referee audit, 1(b))
                v_ = Mk(w_); e = eps_rel * float(u.norm()) / max(float(v_.norm()), 1e-300)
                Rp, _, _, _, _ = R_of(u + e * v_, clip=False)
                return Mk(Sm((Rp - R) / e))
            for k in range(kmax):
                w = Lv(V[k]); nT += 1
                for i in range(k + 1):
                    H[i, k] = float(torch.dot(V[i], w)); w = w - H[i, k] * V[i]
                for i in range(k + 1):
                    h2 = float(torch.dot(V[i], w)); w = w - h2 * V[i]; H[i, k] += h2
                H[k + 1, k] = float(w.norm()); kk = k + 1
                y, *_ = np.linalg.lstsq(H[:kk + 1, :kk], np.concatenate([[beta], np.zeros(kk)]), rcond=None)
                rres = float(np.linalg.norm(H[:kk + 1, :kk] @ y - np.concatenate([[beta], np.zeros(kk)]))) / beta; rres_hist.append(round(rres, 5))
                if H[k + 1, k] < 1e-14 or rres < gm_tol:
                    break
                V.append(w / H[k + 1, k])
            Hk = H[:kk + 1, :kk]; e1 = np.concatenate([[beta], np.zeros(kk)])
            Uh, Sh, Vh = np.linalg.svd(Hk, full_matrices=False); keep = Sh > tsvd if tsvd > 0 else np.ones_like(Sh, bool)
            y = Vh[keep].T @ ((Uh[:, keep].T @ e1) / Sh[keep]); rres_tsvd = float(np.linalg.norm(Hk @ y - e1)) / beta
            w_sol = sum(float(y[i]) * V[i] for i in range(kk)); d = Mk(w_sol)
            r_true = float((Lv(w_sol) - b).norm() / beta); nT += 1                          # true residual of the linear system along w (the operator applies the mask itself)
            u_old, R_old, g_old, Tg_old, info_old, mer_old = u, R, g, Tg, info, mer
            accepted = False; fac = None
            for fac_ in (1.0, 0.5, 0.25, 0.125):
                Rn, gn, Tgn, infon, un = R_of(u + fac_ * d); nT += 1; mern = merit(Rn)
                if mern < mer and infon['unfinished'] == 0 and infon.get('gamma_ok', True):
                    u = un; R, g, Tg, info = Rn, gn, Tgn, infon; mer = mern; accepted = True; fac = fac_; break
            sweep_hist = []; sweeps_kept = None
            if accepted and Cm is not None and core_sweeps > 0:
                u_ns, R_ns, g_ns, Tg_ns, info_ns, mer_ns = u, R, g, Tg, info, mer       # state after the Newton step, before the sweeps
                for sw in range(core_sweeps):                                            # core Picard sweeps (region M < 1) with the outer state fixed
                    Rs, gs, Tgs, infos, us = R_of(u - Cm * R); nT += 1
                    sweep_hist.append([round(float((Rs * Cm).norm()), 6), round(merit(Rs), 6), round(outer(Rs), 6)])
                    if infos['unfinished'] == 0 and infos.get('gamma_ok', True):
                        u, R, g, Tg, info = us, Rs, gs, Tgs, infos
                    else:
                        break
                mer = merit(R)
                if mer >= mer_old:                                                       # the complete update (step + sweeps) must decrease the merit; otherwise keep the step without the sweeps
                    u, R, g, Tg, info, mer = u_ns, R_ns, g_ns, Tg_ns, info_ns, mer_ns; sweeps_kept = False
                else:
                    sweeps_kept = True
            dmax, drms, nbad, drest = self.defect(g, Tg, tol)
            rec = dict(it=it, kind='newtonm', gmres_k=kk, gmres_resid=rres_hist, resid_tsvd=rres_tsvd, resid_true=r_true, H_sv=[float('%.4g' % s_) for s_ in Sh], d_norm=float(d.norm()), u_norm=float(u.norm()), step_fac=fac,
                       sweeps=sweep_hist, sweeps_kept=sweeps_kept, defect_max=dmax, defect_rms=drms, ncells_above_tol=nbad, rms_rest=drest, unfinished=info['unfinished'], th12=[round(info['th1_deg'], 4), round(info['th2_deg'], 4)],
                       R2=float(R.norm()), R2_core=(float((R * Cm).norm()) if Cm is not None else None), R2_outer=outer(R), merit=mer, merit_before=mer_old, accepted=accepted, nT=nT, wall=round(time.time() - t0, 1))
            hist.append(rec); log(json.dumps(rec))
            if not accepted:
                break
        hist.append(dict(it=len(hist), defect_max=dmax, defect_rms=drms, ncells_above_tol=nbad, rms_rest=drest, merit=mer, converged=bool(conv(dmax, nbad, drest) or (merit_tol is not None and mer < merit_tol)), final=True, evaluations=nT, unfinished=info['unfinished'], wall=round(time.time() - t0, 1)))
        log(json.dumps(hist[-1]))
        return g, Tg, hist

    # ---------------------------------------------------------------- residual rows
    def cos3_moment(self, rho, A, qj=2.0):
        """(1/pi) int rho r^-3 cos 3th dX (grid + outer tail + core term), the mirror of PFwdB.c_moment; psi_yy(0) = -this."""
        SB = self.SB
        wl = torch.full((SB.Nr,), SB.d, device=self.dev); wl[0] = 0.5 * SB.d; wl[-1] = 0.5 * SB.d
        w = (SB.r ** (-1) * wl)[None, :, None] * SB.dth / math.pi
        c3 = torch.cos(3 * SB.th)
        grid = (rho * c3[None, None, :] * w).sum(dim=(1, 2))
        a3c = (A * c3[None, :]).sum(dim=1) * SB.dth / math.pi
        rmax = float(SB.r[-1]); tail = rmax ** (self.pB - 1) / (1 - self.pB)
        r0 = float(SB.r[0])
        core = r0 / math.pi * ((rho[:, 0, :] / r0 ** 2) * c3[None, :]).sum(dim=1) * SB.dth / (qj - 1.0)
        return grid + a3c * tail + core, core

    def rows(self, g, want_axis=True):
        """Weighted residual F [nrows] and the diagnostics dict for the state g at the current datum."""
        S, SB = self.S, self.SB
        Wr, Wt, rho2 = self.velocity(g); rho = rho2[None]
        rhs = self._fields(Wr, Wt); the1, the2, gok = self.gamma_angles(rhs)
        th1, th2 = (the1, the2) if self.slave else self.zeros()                                     # datum zeros (slaved to the exits, or the unknowns)
        A_grid = self.Afun(S.th[None, :], (th1, th2))                                            # [1, Nth]
        cm, core = SB.c_moment(rho, self.pB, A_grid); c = float(cm[0]); m1 = 1.0 / self.p - c
        cc, core_c = self.cos3_moment(rho, A_grid); psi_yy0 = -float(cc[0])
        # exit labels: the uniform 1440-angle circle plus paired offsets th_z +- delta_k attached to each (moving) zero for the band rows (referee audit, item 1:
        # fixed-membership bands jump when a zero crosses a sample; traced offset labels make the band rows smooth functions of the state)
        offs = torch.tensor(self.band_offsets, device=self.dev, dtype=torch.float64) * math.pi / 180.0
        extra = torch.cat([th1 + offs, th1 - offs, th2 + offs, th2 - offs])
        thAll = torch.cat([self.thA, extra])
        T, u0, w0, th0, it, arrived = SB.trace(Wr, Wt, self.pB, thAll, self.lr0, dt=self.dt, max_it=8000)
        A_fine = self.Afun(thAll[None, :], (th1, th2))
        logAll = (torch.log(torch.clamp(A_fine, min=1e-300)) - 2.0 * torch.log(torch.clamp(u0.abs(), min=1e-300)) - 2.0 * m1 * T)[0]
        arr = arrived[0]
        nA = self.nA; logGt = logAll[:nA]; arrA = arr[:nA]; thA = self.thA
        wrap = lambda d: (torch.remainder(d + math.pi, 2 * math.pi) - math.pi).abs()
        msk = (wrap(thA - th1) > math.asin(self.cut)) & (wrap(thA - th2) > math.asin(self.cut)) & arrA     # wrapped distance to EACH zero (not its antipode); non-arrived labels excluded
        cols = [torch.ones_like(thA)]
        for j in range(self.K):
            n = j + 1; cols.append(torch.sin(n * thA) if n % 2 == 1 else torch.cos(n * thA))
        for j in range(self.Ko):
            n = j + 1; cols.append(torch.cos(n * thA) if n % 2 == 1 else torch.sin(n * thA))
        Phi = torch.stack(cols, 1)[msk]
        Y = logGt[msk]; mean = Y.mean(); Y = Y - mean
        Pn = Phi.cpu().numpy(); Pinv = np.linalg.pinv(Pn, rcond=1e-8)
        C = Pinv @ Y.cpu().numpy(); fit = Pn @ C; rms_un = float(np.sqrt(((Y.cpu().numpy() - fit) ** 2).mean()))
        lg = (logGt - mean).cpu().numpy(); thd = np.degrees(thA.cpu().numpy())
        nb = len(self.band_offsets); lx = (logAll[nA:] - mean).cpu().numpy(); ax = arr[nA:].cpu().numpy()
        def bm(k):                                                                           # band k: 0 = th1 +, 1 = th1 -, 2 = th2 +, 3 = th2 -
            v = lx[k * nb:(k + 1) * nb]; a = ax[k * nb:(k + 1) * nb]
            return float(v[a].mean()) if a.all() else float('nan')
        t1d, t2d = math.degrees(th1), math.degrees(th2)
        up_p, up_m, dn_p, dn_m = bm(0), bm(1), bm(2), bm(3)
        M_up = up_p - up_m; M_dn = dn_p - dn_m; D_band = 0.5 * (dn_p + dn_m) - 0.5 * (up_p + up_m)
        wrapd = lambda d: (d + math.pi) % (2 * math.pi) - math.pi
        G_up = wrapd(the1 - th1); G_dn = wrapd(the2 - th2)                                           # Gamma matching: exits minus datum zeros (radians); 0 when slaved
        info = dict(m1=m1, c=c, core=float(core[0]), psi_yy0=psi_yy0, core_c=float(core_c[0]), th1_deg=t1d, th2_deg=t2d, exit1_deg=math.degrees(the1), exit2_deg=math.degrees(the2),
                    G_up=G_up, G_dn=G_dn, gamma_ok=gok, arrived_frac=float(arrA.double().mean()),
                    band_arrived=bool(ax.all()),
                    rms_unresolved=rms_un, M_up=M_up, M_dn=M_dn, D_band=D_band, band_vals=[up_p, up_m, dn_p, dn_m], bulk_std=float(lg[np.abs(np.cos(np.radians(thd))) > 0.3].std()),
                    m1_true=1.0 / self.p - math.sqrt(c ** 2 + psi_yy0 ** 2))
        D_ax = float('nan')
        if want_axis:
            try:
                axd = axis_D(S, g, Wr[0], self.p, m1, A=A_grid[0], qj=2.0, hmode='fd1')
                D_ax = float(axd['D_ax_k']); info.update(D_ax=D_ax, drift_up=axd['drift_up'], drift_down=axd['drift_down'])
                axr = axis_D(S, g, Wr[0], self.p, m1, A=A_grid[0], Wt=Wt[0], qj=2.0)
                info['D_ax_dir'] = float(axr['D_ax_k'])
            except Exception as e:
                info['axis_error'] = str(e)
        dg = self.diag(g, Wr, Wt)
        info.update(godd_rel_rms=dg['godd_rel_rms'], godd_max_rel=dg['godd_max_rel'], DW_lr12=dg['DW_lr-12.0'] if 'DW_lr-12.0' in dg else dg.get('DW_lr-12'), DW_lr10=dg.get('DW_lr-10.0', dg.get('DW_lr-10')))
        info['minVr_r'] = float(((1.0 / self.p) + Wr[0] / S.r[:, None]).min())
        F = np.concatenate([[self.wm * (m1 - 0.5)], C[1:1 + self.K], C[1 + self.K:1 + self.K + self.Ko], [self.wD * D_ax, self.wM * M_up, self.wM * M_dn, self.wO * psi_yy0]] + ([[self.wG * G_up, self.wG * G_dn]] if not self.slave else []))
        iD = 1 + self.K + self.Ko
        info['F_parts'] = dict(m1=float(F[0] ** 2), lsq_even=float((F[1:1 + self.K] ** 2).sum()), lsq_odd=float((F[1 + self.K:1 + self.K + self.Ko] ** 2).sum()), D=float(F[iD] ** 2), M=float(F[iD + 1] ** 2 + F[iD + 2] ** 2), O=float(F[iD + 3] ** 2), G=(float(F[iD + 4] ** 2 + F[iD + 5] ** 2) if not self.slave else 0.0))
        info['normF'] = float(np.linalg.norm(F)); info['normF_odd'] = float(np.linalg.norm(F[self.odd_rows])); info['normF_even'] = float(np.linalg.norm(F[~self.odd_rows]))
        info['R_reduced'] = float(np.sqrt(F[0] ** 2 + (F[2:1 + self.K] ** 2).sum()))                       # x-even physical residual without the sin th row (as in the DR runs)
        info['beta1_raw'] = float(F[1]); info['b_norm'] = float(np.linalg.norm(self.F_odd))
        return F, info, lg

    # ---------------------------------------------------------------- Jacobian columns and LM
    def column(self, j, x, g, F, h, jac_its, tol, log=None):
        xj = np.asarray(x, float).copy(); xj[j] += h
        g_ws = self.warm_start(g, x, xj); self.set_x(xj)
        gj, Tgj, hist = self.solve(g_ws, maxit=jac_its, tol=tol, log=log)
        Fj, infj, lgj = self.rows(gj)
        self.set_x(x)
        rec = dict(col=j, name=self.col_names[j], h=h, defect_max=hist[-1]['defect_max'], defect_rms=hist[-1]['defect_rms'],
                   ncells=hist[-1]['ncells_above_tol'], converged=hist[-1]['converged'], evaluations=hist[-1]['evaluations'], dF_norm=float(np.linalg.norm(Fj - F)), dF_even=float(np.linalg.norm((Fj - F)[~self.odd_rows])),
                   dF_odd=float(np.linalg.norm((Fj - F)[self.odd_rows])), dm1_dx=(infj['m1'] - float(1.0 / self.p - 0)) if False else None, m1_j=infj['m1'], psi_yy0_j=infj['psi_yy0'], th12_j=[infj['th1_deg'], infj['th2_deg']],
                   godd_j=infj['godd_rel_rms'], M_j=[infj['M_up'], infj['M_dn']], D_ax_j=infj.get('D_ax'), wall=hist[-1]['wall'])
        return (Fj - F) / h, rec, gj, infj



    def T_exit(self, g):
        """Gamma-slaved exit map returning (Tg, info, TH_exit [Nr, Nth]) so that the analytic datum derivative dT/db_j = Tg chi_j(th_exit) can be formed."""
        S = self.S
        Wr, Wt, rho = self.velocity(g)
        rhs = self._fields(Wr, Wt)
        the1, the2, ok = self.gamma_angles(rhs)
        LR, TH, Tt, live, it = self._orbits(rhs, self.LR.clone(), self.TH.clone(), self.orbit_cap)
        th1, th2 = (the1, the2) if self.slave else self.zeros()
        Tg = (torch.exp(-Tt) * math.exp(self.p * S.hi) * self.Afun(TH, (th1, th2))).reshape(S.Nr, S.Nth) / S.r[:, None] ** self.p
        info = dict(th1_deg=math.degrees(th1), th2_deg=math.degrees(th2), exit1_deg=math.degrees(the1), exit2_deg=math.degrees(the2), gamma_ok=ok, orbit_its=it, unfinished=int(live.sum()))
        return Tg, info, TH.reshape(S.Nr, S.Nth)

    def mode_fn(self, j, th):
        """datum basis function of unknown j at angles th (phi_j for a_j, chi_j for b_j); None for p."""
        if j < self.K:
            n = j + 1; return torch.sin(n * th) if n % 2 == 1 else torch.cos(n * th)
        if j < self.K + self.Ko:
            n = j - self.K + 1; return torch.cos(n * th) if n % 2 == 1 else torch.sin(n * th)
        if (not self.slave) and j < self.K + self.Ko + 2:
            thz = self.zeros()[j - self.K - self.Ko]; d = th - thz                     # d log A / d th_z = -cot((th - th_z)/2); A cot -> 0 at the zero
            c = -1.0 / torch.tan(0.5 * d); return torch.where(torch.sin(0.5 * d).abs() < 1e-9, torch.zeros_like(c), c)
        return None


    def smoother(self, kang=32, sig_lr=0.5):
        """Low-pass filter on [Nr, Nth] fields: angular Fourier modes |k| <= kang kept, Gaussian of width sig_lr (in lr units) along lr (reflect padding).
        The verifier's filter for its smoothed x-odd Ritz computations (report Section 5.8); defines the response in a smooth class."""
        import torch.nn.functional as Fn
        S = self.S; n = int(round(4 * sig_lr / S.d)); t = torch.arange(-n, n + 1, device=self.dev, dtype=torch.float64) * S.d
        ker = torch.exp(-0.5 * (t / sig_lr) ** 2); ker = (ker / ker.sum()).view(1, 1, -1)
        def apply(v):
            vm = v.reshape(S.Nr, S.Nth)
            Fh = torch.fft.rfft(vm, dim=1); Fh[:, kang + 1:] = 0.0; vm = torch.fft.irfft(Fh, n=S.Nth, dim=1)
            x = vm.T.unsqueeze(1)                                                  # [Nth, 1, Nr]
            x = Fn.pad(x, (n, n), mode='reflect'); x = Fn.conv1d(x, ker)
            return x.squeeze(1).T.reshape(-1)
        return apply

    def linear_column(self, j, x, g, F, h, kmax=25, eps_rel=1e-3, log=None, podd=0, smooth=0, kang=32, sig_lr=0.5, tsvd=0.0, lrcut=None, lrw=1.0, core_fill=1):
        """Fallback column by the LINEAR response at the base state: solve (I - DT) v = b by GMRES (matrix-free, scaled variable u = g/scale),
        b = (T_{x + h e_j}(g) - T_x(g)) / (h scale) (datum derivative at the frozen state), DT v = (T(g + e v scale) - T(g)) / e; then the column is
        (rows(g + h v scale; x + h e_j) - rows(g; x)) / h.  Returns column, record (GMRES relative residual, Hessenberg singular values).
        lrcut (V181 / lead 18:26Z item 3): CORE-FROZEN response: the unknown is restricted to lr > lrcut by a smoothstep mask M over [lrcut - lrw/2, lrcut + lrw/2]
        (the core lr < lrcut - lrw/2 does not move); the system solved is M (I - S DT) M w = M b, response v = M w; the true residual is reported for this masked
        system (resid_true) and for the full unmasked equation along v (resid_full, with its core part resid_core)."""
        log = log or (lambda s_: None)
        S = self.S; N = S.Nr * S.Nth
        xj = np.asarray(x, float).copy(); xj[j] += h
        Tg0, info0, THex = self.T_exit(g); u = (g / self.scale).reshape(-1); Tu0 = (Tg0 / self.scale).reshape(-1); nT = 1
        chi = self.mode_fn(j, THex)
        if chi is not None:
            b = (Tg0 * chi / self.scale).reshape(-1)                              # ANALYTIC datum derivative at the frozen state: dT/dx_j = Tg chi_j(th_exit) (velocity, orbits and slaved zeros do not depend on x_j at frozen g)
            rhs_kind = 'analytic'
        else:
            self.set_x(xj); Tgj, infoj = self.Tp(g); self.set_x(x); nT += 1
            b = ((Tgj / self.scale).reshape(-1) - Tu0) / h; rhs_kind = 'fd'          # p: finite difference
        sgn = -1.0 if self.odd_cols[j] else 1.0                                   # parity of the right-hand side under th -> pi - th
        b0 = b.clone()                                                            # RAW right-hand side (unprojected, unsmoothed) for the raw-equation residual (referee audit, 1(a))
        def par_force(v):                                                         # projection onto the column's parity, always applied (diagnostics)
            vm = v.reshape(S.Nr, S.Nth); return (0.5 * (vm + sgn * vm[:, self.flip])).reshape(-1)
        def par(v):                                                               # projection onto that parity (removes the opposite-parity part of the finite-difference products: flip noise, even truncation terms)
            if not podd: return v
            return par_force(v)
        b_even_frac = float((b - par_force(b)).norm() / max(float(b.norm()), 1e-300))
        b = par(b)
        Sm = self.smoother(kang, sig_lr) if smooth else (lambda v: v)
        b_raw_norm = float(b.norm()); b = Sm(b); b_smooth_frac = float(b.norm()) / max(b_raw_norm, 1e-300)
        if lrcut is not None:                                                     # core-frozen response: smoothstep mask in lr (0 below lrcut - lrw/2, 1 above lrcut + lrw/2)
            s_ = ((S.lr - (lrcut - 0.5 * lrw)) / lrw).clamp(0.0, 1.0); Mr = s_ * s_ * (3.0 - 2.0 * s_)
            Mmask = Mr[:, None].expand(S.Nr, S.Nth).reshape(-1).contiguous()
            Mk = lambda v_: v_ * Mmask
        else:
            Mmask = None; Mk = lambda v_: v_
        b_s = b; b = Mk(b_s); b_mask_frac = float(b.norm()) / max(float(b_s.norm()), 1e-300)
        def DTs(v):                                                               # S par DT v: smoothed, parity-projected finite-difference product
            e = eps_rel * float(u.norm()) / max(float(v.norm()), 1e-300)
            gp = (u + e * v).reshape(S.Nr, S.Nth) * self.scale                     # NO clipping in the finite-difference products (T is linear in g through the velocity; negative values are harmless)
            Tgp, _ = self.Tp(gp)
            return Sm(par(((Tgp / self.scale).reshape(-1) - Tu0) / e))
        def Lv(w):
            v_ = Mk(w)
            return Mk(v_ - DTs(v_))                                               # masked smoothed operator M (I - S DT) M (M = identity without lrcut)
        beta = float(b.norm()); V = [b / beta]; H = np.zeros((kmax + 1, kmax)); kk = 0; rres_hist = []
        for k in range(kmax):
            w = Lv(V[k]); nT += 1
            for i in range(k + 1):
                H[i, k] = float(torch.dot(V[i], w)); w = w - H[i, k] * V[i]
            for i in range(k + 1):                                                # second orthogonalisation pass (referee audit, item 1)
                h2 = float(torch.dot(V[i], w)); w = w - h2 * V[i]; H[i, k] += h2
            H[k + 1, k] = float(w.norm()); kk = k + 1
            y, *_ = np.linalg.lstsq(H[:kk + 1, :kk], np.concatenate([[beta], np.zeros(kk)]), rcond=None)
            rres = float(np.linalg.norm(H[:kk + 1, :kk] @ y - np.concatenate([[beta], np.zeros(kk)]))) / beta; rres_hist.append(round(rres, 5))
            if H[k + 1, k] < 1e-14 or rres < 1e-3:
                break
            V.append(w / H[k + 1, k])
        Hk = H[:kk + 1, :kk]; e1 = np.concatenate([[beta], np.zeros(kk)])
        Uh, Sh, Vh = np.linalg.svd(Hk, full_matrices=False)
        keep = Sh > tsvd if tsvd > 0 else np.ones_like(Sh, bool)                   # truncated SVD of the Hessenberg least-squares problem (drops near-neutral Krylov directions)
        y = Vh[keep].T @ ((Uh[:, keep].T @ e1) / Sh[keep]); y_full = Vh.T @ ((Uh.T @ e1) / Sh)
        rres_tsvd = float(np.linalg.norm(Hk @ y - e1)) / beta
        w = sum(float(y[i]) * V[i] for i in range(kk)); v = Mk(w)
        VtV = np.array([[float(torch.dot(V[a], V[c])) for c in range(len(V))] for a in range(len(V))]); orth_err = float(np.abs(VtV - np.eye(len(V))).max())
        dv = DTs(v); nT += 1                                                      # one extra product along the final response
        r_true = float((Mk(v - dv) - b).norm() / beta)                            # TRUE residual of the system solved (masked if lrcut; referee audit, item 1)
        full = v - dv - b_s; r_full = float(full.norm()) / max(float(b_s.norm()), 1e-300)   # residual of the full SMOOTHED, projected equation along v (unmasked)
        r_core = (float((full * (1.0 - Mmask)).norm()) / max(float(b_s.norm()), 1e-300)) if Mmask is not None else None
        e_r = eps_rel * float(u.norm()) / max(float(v.norm()), 1e-300)            # RAW product along v (unsmoothed, unprojected): raw-equation residual v - DT v - b0 (referee audit, 1(a))
        Tgr, _ = self.Tp((u + e_r * v).reshape(S.Nr, S.Nth) * self.scale); nT += 1
        dv_raw = ((Tgr / self.scale).reshape(-1) - Tu0) / e_r
        prod_even_frac = float((dv_raw - par_force(dv_raw)).norm() / max(float(dv_raw.norm()), 1e-300))   # opposite-parity fraction of the raw product (what the projection removes)
        if Mmask is not None:                                                     # the same split into the outer (M) and core (1 - M) parts
            dvo = dv_raw * Mmask; dvc = dv_raw * (1.0 - Mmask)
            prod_even_frac_outer = float((dvo - par_force(dvo)).norm() / max(float(dvo.norm()), 1e-300)); prod_even_frac_core = float((dvc - par_force(dvc)).norm() / max(float(dvc.norm()), 1e-300))
            prod_core_frac = float(dvc.norm() / max(float(dv_raw.norm()), 1e-300))
        else:
            prod_even_frac_outer = prod_even_frac_core = prod_core_frac = None
        raw = v - dv_raw - b0; b0n = max(float(b0.norm()), 1e-300); r_raw = float(raw.norm()) / b0n
        r_raw_core = (float((raw * (1.0 - Mmask)).norm()) / b0n) if Mmask is not None else None
        r_raw_outer = (float((raw * Mmask).norm()) / b0n) if Mmask is not None else r_raw
        v_fill = (v + (1.0 - Mmask) * dv_raw) if (core_fill and Mmask is not None) else None   # one core sweep: the core's linear image response to the outer response (omits the core -> core feedback, O(r_core))
        v_even_frac = float((v - par_force(v)).norm() / max(float(v.norm()), 1e-300))   # opposite-parity fraction of the response (0 by construction when podd)
        gj = ((u + h * v).reshape(S.Nr, S.Nth) * self.scale).clamp(min=0.0)
        self.set_x(xj); Fj, infj, lgj = self.rows(gj); Tgj2, infoj2 = self.Tp(gj); dmax, drms = self.defect(gj, Tgj2); nT += 1
        col_fill = None; dF_fill_odd = None
        if v_fill is not None:                                                    # rows with the core filled by one sweep (second column variant)
            gjf = ((u + h * v_fill).reshape(S.Nr, S.Nth) * self.scale).clamp(min=0.0); Fjf, infjf, _ = self.rows(gjf)
            col_fill = [round(float(q_), 5) for q_ in (Fjf - F) / h]; dF_fill_odd = float(np.linalg.norm((Fjf - F)[self.odd_rows]))
        self.set_x(x)
        rec = dict(col=j, h=h, eps_rel=eps_rel, podd=int(podd), smooth=int(smooth), kang=kang, sig_lr=sig_lr, tsvd=tsvd, lrcut=lrcut, lrw=lrw, b_mask_frac=b_mask_frac, n_kept=int(keep.sum()), b_smooth_frac=b_smooth_frac, rhs=rhs_kind, b_even_frac=b_even_frac, gmres_k=kk, gmres_resid=rres_hist, resid_tsvd=rres_tsvd, resid_true=r_true, resid_full=r_full, resid_core=r_core, resid_raw=r_raw, resid_raw_core=r_raw_core, resid_raw_outer=r_raw_outer, prod_even_frac=prod_even_frac, prod_even_frac_outer=prod_even_frac_outer, prod_even_frac_core=prod_even_frac_core, prod_core_frac=prod_core_frac, core_fill=int(core_fill), col_fill=col_fill, dF_fill_odd=dF_fill_odd, orth_err=orth_err, v_norm_full=float(np.linalg.norm(y_full)), H_sv=[float('%.4g' % s_) for s_ in np.linalg.svd(Hk, compute_uv=False)], b_norm=beta, v_norm=float(v.norm()),
                   v_even_frac=v_even_frac, defect_of_linear_state=[dmax, drms], dF_norm=float(np.linalg.norm(Fj - F)), dF_even=float(np.linalg.norm((Fj - F)[~self.odd_rows])), dF_odd=float(np.linalg.norm((Fj - F)[self.odd_rows])),
                   m1_j=infj['m1'], psi_yy0_j=infj['psi_yy0'], th12_j=[infj['th1_deg'], infj['th2_deg']], godd_j=infj['godd_rel_rms'], M_j=[infj['M_up'], infj['M_dn']], nT=nT)
        self._last_arnoldi = dict(H=Hk, y=y, beta=beta)
        return (Fj - F) / h, rec, gj, infj


def load_base(fn, Nth):
    d = np.load(fn, allow_pickle=True); g0 = d['g']; lr = d['lr']; th = d['th']; a = json.loads(str(d['args'])); p = float(a['p'])
    coef = np.array(a['par'], float)
    if a.get('kind') == 'bnewton': coef = coef[:int(a['K'])]
    elif a.get('kind') == 'parity': coef = coef
    if g0.shape[1] != Nth:
        assert g0.shape[1] % Nth == 0, (g0.shape, Nth); g0 = g0[:, ::g0.shape[1] // Nth]; th = th[::len(th) // Nth]
    F_odd = np.array(a.get('F_odd', []), float)
    return torch.tensor(g0, device='cuda'), coef, F_odd, p, float(lr[0]), float(lr[-1])


def save_state(fn, PM, g, x, F, info, lg, extra=None):
    np.savez(fn, g=g.cpu().numpy(), lr=PM.S.lr.cpu().numpy(), th=PM.S.th.cpu().numpy(), x=np.asarray(x), F=np.asarray(F), logGt=lg, thA=PM.thA.cpu().numpy(), info=json.dumps(info),
             args=json.dumps(dict(p=float(x[-1]), kind='parity', K=PM.K, Ko=PM.Ko, par=[float(v) for v in x[:PM.K]], F_odd=[float(v) for v in x[PM.K:PM.K + PM.Ko]], th12_deg=[info['th1_deg'], info['th2_deg']], slave=PM.slave, dth12=[float(v) for v in PM.dth12], **(extra or {}))))


if __name__ == '__main__':
    # usage: python3 code/pfwd_parity.py base.npz tag mode=rows|polish|col|jodd|search [Nth=512] [K=16] [Ko=16] [cols=b1,b3,p,a2] [h=0.02] [h_p=0.004] [jac_its=15]
    #        [tol=2e-5] [xeven=0] [eps_odd=0.01] [odd_modes=1] [J0=file] [Jodd=file] [maxit=6] [lams=0.7,0.35] [da_max=0.05] [dp_max=0.02] [mu0=0.01] [wm=50] [wD=5] [wM=5] [wO=50] [exit_maxit=30]
    fn = sys.argv[1]; tag = sys.argv[2]
    opt = dict(mode='rows', Nth=512, K=16, Ko=16, cols='', h=0.02, h_p=0.004, jac_its=15, tol=2e-5, xeven=0, eps_odd=0.01, odd_modes='1', J0='', Jodd='', maxit=6, lams='0.7,0.35', da_max=0.05, dp_max=0.02, mu0=0.01,
               wm=50.0, wD=5.0, wM=5.0, wO=50.0, exit_maxit=30, polish_its=30, b0='', free_a2=1, kmax=25, eps_rel=1e-3, safe=1, collog=0, solver='anderson', newton_steps=2, resp='', podd=1, smooth=0, kang=32, sig_lr=0.5, tsvd=0.0, slave=1, wG=50.0, lrcut='', lrw=1.0, core_fill=0, core_sweeps=2, gm_tol=0.02, pert='', pertfile='', tamp='0.05', signs='1,-1', merit_tol=0.0, ws='', ws_mirror=1, cont=0)
    for s_ in sys.argv[3:]:
        k, v = s_.split('=', 1); opt[k] = v if k in ('mode', 'cols', 'J0', 'Jodd', 'lams', 'odd_modes', 'b0', 'solver', 'resp', 'lrcut', 'pert', 'pertfile', 'tamp', 'signs', 'ws') else (int(v) if k in ('Nth', 'K', 'Ko', 'jac_its', 'xeven', 'maxit', 'exit_maxit', 'polish_its', 'free_a2', 'kmax', 'safe', 'collog', 'newton_steps', 'podd', 'smooth', 'kang', 'slave', 'core_sweeps', 'core_fill', 'ws_mirror', 'cont') else float(v))
    os.makedirs('runs/pfwd/par', exist_ok=True); logf = open('runs/pfwd/par/%s.log' % tag, 'a')
    def log(line):
        print(line, flush=True); logf.write(line + '\n'); logf.flush()
    g0, coef, F_odd0, p, lo, hi = load_base(fn, opt['Nth'])
    K, Ko = opt['K'], opt['Ko']
    F_even = np.zeros(K); F_even[:min(K, len(coef))] = coef[:K]
    F_odd = np.zeros(Ko); F_odd[:min(Ko, len(F_odd0))] = F_odd0[:Ko]
    dth0 = [0.0, 0.0]
    if opt['b0']:
        bb = [float(v) for v in opt['b0'].split(',')]; F_odd[:len(bb)] = bb
    Nr = g0.shape[0]
    PM = ParityMap(Nr, opt['Nth'], lo, hi, p, F_even, F_odd, xeven=bool(opt['xeven']), wm=opt['wm'], wD=opt['wD'], wM=opt['wM'], wO=opt['wO'], slave=bool(opt['slave']), wG=opt['wG']); PM.safe = bool(opt['safe'])
    if not PM.slave: PM.dth12 = np.array(dth0, float); PM.th12 = PM.zeros()
    PM.solver = opt['solver']; PM.newton_steps = int(opt['newton_steps']); PM.newton_kmax = int(opt['kmax'])
    PM.nm_opts = dict(eps_rel=float(opt['eps_rel']), smooth=int(opt['smooth']), kang=int(opt['kang']), sig_lr=float(opt['sig_lr']), lrcut=(float(opt['lrcut']) if str(opt['lrcut']) != '' else None), lrw=float(opt['lrw']),
                      core_sweeps=int(opt['core_sweeps']), tsvd=float(opt['tsvd']), gm_tol=float(opt['gm_tol']), merit_tol=(float(opt['merit_tol']) if float(opt['merit_tol']) > 0 else None))
    if opt['resp']:                                                        # linear state responses for warm starts: files <resp>_resp_<name>.npz (from mode=lincol)
        import glob
        for fnr in sorted(glob.glob(opt['resp'] + '_resp_*.npz')):
            dr = np.load(fnr, allow_pickle=True); PM.resp[int(dr['col'])] = torch.tensor(dr['dg'].astype(np.float64), device='cuda')
        print(json.dumps(dict(responses_loaded=sorted(PM.resp.keys()))), flush=True)
    x = PM.get_x()
    log(json.dumps(dict(tag=tag, base=fn, mode=opt['mode'], K=K, Ko=Ko, n=PM.n, nrows=PM.nrows, p=p, x0=[round(float(v), 6) for v in x], opt=opt, Nr=Nr, Nth=opt['Nth'], start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))))
    t0 = time.time()
    if opt['mode'] in ('rows', 'polish'):
        g = g0
        if opt['mode'] == 'polish':
            g, Tg, hist = PM.solve(g0, maxit=opt['polish_its'], tol=opt['tol'], log=log)
        F, info, lg = PM.rows(g)
        log(json.dumps(dict(mode=opt['mode'], F=[round(float(v), 6) for v in F], row_names=PM.row_names, info=info, wall=round(time.time() - t0, 1))))
        save_state('runs/pfwd/par/%s_state.npz' % tag, PM, g, x, F, info, lg)
    elif opt['mode'] in ('col', 'jodd'):
        # base residual at the (possibly re-polished) base
        g, Tg, hist = PM.solve(g0, maxit=opt['polish_its'], tol=opt['tol'], log=log)
        F, info, lg = PM.rows(g)
        log(json.dumps(dict(base=True, F=[round(float(v), 6) for v in F], info=info, wall=round(time.time() - t0, 1))))
        save_state('runs/pfwd/par/%s_base.npz' % tag, PM, g, x, F, info, lg)
        names = PM.col_names
        if opt['mode'] == 'jodd':
            cols = ['b%d' % (j + 1) for j in range(Ko)] + ([c for c in opt['cols'].split(',') if c] if opt['cols'] else [])
        else:
            cols = [c for c in opt['cols'].split(',') if c]
        J = np.full((PM.nrows, PM.n), np.nan); recs = []; extra = {}
        for centry in cols:
            cname, hov = (centry.split(':') + [None])[:2]                      # "b1:0.01" = noise column: same unknown, step 0.01, compared with the main column, not stored in J
            j = names.index(cname); h = float(hov) if hov else (opt['h_p'] if cname == 'p' else opt['h'])
            colj, rec, gj, infj = PM.column(j, x, g, F, h, opt['jac_its'], opt['tol'], log=(log if opt['collog'] else None))
            if hov:
                rec['noise_column'] = True
                if np.all(np.isfinite(J[:, j])):
                    dcol = colj - J[:, j]
                    rec['diff_to_main'] = dict(norm=float(np.linalg.norm(dcol)), odd=float(np.linalg.norm(dcol[PM.odd_rows])), even=float(np.linalg.norm(dcol[~PM.odd_rows])), main_odd_norm=float(np.linalg.norm(J[PM.odd_rows, j])), main_h=opt['h'])
                extra[centry] = colj
            else:
                J[:, j] = colj
            recs.append(rec); log(json.dumps(dict(jac_col=rec, col_values=[round(float(v), 5) for v in colj], wall=round(time.time() - t0, 1))))
            np.savez('runs/pfwd/par/%s_J.npz' % tag, J=J, x=x, F=F, cols=np.array([c for c in cols if ':' not in c]), row_names=np.array(PM.row_names), recs=json.dumps(recs), extra=json.dumps({k: [float(v) for v in vv] for k, vv in extra.items()}))
            np.savez('runs/pfwd/par/%s_col_%s.npz' % (tag, centry.replace(':', '_h')), g=gj.cpu().numpy(), info=json.dumps(infj), x=x, h=h, col=j)
        done = [names.index(c) for c in cols if ':' not in c]
        Jo = J[:, [j for j in done if PM.odd_cols[j]]]
        if Jo.shape[1] > 0:
            Joo = Jo[PM.odd_rows]; Jeo = Jo[~PM.odd_rows]
            log(json.dumps(dict(odd_block=dict(shape=list(Joo.shape), sv=[float('%.4g' % v) for v in np.linalg.svd(Joo, compute_uv=False)], cross_even_rows_norm=float(np.linalg.norm(Jeo)), odd_norm=float(np.linalg.norm(Joo))))))
        log('PARITY_DONE')
    elif opt['mode'] == 'lincol':
        g, Tg, hist = PM.solve(g0, maxit=opt['polish_its'], tol=opt['tol'], log=log)
        F, info, lg = PM.rows(g)
        log(json.dumps(dict(base=True, F=[round(float(v), 6) for v in F], info=info, wall=round(time.time() - t0, 1))))
        names = PM.col_names
        cols = [c for c in opt['cols'].split(',') if c]; J = np.full((PM.nrows, PM.n), np.nan); recs = []
        for cname in cols:
            j = names.index(cname); h = opt['h_p'] if cname == 'p' else opt['h']
            colj, rec, gj, infj = PM.linear_column(j, x, g, F, h, kmax=int(opt['kmax']), eps_rel=opt['eps_rel'], podd=int(opt['podd']), smooth=int(opt['smooth']), kang=int(opt['kang']), sig_lr=opt['sig_lr'], tsvd=opt['tsvd'], lrcut=(float(opt['lrcut']) if str(opt['lrcut']) != '' else None), lrw=float(opt['lrw']), core_fill=int(opt['core_fill']))
            J[:, j] = colj; recs.append(rec); log(json.dumps(dict(lin_col=rec, col_values=[round(float(v), 5) for v in colj], wall=round(time.time() - t0, 1))))
            np.savez('runs/pfwd/par/%s_J.npz' % tag, J=J, x=x, F=F, cols=np.array(cols), row_names=np.array(PM.row_names), recs=json.dumps(recs))
            np.savez('runs/pfwd/par/%s_resp_%s.npz' % (tag, cname), dg=((gj - g) / h).cpu().numpy().astype(np.float32), col=j, h=h, info=json.dumps(infj), H=PM._last_arnoldi['H'], y=PM._last_arnoldi['y'], beta=PM._last_arnoldi['beta'])   # linear state response dg/dx_j (float32) for warm starts; Arnoldi data
        log('PARITY_DONE')
    elif opt['mode'] == 'nsolve':
        # lead 18:18Z second-order measurement: base (Anderson polish, x-even) then the state at the perturbed datum x_b + sign * t * v for each sign and amplitude,
        # solved by the masked smoothed Newton-GMRES (solver=newtonm) from the rescaled warm start (+ linear responses if resp= given); rows recorded per state.
        names = PM.col_names; solver0 = PM.solver; PM.solver = 'anderson'
        g, Tg, hist = PM.solve(g0, maxit=opt['polish_its'], tol=opt['tol'], log=log)
        Fb, infob, lgb = PM.rows(g); xb = x.copy(); gb = g.clone()
        log(json.dumps(dict(base=True, F=[round(float(v), 6) for v in Fb], info=infob, wall=round(time.time() - t0, 1))))
        vdir = np.zeros(PM.n)
        if opt['pertfile']:
            dv = np.load(opt['pertfile'], allow_pickle=True); vv = np.asarray(dv['v'], float); cnames = [str(c) for c in dv['cols']] if 'cols' in dv else ['b%d' % (i + 1) for i in range(len(vv))]
            for cn, val in zip(cnames, vv): vdir[names.index(cn)] = val
        for item in [q for q in opt['pert'].split(',') if q]:
            cn, val = item.split(':'); vdir[names.index(cn)] += float(val)
        log(json.dumps(dict(vdir=[round(float(v), 6) for v in vdir], vdir_norm=float(np.linalg.norm(vdir)))))
        PM.solver = solver0 if solver0 in ('newton', 'newtonm', 'anderson') else 'newtonm'   # anderson = the UNPROJECTED safeguarded fixed-point iteration (lead 20:39Z (b))
        ws_g = ws_x = None; prev = None
        if opt['ws']:                                                              # warm start from a saved nsolve / parity state file (keys g, x); rescaled from its datum to the target datum
            dws = np.load(opt['ws'], allow_pickle=True); ws_g = torch.tensor(dws['g'], device='cuda'); ws_x = np.asarray(dws['x'], float)
            log(json.dumps(dict(ws=opt['ws'], ws_x=[round(float(v), 6) for v in ws_x], ws_mirror=int(opt['ws_mirror']))))
        results = []
        for tamp in [float(v) for v in str(opt['tamp']).split(',')]:
            for sgn in [float(v) for v in str(opt['signs']).split(',')]:
                x = xb + sgn * tamp * vdir
                if opt['cont'] and prev is not None and prev[2] == sgn:                      # amplitude continuation: warm start from the previous amplitude's state of the same sign
                    g_ws = PM.warm_start(prev[0], prev[1], x); log(json.dumps(dict(cont_from=[round(float(v_), 6) for v_ in prev[1][K:K + Ko] if v_ != 0], tamp=tamp, sign=sgn)))
                elif ws_g is not None:
                    gsrc, xsrc = ws_g, ws_x
                    if opt['ws_mirror'] and sgn * (ws_x[K:K + Ko] @ vdir[K:K + Ko]) < 0:   # the saved state has the opposite sign: use its exact reflection th -> pi - th (b -> -b)
                        gsrc = ws_g[:, PM.flip]; xsrc = ws_x.copy(); xsrc[K:K + Ko] = -xsrc[K:K + Ko]
                        log(json.dumps(dict(ws_reflected=True, sign=sgn)))
                    g_ws = PM.warm_start(gsrc, xsrc, x)
                else:
                    g_ws = PM.warm_start(gb, xb, x)
                PM.set_x(x)
                g, Tg, hist = PM.solve(g_ws, maxit=opt['exit_maxit'], tol=opt['tol'], log=log)
                if opt['cont'] and (hist[-1]['converged'] or opt['cont'] == 2): prev = (g.clone(), x.copy(), sgn)   # cont=2: continue even from an unconverged state
                F, info, lg = PM.rows(g); info['exit_defect'] = hist[-1]['defect_max']; info['exit_converged'] = hist[-1]['converged']; info['merit'] = hist[-1].get('merit')
                godd = float(torch.sqrt(((g - g[:, PM.flip]) ** 2).mean() / (g ** 2).mean()))
                rec = dict(state=True, tamp=tamp, sign=sgn, x=[round(float(v), 6) for v in x], F=[round(float(v), 6) for v in F], info=info, godd_state=godd, wall=round(time.time() - t0, 1),
                           evaluations=hist[-1].get('evaluations'), accepted_steps=hist[-1].get('accepted_steps'), defect_rms=hist[-1].get('defect_rms'),
                           normFo=float(np.linalg.norm(F[PM.odd_rows])), normFe=float(np.linalg.norm(F[~PM.odd_rows])), dnormFe=float(np.linalg.norm(F[~PM.odd_rows]) - np.linalg.norm(Fb[~PM.odd_rows])),
                           normF_minus_base=float(np.linalg.norm(F) - np.linalg.norm(Fb)))
                results.append(dict(rec, F_full=np.asarray(F, float).copy(), converged=bool(hist[-1]['converged']), ok=bool(np.all(np.isfinite(F)) and info.get('axis_error') is None and info['arrived_frac'] > 0.999 and info['band_arrived'] and info['gamma_ok'])))
                log(json.dumps(rec))
                save_state('runs/pfwd/par/%s_t%g_s%+d.npz' % (tag, tamp, int(sgn)), PM, g, x, F, info, lg, extra=dict(tamp=tamp, sign=sgn, vdir=[float(v) for v in vdir]))
                PM.set_x(xb)
            # symmetric and antisymmetric differences for this amplitude (lead 18:18Z: q_k(v) = (F_k(tv) + F_k(-tv) - 2 F_k(0)) / (2 t^2))
            rp = [r for r in results if r['tamp'] == tamp and r['sign'] > 0]; rm = [r for r in results if r['tamp'] == tamp and r['sign'] < 0]
            if len(rp) == 1 and len(rm) == 1:
                rs = [rp[0], rm[0]]                                                      # selected by sign (+t first); FULL-precision rows (referee audit, 1(c))
                Fp = rs[0]['F_full']; Fm = rs[1]['F_full']; q = (Fp + Fm - 2 * Fb) / (2 * tamp ** 2); a = (Fp - Fm) / (2 * tamp)
                keys = ['m1', 'D_ax', 'D_ax_dir', 'M_up', 'M_dn', 'psi_yy0', 'D_band']
                qi = {k_: ((rs[0]['info'].get(k_, float('nan')) + rs[1]['info'].get(k_, float('nan')) - 2 * infob.get(k_, float('nan'))) / (2 * tamp ** 2)) for k_ in keys}
                ai = {k_: ((rs[0]['info'].get(k_, float('nan')) - rs[1]['info'].get(k_, float('nan'))) / (2 * tamp)) for k_ in keys}
                even_rows = ~PM.odd_rows; odd_rows = PM.odd_rows
                f0 = float(Fb @ Fb); fp = float(Fp @ Fp); fm = float(Fm @ Fm)
                # v^T H v directly from the full functional f = |F|^2 (f(+-tv) = |F_e(0)|^2 + t^2 v^T H v + O(t^4)); |F_o(+-tv)|^2 / t^2 estimates |J_oo v|^2 (= s^2 for a unit right singular vector)
                log(json.dumps(dict(second_order=True, tamp=tamp, q_rows=[round(float(v), 5) for v in q], a_rows=[round(float(v), 5) for v in a], q_info=qi, a_info=ai,
                                    two_sum_Fe_q=float(2.0 * (Fb[even_rows] * q[even_rows]).sum()), Fe0_norm2=float((Fb[even_rows] ** 2).sum()), f0=f0, f_plus=fp, f_minus=fm,
                                    vHv_from_f=float((fp + fm - 2 * f0) / (2 * tamp ** 2)), Joo_v_norm2_est=[float((Fp[odd_rows] ** 2).sum() / tamp ** 2), float((Fm[odd_rows] ** 2).sum() / tamp ** 2)],
                                    f_odd_part=float((fp - fm) / (2 * tamp)), valid=bool(rs[0]['converged'] and rs[1]['converged'] and rs[0]['ok'] and rs[1]['ok']),
                                    converged=[rs[0]['converged'], rs[1]['converged']], ok=[rs[0]['ok'], rs[1]['ok']], row_names=list(PM.row_names))))
        log('PARITY_DONE')
    elif opt['mode'] == 'search':
        # start: x-even base (polished unprojected) + x-odd perturbation eps_odd on the listed odd modes (b_j = eps_odd)
        names = PM.col_names
        g, Tg, hist = PM.solve(g0, maxit=opt['polish_its'], tol=opt['tol'], log=log)
        Fb, infob, lgb = PM.rows(g); xb = x.copy()
        log(json.dumps(dict(base=True, F=[round(float(v), 6) for v in Fb], info=infob, wall=round(time.time() - t0, 1))))
        J = np.zeros((PM.nrows, PM.n)); have = np.zeros(PM.n, bool)
        if opt['J0']:                                                     # x-even block from a DFD-type Jacobian (rows m1 (wm0), K LSQ, D_ax (wD0); columns a_1..a_K, [D], p)
            dj = np.load(opt['J0'], allow_pickle=True); J0 = dj['J']; wm0, wD0 = 50.0, 50.0
            if J0.shape[1] == K + 2: J0 = np.delete(J0, K, axis=1)       # drop the D column
            assert J0.shape == (K + 2, K + 1), J0.shape
            for jj in range(K):
                J[0, jj] = J0[0, jj] * PM.wm / wm0; J[1:1 + K, jj] = J0[1:1 + K, jj]; J[1 + K + Ko, jj] = J0[K + 1, jj] * PM.wD / wD0; have[jj] = True
            J[0, -1] = J0[0, K] * PM.wm / wm0; J[1:1 + K, -1] = J0[1:1 + K, K]; J[1 + K + Ko, -1] = J0[K + 1, K] * PM.wD / wD0; have[-1] = True
            if np.abs(J0[:, 1]).max() == 0: have[1] = False           # frozen a_2 column
            log(json.dumps(dict(J0=opt['J0'], used_cols=int(have.sum()))))
        if opt['Jodd']:
            dj = np.load(opt['Jodd'], allow_pickle=True); Jo = dj['J']; cols_o = list(dj['cols'])
            for cname in cols_o:
                jj = names.index(cname)
                if np.all(np.isfinite(Jo[:, jj])): J[:, jj] = Jo[:, jj]; have[jj] = True
            log(json.dumps(dict(Jodd=opt['Jodd'], used_cols=int(have.sum()), cols=cols_o)))
        recs = []
        for jj in np.where(~have)[0]:
            h = opt['h_p'] if jj == PM.n - 1 else opt['h']
            colj, rec, gj, infj = PM.column(jj, xb, g, Fb, h, opt['jac_its'], opt['tol']); J[:, jj] = colj; have[jj] = True; recs.append(rec)
            log(json.dumps(dict(jac_col=rec, wall=round(time.time() - t0, 1))))
        np.savez('runs/pfwd/par/%s_J0full.npz' % tag, J=J, x=xb, F=Fb, row_names=np.array(PM.row_names), recs=json.dumps(recs))
        Joo = J[PM.odd_rows][:, PM.odd_cols]; Jee = J[~PM.odd_rows][:, ~PM.odd_cols]
        log(json.dumps(dict(jacobian='assembled', sv_full=[float('%.4g' % v) for v in np.linalg.svd(J, compute_uv=False)], sv_odd_block=[float('%.4g' % v) for v in np.linalg.svd(Joo, compute_uv=False)],
                            sv_even_block=[float('%.4g' % v) for v in np.linalg.svd(Jee, compute_uv=False)], cross_norm=float(np.linalg.norm(J[PM.odd_rows][:, ~PM.odd_cols]) + np.linalg.norm(J[~PM.odd_rows][:, PM.odd_cols])))))
        # perturbed start
        x = xb.copy()
        for mstr in opt['odd_modes'].split(','):
            x[K + int(mstr) - 1] += opt['eps_odd']
        g_ws = PM.warm_start(g, xb, x); PM.set_x(x)
        g, Tg, hist = PM.solve(g_ws, maxit=opt['exit_maxit'], tol=opt['tol'], log=log)
        F, info, lg = PM.rows(g); info['exit_defect'] = hist[-1]['defect_max']; info['exit_converged'] = hist[-1]['converged']
        log(json.dumps(dict(it=0, x=[round(float(v), 6) for v in x], normF=info['normF'], info=info, pred_from_base=float(np.linalg.norm(Fb + J @ (x - xb))), wall=round(time.time() - t0, 1))))
        save_state('runs/pfwd/par/%s_it0.npz' % tag, PM, g, x, F, info, lg)
        mu = opt['mu0']; lams = [float(v) for v in opt['lams'].split(',')]
        free = np.ones(PM.n, bool)
        if not opt['free_a2']: free[1] = False                                     # frozen a_2: solve on the free columns only (referee audit, item 6)
        for it in range(1, opt['maxit'] + 1):
            accepted = False
            for attempt in range(4):
                J_frozen = J.copy()
                Jf = J[:, free]; JTJ = Jf.T @ Jf; Dm = np.diag(np.maximum(np.diag(JTJ), max(1e-12 * np.diag(JTJ).max(), 1e-14)))   # normal equations rebuilt per attempt (Broyden updates of rejected trials included)
                dx = np.zeros(PM.n); dx[free] = -np.linalg.solve(JTJ + mu * Dm, Jf.T @ F)
                sc = max(1.0, np.abs(dx[:-1]).max() / opt['da_max'], abs(dx[-1]) / opt['dp_max']); dx = dx / sc
                log(json.dumps(dict(it=it, attempt=attempt, mu=mu, step_scale=1 / sc, dx_norm=float(np.linalg.norm(dx)), dx_odd_norm=float(np.linalg.norm(dx[PM.odd_cols])), pred=[float(np.linalg.norm(F + J @ (lam * dx))) for lam in lams])))
                k = None
                for lam in lams:
                    xt = x + lam * dx; xt[-1] = float(np.clip(xt[-1], 0.12, 0.9))
                    g_ws = PM.warm_start(g, x, xt); PM.set_x(xt)
                    gt, Tgt, ht = PM.solve(g_ws, maxit=opt['exit_maxit'], tol=opt['tol'])
                    Ft, inft, lgt = PM.rows(gt); inft['exit_defect'] = ht[-1]['defect_max']; inft['exit_converged'] = ht[-1]['converged']; inft['exit_evaluations'] = ht[-1]['evaluations']
                    PM.set_x(x)
                    ok = np.all(np.isfinite(Ft)) and inft.get('axis_error') is None and inft['arrived_frac'] > 0.999 and inft['band_arrived'] and inft['gamma_ok'] and ht[-1]['converged']
                    log(json.dumps(dict(it=it, trial_lam=lam, normF_try=(inft['normF'] if ok else float('inf')), normF_base=info['normF'], defect=ht[-1]['defect_max'], defect_rms=ht[-1]['defect_rms'], converged=ht[-1]['converged'],
                                        m1=inft['m1'], psi_yy0=inft['psi_yy0'], godd=inft['godd_rel_rms'], b_norm=inft['b_norm'], th12=[inft['th1_deg'], inft['th2_deg']], F_parts=inft['F_parts'], wall=round(time.time() - t0, 1))))
                    if ok:
                        dxk = xt - x; nn = float(dxk @ dxk)
                        if nn > 0 and ht[-1]['converged']:
                            J = J + np.outer((Ft - F) - J @ dxk, dxk) / nn                              # Broyden secant update with the exact residual pair (converged trial states only)
                        if inft['normF'] < info['normF']:
                            k = lam; pred_dec = info['normF'] - float(np.linalg.norm(F + J_frozen @ dxk)); real_dec = info['normF'] - inft['normF']
                            x = xt; F = Ft; g = gt; info = inft; lg = lgt; PM.set_x(x); accepted = True
                            log(json.dumps(dict(it=it, accepted=True, lam=lam, x=[round(float(v), 6) for v in x], normF=info['normF'], step_quality=dict(predicted_decrease=pred_dec, realised_decrease=real_dec, ratio=(real_dec / pred_dec if pred_dec > 0 else None)), info=info)))
                            save_state('runs/pfwd/par/%s_it%d.npz' % (tag, it), PM, g, x, F, info, lg)
                            np.savez('runs/pfwd/par/%s_J_it%d.npz' % (tag, it), J=J, x=x, F=F)
                            break
                if accepted:
                    mu = max(mu / 3, 1e-6); break
                mu *= 10
            if not accepted:
                log(json.dumps(dict(it=it, accepted=False, note='no decrease after 4 LM attempts'))); break
            if info['normF'] < 1e-4:
                log(json.dumps(dict(it=it, converged=True))); break
        Joo = J[PM.odd_rows][:, PM.odd_cols]
        log(json.dumps(dict(final=True, x=[float(v) for v in x], normF=info['normF'], normF_odd=info['normF_odd'], normF_even=info['normF_even'], b_norm=info['b_norm'], godd=info['godd_rel_rms'], psi_yy0=info['psi_yy0'], m1=info['m1'],
                            sv_odd_block_final=[float('%.4g' % v) for v in np.linalg.svd(Joo, compute_uv=False)], wall=round(time.time() - t0, 1))))
        log('PARITY_DONE')
