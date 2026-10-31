#!/usr/bin/env python
"""D6FP profiling report (SPEC 9) on one GPU for an existing degree-6 state: synchronized device timings (median and spread of >= 5 repetitions) of
velocity/derivative assembly, pressure source, kernel-table construction, Green integrals (solve), residual and objective evaluation, Jacobian
(coefficient block, parameter columns), normal equations and Cholesky, trial-step evaluation (self-consistent rebuild), complete gradient,
host-device transfers; peak GPU memory, peak RAM; fixed versus free parameters; GPU utilization sampled with nvidia-smi during 3 LM iterations.
Usage: CUDA_VISIBLE_DEVICES=5 python validation/profile_d6.py --start starts/S01_nest6_cl0.45_om1.0_p0.pt --out profiling/profile_S01.json"""
import sys, os, time, json, math, argparse, subprocess, threading, resource, platform
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numpy as np, torch
torch.set_default_dtype(torch.float64)
torch.backends.cuda.matmul.allow_tf32 = False; torch.backends.cudnn.allow_tf32 = False
from src.equations.fields import Model, alpha_of
from src.equations import residuals as res
from src.optimization.problem import Problem
from src.optimization.tail_constraints import TailConstraints
from src.optimization.param_map import ParamMap
from src.optimization.lm import jacobian_fwd, param_columns, lm_solve_free
from src.pressure.poisson_sh import PressureSolver
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DT = torch.float64


def sync():
    (torch.cuda.synchronize() if torch.cuda.is_available() else None)


def timeit(f, reps=5, warm=1):
    for _ in range(warm):
        f()
    sync(); ts = []
    for _ in range(reps):
        t0 = time.perf_counter(); f(); sync(); ts.append(time.perf_counter() - t0)
    return dict(median=float(np.median(ts)), min=float(min(ts)), max=float(max(ts)), reps=reps)


class GpuSampler(threading.Thread):
    def __init__(self, gpu_index, interval=1.0):
        super().__init__(daemon=True); self.gpu = gpu_index; self.interval = interval; self.samples = []; self.stop = threading.Event()

    def run(self):
        while not self.stop.is_set():
            try:
                out = subprocess.run(["nvidia-smi", "-i", str(self.gpu), "--query-gpu=utilization.gpu,memory.used", "--format=csv,noheader,nounits"], capture_output=True, text=True, timeout=5).stdout
                u, m = [float(x) for x in out.strip().split(",")]
                self.samples.append((time.time(), u, m))
            except Exception:
                pass
            self.stop.wait(self.interval)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", default=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")); ap.add_argument("--out", default=os.path.join(ROOT, "profiling", "profile_S01.json"))
    ap.add_argument("--chunk", type=int, default=256); ap.add_argument("--lm_iters", type=int, default=3); ap.add_argument("--gpu_index", type=int, default=None)
    a = ap.parse_args()
    dev = ("cuda:0" if torch.cuda.is_available() else "cpu")      # CPU after the GPU revocation of 2026-10-29T00:57:59Z
    S = torch.load(a.start, map_location="cpu", weights_only=False); cfg = S["config"]
    phys_gpu = a.gpu_index if a.gpu_index is not None else int((os.environ.get("CUDA_VISIBLE_DEVICES") or "0").split(",")[0])
    rep = dict(ts=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), start=a.start, gpu=(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "cpu"), physical_gpu=phys_gpu, host=platform.node(),
               cuda_visible=os.environ.get("CUDA_VISIBLE_DEVICES"), omp=os.environ.get("OMP_NUM_THREADS"), affinity=sorted(os.sched_getaffinity(0)), chunk=a.chunk,
               other_processes_on_gpu=subprocess.run(["nvidia-smi", "-i", str(phys_gpu), "--query-compute-apps=pid,used_memory", "--format=csv,noheader"], capture_output=True, text=True).stdout.strip().splitlines())
    out = {}
    for mode in ("free", "fixed"):
        free = mode == "free"
        (torch.cuda.reset_peak_memory_stats() if torch.cuda.is_available() else None); torch.cuda.empty_cache()
        t0 = time.perf_counter()
        model = Model(L=cfg["L"], Nk=cfg["Nk"], m_parity=cfg.get("m_parity", "even"), R0=cfg.get("R0", 1.0), Nr=cfg.get("Nr"), c_l=cfg["c_l"], omega=cfg["omega"],
                      free_params=free, device=dev, channels=cfg.get("channels"), extra_r=cfg.get("far_radii"))
        sync(); t_model = time.perf_counter() - t0
        t0 = time.perf_counter()
        prob = Problem(model, formulation="mom", nl_weighting=True, nl_denominator=cfg.get("nl_denominator", "all5far"), far_lambda=1e-2, closure_lambda=float(cfg.get("closure_lambda", 1e-3)), far_radii=cfg.get("far_radii"))
        sync(); t_prob = time.perf_counter() - t0
        tc = TailConstraints(model); pm = ParamMap(free=free)
        zf = torch.cat([S["z"].to(dev), torch.tensor([cfg["c_l"], cfg["omega"]], device=dev)]) if free else S["z"].to(dev)
        prob.pivot = prob.choose_pivot(zf); zf = prob.phase_align(zf)
        to_full = (lambda zo: tc.expand(pm.expand(zo))); to_opt = (lambda z: pm.reduce(tc.reduce(z)))
        zo = to_opt(zf); zf = to_full(zo); n = zo.numel()
        r, aux = prob.objective_at(zf); prob.commit_aux(aux)
        m = dict(t_model_build=t_model, t_problem_build=t_prob, n_opt=int(n), n_rows=int(r.numel()), n_quad=prob.pressure.n_quad)
        # components
        F = model.fields_grid(zf, need_vort=False); src = res.pressure_source(F["GU"])
        m["fields_grid(U,DU)"] = timeit(lambda: model.fields_grid(zf, need_vort=False))
        m["pressure_source"] = timeit(lambda: res.pressure_source(F["GU"]))
        c_t = torch.tensor(float(zf[-2]) if free else cfg["c_l"], device=dev); w_t = torch.tensor(float(zf[-1]) if free else cfg["omega"], device=dev)
        m["pressure_tables_build(GPU)"] = timeit(lambda: prob.pressure.build_tables(c_t, w_t))
        m["pressure_solve(Green integrals, synthesis)"] = timeit(lambda: prob.pressure.solve(src))
        m["pressure_geometry_rebuild(CPU numpy + tables)"] = timeit(lambda: PressureSolver(model, p0=2 * alpha_of(float(c_t)) + 2, omega=float(w_t), c_l=float(c_t)), reps=3)
        m["residual_vector(frozen weights, base tables)"] = timeit(lambda: prob.residual_vector(zf))
        if free:
            m["residual_vector(differentiable tables)"] = timeit(lambda: prob.residual_vector(zf, differentiable_pressure=True))
        m["objective_at(self-consistent: tables+weights+closure target)"] = timeit(lambda: prob.objective_at(zf), reps=5)
        m["closure_state_at(first_correction + patterns)"] = timeit(lambda: prob.closure_state_at(zf), reps=5)
        m["nl_weights_from_ev"] = timeit(lambda: prob.nl_weights_from_ev(prob.evaluate(zf)), reps=5)
        m["phase_align"] = timeit(lambda: prob.phase_align(zf))
        fun = lambda q: prob.residual_vector(to_full(q))
        (torch.cuda.reset_peak_memory_stats() if torch.cuda.is_available() else None)
        tj = timeit(lambda: jacobian_fwd(fun, zo, chunk=a.chunk), reps=3, warm=1); m["jacobian_coefficient_block"] = tj; m["jacobian_peak_GB"] = (torch.cuda.max_memory_allocated() if torch.cuda.is_available() else 0) / 2 ** 30
        if free:
            pfun = lambda q: prob.residual_vector(to_full(q), differentiable_pressure=True)
            m["jacobian_parameter_columns(2 jvp)"] = timeit(lambda: param_columns(pfun, zo, [n - 2, n - 1]), reps=5)
        J = jacobian_fwd(fun, zo, chunk=a.chunk)
        m["normal_equations(J^T J, J^T r)"] = timeit(lambda: (J.T @ J, J.T @ r), reps=5)
        A = J.T @ J; g = J.T @ r; D = torch.diagonal(A).clamp_min(1e-30); D = torch.maximum(D, 1e-12 * D.max())   # as lm_solve_free: zero columns (E channel l < 2) get the floor
        m["cholesky_solve"] = timeit(lambda: torch.cholesky_solve(g[:, None], torch.linalg.cholesky(A + 1e-2 * torch.diag(D))), reps=5)
        m["qr_linearization(geqrf+ormqr)"] = timeit(lambda: torch.ormqr(*torch.geqrf(J / D.sqrt()[None, :]), r[:, None], transpose=True), reps=2, warm=1)
        m["jacobian_weights_differentiated(J_cw)"] = timeit(lambda: jacobian_fwd(lambda q: prob.residual_vector_wd(to_full(q)), zo, chunk=a.chunk), reps=2, warm=1)
        m["closure_target_correction(J_c, FD over tail amplitudes)"] = timeit(lambda: prob.closure_target_correction(zf, to_full=to_full, z_opt=zo), reps=1, warm=0) if (free and prob.closure is not None) else None
        del J
        if free:
            m["complete_gradient(reverse pass + pattern FD)"] = timeit(lambda: prob.complete_gradient(zf), reps=3)
        # angular tables: double-double build cost at the production degrees and the cache (lead 22:49Z item 5)
        from src.bases.solid_harmonics import eval_solid_fp64, eval_solid, mode_list, AngularGrid, path_summary, _TABLE_CACHE
        gA = AngularGrid(model.ntheta, model.nphi, device=dev)
        for Lt, nd, lmin, tag in ((model.L_ext, 2, 1, "field tables (degree L_ext, Hessians)"), (prob.pressure.Lf, 1, 0, "pressure synthesis tables (degree Lf, gradients)")):
            modes_t = mode_list(Lt, model.m_parity, l_min=lmin)
            _TABLE_CACHE.clear()
            m[f"angular_tables_fp64 {tag}"] = timeit(lambda: eval_solid_fp64(gA.n, modes_t, Lt, nd), reps=3)
            _TABLE_CACHE.clear()
            m[f"angular_tables_dd_build {tag}"] = timeit(lambda: (_TABLE_CACHE.clear(), eval_solid(gA.n, modes_t, Lt, nd, path="dd")), reps=3, warm=1)
            m[f"angular_tables_dd_cached {tag}"] = timeit(lambda: eval_solid(gA.n, modes_t, Lt, nd, path="dd"), reps=3, warm=1)
        m["angular_table_paths_this_process"] = path_summary()
        # host-device transfer and sync
        x = torch.randn(1000000, device=dev); sync()
        m["device_to_host_8MB"] = timeit(lambda: x.cpu(), reps=5); m["host_to_device_8MB"] = timeit(lambda: torch.randn(1000000).to(dev), reps=5)
        m["synchronize_only"] = timeit(lambda: None, reps=10)
        m["item_sync(float(tensor))"] = timeit(lambda: float(x[0]), reps=10)
        # short LM with utilization sampling
        sampler = GpuSampler(phys_gpu, 0.5); sampler.start()
        (torch.cuda.reset_peak_memory_stats() if torch.cuda.is_available() else None)
        t0 = time.perf_counter()
        outlm = lm_solve_free(fun, zo, param_fun=(pfun if free else None), param_idx=([n - 2, n - 1] if free else []), objective=lambda q: prob.objective_at(to_full(q)), commit=prob.commit_aux,
                              project=lambda q: to_opt(prob.phase_align(to_full(q))), phys=(lambda q: pm.describe(q)) if free else None, max_iter=a.lm_iters, lam0=1e-2, chunk=a.chunk,
                              verbose=True, grad_fun=((lambda q: prob.complete_gradient(to_full(q))) if free else None), param_step_max=({n - 2: 0.5, n - 1: 0.5} if free else None))
        sync(); t_lm = time.perf_counter() - t0; sampler.stop.set(); sampler.join(timeout=3)
        hist = outlm["history"]
        m["lm_iterations"] = [{k: h[k] for k in ("it", "cost", "accepted", "n_trials", "t_jac", "t_param_cols", "t_normal", "t_solve", "t_trial", "t_iter")} | {"grad_s": (h.get("complete_gradient") or {}).get("seconds")} for h in hist]
        m["lm_seconds_total"] = t_lm; m["lm_accepted"] = outlm["n_accepted"]; m["accepted_steps_per_hour_estimate"] = 3600.0 * outlm["n_accepted"] / t_lm
        m["lm_peak_GB"] = (torch.cuda.max_memory_allocated() if torch.cuda.is_available() else 0) / 2 ** 30
        m["gpu_utilization_samples"] = dict(n=len(sampler.samples), util_mean=float(np.mean([s[1] for s in sampler.samples])) if sampler.samples else None,
                                           util_max=float(np.max([s[1] for s in sampler.samples])) if sampler.samples else None, mem_used_max_MiB=float(np.max([s[2] for s in sampler.samples])) if sampler.samples else None,
                                           note="whole-GPU utilization including other processes on the GPU")
        m["peak_RSS_GB"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20
        out[mode] = m
        print(json.dumps({k: (v if not isinstance(v, dict) or "median" not in v else round(v["median"], 4)) for k, v in m.items() if k != "lm_iterations"}, indent=0, default=str), flush=True)
        del prob, model, tc; torch.cuda.empty_cache()
    rep["modes"] = out
    fr, fx = out["free"], out["fixed"]
    rep["comparison"] = dict(extra_time_parameter_columns_s=fr["jacobian_parameter_columns(2 jvp)"]["median"], jacobian_free_s=fr["jacobian_coefficient_block"]["median"], jacobian_fixed_s=fx["jacobian_coefficient_block"]["median"],
                             trial_rebuild_free_s=fr["objective_at(self-consistent: tables+weights+closure target)"]["median"], trial_rebuild_fixed_s=fx["objective_at(self-consistent: tables+weights+closure target)"]["median"],
                             mean_iteration_free_s=float(np.mean([h["t_iter"] for h in fr["lm_iterations"]])), mean_iteration_fixed_s=float(np.mean([h["t_iter"] for h in fx["lm_iterations"]])),
                             complete_gradient_s=fr.get("complete_gradient(reverse pass + pattern FD)", {}).get("median"))
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    json.dump(rep, open(a.out, "w"), indent=1, default=str)
    print("WROTE", a.out, json.dumps(rep["comparison"], indent=0))


if __name__ == "__main__":
    main()
