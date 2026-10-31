#!/usr/bin/env python
"""S11_own random_scaled_2: resolved directional closure action (verifier V345/V347 request; lead 15:27:53Z item 6: diagnostic, no outcome change).
The G3 add-on's J_c v replaced the closure block by a five-point difference of the fresh closure rows along v with the step h = 1e-4 / |v|; with |v| = 4.2e13
(the direction is unit in the SCALED coordinates D X, so its components span 13 orders of magnitude) that step leaves both parameters and most coefficients
bitwise unchanged (V345). This script computes the closure action from the PRODUCTION complete Jacobian: J_cw at the capture's base state (jacobian_fwd of
residual_vector_wd plus the differentiable-pressure parameter columns, as the worker), then complete_jacobian_from_Jcw (closure target correction and the
carried-pattern parameter columns, each column with its own resolved step), and contracts J_c[closure rows] with the captured direction v. It reports:
the captured J_c v closure block (from the capture NPZ) against J_c[closure] v (norms, difference norm, cosine); five-point directional differences of the
fresh closure rows along v at several steps h (1e-4/|v| as the add-on, and larger steps) with the number of coordinates that actually change at each step;
r . (J_c v) against the complete derivative d = g_c . v and the pattern contribution; the G3 floor F = 1e-3 ||r|| ||J_c v|| with the captured and with the
resolved J_c v, and the registered-rule errors of the saved O1 and gauge-subtracted ladders re-judged with the resolved floor (information only: the
outcomes are floor-independent, PASS_rel = PASS = false). No gate, threshold, estimator or pass rule changes. Usage: python validation/s11_closure_diag.py <abs capture json> [device]"""
import sys, os, json, time, hashlib
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False; torch.backends.cudnn.allow_tf32 = False
from validation.gates import Case, PAIRS, ROOT, code_hashes
from validation.g3_addon import ladder_report, HS7, HS5
from src.optimization.lm import jacobian_fwd, param_columns
import importlib.util
spec = importlib.util.spec_from_file_location("worker_d6", os.path.join(ROOT, "scripts", "worker_d6.py")); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W)


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main():
    cap_json = sys.argv[1]; dev = sys.argv[2] if len(sys.argv) > 2 else ("cuda:0" if torch.cuda.is_available() else "cpu")
    cap = json.load(open(cap_json)); cap_npz = os.path.join(os.path.dirname(cap_json), os.path.basename(cap["arrays_npz"]["path"])); Z = np.load(cap_npz)
    assert sha(cap_npz) == cap["arrays_npz"]["sha256"], "capture NPZ hash mismatch"
    out_json = os.path.join(ROOT, "validation", "s11_closure_diag_random_scaled_2.json"); out_npz = out_json.replace(".json", "_arrays.npz")
    for p in (out_json, out_npz):
        if os.path.exists(p):
            raise FileExistsError(p)
    t0 = time.time(); log = lambda m: print(time.strftime("%H:%M:%S", time.gmtime()) + " " + m, flush=True)
    case = Case(cap["case"], dev, start=os.path.join(ROOT, "starts", "S11_nest6_cl0.42_om0.3_p0.pt")); prob, model, pm = case.prob, case.model, case.pm
    zo = case.z_opt.detach().clone(); to_full = case.to_full_opt; n = zo.numel()
    assert np.array_equal(Z["z_base_opt"], zo.cpu().numpy()), "base reduced vector differs from the capture"
    v = torch.as_tensor(Z["direction"], device=dev); assert hashlib.sha256(Z["direction"].tobytes()).hexdigest() == cap["direction_sha256"]
    blocks = case.block_slices; a0, a1 = blocks["closure"]; sl = slice(a0, a1)
    jcv_cap = torch.as_tensor(Z["Jc_v"], device=dev); r = case.r; d = float(cap["derivative_complete"])
    # ---- production J_cw and J_c at the base
    pidx = [n - 2, n - 1]
    fun = lambda q: prob.residual_vector_wd(to_full(q)); pfun = lambda q: prob.residual_vector_wd(to_full(q), differentiable_pressure=True)
    t1 = time.time(); J = jacobian_fwd(fun, zo, chunk=256); Jp = param_columns(pfun, zo, pidx)
    for j, k in enumerate(pidx):
        J[:, k] = Jp[:, j]
    t_jcw = time.time() - t1; t2 = time.time()
    J_c, info = W.complete_jacobian_from_Jcw(prob, to_full, zo, J, pidx, pm=pm, log=log); t_jc = time.time() - t2
    jcw_v = J @ v; jc_v = J_c @ v
    # ---- comparisons on the closure block
    def blk(x):
        return x[sl]
    cos = lambda a, b: float((a @ b) / (a.norm() * b.norm() + 1e-300))
    cmp = dict(closure_rows=int(a1 - a0), captured_Jcv_closure_norm=float(blk(jcv_cap).norm()), resolved_Jc_v_closure_norm=float(blk(jc_v).norm()), Jcw_v_closure_norm=float(blk(jcw_v).norm()),
               diff_norm_captured_vs_resolved=float((blk(jcv_cap) - blk(jc_v)).norm()), cosine_captured_vs_resolved=cos(blk(jcv_cap), blk(jc_v)),
               nonclosure_diff_norm_captured_vs_resolved=float((jcv_cap - jc_v).norm() ** 2 - (blk(jcv_cap) - blk(jc_v)).norm() ** 2) ** 0.5 if False else float(torch.cat([(jcv_cap - jc_v)[:a0], (jcv_cap - jc_v)[a1:]]).norm()),
               nonclosure_norm=float(torch.cat([jc_v[:a0], jc_v[a1:]]).norm()), whole_captured_norm=float(jcv_cap.norm()), whole_resolved_norm=float(jc_v.norm()))
    # ---- directional five-point differences of the fresh closure rows along v at several steps, with the count of coordinates that change
    crow = lambda q: prob.closure_rows(to_full(q), closure=prob.closure_state_at(to_full(q)))
    vn = float(v.norm()); fd = {}
    base_crow = crow(zo)
    for lab, h in (("1e-4/|v| (the add-on's step)", 1e-4 / vn), ("1e-2/|v|", 1e-2 / vn), ("1/|v|", 1.0 / vn), ("1e2/|v|", 1e2 / vn), ("1e4/|v|", 1e4 / vn)):
        qp = zo + h * v; qm = zo - h * v; q2p = zo + 2 * h * v; q2m = zo - 2 * h * v
        changed = int((qp != zo).sum()); changed_params = int((qp[-2:] != zo[-2:]).sum())
        D4 = (8 * (crow(qp) - crow(qm)) - (crow(q2p) - crow(q2m))) / (12 * h)
        fd[lab] = dict(h=h, coordinates_changed_of=f"{changed} of {n}", parameters_changed=changed_params, norm=float(D4.norm()), diff_to_resolved_norm=float((D4 - blk(jc_v)).norm()), cosine_to_resolved=cos(D4, blk(jc_v)), diff_to_captured_norm=float((D4 - blk(jcv_cap)).norm()))
        log(f"closure five-point along v, h = {lab}: {json.dumps({k: fd[lab][k] for k in ('coordinates_changed_of', 'parameters_changed', 'norm', 'diff_to_resolved_norm', 'cosine_to_resolved')})}")
    # ---- r . J_c v against d = g_c . v and the pattern contribution of the complete gradient
    g_c = torch.as_tensor(Z["g_c"], device=dev)
    _, parts = prob.complete_gradient(to_full(zo).detach(), return_parts=True); dsc = pm.describe(zo)
    pattern_contrib = (float(parts["pattern_fd"][0]) * dsc["dcl_dzc"] * float(v[-2]) + float(parts["pattern_fd"][1]) * dsc["domega_dzw"] * float(v[-1])) if parts.get("pattern_fd") is not None else 0.0
    rJ = dict(r_dot_Jc_v_resolved=float(r @ jc_v), r_dot_Jcw_v=float(r @ jcw_v), r_dot_Jcv_captured=float(r @ jcv_cap), g_c_dot_v=float(g_c @ v), derivative_complete_record=d, pattern_contribution_to_g_c_dot_v=pattern_contrib,
              r_dot_Jc_v_resolved_plus_pattern=float(r @ jc_v) + pattern_contrib, rel_diff_resolved_plus_pattern_vs_d=(float(r @ jc_v) + pattern_contrib - d) / d,
              closure_block_r_dot=dict(resolved=float(r[sl] @ jc_v[sl]), captured=float(r[sl] @ jcv_cap[sl]), Jcw=float(r[sl] @ jcw_v[sl])))
    # ---- floors and the re-judged (information) ladders from the capture's saved O1 and gauge values
    F_cap = float(cap["floor"]); F_res = 1e-3 * float(r.norm()) * float(jc_v.norm())
    pts = cap["points"]; vals = {}; gs = {}
    for k, pv in pts.items():
        t = float(k); vals[t] = pv["O1_device"]; gs[t] = pv["gauge"]
    valid = {h: bool(cap["step_valid"][f"{h:.0e}"]) for h in HS7}
    rej = {}
    for lad_name, lad in (("v1.4_ladder", HS5), ("seven_step_ladder", HS7)):
        for est, sub in (("O1", False), ("O_tilde_gauge_subtracted", True)):
            o_res = ladder_report(vals, gs, d, F_res, lad, sub, valid); o_cap = ladder_report(vals, gs, d, F_cap, lad, sub, valid)
            rej[f"{est}:{lad_name}"] = dict(PASS_with_resolved_floor=o_res["PASS"], PASS_with_captured_floor=o_cap["PASS"], PASS_rel=o_res["PASS_rel"], min_second_order_error=min(o_res["errors_second_order"].values()), richardson_resolved=o_res["richardson_error"])
    rec = dict(case=cap["case"], direction=cap["direction"], capture=dict(path=cap_json, sha256=sha(cap_json), npz_sha256=cap["arrays_npz"]["sha256"]), device=str(dev), direction_norm=vn,
               J_cw_seconds=t_jcw, J_c_seconds=t_jc, J_c_info=info, closure_block=cmp, closure_five_point_along_v=fd, r_dot=rJ,
               floor=dict(captured=F_cap, resolved=F_res, ratio=F_res / F_cap, rule="F = 1e-3 ||r|| ||J_c v||"), rejudged_information_only=rej,
               statement="Diagnostic only. The add-on's J_c v closure block was formed by a five-point difference along v with h = 1e-4/|v|, which leaves most coordinates (and both parameters) bitwise unchanged for this direction (|v| = 4.2e13); the resolved closure action J_c[closure] v uses the production per-column closure derivatives (complete_jacobian_from_Jcw, each column with its own step). The registered G3 outcomes are floor-independent (PASS_rel = false) and stand; any change of the add-on's construction is a prospective amendment for the lead.",
               code_sha256=code_hashes(), launcher_manifest=(open(os.path.join(ROOT, "SOURCES_SHA256.txt")).read() if os.path.exists(os.path.join(ROOT, "SOURCES_SHA256.txt")) else None), seconds=time.time() - t0, ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    np.savez_compressed(out_npz, Jc_v_resolved=jc_v.cpu().numpy(), Jcw_v=jcw_v.cpu().numpy(), Jcv_captured=jcv_cap.cpu().numpy(), Jc_closure_rows=J_c[sl, :].cpu().numpy(), direction=v.cpu().numpy(), r=r.cpu().numpy())
    rec["arrays_npz"] = dict(path=os.path.relpath(out_npz, ROOT), sha256=sha(out_npz), keys=["Jc_v_resolved", "Jcw_v", "Jcv_captured", "Jc_closure_rows", "direction", "r"])
    with open(out_json, "x") as fh:
        json.dump(rec, fh, indent=1, default=str)
    log(f"closure block: captured |Jcv| {cmp['captured_Jcv_closure_norm']:.6e} resolved |Jc v| {cmp['resolved_Jc_v_closure_norm']:.6e} diff {cmp['diff_norm_captured_vs_resolved']:.3e} cos {cmp['cosine_captured_vs_resolved']:.6f} | r.Jc v + pattern vs d rel {rJ['rel_diff_resolved_plus_pattern_vs_d']:.3e} | floor captured {F_cap:.4e} resolved {F_res:.4e}")
    log(f"DONE {out_json} {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
