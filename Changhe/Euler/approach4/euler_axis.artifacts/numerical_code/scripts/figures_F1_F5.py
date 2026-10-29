"""FINAL_REPORT figures F1 and F5 (lead note 34 item 3), PNG plus CSV, from FAILURE_MAP.csv (run scripts/failure_map.py first).
  F1  figures/F1_residual_vs_resolution.{png,csv}: best B2-admissible holdout rho_max per resolution level (D) for the registered ladders:
      single-source q0 = 3.5 and q0 = 2.5 at c_l 0.749, the reflection class at 0.749 and 0.74; plus the verifier's registered S1
      continuation ladder (values quoted from lead note 34: 4.07 / 6.54 / 5.71 at L0 / L1 / L2, not computed in this lane). Each point is
      labelled with its dominant equation.
  F5  figures/F5_cl_continuation.{png,csv}: B2-admissible floor per c_l and basis level (levels never joined by one line), the q0 = 3.5
      small-step chain from 0.749 down, the other chains (q0 5.0 fixed, q0 raised), and the free-c_l endpoints of Stage I.
Usage: CUDA_VISIBLE_DEVICES= python3 scripts/figures_F1_F5.py"""
import os, sys, csv, math, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
FIG = os.path.join(ROOT, "figures"); os.makedirs(FIG, exist_ok=True)


def fl(v):
    try:
        return float(v)
    except Exception:
        return float("nan")


rows = list(csv.DictReader(open(os.path.join(ROOT, "FAILURE_MAP.csv"))))
for r in rows:
    r["rho"] = fl(r["rho_max"]); r["cl"] = fl(r["cl_final"]); r["D"] = int(fl(r["level"].split("n")[0][1:])) if r["level"].startswith("D") else None
    r["b2"] = r["B2"] == "True"; r["q0"] = fl(r.get("q0_pin") or "nan"); r["par"] = r.get("parity") or ""
    r["rm"] = 20 if "Rm20" in r["job_id"] or "rm20" in r["job_id"] else (5 if r["job_id"].startswith("rm5") else 10)   # fallback name rule
    try:                                                                   # actual outer interface radius from the saved configuration (verifier audit 07:43Z)
        _cfg = json.load(open(os.path.join(ROOT, "runs", r["job_id"], "result.json")))["cfg"]
        r["rm"] = float(_cfg["shells"][-1][0]) if _cfg.get("shells") else float(_cfg.get("R1", 10))
    except Exception:
        pass

# ---------------- F1
def best_per_level(filt):
    out = {}
    for r in rows:
        if not r["b2"] or not math.isfinite(r["rho"]) or not filt(r):
            continue
        if r["D"] not in out or r["rho"] < out[r["D"]]["rho"]:
            out[r["D"]] = r
    return out

pin = lambda r: any(r["job_id"].startswith(p) for p in ("lad2", "lad3", "lad4", "t1lad2_cl0p740", "refl", "chain", "fmA", "fmB", "fmC", "t1seed", "rm5"))
series = [
    ("single-source q0 = 3.5, c_l 0.749", best_per_level(lambda r: pin(r) and abs(r["q0"] - 3.5) < 1e-9 and abs(r["cl"] - 0.749) < 1e-6 and not r["par"] and r["rm"] == 10)),
    ("single-source q0 = 2.5, c_l 0.749", best_per_level(lambda r: pin(r) and abs(r["q0"] - 2.5) < 1e-9 and abs(r["cl"] - 0.749) < 1e-6 and not r["par"] and r["rm"] == 10)),
    ("reflection class q0 = 3.5, c_l 0.749", best_per_level(lambda r: r["job_id"].startswith("refl") and abs(r["cl"] - 0.749) < 1e-6)),
    ("reflection class q0 = 3.5, c_l 0.74", best_per_level(lambda r: r["job_id"].startswith("refl") and abs(r["cl"] - 0.74) < 1e-6)),
    ("chain from 0.749, q0 = 3.5, c_l 0.74 (chain members only)", best_per_level(lambda r: r["job_id"].startswith(("chain", "fmA")) and abs(r["q0"] - 3.5) < 1e-9 and abs(r["cl"] - 0.74) < 1e-6 and not r["par"] and r["rm"] == 10)),
    ("direct seed q0 = 2.5, c_l 0.74 (fixed c_l)", best_per_level(lambda r: r["job_id"].startswith("t1seed") and abs(r["q0"] - 2.5) < 1e-9 and abs(r["cl"] - 0.74) < 1e-6 and r["rm"] == 10
                                                                  and not any(t in r["job_id"] for t in ("Quad", "Wint", "Shift", "Pert", "LB")))),
]
verifier_ladder = [(0, 4.07, "level 0 (4/3/2)"), (1, 6.54, "level 1 (6/4/3)"), (2, 5.71, "level 2 (8/5/4)")]   # independent single-source ladder, c_l 0.74, q0 2 (verifier registered; lead note 35)
fig, axs = plt.subplots(1, 2, figsize=(13, 5.2), gridspec_kw=dict(width_ratios=[2.2, 1]))
ax = axs[0]
csv_rows = []
for si, (lab, bp) in enumerate(series):
    if not bp:
        continue
    Ds = sorted(bp); ys = [bp[D]["rho"] for D in Ds]
    ax.semilogy(Ds, ys, "o-", ms=6, label=lab)
    for D in Ds:
        off = [(4, 6), (4, -16), (-70, 6), (-70, -16), (4, 18), (-70, -28)][si % 6]      # staggered label offsets so that labels at the same D do not overlap
        if si == 0: off = (4, -16)                      # q0 = 3.5 series (lower curve): labels below the points
        if si == 1: off = (4, 6) if D >= 48 else (4, -16)   # q0 = 2.5 series (just above it): labels above the points at D48/D64 (verifier audit 06:37Z), below at D36 (markers of the other series sit just above)
        if D == 24: off = (6, -14)                      # the D24 point sits next to the y-axis: label to its right (verifier audit 08:41Z)
        ax.annotate(f"{bp[D]['dominant_eq']} ({bp[D]['dominant_shell']})\n{bp[D]['level'].split('-')[0]}", (D, bp[D]["rho"]), textcoords="offset points", xytext=off, fontsize=6)
        csv_rows.append(dict(series=lab, D=D, level=bp[D]["level"], rho_max=bp[D]["rho"], dominant_eq=bp[D]["dominant_eq"], dominant_shell=bp[D]["dominant_shell"], job_id=bp[D]["job_id"],
                             source="numerics holdout rho_max; best swirl-magnitude-filtered run of the branch at this level with outer interface radius 10 (may be a run other than the refinement-chain parent)"))
ax.set_xlabel("ball polynomial degree D (per-point basis label D/nmax/K next to each point)"); ax.set_ylabel("holdout rho_max (SPEC 6.1), radius-10 runs")
ax.set_title("F1: residual metric against spectral resolution, primary basis\n(no displayed series establishes convergence to an accepted approximation; labels: dominant equation (shell, point set))", fontsize=9)
ax.grid(alpha=0.3); ax.legend(fontsize=7); ax.set_xticks([24, 36, 48, 64]); ax.set_xlim(20, 70)
_y0, _y1 = ax.get_ylim(); ax.set_ylim(_y0 * 0.6, _y1 * 1.3)          # room for the lowest and highest annotations (verifier audit 07:43Z)
ax2 = axs[1]
ax2.semilogy([d for d, _, _ in verifier_ladder], [v for _, v, _ in verifier_ladder], "k^--", ms=7)
for d, v, t in verifier_ladder:
    ax2.annotate(t, (d, v), textcoords="offset points", xytext=(4, 4), fontsize=7)
    csv_rows.append(dict(series="independent single-source ladder (c_l 0.74, q0 2; verifier)", D="", level=t, rho_max=v, dominant_eq="", dominant_shell="", job_id="",
                         source="verifier registered values (independent representation: angular/radial/correction counts per level), quoted from lead notes 34 and 35"))
ax2.set_xticks([0, 1, 2]); ax2.set_xlabel("level (angular/radial/correction counts)"); ax2.set_ylabel("registered rho_max")
ax2.set_title("independent single-source ladder (c_l = 0.74, q0 = 2)\nverifier's representation; not the primary basis", fontsize=9); ax2.grid(alpha=0.3)
fig.tight_layout(); fig.savefig(os.path.join(FIG, "F1_residual_vs_resolution.png"), dpi=120, bbox_inches="tight"); plt.close(fig)
with open(os.path.join(FIG, "F1_residual_vs_resolution.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(csv_rows[0].keys())); w.writeheader(); [w.writerow(x) for x in csv_rows]
open(os.path.join(FIG, "F1_caption.txt"), "w").write("F1. Holdout rho_max (SPEC 6.1) against resolution level; all displayed residuals exceed the thresholds. Population: runs with the outer interface at R = 10 only (the R = 5 variant of the q0 = 3.5 ladder, 1.58 at D36, and the R = 20 variants are excluded from this plot and from F5; they are reported in the tables and in FAILURE_ANALYSIS 18). Left: primary basis; each point is the best swirl-magnitude-filtered run of the branch at that level (it may come from a run other than the refinement-chain parent, e.g. q0 = 2.5 at D36: 4.12 against 4.24 for the chain parent), labelled with its dominant equation, shell and point set, and its basis D/nmax/K. The direct-seed series at c_l = 0.74 (q0 = 2.5) shows the levels D36 (seed and its continuation), D48 and D64 of the best interior state; its D24 point is the separately initialized fresh D24 seed (t1seedFreshD24_cl0p74_q2p5), not a transfer of the D36 state. Right: the verifier's independent single-source ladder (c_l = 0.74, q0 = 2) in its own representation and level axis. No displayed series establishes convergence to an accepted approximation; the c_l = 0.74 chain series contains chain members only, the other series the best swirl-filtered run of the branch at each level.\n")

# ---------------- F5
fig, axs = plt.subplots(1, 2, figsize=(14, 5.5))
csv5 = []
# (i) B2-admissible floor per (c_l, level) over ALL runs (pilot families included), one marker style per level, never joined
floor = {}
for r in rows:
    if not r["b2"] or not math.isfinite(r["rho"]) or r["D"] is None or r["rm"] != 10:
        continue
    key = (round(r["cl"], 4), r["D"])
    if key not in floor or r["rho"] < floor[key]["rho"]:
        floor[key] = r
mk = {24: "s", 36: "o", 48: "D", 64: "^"}
for D in sorted(set(k[1] for k in floor)):
    pts = sorted((k[0], floor[k]["rho"]) for k in floor if k[1] == D)
    axs[0].semilogy([p[0] for p in pts], [p[1] for p in pts], mk.get(D, "x"), ms=6, mfc="none", label=f"swirl-magnitude-filtered floor, level D{D} (not joined)")
    for k in floor:
        if k[1] == D:
            csv5.append(dict(kind="floor_per_cl_level", cl=k[0], D=D, rho_max=floor[k]["rho"], q0_pin=floor[k].get("q0_pin"), dominant_eq=floor[k]["dominant_eq"], job_id=floor[k]["job_id"]))
# (ii) chains: q0 = 3.5 small steps from 0.749 (D36), q0 = 5.0 fixed (fmB), q0 raised (fmC); D36 only, joined within one chain
def chain_pts(filt):
    pts = {}
    for r in rows:
        if r["D"] == 36 and r["rm"] == 10 and math.isfinite(r["rho"]) and filt(r):
            c = round(r["cl"], 4)
            if c not in pts or r["rho"] < pts[c]["rho"]:
                pts[c] = r
    return sorted(pts.items())
chains = [
    ("q0 = 3.5 chain from 0.749 (D36, fixed c_l, each step from the previous state)", chain_pts(lambda r: abs(r["q0"] - 3.5) < 1e-9 and not r["par"] and any(r["job_id"].startswith(p) for p in ("lad3c0745", "chain", "fmA_", "lad2cont_t1lad2_cl0p740_q3p5", "lad3cont_lad2cont_t1lad2_cl0p740_q3p5")))),
    ("q0 = 5.0 chain (fmB, D36)", chain_pts(lambda r: abs(r["q0"] - 5.0) < 1e-9 and any(r["job_id"].startswith(p) for p in ("fmB_", "lad4q5p0")))),
    ("q0 raised 5.5 / 6.0 / 7.0 chain (fmC, D36)", chain_pts(lambda r: r["job_id"].startswith("fmC_"))),
    ("reflection class (D36)", chain_pts(lambda r: r["job_id"].startswith("refl_D36"))),
    ("0.005-step chain from the 0.74 direct seed (fmE, q0 = 2.5, D36)", chain_pts(lambda r: r["job_id"].startswith("fmE_") or r["job_id"] == "t1seedC_cl0p74_q2p5")),
    ("0.005-step chain from the 0.68 direct seed (fmF, q0 = 3.9, D36)", chain_pts(lambda r: r["job_id"].startswith("fmF_") or r["job_id"] == "t1seedC2_cl0p68")),
]
for lab, pts in chains:
    if not pts:
        continue
    axs[0].semilogy([c for c, _ in pts], [r["rho"] for _, r in pts], "-", lw=1.5, alpha=0.8, label=lab)
    for c, r in pts:
        csv5.append(dict(kind="chain", chain=lab, cl=c, D=36, rho_max=r["rho"], q0_pin=r.get("q0_pin"), dominant_eq=r["dominant_eq"], job_id=r["job_id"]))
axs[0].axvspan(0.5, 0.75, color="C2", alpha=0.08, label="target interval 1/2 < c_l < 3/4")
axs[0].axvline(2.0 / 3.0, color="gray", ls=":", lw=1, label="c_l = 2/3 (alpha = 1/2: degree-0 pressure resonance, PROMPT section 5)")
axs[0].axvline(0.75, color="k", ls="--", lw=1); axs[0].axvline(0.5, color="k", ls="--", lw=1)
for k in floor:
    if k[0] > 0.75:
        axs[0].annotate("outside the target interval\n(free-c_l run with bound 0.80)", (k[0], floor[k]["rho"]), textcoords="offset points", xytext=(-90, 12), fontsize=6, arrowprops=dict(arrowstyle="-", lw=0.5))
axs[0].set_xlabel("c_l (final)"); axs[0].set_ylabel("holdout rho_max (SPEC 6.1)"); axs[0].grid(alpha=0.3)
axs[0].legend(fontsize=6, loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2)
axs[0].set_title("F5: c_l continuation: swirl-magnitude-filtered floors per level (markers, never joined across levels)\nand the fixed-c_l chains (lines, D36 only)", fontsize=9)
# (iii) free-c_l endpoints: start -> final c_l
ends = [r for r in rows if r["free_cl"] == "True" and math.isfinite(fl(r["cl_start"])) and math.isfinite(r["cl"])]
for r in ends:
    axs[1].plot([fl(r["cl_start"]), r["cl"]], [0, 1], "-", color="C0" if r["b2"] else "0.7", alpha=0.6, lw=1)
    csv5.append(dict(kind="free_cl_endpoint", cl=r["cl"], cl_start=fl(r["cl_start"]), D=r["D"], rho_max=r["rho"], B2=r["b2"], job_id=r["job_id"]))
axs[1].axvline(2.0 / 3.0, color="gray", ls=":", lw=1); axs[1].axvline(0.749, color="k", ls="--", lw=1); axs[1].axvline(0.501, color="k", ls="--", lw=1)
axs[1].set_yticks([0, 1]); axs[1].set_yticklabels(["start c_l", "final c_l"]); axs[1].set_xlabel("c_l"); axs[1].grid(alpha=0.3)
axs[1].axvspan(0.5, 0.75, color="C2", alpha=0.08)
axs[1].set_title(f"free-c_l runs ({len(ends)}): start to final c_l\n(blue: swirl magnitude filter passed; grey: swirl collapsed; dashed: bounds 0.501, 0.749)", fontsize=9)
fig.tight_layout(); fig.savefig(os.path.join(FIG, "F5_cl_continuation.png"), dpi=120, bbox_inches="tight"); plt.close(fig)
open(os.path.join(FIG, "F5_caption.txt"), "w").write("F5. c_l continuation. Population: runs with the outer interface at R = 10 only (the R = 5 and R = 20 variants are excluded). Left: swirl-magnitude-filtered floors (best holdout rho_max among runs with s_core and s_far >= 0.05; B2 stability under refinement is tested separately) per final c_l and basis level, drawn as unjoined markers because D24 pilot values and D36 chain values are different levels; the fixed-c_l chains (each step 1000 to 2500 LM iterations from the previous state) as lines, including the 0.005-step chains fmE and fmF from the 0.74 and 0.68 direct-seed states, which rise by a factor 3 to 50 within 0.03 of their seed c_l; the shaded band is the target interval 1/2 < c_l < 3/4, the dotted line c_l = 2/3 (alpha = 1/2, the degree-0 pressure resonance of PROMPT section 5), the c_l = 0.80 point a free-c_l run with the bound widened to 0.80, outside the target class. Right: start and final c_l of every free-c_l run.\n")
keys = sorted(set(k for d in csv5 for k in d))
with open(os.path.join(FIG, "F5_cl_continuation.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); [w.writerow(x) for x in csv5]
print("written F1 and F5 (png + csv);", len(csv_rows), "F1 rows,", len(csv5), "F5 rows")
