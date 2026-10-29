"""Late Stage II jobs (2026-10-29T07:55Z; GPUs free until the 11:30Z stop), priority 9, all fixed c_l, S1 rows, q0 pin and slaved exterior as in
the direct-seed jobs:
 (a) unrelated initializations at fixed c_l 0.74 with the direct-seed rows (q0 pin 2.5, S1 rows, slaved exterior, D36/n24/K24): families
     gauss_core, ring_core, asym_dipole, swirl_dominant, poloidal_dominant, random_spectral (1500 LM iterations): is the 2.8 floor reached
     from starts unrelated to the referee seed, or is it a property of the seed's structure?
 (b) fresh-level direct seeds at 0.74: the referee seed optimized directly at D24/n12/K16 and at D48/n32/K32 (no transfer from D36): does the
     level value depend on the path?
 (c) the sensitivity suite for the 0.68 state (t1seedC2_cl0p68, 3.38): outer interface R = 5 and 20, 1.5x quadrature, shell-weight shift 0.
Idempotent. Usage: python3 scripts/make_stage2_late.py [--dry]"""
import os, sys, json, copy
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); Q = os.path.join(ROOT, "queue", "pending"); dry = "--dry" in sys.argv
def load(j): return json.load(open(os.path.join(ROOT, "runs", j, "job.json")))
def write(job):
    path = os.path.join(Q, job["job_id"] + ".json")
    if os.path.exists(path) or os.path.isdir(os.path.join(ROOT, "runs", job["job_id"])): print("skip", job["job_id"]); return
    if dry: print("would write", job["job_id"]); return
    json.dump(job, open(path + ".tmp", "w"), indent=1); os.replace(path + ".tmp", path); print("queued", job["job_id"])
seed = load("t1seed_cl0p74_q2p5")                      # direct seed job: init t1budget, gauge_from_seed, S1 rows, q0 pin 2.5, slaved exterior, D36
# (a) unrelated initializations with the same rows
for k, fam in enumerate(["gauss_core", "ring_core", "asym_dipole", "swirl_dominant", "poloidal_dominant", "random_spectral"], start=1):
    j = copy.deepcopy(seed); j["job_id"] = f"unrel_{fam}_cl0p74_q2p5"; j["priority"] = 9; j["branch"] = "S1pin_unrelated_fixedcl_0p74"
    j["init"] = {"family": fam, "seed": 100 + k, "extra": {"q0": 2.5}}
    j["tags"] = ["T1rows", "unrelated_init", fam, "fixed_cl", "direct_0p74", "slaved_exterior"]
    j["optimizer"] = [{"name": "lm", "max_iter": 1500, "verbose": False, "time_limit": 3600, "ftol": 1e-11}]
    j["note"] = f"unrelated initialization ({fam}, seed {100 + k}) at fixed c_l 0.74 with the direct-seed rows (S1 rows, q0 pin 2.5, slaved exterior), D36, 1500 LM iterations"
    write(j)
# (b) fresh-level seeds
for D, n, K, tag in [(24, 12, 16, "D24"), (48, 32, 32, "D48")]:
    j = copy.deepcopy(seed); j["job_id"] = f"t1seedFresh{tag}_cl0p74_q2p5"; j["priority"] = 9; j["branch"] = f"S1pin_t1budget_fixedcl_seed_fresh{tag}"
    j["cfg"]["D"] = D; j["cfg"]["nmax"] = n; j["cfg"]["shells"] = [[10.0, K]]; j["cfg"]["nR_ball"] = j["cfg"]["nR_shell"] = j["cfg"]["nR_ext"] = j["cfg"]["nmu"] = 0
    j["tags"] = ["T1", "positive_strain_seed", "fixed_cl", "direct_0p74", "slaved_exterior", f"fresh_{tag}"]
    j["optimizer"] = [{"name": "lm", "max_iter": 1500, "verbose": False, "time_limit": 3600, "ftol": 1e-11}]
    j["note"] = f"direct positive-strain seed at fixed c_l 0.74 (q0 2.5) optimized directly at {tag}/n{n}/K{K} (no transfer from D36), 1500 LM iterations"
    write(j)
# (c) sensitivity suite for the 0.68 state
P = "t1seedC2_cl0p68"; base = load(P); st = os.path.join(ROOT, "runs", P, "final.pt")
def child(job_id, suffix, tags, note, cfg_over, iters=1000):
    j = copy.deepcopy(base); j["job_id"] = job_id; j["priority"] = 9; j["branch"] = "S1pin_t1budget_fixedcl_seed_" + suffix; j["stage"] = "II"
    j["from_state"] = st; j["parent"] = P; j["tags"] = tags + ["from:" + P, "sensitivity_0p68"]; j["note"] = note; j["cfg"].update(cfg_over)
    j["optimizer"] = [{"name": "lm", "max_iter": iters, "verbose": False, "time_limit": 3600, "ftol": 1e-12}]; return j
write(child("t1seedRm5_cl0p68", "rm5", ["Rm5", "matching_radius"], "0.68 direct-seed state (3.38) with the outer interface moved from R = 10 to R = 5, 1000 LM iterations", {"shells": [[5.0, 24]]}))
write(child("t1seedRm20_cl0p68", "rm20", ["Rm20", "matching_radius"], "0.68 direct-seed state (3.38) with the outer interface moved from R = 10 to R = 20 (K 32), 1500 LM iterations", {"shells": [[20.0, 32]]}, 1500))
write(child("t1seedQuad_cl0p68", "quad1p5", ["quadrature_1p5x"], "0.68 direct-seed state (3.38) re-optimized with 1.5x quadrature nodes (nR_ball 40, nR_shell 52, nmu 45), 1000 LM iterations", {"nR_ball": 40, "nR_shell": 52, "nmu": 45}))
write(child("t1seedShift_cl0p68", "shift0", ["scale_power_shift_0", "weights"], "0.68 direct-seed state (3.38) re-optimized with scale_power_shift 0 instead of -2, 1000 LM iterations", {"scale_power_shift": 0.0}))
