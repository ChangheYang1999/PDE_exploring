#!/usr/bin/env python
"""Campaign worker: runs one job file (multistart / refine) on one GPU with heartbeats, periodic atomic
checkpoints (every <= 15 min and after every start), resume from checkpoint, and ledger records.
Usage: worker.py <job.json> <run_dir>   (CUDA_VISIBLE_DEVICES set by the supervisor to one physical GPU)."""
import sys, os, json, time, hashlib, math, signal, traceback, platform
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")   # 2026-10-25T13:06Z: the Nk 32 and both-formulation OOMs showed 15-21 GB reserved-but-unallocated (fragmentation); must precede the torch import
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model, alpha_of
from src.optimization.problem import Problem
from src.optimization.lm import lm_solve, lbfgs_solve
from src.validation.spec_diagnostics import spec_diagnostics, tier_S
from src.validation.holdout import HoldoutGrid, half_offset_edges, sphere_diagnostics, exchange_radii, two_family_summary, summary_text, structure_text
from src.validation.critical_points import local_maxima_omega, zeros_of_W
from src.validation.strength import strength_diagnostics
from src.optimization.tail_constraints import TailConstraints
from src.far_field.eigen import min_pressure_eigenvalue
from src.optimization.seeds import make_seed
from src.validation.diagnostics import candidate_diagnostics, summary_line
from src.campaign import ledger
from src.campaign.checkpoint import atomic_save, atomic_write_text

LEDGER = os.path.join(ROOT, "status", "ledger.jsonl")
SOLVER_VERSION = "v5-2026-10-24T21:05Z"   # v1: plain LS (s1a); v2: nlw un-normalized + gauge norm fix (collapsed, 18:53-19:09Z); v3: nlw mean-normalized, gauge row ||F||-1, holdout, critical points;
# v4: phase gauge by exact rotation projection (no row), dilation row weight 100 + final exact projection, constraint rows absolute weights, merged far nodes;
# v5: Green panels split at evaluation radii, PDE-row Marquardt scaling, rebuilt-pressure FD parameter columns, optional exact alpha+1/alpha+2 tail-moment constraints
CKPT_INTERVAL = 14 * 60
STOP = {"flag": False}


def _sigterm(signum, frame):
    STOP["flag"] = True


signal.signal(signal.SIGTERM, _sigterm)
signal.signal(signal.SIGINT, _sigterm)


class Heartbeat:
    def __init__(self, path, job_id):
        self.path, self.job_id, self.t = path, job_id, 0.0

    def beat(self, **info):
        now = time.time()
        if now - self.t < 20 and not info.get("force"):
            return
        self.t = now
        rec = dict(job_id=self.job_id, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), epoch=now, pid=os.getpid(), host=platform.node())
        rec.update({k: v for k, v in info.items() if k != "force"})
        atomic_write_text(json.dumps(rec), self.path)


def build(cfg, device):
    model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0),
                  Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"], free_params=cfg.get("free_params", False), device=device,
                  channels=cfg.get("channels"), extra_r=(cfg.get("far_radii") if cfg.get("far_merged", True) else None))
    prob = Problem(model, formulation=cfg.get("formulation", "vort"), gauge_weight=cfg.get("gauge_weight", 100.0),
                   both_weight=cfg.get("both_weight", 1.0), nl_weighting=bool(cfg.get("nl_weighting", False)),
                   efrac=cfg.get("efrac"), efrac_weight=cfg.get("efrac_weight", 100.0),
                   gauge=cfg.get("gauge", "F"), Z_star=cfg.get("Z_star", 1.0), sigmaZ=cfg.get("sigmaZ"), sigmaZ_weight=cfg.get("sigmaZ_weight", 100.0),
                   far_radii=cfg.get("far_radii"), far_weight=cfg.get("far_weight", 1.0),
                   sigmaZ_fine=int(cfg.get("sigmaZ_fine", 4)), sigmaZ_ramp_iters=int(cfg.get("sigmaZ_ramp_iters", 0)),
                   nl_denominator=cfg.get("nl_denominator", "nl"), far_lambda=float(cfg.get("far_lambda", 1e-2)), closure_lambda=float(cfg.get("closure_lambda", 0.0)),
                   fsw=cfg.get("fsw"), fsw_weight=float(cfg.get("fsw_weight", 100.0)),
                   nu=float(cfg.get("nu", 0.0) or 0.0), pin_c_l=cfg.get("pin_c_l"), pin_weight=float(cfg.get("pin_weight", 100.0)),
                   balance_lambda=float(cfg.get("balance_lambda", 0.0) or 0.0), core_pin=cfg.get("core_pin"), core_pin_weight=float(cfg.get("core_pin_weight", 100.0)),
                   nonaxi_pin=(cfg.get("nonaxi_pin") if isinstance(cfg.get("nonaxi_pin"), (list, tuple)) else None), nonaxi_pin_weight=float(cfg.get("nonaxi_pin_weight", 100.0)),
                   radial_lambda_w=float(cfg.get("radial_lambda_w", 0.0) or 0.0))
    return model, prob


def code_versions():
    """sha256 (first 12 hex digits) and mtime of the solver source files this worker imported (lead 2026-10-25T16:25Z: record the lm.py
    version each job ran); logged at START and stored in every start_result / lm_only_result record."""
    import hashlib
    out = {}
    for rel in ("src/optimization/lm.py", "scripts/worker.py", "src/optimization/problem.py", "src/equations/fields.py", "src/pressure/poisson_sh.py", "src/equations/residuals.py", "src/far_field/correction.py", "src/validation/spec_diagnostics.py", "src/pressure/ray_integral.py"):   # lead 19:22Z: the pressure solver hash in every ledger entry; 21:58Z: the battery (stored shell ratios, ray check) too
        fp = os.path.join(ROOT, rel)
        try:
            h = hashlib.sha256(open(fp, "rb").read()).hexdigest()[:12]
            out[rel] = dict(sha256_12=h, mtime=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(os.path.getmtime(fp))))
        except Exception as e:
            out[rel] = dict(error=repr(e))
    return out


def run_job(job_path, run_dir):
    job = json.load(open(job_path))
    cfg = job["config"]; job_id = job["job_id"]
    os.makedirs(run_dir, exist_ok=True); os.makedirs(os.path.join(run_dir, "starts"), exist_ok=True)
    logf = open(os.path.join(run_dir, "worker.log"), "a")
    def log(msg):
        line = f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} {msg}"
        logf.write(line + "\n"); logf.flush(); print(line, flush=True)
    hb = Heartbeat(os.path.join(ROOT, "status", f"heartbeat_{job_id}.json"), job_id)
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    if device != "cpu" and cfg.get("gpu_mem_fraction"):
        torch.cuda.set_per_process_memory_fraction(float(cfg["gpu_mem_fraction"]), 0)
    torch.set_num_threads(int(cfg.get("threads", 1)))
    t_job0 = time.time()
    global CKPT_INTERVAL
    CKPT_INTERVAL = float(cfg.get("ckpt_interval_s", CKPT_INTERVAL))
    ck_path = os.path.join(run_dir, "checkpoint.pt")
    state = dict(job_id=job_id, config=cfg, completed=[], current=None, started=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                 versions=dict(torch=torch.__version__, numpy=np.__version__, python=sys.version.split()[0]),
                 gpu=torch.cuda.get_device_name(0) if device != "cpu" else "cpu", resumed=0)
    if os.path.exists(ck_path):
        state = torch.load(ck_path, map_location="cpu", weights_only=False)
        state["resumed"] = state.get("resumed", 0) + 1
        log(f"RESUME from checkpoint: {len(state['completed'])} starts completed, current={None if state['current'] is None else state['current']['idx']}, resumed {state['resumed']}x")
        ledger.append(LEDGER, dict(kind="resume", job_id=job_id, completed=len(state["completed"]), resumed=state["resumed"]))
    cmark = os.path.join(ROOT, "queue", "cancel", job_id)
    if os.path.exists(cmark):                      # operator cancel marker (2026-10-25T16:12Z): no computation, exit 0 so that the supervisor files the job under done/ (move it to cancelled/ by hand)
        log(f"CANCELLED at launch: marker {cmark} found; no computation (the supervisor files the job as done; move it to queue/cancelled)")
        ledger.append(LEDGER, dict(kind="job_cancelled", job_id=job_id, marker=cmark, retries=job.get("retries", 0)))
        hb.beat(force=True, phase="cancelled")
        return 0
    log(f"START job {job_id} on {device} ({state['gpu']}) cfg={json.dumps(cfg)}")
    CODE_VERSIONS = code_versions()
    log("CODE VERSIONS (sha256[:12], mtime): " + ", ".join(f"{k} {v.get('sha256_12')} {v.get('mtime')}" for k, v in CODE_VERSIONS.items()))
    ledger.append(LEDGER, dict(kind="job_code_versions", job_id=job_id, retries=job.get("retries", 0), code_versions=CODE_VERSIONS))
    model, prob = build(cfg, device)
    if cfg.get("nonaxi_r_tail") is not None:            # S9d (verifier rule via the lead 17:49Z): the e_core shell-set cutoff frozen from Z0 for numeric pins
        prob.nonaxi_r_tail = float(cfg["nonaxi_r_tail"])
    tc = TailConstraints(model, nu=float(cfg.get("nu", 0.0) or 0.0)) if cfg.get("tail_constraints", False) else None     # exact alpha+1, alpha+2 tail-moment cancellation (S8: inhomogeneous alpha+2 moment for nu > 0)
    if float(cfg.get("nu", 0.0) or 0.0) > 0:
        log(f"S8 ARTIFICIAL VISCOSITY nu = {float(cfg['nu']):.4e}: every state of this job is a viscous continuation state, never an Euler candidate (R^nu = R_u - nu Delta U; tail constraints inhomogeneous at rate alpha+2; c_l pin {cfg.get('pin_c_l')})")
    if tc is not None:
        log(f"tail constraints on: {model.n_z} -> {tc.n_red} unknowns (top two Chebyshev coefficients per A/C column eliminated)")
    hb.beat(force=True, phase="build", n_z=model.n_z, n_res=prob.n_pde_residuals())
    log(f"model: Nq={model.Nq} Nk={model.Nk} Nr={model.Nr} Na={model.Na} n_z={model.n_z} n_res={prob.n_pde_residuals()}")
    peig = min_pressure_eigenvalue(cfg["c_l"], cfg["omega"], cfg["L"], cfg.get("m_parity", "even"))
    log(f"smallest pressure eigenvalue modulus (SPEC 3.4) at c_l={cfg['c_l']}, omega={cfg['omega']}: {peig['min_abs']:.4f} at (l,m)=({peig['l']},{peig['m']})")
    JOB_PEAK = [0.0]                                     # whole-job allocated peak (GB) across the LM and every battery item (the per-item instrumentation resets torch's peak counter)
    n_starts = int(cfg.get("n_starts", 1))
    holdout = None   # built lazily once per job (fixed R0-relative shells, so the holdout pressure kernels are reused)
    families = cfg.get("families", ["random", "tail", "nonaxi", "poloidal", "toroidal"])
    last_ck = time.time()
    for idx in range(n_starts):
        if idx in [c["idx"] for c in state["completed"]]:
            continue
        if STOP["flag"]:
            break
        rng_seed = int(cfg.get("seed", 0)) * 1000003 + idx
        rng = np.random.default_rng(rng_seed)
        fam = families[idx % len(families)]
        cur = state["current"]
        if cur is not None and cur["idx"] == idx:
            z = cur["z"].to(device); meta = cur["meta"]; it0 = cur["it"]; lam = cur["lam"]; hist = cur["history"]; prob.pivot = cur["pivot"]
            if cfg.get("init_from"):
                pass
            log(f"start {idx}: resuming at iteration {it0}")
            prob.maybe_rebuild_pressure(z); prob.set_sigmaZ_ramp(z); prob.update_nl_weights(z); prob.update_closure(z)
            if prob.sigmaZ is not None and prob.sigmaZ_ramp_iters > 0:
                log(f"  Sigma_Z continuation (resumed): start value {prob.sigmaZ:.4f} -> target {prob.sigmaZ_target_final} over {prob.sigmaZ_ramp_iters} accepted iterations")
        else:
            if cfg.get("init_from"):
                from src.optimization.transfer import embed_state
                src = torch.load(cfg["init_from"], map_location="cpu", weights_only=False)
                scfg = src["config"]
                msrc = Model(L=scfg["L"], Nk=scfg["Nk"], m_parity=scfg.get("m_parity", "even"), R0=scfg.get("R0", 1.0), Nr=scfg.get("Nr"),
                             c_l=scfg["c_l"], omega=scfg["omega"], free_params=src.get("free_params", False), channels=scfg.get("channels"), device=device)
                z = embed_state(src["z"].to(device), msrc, model)          # exact embedding into this (possibly larger) basis
                meta = dict(family="init_from", source=cfg["init_from"], source_L=scfg["L"], source_Nk=scfg["Nk"], source_rho_u=(src.get("spec_diag_holdout") or src.get("spec_diag") or {}).get("global_", {}).get("rho_u_max"),
                            max_U_start=((src.get("spec_diag_holdout") or src.get("spec_diag") or {}).get("guards") or {}).get("N4_max_U"),
                            source_rho_u_half=(src.get("two_family") or {}).get("rho_u_max_half"), source_rho_nl=(src.get("spec_diag_holdout") or {}).get("global_", {}).get("rho_nl_max"),
                            source_sphere_rho_u=(src.get("two_family") or {}).get("sphere_rho_u_max"))
                z_parent_embedded = z.clone()
                if cfg.get("perturb", 0) > 0:
                    z = z + cfg["perturb"] * torch.randn_like(z) * z.abs().mean()
                    meta["perturb"] = cfg["perturb"]
                if cfg.get("boost_e_core", None) is not None:
                    # Stage II S7 (b)/(c) eddy seeding: scale every m != 0 coefficient (all channels) by s so that the core eddy energy fraction
                    # e_core = RMS(U - <U>_phi)^2 / RMS(U)^2 reaches the target (orthogonal energies: e(s) = s^2 e0 / (1 - e0 + s^2 e0));
                    # e0 from the source's holdout diagnostics (nonaxi.e_core), else from the training diagnostics
                    e0 = ((src.get("spec_diag_holdout") or src.get("spec_diag") or {}).get("nonaxi") or {}).get("e_core")
                    tgt = float(cfg["boost_e_core"])
                    if e0 is not None and 0 < e0 < 1 and 0 < tgt < 1:
                        sfac = math.sqrt(tgt * (1 - e0) / (e0 * (1 - tgt)))
                        dd = model.unpack_all(z); mm = (model.m_arr != 0).to(torch.float64)
                        extra = {k: dd[k] * (1 + (sfac - 1) * mm[None, :]) for k in ("B", "D", "E") if dd[k].numel() > 0}
                        z = model.pack(dd["A"] * (1 + (sfac - 1) * mm[None, :]), dd["C"] * (1 + (sfac - 1) * mm[None, :]), dd["c_l"], dd["omega"], extra=extra)
                        meta["boost_e_core"] = tgt; meta["boost_factor"] = sfac; meta["boost_e_core_source"] = e0
                        log(f"  S7 eddy seeding: m != 0 coefficients scaled by {sfac:.3f} (source core eddy fraction {e0:.4f} -> target {tgt})")
                    else:
                        log(f"  S7 eddy seeding skipped: source e_core {e0}, target {tgt}")
                if cfg.get("perturb_m", None) is not None and cfg.get("perturb_m_rel", 0) > 0:
                    # odd-m test (lead 23:06Z item 3): add a random perturbation on the modes with m = perturb_m only (A and C channels),
                    # of relative size perturb_m_rel * ||z|| (coefficient norm), so that an m = 1 component of controlled size enters
                    dz = torch.zeros_like(z); dd = model.unpack_all(torch.randn_like(z))
                    mm = model.m_arr == int(cfg["perturb_m"])
                    pa = dd["A"] * mm[None, :].to(torch.float64); pc = dd["C"] * mm[None, :].to(torch.float64)
                    dz = model.pack(pa, pc, dd["c_l"], dd["omega"]) if not model.free_params else torch.cat([model.pack(pa, pc, dd["c_l"], dd["omega"])[:-2], torch.zeros(2, dtype=torch.float64, device=z.device)])
                    # FIELD-relative scaling (coefficient norms are not field norms in this ill-conditioned basis: a 1e-2 coefficient-relative
                    # perturbation gave a cost of 8.7e2 on 2026-10-25T01:06Z): ||U_pert||/||U|| = perturb_m_rel on the training grid
                    with torch.no_grad():
                        U0n = model.fields_grid(z, need_vort=False)["U"].norm(); Upn = model.fields_grid(dz, need_vort=False)["U"].norm()
                    dz = dz * (cfg["perturb_m_rel"] * U0n / Upn.clamp_min(1e-300))
                    z = z + dz
                    meta["perturb_m"] = int(cfg["perturb_m"]); meta["perturb_m_rel"] = cfg["perturb_m_rel"]; meta["perturb_m_field_rel"] = float(cfg["perturb_m_rel"])
                    log(f"  odd-m perturbation: m = {int(cfg['perturb_m'])} modes, field-relative size {cfg['perturb_m_rel']:.1e} (||U_pert||/||U|| on the training grid)")
            else:
                z, meta = make_seed(prob, fam, rng, cfg["c_l"], cfg["omega"], cfg.get("seed_params"))
            prob.pivot = prob.choose_pivot(z)
            it0 = 0; lam = cfg.get("lam0", 1e-2); hist = []
            prob.maybe_rebuild_pressure(z); prob.set_sigmaZ_ramp(z); prob.update_nl_weights(z); prob.update_closure(z)
            if prob.sigmaZ is not None and prob.sigmaZ_ramp_iters > 0:
                log(f"  Sigma_Z continuation: start value {prob.sigmaZ:.4f} -> target {prob.sigmaZ_target_final} over {prob.sigmaZ_ramp_iters} accepted iterations (fine grid Nr={prob.fine_model.Nr if prob.fine_model is not None else model.Nr_src})")
            r0 = prob.residual_vector(z)
            meta["cost0"] = 0.5 * float(r0 @ r0); meta["rms0"] = math.sqrt(2 * meta["cost0"] / r0.numel())
            log(f"start {idx} family={fam} meta={json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in meta.items()})}")
        t0 = time.time()
        # "projected warm start" bookkeeping (lead 21:16Z item 2): with tail constraints the reduce/expand projection changes the
        # parent state; record the relative change of U on the holdout grid and of each cost block at iteration 0
        if tc is not None and cfg.get("init_from") and 'z_parent_embedded' in dir():
            try:
                zp = tc.expand(tc.reduce(z_parent_embedded))
                if holdout is None:
                    holdout = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)))
                Up = holdout.model.fields_grid(z_parent_embedded, need_vort=False)['U']; Uz = holdout.model.fields_grid(zp, need_vort=False)['U']
                relU = ((Uz - Up).norm() / Up.norm()).item()
                rp = prob.residual_vector(z_parent_embedded); rz = prob.residual_vector(zp); npde = prob.n_pde_residuals()
                meta.update(projected_warm_start=True, relU_change_holdout=relU,
                            cost_blocks_parent=dict(pde=0.5 * (rp[:npde] @ rp[:npde]).item(), gauge=0.5 * (rp[npde:] @ rp[npde:]).item()),
                            cost_blocks_projected=dict(pde=0.5 * (rz[:npde] @ rz[:npde]).item(), gauge=0.5 * (rz[npde:] @ rz[npde:]).item()))
                log(f"  projected warm start: relative change of U on the holdout grid {relU:.3e}; cost blocks parent pde {meta['cost_blocks_parent']['pde']:.3e} gauge {meta['cost_blocks_parent']['gauge']:.3e} -> projected pde {meta['cost_blocks_projected']['pde']:.3e} gauge {meta['cost_blocks_projected']['gauge']:.3e}")
            except Exception as e:
                log(f"  projected warm start bookkeeping failed: {e!r}")
        bounds = None
        if model.free_params:
            lo = torch.full((model.n_z,), -float("inf"), device=device); hi = torch.full((model.n_z,), float("inf"), device=device)
            lo[-2], hi[-2] = cfg.get("c_l_min", 0.401), cfg.get("c_l_max", 0.499)
            if cfg.get("omega_min") is not None: lo[-1] = cfg["omega_min"]
            if cfg.get("omega_max") is not None: hi[-1] = cfg["omega_max"]
            bounds = (lo, hi)
        box = dict(last_ck=last_ck); cur_hist = []
        # Safeguarded lagged-target refresh (lead d128 CV item 4, 2026-10-26; default OFF: refresh_block 0 keeps the refresh after every accepted step).
        # With refresh_block = N > 0: the closure target G_required[F] and the nonlinear weights are FROZEN during blocks of N accepted iterations (the weights stay
        # at their Z0 reference values for the whole run); at a block boundary the target is refreshed from the current state and the merit function
        # (the cost of the refreshed objective with the reference weights) is compared with the merit at the previous boundary; with refresh_backtrack the state is
        # restored to the previous boundary when the merit rose, and the Marquardt damping is restarted conservatively (max(lam, lam0), x10 after a backtrack).
        sg = dict(block=int(cfg.get("refresh_block", 0) or 0), backtrack=bool(cfg.get("refresh_backtrack", False)), lam0=float(cfg.get("lam0", 1e-2) or 1e-2),
                  n_acc=0, merit_prev=None, z_prev=None, events=[])
        if sg["block"] > 0:
            log(f"SAFEGUARDED REFRESH (lead d128 CV 4): closure target and nonlinear weights frozen for blocks of {sg['block']} accepted iterations; merit function with fresh "
                f"G_required and the Z0 reference weights at block boundaries; backtrack {'ON' if sg['backtrack'] else 'OFF'}; damping restart to max(lam, {sg['lam0']:g}) at a refresh, x10 after a backtrack")

        def merit_of(zc, blocks=False):
            with torch.no_grad():
                rr = prob.residual_vector(zc)
                tot = 0.5 * float(rr @ rr)
                if not blocks:
                    return tot
                cr = prob.closure_rows(zc) if prob.closure is not None else None
                ccl = 0.5 * float(cr @ cr) if cr is not None else 0.0
            return tot, ccl

        def cb(it, zc, cost, rec):
            try:                                                   # 2026-10-25T22:17Z (T11 literal criterion): hash of the full iterate, so a resumed run's post-kill iterates can be compared with an uninterrupted run's
                rec["z_sha256_12"] = hashlib.sha256(zc.detach().cpu().numpy().tobytes()).hexdigest()[:12]
                if cfg.get("save_iterates"):                   # disposable T11 tests only: keep every full iterate (n_z doubles per iteration)
                    rec["z_iter"] = zc.detach().cpu().clone()
            except Exception:
                pass
            cur_hist.append(rec)
            hb.beat(start=idx, it=it0 + it, cost=cost, rms=rec["rms"], lam=rec["lam"], phase="lm")
            changed = False
            lam_new = None
            if rec.get("accepted", True) and sg["block"] > 0:
                # safeguarded refresh: frozen target and weights inside a block; refresh, merit test and optional backtrack at the boundary
                if prob.maybe_rebuild_pressure(zc):
                    changed = True
                lm_z = sg.get("lm_z") if sg.get("lm_z") is not None else zc      # the LM's own iterate (the reduced vector with tail constraints)
                if sg["z_prev"] is None:                                           # fallback only: Z0 is registered before the LM starts
                    sg["z_prev"] = zc.detach().clone(); sg["lm_z_prev"] = lm_z.detach().clone(); sg["merit_prev"] = cost
                sg["n_acc"] += 1
                if sg["n_acc"] >= sg["block"]:
                    sg["n_acc"] = 0
                    if prob.closure is not None:
                        prob.update_closure(zc)
                    merit, merit_cl = merit_of(zc, blocks=True); changed = True
                    ev = dict(it=it0 + it, merit=merit, merit_closure_part=merit_cl, merit_prev=sg["merit_prev"], frozen_cost=cost, backtrack=False)
                    force_bt = os.environ.get("E3_SG_TEST_FORCE_BACKTRACK")       # disposable smoke tests only: force one backtrack at this iteration
                    if sg["backtrack"] and sg["merit_prev"] is not None and (merit > sg["merit_prev"] or (force_bt is not None and int(force_bt) == it0 + it)):
                        lm_z.copy_(sg["lm_z_prev"])                                   # restore the previous boundary state IN PLACE in the LM's own iterate
                        zr = sg["z_prev"]                                              # its full vector (expanded) for the target refresh and the merit
                        if prob.closure is not None:
                            prob.update_closure(zr)
                        ev["backtrack"] = True; ev["merit_restored"] = merit_of(zr)
                        lam_new = max(float(rec["lam"]), sg["lam0"]) * 10.0
                    else:
                        sg["z_prev"] = zc.detach().clone(); sg["lm_z_prev"] = lm_z.detach().clone(); sg["merit_prev"] = merit
                        lam_new = max(float(rec["lam"]), sg["lam0"])
                    ev["lam_restart"] = lam_new; sg["events"].append(ev); rec["refresh_event"] = ev
                    log(f"  REFRESH BOUNDARY it {it0 + it}: frozen-objective cost {cost:.6e}, merit (fresh target, reference weights) {merit:.6e} (closure rows {merit_cl:.3e}) vs previous {ev['merit_prev']:.6e}"
                        + (f" -> BACKTRACK to the previous boundary (merit restored {ev['merit_restored']:.6e})" if ev["backtrack"] else " -> accepted") + f"; damping restart {lam_new:.1e}")
            elif rec.get("accepted", True):
                if prob.maybe_rebuild_pressure(zc):          # exact base parameters before the next Jacobian (free parameters)
                    changed = True
                if prob.nl_weighting:
                    prob.update_nl_weights(zc); changed = True
                if prob.closure is not None:                  # lagged G_required for the closure rows (FAILURE_ANALYSIS item 18)
                    prob.update_closure(zc); changed = True
                if prob.step_sigmaZ_ramp():
                    changed = True
            if time.time() - box["last_ck"] > CKPT_INTERVAL or STOP["flag"]:
                state["current"] = dict(idx=idx, z=zc.detach().cpu(), meta=meta, it=it0 + it + 1, lam=rec["lam"], history=hist + list(cur_hist), pivot=prob.pivot)
                atomic_save(state, ck_path); box["last_ck"] = time.time()
                log(f"  checkpoint at start {idx} it {it0+it}")
            if STOP["flag"]:
                raise KeyboardInterrupt
            if lam_new is not None:
                return dict(changed=changed, lam=lam_new)
            return changed

        # with tail constraints the optimizer works on the reduced vector; everything stored/diagnosed is the full vector
        use_scalar = prob.sigmaZ is not None and prob.fine_model is not None     # Sigma_Z row via reverse-mode gradient (memory)
        if tc is not None:
            fun = (lambda zr: prob.residual_vector_main(tc.expand(zr))) if use_scalar else (lambda zr: prob.residual_vector(tc.expand(zr)))
            fun_fd = lambda zr: prob.residual_vector_rebuild(tc.expand(zr))
            proj = lambda zr: tc.reduce(prob.phase_align(tc.expand(zr)))
            srows = [lambda zr: prob.sigmaZ_row(tc.expand(zr))] if use_scalar else None
            z_opt = tc.reduce(z); n_opt = tc.n_red
            cb_full = cb
            def cb(it, zc, cost, rec, _cb=cb_full):
                sg["lm_z"] = zc                                   # the LM's reduced iterate (the safeguarded refresh restores it in place on a backtrack)
                return _cb(it, tc.expand(zc), cost, rec)
            bnds = None
        else:
            fun = prob.residual_vector_main if use_scalar else prob.residual_vector
            fun_fd, proj, z_opt, n_opt, bnds = prob.residual_vector_rebuild, prob.phase_align, z, model.n_z, bounds
            srows = [prob.sigmaZ_row] if use_scalar else None
        if sg["block"] > 0:                                       # register Z0 as the first boundary reference (its target was refreshed above)
            sg["z_prev"] = z.detach().clone(); sg["lm_z_prev"] = z_opt.detach().clone(); sg["merit_prev"] = merit_of(z)
            log(f"  REFRESH BOUNDARY reference Z0: merit {sg['merit_prev']:.6e}")
        if cfg.get("core_pin") == "auto" and prob.core_pin is None:   # S8 core nontriviality row: pin the core RMS of U at the start state's value
            if meta.get("core_pin_value") is not None:                   # 2026-10-25T23:22Z (astra referee): on resume reuse the START state's pin (meta is checkpointed), never the resumed state's
                prob.core_pin = float(meta["core_pin_value"]); log(f"S8 CORE PIN restored from the checkpoint meta: {prob.core_pin:.6g}")
            else:
                with torch.no_grad():
                    prob.core_pin = float(prob.core_rms(model.fields_grid(z, need_vort=False)))
                meta["core_pin_value"] = prob.core_pin
            log(f"S8 CORE PIN: row {prob.core_pin_weight:g} (core_rms(U)/{prob.core_pin:.6g} - 1) on the training nodes r < R0 (lead 06:56Z item 4)")
        if cfg.get("nonaxi_pin") == "auto" and prob.nonaxi_pin is None:   # S9b guard rows: pin e_core and e_F at the start state's values
            if meta.get("nonaxi_pin_value") is not None:                 # 2026-10-25T23:22Z: resume reuses the START state's pins and shell cutoff
                prob.nonaxi_pin = tuple(float(v) for v in meta["nonaxi_pin_value"]); prob.nonaxi_r_tail = float(meta.get("nonaxi_r_tail_value", 1.0))
                log(f"S9b GUARD ROWS restored from the checkpoint meta: {prob.nonaxi_pin}, r_tail {prob.nonaxi_r_tail:.3g}")
            else:
                try:                                                           # SPEC 7.4 core shell set: lower edge <= r_tail of the start state (its training spec_diag)
                    prob.nonaxi_r_tail = float(((torch.load(cfg["init_from"], map_location="cpu", weights_only=False).get("spec_diag") or {}).get("guards") or {}).get("N5_r_tail") or 1.0) if cfg.get("init_from") else 1.0
                except Exception:
                    prob.nonaxi_r_tail = 1.0
                with torch.no_grad():
                    F0_ = model.fields_grid(z, need_vort=False); aT0, aS0, cl0, om0 = model.unpack(z)
                    prob.nonaxi_pin = (float(prob.e_core_training(F0_)), float(prob.e_F_tail(aT0, aS0, cl0, om0)))
                meta["nonaxi_pin_value"] = list(prob.nonaxi_pin); meta["nonaxi_r_tail_value"] = prob.nonaxi_r_tail
            log(f"S9b NON-AXISYMMETRY GUARD ROWS: {prob.nonaxi_pin_weight:g} (e_core/{prob.nonaxi_pin[0]:.4g} - 1) and (e_F/{prob.nonaxi_pin[1]:.4g} - 1), core shells with lower edge <= r_tail {prob.nonaxi_r_tail:.3g} (lead 07:26Z item 6)")
        if prob.core_pin is not None or prob.nonaxi_pin is not None:   # S9d: log the pin rows at the start state before each step (frozen numeric pins or auto)
            try:
                with torch.no_grad():
                    Fp_ = model.fields_grid(z, need_vort=False); aTp, aSp, clp, omp = model.unpack(z)
                    parts = []
                    if prob.core_pin is not None:
                        parts.append(f"core row {prob.core_pin_weight:g} x (core_rms {float(prob.core_rms(Fp_)):.6g} / pin {prob.core_pin:.6g} - 1) = {float(prob.core_pin_weight * (prob.core_rms(Fp_) / prob.core_pin - 1.0)):.3e}")
                    if prob.nonaxi_pin is not None:
                        ec_ = float(prob.e_core_training(Fp_)); ef_ = float(prob.e_F_tail(aTp, aSp, clp, omp))
                        parts.append(f"e_core row {prob.nonaxi_pin_weight:g} x ({ec_:.6g} / pin {prob.nonaxi_pin[0]:.6g} - 1) = {prob.nonaxi_pin_weight * (ec_ / prob.nonaxi_pin[0] - 1.0):.3e}; e_F row ({ef_:.6g} / pin {prob.nonaxi_pin[1]:.6g} - 1) = {prob.nonaxi_pin_weight * (ef_ / prob.nonaxi_pin[1] - 1.0):.3e}; e_core shell cutoff r_tail {getattr(prob, 'nonaxi_r_tail', None)}")
                log("PIN ROWS AT START (" + ("frozen numeric" if cfg.get("core_pin") != "auto" and cfg.get("nonaxi_pin") != "auto" else "auto") + "): " + " | ".join(parts))
            except Exception as e:
                log(f"PIN ROWS AT START: evaluation failed: {e!r}")
        if prob.radial_lambda_w > 0:                        # S12 (lead 2026-10-25T11:27Z): sphere rows on the radial-lambda part of the momentum residual
            log(f"S12 RADIAL-LAMBDA ROWS: w = {prob.radial_lambda_w:g}; rows sqrt(w) sqrt(w_k) sc_k <U.R_u>_k / <|U|^2>_k^(1/2) on the {model.Nr} radial training nodes (d93; registered diagnostics, never acceptance criteria)")
        if prob.balance_lambda > 0:                         # S9: lambda E_ren and lambda H_tot/int|h| as scalar rows (reverse-mode Jacobian rows)
            brows = ([lambda zr, i=i: prob.balance_rows(tc.expand(zr))[i] for i in range(2)] if tc is not None else [lambda zz, i=i: prob.balance_rows(zz)[i] for i in range(2)])
            srows = (srows or []) + brows
            log(f"S9 GLOBAL-BALANCE ROWS: lambda = {prob.balance_lambda:g} on E_ren and H_tot/int|h| (d64; scalar rows; registered diagnostics, never acceptance criteria)")
        if tc is not None and model.free_params:
            bnds = (torch.cat([torch.full((n_opt - 2,), -float("inf"), device=device), bounds[0][-2:]]), torch.cat([torch.full((n_opt - 2,), float("inf"), device=device), bounds[1][-2:]]))
        try:
            if cfg.get("optimizer", "lm") == "lbfgs" and not model.free_params:
                # L-BFGS on the COMPLETE residual (the Sigma_Z row included; the main-only split is an LM device). Free parameters are
                # not supported on this branch (no rebuilt-parameter gradient): such jobs fall through to LM.
                fun_full = (lambda zr: prob.residual_vector(tc.expand(zr))) if tc is not None else prob.residual_vector
                out = lbfgs_solve(fun_full, z_opt, max_iter=max(0, int(cfg.get("max_iter", 500)) - it0), callback=cb, log=log,
                                  time_limit=cfg.get("time_limit_per_start"), verbose=True)
            else:
                if cfg.get("optimizer", "lm") == "lbfgs":
                    log("  L-BFGS with free parameters is not supported (no rebuilt-parameter gradient): using LM")
                out = lm_solve(fun, z_opt, max_iter=max(0, int(cfg.get("max_iter", 100)) - it0), lam0=lam, chunk=int(cfg.get("chunk", 128)),
                               callback=cb, log=log, bounds=bnds, time_limit=cfg.get("time_limit_per_start"), verbose=True,
                               ftol=cfg.get("ftol", 1e-10), xtol=cfg.get("xtol", 1e-12), project=proj, scale_rows=None,   # full-diagonal Marquardt scaling: PDE-row-only scaling leaves the gauge/constraint directions undamped and stalled L=10 at iteration 0
                               fd_cols=([n_opt - 2, n_opt - 1] if (model.free_params and prob.formulation in ("mom", "both")) else None),
                               fd_fun=fun_fd, scalar_rows=srows,
                               eval_fun=(fun_fd if (model.free_params and prob.formulation in ("mom", "both")) else None),
                               jtj_blocks=int(cfg.get("jtj_blocks", 1)))     # > 1: split-column J^T J accumulation (memory J/jtj_blocks; L10 with SPEC channels)
        except KeyboardInterrupt:
            log("interrupted by SIGTERM; checkpoint written")
            break
        z = tc.expand(out["z"]) if tc is not None else out["z"]; hist = hist + out["history"]
        elapsed = time.time() - t0
        # exact F-gauge projection of the reported state (all coefficients scaled by 1/||F||; identity for an exact solution;
        # for a stalled state it perturbs the field by the soft-row defect, a few 1e-6 at most): report both defects
        gauge_defect_opt, _ = prob.gauge_defects(z)
        if prob.gauge == "F":
            aT_, aS_, c_l_, om_ = model.unpack(z)
            nF = prob.tail_norm2(aT_, aS_, c_l_, om_).clamp_min(1e-300).sqrt()
            if torch.isfinite(nF) and nF > 1e-8:
                z = z.clone(); z[: model.n_coef] = z[: model.n_coef] / nF
        if cfg.get("lm_only"):                     # solver validation mode (2026-10-25T16:12Z): save the LM output and skip the battery; never a ranked state
            zpath = os.path.join(run_dir, "starts", f"start_{idx:03d}.pt")
            z_raw = tc.expand(out["z"]) if tc is not None else out["z"]
            atomic_save(dict(z=z.detach().cpu(), z_lm_raw=z_raw.detach().cpu(), config=cfg, meta=meta, status=out["status"], lam=out["lam"], history=hist,
                             free_params=model.free_params, modes=model.modes, iterations=len(hist), pivot=prob.pivot, lm_only=True), zpath)
            ledger.append(LEDGER, dict(kind="lm_only_result", job_id=job_id, start=idx, status=out["status"], iterations=len(hist), seconds=elapsed,
                                       cost_history=[h.get("cost") for h in hist], t_jac=[h.get("t_jac") for h in hist], jtj_blocks=int(cfg.get("jtj_blocks", 1)),
                                       chunk=int(cfg.get("chunk", 128)), zfile=os.path.relpath(zpath, ROOT), code_versions=CODE_VERSIONS,
                                       gpu_peak_mem_GB=(torch.cuda.max_memory_allocated() / 2**30 if device != "cpu" else 0.0)))
            log(f"start {idx} LM-ONLY done: {out['status']}, {len(hist)} its, {elapsed:.0f}s; costs {[('%.6e' % h.get('cost')) for h in hist]}; peak GPU memory {torch.cuda.max_memory_allocated() / 2**30 if device != 'cpu' else 0.0:.1f} GB; no battery, not a ranked state")
            state["completed"].append(dict(idx=idx, rms=out["rms"], status=out["status"], zfile=zpath, lm_only=True))
            state["current"] = None
            atomic_save(state, ck_path); box["last_ck"] = time.time(); last_ck = box["last_ck"]
            hb.beat(force=True, start=idx, phase="start_done", rms=out["rms"])
            continue
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
                         free_params=model.free_params, modes=model.modes, iterations=len(hist), pivot=prob.pivot, pressure_eig_min=peig), zpath)
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
        ledger.append(LEDGER, rec)
        with open(os.path.join(run_dir, "results.jsonl"), "a") as f:
            f.write(json.dumps(rec) + "\n")
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
        state["completed"].append(dict(idx=idx, rms=out["rms"], status=out["status"], zfile=zpath))
        state["current"] = None
        atomic_save(state, ck_path); box["last_ck"] = time.time(); last_ck = box["last_ck"]
        _hb_stop.set()
        hb.beat(force=True, start=idx, phase="start_done", rms=out["rms"])
    done = len(state["completed"]) >= n_starts
    state["finished"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()) if done else None
    state["elapsed_job_seconds"] = state.get("elapsed_job_seconds", 0.0) + (time.time() - t_job0)
    atomic_save(state, ck_path)
    ledger.append(LEDGER, dict(kind="job_end", job_id=job_id, done=done, completed=len(state["completed"]), elapsed_job_seconds=state["elapsed_job_seconds"],
                               gpu_peak_mem_GB=(max(torch.cuda.max_memory_allocated() / 2**30, JOB_PEAK[0]) if device != "cpu" else 0.0)))   # whole-job peak (the battery items reset the counter)
    hb.beat(force=True, phase="done" if done else "interrupted")
    log(f"JOB {'DONE' if done else 'INTERRUPTED'} ({len(state['completed'])}/{n_starts} starts, {state['elapsed_job_seconds']:.0f}s total)")
    return 0 if done else 3


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
