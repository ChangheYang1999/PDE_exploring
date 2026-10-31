#!/usr/bin/env python
"""STRATEGY-2 COPY of scripts/worker_d6.py (2026-10-29T18:5xZ; lead 18:31:20Z item 4 (i)): identical to worker_d6.py (sha256 cd35acf01f770dfb) except: the solver import (src/optimization/lm_s2.py), the local function s2_jac_post (complete_jacobian_from_Jcw of the assembled J_cw, the same function as the J_c EVAL records; optional save of the iteration-0 J_c for the smoke record) and the keyword jac_post passed to lm_solve_free when the configuration has step_jacobian "J_c"; the continuation rule (a) additionally ignores the keys step_jacobian, s2_smoke, s2_smoke_save_Jc_it0 (and battery when s2_smoke is set, smoke runs only); V420: unknown step_jacobian values are refused, the periodic linearization record carries kind J_c when the hook is on and is never corrected again, the trajectory carries t_jac_post and step_jacobian, the end record carries step_jacobian. With step_jacobian absent or "J_cw" the control flow and every number are those of worker_d6.py. Launched by hand (not by the supervisor); production files unchanged.
D6FP campaign worker (degree-6 free-parameter campaign, 2026-10-28): runs one job file on one GPU with heartbeats, atomic checkpoints
(every <= 14 min, after every accepted improvement block, at SIGTERM), resume from checkpoint, ledger records and the frozen Euler3
end-of-start diagnostics battery (copied verbatim from the frozen worker, function finish_start).
Optimizer: lm_solve_free (src/optimization/lm.py): frozen-weight Gauss-Newton model with EXACT AD parameter columns (pressure tables inside
the graph), self-consistent acceptance (objective_at), smooth parameter map c_l = 0.4 + 0.1 sigmoid(z_c), omega = exp(z_w) (SPEC 5.1),
trust region |dz_c|, |dz_w| <= 0.5 (SPEC 5.5), saturation stop (SPEC 5.3), complete gradient of O1 per accepted iteration (SPEC 7.1),
QR linearization records (lead note 2026-10-28T20:43Z).
Usage: worker_d6.py <job.json> <run_dir>   (CUDA_VISIBLE_DEVICES set by the supervisor to one physical GPU)."""
import sys, os, json, time, hashlib, math, signal, traceback, platform
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False; torch.backends.cudnn.allow_tf32 = False      # SPEC 1.4
from src.equations.fields import Model, alpha_of
from src.optimization.problem import Problem
from src.optimization.lm_s2 import lm_solve_free      # STRATEGY 2: the lm.py copy with the jac_post hook (src/optimization/lm_s2.py)
from src.optimization.param_map import ParamMap
from src.validation.spec_diagnostics import spec_diagnostics, tier_S
from src.validation.holdout import HoldoutGrid, half_offset_edges, sphere_diagnostics, exchange_radii, two_family_summary, summary_text, structure_text
from src.validation.critical_points import local_maxima_omega, zeros_of_W
from src.validation.strength import strength_diagnostics
from src.optimization.tail_constraints import TailConstraints
from src.far_field.eigen import min_pressure_eigenvalue
from src.optimization.seeds import make_seed
from src.optimization.transfer import embed_state, fit_field
from src.validation.diagnostics import candidate_diagnostics, summary_line
from src.campaign import ledger
from src.campaign.checkpoint import atomic_save, atomic_write_text
from src.pressure.poisson_sh import PressureSolver

LEDGER = os.path.join(ROOT, "status", "ledger.jsonl")
SOLVER_VERSION = "d6fp-v1-2026-10-28"      # frozen e3 v5 + D6FP: torch pressure tables, AD parameter columns, self-consistent acceptance, parameter map
CKPT_INTERVAL = 14 * 60
T0_EPOCH = time.mktime(time.strptime("2026-10-28T20:30:31Z", "%Y-%m-%dT%H:%M:%SZ")) - time.timezone
TEAM_STOP_EPOCH = T0_EPOCH + 47.0 * 3600.0           # 2026-10-30T19:30:31Z
STOP = {"flag": False}


def _sigterm(signum, frame):
    STOP["flag"] = True


signal.signal(signal.SIGTERM, _sigterm)
signal.signal(signal.SIGINT, _sigterm)


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


class Heartbeat:
    def __init__(self, path, job_id):
        self.path, self.job_id, self.t = path, job_id, 0.0

    def beat(self, **info):
        t = time.time()
        if t - self.t < 20 and not info.get("force"):
            return
        self.t = t
        rec = dict(job_id=self.job_id, ts=now(), epoch=t, pid=os.getpid(), host=platform.node())
        rec.update({k: v for k, v in info.items() if k != "force"})
        atomic_write_text(json.dumps(rec), self.path)


def build(cfg, device):
    model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0),
                  Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"], free_params=cfg.get("free_params", False), device=device,
                  channels=cfg.get("channels"), extra_r=(cfg.get("far_radii") if cfg.get("far_merged", True) else None))
    prob = Problem(model, formulation=cfg.get("formulation", "mom"), gauge_weight=cfg.get("gauge_weight", 100.0),
                   both_weight=cfg.get("both_weight", 1.0), nl_weighting=bool(cfg.get("nl_weighting", True)),
                   gauge=cfg.get("gauge", "F"), sigmaZ=cfg.get("sigmaZ"), sigmaZ_weight=cfg.get("sigmaZ_weight", 100.0),
                   far_radii=cfg.get("far_radii"), far_weight=cfg.get("far_weight", 1.0),
                   sigmaZ_fine=int(cfg.get("sigmaZ_fine", 4)), sigmaZ_ramp_iters=int(cfg.get("sigmaZ_ramp_iters", 0)),
                   nl_denominator=cfg.get("nl_denominator", "all5far"), far_lambda=float(cfg.get("far_lambda", 1e-2)),
                   closure_lambda=float(cfg.get("closure_lambda", 0.0)), stable_linear=bool(cfg.get("stable_linear", True)), exterior_monopole=bool(cfg.get("exterior_monopole", False)))
    from src.optimization.problem import apply_precision_mode
    apply_precision_mode(prob, cfg.get("precision_mode"))                    # D6FP D1: cfg override of the module default
    return model, prob


def code_versions():
    out = {}
    for rel in ("scripts/worker_d6.py", "src/optimization/lm.py", "src/optimization/problem.py", "src/optimization/param_map.py", "src/equations/fields.py",
                "src/pressure/poisson_sh.py", "src/equations/residuals.py", "src/far_field/correction.py", "src/optimization/tail_constraints.py",
                "src/bases/radial.py", "src/bases/jets.py", "src/bases/solid_harmonics.py", "src/validation/spec_diagnostics.py", "src/pressure/ray_integral.py"):
        fp = os.path.join(ROOT, rel)
        try:
            h = hashlib.sha256(open(fp, "rb").read()).hexdigest()[:12]
            out[rel] = dict(sha256_12=h, mtime=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(os.path.getmtime(fp))))
        except Exception as e:
            out[rel] = dict(error=repr(e))
    return out


def sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def phase_generator(model, z_full):
    """d/dgamma of the azimuthal rotation of the state at gamma = 0 (SPEC 7.3: the exact phase-rotation generator):
    cos-mode a_c -> m a_s, sin-mode a_s -> -m a_c for every (l, m > 0) pair of every channel; parameters unchanged."""
    d = model.unpack_all(z_full)
    m = model.m_arr.to(z_full.dtype); partner = model.partner; sign = model.tw_sign
    def gen(a):
        return sign[None, :] * m[None, :] * a[:, partner]
    extra = {k: gen(d[k]) for k in ("B", "D", "E") if d[k].numel() > 0}
    v = model.pack(gen(d["A"]), gen(d["C"]), d["c_l"], d["omega"], extra=extra)
    if model.free_params:
        v = v.clone(); v[-2:] = 0.0
    return v


def linearization_record(path, it, J, r, colnorm, param_idx, gauge_rows, gen_red, z_opt, phys, cost, note="", note_label="production Jacobian J_cw (pressure tables and nonlinear weights differentiated; closure target lagged)", kind="J_cw"):
    """Lead note 2026-10-28T20:43Z: R of the Householder QR of the scaled Jacobian J D^-1 with the parameter columns last, Q^T r, ||r||^2,
    the scaling D, column index map, gauge row indices and the phase-rotation generator (reduced coordinates), saved as .npz (float64)."""
    n = J.shape[1]
    others = [k for k in range(n) if k not in set(int(p) for p in param_idx)]
    perm = others + [int(p) for p in param_idx]
    Js = J[:, perm] / colnorm[perm][None, :]
    a, tau = torch.geqrf(Js)
    R = torch.triu(a[:n, :])
    Qtr = torch.ormqr(a, tau, r[:, None], transpose=True)[:n, 0]
    ph = phys or {}
    np.savez_compressed(path, R=R.cpu().numpy(), Qtr=Qtr.cpu().numpy(), r_norm2=float(r @ r), cost=cost, D=colnorm[perm].cpu().numpy(), perm=np.array(perm),
                        param_positions=np.arange(n - len(param_idx), n), gauge_rows=np.array(gauge_rows), n_rows=J.shape[0], generator_red=gen_red[perm].cpu().numpy(),
                        z_opt=z_opt.cpu().numpy(), params=json.dumps(ph), it=it, ts=now(), note=note, label=note_label,
                        jacobian_kind=kind, weights_differentiated=True, closure_target_differentiated=(kind == "J_c"), pressure_tables_differentiated=True,
                        supports_spec7_complete=(kind == "J_c"), coordinates="optimizer (z_c, z_w) with reduced tail-constrained coefficients",
                        chain_dcl_dzc=float(ph.get("dcl_dzc", float("nan"))), chain_domega_dzw=float(ph.get("domega_dzw", float("nan"))),
                        c_l=float(ph.get("c_l", float("nan"))), omega=float(ph.get("omega", float("nan"))))
    del a, tau, Js


def complete_jacobian_from_Jcw(prob, to_full, z_opt, J_cw, pidx, pm=None, log=None):
    """J_c (SPEC 7.0) from the production J_cw: closure block corrected for the lagged target G_required (dependence through the tail
    amplitudes and the parameters) and, for the two parameter columns, replaced by five-point differences of the closure rows with the
    carried patterns V(c_l, omega) and the target refreshed (closure_param_columns). Returns (J_c, info) or (None, reason)."""
    zf = to_full(z_opt).detach()
    out = prob.closure_target_correction(zf, to_full=to_full, z_opt=z_opt, log=log)
    if out is None:
        return J_cw, dict(note="no closure rows: J_c = J_cw")
    sl, corr, info = out
    if info and info.get("dN_fallback"):
        (log or print)("  WARNING: J_c target correction used the stencil dN (base-norm mismatch); the record is labelled dN_fallback")
    J_c = J_cw.clone()
    J_c[sl, :] = J_c[sl, :] + corr                                     # target G_required through (t, s, c_l, omega)(z_opt), tail expansion included
    cp = prob.closure_pattern_param_columns(zf)                          # carried patterns V(c_l, omega) only, physical derivatives
    if cp is not None and pidx:
        sl2, cols = cp
        d = pm.describe(z_opt); chain = (d["dcl_dzc"], d["domega_dzw"])
        for j, k in enumerate(pidx):
            J_c[sl2, k] = J_c[sl2, k] + cols[:, j] * chain[j]           # ADDED to J_cw + target correction, converted to optimizer coordinates (lead 22:58Z item 3)
    info = dict(info or {}); info.update(n_closure_rows=int(sl.stop - sl.start), correction_norm=float(corr.norm()), Jcw_closure_block_norm=float(J_cw[sl, :].norm()),
                pattern_columns_norm=(float(cols.norm()) if cp is not None else None), chain_factors=(chain if cp is not None else None),
                construction="J_c = J_cw + target correction (all columns, through to_full) + V(c_l, omega) five-point columns x chain factors on the closure block")
    return J_c, info


def cost_blocks_split(prob, model, r):
    """Deliverable B (lead 23:51Z item 2 (a)): 0.5 sum r^2 per row block: near origin (r <= 0.1 R0), core intermediate (0.1 R0 < r <= 256 R0),
    far momentum rows (r > 256 R0, source nodes), far anchors (appended anchor nodes), closure, gauge, other named blocks; and the total."""
    Nr, Na = model.Nr, model.Na; npde = 3 * Nr * Na
    rows = torch.arange(npde, device=r.device); node = (rows // Na) % Nr; rr = model.r[node]
    anc = (node >= model.Nr_src) if model.extra_r else torch.zeros_like(node, dtype=torch.bool)
    rp = r[:npde]
    out = dict(near_origin=0.5 * float((rp[rr <= 0.1 * model.R0] ** 2).sum()), core_intermediate=0.5 * float((rp[(rr > 0.1 * model.R0) & (rr <= 256.0 * model.R0)] ** 2).sum()),
               far_momentum=0.5 * float((rp[(rr > 256.0 * model.R0) & ~anc] ** 2).sum()), far_anchors=0.5 * float((rp[anc] ** 2).sum()))
    for nm, a0, a1 in prob.row_blocks():
        if nm != "pde":
            out[nm] = 0.5 * float((r[a0:(a1 if a1 is not None else r.numel())] ** 2).sum())
    out["total"] = 0.5 * float(r @ r)
    return out


def complete_gradient_opt(prob, pm, to_full, z_opt):
    """Complete gradient of O1 with respect to the optimizer coordinates: autograd through objective_graph and the composed map
    (tail-constraint expansion, parameter transform), plus the central-difference part through the carried closure patterns V(c_l, omega)."""
    zz = z_opt.detach().clone().requires_grad_(True)
    r = prob.objective_graph(to_full(zz))
    c = 0.5 * (r @ r)
    g, = torch.autograd.grad(c, zz); g = g.detach().clone()
    if pm.free and prob.closure is not None and prob.closure.get("G_req") is not None:
        zf = to_full(z_opt).detach()
        gV = prob_pattern_fd(prob, zf)
        d = pm.describe(z_opt)
        g[-2] += gV[0] * d["dcl_dzc"]; g[-1] += gV[1] * d["domega_dzw"]
    return g


def prob_pattern_fd(prob, zf, h=1e-4):
    from src.far_field.correction import carried_patterns
    if True:                                                          # closure_state_at and carried_patterns use autograd internally
        cl0 = prob.closure_state_at(zf)
        gV = torch.zeros(2, dtype=torch.float64, device=zf.device)
        for j, k in enumerate((-2, -1)):
            vals = []
            for sgn in (1.0, -1.0):
                zp = zf.detach().clone(); hk = h * max(1.0, abs(float(zf[k]))); zp[k] += sgn * hk
                aT, aS, c_l, omega = prob.model.unpack(zp)
                V, _ = carried_patterns(prob.model, float(c_l), float(omega), prob.model.R0 * cl0["grid"].n)
                clV = dict(cl0); clV["V"] = V
                with torch.no_grad():
                    rr = prob.closure_rows(zf.detach(), closure=clV)
                vals.append(0.5 * float(rr @ rr))
            gV[j] = (vals[0] - vals[1]) / (2 * hk)
    return gV


def source_moments(prob, model, z):
    """D6FP: discrete l = 0, 1 moments of the pressure source relative to the absolute sum of the integrand (lead 22:39Z item 3 (c))."""
    from src.equations import residuals as res
    with torch.no_grad():
        F = model.fields_grid(z, need_vort=False); f = res.pressure_source(F["GU"])
        mom = prob.pressure.discrete_moments(f, lmax=1)
    return mom                                                   # dict mode -> (M, abs_sum, ratio)


def load_start_state(cfg, model, prob, device, log, rng):
    """Initial full vector z (model layout; parameters cfg c_l, omega) and meta. Families (SPEC 8.2): init_from saved state (F1), parameter
    change with coefficients kept or refit (F2), coefficient perturbations (F3), random seeds (F4/F5) at any initial parameters (F6)."""
    meta = {}
    c_l0, om0 = float(cfg["c_l"]), float(cfg["omega"])
    if cfg.get("init_from"):
        src_path = cfg["init_from"] if os.path.isabs(cfg["init_from"]) else os.path.join(ROOT, cfg["init_from"])
        S = torch.load(src_path, map_location="cpu", weights_only=False); scfg = S["config"]
        msrc = Model(L=scfg["L"], Nk=scfg["Nk"], m_parity=scfg.get("m_parity", "even"), R0=scfg.get("R0", 1.0), Nr=scfg.get("Nr"), c_l=scfg["c_l"], omega=scfg["omega"],
                     free_params=bool(S.get("free_params", False)), channels=scfg.get("channels"), device=device, extra_r=scfg.get("far_radii"))
        if msrc.L != model.L:
            raise RuntimeError(f"main degree of the start ({msrc.L}) differs from the job ({model.L}); degree changes are forbidden (SPEC 1.1)")
        if msrc.Nk != model.Nk or (scfg.get("channels") or {}) != (cfg.get("channels") or {}) or abs(float(scfg.get("R0", 1.0)) - float(cfg.get("R0", 1.0))) > 0:
            raise RuntimeError("the job's basis (Nk, channels, R0) differs from the start's; a restart never changes the basis (SPEC 1.3)")
        zs = S["z"].to(device)
        if msrc.free_params:
            c_src, om_src = float(zs[-2]), float(zs[-1])
        else:
            c_src, om_src = float(scfg["c_l"]), float(scfg["omega"])
        z = embed_state(zs, msrc, model)                       # same basis: exact copy (parameters replaced below)
        if model.free_params:
            z = z.clone(); z[-2] = c_src; z[-1] = om_src
        sdh = S.get("spec_diag_holdout") or S.get("spec_diag") or {}
        meta.update(family="init_from", source=src_path, source_sha256=sha_file(src_path), source_c_l=c_src, source_omega=om_src,
                    source_rho_u=(sdh.get("global_") or {}).get("rho_u_max"), source_rho_u_half=(S.get("two_family") or {}).get("rho_u_max_half"),
                    max_U_start=((sdh.get("guards") or {}).get("N4_max_U")))
        if abs(c_l0 - c_src) > 1e-15 or abs(om0 - om_src) > 1e-15:
            mode = cfg.get("param_init_mode", "keep_coefficients")
            with torch.no_grad():
                U_src = msrc.fields_grid(zs, need_vort=False)["U"] if msrc.free_params else msrc.fields_grid(zs, need_vort=False)["U"]
            zp = z.clone()
            if model.free_params:
                zp[-2] = c_l0; zp[-1] = om0
            else:
                pass                                               # fixed-parameter model carries cfg parameters already
            if mode == "refit":
                # least-squares fit of the SOURCE velocity field (at the source parameters) into the basis at the new parameters
                tcf = TailConstraints(model) if cfg.get("tail_constraints", True) else None
                zfit, info = fit_field(model, U_src, expand=(lambda zr: tcf.expand(zr)) if tcf is not None else None, n_red=(tcf.n_red if tcf is not None else None))
                if model.free_params:
                    zfit = zfit.clone(); zfit[-2] = c_l0; zfit[-1] = om0
                zp = zfit
                meta["refit_info"] = {k: (float(v) if isinstance(v, (int, float)) else v) for k, v in info.items() if isinstance(v, (int, float))}
            with torch.no_grad():
                U_new = model.fields_grid(zp, need_vort=False)["U"]
                relU = float((U_new - U_src).norm() / U_src.norm().clamp_min(1e-300))
                # common-domain comparison (SPEC 6.5): per dyadic shell RMS change of U, F-gauge
                shells = {}
                for jj in range(-4, 9):
                    msk = (model.r >= model.R0 * 2.0 ** jj) & (model.r < model.R0 * 2.0 ** (jj + 1))
                    if msk.any():
                        a = (U_new[:, msk] - U_src[:, msk]).norm(); b = U_src[:, msk].norm().clamp_min(1e-300)
                        shells[f"2^{jj}"] = float(a / b)
            meta.update(param_init_mode=mode, param_init_from=[c_src, om_src], param_init_to=[c_l0, om0], relU_change_training=relU, relU_change_by_shell=shells)
            log(f"  parameter initialization {mode}: ({c_src:.6f}, {om_src:.6f}) -> ({c_l0:.6f}, {om0:.6f}); relative change of U on the training grid {relU:.3e}")
            z = zp
    else:
        fam = cfg.get("family", "random")
        z, meta = make_seed(prob, fam, rng, c_l0, om0, cfg.get("seed_params"))
        meta["family"] = fam
    # coefficient perturbations (F3): all coefficients (relative to the mean magnitude) or m != 0 modes only (field-relative)
    if float(cfg.get("perturb", 0) or 0) > 0:
        g = torch.tensor(rng.normal(size=model.n_coef), dtype=torch.float64, device=device)
        z = z.clone(); z[: model.n_coef] = z[: model.n_coef] + float(cfg["perturb"]) * g * z[: model.n_coef].abs().mean()
        meta["perturb"] = float(cfg["perturb"])
    if float(cfg.get("perturb_nonaxi", 0) or 0) > 0:
        dd = model.unpack_all(torch.tensor(rng.normal(size=model.n_z), dtype=torch.float64, device=device))
        mm = (model.m_arr > 0).to(torch.float64)
        extra = {k: dd[k] * mm[None, :] for k in ("B", "D", "E") if dd[k].numel() > 0}
        dz = model.pack(dd["A"] * mm[None, :], dd["C"] * mm[None, :], dd["c_l"], dd["omega"], extra=extra)
        if model.free_params:
            dz = dz.clone(); dz[-2:] = 0.0
        with torch.no_grad():
            U0n = model.fields_grid(z, need_vort=False)["U"].norm(); Upn = model.fields_grid(dz, need_vort=False)["U"].norm()
        z = z + dz * (float(cfg["perturb_nonaxi"]) * U0n / Upn.clamp_min(1e-300))
        meta["perturb_nonaxi_field_rel"] = float(cfg["perturb_nonaxi"])
    return z, meta


def finish_start(prob, model, z, cfg, log, hb, idx, holdout, device, JOB_PEAK, meta, out, hist, elapsed, rng_seed, tc, CODE_VERSIONS, job_id, run_dir, peig, gauge_defect_opt, extra_rec):
    """The frozen Euler3 end-of-start battery (copied verbatim from the frozen worker.py lines 569-884; variable names unchanged), followed by
    the start file and the ledger record. Returns (rec, zpath, holdout)."""
    state = {"gpu": torch.cuda.get_device_name(0) if device != "cpu" else "cpu"}
    t_fb0 = time.time(); _cpu_fb0 = time.process_time()                        # battery wall and process CPU time, recorded separately from the LM time (lead 23:51Z item 4, 02:09Z item 3 (e))
    battery = cfg.get("battery") or ("cheap" if str(device) == "cpu" else "full")   # lead 02:09Z item 3 (e): cheap set by default on CPU (spec diagnostics, holdout families, records);
    if battery == "cheap":                                                       # the long items (critical points, ray functionals, strength, core resolution, global balances) run only in "full" (separate EVAL jobs)
        cfg = dict(cfg); cfg.update(critical_points=False, ray_functionals=False, strength=False, core_resolution=False, global_balances=False)
    # re-pivot safety check and diagnostics
    diag = candidate_diagnostics(prob, z)
    gauge_defect, pivot_defect = prob.gauge_defects(z)
    maxU_fg = diag["nontriviality"]["max_abs_U"]
    hb.beat(force=True, start=idx, phase="diagnostics")           # the end-of-start battery can take 20-55 min at L6-ext/L8-ext: keep the heartbeat fresh (stale limit 1500 s)
    import threading
    _hb_stop = threading.Event()
    def _hb_watchdog():                                            # 2026-10-25T14:20Z: single battery items (RAY, holdout spheres) run 30 min without a beat at L8-ext
        while not _hb_stop.wait(60.0):
            try:
                hb.beat(force=True, start=idx, phase="diagnostics (watchdog)")
            except Exception:
                pass
    threading.Thread(target=_hb_watchdog, daemon=True).start()
    _mem_box = dict(last=time.time(), items=[])
    def _mem(tag):                                                 # 2026-10-25T18:40Z (lead): per-item allocated peak of the battery, then release the cached blocks
        if device != "cpu":
            try:
                pk = torch.cuda.max_memory_allocated() / 2**30; cur = torch.cuda.memory_allocated() / 2**30
                JOB_PEAK[0] = max(JOB_PEAK[0], pk)
                _mem_box["items"].append(dict(item=tag, peak_GB=round(pk, 2), after_GB=round(cur, 2), seconds=round(time.time() - _mem_box["last"], 1)))
                log(f"  BATTERY MEMORY [{tag}]: allocated peak since the previous item {pk:.1f} GB, held after it {cur:.1f} GB, {time.time() - _mem_box['last']:.0f} s")
                torch.cuda.empty_cache(); torch.cuda.reset_peak_memory_stats()
            except Exception:
                pass
        _mem_box["last"] = time.time()
    _mem("start (LM state released)")
    failure = None
    if maxU_fg < 1e-6 or gauge_defect > 1e-3:
        failure = "collapse_to_zero_or_gauge_failure"
        log(f"  FAILURE: {failure} (max|U|={maxU_fg:.2e}, gauge defect={gauge_defect:.2e}); no ratios, no tier evaluation")
    try:
        sd = spec_diagnostics(prob, z) if failure is None else None; tS, tS_checks = (tier_S(sd) if sd is not None else (False, {}))
    except Exception as e:
        log(f"  spec diagnostics failed: {e!r}"); sd = None; tS, tS_checks = False, {}
    _mem("spec_diagnostics (training grid)")
    sdh = None
    if sd is not None and cfg.get("holdout", True):
        try:
            if holdout is None:
                holdout = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)))
            sdh = spec_diagnostics(prob, z, holdout=holdout); tSh, tSh_checks = tier_S(sdh)
        except Exception as e:
            log(f"  holdout diagnostics failed: {e!r}"); sdh = None; tSh, tSh_checks = False, {}
    _mem("spec_diagnostics (holdout grid)")
    # SPEC v1.11 7.3a (lead 22:40Z item (c)): second shell family (half-offset dyadic shells), rho_nl^max over all shells of each
    # family, and the single-sphere maxima on the exchange radii R0 2^(j/4) inside the holdout range
    sdh_half = None; sph = None; tf = None
    if sdh is not None:
        try:
            r_max_h = float(model.r.max())
            holdout_half = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)), edges=half_offset_edges(model.R0, r_max_h))
            sdh_half = spec_diagnostics(prob, z, holdout=holdout_half, extras=False)
            sph = sphere_diagnostics(prob, z, exchange_radii(model.R0, model.R0 * 2.0 ** -6, r_max_h))
            tf = two_family_summary(sdh, sdh_half, sph)
        except Exception as e:
            log(f"  half-offset/sphere diagnostics failed: {e!r}"); sdh_half = None; sph = None; tf = None
    _mem("half-offset family and spheres")
    vd = None
    if sdh is not None and float(cfg.get("nu", 0.0) or 0.0) > 0:            # S8: viscous residual diagnostics on the holdout family
        try:
            from src.validation.viscous import viscous_diagnostics, viscous_text
            vd = viscous_diagnostics(prob, z, holdout, float(cfg["nu"]))
            log("  VISC (S8): " + viscous_text(vd))
        except Exception as e:
            log(f"  viscous diagnostics failed: {e!r}"); vd = None
    # SPEC v1.22 (a)(b) (lead 03:21Z item 5): tau_F at R = 2^8 R0 and 2^12 R0 and delta_G (core ball, every shell) by the twisted-ray functionals
    rayf = None
    if sd is not None and cfg.get("ray_functionals", True):
        try:
            from src.far_field.ray_functional import ray_functionals
            rayf = ray_functionals(prob, z, n_per_octave=12, k_in=8, k_out=16, radii_tau=[2.0 ** 8 * model.R0, 2.0 ** 12 * model.R0])
            tau_txt = ", ".join("%.4f at R %s" % (v, k) for k, v in rayf["tau_F"].items())
            log(f"  RAY (SPEC v1.22): tau_F = {tau_txt}; self-check F^(R)[LU] vs R^alpha U {max(rayf['selfcheck_FR_LU_vs_RalphaU'].values()):.1e}; delta_G core ball {rayf['delta_G_core_ball']:.3f}, max over shells {rayf['delta_G_max']:.3f}")
            sw = rayf.get("mean_swirl") or {}
            if sw.get("Q_sw") is not None:
                log(f"  SWIRL (d50/d55, lead 04:04Z): Q_sw = (1 - 2 c_l) max|Gamma_0| / max|S| = {sw['Q_sw']:.3f} (exact profile <= 1); max|Gamma_0| {sw['Gamma0_max']:.4f} at r {sw['r_at_Gamma0_max']:.3g}, max|S| {sw['S_max']:.4f} at r {sw['r_at_S_max']:.3g}, max|E| {sw['E_max']:.4f}; identity closure {sw['identity_closure']:.1e}")
            elif sw:
                log(f"  SWIRL block failed: {sw.get('error')}")
            bm = rayf.get("tau_F_by_m") or {}
            if bm:
                log("  RAY by |m| (d49b): generated fraction " + " ".join(f"m{m}:{v:.2f}" for m, v in zip(bm["m"], bm["generated_fraction"])) + " | tail fraction " + " ".join(f"m{m}:{v:.2f}" for m, v in zip(bm["m"], bm["tail_fraction"]))
                    + " | amplitude ratio generated/tail " + " ".join(f"m{m}:{v:.2f}" for m, v in zip(bm["m"], bm["amplitude_ratio"])) + " | m0 components (r, theta, phi) " + " ".join(f"{v:.2f}" for v in bm["m0_components_generated_over_tail"]))
        except Exception as e:
            log(f"  ray functionals failed: {e!r}"); rayf = None
    _mem("ray functionals (tau_F, delta_G, Q_sw)")
    # SPEC 4.4 angular closure (lead 22:40Z (a)): ||G[F]|| of the leading tail and dist(G[F], span of the carried B/D patterns)/||G[F]||
    gclos = None
    if sd is not None and (model.channels.get("NkB", 0) > 0 or model.channels.get("NkD", 0) > 0):
        try:
            from src.far_field.correction import closure_distance
            gclos = closure_distance(prob, z)
            log(f"  G-CLOSURE: ||G[F]||={gclos['G_norm']:.4f} dist(G, carried B/D span)/||G||={gclos['dist_rel']:.3e} (B degree {gclos.get('max_B_degree')}, D degree {gclos.get('max_D_degree')}, {gclos['n_columns']} columns, rank {gclos.get('rank')}); carried coefficient mismatch ||G_req - G_carried||/||G_req||={gclos.get('carried_mismatch_rel')} correlation={gclos.get('carried_correlation')}; direct far-energy coefficient ratio K_carried/K_required={gclos.get('K_ratio_direct')} (exact 1)")
            if gclos.get("K_H_required") is not None:            # SPEC v1.24 7.8 (lead 2026-10-25T09:58Z items 1-3)
                fm = lambda v, f="%.4f": (f % v) if isinstance(v, (int, float)) else "n/a"
                log(f"  FAR HELICITY (SPEC v1.24 7.8): K_H required={fm(gclos.get('K_H_required'))} carried={fm(gclos.get('K_H_carried'))} ratio K_H(carried)/K_H(required)={fm(gclos.get('K_H_ratio_direct'))} (exact 1; energy ratio {fm(gclos.get('K_ratio_direct'))}); "
                    f"identity closure {fm(gclos.get('K_H_identity_rel_closure'), '%.1e')}, two carried forms {fm(gclos.get('K_H_carried_two_forms_rel'), '%.1e')}, H_F(tail)={fm(gclos.get('H_F_tail'))} | "
                    f"G defect (d84): F-component {fm(gclos.get('G_defect_F_component'))}, cos against F {fm(gclos.get('G_defect_cos_F'), '%.3f')}, parallel fraction {fm(gclos.get('G_defect_parallel_fraction'), '%.3f')}, bound |K_E ratio - 1| <= m/c = {fm(gclos.get('d84_bound_energy_ratio'), '%.3f')}")
        except Exception as e:
            log(f"  G-closure diagnostics failed: {e!r}"); gclos = None
    _mem("G closure and far helicity")
    hb.beat(force=True, start=idx, phase="diagnostics (critical points)")
    crit = None
    if sd is not None and cfg.get("critical_points", True):
        try:
            tc0 = time.time()
            mx = local_maxima_omega(model, z, cfg["c_l"] if not model.free_params else float(z[-2]), cfg["omega"] if not model.free_params else float(z[-1]))
            zw = zeros_of_W(model, z, cfg["c_l"] if not model.free_params else float(z[-2]), cfg["omega"] if not model.free_params else float(z[-1]))
            crit = dict(local_maxima=mx, W_zeros=zw, seconds=time.time() - tc0)
            if sdh is not None and mx:
                tSh, tSh_checks = tier_S(sdh, located_lambda_max=mx[0].get("lambda_max_S"))   # N2 from the located maximum
            if mx:
                log(f"  CRITICAL: located |Omega| max {mx[0]['abs_Omega']:.4f} at r={mx[0]['r']:.3f}, strain ratio {mx[0]['strain_ratio']:.4f} (exact 1), transport {mx[0]['transport_ratio']:.1e}; W zeros found {len(zw)}" + (f", min eigvec defect {min(q['eigvec_defect'] for q in zw if q['eigvec_defect'] is not None):.3f}" if zw and any(q['eigvec_defect'] is not None for q in zw) else ""))
        except Exception as e:
            log(f"  critical-point diagnostics failed: {e!r}")
    _mem("critical points")
    strength = None
    if sd is not None and cfg.get("strength", True):
        try:
            strength = strength_diagnostics(model, z, cfg["c_l"] if not model.free_params else float(z[-2]), cfg["omega"] if not model.free_params else float(z[-1]),
                                            located_max_r=(crit["local_maxima"][0]["r"] if crit and crit["local_maxima"] else None))
            log(f"  STRENGTH: R_trap={strength['R_trap']} max|U|/c_l={strength['maxU_over_cl']:.3f} lam_max_S inside={strength['lambda_max_S_inside_Rtrap']} B(u)={strength['B_u']:.3f} |KU|/|U|={strength['KU_ratio']:.3f} |KOm|^2/|Om|^2={strength['KOmega_L2_ratio']:.3f}")
        except Exception as e:
            log(f"  strength diagnostics failed: {e!r}")
    _mem("strength")
    corer = None
    if sdh is not None and cfg.get("core_resolution", True):          # SPEC v1.21 (a)-(c) (lead 2026-10-25T02:24Z item 2)
        try:
            from src.validation.core_resolution import core_resolution, core_text
            mx = (crit or {}).get("local_maxima") or []
            guh = sdh["guards"]
            maxOm = max([guh["N2_max_abs_Omega"]] + [m_["abs_Omega"] for m_ in mx])
            if mx:
                ystar = mx[max(range(len(mx)), key=lambda i: mx[i]["abs_Omega"])]["y"]
                corer = core_resolution(prob, z, cfg["c_l"] if not model.free_params else float(z[-2]), cfg["omega"] if not model.free_params else float(z[-1]),
                                        ystar, guh["N4_max_U"], maxOm, core_ball_radius=sdh["shells"]["edges"][0][1])
                log("  CORE (SPEC v1.21): " + core_text(corer))
            else:
                log("  CORE (SPEC v1.21): no located |Omega| maximum; core-resolution sets not evaluated")
        except Exception as e:
            log(f"  core-resolution diagnostics failed: {e!r}"); corer = None
    _mem("core resolution")
    hb.beat(force=True, start=idx, phase="diagnostics (balances)")
    bal = None
    if sdh is not None and cfg.get("global_balances", True):             # d64 / S9 (lead 2026-10-25T05:36Z item 2): E_ren, H_tot, H_tot/int|h|, core alignment
        try:
            from src.validation.global_balances import GlobalBalances, balances_text
            gb_ = getattr(prob, "_gb", None)
            if gb_ is None:
                gb_ = GlobalBalances(model); prob._gb = gb_
            with torch.no_grad():
                b_ = gb_.integrals(z, r_core=sdh["guards"].get("N4_r_core"), K_H=((gclos or {}).get("K_H_carried")))   # v1.24: second exterior helicity term
            bal = {k: (float(v) if torch.is_tensor(v) else v) for k, v in b_.items()}
            log("  BALANCE (d64): " + balances_text(bal))
            try:
                from src.validation.global_balances import far_rate_text
                fr_ = gb_.far_energy_rate(prob, z); bal["far_rate"] = fr_
                log("  FAR RATE (d67): " + far_rate_text(fr_))
            except Exception as e:
                log(f"  far-rate diagnostics failed: {e!r}")
        except Exception as e:
            log(f"  global-balance diagnostics failed: {e!r}"); bal = None
    _mem("global balances and far rate")
    zpath = os.path.join(run_dir, "starts", f"start_{idx:03d}.pt")
    atomic_save(dict(z=z.detach().cpu(), config=cfg, meta=meta, diag=diag, spec_diag=sd, spec_diag_holdout=sdh, spec_diag_holdout_half=sdh_half, sphere_diag=sph, two_family=tf, G_closure=gclos, ray_functionals=rayf, global_balances=bal,
                     history=[{k: v for k, v in h.items() if k != "z"} for h in hist],      # 2026-10-25T22:33Z: per-iteration LM records (cost, rms, lam, accepted, t_jac, z_sha256_12) for T11 and V10 readings
                     critical=crit, strength=strength, core_resolution=corer, tier_S=tS, tier_S_checks=tS_checks,
                     tier_S_holdout=(tSh if sdh is not None else None), status=out["status"], lam=out["lam"],
                     free_params=model.free_params, modes=model.modes, iterations=len(hist), pivot=prob.pivot, pressure_eig_min=peig, d6fp=extra_rec), zpath)
    try:
        costs = [h.get("cost") for h in hist if h.get("cost") is not None]
        nten = max(1, len(costs) // 10)
        v10 = (costs[-1 - nten] - costs[-1]) / max(abs(costs[-1 - nten]), 1e-300) if len(costs) > nten else None
    except Exception:
        v10 = None; costs = []
    if v10 is not None:
        log(f"  V10 stationarity (SPEC 11c v1.18): relative cost decrease over the last tenth ({nten} of {len(costs)} iterations) = {v10:.3e} (GN-stationary if <= 1e-3)")
    rec = dict(kind="start_result", job_id=job_id, start=idx, family=meta.get("family"), c_l=diag["c_l"], omega=diag["omega"], v10_last_tenth_rel_decrease=v10, v10_iterations=len(costs),
               L=cfg["L"], Nk=cfg["Nk"], formulation=prob.formulation, m_parity=model.m_parity, rms0=meta.get("rms0"),
               rms_final=(diag["vorticity"]["rms_weighted"] if "vorticity" in diag else diag["momentum"]["rms_weighted"]),
               lm_rms_per_entry=out["rms"], cost_final=out["cost"], status=out["status"], iterations=len(hist), seconds=elapsed,
               rel_defect_max=max([v for v in (diag.get("vorticity") or diag.get("momentum"))["rel_defect_shells"] if v is not None] or [float("nan")]),
               rel_defect_mean=float(np.mean([v for v in (diag.get("vorticity") or diag.get("momentum"))["rel_defect_shells"] if v is not None] or [float("nan")])),
               core_nonaxi=diag["spectra"]["nonaxi_coef_fraction"],
               max_abs_Omega=diag["nontriviality"]["max_abs_Omega"], rotation_content_rel=diag["nontriviality"]["rotation_content_rel"],
               tail_nonaxi=diag["tail"]["nonaxi_fraction"], strain_at_max=diag["strain"]["omega_S_omega_over_omega2_at_max"],
               lambda_max_S=diag["strain"]["lambda_max_S_global"], r_peak_Omega=diag["core"]["r_peak_Omega"],
               top_k_fraction=diag["spectra"]["top_k_fraction"], top_l_fraction=diag["spectra"]["top_l_fraction"],
               zfile=os.path.relpath(zpath, ROOT), gpu=state["gpu"], gauge_version=2, gauge_defect=gauge_defect, pivot_defect=pivot_defect,
               gauge_weight=cfg.get("gauge_weight", 100.0), max_U=maxU_fg, failure=failure, solver_version=SOLVER_VERSION,
               gauge_defect_optimizer=gauge_defect_opt, rng_seed=rng_seed, tail_constraints=bool(tc is not None), nl_denominator=cfg.get("nl_denominator", "nl"),
               projected_warm_start=meta.get("projected_warm_start", False), relU_change_holdout=meta.get("relU_change_holdout"),
               cost_blocks_parent=meta.get("cost_blocks_parent"), cost_blocks_projected=meta.get("cost_blocks_projected"), source_rho_u=meta.get("source_rho_u"),
               code_versions=CODE_VERSIONS, jtj_blocks=int(cfg.get("jtj_blocks", 1)), battery_memory=_mem_box["items"])
    rec["t_battery_s"] = time.time() - t_fb0; rec["t_lm_s"] = elapsed; rec["battery_set"] = battery; rec["battery_cpu_time_s"] = time.process_time() - _cpu_fb0
    if strength is not None:
        rec.update(R_trap=strength["R_trap"], lambda_max_S_inside_Rtrap=strength["lambda_max_S_inside_Rtrap"], B_u=strength["B_u"], KU_ratio=strength["KU_ratio"], KOmega_L2_ratio=strength["KOmega_L2_ratio"])
    if sd is not None:
        g = sd["global_"]; n = sd["nonaxi"]; gu = sd["guards"]
        rec.update(rho_u_max=g["rho_u_max"], rho_u_bal=g["rho_u_bal"], rho_nl_max=g["rho_nl_max"], pi_u_max=g["pi_u_max"], rho_Om_max=g["rho_Om_max"],
                   A_u=g["A_u"], A_Om=g["A_Om"], N_core=n["N_core"], e_core=n["e_core"], N_F=n["N_F"], e_F=n["e_F"], r_core=gu["N4_r_core"],
                   r_tail=gu["N5_r_tail"], max_U=gu["N4_max_U"], lambda_max_S=gu["N2_lambda_max_S"], tier_S=tS,
                   optimizer=cfg.get("optimizer", "lm"), nl_weighting=bool(cfg.get("nl_weighting", False)), efrac=cfg.get("efrac"))
        if sdh is not None:
            gh = sdh["global_"]; nh = sdh["nonaxi"]; guh = sdh["guards"]
            rec.update(rho_u_max_holdout=gh["rho_u_max"], rho_u_bal_holdout=gh["rho_u_bal"], rho_nl_max_holdout=gh["rho_nl_max"], pi_u_max_holdout=gh["pi_u_max"],
                       rho_Om_max_holdout=gh["rho_Om_max"], A_u_holdout=gh["A_u"], N_core_holdout=nh["N_core"], e_core_holdout=nh["e_core"],
                       r_core_holdout=guh["N4_r_core"], r_tail_holdout=guh["N5_r_tail"], tier_S_holdout=tSh,
                       pressure_ray_check=(sdh["pressure"].get("ray_check", {}).get("max_rel_diff")))
            if tf is not None:
                rec.update(rho_u_max_holdout_half=tf["rho_u_max_half"], rho_u_max_holdout_both=tf["rho_u_max_both"], rho_nl_max_holdout_half=tf["rho_nl_max_half"],
                           rho_nl_max_holdout_both=tf["rho_nl_max_both"], sphere_rho_u_max=tf["sphere_rho_u_max"], sphere_r_at_max=tf["sphere_r_at_max"],
                           sphere_rho_nl_max=tf["sphere_rho_nl_max"], sphere_r_at_nl_max=tf["sphere_r_at_nl_max"], tier_S_holdout_half=tier_S(sdh_half)[0],
                           rho_lin_max_holdout=tf.get("rho_lin_max_std"), rho_lin_max_holdout_half=tf.get("rho_lin_max_half"), rho_sp_max_holdout=tf.get("rho_sp_max_std"),
                           rho_sp_max_holdout_half=tf.get("rho_sp_max_half"), rho_lin_max_r1_holdout=tf.get("rho_lin_max_r1_std"), rho_sp_max_r1_holdout=tf.get("rho_sp_max_r1_std"),
                           d30_Ru_over_T1_r1=tf.get("d30_Ru_over_T1_r1"), d30_ROm_over_Om=tf.get("d30_ROm_over_Om"), gram_gamma_shells=tf.get("gram_gamma_std"),
                           gram_a_shells=tf.get("gram_a_std"), gram_b_shells=tf.get("gram_b_std"), gram_check_max=tf.get("gram_check_max"),
                           sigma_u_max=tf.get("sigma_u_max_std"), sigma_u_max_shell=tf.get("sigma_u_max_shell_std"), sigma_u_max_half=tf.get("sigma_u_max_half"),
                           sigma_u_max_r1=tf.get("sigma_u_max_r1_std"), sigma_Om=tf.get("sigma_Om"), a_max=tf.get("a_max_std"), a_max_half=tf.get("a_max_half"),
                           origin_U_rms=tf.get("origin_U_rms"), origin_B=tf.get("origin_B"), origin_L=tf.get("origin_L"),
                           structure=tf.get("structure"), peak_max_holdout=tf.get("peak_max_std"),
                           max_U_start=meta.get("max_U_start"), source_rho_u_half=meta.get("source_rho_u_half"), source_rho_nl=meta.get("source_rho_nl"), source_sphere_rho_u=meta.get("source_sphere_rho_u"))
        if gclos is not None:
            rec.update(G_norm=gclos.get("G_norm"), G_closure_rel=gclos.get("dist_rel"), G_span_rank=gclos.get("rank"), G_span_columns=gclos.get("n_columns"),
                       G_carried_mismatch_rel=gclos.get("carried_mismatch_rel"), G_carried_correlation=gclos.get("carried_correlation"), G_carried_norm=gclos.get("G_carried_norm"),
                       K_ratio_direct=gclos.get("K_ratio_direct"), K_H_required=gclos.get("K_H_required"), K_H_carried=gclos.get("K_H_carried"), K_H_ratio_direct=gclos.get("K_H_ratio_direct"),
                       K_H_identity_rel_closure=gclos.get("K_H_identity_rel_closure"), G_defect_F_component=gclos.get("G_defect_F_component"), G_defect_cos_F=gclos.get("G_defect_cos_F"),
                       G_defect_parallel_fraction=gclos.get("G_defect_parallel_fraction"), d84_bound_energy_ratio=gclos.get("d84_bound_energy_ratio"))
        rec.update(channels=model.channels, L_ext=getattr(model, "L_ext", cfg["L"]), n_z=model.n_z)
        if vd is not None:
            rec.update(nu=vd["nu"], label="viscous continuation state (S8); not an Euler candidate", rho_nu_max_holdout=vd["rho_nu_max"], sigma_nu_max_holdout=vd["sigma_nu_max"],
                       rho_u_inviscid_of_viscous_state=vd["rho_u_max"], sigma_u_inviscid_of_viscous_state=vd["sigma_u_max"], visc_share_max=vd["visc_share_max"],
                       dissipation_D_holdout=vd["dissipation_D_holdout_range"], omega_final=vd["omega"], c_l_final=vd["c_l"])
        try:                                                   # lead 2026-10-25T07:14Z item 5: radial Chebyshev decay per block (last-coefficient ratio)
            dd_ = model.unpack_all(z); spec_ = {}
            for nm_ in ("A", "C", "B", "D", "E"):
                arr = dd_.get(nm_)
                if arr is None or arr.numel() == 0 or arr.shape[0] < 2:
                    continue
                mx = float(arr.abs().max()); last = float(arr[-1].abs().max()); last2 = float(arr[-2:].abs().max())
                spec_[nm_] = dict(n_k=int(arr.shape[0]), last_over_max=last / max(mx, 1e-300), last2_over_max=last2 / max(mx, 1e-300))
            rec.update(coef_decay=spec_)
            log("  SPECTRUM (radial Chebyshev, last coefficient / block maximum): " + ", ".join(f"{k}: {v['last_over_max']:.2e} (Nk {v['n_k']})" for k, v in spec_.items()))
        except Exception as e:
            log(f"  SPECTRUM line failed: {e!r}")
        try:                                                   # d93 / S12 (lead 11:17Z, 11:27Z): radial-lambda structure of the momentum residual on the training grid
            if prob.formulation in ("mom", "both"):
                rl_ = prob.radial_lambda_diagnostics(z)
                rec.update(radial_lambda_share=rl_["radial_lambda_share"], pointwise_along_U_share=rl_["pointwise_along_U_share"], lambda_max=rl_["lambda_max"], r_at_lambda_max=rl_["r_at_lambda_max"],
                           negative_pairing_fraction=rl_["negative_pairing_fraction"], lambda_n_octaves_negative=rl_["n_octaves_negative"], radial_lambda_w=cfg.get("radial_lambda_w"))
                log(f"  RADIAL LAMBDA (d93, training grid): share of the weighted squared momentum residual along lambda(r) U = {rl_['radial_lambda_share']:.3f} (pointwise along-U share {rl_['pointwise_along_U_share']:.3f}); lambda max {rl_['lambda_max']:.3f} at r {rl_['r_at_lambda_max']:.3g}; shell-balanced negative radial-average fraction sum max(-w_k a_k, 0)/sum |w_k a_k| {rl_['negative_pairing_fraction']:.2e}; octaves with lambda < 0: {rl_['n_octaves_negative']} of {len(rl_['lambda_by_octave'])} (lambda by octave of r/R0: " + " ".join(f"{k}:{v:+.3f}" for k, v in rl_['lambda_by_octave'].items()) + ")")
        except Exception as e:
            log(f"  RADIAL LAMBDA line failed: {e!r}")
        try:                                                   # S7: mean-swirl fraction of the leading tail (toroidal m = 0 energy / ||F||^2)
            aT_, aS_, cl_, om_ = model.unpack(z)
            rec.update(f_sw_tail=float(prob.tail_mean_swirl_fraction(aT_, aS_, cl_, om_)), fsw_target=cfg.get("fsw"), boost_e_core=cfg.get("boost_e_core"))
        except Exception:
            pass
        if rayf is not None:
            tk = sorted(rayf["tau_F"].keys(), key=float)
            rec.update(tau_F_R8=rayf["tau_F"][tk[0]], tau_F_R12=(rayf["tau_F"][tk[1]] if len(tk) > 1 else None), tau_F_selfcheck=max(rayf["selfcheck_FR_LU_vs_RalphaU"].values()),
                       delta_G_core=rayf["delta_G_core_ball"], delta_G_max=rayf["delta_G_max"], delta_G_shells=rayf["delta_G_shells"]["delta_G"], G_identity_rel=rayf["G_identity_rel"],
                       tau_F_by_m=rayf.get("tau_F_by_m"))
            sw = rayf.get("mean_swirl") or {}
            rec.update(Q_sw=sw.get("Q_sw"), Gamma0_max=sw.get("Gamma0_max"), S_max=sw.get("S_max"), E_swirl_max=sw.get("E_max"), swirl_identity_closure=sw.get("identity_closure"))
        try:                                                   # SPEC 7.6 / T08 origin Taylor ratios (floored), from the holdout evaluation's origin block
            og = (sdh or sd).get("origin") or {}
            rec.update(tau0_floored=og.get("tau0_floored"), tau1_floored=og.get("tau1_floored"), tau2_floored=og.get("tau2_floored"), tau0_raw=og.get("tau0_raw"),
                       tau1_raw=og.get("tau1_raw"), tau2_raw=og.get("tau2_raw"), taylor_consistency=og.get("taylor_consistency_rel_change_tau"))
            if og.get("tau1_floored") is not None:
                log(f"  ORIGIN (SPEC 7.6, T08): tau_0 {og.get('tau0_floored'):.3e} tau_1 {og['tau1_floored']:.3e} tau_2 {og['tau2_floored']:.3e} (floored; raw {og.get('tau0_raw')}, {og.get('tau1_raw')}, {og.get('tau2_raw')}); fit/check consistency {['%.1e' % v for v in og.get('taylor_consistency_rel_change_tau', [])]}; D0 vs exact {og.get('taylor_D0_Ru_vs_exact_rel')}")
        except Exception as e:
            log(f"  ORIGIN line failed: {e!r}")
        if bal is not None:
            rec.update(E_ren=bal["E_ren"], H_tot=bal["H_tot"], H_abs=bal["H_abs"], H_tot_over_abs=bal["H_tot_over_abs"], core_alignment=bal.get("core_alignment"),
                       E_ren_change_2oct=bal["E_ren_change_2oct"], H_tot_change_2oct=bal["H_tot_change_2oct"], E_F_max=bal.get("E_F_max"), r_at_E_F_max=bal.get("r_at_E_F_max"),
                       E_F_weighted_excess=bal.get("E_F_weighted_excess"), E_F_weighted_deficit=bal.get("E_F_weighted_deficit"), E_ren_two_forms_rel_diff=bal.get("E_ren_two_forms_rel_diff"),
                       H_F_sign_change_radii=bal.get("H_F_sign_change_radii"), balance_lambda=cfg.get("balance_lambda"),
                       kappa_far_finite_radius={k: v.get("kappa") for k, v in (bal.get("far_rate") or {}).items()}, Phi_F_far_finite_radius={k: v.get("Phi_F") for k, v in (bal.get("far_rate") or {}).items()})
        if corer is not None and "a_eff" in corer:
            bh, bq = corer["balls"]["half"], corer["balls"]["quarter"]; ish = corer.get("inner_shells") or {}
            rec.update(a_eff=corer["a_eff"], y_star=corer["y_star"], r_star=corer["r_star"], core_ball_over_a_eff=corer["core_ball_over_a_eff"],
                       sigma_u_ball_half=bh["sigma_u"], sigma_u_ball_quarter=bq["sigma_u"], a_max_ball_half_centre=bh["a_max_centre"], a_max_ball_half_upper=bh["a_max_upper"],
                       a_max_ball_quarter_centre=bq["a_max_centre"], a_max_ball_quarter_upper=bq["a_max_upper"], sigma_Om_ball_half=bh["sigma_Om"],
                       inner_sigma_u_max=ish.get("sigma_u_max"), inner_a_max=ish.get("a_max"), core_resolved=corer["core_resolved"], core_doubling_change_max=corer["max_doubling_rel_change"],
                       sigma_u_max_core=max([v for v in (rec.get("sigma_u_max"), rec.get("sigma_u_max_half"), corer["sigma_u_max_added"]) if v is not None]),
                       a_max_core=max([v for v in (rec.get("a_max"), rec.get("a_max_half"), corer["a_max_added_centre"]) if v is not None]),
                       a_max_core_upper=max([v for v in (rec.get("a_max"), rec.get("a_max_half"), corer["a_max_added_upper"]) if v is not None]))
        if crit is not None and crit["local_maxima"]:
            m0 = crit["local_maxima"][0]
            rec.update(located_max_abs_Omega=m0["abs_Omega"], located_max_r=m0["r"], located_strain_ratio=m0["strain_ratio"], located_transport_ratio=m0["transport_ratio"],
                       n_W_zeros=len(crit["W_zeros"]), min_W_eigvec_defect=(min([q["eigvec_defect"] for q in crit["W_zeros"] if q["eigvec_defect"] is not None] or [None]) if crit["W_zeros"] else None))
        gi = sd.get("global_integrals", {}) if sd else {}
        rec.update(Z=gi.get("Z"), Sigma_Z=gi.get("Sigma_Z"), F_norm2=gi.get("F_norm2"), gauge=cfg.get("gauge", "F"), sigmaZ_target=cfg.get("sigmaZ"), far_radii=cfg.get("far_radii"))
    if "momentum" in diag:
        rec["rms_mom"] = diag["momentum"]["rms_weighted"]; rec["max_mom"] = diag["momentum"]["max_scaled"]
    if "vorticity" in diag:
        rec["rms_vort"] = diag["vorticity"]["rms_weighted"]; rec["max_vort"] = diag["vorticity"]["max_scaled"]
    log(f"start {idx} done: rms {meta.get('rms0', float('nan')):.3e} -> {out['rms']:.3e} ({out['status']}, {len(hist)} its, {elapsed:.0f}s) | {summary_line(diag)} | gauge defect {gauge_defect:.2e} (optimizer {gauge_defect_opt:.2e} before the exact projection) pivot defect {pivot_defect}")
    if sd is not None:
        log(f"  SPEC: rho_u_max={g['rho_u_max']:.3e} rho_nl_max={g['rho_nl_max']:.3e} pi_u_max={g['pi_u_max']:.3e} rho_Om_max={g['rho_Om_max']:.3e} N_core={n['N_core']:.2e} e_F={n['e_F']:.2e} r_core={gu['N4_r_core']:.3g} r_tail={gu['N5_r_tail']} maxU={gu['N4_max_U']:.3e} lam_max_S={gu['N2_lambda_max_S']:.3f} tierS={tS}")
        if sdh is not None:
            log(f"  HOLDOUT: rho_u_max={gh['rho_u_max']:.3e} rho_nl_max={gh['rho_nl_max']:.3e} pi_u_max={gh['pi_u_max']:.3e} rho_Om_max={gh['rho_Om_max']:.3e} N_core={nh['N_core']:.2e} e_core={nh['e_core']:.2e} r_core={guh['N4_r_core']:.3g} r_tail={guh['N5_r_tail']} tierS={tSh}")
            if tf is not None:
                log(f"  TWO-FAMILY (SPEC 7.3a): {summary_text(tf)} | max|U| start {meta.get('max_U_start')} -> {guh['N4_max_U']:.3e}")
                log(f"  STRUCTURE (lead 02:02Z 2(b)(c)(e)): {structure_text(tf)}")
                if rec.get("f_sw_tail") is not None:
                    log(f"  TAIL SWIRL (S7): mean-swirl fraction of the tail f_sw = {rec['f_sw_tail']:.4f}" + (f" (constraint target {cfg.get('fsw')})" if cfg.get("fsw") is not None else ""))
                try:
                    gr = sdh.get("gram") or {}; ed = sdh["shells"]["edges"]
                    core = [k for k in range(len(ed)) if ed[k][1] <= 1.0 + 1e-12 and gr["gamma"][k] is not None]
                    log("  GRAM (SPEC v1.15 7.2, core shells r_hi <= 1; exact profile b/a = 1, gamma = -1): " + "; ".join(f"[{ed[k][0]:.3g},{ed[k][1]:.3g}) b/a={gr['b_rms_N'][k] / max(gr['a_rms_L'][k], 1e-300):.2f} gamma={gr['gamma'][k]:+.2f} rho_u={sdh['rho_u'][k]:.3f}" for k in core))
                except Exception as e:
                    log(f"  GRAM line failed: {e!r}")
    rec.update(extra_rec)
    ledger.append(LEDGER, rec)
    with open(os.path.join(run_dir, "results.jsonl"), "a") as f:
        f.write(json.dumps(rec) + "\n")
    _hb_stop.set()
    return rec, zpath, holdout


def run_job(job_path, run_dir):
    job = json.load(open(job_path))
    cfg = job["config"]; job_id = job["job_id"]; label = job.get("label", "FREE" if cfg.get("free_params") else "FIXED-CONTROL")
    os.makedirs(run_dir, exist_ok=True); os.makedirs(os.path.join(run_dir, "starts"), exist_ok=True)
    logf = open(os.path.join(run_dir, "worker.log"), "a")
    def log(msg):
        line = f"{now()} {msg}"
        logf.write(line + "\n"); logf.flush(); print(line, flush=True)
    hb = Heartbeat(os.path.join(ROOT, "status", f"heartbeat_{job_id}.json"), job_id)
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch.set_num_threads(int(cfg.get("threads", 1)))
    t_job0 = time.time()
    global CKPT_INTERVAL
    CKPT_INTERVAL = float(cfg.get("ckpt_interval_s", CKPT_INTERVAL))
    ck_path = os.path.join(run_dir, "checkpoint.pt")
    state = dict(job_id=job_id, label=label, config=cfg, completed=[], current=None, started=now(), resumed=0,
                 versions=dict(torch=torch.__version__, numpy=np.__version__, python=sys.version.split()[0]),
                 gpu=torch.cuda.get_device_name(0) if device != "cpu" else "cpu", interruptions=[])
    resumed_from_checkpoint = False                                                    # gpu_v1 patch 1 (lead 05:23Z item 1): keys the entry projection
    if cfg.get("continue_from_run") and not os.path.exists(ck_path):                   # gpu_v1 patch 1 (SPEC v1.14 3.6 (f), lead 05:23Z item 2 and 05:30Z item 2):
        src_ck = os.path.join(ROOT, cfg["continue_from_run"], "checkpoint_segment_end.pt")   # segment k+1 continues the SAME optimizer state of segment k through the resume path
        ok_cont, why = False, ""
        if os.path.exists(src_ck):
            prev = torch.load(src_ck, map_location="cpu", weights_only=False); pc = prev.get("current") or {}
            IGN = {"max_iter", "time_limit_per_start", "continue_from_run", "segment", "tag"} | {"step_jacobian", "s2_smoke", "s2_smoke_save_Jc_it0"} | ({"battery"} if cfg.get("s2_smoke") else set())   # STRATEGY 2: the s2 keys (and, for the smoke runs only, the battery set) may be added to a continued configuration
            diff_keys = sorted(k for k in set(prev.get("config", {})) | set(cfg) if k not in IGN and prev.get("config", {}).get(k) != cfg.get(k))
            if not pc or int(pc.get("it", 0)) <= 0:
                why = "no resumable current state or iteration count not positive (3.6 rule (b))"
            elif pc.get("counters") is None:
                why = "checkpoint without the counters field (legacy, rule (b))"
            elif pc.get("grad_every") is not None and int(pc["grad_every"]) != int(cfg.get("complete_gradient_every", 1) or 1):
                why = f"grad_every mismatch: checkpoint {pc.get('grad_every')} vs cfg {cfg.get('complete_gradient_every')} (rule (a))"
            elif diff_keys:
                why = f"job config differs from the checkpoint's in {diff_keys} (only max_iter and time_limit may change, rule (a))"
            else:
                ok_cont = True
        else:
            why = f"{src_ck} missing"
        if ok_cont:
            prev["job_id_segment_source"] = prev.get("job_id"); prev["job_id"] = job_id; prev["config"] = cfg
            atomic_save(prev, ck_path)
            log(f"SEGMENT CONTINUATION from {cfg['continue_from_run']}: checkpoint_segment_end.pt (it {pc['it']}, counters {pc.get('counters')}, lam {pc['lam']:.17e}) copied; resuming by the production path")
            ledger.append(LEDGER, dict(kind="segment_continuation", job_id=job_id, source_run=cfg["continue_from_run"], source_job=prev.get("job_id_segment_source"), it=int(pc["it"]), counters=pc.get("counters"), label=label))
        else:
            log(f"SEGMENT CONTINUATION REFUSED ({why}): this job runs as a FRESH START (recorded)")
            ledger.append(LEDGER, dict(kind="continuation_refused", job_id=job_id, source_run=cfg.get("continue_from_run"), reason=why, label=label))
    if os.path.exists(ck_path):
        state = torch.load(ck_path, map_location="cpu", weights_only=False)
        resumed_from_checkpoint = state.get("current") is not None
        if resumed_from_checkpoint:                                                     # gpu_v1 patch 1 (lead 05:30Z rules (a), (b)): a resumable state must have it > 0,
            pc = state["current"]; ge_ck = pc.get("grad_every"); ge_cfg = int(cfg.get("complete_gradient_every", 1) or 1)   # the counters field and the same gradient spacing
            why = None
            if int(pc.get("it", 0)) <= 0:
                why = "checkpoint at iteration 0 (rule (b)): rerun as a fresh start"
            elif pc.get("counters") is None:
                why = "checkpoint without the counters field (legacy cpu_v1, rule (b)): rerun as a fresh start"
            elif ge_ck is not None and int(ge_ck) != ge_cfg:
                why = f"grad_every mismatch: checkpoint {ge_ck} vs cfg {ge_cfg} (rule (a)): rerun as a fresh start"
            if why:
                log(f"RESUME REFUSED: {why}"); ledger.append(LEDGER, dict(kind="resume_refused_fresh_start", job_id=job_id, reason=why, it=int(pc.get("it", 0)), label=label))
                state["current"] = None; resumed_from_checkpoint = False
        state["resumed"] = state.get("resumed", 0) + 1
        state.setdefault("interruptions", []).append(dict(ts=now(), event="resume", completed=len(state["completed"]), current_it=(None if state["current"] is None else state["current"]["it"])))
        log(f"RESUME from checkpoint: {len(state['completed'])} starts completed, current={None if state['current'] is None else state['current']['idx']}, resumed {state['resumed']}x")
        ledger.append(LEDGER, dict(kind="resume", job_id=job_id, completed=len(state["completed"]), resumed=state["resumed"]))
    cmark = os.path.join(ROOT, "queue", "cancel", job_id)
    if os.path.exists(cmark):
        log(f"CANCELLED at launch: marker {cmark} found; no computation"); ledger.append(LEDGER, dict(kind="job_cancelled", job_id=job_id)); hb.beat(force=True, phase="cancelled")
        return 0
    log(f"START job {job_id} label {label} on {device} ({state['gpu']}) cfg={json.dumps(cfg)}")
    log(f"PRECISION: float64; TF32 matmul {torch.backends.cuda.matmul.allow_tf32}, cudnn {torch.backends.cudnn.allow_tf32} (SPEC 1.4); OMP_NUM_THREADS {os.environ.get('OMP_NUM_THREADS')}; CUDA_VISIBLE_DEVICES {os.environ.get('CUDA_VISIBLE_DEVICES')}")
    CODE_VERSIONS = code_versions()
    log("CODE VERSIONS (sha256[:12], mtime): " + ", ".join(f"{k} {v.get('sha256_12')}" for k, v in CODE_VERSIONS.items()))
    solver_settings = dict(jacobian_mode=cfg.get("jacobian_mode", "weights_differentiated"), param_scale_pde_rows=bool(cfg.get("param_scale_pde_rows", True)),
                           stable_linear=bool(cfg.get("stable_linear", True)), exterior_monopole=bool(cfg.get("exterior_monopole", False)), param_map="c_l = 0.4 + 0.1 sigmoid(z_c), omega = exp(z_w)" if cfg.get("free_params") else "fixed",
                           param_step_max=float(cfg.get("param_step_max", 0.5)), acceptance="self-consistent O1 (objective_at)", kappa_margin=2.0, alpha_margin=0.7,
                           complete_gradient_every=int(cfg.get("complete_gradient_every", 1) or 1), linearization_every=int(cfg.get("linearization_every", 0) or 0))
    log("SOLVER SETTINGS: " + json.dumps(solver_settings))
    ledger.append(LEDGER, dict(kind="job_code_versions", job_id=job_id, retries=job.get("retries", 0), code_versions=CODE_VERSIONS, label=label, solver_settings=solver_settings,
                               config_sha256=hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()))
    t_b = time.time()
    model, prob = build(cfg, device)
    tc = TailConstraints(model) if cfg.get("tail_constraints", True) else None
    pm = ParamMap(free=bool(model.free_params))
    log(f"build {time.time() - t_b:.1f}s: Nq={model.Nq} Nk={model.Nk} Nr={model.Nr} Na={model.Na} n_z={model.n_z} n_res={prob.n_pde_residuals()} pressure quad {prob.pressure.n_quad} geometry {prob.pressure.geometry_id}" + (f"; tail constraints {model.n_z} -> {tc.n_red} unknowns" if tc else ""))
    hb.beat(force=True, phase="build", n_z=model.n_z, n_res=prob.n_pde_residuals())
    peig = min_pressure_eigenvalue(cfg["c_l"], cfg["omega"], cfg["L"], cfg.get("m_parity", "even"))
    JOB_PEAK = [0.0]
    n_starts = int(cfg.get("n_starts", 1))
    holdout = None
    to_full = (lambda zo: tc.expand(pm.expand(zo))) if tc is not None else (lambda zo: pm.expand(zo))
    to_opt = (lambda zf: pm.reduce(tc.reduce(zf))) if tc is not None else (lambda zf: pm.reduce(zf))
    time_cap_job = TEAM_STOP_EPOCH - 25 * 60 - time.time()          # leave 25 min for the battery and the record before the team stop
    for idx in range(n_starts):
        if idx in [c["idx"] for c in state["completed"]]:
            continue
        if STOP["flag"]:
            break
        rng_seed = int(cfg.get("seed", 0)) * 1000003 + idx
        rng = np.random.default_rng(rng_seed)
        cur = state["current"]
        geometry_base = None
        if cur is not None and cur["idx"] == idx:
            z_opt = cur["z_opt"].to(device); meta = cur["meta"]; it0 = cur["it"]; lam = cur["lam"]; hist = cur["history"]; prob.pivot = cur["pivot"]
            geometry_base = cur.get("geometry_base"); rng.bit_generator.state = cur["rng_state"]
            counters0 = cur.get("counters")                                                      # gpu_v1 (V161): cumulative LM counters saved with the checkpoint
            ge_ck, ge_cfg = cur.get("grad_every"), int(cfg.get("complete_gradient_every", 1) or 1)
            log(f"  resume record: checkpoint grad_every {ge_ck}, cfg complete_gradient_every {ge_cfg} (equal: {ge_ck is None or int(ge_ck) == ge_cfg}), counters {counters0}, it {it0}")
            log(f"start {idx}: resuming at iteration {it0} with lam {lam:.17e}; geometry base {geometry_base}; counters {counters0}; rng_state_sha256 {hashlib.sha256(json.dumps(rng.bit_generator.state, sort_keys=True, default=str).encode()).hexdigest()}; resumed vector sha256 {hashlib.sha256(z_opt.detach().cpu().numpy().tobytes()).hexdigest()} (no entry projection on resume, V162)")
            zf = to_full(z_opt)
            if geometry_base is not None and model.free_params:                      # identical quadrature layout (SPEC G7)
                prob.geometry_generation = getattr(prob, "geometry_generation", 0) + 1     # table-cache generation counter (lead 02:48Z item 6)
                prob.pressure = PressureSolver(model, p0=2 * alpha_of(geometry_base["c_l"]) + 2, omega=geometry_base["omega"], c_l=geometry_base["c_l"])
                if prob.fine_model is not None:
                    prob.fine_ps = PressureSolver(prob.fine_model, p0=2 * alpha_of(geometry_base["c_l"]) + 2, omega=geometry_base["omega"], c_l=geometry_base["c_l"])
        else:
            zf, meta = load_start_state(cfg, model, prob, device, log, rng)
            prob.pivot = prob.choose_pivot(zf)
            it0 = 0; lam = float(cfg.get("lam0", 1e-2)); hist = []; counters0 = None
            if model.free_params:                                                      # geometry sized at the initial parameters (SPEC 2.5 stage layout)
                prob.ensure_geometry(zf)
            zf = prob.phase_align(zf)
            z_opt = to_opt(zf); zf = to_full(z_opt)
            meta["pivot"] = prob.pivot; meta["n_opt"] = int(z_opt.numel())
            r0, aux0 = prob.objective_at(zf); prob.commit_aux(aux0)
            meta["cost0"] = 0.5 * float(r0 @ r0); meta["rms0"] = math.sqrt(2 * meta["cost0"] / r0.numel())
            meta["discrete_moments_start"] = source_moments(prob, model, zf)
            _ms = json.dumps({k: "%.2e" % v["ratio"] for k, v in meta["discrete_moments_start"].items()})
            log("  discrete source moments at the start (M/abs-sum): " + _ms)
            m0 = max(abs(v["ratio"]) for k, v in meta["discrete_moments_start"].items() if k.startswith("(0,"))
            if m0 > float(cfg.get("monopole_flag", 1e-13)):
                meta["monopole_flag"] = m0
                log(f"  MONOPOLE FLAG: |M_0|/abs-sum = {m0:.2e} > 1e-13 (SPEC 2.6): the source monopole is not realized at rounding level")
                if prob.exterior_monopole:                               # SPEC 2.6: the exterior form requires the rounding-level condition; stop the job with the flag
                    ledger.append(LEDGER, dict(kind="job_stopped", job_id=job_id, reason="monopole_flag", value=m0, label=label))
                    log("  JOB STOPPED: exterior_monopole is enabled and the rounding-level monopole condition fails (SPEC 2.6)")
                    hb.beat(force=True, phase="stopped_monopole_flag")
                    return 0
            meta["params0"] = pm.describe(z_opt) if model.free_params else dict(c_l=float(cfg["c_l"]), omega=float(cfg["omega"]))
            log(f"start {idx} meta={json.dumps({k: (round(v, 6) if isinstance(v, float) else v) for k, v in meta.items() if k not in ('relU_change_by_shell',)}, default=str)}")
        geometry_base = dict(prob.pressure.geometry_base) if prob.pressure is not None else None
        n_opt = z_opt.numel(); pidx = [n_opt - 2, n_opt - 1] if model.free_params else []
        gauge_rows = list(range(prob.row_blocks()[-1][1], prob.row_blocks()[-1][1] + 1))
        s2_step = cfg.get("step_jacobian", "J_cw")                                # STRATEGY 2: "J_cw" (production step model, hook off) or "J_c" (complete Jacobian step model)
        if s2_step not in ("J_cw", "J_c"):
            raise RuntimeError(f"step_jacobian {s2_step!r} is not 'J_cw' or 'J_c' (strategy-2 worker; V420: no silent fallback)")
        jac_mode = cfg.get("jacobian_mode", "weights_differentiated")           # D6FP: 'weights_differentiated' (production: the shell weights are part of the
        if jac_mode == "weights_differentiated":                                 # differentiated residual, closure target lagged) or 'frozen_weights' (IRLS model of the frozen code)
            fun = lambda zo: prob.residual_vector_wd(to_full(zo))
            pfun = (lambda zo: prob.residual_vector_wd(to_full(zo), differentiable_pressure=True)) if model.free_params else None
        else:
            fun = lambda zo: prob.residual_vector(to_full(zo))
            pfun = (lambda zo: prob.residual_vector(to_full(zo), differentiable_pressure=True)) if model.free_params else None
        r_box = dict(r=None)
        def objective(zo):                                                       # deliverable B (lead 23:51Z item 2): keep the residual of the last evaluated trial for the per-iteration block split
            r_, aux_ = prob.objective_at(to_full(zo)); r_box["r"] = r_
            return r_, aux_
        project = lambda zo: to_opt(prob.phase_align(to_full(zo)))
        phys = (lambda zo: pm.describe(zo)) if model.free_params else (lambda zo: dict(c_l=float(cfg["c_l"]), omega=float(cfg["omega"])))
        relayout = (lambda zo: (prob.ensure_geometry(to_full(zo)), dict(geometry=prob.pressure.geometry_id, base=prob.pressure.geometry_base))) if model.free_params else None
        grad_fun = (lambda zo: complete_gradient_opt(prob, pm, to_full, zo)) if cfg.get("complete_gradient", True) else None
        lin_every = int(cfg.get("linearization_every", 0) or 0)
        def jac_hook(it, zo, J, r, colnorm, aux, _box={"last": -1}):
            want = (it == 0) or (lin_every > 0 and it > 0 and it % lin_every == 0)
            if not want:
                return
            zf_ = to_full(zo)
            gen = phase_generator(model, zf_)
            gen_red = tc.reduce(gen) if tc is not None else gen
            if model.free_params:
                gen_red = gen_red.clone(); gen_red[-2:] = 0.0
            path = os.path.join(run_dir, f"linearization_{it0 + it:05d}.npz")
            t_ = time.time()
            if s2_step == "J_c":                                                    # STRATEGY 2 (V420): the hook receives the step Jacobian J_c: record it under its own kind and never correct it again
                linearization_record(path, it0 + it, J, r, colnorm, pidx, gauge_rows, gen_red, zo, phys(zo), 0.5 * float(r @ r), note="strategy-2 step Jacobian (in-loop J_c)",
                                     note_label="complete Jacobian J_c (pressure tables, weights and closure target and patterns differentiated; strategy-2 step model)", kind="J_c")
            else:
                linearization_record(path, it0 + it, J, r, colnorm, pidx, gauge_rows, gen_red, zo, phys(zo), 0.5 * float(r @ r))
            log(f"  linearization record {os.path.basename(path)} written ({time.time() - t_:.1f}s; kind {s2_step})")
            if s2_step == "J_cw" and cfg.get("linearization_complete_periodic", False) and lin_every > 0 and it > 0 and it % (lin_every * int(cfg.get("linearization_complete_every_n_records", 2))) == 0:   # default: the complete J_c record only at the end state (cost: 2 (2 Nq + 2) closure-target evaluations, several minutes)
                try:
                    t_ = time.time()
                    J_c, info = complete_jacobian_from_Jcw(prob, to_full, zo, J, pidx, pm=pm)
                    cn = (J_c * J_c).sum(0).clamp_min(1e-30).sqrt()
                    linearization_record(os.path.join(run_dir, f"linearization_{it0 + it:05d}_complete.npz"), it0 + it, J_c, r, cn, pidx, gauge_rows, gen_red, zo, phys(zo), 0.5 * float(r @ r),
                                         note=json.dumps(info), note_label="complete Jacobian J_c (pressure tables, weights and closure target and patterns differentiated)", kind="J_c")
                    del J_c
                    log(f"  complete linearization record written ({time.time() - t_:.1f}s; {info})")
                except Exception as e:
                    log(f"  complete linearization record failed: {e!r}")
        def s2_jac_post(J, zo, it):                                         # STRATEGY 2: the complete Jacobian J_c of the admitted EVAL path from the assembled J_cw (same function as the J_c records)
            t_ = time.time()
            J_c, info = complete_jacobian_from_Jcw(prob, to_full, zo, J, pidx, pm=pm)
            log(f"  STRATEGY 2: step Jacobian J_c from J_cw at it {it0 + it} ({time.time() - t_:.1f}s; {info})")
            if it == 0 and cfg.get("s2_smoke_save_Jc_it0", False):              # smoke record (1): the in-loop J_c at iteration 0 saved for the comparison with the EVAL record
                np.savez(os.path.join(run_dir, f"s2_Jc_it{it0 + it:05d}.npz"), J_c=J_c.detach().cpu().numpy(), z_opt=zo.detach().cpu().numpy(), it=it0 + it, info=json.dumps(info))
                log(f"  STRATEGY 2: in-loop J_c at it {it0 + it} saved (s2_Jc_it{it0 + it:05d}.npz)")
            return J_c
        cur_hist = []; box = dict(last_ck=time.time())
        def checkpoint(zo, it, lam_, force_phase=None):
            state["current"] = dict(idx=idx, z_opt=zo.detach().cpu(), z_full=to_full(zo).detach().cpu(), meta=meta, it=it, lam=lam_, history=hist + list(cur_hist), pivot=prob.pivot,
                                    geometry_base=geometry_base if prob.pressure is None else dict(prob.pressure.geometry_base), rng_state=rng.bit_generator.state, ts=now(),
                                    counters=(cur_hist[-1].get("counters") if cur_hist else counters0), grad_every=int(cfg.get("complete_gradient_every", 1) or 1),   # gpu_v1 (V161)
                                    rng_state_sha256=hashlib.sha256(json.dumps(rng.bit_generator.state, sort_keys=True, default=str).encode()).hexdigest(),
                                    z_opt_sha256=hashlib.sha256(zo.detach().cpu().numpy().tobytes()).hexdigest())
            atomic_save(state, ck_path); box["last_ck"] = time.time()
            if cfg.get("checkpoint_diagnostics", True):                          # deliverable B (lead 23:51Z item 2 (c)): holdout rho_u max on both shell families and sigma_u at every checkpoint
                try:
                    t_d0 = time.time(); zf_ = to_full(zo).detach()
                    if "H_std" not in box:
                        box["H_std"] = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)))
                        box["H_half"] = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)), edges=half_offset_edges(model.R0, float(model.r.max())))
                    g_s = spec_diagnostics(prob, zf_, holdout=box["H_std"], extras=False)["global_"]; g_h = spec_diagnostics(prob, zf_, holdout=box["H_half"], extras=False)["global_"]
                    meta.setdefault("checkpoint_diagnostics", []).append(dict(it=int(it), ts=now(), rho_u_max_std=g_s.get("rho_u_max"), rho_u_max_half=g_h.get("rho_u_max"),
                                                                              rho_nl_max_std=g_s.get("rho_nl_max"), rho_nl_max_half=g_h.get("rho_nl_max"), sigma_u_max_std=g_s.get("sigma_u_max"),
                                                                              sigma_u_max_half=g_h.get("sigma_u_max"), sigma_u_max_r1_std=g_s.get("sigma_u_max_r1"), t_s=time.time() - t_d0))
                    log(f"  checkpoint diagnostics at it {it}: rho_u max std {g_s.get('rho_u_max')} half {g_h.get('rho_u_max')} sigma_u {g_s.get('sigma_u_max')} ({time.time() - t_d0:.1f}s)")
                except Exception as e_:
                    log(f"  checkpoint diagnostics failed: {e_!r}")
        def cb(it, zo, cost, rec):
            rec["z_sha256_12"] = hashlib.sha256(zo.detach().cpu().numpy().tobytes()).hexdigest()[:12]
            rec["it_cum"] = it0 + it                                             # cumulative iteration index across resumes (deliverable B)
            if rec.get("accepted") and r_box.get("r") is not None:
                try:
                    rec["cost_blocks"] = cost_blocks_split(prob, model, r_box["r"])
                except Exception as e_:
                    rec["cost_blocks"] = dict(error=repr(e_)[:200])
            if model.free_params:
                p = rec.get("params") or {}
                for key in ("g_param_opt", "g_param_scaled"):
                    pass
                # physical gradient components of the frozen model (chain rule, SPEC 5.2): dO/dc_l = dO/dz_c / (dc_l/dz_c), with the chain
                # factors of the PRE-STEP point, where g = J^T r was formed (verifier V130); the complete gradient below uses the new point's factors
                pp = rec.get("params_prestep") or p
                if rec.get("g_param_opt") and pp.get("dcl_dzc"):
                    rec["g_param_phys"] = dict(c_l=rec["g_param_opt"][pidx[0]] / pp["dcl_dzc"], omega=rec["g_param_opt"][pidx[1]] / pp["domega_dzw"], chain_point="pre-step")
                if rec.get("complete_gradient") and rec["complete_gradient"].get("g_param_opt") and p.get("dcl_dzc"):
                    rec["complete_gradient"]["g_param_phys"] = dict(c_l=rec["complete_gradient"]["g_param_opt"][pidx[0]] / p["dcl_dzc"], omega=rec["complete_gradient"]["g_param_opt"][pidx[1]] / p["domega_dzw"])
            cur_hist.append(rec)
            hb.beat(start=idx, it=it0 + it, cost=cost, rms=rec["rms"], lam=rec["lam"], phase="lm", params=rec.get("params"))
            if time.time() - box["last_ck"] > CKPT_INTERVAL or STOP["flag"]:
                checkpoint(zo, it0 + it + 1, rec["lam"])
                log(f"  checkpoint at start {idx} it {it0 + it} ({'SIGTERM' if STOP['flag'] else 'periodic'})")
                if prob.exterior_monopole:                                # SPEC 2.6 per-evaluated-state condition (checked at every checkpoint)
                    mm = source_moments(prob, model, to_full(zo)); rec["discrete_moments"] = {k: v["ratio"] for k, v in mm.items()}
                    m0 = max(abs(v["ratio"]) for k, v in mm.items() if k.startswith("(0,"))
                    if m0 > float(cfg.get("monopole_flag", 1e-13)):
                        meta["monopole_flag"] = m0; meta["monopole_flag_it"] = it0 + it
                        log(f"  MONOPOLE FLAG at it {it0 + it}: |M_0|/abs-sum = {m0:.2e} > 1e-13 with the exterior form on: stopping (SPEC 2.6)")
                        ledger.append(LEDGER, dict(kind="job_stopped", job_id=job_id, reason="monopole_flag", value=m0, it=it0 + it, label=label))
                        STOP["flag"] = True
            if STOP["flag"]:
                raise KeyboardInterrupt
            return False
        t0 = time.time()
        time_limit = min(float(cfg.get("time_limit_per_start", 7200)), max(60.0, time_cap_job - (time.time() - t_job0)))
        log(f"  LM start: {n_opt} unknowns ({len(pidx)} free parameters), max_iter {int(cfg.get('max_iter', 300)) - it0}, time limit {time_limit:.0f}s, lam0 {lam:.2e}, chunk {int(cfg.get('chunk', 256))}, trust |dz_c|,|dz_w| <= {cfg.get('param_step_max', 0.5)}, Jacobian mode {jac_mode} (acceptance on the self-consistent O1), parameter-column Marquardt scaling from the PDE rows: {cfg.get('param_scale_pde_rows', True)}")
        try:
            out = lm_solve_free(fun, z_opt, param_fun=pfun, param_idx=pidx, objective=objective, commit=prob.commit_aux, project=project, phys=phys, relayout=relayout,
                                max_iter=max(0, int(cfg.get("max_iter", 300)) - it0), lam0=lam, chunk=int(cfg.get("chunk", 256)), callback=cb, log=log,
                                time_limit=time_limit, verbose=True, ftol=float(cfg.get("ftol", 1e-7)), xtol=float(cfg.get("xtol", 1e-12)),
                                param_step_max=({pidx[0]: float(cfg.get("param_step_max", 0.5)), pidx[1]: float(cfg.get("param_step_max", 0.5))} if pidx else None),
                                grad_fun=grad_fun, jac_hook=(jac_hook if cfg.get("linearization", True) else None),
                                saturation=((lambda zo: pm.saturation_flag(zo)) if model.free_params else None), log_every=int(cfg.get("log_every", 1)),
                                param_scale_rows=(prob.n_pde_residuals() if cfg.get("param_scale_pde_rows", True) else None),
                                lag_jacobian=(dict(max_reuse=int(cfg.get("lagJ_max_reuse", 8)), rho_min=float(cfg.get("lagJ_rho_min", 0.25))) if cfg.get("lag_jacobian", False) else None),   # lead 01:11Z R2 (off until adopted)
                                grad_every=int(cfg.get("complete_gradient_every", 1) or 1),   # lead R5 (2026-10-29): complete gradient at fresh-J steps and every N accepted steps
                                counters=counters0, project_start=(not resumed_from_checkpoint),   # gpu_v1 patch 1: no entry projection of ANY resumed vector (lead 05:23Z item 1; V161, V162)
                                jac_post=(s2_jac_post if s2_step == "J_c" else None))   # STRATEGY 2 (lead 18:31:20Z item 4 (i)): step model J_c when the configuration says so
        except KeyboardInterrupt:
            log("interrupted by SIGTERM; checkpoint written"); state.setdefault("interruptions", []).append(dict(ts=now(), event="sigterm", it=it0 + len(cur_hist)))
            atomic_save(state, ck_path)
            break
        z_opt = out["z"]; hist = hist + out["history"]; elapsed = time.time() - t0
        zf = to_full(z_opt)
        try:                                                                           # gpu_v1 patch 1: end-of-segment checkpoint (same fields as the periodic one) for a continuation job
            seg_state = dict(state); seg_state["current"] = dict(idx=idx, z_opt=z_opt.detach().cpu(), z_full=zf.detach().cpu(), meta=meta, it=it0 + len(out["history"]), lam=out["lam"], history=hist, pivot=prob.pivot,
                                                                 geometry_base=geometry_base if prob.pressure is None else dict(prob.pressure.geometry_base), rng_state=rng.bit_generator.state, ts=now(),
                                                                 counters=out.get("counters"), grad_every=int(cfg.get("complete_gradient_every", 1) or 1),
                                                                 rng_state_sha256=hashlib.sha256(json.dumps(rng.bit_generator.state, sort_keys=True, default=str).encode()).hexdigest(),
                                                                 z_opt_sha256=hashlib.sha256(z_opt.detach().cpu().numpy().tobytes()).hexdigest(), lm_status=out["status"])
            atomic_save(seg_state, os.path.join(run_dir, "checkpoint_segment_end.pt"))
            ledger.append(LEDGER, dict(kind="segment_end", job_id=job_id, it=it0 + len(out["history"]), status=out["status"], counters=out.get("counters"), lam=out["lam"], cost=out["cost"], elapsed_lm_s=elapsed, label=label))
            log(f"  end-of-segment checkpoint written (it {it0 + len(out['history'])}, status {out['status']}, counters {out.get('counters')}); a continuation job (cfg continue_from_run) resumes from it")
        except Exception as e:
            log(f"  end-of-segment checkpoint failed: {e!r}")
        if model.free_params and cfg.get("linearization", True):
            try:                                                                       # final linearization record at the end state
                J = None
                from src.optimization.lm import jacobian_fwd, param_columns
                r_end, aux_end = prob.objective_at(zf); prob.commit_aux(aux_end)
                J = jacobian_fwd(fun, z_opt, chunk=int(cfg.get("chunk", 256))); Jp = param_columns(pfun, z_opt, pidx)
                for j, k in enumerate(pidx):
                    J[:, k] = Jp[:, j]
                colnorm = (J * J).sum(0).clamp_min(1e-30).sqrt()
                gen = phase_generator(model, zf); gen_red = tc.reduce(gen) if tc is not None else gen; gen_red = gen_red.clone(); gen_red[-2:] = 0.0
                linearization_record(os.path.join(run_dir, f"linearization_{it0 + len(out['history']):05d}_final.npz"), it0 + len(out["history"]), J, r_end, colnorm, pidx, gauge_rows, gen_red, z_opt, phys(z_opt), 0.5 * float(r_end @ r_end), note="end state")
                if cfg.get("linearization_complete", False):             # default OFF (about 20 min per record under GPU sharing); J_c records on demand (scripts/jc_record.py, Phase III)
                    J_c, info = complete_jacobian_from_Jcw(prob, to_full, z_opt, J, pidx, pm=pm)
                    cn = (J_c * J_c).sum(0).clamp_min(1e-30).sqrt()
                    linearization_record(os.path.join(run_dir, f"linearization_{it0 + len(out['history']):05d}_final_complete.npz"), it0 + len(out["history"]), J_c, r_end, cn, pidx, gauge_rows, gen_red, z_opt, phys(z_opt), 0.5 * float(r_end @ r_end),
                                         note="end state; " + json.dumps(info), note_label="complete Jacobian J_c (pressure tables, weights and closure target and patterns differentiated)", kind="J_c")
                    del J_c
                del J, Jp
                log("  final linearization record(s) written" + (" (J_cw and J_c)" if cfg.get("linearization_complete", False) else " (J_cw)"))
            except Exception as e:
                log(f"  final linearization record failed: {e!r}")
        # exact F-gauge projection of the reported state (as the frozen worker)
        gauge_defect_opt, _ = prob.gauge_defects(zf)
        z = zf.clone()
        aT_, aS_, c_l_, om_ = model.unpack(z)
        nF = prob.tail_norm2(aT_, aS_, c_l_, om_).clamp_min(1e-300).sqrt()
        if torch.isfinite(nF) and nF > 1e-8:
            z[: model.n_coef] = z[: model.n_coef] / nF
        torch.cuda.synchronize() if device != "cpu" else None
        peak = torch.cuda.max_memory_allocated() / 2 ** 30 if device != "cpu" else 0.0
        JOB_PEAK[0] = max(JOB_PEAK[0], peak)
        p_final = pm.describe(z_opt) if model.free_params else dict(c_l=float(cfg["c_l"]), omega=float(cfg["omega"]))
        try:
            moments_end = source_moments(prob, model, zf); log("  discrete source moments at the end (M/abs-sum): " + json.dumps({k: "%.2e" % v["ratio"] for k, v in moments_end.items()}))
        except Exception as e:
            moments_end = dict(error=repr(e))
        rejections = [rj for h in out["history"] for rj in h.get("rejections", [])]
        reasons = {}
        for rj in rejections:
            reasons[rj["reason"]] = reasons.get(rj["reason"], 0) + 1
        traj = [dict(it=h["it"], cost=h["cost"], accepted=h["accepted"], c_l=(h.get("params") or {}).get("c_l"), omega=(h.get("params") or {}).get("omega"),
                     gD_inf_over_r=h.get("gD_inf_over_r"), g_param_scaled=h.get("g_param_scaled"), lam=h["lam"], complete_gradient=h.get("complete_gradient"), layout_change=h.get("layout_change"), t_iter=h.get("t_iter"),
                     it_cum=h.get("it_cum"), cost_blocks=h.get("cost_blocks"), n_trials=h.get("n_trials"), J_age=h.get("J_age"), rho=h.get("rho"),
                     gD_scaling=h.get("gD_scaling"), g_param_phys=h.get("g_param_phys"), params_prestep=h.get("params_prestep"), t_jac_post=h.get("t_jac_post"), step_jacobian=s2_step) for h in hist]      # V130: scaling label and pre-step chain factors kept      # deliverable B: cumulative index and cost split by row block per accepted iteration
        extra_rec = dict(step_jacobian=s2_step, strategy2_worker=True, label=label, d6fp_solver=SOLVER_VERSION, params_initial=meta.get("params0"), params_final=p_final, cost_initial=meta.get("cost0"), cost_final=out["cost"],
                         spec_version=cfg.get("spec_version"), spec_sha256=cfg.get("spec_sha256"), release_battery=cfg.get("release_battery"), lag_jacobian=bool(cfg.get("lag_jacobian", False)),
                         precision_mode=getattr(prob, "precision_mode", "fp64"), jacobian_precision=("fp64" if getattr(prob, "precision_mode", "fp64") in ("fp64", "dd_fp64tangent", "dd_fp64jac") else "dd"),
                         residual_precision=("dd" if getattr(prob, "precision_mode", "fp64") != "fp64" else "fp64"),
                         checkpoint_diagnostics=meta.get("checkpoint_diagnostics"), cost_blocks_final=(cost_blocks_split(prob, model, r_box["r"]) if r_box.get("r") is not None else None),
                         n_accepted=out["n_accepted"], n_rejected=out["n_rejected"], rejection_reasons=reasons, stop_reason=out["status"], lm_seconds=elapsed,
                         gpu_peak_GB_lm=peak, geometry_base=dict(prob.pressure.geometry_base) if prob.pressure is not None else None, geometry_id=prob.pressure.geometry_id if prob.pressure is not None else None,
                         layout_changes=[h["layout_change"] for h in hist if h.get("layout_change")], saturation_stop=(out["status"] == "saturation"),
                         near_edge=(min(p_final["c_l"] - 0.4, 0.5 - p_final["c_l"]) < 0.02), free_params=bool(model.free_params), param_map="c_l = 0.4 + 0.1 sigmoid(z_c), omega = exp(z_w)" if model.free_params else None,
                         start_sha256=meta.get("source_sha256"), start_path=meta.get("source"), init_meta={k: v for k, v in meta.items() if k not in ("relU_change_by_shell", "pivot")},
                         discrete_moments_start=meta.get("discrete_moments_start"), discrete_moments_end=moments_end, monopole_flag=meta.get("monopole_flag"),
                         angular_table_paths=_table_paths(),
                         trajectory=traj, interruptions=state.get("interruptions", []), cpu_affinity=sorted(os.sched_getaffinity(0)), host=platform.node(), rss_peak_GB=(_rss_peak()))
        log(f"  LM finished: {out['status']} after {len(out['history'])} iterations ({out['n_accepted']} accepted, {out['n_rejected']} rejected trials {reasons}), cost {meta.get('cost0', float('nan')):.6e} -> {out['cost']:.6e}; params {json.dumps(p_final)}; peak GPU {peak:.1f} GB")
        hb.beat(force=True, start=idx, phase="battery")
        try:
            rec, zpath, holdout = finish_start(prob, model, z, cfg, log, hb, idx, holdout, device, JOB_PEAK, meta, out, hist, elapsed, rng_seed, tc, CODE_VERSIONS, job_id, run_dir, peig, gauge_defect_opt, extra_rec)
        except Exception as e:
            log(f"  BATTERY FAILED: {e!r}\n{traceback.format_exc()[-3000:]}")
            zpath = os.path.join(run_dir, "starts", f"start_{idx:03d}_nobattery.pt")
            atomic_save(dict(z=z.detach().cpu(), z_opt=z_opt.detach().cpu(), config=cfg, meta=meta, history=hist, status=out["status"], lam=out["lam"], free_params=model.free_params, modes=model.modes, pivot=prob.pivot, d6fp=extra_rec, battery_error=repr(e)), zpath)
            rec = dict(kind="start_result", job_id=job_id, start=idx, failure="battery_error", error=repr(e)[:500], zfile=os.path.relpath(zpath, ROOT), **{k: v for k, v in extra_rec.items() if k != "trajectory"})
            ledger.append(LEDGER, rec)
        state["completed"].append(dict(idx=idx, status=out["status"], zfile=zpath, cost_final=out["cost"], params_final=p_final))
        state["current"] = None
        atomic_save(state, ck_path)
        hb.beat(force=True, start=idx, phase="start_done")
    done = len(state["completed"]) >= n_starts
    state["finished"] = now() if done else None
    state["elapsed_job_seconds"] = state.get("elapsed_job_seconds", 0.0) + (time.time() - t_job0)
    atomic_save(state, ck_path)
    ledger.append(LEDGER, dict(kind="job_end", job_id=job_id, done=done, completed=len(state["completed"]), elapsed_job_seconds=state["elapsed_job_seconds"],
                               gpu_peak_mem_GB=(max(torch.cuda.max_memory_allocated() / 2 ** 30, JOB_PEAK[0]) if device != "cpu" else 0.0), label=label))
    hb.beat(force=True, phase="done" if done else "interrupted")
    log(f"JOB {'DONE' if done else 'INTERRUPTED'} ({len(state['completed'])}/{n_starts} starts, {state['elapsed_job_seconds']:.0f}s total)")
    return 0 if done else 3


def _table_paths():
    """angular-table path usage of this process (lead 22:35Z item 1 (c)): counts per path and the distinct call sites."""
    try:
        from src.bases.solid_harmonics import path_summary
        return path_summary()
    except Exception as e:
        return dict(error=repr(e))


def _rss_peak():
    try:
        import resource
        return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20
    except Exception:
        return None


if __name__ == "__main__":
    try:
        rc = run_job(sys.argv[1], sys.argv[2])
    except Exception as e:
        traceback.print_exc()
        try:
            ledger.append(LEDGER, dict(kind="job_error", job=sys.argv[1], error=repr(e), trace=traceback.format_exc()[-2000:]))
        except Exception:
            pass
        rc = 1
    sys.exit(rc)
