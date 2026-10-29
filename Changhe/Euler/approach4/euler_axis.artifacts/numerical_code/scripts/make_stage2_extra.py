"""Three further Stage II jobs for the 0.74 direct-seed state (priority 8, after the chains and perturbations), 2026-10-29T07:15Z:
 (1) t1seedC2_cl0p74_q2p5: 3000 more LM iterations at D36 (does the crawl continue beyond 6000 iterations? the 0.68 state did not improve);
 (2) t1seedShiftL2_cl0p74_q2p5: D48 level of the shell-weight-shift-0 state (reduced-equation holdout 0.70, momentum 7.55 at D36);
 (3) freeclwide_t1seedC_cl0p74: free c_l from the 0.74 state with the upper bound widened to 0.80 (does it leave the target interval as the
     0.749 ladder did?). Idempotent. Usage: python3 scripts/make_stage2_extra.py [--dry]"""
import os, sys, json, copy
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); Q = os.path.join(ROOT, "queue", "pending"); dry = "--dry" in sys.argv
def load(j): return json.load(open(os.path.join(ROOT, "runs", j, "job.json")))
def write(job):
    path = os.path.join(Q, job["job_id"] + ".json")
    if os.path.exists(path) or os.path.isdir(os.path.join(ROOT, "runs", job["job_id"])): print("skip", job["job_id"]); return
    if dry: print("would write", job["job_id"]); return
    json.dump(job, open(path + ".tmp", "w"), indent=1); os.replace(path + ".tmp", path); print("queued", job["job_id"])
base = load("t1seedC_cl0p74_q2p5")
j = copy.deepcopy(base); j["job_id"] = "t1seedC2_cl0p74_q2p5"; j["priority"] = 8; j["from_state"] = os.path.join(ROOT, "runs", "t1seedC_cl0p74_q2p5", "final.pt")
j["parent"] = "t1seedC_cl0p74_q2p5"; j["tags"] = ["continue", "from:t1seedC_cl0p74_q2p5"]; j["note"] = "second continuation of the 0.74 direct seed (3000 -> 6000 LM iterations, D36)"
j["optimizer"] = [{"name": "lm", "max_iter": 3000, "verbose": False, "time_limit": 3600, "ftol": 1e-12}]; write(j)
sh = load("t1seedShift_cl0p74_q2p5")
j = copy.deepcopy(sh); j["job_id"] = "t1seedShiftL2_cl0p74_q2p5"; j["priority"] = 8; j["branch"] = sh["branch"] + "_L2"
j["from_state"] = os.path.join(ROOT, "runs", "t1seedShift_cl0p74_q2p5", "final.pt"); j["parent"] = "t1seedShift_cl0p74_q2p5"
j["cfg"]["D"] = 48; j["cfg"]["nmax"] = 32; j["cfg"]["shells"] = [[10.0, 32]]; j["tags"] = ["L2", "scale_power_shift_0", "from:t1seedShift_cl0p74_q2p5", "sensitivity_0p74"]
j["note"] = "D48/n32/K32 level of the shell-weight-shift-0 variant of the 0.74 state (reduced holdout 0.70, momentum 7.55 at D36), 1500 LM iterations"
j["optimizer"] = [{"name": "lm", "max_iter": 1500, "verbose": False, "time_limit": 3600, "ftol": 1e-12}]; write(j)
fc = load("freecl_t1seedC_cl0p74")
j = copy.deepcopy(fc); j["job_id"] = "freeclwide_t1seedC_cl0p74"; j["priority"] = 8; j["cfg"]["cl_bounds"] = [0.501, 0.80]
j["tags"] = list(fc.get("tags", [])) + ["cl_bound_0p80"]; j["note"] = "free c_l from the 3000-iteration 0.74 direct-seed state with the upper bound widened to 0.80 (the ladder left the interval to 0.80), 1500 LM iterations"
j["optimizer"] = [{"name": "lm", "max_iter": 1500, "verbose": False, "time_limit": 3600, "ftol": 1e-12}]; write(j)
