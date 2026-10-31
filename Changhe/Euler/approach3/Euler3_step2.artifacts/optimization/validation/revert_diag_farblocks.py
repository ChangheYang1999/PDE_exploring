#!/usr/bin/env python
"""DIAG far-block reversion test at a FREE end state (lead 2026-10-29T20:52:40Z item 3; prospective rule replacing the withdrawn 20:22:14Z item 3 (a)): one battery,
no optimization. State: the run's F-projected end runs/<run>/starts/start_000.pt (parameters unchanged). The coefficients of radial modes k in K (default 2 and 3,
the top two of four) of each far block (B, D, E), all angular modes, are set to their values in the lineage's F-projected start reference (record_63a start
state <tag>_state.pt). The phase pivots of the two states must be equal (same pivot potential, mode and amplitude sign), else the test is OPEN and not run.
Then the worker's exact F-gauge projection is re-applied and the end battery runs (O1 by Problem.objective_at + commit_aux; rho_u^max on the training grid,
the dyadic and the half-offset holdout families for start, end and reverted with the same code; record_63a.full_battery of the reverted state: sigma_u^max,
a_max_core with both core weights, N_core, ...; spectra). The energy of the modes k in K of each far block is reported at the start, at the end and in the
reverted state (F-gauge). Criterion (lead): on both holdout families rho_u^max(reverted) <= rho_u^max(start) - 0.5 (rho_u^max(start) - rho_u^max(end)); the
verifier's concurrence on the actual values is needed for any clearance. Label DIAG.
Usage: python validation/revert_diag_farblocks.py <abs run dir> <device> --start-state <abs *_state.pt> --start-record <abs json> --end-record <abs json> [--blocks B,D,E] [--modes 2,3] [--tag TAG]"""
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
    out = {}
    out["training"] = spec_diagnostics(prob, z)["global_"]["rho_u_max"]
    H = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6))); out["dyadic_holdout"] = spec_diagnostics(prob, z, holdout=H)["global_"]["rho_u_max"]
    r_max = float(model.r.max()); Hh = HoldoutGrid(model, r_core=model.R0, n_per_shell=int(cfg.get("holdout_per_shell", 6)), edges=half_offset_edges(model.R0, r_max))
    out["half_offset_holdout"] = spec_diagnostics(prob, z, holdout=Hh, extras=False)["global_"]["rho_u_max"]
    return out


def block_slices(model, name):
    off = 0
    for nm, n in model.layout:
        if nm == name:
            return off, n, model.ncols[nm]
        off += n * model.ncols[nm]
    raise KeyError(name)


def mode_energies(model, z, blocks, modes):
    dd = model.unpack_all(z); out = {}
    for b in blocks:
        arr = dd[b]; e_k = (arr ** 2).sum(1)
        out[b] = dict(block_energy=float(e_k.sum()), energy_per_k=[float(v) for v in e_k], energy_modes=float(sum(float(e_k[k]) for k in modes)), fraction_modes=(float(sum(float(e_k[k]) for k in modes)) / float(e_k.sum()) if float(e_k.sum()) > 0 else None),
                      max_abs=float(arr.abs().max()), last2_over_max=(float(arr[-2:].abs().max()) / float(arr.abs().max()) if float(arr.abs().max()) > 0 else None))
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("run"); ap.add_argument("device"); ap.add_argument("--start-state", required=True); ap.add_argument("--start-record", required=True); ap.add_argument("--end-record", required=True)
    ap.add_argument("--blocks", default="B,D,E"); ap.add_argument("--modes", default="2,3"); ap.add_argument("--tag", default=None)
    a = ap.parse_args(); t0 = time.time(); dev = a.device; blocks = a.blocks.split(","); modes = [int(v) for v in a.modes.split(",")]
    run = os.path.abspath(a.run); sp = os.path.join(run, "starts", "start_000.pt"); S = torch.load(sp, map_location="cpu", weights_only=False); cfg = dict(S["config"])
    tag = a.tag or f"revertBDE_{os.path.basename(run).split('_L6')[0]}"
    od = os.path.join(ROOT, "validation", "revert_diag"); os.makedirs(od, exist_ok=True); op = os.path.join(od, tag + ".json"); zp = os.path.join(od, tag + "_state.pt")
    if os.path.exists(op):
        raise FileExistsError(op)
    log = lambda m: print(time.strftime("%H:%M:%S", time.gmtime()) + " " + m, flush=True)
    model, prob = W.build(cfg, dev); z_end = S["z"].to(dev); prob.pivot = S.get("pivot") or prob.choose_pivot(z_end)
    if model.free_params:
        prob.ensure_geometry(z_end)
    ST = torch.load(a.start_state, map_location="cpu", weights_only=False); cfg_s = dict(ST["config"]); z_s = ST["z"].to(dev)
    piv_s = (ST.get("meta") or {}).get("pivot") or ST.get("pivot"); piv_e = S.get("pivot")
    log(f"end {sp} ({sha(sp)[:16]}): it {S.get('iterations')}, pivot {piv_e}; start {a.start_state} ({sha(a.start_state)[:16]}), pivot {piv_s}")
    same_pivot = (piv_s is not None and piv_e is not None and piv_s.get("pot") == piv_e.get("pot") and int(piv_s.get("q", -1)) == int(piv_e.get("q", -2)) and math.copysign(1.0, float(piv_s.get("amp", 0.0))) == math.copysign(1.0, float(piv_e.get("amp", 0.0))))
    if (model.L, model.Nk, float(model.R0), tuple(map(tuple, model.layout))) != (cfg_s["L"], cfg_s["Nk"], float(cfg_s.get("R0", 1.0)), tuple(map(tuple, model.layout))):
        raise SystemExit("start and end states have different layouts")
    rec = dict(kind="DIAG far-block reversion test (lead 20:52:40Z item 3; prospective)", tag=tag, label="DIAG", run=run, end_state=dict(path=sp, sha256=sha(sp), iterations=S.get("iterations"), pivot=piv_e), start_state=dict(path=os.path.abspath(a.start_state), sha256=sha(a.start_state), pivot=piv_s),
               blocks=blocks, modes=modes, same_pivot=same_pivot, script_sha256=sha(os.path.abspath(__file__)), record_63a_sha256=sha(os.path.join(ROOT, "validation", "record_63a.py")), worker_sha256=sha(os.path.join(ROOT, "scripts", "worker_d6.py")), device=dev, torch=torch.__version__)
    if not same_pivot:
        rec.update(status="OPEN: the phase pivots of the start and end states differ; the reversion is not defined (lead 20:52:40Z item 3)", seconds=time.time() - t0, ts=now()); json.dump(rec, open(op, "w"), indent=1, default=str); log(rec["status"]); print("DONE", op); return
    # energies before
    en_start = mode_energies(model, z_s, blocks, modes); en_end = mode_energies(model, z_end, blocks, modes)
    # revert
    z_rv = z_end.clone()
    for b in blocks:
        off, nk, nc = block_slices(model, b)
        for k in modes:
            if k >= nk:
                raise SystemExit(f"block {b} has only {nk} radial modes; mode {k} absent")
            z_rv[off + k * nc: off + (k + 1) * nc] = z_s[off + k * nc: off + (k + 1) * nc]
    nF_raw = math.sqrt(R63.gauge_norm2(prob, model, z_rv)); z_rv[: model.n_coef] = z_rv[: model.n_coef] / nF_raw; nF2 = R63.gauge_norm2(prob, model, z_rv)
    en_rv = mode_energies(model, z_rv, blocks, modes)
    gd0, pd0 = prob.gauge_defects(z_end); gd, pd = prob.gauge_defects(z_rv)
    log(f"reverted modes {modes} of blocks {blocks}; far-field norm before projection {nF_raw:.15f}, F_norm2 after {nF2:.15f}; gauge/pivot defects end {gd0:.2e}/{pd0:.2e}, reverted {gd:.2e}/{pd:.2e}")
    for b in blocks:
        log(f"  block {b}: energy of modes {modes}: start {en_start[b]['energy_modes']:.6e}, end {en_end[b]['energy_modes']:.6e}, reverted {en_rv[b]['energy_modes']:.6e} (block energy start/end/reverted {en_start[b]['block_energy']:.4e}/{en_end[b]['block_energy']:.4e}/{en_rv[b]['block_energy']:.4e}; last2/max {en_start[b]['last2_over_max']:.4f}/{en_end[b]['last2_over_max']:.4f}/{en_rv[b]['last2_over_max']:.4f})")
    r0, aux0 = prob.objective_at(z_end); prob.commit_aux(aux0); O1_end = 0.5 * float(r0 @ r0)
    r1, aux1 = prob.objective_at(z_rv); prob.commit_aux(aux1); O1_rv = 0.5 * float(r1 @ r1)
    log(f"O1 end {O1_end:.17e} (saved {(S.get('d6fp') or {}).get('cost_final')!r}); O1 reverted {O1_rv:.17e} (ratio {O1_rv / O1_end:.6f})")
    rho_end = rho_three(prob, model, z_end, cfg); rho_rv = rho_three(prob, model, z_rv, cfg)
    model_s, prob_s = W.build(cfg_s, dev); prob_s.pivot = piv_s or prob_s.choose_pivot(z_s)
    if model_s.free_params:
        prob_s.ensure_geometry(z_s)
    rho_start = rho_three(prob_s, model_s, z_s, cfg_s)
    log(f"rho_u^max training/dyadic/half: start {rho_start['training']:.6e}/{rho_start['dyadic_holdout']:.6e}/{rho_start['half_offset_holdout']:.6e}; end {rho_end['training']:.6e}/{rho_end['dyadic_holdout']:.6e}/{rho_end['half_offset_holdout']:.6e}; reverted {rho_rv['training']:.6e}/{rho_rv['dyadic_holdout']:.6e}/{rho_rv['half_offset_holdout']:.6e}")
    B_rv, _ = R63.full_battery(prob, model, z_rv, cfg); sp_rv = R63.spectra(model, z_rv)
    recs = {}
    for nm, pth in (("start", a.start_record), ("end", a.end_record)):
        d = json.load(open(pth)); b = d["battery"]; recs[nm] = dict(path=os.path.abspath(pth), sha256=sha(pth), version=d.get("version"), tag=d.get("tag"), battery={k: b.get(k) for k in ("c_l", "omega", "rho_u_max", "rho_u_max_holdout", "sigma_u_max", "sigma_u_max_core", "a_max", "a_max_half", "a_max_core", "a_max_core_upper", "max_U", "N_core", "N_F", "e_core", "e_F", "core_resolved", "a_eff", "r_tail")},
                                                                     spectra={bl: {k: (d.get("spectra") or {}).get("per_block", {}).get(bl, {}).get(k) for k in ("top_fraction", "last2_over_max", "block_energy")} for bl in blocks})
    crit = {}
    for fam in ("training", "dyadic_holdout", "half_offset_holdout"):
        rs, re_, rt = rho_start[fam], rho_end[fam], rho_rv[fam]; bound = rs - 0.5 * (rs - re_)
        crit[fam] = dict(rho_start=rs, rho_end=re_, rho_reverted=rt, bound_half_improvement=bound, passes=bool(rt <= bound), retained_fraction_of_improvement=((rs - rt) / (rs - re_) if rs != re_ else None))
    both = bool(crit["dyadic_holdout"]["passes"] and crit["half_offset_holdout"]["passes"])
    log("criterion: " + ", ".join(f"{k}: {v['passes']} (retained {v['retained_fraction_of_improvement']})" for k, v in crit.items()) + f"; both holdout families: {both} (verifier's concurrence on the values needed for any clearance)")
    torch.save(dict(z=z_rv.detach().cpu(), config=cfg, free_params=bool(model.free_params), iterations=S.get("iterations"), pivot=prob.pivot, kind=f"DIAG reverted state: modes {modes} of blocks {blocks} set to the start reference's values, then F-projected; from {sp}", source=sp, source_sha256=sha(sp), start_state=os.path.abspath(a.start_state), start_state_sha256=sha(a.start_state), ts=now()), zp)
    rec.update(status="computed", F_norm_before_projection=nF_raw, F_norm2_after=nF2, gauge_defects=dict(end=[gd0, pd0], reverted=[gd, pd]), energies=dict(start=en_start, end=en_end, reverted=en_rv),
               O1=dict(end=O1_end, reverted=O1_rv, ratio_reverted_over_end=O1_rv / O1_end, end_saved=(S.get("d6fp") or {}).get("cost_final")), rho_u_max=dict(start=rho_start, end=rho_end, reverted=rho_rv), criterion=crit, criterion_both_holdout_families=both,
               core=dict(reverted={k: B_rv.get(k) for k in ("a_max_core", "a_max_core_upper", "sigma_u_max", "sigma_u_max_core", "a_max", "a_max_half", "max_U", "N_core", "N_F", "core_resolved")}, end_record=recs["end"]["battery"], start_record=recs["start"]["battery"]),
               battery_reverted=B_rv, spectra_reverted={k: {kk: v.get(kk) for kk in ("top_fraction", "last2_over_max", "block_energy")} for k, v in sp_rv["per_block"].items()}, records=recs, reverted_state_file=zp, reverted_state_sha256=sha(zp),
               notes=["no optimization: the reverted state is the end state with the named far-block modes replaced by the start reference's values and the F-gauge projection re-applied", "rho_u^max of start, end and reverted computed here with the same code and grids; a_max and sigma values of start and end quoted from the named records",
                      "clearance of the far-block flags needs the criterion on both holdout families AND the verifier's concurrence on the actual values (lead 20:52:40Z item 3)"], seconds=time.time() - t0, ts=now())
    json.dump(rec, open(op, "w"), indent=1, default=str); log(f"DONE {op} sha256 {sha(op)[:16]}; {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
