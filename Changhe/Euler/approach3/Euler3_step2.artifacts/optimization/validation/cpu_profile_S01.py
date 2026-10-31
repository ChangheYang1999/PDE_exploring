"""D6FP CPU timing of S01 after the GPU revocation (lead 01:02:03Z item 2 (a)); label VALIDATION. Wall times (time.perf_counter, CPU ops are
synchronous), median of 3, at torch threads 1 and 4 (taskset cores 31-34), for: one fp64 residual (residual_vector_wd); one objective_at in the
modes fp64, dd (double-double values; identical for dd_fp64tangent and dd_fp64jac, which change only the derivative path); the two parameter
columns in every mode; J_cw on one chunk of 64 coefficient columns in every mode (linear extrapolation to 1469 columns, stated); J^T J and the
Cholesky solve on a full float64 J_cw (433009 x 1469, built once at 4 threads, peak RSS recorded); one trial evaluation (objective_at + commit);
the complete gradient (fp64 and dd). Then the projected time per accepted LM iteration per mode at 1 and 4 threads
(J_cw + parameter columns + normal equations + solve + two trial evaluations + complete gradient). Output validation/cpu_profile_S01.json."""
import sys, os, json, time, resource, statistics
MYROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, MYROOT); sys.path.insert(0, os.path.join(MYROOT, "scripts"))
os.environ["CUDA_VISIBLE_DEVICES"] = ""
import torch
torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
from src.optimization.problem import apply_precision_mode
from src.optimization.lm import param_columns
import worker_d6 as W
dev = "cpu"
def med(fn, n=3):
    ts = []
    for _ in range(n):
        t0 = time.perf_counter(); fn(); ts.append(time.perf_counter() - t0)
    return dict(median=statistics.median(ts), min=min(ts), max=max(ts), n=n)
def rss_gb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6
out = dict(started=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), host=os.uname().nodename, cores=sorted(os.sched_getaffinity(0)), start="S01_nest6_cl0.45_om1.0_p0.pt", threads={})
case = Case("S01", dev, start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")); prob, model, pm = case.prob, case.model, case.pm
zo = case.z_opt; zf = case.z_full; n = zo.numel(); pidx = [n - 2, n - 1]; to_full = case.to_full_opt
out["n_opt"] = int(n); out["n_rows"] = int(case.r.numel()); out["rss_after_build_GB"] = rss_gb()
MODES = ["fp64", "dd", "dd_fp64tangent", "dd_fp64jac"]
rng = torch.Generator().manual_seed(0)
cols64 = torch.randperm(n - 2, generator=rng)[:64].tolist()
E64 = torch.zeros(64, n); 
for i, k in enumerate(cols64):
    E64[i, k] = 1.0
fun_w = lambda q: prob.residual_vector_wd(to_full(q))
pfun = lambda q: prob.residual_vector_wd(to_full(q), differentiable_pressure=True)
THREADS = [int(v) for v in os.environ.get("CPU_PROFILE_THREADS", "1,4").split(",")]        # supplementary runs: CPU_PROFILE_THREADS=2 CPU_PROFILE_N=3
NSAMP = int(os.environ.get("CPU_PROFILE_N", "0"))                                           # 0 = the first run's sample plan (3 for cheap items, 1 or 2 for the expensive dd items; n recorded per entry)
OUTNAME = os.environ.get("CPU_PROFILE_OUT", "cpu_profile_S01.json")
def nn(default):
    return NSAMP if NSAMP > 0 else default
for nth in THREADS:
    torch.set_num_threads(nth); rec = {}
    apply_precision_mode(prob, "fp64")
    with torch.no_grad():
        rec["residual_vector_wd_fp64"] = med(lambda: fun_w(zo))
    for mode in ("fp64", "dd"):
        apply_precision_mode(prob, mode)
        rec[f"objective_at_{mode}"] = med(lambda: prob.objective_at(zf))
        rec[f"trial_evaluation_{mode}"] = med(lambda: prob.commit_aux(prob.objective_at(zf)[1]))
        rec[f"complete_gradient_{mode}"] = med(lambda: W.complete_gradient_opt(prob, pm, to_full, zo), n=nn(1 if mode == "dd" else 3))
    for mode in MODES:
        apply_precision_mode(prob, mode)
        rec[f"param_columns_{mode}"] = med(lambda: param_columns(pfun, zo, pidx), n=nn(3 if mode == "fp64" else 1))
        def jchunk():
            return torch.func.vmap(lambda ee: torch.func.jvp(fun_w, (zo,), (ee,))[1])(E64)
        r_ = med(jchunk, n=nn(1 if mode != "fp64" else 2))
        r_["extrapolated_1469_columns"] = r_["median"] * (n - 2) / 64.0 * (1.0)   # linear in the number of columns (23 chunks of 64)
        rec[f"Jcw_chunk64_{mode}"] = r_
    apply_precision_mode(prob, "fp64")
    out["threads"][str(nth)] = rec
    print(f"threads {nth}: " + json.dumps({k: round(v["median"], 3) for k, v in rec.items()}), flush=True)
    json.dump(out, open(os.path.join(MYROOT, "validation", OUTNAME), "w"), indent=1)
# full J_cw at 4 threads (fp64): peak RSS, J^T J, Cholesky solve
if os.environ.get("CPU_PROFILE_SKIP_FULLJ"):
    out["note"] = "supplementary run: thread count(s) %s, %d samples per entry; full-J stage skipped" % (THREADS, NSAMP)
    json.dump(out, open(os.path.join(MYROOT, "validation", OUTNAME), "w"), indent=1); print("DONE (supplementary)"); raise SystemExit(0)
torch.set_num_threads(4); apply_precision_mode(prob, "fp64")
t0 = time.perf_counter(); J = torch.func.vmap(lambda ee: torch.func.jvp(fun_w, (zo,), (ee,))[1], chunk_size=64)(torch.eye(n)).T; t_full = time.perf_counter() - t0
out["full_Jcw_fp64_4threads"] = dict(seconds=t_full, shape=list(J.shape), rss_peak_GB=rss_gb())
with torch.no_grad():
    r = prob.residual_vector_wd(zf)
    out["normal_equations_4threads"] = med(lambda: (J.T @ J, J.T @ r), n=3)
    A = J.T @ J; g = J.T @ r; A = A + 1e-2 * torch.diag(torch.diag(A)) + 1e-30 * torch.eye(n)
    out["cholesky_solve_4threads"] = med(lambda: torch.cholesky_solve(g[:, None], torch.linalg.cholesky(A)), n=3)
torch.set_num_threads(1)
with torch.no_grad():
    out["normal_equations_1thread"] = med(lambda: (J.T @ J, J.T @ r), n=3)
    out["cholesky_solve_1thread"] = med(lambda: torch.cholesky_solve(g[:, None], torch.linalg.cholesky(A)), n=3)
# projections per accepted LM iteration: J_cw + parameter columns + normal + solve + 2 trial evaluations + complete gradient
proj = {}
for nth in ("1", "4"):
    rec = out["threads"][nth]; p = {}
    for mode in MODES:
        obj_mode = "fp64" if mode == "fp64" else "dd"
        t = rec[f"Jcw_chunk64_{mode}"]["extrapolated_1469_columns"] + rec[f"param_columns_{mode}"]["median"] + out[f"normal_equations_{'4threads' if nth == '4' else '1thread'}"]["median"] + out[f"cholesky_solve_{'4threads' if nth == '4' else '1thread'}"]["median"] + 2 * rec[f"trial_evaluation_{obj_mode}"]["median"] + rec[f"complete_gradient_{obj_mode}"]["median"]
        p[mode] = dict(seconds_per_accepted_iteration=t, accepted_iterations_per_hour=3600.0 / t)
    proj[nth] = p
out["projected_per_accepted_iteration"] = proj
out["rss_peak_GB_end"] = rss_gb()
json.dump(out, open(os.path.join(MYROOT, "validation", OUTNAME), "w"), indent=1)
print("projection:", json.dumps(proj), flush=True); print("DONE")
