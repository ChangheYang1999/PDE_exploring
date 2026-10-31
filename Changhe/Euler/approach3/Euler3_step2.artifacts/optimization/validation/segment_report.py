#!/usr/bin/env python
"""Post-hoc segment report (lead 11:29:05Z item 4, accepted 11:35:30Z item 4; no worker change): for a production run directory with
checkpoint_segment_end.pt, evaluate the production objective at the segment START state (the job's start file for segment 1, or the previous segment's
end state for a continuation) and at the END state, and report (a) O1 and its per-group split (near-origin r <= 0.1 R0, core/intermediate, far
r > 256 R0, closure rows, gauge rows, far-anchor block: squared norms of the weighted residual rows, summing to 2 O1), (b) a core-ball residual on the
production grid: the RMS of the unweighted momentum residual R_u over the grid points with r <= r_core and its ratio to the RMS of the convection term
(U . grad) U there, on THREE separately named domains (lead 12:05:03Z item 2; V281, V304): the registered core ball r <= reference_core/32 (the
domain of the verifier's holdout core-ball numbers), the origin ball r <= reference_core/256, and the core-scale ball r <= reference_core (a producer
diagnostic on a different domain, never identified with the verifier's core-ball numbers). reference_core is PAIR DEPENDENT (the verifier's baseline
core radius of the pair's start: P1/S01 0.4304351316933 (V235 plan), P2/S09 0.14364049210478602 = 32 x 0.004488765378274563 (V304)) and is a required
argument; its value and stated source go into the record. The values are the producer's own reading on the production grid nodes; the verifier's
holdout values decide what is reported as checked.
Usage: python validation/segment_report.py <run dir> --reference-core <value> --source "<where the value comes from>" [device]   (v4: FIXED-CONTROL checkpoints get the configuration's parameters appended; v3's positional radius and v2's fixed radii are gone)
Writes validation/segment_report_<job_id>.json (exclusive create)."""
import sys, os, json, time, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False
from validation.gates import Case, ROOT
from src.equations import residuals as res
import src.optimization.problem as problem_mod


def groups_of(case, vec):
    out = {"all": float(vec.norm()) ** 2}
    for gi, g in enumerate(case.group_names):
        out[g] = float(vec[case.row_group == gi].norm()) ** 2
    if hasattr(case, "anchor_mask") and bool(case.anchor_mask.any()):
        out["far_anchor_block"] = float(vec[case.anchor_mask].norm()) ** 2
    return out


def core_ball(prob, model, z, r_core):
    with torch.no_grad():
        ev = prob.evaluate(z)
        R = ev["R_u"]; F = ev["F"]
        conv = torch.einsum('m...,mi...->i...', F["U"], F["GU"])
        m = (model.r <= r_core)
        if int(m.sum()) == 0:
            return dict(n_nodes=0)
        rms_R = float((R[:, m, :] ** 2).mean().sqrt()); rms_conv = float((conv[:, m, :] ** 2).mean().sqrt()); rms_U = float((F["U"][:, m, :] ** 2).mean().sqrt())
        return dict(n_nodes=int(m.sum()), r_max_in_ball=float(model.r[m].max()), rms_R_u=rms_R, rms_conv=rms_conv, rms_U=rms_U, ratio_R_over_conv=(rms_R / rms_conv if rms_conv > 0 else None))


def main():
    run = sys.argv[1]; args = sys.argv[2:]
    if "--reference-core" not in args or "--source" not in args:
        raise SystemExit("REFUSED: --reference-core <value> and --source <text> are required (the registered core radius is pair dependent, V304)")
    ref_core = float(args[args.index("--reference-core") + 1]); ref_source = args[args.index("--source") + 1]
    rest = [a for i, a in enumerate(args) if a not in ("--reference-core", "--source") and (i == 0 or args[i - 1] not in ("--reference-core", "--source"))]
    dev = rest[0] if rest else ("cuda:0" if torch.cuda.is_available() else "cpu")
    BALLS = {"registered_core_ball": ref_core / 32.0, "origin_ball": ref_core / 256.0, "core_scale_ball": ref_core}
    problem_mod.TABLE_CACHE = False
    ck = torch.load(os.path.join(run, "checkpoint_segment_end.pt"), map_location="cpu", weights_only=False)
    cfg = ck["config"]; job_id = ck["job_id"]
    out_path = os.path.join(ROOT, "validation", f"segment_report_{job_id}.json")
    if os.path.exists(out_path):
        raise FileExistsError(out_path)
    t0 = time.time()
    start_file = cfg.get("init_from"); start_file = start_file if os.path.isabs(start_file) else os.path.join(ROOT, start_file)
    case = Case(job_id, dev, start=start_file); prob, model = case.prob, case.model
    def as_full(zf, cfg_):
        """v4 (2026-10-29T15:05Z): a FIXED-CONTROL checkpoint stores z_full WITHOUT the two parameter slots (n_coef entries); the Case model is free_params=True
        (n_coef + 2), so the fixed parameters of the configuration are appended, as gates.Case does for fixed starts (v3 fed the short vector to the free model
        and read two coefficients as c_l and omega: the v3 records of the FIXED members are invalid and are kept as *_v3_invalid)."""
        zf = torch.as_tensor(zf, dtype=torch.float64, device=dev)
        if zf.numel() == model.n_coef and not cfg_.get("free_params", True):
            zf = torch.cat([zf, torch.tensor([float(cfg_["c_l"]), float(cfg_["omega"])], dtype=torch.float64, device=dev)])
        assert zf.numel() == model.n_coef + 2, (zf.numel(), model.n_coef)
        return zf
    z_end = as_full(ck["current"]["z_full"], cfg)
    if cfg.get("continue_from_run"):
        prev_dir = cfg["continue_from_run"] if os.path.isabs(cfg["continue_from_run"]) else os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(run))), cfg["continue_from_run"])   # v4.1 (16:4xZ): resolve against the run's own tree (a frozen copy has no runs/)
        prev = torch.load(os.path.join(prev_dir, "checkpoint_segment_end.pt"), map_location="cpu", weights_only=False)
        z_start = as_full(prev["current"]["z_full"], prev["config"]); start_desc = f"end state of {cfg['continue_from_run']}"
    else:
        z_start = case.z_full.detach().clone(); start_desc = f"start file {cfg.get('init_from')}"
    rep = dict(job_id=job_id, label=ck.get("label"), segment=cfg.get("segment", 1), start=start_desc, end_it=ck["current"]["it"], counters=ck["current"].get("counters"), lm_status=ck["current"].get("lm_status"),
               balls=BALLS, reference_core=ref_core, reference_core_source=ref_source, device=dev, states={})
    for name, z in (("start", z_start), ("end", z_end)):
        with torch.no_grad():
            r, aux = prob.objective_at(z)
        g = groups_of(case, r)
        rep["states"][name] = dict(O1=0.5 * g["all"], O1_split_half_sq_norm={k: 0.5 * v for k, v in g.items()}, c_l=float(z[-2]), omega=float(z[-1]), free_params=bool(cfg.get("free_params", True)),
                                   balls={k: core_ball(prob, model, z, rv) for k, rv in BALLS.items()})
        print(name, json.dumps(rep["states"][name], default=str)[:400], flush=True)
    rep["seconds"] = time.time() - t0; rep["ts"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    rep["definitions"] = "balls: registered_core_ball r <= reference_core/32 is the domain of the verifier's core-ball numbers (V281, V304; reference_core pair dependent, value and source recorded); origin_ball r <= reference_core/256; core_scale_ball r <= reference_core is a different domain and is never identified with the verifier's core-ball numbers (lead 12:05:03Z item 2). O1 = 0.5 |r|^2 of the production weighted residual at the state (objective_at, self-consistent weights and closure target); the split gives 0.5 of the squared norm per group (sums to O1); core ball: RMS of the unweighted momentum residual R_u over the production grid points with r <= r_core and the ratio to the RMS of (U . grad) U there; the verifier's holdout values decide what is reported as checked"
    with open(out_path, "x") as fh_:
        json.dump(rep, fh_, indent=1, default=str)
    print("DONE", out_path, f"{time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
