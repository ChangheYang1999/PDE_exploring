"""Attach the SPEC 6.1 holdout validation (axi.validate) to a finished run: writes runs/<id>/validation.json and adds a
'validation' summary into result.json (used by the leaderboard ranking).  Usage: python3 scripts/validate_candidate.py <run_dir> [more...]"""
import os, sys, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(ROOT, "src"))
import torch
from axi.problem import Problem, Config
from axi import validate
torch.set_default_dtype(torch.float64)
for run_dir in sys.argv[1:]:
    t0 = time.time()
    d = torch.load(os.path.join(run_dir, "final.pt"), weights_only=False, map_location="cpu")
    prob, x = Problem.from_state(d, device="cpu")
    v = validate.validate(prob, x)
    try:
        v["stagnation"] = validate.stagnation(prob, x)
    except Exception as ex:
        v["stagnation"] = dict(error=repr(ex))
    v["elapsed_s"] = time.time() - t0; v["time"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    json.dump(v, open(os.path.join(run_dir, "validation.json"), "w"), indent=1, default=float)
    rp = os.path.join(run_dir, "result.json")
    if os.path.exists(rp):
        r = json.load(open(rp)); r["validation"] = {k: v[k] for k in ("rho_max", "m_max", "rho_M_max", "rho_reduced_max", "a_eff", "s_core", "s_far", "Omega_max", "rho_max_by_eq", "status", "n_degenerate")}
        stg = v.get("stagnation", {}); r["validation"]["n_axis_zeros"] = len(stg.get("axis_zeros", [])); r["validation"]["n_offaxis_zeros"] = len(stg.get("offaxis_zeros", []))
        r["validation"]["swirl_max_defect"] = (stg.get("swirl_max") or {}).get("defect"); r["validation"]["elliptic_max_rel_diff_phi"] = (v.get("elliptic") or {}).get("max_rel_diff_phi")
        tmp = rp + ".tmp"; json.dump(r, open(tmp, "w"), indent=1, default=float); os.replace(tmp, rp)
    print(f"{os.path.basename(run_dir)}: {validate.summary_line(v)} ({v['elapsed_s']:.0f}s)")
