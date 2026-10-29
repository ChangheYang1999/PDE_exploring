"""Markdown table of one branch's runs (job id prefix list): c_l, q0 pin, level (D/nmax/K/Rm), iterations, SPEC rho_max and its equation,
rho_M, s_core, s_far, holdout relative residuals of q and eta.  Usage: python3 scripts/branch_table.py <prefix> [<prefix> ...]"""
import os, sys, json, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
import numpy as np, torch
from numpy.polynomial import legendre as L
from axi.problem import Problem
from axi import validate
torch.set_default_dtype(torch.float64)


def tail_signs(run_dir, r):
    """min over mu of the leading far swirl coefficient B(mu) relative to max |B|, and the sign of eta on the far upper axis."""
    try:
        t = r["report"]["tail"]; B = np.array(t["B_legendre"]); mu = np.linspace(-1, 1, 401); Bv = L.legval(mu, B)
        minB = float(np.min(Bv) / max(np.max(np.abs(Bv)), 1e-300))
        d = torch.load(os.path.join(run_dir, "final.pt"), weights_only=False, map_location="cpu"); prob, x = Problem.from_state(d, device="cpu")
        R = np.array([50.0, 200.0, 1000.0]); f = validate.fields(prob, x, R, np.ones(3), prob.cl_of(x))
        ij, where = interface_derivative_jump(prob, x)
        return minB, "".join("+" if v > 0 else "-" for v in f["eta"]), ij, where
    except Exception as ex:
        return float("nan"), "?", float("nan"), repr(ex)[:40]


def interface_derivative_jump(prob, x):
    """SPEC 6.5 interface measure (diagnostics.interface_jumps_spec65): phi to total order 3, q to order 2, 64 angular points, relative to
    the scale of the same derivative on the interface."""
    from axi import diagnostics
    w, where, _ = diagnostics.interface_jumps_spec65(prob, x)
    return w, where


def failure_class(run_dir, r):
    """SPEC 9.1 classes as in scripts/failure_map.py: F1 swirl collapse (B2 fails), F6 no cost decrease over the last 20 percent of the
    iterations, F5 interface defect > 1e-3, else F7 plateau."""
    v = r.get("validation") or {}; rep = r.get("report", {})
    s_core, s_far = v.get("s_core"), v.get("s_far")
    if not (s_core is not None and s_far is not None and s_core >= 0.05 and s_far >= 0.05):
        return "F1"
    try:
        h = torch.load(os.path.join(run_dir, "final.pt"), weights_only=False, map_location="cpu").get("history", [])
        c = [x["cost"] for x in h if "cost" in x]
        if len(c) >= 10 and c[-1] / max(c[int(0.8 * len(c))], 1e-300) > 0.99:
            return "F6"
    except Exception:
        pass
    ifc = rep.get("interfaces", [])
    if max([d["dphi"] / max(d["phi_scale"], 1e-300) for d in ifc], default=0.0) > 1e-3:
        return "F5"
    return "F7"


def exterior_labels(cfg, cl):
    """Exterior exponent set of phi at the final c_l (merge_tol applied), as m*alpha+k labels, plus the parity restriction."""
    from axi import basis
    alpha = (1.0 - cl) / cl
    ex = basis.exterior_exponents(alpha, cfg["emax"], "phi", cfg.get("merge_tol", 0.03))
    par = f" parity phi {cfg.get('parity_phi')}/q {cfg.get('parity_q')}" if cfg.get("parity_phi") or cfg.get("parity_q") else ""
    return " ".join(f"{e:.3f}" for e in ex) + f" (tol {cfg.get('merge_tol', 0.03)}){par}"


rows = []
for pref in sys.argv[1:]:
    for f in glob.glob(os.path.join(ROOT, "runs", pref + "*", "result.json")):
        r = json.load(open(f)); v = r.get("validation") or {}; rep = r.get("report", {}); cfg = r["cfg"]
        eq = max(v.get("rho_max_by_eq", {"?": 0}).items(), key=lambda t: (t[1] if t[1] == t[1] else -1))[0] if v.get("rho_max_by_eq") else "?"
        vf = f.replace("result.json", "validation.json")
        t1 = {}
        if os.path.exists(vf):
            t1 = (json.load(open(vf)).get("stagnation") or {}).get("t1_diagnostics") or {}
        minB, esign, ij, ijw = tail_signs(os.path.dirname(f), r)
        fcls = failure_class(os.path.dirname(f), r); ext = exterior_labels(cfg, r["cl"])
        rows.append((v.get("rho_max", float("nan")), dict(job=r["job_id"], cl=r["cl"], q0=cfg.get("q0_pin"), minB=minB, esign=esign, fcls=fcls, ext=ext, ij=ij, ijw=ijw, pz=t1.get("p_z", float("nan")), ps=t1.get("p_s", float("nan")),
                     jr=t1.get("jet_ratio", float("nan")), jrt=t1.get("jet_ratio_target", float("nan")), qmaxK=t1.get("max_abs_q_over_K", float("nan")), level=f"D{cfg['D']}/n{cfg['nmax']}/K{cfg['shells'][-1][1]}/Rm{cfg['shells'][-1][0]:g}",
                     it=r.get("n_iter"), rho=v.get("rho_max", float("nan")), eq=eq, rhoM=v.get("rho_M_max", float("nan")), sc=v.get("s_core", float("nan")), sf=v.get("s_far", float("nan")),
                     relq=rep.get("rel_Rq_inner", float("nan")), rele=rep.get("rel_Reta_inner", float("nan")), st="/".join(s["status"] for s in r.get("stage_status", [])))))
rows.sort(key=lambda t: t[1]["job"])
print("Iteration counts: the 'iterations' columns and n_iter are len(history) of the run record; for the six runs resumed on CPU inside an LM stage after the GPU withdrawal (fmA_cl0p73, fmAL0_cl0p74, refl_D36_cl0p74_q3p5, refl_D48_cl0p74_q3p5, refl_D36_cl0p749_q3p5, refl_D48_cl0p749_q3p5) this double counts the checkpoint prefix; the actual LM iteration counts (1500, 2500, 2500, 1600, 2500, 1600) and the recomputed last-20-percent cost ratios are in docs/RESUME_HISTORY_QUALIFICATION.md (recorded 2026-10-29T12:36Z; no class changes)."); print()
print("| run | c_l | q0 pin | level | iterations (this run) | rho_max (eq) | rho_M | s_core | s_far | rel R_q | rel R_eta | p_z | p_s | jet ratio (target) | max q / K | min B/max|B| | eta sign upper axis R=50,200,1000 | stop | SPEC 9.1 class | SPEC 6.5 interface jump (phi order <= 3 incl. mu, q order <= 2; same-derivative scale, 64 angles) | exterior exponents of phi (final c_l) |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for _, d in rows:
    print(f"| {d['job'][:46]} | {d['cl']:.4f} | {d['q0']} | {d['level']} | {d['it']} | {d['rho']:.2f} ({d['eq']}) | {d['rhoM']:.2f} | {d['sc']:.2f} | {d['sf']:.2f} | {d['relq']:.3f} | {d['rele']:.4f} | {d['pz']:+.3f} | {d['ps']:+.3f} | {d['jr']:.2f} ({d['jrt']:.2f}) | {d['qmaxK']:.2f} | {d['minB']:+.2f} | {d['esign']} | {d['st']} | {d['fcls']} | {d['ij']:.1e} ({d['ijw']}) | {d['ext']} |")
