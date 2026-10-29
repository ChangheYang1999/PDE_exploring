"""Perturbed restarts of the 0.74 direct-seed state with PER-COEFFICIENT relative Gaussian noise, x_k -> x_k (1 + eps g_k), g_k ~ N(0, 1)
(the earlier global-RMS perturbation of make_stage2_sensitivity.py destroyed the exterior tail, whose coefficients are far smaller than the
global RMS: initial cost 2e15). eps = 1e-2, 3e-2, 1e-1 with seeds 11, 12, 13; 1500 LM iterations each. Idempotent.
Usage: python3 scripts/make_relative_perturbations.py [--dry]"""
import os, sys, json, copy, torch
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
Q = os.path.join(ROOT, "queue", "pending"); dry = "--dry" in sys.argv
PARENT = "t1seedC_cl0p74_q2p5"
base = json.load(open(os.path.join(ROOT, "runs", PARENT, "job.json")))
st = torch.load(os.path.join(ROOT, "runs", PARENT, "final.pt"), map_location="cpu", weights_only=False)
x = st["x"].clone(); pdir = os.path.join(ROOT, "scratch", "perturbed_0p74"); os.makedirs(pdir, exist_ok=True)
for k, (eps, seed) in enumerate([(1e-2, 11), (3e-2, 12), (1e-1, 13)], start=1):
    g = torch.Generator().manual_seed(seed)
    xp = x * (1.0 + eps * torch.randn(x.shape, generator=g, dtype=x.dtype))
    sp = dict(st); sp["x"] = xp; sp["perturbation"] = {"type": "per-coefficient relative", "eps": eps, "seed": seed, "parent": PARENT}
    ppath = os.path.join(pdir, f"relpert{k}_eps{eps:g}_seed{seed}.pt")
    if not os.path.exists(ppath) and not dry:
        torch.save(sp, ppath)
    j = copy.deepcopy(base)
    j["job_id"] = f"t1seedRPert{k}_cl0p74_q2p5"; j["priority"] = 7; j["branch"] = "S1pin_t1budget_fixedcl_seed_relpert"; j["stage"] = "II"
    j["from_state"] = ppath; j["parent"] = PARENT
    j["tags"] = ["perturbed_restart_relative", f"eps_{eps:g}", "from:" + PARENT, "sensitivity_0p74"]
    j["note"] = f"0.74 direct-seed state with per-coefficient relative Gaussian noise eps {eps:g} (seed {seed}), then 1500 LM iterations: does it return to the 2.8 floor?"
    j["optimizer"] = [{"name": "lm", "max_iter": 1500, "verbose": False, "time_limit": 3600, "ftol": 1e-12}]
    path = os.path.join(Q, j["job_id"] + ".json")
    if os.path.exists(path) or os.path.isdir(os.path.join(ROOT, "runs", j["job_id"])):
        print("skip", j["job_id"]); continue
    if dry: print("would write", j["job_id"]); continue
    json.dump(j, open(path + ".tmp", "w"), indent=1); os.replace(path + ".tmp", path); print("queued", j["job_id"])
