"""D6FP 2026-10-29: bitwise regression of the exact one-entry parameter-table cache in Problem.pressure_tables_at (label VALIDATION, CPU).
S01 at its own parameters: (1) objective_at twice at the same z: identical residual bitwise, one cache hit; (2) z with moved parameters: miss,
different residual; (3) back at z: miss (one entry), residual bitwise equal to (1) (determinism of the rebuild); (4) TABLE_CACHE False: residual
bitwise equal to (1); (5) relayout (new pressure solvers at the same parameters) must miss and give the same bytes; (6) parameter columns (jvp) and the
complete gradient byte-identical with the cache on and off (lead 02:48Z item 6). Also a coefficient-only perturbation (parameters unchanged): hit, and its residual equals the uncached evaluation bitwise.
Output validation/test_table_cache.json."""
import sys, os, json, time
MYROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); sys.path.insert(0, MYROOT); sys.path.insert(0, os.path.join(MYROOT, "scripts"))
os.environ["CUDA_VISIBLE_DEVICES"] = ""
import torch; torch.set_default_dtype(torch.float64); torch.set_num_threads(int(os.environ.get("OMP_NUM_THREADS", "1")))
def same_bytes(a, b):                     # genuine bitwise comparison (torch.equal equates signed zeros; astra review 02:54Z)
    return a.detach().numpy().tobytes() == b.detach().numpy().tobytes()
from validation.gates import Case, ROOT
import src.optimization.problem as P
case = Case("S01", "cpu", start=os.path.join(ROOT, "starts", "S01_nest6_cl0.45_om1.0_p0.pt")); prob = case.prob; zf = case.z_full.clone(); n = zf.numel()
out = dict(started=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), precision_mode=getattr(prob, "precision_mode", None), table_cache=P.TABLE_CACHE, steps=[])
def ev(z, tag):
    t0 = time.perf_counter(); r, aux = prob.objective_at(z); dt = time.perf_counter() - t0
    rec = dict(tag=tag, seconds=dt, hits=getattr(prob, "_table_cache_hits", 0), misses=getattr(prob, "_table_cache_misses", 0), cost=0.5 * float(r @ r))
    out["steps"].append(rec); print(json.dumps(rec), flush=True); return r
H0, M0 = getattr(prob, "_table_cache_hits", 0), getattr(prob, "_table_cache_misses", 0)      # the Case construction already built (and cached) the tables at z
out["counts_after_case_build"] = dict(hits=H0, misses=M0)
def dh(i, j): return out["steps"][j]["hits"] - out["steps"][i]["hits"]
def dm(i, j): return out["steps"][j]["misses"] - out["steps"][i]["misses"]
r1 = ev(zf, "first at z (hit or miss depending on the Case build)"); r2 = ev(zf, "same z (hit expected)")
ok1 = same_bytes(r1, r2) and dh(0, 1) == 1 and dm(0, 1) == 0
zc = zf.clone(); zc[: n - 2] += 1e-6 * torch.randn(n - 2, generator=torch.Generator().manual_seed(3))     # coefficients only: parameters unchanged
r3 = ev(zc, "coefficients moved, parameters unchanged (hit expected)")
P.TABLE_CACHE = False; r3u = ev(zc, "same, cache off (uncached reference)"); P.TABLE_CACHE = True
ok3 = same_bytes(r3, r3u) and dh(1, 2) == 1 and dm(1, 2) == 0
zp = zf.clone(); zp[n - 2] += 1e-3; zp[n - 1] -= 1e-3
r4 = ev(zp, "parameters moved (miss expected)"); ok4 = (not same_bytes(r4, r1)) and dm(3, 4) == 1
r5 = ev(zf, "back at z (miss, one entry)"); ok5 = same_bytes(r5, r1) and dm(4, 5) == 1 and dh(4, 5) == 0
P.TABLE_CACHE = False; r6 = ev(zf, "cache off at z"); P.TABLE_CACHE = True; ok6 = same_bytes(r6, r1)
# (c) relayout between two evaluations at the same (c_l, omega) must miss (lead 02:48Z item 6 (c)): rebuild the pressure solver as ensure_geometry does
from src.pressure.poisson_sh import PressureSolver
from src.equations.fields import alpha_of
cl0, om0 = float(prob.pressure.c_l), float(prob.pressure.omega)
prob.geometry_generation = getattr(prob, "geometry_generation", 0) + 1
prob.pressure = PressureSolver(prob.model, p0=2 * alpha_of(cl0) + 2, omega=om0, c_l=cl0, exterior_monopole=prob.exterior_monopole)
if prob.fine_model is not None:
    prob.fine_ps = PressureSolver(prob.fine_model, p0=2 * alpha_of(cl0) + 2, omega=om0, c_l=cl0)
r7 = ev(zf, "after relayout at the same parameters (miss expected)"); ok7 = (dm(-2, -1) == 1) and same_bytes(r7, r1)
# (a) parameter columns (jvp; the cache is bypassed inside functorch) and the complete gradient, cache on and off, byte-identical
from src.optimization.lm import param_columns
import worker_d6 as W
pfun = lambda q: prob.residual_vector_wd(case.to_full_opt(q), differentiable_pressure=True)
zo = case.z_opt; nn_ = zo.numel()
t0 = time.perf_counter(); pc_on = param_columns(pfun, zo, [nn_ - 2, nn_ - 1]); t_pc_on = time.perf_counter() - t0
P.TABLE_CACHE = False; t0 = time.perf_counter(); pc_off = param_columns(pfun, zo, [nn_ - 2, nn_ - 1]); t_pc_off = time.perf_counter() - t0; P.TABLE_CACHE = True
ok8 = all(same_bytes(a, b) for a, b in zip(pc_on, pc_off))
t0 = time.perf_counter(); g_on = W.complete_gradient_opt(prob, case.pm, case.to_full_opt, zo); t_g_on = time.perf_counter() - t0
P.TABLE_CACHE = False; t0 = time.perf_counter(); g_off = W.complete_gradient_opt(prob, case.pm, case.to_full_opt, zo); t_g_off = time.perf_counter() - t0; P.TABLE_CACHE = True
ok9 = same_bytes(g_on, g_off)
out["param_columns"] = dict(seconds_cache_on=t_pc_on, seconds_cache_off=t_pc_off, bitwise=ok8); out["complete_gradient"] = dict(seconds_cache_on=t_g_on, seconds_cache_off=t_g_off, bitwise=ok9)
out["hits_total"] = getattr(prob, "_table_cache_hits", 0); out["misses_total"] = getattr(prob, "_table_cache_misses", 0)
out["checks"] = dict(same_point_hit_bitwise=ok1, coefficient_move_hit_bitwise_vs_uncached=ok3, parameter_move_miss=ok4, return_miss_bitwise=ok5, cache_off_bitwise=ok6,
                     relayout_same_parameters_miss_and_bitwise=ok7, param_columns_bitwise_on_off=ok8, complete_gradient_bitwise_on_off=ok9)
out["all_pass"] = all(out["checks"].values()); out["finished"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
json.dump(out, open(os.path.join(MYROOT, "validation", "test_table_cache.json"), "w"), indent=1)
print("CHECKS", json.dumps(out["checks"]), "ALL_PASS", out["all_pass"])
