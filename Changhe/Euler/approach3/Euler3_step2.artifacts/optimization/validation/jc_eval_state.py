#!/usr/bin/env python
"""J_c EVAL of a segment-end state (SPEC v1.23 3.6 (o); lead 14:44:24Z item 2 (e), 15:16:53Z item 1): build the state through the worker's resume path
(worker_d6.build(cfg), the checkpoint's reduced optimizer vector, pivot and pressure geometry), evaluate the self-consistent residual, build the production
Jacobian J_cw exactly as the worker's final record does (jacobian_fwd of residual_vector_wd plus param_columns with the differentiable pressure), compare it with
the stored final J_cw record of the run (QR factors: z_opt bitwise, cost, column norms D, Gram matrix R^T R against J^T J with the stored permutation), then the
complete Jacobian J_c = complete_jacobian_from_Jcw (closure target correction and carried-pattern parameter columns) with its time. FIXED-CONTROL states (no
parameter slots in the checkpoint, no stored final record) are evaluated with a free_params model: the configuration's c_l and omega are appended and the
reduced vector mapped to optimizer coordinates, so J_c has the two parameter columns too. Records (the worker's linearization_record format, kind J_cw and J_c)
and a JSON with the checkpoint sha256, config sha256, code hashes, timings and the comparison go to validation/jc_eval/<job_id>/. EVAL only: no optimizer
iteration, no change to any run. v5 (16:1xZ; verifier 16:13:32Z): phys assigned before the endpoint validation (v4 raised UnboundLocalError on FREE endpoints); the scaled Gram comparison is judged with a stated criterion (1e-12 relative Frobenius) beside the bitwise record-summary check.
v4 (16:1xZ; verifier 16:00:50Z, V367): endpoint validation BEFORE the Jacobian build (iteration, kind J_cw, the exact stored coordinates string, parameters, vector, cost; a FREE endpoint without a stored final record FAILS explicitly), judged criteria (scale: bitwise D; record summaries: bitwise R, Q^T r, D, perm, z_opt, generator), the Gram informational, a failed flag never yields an accepted record (status FAILED, exit 3); summary equality is not full-matrix equality.
v3 (16:0xZ, V364, lead 15:52:20Z): endpoint match (iteration, kind, coordinates, parameters, z_opt) of the stored final record, cost / scale / Gram judged separately, explicit full-field and parameter tie for FIXED states, source-copy and library versions, explicit exit code; the four v1 records are superseded.
v2 (15:5xZ): the comparison uses the record's scaled-QR convention and compares the two records bitwise (v1 kept as jc_eval_state.py.v1_b68dc6b0; its gram field is invalid).
Usage: python validation/jc_eval_state.py <run dir with checkpoint_segment_end.pt> [device] [chunk]"""
import sys, os, json, time, hashlib, importlib.util
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, ROOT)
import numpy as np, torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False; torch.backends.cudnn.allow_tf32 = False
spec = importlib.util.spec_from_file_location("worker_d6", os.path.join(ROOT, "scripts", "worker_d6.py")); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W)
from src.optimization.lm import jacobian_fwd, param_columns
from src.optimization.tail_constraints import TailConstraints
from src.optimization.param_map import ParamMap
from src.pressure.poisson_sh import PressureSolver
from src.equations.fields import alpha_of


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def write_failed(out_dir, out_json, job_id, status, endpoint=None):
    """v4: a record that fails its pre-checks is written as FAILED (no Jacobian built) and the process exits 3."""
    rec = dict(job_id=job_id, kind="EVAL", status="FAILED", failures=status["failures"], endpoint=endpoint, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    with open(out_json, "x") as fh:
        json.dump(rec, fh, indent=1, default=str)
    print("EXIT 3 (FAILED before the build)", flush=True); sys.stdout.flush(); os._exit(3)


def main():
    run = os.path.abspath(sys.argv[1]); dev = sys.argv[2] if len(sys.argv) > 2 else ("cuda:0" if torch.cuda.is_available() else "cpu"); chunk = int(sys.argv[3]) if len(sys.argv) > 3 else 256
    ck_path = os.path.join(run, "checkpoint_segment_end.pt"); ck = torch.load(ck_path, map_location="cpu", weights_only=False)
    cfg = dict(ck["config"]); job_id = ck["job_id"]; cur = ck["current"]
    out_dir = os.path.join(ROOT, "validation", "jc_eval", job_id); os.makedirs(out_dir, exist_ok=True)
    out_json = os.path.join(out_dir, "jc_eval.json")
    if os.path.exists(out_json):
        raise FileExistsError(out_json)
    t0 = time.time(); log = lambda m: print(time.strftime("%H:%M:%S", time.gmtime()) + " " + m, flush=True)
    fixed_state = not cfg.get("free_params", False)
    cfg_free = dict(cfg); cfg_free["free_params"] = True                                   # FIXED states: free_params model (lead 14:44:24Z item 2 (e))
    model, prob = W.build(cfg_free, dev)
    tc = TailConstraints(model) if cfg.get("tail_constraints", True) else None; pm = ParamMap(free=True)
    to_full = (lambda zo: tc.expand(pm.expand(zo))) if tc is not None else (lambda zo: pm.expand(zo))
    z_opt_ck = torch.as_tensor(cur["z_opt"], dtype=torch.float64, device=dev)
    if fixed_state:
        z_phys = torch.cat([z_opt_ck, torch.tensor([float(cfg["c_l"]), float(cfg["omega"])], dtype=torch.float64, device=dev)]); z_opt = pm.reduce(z_phys)
    else:
        z_opt = z_opt_ck.clone()
    prob.pivot = cur["pivot"]
    gb = cur.get("geometry_base")
    if gb is not None:                                                                       # the worker's resume path: pressure geometry sized at the geometry base
        prob.pressure = PressureSolver(model, p0=2 * alpha_of(gb["c_l"]) + 2, omega=gb["omega"], c_l=gb["c_l"])
        if prob.fine_model is not None:
            prob.fine_ps = PressureSolver(prob.fine_model, p0=2 * alpha_of(gb["c_l"]) + 2, omega=gb["omega"], c_l=gb["c_l"])
    zf = to_full(z_opt).detach()
    fixed_tie = None
    if fixed_state:                                                                                 # v3 (V364): explicit full-field and physical-parameter tie after the free-model conversion
        z_full_ck = torch.as_tensor(cur["z_full"], dtype=torch.float64, device=dev)
        fixed_tie = dict(checkpoint_z_full_len=int(z_full_ck.numel()), model_n_coef=int(model.n_coef), coefficients_bitwise_equal=bool(torch.equal(zf[: model.n_coef], z_full_ck[: model.n_coef])),
                         c_l_equal=(float(zf[-2]) == float(cfg["c_l"])), omega_equal=(float(zf[-1]) == float(cfg["omega"])), c_l=float(zf[-2]), omega=float(zf[-1]),
                         reduced_vector_bitwise_equal=bool(torch.equal(z_opt[:-2], z_opt_ck)), note="z_opt of the FIXED checkpoint plus the configuration's (c_l, omega) mapped to (z_c, z_w) by ParamMap.reduce; the full coefficient vector of the free model equals the checkpoint's z_full and the parameters equal the configuration")
        assert fixed_tie["coefficients_bitwise_equal"] and fixed_tie["c_l_equal"] and fixed_tie["omega_equal"], f"FIXED-state tie failed: {fixed_tie}"
    r_end, aux_end = prob.objective_at(zf); prob.commit_aux(aux_end); cost = 0.5 * float(r_end @ r_end)
    n_opt = z_opt.numel(); pidx = [n_opt - 2, n_opt - 1]
    phys = pm.describe(z_opt)                                                                       # v5 (verifier 16:13:32Z): assigned BEFORE the endpoint validation uses it
    gauge_rows = list(range(prob.row_blocks()[-1][1], prob.row_blocks()[-1][1] + 1))
    fun = lambda zo: prob.residual_vector_wd(to_full(zo)); pfun = lambda zo: prob.residual_vector_wd(to_full(zo), differentiable_pressure=True)
    log(f"state {job_id}: it {cur['it']}, fixed_state {fixed_state}, n_opt {n_opt}, rows {r_end.numel()}, cost {cost:.17e}, checkpoint cost field {cur.get('cost')}")
    # ---- v4 (verifier 16:00:50Z, V367): endpoint validation BEFORE the expensive build; a FREE endpoint without a stored final record is an explicit failure
    STORED_COORDS = "optimizer (z_c, z_w) with reduced tail-constrained coefficients"
    finals = sorted(f for f in os.listdir(run) if f.startswith("linearization_") and f.endswith("_final.npz"))
    status = dict(accepted=True, failures=[])
    def fail(msg):
        status["accepted"] = False; status["failures"].append(msg); log("FAIL: " + msg)
    endpoint = None
    if not fixed_state:
        if not finals:
            fail("FREE endpoint without a stored final linearization record"); write_failed(out_dir, out_json, job_id, status); return
        fpath = os.path.join(run, finals[-1]); Z = np.load(fpath)
        endpoint = dict(stored_record=finals[-1], stored_sha256=sha(fpath), stored_it=int(Z["it"]), checkpoint_it=int(cur["it"]), it_match=(int(Z["it"]) == int(cur["it"])), stored_kind=str(Z["jacobian_kind"]), kind_match=(str(Z["jacobian_kind"]) == "J_cw"),
                        stored_coordinates=str(Z["coordinates"]), coordinates_match=(str(Z["coordinates"]) == STORED_COORDS), stored_c_l=float(Z["c_l"]), stored_omega=float(Z["omega"]), params_match=(float(Z["c_l"]) == float(phys["c_l"]) and float(Z["omega"]) == float(phys["omega"])),
                        z_opt_bitwise_equal=bool(np.array_equal(Z["z_opt"], z_opt.detach().cpu().numpy())), cost_check=dict(stored_cost=float(Z["cost"]), eval_cost=cost, equal=(float(Z["cost"]) == cost), r_norm2_equal=(float(Z["r_norm2"]) == float(r_end @ r_end))))
        endpoint["ok"] = bool(endpoint["it_match"] and endpoint["kind_match"] and endpoint["coordinates_match"] and endpoint["params_match"] and endpoint["z_opt_bitwise_equal"] and endpoint["cost_check"]["equal"] and endpoint["cost_check"]["r_norm2_equal"])
        log(f"endpoint validation: {json.dumps({k: v for k, v in endpoint.items() if k not in ('stored_sha256',)}, default=str)}")
        if not endpoint["ok"]:
            fail("stored final record does not match the selected endpoint (iteration, kind, coordinates, parameters, vector or cost)"); write_failed(out_dir, out_json, job_id, status, endpoint=endpoint); return
    t1 = time.time(); J = jacobian_fwd(fun, z_opt, chunk=chunk); Jp = param_columns(pfun, z_opt, pidx)
    for j, k in enumerate(pidx):
        J[:, k] = Jp[:, j]
    if dev.startswith("cuda"): torch.cuda.synchronize()
    t_jcw = time.time() - t1
    colnorm = (J * J).sum(0).clamp_min(1e-30).sqrt()
    gen = W.phase_generator(model, zf); gen_red = tc.reduce(gen) if tc is not None else gen; gen_red = gen_red.clone(); gen_red[-2:] = 0.0
    # ---- comparison with the stored final J_cw record (FREE endpoints; the endpoint itself was validated before the build)
    cmp = dict(stored_record=None, applicable=(not fixed_state))
    if not fixed_state:
        fpath = os.path.join(run, finals[-1]); Z = np.load(fpath); perm = torch.as_tensor(Z["perm"], device=dev)
        # v2 (15:5xZ): the stored R is the Householder QR of the SCALED Jacobian J[:, perm] / D (linearization_record); compare in that convention: Gram of the scaled EVAL
        # Jacobian against R^T R, and the EVAL record's own R (same routine) bitwise against the stored R (v1 compared the unscaled J^T J: invalid field, see the note of 15:5xZ)
        R = torch.as_tensor(Z["R"], device=dev); Dst = torch.as_tensor(Z["D"], device=dev); Js = J[:, perm] / Dst[None, :]; G = Js.T @ Js; GR = R.T @ R
        cmp = dict(stored_record=finals[-1], stored_sha256=sha(fpath), applicable=True, endpoint=endpoint,
                   scale_check=dict(colnorm_D_max_rel_diff=float(((colnorm[perm] - Dst).abs() / Dst.clamp_min(1e-300)).max()), equal=bool(torch.equal(colnorm[perm], Dst)), criterion="bitwise equality of the column norms D (judged)"),
                   gram_check=dict(scaled_rel_frobenius_diff=float((G - GR).norm() / GR.norm()), scaled_max_abs_diff=float((G - GR).abs().max()), tolerance_rel_frobenius=1e-12,
                                   passed=bool(float((G - GR).norm() / GR.norm()) <= 1e-12),
                                   criterion="judged (lead 15:52:20Z item 1): ||R^T R - Js^T Js||_F / ||R^T R||_F <= 1e-12, where R is the stored Householder QR factor of the scaled Jacobian J[:, perm]/D and Js the scaled EVAL J_cw; justification: both sides are float64 evaluations of the same Gram matrix of unit-norm columns (433009-term inner products, Householder QR), whose rounding is of order 1e-15 to 1e-14 relative, so a difference above 1e-12 would show a different Jacobian; a Gram equality is not a matrix equality (Q is not retained): the record-summary comparison below is the bitwise check"))
        if not cmp["scale_check"]["equal"]:
            fail("column norms D differ from the stored record")
        if not cmp["gram_check"]["passed"]:
            fail("scaled Gram matrices differ above 1e-12 relative")
        del G, GR, R, Js
    log(f"J_cw built in {t_jcw:.1f} s; comparison with the stored record: {json.dumps({k: v for k, v in cmp.items() if k != 'note'}, default=str)}")
    W.linearization_record(os.path.join(out_dir, f"linearization_{int(cur['it']):05d}_eval_Jcw.npz"), int(cur["it"]), J, r_end, colnorm, pidx, gauge_rows, gen_red, z_opt, phys, cost, note="EVAL at the segment-end checkpoint (3.6 (o))")
    if finals:                                                                                   # v2: bitwise comparison of the two records (same routine, same convention)
        Zs = np.load(os.path.join(run, finals[-1])); Ze = np.load(os.path.join(out_dir, f"linearization_{int(cur['it']):05d}_eval_Jcw.npz"))
        cmp["record_fields_bitwise_equal"] = {k: bool(np.array_equal(Zs[k], Ze[k])) for k in ("R", "Qtr", "D", "perm", "z_opt", "generator_red")}; cmp["r_norm2_equal"] = bool(float(Zs["r_norm2"]) == float(Ze["r_norm2"]))
        cmp["record_summary_criterion"] = "judged: every saved summary field (R, Q^T r, D, perm, z_opt, generator) of the EVAL record equals the stored record bitwise; this establishes equality of the saved QR summaries, not of the full Jacobian (Q is not retained)"
        cmp["record_summary_equal"] = bool(all(cmp["record_fields_bitwise_equal"].values()) and cmp["r_norm2_equal"])
        if not cmp["record_summary_equal"]:
            fail("EVAL J_cw record summaries differ from the stored final record")
        log(f"record comparison (bitwise): {cmp['record_fields_bitwise_equal']} r_norm2 {cmp['r_norm2_equal']}")
    t2 = time.time(); J_c, info = W.complete_jacobian_from_Jcw(prob, to_full, z_opt, J, pidx, pm=pm, log=log)
    if dev.startswith("cuda"): torch.cuda.synchronize()
    t_jc = time.time() - t2
    cn = (J_c * J_c).sum(0).clamp_min(1e-30).sqrt()
    W.linearization_record(os.path.join(out_dir, f"linearization_{int(cur['it']):05d}_eval_complete.npz"), int(cur["it"]), J_c, r_end, cn, pidx, gauge_rows, gen_red, z_opt, phys, cost,
                           note="EVAL at the segment-end checkpoint (3.6 (o)); " + json.dumps(info, default=str), note_label="complete Jacobian J_c (pressure tables, weights and closure target and patterns differentiated)", kind="J_c")
    # smallest singular values of the scaled J_c with the gauge generator removed (information for Phase III; SPEC 5 reduced sensitivity comes later)
    try:
        Dm = cn.clamp_min(1e-30); Js = J_c / Dm
        sv = torch.linalg.svdvals(Js); sv_min = sv[-6:].cpu().tolist(); sv_max = float(sv[0])
    except Exception as ex:
        sv_min, sv_max = None, repr(ex)
    rec = dict(job_id=job_id, run=run, label=ck.get("label"), fixed_state=fixed_state, kind="EVAL", status=("ACCEPTED" if status["accepted"] else "FAILED"), failures=status["failures"], it=int(cur["it"]), counters=cur.get("counters"), lm_status=cur.get("lm_status"),
               checkpoint=dict(path=ck_path, sha256=sha(ck_path), z_opt_sha256_field=cur.get("z_opt_sha256"), ts=cur.get("ts")), config_sha256=hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest(),
               config_used_for_eval=dict(free_params=True, note="FIXED-CONTROL checkpoints: the configuration's c_l, omega appended and mapped to optimizer coordinates" if fixed_state else "as the run"), fixed_state_tie=fixed_tie,
               source_copy=dict(root=ROOT, manifest="SOURCES_SHA256.txt of the frozen copy (src/, validation/*.py, scripts/worker_d6.py) when run through run_frozen.sh", torch=torch.__version__, numpy=np.__version__),
               known_exit_code_note="the v1 copy of p2c_s2_S09 reported exit code 2 to l_launch.sh after printing DONE and writing its record; its launch.log has no exit line; cause not identified from the logs (v3 records the python exit explicitly at the end)",
               device=dev, chunk=chunk, n_opt=int(n_opt), n_rows=int(r_end.numel()), cost=cost, params=phys, pivot=cur["pivot"], geometry_base=gb,
               J_cw=dict(seconds=t_jcw, record=f"linearization_{int(cur['it']):05d}_eval_Jcw.npz", comparison_with_stored_final_record=cmp, column_norm_min=float(colnorm.min()), column_norm_max=float(colnorm.max())),
               J_c=dict(seconds=t_jc, record=f"linearization_{int(cur['it']):05d}_eval_complete.npz", info=info, column_norm_min=float(cn.min()), column_norm_max=float(cn.max()),
                        scaled_singular_values_smallest_six=sv_min, scaled_singular_value_largest=sv_max, scaling="columns divided by their norms (no gauge projection yet)"),
               code_sha256=W.code_versions(), launcher_manifest=(open(os.path.join(ROOT, "SOURCES_SHA256.txt")).read() if os.path.exists(os.path.join(ROOT, "SOURCES_SHA256.txt")) else None),
               seconds=time.time() - t0, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    with open(out_json, "x") as fh:
        json.dump(rec, fh, indent=1, default=str)
    log(f"J_c in {t_jc:.1f} s; smallest scaled singular values {sv_min}; DONE {out_json} {time.time() - t0:.0f}s")
    del J, J_c
    if dev.startswith("cuda"): torch.cuda.synchronize()
    code = 0 if status["accepted"] else 3
    print(f"EXIT {code} ({rec['status']})", flush=True); sys.stdout.flush(); os._exit(code)          # v3/v4: explicit exit code; a FAILED record exits 3 and is never an accepted record


if __name__ == "__main__":
    main()
