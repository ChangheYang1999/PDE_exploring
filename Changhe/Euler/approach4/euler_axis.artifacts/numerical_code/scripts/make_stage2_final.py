"""Final Stage II jobs (2026-10-29T08:45Z, priority 9; the GPUs were idle), each answering one named question about the 0.74 direct-seed state:
 (1) t1seedNoS1_cl0p74_q2p5: the S1 rows and the q0 pin removed (gauge only) from the 0.74 state: do the rows hold the swirl, or does it collapse?
 (2) t1seedSep_cl0p74_q2p5: separated exterior columns (slave_correction false, merge_tol 0.002, as L3sep) instead of the slaved correction:
     the second outer-domain treatment at the best interior state.
 (3) freeclmid_t1seedC_cl0p74: free c_l with the bounds [0.70, 0.745]: with 0.749 unreachable, does c_l go to the new upper bound or stay at 0.74?
 (4) direct seeds (referee 0.74 seed, q0 2.5, D36, 1500 LM) at fixed c_l 0.745, 0.7425, 0.7375: is the 0.74 floor a point or a valley?
Idempotent. Usage: python3 scripts/make_stage2_final.py [--dry]"""
import os, sys, json, copy
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); Q = os.path.join(ROOT, "queue", "pending"); dry = "--dry" in sys.argv
def load(j): return json.load(open(os.path.join(ROOT, "runs", j, "job.json")))
def write(job):
    path = os.path.join(Q, job["job_id"] + ".json")
    if os.path.exists(path) or os.path.isdir(os.path.join(ROOT, "runs", job["job_id"])): print("skip", job["job_id"]); return
    if dry: print("would write", job["job_id"]); return
    json.dump(job, open(path + ".tmp", "w"), indent=1); os.replace(path + ".tmp", path); print("queued", job["job_id"])
P = "t1seedC_cl0p74_q2p5"; base = load(P); st = os.path.join(ROOT, "runs", P, "final.pt")
def child(job_id, suffix, tags, note, cfg_over, iters=1000):
    j = copy.deepcopy(base); j["job_id"] = job_id; j["priority"] = 9; j["branch"] = "S1pin_t1budget_fixedcl_seed_" + suffix; j["stage"] = "II"
    j["from_state"] = st; j["parent"] = P; j["tags"] = tags + ["from:" + P, "sensitivity_0p74"]; j["note"] = note; j["cfg"].update(cfg_over)
    j["optimizer"] = [{"name": "lm", "max_iter": iters, "verbose": False, "time_limit": 3600, "ftol": 1e-12}]; return j
write(child("t1seedNoS1_cl0p74_q2p5", "noS1", ["no_S1_rows", "no_q0_pin"], "0.74 direct-seed state re-optimized WITHOUT the S1 rows and the q0 pin (gauge row only), 1000 LM iterations: do the rows hold the swirl?",
            {"s1_constraint": False, "q0_pin": None, "w_s1": 0.0}))
write(child("t1seedSep_cl0p74_q2p5", "sep", ["separated_exterior", "outer_treatment"], "0.74 direct-seed state re-optimized with separated exterior columns (no slaved correction, merge_tol 0.002, as L3sep), 1000 LM iterations: second outer-domain treatment",
            {"slave_correction": False, "merge_tol": 0.002}))
fc = load("freecl_t1seedC_cl0p74"); j = copy.deepcopy(fc); j["job_id"] = "freeclmid_t1seedC_cl0p74"; j["priority"] = 9; j["cfg"]["cl_bounds"] = [0.70, 0.745]
j["tags"] = list(fc.get("tags", [])) + ["cl_bounds_0p70_0p745"]; j["note"] = "free c_l from the 3000-iteration 0.74 direct-seed state with bounds [0.70, 0.745]: with 0.749 unreachable, does c_l go to the new upper bound or stay near 0.74? 1500 LM iterations"
j["optimizer"] = [{"name": "lm", "max_iter": 1500, "verbose": False, "time_limit": 3600, "ftol": 1e-12}]; write(j)
seed = load("t1seed_cl0p74_q2p5")
for cl in (0.745, 0.7425, 0.7375):
    assert round(cl, 2) == 0.74
    j = copy.deepcopy(seed); tag = ("%.4f" % cl).rstrip("0").replace(".", "p"); j["job_id"] = f"t1seed_cl{tag}_q2p5"; j["priority"] = 9
    j["cfg"]["cl"] = cl; j["tags"] = ["T1", "positive_strain_seed", "fixed_cl", "near_0p74", "slaved_exterior"]
    j["optimizer"] = [{"name": "lm", "max_iter": 1500, "verbose": False, "time_limit": 3600, "ftol": 1e-11}]
    j["note"] = f"direct positive-strain seed (the tabulated 0.74 seed) at fixed c_l {cl} with q0 2.5, D36, 1500 LM iterations: is the 0.74 floor a point or a valley?"
    write(j)
