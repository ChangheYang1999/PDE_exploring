#!/usr/bin/env python
"""CPU diagnostic (shift 10, lead-approved): split the LM cost of a job's warm start into its row blocks exactly as the worker builds them:
PDE rows (momentum, n_pde), far anchor rows, closure rows, gauge rows (||F|| - 1 and any pin/constraint rows). Reproduces the worker's
init_from path (embed_state, pivot, nl weights, closure target, tail-constraint projection) with no GPU. A diagnostic of a START, never a
reading of a state. Usage: block_costs.py JOB.json [--start PATH] [--json OUT]"""
import sys, os, json, math, argparse, time
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT); sys.path.insert(0, os.path.join(ROOT, "scripts"))
import torch
torch.set_default_dtype(torch.float64)
from src.equations.fields import Model
from src.optimization.tail_constraints import TailConstraints
from src.optimization.transfer import embed_state

import worker as W

ap = argparse.ArgumentParser(); ap.add_argument("job"); ap.add_argument("--start", default=None); ap.add_argument("--json", default=None)
ap.add_argument("--phase_align", action="store_true", help="also evaluate the blocks on prob.phase_align(z) (the LM's exact projection at its first step)")
a = ap.parse_args()
J = json.load(open(a.job)); cfg = J["config"]; dev = "cpu"
t0 = time.time()
model, prob = W.build(cfg, dev)
tc = TailConstraints(model, nu=float(cfg.get("nu", 0.0) or 0.0)) if cfg.get("tail_constraints", False) else None
path = a.start or cfg["init_from"]
src = torch.load(path, map_location="cpu", weights_only=False); scfg = src["config"]
msrc = Model(L=scfg["L"], Nk=scfg["Nk"], m_parity=scfg.get("m_parity", "even"), R0=scfg.get("R0", 1.0), Nr=scfg.get("Nr"), c_l=scfg["c_l"], omega=scfg["omega"],
             free_params=src.get("free_params", False), channels=scfg.get("channels"), device=dev)
z = embed_state(src["z"].to(dev), msrc, model)
prob.pivot = prob.choose_pivot(z, rank=int(cfg.get("pivot_rank", 1) or 1))                 # honours the job's pivot_rank (lead IE S3-5)
prob.maybe_rebuild_pressure(z); prob.set_sigmaZ_ramp(z); prob.update_nl_weights(z); prob.update_closure(z)
zp = tc.expand(tc.reduce(z)) if tc is not None else z
if tc is not None:
    prob.update_closure(zp)
out = dict(job=J["job_id"], start=path, R0=model.R0, L=cfg["L"], Nk=cfg["Nk"], c_l=cfg["c_l"], omega=cfg["omega"], closure_lambda=cfg.get("closure_lambda", 0.0))
with torch.no_grad():
    r = prob.residual_vector(zp)
    npde = prob.n_pde_residuals()
    nfar = 0
    if getattr(prob, "far_model", None) is not None:
        nfar = 3 * len(prob.far_radii) * prob.far_model.grid.w.numel()
    cr = prob.closure_rows(zp); ncl = 0 if cr is None else cr.numel()
    ng = r.numel() - npde - nfar - ncl
    blocks = dict(pde=r[:npde], far=r[npde:npde + nfar], closure=r[npde + nfar:npde + nfar + ncl], gauge=r[npde + nfar + ncl:])
    out["rows"] = {k: int(v.numel()) for k, v in blocks.items()}
    out["cost"] = {k: 0.5 * float(v @ v) for k, v in blocks.items()}
    out["cost_total"] = 0.5 * float(r @ r)
    out["max_abs_row"] = {k: (float(v.abs().max()) if v.numel() else 0.0) for k, v in blocks.items()}
    if nfar:
        per = blocks["far"].reshape(3, len(prob.far_radii), -1)
        out["far_cost_by_radius"] = {str(prob.far_radii[i]): 0.5 * float((per[:, i] ** 2).sum()) for i in range(len(prob.far_radii))}
    out["closure_mismatch_m"] = (prob.closure or {}).get("mismatch")
    out["gauge_rows_values"] = [float(v) for v in blocks["gauge"]]
    try:
        gd = prob.gauge_defects(zp); out["gauge_defects"] = [float(x) for x in gd] if isinstance(gd, (tuple, list)) else str(gd)
    except Exception as e:
        out["gauge_defects"] = repr(e)
    F = model.fields_grid(zp, need_vort=True)
    out["maxU_train"] = float(F["U"].norm(dim=0).max()) if F["U"].dim() == 3 else float(F["U"].abs().max())
    try:
        dd = model.unpack_all(zp)
        out["coef_norms"] = {k: float(dd[k].norm()) for k in ("A", "C", "B", "D", "E") if k in dd and hasattr(dd[k], "norm") and dd[k].numel() > 0}
    except Exception as e:
        out["coef_norms"] = repr(e)
    out["relU_projection"] = float(((model.fields_grid(zp, need_vort=False)["U"] - model.fields_grid(z, need_vort=False)["U"]).norm() / model.fields_grid(z, need_vort=False)["U"].norm()))
if a.phase_align:
    with torch.no_grad():
        za = prob.phase_align(zp)
        ra = prob.residual_vector(za)
        out["phase_aligned"] = dict(cost_total=0.5 * float(ra @ ra), cost_pde=0.5 * float(ra[:npde] @ ra[:npde]), cost_nonpde=0.5 * float(ra[npde:] @ ra[npde:]),
                                    rel_change_z=float((za - zp).norm() / zp.norm()), gauge_defects=[float(x) for x in prob.gauge_defects(za)], pivot=str(prob.pivot))
    prob.update_closure(za)                                   # refresh the lagged closure target AT the rotated state
    with torch.no_grad():
        rb = prob.residual_vector(za)
        out["phase_aligned"]["after_closure_refresh"] = dict(cost_total=0.5 * float(rb @ rb), cost_pde=0.5 * float(rb[:npde] @ rb[:npde]), cost_nonpde=0.5 * float(rb[npde:] @ rb[npde:]),
                                                             closure_mismatch_m=(prob.closure or {}).get("mismatch"))
    out["source_saved_pivot"] = str(src.get("pivot"))
out["seconds"] = time.time() - t0
print(json.dumps(out, indent=1))
if a.json:
    os.makedirs(os.path.dirname(a.json), exist_ok=True); json.dump(out, open(a.json, "w"), indent=1)
