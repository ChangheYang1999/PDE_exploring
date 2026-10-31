"""D6FP 2026-10-29: supplementary CPU timing of S01 (SPEC v1.10 section 9: at least three timings for items of at most 300 s). Repeats, at the
given thread count, the measured components whose first-run sample count was below three and whose median was at most 300 s, with n = 3 each,
and writes validation/cpu_profile_S01_supplement_threads<t>.json (same entry format: median, min, max, n; plus the first-run values for the record).
Items (one thread): complete_gradient_dd (n 1), param_columns_dd, param_columns_dd_fp64tangent, param_columns_dd_fp64jac (n 1), Jcw_chunk64_fp64
(n 2), Jcw_chunk64_dd_fp64tangent, Jcw_chunk64_dd_fp64jac (n 1). Jcw_chunk64_dd (1665 s) exceeds 300 s and keeps n = 1.
Usage: CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 python validation/cpu_profile_supplement.py [threads=1] [source json]"""
import sys, os, json, time, statistics
MYROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); sys.path.insert(0, MYROOT); sys.path.insert(0, os.path.join(MYROOT, "scripts"))
os.environ["CUDA_VISIBLE_DEVICES"] = ""
import torch; torch.set_default_dtype(torch.float64)
from validation.gates import Case, ROOT
from src.optimization.problem import apply_precision_mode
from src.optimization.lm import param_columns
import worker_d6 as W
nth = int(sys.argv[1]) if len(sys.argv) > 1 else 1; torch.set_num_threads(nth)
src = sys.argv[2] if len(sys.argv) > 2 else os.path.join(MYROOT, "validation", "cpu_profile_S01.json")
first = json.load(open(src)); rec0 = first["threads"][str(nth)]
todo = [k for k, v in rec0.items() if v.get("n", 3) < 3 and v["median"] <= 300.0]
print("threads", nth, "items to repeat with n = 3:", todo, flush=True)
def med(fn, n=3):
    ts = []
    for _ in range(n):
        t0 = time.perf_counter(); fn(); ts.append(time.perf_counter() - t0)
    return dict(median=statistics.median(ts), min=min(ts), max=max(ts), n=n, samples=ts)
case = Case("S01", "cpu", start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")); prob, pm = case.prob, case.pm
zo = case.z_opt; zf = case.z_full; n = zo.numel(); pidx = [n - 2, n - 1]; to_full = case.to_full_opt
rng = torch.Generator().manual_seed(0); cols64 = torch.randperm(n - 2, generator=rng)[:64].tolist()
E64 = torch.zeros(64, n)
for i, k in enumerate(cols64):
    E64[i, k] = 1.0
fun_w = lambda q: prob.residual_vector_wd(to_full(q))
pfun = lambda q: prob.residual_vector_wd(to_full(q), differentiable_pressure=True)
out = dict(started=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), threads=nth, source=os.path.basename(src), cores=sorted(os.sched_getaffinity(0)), items={})
for k in todo:
    mode = k.split("_", 2)[-1] if k.startswith("Jcw_chunk64_") or k.startswith("param_columns_") else ("dd" if k.endswith("_dd") else "fp64")
    if k.startswith("complete_gradient_"):
        mode = k[len("complete_gradient_"):]
    apply_precision_mode(prob, mode)
    if k.startswith("complete_gradient_"):
        r_ = med(lambda: W.complete_gradient_opt(prob, pm, to_full, zo))
    elif k.startswith("param_columns_"):
        r_ = med(lambda: param_columns(pfun, zo, pidx))
    elif k.startswith("Jcw_chunk64_"):
        r_ = med(lambda: torch.func.vmap(lambda ee: torch.func.jvp(fun_w, (zo,), (ee,))[1])(E64))
        r_["extrapolated_1469_columns"] = r_["median"] * (n - 2) / 64.0
    else:
        continue
    r_["first_run"] = rec0[k]; out["items"][k] = r_
    print(k, json.dumps({kk: (round(vv, 3) if isinstance(vv, float) else vv) for kk, vv in r_.items() if kk != "first_run"}), flush=True)
    json.dump(out, open(os.path.join(MYROOT, "validation", f"cpu_profile_S01_supplement_threads{nth}.json"), "w"), indent=1)
apply_precision_mode(prob, "fp64")
out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
json.dump(out, open(os.path.join(MYROOT, "validation", f"cpu_profile_S01_supplement_threads{nth}.json"), "w"), indent=1)
print("DONE supplement", flush=True)
