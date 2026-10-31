#!/usr/bin/env python
"""v2 (2026-10-29T21:0xZ; V458, V460): the factor comparison is labelled LOCAL QUADRATIC MODEL agreement (residual norm, gradient J^T r and Gram J^T J), not equality of the vector Jacobian; the gradient is recomputed from each record's factors with the verifier's formula gradient[perm] = D * (R^T Qtr) (D stored already permuted) and compared; the full in-loop J_c (5.09 GB) was deleted at 20:51:37Z before V458 asked to keep it, so a direct matrix comparison is OPEN unless the smoke is re-run; when the full matrix is present the script also compares J^T J and the fresh column norms with it (v1 behaviour); the stale gauge-row index of the in-loop record is reported as a metadata capture defect (V460 item 2), not a row-order difference. v1 (344dd92e5aecd186) kept as s2_smoke_compare.py.v1_344dd92e.
Strategy-2 smoke comparison (lead 18:31:20Z item 4 (i); RUN_STATUS 'STRATEGY 2'): (1) the in-loop complete Jacobian J_c saved by worker_d6_s2.py at the
cont1_s3 end checkpoint (runs/s2smoke_Jc_cont1s3/s2_Jc_it00409.npz, full matrix) against the J_c EVAL v5 record of the same state
(validation/jc_eval/cont1_s3_.../linearization_00409_eval_complete.npz: R, D, perm of the scaled QR, no full matrix): row-order-free comparison through the
Gram matrix G = J^T J (the EVAL's G is reconstructed from its factors with the convention verified on the smoke's own in-loop linearization record), the
fresh column norms against the EVAL's D, and the gradient J^T r through Qtr; (2) the hook-disabled smoke (worker_d6_s2.py, step_jacobian J_cw) against the
production worker's iteration from the same checkpoint: z_opt bitwise and cost. CPU, one process, about 6 GB of RAM. Output validation/s2_smoke/compare.json."""
import os, sys, json, time, hashlib, math
import numpy as np, torch
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
t0 = time.time()
sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()
out = dict(kind="strategy-2 smoke comparison", ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
# ---- (1) in-loop J_c vs EVAL J_c
JF = os.path.join(ROOT, "runs/s2smoke_Jc_cont1s3/s2_Jc_it00409.npz"); LF = os.path.join(ROOT, "runs/s2smoke_Jc_cont1s3/linearization_00409.npz")
EF = os.path.join(ROOT, "validation/jc_eval/cont1_s3_S01_L6_cl0.4500_om1.0000_free/linearization_00409_eval_complete.npz")
L = np.load(LF, allow_pickle=True); E = np.load(EF, allow_pickle=True)
HAVE_J = os.path.isfile(JF)
if HAVE_J:
    Z = np.load(JF, allow_pickle=True); J = Z["J_c"]; info = str(Z["info"]); it_j = int(Z["it"]); z_j = Z["z_opt"]
    print(f"J_c {J.shape} loaded ({time.time() - t0:.0f} s); info: {info[:300]}")
    G = J.T @ J; print(f"Gram computed ({time.time() - t0:.0f} s)")
    cn = np.sqrt(np.einsum("ij,ij->j", J, J))
else:
    J = None; G = None; cn = None; it_j = int(L["it"]); z_j = L["z_opt"]; info = "full J_c file absent (deleted 2026-10-29T20:51:37Z after the v1 comparison; see s2_Jc_it00409.DELETED.txt)"
    print("full in-loop J_c absent: direct matrix comparison OPEN; factor comparison only")
def recon(R, D, perm, conv):
    """candidate conventions for the stored factor: R = qr(J[:, perm] / D[perm]) or qr(J[:, perm] * D[perm]) or qr(J / D)[:, perm] ... returns G reconstructed."""
    n = R.shape[0]; P = np.asarray(perm)
    if conv == "div_perm":      # columns permuted then divided by D[perm]
        M = R.T @ R; Dp = D[P]; Gp = M * Dp[:, None] * Dp[None, :]; Gr = np.zeros_like(Gp); Gr[np.ix_(P, P)] = Gp; return Gr
    if conv == "mul_perm":
        M = R.T @ R; Dp = D[P]; Gp = M / (Dp[:, None] * Dp[None, :]); Gr = np.zeros_like(Gp); Gr[np.ix_(P, P)] = Gp; return Gr
    if conv == "div_noperm":
        M = R.T @ R; return M * D[:, None] * D[None, :]
    if conv == "mul_noperm":
        M = R.T @ R; return M / (D[:, None] * D[None, :])
    if conv == "perm_only":
        M = R.T @ R; Gr = np.zeros_like(M); Gr[np.ix_(P, P)] = M; return Gr
    if conv == "none":
        return R.T @ R
rel = lambda A, B: float(np.abs(A - B).max() / max(np.abs(B).max(), 1e-300))
conv_tests = {}; best = "div_perm"                       # v1 established on the full matrix: G = P D R^T R D P^T with D stored permuted (V460 item 1 agrees)
if HAVE_J:
    for conv in ("div_perm", "mul_perm", "div_noperm", "mul_noperm", "perm_only", "none"):
        try:
            conv_tests[conv] = rel(recon(L["R"], L["D"], L["perm"], conv), G)
        except Exception as e:
            conv_tests[conv] = f"error {e!r}"
    best = min((k for k in conv_tests if isinstance(conv_tests[k], float)), key=lambda k: conv_tests[k])
    print("convention test on the smoke's own in-loop record (rel diff of reconstructed G to J^T J):", conv_tests, "-> best", best)
G_eval = recon(E["R"], E["D"], E["perm"], best); G_loop = recon(L["R"], L["D"], L["perm"], best)
g_rel = rel(G_eval, G) if HAVE_J else None; g_abs = float(np.abs(G_eval - G).max()) if HAVE_J else None
diag_rel = float(np.abs(np.diag(G_eval) - np.diag(G)).max() / np.abs(np.diag(G)).max()) if HAVE_J else None
cn_eval_rel = float(np.abs(cn - E["D"]).max() / np.abs(E["D"]).max()) if HAVE_J else None; cn_loop_rel = float(np.abs(cn - L["D"]).max() / np.abs(L["D"]).max()) if HAVE_J else None
# v2: local quadratic model from the factors alone: Gram (EVAL scaling) and gradient g[perm] = D * (R^T Qtr) (V460 item 1)
def grad_from(rec):
    R = rec["R"]; D = rec["D"]; P = np.asarray(rec["perm"]); Qtr = rec["Qtr"]; g = np.zeros(R.shape[0]); g[P] = D * (R.T @ Qtr); return g
g_loop = grad_from(L); g_eval = grad_from(E); rnorm = math.sqrt(float(E["r_norm2"]))
grad_cmp = dict(formula="gradient[perm] = D * (R^T Qtr), D stored permuted (V460)", max_abs_diff=float(np.abs(g_loop - g_eval).max()), max_abs_diff_over_r_norm=float(np.abs(g_loop - g_eval).max() / rnorm), rel_inf=float(np.abs(g_loop - g_eval).max() / np.abs(g_eval).max()),
                g_inf_eval=float(np.abs(g_eval).max()), g_inf_loop=float(np.abs(g_loop).max()), r_norm=rnorm, param_components=dict(loop=g_loop[-2:].tolist(), eval=g_eval[-2:].tolist()))
gram_factors = dict(gram_rel_max_loop_vs_eval=rel(G_loop, G_eval), gram_abs_max_loop_vs_eval=float(np.abs(G_loop - G_eval).max()), note="both Gram matrices reconstructed from the stored factors in the EVAL convention")
print("local quadratic model from the factors: Gram rel", gram_factors["gram_rel_max_loop_vs_eval"], "gradient max|diff|/||r||", grad_cmp["max_abs_diff_over_r_norm"], "rel inf", grad_cmp["rel_inf"])
# gradient J^T r: the records carry Qtr (Q^T r in the scaled, permuted system); generator_red is the gradient in optimizer coordinates? compare the records' generator_red (bitwise equal already) and r_norm2
grad_rec = dict(generator_red_equal=bool(np.array_equal(L["generator_red"], E["generator_red"])), r_norm2_equal=bool(np.array_equal(L["r_norm2"], E["r_norm2"])), cost_equal=bool(np.array_equal(L["cost"], E["cost"])),
                z_opt_equal=bool(np.array_equal(L["z_opt"], E["z_opt"])) and bool(np.array_equal(z_j, E["z_opt"])), perm_equal=bool(np.array_equal(L["perm"], E["perm"])),
                gauge_rows=dict(in_loop=L["gauge_rows"].tolist(), eval=E["gauge_rows"].tolist()), n_rows=dict(in_loop=int(L["n_rows"]), eval=int(E["n_rows"]), J_c_file=(int(J.shape[0]) if HAVE_J else None)))
# the parameter columns (last two) directly: compare column norms and the Gram entries of the two parameter columns
n_ = E["R"].shape[0]; pp = [n_ - 2, n_ - 1]
par = dict(colnorm_J=([float(cn[i]) for i in pp] if HAVE_J else None), D_eval=[float(E["D"][i]) for i in pp], D_in_loop=[float(L["D"][i]) for i in pp], G_param_block_J=(G[np.ix_(pp, pp)].tolist() if HAVE_J else None), G_param_block_eval=G_eval[np.ix_(pp, pp)].tolist(),
           G_param_block_loop_factors=G_loop[np.ix_(pp, pp)].tolist(), G_param_block_rel=(rel(G_eval[np.ix_(pp, pp)], G[np.ix_(pp, pp)]) if HAVE_J else None), G_param_rows_rel=(rel(G_eval[pp, :], G[pp, :]) if HAVE_J else None),
           G_param_block_rel_factors=rel(G_loop[np.ix_(pp, pp)], G_eval[np.ix_(pp, pp)]))
out["Jc_vs_eval"] = dict(version="v2", J_c_file=JF, J_c_present=HAVE_J, J_c_sha256=(sha(JF) if HAVE_J else "f16bbf7949e8517425624446a0f6ed8d18d34d61ffeac3c22fa532743fa45c2f (recorded by v1 before deletion)"), J_c_shape=(list(J.shape) if HAVE_J else None), it=it_j, in_loop_record=LF, in_loop_sha256=sha(LF), eval_record=EF, eval_sha256=sha(EF),
                         convention_tests=conv_tests, convention=best, full_matrix_comparison=(dict(gram_rel_max=g_rel, gram_abs_max=g_abs, gram_diag_rel_max=diag_rel, colnorm_vs_eval_D_rel_max=cn_eval_rel, colnorm_vs_in_loop_D_rel_max=cn_loop_rel) if HAVE_J else "OPEN: full in-loop J_c deleted before V458; v1 values (gram 9.9e-16, colnorm 1.7e-16) are in compare_v1.json"),
                         local_quadratic_model=dict(gram=gram_factors, gradient=grad_cmp, residual_norm2_equal=bool(np.array_equal(L["r_norm2"], E["r_norm2"])), cost_equal=bool(np.array_equal(L["cost"], E["cost"]))),
                         records=grad_rec, parameter_columns=par,
                         gauge_row_metadata="in-loop gauge_rows index is stale (captured before the first resumed objective installs the closure block; V460 item 2): metadata defect of the in-loop record, not a row-order difference",
                         reading="LOCAL QUADRATIC MODEL agreement (residual norm, gradient, Gram) between the in-loop J_c step record and the EVAL J_c record; equality of the vector Jacobian is not established by this (V458); the v1 full-matrix Gram and column-norm agreement supports but does not prove identity of the matrix")
if HAVE_J:
    del J, G
# ---- (2) hook-off vs production iteration
def load_ck(run):
    p = os.path.join(ROOT, "runs", run, "checkpoint_segment_end.pt")
    if not os.path.isfile(p):
        return None, p
    C = torch.load(p, map_location="cpu", weights_only=False); return C, p
res = {}
Ch, ph = load_ck("s2smoke_hookoff_cont1s3"); Cp, pp_ = load_ck("s2smoke_prod_cont1s3"); Cj, pj = load_ck("s2smoke_Jc_cont1s3")
if Ch is not None and Cp is not None:
    zh = Ch["current"]["z_opt"].numpy(); zp = Cp["current"]["z_opt"].numpy(); hh = [h for h in Ch["current"]["history"] if h.get("accepted")]; hp = [h for h in Cp["current"]["history"] if h.get("accepted")]
    res = dict(hookoff_ck=ph, hookoff_sha256=sha(ph), prod_ck=pp_, prod_sha256=sha(pp_), it=dict(hookoff=Ch["current"]["it"], prod=Cp["current"]["it"]),
               z_opt_bitwise_equal=bool(np.array_equal(zh, zp)), z_opt_max_abs_diff=float(np.abs(zh - zp).max()), z_opt_sha256=dict(hookoff=Ch["current"].get("z_opt_sha256"), prod=Cp["current"].get("z_opt_sha256")),
               cost=dict(hookoff=hh[-1]["cost"] if hh else None, prod=hp[-1]["cost"] if hp else None), cost_equal=(hh[-1]["cost"] == hp[-1]["cost"]) if (hh and hp) else None,
               lam=dict(hookoff=Ch["current"]["lam"], prod=Cp["current"]["lam"]), n_trials=dict(hookoff=hh[-1].get("n_trials") if hh else None, prod=hp[-1].get("n_trials") if hp else None),
               params=dict(hookoff=hh[-1].get("params") if hh else None, prod=hp[-1].get("params") if hp else None))
    if Cj is not None:
        hj = [h for h in Cj["current"]["history"] if h.get("accepted")]
        res["Jc_step"] = dict(ck=pj, sha256=sha(pj), it=Cj["current"]["it"], cost=hj[-1]["cost"] if hj else None, params=hj[-1].get("params") if hj else None, n_trials=hj[-1].get("n_trials") if hj else None, lam=Cj["current"]["lam"],
                             t_iter=hj[-1].get("t_iter") if hj else None, t_jac=hj[-1].get("t_jac") if hj else None, cost_hookoff_minus_Jc=(hh[-1]["cost"] - hj[-1]["cost"]) if (hh and hj) else None)
else:
    res = dict(note="hookoff or prod checkpoint missing", hookoff=ph, prod=pp_)
out["hookoff_vs_prod"] = res
out["seconds"] = time.time() - t0; out["script_sha256"] = sha(os.path.abspath(__file__))
od = os.path.join(ROOT, "validation", "s2_smoke"); os.makedirs(od, exist_ok=True); op = os.path.join(od, "compare_v2.json")
if os.path.isfile(os.path.join(od, "compare.json")) and not os.path.isfile(os.path.join(od, "compare_v1.json")):
    os.rename(os.path.join(od, "compare.json"), os.path.join(od, "compare_v1.json"))
json.dump(out, open(op, "w"), indent=1, default=str); print(json.dumps({k: out[k] for k in out if k != "Jc_vs_eval"}, indent=1, default=str)[:3000]); print("Jc_vs_eval:", json.dumps({k: v for k, v in out["Jc_vs_eval"].items() if k not in ("parameter_columns",)}, indent=1, default=str)[:3000]); print("parameter columns:", json.dumps(par, indent=1)); print("DONE", op, sha(op)[:16], f"{out['seconds']:.0f} s")
