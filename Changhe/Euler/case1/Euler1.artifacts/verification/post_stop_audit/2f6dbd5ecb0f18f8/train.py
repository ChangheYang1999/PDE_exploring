#!/usr/bin/env python3
"""Supervised training worker for one experiment (one process, one GPU or CPU).

Usage: python3 train.py --exp <experiment.json> [--device cuda:0] [--run-root runs]
The experiment file holds {"exp_id":..., "config": {...}, ...}. The worker resumes from
runs/<exp_id>/ckpt_last.pt if present. Exit codes: 0 done, 3 stopped (resumable), 4 failed.
Everything is FP64. Checkpoints are atomic (write tmp + os.replace). Active time is accumulated
step by step and capped per step so pauses (SIGSTOP, suspension) are not counted.
"""
import argparse, copy, hashlib, json, math, os, random, signal, socket, sys, time
import numpy as np
import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
torch.set_default_dtype(torch.float64)
from euler_ss.model import ProfileModel
from euler_ss.sampling import Sampler
from euler_ss.losses import compute_loss, nonaxi_ratio
from euler_ss import physics as ph
from euler_ss import diagnostics as dg

PROJECT = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(PROJECT, "CAMPAIGN_LEDGER.jsonl")
STEP_GAP_CAP = 30.0  # seconds; a gap between steps longer than this is an interruption, not active time (legacy accounting)
MERGE_GAP = 0.0      # no merging: every instrumented work interval is stored separately, so gaps between steps are never credited


def now_iso():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def cfg_hash(cfg):
    return hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()[:16]


def atomic_write_json(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=1, default=float)
    os.replace(tmp, path)


def atomic_torch_save(obj, path):
    tmp = path + ".tmp"
    torch.save(obj, tmp)
    os.replace(tmp, path)


def append_jsonl(path, obj):
    with open(path, "a") as f:
        f.write(json.dumps(obj, default=float) + "\n")


class Stopper:
    def __init__(self, run_dir, ignore_global=False):
        self.flag = False
        self.run_dir = run_dir
        self.ignore_global = ignore_global
        signal.signal(signal.SIGTERM, self._h)
        signal.signal(signal.SIGINT, self._h)

    def _h(self, *a):
        self.flag = True

    def check(self):
        if os.path.exists(os.path.join(self.run_dir, "STOP")) or (not self.ignore_global and os.path.exists(os.path.join(PROJECT, "STOP"))):
            self.flag = True
        return self.flag


def rng_state():
    st = {"torch": torch.get_rng_state(), "python": random.getstate(), "numpy": np.random.get_state()}
    if torch.cuda.is_available():
        st["cuda"] = torch.cuda.get_rng_state_all()
    return st


def set_rng_state(st):
    torch.set_rng_state(st["torch"].cpu())
    random.setstate(st["python"])
    np.random.set_state(st["numpy"])
    if "cuda" in st and torch.cuda.is_available():
        torch.cuda.set_rng_state_all([t.cpu() for t in st["cuda"]])


# ---------------------------------------------------------------------------------------------
# validation on untouched holdout points
# ---------------------------------------------------------------------------------------------
REGION_EDGES = [(0.0, 1.0, "D1_R<1"), (1.0, 3.0, "D2_1-3"), (3.0, 10.0, "D3_3-10"), (10.0, 100.0, "D4_10-100"),
                (100.0, 1e3, "D5_100-1e3"), (1e3, 1e5, "D6_1e3-1e5")]


@torch.no_grad()
def _noop():
    pass


def validate(model, val, cfg, device, chunk=4096):
    """Holdout metrics. val: dict region -> (y, w). Returns flat dict of floats."""
    cl = model.cl().item()
    C = model.C
    d = 1.0 - 1.0 / cl
    out = {"cl": cl}
    ys, ws, Rms, Us, gUs, gPs, Oms = [], [], [], [], [], [], []
    for name, (y, w) in val.items():
        F, J, H = ph.derivs(lambda p: model.fields(p), y, order=2, chunk=chunk)
        U, gU, P, gP, HP = ph.velocity_and_grad(F, J, H)
        Rm, V, conv = ph.momentum_residual(y, U, gU, gP, cl, C)
        Tn = ph.term_scale(y, cl, lam=1.0, l_env=model.l_env)
        Tl = ph.term_scale(y, cl, lam=0.0, l_env=model.l_env)
        rn = (Rm.norm(dim=-1) / Tn).detach()
        rl = (Rm.norm(dim=-1) / Tl).detach()
        out["val_mom_%s_rms_nl" % name] = rn.pow(2).mean().sqrt().item()
        out["val_mom_%s_max_nl" % name] = rn.max().item()
        out["val_mom_%s_rms_lin" % name] = rl.pow(2).mean().sqrt().item()
        out["val_div_%s_max" % name] = ph.divergence(gU).abs().max().item()
        ys.append(y); ws.append(w); Rms.append(Rm.detach()); Us.append(U.detach()); gUs.append(gU.detach()); gPs.append(gP.detach())
        Oms.append(ph.vorticity(gU).detach())
    # physical-volume norms use only the DISJOINT core ball + log shells (axis tube and origin ball overlap them and are
    # reported separately above as sampler-distribution RMS, never merged into a physical measure)
    keep = [i for i, name in enumerate(val.keys()) if name in ("core", "shell")]
    sel = lambda lst: torch.cat([lst[i] for i in keep])
    y = sel(ys); w = sel(ws); Rm = sel(Rms); U = sel(Us); gU = sel(gUs); gP = sel(gPs); Om = sel(Oms)
    R = y.norm(dim=-1)
    terms = ph.momentum_terms(y, U, gU, gP, cl, C)
    # physical-volume weighted relative residual eps_m(D) per region (PROMPT.md section 11)
    for lo, hi, nm in REGION_EDGES:
        msk = (R >= lo) & (R < hi)
        if msk.sum() < 10:
            continue
        ww = w[msk]
        def l2(v):
            return torch.sqrt((ww * (v[msk] ** 2).sum(-1)).sum()).item()
        num = l2(Rm)
        den = l2(terms["lin"]) + l2(terms["cl_ygradU"]) + l2(terms["C_dzU"]) + l2(terms["UgradU"]) + l2(terms["gradP"])  # C_dzU already carries the factor C
        out["eps_m_" + nm] = num / den if den > 0 else float("nan")
        out["den_m_" + nm] = den
        # residual at nonlinear scale: ||R_m||/(||U.gradU|| + ||gradP||)
        dn = l2(terms["UgradU"]) + l2(terms["gradP"])
        out["eps_nl_" + nm] = num / dn if dn > 0 else float("nan")
        out["n_" + nm] = int(msk.sum().item())
    # amplitude, vorticity, core size
    Un = U.norm(dim=-1); On = Om.norm(dim=-1)
    out["max_U_sampled"] = Un.max().item()
    out["max_Om_sampled"] = On.max().item()
    i = int(On.argmax().item())
    out["argmax_Om_R"] = R[i].item(); out["argmax_Om_r"] = float(math.hypot(y[i, 0].item(), y[i, 1].item())); out["argmax_Om_z"] = y[i, 2].item()
    core = R < cfg["sampling"]["R_core"]
    e = (w * On ** 2)[core]
    if e.sum() > 0:
        order = torch.argsort(R[core]); ce = torch.cumsum(e[order], 0) / e.sum()
        k = int((ce < 0.5).sum().item())
        out["core_R50_vort"] = R[core][order][min(k, len(order) - 1)].item()
    # stretching check at sampled vorticity maximum: Om.(gU Om)/|Om|^2 should be 1 for an exact profile
    om = Om[i]; out["stretch_at_max"] = (om @ (gU[i] @ om) / (om @ om)).item()
    # non-axisymmetry on core points (group average over 8 rotations)
    yc = y[core][:1024]
    e_non, e_tot, _, _ = nonaxi_ratio(model, yc, K=16)
    out["nonaxi_ratio_core"] = (e_non / e_tot).item()
    # vorticity fraction (irrotational check): ||Om||^2 / ||gradU||^2 on core (weighted)
    out["vort_frac_core"] = ((w * On ** 2)[core].sum() / (w * (gU ** 2).sum((-1, -2)))[core].sum()).item()
    # affine fit on core: U ~ M y + m0, report residual fraction
    yc, Uc, wc = y[core], U[core], w[core]
    X = torch.cat([yc, torch.ones_like(yc[:, :1])], 1)
    W = wc.sqrt().unsqueeze(-1)
    sol = torch.linalg.lstsq(X * W, Uc * W).solution
    res = Uc - X @ sol
    out["affine_resid_frac_core"] = ((wc * (res ** 2).sum(-1)).sum() / (wc * (Uc ** 2).sum(-1)).sum()).sqrt().item()
    # velocity and gradient at the origin
    F0, J0, H0 = ph.derivs(lambda p: model.fields(p), torch.zeros(1, 3, dtype=torch.float64, device=device), order=2)
    U0, gU0, P0, gP0, HP0 = ph.velocity_and_grad(F0, J0, H0)
    out["U0_z"] = U0[0, 2].item(); out["gradU0"] = gU0[0].detach().cpu().tolist(); out["P0"] = P0[0].item()
    # tail exponent estimate from shell points: slope of log|U| vs log R in 1e2<R<1e4
    msk = (R > 1e2) & (R < 1e4) & (Un > 0)
    if msk.sum() > 20:
        lr_, lu = torch.log(R[msk]), torch.log(Un[msk])
        A = torch.stack([lr_, torch.ones_like(lr_)], 1)
        sl = torch.linalg.lstsq(A, lu.unsqueeze(-1)).solution[0, 0].item()
        out["tail_slope_U"] = sl; out["tail_slope_expected_d"] = d
    # 3D dependence and parity defects (core), hard symmetry check
    out["dz_frac_core"] = dg.three_d_dependence(gU[core], w[core])
    inv, zr = dg.parity_defects(model, y[core][:2048])
    out["inversion_defect_core"] = inv; out["zrefl_defect_core"] = zr
    out["Qsym_defect_core"] = dg.symmetry_defect(model, y[core][:512])
    # ring Fourier content in the core (r in {0.25,0.5,1,2}, z in {-1,-0.5,0,0.5,1})
    rf = dg.ring_fourier_energy(model, [0.25, 0.5, 1.0, 2.0], [-1.0, -0.5, 0.0, 0.5, 1.0], K=32)
    for k, v in rf.items():
        out["ring_" + k] = v
    # stagnation set of V (Newton from fixed starts; EQUATIONS.md 7.3(h), 9.3)
    g = torch.Generator(); g.manual_seed(12345)
    starts = dg.stagnation_starts(int(cfg.get("stag_starts", 192)), cfg["sampling"]["R_core"], g, device)
    zeros, nconv, nfail = dg.find_stagnation_points(model, starts, cl, C, R_max=10 * cfg["sampling"]["R_core"])
    out["stag_n_zeros"] = len(zeros); out["stag_starts_converged"] = nconv
    out["stag_zeros"] = zeros[:16]
    if zeros:
        out["stag_min_nearest_other"] = min(z["nearest_other_zero"] for z in zeros)
        out["stag_min_abs_eig_gradV"] = min(z["min_abs_eig_gradV"] for z in zeros)
        out["stag_max_lambda_max_S"] = max(z["lambda_max_S"] for z in zeros)
        out["stag_max_abs_Omega"] = max(z["abs_Omega"] for z in zeros)
    out["val_score"] = float(np.mean([out[k] for k in out if k.startswith("val_mom_") and k.endswith("_rms_nl")]))
    return out


# ---------------------------------------------------------------------------------------------
def make_optimizer(model, stage):
    params = [p for p in model.parameters() if p.requires_grad]
    if stage["opt"] == "adam":
        return torch.optim.Adam(params, lr=stage["lr"], betas=tuple(stage.get("betas", (0.9, 0.999))), eps=stage.get("eps", 1e-12))
    if stage["opt"] == "lbfgs":
        return torch.optim.LBFGS(params, lr=stage.get("lr", 1.0), max_iter=stage.get("max_iter", 50), history_size=stage.get("history", 50),
                                 tolerance_grad=stage.get("tol_grad", 1e-14), tolerance_change=stage.get("tol_change", 1e-16),
                                 line_search_fn="strong_wolfe")
    raise ValueError(stage["opt"])


def lr_at(stage, k):
    """Cosine decay from lr to lr_final over the stage (Adam)."""
    lr0 = stage["lr"]; lr1 = stage.get("lr_final", lr0); n = max(1, stage["steps"])
    warm = int(stage.get("warmup", 0))
    if k < warm:
        return lr0 * (k + 1) / warm
    t = min(1.0, (k - warm) / max(1, n - warm))
    return lr1 + 0.5 * (lr0 - lr1) * (1 + math.cos(math.pi * t))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--exp", required=True)
    ap.add_argument("--device", default="cuda:0" if torch.cuda.is_available() else "cpu")
    ap.add_argument("--run-root", default=os.path.join(PROJECT, "runs"))
    ap.add_argument("--max-steps", type=int, default=None, help="stop after this many total steps (tests)")
    ap.add_argument("--no-ledger", action="store_true")
    ap.add_argument("--ignore-global-stop", action="store_true", help="tests only: ignore project/STOP (per-run STOP still honored)")
    ap.add_argument("--ledger-path", default=None, help="tests only: write ledger records to this file instead of the campaign ledger")
    args = ap.parse_args()

    global LEDGER
    if args.ledger_path:
        LEDGER = args.ledger_path
    with open(args.exp) as f:
        exp = json.load(f)
    exp_id = exp["exp_id"]; cfg = exp["config"]
    run_dir = os.path.join(args.run_root, exp_id)
    os.makedirs(run_dir, exist_ok=True)
    atomic_write_json(os.path.join(run_dir, "config.json"), cfg)
    device = torch.device(args.device)
    log = open(os.path.join(run_dir, "train.log"), "a")

    def say(*a):
        msg = now_iso() + " " + " ".join(str(x) for x in a)
        print(msg, flush=True); log.write(msg + "\n"); log.flush()

    chash = cfg_hash(cfg)
    say("start exp", exp_id, "device", device, "cfg_hash", chash, "pid", os.getpid(), "host", socket.gethostname())
    gpu_name = torch.cuda.get_device_name(device) if device.type == "cuda" else "cpu"
    say("hardware", gpu_name, "torch", torch.__version__, "default dtype", torch.get_default_dtype())

    seed = int(cfg.get("rng_seed", 0))
    torch.manual_seed(seed); random.seed(seed); np.random.seed(seed)
    model = ProfileModel(cfg).to(device)
    for n_, p_ in model.named_parameters():
        assert p_.dtype == torch.float64, (n_, p_.dtype)
    nparam = sum(p.numel() for p in model.parameters() if p.requires_grad)
    say("params", nparam, "trainable cl", model.cl_trainable, "cl0", model.cl().item())

    scfg = cfg["sampling"]
    sampler = Sampler(scfg, seed + 1)
    # untouched holdout: separate generator stream; saved once and reused on resume
    val_path = os.path.join(run_dir, "holdout.pt")
    if os.path.exists(val_path):
        val_cpu = torch.load(val_path, weights_only=False)
    else:
        vs = Sampler(scfg, seed + 7919)
        vc = cfg.get("val_counts", {"n_core": 4096, "n_shell": 4096, "n_axis": 1024, "n_origin": 512})
        val_cpu = {k: (y, w) for k, (y, w) in vs.sample(vc, "cpu").items()}
        atomic_torch_save(val_cpu, val_path)
    val = {k: (y.to(device), w.to(device)) for k, (y, w) in val_cpu.items()}
    gs = Sampler(scfg, seed + 104729)
    gauge_pts = gs.sample_region("core", int(cfg["loss"].get("n_gauge", 2048)))[0].to(device)

    stages = cfg["stages"]
    state = {"stage": 0, "step": 0, "global_step": 0, "active_seconds": 0.0, "best_val": float("inf"), "nan_count": 0, "interruptions": []}
    ckpt_last = os.path.join(run_dir, "ckpt_last.pt")
    opt = None
    saved_batch = None; batch_step_drawn = None
    if os.path.exists(ckpt_last):
        ck = torch.load(ckpt_last, map_location=device, weights_only=False)
        saved_batch = ck.get("batch")
        missing, unexpected = model.load_state_dict(ck["model"], strict=False)
        if missing or unexpected:
            say("WARNING state_dict keys missing", missing, "unexpected", unexpected)
        state = ck["state"]
        sampler.load_state_dict(ck["sampler"])
        set_rng_state(ck["rng"])
        say("resumed from", ckpt_last, "stage", state["stage"], "step", state["step"], "active_s", round(state["active_seconds"], 1))
        if state["stage"] < len(stages):
            opt = make_optimizer(model, stages[state["stage"]])
            if ck.get("opt") is not None:
                try:
                    opt.load_state_dict(ck["opt"])
                except Exception as e:  # optimizer type changed between stages or config edit
                    say("WARNING optimizer state not loaded:", repr(e))
        last_ckpt_state = ck
    else:
        last_ckpt_state = None
        if cfg.get("init_from"):
            # warm start from another run's checkpoint (same architecture); c_l handled separately so that a fixed-c_l
            # source can initialize a trainable-c_l branch at the same value, and vice versa.
            src = torch.load(cfg["init_from"], map_location=device, weights_only=False)
            sd = {k: v for k, v in src["model"].items() if k not in ("cl_fixed", "cl_theta")}
            tgt = model.state_dict()
            for k in list(sd.keys()):
                if k in tgt and sd[k].shape != tgt[k].shape:  # e.g. last layer with a different number of tail terms
                    new = torch.zeros_like(tgt[k]); n0 = min(sd[k].shape[0], new.shape[0]); new[:n0] = sd[k][:n0].to(new.dtype)
                    say("warm start: resized", k, tuple(sd[k].shape), "->", tuple(new.shape), "(extra rows zero)")
                    sd[k] = new
            missing, unexpected = model.load_state_dict(sd, strict=False)
            say("warm start from", cfg["init_from"], "src exp", src.get("exp_id"), "src step", src.get("state", {}).get("global_step"),
                "missing", [k for k in missing if k not in ("cl_fixed", "cl_theta")], "unexpected", unexpected)
            if cfg.get("init_cl_from_source", False):
                src_cl = float(src["model"]["cl_fixed"]) if "cl_fixed" in src["model"] else None
                if src_cl is not None and model.cl_trainable:
                    t = (src_cl - model.cl_lo) / (model.cl_hi - model.cl_lo); t = min(max(t, 1e-6), 1 - 1e-6)
                    with torch.no_grad():
                        model.cl_theta.fill_(math.log(t / (1 - t)))
                    say("c_l initialized from source value", src_cl)
            state["init_from"] = cfg["init_from"]; state["init_from_sha256"] = sha256_file(cfg["init_from"])

    stopper = Stopper(run_dir, ignore_global=args.ignore_global_stop)
    ckpt_minutes = float(cfg.get("ckpt_minutes", 10))
    log_every = int(cfg.get("log_every", 50)); eval_every = int(cfg.get("eval_every", 500)); archive_every = int(cfg.get("archive_every_steps", 5000))
    metrics_f = open(os.path.join(run_dir, "metrics.jsonl"), "a")
    val_f = open(os.path.join(run_dir, "val.jsonl"), "a")

    interval = {"start": None, "start_step": None, "active": 0.0, "chunks": [], "open": None}  # open = [start_epoch, last_epoch]
    t_last_step = None
    t_last_ckpt = time.time()

    def write_status(st, extra=None):
        d = {"exp_id": exp_id, "state": st, "stage": state["stage"], "step": state["step"], "global_step": state["global_step"],
             "active_seconds": state["active_seconds"], "best_val": state["best_val"], "cl": model.cl().item(), "updated": now_iso(), "pid": os.getpid(),
             "device": str(device), "gpu": gpu_name}
        if extra:
            d.update(extra)
        atomic_write_json(os.path.join(run_dir, "status.json"), d)

    cur_batch = {"batch": None, "step_drawn": None, "resample_every": 1}

    def checkpoint(reason, val_metrics=None, final=False):
        nonlocal t_last_ckpt, last_ckpt_state
        ck = {"model": model.state_dict(), "opt": opt.state_dict() if opt is not None else None, "state": copy.deepcopy(state),
              "sampler": sampler.state_dict(), "rng": rng_state(), "cfg": cfg, "exp_id": exp_id, "saved": now_iso(), "cfg_hash": chash}
        if cur_batch["batch"] is not None and cur_batch.get("resample_every", 1) > 1:
            ck["batch"] = {"step_drawn": cur_batch["step_drawn"], "stage": cur_batch["stage"], "counts": cur_batch["counts"], "sampler_cfg": dict(sampler.cfg),
                           "batch": {k: (y_.cpu(), w_.cpu()) for k, (y_, w_) in cur_batch["batch"].items()}}
        atomic_torch_save(ck, ckpt_last)
        last_ckpt_state = ck
        h = sha256_file(ckpt_last)
        if interval["open"] is not None:  # close the open compute chunk at the last accepted step
            interval["chunks"].append([round(interval["open"][0], 3), round(interval["open"][1], 3)])
            interval["open"] = None
        if interval["start"] is not None and not args.no_ledger:
            chunk_active = sum(e - s0 for s0, e in interval["chunks"])
            rec = {"exp_id": exp_id, "interval_start": interval["start"], "interval_end": now_iso(), "active_seconds": round(chunk_active, 3),
                   "chunks": list(interval["chunks"]), "chunks_note": "instrumented work intervals [epoch_start, epoch_end], one per optimizer step (batch draw through GPU-synchronized update) or validation pass, never merged, so inter-step gaps, checkpoint I/O, logging and pauses are not credited; endpoints rounded to 1 ms; active_seconds is their total",
                   "accounting_version": 3,
                   "wall_seconds": round(time.time() - interval["t0"], 3), "step_start": interval["start_step"], "step_end": state["global_step"],
                   "stage": state["stage"], "host": socket.gethostname(), "device": str(device), "gpu": gpu_name, "pid": os.getpid(),
                   "dtype": "float64", "cfg_hash": chash, "ckpt_sha256": h, "cl": model.cl().item(),
                   "cumulative_active_seconds": round(state["active_seconds"], 3), "reason": reason}
            if val_metrics:
                rec["val_score"] = val_metrics.get("val_score"); rec["nonaxi_ratio_core"] = val_metrics.get("nonaxi_ratio_core")
                rec["eps_m_D1"] = val_metrics.get("eps_m_D1_R<1")
            append_jsonl(LEDGER, rec)
            append_jsonl(os.path.join(run_dir, "ledger_local.jsonl"), rec)
        interval["start"] = now_iso(); interval["t0"] = time.time(); interval["start_step"] = state["global_step"]; interval["active"] = 0.0
        interval["chunks"] = []; interval["open"] = None
        t_last_ckpt = time.time()
        say("checkpoint", reason, "stage", state["stage"], "step", state["step"], "active_s", round(state["active_seconds"], 1), "sha", h[:12])

    def do_validation():
        t0 = time.time()
        vm = validate(model, val, cfg, device)
        if device.type == "cuda":
            torch.cuda.synchronize()
        t1 = time.time()
        if interval["start"] is not None:  # credit the validation compute as an instrumented work interval
            state["active_seconds"] += t1 - t0; interval["active"] += t1 - t0
            if interval["open"] is not None:
                interval["chunks"].append([round(interval["open"][0], 3), round(interval["open"][1], 3)])
            interval["open"] = [t0, t1]
        vm.update({"stage": state["stage"], "step": state["step"], "global_step": state["global_step"], "time": now_iso(), "active_seconds": state["active_seconds"], "eval_seconds": time.time() - t0})
        val_f.write(json.dumps(vm, default=float) + "\n"); val_f.flush()
        score = vm["val_score"]
        if score < state["best_val"] and math.isfinite(score):
            state["best_val"] = score
            atomic_torch_save({"model": model.state_dict(), "state": copy.deepcopy(state), "cfg": cfg, "exp_id": exp_id, "val": vm, "saved": now_iso()},
                              os.path.join(run_dir, "ckpt_best.pt"))
        say("VAL step", state["global_step"], "score(nl rms)", "%.3e" % score, "best", "%.3e" % state["best_val"], "eps_m D1/D2/D3",
            "%.2e/%.2e/%.2e" % (vm.get("eps_m_D1_R<1", float("nan")), vm.get("eps_m_D2_1-3", float("nan")), vm.get("eps_m_D3_3-10", float("nan"))),
            "nonaxi", "%.3e" % vm["nonaxi_ratio_core"], "maxU", "%.3f" % vm["max_U_sampled"], "R50", "%.3f" % vm.get("core_R50_vort", float("nan")),
            "tail", "%.3f" % vm.get("tail_slope_U", float("nan")), "cl", "%.5f" % vm["cl"], "epsnl D4/D5", "%.2e/%.2e" % (vm.get("eps_nl_D4_10-100", float("nan")), vm.get("eps_nl_D5_100-1e3", float("nan"))),
            "zeros", vm["stag_n_zeros"], "ring n2/n4", "%.3f/%.3f" % (vm["ring_n2"], vm["ring_n4"]), "inv/zref", "%.2e/%.2e" % (vm["inversion_defect_core"], vm["zrefl_defect_core"]))
        return vm

    write_status("running")
    exit_code = 0
    last_val = None
    try:
        while state["stage"] < len(stages):
            stage = stages[state["stage"]]
            if opt is None:
                opt = make_optimizer(model, stage)
            sampler.cfg.update(stage.get("sampling", {}))
            counts = dict(cfg.get("counts", {"n_core": 4096, "n_shell": 4096, "n_axis": 1024, "n_origin": 512}))
            counts.update(stage.get("counts", {}))
            lcfg_stage = dict(cfg["loss"]); lcfg_stage.update(stage.get("loss", {}))
            cfg_stage = dict(cfg); cfg_stage["loss"] = lcfg_stage
            resample_every = int(stage.get("resample_every", 1))
            say("stage", state["stage"], stage["opt"], "steps", stage["steps"], "from step", state["step"], "counts", counts, "loss", lcfg_stage,
                "derivs", "fast" if lcfg_stage.get("fast_derivs", True) else "torch.func")
            batch = None; cur_batch.update({"batch": None, "resample_every": resample_every})
            while state["step"] < stage["steps"]:
                if stopper.check():
                    raise KeyboardInterrupt
                if args.max_steps is not None and state["global_step"] >= args.max_steps:
                    raise KeyboardInterrupt
                t_begin = time.time()  # begin of eligible work for this step (batch draw + loss + optimizer update)
                if batch is None or state["step"] % resample_every == 0:
                    if (batch is None and saved_batch is not None and saved_batch.get("step_drawn") == state["step"] - (state["step"] % resample_every)
                            and saved_batch.get("stage") == state["stage"] and saved_batch.get("counts") == counts and saved_batch.get("sampler_cfg") == dict(sampler.cfg)
                            and state["step"] % resample_every != 0):
                        batch = {k: (y_.to(device), w_.to(device)) for k, (y_, w_) in saved_batch["batch"].items()}
                        say("restored saved batch drawn at stage", saved_batch["stage"], "step", saved_batch["step_drawn"])
                    else:
                        batch = sampler.sample(counts, device)
                        if stage["opt"] == "lbfgs" and state["step"] > 0 and state["step"] % resample_every == 0:
                            opt = make_optimizer(model, stage)  # reset quasi-Newton history when the objective changes
                    batch_step_drawn = state["step"] - (state["step"] % resample_every)
                    saved_batch = None
                    cur_batch.update({"batch": batch, "step_drawn": batch_step_drawn, "resample_every": resample_every, "stage": state["stage"], "counts": dict(counts)})
                if stage["opt"] == "adam":
                    for g in opt.param_groups:
                        g["lr"] = lr_at(stage, state["step"])
                    opt.zero_grad(set_to_none=True)
                    loss, logs = compute_loss(model, batch, gauge_pts, cfg_stage)
                    loss.backward()
                    if stage.get("grad_clip"):
                        torch.nn.utils.clip_grad_norm_(model.parameters(), stage["grad_clip"])
                    opt.step()
                else:
                    holder = {}
                    def closure():
                        opt.zero_grad(set_to_none=True)
                        l, lg = compute_loss(model, batch, gauge_pts, cfg_stage)
                        l.backward()
                        holder["loss"], holder["logs"] = l, lg
                        return l
                    opt.step(closure)
                    loss, logs = holder["loss"], holder["logs"]
                if device.type == "cuda":
                    torch.cuda.synchronize()
                lv = loss.item()
                # ---- NaN guard
                if not math.isfinite(lv):
                    state["nan_count"] += 1
                    say("NaN/inf loss at step", state["global_step"], "count", state["nan_count"])
                    if os.path.exists(ckpt_last):  # reload from disk: an in-memory state_dict() aliases the live parameters
                        ck_r = torch.load(ckpt_last, map_location=device, weights_only=False)
                        model.load_state_dict(ck_r["model"], strict=False)
                        if ck_r.get("opt") is not None and stage["opt"] == "adam":
                            try:
                                opt.load_state_dict(ck_r["opt"])
                            except Exception as e_:
                                say("opt state reload failed", repr(e_))
                        say("rolled back to", ckpt_last, "step", ck_r["state"]["global_step"])
                    for g in opt.param_groups:
                        g["lr"] = g["lr"] * 0.5
                    if stage["opt"] == "adam":
                        stage["lr"] = stage["lr"] * 0.5; stage["lr_final"] = stage.get("lr_final", stage["lr"]) * 0.5
                    if state["nan_count"] > 5:
                        say("too many NaNs; failing")
                        exit_code = 4
                        raise RuntimeError("NaN")
                    continue
                # ---- active time accounting: instrumented work interval [t_begin, t] (GPU synchronized above); checkpoint I/O,
                # logging and pauses lie outside these intervals. Adjacent intervals closer than MERGE_GAP are merged into a chunk.
                t = time.time()
                dur = t - t_begin
                state["active_seconds"] += dur; interval["active"] += dur
                if interval["start"] is None:
                    interval["start"] = now_iso(); interval["t0"] = t_begin; interval["start_step"] = state["global_step"]; interval["active"] = dur
                    interval["chunks"] = []; interval["open"] = None
                if interval["open"] is not None:
                    interval["chunks"].append([round(interval["open"][0], 3), round(interval["open"][1], 3)])
                interval["open"] = [t_begin, t]  # one interval per optimizer step; closed at the next step or at the checkpoint
                if t_last_step is not None and t - t_last_step > STEP_GAP_CAP:
                    state["interruptions"].append({"at": now_iso(), "gap_s": round(t - t_last_step - dur, 1), "step": state["global_step"]})
                    say("gap of", round(t - t_last_step - dur, 1), "s between steps (not credited)")
                t_last_step = t
                state["step"] += 1; state["global_step"] += 1
                if state["global_step"] % log_every == 0:
                    rec = {"global_step": state["global_step"], "stage": state["stage"], "step": state["step"], "time": now_iso(), "active_seconds": round(state["active_seconds"], 2),
                           "lr": opt.param_groups[0]["lr"], "loss": lv}
                    rec.update({k: (v.item() if torch.is_tensor(v) else v) for k, v in logs.items()})
                    metrics_f.write(json.dumps(rec, default=float) + "\n"); metrics_f.flush()
                    write_status("running", {"last_val": {k: last_val[k] for k in ("val_score", "nonaxi_ratio_core", "max_U_sampled", "core_R50_vort", "tail_slope_U") if k in last_val}} if last_val else None)
                    say("step", state["global_step"], "loss %.4e" % lv, " ".join("%s=%.3e" % (k, rec[k]) for k in ("mom_core", "mom_shell", "mom_axis", "gauge_amp", "amp_max") if k in rec), "cl=%.5f" % rec["cl"])
                if state["global_step"] % eval_every == 0:
                    last_val = do_validation()
                    write_status("running", {"last_val": {k: last_val[k] for k in ("val_score", "nonaxi_ratio_core", "max_U_sampled", "core_R50_vort", "tail_slope_U") if k in last_val}})
                if archive_every and state["global_step"] % archive_every == 0:
                    os.makedirs(os.path.join(run_dir, "archive"), exist_ok=True)
                    atomic_torch_save({"model": model.state_dict(), "state": copy.deepcopy(state), "cfg": cfg, "exp_id": exp_id, "saved": now_iso()},
                                      os.path.join(run_dir, "archive", "ckpt_step%07d.pt" % state["global_step"]))
                if time.time() - t_last_ckpt > ckpt_minutes * 60:
                    checkpoint("periodic", last_val)
            # stage finished
            last_val = do_validation()
            checkpoint("stage_end", last_val)
            state["stage"] += 1; state["step"] = 0
            opt = None
            cur_batch.update({"batch": None, "step_drawn": None})  # the old stage's batch must not survive the stage boundary
            checkpoint("stage_advance", last_val)  # persist the stage index with cleared optimizer and no batch
        # all stages done
        write_status("done", {"last_val": last_val})
        say("DONE exp", exp_id, "active_s", round(state["active_seconds"], 1))
        exit_code = 0
    except KeyboardInterrupt:
        last_val = do_validation() if (state["global_step"] > 0) else None
        checkpoint("stop", last_val)
        write_status("stopped", {"last_val": last_val})
        say("STOPPED exp", exp_id, "at stage", state["stage"], "step", state["step"])
        exit_code = 3
    except Exception as e:
        import traceback
        say("FAILED exp", exp_id, repr(e)); say(traceback.format_exc())
        try:
            checkpoint("fail")
        except Exception as e2:
            say("checkpoint failed", repr(e2))
        write_status("failed", {"error": repr(e)})
        exit_code = 4
    log.close(); metrics_f.close(); val_f.close()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
