#!/usr/bin/env python
"""PROMPT section 8 plots (lead 2026-10-25T06:47Z item 3), each with its data file (CSV) in reports/figures/: residual against resolution,
residual against radius (dyadic shells), spectral coefficient decay, non-axisymmetric content, parameter continuation, tail convergence, for the
leading states of the D6 lineage (c_l 0.45, omega 0.3) and the nest ladder. All values are the primary route's holdout diagnostics (start files
and ledger); they are diagnostics of approximate states, not validation. Usage: make_plots.py (CPU only)."""
import sys, os, json, math, csv, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from src.campaign import ledger
OUT = os.path.join(ROOT, "reports", "figures"); os.makedirs(OUT, exist_ok=True)
TS = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime())
STATES = {  # label: start file
    "d6t_L6 (D6 lineage, degree-L channels)": "runs/d6t_L6_cl0.45_om+0.3_fixed/starts/start_000.pt",
    "d6w3_L6 (D6 lineage, SPEC channels + closure rows)": "runs/d6w3_L6_cl0.45_om+0.3_fixed/starts/start_000.pt",
    "d6w_L8 (D6 lineage, SPEC channels)": "runs/d6w_L8_cl0.45_om+0.3_fixed/starts/start_000.pt",
    "nest4 (0.45, 1) L4": "runs/nest4_L4_cl0.45_om+1.0_fixed_p0_om+1.0s31/starts/start_000.pt",
    "nest6 (0.45, 0.3) p0 L6": "runs/nest6_L6_cl0.45_om+0.3_fixed_p0_om+0.3s55s0/starts/start_000.pt",
    "nest6 (0.45, 0.3) p1 L6": "runs/nest6_L6_cl0.45_om+0.3_fixed_p1_om+0.3s16s0/starts/start_000.pt",
}
def load(rel):
    return torch.load(os.path.join(ROOT, rel), map_location="cpu", weights_only=False)
def gauss_radii(edges, n=6):
    xg, _ = np.polynomial.legendre.leggauss(n); out = []
    for (a, b) in edges:
        out.append(0.5 * (b - a) * xg + 0.5 * (a + b))
    return np.concatenate(out)
def write_csv(name, header, rows):
    with open(os.path.join(OUT, name), "w", newline="") as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)
states = {k: load(v) for k, v in STATES.items() if os.path.exists(os.path.join(ROOT, v))}
# ---- 1. residual against radius (dyadic shells): per-shell rho_u and RMS R_u (holdout, standard family)
fig, ax = plt.subplots(1, 2, figsize=(12, 4.5)); rows = []
for lab, S in states.items():
    sd = S["spec_diag_holdout"]; ed = sd["shells"]["edges"]; rmid = [math.sqrt(max(a, b / 64) * b) for a, b in ed]
    rho = [v if v is not None else np.nan for v in sd["rho_u"]]; rms = sd["rms"]["R_u"]
    ax[0].loglog(rmid, rho, "o-", ms=3, label=lab); ax[1].loglog(rmid, rms, "o-", ms=3, label=lab)
    rows += [[lab, a, b, r, rh, rm] for (a, b), r, rh, rm in zip(ed, rmid, rho, rms)]
ax[0].set_xlabel("shell geometric midpoint r"); ax[0].set_ylabel("rho_u per shell (holdout)"); ax[0].set_title("Residual against radius: rho_u = RMS(R_u)/sum of five term RMS")
ax[1].set_xlabel("shell geometric midpoint r"); ax[1].set_ylabel("RMS(R_u) per shell"); ax[1].set_title("Absolute momentum residual per dyadic shell")
ax[0].legend(fontsize=6); fig.tight_layout(); fig.savefig(os.path.join(OUT, "residual_vs_radius.png"), dpi=130); plt.close(fig)
write_csv("residual_vs_radius.csv", ["state", "r_lo", "r_hi", "r_mid", "rho_u", "rms_R_u"], rows)
# ---- 2. tail convergence: E_F(r) = ||U - r^-alpha F_twisted|| / ||r^-alpha F|| on the holdout radii
fig, ax = plt.subplots(figsize=(7, 4.5)); rows = []
for lab, S in states.items():
    sd = S["spec_diag_holdout"]; r = gauss_radii(sd["shells"]["edges"], len(sd["E_F"]) // len(sd["shells"]["edges"]))
    EF = np.array(sd["E_F"]); ax.loglog(r, np.maximum(EF, 1e-16), "-", lw=1, label=lab)
    rows += [[lab, float(rv), float(ev)] for rv, ev in zip(r, EF)]
ax.set_xlabel("r"); ax.set_ylabel("E_F(r) = ||U - U_0||/||U_0|| on the sphere"); ax.set_title("Tail convergence to the untwisted leading field r^-alpha F(theta, chi)")
ax.legend(fontsize=6); fig.tight_layout(); fig.savefig(os.path.join(OUT, "tail_convergence.png"), dpi=130); plt.close(fig)
write_csv("tail_convergence.csv", ["state", "r", "E_F"], rows)
# ---- 3. non-axisymmetric content: e_k per shell (core) and tail m-energy fractions
fig, ax = plt.subplots(1, 2, figsize=(12, 4.5)); rows = []
for lab, S in states.items():
    sd = S["spec_diag_holdout"]; ed = sd["shells"]["edges"]; rmid = [math.sqrt(max(a, b / 64) * b) for a, b in ed]
    ek = [v if v is not None else np.nan for v in sd["e_k"]]
    ax[0].semilogx(rmid, ek, "o-", ms=3, label=lab)
    bym = S["diag"]["tail"]["by_m"]; ms = sorted(int(k) for k in bym); fr = [bym[str(m)] if str(m) in bym else bym[m] for m in ms]; tot = sum(fr)
    ax[1].bar([m + 0.12 * list(states).index(lab) for m in ms], [v / tot for v in fr], width=0.12, label=lab)
    rows += [[lab, "e_k", a, b, v] for (a, b), v in zip(ed, ek)] + [[lab, f"tail_m{m}", "", "", v / tot] for m, v in zip(ms, fr)]
ax[0].set_xlabel("shell midpoint r"); ax[0].set_ylabel("e_k = RMS(U - <U>_phi)^2 / RMS(U)^2"); ax[0].set_title("Non-axisymmetric energy fraction per shell")
ax[1].set_xlabel("azimuthal order m"); ax[1].set_ylabel("tail energy fraction"); ax[1].set_title("Leading-tail energy by m (gauge int |F|^2 = 1)")
ax[0].legend(fontsize=6); fig.tight_layout(); fig.savefig(os.path.join(OUT, "nonaxisymmetric_content.png"), dpi=130); plt.close(fig)
write_csv("nonaxisymmetric_content.csv", ["state", "quantity", "r_lo", "r_hi", "value"], rows)
# ---- 4. spectral coefficient decay: leading channels A (toroidal) and C (poloidal): max |a_kq| over modes per Chebyshev index k, and energy per degree l
fig, ax = plt.subplots(1, 2, figsize=(12, 4.5)); rows = []
from src.equations.fields import Model
for lab, S in states.items():
    cfg = S["config"]
    model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg["R0"], Nr=cfg["Nr"], c_l=cfg["c_l"], omega=cfg["omega"], channels=cfg.get("channels"), device="cpu")
    d = model.unpack_all(S["z"])
    A, C = d["A"].numpy(), d["C"].numpy(); l = model.l_arr.numpy()
    dec = np.maximum(np.abs(A), np.abs(C)).max(1)
    ax[0].semilogy(np.arange(len(dec)), dec / dec.max(), "o-", ms=3, label=lab)
    el = {}
    for q in range(A.shape[1]):
        el[int(l[q])] = el.get(int(l[q]), 0.0) + float((A[:, q] ** 2).sum() + (C[:, q] ** 2).sum())
    ls = sorted(el); tot = sum(el.values())
    ax[1].semilogy(ls, [el[v] / tot for v in ls], "s-", ms=3, label=lab)
    rows += [[lab, "cheb_k", k, float(v / dec.max())] for k, v in enumerate(dec)] + [[lab, "degree_l", v, el[v] / tot] for v in ls]
ax[0].set_xlabel("Chebyshev index k"); ax[0].set_ylabel("max_q |a_kq| / max (A and C channels)"); ax[0].set_title("Radial spectral coefficient decay")
ax[1].set_xlabel("spherical degree l"); ax[1].set_ylabel("coefficient energy fraction per l"); ax[1].set_title("Angular degree spectrum of the leading potentials")
ax[0].legend(fontsize=6); fig.tight_layout(); fig.savefig(os.path.join(OUT, "spectral_decay.png"), dpi=130); plt.close(fig)
write_csv("spectral_decay.csv", ["state", "quantity", "index", "value"], rows)
# ---- 5. residual against resolution: holdout rho_u^max and sigma_u^max per L along the two ladders (ledger)
recs = ledger.merge_reevaluations(ledger.read(os.path.join(ROOT, "status", "ledger.jsonl")))
def best(prefixes, L):
    rs = [r for r in recs if r.get("L") == L and any(str(r.get("job_id", "")).startswith(p) for p in prefixes) and r.get("rho_u_max_holdout") and not r.get("failure") and (r.get("e_F") is None or r["e_F"] > 1e-4)]
    return min(rs, key=lambda r: r["rho_u_max_holdout"]) if rs else None
ladders = {"D6 lineage (d6t/d6w/d6w3, c_l 0.45, omega 0.3)": (["d6t_", "d6w_", "d6w3_", "d6w4_"], [6, 8]),
           "nest ladder (0.45, 0.3)": (["nest2_L2_cl0.45_om+0.3", "nest4_L4_cl0.45_om+0.3", "nest6_L6_cl0.45_om+0.3"], [2, 4, 6]),
           "nest ladder (0.45, 1)": (["nest2_L2_cl0.45_om+1.0", "nest4_L4_cl0.45_om+1.0", "nest6_L6_cl0.45_om+1.0"], [2, 4, 6]),
           "from-scratch c2x2c (0.47, 1)": (["c2x2c_"], [6, 8])}
fig, ax = plt.subplots(1, 2, figsize=(12, 4.5)); rows = []
for lab, (pref, Ls) in ladders.items():
    xs, ys, ss = [], [], []
    for L in Ls:
        b = best(pref, L)
        if b is None: continue
        xs.append(L); ys.append(b["rho_u_max_holdout"]); ss.append(b.get("sigma_u_max") or np.nan)
        rows.append([lab, L, b["job_id"], b["start"], b["rho_u_max_holdout"], b.get("rho_u_max_holdout_half"), b.get("sigma_u_max"), b.get("a_max"), b.get("iterations"), b.get("seconds")])
    if xs:
        ax[0].semilogy(xs, ys, "o-", label=lab); ax[1].semilogy(xs, ss, "s-", label=lab)
ax[0].set_xlabel("maximum spherical degree L"); ax[0].set_ylabel("best holdout rho_u^max"); ax[0].set_title("Residual against resolution (best state per level)")
ax[1].set_xlabel("L"); ax[1].set_ylabel("sigma_u^max = max_k RMS(R_u)/RMS((1-c_l)U)"); ax[1].set_title("Single-term ratio against resolution")
ax[0].legend(fontsize=6); fig.tight_layout(); fig.savefig(os.path.join(OUT, "residual_vs_resolution.png"), dpi=130); plt.close(fig)
write_csv("residual_vs_resolution.csv", ["ladder", "L", "job_id", "start", "rho_u_max_holdout_std", "rho_u_max_holdout_half", "sigma_u_max", "a_max", "iterations", "seconds"], rows)
# ---- 6. parameter continuation: fixed-omega c_l scan (d6scan) and the free-parameter arms' end points
fig, ax = plt.subplots(1, 2, figsize=(12, 4.5)); rows = []
scan = [r for r in recs if str(r.get("job_id", "")).startswith("d6scan") and r.get("rho_u_max_holdout")] + [r for r in recs if str(r.get("job_id", "")).startswith("d6t_L6") and r.get("rho_u_max_holdout")]
scan = sorted({(round(r["c_l"], 4)): r for r in scan}.values(), key=lambda r: r["c_l"])
ax[0].plot([r["c_l"] for r in scan], [r["rho_u_max_holdout"] for r in scan], "o-", label="holdout rho_u^max (std)")
ax[0].plot([r["c_l"] for r in scan], [r.get("rho_u_max_holdout_half") or np.nan for r in scan], "s--", label="half-offset family")
ax[0].set_xlabel("c_l (omega = 0.3 fixed; warm starts from d6t_L6 at 0.45)"); ax[0].set_ylabel("holdout rho_u^max"); ax[0].set_title("Fixed-omega continuation in c_l (D6 lineage)"); ax[0].legend(fontsize=7)
rows += [["d6scan", r["job_id"], r["c_l"], r["omega"], r["rho_u_max_holdout"], r.get("rho_u_max_holdout_half")] for r in scan]
free = [r for r in recs if ("_free" in str(r.get("job_id", ""))) and r.get("rho_u_max_holdout") and r.get("c_l") is not None]
for r in free:
    ax[1].annotate(r["job_id"].split("_cl")[0], (r["c_l"], r["omega"]), fontsize=6)
    rows.append(["free_arm_end", r["job_id"], r["c_l"], r["omega"], r["rho_u_max_holdout"], r.get("rho_u_max_holdout_half")])
ax[1].scatter([r["c_l"] for r in free], [r["omega"] for r in free], c=[r["rho_u_max_holdout"] for r in free], cmap="viridis", s=30)
ax[1].axvline(0.5, color="k", lw=0.5); ax[1].axvline(0.4, color="k", lw=0.5); ax[1].set_xlabel("final c_l"); ax[1].set_ylabel("final omega"); ax[1].set_title("Free-parameter arms: end points (colour = holdout rho_u^max; rank only after fixed evaluation)")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "parameter_continuation.png"), dpi=130); plt.close(fig)
write_csv("parameter_continuation.csv", ["kind", "job_id", "c_l", "omega", "rho_u_max_holdout_std", "rho_u_max_holdout_half"], rows)
open(os.path.join(OUT, "README.md"), "w").write(f"""# Figures and data files (generated {TS} by scripts/make_plots.py)

Primary-route holdout diagnostics of approximate states (not validation; no state is a profile). Each PNG has a CSV with the plotted values.
- residual_vs_radius.png/.csv: per-shell rho_u and RMS(R_u) on the standard dyadic family for the leading states of both groups.
- tail_convergence.png/.csv: E_F(r) = ||U - r^-alpha F(theta, chi)||/||r^-alpha F|| on the holdout radii (untwisted leading field).
- nonaxisymmetric_content.png/.csv: e_k per shell and the leading-tail energy by azimuthal order m.
- spectral_decay.png/.csv: radial Chebyshev coefficient decay (max over modes, A and C channels) and the angular degree spectrum.
- residual_vs_resolution.png/.csv: best holdout rho_u^max and sigma_u^max per L along the D6 lineage, the nest ladders and the from-scratch c2x2c arm.
- parameter_continuation.png/.csv: fixed-omega c_l scan (d6scan) and the free-parameter arms' end points.
Energy-flux and helicity profiles: lead lane figures/balance_profiles.png (theory-route evaluation on primary samples); the d64 balances per state are in the shortlist.
States: {', '.join(STATES)}.
""")
print("figures written to", OUT, "at", TS)
