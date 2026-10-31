#!/usr/bin/env python
"""DIAG truncation evaluation of the block-C high radial modes at a FREE end state (lead 2026-10-29T20:22:14Z item 3 (b); V449): one battery, no optimization.
State: the run's F-projected end runs/<run>/starts/start_000.pt (parameters unchanged). The coefficients of block C with radial index k >= k_from (all angular
modes) are scaled by s = sqrt(f0 (E_C - E_top) / ((1 - f0) E_top)), f0 = the start reference's N6 fraction of block C (bound value), E_C the block energy and
E_top the energy of the modes k >= k_from as in record_63a.spectra; this restores the start fraction exactly (algebra; verified after the scaling and after the
worker's exact F-gauge projection z[:n_coef] /= ||F||, which leaves fractions unchanged). Then: the self-consistent O1 (Problem.objective_at + commit_aux) of
the end and of the truncated state, rho_u^max on the training grid, on the dyadic holdout family and on the half-offset family for the start reference, the end
and the truncated state (same code, same grids), and the full worker battery (record_63a.full_battery: sigma_u^max, a_max_core with both core weights, N_core, ...)
of the truncated state; start and end battery values are quoted from the named v10 records. Prospective criterion (lead): on both families
rho_u^max(truncated) <= rho_u^max(start) - 0.5 (rho_u^max(start) - rho_u^max(end)). Conservative: the truncated state is not re-optimized.
Usage: python validation/trunc_diag_blockC.py <abs run dir> <f0> <device> --start-state <abs *_state.pt of the start reference> --start-record <abs json> --end-record <abs json> [--block C] [--k-from 13] [--tag TAG]
Output: validation/trunc_diag/<tag>.json and <tag>_state.pt (the truncated, projected state). Label DIAG (no production change)."""
import os, sys, json, time, math, hashlib, argparse, importlib.util
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
_s = importlib.util.spec_from_file_location("record_63a", os.path.join(ROOT, "validation", "record_63a.py")); R63 = importlib.util.module_from_spec(_s); _s.loader.exec_module(R63)
W = R63.W
from src.validation.spec_diagnostics import spec_diagnostics
from src.validation.holdout import HoldoutGrid, half_offset_edges
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
now = lambda: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def rho_three(prob, model, z, cfg):
    """rho_u^max on the training grid, the dyadic holdout family and the half-offset family (same definitions as the worker battery)."""
    out = {}
    sd = spec_diagnostics(prob, z); out["training"] = sd["global_"]["rho_u_max"]
    H = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6))); out["dyadic_holdout"] = spec_diagnostics(prob, z, holdout=H)["global_"]["rho_u_max"]
    r_max = float(model.r.max()); Hh = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)), edges=half_offset_edges(model.R0, r_max))
    out["half_offset_holdout"] = spec_diagnostics(prob, z, holdout=Hh, extras=False)["global_"]["rho_u_max"]
    out["edges_dyadic"] = [list(map(float, e)) for e in H.edges]; out["edges_half"] = [list(map(float, e)) for e in Hh.edges]
    return out


def block_offset(model, name):
    off = 0
    for nm, n in model.layout:
        if nm == name:
            return off, n, model.ncols[nm]
        off += n * model.ncols[nm]
    raise KeyError(name)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("run"); ap.add_argument("f0", type=float); ap.add_argument("device"); ap.add_argument("--start-state", required=True); ap.add_argument("--start-record", required=True)
    ap.add_argument("--end-record", required=True); ap.add_argument("--block", default="C"); ap.add_argument("--k-from", type=int, default=13); ap.add_argument("--tag", default=None)
    a = ap.parse_args(); t0 = time.time(); dev = a.device
    run = os.path.abspath(a.run); sp = os.path.join(run, "starts", "start_000.pt"); S = torch.load(sp, map_location="cpu", weights_only=False); cfg = dict(S["config"])
    tag = a.tag or f"truncC_{os.path.basename(run).split('_L6')[0]}"
    od = os.path.join(ROOT, "validation", "trunc_diag"); os.makedirs(od, exist_ok=True); op = os.path.join(od, tag + ".json"); zp = os.path.join(od, tag + "_state.pt")
    if os.path.exists(op):
        raise FileExistsError(op)
    model, prob = W.build(cfg, dev); z_end = S["z"].to(dev); prob.pivot = S.get("pivot") or prob.choose_pivot(z_end)
    if model.free_params:
        prob.ensure_geometry(z_end)
    c_l, omega = (float(z_end[-2]), float(z_end[-1])) if model.free_params else (float(cfg["c_l"]), float(cfg["omega"]))
    log = lambda m: print(time.strftime("%H:%M:%S", time.gmtime()) + " " + m, flush=True)
    log(f"end state {sp} (sha256 {sha(sp)[:16]}): iterations {S.get('iterations')}, (c_l, omega) = ({c_l!r}, {omega!r}), saved cost_final {(S.get('d6fp') or {}).get('cost_final')!r}")
    # ---- spectra of the end state and the scaling
    sp_end = R63.spectra(model, z_end); pb = sp_end["per_block"][a.block]
    off, nk, nc = block_offset(model, a.block); dd = model.unpack_all(z_end); arr = dd[a.block]
    e_k = (arr ** 2).sum(1); E_C = float(e_k.sum()); E_top = float(e_k[a.k_from:].sum()); f_end = E_top / E_C
    assert abs(f_end - pb["top_fraction"]) <= 1e-12 * max(1.0, abs(f_end)) and pb["top_modes_from_k"] == a.k_from, (f_end, pb)
    f0 = a.f0; s = math.sqrt(f0 * (E_C - E_top) / ((1.0 - f0) * E_top))
    log(f"block {a.block}: n_k {nk}, modes k >= {a.k_from}; E_C {E_C:.12e}, E_top {E_top:.12e}, fraction at the end {f_end:.12e}, start fraction f0 {f0!r}, scale s {s:.12e}")
    z_tr = z_end.clone()
    if nc != model.Nq:
        raise SystemExit("block with a reduced column set: not handled (block C is a leading channel with all columns)")
    for k in range(a.k_from, nk):
        z_tr[off + k * nc: off + (k + 1) * nc] *= s
    sp_tr0 = R63.spectra(model, z_tr); f_tr0 = sp_tr0["per_block"][a.block]["top_fraction"]
    nF_raw = math.sqrt(R63.gauge_norm2(prob, model, z_tr)); z_tr[: model.n_coef] = z_tr[: model.n_coef] / nF_raw        # the worker's exact F-gauge projection
    nF2 = R63.gauge_norm2(prob, model, z_tr); sp_tr = R63.spectra(model, z_tr); f_tr = sp_tr["per_block"][a.block]["top_fraction"]
    gd, pd = prob.gauge_defects(z_tr); gd0, pd0 = prob.gauge_defects(z_end)
    log(f"fraction after scaling {f_tr0:.17e}, after projection {f_tr:.17e} (f0 {f0:.17e}; |f_tr - f0| {abs(f_tr - f0):.3e}); far-field norm before projection {nF_raw:.15f}, F_norm2 after {nF2:.15f}; gauge/pivot defects end {gd:.2e}/{pd:.2e} -> truncated {gd0:.2e}/{pd0:.2e}")
    # ---- O1 of the end and of the truncated state (self-consistent: objective_at + commit_aux)
    r0, aux0 = prob.objective_at(z_end); prob.commit_aux(aux0); O1_end = 0.5 * float(r0 @ r0)
    r1, aux1 = prob.objective_at(z_tr); prob.commit_aux(aux1); O1_tr = 0.5 * float(r1 @ r1)
    r0b, aux0b = prob.objective_at(z_end); prob.commit_aux(aux0b); O1_end_b = 0.5 * float(r0b @ r0b)      # end again after the truncated commit (state dependence of the committed weights, information)
    log(f"O1 end {O1_end:.17e} (record {(S.get('d6fp') or {}).get('cost_final')!r}); O1 truncated {O1_tr:.17e}; O1 end re-evaluated after the truncated commit {O1_end_b:.17e}")
    # ---- rho_u^max on three grids for start, end, truncated (same code)
    rho_end = rho_three(prob, model, z_end, cfg); rho_tr = rho_three(prob, model, z_tr, cfg)
    ST = torch.load(a.start_state, map_location="cpu", weights_only=False); cfg_s = dict(ST["config"]); model_s, prob_s = W.build(cfg_s, dev); z_s = ST["z"].to(dev)
    prob_s.pivot = (ST.get("meta") or {}).get("pivot") or ST.get("pivot") or prob_s.choose_pivot(z_s)
    if model_s.free_params:
        prob_s.ensure_geometry(z_s)
    rho_start = rho_three(prob_s, model_s, z_s, cfg_s); sp_start = R63.spectra(model_s, z_s)
    log(f"rho_u^max training/dyadic/half: start {rho_start['training']:.6e}/{rho_start['dyadic_holdout']:.6e}/{rho_start['half_offset_holdout']:.6e}; end {rho_end['training']:.6e}/{rho_end['dyadic_holdout']:.6e}/{rho_end['half_offset_holdout']:.6e}; truncated {rho_tr['training']:.6e}/{rho_tr['dyadic_holdout']:.6e}/{rho_tr['half_offset_holdout']:.6e}")
    # ---- full battery of the truncated state
    B_tr, _ = R63.full_battery(prob, model, z_tr, cfg)
    recs = {}
    for nm, pth in (("start", a.start_record), ("end", a.end_record)):
        d = json.load(open(pth)); b = d["battery"]; recs[nm] = dict(path=os.path.abspath(pth), sha256=sha(pth), version=d.get("version"), tag=d.get("tag"), battery={k: b.get(k) for k in ("c_l", "omega", "rho_u_max", "rho_u_max_holdout", "sigma_u_max", "sigma_u_max_core", "a_max", "a_max_half", "a_max_core", "a_max_core_upper", "max_U", "N_core", "N_F", "e_core", "e_F", "core_resolved", "a_eff", "r_tail")},
                                                                     spectra_block={k: (d.get("spectra") or {}).get("per_block", {}).get(a.block, {}).get(k) for k in ("top_fraction", "last2_over_max", "block_energy", "n_k", "top_modes_from_k")})
    # ---- criterion per family
    crit = {}
    for fam in ("training", "dyadic_holdout", "half_offset_holdout"):
        rs, re_, rt = rho_start[fam], rho_end[fam], rho_tr[fam]; bound = rs - 0.5 * (rs - re_)
        crit[fam] = dict(rho_start=rs, rho_end=re_, rho_truncated=rt, bound_half_improvement=bound, passes=bool(rt <= bound), retained_fraction_of_improvement=((rs - rt) / (rs - re_) if rs != re_ else None))
    both = bool(crit["dyadic_holdout"]["passes"] and crit["half_offset_holdout"]["passes"])
    log("criterion (rho_tr <= rho_start - 0.5 (rho_start - rho_end)): " + ", ".join(f"{k}: {v['passes']} (retained {v['retained_fraction_of_improvement']})" for k, v in crit.items()) + f"; both holdout families: {both}")
    # a_max core weights: truncated vs end vs start (records)
    core = dict(truncated=dict(a_max_core=B_tr.get("a_max_core"), a_max_core_upper=B_tr.get("a_max_core_upper"), sigma_u_max=B_tr.get("sigma_u_max"), sigma_u_max_core=B_tr.get("sigma_u_max_core"), a_max=B_tr.get("a_max"), a_max_half=B_tr.get("a_max_half"), max_U=B_tr.get("max_U"), N_core=B_tr.get("N_core"), N_F=B_tr.get("N_F"), core_resolved=B_tr.get("core_resolved")),
                end_record=recs["end"]["battery"], start_record=recs["start"]["battery"],
                ratios_truncated_over_start={k: (B_tr.get(k) / recs["start"]["battery"][k] if (B_tr.get(k) is not None and recs["start"]["battery"].get(k)) else None) for k in ("a_max_core", "a_max_core_upper", "rho_u_max", "max_U")},
                ratios_end_over_start={k: (recs["end"]["battery"][k] / recs["start"]["battery"][k] if (recs["end"]["battery"].get(k) is not None and recs["start"]["battery"].get(k)) else None) for k in ("a_max_core", "a_max_core_upper", "rho_u_max", "max_U")})
    torch.save(dict(z=z_tr.detach().cpu(), config=cfg, free_params=bool(model.free_params), iterations=S.get("iterations"), pivot=prob.pivot, kind=f"DIAG truncated state: block {a.block} modes k >= {a.k_from} scaled by s then F-projected; from {sp}", source=sp, source_sha256=sha(sp), s=s, f0=f0, ts=now()), zp)
    rec = dict(kind="DIAG block-C truncation evaluation (lead 20:22:14Z item 3 (b); V449)", tag=tag, label="DIAG", run=run, end_state=dict(path=sp, sha256=sha(sp), iterations=S.get("iterations"), c_l=c_l, omega=omega, cost_final_saved=(S.get("d6fp") or {}).get("cost_final")),
               block=a.block, k_from=a.k_from, n_k=nk, E_C=E_C, E_top=E_top, fraction_end=f_end, f0=f0, f0_source="P1_start fraction (bound value, V449)", scale_s=s, fraction_after_scaling=f_tr0, fraction_after_projection=f_tr, fraction_minus_f0=f_tr - f0,
               F_norm_before_projection=nF_raw, F_norm2_after=nF2, gauge_defects=dict(end=[gd0, pd0], truncated=[gd, pd]), O1=dict(end=O1_end, truncated=O1_tr, end_after_truncated_commit=O1_end_b, ratio_truncated_over_end=O1_tr / O1_end),
               rho_u_max=dict(start=rho_start, end=rho_end, truncated=rho_tr), criterion=crit, criterion_both_holdout_families=both, core=core, battery_truncated=B_tr, spectra=dict(start=sp_start["per_block"].get(a.block), end=sp_end["per_block"].get(a.block), truncated=sp_tr["per_block"].get(a.block), truncated_all_blocks={k: {kk: v.get(kk) for kk in ("top_fraction", "last2_over_max")} for k, v in sp_tr["per_block"].items()}),
               records=recs, start_state=dict(path=os.path.abspath(a.start_state), sha256=sha(a.start_state), c_l=float(z_s[-2]) if model_s.free_params else cfg_s["c_l"], omega=float(z_s[-1]) if model_s.free_params else cfg_s["omega"]),
               truncated_state_file=zp, truncated_state_sha256=sha(zp), notes=["no optimization: the truncated state is the end state with the block-C modes k >= k_from scaled and the F-gauge projection re-applied",
                                                                                "rho_u^max values of start, end and truncated are computed here with the same code and grids; a_max and sigma values of start and end are quoted from the named records",
                                                                                "the criterion is the lead's prospective rule; a failure can come from the sensitivity of the residual to the truncation, not only from the high modes carrying the improvement (lead 20:22:14Z item 3 (b))"],
               script_sha256=sha(os.path.abspath(__file__)), record_63a_sha256=sha(os.path.join(ROOT, "validation", "record_63a.py")), worker_sha256=sha(os.path.join(ROOT, "scripts", "worker_d6.py")), device=dev, torch=torch.__version__, seconds=time.time() - t0, ts=now())
    json.dump(rec, open(op, "w"), indent=1, default=str); log(f"DONE {op} sha256 {sha(op)[:16]}; {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
