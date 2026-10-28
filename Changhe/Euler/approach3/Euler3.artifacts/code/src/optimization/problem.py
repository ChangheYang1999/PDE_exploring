"""Least-squares problem: weighted residual vector of the profile equations plus gauge equations.

Weights (fixed gauge, shell balanced):
  shells: core ball [0, R0) and dyadic shells [R0 2^k, R0 2^(k+1)); every shell containing nodes gets total weight
  1/N_shells, spread uniformly over its radial nodes; angular weights w_a / (4 pi) (angular mean).
  scaling: momentum residual multiplied by (1 + r^2/R0^2)^(alpha/2) (r^alpha R_u in the far field),
           vorticity residual by (1 + r^2/R0^2)^(1/(2 c_l))  (r^(1/c_l) R_Omega).
Gauges: dilation  int_S2 |F|^2 dS = 1 with F the leading tail (from the x = 1 limit of the basis),
        azimuthal phase: a chosen sin-type tail amplitude (pivot) is zero.
Formulations: 'vort' (R_Omega only, no pressure), 'mom' (R_u with full-space pressure), 'both'."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations.fields import Model, alpha_of
from ..equations import residuals as res
from ..pressure.poisson_sh import PressureSolver

DT = torch.float64


class Problem:
    def __init__(self, model: Model, formulation="vort", pressure: PressureSolver = None, gauge_weight=100.0,
                 both_weight=1.0, pivot=None, shell_base=2.0, nl_weighting=False, efrac=None, efrac_weight=100.0,
                 gauge="F", Z_star=1.0, sigmaZ=None, sigmaZ_weight=100.0, far_radii=None, far_weight=1.0, nl_weight_cap=1e3,
                 sigmaZ_fine=4, sigmaZ_ramp_iters=0, nl_denominator="nl", far_lambda=1e-2, closure_lambda=0.0, fsw=None, fsw_weight=100.0,
                 nu=0.0, pin_c_l=None, pin_weight=100.0, balance_lambda=0.0, core_pin=None, core_pin_weight=100.0, nonaxi_pin=None, nonaxi_pin_weight=100.0,
                 radial_lambda_w=0.0):
        """gauge: 'F' (int_S2 |F|^2 = 1, SPEC 6.1 primary) or 'Z' (enstrophy Z = int |Omega|^2 dy = Z_star, SPEC 11 v1.5 (iii)
        alternative dilation gauge; int |F|^2 is then monitored). sigmaZ: optional constraint/continuation row on the total
        stretching ratio in normalized form I/Z - sigmaZ*(1 - 3 c_l/2) with I = int Omega.S Omega dy (exact profile: sigmaZ = 1)."""
        self.model, self.formulation = model, formulation
        self.gauge, self.Z_star, self.sigmaZ, self.sigmaZ_weight = gauge, float(Z_star), sigmaZ, sigmaZ_weight
        self.sigmaZ_target_final = sigmaZ            # the ramp (continuation) moves self.sigmaZ from the start value to this
        self.sigmaZ_ramp_iters = sigmaZ_ramp_iters
        # nonlinear-balance denominator: "nl" = RMS_k(T4) + RMS_k(T5) (can be gamed by inflating the core: large nonlinear terms
        # make the core weights tiny, observed c2x2_L8_cl0.45 fixed 21:57Z: weighted rms 1.5e-6, holdout rho_u 0.48);
        # "all5" = sum of the five term RMS values per shell (rho_u-like, neutral under amplitude inflation).
        self.nl_denominator = nl_denominator
        self.far_lambda = float(far_lambda)          # all5far: weight of the far-imbalance term lambda/den_nl on shells r >= 1 (lead 22:40Z (b); default 1e-2)
        # closure rows (SPEC 3 first nonlinear correction; FAILURE_ANALYSIS item 18): residual rows closure_lambda * (G_carried(b) - G_required(F))/||G_required||
        # on a sphere grid, G_carried linear in the B/D coefficients, G_required recomputed (lagged, detached) at every accepted step
        self.closure_lambda = float(closure_lambda); self.closure = None
        if self.closure_lambda > 0 and (model.channels.get("NkB", 0) > 0 or model.channels.get("NkD", 0) > 0):
            self._init_closure()
        # the cubic stretching integrand needs >= 3 Nk radial nodes (astra review2): evaluate Z, I on a dedicated fine model
        self.fine_model = None; self.fine_ps = None
        if (sigmaZ is not None or gauge == "Z") and sigmaZ_fine and sigmaZ_fine * model.Nk > model.Nr_src:
            self.fine_model = Model(L=model.L, Nk=model.Nk, m_parity=model.m_parity, R0=model.R0, Nr=sigmaZ_fine * model.Nk, ntheta=model.ntheta, nphi=model.nphi,
                                    c_l=model.c_l0, omega=model.omega0, free_params=model.free_params, channels=model.channels, device=model.r.device)
            self.fine_ps = PressureSolver(self.fine_model, p0=2 * alpha_of(model.c_l0) + 2)
        # far-field anchoring (training only): pressure-free vorticity residual rows at far checkpoint radii (SPEC 7.1 far
        # checkpoints, here r = far_radii * R0), fixed-gauge scaled; each radius is one shell of weight 1/(n_shells + n_far).
        self.far_radii = None if (not far_radii or getattr(model, "extra_r", None)) else [float(v) * model.R0 for v in far_radii]
        self.far_weight = far_weight
        self.far_model = None
        if self.far_radii:                    # separate far model (older path); with model.extra_r the far nodes are part of the grid
            self.far_model = Model(L=model.L, Nk=model.Nk, m_parity=model.m_parity, R0=model.R0, r_nodes=self.far_radii,
                                   ntheta=getattr(model, "L_ext", model.L) + 3, nphi=2 * getattr(model, "L_ext", model.L) + 4, c_l=model.c_l0, omega=model.omega0,
                                   free_params=model.free_params, channels=model.channels, device=model.r.device)
        self.nl_weighting = nl_weighting      # iteratively reweighted: shell weight 1/(RMS_k(T4)+RMS_k(T5))^2 (frozen per LM iteration)
        self.nl_weight_cap = nl_weight_cap    # max ratio of a shell weight to the median shell weight
        self.efrac, self.efrac_weight = efrac, efrac_weight   # optional continuation constraint on the m != 0 tail energy fraction
        # Stage II S7 (a) (lead stage2_plan_draft S7, 2026-10-25T04:26Z): continuation row on the mean-swirl fraction of the tail,
        # f_sw = (toroidal m = 0 tail energy) / int_S2 |F|^2 (the m = 0 toroidal modes give F_phi only: the mean swirl of F)
        self.fsw, self.fsw_weight = fsw, fsw_weight
        # Stage II S8 (lead 2026-10-25T05:18Z, stage2_plan_draft S8): artificial viscosity, R^nu = R_u - nu Delta U (constant nu, a separately
        # labelled continuation device; never an Euler residual). pin_c_l: with free_params, a row pin_weight (c_l - pin_c_l) keeps c_l fixed while
        # omega moves (S8 formulation: c_l fixed, omega free, nu fixed per run in this prototype).
        self.nu = float(nu); self.pin_c_l = pin_c_l; self.pin_weight = float(pin_weight)
        # Stage II S9 (lead 2026-10-25T05:36Z): scalar rows lambda E_ren and lambda H_tot / int |h| (d64 formulas, src/validation/global_balances.py),
        # appended to the LM residual as scalar rows (reverse-mode Jacobian rows); registered diagnostics, never acceptance criteria
        self.balance_lambda = float(balance_lambda); self._gb = None
        # S8 core nontriviality row (lead 2026-10-25T06:56Z item 4): core_pin_weight (core_rms(U)/core_pin - 1) with core_rms the weighted RMS of U on the
        # training nodes with r < R0; core_pin = the start state's value (set by the worker when the config says "auto")
        self.core_pin = (float(core_pin) if core_pin not in (None, "auto") else None); self.core_pin_weight = float(core_pin_weight)
        # S9b (lead 2026-10-25T07:26Z item 6): guard rows nonaxi_pin_weight (e_core/e_core,0 - 1) and (e_F/e_F,0 - 1); nonaxi_pin = (e_core,0, e_F,0) set by the
        # worker from the start state when the config says "auto". e_F = SPEC 7.4 tail non-axisymmetric energy fraction; e_core = max over the training
        # shells with r_hi <= 1 of RMS(U - <U>_phi)^2 / RMS(U)^2 (spherical components, node weights)
        self.nonaxi_pin = (tuple(float(v) for v in nonaxi_pin) if isinstance(nonaxi_pin, (list, tuple)) else None); self.nonaxi_pin_weight = float(nonaxi_pin_weight)
        # Stage II S12 (lead 2026-10-25T11:27Z, registered before data; d93: the residual of the exports is mostly lambda(r) U with lambda > 0): sphere rows
        # sqrt(w) sqrt(w_k) sc_k <U . R_u>_k / <|U|^2>_k^(1/2) on every radial training node k (<.>_k the angular mean, sc_k the fixed-gauge scaling and the
        # nonlinear weight of the momentum rows), so that the squares of the rows sum to w times the radial-lambda part of the weighted squared momentum
        # residual (the part along lambda_k U per sphere). Readings R13 on the radial-lambda share and the holdout ratio. Diagnostics: radial_lambda_diagnostics.
        self.radial_lambda_w = float(radial_lambda_w)
        self.nl_w_mom = None; self.nl_w_vort = None
        self.pressure = pressure
        if (formulation in ("mom", "both") or gauge == "Z" or sigmaZ is not None) and pressure is None:
            self.pressure = PressureSolver(model, p0=2 * alpha_of(model.c_l0) + 2)   # also provides the volume weights (decay 2/c_l)
        self.gauge_weight = gauge_weight
        self.both_weight = both_weight
        dev = model.r.device
        # shell weights
        r = model.r.cpu().numpy(); R0 = model.R0
        edges = [0.0, R0]
        while edges[-1] < r.max():
            edges.append(edges[-1] * shell_base)
        shell_id = np.searchsorted(edges, r, side="right") - 1
        ids, counts = np.unique(shell_id, return_counts=True)
        nsh = len(ids)
        wnode = np.zeros_like(r)
        for sid, cnt in zip(ids, counts):
            wnode[shell_id == sid] = 1.0 / (nsh * cnt)
        if getattr(model, "extra_r", None):                     # merged far anchoring nodes: shells scaled by far_weight
            n_src = model.Nr_src
            wnode[n_src:] *= far_weight
        self.shell_id = torch.tensor(shell_id, dtype=torch.long, device=dev)
        self.shell_edges = edges
        self.n_shells = nsh
        self.w_node = torch.tensor(wnode, dtype=DT, device=dev)
        self.w_ang = model.grid.w / (4 * math.pi)
        self.pivot = pivot          # dict(pot='T'|'S', q=int) or None
        self.l = model.l_arr

    # ----- scalings -----
    def scale_mom(self, c_l):
        a = alpha_of(c_l)
        return (1 + self.model.rho / self.model.R0 ** 2) ** (a / 2)

    def scale_vort(self, c_l):
        return (1 + self.model.rho / self.model.R0 ** 2) ** (1 / (2 * c_l))

    # ----- tail amplitudes and gauges -----
    def tail_amplitudes(self, aT, aS, c_l):
        """t_q^inf, s_q^inf: U ~ r^-alpha with T_q ~ t_q r^-alpha, S_q ~ s_q r^(1-alpha)."""
        a = alpha_of(c_l); R0 = self.model.R0; l = self.l
        t = aT.sum(0) * R0 ** (a + l)
        s = aS.sum(0) * R0 ** (a + l - 1)
        return t, s

    def mode_tail_energies(self, aT, aS, c_l, omega):
        """Per-mode contributions to int_S2 |F|^2 dS (toroidal eT, poloidal eS). F = -Lap_S2 sigma e_r
        + grad_S2[(2-alpha) sigma + (omega/c_l) d_chi sigma] - e_r x grad_S2 tau (SPEC 3.2), so
        eT = l(l+1) t^2, eS = [l^2(l+1)^2 + l(l+1)((2-alpha)^2 + (m omega/c_l)^2)] s^2 (orthogonal pieces)."""
        a = alpha_of(c_l); l = self.l; m = self.model.m_arr.to(DT)
        t, s = self.tail_amplitudes(aT, aS, c_l)
        eT = t ** 2 * l * (l + 1)
        eS = s ** 2 * (l ** 2 * (l + 1) ** 2 + l * (l + 1) * ((2 - a) ** 2 + (m * omega / c_l) ** 2))
        return eT, eS

    def tail_norm2(self, aT, aS, c_l, omega=None):
        """int_S2 |F|^2 dS (F-gauge quantity)."""
        omega = self._omega(omega)
        eT, eS = self.mode_tail_energies(aT, aS, c_l, omega)
        return eT.sum() + eS.sum()

    def _omega(self, omega):
        if omega is not None:
            return omega
        return torch.tensor(self.model.omega0, dtype=DT, device=self.model.r.device)

    def choose_pivot(self, z, rank=1):
        """SPEC 6.2 phase pivot: the m != 0 cos/sin tail pair of largest amplitude (rank 1, the production default, unchanged code path).
        rank > 1 (Stage III R2d, lead IE S3-5): the rank-th largest pair; the returned dict then also carries 'rank' and 'margin' (its amplitude over the
        next pair's)."""
        aT, aS, c_l, omega = self.model.unpack(z)
        eT, eS = self.mode_tail_energies(aT, aS, c_l, omega)
        ampT, ampS = eT.sqrt(), eS.sqrt()
        m = self.model.m_arr
        if int(rank) <= 1:
            best = None
            for q, (ll, mm, tt) in enumerate(self.model.modes):
                if mm == 0 or tt != 0:
                    continue
                for pot, amp in (("T", ampT), ("S", ampS)):
                    v = math.hypot(amp[q].item(), amp[q + 1].item())
                    if best is None or v > best[0]:
                        best = (v, pot, q)
            if best is None or best[0] == 0.0:
                return None
            return dict(pot=best[1], q=best[2], amp=best[0])
        cands = []
        for q, (ll, mm, tt) in enumerate(self.model.modes):
            if mm == 0 or tt != 0:
                continue
            for pot, amp in (("T", ampT), ("S", ampS)):
                cands.append((math.hypot(amp[q].item(), amp[q + 1].item()), pot, q))
        cands.sort(key=lambda c: -c[0])
        r = int(rank)
        if len(cands) < r or cands[r - 1][0] == 0.0:
            return None
        nxt = cands[r][0] if len(cands) > r else 0.0
        return dict(pot=cands[r - 1][1], q=cands[r - 1][2], amp=cands[r - 1][0], rank=r, margin=(cands[r - 1][0] / nxt if nxt > 0 else float("inf")))

    def tail_mean_swirl_fraction(self, aT, aS, c_l, omega=None):
        """f_sw = sum over m = 0 toroidal modes of eT / int_S2 |F|^2 (the mean azimuthal part of the leading tail F)."""
        omega = self._omega(omega); m = self.model.m_arr
        eT, eS = self.mode_tail_energies(aT, aS, c_l, omega)
        return eT[m == 0].sum() / (eT.sum() + eS.sum()).clamp_min(1e-300)

    def tail_nonaxi_energy(self, aT, aS, c_l, omega=None):
        omega = self._omega(omega); m = self.model.m_arr
        eT, eS = self.mode_tail_energies(aT, aS, c_l, omega)
        return (eT + eS)[m > 0].sum()

    def maybe_rebuild_pressure(self, z, tol=0.0):
        """Free-parameter runs: rebuild the pressure kernels (and the fine-grid volume weights of the Sigma_Z row) whenever (c_l, omega)
        differ from the stored ones by more than tol (default 0: at every accepted step, so that the coefficient Jacobian columns, the
        base and the trial costs use one discretization at the exact base parameters)."""
        if self.pressure is None or not self.model.free_params:
            return False
        aT, aS, c_l, omega = self.model.unpack(z)
        c_l, omega = float(c_l), float(omega)
        ps = self.pressure
        if abs(omega / c_l - ps.kappa) > tol * max(abs(ps.kappa), 1e-3) or abs(c_l - ps.c_l) > tol or abs(omega - ps.omega) > tol:
            self.pressure = PressureSolver(self.model, p0=2 * alpha_of(c_l) + 2, omega=omega, c_l=c_l)
            if self.fine_model is not None:
                self.fine_ps = PressureSolver(self.fine_model, p0=2 * alpha_of(c_l) + 2, omega=omega, c_l=c_l)
            return True
        return False

    def residual_vector_rebuild(self, z):
        """Residual with the pressure kernels rebuilt at z's own (c_l, omega) (for finite-difference parameter columns);
        restores the previous solver afterwards."""
        if self.pressure is None or not self.model.free_params:
            return self.residual_vector(z)
        saved, saved_fine = self.pressure, self.fine_ps
        aT, aS, c_l, omega = self.model.unpack(z)
        c_l, omega = float(c_l), float(omega)
        if abs(c_l - saved.c_l) > 0 or abs(omega - saved.omega) > 0:
            self.pressure = PressureSolver(self.model, p0=2 * alpha_of(c_l) + 2, omega=omega, c_l=c_l)
            if self.fine_model is not None:
                self.fine_ps = PressureSolver(self.fine_model, p0=2 * alpha_of(c_l) + 2, omega=omega, c_l=c_l)
        try:
            r = self.residual_vector(z)
        finally:
            self.pressure, self.fine_ps = saved, saved_fine
        return r

    def _init_closure(self, c_l=None, omega=None):
        from ..far_field.correction import carried_patterns
        from ..bases.solid_harmonics import AngularGrid
        model = self.model
        c_l = float(model.c_l0 if c_l is None else c_l); omega = float(model.omega0 if omega is None else omega)
        L = model.L
        grid = AngularGrid(2 * L + 10, 4 * L + 18, device=model.r.device)
        V, labels = carried_patterns(model, c_l, omega, model.R0 * grid.n)              # (Na, 3, J) unit patterns incl. R0^(2alpha+1)
        idx = torch.tensor([model.modes.index(lab[1:]) for lab in labels], dtype=torch.long, device=model.r.device)
        isB = torch.tensor([lab[0] == "B" for lab in labels], dtype=torch.bool, device=model.r.device)
        lq = torch.tensor([float(lab[1]) for lab in labels], dtype=DT, device=model.r.device)
        self.closure = dict(V=V.detach(), idx=idx, isB=isB, l=lq, w=(grid.w / (4 * math.pi)).sqrt(), grid=grid, c_l=c_l, omega=omega, G_req=None, G_req_norm=None, mismatch=None)

    def update_closure(self, z):
        """Recompute the lagged target G_required(F) (detached) from the current leading tail; refresh the patterns if (c_l, omega) moved."""
        if self.closure is None:
            return
        from ..far_field.correction import first_correction
        with torch.no_grad():
            aT, aS, c_l, omega = self.model.unpack(z)
        c_lf, omf = float(c_l), float(omega)
        if abs(c_lf - self.closure["c_l"]) > 1e-14 or abs(omf - self.closure["omega"]) > 1e-14:
            self._init_closure(c_lf, omf)
        fc = first_correction(self, z.detach(), ntheta=self.closure["grid"].ntheta, nphi=self.closure["grid"].nphi)
        self.closure["G_req"] = fc["G"].detach(); self.closure["G_req_norm"] = max(fc["G_norm"], 1e-300)
        with torch.no_grad():
            Gc = self.carried_G(z.detach())
            self.closure["mismatch"] = float((((Gc - fc["G"]) ** 2).sum(-1) * self.closure["grid"].w).sum().sqrt() / self.closure["G_req_norm"])

    def carried_G(self, z):
        """G carried by the B/D coefficients (linear in z): coefficient R0^(2alpha+1+l) sum_k B_kq (B) or R0^(2alpha+l) sum_k D_kq (D) on the unit patterns."""
        d = self.model.unpack_all(z)
        alpha = alpha_of(d["c_l"]); R0 = self.model.R0; cl = self.closure
        cB = d["B"].sum(0)[cl["idx"]] * R0 ** (2 * alpha + 1 + cl["l"]) if d["B"].numel() else torch.zeros(len(cl["idx"]), dtype=DT, device=z.device)
        cD = d["D"].sum(0)[cl["idx"]] * R0 ** (2 * alpha + cl["l"]) if d["D"].numel() else torch.zeros(len(cl["idx"]), dtype=DT, device=z.device)
        c = torch.where(cl["isB"], cB, cD)
        return torch.einsum('aij,j->ai', cl["V"], c)

    def closure_rows(self, z):
        cl = self.closure
        if cl is None or cl["G_req"] is None:
            return None
        Gc = self.carried_G(z)
        return (self.closure_lambda / cl["G_req_norm"]) * (cl["w"][:, None] * (Gc - cl["G_req"])).reshape(-1)

    def update_nl_weights(self, z):
        """Recompute the per-node nonlinear-balance weights from the current state (detached)."""
        if not self.nl_weighting:
            return
        from ..validation.spec_diagnostics import five_term_split, vorticity_split
        with torch.no_grad():
            model = self.model
            ev = self.evaluate(z)
            F = ev['F']
            def shell_w(terms, sc=None, far_lambda=None, split=False):
                # per-shell denominator: sum over the given terms of RMS_k(term) (angular mean, node mean inside the shell).
                # "nl": raw T4, T5. "all5": the five terms multiplied by the row scaling sc (the same (1+r^2/R0^2)^(alpha/2)
                # that the residual rows carry), so that the weighted shell cost is RMS_k(scaled R) / sum_i RMS_k(scaled T_i):
                # a rho_u-like objective, neutral under core amplitude inflation and without the extra far-shell emphasis.
                rms_k = []
                for t in terms:
                    per_node = ((t ** 2).sum(0) * self.w_ang[None, :]).sum(1)
                    if sc is not None:
                        per_node = per_node * sc ** 2
                    d = torch.zeros(len(self.shell_edges), dtype=DT, device=z.device)
                    for sid in self.shell_id.unique().tolist():
                        msk = self.shell_id == sid
                        d[sid] = per_node[msk].mean().sqrt()
                    rms_k.append(d)
                den = sum(rms_k)
                if split:
                    # lead 23:19Z (d29, SPEC v1.14): shell weight 1/min(lin sum, nl sum)^2 with lin = T1+T2+T3 and nl = T4+T5 RMS sums,
                    # so that a core whose large nonlinear terms cancel each other (near-steady Euler core) is normalized by the
                    # smaller self-similar group and does not look converged. Pilot until astra steadycore1 is reviewed.
                    den = torch.minimum(rms_k[0] + rms_k[1] + rms_k[2], rms_k[3] + rms_k[4])
                floor = torch.clamp(1e-6 * den.max(), min=1e-300)
                w = 1.0 / (den + floor) ** 2
                if far_lambda is not None:
                    # lead 22:40Z request (b): far imbalance must cost something. Row scaling 1/den5 + lambda/den_nl on shells with
                    # r >= 1 (den_nl = RMS of the two nonlinear terms, scaled), lambda = 1e-2 (the Tier S rho_nl ratio); core shells keep
                    # the five-term weights so that inflating the core stays unrewarded.
                    den_nl = rms_k[3] + rms_k[4]
                    far = torch.tensor([float(e) >= 1.0 for e in self.shell_edges], dtype=torch.bool, device=z.device)   # lower edges
                    sc_far = 1.0 / (den + floor) + far_lambda / (den_nl + torch.clamp(1e-6 * den_nl.max(), min=1e-300))
                    w = torch.where(far, sc_far ** 2, w)
                occupied = torch.zeros(len(self.shell_edges), dtype=torch.bool, device=z.device); occupied[self.shell_id.unique()] = True
                wmed = w[occupied].median()
                w = torch.clamp(w, max=self.nl_weight_cap * wmed)          # far shells with tiny nonlinear terms cannot dominate
                # Mean-normalized (mean weight one over nodes). Frozen per-iteration weights cannot implement an
                # amplitude penalty: without normalization the weights grow without bound as the field shrinks, the gauge
                # row becomes negligible and LM collapses to U = 0 (observed 2026-10-24T18:53-18:59Z, lead's note). So this
                # option is a shell REBALANCING of the residual by the local nonlinear scale, nothing more.
                return w[self.shell_id] / w[self.shell_id].mean()
            fl = self.far_lambda if self.nl_denominator == "all5far" else None
            sp = self.nl_denominator == "split"
            if 'R_u' in ev:
                T = five_term_split(F, ev['gradP'])
                if self.nu > 0 and 'LapU' in ev:
                    T = T + [-self.nu * ev['LapU']]                  # S8: the viscous term is one more term in the denominators
                self.nl_w_mom = shell_w(T, self.scale_mom(F['c_l']), fl, sp) if self.nl_denominator in ("all5", "all5far", "split") else shell_w([T[3], T[4]])
            if 'R_Om' in ev:
                V = vorticity_split(F)
                self.nl_w_vort = shell_w(V, self.scale_vort(F['c_l']), fl, sp) if self.nl_denominator in ("all5", "all5far", "split") else shell_w([V[3], V[4]])

    def gauge_defects(self, z):
        """Independent of the residual vector: |int |F|^2 - 1| and the pivot phase defect |sin-part|/|pivot amplitude|."""
        aT, aS, c_l, omega = self.model.unpack(z)
        with torch.no_grad():
            if self.gauge == "Z":
                Z, I = self.enstrophy_and_stretching(None, z=z) if self.fine_model is not None else self.enstrophy_and_stretching(self.model.fields_grid(z, need_vort=True))
                g = abs(Z.item() / self.Z_star - 1.0)
            else:
                g = abs(self.tail_norm2(aT, aS, c_l, omega).item() - 1.0)
            pd = None
            if self.pivot is not None:
                t, s = self.tail_amplitudes(aT, aS, c_l)
                amp = t if self.pivot["pot"] == "T" else s
                q = self.pivot["q"]
                mag = math.hypot(amp[q].item(), amp[q + 1].item())
                pd = abs(amp[q + 1].item()) / mag if mag > 0 else None
        return g, pd

    def enstrophy_and_stretching(self, F, z=None):
        """Z = int |Omega|^2 dy and I = int Omega.S Omega dy with the factored radial weights (decay 2/c_l); on the fine model
        (Nr = sigmaZ_fine * Nk) when available and z is given, else on the training grid (F)."""
        if self.fine_model is not None and z is not None:
            Ff = self.fine_model.fields_grid(z, need_vort=True); ps = self.fine_ps
            Om, GU = Ff['Om'], Ff['GU']
        else:
            Om, GU = F['Om'], F['GU']; ps = self.pressure
        S = 0.5 * (GU + GU.transpose(0, 1))
        q = (Om ** 2).sum(0)
        OSO = torch.einsum('i...,ij...,j...->...', Om, S, Om)
        return ps.volume_integral(q), ps.volume_integral(OSO)

    def set_sigmaZ_ramp(self, z):
        """Continuation: start the Sigma_Z target at the state's current value (fine grid) and move it to the final target over
        sigmaZ_ramp_iters accepted iterations (call once at the start of a run)."""
        if self.sigmaZ_target_final is None or self.sigmaZ_ramp_iters <= 0:
            return
        with torch.no_grad():
            Z, I = self.enstrophy_and_stretching(None, z=z)
            c_l = float(self.model.unpack(z)[2])
            self._sigmaZ_start = float((I / Z) / (1 - 1.5 * c_l)); self._ramp_it = 0
            self.sigmaZ = self._sigmaZ_start

    def step_sigmaZ_ramp(self):
        if self.sigmaZ_target_final is None or self.sigmaZ_ramp_iters <= 0 or not hasattr(self, "_ramp_it"):
            return False
        self._ramp_it += 1
        t = min(1.0, self._ramp_it / self.sigmaZ_ramp_iters)
        new = self._sigmaZ_start + (self.sigmaZ_target_final - self._sigmaZ_start) * t
        changed = abs(new - self.sigmaZ) > 1e-15
        self.sigmaZ = new
        return changed

    def gauge_residuals(self, aT, aS, c_l, omega=None, F=None, z=None, include_sigmaZ=True):
        """F: field dict with vorticity (needed for the Z gauge or the Sigma_Z row); if None and z is given, it is computed."""
        omega = self._omega(omega)
        if F is None and (self.gauge == "Z" or self.sigmaZ is not None) and self.fine_model is None:
            if z is None:
                raise ValueError("gauge_residuals needs F or z when the Z gauge or Sigma_Z row is active")
            F = self.model.fields_grid(z, need_vort=True)
        # rows are returned WITH their absolute weights: gauge_weight for the dilation gauge, sigmaZ_weight (default 100) and
        # efrac_weight (default 100) for the constraint rows (decoupled from the gauge weight; a 1e3 Sigma_Z row stalled LM)
        if self.gauge == "Z":
            Z, I = self.enstrophy_and_stretching(F, z=z)
            g = [self.gauge_weight * (Z / self.Z_star - 1.0)]
        else:
            g = [self.gauge_weight * (self.tail_norm2(aT, aS, c_l, omega).clamp_min(1e-300).sqrt() - 1.0)]   # ||F|| - 1 (norm form)
        if self.sigmaZ is not None and include_sigmaZ:
            if self.gauge != "Z":
                Z, I = self.enstrophy_and_stretching(F, z=z)
            g.append(self.sigmaZ_weight * (I / Z.clamp_min(1e-300) - self.sigmaZ * (1.0 - 1.5 * c_l)))
        if self.efrac is not None:
            # fraction form E_{m!=0}/||F||^2 (equivalent to the absolute form only on the exact F-gauge; astra review2)
            g.append(self.efrac_weight * (self.tail_nonaxi_energy(aT, aS, c_l, omega) / self.tail_norm2(aT, aS, c_l, omega).clamp_min(1e-300) - self.efrac))
        if self.fsw is not None:
            g.append(self.fsw_weight * (self.tail_mean_swirl_fraction(aT, aS, c_l, omega) - self.fsw))
        if self.pin_c_l is not None and self.model.free_params:
            g.append(self.pin_weight * (c_l - self.pin_c_l))
        if self.core_pin is not None:
            if F is None:
                F = self.model.fields_grid(z, need_vort=False)
            g.append(self.core_pin_weight * (self.core_rms(F) / self.core_pin - 1.0))
        if self.nonaxi_pin is not None:
            if F is None:
                F = self.model.fields_grid(z, need_vort=False)
            g.append(self.nonaxi_pin_weight * (self.e_core_training(F) / self.nonaxi_pin[0] - 1.0))
            g.append(self.nonaxi_pin_weight * (self.e_F_tail(aT, aS, c_l, omega) / self.nonaxi_pin[1] - 1.0))
        # the azimuthal phase gauge is imposed by the exact symmetry projection phase_align (not a residual row)
        return torch.stack(g)

    def phase_align(self, z):
        """Rotate the state about the z axis (exact symmetry of the equations) so that the pivot pair's sin-type tail
        amplitude vanishes. Field rotation by gamma: cos-mode a_c' = a_c cos(m gamma) + a_s sin(m gamma),
        sin-mode a_s' = -a_c sin(m gamma) + a_s cos(m gamma) (same convention as the twist pair rotation)."""
        if self.pivot is None:
            return z
        model = self.model
        d = model.unpack_all(z)
        q = self.pivot["q"]; mq = int(model.m_arr[q].item())
        arr = d["A"] if self.pivot["pot"] == "T" else d["C"]
        ac, as_ = arr[:, q].sum(), arr[:, q + 1].sum()                 # tail amplitudes up to the common R0 factor
        gamma = torch.atan2(as_, ac) / mq                                # choose gamma with a_s' = 0 and a_c' >= 0
        m = model.m_arr.to(z.dtype)
        cm, sm = torch.cos(m * gamma), torch.sin(m * gamma)
        sign = model.tw_sign; partner = model.partner
        def rot(a):
            ap = a[:, partner]
            # cos modes (sign +1): a cos + partner sin ; sin modes (sign -1): a cos - partner sin ; m = 0 unchanged (sin = 0)
            return a * cm[None, :] + sign[None, :] * ap * sm[None, :]
        extra = {k: rot(d[k]) for k in ("B", "D", "E") if d[k].numel() > 0}
        znew = model.pack(rot(d["A"]), rot(d["C"]), d["c_l"], d["omega"], extra=extra)
        return znew

    # ----- residuals -----
    def evaluate(self, z, need_terms=False):
        """Return dict with fields F, residual tensors R_u (3,Nr,Na) [if mom/both], R_Om, pressure P, terms."""
        model = self.model
        need_vort = self.formulation in ("vort", "both") or self.gauge == "Z" or self.sigmaZ is not None
        F = model.fields_grid(z, need_vort=need_vort)
        out = dict(F=F)
        if self.formulation in ("mom", "both"):
            f = res.pressure_source(F['GU'])
            P, gradP, Plm, dPlm = self.pressure.solve(f)
            mt = res.momentum_terms(F, gradP)
            if self.nu > 0:                                         # S8: R^nu = R_u - nu Delta U
                lap = model.laplacian_grid(z)
                mt['visc'] = -self.nu * lap; mt['sum'] = mt['sum'] + mt['visc']
                out['LapU'] = lap
            out.update(R_u=mt['sum'], P=P, gradP=gradP, mom_terms=mt)
        if need_vort:
            vt = res.vorticity_terms(F)
            out.update(R_Om=vt['sum'], vort_terms=vt)
        return out

    def e_core_training(self, F, r_tail=None):
        """SPEC 7.4 e_core on the training grid exactly as spec_diagnostics computes it (Shells weights r^2 dr, angular means): max over the shells
        with lower edge <= r_tail of RMS_k(U - <U>_phi)^2 / RMS_k(U)^2 (spherical components); differentiable in the coefficients."""
        from ..validation.spec_diagnostics import Shells
        model = self.model; U = F['U']
        sh = getattr(self, "_shells_train", None)
        if sh is None:
            sh = Shells(model); self._shells_train = sh
        er, eth, eph = model.grid.sph_basis()
        Us = torch.stack([torch.einsum('ija,ai->ja', U, e) for e in (er, eth, eph)], 0).reshape(3, model.Nr, model.ntheta, model.nphi)
        dev = (Us - Us.mean(-1, keepdim=True)).reshape(3, model.Nr, model.Na)
        num = ((dev ** 2).sum(0) * sh.w_ang[None, :]).sum(1); den = ((U ** 2).sum(0) * sh.w_ang[None, :]).sum(1)
        rt = float(r_tail) if r_tail is not None else (self.nonaxi_r_tail if getattr(self, "nonaxi_r_tail", None) is not None else float("inf"))
        vals = []
        for k, m in enumerate(sh.masks):
            if sh.edges[k][0] <= rt:
                w = sh.wvol[m]
                vals.append(((num[m] * w).sum() / w.sum()) / (((den[m] * w).sum() / w.sum()).clamp_min(1e-300)))
        return torch.stack(vals).max() if vals else torch.zeros((), dtype=DT, device=U.device)

    def e_F_tail(self, aT, aS, c_l, omega):
        return self.tail_nonaxi_energy(aT, aS, c_l, omega) / self.tail_norm2(aT, aS, c_l, omega).clamp_min(1e-300)

    def core_rms(self, F):
        """Weighted RMS of U over the training nodes with r < R0 (node weights w_node x angular weights)."""
        model = self.model
        msk = (model.r < model.R0)
        w = (self.w_node[msk][:, None] * self.w_ang[None, :])
        return (((F['U'][:, msk, :] ** 2).sum(0) * w).sum() / w.sum()).sqrt()

    def balance_rows(self, z):
        """S9: (lambda E_ren, lambda H_tot / int |h|) of the state, differentiable in z."""
        from ..validation.global_balances import GlobalBalances
        if self._gb is None:
            self._gb = GlobalBalances(self.model)
        b = self._gb.integrals(z)
        return torch.stack([self.balance_lambda * b["E_ren"], self.balance_lambda * b["H_tot_over_abs"]])

    def radial_lambda_parts(self, ev, c_l):
        """Per radial node k: a_k = <U . R_u>_k, b_k = <|U|^2>_k (angular means), the momentum-row weights q_k = w_k sc_k^2 (nl weight included) and the
        node-weighted radial-lambda part q_k a_k^2 / b_k of the weighted squared momentum residual (S12, d93)."""
        U = ev['F']['U']; R = ev['R_u']
        a = ((U * R).sum(0) * self.w_ang[None, :]).sum(1)                         # (Nr,)
        b = ((U ** 2).sum(0) * self.w_ang[None, :]).sum(1).clamp_min(1e-300)
        sc = self.scale_mom(c_l)
        if self.nl_weighting and self.nl_w_mom is not None:
            sc = sc * self.nl_w_mom.sqrt()
        q = self.w_node * sc ** 2
        return a, b, q

    def radial_lambda_rows(self, ev, c_l):
        """S12 rows r_k = sqrt(w) sqrt(q_k) a_k / sqrt(b_k) (sum of squares = w x radial-lambda part); None when the weight is 0."""
        if self.radial_lambda_w <= 0 or self.formulation not in ("mom", "both"):
            return None
        a, b, q = self.radial_lambda_parts(ev, c_l)
        return math.sqrt(self.radial_lambda_w) * q.sqrt() * a / b.sqrt()

    def radial_lambda_diagnostics(self, z):
        """d93 structure on the training grid: lambda_k = a_k / b_k, the share of the weighted squared momentum residual carried by lambda_k U
        (sum_k q_k a_k^2 / b_k divided by sum_k q_k <|R_u|^2>_k), the pointwise along-U share, lambda max and its radius, the fraction of the
        node-weighted int U . R_u carried by nodes with negative pairing, and the sign of lambda per octave of r/R0."""
        with torch.no_grad():
            ev = self.evaluate(z)
            aT, aS, c_l, omega = self.model.unpack(z)
            a, b, q = self.radial_lambda_parts(ev, c_l)
            U = ev['F']['U']; R = ev['R_u']
            tot = (q * ((R ** 2).sum(0) * self.w_ang[None, :]).sum(1)).sum()
            rad = (q * a ** 2 / b).sum()
            UR = (U * R).sum(0); U2 = (U ** 2).sum(0).clamp_min(1e-300)
            pw = (q[:, None] * self.w_ang[None, :] * UR ** 2 / U2).sum() / tot.clamp_min(1e-300)
            lam = a / b; r = self.model.r
            vol = self.w_node * a
            neg = float(vol[vol < 0].sum().abs() / vol.abs().sum().clamp_min(1e-300))
            k = int(torch.argmax(lam.abs()).item())
            octs = {}
            for j in range(-6, 8):
                m = (r >= self.model.R0 * 2.0 ** j) & (r < self.model.R0 * 2.0 ** (j + 1))
                if m.any():
                    octs[f"2^{j}"] = float((self.w_node[m] * a[m]).sum() / (self.w_node[m] * b[m]).sum())
        return dict(radial_lambda_share=float(rad / tot.clamp_min(1e-300)), pointwise_along_U_share=float(pw), lambda_max=float(lam[k]), r_at_lambda_max=float(r[k]),
                    negative_pairing_fraction=neg, lambda_by_octave=octs, n_octaves_negative=sum(1 for v in octs.values() if v < 0), total_weighted_sq_residual=float(tot))

    def sigmaZ_row(self, z):
        """Scalar Sigma_Z constraint row (fine grid), weighted; for lm_solve(scalar_rows=...)."""
        aT, aS, c_l, omega = self.model.unpack(z)
        Z, I = self.enstrophy_and_stretching(None, z=z)
        return self.sigmaZ_weight * (I / Z.clamp_min(1e-300) - self.sigmaZ * (1.0 - 1.5 * c_l))

    def residual_vector(self, z, include_sigmaZ=True):
        model = self.model
        aT, aS, c_l, omega = model.unpack(z)
        ev = self.evaluate(z)
        wn = (self.w_node[:, None] * self.w_ang[None, :]).sqrt()        # (Nr, Na)
        parts = []
        if self.formulation in ("mom", "both"):
            sc = self.scale_mom(c_l)
            if self.nl_weighting and self.nl_w_mom is not None:
                sc = sc * self.nl_w_mom.sqrt()
            parts.append((ev['R_u'] * (wn * sc[:, None])[None]).reshape(-1))
        if self.formulation in ("vort", "both"):
            w = self.both_weight if self.formulation == "both" else 1.0
            sc = self.scale_vort(c_l)
            if self.nl_weighting and self.nl_w_vort is not None:
                sc = sc * self.nl_w_vort.sqrt()
            parts.append((w * ev['R_Om'] * (wn * sc[:, None])[None]).reshape(-1))
        if self.far_model is not None:
            Ff = self.far_model.fields_grid(z, need_vort=True)
            Rf = res.vorticity_terms(Ff)['sum']                                            # (3, n_far, Na)
            scf = (1 + self.far_model.rho / self.model.R0 ** 2) ** (1 / (2 * c_l))         # fixed-gauge scaling
            wf = (self.far_weight / (self.n_shells + len(self.far_radii))) * torch.ones_like(scf)
            wnf = (wf[:, None] * (self.far_model.grid.w / (4 * math.pi))[None, :]).sqrt()
            parts.append((Rf * (wnf * scf[:, None])[None]).reshape(-1))
        cr = self.closure_rows(z)
        if cr is not None:
            parts.append(cr)
        rl = self.radial_lambda_rows(ev, c_l) if self.radial_lambda_w > 0 else None     # S12 sphere rows (lead 11:27Z)
        if rl is not None:
            parts.append(rl)
        parts.append(self.gauge_residuals(aT, aS, c_l, omega, F=ev['F'], z=z, include_sigmaZ=include_sigmaZ))
        return torch.cat(parts)

    def residual_vector_main(self, z):
        """Residual without the Sigma_Z row (the row is supplied separately as a scalar row to lm_solve)."""
        return self.residual_vector(z, include_sigmaZ=False)

    def n_pde_residuals(self):
        n = 0
        if self.formulation in ("mom", "both"):
            n += 3 * self.model.Nr * self.model.Na
        if self.formulation in ("vort", "both"):
            n += 3 * self.model.Nr * self.model.Na
        return n

    # ----- diagnostics -----
    def shell_rms(self, R, scale):
        """RMS of a (3,Nr,Na) residual per shell, with the fixed-gauge scaling, and the global weighted RMS."""
        sq = (R ** 2).sum(0) * scale[:, None] ** 2                 # (Nr, Na)
        per_node = (sq * self.w_ang[None, :]).sum(1)              # angular mean per node
        out = []
        for sid in range(self.n_shells):
            mask = self.shell_id == sid
            if mask.any():
                out.append(per_node[mask].mean().sqrt().item())
        glob = (per_node * self.w_node).sum().sqrt().item()
        return out, glob
