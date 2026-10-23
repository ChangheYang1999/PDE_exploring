#!/usr/bin/env python3
"""Generate experiment files (reproducible). Usage: python3 make_configs.py <family> ; writes configs/<exp_id>.json"""
import json, os, sys, copy
P = os.path.dirname(os.path.abspath(__file__))

BASE_V1 = {
  "cl": 0.45, "cl_trainable": False, "cl_bounds": [0.4, 0.5], "C": 0.0,
  "model": {"width": 96, "depth": 5, "feature_set": "dir_log", "l_in": 1.0, "xi_scale": 3.0, "l_env": 1.0, "zero_last": True},
  "seed": {"use": True, "a": 0.2, "b": -0.4, "c": 0.7, "trainable": True, "scale": 1.0, "scale_trainable": False},
  "sampling": {"R_core": 4.0, "R_max": 1000.0, "r_tube": 0.2, "z_min": 0.01, "R_origin": 0.5},
  "counts": {"n_core": 6144, "n_shell": 6144, "n_axis": 2048, "n_origin": 1024},
  "val_counts": {"n_core": 4096, "n_shell": 4096, "n_axis": 1024, "n_origin": 512},
  "loss": {"T_lambda": 0.0, "lambda_amp": 1.0, "amp_p": 8, "n_gauge": 2048, "lambda_nonaxi": 0.0, "log_nonaxi": False},
  "stages": [
    {"opt": "adam", "steps": 8000, "lr": 1e-3, "lr_final": 1e-4, "warmup": 200, "resample_every": 1, "loss": {"T_lambda": 0.0}},
    {"opt": "adam", "steps": 6000, "lr": 3e-4, "lr_final": 3e-5, "resample_every": 1, "loss": {"T_lambda": 0.5}},
    {"opt": "adam", "steps": 6000, "lr": 1e-4, "lr_final": 1e-5, "resample_every": 1, "loss": {"T_lambda": 1.0}},
    {"opt": "lbfgs", "steps": 200, "max_iter": 50, "history": 50, "resample_every": 10, "loss": {"T_lambda": 1.0}}
  ],
  "eval_every": 500, "log_every": 50, "ckpt_minutes": 10, "archive_every_steps": 4000, "rng_seed": 1
}

# seed families (EQUATIONS.md section 10): M1 default; Z0 strongly non-axisymmetric with ZERO axis vorticity (b = c_M,
# a + 1/2 large); M3 another generic matrix with opposite swirl sign. Off-axis paired blobs are a separate representation
# option (TODO v3: A_core blobs).
SEEDS = {"M1": (0.2, -0.4, 0.7), "Z0": (0.6, 0.5, 0.5), "M3": (-0.9, 0.8, -0.3)}

BASE_V2 = copy.deepcopy(BASE_V1)
BASE_V2["model"] = {"width": 96, "depth": 5, "feature_set": "dir_tau", "n_tail": 2, "l_in": 1.0, "l_env": 1.0, "zero_last": True,
                    "last_init_std": 0.02}
BASE_V2["sampling"] = {"R_core": 4.0, "R_max": 3000.0, "r_tube": 0.2, "z_min": 0.01, "R_origin": 0.5}
BASE_V2["stages"] = [
    {"opt": "adam", "steps": 8000, "lr": 1e-3, "lr_final": 1e-4, "warmup": 200, "resample_every": 1, "loss": {"T_lambda": 0.0}},
    {"opt": "adam", "steps": 6000, "lr": 3e-4, "lr_final": 3e-5, "resample_every": 1, "loss": {"T_lambda": 0.5}},
    {"opt": "adam", "steps": 8000, "lr": 1e-4, "lr_final": 1e-5, "resample_every": 1, "loss": {"T_lambda": 1.0}},
    {"opt": "lbfgs", "steps": 300, "max_iter": 50, "history": 50, "resample_every": 10, "loss": {"T_lambda": 1.0}}
]


def write(exp_id, cfg, priority, extra=None):
    ent = {"exp_id": exp_id, "priority": priority, "config": cfg}
    if extra:
        ent.update(extra)
    path = os.path.join(P, "configs", exp_id + ".json")
    json.dump(ent, open(path, "w"), indent=1)
    print(path)
    return path


def family_v1_sweep():
    out = []
    for cl in (0.5, 0.49, 0.47, 0.45, 0.43, 0.41):
        cfg = copy.deepcopy(BASE_V1); cfg["cl"] = cl
        pr = 50 if cl != 0.45 else 40  # pilot covers 0.45 first
        out.append(write("v1_M1_cl%03d" % round(cl * 100), cfg, pr))
    return out


def family_v2_sweep():
    """v2 representation (tail-informed), three seed families, fixed c_l sweep."""
    out = []
    for sname, abc in SEEDS.items():
        for cl in (0.5, 0.49, 0.47, 0.45, 0.43, 0.41):
            cfg = copy.deepcopy(BASE_V2); cfg["cl"] = cl
            cfg["seed"] = {"use": True, "a": abc[0], "b": abc[1], "c": abc[2], "trainable": True}
            cfg["rng_seed"] = {"M1": 1, "Z0": 2, "M3": 3}[sname]
            pr = {"M1": 60, "Z0": 58, "M3": 56}[sname] + (2 if cl in (0.45, 0.5) else 0)
            out.append(write("v2_%s_cl%03d" % (sname, round(cl * 100)), cfg, pr))
    return out


def family_v2b_blobs():
    """v2 representation with an off-axis Q-paired blob core added to a weak axisymmetric-ish seed (no extra parities)."""
    out = []
    blobs = {"trainable": True, "list": [{"y0": [0.9, 0.0, 0.25], "m": [0.0, 0.6, 0.3], "sigma": 0.6},
                                         {"y0": [0.0, 0.7, -0.4], "m": [0.4, 0.0, -0.2], "sigma": 0.5}]}
    for cl in (0.5, 0.47, 0.45, 0.43, 0.41):
        cfg = copy.deepcopy(BASE_V2); cfg["cl"] = cl
        cfg["seed"] = {"use": True, "a": -0.3, "b": -0.2, "c": 0.5, "trainable": True}
        cfg["blobs"] = blobs
        cfg["rng_seed"] = 4
        out.append(write("v2b_BL_cl%03d" % round(cl * 100), cfg, 54 + (2 if cl in (0.45, 0.5) else 0)))
    return out


def family_refine(src_exp, cl, tag="r1", width=None, points=2.0, R_max=30000.0, lbfgs_steps=600, priority=70):
    """Refinement of a finished branch: warm start from its ckpt_best, more points, wider domain, longer L-BFGS.
    width=None keeps the architecture (required for warm start); a different width starts fresh (no warm start)."""
    src_cfg = json.load(open(os.path.join(P, "configs", src_exp + ".json")))["config"]
    cfg = copy.deepcopy(src_cfg); cfg["cl"] = cl
    if width is None:
        cfg["init_from"] = os.path.join(P, "runs", src_exp, "ckpt_best.pt")
        cfg["stages"] = [
            {"opt": "adam", "steps": 4000, "lr": 1e-4, "lr_final": 1e-5, "resample_every": 1, "loss": {"T_lambda": 1.0}},
            {"opt": "lbfgs", "steps": lbfgs_steps, "max_iter": 50, "history": 50, "resample_every": 10, "loss": {"T_lambda": 1.0}}]
    else:
        cfg["model"]["width"] = width
    cfg["sampling"]["R_max"] = R_max
    cfg["counts"] = {k: int(v * points) for k, v in cfg["counts"].items()}
    eid = "%s_%s" % (src_exp, tag if width is None else "w%d" % width)
    return write(eid, cfg, priority)


def family_clfree(src_exp, tag="clfree", lo=0.40, hi=0.50, priority=72):
    """Trainable c_l (bounded) warm-started from a fixed-c_l branch; c_l initialized at the source value."""
    src_cfg = json.load(open(os.path.join(P, "configs", src_exp + ".json")))["config"]
    cfg = copy.deepcopy(src_cfg)
    cfg["cl_trainable"] = True; cfg["cl_bounds"] = [lo, hi]; cfg["init_from"] = os.path.join(P, "runs", src_exp, "ckpt_best.pt"); cfg["init_cl_from_source"] = True
    cfg["stages"] = [
        {"opt": "adam", "steps": 6000, "lr": 1e-4, "lr_final": 1e-5, "resample_every": 1, "loss": {"T_lambda": 1.0}},
        {"opt": "lbfgs", "steps": 300, "max_iter": 50, "history": 50, "resample_every": 10, "loss": {"T_lambda": 1.0}}]
    return write("%s_%s" % (src_exp, tag), cfg, priority)


if __name__ == "__main__":
    fam = sys.argv[1] if len(sys.argv) > 1 else "v1_sweep"
    args = sys.argv[2:]
    if fam == "refine":
        family_refine(args[0], float(args[1]), *(args[2:3] or ["r1"]), width=(int(args[3]) if len(args) > 3 and args[3] != "same" else None))
    elif fam == "clfree":
        family_clfree(args[0])
    else:
        globals()["family_" + fam]()
