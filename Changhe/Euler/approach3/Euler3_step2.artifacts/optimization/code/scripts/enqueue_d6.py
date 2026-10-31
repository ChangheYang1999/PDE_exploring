#!/usr/bin/env python
"""D6FP: enqueue a degree-6 job (FREE, FIXED-CONTROL, PROFILE, SMOKE, VALIDATION or DIAG) with the production objective O1 (SPEC 4.1).
The basis (L, Nk, Nr, R0, channels, parity) is taken from the start file and never changed (SPEC 1.3).
Usage:
  enqueue_d6.py --start starts/S01_nest6_cl0.45_om1.0_p0.pt --label FREE --tag f01 [--c_l 0.45 --omega 1.0] [--param_init refit|keep_coefficients]
                [--perturb 1e-3] [--perturb_nonaxi 0.1] [--seed 0] [--max_iter 300] [--time_limit 7200] [--priority 10] [--fixed] [--closure_lambda 1e-3]
                [--gpus 5,6] [--max_retries 2] [--lin_every 50] [--note ...]
  enqueue_d6.py --random --c_l 0.44 --omega 0.3 --family random --seed 7 --label FREE --tag f_rand07 (random seed in the production basis)"""
import sys, os, json, time, argparse, hashlib
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import torch

PROD = dict(L=6, Nk=16, Nr=48, m_parity="even", R0=0.3, formulation="mom", nl_weighting=True, nl_denominator="all5far", far_lambda=1e-2,
            far_radii=[4096.0, 16384.0, 65536.0], tail_constraints=True, channels=dict(NkB=4, NkD=4, NkE=4, core_damp=2, LB=15, LD=14, LE=6),
            closure_lambda=1e-3, gauge_weight=100.0, chunk=256, threads=1, ftol=1e-7, xtol=1e-12, lam0=1e-2, param_step_max=0.5, complete_gradient=True,
            linearization=True, linearization_every=50, holdout_per_shell=6,
            spec_version="v1.9", spec_sha256="c8923e0b57dc25ae30a35b9943d083d14d0bb3f4aa9bce95ebb8cfc55d601ee3", release_battery="CPU-reduced (v1.9)", precision_mode=None, lag_jacobian=False)   # lead 01:14Z: SPEC v1.9 binding; precision_mode None = module default (set at the freeze)


def enqueue(job):
    path = os.path.join(ROOT, "queue", "pending", job["job_id"] + ".json")
    for d in ("pending", "running", "done", "failed", "hold", "cancelled"):
        if os.path.exists(os.path.join(ROOT, "queue", d, job["job_id"] + ".json")):
            return False, os.path.join(ROOT, "queue", d, job["job_id"] + ".json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(job, f, indent=1)
    os.replace(tmp, path)
    return True, path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default=None); ap.add_argument("--random", action="store_true"); ap.add_argument("--family", default="random")
    ap.add_argument("--label", required=True, choices=["FREE", "FIXED-CONTROL", "PROFILE", "SMOKE", "VALIDATION", "DIAG"]); ap.add_argument("--tag", required=True)
    ap.add_argument("--c_l", type=float, default=None); ap.add_argument("--omega", type=float, default=None); ap.add_argument("--param_init", default="keep_coefficients")
    ap.add_argument("--perturb", type=float, default=0.0); ap.add_argument("--perturb_nonaxi", type=float, default=0.0); ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--max_iter", type=int, default=300); ap.add_argument("--time_limit", type=float, default=7200.0); ap.add_argument("--priority", type=int, default=10)
    ap.add_argument("--fixed", action="store_true", help="fixed parameters (FIXED-CONTROL / PROFILE)"); ap.add_argument("--closure_lambda", type=float, default=None)
    ap.add_argument("--gpus", default=None); ap.add_argument("--max_retries", type=int, default=2); ap.add_argument("--lin_every", type=int, default=None)
    ap.add_argument("--note", default=""); ap.add_argument("--ckpt_interval", type=float, default=None); ap.add_argument("--chunk", type=int, default=None)
    ap.add_argument("--no_complete_gradient", action="store_true"); ap.add_argument("--no_linearization", action="store_true"); ap.add_argument("--ftol", type=float, default=None)
    ap.add_argument("--extra", default=None, help="JSON dict merged into the config (diagnostic variants; recorded)")
    a = ap.parse_args()
    cfg = dict(PROD)
    if a.start:
        sp = a.start if os.path.isabs(a.start) else os.path.join(ROOT, a.start)
        S = torch.load(sp, map_location="cpu", weights_only=False); scfg = S["config"]
        for k in ("L", "Nk", "Nr", "m_parity", "R0", "channels", "far_radii"):
            if scfg.get(k) is not None:
                cfg[k] = scfg[k]
        if scfg.get("channels") is None:
            cfg["channels"] = None
        if a.closure_lambda is None and scfg.get("closure_lambda") is not None and scfg.get("closure_lambda") != cfg["closure_lambda"]:
            pass   # the production objective keeps closure_lambda 1e-3 unless overridden explicitly (recorded)
        src_free = bool(S.get("free_params", False))
        c_src = float(S["z"][-2]) if src_free else float(scfg["c_l"]); om_src = float(S["z"][-1]) if src_free else float(scfg["omega"])
        cfg["init_from"] = sp; cfg["c_l"] = a.c_l if a.c_l is not None else c_src; cfg["omega"] = a.omega if a.omega is not None else om_src
        cfg["param_init_mode"] = a.param_init
        start_sha = hashlib.sha256(open(sp, "rb").read()).hexdigest()
    else:
        if a.c_l is None or a.omega is None:
            raise SystemExit("--random needs --c_l and --omega")
        cfg["c_l"], cfg["omega"], cfg["family"] = a.c_l, a.omega, a.family
        start_sha = None
    if cfg["L"] != 6:
        raise SystemExit("main degree must be 6")
    cfg["free_params"] = not a.fixed
    cfg["perturb"] = a.perturb; cfg["perturb_nonaxi"] = a.perturb_nonaxi; cfg["seed"] = a.seed; cfg["n_starts"] = 1
    cfg["max_iter"] = a.max_iter; cfg["time_limit_per_start"] = a.time_limit
    if a.closure_lambda is not None:
        cfg["closure_lambda"] = a.closure_lambda
    if a.lin_every is not None:
        cfg["linearization_every"] = a.lin_every
    if a.ckpt_interval is not None:
        cfg["ckpt_interval_s"] = a.ckpt_interval
    if a.chunk is not None:
        cfg["chunk"] = a.chunk
    if a.ftol is not None:
        cfg["ftol"] = a.ftol
    if a.no_complete_gradient:
        cfg["complete_gradient"] = False
    if a.no_linearization:
        cfg["linearization"] = False
    if a.extra:
        cfg.update(json.loads(a.extra))
    objective_label = "O1" if (cfg["closure_lambda"] == 1e-3 and cfg["nl_denominator"] == "all5far" and not a.extra) else "variant"
    job_id = f"{a.tag}_L6_cl{cfg['c_l']:.4f}_om{cfg['omega']:.4f}_{'free' if cfg['free_params'] else 'fixed'}"
    job = dict(job_id=job_id, label=a.label, type="d6fp", priority=a.priority, max_retries=a.max_retries, config=cfg, exclusive=True,
               created=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), note=a.note, start_sha256=start_sha, objective=objective_label,
               gpus_allowed=([int(g) for g in a.gpus.split(",")] if a.gpus else None))
    ok, path = enqueue(job)
    print(("enqueued " if ok else "exists: ") + path)


if __name__ == "__main__":
    main()
