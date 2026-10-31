"""D6FP (lead 00:33Z item 1 (a), remedy (a1)): first_correction_graph on the exact route against (1) the production first_correction values,
(2) the former eval_Y graph version (values and the gradient of G_norm_t and of the closure rows' cost with respect to z), and (3) eval_Y call
counts over one objective_at, one J_cw column (jvp of residual_vector_wd), one J_c assembly step (closure_target_correction) and one complete
gradient: all must be zero. S01 and S05."""
import sys, os, json, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
import src.far_field.correction as C
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z; out = {}
for cname, fn in (("S01", "S01_nest6_cl0.45_om1.0_p0.pt"), ("S05", "S05_nest6_cl0.45_om0.3_p0.pt")):
    case = Case(cname, dev, start=os.path.join(ROOT, "starts", fn)); prob, model = case.prob, case.model
    z = case.z_full.detach().clone().requires_grad_(True)
    t0 = time.time(); gx = C.first_correction_graph(prob, z); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t_x = time.time() - t0
    t0 = time.time(); gy = C.first_correction_graph_evalY(prob, z); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t_y = time.time() - t0
    fc = C.first_correction(prob, z.detach())
    rec = dict(G_exact_vs_production=float((gx["G"] - fc["G"]).norm() / fc["G"].norm()), G_exact_vs_evalY=float((gx["G"] - gy["G"]).norm() / gy["G"].norm()), Gnorm_exact=float(gx["G_norm_t"]), Gnorm_production=fc["G_norm"], Gnorm_evalY=float(gy["G_norm_t"]), t_exact=t_x, t_evalY=t_y)
    gN_x, = torch.autograd.grad(gx["G_norm_t"], z, retain_graph=True); gN_y, = torch.autograd.grad(gy["G_norm_t"], z, retain_graph=True)
    rec["grad_Gnorm_rel_diff"] = float((gN_x - gN_y).norm() / gN_y.norm())
    # gradient of a random functional of G (all entries)
    torch.manual_seed(1); wv = torch.randn_like(gx["G"])
    gG_x, = torch.autograd.grad((gx["G"] * wv).sum(), z); gG_y, = torch.autograd.grad((gy["G"] * wv).sum(), z)
    rec["grad_G_functional_rel_diff"] = float((gG_x - gG_y).norm() / gG_y.norm())
    rec["grad_param_components"] = dict(exact=[float(gN_x[-2]), float(gN_x[-1])], evalY=[float(gN_y[-2]), float(gN_y[-1])])
    # eval_Y call counts on the production routes
    counts = {}
    C.EVAL_Y_CALLS[0] = 0; prob.objective_at(case.z_full); counts["objective_at"] = C.EVAL_Y_CALLS[0]
    C.EVAL_Y_CALLS[0] = 0
    zo = case.z_opt; e = torch.zeros_like(zo); e[-2] = 1.0
    torch.func.jvp(lambda q: prob.residual_vector_wd(case.to_full_opt(q), differentiable_pressure=True), (zo,), (e,)); counts["Jcw_param_column_jvp"] = C.EVAL_Y_CALLS[0]
    C.EVAL_Y_CALLS[0] = 0
    sys.path.insert(0, os.path.join(ROOT, "scripts")); import worker_d6 as W
    g = W.complete_gradient_opt(prob, case.pm, case.to_full_opt, zo); counts["complete_gradient_opt"] = C.EVAL_Y_CALLS[0]
    C.EVAL_Y_CALLS[0] = 0
    prob.closure_target_correction(case.z_full, to_full=case.to_full_opt, z_opt=zo); counts["closure_target_correction(J_c)"] = C.EVAL_Y_CALLS[0]
    rec["eval_Y_calls"] = counts
    out[cname] = rec
    print(cname, json.dumps(rec), flush=True)
    del case; torch.cuda.empty_cache()
json.dump(out, open(os.path.join(ROOT, "validation", "test_graph_exact.json"), "w"), indent=1)
print("DONE")
