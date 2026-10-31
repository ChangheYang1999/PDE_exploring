#!/usr/bin/env python
"""scripts/linear_response_start.py v1 (2026-10-30T02:4xZ; lead 22:04:42Z item 2 (iii), 02:05:41Z item 2; verifier V573): PROFILE start candidates at a
displaced parameter point from a branch end's complete J_c EVAL factor, written as worker start files (initial conditions, not results).

Model (from the EVAL npz written by scripts/worker_d6.py linearization_record): J[:, perm] / D = Q R with D stored PERMUTED (D[i] = ||J[:, perm[i]]||,
null columns clamped by the LM to 1e-12 D_max or 1e-30 in the squared norm), q = Q^T r, r_norm2 = ||r||^2, cost = ||r||^2 / 2; z_opt in optimizer
coordinates (reduced tail-constrained coefficients, z_c, z_w); param_positions = positions of the two parameter columns in the permuted order. With the
scaled coordinates s_i = D_i dz[perm_i], the affine model of the self-consistent objective is M(s) = 1/2 ||q + R s||^2 + 1/2 (r_norm2 - ||q||^2),
M(0) = cost.
Linear response (zero-preserving; V573): for the parameter displacement s_p = D_p dz_p the coefficient block minimizes ||R_a s_a + R_p s_p||:
s_a = -R_a^+ R_p s_p through the SVD of R_a with the cutoff 1e-8 relative to its largest singular value; the exactly null columns (block E, l = 1:
R column exactly zero) are dropped (s = 0 there). Then dz[perm_i] = s_i / D_i (the saved D is used as it is, with no second permutation), the
response start is TailConstraints.expand(ParamMap.expand(z_opt + dz)) and the kept start is the same map of z_opt with only the parameter slots
displaced; both at the displaced parameters. The affine identity 2 [M(resp) - M(kept)] = -2 q^T P v - ||P v||^2 with v = R_p s_p, P = U_k U_k^T
(lead 02:05:41Z item 2) is evaluated from the formula and directly.
Correctness tests (lead 02:05:41Z item 2 (a)); every result is recorded in the json, a failure sets tests_ok false and marks the files UNUSABLE):
 (i)  dz_p = 0 returns the end state exactly (z_opt bitwise, full vector bitwise against the checkpoint-derived expansion, parameters equal);
 (ii) the affine prediction computed twice, from the formula and as M(s) - M(s_kept) with s re-gathered from the dz actually written into the start
      files (reduce of the written full vector, s_i = D_i dz[perm_i]), agreeing to a relative 1e-10;
 (iii) nonidentity-permutation fixtures (small random least-squares problems with the parameter columns in the middle, a null column, a shuffled
      permutation and unequal column scales) against a direct unscaled least-squares solution and the direct objective difference, relative 1e-10;
 (iv) a finite omega move is the optimizer-coordinate displacement log(omega_new) - log(omega_base) (c_l: logit difference); tangent values are
      reported with the label 'tangent (not used)'.
Not a test (lead item 2 (b)): the iteration-0 O1 of the kept and of the response start at the displaced point (the worker's fresh-entry path:
choose_pivot, ensure_geometry at the displaced parameters, phase_align, reduce/expand maps, objective_at, commit_aux; gauge row separate) are
BOTH reported beside the affine predictions M(kept) and M(resp); the measured difference agrees with the prediction only up to the nonlinear
remainder (and the fresh quadrature geometry), so it is reported, not gated. The PROFILE selection rule (lead 22:04:42Z item 2) takes the lower
measured iteration-0 O1 (entry path) of the candidates at the same actual parameters, map, gauge and objective settings; the json names it.
Diagnostic only (item 2 (c)): the fully relaxed affine minimizer s_a = -R_a^+ (q + v) is reported as 'relaxed affine minimizer, diagnostic' and is
never written as a start.
Usage:
  python scripts/linear_response_start.py <run dir> --out <prefix> (--domega X | --dzw X) (--dcl Y | --dzc Y) [--eval <complete EVAL npz>]
         [--cutoff 1e-8] [--device cuda:0] [--no-objective]
  python scripts/linear_response_start.py --fixtures-only
Writes <prefix>_resp.pt and <prefix>_kept.pt (exclusive create; z full with the displaced parameters, config, free_params true, meta) and <prefix>.json."""
import os, sys, json, time, math, hashlib, argparse, importlib.util
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, ROOT)
import numpy as np
import torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False; torch.backends.cudnn.allow_tf32 = False
DT = torch.float64
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
now = lambda: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
TOOL = "scripts/linear_response_start.py v1"


def response_from_factor(R, D, perm, param_positions, Qtr, r_norm2, dz_p, cutoff=1e-8):
    """Pure numpy core (tested by the fixtures). Returns dz (unpermuted optimizer coordinates, parameter slots = dz_p), dz_kept, the scaled
    vectors and the affine quantities. Null columns = columns of R that are exactly zero (dropped: s = dz = 0 there)."""
    R = np.asarray(R, dtype=np.float64); D = np.asarray(D, dtype=np.float64); q = np.asarray(Qtr, dtype=np.float64); perm = np.asarray(perm, dtype=int)
    n = R.shape[0]; pp = np.asarray(param_positions, dtype=int)
    is_p = np.zeros(n, bool); is_p[pp] = True
    colnorm_R = np.sqrt((R ** 2).sum(0))
    null = (colnorm_R == 0.0) & (~is_p)
    oth = np.where((~is_p) & (~null))[0]
    R_a = R[:, oth]; R_p = R[:, pp]
    s_p = D[pp] * np.asarray(dz_p, dtype=np.float64)
    v = R_p @ s_p
    U, S, Vt = np.linalg.svd(R_a, full_matrices=False)
    keep = S > cutoff * S[0]; k = int(keep.sum())
    Uk, Sk, Vk = U[:, keep], S[keep], Vt[keep]
    coef = Uk.T @ v
    s_a = -(Vk.T @ (coef / Sk))
    Pv = Uk @ coef
    s = np.zeros(n); s[oth] = s_a; s[pp] = s_p
    s_kept = np.zeros(n); s_kept[pp] = s_p
    dz = np.zeros(n); dz[perm] = s / D                    # dz[perm_i] = s_i / D_i; the saved D is already permuted (no second permutation)
    dz_kept = np.zeros(n); dz_kept[perm] = s_kept / D
    const = 0.5 * (float(r_norm2) - float(q @ q))
    M = lambda ss: 0.5 * float(np.sum((q + R @ ss) ** 2)) + const
    M_base, M_kept, M_resp = M(np.zeros(n)), M(s_kept), M(s)
    diff_formula = -float(q @ Pv) - 0.5 * float(Pv @ Pv)
    diff_direct = M_resp - M_kept
    # relaxed affine minimizer (diagnostic only; never a start): s_a = -R_a^+ (q + v)
    coef_r = Uk.T @ (q + v); s_a_relax = -(Vk.T @ (coef_r / Sk)); s_relax = np.zeros(n); s_relax[oth] = s_a_relax; s_relax[pp] = s_p
    M_relax = M(s_relax)
    nv = float(np.linalg.norm(v)); nPv = float(np.linalg.norm(Pv))
    return dict(dz=dz, dz_kept=dz_kept, s=s, s_kept=s_kept, s_a=s_a, oth=oth, null=np.where(null)[0], pp=pp, n=n, rank_kept=k, n_coef_columns=int(len(oth)),
                sigma_max=float(S[0]), sigma_min_kept=float(Sk[-1]), sigma_min_all=float(S[-1]), n_dropped_by_cutoff=int((~keep).sum()), cutoff=cutoff,
                norm_v=nv, norm_Pv=nPv, absorption_c=(math.sqrt(max(nv ** 2 - nPv ** 2, 0.0)) / nv if nv > 0 else float("nan")),
                M_base=M_base, M_kept=M_kept, M_resp=M_resp, diff_formula=diff_formula, diff_direct=diff_direct,
                relaxed_diagnostic=dict(label="relaxed affine minimizer, diagnostic (not a start; lead 02:05:41Z item 2 (c))", M_relax=M_relax, norm_s_a_relax=float(np.linalg.norm(s_a_relax)),
                                        predicted_relative_decrease_vs_kept=((M_kept - M_relax) / M_kept if M_kept > 0 else float("nan"))),
                M_fn=M)


def rel_close(a, b, tol):
    return abs(a - b) <= tol * max(abs(a), abs(b), 1e-300)


def fixture_tests(seed=12345):
    """(iii) nonidentity-permutation fixtures. Each fixture: random J (m x n) with two parameter columns in the MIDDLE of the original order, one
    exactly null column, unequal column scales; perm = others (+ a shuffle in fixture B) followed by the parameter columns; D = column norms (null
    clamped as the LM does); Q R = J[:, perm] / D by Householder QR (numpy); q = Q^T r. Checks against the direct unscaled least squares and the
    direct objective difference."""
    rng = np.random.default_rng(seed); out = []
    for name, shuffle, dz_p in (("A_params_middle_null_col", False, np.array([0.3, -0.7])), ("B_shuffled_others", True, np.array([-0.05, 0.02])), ("C_zero_displacement", True, np.array([0.0, 0.0])), ("D_params_first", False, np.array([1e-3, 2e-3]))):
        m, n = 60, 9; param_idx = [0, 1] if name.startswith("D") else [3, 7]; null_col = 5
        J = rng.normal(size=(m, n)); J[:, 2] *= 1e3; J[:, 6] *= 1e-3; J[:, null_col] = 0.0
        r = rng.normal(size=m)
        others = [k for k in range(n) if k not in param_idx]
        if shuffle:
            others = list(rng.permutation(others))
        perm = np.array(others + param_idx)
        cn = np.sqrt((J ** 2).sum(0)); Dfull = np.maximum(np.maximum(cn ** 2, 1e-30), 1e-12 * (cn ** 2).max()); colnorm = np.sqrt(Dfull)
        D = colnorm[perm]; Js = J[:, perm] / D[None, :]
        Q, R = np.linalg.qr(Js); q = Q.T @ r; r_norm2 = float(r @ r)
        pp = np.arange(n - 2, n)
        res = response_from_factor(R, D, perm, pp, q, r_norm2, dz_p, cutoff=1e-8)
        dz = res["dz"]
        # direct: minimize ||J_nn dz_nn + J_p dz_p|| over the non-null coefficient columns
        nn = [k for k in range(n) if k not in param_idx and k != null_col]
        x = np.linalg.lstsq(J[:, nn], -(J[:, param_idx] @ dz_p), rcond=None)[0]
        err_dz = float(np.max(np.abs(dz[nn] - x)) / max(np.max(np.abs(x)), 1e-300)) if np.max(np.abs(x)) > 0 else float(np.max(np.abs(dz[nn])))
        ok_dz = (err_dz <= 1e-10) if np.max(np.abs(x)) > 0 else (err_dz == 0.0)
        ok_p = bool(np.array_equal(dz[param_idx], dz_p)); ok_null = bool(dz[null_col] == 0.0)
        dz_k = np.zeros(n); dz_k[param_idx] = dz_p
        direct_diff = 0.5 * float(np.sum((r + J @ dz) ** 2)) - 0.5 * float(np.sum((r + J @ dz_k) ** 2))
        ok_diff = rel_close(res["diff_direct"], direct_diff, 1e-10) and rel_close(res["diff_formula"], direct_diff, 1e-10) if abs(direct_diff) > 0 else (res["diff_direct"] == 0.0 and res["diff_formula"] == 0.0)
        ok_zero = True
        if not np.any(dz_p):
            ok_zero = bool(np.all(dz == 0.0))
        M_kept_direct = 0.5 * float(np.sum((r + J @ dz_k) ** 2)); ok_Mk = rel_close(res["M_kept"], M_kept_direct, 1e-10)
        out.append(dict(fixture=name, m=m, n=n, param_idx=param_idx, null_col=null_col, perm=[int(p) for p in perm], perm_is_identity=bool(np.array_equal(perm, np.arange(n))), dz_p=[float(a) for a in dz_p],
                        max_rel_err_dz_coefficients=err_dz, dz_params_exact=ok_p, dz_null_col_zero=ok_null, diff_formula=res["diff_formula"], diff_direct_from_factor=res["diff_direct"], diff_direct_unscaled=direct_diff,
                        M_kept_factor=res["M_kept"], M_kept_direct=M_kept_direct, zero_displacement_gives_zero_dz=ok_zero, passed=bool(ok_dz and ok_p and ok_null and ok_diff and ok_zero and ok_Mk)))
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("run", nargs="?"); ap.add_argument("--eval"); ap.add_argument("--out"); ap.add_argument("--domega", type=float); ap.add_argument("--dzw", type=float)
    ap.add_argument("--dcl", type=float); ap.add_argument("--dzc", type=float); ap.add_argument("--cutoff", type=float, default=1e-8); ap.add_argument("--device", default="cuda:0"); ap.add_argument("--no-objective", action="store_true")
    ap.add_argument("--fixtures-only", action="store_true")
    a = ap.parse_args(); t0 = time.time()
    log = lambda m: print(time.strftime("%H:%M:%S", time.gmtime()) + " " + m, flush=True)
    fx = fixture_tests(); fx_ok = all(f["passed"] for f in fx)
    log("(iii) fixtures: " + "; ".join(f"{f['fixture']} {'PASS' if f['passed'] else 'FAIL'} (max rel err dz {f['max_rel_err_dz_coefficients']:.2e})" for f in fx))
    if a.fixtures_only:
        print(json.dumps(dict(tool=TOOL, tool_sha256=sha(os.path.abspath(__file__)), fixtures=fx, fixtures_ok=fx_ok, ts=now()), indent=1, default=str)); return 0 if fx_ok else 2
    if not a.run or not a.out:
        raise SystemExit("usage: <run dir> --out <prefix> with a displacement (see the docstring)")
    if (a.domega is not None and a.dzw is not None) or (a.dcl is not None and a.dzc is not None):
        raise SystemExit("REFUSED: give either --domega or --dzw, and either --dcl or --dzc")
    for suf in ("_resp.pt", "_kept.pt", ".json"):
        if os.path.exists(a.out + suf):
            raise FileExistsError(a.out + suf)
    dev = a.device
    spec = importlib.util.spec_from_file_location("worker_d6", os.path.join(ROOT, "scripts", "worker_d6.py")); W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W)
    from src.optimization.tail_constraints import TailConstraints
    from src.optimization.param_map import ParamMap
    run = os.path.abspath(a.run); ck_path = os.path.join(run, "checkpoint_segment_end.pt"); ck = torch.load(ck_path, map_location="cpu", weights_only=False)
    cfg = dict(ck["config"]); job_id = ck["job_id"]; cur = ck["current"]
    if not cfg.get("free_params", False):
        raise SystemExit("REFUSED: the run is not a free-parameter run (the EVAL factor of a FIXED state has no optimizer parameter history to displace from)")
    ev_path = a.eval
    if ev_path is None:
        cands = sorted(f for f in os.listdir(os.path.join(ROOT, "validation", "jc_eval", job_id)) if f.endswith("_eval_complete.npz"))
        if not cands:
            raise SystemExit("no complete EVAL npz found for " + job_id)
        ev_path = os.path.join(ROOT, "validation", "jc_eval", job_id, cands[-1])
    ev_path = os.path.abspath(ev_path); Z = np.load(ev_path, allow_pickle=True)
    # base consistency: the EVAL factor belongs to the checkpoint's end state
    z_opt_ck = np.asarray(cur["z_opt"], dtype=np.float64); z_opt_np = np.asarray(Z["z_opt"], dtype=np.float64)
    base_checks = dict(z_opt_bitwise_equal_checkpoint=bool(np.array_equal(z_opt_ck, z_opt_np)), it_equal=(int(Z["it"]) == int(cur["it"])), jacobian_kind=str(Z["jacobian_kind"]), kind_is_J_c=(str(Z["jacobian_kind"]) == "J_c"),
                       coordinates=str(Z["coordinates"]), supports_spec7_complete=bool(Z["supports_spec7_complete"]), eval_it=int(Z["it"]), checkpoint_it=int(cur["it"]))
    if not (base_checks["z_opt_bitwise_equal_checkpoint"] and base_checks["it_equal"] and base_checks["kind_is_J_c"]):
        raise SystemExit(f"REFUSED: the EVAL record does not match the checkpoint's end state or is not J_c: {base_checks}")
    P0 = json.loads(str(Z["params"])); c_l0, om0, zc0, zw0 = float(P0["c_l"]), float(P0["omega"]), float(P0["z_c"]), float(P0["z_w"])
    pm = ParamMap(free=True); lo, hi = pm.lo, pm.hi
    # (iv) the displacement in optimizer coordinates (exact), tangent values labelled
    disp = dict(requested=dict(domega=a.domega, dzw=a.dzw, dcl=a.dcl, dzc=a.dzc))
    if a.dzw is not None:
        dzw = float(a.dzw); om1 = math.exp(zw0 + dzw); disp["omega_move"] = dict(given="dz_w", dz_w=dzw, omega_new=om1)
    else:
        dom = float(a.domega or 0.0); om1 = om0 + dom
        if not om1 > 0:
            raise SystemExit("REFUSED: omega_new must be positive")
        dzw = math.log(om1) - math.log(om0); disp["omega_move"] = dict(given="domega", domega=dom, omega_new=om1, dz_w_exact=dzw, dz_w_tangent_not_used=dom / om0, tangent_label="tangent (not used): domega / omega_base")
    if a.dzc is not None:
        dzc = float(a.dzc); cl1 = lo + (hi - lo) / (1.0 + math.exp(-(zc0 + dzc))); disp["c_l_move"] = dict(given="dz_c", dz_c=dzc, c_l_new=cl1)
    else:
        dcl = float(a.dcl or 0.0); cl1 = c_l0 + dcl
        if not (lo < cl1 < hi):
            raise SystemExit("REFUSED: c_l_new outside the open domain (0.4, 0.5)")
        dzc = math.log((cl1 - lo) / (hi - cl1)) - zc0; disp["c_l_move"] = dict(given="dcl", dcl=dcl, c_l_new=cl1, dz_c_exact=dzc, dz_c_tangent_not_used=(dcl / float(P0["dcl_dzc"]) if float(P0.get("dcl_dzc", 0) or 0) else None), tangent_label="tangent (not used): dcl / (dc_l/dz_c)")
    dz_p = np.array([dzc, dzw]); zero_disp = not np.any(dz_p)
    log(f"run {job_id} it {int(cur['it'])}; EVAL {os.path.basename(ev_path)} (cost {float(Z['cost']):.6e}); base ({c_l0!r}, {om0!r}) z ({zc0!r}, {zw0!r}); displacement dz_c {dzc!r} dz_w {dzw!r} -> ({cl1!r}, {om1!r})")
    R = Z["R"]; D = Z["D"]; perm = Z["perm"]; pp = Z["param_positions"]; q = Z["Qtr"]; r_norm2 = float(Z["r_norm2"])
    t1 = time.time(); res = response_from_factor(R, D, perm, pp, q, r_norm2, dz_p, cutoff=a.cutoff); t_svd = time.time() - t1
    log(f"factor: n {res['n']}, coefficient columns {res['n_coef_columns']} (null dropped {len(res['null'])}: {res['null'].tolist()}), rank kept {res['rank_kept']} (cutoff {a.cutoff:g}: dropped {res['n_dropped_by_cutoff']}), sigma max {res['sigma_max']:.3e} min kept {res['sigma_min_kept']:.3e}; ||v|| {res['norm_v']:.3e} ||Pv|| {res['norm_Pv']:.3e} absorption c {res['absorption_c']:.3e}; {t_svd:.1f} s")
    log(f"affine: M(base) {res['M_base']:.9e} (cost {float(Z['cost']):.9e}), M(kept) {res['M_kept']:.9e}, M(resp) {res['M_resp']:.9e}; diff formula {res['diff_formula']:.9e} direct {res['diff_direct']:.9e}; relaxed (diagnostic) M {res['relaxed_diagnostic']['M_relax']:.9e}")
    ok_identity = rel_close(res["diff_formula"], res["diff_direct"], 1e-10) if not zero_disp else (res["diff_formula"] == 0.0 and res["diff_direct"] == 0.0)
    # control (i) in memory, always: dz_p = 0 returns the end state exactly
    res0 = response_from_factor(R, D, perm, pp, q, r_norm2, np.zeros(2), cutoff=a.cutoff)
    cfg1 = dict(cfg); cfg1.update(c_l=cl1, omega=om1, free_params=True)
    model, prob = W.build(cfg1, dev); tc = TailConstraints(model) if cfg.get("tail_constraints", True) else None
    to_full = (lambda zo: tc.expand(pm.expand(zo))) if tc is not None else (lambda zo: pm.expand(zo))
    to_opt = (lambda zf: pm.reduce(tc.reduce(zf))) if tc is not None else (lambda zf: pm.reduce(zf))
    z_opt = torch.as_tensor(z_opt_np, dtype=DT, device=dev)
    z_full_base = to_full(z_opt).detach()
    z0_new = z_opt + torch.as_tensor(res0["dz"], dtype=DT, device=dev); z0_full = to_full(z0_new).detach()
    test_i = dict(dz_all_zero=bool(np.all(res0["dz"] == 0.0)), z_opt_bitwise=bool(torch.equal(z0_new, z_opt)), full_vector_bitwise=bool(torch.equal(z0_full, z_full_base)),
                  params_equal=(float(z0_full[-2]) == float(z_full_base[-2]) and float(z0_full[-1]) == float(z_full_base[-1])), c_l=float(z0_full[-2]), omega=float(z0_full[-1]), eval_c_l=c_l0, eval_omega=om0,
                  params_equal_eval_1e15=(abs(float(z0_full[-2]) - c_l0) <= 1e-15 and abs(float(z0_full[-1]) - om0) <= 1e-15 * max(1.0, om0)))
    test_i["passed"] = bool(test_i["dz_all_zero"] and test_i["z_opt_bitwise"] and test_i["full_vector_bitwise"] and test_i["params_equal"])
    log(f"(i) dz_p = 0: {test_i}")
    # the two starts at the displaced point
    z_resp = z_opt + torch.as_tensor(res["dz"], dtype=DT, device=dev); z_kept = z_opt + torch.as_tensor(res["dz_kept"], dtype=DT, device=dev)
    zf_resp = to_full(z_resp).detach(); zf_kept = to_full(z_kept).detach()
    params_written = dict(resp=dict(c_l=float(zf_resp[-2]), omega=float(zf_resp[-1])), kept=dict(c_l=float(zf_kept[-2]), omega=float(zf_kept[-1])), target=dict(c_l=cl1, omega=om1))
    pw_ok = all(abs(params_written[k]["c_l"] - cl1) <= 1e-15 and abs(params_written[k]["omega"] - om1) <= 1e-15 * max(1.0, om1) for k in ("resp", "kept"))
    dz_a = res["dz"][: res["n"] - 2]; dz_stats = dict(norm_dz_a=float(np.linalg.norm(dz_a)), max_abs_dz_a=float(np.max(np.abs(dz_a))), norm_z_opt_a=float(np.linalg.norm(z_opt_np[:-2])), norm_s_a=float(np.linalg.norm(res["s_a"])), norm_s_p=float(np.linalg.norm(res["s"][res["pp"]])))
    # field change (training grid, unweighted Frobenius; discrete sampling diagnostic)
    with torch.no_grad():
        U_kept = model.fields_grid(zf_kept, need_vort=False)["U"]; U_resp = model.fields_grid(zf_resp, need_vort=False)["U"]; U_base_at_disp = None
        relU_resp_vs_kept = float((U_resp - U_kept).norm() / U_kept.norm().clamp_min(1e-300))
    log(f"starts: dz_a norm {dz_stats['norm_dz_a']:.3e} (|z_a| {dz_stats['norm_z_opt_a']:.3e}), max |dz_a| {dz_stats['max_abs_dz_a']:.3e}; relU(resp vs kept) on the training grid {relU_resp_vs_kept:.3e}; written params ok {pw_ok}")
    # write the start files (exclusive create)
    meta_common = dict(tool=TOOL, tool_sha256=sha(os.path.abspath(__file__)), run=run, job_id=job_id, checkpoint=ck_path, checkpoint_sha256=sha(ck_path), eval_npz=ev_path, eval_sha256=sha(ev_path), eval_it=int(Z["it"]), eval_cost=float(Z["cost"]),
                       base_params=dict(c_l=c_l0, omega=om0, z_c=zc0, z_w=zw0), displacement=disp, dz_p_optimizer=dict(dz_c=dzc, dz_w=dzw), params_after=dict(c_l=cl1, omega=om1), cutoff=a.cutoff,
                       rank_kept=res["rank_kept"], null_columns_dropped=res["null"].tolist(), affine=dict(M_base=res["M_base"], M_kept=res["M_kept"], M_resp=res["M_resp"], diff_formula=res["diff_formula"], diff_direct=res["diff_direct"]),
                       note="PROFILE start candidate at a displaced parameter point (lead 22:04:42Z item 2; initial condition, not a result); the worker's fresh-entry path applies choose_pivot, ensure_geometry, phase_align and the tail/parameter maps", ts=now(), device=dev, torch=torch.__version__, code_versions=W.code_versions())
    files = {}
    for nm, zf_, zo_ in (("resp", zf_resp, z_resp), ("kept", zf_kept, z_kept)):
        p = a.out + f"_{nm}.pt"
        meta = dict(meta_common, family=("PROFILE_linear_response_start" if nm == "resp" else "PROFILE_kept_coefficients_start"), candidate=nm, z_opt_written=zo_.detach().cpu().numpy().tolist())
        torch.save(dict(z=zf_.cpu(), config=cfg1, free_params=True, meta=meta, kind=f"PROFILE {'linear-response' if nm == 'resp' else 'kept-coefficient'} start ({TOOL}; initial condition, not a result)"), p)
        files[nm] = dict(path=os.path.abspath(p), sha256=sha(p))
    # (ii) re-gather s from the dz actually written into the files (reduce of the written full vector), prediction from the factor
    M = res["M_fn"]; gath = {}
    for nm in ("resp", "kept"):
        S_ = torch.load(files[nm]["path"], map_location="cpu", weights_only=False); zf_w = S_["z"].to(dev)
        zo_w = to_opt(zf_w).detach().cpu().numpy(); dz_w = zo_w - z_opt_np
        s_w = np.zeros(res["n"]); s_w[:] = D * dz_w[perm]
        gath[nm] = dict(M_from_file=M(s_w), max_abs_dz_diff_vs_memory=float(np.max(np.abs(dz_w - (res["dz"] if nm == "resp" else res["dz_kept"])))), z_opt_written_bitwise_equal_memory=bool(np.array_equal(np.asarray(S_["meta"]["z_opt_written"]), (z_resp if nm == "resp" else z_kept).detach().cpu().numpy())))
    diff_from_files = gath["resp"]["M_from_file"] - gath["kept"]["M_from_file"]
    ok_ii = rel_close(diff_from_files, res["diff_formula"], 1e-10) if not zero_disp else (diff_from_files == 0.0)
    test_ii = dict(diff_formula=res["diff_formula"], diff_direct_memory=res["diff_direct"], diff_from_written_files=diff_from_files, rel_diff_files_vs_formula=(abs(diff_from_files - res["diff_formula"]) / max(abs(res["diff_formula"]), 1e-300)), gather=gath, identity_formula_vs_direct_ok=ok_identity, passed=bool(ok_ii and ok_identity))
    log(f"(ii) affine prediction: formula {res['diff_formula']:.9e}, direct {res['diff_direct']:.9e}, from the written files {diff_from_files:.9e} (rel {test_ii['rel_diff_files_vs_formula']:.2e}); passed {test_ii['passed']}")
    test_iv = dict(dz_w_used=dzw, dz_c_used=dzc, omega_new_from_map=params_written["resp"]["omega"], c_l_new_from_map=params_written["resp"]["c_l"], omega_target=om1, c_l_target=cl1, exact_optimizer_displacement_used=True, tangent_values_labelled_not_used=True, params_written_match_target_1e15=pw_ok, passed=bool(pw_ok))
    # objective rows (not a test): the worker's fresh-entry iteration-0 O1 at the displaced point for both candidates
    obj = {}
    if not a.no_objective:
        for nm, zf_ in (("kept", zf_kept), ("resp", zf_resp)):
            t2 = time.time(); m_, p_ = W.build(cfg1, dev); tc_ = TailConstraints(m_) if tc is not None else None
            tf_ = (lambda zo: tc_.expand(pm.expand(zo))) if tc_ is not None else (lambda zo: pm.expand(zo)); to_ = (lambda zf: pm.reduce(tc_.reduce(zf))) if tc_ is not None else (lambda zf: pm.reduce(zf))
            zz = zf_.to(dev).clone()
            p_.pivot = p_.choose_pivot(zz); rebuilt = p_.ensure_geometry(zz)
            with torch.no_grad():
                r_raw, _ = p_.objective_at(zz)
            g0 = p_.row_blocks()[-1][1]
            za = p_.phase_align(zz); zo = to_(za); ze = tf_(zo)
            r_e, aux_e = p_.objective_at(ze); p_.commit_aux(aux_e)
            row = lambda r_: dict(O1=0.5 * float(r_ @ r_), gauge_part=0.5 * float(r_[g0:] @ r_[g0:]), O1_without_gauge=0.5 * float(r_[:g0] @ r_[:g0]), n_rows=int(r_.numel()))
            obj[nm] = dict(raw=row(r_raw), entry=row(r_e), pivot=p_.pivot, geometry_rebuilt_at_entry=bool(rebuilt), geometry_id=getattr(p_.pressure, "geometry_id", None), geometry_base=getattr(p_.pressure, "geometry_base", None),
                           params_entry=dict(c_l=float(ze[-2]), omega=float(ze[-1])), seconds=time.time() - t2)
            log(f"objective {nm}: raw O1 {obj[nm]['raw']['O1']:.9e}, entry O1 {obj[nm]['entry']['O1']:.9e} (gauge part {obj[nm]['entry']['gauge_part']:.3e}); geometry {obj[nm]['geometry_id']} (rebuilt {rebuilt}); {obj[nm]['seconds']:.0f} s")
            del m_, p_
        meas_diff = obj["resp"]["entry"]["O1"] - obj["kept"]["entry"]["O1"]
        obj["comparison"] = dict(measured_entry_O1_kept=obj["kept"]["entry"]["O1"], measured_entry_O1_resp=obj["resp"]["entry"]["O1"], affine_M_kept=res["M_kept"], affine_M_resp=res["M_resp"], measured_difference=meas_diff, affine_predicted_difference=res["diff_formula"],
                                 nonlinear_remainder_of_difference=meas_diff - res["diff_formula"], measured_minus_affine_kept=obj["kept"]["entry"]["O1"] - res["M_kept"], measured_minus_affine_resp=obj["resp"]["entry"]["O1"] - res["M_resp"],
                                 note="reported, not gated (lead 02:05:41Z item 2 (b)): the measured values include the nonlinear remainder and the fresh quadrature geometry at the displaced point, the affine model is in the lineage's EVAL geometry")
        sel = "resp" if obj["resp"]["entry"]["O1"] < obj["kept"]["entry"]["O1"] else "kept"
        obj["selection"] = dict(rule="lower measured iteration-0 O1 (entry path) at the same actual parameters, map, gauge and objective settings (lead 22:04:42Z item 2)", selected=sel, selected_file=files[sel]["path"], ratio_resp_over_kept=(obj["resp"]["entry"]["O1"] / obj["kept"]["entry"]["O1"] if obj["kept"]["entry"]["O1"] > 0 else None))
        log(f"selection: {sel} (resp/kept entry O1 ratio {obj['selection']['ratio_resp_over_kept']}); measured difference {meas_diff:.3e} vs affine {res['diff_formula']:.3e} (remainder {meas_diff - res['diff_formula']:.3e})")
    tests_ok = bool(fx_ok and test_i["passed"] and test_ii["passed"] and test_iv["passed"])
    if not tests_ok:
        for nm in files:
            open(files[nm]["path"] + ".UNUSABLE", "w").write("a correctness test failed; see the json\n")
    rec = dict(tool=TOOL, tool_sha256=meta_common["tool_sha256"], inputs=dict(run=run, job_id=job_id, checkpoint_sha256=meta_common["checkpoint_sha256"], eval_npz=ev_path, eval_sha256=meta_common["eval_sha256"], config_sha256=hashlib.sha256(json.dumps(cfg, sort_keys=True).encode()).hexdigest()),
               base=dict(it=int(cur["it"]), cost=float(Z["cost"]), r_norm2=r_norm2, q_norm2=float(np.asarray(q) @ np.asarray(q)), params=P0, checks=base_checks), displacement=disp, dz_p_optimizer=dict(dz_c=dzc, dz_w=dzw), params_after=dict(c_l=cl1, omega=om1),
               factor=dict(n=res["n"], n_coef_columns=res["n_coef_columns"], null_columns_dropped=res["null"].tolist(), rank_kept=res["rank_kept"], n_dropped_by_cutoff=res["n_dropped_by_cutoff"], cutoff=a.cutoff, sigma_max=res["sigma_max"], sigma_min_kept=res["sigma_min_kept"], sigma_min_all=res["sigma_min_all"],
                           norm_v=res["norm_v"], norm_Pv=res["norm_Pv"], absorption_c=res["absorption_c"], svd_seconds=t_svd, D_params=[float(D[i]) for i in res["pp"]]),
               affine=dict(M_base=res["M_base"], M_kept=res["M_kept"], M_resp=res["M_resp"], diff_formula=res["diff_formula"], diff_direct=res["diff_direct"], relaxed_diagnostic=res["relaxed_diagnostic"]),
               dz_stats=dz_stats, relU_resp_vs_kept_training_grid=relU_resp_vs_kept, params_written=params_written, files=files, objective=obj,
               tests=dict(i_zero_displacement=test_i, ii_affine_prediction_two_ways=test_ii, iii_fixtures=fx, iii_fixtures_ok=fx_ok, iv_displacement_coordinates=test_iv, tests_ok=tests_ok), seconds=time.time() - t0, ts=now(), device=dev)
    json.dump(rec, open(a.out + ".json", "w"), indent=1, default=str)
    fl = ", ".join(k + " " + v["sha256"][:16] for k, v in files.items())
    log(f"DONE {a.out}.json; tests_ok {tests_ok}; files {fl}; {time.time() - t0:.0f} s")
    return 0 if tests_ok else 2


if __name__ == "__main__":
    sys.exit(main())
