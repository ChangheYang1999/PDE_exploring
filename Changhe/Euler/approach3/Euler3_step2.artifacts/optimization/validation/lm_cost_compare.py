"""D6FP D1 / R2 (b) (lead 00:06Z): wall time of five accepted free LM iterations of the worker path from S01, float64 against v2 (double-double
source and pressure chain), on the same GPU under the same sharing. The worker's functions are used (residual_vector_wd, its parameter function,
objective_at and commit_aux, phase projection, PDE-row Marquardt scaling, complete gradient as the worker calls it); linearization records off.
nvidia-smi compute apps are recorded at start and end. Output validation/lm_cost_compare.json."""
import sys, os, json, time, subprocess, math
MYROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, MYROOT); sys.path.insert(0, os.path.join(MYROOT, "scripts"))
import torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False; torch.backends.cudnn.allow_tf32 = False
import worker_d6 as W
from enqueue_d6 import PROD
from src.optimization.lm import lm_solve_free
from src.optimization.tail_constraints import TailConstraints
from src.optimization.param_map import ParamMap
dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
def smi():
    try:
        return subprocess.run(["nvidia-smi", "--query-compute-apps=pid,used_memory", "--format=csv,noheader"], capture_output=True, text=True, timeout=20).stdout.strip().splitlines()
    except Exception as e:
        return [repr(e)]
start = os.path.join(MYROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")
for _a in sys.argv[2:]:
    if _a.startswith("--start="):
        start = _a.split("=", 1)[1] if os.path.isabs(_a.split("=", 1)[1]) else os.path.join(MYROOT, _a.split("=", 1)[1])
S = torch.load(start, map_location="cpu", weights_only=False); scfg = S["config"]
c_l, omega = (float(S["z"][-2]), float(S["z"][-1])) if S.get("free_params") else (scfg["c_l"], scfg["omega"])
cfg = dict(PROD); cfg.update(c_l=c_l, omega=omega, free_params=True, L=scfg["L"], Nk=scfg["Nk"], Nr=scfg.get("Nr"), R0=scfg.get("R0", 1.0), m_parity=scfg.get("m_parity", "even"), channels=scfg.get("channels"))
class _Stop(Exception):
    pass
out = dict(start=os.path.basename(start), gpu=(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu"), smi_start=smi(), runs={}, n_accepted_target=5)
import src.pressure.poisson_sh as _ps
PRECS = sys.argv[1].split(",") if len(sys.argv) > 1 else ["fp64", "dd"]
from src.optimization.problem import apply_precision_mode
MODES = dict(fp64="fp64", dd="dd", ddt="dd_fp64tangent", ddj="dd_fp64jac")
for precision in PRECS:
    model, prob = W.build(cfg, dev)
    apply_precision_mode(prob, MODES[precision])
    zs = S["z"].to(dev)
    z = zs.clone() if S.get("free_params") else torch.cat([zs[: model.n_coef], torch.tensor([c_l, omega], device=dev)])
    prob.pivot = prob.choose_pivot(z); prob.ensure_geometry(z); z = prob.phase_align(z)
    tc = TailConstraints(model); pm = ParamMap()
    to_full = lambda zo: tc.expand(pm.expand(zo)); to_opt = lambda zf: pm.reduce(tc.reduce(zf))
    z_opt = to_opt(z)
    r0, aux0 = prob.objective_at(to_full(z_opt)); prob.commit_aux(aux0)
    n_opt = z_opt.numel(); pidx = [n_opt - 2, n_opt - 1]
    fun = lambda zo: prob.residual_vector_wd(to_full(zo)); pfun = lambda zo: prob.residual_vector_wd(to_full(zo), differentiable_pressure=True)
    def objective(zo):
        return prob.objective_at(to_full(zo))
    project = lambda zo: to_opt(prob.phase_align(to_full(zo))); phys = lambda zo: pm.describe(zo)
    relayout = lambda zo: (prob.ensure_geometry(to_full(zo)), dict(geometry=prob.pressure.geometry_id, base=prob.pressure.geometry_base))
    grad_fun = (lambda zo: W.complete_gradient_opt(prob, pm, to_full, zo)) if cfg.get("complete_gradient", True) else None
    recs = []; box = dict(acc=0)
    def cb(it, zo, cost, rec):
        recs.append({k: rec[k] for k in ("it", "cost", "accepted", "n_trials", "t_jac", "t_param_cols", "t_normal", "t_solve", "t_trial", "t_iter", "step_rel", "dparam_opt", "gain_ratio") if k in rec})
        recs[-1]["z_norm"] = float(zo.norm()); recs[-1]["z_sha256_12"] = __import__("hashlib").sha256(zo.detach().cpu().numpy().tobytes()).hexdigest()[:12]
        if rec.get("accepted"):
            box["acc"] += 1
        if box["acc"] >= out["n_accepted_target"]:
            raise _Stop()
        return False
    (torch.cuda.synchronize() if torch.cuda.is_available() else None); (torch.cuda.reset_peak_memory_stats() if torch.cuda.is_available() else None); t0 = time.time()
    try:
        lm_solve_free(fun, z_opt, param_fun=pfun, param_idx=pidx, objective=objective, commit=prob.commit_aux, project=project, phys=phys, relayout=relayout,
                      max_iter=60, lam0=float(cfg.get("lam0", 1e-2)), chunk=int(cfg.get("chunk", 256)), callback=cb, log=lambda *a, **k: None, time_limit=2400.0, verbose=False,
                      ftol=float(cfg.get("ftol", 1e-7)), xtol=float(cfg.get("xtol", 1e-12)), param_step_max={pidx[0]: float(cfg.get("param_step_max", 0.5)), pidx[1]: float(cfg.get("param_step_max", 0.5))},
                      grad_fun=grad_fun, jac_hook=None, saturation=(lambda zo: pm.saturation_flag(zo)), log_every=1, param_scale_rows=prob.n_pde_residuals())
        status = "finished_before_target"
    except _Stop:
        status = "target_reached"
    (torch.cuda.synchronize() if torch.cuda.is_available() else None); wall = time.time() - t0
    run = dict(status=status, wall_s=wall, n_iterations=len(recs), n_accepted=sum(1 for r in recs if r.get("accepted")), n_trials=sum(r.get("n_trials", 0) for r in recs),
               cost_start=0.5 * float(r0 @ r0), cost_end=(recs[-1]["cost"] if recs else None), peak_GPU_GB=(torch.cuda.max_memory_allocated() if torch.cuda.is_available() else 0) / 1e9, records=recs,
               mean_t_iter=(sum(r["t_iter"] for r in recs) / len(recs) if recs else None), mean_t_jac=(sum(r.get("t_jac", 0) for r in recs) / len(recs) if recs else None),
               mean_t_trial_per_trial=(sum(r.get("t_trial", 0) for r in recs) / max(1, sum(r.get("n_trials", 0) for r in recs))))
    out["runs"][precision] = run
    print(f"{precision}: {status}, wall {wall:.1f}s for {run['n_accepted']} accepted in {len(recs)} iterations ({run['n_trials']} trials); mean t_iter {run['mean_t_iter']:.1f}s, t_jac {run['mean_t_jac']:.1f}s, trial {run['mean_t_trial_per_trial']:.2f}s; cost {run['cost_start']:.4e} -> {run['cost_end']}; peak GPU {run['peak_GPU_GB']:.1f} GB", flush=True)
    del model, prob; torch.cuda.empty_cache()
out["smi_end"] = smi()
ref_fp64 = json.load(open(os.path.join(MYROOT, "validation", "lm_cost_compare.json")))["runs"]["fp64"] if ("fp64" not in out["runs"] and os.path.exists(os.path.join(MYROOT, "validation", "lm_cost_compare.json"))) else out["runs"].get("fp64")
for k in out["runs"]:
    if k != "fp64" and ref_fp64 is not None:
        out[f"ratio_wall_{k}_over_fp64"] = out["runs"][k]["wall_s"] / ref_fp64["wall_s"]
        print(f"ratio wall {k}/fp64 = {out[f'ratio_wall_{k}_over_fp64']:.3f} (fp64 reference wall {ref_fp64['wall_s']:.1f}s)", flush=True)
tagname = "lm_cost_compare" + ("" if PRECS == ["fp64", "dd"] else "_" + "_".join(PRECS)) + ("" if os.path.basename(start).startswith("S01_") else "_" + os.path.basename(start).split("_")[0])
json.dump(out, open(os.path.join(MYROOT, "validation", tagname + ".json"), "w"), indent=1)
print("DONE")
