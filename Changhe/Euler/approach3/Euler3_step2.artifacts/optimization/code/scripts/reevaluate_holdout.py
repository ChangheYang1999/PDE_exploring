#!/usr/bin/env python
"""Re-evaluate the holdout SPEC diagnostics of saved starts with the current code and append ledger records of kind
'reevaluation' holding the stored and the new values. Since 2026-10-24T23:xxZ (lead 22:40Z item (c), SPEC v1.11 7.3a) the
re-evaluation reports BOTH shell families (standard dyadic [2^j, 2^(j+1)) and half-offset [2^(j+1/2), 2^(j+3/2))), rho_nl^max over
all shells of each family, and the single-sphere maxima on the exchange radii r = R0 2^(j/4) inside the holdout range.
Usage: reevaluate_holdout.py [--top N] [--device cuda:k] [--no-ledger] [start files...]"""
import sys, os, json, time, argparse
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.problem import Problem
from src.validation.spec_diagnostics import spec_diagnostics, tier_S
from src.validation.holdout import HoldoutGrid, half_offset_edges, sphere_diagnostics, exchange_radii, two_family_summary, summary_text, structure_text
from src.campaign import ledger
LEDGER = os.path.join(ROOT, "status", "ledger.jsonl")
ap = argparse.ArgumentParser(); ap.add_argument("files", nargs="*"); ap.add_argument("--top", type=int, default=0)
ap.add_argument("--device", default="cuda:0" if torch.cuda.is_available() else "cpu"); ap.add_argument("--no-ledger", action="store_true")
ap.add_argument("--Nr_src", type=int, default=None, help="radial collocation/source nodes of the training model (default cfg Nr = 3 Nk); the holdout pressure samples its source on these nodes (lead 2026-10-25T18:4xZ item 2: 6 Nk resampling)")
ap.add_argument("--light", action="store_true", help="skip the ray functionals and the core-resolution sets (shell ratios, far coefficients and balances only)")
ap.add_argument("--json_out", default=None, help="write the holdout diagnostics (both families, spheres, summary) to this JSON file (no ledger record unless --no-ledger is absent)")
a = ap.parse_args()
dev = a.device
files = list(a.files)
if a.top > 0:
    recs = ledger.read(LEDGER)
    board = ledger.leaderboard(recs, n=a.top, solver_version="all")
    files = [os.path.join(ROOT, b["zfile"]) for b in board] + files


def evaluate(zf, dev):
    S = torch.load(zf, map_location="cpu", weights_only=False); cfg = S["config"]; z = S["z"].to(dev)
    model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=(a.Nr_src if a.Nr_src else cfg.get("Nr")), c_l=cfg["c_l"], omega=cfg["omega"],
                  free_params=S.get("free_params", False), channels=cfg.get("channels"), device=dev, extra_r=cfg.get("far_radii") if cfg.get("far_merged", True) else None)
    prob = Problem(model, formulation="mom"); prob.pivot = S.get("pivot")
    t0 = time.time()
    hg = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)))
    sdh = spec_diagnostics(prob, z, holdout=hg)
    r_max = float(model.r.max())
    hg2 = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)), edges=half_offset_edges(model.R0, r_max))
    sdh2 = spec_diagnostics(prob, z, holdout=hg2, extras=False)
    sph = sphere_diagnostics(prob, z, exchange_radii(model.R0, model.R0 * 2.0 ** -6, r_max))
    tf = two_family_summary(sdh, sdh2, sph)
    og = sdh.get("origin") or {}                             # SPEC 7.6 / T08 origin Taylor ratios (floored)
    tf.update(tau0_floored=og.get("tau0_floored"), tau1_floored=og.get("tau1_floored"), tau2_floored=og.get("tau2_floored"), taylor_consistency=og.get("taylor_consistency_rel_change_tau"))
    try:                                                     # SPEC v1.22 tau_F / delta_G (lead 03:21Z item 5) for the shortlist
        if a.light:
            raise RuntimeError("skipped (--light)")
        from src.far_field.ray_functional import ray_functionals
        rf = ray_functionals(prob, z, n_per_octave=12, k_in=8, k_out=16, radii_tau=[2.0 ** 8 * model.R0, 2.0 ** 12 * model.R0])
        tk = sorted(rf["tau_F"].keys(), key=float)
        tf.update(tau_F_R8=rf["tau_F"][tk[0]], tau_F_R12=rf["tau_F"][tk[1]] if len(tk) > 1 else None, delta_G_core=rf["delta_G_core_ball"], delta_G_max=rf["delta_G_max"],
                  tau_F_by_m=rf.get("tau_F_by_m"), tau_F_selfcheck=max(rf["selfcheck_FR_LU_vs_RalphaU"].values()))
        sw = rf.get("mean_swirl") or {}
        tf.update(Q_sw=sw.get("Q_sw"), Gamma0_max=sw.get("Gamma0_max"), S_max=sw.get("S_max"), E_swirl_max=sw.get("E_max"), swirl_identity_closure=sw.get("identity_closure"))
    except Exception as e:
        tf["tau_F_error"] = repr(e)
    try:                                                     # SPEC v1.21 core-resolution sets (lead 02:24Z item 2)
        if a.light:
            raise RuntimeError("skipped (--light)")
        from src.validation.core_resolution import core_resolution, core_text
        from src.validation.critical_points import local_maxima_omega
        mx = ((S.get("critical") or {}).get("local_maxima")) or []
        if not mx:
            mx = local_maxima_omega(model, z, cfg["c_l"], cfg["omega"])
        guh = sdh["guards"]; maxOm = max([guh["N2_max_abs_Omega"]] + [m_["abs_Omega"] for m_ in mx])
        if mx:
            ystar = mx[max(range(len(mx)), key=lambda i: mx[i]["abs_Omega"])]["y"]
            cr = core_resolution(prob, z, cfg["c_l"], cfg["omega"], ystar, guh["N4_max_U"], maxOm, core_ball_radius=sdh["shells"]["edges"][0][1])
            bh, bq = cr["balls"]["half"], cr["balls"]["quarter"]; ish = cr.get("inner_shells") or {}
            tf.update(a_eff=cr["a_eff"], y_star=cr["y_star"], r_star=cr["r_star"], core_ball_over_a_eff=cr["core_ball_over_a_eff"], sigma_u_ball_half=bh["sigma_u"], sigma_u_ball_quarter=bq["sigma_u"],
                      a_max_ball_half_centre=bh["a_max_centre"], a_max_ball_half_upper=bh["a_max_upper"], a_max_ball_quarter_centre=bq["a_max_centre"], a_max_ball_quarter_upper=bq["a_max_upper"],
                      sigma_Om_ball_half=bh["sigma_Om"], inner_sigma_u_max=ish.get("sigma_u_max"), inner_a_max=ish.get("a_max"), core_resolved=cr["core_resolved"], core_doubling_change_max=cr["max_doubling_rel_change"],
                      sigma_u_max_core=max([v for v in (tf.get("sigma_u_max_std"), tf.get("sigma_u_max_half"), cr["sigma_u_max_added"]) if v is not None]),
                      a_max_core=max([v for v in (tf.get("a_max_std"), tf.get("a_max_half"), cr["a_max_added_centre"]) if v is not None]),
                      a_max_core_upper=max([v for v in (tf.get("a_max_std"), tf.get("a_max_half"), cr["a_max_added_upper"]) if v is not None]), core_text=core_text(cr))
            S["core_resolution"] = cr
    except Exception as e:
        tf["core_error"] = repr(e)
    gclos = None
    if model.channels.get("NkB", 0) > 0 or model.channels.get("NkD", 0) > 0:     # SPEC 4.4 closure, direct K_E ratio, K_H (v1.24 7.8), d84 defect F-component
        try:
            from src.far_field.correction import closure_distance
            gclos = closure_distance(prob, z)
            tf.update(K_ratio_direct=gclos.get("K_ratio_direct"), carried_mismatch_rel=gclos.get("carried_mismatch_rel"), carried_correlation=gclos.get("carried_correlation"),
                      K_H_required=gclos.get("K_H_required"), K_H_carried=gclos.get("K_H_carried"), K_H_ratio_direct=gclos.get("K_H_ratio_direct"), K_H_identity_rel_closure=gclos.get("K_H_identity_rel_closure"),
                      K_H_carried_two_forms_rel=gclos.get("K_H_carried_two_forms_rel"), G_defect_F_component=gclos.get("G_defect_F_component"), G_defect_cos_F=gclos.get("G_defect_cos_F"),
                      G_defect_parallel_fraction=gclos.get("G_defect_parallel_fraction"), G_defect_parallel_rel=gclos.get("G_defect_parallel_rel"), G_defect_orth_rel=gclos.get("G_defect_orth_rel"),
                      d84_bound_energy_ratio=gclos.get("d84_bound_energy_ratio"), H_F_tail=gclos.get("H_F_tail"))
            S["G_closure"] = gclos
        except Exception as e:
            tf["G_closure_error"] = repr(e)
    try:                                                     # d64 global balances (lead 05:36Z item 2)
        from src.validation.global_balances import GlobalBalances, balances_text
        gb_ = GlobalBalances(model)
        with torch.no_grad():
            b_ = gb_.integrals(z, r_core=sdh["guards"].get("N4_r_core"), K_H=((gclos or {}).get("K_H_carried")))
        bal = {k: (float(v) if torch.is_tensor(v) else v) for k, v in b_.items()}
        try:
            from src.validation.global_balances import far_rate_text
            bal["far_rate"] = gb_.far_energy_rate(prob, z); tf["kappa_far_finite_radius"] = {k: v.get("kappa") for k, v in bal["far_rate"].items()}; tf["Phi_F_far_finite_radius"] = {k: v.get("Phi_F") for k, v in bal["far_rate"].items()}
            tf["far_rate_text"] = far_rate_text(bal["far_rate"])
        except Exception as e:
            tf["far_rate_error"] = repr(e)
        tf.update(E_ren=bal["E_ren"], H_tot=bal["H_tot"], H_abs=bal["H_abs"], H_tot_over_abs=bal["H_tot_over_abs"], core_alignment=bal.get("core_alignment"),
                  E_ren_change_2oct=bal["E_ren_change_2oct"], H_tot_change_2oct=bal["H_tot_change_2oct"], balance_text=balances_text(bal), E_F_max=bal.get("E_F_max"), r_at_E_F_max=bal.get("r_at_E_F_max"),
                  E_F_weighted_excess=bal.get("E_F_weighted_excess"), E_F_weighted_deficit=bal.get("E_F_weighted_deficit"), E_ren_two_forms_rel_diff=bal.get("E_ren_two_forms_rel_diff"), H_F_sign_change_radii=bal.get("H_F_sign_change_radii"))
        S["global_balances"] = bal
    except Exception as e:
        tf["balance_error"] = repr(e)
    tf["_Nr_src"] = int(model.Nr_src); tf["_Nr_model"] = int(model.Nr)
    return S, sdh, sdh2, sph, tf, time.time() - t0


for zf in files:
    S, sdh, sdh2, sph, tf, secs = evaluate(zf, dev)
    old = S.get("spec_diag_holdout") or {}
    go, gn = (old.get("global_") or {}), sdh["global_"]
    rec = dict(kind="reevaluation", zfile=os.path.relpath(zf, ROOT), reason="two shell families (SPEC v1.11 7.3a), rho_nl^max over all shells, single-sphere maxima on exchange radii",
               old=dict(rho_u_max=go.get("rho_u_max"), rho_nl_max=go.get("rho_nl_max"), pi_u_max=go.get("pi_u_max"), Sigma_Z=(old.get("global_integrals") or {}).get("Sigma_Z")),
               new=dict(rho_u_max=gn["rho_u_max"], rho_nl_max=gn["rho_nl_max"], pi_u_max=gn["pi_u_max"], Sigma_Z=sdh["global_integrals"].get("Sigma_Z"), tier_S=tier_S(sdh)[0],
                        tier_S_half=tier_S(sdh2)[0], **tf),
               max_U=(sdh.get("guards") or {}).get("N4_max_U"), seconds=secs)
    if a.json_out:
        def _j(o):
            if torch.is_tensor(o): return o.detach().cpu().tolist()
            if isinstance(o, dict): return {str(k): _j(v) for k, v in o.items()}
            if isinstance(o, (list, tuple)): return [_j(v) for v in o]
            try:
                import numpy as _np
                if isinstance(o, _np.ndarray): return o.tolist()
                if isinstance(o, (_np.floating, _np.integer)): return o.item()
            except Exception:
                pass
            return o if isinstance(o, (int, float, str, bool)) or o is None else str(o)
        json.dump(dict(zfile=os.path.relpath(zf, ROOT), Nr_src=tf.get("_Nr_src"), Nr_model=tf.get("_Nr_model"), light=bool(a.light), seconds=secs, holdout_std=_j(sdh), holdout_half=_j(sdh2), spheres=_j(sph), summary=_j(tf)),
                  open(a.json_out, "w"), indent=1)
        print(f"wrote {a.json_out} (Nr_src {tf.get('_Nr_src')})")
    if not a.no_ledger:
        ledger.append(LEDGER, rec)
        S["spec_diag_holdout_reeval"] = sdh; S["spec_diag_holdout_half"] = sdh2; S["sphere_diag"] = sph; S["two_family"] = tf
        tmp = zf + ".tmp"; torch.save(S, tmp); os.replace(tmp, zf)
    print(f"{os.path.relpath(zf, ROOT)}: stored rho_u_max {go.get('rho_u_max')} -> {gn['rho_u_max']:.4e}; {summary_text(tf)}; max|U| {rec['max_U']:.3e}; {secs:.0f}s")
    print(f"   RAY: tau_F(2^8 R0) {tf.get('tau_F_R8')} tau_F(2^12 R0) {tf.get('tau_F_R12')} delta_G core {tf.get('delta_G_core')} max {tf.get('delta_G_max')} {tf.get('tau_F_error', '')}")
    print(f"   SWIRL: Q_sw {tf.get('Q_sw')} max|Gamma_0| {tf.get('Gamma0_max')} max|S| {tf.get('S_max')} closure {tf.get('swirl_identity_closure')} | ORIGIN tau_0/1/2 floored {tf.get('tau0_floored')} {tf.get('tau1_floored')} {tf.get('tau2_floored')} consistency {tf.get('taylor_consistency')}")
    print(f"   STRUCTURE: {structure_text(tf)}")
    print(f"   CORE (SPEC v1.21): {tf.get('core_text', tf.get('core_error', 'n/a'))}")
    print(f"   BALANCE (d64): {tf.get('balance_text', tf.get('balance_error', 'n/a'))}")
    print(f"   FAR RATE (d67): {tf.get('far_rate_text', tf.get('far_rate_error', 'n/a'))}")
    print(f"   FAR COEFFICIENTS (v1.24 7.8): K_E ratio {tf.get('K_ratio_direct')} | K_H required {tf.get('K_H_required')} carried {tf.get('K_H_carried')} ratio {tf.get('K_H_ratio_direct')} (identity closure {tf.get('K_H_identity_rel_closure')}) | defect m {tf.get('carried_mismatch_rel')} cos_F {tf.get('G_defect_cos_F')} d84 bound {tf.get('d84_bound_energy_ratio')} {tf.get('G_closure_error', '')}")
    sys.stdout.flush()
