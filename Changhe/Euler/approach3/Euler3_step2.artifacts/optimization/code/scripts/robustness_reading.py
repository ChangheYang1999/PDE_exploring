#!/usr/bin/env python
"""Reading of one registered robustness re-solve against its same-budget control (reports/STAGE2_ROBUSTNESS_REGISTRATION_20261026.md).

Steps: (1) scripts/arm_reading.py --json for the control and the variant when their JSONs are absent (ledger rows of the end states);
(2) scripts/compare_fields.py <control start> <variant start> (SPEC 7.10; the re-solved CONTROL is the reference; CPU);
(3) the registered readings: variant / control ratios of the standing quantities, the representation-dependence flag (||V||_* above the
control's holdout rho_u^max on the standard family = 'moves the re-solved state by more than its residual level'), and for --kind far the
SPEC 7.11 X3 criteria (X3a holdout rho_u^max within a factor 2 on both families; X3b rho_nl^max within a factor 2 on both families; X3c far-sphere
U ratio at most the control's holdout rho_u^max and the carried K_E and K_H ratios within 0.1 of the control's). Every criterion is reported
met / not met with its numbers; nothing is ranked. Output: reports/robustness_<variant>.json and a markdown block on stdout.
Usage: CUDA_VISIBLE_DEVICES=-1 OMP_NUM_THREADS=4 .venv/bin/python scripts/robustness_reading.py --control <job_id> --variant <job_id> --kind r0|far"""
import sys, os, json, math, argparse, subprocess, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PY = os.path.join(ROOT, ".venv", "bin", "python")
ap = argparse.ArgumentParser()
ap.add_argument("--control", required=True); ap.add_argument("--variant", required=True); ap.add_argument("--kind", choices=["r0", "far"], required=True)
ap.add_argument("--far", default="4096,16384,65536", help="far spheres (units of the CONTROL's R0) for the comparison")
ap.add_argument("--redo", action="store_true", help="recompute the arm readings and the comparison even if their JSONs exist")
ap.add_argument("--original", default=None, help="job id of the ORIGINAL start state (e.g. nest6 p0): adds the optimization-drift comparison original -> continued control")
a = ap.parse_args()
env = dict(os.environ, CUDA_VISIBLE_DEVICES="-1"); env.setdefault("OMP_NUM_THREADS", "4")


def arm(job):
    fn = os.path.join(ROOT, "reports", f"arm_reading_{job}.json")
    if a.redo or not os.path.exists(fn):
        subprocess.run([PY, os.path.join(ROOT, "scripts", "arm_reading.py"), job, "--json"], cwd=ROOT, env=env, check=True, stdout=subprocess.DEVNULL)
    return json.load(open(fn))


def start_of(job, row=None):
    """The end state file: the ledger row's zfile when present, else runs/<job>/starts/start_000.pt."""
    p = None
    if row and row.get("zfile"):
        p = row["zfile"] if os.path.isabs(row["zfile"]) else os.path.join(ROOT, row["zfile"])
    if p is None or not os.path.exists(p):
        p = os.path.join(ROOT, "runs", job, "starts", "start_000.pt")
    if not os.path.exists(p):
        raise SystemExit(f"missing start file {p}")
    return p


def sha256(p):
    import hashlib
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def finite(v):
    return v is not None and isinstance(v, (int, float)) and math.isfinite(v)


C = arm(a.control); V = arm(a.variant)
rc, rv = C["row"], V["row"]
sc, sv = start_of(a.control, rc), start_of(a.variant, rv)
hashes = dict(control=sha256(sc), variant=sha256(sv))
complete = all(rr.get("status") in ("max_iter", "ftol", "xtol", "converged", "time_limit") and not rr.get("failure") and finite(rr.get("rho_u_max_holdout")) for rr in (rc, rv))
cmp_json = os.path.join(ROOT, "reports", f"cmp_{a.variant}__vs__{a.control}.json")
if a.redo or not os.path.exists(cmp_json):
    subprocess.run([PY, os.path.join(ROOT, "scripts", "compare_fields.py"), sc, sv, "--json", cmp_json, "--far", a.far],
                   cwd=ROOT, env=env, check=True, stdout=subprocess.DEVNULL)
cmp = json.load(open(cmp_json))
if cmp.get("ref") not in (sc, os.path.relpath(sc, ROOT)) or cmp.get("other") not in (sv, os.path.relpath(sv, ROOT)):
    print("WARNING: the cached comparison JSON names other state files; use --redo", file=sys.stderr)
drift = None
if a.original:
    so = start_of(a.original)
    drift_json = os.path.join(ROOT, "reports", f"cmp_{a.control}__vs_original__{a.original}.json")
    if a.redo or not os.path.exists(drift_json):
        subprocess.run([PY, os.path.join(ROOT, "scripts", "compare_fields.py"), so, sc, "--json", drift_json, "--far", a.far], cwd=ROOT, env=env, check=True, stdout=subprocess.DEVNULL)
    dj = json.load(open(drift_json))
    drift = dict(original=a.original, json=os.path.relpath(drift_json, ROOT), norm_star_U=dj["norm_star_U"], norm_star1_DU=dj["norm_star1_DU"], norm_star1_Om=dj["norm_star1_Om"], gamma=dj["rotation"]["gamma"])
# per-shell holdout rho_u on the shells with identical edges (the states' own holdout batteries; both are max-over-shells quantities whose shell sets differ when R0 or far_radii differ)
common_shells = []
try:
    import torch
    Sc = torch.load(sc, map_location="cpu", weights_only=False); Sv = torch.load(sv, map_location="cpu", weights_only=False)
    hc, hv = Sc.get("spec_diag_holdout") or {}, Sv.get("spec_diag_holdout") or {}
    ec = [tuple(e) for e in hc["shells"]["edges"]]; ev = [tuple(e) for e in hv["shells"]["edges"]]
    for i, e in enumerate(ec):
        if e in ev:
            j = ev.index(e)
            common_shells.append(dict(edges=e, rho_u_control=hc["rho_u"][i], rho_u_variant=hv["rho_u"][j], ratio=(hv["rho_u"][j] / hc["rho_u"][i] if hc["rho_u"][i] else None)))
    only_c = [e for e in ec if e not in ev]; only_v = [e for e in ev if e not in ec]
except Exception as e:
    only_c = only_v = None; print(f"per-shell holdout comparison unavailable: {e!r}", file=sys.stderr)
far_n = len(cmp["grid"]["far"]); far_ratios = cmp["per_shell"]["ratio_U"][-far_n:] if far_n else []
far_labels = cmp["shells"][-far_n:] if far_n else []


def g(r, k):
    v = r.get(k)
    return None if v is None else float(v)


def ratio(k):
    cv, vv = g(rc, k), g(rv, k)
    return None if (cv is None or vv is None or cv == 0) else vv / cv


keys = [("holdout rho_u^max std", "rho_u_max_holdout"), ("holdout rho_u^max half", "rho_u_max_holdout_half"), ("rho_nl^max holdout std", "rho_nl_max_holdout"),
        ("rho_nl^max holdout half", "rho_nl_max_holdout_half"), ("single-sphere rho_u max", "sphere_rho_u_max"), ("rho_lin^max holdout", "rho_lin_max_holdout"),
        ("sigma_u^max std", "sigma_u_max"), ("sigma_u^max half", "sigma_u_max_half"), ("sigma_u^max core sets", "sigma_u_max_core"), ("sigma_Om", "sigma_Om"),
        ("a_max std", "a_max"), ("a_max half", "a_max_half"), ("a_max core sets", "a_max_core"), ("a_eff", "a_eff"), ("strain ratio at located max", "located_strain_ratio"),
        ("holdout rho_Om^max", "rho_Om_max_holdout"), ("sampled Q_sw", "Q_sw"), ("e_core holdout", "e_core_holdout"), ("e_F", "e_F"), ("N_core", "N_core"), ("N_F", "N_F"),
        ("E_ren", "E_ren"), ("H_tot/int|h|", "H_tot_over_abs"), ("max E_F", "E_F_max"), ("K_E ratio carried/required", "K_ratio_direct"), ("K_H ratio", "K_H_ratio_direct"),
        ("carried mismatch m", "G_carried_mismatch_rel"), ("radial-lambda share", "radial_lambda_share"), ("rotation content", "rotation_content_rel"),
        ("max|U|", "max_U"), ("max|Omega|", "max_abs_Omega"), ("V10 last-tenth decrease", "v10_last_tenth_rel_decrease"), ("F-gauge int|F|^2", "F_norm2"),
        ("iterations", "iterations"), ("LM seconds", "seconds")]
table = []
for name, k in keys:
    table.append(dict(name=name, key=k, control=g(rc, k), variant=g(rv, k), ratio=ratio(k)))
ctl_rho = g(rc, "rho_u_max_holdout")
flag = "unevaluated (incomplete battery, failure or non-finite value)"
if complete and finite(ctl_rho) and finite(cmp.get("norm_star_U")):
    flag = ("field discrepancy above the registered residual-number threshold: the change moves the re-solved state by more than the control's holdout rho_u^max"
            if cmp["norm_star_U"] > ctl_rho else "field discrepancy below the registered residual-number threshold (the control's holdout rho_u^max)")
out = dict(control=a.control, variant=a.variant, kind=a.kind, utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           control_status=rc.get("status"), variant_status=rv.get("status"), control_failure=rc.get("failure"), variant_failure=rv.get("failure"),
           R0=dict(control=cmp["R0"][0], variant=cmp["R0"][1]), far_radii=dict(control=rc.get("far_radii"), variant=rv.get("far_radii")),
           compare=dict(json=os.path.relpath(cmp_json, ROOT), gamma=cmp["rotation"]["gamma"], norm_star_U=cmp["norm_star_U"], norm_star1_DU=cmp["norm_star1_DU"],
                        norm_star1_Om=cmp["norm_star1_Om"], far_sphere_ratio_U=dict(zip(far_labels, far_ratios)), F_norm2=cmp.get("F_norm2"), flagged_shells=cmp.get("flagged_shells")),
           flag=dict(rule="||V||_* against the control above the control's holdout rho_u^max (standard family); a descriptive threshold, not a solution-error or representation-independence statement", control_holdout_rho_u=ctl_rho, norm_star_U=cmp["norm_star_U"], reading=flag),
           state_sha256=hashes, state_files=dict(control=os.path.relpath(sc, ROOT), variant=os.path.relpath(sv, ROOT)), code_versions=dict(control=rc.get("code_versions"), variant=rv.get("code_versions")),
           complete=complete, drift_original_to_control=drift, common_shell_holdout=dict(shells=common_shells, only_control=only_c, only_variant=only_v),
           table=table)
if a.kind == "far":
    def within2(k):
        r = ratio(k); return (finite(r) and 0.5 < r < 2.0), r          # SPEC 7.11 X3: 'less than a factor 2' (strict)
    x3a = [within2("rho_u_max_holdout"), within2("rho_u_max_holdout_half")]
    x3b = [within2("rho_nl_max_holdout"), within2("rho_nl_max_holdout_half")]
    far_fin = [v for v in far_ratios if finite(v)]
    far_ok = (len(far_fin) == len(far_ratios) > 0 and finite(ctl_rho) and max(far_fin) <= ctl_rho)
    dKE = None if (g(rc, "K_ratio_direct") is None or g(rv, "K_ratio_direct") is None) else abs(g(rv, "K_ratio_direct") - g(rc, "K_ratio_direct"))
    dKH = None if (g(rc, "K_H_ratio_direct") is None or g(rv, "K_H_ratio_direct") is None) else abs(g(rv, "K_H_ratio_direct") - g(rc, "K_H_ratio_direct"))
    k_ok = finite(dKE) and finite(dKH) and dKE <= 0.1 and dKH <= 0.1
    evaluable = complete and all(finite(t[1]) for t in x3a + x3b) and finite(ctl_rho)
    X3 = dict(evaluable=evaluable,
              X3a=dict(met=(all(t[0] for t in x3a) if evaluable else None), ratios=[t[1] for t in x3a]),
              X3b=dict(met=(all(t[0] for t in x3b) if evaluable else None), ratios=[t[1] for t in x3b]),
              X3c_proxy=dict(met=(bool(far_ok and k_ok) if evaluable else None), far_sphere_U_ratio_max=(max(far_fin) if far_fin else None), control_holdout_rho_u=ctl_rho, dK_E=dKE, dK_H=dKH,
                             note="far-field sensitivity PROXY (far-sphere velocity ratio and the carried K_E, K_H ratios); the stability of the fitted pressure-multipole coefficients C_lm of SPEC 7.11 X3 is NOT measured by it and stays unevaluated"),
              proxy_met=(bool(all(t[0] for t in x3a) and all(t[0] for t in x3b) and far_ok and k_ok) if evaluable else None),
              note="group (iii) label (lead decision, registration Appendix C): far anchor radii sensitivity (x 1/4, x 4); far_radii moves the far anchor residual rows (and the holdout's outermost node), not an analytic matching boundary: the compactified basis has none")
    out["X3"] = X3
fn = os.path.join(ROOT, "reports", f"robustness_{a.variant}.json")
json.dump(out, open(fn, "w"), indent=1, default=str)
# markdown block
print(f"## Robustness reading: {a.variant} against its control {a.control} ({a.kind}; {out['utc']}; primary-reported, unvalidated)")
print(f"- status control / variant: {rc.get('status')} / {rv.get('status')}; failures: {rc.get('failure')} / {rv.get('failure')}; R0 {cmp['R0'][0]} / {cmp['R0'][1]}; far_radii {rc.get('far_radii')} / {rv.get('far_radii')}")
print(f"- compare_fields (control = reference): aligned angle {cmp['rotation']['gamma']:.6f} rad; ||V||_* (U) {cmp['norm_star_U']:.4e}; ||V||_*,1 DU {cmp['norm_star1_DU']:.4e}, Omega {cmp['norm_star1_Om']:.4e}; "
      f"far spheres U ratio {', '.join(f'{l}: {v:.3e}' for l, v in zip(far_labels, far_ratios))}; F-gauge {cmp.get('F_norm2')}")
print(f"- states: control {os.path.relpath(sc, ROOT)} sha256 {hashes['control'][:16]}..., variant {os.path.relpath(sv, ROOT)} sha256 {hashes['variant'][:16]}...; complete batteries: {complete}")
print(f"- flag: ||V||_* {cmp['norm_star_U']:.4e} against the control's holdout rho_u^max {ctl_rho}: {flag}")
if drift:
    print(f"- optimization drift of the control (original {a.original} -> continued control): ||V||_* {drift['norm_star_U']:.4e}, ||V||_*,1 DU {drift['norm_star1_DU']:.4e} / Omega {drift['norm_star1_Om']:.4e} (gamma {drift['gamma']:.6f})")
if common_shells:
    worst = max(common_shells, key=lambda d: (d['ratio'] or 0))
    print(f"- per-shell holdout rho_u on the {len(common_shells)} shells with identical edges: max variant/control ratio {worst['ratio']:.3f} on {worst['edges']}; shells only in the control {only_c}, only in the variant {only_v}")
if a.kind == "far":
    X3 = out["X3"]
    lab = lambda m: 'unevaluated' if m is None else ('met' if m else 'NOT met')
    print(f"- X3a (rho_u^max within a factor 2, both families): {lab(X3['X3a']['met'])} (ratios {X3['X3a']['ratios']}); X3b (rho_nl^max): {lab(X3['X3b']['met'])} (ratios {X3['X3b']['ratios']}); "
          f"X3c PROXY (far-sphere U ratio {X3['X3c_proxy']['far_sphere_U_ratio_max']} <= {ctl_rho}; dK_E {X3['X3c_proxy']['dK_E']}, dK_H {X3['X3c_proxy']['dK_H']} <= 0.1): {lab(X3['X3c_proxy']['met'])}; "
          f"X3 proxy overall: {lab(X3['proxy_met'])}. The fitted C_lm stability of SPEC X3 is unevaluated; the proxy counts as X3 for no tier. Label: far anchor radii sensitivity (x 1/4, x 4), not the motion of a matching boundary.")
print("| quantity | control | variant | variant/control |")
print("|---|---|---|---|")
for t in table:
    fmt = lambda v: "n/a" if v is None else (f"{v:.4g}" if isinstance(v, float) else str(v))
    print(f"| {t['name']} | {fmt(t['control'])} | {fmt(t['variant'])} | {fmt(t['ratio'])} |")
print(f"written {os.path.relpath(fn, ROOT)}")
