"""Quantitative figures (PROMPT section 13) from finished runs. Usage: python3 scripts/make_figures.py [run_dir ...]
Without arguments: the top 6 of CANDIDATE_LEADERBOARD.csv. Writes PNGs to figures/<job_id>_*.png and figures/sweep_*.png."""
import os, sys, json, csv, math, glob
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
import numpy as np, torch
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from axi.problem import Problem, Config
from axi import validate
torch.set_default_dtype(torch.float64)
FIG = os.path.join(ROOT, "figures"); os.makedirs(FIG, exist_ok=True)


def run_figures(run_dir):
    jid = os.path.basename(os.path.normpath(run_dir))
    d = torch.load(os.path.join(run_dir, "final.pt"), weights_only=False, map_location="cpu")
    prob, x = Problem.from_state(d, device="cpu"); cfg = prob.cfg
    res = json.load(open(os.path.join(run_dir, "result.json")))
    val = json.load(open(os.path.join(run_dir, "validation.json"))) if os.path.exists(os.path.join(run_dir, "validation.json")) else None
    # 1. cost history
    h = [r for r in d["history"] if "cost" in r]
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.semilogy([r["cost"] for r in h]); ax.set_xlabel("iteration (all stages)"); ax.set_ylabel("weighted cost 0.5||r||^2"); ax.set_title(f"{jid[:50]}\nc_l={res['cl']:.4f}")
    fig.tight_layout(); fig.savefig(os.path.join(FIG, f"{jid}_cost.png"), dpi=110); plt.close(fig)
    # 2. residual vs radius (SPEC shells) and swirl/poloidal RMS per shell
    if val:
        sh = val["shells"]; Rc = [math.sqrt(s["Rlo"] * s["Rhi"]) for s in sh]
        fig, axs = plt.subplots(1, 2, figsize=(11, 3.8))
        for e in ("Mr", "Mt", "Mz", "q", "eta"):
            axs[0].loglog(Rc, [s.get(f"rho_{e}_gauss", float("nan")) for s in sh], marker="o", ms=3, label=f"rho_{e}")
        axs[0].axhline(1e-6, color="k", ls=":", lw=0.8); axs[0].set_xlabel("shell centre R / a_eff units (a_eff=%.3g)" % val["a_eff"]); axs[0].set_ylabel("SPEC rho_E (Gauss set)"); axs[0].legend(fontsize=7)
        axs[1].loglog(Rc, [s.get("rms_U", float("nan")) for s in sh], label="RMS |U|"); axs[1].loglog(Rc, [s.get("rms_Ut", float("nan")) for s in sh], label="RMS U^theta")
        axs[1].loglog(Rc, [s.get("rms_q", float("nan")) for s in sh], label="RMS q"); axs[1].loglog(Rc, [s.get("rms_eta", float("nan")) for s in sh], label="RMS eta")
        axs[1].set_xlabel("shell centre R"); axs[1].legend(fontsize=7); axs[1].set_title("field distribution per shell")
        fig.suptitle(f"{jid[:60]}  rho_max={val['rho_max']:.2e}  s_core={val['s_core']:.3f}", fontsize=9); fig.tight_layout(); fig.savefig(os.path.join(FIG, f"{jid}_residual_vs_radius.png"), dpi=110); plt.close(fig)
    # 3. spectral coefficient decay (by Legendre degree n and radial index k per element)
    cphi, cq, _ = prob.split(x)
    fig, axs = plt.subplots(1, 2, figsize=(11, 3.8))
    for i, e in enumerate(prob.elements):
        if e.kind == "exterior": continue
        labs = [e.labels[j] for j in prob.cols_phi[i]]; n_arr = np.array([l[0] for l in labs]); k_arr = np.array([l[1] for l in labs])
        labs_q = [e.labels[j] for j in prob.cols_q[i]]; nq_arr = np.array([l[0] for l in labs_q]); kq_arr = np.array([l[1] for l in labs_q])
        for arr, arrq, ax, nm in ((n_arr, nq_arr, axs[0], "Legendre degree n"), (k_arr, kq_arr, axs[1], "radial index k")):
            u = np.unique(arr); uq = np.unique(arrq)
            ax.semilogy(u, [np.sqrt(np.sum(cphi[i].numpy()[arr == a] ** 2)) for a in u], marker="o", ms=3, label=f"phi el{i} ({e.kind})")
            ax.semilogy(uq, [np.sqrt(np.sum(cq[i].numpy()[arrq == a] ** 2)) for a in uq], marker="s", ms=3, ls="--", label=f"q el{i}")
            ax.set_xlabel(nm)
    axs[0].legend(fontsize=7); axs[0].set_ylabel("coefficient norm"); fig.suptitle(f"{jid[:60]} spectral decay", fontsize=9); fig.tight_layout()
    fig.savefig(os.path.join(FIG, f"{jid}_spectral_decay.png"), dpi=110); plt.close(fig)
    # 4. fields in the meridional plane: q, eta, |U_pol|, W_m streamlines
    L = 3 * (val["a_eff"] if val else prob.cfg.R1)
    r = np.linspace(1e-3, L, 161); z = np.linspace(-L, L, 241); RR_, ZZ = np.meshgrid(r, z, indexing="ij")
    R = np.sqrt(RR_ ** 2 + ZZ ** 2); mu = ZZ / R
    f = validate.fields(prob, x, R.ravel(), mu.ravel())
    fig, axs = plt.subplots(1, 4, figsize=(16, 4.2))
    for ax, (nm, v) in zip(axs, [("q", f["q"]), ("eta", f["eta"]), ("|U_pol|", np.sqrt(f["Ur"] ** 2 + f["Uz"] ** 2)), ("U^theta", f["Ut"])]):
        vv = v.reshape(RR_.shape); m = np.max(np.abs(vv)) or 1
        im = ax.pcolormesh(RR_, ZZ, vv, cmap="RdBu_r", vmin=-m, vmax=m, shading="auto"); ax.set_title(nm); ax.set_xlabel("r"); ax.set_aspect("equal"); fig.colorbar(im, ax=ax, shrink=0.8)
    Wr = (prob.cl * RR_ + f["Ur"].reshape(RR_.shape)); Wz = (prob.cl * ZZ + f["Uz"].reshape(RR_.shape))
    axs[2].streamplot(r, z, Wr.T, Wz.T, color="k", linewidth=0.5, density=0.9)
    axs[2].set_title("|U_pol| with W_m streamlines")
    fig.suptitle(f"{jid[:60]}  c_l={res['cl']:.4f}", fontsize=9); fig.tight_layout(); fig.savefig(os.path.join(FIG, f"{jid}_fields.png"), dpi=110); plt.close(fig)
    # 5. axis profiles: phi_z(0,z) (S1 condition at 1/2), q(0,z), W_z(0,z), and axis residuals
    zz = np.linspace(-L, L, 801); Rz = np.abs(zz); Rz[Rz < 1e-9] = 1e-9; muz = np.sign(zz); muz[muz == 0] = 1
    fa = validate.fields(prob, x, Rz, muz)
    fig, axs = plt.subplots(1, 2, figsize=(11, 3.6))
    axs[0].plot(zz, -fa["Ur_over_r"], label="phi_z(0,z) = -U^r/r"); axs[0].axhline(0.5, color="k", ls=":"); axs[0].plot(zz, fa["q"], label="q(0,z)"); axs[0].plot(zz, prob.cl * zz + fa["Uz"], label="W_z(0,z)")
    axs[0].set_xlabel("z"); axs[0].legend(fontsize=7); axs[0].set_ylim(-3, 3); axs[0].set_title("axis profiles")
    axs[1].semilogy(zz, np.abs(fa["Rq"]) + 1e-300, label="|R_q| axis"); axs[1].semilogy(zz, np.abs(fa["Reta"]) + 1e-300, label="|R_eta| axis"); axs[1].legend(fontsize=7); axs[1].set_xlabel("z"); axs[1].set_title("axis residuals")
    fig.tight_layout(); fig.savefig(os.path.join(FIG, f"{jid}_axis.png"), dpi=110); plt.close(fig)
    return jid


def sweep_figures():
    rows = list(csv.DictReader(open(os.path.join(ROOT, "PARAMETER_SWEEP.csv"))))
    def fl(v):
        try: return float(v)
        except Exception: return float("nan")
    fig, axs = plt.subplots(1, 2, figsize=(11, 4))
    for br, mk in (("S1", "o"), ("S1free", "^"), ("S1pin_freecl", "D"), ("S1amp", "x"), ("S1_continue", "P"), ("T2", "v"), ("T3", "<"), ("generic", "s")):
        rr = [r for r in rows if r["branch"] == br]
        if not rr: continue
        axs[0].semilogy([fl(r["cl"]) for r in rr], [fl(r["rho_max_spec"]) if r["rho_max_spec"] else fl(r["rel_Reta"]) * 10 for r in rr], mk, ms=4, alpha=0.7, label=br)
        axs[1].plot([fl(r["cl"]) for r in rr], [fl(r["s_core_spec"]) if r["s_core_spec"] else fl(r["swirl_ratio"]) for r in rr], mk, ms=4, alpha=0.7, label=br)
    axs[0].set_xlabel("c_l"); axs[0].set_ylabel("SPEC rho_max (holdout)"); axs[0].legend(fontsize=7); axs[0].set_title("pilot sweep: residual metric vs c_l")
    axs[1].set_xlabel("c_l"); axs[1].set_ylabel("core swirl fraction s_core"); axs[1].axhline(0.05, color="k", ls=":"); axs[1].set_title("swirl fraction vs c_l")
    fig.tight_layout(); fig.savefig(os.path.join(FIG, "sweep_rho_and_swirl_vs_cl.png"), dpi=110); plt.close(fig)


if __name__ == "__main__":
    dirs = sys.argv[1:]
    if not dirs:
        rows = list(csv.DictReader(open(os.path.join(ROOT, "CANDIDATE_LEADERBOARD.csv"))))[:6]
        dirs = [os.path.join(ROOT, "runs", r["job_id"]) for r in rows]
    for dd in dirs:
        try:
            print("figures:", run_figures(dd))
        except Exception as ex:
            print("failed", dd, repr(ex))
    sweep_figures(); print("sweep figures written")
