"""Least-squares problem: unknown coefficient vector -> weighted residual vector and analytic Jacobian.

Unknown layout x = [phi coefficients of element 0, ..., phi coefficients of element E-1,
                    q coefficients of element 0, ..., q coefficients of element E-1,
                    (c_l if cfg.free_cl), (z0 if cfg.s1_constraint)].
Indices of the scalar unknowns are prob.ix_cl and prob.ix_z0 (None when absent).

Ball and shell elements use the same basis for phi and q.  The exterior element uses separate exponent
sets: phi gets {alpha} U {3,4,...} closed under (a,b)->a+b+1; q gets {alpha+1} closed under
(a_phi, b_q) -> a+b+1 (see basis.exterior_exponents).  Sharing them would create columns whose scaled
far-field residual grows like a positive power of R (badly conditioned, physically wrong terms).

Residual rows (all float64):
  PDE rows:        sqrt(w_node) * scale_q(R)   * R_q      for every collocation node of every element
                   sqrt(w_node) * scale_eta(R) * R_eta
  interface rows:  w_int * Rint^m [d^m_R f_A - d^m_R f_B] at the angular Gauss nodes of each element interface,
                   m = 0..3 for f = phi (C^3) and m = 0..2 for f = q (C^2).  Both sides share the Legendre basis in
                   mu, so matching at nmu >= nmax+1 angular nodes controls every mixed derivative as well: the
                   velocity is then Cartesian C^2 across the interface (SPEC section 2 and 6.5).
  reg rows:        w_reg_ext * c  for every non-leading exterior coefficient (Tikhonov, small)
  gauge row:       w_gauge * ( G - 1 ),  G = int_{S^2} F_theta^2 dS ("swirl" gauge) or int |F|^2 dS ("full", SPEC 3.2),
                   F = leading far-field angular velocity profile from the leading exterior coefficients.
  S1 rows (cfg.s1_constraint): w_s1 * (phi_z(0, z0) - 1/2) and w_s1 * (c_l z0 + 2 phi(0, z0)), with z0 an unknown:
                   an axis stagnation point of W_m at (0, z0) carrying swirl must have d_r U^r = -1/2 there
                   (SPEC section 7, scenario S1).  z0 is never pinned; its start value is cfg.z0_init.
Node weights: quadrature weight wR*wmu, renormalized so that every dyadic radial shell carries the same
total weight (balanced shells, PROMPT.md section 9); no volume factor r, so the axis is not hidden.
Row scales: scale_q = (1+R^2)^((2 alpha + 2 + s)/d), scale_eta = (1+R^2)^((2 alpha + 3 + s)/d) with s = cfg.scale_power_shift and
d = cfg.scale_divisor. d = 2 gives rows ~ R^(2 alpha + 2) R_q and R^(2 alpha + 3) R_eta (PROMPT section 9, SPEC; lead note 16);
d = 4 (the shift-1 choice used by every job before 2026-10-28T21:45Z) weights the cost by the first power of those multipliers only,
which hides the first nonlinear far-field correction from the optimizer (FAILURE_ANALYSIS 8).  Holdout diagnostics always use the
unweighted scaled residuals of the prompt.
Point rows and S1 rows are weighted least-squares (penalty) rows, not exact constraints; their defects are reported with every result.
"""
from __future__ import annotations

import json
import math
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Tuple

import numpy as np
import torch

from . import basis, ops

DT = torch.float64
PHI_KEYS = basis.DERIV_KEYS                     # all orders <= 3
Q_KEYS = [(0, 0), (1, 0), (0, 1)]
INT_KEYS_PHI = [(0, 0), (1, 0), (2, 0), (3, 0)]
INT_KEYS_Q = [(0, 0), (1, 0), (2, 0)]


@dataclass
class Config:
    cl: float = 0.6
    free_cl: bool = False
    R1: float = 2.0                 # ball radius
    D: int = 24                     # ball Cartesian degree
    ball_radial: str = "cheb"       # "cheb" (shift-1 states) or "jacobi" (3D Zernike radial polynomials; well conditioned)
    nmax: int = 12                  # Legendre degree in mu (all elements)
    shells: List[Tuple[float, int]] = field(default_factory=lambda: [(8.0, 16)])  # (outer radius, K) per shell
    emax: float = 5.0               # exterior exponent cutoff
    merge_tol: float = 0.03
    nR_ball: int = 0                # 0 -> auto (~1.3*D/2+4)
    nR_shell: int = 0               # 0 -> auto (~1.3*K+4)
    nR_ext: int = 0                 # 0 -> auto (2*n_exponents + 6; the six-decade node range needs >= 2 nodes per exponent)
    nmu: int = 0                    # 0 -> auto (nmax + 6)
    w_int: float = 10.0
    w_gauge: float = 10.0
    w_q: float = 1.0
    w_eta: float = 1.0
    scale_power_shift: float = 0.0  # extra power shift s on both PDE scales (see scale_divisor)
    scale_divisor: float = 4.0      # rows ~ (1+R^2)^((2 alpha + k + s)/divisor): 4 = shift-1 choice (cost weights R^(2 alpha + k + s) R_E^2);
                                    # 2 = SPEC/PROMPT section 9 (rows ~ R^(2 alpha + k) R_E, lead note 16)
    reg_exempt_correction: bool = False   # exempt the forced first-correction exponents (2 alpha + 1 for phi, 2 alpha + 2 for q) from the Tikhonov rows
    slave_correction: bool = False  # rows w_slave (c_corr - S(c_lead)): exterior coefficients at exponents 2 alpha + 1 (phi) and 2 alpha + 2 (q)
                                    # slaved to the leading tail by the far-field algebra (axi.farfield.SlaveMap; lead note 16 item 2)
    w_slave: float = 1000.0
    scale_shell_normalize: bool = False   # divide the row scale by its value at the node's dyadic-shell centre: every shell then weights the SPEC
                                          # scaled residual R^(2 alpha + k) R_E with an O(1) factor (balanced shells, PROMPT section 9) instead of
                                          # letting the far shells dominate by R^(2 alpha + k) (lead note 16 test, FAILURE_ANALYSIS 11)
    gauge: str = "swirl"            # "swirl": int F_theta^2 dS = target ; "full": int |F|^2 dS = target
    gauge_target: float = 1.0       # working-gauge value of the gauge integral (SPEC 5 allows a working gauge; reports convert)
    w_reg_ext: float = 1e-3         # Tikhonov weight on non-leading exterior coefficients (0 disables)
    Tmax_ext: float = 9.210340371976184    # ln(1e4): exterior nodes reach Rm * e^Tmax
    seed: int = 0
    cl_bounds: Tuple[float, float] = (0.501, 0.749)
    s1_constraint: bool = False     # hard S1 rows with free z0
    w_s1: float = 30.0
    z0_init: float = 0.0
    z0_fixed: bool = False          # with s1_constraint: hold the source at z0 = z0_init (no z0 unknown); reflection-class runs use z0 = 0
    q0_pin: Optional[float] = None  # if set (with s1_constraint): third row w_s1 (q(0, z0) - q0_pin); use with free_cl (lead note 2)
    amp_param: bool = False         # q = A qhat with A = exp(x[ix_a]) an unknown and qhat(0, z0) = 1 pinned (q0_pin forced to 1);
                                    # the eta rows are divided by A^2 (referee suggestion: removes the trivial swirl-shrinking descent)
    parity_phi: Optional[str] = None   # None, "odd" or "even" in z: restricts the Legendre degrees n (separate experiment, SPEC 2)
    parity_q: Optional[str] = None
    point_rows: List[dict] = field(default_factory=list)
                                    # generic linear hard rows: {field: phi|q|eta, der: val|r|z|rr|rz|zz|s|sz, r, z, target or target_expr (in c, K), weight}
    K_param: float = 1.0            # constant K available to target_expr (T2 ring amplitude q_z(1, 0) = K)
    axis_rows_q: int = 0            # if > 0: rows w_axis_q * q(0, z_j) = 0 at that many axis points per side (q = s x smooth, T2/S3 portraits)
    w_axis_q: float = 100.0
    axis_rows_zmax_factor: float = 100.0   # axis points reach Rm times this factor
    note: str = ""

    def to_json(self):
        return json.dumps(asdict(self), indent=1)

    @staticmethod
    def from_json(s):
        d = json.loads(s) if isinstance(s, str) else dict(s)
        d["shells"] = [tuple(x) for x in d.get("shells", [])]
        d["cl_bounds"] = tuple(d.get("cl_bounds", (0.501, 0.749)))
        return Config(**d)


def alpha_of(cl):
    return (1.0 - cl) / cl


def exponent_pairs(alpha, emax, kind, merge_tol):
    """Exponents as (m, k) with e = m*alpha + k (integers), so that d e / d alpha = m is known exactly."""
    vals = basis.exterior_exponents(alpha, emax, kind, merge_tol)
    pairs = []
    for e in vals:
        best = None
        for m in range(0, 12):
            k = e - m * alpha
            if abs(k - round(k)) < 1e-9:
                best = (m, int(round(k)))
                break
        if best is None:
            raise RuntimeError(f"exponent {e} not of form m*alpha+k")
        pairs.append(best)
    return pairs


class Problem:
    def __init__(self, cfg: Config, device="cpu"):
        self.cfg = cfg
        self.device = torch.device(device)
        self.build(cfg.cl)

    @staticmethod
    def from_state(d, device="cpu"):
        """Rebuild the Problem of a saved state dict (final.pt / checkpoint.pt): restores gauge_target and row_scale and, for free-c_l
        states, sets c_l (hence the exterior exponents) from the saved coefficient vector.  Every loader must use this: before
        2026-10-28T23:58Z the scripts rebuilt the Problem at the START value of c_l, so re-evaluations of free-c_l states used slightly
        wrong exterior exponents (the in-job validation, done on the live Problem, was correct).  Returns (prob, x)."""
        cfg = Config.from_json(d["cfg"])
        prob = Problem(cfg, device=device)
        if "gauge_target" in d:
            prob.cfg.gauge_target = float(d["gauge_target"])
        if "row_scale" in d:
            prob.cfg.w_q, prob.cfg.w_eta = [float(v) for v in d["row_scale"]]
        x = d["x"].detach().clone().to(device)
        if cfg.free_cl:
            prob.set_cl(float(x[prob.ix_cl]))
        return prob, x

    # ------------------------------------------------------------------ construction
    def build(self, cl):
        cfg = self.cfg
        self.cl = float(cl)
        alpha = alpha_of(cl)
        self.alpha = alpha
        nmu = cfg.nmu or (cfg.nmax + 6)
        self.nmu = nmu
        self.ext_pairs_phi = exponent_pairs(alpha, cfg.emax, "phi", cfg.merge_tol)
        self.ext_pairs_q = exponent_pairs(alpha, cfg.emax, "q", cfg.merge_tol)
        pairs = sorted(set(self.ext_pairs_phi) | set(self.ext_pairs_q), key=lambda p: p[0] * alpha + p[1])
        self.ext_pairs = pairs                   # union, used to build one node/basis set; columns are masked per field
        exps = [m * alpha + k for (m, k) in pairs]
        els = []
        nRb = cfg.nR_ball or int(1.3 * (cfg.D // 2) + 4)
        els.append(basis.make_element("ball", 0.0, cfg.R1, cfg.nmax, {"D": cfg.D, "radial": cfg.ball_radial}, nR=nRb, nmu=nmu))
        Rlo = cfg.R1
        for (Rhi, K) in cfg.shells:
            nRs = cfg.nR_shell or int(1.3 * K + 4)
            els.append(basis.make_element("shell", Rlo, Rhi, cfg.nmax, {"K": K, "map": "log"}, nR=nRs, nmu=nmu))
            Rlo = Rhi
        self.Rm = Rlo
        nRe = cfg.nR_ext or (2 * len(exps) + 6)
        els.append(basis.make_element("exterior", Rlo, math.inf, cfg.nmax, {"exponents": exps, "Tmax": cfg.Tmax_ext}, nR=nRe, nmu=nmu))
        self.elements = els
        self.nel = len(els)
        self._column_masks()
        self.nb_phi = [len(m) for m in self.cols_phi]
        self.nb_q = [len(m) for m in self.cols_q]
        self.off_phi = np.concatenate([[0], np.cumsum(self.nb_phi)]).astype(int)
        self.nphi = int(self.off_phi[-1])
        self.off_q = (np.concatenate([[0], np.cumsum(self.nb_q)]) + self.nphi).astype(int)
        self.nq = int(sum(self.nb_q))
        self.nfield = self.nphi + self.nq
        n = self.nfield
        self.ix_cl = None
        self.ix_z0 = None
        if cfg.free_cl:
            self.ix_cl = n; n += 1
        if cfg.s1_constraint and not cfg.z0_fixed:
            self.ix_z0 = n; n += 1
        self.ix_a = None
        if cfg.amp_param:
            assert cfg.s1_constraint, "amp_param needs the S1 rows (source position z0)"
            cfg.q0_pin = 1.0
            self.ix_a = n; n += 1
        self.nx = n
        dev = self.device
        self.Bphi, self.Bq, self.G = [], [], []
        for i, e in enumerate(els):
            self.Bphi.append({k: torch.tensor(v[:, self.cols_phi[i]], dtype=DT, device=dev) for k, v in e.B.items()})
            self.Bq.append({k: torch.tensor(v[:, self.cols_q[i]], dtype=DT, device=dev) for k, v in e.B.items() if k in Q_KEYS})
            R = torch.tensor(e.R, dtype=DT, device=dev)
            mu = torch.tensor(e.mu, dtype=DT, device=dev)
            self.G.append(ops.geom(R, mu))
        # node weights: balanced dyadic shells
        allR = np.concatenate([e.R for e in els])
        allw = np.concatenate([e.wR * e.wmu for e in els])
        shell_id = np.floor(np.log2(np.maximum(allR / cfg.R1, 1e-300))).astype(int)
        shell_id = np.clip(shell_id, -6, None)
        ids = np.unique(shell_id)
        wnode = np.zeros_like(allw)
        for sid in ids:
            m = shell_id == sid
            wnode[m] = allw[m] / allw[m].sum() / len(ids)
        self.n_nodes_per_el = [len(e.R) for e in els]
        offs = np.concatenate([[0], np.cumsum(self.n_nodes_per_el)])
        self.wnode = [torch.tensor(np.sqrt(wnode[offs[i]:offs[i + 1]]), dtype=DT, device=dev) for i in range(self.nel)]
        self.n_shells = len(ids)
        # dyadic-shell centre radius per node (for scale_shell_normalize): R_c = R1 2^(sid + 1/2); inner shells (R < R1) use R_c = R1/2^(1/2) at most R1
        Rc = cfg.R1 * 2.0 ** (shell_id + 0.5)
        Rc = np.where(allR < cfg.R1, np.minimum(Rc, cfg.R1), Rc)
        self.Rc_node = [torch.tensor(Rc[offs[i]:offs[i + 1]], dtype=DT, device=dev) for i in range(self.nel)]
        self._build_interfaces()
        self._build_reg()
        self._build_point_rows()
        # gauge quadrature
        mu_g, w_g = basis.gauss_legendre(2 * cfg.nmax + 4)
        self.mu_gauge = torch.tensor(mu_g, dtype=DT, device=dev)
        self.w_gauge_quad = torch.tensor(w_g, dtype=DT, device=dev)
        Pg = basis.legendre_derivs(mu_g, cfg.nmax, 1)
        self.P_gauge = torch.tensor(Pg[0], dtype=DT, device=dev)
        self.dP_gauge = torch.tensor(Pg[1], dtype=DT, device=dev)
        self._setup_slave()
        self.n_pde_rows = 2 * sum(self.n_nodes_per_el)
        self.n_int_rows = self.Jint.shape[0]
        self.n_reg_rows = self.Jreg.shape[0] + self.Jpt.shape[0]        # point rows are appended to the linear block
        self.n_s1_rows = (3 if cfg.q0_pin is not None else 2) if cfg.s1_constraint else 0
        self.n_slave_rows = (len(self.slave_corr_phi) + len(self.slave_corr_q)) if cfg.slave_correction else 0
        self.n_rows = self.n_pde_rows + self.n_int_rows + self.n_reg_rows + 1 + self.n_s1_rows + self.n_slave_rows

    def _column_masks(self):
        """Column index arrays per element for phi and q; leading exterior indices within the masked sets."""
        alpha = self.alpha
        self.cols_phi, self.cols_q = [], []
        def par_ok(n, par):
            return par is None or (par == "odd" and n % 2 == 1) or (par == "even" and n % 2 == 0)
        pphi, pq = self.cfg.parity_phi, self.cfg.parity_q
        self.n_allowed_phi = [n for n in range(self.cfg.nmax + 1) if par_ok(n, pphi)]
        self.n_allowed_q = [n for n in range(self.cfg.nmax + 1) if par_ok(n, pq)]
        for i, e in enumerate(self.elements):
            if e.kind != "exterior":
                self.cols_phi.append(np.array([j for j, lab in enumerate(e.labels) if par_ok(lab[0], pphi)]))
                self.cols_q.append(np.array([j for j, lab in enumerate(e.labels) if par_ok(lab[0], pq)]))
            else:
                exps_phi = [m * alpha + k for (m, k) in self.ext_pairs_phi]
                exps_q = [m * alpha + k for (m, k) in self.ext_pairs_q]
                cphi = [j for j, (n, ex) in enumerate(e.labels) if any(abs(ex - v) < 1e-9 for v in exps_phi) and par_ok(n, pphi)]
                cq = [j for j, (n, ex) in enumerate(e.labels) if any(abs(ex - v) < 1e-9 for v in exps_q) and par_ok(n, pq)]
                self.cols_phi.append(np.array(cphi))
                self.cols_q.append(np.array(cq))
                self.ext_labels_phi = [e.labels[j] for j in cphi]
                self.ext_labels_q = [e.labels[j] for j in cq]
                self.ext_lead_idx_phi = [t for t, (n, ex) in enumerate(self.ext_labels_phi) if abs(ex - alpha) < 1e-9]
                self.ext_lead_n_phi = [n for (n, ex) in self.ext_labels_phi if abs(ex - alpha) < 1e-9]
                self.ext_lead_idx_q = [t for t, (n, ex) in enumerate(self.ext_labels_q) if abs(ex - (alpha + 1)) < 1e-9]
                self.ext_lead_n_q = [n for (n, ex) in self.ext_labels_q if abs(ex - (alpha + 1)) < 1e-9]
                assert len(self.ext_lead_idx_phi) == len(self.n_allowed_phi) and len(self.ext_lead_idx_q) == len(self.n_allowed_q)

    def _build_interfaces(self):
        cfg = self.cfg
        mu_i, _ = basis.gauss_legendre(self.nmu)
        rows = []
        if not hasattr(self, "_int_cache"):
            self._int_cache = {}
        for i in range(self.nel - 1):
            A, Bel = self.elements[i], self.elements[i + 1]
            Rint = A.Rhi
            Rv = np.full_like(mu_i, Rint)
            # ball/shell interface evaluations do not depend on c_l: cache them (free-c_l mode rebuilds interfaces often)
            if (i, "A") not in self._int_cache:
                self._int_cache[(i, "A")] = A.eval_at(Rv, mu_i)
            BA = self._int_cache[(i, "A")]
            if Bel.kind == "exterior":
                BB = Bel.eval_at(Rv, mu_i)
            else:
                if (i, "B") not in self._int_cache:
                    self._int_cache[(i, "B")] = Bel.eval_at(Rv, mu_i)
                BB = self._int_cache[(i, "B")]
            for (fld, keys) in (("phi", INT_KEYS_PHI), ("q", INT_KEYS_Q)):
                for k in keys:
                    sc = Rint ** k[0]
                    blk = np.zeros((len(mu_i), self.nx))
                    if fld == "phi":
                        oa, ob, ca, cb = self.off_phi[i], self.off_phi[i + 1], self.cols_phi[i], self.cols_phi[i + 1]
                    else:
                        oa, ob, ca, cb = self.off_q[i], self.off_q[i + 1], self.cols_q[i], self.cols_q[i + 1]
                    blk[:, oa:oa + len(ca)] = cfg.w_int * sc * BA[k][:, ca]
                    blk[:, ob:ob + len(cb)] = -cfg.w_int * sc * BB[k][:, cb]
                    rows.append(blk)
        self.Jint = torch.tensor(np.concatenate(rows, 0), dtype=DT, device=self.device)

    def _build_reg(self):
        cfg = self.cfg
        i = self.nel - 1
        cols = []
        if cfg.w_reg_ext > 0:
            ex_phi = [self.alpha] + ([2 * self.alpha + 1] if cfg.reg_exempt_correction else [])
            ex_q = [self.alpha + 1] + ([2 * self.alpha + 2] if cfg.reg_exempt_correction else [])
            for t, (n, e) in enumerate(self.ext_labels_phi):
                if all(abs(e - v) > 1e-9 for v in ex_phi):
                    cols.append(self.off_phi[i] + t)
            for t, (n, e) in enumerate(self.ext_labels_q):
                if all(abs(e - v) > 1e-9 for v in ex_q):
                    cols.append(self.off_q[i] + t)
        Jr = np.zeros((len(cols), self.nx))
        for k, c in enumerate(cols):
            Jr[k, c] = cfg.w_reg_ext
        self.Jreg = torch.tensor(Jr, dtype=DT, device=self.device)

    def _setup_slave(self):
        """Exterior columns of the first-correction exponents (2 alpha + 1 for phi, 2 alpha + 2 for q), matched by Legendre degree to
        the leading columns, and the differentiable slave map."""
        cfg = self.cfg
        self.slave_corr_phi = []; self.slave_corr_q = []; self.slave = None
        if not cfg.slave_correction:
            return
        from . import farfield
        alpha = self.alpha; i = self.nel - 1
        lead_phi = {n: t for t, (n, e) in enumerate(self.ext_labels_phi) if abs(e - alpha) < 1e-9}
        corr_phi = {n: t for t, (n, e) in enumerate(self.ext_labels_phi) if abs(e - (2 * alpha + 1)) < 1e-9}
        lead_q = {n: t for t, (n, e) in enumerate(self.ext_labels_q) if abs(e - (alpha + 1)) < 1e-9}
        corr_q = {n: t for t, (n, e) in enumerate(self.ext_labels_q) if abs(e - (2 * alpha + 2)) < 1e-9}
        assert corr_phi and corr_q, "slave_correction needs the exponents 2 alpha + 1 and 2 alpha + 2 in the exterior set (emax >= 2 alpha + 2)"
        self.slave_n_phi = sorted(n for n in lead_phi if n in corr_phi); self.slave_n_q = sorted(n for n in lead_q if n in corr_q)
        self.slave_lead_phi = [self.off_phi[i] + lead_phi[n] for n in self.slave_n_phi]; self.slave_corr_phi = [self.off_phi[i] + corr_phi[n] for n in self.slave_n_phi]
        self.slave_lead_q = [self.off_q[i] + lead_q[n] for n in self.slave_n_q]; self.slave_corr_q = [self.off_q[i] + corr_q[n] for n in self.slave_n_q]
        self.slave = farfield.SlaveMap(self.slave_n_phi, self.slave_n_q, cfg.nmax, alpha, device=str(self.device))

    def slave_targets(self, x):
        """Target values of the correction coefficients from the leading ones (torch, differentiable in x)."""
        Rm = self.Rm; alpha = self.alpha
        a = x[self.slave_lead_phi] * Rm ** alpha
        b = x[self.slave_lead_q] * Rm ** (alpha + 1)
        a1, b1 = self.slave(a, b)
        return a1 * Rm ** (-(2 * alpha + 1)), b1 * Rm ** (-(2 * alpha + 2))

    def slave_rows(self, x):
        ta, tb = self.slave_targets(x)
        return self.cfg.w_slave * torch.cat([x[self.slave_corr_phi] - ta, x[self.slave_corr_q] - tb])

    def _functional_rows(self, fld, der, r, z, cl):
        """Row vector (nx,) of the linear functional 'der of field at (r, z)' on the coefficient vector (c_l-dependent for eta only
        through nothing: eta = -Delta_5 phi is c_l independent; the exterior basis depends on c_l and is rebuilt by set_cl)."""
        R = math.hypot(r, z)
        at_origin = R < 1e-14
        if at_origin:
            # exact origin: evaluate the basis at R = 0 along the axis direction mu = +1 (power_derivs handles R = 0 exactly);
            # only value, d_z and d_zz (= f_RR at mu = 1) are supported there; d_r and d_rz vanish identically for fields smooth in (r^2, z)
            R = 0.0; mu = 1.0
            if der not in ("val", "z", "zz"):
                if der in ("r", "rz"):
                    return np.zeros(self.nx)
                raise ValueError(f"derivative {der} at the exact origin is not supported")
        else:
            mu = max(-1.0, min(1.0, z / R))
        s_ = math.sqrt(max(0.0, 1 - mu * mu))
        i = self.element_index(R)
        e = self.elements[i]
        B = e.eval_at(np.array([R]), np.array([mu]))
        cols = self.cols_phi[i] if fld in ("phi", "eta") else self.cols_q[i]
        off = self.off_phi[i] if fld in ("phi", "eta") else self.off_q[i]
        f = {k: torch.tensor(B[k][0, cols]) for k in B}
        if at_origin:
            # axis forms at mu = +1 with s = 0 (no division by R): f_z = f_R, f_zz = f_RR
            v = {"val": f[(0, 0)], "z": f[(1, 0)], "zz": f[(2, 0)]}[der]
            row = np.zeros(self.nx); row[off:off + len(cols)] = v.numpy()
            return row
        g = ops.geom(torch.tensor([R]), torch.tensor([mu]))
        if fld == "eta":
            if der not in ("val", "r", "z", "s"):
                raise ValueError("second derivatives of eta need fourth derivatives of phi; not available")
            et = ops.eta_and_grad(f, g)
            f = {(0, 0): et[(0, 0)], (1, 0): et[(1, 0)], (0, 1): et[(0, 1)]}
        if der == "val":
            v = f[(0, 0)]
        elif der in ("r", "z", "s"):
            fr, fz = ops.grad_rz(f, g)
            if der == "r":
                v = fr
            elif der == "z":
                v = fz
            else:
                assert r > 0, "d/ds at r = 0 equals f_rr/2 there (regular limit); request der='rr' and halve the target"
                v = fr / (2 * r)
        elif der in ("rr", "rz", "zz", "sz"):
            frr, frz, fzz = ops.hess_rz(f, g)
            if der == "sz":
                assert r > 0
                v = frz / (2 * r)
            else:
                v = {"rr": frr, "rz": frz, "zz": fzz}[der]
        else:
            raise ValueError(der)
        row = np.zeros(self.nx)
        row[off:off + len(cols)] = v.numpy()
        return row

    def _point_targets(self):
        cl = self.cl; K = self.cfg.K_param
        t = []
        for pr in self.cfg.point_rows:
            if "target_expr" in pr:
                t.append(float(eval(pr["target_expr"], {"__builtins__": {}}, {"c": cl, "K": K, "math": math})))
            else:
                t.append(float(pr.get("target", 0.0)))
        return np.array(t)

    def _build_point_rows(self):
        """Jpt x - bpt: generic point rows (weighted) and the q axis rows."""
        cfg = self.cfg
        rows, b = [], []
        for pr in cfg.point_rows:
            w = float(pr.get("weight", 100.0))
            rows.append(w * self._functional_rows(pr["field"], pr["der"], float(pr["r"]), float(pr["z"]), self.cl))
            b.append(w)
        self._point_weights = np.array(b)
        if cfg.axis_rows_q > 0:
            zs = np.geomspace(1e-3 * cfg.R1, cfg.axis_rows_zmax_factor * self.Rm, cfg.axis_rows_q)
            for zz in np.concatenate([zs, -zs]):
                rows.append(cfg.w_axis_q * self._functional_rows("q", "val", 0.0, float(zz), self.cl))
        if rows:
            self.Jpt = torch.tensor(np.array(rows), dtype=DT, device=self.device)
        else:
            self.Jpt = torch.zeros((0, self.nx), dtype=DT, device=self.device)
        bt = np.zeros(self.Jpt.shape[0])
        if len(cfg.point_rows):
            bt[:len(cfg.point_rows)] = self._point_weights * self._point_targets()
        self.bpt = torch.tensor(bt, dtype=DT, device=self.device)

    # ------------------------------------------------------------------ helpers
    def split(self, x):
        cphi = [x[self.off_phi[i]:self.off_phi[i + 1]] for i in range(self.nel)]
        cq = [x[self.off_q[i]:self.off_q[i + 1]] for i in range(self.nel)]
        cl = x[self.ix_cl] if self.ix_cl is not None else None
        return cphi, cq, cl

    def z0_of(self, x):
        if self.ix_z0 is not None:
            return float(x[self.ix_z0])
        return float(self.cfg.z0_init) if self.cfg.s1_constraint else None

    def cl_of(self, x):
        return float(x[self.ix_cl]) if self.ix_cl is not None else self.cl

    def amp_of(self, x):
        """Swirl amplitude A (1 when amp_param is off)."""
        return float(torch.exp(x[self.ix_a])) if self.ix_a is not None else 1.0

    def to_physical(self, x):
        """(x_phys, cfg_phys): the state with q = A qhat and no amplitude unknown, for diagnostics and export."""
        from dataclasses import replace
        if self.ix_a is None:
            return x.detach().clone(), self.cfg
        A = torch.exp(x[self.ix_a])
        xp = x.detach().clone()
        xp[self.nphi:self.nphi + self.nq] = xp[self.nphi:self.nphi + self.nq] * A
        xp = torch.cat([xp[:self.ix_a], xp[self.ix_a + 1:]])
        cfg_p = replace(self.cfg, amp_param=False, q0_pin=None)
        return xp, cfg_p

    def _eta_rows(self, Reta, q, qz, x):
        """Eta equation rows; with amp_param: ((1+c) eta + W . grad eta)/A^2 - 2 qhat qhat_z."""
        if self.ix_a is None:
            return Reta
        inv_A2 = torch.exp(-2.0 * x[self.ix_a])
        lin = Reta + 2.0 * q * qz
        return lin * inv_A2 - 2.0 * q * qz

    def set_cl(self, cl):
        """Rebuild the exterior basis for a new c_l (free-c_l mode); other elements are unchanged.
        The exponent pattern (m, k) is frozen at construction, so the unknown layout does not change."""
        if abs(float(cl) - self.cl) < 1e-15:
            return
        alpha = alpha_of(float(cl))
        self.cl = float(cl)
        self.alpha = alpha
        exps = [m * alpha + k for (m, k) in self.ext_pairs]
        ext = self.elements[-1]
        ext.params = dict(ext.params, exponents=exps)
        Bn, labels = basis.build_B("exterior", ext.Rlo, ext.Rhi, ext.nmax, ext.params, ext.R, ext.mu)
        ext.B = Bn
        ext.labels = labels
        i = self.nel - 1
        self.ext_labels_phi = [labels[j] for j in self.cols_phi[i]]
        self.ext_labels_q = [labels[j] for j in self.cols_q[i]]
        self.Bphi[i] = {k: torch.tensor(v[:, self.cols_phi[i]], dtype=DT, device=self.device) for k, v in Bn.items()}
        self.Bq[i] = {k: torch.tensor(v[:, self.cols_q[i]], dtype=DT, device=self.device) for k, v in Bn.items() if k in Q_KEYS}
        self._build_interfaces()
        if len(self.cfg.point_rows) or self.cfg.axis_rows_q > 0:
            self._build_point_rows()
        if self.cfg.slave_correction:
            self._setup_slave()

    def scales(self, g, alpha, i=None):
        sh = self.cfg.scale_power_shift
        dv = self.cfg.scale_divisor
        one = 1.0 + g["R"] ** 2
        eq_ = (2 * alpha + 2 + sh) / dv; ee_ = (2 * alpha + 3 + sh) / dv
        sq = self.cfg.w_q * one ** eq_
        se = self.cfg.w_eta * one ** ee_
        if self.cfg.scale_shell_normalize and i is not None:
            onec = 1.0 + self.Rc_node[i] ** 2
            sq = sq / onec ** eq_
            se = se / onec ** ee_
        return sq, se

    def element_index(self, R):
        """Index of the element containing radius R (ball for R <= R1)."""
        for i, e in enumerate(self.elements):
            if R <= e.Rhi:
                return i
        return self.nel - 1

    # ------------------------------------------------------------------ S1 rows
    def axis_phi_rows(self, z0, with_q=False):
        """Row vectors (numpy, length nx) r0, r1, r2 with phi(0,z0) = r0.x, phi_R(0,z0) = r1.x, phi_RR(0,z0) = r2.x,
        and the axis sign mu (= +1 for z0 >= 0, -1 otherwise).  With with_q also q(0,z0) = s0.x, q_R(0,z0) = s1.x."""
        mu = 1.0 if z0 >= 0 else -1.0
        R = abs(float(z0))
        i = self.element_index(R)
        e = self.elements[i]
        B = e.eval_at(np.array([R]), np.array([mu]))
        rows = []
        for k in ((0, 0), (1, 0), (2, 0)):
            v = np.zeros(self.nx)
            v[self.off_phi[i]:self.off_phi[i + 1]] = B[k][0, self.cols_phi[i]]
            rows.append(v)
        if with_q:
            for k in ((0, 0), (1, 0)):
                v = np.zeros(self.nx)
                v[self.off_q[i]:self.off_q[i + 1]] = B[k][0, self.cols_q[i]]
                rows.append(v)
            return rows[0], rows[1], rows[2], mu, rows[3], rows[4]
        return rows[0], rows[1], rows[2], mu

    def s1_residual_and_jac(self, x):
        """S1 rows: w_s1 [phi_z(0,z0) - 1/2], w_s1 [c z0 + 2 phi(0,z0)]; returns (res (2,), jac (2, nx)) as numpy."""
        cfg = self.cfg
        xs = x.detach().cpu().numpy()
        z0 = float(xs[self.ix_z0]) if self.ix_z0 is not None else float(cfg.z0_init)
        cl = self.cl_of(x)
        r0, r1, r2, mu = self.axis_phi_rows(z0)
        phi0 = float(r0 @ xs); phiR = float(r1 @ xs); phiRR = float(r2 @ xs)
        phi_z = mu * phiR                       # on the axis f_z = mu f_R
        phi_zz = phiRR                          # on the axis f_zz = f_RR
        nrow = self.n_s1_rows
        res = np.zeros(nrow); jac = np.zeros((nrow, self.nx))
        res[0] = cfg.w_s1 * (phi_z - 0.5); res[1] = cfg.w_s1 * (cl * z0 + 2 * phi0)
        jac[0, :] = cfg.w_s1 * mu * r1
        jac[1, :] = cfg.w_s1 * 2 * r0
        if self.ix_z0 is not None:
            jac[0, self.ix_z0] = cfg.w_s1 * phi_zz
            jac[1, self.ix_z0] = cfg.w_s1 * (cl + 2 * phi_z)
        if self.ix_cl is not None:
            jac[1, self.ix_cl] = cfg.w_s1 * z0
        if cfg.q0_pin is not None:
            _, _, _, _, s0, s1 = self.axis_phi_rows(z0, with_q=True)
            qv = float(s0 @ xs); qR = float(s1 @ xs)
            res[2] = cfg.w_s1 * (qv - cfg.q0_pin)
            jac[2, :] = cfg.w_s1 * s0
            if self.ix_z0 is not None:
                jac[2, self.ix_z0] = cfg.w_s1 * mu * qR      # d/dz0 q(0, z0) = q_z = mu q_R on the axis
        return res, jac

    # ------------------------------------------------------------------ residual
    def fields_at(self, i, cphi_i, cq_i):
        phi = {k: self.Bphi[i][k] @ cphi_i for k in PHI_KEYS}
        q = {k: self.Bq[i][k] @ cq_i for k in Q_KEYS}
        return phi, q

    def _tail_profiles(self, cphi_ext, cq_ext, alpha):
        Rm = self.Rm
        a = cphi_ext[self.ext_lead_idx_phi] * Rm ** alpha          # A(mu) = sum a_n P_n over the allowed degrees n
        b = cq_ext[self.ext_lead_idx_q] * Rm ** (alpha + 1)         # B(mu)
        mu = self.mu_gauge
        A = self.P_gauge[:, self.ext_lead_n_phi] @ a
        dA = self.dP_gauge[:, self.ext_lead_n_phi] @ a
        Bq = self.P_gauge[:, self.ext_lead_n_q] @ b
        s2 = 1 - mu * mu
        FR = 2 * mu * A - s2 * dA
        Fth2 = (alpha - 2) ** 2 * s2 * A * A
        Ftheta2 = s2 * Bq * Bq
        return FR * FR + Fth2, Ftheta2

    def gauge_integral(self, cphi_ext, cq_ext, alpha):
        pol2, sw2 = self._tail_profiles(cphi_ext, cq_ext, alpha)
        if self.cfg.gauge == "swirl":
            return 2 * math.pi * torch.sum(self.w_gauge_quad * sw2)
        return 2 * math.pi * torch.sum(self.w_gauge_quad * (pol2 + sw2))

    def tail_integrals(self, cphi_ext, cq_ext, alpha):
        """(int |F|^2 dS, int F_theta^2 dS, int (F_R^2+F_vartheta^2) dS)."""
        pol2, sw2 = self._tail_profiles(cphi_ext, cq_ext, alpha)
        pol = 2 * math.pi * float(torch.sum(self.w_gauge_quad * pol2))
        sw = 2 * math.pi * float(torch.sum(self.w_gauge_quad * sw2))
        return pol + sw, sw, pol

    def residual(self, x, return_parts=False):
        if self.cfg.free_cl:
            self.set_cl(float(x[self.ix_cl]))
        cl = self.cl
        alpha = alpha_of(cl)
        cphi, cq, _ = self.split(x)
        rows = []
        parts = {}
        for i in range(self.nel):
            phi, q = self.fields_at(i, cphi[i], cq[i])
            Rq, Reta, aux = ops.reduced_residuals(phi, q, self.G[i], cl)
            Reta = self._eta_rows(Reta, q[(0, 0)], aux["qz"], x)
            sq, se = self.scales(self.G[i], alpha, i)
            rows.append(self.wnode[i] * sq * Rq)
            rows.append(self.wnode[i] * se * Reta)
            if return_parts:
                parts[i] = dict(Rq=Rq, Reta=Reta, q=q[(0, 0)], phi=phi[(0, 0)], **aux)
        rows.append(self.Jint @ x)
        rows.append(self.Jreg @ x)
        if self.Jpt.shape[0]:
            rows.append(self.Jpt @ x - self.bpt)
        Aq = torch.exp(x[self.ix_a]) if self.ix_a is not None else 1.0
        gI = self.gauge_integral(cphi[-1], cq[-1] * Aq, alpha)
        rows.append((self.cfg.w_gauge * (gI - self.cfg.gauge_target)).reshape(1))
        if self.cfg.s1_constraint:
            res_s1, jac_s1 = self.s1_residual_and_jac(x)
            # differentiable in the field coefficients and z0 through the linear row form r.x (jac rows at the
            # current z0; the nonlinearity in z0 enters only through the Jacobian, see jacobian()).
            Js1 = torch.tensor(jac_s1, dtype=DT, device=x.device)
            base = torch.tensor(res_s1, dtype=DT, device=x.device)
            rows.append(base + (Js1 @ (x - x.detach())))
        if self.cfg.slave_correction:
            rows.append(self.slave_rows(x))
        r = torch.cat(rows)
        if getattr(self, "r_offset", None) is not None:
            r = r - self.r_offset          # forced manufactured problem: r(x*) = 0 exactly for the chosen x* (tests only)
        if return_parts:
            return r, parts
        return r

    def cost_breakdown(self, x):
        """Sum of squares of the weighted residual per row block (cost = 0.5 * total)."""
        r = self.residual(x).detach()
        out = {}
        row = 0
        for i, n in enumerate(self.n_nodes_per_el):
            out[f"pde_q_el{i}"] = float(torch.sum(r[row:row + n] ** 2)); row += n
            out[f"pde_eta_el{i}"] = float(torch.sum(r[row:row + n] ** 2)); row += n
        out["interface"] = float(torch.sum(r[row:row + self.n_int_rows] ** 2)); row += self.n_int_rows
        out["reg_ext"] = float(torch.sum(r[row:row + self.Jreg.shape[0]] ** 2)); row += self.Jreg.shape[0]
        out["point_rows"] = float(torch.sum(r[row:row + self.Jpt.shape[0]] ** 2)); row += self.Jpt.shape[0]
        out["gauge"] = float(r[row] ** 2); row += 1
        if self.cfg.s1_constraint:
            out["s1"] = float(torch.sum(r[row:row + self.n_s1_rows] ** 2)); row += self.n_s1_rows
        if self.cfg.slave_correction:
            out["slave"] = float(torch.sum(r[row:row + self.n_slave_rows] ** 2)); row += self.n_slave_rows
        out["total"] = float(torch.sum(r ** 2))
        return out

    # ------------------------------------------------------------------ analytic Jacobian
    def jacobian(self, x):
        cfg = self.cfg
        if cfg.free_cl:
            self.set_cl(float(x[self.ix_cl]))
        cl = self.cl
        alpha = self.alpha
        cphi, cq, _ = self.split(x)
        J = torch.zeros((self.n_rows, self.nx), dtype=DT, device=self.device)
        row = 0
        for i in range(self.nel):
            Bp, Bq = self.Bphi[i], self.Bq[i]
            phi = {k: (Bp[k] @ cphi[i]).detach().requires_grad_(True) for k in PHI_KEYS}
            q = {k: (Bq[k] @ cq[i]).detach().requires_grad_(True) for k in Q_KEYS}
            Rq, Reta, aux_i = ops.reduced_residuals(phi, q, self.G[i], cl)
            if self.ix_a is not None:
                lin_i = (Reta + 2.0 * q[(0, 0)] * aux_i["qz"]).detach()
                Reta = self._eta_rows(Reta, q[(0, 0)], aux_i["qz"], x.detach())
            sq, se = self.scales(self.G[i], alpha, i)
            wq = self.wnode[i] * sq
            we = self.wnode[i] * se
            n = Rq.shape[0]
            leaves = [phi[k] for k in PHI_KEYS] + [q[k] for k in Q_KEYS]
            gq = torch.autograd.grad(Rq.sum(), leaves, retain_graph=True, allow_unused=True)
            ge = torch.autograd.grad(Reta.sum(), leaves, allow_unused=True)
            op, oq = self.off_phi[i], self.off_q[i]
            nbp, nbq = self.nb_phi[i], self.nb_q[i]
            Jq_phi = torch.zeros((n, nbp), dtype=DT, device=self.device)
            Je_phi = torch.zeros((n, nbp), dtype=DT, device=self.device)
            Jq_q = torch.zeros((n, nbq), dtype=DT, device=self.device)
            Je_q = torch.zeros((n, nbq), dtype=DT, device=self.device)
            for idx, k in enumerate(PHI_KEYS):
                if gq[idx] is not None:
                    Jq_phi += gq[idx][:, None] * Bp[k]
                if ge[idx] is not None:
                    Je_phi += ge[idx][:, None] * Bp[k]
            for jdx, k in enumerate(Q_KEYS):
                idx = len(PHI_KEYS) + jdx
                if gq[idx] is not None:
                    Jq_q += gq[idx][:, None] * Bq[k]
                if ge[idx] is not None:
                    Je_q += ge[idx][:, None] * Bq[k]
            J[row:row + n, op:op + nbp] = wq[:, None] * Jq_phi
            J[row:row + n, oq:oq + nbq] = wq[:, None] * Jq_q
            row += n
            J[row:row + n, op:op + nbp] = we[:, None] * Je_phi
            J[row:row + n, oq:oq + nbq] = we[:, None] * Je_q
            if self.ix_a is not None:
                J[row:row + n, self.ix_a] = we * (-2.0 * lin_i * torch.exp(-2.0 * x[self.ix_a]))
            row += n
        J[row:row + self.n_int_rows, :] = self.Jint
        row += self.n_int_rows
        J[row:row + self.Jreg.shape[0], :] = self.Jreg
        row += self.Jreg.shape[0]
        if self.Jpt.shape[0]:
            J[row:row + self.Jpt.shape[0], :] = self.Jpt
            row += self.Jpt.shape[0]
        xe = x.detach().clone().requires_grad_(True)
        cphi_e, cq_e, _ = self.split(xe)
        Aq_e = torch.exp(xe[self.ix_a]) if self.ix_a is not None else 1.0
        gI = self.gauge_integral(cphi_e[-1], cq_e[-1] * Aq_e, alpha)
        (gg,) = torch.autograd.grad(cfg.w_gauge * gI, xe)
        J[row, :] = gg
        row += 1
        if cfg.s1_constraint:
            _, jac_s1 = self.s1_residual_and_jac(x)
            J[row:row + self.n_s1_rows, :] = torch.tensor(jac_s1, dtype=DT, device=self.device)
            row += self.n_s1_rows
        if cfg.slave_correction:
            xs_ = x.detach().clone().requires_grad_(True)
            Js = torch.autograd.functional.jacobian(self.slave_rows, xs_)
            J[row:row + self.n_slave_rows, :] = Js
            row += self.n_slave_rows
        if cfg.free_cl:
            h = 1e-6
            ic = self.ix_cl
            xp = x.detach().clone(); xp[ic] += h
            xm = x.detach().clone(); xm[ic] -= h
            rp = self.residual(xp)
            rm = self.residual(xm)
            self.set_cl(float(x[ic]))
            col = (rp - rm) / (2 * h)
            if cfg.s1_constraint:
                k0 = self.n_rows - self.n_slave_rows - self.n_s1_rows
                col[k0:k0 + self.n_s1_rows] = J[k0:k0 + self.n_s1_rows, ic]      # S1 rows: analytic c_l derivative
            J[:, ic] = col
        return J

    # ------------------------------------------------------------------ initialization helpers
    def fit_function(self, fphi, fq, x0=None, skip_exterior=True, joint=True):
        """Least-squares fit of callables fphi(R, mu), fq(R, mu) onto the ball/shell bases (exterior untouched).
        joint=True (default since 2026-10-28T22:30Z): one least-squares problem per field over all inner elements INCLUDING the
        weighted interface-continuity rows, so that under-resolved seeds do not start with large interface jumps (independent
        per-element fits of a sharp seed gave interface costs of 1e13, FAILURE_ANALYSIS 13).  The exterior block is fitted
        afterwards by the caller (its columns are zero in the interface rows used here only if the exterior is skipped)."""
        x = torch.zeros(self.nx, dtype=DT) if x0 is None else x0.detach().cpu().clone()
        inner = [i for i, e in enumerate(self.elements) if not (e.kind == "exterior" and skip_exterior)]
        if not joint:
            for i in inner:
                e = self.elements[i]
                Ap = e.B[(0, 0)][:, self.cols_phi[i]]; Aq = e.B[(0, 0)][:, self.cols_q[i]]
                cph, *_ = np.linalg.lstsq(Ap, fphi(e.R, e.mu), rcond=None); cqq, *_ = np.linalg.lstsq(Aq, fq(e.R, e.mu), rcond=None)
                x[self.off_phi[i]:self.off_phi[i + 1]] = torch.tensor(cph); x[self.off_q[i]:self.off_q[i + 1]] = torch.tensor(cqq)
        else:
            Jint = self.Jint.detach().cpu().numpy()
            for fld, offs, colsets, f in (("phi", self.off_phi, self.cols_phi, fphi), ("q", self.off_q, self.cols_q, fq)):
                cols_all = np.concatenate([np.arange(offs[i], offs[i + 1]) for i in inner])
                blocks = []; rhs = []
                for i in inner:
                    e = self.elements[i]
                    row = np.zeros((len(e.R), len(cols_all)))
                    j0 = int(np.searchsorted(cols_all, offs[i]))
                    row[:, j0:j0 + len(colsets[i])] = e.B[(0, 0)][:, colsets[i]]
                    blocks.append(row); rhs.append(f(e.R, e.mu))
                # interface rows restricted to the inner columns of this field (rows that involve only these columns)
                Ji = Jint[:, cols_all]
                keep = np.abs(Ji).sum(axis=1) > 0
                if skip_exterior:   # drop rows that also touch exterior columns (the exterior is fitted later)
                    ext_cols = np.concatenate([np.arange(offs[i], offs[i + 1]) for i, e in enumerate(self.elements) if e.kind == "exterior"])
                    keep &= np.abs(Jint[:, ext_cols]).sum(axis=1) == 0
                A = np.concatenate(blocks + [Ji[keep]], 0); b = np.concatenate(rhs + [np.zeros(int(keep.sum()))])
                cs = np.max(np.abs(A), axis=0); cs[cs == 0] = 1.0
                c, *_ = np.linalg.lstsq(A / cs, b, rcond=None); c = c / cs
                x[torch.tensor(cols_all)] = torch.tensor(c)
        if self.ix_cl is not None:
            x[self.ix_cl] = self.cl
        if self.ix_z0 is not None:
            x[self.ix_z0] = self.cfg.z0_init
        if self.ix_a is not None:
            x[self.ix_a] = 0.0
        return x.to(self.device)

    def eval_field(self, x, which, R, mu, key=(0, 0)):
        """Evaluate phi or q (or an (R,mu)-derivative) at arbitrary points, using the element containing each point."""
        xs = x.detach().cpu()
        cphi, cq, _ = self.split(xs)
        R = np.asarray(R, float); mu = np.asarray(mu, float)
        out = np.zeros_like(R)
        for i, e in enumerate(self.elements):
            lo = e.Rlo if i > 0 else -1.0
            m = (R > lo) & (R <= e.Rhi) if i < self.nel - 1 else (R > lo)
            if not np.any(m):
                continue
            Bm = e.eval_at(R[m], mu[m])[key]
            if which == "phi":
                out[m] = Bm[:, self.cols_phi[i]] @ cphi[i].numpy()
            else:
                out[m] = Bm[:, self.cols_q[i]] @ cq[i].numpy()
        return out

    def eval_all(self, x, R, mu):
        """Dicts of (R,mu)-derivatives of phi (order<=3) and q (order<=1) at arbitrary points, as torch CPU tensors."""
        xs = x.detach().cpu()
        cphi, cq, _ = self.split(xs)
        R = np.asarray(R, float); mu = np.asarray(mu, float)
        phi = {k: np.zeros_like(R) for k in PHI_KEYS}
        q = {k: np.zeros_like(R) for k in Q_KEYS}
        for i, e in enumerate(self.elements):
            lo = e.Rlo if i > 0 else -1.0
            m = (R > lo) & (R <= e.Rhi) if i < self.nel - 1 else (R > lo)
            if not np.any(m):
                continue
            Bm = e.eval_at(R[m], mu[m])
            for k in PHI_KEYS:
                phi[k][m] = Bm[k][:, self.cols_phi[i]] @ cphi[i].numpy()
            for k in Q_KEYS:
                q[k][m] = Bm[k][:, self.cols_q[i]] @ cq[i].numpy()
        return ({k: torch.tensor(v) for k, v in phi.items()}, {k: torch.tensor(v) for k, v in q.items()})

    def eval_all_q2(self, x, R, mu):
        """q derivatives to second order (for interface and regularity diagnostics)."""
        xs = x.detach().cpu()
        cphi, cq, _ = self.split(xs)
        R = np.asarray(R, float); mu = np.asarray(mu, float)
        keys = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]
        q = {k: np.zeros_like(R) for k in keys}
        for i, e in enumerate(self.elements):
            lo = e.Rlo if i > 0 else -1.0
            m = (R > lo) & (R <= e.Rhi) if i < self.nel - 1 else (R > lo)
            if not np.any(m):
                continue
            Bm = e.eval_at(R[m], mu[m])
            for k in keys:
                q[k][m] = Bm[k][:, self.cols_q[i]] @ cq[i].numpy()
        return q

    def describe(self):
        ext = self.elements[-1]
        return dict(cl=self.cl, alpha=self.alpha, nx=self.nx, n_rows=self.n_rows, Rm=self.Rm, nmu=self.nmu,
                    gauge=self.cfg.gauge, gauge_target=self.cfg.gauge_target, s1_constraint=self.cfg.s1_constraint, q0_pin=self.cfg.q0_pin,
                    ix_cl=self.ix_cl, ix_z0=self.ix_z0, ix_a=self.ix_a, amp_param=self.cfg.amp_param, n_s1_rows=self.n_s1_rows,
                    interface_orders=dict(phi=[k[0] for k in INT_KEYS_PHI], q=[k[0] for k in INT_KEYS_Q]),
                    parity=dict(phi=self.cfg.parity_phi, q=self.cfg.parity_q), point_rows=self.cfg.point_rows, axis_rows_q=self.cfg.axis_rows_q, K_param=self.cfg.K_param,
                    elements=[dict(kind=e.kind, Rlo=e.Rlo, Rhi=(None if math.isinf(e.Rhi) else e.Rhi), nmax=e.nmax,
                                   params={k: (v if k != "exponents" else [float(t) for t in v]) for k, v in e.params.items()},
                                   n_nodes=len(e.R), nb_phi=int(self.nb_phi[i]), nb_q=int(self.nb_q[i]),
                                   labels_phi=[list(map(float, e.labels[j])) for j in self.cols_phi[i]],
                                   labels_q=[list(map(float, e.labels[j])) for j in self.cols_q[i]])
                              for i, e in enumerate(self.elements)],
                    ext_pairs_phi=[list(p) for p in self.ext_pairs_phi], ext_pairs_q=[list(p) for p in self.ext_pairs_q],
                    layout=dict(off_phi=[int(v) for v in self.off_phi], off_q=[int(v) for v in self.off_q], free_cl=self.cfg.free_cl))
