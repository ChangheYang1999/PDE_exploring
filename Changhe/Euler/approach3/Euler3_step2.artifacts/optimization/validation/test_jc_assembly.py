"""D6FP: direct test of the worker's complete-Jacobian assembly (complete_jacobian_from_Jcw) on S01: traceback of any failure, timing, and the J_c
parameter columns of the closure block against five-point differences of the complete residual (fresh closure state through to_full) in optimizer
coordinates (lead 22:58Z item 3). Also the share of the closure rows in O1 at S01 and S05 (eval_Y path question)."""
import sys, os, time, json, traceback
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
from src.optimization.lm import jacobian_fwd, param_columns
import scripts.worker_d6 as W
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z; out = {}
for cname, fn in (("S01", "S01_nest6_cl0.45_om1.0_p0.pt"), ("S05", "S05_nest6_cl0.45_om0.3_p0.pt")):
    case = Case(cname, dev, start=os.path.join(ROOT, "starts", fn)); prob, model, tc, pm = case.prob, case.model, case.tc, case.pm
    r = case.r; a0, a1 = case.block_slices["closure"]
    share = 0.5 * float(r[a0:a1] @ r[a0:a1]) / case.cost
    out[cname] = dict(O1=case.cost, closure_block_share=share, closure_block_norm=float(r[a0:a1].norm()), gauge_row=float(r[-1]))
    print(cname, "closure block share of O1:", f"{share:.3e}", flush=True)
    if cname == "S01":
        zo = case.z_opt; n = zo.numel(); pidx = [n - 2, n - 1]
        fun = lambda q: prob.residual_vector_wd(case.to_full_opt(q)); pfun = lambda q: prob.residual_vector_wd(case.to_full_opt(q), differentiable_pressure=True)
        t0 = time.time(); J = jacobian_fwd(fun, zo, chunk=256); Jp = param_columns(pfun, zo, pidx)
        for j, k in enumerate(pidx):
            J[:, k] = Jp[:, j]
        (torch.cuda.synchronize() if torch.cuda.is_available() else None); t_jcw = time.time() - t0
        try:
            t0 = time.time(); J_c, info = W.complete_jacobian_from_Jcw(prob, case.to_full_opt, zo, J, pidx, pm=pm); (torch.cuda.synchronize() if torch.cuda.is_available() else None); t_jc = time.time() - t0
            print("complete_jacobian_from_Jcw OK", f"{t_jc:.1f}s", json.dumps({k: v for k, v in info.items() if k != 'construction'}, default=str), flush=True)
            # closure block of the J_c parameter columns vs five-point differences of the complete residual (fresh closure state) through to_full
            def rcl(q):
                zz = case.to_full_opt(q); return prob.closure_rows(zz, closure=prob.closure_state_at(zz))
            errs = {}
            for j, k in enumerate(pidx):
                e = torch.zeros_like(zo); e[k] = 1.0
                for h in (1e-3, 1e-4, 1e-5):
                    D4 = (8 * (rcl(zo + h * e) - rcl(zo - h * e)) - (rcl(zo + 2 * h * e) - rcl(zo - 2 * h * e))) / (12 * h)
                    errs[f"{'z_c' if j == 0 else 'z_w'}:{h:.0e}"] = float((J_c[a0:a1, k] - D4).norm() / max(float(D4.norm()), 1e-300))
                errs[f"{'z_c' if j == 0 else 'z_w'}:Jcw_only_error"] = float((J[a0:a1, k] - D4).norm() / max(float(D4.norm()), 1e-300))
            # 3 random coefficient directions of the closure block
            import numpy as np
            rng = np.random.default_rng(5)
            for i in range(3):
                v = torch.tensor(rng.normal(size=n), device=dev); v[-2:] = 0; v = v / v.norm()
                h = 1e-4
                D4 = (8 * (rcl(zo + h * v) - rcl(zo - h * v)) - (rcl(zo + 2 * h * v) - rcl(zo - 2 * h * v))) / (12 * h)
                errs[f"coef_dir_{i}"] = float((J_c[a0:a1, :] @ v - D4).norm() / max(float(D4.norm()), 1e-300)); errs[f"coef_dir_{i}_Jcw_only"] = float((J[a0:a1, :] @ v - D4).norm() / max(float(D4.norm()), 1e-300))
            out["S01"].update(t_Jcw=t_jcw, t_Jc_assembly=t_jc, closure_block_param_column_errors=errs, info=info)
            print("closure block J_c vs five-point differences:", json.dumps({k: f"{v:.2e}" for k, v in errs.items()}), flush=True)
        except Exception as e:
            traceback.print_exc(); out["S01"]["error"] = repr(e)
    del case; torch.cuda.empty_cache()
json.dump(out, open(os.path.join(ROOT, "validation", "test_jc_assembly.json"), "w"), indent=1, default=str); print("DONE")
