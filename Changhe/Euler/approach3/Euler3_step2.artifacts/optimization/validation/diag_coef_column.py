"""D6FP diagnostic (2026-10-29): block-wise comparison of the G1 coefficient-column constructions of validation/gates.py for given columns of a case:
J_f (jvp of residual_vector), J_cw (jvp of residual_vector_wd) and the harness J_c (jvp of the tables+weights-differentiable residual with the closure block
by five-point differences of the fresh closure rows), each against the centered differences of its own reference function (residual_vector, residual_vector_wd,
objective_at) at the gates' scaled steps. For every block (pde rows by radial group and the far-anchor block, closure rows, gauge row) and every step: norm of
the column, norm of the FD, norm of the difference, relative error with the floor and with F = 0. Usage:
  CUDA_VISIBLE_DEVICES=5 python validation/diag_coef_column.py S09_own 793,873,186 > validation/logs/diag_coef_S09.log ; JSON validation/diag_coef_<case>.json"""
import sys, os, json, time, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT, H_LADDER, PAIRS
from src.optimization.lm import param_columns
from src.equations import residuals as res
dev = "cuda:0" if torch.cuda.is_available() else "cpu"
cname = sys.argv[1]; cols = [int(x) for x in sys.argv[2].split(",")]
defs = {"S01_own": dict(start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")), "S09_own": dict(start=os.path.join(ROOT, "starts", "S09_d6w_cl0.45_om0.3_R1.pt")),
        "S05_own": dict(start=os.path.join(ROOT, "starts", "S05_nest6_cl0.45_om0.3_p0.pt")), "manu_large_omega": dict(pair=PAIRS["large_omega"], seed=6)}
case = Case(cname, dev, **defs[cname]); prob = case.prob; zo = case.z_opt; n = zo.numel()
fun = lambda q: prob.residual_vector(case.to_full_opt(q)); fun_w = lambda q: prob.residual_vector_wd(case.to_full_opt(q))
sc_fun_o = lambda q: prob.objective_at(case.to_full_opt(q), need_aux=False)[0]
def fun_wd(q):
    zz = case.to_full_opt(q); tabs = prob.pressure_tables_at(zz, differentiable=True); ev = prob.evaluate(zz, tables=tabs)
    return prob.residual_vector(zz, tables=tabs, nl_w=prob.nl_weights_from_ev(ev, differentiable=True), closure=prob.closure, ev=ev)
def jc_col(k):
    e = torch.zeros_like(zo); e[k] = 1.0
    col = torch.func.jvp(fun_wd, (zo,), (e,))[1].clone()
    if "closure" in case.block_slices:
        a0, a1 = case.block_slices["closure"]; h = 1e-4
        crow = lambda q: prob.closure_rows(case.to_full_opt(q), closure=prob.closure_state_at(case.to_full_opt(q)))
        col[a0:a1] = (8 * (crow(zo + h * e) - crow(zo - h * e)) - (crow(zo + 2 * h * e) - crow(zo - 2 * h * e))) / (12 * h)
    return col
blocks = {}
for gi, gname in enumerate(case.group_names):
    blocks[f"pde:{gname}"] = (case.row_group == gi)
if hasattr(case, "anchor_mask"):
    blocks["far_anchor_block"] = case.anchor_mask
for b, (a0, a1) in case.block_slices.items():
    if b != "pde":
        m = torch.zeros(case.r.numel(), dtype=torch.bool, device=case.r.device); m[a0:a1] = True; blocks[b] = m
out = dict(case=cname, device=dev, precision=getattr(prob, "precision_mode", None), cost=case.cost, r_norm=float(case.r.norm()), columns={})
rn = float(case.r.norm())
for k in cols:
    e = torch.zeros_like(zo); e[k] = 1.0
    with torch.no_grad():
        pass
    d_f = torch.func.jvp(fun, (zo,), (e,))[1]; d_w = torch.func.jvp(fun_w, (zo,), (e,))[1]; d_c = jc_col(k)
    scale = max(1.0, 1e-7 / max(float(d_f.norm()), 1e-300) / 1e-3)
    rec = dict(column=k, norm_Jf=float(d_f.norm()), norm_Jcw=float(d_w.norm()), norm_Jc=float(d_c.norm()), step_scale=scale, diff_Jc_minus_Jcw_norm=float((d_c - d_w).norm()), diff_Jcw_minus_Jf_norm=float((d_w - d_f).norm()),
               blocks={b: dict(norm_Jf=float(d_f[m].norm()), norm_Jcw=float(d_w[m].norm()), norm_Jc=float(d_c[m].norm()), diff_Jc_minus_Jcw=float((d_c[m] - d_w[m]).norm())) for b, m in blocks.items()}, fd={})
    for h0 in [1e-3, 1e-4, 1e-5]:
        h = h0 * scale
        with torch.no_grad():
            D_f = (fun(zo + h * e) - fun(zo - h * e)) / (2 * h); D_w = (fun_w(zo + h * e) - fun_w(zo - h * e)) / (2 * h)
        D_c = (sc_fun_o(zo + h * e) - sc_fun_o(zo - h * e)) / (2 * h)
        row = {}
        for name, d, D in (("Jf_vs_FD_residual", d_f, D_f), ("Jcw_vs_FD_residual_wd", d_w, D_w), ("Jc_vs_FD_objective_at", d_c, D_c)):
            per = {}
            for b, m in blocks.items():
                nd, nD, ndiff = float(d[m].norm()), float(D[m].norm()), float((d[m] - D[m]).norm()); F = 1e-3 * rn * nd
                per[b] = dict(norm_d=nd, norm_fd=nD, norm_diff=ndiff, e_floor=ndiff / max(nd, nD, F, 1e-300), e_F0=ndiff / max(nd, nD, 1e-300), floor=F)
            nd, nD, ndiff = float(d.norm()), float(D.norm()), float((d - D).norm())
            per["all"] = dict(norm_d=nd, norm_fd=nD, norm_diff=ndiff, e_floor=ndiff / max(nd, nD, 1e-3 * rn * nd, 1e-300), e_F0=ndiff / max(nd, nD, 1e-300))
            row[name] = per
        rec["fd"][f"{h0:.0e}"] = row
        print(f"col {k} h {h0:.0e} (step {h:.3e}): " + "; ".join(f"{name} all e {row[name]['all']['e_floor']:.2e} | " + " ".join(f"{b}:{row[name][b]['e_F0']:.1e}" for b in blocks) for name in row), flush=True)
    out["columns"][str(k)] = rec
json.dump(out, open(os.path.join(ROOT, "validation", f"diag_coef_{cname}.json"), "w"), indent=1)
print("DONE")
