#!/usr/bin/env python
"""D6FP: markdown profiling report (SPEC 9) from profiling/profile_S01.json."""
import json, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
p = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "profiling", "profile_S01.json")))
fr, fx = p["modes"]["free"], p["modes"]["fixed"]
def med(m, k):
    v = m.get(k); return (f"{v['median']:.3f} s (min {v['min']:.3f}, max {v['max']:.3f}, n {v['reps']})" if isinstance(v, dict) and "median" in v else ("n/a" if v is None else str(v)))
print(f"Profiling (SPEC 9) at {p['ts']}: GPU {p['gpu']} (physical index {p['physical_gpu']}), other processes on the GPU: {p['other_processes_on_gpu']}; CPU affinity {p['affinity']}, OMP {p['omp']}; chunk {p['chunk']}; start {os.path.basename(p['start'])}.")
print(f"Synchronized device timings (torch.cuda.synchronize around each region; medians of repeated runs). Free: n_opt {fr['n_opt']}, rows {fr['n_rows']}, pressure quadrature points {fr['n_quad']}; fixed: n_opt {fx['n_opt']}.\n")
print("| region | free parameters | fixed parameters |\n|---|---|---|")
keys = [k for k in fr if isinstance(fr[k], dict) and "median" in fr[k]]
for k in keys:
    print(f"| {k} | {med(fr, k)} | {med(fx, k)} |")
print(f"| model build (s) | {fr['t_model_build']:.1f} | {fx['t_model_build']:.1f} |\n| problem build incl. pressure geometry and tables (s) | {fr['t_problem_build']:.1f} | {fx['t_problem_build']:.1f} |")
print(f"| Jacobian peak GPU memory (GB) | {fr['jacobian_peak_GB']:.1f} | {fx['jacobian_peak_GB']:.1f} |\n| LM peak GPU memory (GB) | {fr['lm_peak_GB']:.1f} | {fx['lm_peak_GB']:.1f} |\n| peak RSS (GB) | {fr['peak_RSS_GB']:.2f} | {fx['peak_RSS_GB']:.2f} |")
print(f"| GPU utilization during the LM (whole GPU, nvidia-smi 0.5 s samples; mean / max) | {fr['gpu_utilization_samples']['util_mean']:.0f} / {fr['gpu_utilization_samples']['util_max']:.0f} per cent | {fx['gpu_utilization_samples']['util_mean']:.0f} / {fx['gpu_utilization_samples']['util_max']:.0f} per cent |")
print(f"| accepted steps per hour (extrapolated from {len(fr['lm_iterations'])} LM iterations) | {fr['accepted_steps_per_hour_estimate']:.0f} | {fx['accepted_steps_per_hour_estimate']:.0f} |")
print("\nPer-iteration breakdown of the short LM runs (seconds):\n\n| mode | it | accepted | trials | t_jac | t_param_cols | t_normal | t_solve | t_trial | complete gradient | t_iter |\n|---|---|---|---|---|---|---|---|---|---|---|")
for mode, m in (("free", fr), ("fixed", fx)):
    for h in m["lm_iterations"]:
        g = h.get("grad_s"); print(f"| {mode} | {h['it']} | {h['accepted']} | {h['n_trials']} | {h['t_jac']:.1f} | {h['t_param_cols']:.1f} | {h['t_normal']:.2f} | {h['t_solve']:.2f} | {h['t_trial']:.1f} | {('%.1f' % g) if g else 'n/a'} | {h['t_iter']:.1f} |")
c = p["comparison"]
print(f"\nComparison: parameter columns {c['extra_time_parameter_columns_s']:.1f} s per iteration (two exact jvp columns) on top of the coefficient Jacobian ({c['jacobian_free_s']:.1f} s free vs {c['jacobian_fixed_s']:.1f} s fixed); self-consistent trial evaluation {c['trial_rebuild_free_s']:.2f} s (free, tables rebuilt) vs {c['trial_rebuild_fixed_s']:.2f} s (fixed); mean iteration {c['mean_iteration_free_s']:.1f} s free vs {c['mean_iteration_fixed_s']:.1f} s fixed; complete gradient {c['complete_gradient_s']:.1f} s per accepted iteration.")
if "angular_table_paths_this_process" in fr:
    print(f"\nAngular-table paths in the profiling process: {json.dumps(fr['angular_table_paths_this_process']['counts'])}.")
