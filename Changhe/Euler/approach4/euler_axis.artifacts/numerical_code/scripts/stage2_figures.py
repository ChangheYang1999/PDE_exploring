"""Stage II figures (PROMPT section 13, lead notes 21 item 5 and 27 item 5) from finished runs, CPU only:
  figures/stage2_rho_vs_level.png        residual metric (holdout rho_max, rel R_q, rel R_eta) against resolution level for the pinned-q0 branches
  figures/stage2_rho_vs_cl.png           c_l continuation: rho_max and s_core against c_l for each chain (fmA, fmB, fmC, lad/chain, reflection)
  figures/stage2_farfield_convergence.png  R^alpha |U| (poloidal and swirl rms over mu) against R for the best states, with the leading-tail value
  figures/stage2_axis_origin.png         axis and origin residual diagnostics against level and c_l
Usage: CUDA_VISIBLE_DEVICES= python3 scripts/stage2_figures.py"""
import os, sys, json, glob, math
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
import numpy as np, torch
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from axi.problem import Problem
from axi import validate
torch.set_default_dtype(torch.float64); torch.set_num_threads(1)
FIG = os.path.join(ROOT, "figures"); os.makedirs(FIG, exist_ok=True)

rows = []
for f in glob.glob(os.path.join(ROOT, "runs", "*", "result.json")):
    jid = os.path.basename(os.path.dirname(f))
    if not any(jid.startswith(p) for p in ("lad2", "lad3", "lad4", "chain", "fmA", "fmB", "fmC", "refl", "t1lad2_cl0p740", "t1seed", "rm5")):
        continue
    r = json.load(open(f)); v = r.get("validation") or {}; cfg = r["cfg"]; rep = r.get("report", {})
    if v.get("rho_max") is None or cfg.get("q0_pin") is None:
        continue
    rows.append(dict(job=jid, cl=r["cl"], D=cfg["D"], q0=cfg["q0_pin"], parity=bool(cfg.get("parity_phi")), rho=v["rho_max"], s_core=v.get("s_core"),
                     relq=rep.get("rel_Rq_inner"), rele=rep.get("rel_Reta_inner"), axis_q=(rep.get("axis") or {}).get("Rq", {}).get("rms"), axis_eta=(rep.get("axis") or {}).get("Reta", {}).get("rms"),
                     origin_q=(rep.get("origin_collar") or {}).get("Rq", {}).get("rms"), origin_eta=(rep.get("origin_collar") or {}).get("Reta", {}).get("rms"), n_iter=r.get("n_iter"),
                     Rm=cfg["shells"][-1][0], tag=("fmA" if jid.startswith("fmA") else "fmB" if jid.startswith("fmB") else "fmC" if jid.startswith("fmC") else "fmD" if jid.startswith("fmD") else "refl" if jid.startswith("refl") else "seed" if jid.startswith("t1seed") else "ladder")))
print(len(rows), "pinned-q0 states")

# 1. residual vs level, per (q0, c_l) group at c_l 0.749 and for the chain levels
fig, axs = plt.subplots(1, 3, figsize=(14, 4))
groups = {}
for d in rows:
    key = (d["q0"], round(d["cl"], 3), d["parity"], d["Rm"])
    groups.setdefault(key, []).append(d)
for key, g in sorted(groups.items()):
    if len(set(d["D"] for d in g)) < 2:
        continue
    g = sorted(g, key=lambda d: (d["D"], -(d["n_iter"] or 0)))
    best = {}
    for d in g:
        best.setdefault(d["D"], d)          # most iterations per level
    Ds = sorted(best); lab = f"q0 {key[0]} c_l {key[1]:.3f}{' refl' if key[2] else ''}{' Rm20' if key[3] > 10 else ''}"
    axs[0].semilogy(Ds, [best[D]["rho"] for D in Ds], "o-", label=lab)
    axs[1].semilogy(Ds, [best[D]["relq"] for D in Ds], "o-", label=lab)
    axs[2].semilogy(Ds, [best[D]["rele"] for D in Ds], "o-", label=lab)
for ax, t in zip(axs, ("holdout rho_max (SPEC 6.1)", "holdout rel R_q (inner)", "holdout rel R_eta (inner)")):
    ax.set_xlabel("ball degree D"); ax.set_title(t); ax.grid(alpha=0.3)
axs[0].legend(fontsize=6)
fig.suptitle("Stage II: residual against resolution level for the pinned-q0 T1 branches (levels D24/n12/K16, D36/n24/K24, D48/n32/K32, D64/n43/K43; no accepted profile, no sustained decrease with resolution)", fontsize=9)
fig.tight_layout(); fig.savefig(os.path.join(FIG, "stage2_rho_vs_level.png"), dpi=110); plt.close(fig)

# 2. c_l continuation
fig, axs = plt.subplots(1, 2, figsize=(11, 4))
for tag, mk in (("ladder", "o"), ("fmA", "s"), ("fmB", "^"), ("fmC", "D"), ("fmD", "P"), ("refl", "x"), ("seed", "*")):
    g = [d for d in rows if d["tag"] == tag and d["D"] == 36 and d["Rm"] <= 10]
    if tag == "ladder":
        g = [d for d in g if d["q0"] == 3.5 and (d["job"].startswith("chain") or d["job"].startswith("lad3c0745") or d["job"].startswith("lad3cont_lad2cont_t1lad2_cl0p740_q3p5"))]
    if not g:
        continue
    g = sorted(g, key=lambda d: d["cl"])
    axs[0].semilogy([d["cl"] for d in g], [d["rho"] for d in g], mk + "-", ms=5, label=f"{tag} (D36)")
    axs[1].plot([d["cl"] for d in g], [d["s_core"] for d in g], mk + "-", ms=5, label=f"{tag} (D36)")
for ax in axs:
    ax.axvline(2.0 / 3.0, color="gray", ls=":", lw=1); ax.axvline(0.75, color="k", ls="--", lw=1); ax.set_xlabel("c_l"); ax.grid(alpha=0.3)
axs[0].set_ylabel("holdout rho_max"); axs[0].set_title("c_l continuation by small steps (fixed c_l, from the previous state)"); axs[0].legend(fontsize=7)
axs[1].set_ylabel("core swirl fraction s_core"); axs[1].axhline(0.05, color="k", ls=":"); axs[1].set_title("swirl fraction along the chains")
fig.tight_layout(); fig.savefig(os.path.join(FIG, "stage2_rho_vs_cl.png"), dpi=110); plt.close(fig)

# 3. far-field convergence for selected states (R^alpha |U| against R)
sel = ["lad2cont_t1lad2_cl0p740_q3p5_freecl_lm", "lad3ref_lad2cont_t1lad2_cl0p740_q3p5_freecl_lm", "lad4ref64_lad3ref_lad2cont_t1lad2_cl0p740_q3p5_freecl_lm",
       "lad4q5p0_lad3cont_lad2cont_t1lad2_cl0p740_q3p5_freecl_lm", "refl_D36_cl0p749_q3p5", "chain074_lad3c0745_lad2cont_t1lad2_cl0p740_q3p5_freecl_lm"]
fig, axs = plt.subplots(1, 2, figsize=(11, 4))
mu = np.cos(np.linspace(0.03, math.pi - 0.03, 41))
Rs = np.array([1, 2, 4, 7, 10, 14, 20, 40, 100, 300, 1000, 1e4])
for jid in sel:
    pt = os.path.join(ROOT, "runs", jid, "final.pt")
    if not os.path.exists(pt):
        continue
    st = torch.load(pt, weights_only=False, map_location="cpu"); prob, x = Problem.from_state(st, device="cpu"); cl = prob.cl_of(x); al = (1 - cl) / cl
    pol, sw = [], []
    for R in Rs:
        fl = validate.fields(prob, x, np.full_like(mu, R), mu, cl)
        pol.append(R ** al * math.sqrt(float(np.mean(fl["Ur"] ** 2 + fl["Uz"] ** 2)))); sw.append(R ** al * math.sqrt(float(np.mean(fl["Ut"] ** 2))))
    lab = jid[:22] + f" (c_l {cl:.3f}, D{prob.cfg.D})"
    axs[0].semilogx(Rs, pol, "o-", ms=3, label=lab); axs[1].semilogx(Rs, sw, "o-", ms=3, label=lab)
for ax, t in zip(axs, ("R^alpha rms_mu |U_pol|", "R^alpha rms_mu |U_theta|")):
    ax.axvline(10, color="k", ls="--", lw=1); ax.set_xlabel("R"); ax.set_ylabel(t); ax.grid(alpha=0.3)
axs[0].legend(fontsize=6); axs[0].set_title("far-field convergence of R^alpha U (matching radius 10, dashed)")
fig.tight_layout(); fig.savefig(os.path.join(FIG, "stage2_farfield_convergence.png"), dpi=110); plt.close(fig)

# 4. axis and origin residuals against level and c_l
fig, axs = plt.subplots(1, 2, figsize=(11, 4))
g = sorted([d for d in rows if d["q0"] == 3.5 and not d["parity"] and d["Rm"] <= 10 and d["axis_q"] is not None], key=lambda d: (d["cl"], d["D"]))
for key, mk, lab in (("axis_q", "o", "axis rms R_q"), ("axis_eta", "s", "axis rms R_eta"), ("origin_q", "^", "origin collar rms R_q"), ("origin_eta", "v", "origin collar rms R_eta")):
    axs[0].semilogy([d["cl"] + 0.0004 * (d["D"] - 36) for d in g], [d[key] for d in g], mk, ms=4, label=lab)
axs[0].set_xlabel("c_l (offset by level: D36 at c_l, D48 +0.005, D64 +0.011)"); axs[0].set_title("axis and origin-collar residuals, q0 = 3.5 branch"); axs[0].legend(fontsize=7); axs[0].grid(alpha=0.3)
g2 = [d for d in rows if d["q0"] == 3.5 and abs(d["cl"] - 0.749) < 1e-6 and not d["parity"] and d["Rm"] <= 10 and d["axis_q"] is not None]
for key, mk, lab in (("axis_q", "o", "axis rms R_q"), ("axis_eta", "s", "axis rms R_eta"), ("origin_q", "^", "origin collar rms R_q"), ("origin_eta", "v", "origin collar rms R_eta")):
    axs[1].semilogy([d["D"] for d in g2], [d[key] for d in g2], mk, ms=4, label=lab)
axs[1].set_xlabel("ball degree D"); axs[1].set_title("c_l = 0.749: axis/origin residuals against level"); axs[1].grid(alpha=0.3); axs[1].legend(fontsize=7)
fig.tight_layout(); fig.savefig(os.path.join(FIG, "stage2_axis_origin.png"), dpi=110); plt.close(fig)
print("written: stage2_rho_vs_level.png stage2_rho_vs_cl.png stage2_farfield_convergence.png stage2_axis_origin.png")
