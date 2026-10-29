"""Stage II sensitivity and robustness jobs for the best interior state (the 0.74 direct positive-strain seed after 3000 LM
iterations, runs/t1seedC_cl0p74_q2p5, holdout rho_max 2.86 at D36 and 2.85 at D48). Prompt section 9 (sensitivity to matching
radius, radial-shell weights and quadrature resolution), Stage II (outer-domain treatments, factor-of-two matching radius),
Stage III item 4 (perturbed coefficients re-optimized; this is optimization, so it runs before the 11:59:44Z stop), and the two
optimizer comparison (L-BFGS then LM against LM only). Idempotent: existing queue files or finished runs are skipped.
Usage: python3 scripts/make_stage2_sensitivity.py [--dry]
"""
import os, sys, json, copy
import torch
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
Q = os.path.join(ROOT, "queue", "pending")
dry = "--dry" in sys.argv
PARENT = "t1seedC_cl0p74_q2p5"
base = json.load(open(os.path.join(ROOT, "runs", PARENT, "job.json")))
state_path = os.path.join(ROOT, "runs", PARENT, "final.pt")

def write(job):
    path = os.path.join(Q, job["job_id"] + ".json")
    if os.path.exists(path) or os.path.exists(os.path.join(ROOT, "runs", job["job_id"], "result.json")) \
            or os.path.isdir(os.path.join(ROOT, "runs", job["job_id"])):
        print("skip (exists)", job["job_id"]); return
    if dry:
        print("would write", job["job_id"]); return
    tmp = path + ".tmp"
    json.dump(job, open(tmp, "w"), indent=1); os.replace(tmp, path)
    print("queued", job["job_id"])

def child(job_id, branch_suffix, tags, note, cfg_over=None, optimizer=None, from_state=state_path, iters=1000, prio=7):
    j = copy.deepcopy(base)
    j["job_id"] = job_id
    j["priority"] = prio
    j["branch"] = "S1pin_t1budget_fixedcl_seed_" + branch_suffix
    j["stage"] = "II"
    j["from_state"] = from_state
    j["parent"] = PARENT
    j["tags"] = tags + ["from:" + PARENT, "sensitivity_0p74"]
    j["note"] = note
    if cfg_over:
        j["cfg"].update(cfg_over)
    j["optimizer"] = optimizer or [{"name": "lm", "max_iter": iters, "verbose": False, "time_limit": 3600, "ftol": 1e-12}]
    return j

jobs = []
# 1. matching radius: outer interface at R = 5 and R = 20 (factor-of-two changes around the working value 10)
jobs.append(child("t1seedRm5_cl0p74_q2p5", "rm5", ["Rm5", "matching_radius"],
                  "0.74 direct-seed state with the outer interface moved from R = 10 to R = 5 (shell 2 <= R <= 5), 1000 LM iterations",
                  cfg_over={"shells": [[5.0, 24]]}, iters=1000))
jobs.append(child("t1seedRm20_cl0p74_q2p5", "rm20", ["Rm20", "matching_radius"],
                  "0.74 direct-seed state with the outer interface moved from R = 10 to R = 20 (shell 2 <= R <= 20, K 32), 1500 LM iterations",
                  cfg_over={"shells": [[20.0, 32]]}, iters=1500))
# 2. quadrature density: 1.5 times the automatic node counts (nR_ball 27 -> 40, nR_shell 35 -> 52, nmu 30 -> 45), same basis
jobs.append(child("t1seedQuad_cl0p74_q2p5", "quad1p5", ["quadrature_1p5x"],
                  "0.74 direct-seed state re-optimized with 1.5 times the automatic quadrature node counts (nR_ball 40, nR_shell 52, nmu 45), same D36/n24/K24 basis, 1000 LM iterations",
                  cfg_over={"nR_ball": 40, "nR_shell": 52, "nmu": 45}, iters=1000))
# 3. row weights: interface weight 10x and the shell scaling without the power shift
jobs.append(child("t1seedWint_cl0p74_q2p5", "wint1000", ["w_int_1000", "weights"],
                  "0.74 direct-seed state re-optimized with the interface row weight raised from 100 to 1000, 1000 LM iterations",
                  cfg_over={"w_int": 1000.0}, iters=1000))
jobs.append(child("t1seedShift_cl0p74_q2p5", "shift0", ["scale_power_shift_0", "weights"],
                  "0.74 direct-seed state re-optimized with scale_power_shift 0 instead of -2 (radial-shell weights), 1000 LM iterations",
                  cfg_over={"scale_power_shift": 0.0}, iters=1000))
# 4. perturbed restarts: Gaussian noise added to every coefficient, amplitude relative to the RMS coefficient, seeds 1, 2, 3
st = torch.load(state_path, map_location="cpu", weights_only=False)
x = st["x"].clone()
rms = float(torch.sqrt(torch.mean(x ** 2)))
pdir = os.path.join(ROOT, "scratch", "perturbed_0p74"); os.makedirs(pdir, exist_ok=True)
for k, (eps, seed) in enumerate([(1e-2, 1), (5e-2, 2), (2e-1, 3)], start=1):
    g = torch.Generator().manual_seed(seed)
    xp = x + eps * rms * torch.randn(x.shape, generator=g, dtype=x.dtype)
    sp = dict(st); sp["x"] = xp; sp["perturbation"] = {"eps_rel_rms": eps, "seed": seed, "rms_x": rms, "parent": PARENT}
    ppath = os.path.join(pdir, f"pert{k}_eps{eps:g}_seed{seed}.pt")
    if not os.path.exists(ppath) and not dry:
        torch.save(sp, ppath)
    jobs.append(child(f"t1seedPert{k}_cl0p74_q2p5", f"pert{k}", ["perturbed_restart", f"eps_{eps:g}"],
                      f"0.74 direct-seed state with Gaussian noise of relative RMS amplitude {eps:g} (seed {seed}) added to all coefficients, then 1500 LM iterations (does it return to the 2.85 floor?)",
                      from_state=ppath, iters=1500))
# 5. optimizer comparison: L-BFGS (300 outer steps of 20 inner iterations, strong Wolfe) followed by 500 LM iterations
jobs.append(child("t1seedLB_cl0p74_q2p5", "lbfgs_lm", ["optimizer_lbfgs_then_lm", "two_optimizers"],
                  "0.74 direct-seed state continued with torch L-BFGS (300 outer steps, strong Wolfe) then 500 LM iterations: optimizer dependence of the 2.85 floor",
                  optimizer=[{"name": "lbfgs", "max_iter": 300, "history_size": 50, "time_limit": 2400},
                             {"name": "lm", "max_iter": 500, "verbose": False, "time_limit": 1800, "ftol": 1e-12}]))
# 6. q0 scan at 0.74 (direct seeds; the q0 2.5 seed gave 3.55 -> 2.86, q0 3.5 gave 4.60, q0 1.8 running): add q0 2.0 and 3.0
seedjob = json.load(open(os.path.join(ROOT, "runs", "t1seed_cl0p74_q3p5", "job.json")))
for q0 in (2.0, 3.0):
    j = copy.deepcopy(seedjob)
    tag = f"{q0:.1f}".replace(".", "p")
    j["job_id"] = f"t1seed_cl0p74_q{tag}"
    j["cfg"]["q0_pin"] = q0
    j["init"]["extra"]["q0"] = q0
    j["optimizer"] = [{"name": "lm", "max_iter": 1500, "verbose": False, "time_limit": 3600, "ftol": 1e-11}]
    j["note"] = f"direct positive-strain seed at fixed c_l 0.74 with q0 {q0} (q0 scan at the tabulated seed c_l 0.74), D36"
    jobs.append(j)
for j in jobs:
    write(j)
print(f"{len(jobs)} jobs considered")
