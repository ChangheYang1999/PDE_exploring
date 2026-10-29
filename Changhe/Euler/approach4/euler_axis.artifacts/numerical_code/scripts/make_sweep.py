"""Generate the Stage I pilot sweep as job files in queue/pending/.

Usage: python3 scripts/make_sweep.py <sweep_name> [--dry]
Sweeps:
  pilot1: fixed c_l in the prompt list x {generic families (seeded), S1 seeds (q0 scan, z0 scan)} x {lm, lbfgs->lm},
          pilot resolution D=24, nmax=12, one shell to R=10 (K=16), emax=5.  S1 jobs use the S1-constrained branch
          and the working gauge taken from the seed; generic jobs use the swirl gauge (shift 1 lesson) or the full gauge.
  critical1: the separate c_l = 1/2 experiment (same families; alpha = 1; labelled separately).
Every job records its family, seed and parameters; nothing constrains the solve beyond the documented rows.
"""
import json, os, sys, itertools, hashlib
import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
Q = os.path.join(ROOT, "queue", "pending")
os.makedirs(Q, exist_ok=True)

CL_LIST = [0.505, 0.525, 0.56, 0.60, 0.64, 0.68, 0.72, 0.74]
GENERIC = ["gauss_core", "ring_core", "flat_core", "asym_dipole", "swirl_dominant", "poloidal_dominant", "random_spectral"]
PILOT = dict(D=24, nmax=12, shells=[[10.0, 16]], R1=2.0, emax=5.0, w_int=100.0, w_s1=300.0, Tmax_ext=6.907755278982137)  # Tmax = ln(1e3)
LM = [{"name": "lm", "max_iter": 800, "verbose": False, "time_limit": 600, "ftol": 1e-10}]
LBFGS_LM = [{"name": "lbfgs", "max_iter": 100, "verbose": False, "time_limit": 300}, {"name": "lm", "max_iter": 500, "verbose": False, "time_limit": 400, "ftol": 1e-10}]


def jid(*parts):
    return "_".join(str(p).replace(".", "p") for p in parts)


def write(job, dry):
    path = os.path.join(Q, job["job_id"] + ".json")
    if dry:
        print(job["job_id"]); return
    if os.path.exists(path) or os.path.exists(os.path.join(ROOT, "runs", job["job_id"], "result.json")):
        return
    with open(path, "w") as f:
        json.dump(job, f, indent=1)


PILOT2 = dict(PILOT, ball_radial="jacobi", emax=4.0)   # well-conditioned ball basis (20:45Z); fewer near-coincident exterior exponents


def pilot(name, cls, dry, stage_label, base=None):
    global PILOT
    saved = PILOT
    if base is not None:
        PILOT = base
    n = 0
    for cl in cls:
        cl_tag = f"cl{cl:.3f}"
        # S1 seeds: q0 scan at z0 = 0 and shifted sources
        for q0 in [0.5, 1.0, 2.0]:
            for (fam, z0) in [("s1_sym_v2", 0.0), ("s1_shift_v2", 0.5), ("s1_shift_v2", -1.0)]:
                if fam == "s1_sym_v2" or q0 == 1.0:
                    for shift in ([0.0, -2.0] if fam == "s1_sym_v2" else [-2.0]):
                        opt_name, opt = ("lm", LM) if not (fam == "s1_sym_v2" and q0 == 1.0 and shift == -2.0) else ("lbfgs_lm", LBFGS_LM)
                        cfg = dict(PILOT, cl=cl, gauge="full", s1_constraint=True, z0_init=z0, scale_power_shift=shift)
                        prio = 5 if cl in (0.60, 0.68) else 10
                        job = dict(job_id=jid(name, cl_tag, fam, f"q{q0}", f"z{z0}", f"sh{shift}", opt_name), priority=prio, branch="S1", stage=stage_label,
                                   max_retries=2, ckpt_seconds=300, cfg=cfg, gauge_from_seed=True, auto_row_scale=True,
                                   init=dict(family=fam, seed=1, extra=dict(q0=q0, z0=z0, L=1.0)), optimizer=opt,
                                   tags=["pilot", "s1_constrained", fam, f"shift{shift}"])
                        write(job, dry); n += 1
        # S1 seed without the constraint rows (does the free solve keep the structure?)
        cfg = dict(PILOT, cl=cl, gauge="full", s1_constraint=False, scale_power_shift=-2.0)
        write(dict(job_id=jid(name, cl_tag, "s1_sym_v2_free", "q1p0", "lm"), priority=12, branch="S1free", stage=stage_label, max_retries=2,
                   ckpt_seconds=300, cfg=cfg, gauge_from_seed=True, auto_row_scale=True, init=dict(family="s1_sym_v2", seed=1, extra=dict(q0=1.0, L=1.0)),
                   optimizer=LM, tags=["pilot", "s1_unconstrained"]), dry); n += 1
        # generic families, two seeds, two optimizers, alternating gauges
        for k, fam in enumerate(GENERIC):
            for seed in (1, 2):
                gauge = "swirl" if (k + seed) % 2 == 0 else "full"
                opt_name, opt = (("lm", LM) if seed == 1 else ("lbfgs_lm", LBFGS_LM))
                tail = ["mixed", "poloidal", "swirl", "even", "odd"][(k + seed) % 5]
                cfg = dict(PILOT, cl=cl, gauge=gauge, scale_power_shift=[0.0, -2.0][(k + seed) % 2])
                job = dict(job_id=jid(name, cl_tag, fam, f"s{seed}", gauge, opt_name), priority=20, branch="generic", stage=stage_label,
                           max_retries=2, ckpt_seconds=300, cfg=cfg, auto_row_scale=True,
                           init=dict(family=fam, seed=seed, scale_core=[0.7, 1.0, 1.4][(k + seed) % 3], extra=dict(tail=tail)),
                           optimizer=opt, tags=["pilot", "generic", fam, tail])
                write(job, dry); n += 1
    PILOT = saved
    return n


def s1pin(name, cls, dry, stage_label, base=None):
    """S1 branch with q(0, z0) pinned and c_l free (lead note 2: expect a one-parameter family in (q0, c_l))."""
    base = base or PILOT
    n = 0
    LMF = [{"name": "lm", "max_iter": 1200, "verbose": False, "time_limit": 900, "ftol": 1e-11}]
    for cl in cls:
        for q0 in [0.5, 1.0, 2.0]:
            for (fam, z0) in [("s1_sym_v2", 0.0), ("s1_shift_v2", 0.5)]:
                if fam == "s1_shift_v2" and q0 != 1.0:
                    continue
                cfg = dict(base, cl=cl, free_cl=True, gauge="full", s1_constraint=True, z0_init=z0, q0_pin=q0, scale_power_shift=-2.0)
                job = dict(job_id=jid(name, f"cl{cl:.3f}", fam, f"q{q0}", f"z{z0}", "freecl_lm"), priority=15, branch="S1pin_freecl", stage=stage_label,
                           max_retries=2, ckpt_seconds=300, cfg=cfg, gauge_from_seed=True, auto_row_scale=True,
                           init=dict(family=fam, seed=1, extra=dict(q0=q0, z0=z0, L=1.0)), optimizer=LMF,
                           tags=["pilot", "s1_constrained", "q0_pinned", "free_cl", fam])
                write(job, dry); n += 1
    return n


def s1amp(name, cls, dry, stage_label):
    """S1 branch with the explicit swirl amplitude A (q = A qhat, qhat(0, z0) = 1), c_l fixed (referee suggestion, 20:15Z)."""
    n = 0
    LMA = [{"name": "lm", "max_iter": 1200, "verbose": False, "time_limit": 900, "ftol": 1e-11}]
    for cl in cls:
        for q0 in [0.5, 1.0, 2.0]:
            for (fam, z0) in [("s1_sym_v2", 0.0), ("s1_shift_v2", 0.5)]:
                if fam == "s1_shift_v2" and q0 != 1.0:
                    continue
                for shift in ([-2.0, 0.0] if q0 == 1.0 and fam == "s1_sym_v2" else [-2.0]):
                    cfg = dict(PILOT, cl=cl, gauge="full", s1_constraint=True, z0_init=z0, amp_param=True, scale_power_shift=shift)
                    job = dict(job_id=jid(name, f"cl{cl:.3f}", fam, f"q{q0}", f"z{z0}", f"sh{shift}", "amp_lm"), priority=14, branch="S1amp", stage=stage_label,
                               max_retries=2, ckpt_seconds=300, cfg=cfg, gauge_from_seed=True, auto_row_scale=True,
                               init=dict(family=fam, seed=1, extra=dict(q0=q0, z0=z0, L=1.0)), optimizer=LMA,
                               tags=["pilot", "s1_constrained", "amp_param", fam])
                    write(job, dry); n += 1
    return n


T2_ROWS = [dict(field="phi", der="z", r=0.0, z=0.0, target_expr="(1 + 3*c)/2", weight=100.0),
           dict(field="phi", der="z", r=1.0, z=0.0, target_expr="c", weight=100.0),
           dict(field="phi", der="sz", r=1.0, z=0.0, target_expr="-(1 + c)/2", weight=100.0),
           dict(field="eta", der="z", r=1.0, z=0.0, target_expr="2*K**2/(3*c)", weight=100.0),
           dict(field="q", der="z", r=1.0, z=0.0, target_expr="K", weight=100.0)]


def t2(name, cls, Ks, dry, stage_label, prio=16):
    """T2 branch (lead notes 12 and 13): odd swirl, equatorial ring source at r = 1 (dilation gauge), five hard rows, q = 0 on the
    axis (axis rows), phi and q odd in z, c_l free, K pinned."""
    n = 0
    LMT = [{"name": "lm", "max_iter": 1500, "verbose": False, "time_limit": 1200, "ftol": 1e-11}]
    for cl in cls:
        for K in Ks:
            cfg = dict(PILOT2, cl=cl, free_cl=True, gauge="full", w_gauge=0.0, parity_phi="odd", parity_q="odd", point_rows=T2_ROWS, K_param=K,
                       axis_rows_q=24, w_axis_q=100.0, scale_power_shift=-2.0)
            job = dict(job_id=jid(name, f"cl{cl:.3f}", f"K{K}", "freecl_lm"), priority=prio, branch="T2", stage=stage_label, max_retries=2, ckpt_seconds=300,
                       cfg=cfg, auto_row_scale=True, init=dict(family="ring_t2", seed=1, extra=dict(K=K)), optimizer=LMT, tags=["T2", "odd_parity", "ring_source", "free_cl"])
            write(job, dry); n += 1
    return n


def t3_rows(n_eq=24, Rm=10.0):
    rows = [dict(field="phi", der="z", r=0.0, z=0.0, target_expr="-(1 + 2*c)/2", weight=100.0),   # origin: axial-inflow saddle, w'(0) = -(1 + c)
            dict(field="phi", der="z", r=0.0, z=1.0, target_expr="0.5", weight=100.0),           # S1 at z = 1 (z = -1 by parity)
            dict(field="phi", der="val", r=0.0, z=1.0, target_expr="-c/2", weight=100.0),        # W_z(0, 1) = 0
            dict(field="q", der="val", r=0.0, z=1.0, target_expr="K", weight=100.0)]             # q(0, 1) = K
    for rr in np.geomspace(1e-2, 100.0 * Rm, n_eq):                                             # q = 0 on the equator (Lemma 14)
        rows.append(dict(field="q", der="val", r=float(rr), z=0.0, target=0.0, weight=100.0))
    return rows


def t3(name, cls, Ks, dry, stage_label, prio=17, repair=False, base=None):
    """T3 branch (lead note 14): S1 pair at z = +-1 (dilation gauge), origin saddle, phi odd and q even in z, q = 0 on the equator,
    c_l free, K pinned."""
    n = 0
    LMT = [{"name": "lm", "max_iter": 1500, "verbose": False, "time_limit": 1200, "ftol": 1e-11}]
    for cl in cls:
        for K in Ks:
            cfg = dict(base or PILOT2, cl=cl, free_cl=True, gauge="full", w_gauge=0.0, parity_phi="odd", parity_q="even", point_rows=t3_rows(), K_param=K,
                       scale_power_shift=-2.0)
            job = dict(job_id=jid(name, f"cl{cl:.3f}", f"K{K}", "freecl_lm"), priority=prio, branch="T3", stage=stage_label, max_retries=2, ckpt_seconds=300,
                       cfg=cfg, auto_row_scale=True, init=dict(family="pair_t3", seed=1, extra=dict(K=K, saddle_repair=repair)), optimizer=LMT,
                       tags=["T3", "S1_pair", "free_cl"] + (["saddle_repair"] if repair else []))
            write(job, dry); n += 1
    return n


def t1ladder(name, dry, stage_label, prio=13, base=None, iters=1500):
    """Lead note 20: pinned-q0 ladder from the referee's positive-strain seeds; S1 rows, q0 pinned, c_l free, slaved exterior."""
    n = 0
    LML = [{"name": "lm", "max_iter": iters, "verbose": False, "time_limit": 2400, "ftol": 1e-11}]
    for cl, q0s in ((0.60, (4.0, 8.0, 12.0)), (0.68, (3.0, 4.0, 6.0)), (0.74, (2.5, 3.5, 5.0))):
        for q0 in q0s:
            cfg = dict(base or PILOT2, cl=cl, free_cl=True, gauge="full", s1_constraint=True, z0_init=0.0, q0_pin=q0, slave_correction=True, reg_exempt_correction=True,
                       scale_power_shift=-2.0)
            job = dict(job_id=jid(name, f"cl{cl:.3f}", f"q{q0}", "freecl_lm"), priority=prio, branch="S1pin_freecl_t1budget", stage=stage_label, max_retries=2,
                       ckpt_seconds=300, cfg=cfg, gauge_from_seed=True, auto_row_scale=True, init=dict(family="t1budget", seed=1, extra=dict(q0=q0)), optimizer=LML,
                       tags=["T1", "q0_ladder", "positive_strain_seed", "slaved_exterior"])
            write(job, dry); n += 1
    return n


if __name__ == "__main__":
    name = sys.argv[1]
    dry = "--dry" in sys.argv
    if name == "pilot1":
        n = pilot("p1", CL_LIST, dry, "I")
    elif name == "pilot2":
        n = pilot("p2", CL_LIST, dry, "I", base=PILOT2)
    elif name == "critical2":
        n = pilot("crit2", [0.5], dry, "I-critical", base=PILOT2)
    elif name == "s1pin1":
        n = s1pin("s1pin1", CL_LIST, dry, "I")
    elif name == "s1pin2":
        n = s1pin("s1pin2", [c for c in CL_LIST if c >= 0.56], dry, "I", base=PILOT2)
    elif name == "s1amp1":
        n = s1amp("s1amp1", CL_LIST, dry, "I")
    elif name == "s1amp_crit":
        n = s1amp("s1ampcrit", [0.5], dry, "I-critical")
    elif name == "t2a":
        n = t2("t2a", [0.60, 0.68], [1.0, 2.0], dry, "I")
    elif name == "t2b":
        n = t2("t2b", [0.56, 0.64, 0.72], [1.0, 2.0], dry, "I", prio=18)
    elif name == "t1ladder":
        n = t1ladder("t1lad", dry, "I-II")
    elif name == "t1ladder2":
        # the referee's positive-strain seeds have a narrow axial swirl column (aspect a up to 8): nmax = 12 under-resolves them
        # (ball fit error 16 percent, interface q jump 0.6 of scale); use D = 36, nmax = 24, K = 24
        n = t1ladder("t1lad2", dry, "I-II", base=dict(PILOT2, D=36, nmax=24, shells=[[10.0, 24]]), iters=1200)
    elif name == "t3b":
        n = t3("t3b", [0.64, 0.60], [1.0], dry, "I-II", prio=25, repair=True)
    elif name == "t3a":
        n = t3("t3a", [0.64, 0.60, 0.68], [1.0], dry, "I")
    elif name == "critical1":
        n = pilot("crit1", [0.5], dry, "I-critical")   # separate experiment: c_l = 1/2 (alpha = 1), labelled I-critical
    else:
        raise SystemExit("unknown sweep")
    print(f"{name}: {n} jobs {'(dry)' if dry else 'written to queue/pending'}")
