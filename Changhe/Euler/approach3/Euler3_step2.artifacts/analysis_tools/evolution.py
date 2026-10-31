"""Parameter, objective, gradient and residual evolution of the d6 lineages (prompt section 11 B).
Lead tool, read-only on the numerics run directories. CPU only.

Usage: evolution.py RUNS_DIR OUTDIR

Sources, per lineage (segments in order):
- the results record of the last completed segment: its "trajectory" holds every accepted iteration of the lineage up to
  that segment end (it_cum, cost, cost_blocks, c_l, omega, lam, the J_cw-scaled gradient gD_inf_over_r, and the
  complete gradient of O1 at the new iterate where it was evaluated);
- for a segment still running (no results record): the worker.log "LM it" lines (cost, rms, lam, |gD|/|r|, c_l,
  omega); the cost blocks and the complete gradient are then not available and are left empty;
- the "checkpoint diagnostics" lines of every worker.log (rho_u max on the standard and the half-step holdout
  quadrature, sigma_u max), at the reported accepted-iteration count;
- the end battery of every completed segment record (one row per segment end).
Writes OUTDIR/iterations.csv, OUTDIR/checkpoints.csv, OUTDIR/segment_ends.csv, five PNG figures and
OUTDIR/manifest.json (input hashes and sizes, worker logs included, capture time) and OUTDIR/summary.json.

Version 2 (2026-10-29, after the verifier's V426): the manifest lists every worker log read (sha256, bytes) and the
capture time, and the latest log time per lineage; the running median is the true median (mean of the two middle values
for an even count; windows clipped at the ends); summary.json states every window explicitly. Window convention: "the
last 50 accepted iterations" means the last 50 transitions, from the accepted iterate 50 steps before the latest one to
the latest one (51 rows). Gradient medians are over named row ranges (accepted-iteration indices given). Version 1 is
kept as evolution_v1_d7bdba2f.py.

Version 3 (2026-10-30): adds the all-m pair P3 (start S20) as lineages P3_FREE and P3_FIXED; nothing else changed.
Version 2 is kept as evolution_v2_8bd52f62.py.

Version 4 (2026-10-30): the P3 FREE lineage continues with the FREE-only segments cont3free_S20, cont4free_S20, ...
(segments 3 onward); nothing else changed. Version 3 is kept as evolution_v3_42eeff99.py."""
import csv, datetime, glob, hashlib, json, math, os, re, statistics, sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RUNS, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

S01, S09, S05 = "S01_L6_cl0.4500_om1.0000", "S09_L6_cl0.4500_om0.3000", "S05_L6_cl0.4500_om0.3000"
S20 = "S20_L6_cl0.4500_om1.0000"
LINEAGES = {
    "P1_FREE": ["p1_s1_%s_free" % S01, "p1_s2_%s_free" % S01] + ["cont1_s%d_%s_free" % (k, S01) for k in range(3, 9)],
    "P2_FREE": ["p2_s1_%s_free" % S09, "p2_s2_%s_free" % S09] + ["cont2_s%d_%s_free" % (k, S09) for k in range(3, 9)],
    "P1_FIXED": ["p1c_s1_%s_fixed" % S01, "p1c_s2_%s_fixed" % S01],
    "P2_FIXED": ["p2c_s1_%s_fixed" % S09, "p2c_s2_%s_fixed" % S09],
    "F1_S05": ["f1_s1_%s_free" % S05] + ["f1_S05_m%d_L6_cl0.4500_om0.3000_free" % k for k in range(1, 6)],
    "F2_S01_keep": ["f2_S01_k0_keep_L6_cl0.4597_om1.3389_free", "f2_S01_k0_keep_m1_L6_cl0.4597_om1.3389_free"]
                   + ["f2_S01_k0_keep_m%d_L6_cl0.4597_om1.3389_free" % k for k in range(2, 6)],
    "P3_FREE": ["p3_s%db_%s_free" % (k, S20) for k in (1, 2)] + ["cont%dfree_%s_free" % (k, S20) for k in range(3, 9)],
    "P3_FIXED": ["p3c_s%db_%s_fixed" % (k, S20) for k in range(1, 6)],
}
FREE = ["P1_FREE", "P2_FREE", "F1_S05", "F2_S01_keep", "P3_FREE"]
COL = {"P1_FREE": "C0", "P2_FREE": "C3", "P1_FIXED": "C0", "P2_FIXED": "C3", "F1_S05": "C2", "F2_S01_keep": "C1",
       "P3_FREE": "C4", "P3_FIXED": "C4"}
LM = re.compile(r"^(\S+Z)\s+LM it\s+(\d+) cost (\S+) rms (\S+) lam (\S+) \|gD\|/\|r\| (\S+) .*? c_l (\S+) omega (\S+)")
CK = re.compile(r"^(\S+Z)\s+checkpoint diagnostics at it (\d+): rho_u max std (\S+) half (\S+) sigma_u (\S+)")
BLOCKS = ["near_origin", "core_intermediate", "far_momentum", "far_anchors", "closure", "gauge"]
END_KEYS = ["c_l", "omega", "n_accepted", "n_rejected", "seconds", "cost_final", "rho_u_max", "rho_u_max_holdout",
            "rho_u_max_holdout_half", "sigma_u_max", "sigma_u_max_core", "a_max_core", "a_max_core_upper", "a_eff",
            "N_core", "N_F", "e_core", "e_F", "max_U", "r_core", "r_tail", "tau_F_R8", "core_ball_over_a_eff",
            "stop_reason", "saturation_stop", "near_edge", "core_resolved"]

manifest = {"inputs": {}, "capture_started": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}


def log_input(p):
    manifest["inputs"][os.path.relpath(p, RUNS)] = {"sha256": sha(p), "bytes": os.path.getsize(p)}


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def record(d):
    p = os.path.join(RUNS, d, "results.jsonl")
    if not os.path.exists(p):
        return None
    with open(p) as f:
        recs = [json.loads(l) for l in f if l.strip()]
    recs = [r for r in recs if r.get("kind") == "start_result"]
    if not recs:
        return None
    manifest["inputs"][d + "/results.jsonl"] = {"sha256": sha(p), "bytes": os.path.getsize(p)}
    return recs[-1]


def nan(x):
    return float("nan") if x is None else float(x)


iters, ckpts, ends, status, START, status_last_log = [], [], [], {}, {}, {}
for name, dirs in LINEAGES.items():
    dirs = [d for d in dirs if os.path.isdir(os.path.join(RUNS, d))]
    rows, last_rec_seg, n_done = [], 0, 0
    for seg, d in enumerate(dirs, 1):
        r = record(d)
        if r is not None:
            if seg == 1:
                START[name] = (r["params_initial"]["c_l"], r["params_initial"]["omega"])
            last_rec_seg, n_done = seg, len(r["trajectory"])
            traj = r["trajectory"]
            e = {"lineage": name, "segment": seg, "run": d}
            for k in END_KEYS:
                v = r.get(k)
                e[k] = v if not isinstance(v, (dict, list)) else json.dumps(v)
            for b in BLOCKS:
                e["end_block_" + b] = r["cost_blocks_final"].get(b)
            ends.append(e)
    # trajectory of the last completed record covers segments 1..last_rec_seg
    seg_of = []
    if last_rec_seg:
        r = record(dirs[last_rec_seg - 1])
        seg_no, prev_it = 1, None
        for x in r["trajectory"]:
            if prev_it is not None and x["it"] <= prev_it:
                seg_no += 1
            prev_it = x["it"]
            cg = x.get("complete_gradient") or {}
            gp = cg.get("g_param_phys") or {}
            cb = x.get("cost_blocks") or {}
            rows.append({"lineage": name, "segment": seg_no, "source": "results record", "it_cum": x["it_cum"],
                         "accepted": x["it_cum"] + 1, "it_segment": x["it"], "cost": x["cost"], "rms": "",
                         "c_l": x["c_l"], "omega": x["omega"], "omega_over_c_l": x["omega"] / x["c_l"], "lam": x["lam"],
                         "gD_inf_over_r_Jcw": x.get("gD_inf_over_r"),
                         "g_complete_inf_over_r": cg.get("g_inf_over_r", ""), "g_complete_2_over_r": cg.get("g_2_over_r", ""),
                         "g_complete_phys_c_l": gp.get("c_l", ""), "g_complete_phys_omega": gp.get("omega", ""),
                         **{"block_" + b: cb.get(b, "") for b in BLOCKS}})
    # segments without a results record (running or ended without a record): worker.log lines
    base = rows[-1]["it_cum"] + 1 if rows else 0
    running = []
    for seg in range(last_rec_seg + 1, len(dirs) + 1):
        p = os.path.join(RUNS, dirs[seg - 1], "worker.log")
        if not os.path.exists(p):
            continue
        running.append(dirs[seg - 1])
        log_input(p)
        with open(p) as f:
            for line in f:
                m = LM.match(line)
                if not m:
                    continue
                t, it, cost, rms, lam, gd, cl, om = m.groups()
                it = int(it)
                status_last_log[name] = t
                rows.append({"lineage": name, "segment": seg, "source": "worker.log (no results record)",
                             "it_cum": base + it, "accepted": base + it + 1, "it_segment": it, "cost": float(cost),
                             "rms": float(rms), "c_l": float(cl), "omega": float(om), "omega_over_c_l": float(om) / float(cl),
                             "lam": float(lam), "gD_inf_over_r_Jcw": float(gd), "g_complete_inf_over_r": "",
                             "g_complete_2_over_r": "", "g_complete_phys_c_l": "", "g_complete_phys_omega": "",
                             **{"block_" + b: "" for b in BLOCKS}})
        base = rows[-1]["it_cum"] + 1 if rows else base
    for seg, d in enumerate(dirs, 1):
        p = os.path.join(RUNS, d, "worker.log")
        if not os.path.exists(p):
            continue
        if os.path.relpath(p, RUNS) not in manifest["inputs"]:
            log_input(p)
        with open(p) as f:
            for line in f:
                m = CK.match(line)
                if m:
                    t, it, a, b, s = m.groups()
                    ckpts.append({"lineage": name, "segment": seg, "time": t, "accepted": int(it),
                                  "rho_u_max_std": float(a), "rho_u_max_half": float(b), "sigma_u_max": float(s)})
    iters += rows
    status[name] = {"segments": dirs, "completed_segments_in_record": last_rec_seg, "running_or_unrecorded": running,
                    "accepted_rows": len(rows), "latest_log_iteration_time": status_last_log.get(name)}

# checkpoint lines are repeated in resumed segments' logs only if the worker re-ran them; keep one per (lineage, accepted)
seen, ck = set(), []
for c in ckpts:
    k = (c["lineage"], c["accepted"])
    if k not in seen:
        seen.add(k)
        ck.append(c)
ckpts = ck


def write(path, rows):
    keys = list(rows[0].keys())
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for r in rows:
            w.writerow(r)


write(os.path.join(OUT, "iterations.csv"), iters)
write(os.path.join(OUT, "checkpoints.csv"), ckpts)
write(os.path.join(OUT, "segment_ends.csv"), ends)


def series(name, key, filt=None):
    xs, ys = [], []
    for r in iters:
        if r["lineage"] != name or r[key] in ("", None):
            continue
        if filt and not filt(r):
            continue
        xs.append(r["accepted"])
        ys.append(float(r[key]))
    return xs, ys


def seg_marks(ax, name):
    prev = None
    for r in iters:
        if r["lineage"] == name:
            if prev is not None and r["segment"] != prev:
                ax.axvline(r["accepted"] - 0.5, color=COL[name], lw=0.5, ls=":", alpha=0.6)
            prev = r["segment"]


# Figure 1: parameters
fig, axs = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
for name in FREE:
    for ax, key in zip(axs, ["c_l", "omega", "omega_over_c_l"]):
        x, y = series(name, key)
        if x:
            ax.plot(x, y, color=COL[name], lw=1.2, label=name)
            seg_marks(ax, name)
for ax, key in zip(axs, ["c_l", "omega (log scale)", "omega / c_l (log scale)"]):
    ax.set_ylabel(key)
    ax.grid(alpha=0.3, which="both")
axs[1].set_yscale("log")
axs[2].set_yscale("log")
axs[0].legend(fontsize=8)
axs[-1].set_xlabel("accepted iterations (cumulative over segments; dotted lines: segment ends)")
fig.suptitle("FREE lineages: parameters against accepted iterations", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig1_parameters.png"), dpi=130)
plt.close(fig)

# Figure 2: objective and residual blocks
fig, axs = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
for name in LINEAGES:
    ls = "--" if "FIXED" in name else "-"
    x, y = series(name, "cost")
    if x:
        axs[0].semilogy(x, y, color=COL[name], ls=ls, lw=1.1, label=name)
    for ax, b in zip(axs[1:], ["block_core_intermediate", "block_far_momentum"]):
        x, y = series(name, b)
        if x:
            ax.semilogy(x, y, color=COL[name], ls=ls, lw=1.1, label=name)
axs[0].set_ylabel("O1")
axs[0].set_ylim(1e-7, 4e-7)
axs[1].set_ylim(1e-7, 4e-7)
axs[0].text(0.99, 0.95, "F2_S01_keep starts off scale (O1 25.4 at its start, 4.1e-2 after one step)",
            transform=axs[0].transAxes, ha="right", va="top", fontsize=7)
axs[1].set_ylabel("core/intermediate block of O1")
axs[2].set_ylabel("far-momentum block of O1")
for ax in axs:
    ax.grid(alpha=0.3, which="both")
axs[0].legend(fontsize=7, ncol=2)
axs[-1].set_xlabel("accepted iterations (blocks only where a results record exists)")
fig.suptitle("Objective and residual blocks (dashed: FIXED-CONTROL)", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig2_objective_blocks.png"), dpi=130)
plt.close(fig)

# Figure 3: gradient norms
fig, axs = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
for name in FREE:
    for ax, key in zip(axs, ["gD_inf_over_r_Jcw", "g_complete_phys_c_l", "g_complete_phys_omega"]):
        x, y = series(name, key)
        if x:
            y = [abs(v) for v in y]
            ax.semilogy(x, y, color=COL[name], lw=0.4, alpha=0.45)
            med = [statistics.median(y[max(0, i - 7):i + 9]) for i in range(len(y))]
            ax.semilogy(x, med, color=COL[name], lw=1.6, label=name)
axs[0].set_ylabel("|gD|_inf / |r| (J_cw scaled)")
axs[1].set_ylabel("|dO1/dc_l| (complete)")
axs[2].set_ylabel("|dO1/domega| (complete)")
for ax in axs:
    ax.grid(alpha=0.3, which="both")
axs[0].legend(fontsize=8)
axs[-1].set_xlabel("accepted iterations (thin: every value; thick: running median over 16 iterations, clipped at the ends)")
fig.suptitle("Step-model (J_cw, pre-step) scaled gradient; complete parameter derivatives of O1 at the new iterate.\n"
             "Neither is the registered stationarity quantity (complete-J_c scaled gradient of the EVAL records).", fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig3_gradients.png"), dpi=130)
plt.close(fig)

# Figure 4: momentum residual at checkpoints
fig, axs = plt.subplots(2, 1, figsize=(8, 6.5), sharex=True)
for name in LINEAGES:
    ls = "--" if "FIXED" in name else "-"
    cs = [c for c in ckpts if c["lineage"] == name]
    if cs:
        axs[0].plot([c["accepted"] for c in cs], [c["rho_u_max_std"] for c in cs], color=COL[name], ls=ls, marker=".",
                    label=name + " std")
        axs[0].plot([c["accepted"] for c in cs], [c["rho_u_max_half"] for c in cs], color=COL[name], ls=ls, lw=0.6,
                    alpha=0.6)
        axs[1].plot([c["accepted"] for c in cs], [c["sigma_u_max"] for c in cs], color=COL[name], ls=ls, marker=".",
                    label=name)
axs[0].set_ylabel("rho_u max (holdout; thin: half-step)")
axs[1].set_ylabel("sigma_u max")
for ax in axs:
    ax.grid(alpha=0.3)
axs[0].legend(fontsize=7, ncol=2)
axs[-1].set_xlabel("accepted iterations at the checkpoint")
fig.suptitle("Momentum residual at the periodic checkpoints (dashed: FIXED-CONTROL)", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig4_momentum_residual.png"), dpi=130)
plt.close(fig)

# Figure 5: paths in the parameter plane
fig, ax = plt.subplots(figsize=(7, 5.5))
for name in FREE:
    xs = [r["c_l"] for r in iters if r["lineage"] == name]
    ys = [r["omega"] for r in iters if r["lineage"] == name]
    if xs:
        ax.plot(xs, ys, color=COL[name], lw=1.2, label=name)
        ax.plot(xs[0], ys[0], "o", color=COL[name], mfc="none")
        ax.plot(xs[-1], ys[-1], "s", color=COL[name])
        p0 = START.get(name)
        if p0 and (abs(p0[0] - xs[0]) > 1e-6 or abs(p0[1] - ys[0]) > 1e-6):
            ax.plot(*p0, "x", color=COL[name], ms=8)
            ax.plot([p0[0], xs[0]], [p0[1], ys[0]], color=COL[name], lw=0.8, ls=":")
ax.set_xlabel("c_l")
ax.set_ylabel("omega")
ax.set_yscale("log")
ax.grid(alpha=0.3, which="both")
ax.legend(fontsize=8)
ax.set_title("Parameter paths (cross: start; open circle: first accepted iterate; square: latest)", fontsize=10)
fig.tight_layout()
fig.savefig(os.path.join(OUT, "fig5_parameter_plane.png"), dpi=130)
plt.close(fig)

# summary.json: windows stated explicitly (V426)
summary = {"window_convention": "last 50 accepted iterations = last 50 transitions (51 rows, from accepted index n-51 to n-1)",
           "lineages": {}}
for name in LINEAGES:
    rs = [r for r in iters if r["lineage"] == name]
    if not rs:
        continue
    e = {"latest": {k: rs[-1][k] for k in ("accepted", "segment", "source", "cost", "c_l", "omega")}}
    if len(rs) >= 51:
        a, b = rs[-51], rs[-1]
        e["last_50_transitions"] = {"from_accepted": a["accepted"], "to_accepted": b["accepted"],
                                    "d_c_l": b["c_l"] - a["c_l"], "d_log_omega": math.log(b["omega"] / a["omega"]),
                                    "O1_fall_percent": 100.0 * (a["cost"] - b["cost"]) / a["cost"]}
    g = [r for r in rs if r["gD_inf_over_r_Jcw"] not in ("", None)]
    if len(g) >= 100:
        e["step_model_gradient_median"] = {
            "first_50": {"accepted": [g[0]["accepted"], g[49]["accepted"]],
                         "median": statistics.median(abs(float(r["gD_inf_over_r_Jcw"])) for r in g[:50])},
            "last_50": {"accepted": [g[-50]["accepted"], g[-1]["accepted"]],
                        "median": statistics.median(abs(float(r["gD_inf_over_r_Jcw"])) for r in g[-50:])}}
    cg = [r for r in rs if r["g_complete_phys_c_l"] not in ("", None)]
    if len(cg) >= 100:
        e["complete_gradient_median"] = {}
        for lab, part in (("first_50", cg[:50]), ("last_50", cg[-50:])):
            e["complete_gradient_median"][lab] = {
                "accepted": [part[0]["accepted"], part[-1]["accepted"]],
                "c_l": statistics.median(abs(float(r["g_complete_phys_c_l"])) for r in part),
                "omega": statistics.median(abs(float(r["g_complete_phys_omega"])) for r in part)}
    summary["lineages"][name] = e
with open(os.path.join(OUT, "summary.json"), "w") as f:
    json.dump(summary, f, indent=1)

manifest["status"] = status
manifest["capture_finished"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
manifest["tool_sha256"] = sha(os.path.abspath(__file__))
for f in sorted(os.listdir(OUT)):
    if f != "manifest.json":
        manifest.setdefault("outputs", {})[f] = sha(os.path.join(OUT, f))
with open(os.path.join(OUT, "manifest.json"), "w") as f:
    json.dump(manifest, f, indent=1)
for name, s in status.items():
    print(name, s["completed_segments_in_record"], "recorded segments;", len(s["running_or_unrecorded"]), "from logs;",
          s["accepted_rows"], "rows")
print(len(ckpts), "checkpoint rows;", len(ends), "segment ends")
