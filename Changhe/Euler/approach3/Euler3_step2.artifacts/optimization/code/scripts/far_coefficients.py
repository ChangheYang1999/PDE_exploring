#!/usr/bin/env python
"""First far-field coefficients of every export (SPEC v1.24 7.8; lead 2026-10-25T09:58Z items 1-3 and 10:12Z): for each candidates/<id> load the source
start, compute the SPEC 4.4 closure block with the direct energy ratio K_E(carried)/K_E(required), the helicity coefficients K_H(required),
K_H(carried) and their ratio, the vector defect m = ||G_carried - G_required||/||G_required|| with its component along F and its orthogonal part.
The exports stay immutable: the block is written to candidates/<id>/meta_supplement_v124.json (meta.json and SHA256.json untouched) and the table to
reports/FAR_COEFFICIENTS.md. Usage: far_coefficients.py [--device cuda:0|cpu] [--only id1,id2] [--skip-heavy]"""
import sys, os, json, time, argparse, math
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.far_field.correction import closure_distance
ap = argparse.ArgumentParser(); ap.add_argument("--device", default="cuda:0" if torch.cuda.is_available() else "cpu"); ap.add_argument("--only", default=None)
ap.add_argument("--skip-heavy", action="store_true", help="skip L >= 8 states"); ap.add_argument("--no-write", action="store_true")
a = ap.parse_args()
cdir = os.path.join(ROOT, "candidates")
ids = sorted(os.listdir(cdir)) if a.only is None else a.only.split(",")
rows = []
for cid in ids:
    mp = os.path.join(cdir, cid, "meta.json")
    if not os.path.exists(mp):
        continue
    meta = json.load(open(mp)); zf = os.path.join(ROOT, meta["source_start"])
    if not os.path.exists(zf):
        print(f"{cid}: source start missing ({meta['source_start']})"); continue
    S = torch.load(zf, map_location="cpu", weights_only=False); cfg = S["config"]
    if a.skip_heavy and cfg["L"] >= 8:
        print(f"{cid}: skipped (L {cfg['L']})"); continue
    dev = a.device if cfg["L"] < 8 or a.device == "cpu" else "cpu"          # L8 models are built on the CPU (a GPU shared with a running job must not be loaded)
    t0 = time.time(); z = S["z"].to(dev)
    model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"], free_params=S.get("free_params", False), channels=cfg.get("channels"), device=dev)
    prob = Problem(model, formulation="mom")
    g = closure_distance(prob, z)
    g = {k: (v.tolist() if torch.is_tensor(v) else v) for k, v in g.items()}
    secs = time.time() - t0
    sup = dict(candidate_id=cid, source_start=meta["source_start"], c_l=cfg["c_l"], omega=cfg["omega"], omega_over_c_l=cfg["omega"] / cfg["c_l"], computed=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               spec="SPEC v1.24 7.8 (K_H), SPEC 4.4 closure, lead d84 / 10:12Z defect decomposition", G_closure_v124=g, seconds=secs, device=dev,
               note="supplement to meta.json (which stays immutable with its SHA256 manifest); an approximate state, not an exact profile")
    if not a.no_write:
        tmp = os.path.join(cdir, cid, "meta_supplement_v124.json.tmp"); json.dump(sup, open(tmp, "w"), indent=1, default=str); os.replace(tmp, os.path.join(cdir, cid, "meta_supplement_v124.json"))
    rows.append((cid, cfg, g, secs))
    f = lambda v, p="%.4f": (p % v) if isinstance(v, (int, float)) else "n/a"
    print(f"{cid} (L {cfg['L']}, c_l {cfg['c_l']}, omega {cfg['omega']}, omega/c_l {cfg['omega']/cfg['c_l']:.4f}; {secs:.0f}s on {dev}): K_E ratio {f(g.get('K_ratio_direct'))} | K_H required {f(g.get('K_H_required'))} carried {f(g.get('K_H_carried'))} ratio {f(g.get('K_H_ratio_direct'))} "
          f"(identity closure {f(g.get('K_H_identity_rel_closure'), '%.1e')}, two forms {f(g.get('K_H_carried_two_forms_rel'), '%.1e')}) | m {f(g.get('carried_mismatch_rel'), '%.3f')} along F {f(g.get('G_defect_parallel_rel'), '%.3f')} orth {f(g.get('G_defect_orth_rel'), '%.3f')} cos_F {f(g.get('G_defect_cos_F'), '%.3f')} | H_F {f(g.get('H_F_tail'))} {g.get('K_H_error') or ''} {g.get('carried_error') or ''}")
    sys.stdout.flush()
    del model, prob
    if dev != "cpu":
        torch.cuda.empty_cache()
if rows and not a.no_write:                      # the table is built from EVERY stored supplement (not only the ids processed in this call)
    rows = []
    for cid in sorted(os.listdir(cdir)):
        sp = os.path.join(cdir, cid, "meta_supplement_v124.json")
        if os.path.exists(sp):
            try:
                sup_ = json.load(open(sp)); rows.append((cid, dict(L=json.load(open(os.path.join(cdir, cid, "meta.json")))["L_max"], c_l=sup_["c_l"], omega=sup_["omega"]), sup_["G_closure_v124"], sup_.get("seconds", 0)))
            except Exception as e:
                print(f"{cid}: supplement unreadable ({e!r})")
    L = [f"# First far-field coefficients of the exports (SPEC v1.24 7.8; generated {time.strftime('%Y-%m-%dT%H:%MZ', time.gmtime())})", "",
         "Primary-route values on the exact homogeneous tail fields at r = R0 (far_field.correction.far_helicity_coefficients). K_E ratio = <F, G_carried>/<F, G_required> (exact profile 1);",
         "K_H(required) = (1 - 3 alpha) Psi_F, K_H(carried) = 2 int G_c.H - (1 - 3 alpha) int n.(F x G_c) (sphere form; the direct curl form agrees to the stated figure); exact profile: ratio 1 where the",
         "required value is nonzero. m = ||G_carried - G_required||/||G_required||; 'along F' and 'orthogonal' are the norms of the two parts of the defect relative to ||G_required|| (lead 10:12Z:",
         "both parts are of the same radial order; neither is negligible). States without B/D channels carry 0 and fail both coefficients at order one. Diagnostics of approximate states;",
         "the independent route confirmed all eight K_H rows of the lead's d78 table (verifier 2026-10-25T09:56Z and 10:15Z) to 5e-14 to 4e-12 relative against these values, with the six vector mismatches and perpendicular fractions to seven digits.", "",
         "| export | L | c_l | omega | omega/c_l | K_E ratio (direct) | K_H required | K_H carried | K_H ratio | identity closure | m | along F | orthogonal | cos(defect, F) | H_F (tail) | d84 bound m/c |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    f = lambda v, p="%.4f": (p % v) if isinstance(v, (int, float)) else "n/a"
    for cid, cfg, g, secs in rows:
        L.append(f"| {cid} | {cfg['L']} | {cfg['c_l']} | {cfg['omega']} | {cfg['omega']/cfg['c_l']:.4f} | {f(g.get('K_ratio_direct'), '%.3f')} | {f(g.get('K_H_required'))} | {f(g.get('K_H_carried'))} | {f(g.get('K_H_ratio_direct'), '%.4f')} | {f(g.get('K_H_identity_rel_closure'), '%.1e')} | {f(g.get('carried_mismatch_rel'), '%.3f')} | {f(g.get('G_defect_parallel_rel'), '%.3f')} | {f(g.get('G_defect_orth_rel'), '%.3f')} | {f(g.get('G_defect_cos_F'), '%.3f')} | {f(g.get('H_F_tail'))} | {f(g.get('d84_bound_energy_ratio'), '%.2f')} |")
    open(os.path.join(ROOT, "reports", "FAR_COEFFICIENTS.md"), "w").write("\n".join(L) + "\n")
    print("wrote reports/FAR_COEFFICIENTS.md")
