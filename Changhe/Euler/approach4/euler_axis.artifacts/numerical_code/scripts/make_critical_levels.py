"""Resolution level and continuation for the best swirl-retaining c_l = 1/2 states (the separate critical experiment of the prompt: 46 runs at
D24 so far; FINAL_REPORT 4.6 row 'c_l = 1/2 experiment'). Selection: the two finished c_l = 1/2 runs with the smallest holdout rho_max among
those passing the swirl magnitude filter (s_core and s_far >= 0.05). For each: a refinement (D32/n16/K22, transfer, 1500 LM iterations) and a
continuation (same basis, 2000 more iterations). Priority 8. Idempotent. Usage: python3 scripts/make_critical_levels.py [--dry]"""
import os, sys, json, copy, csv
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); Q = os.path.join(ROOT, "queue", "pending"); dry = "--dry" in sys.argv
rows = [r for r in csv.DictReader(open(os.path.join(ROOT, "FAILURE_MAP.csv"))) if r["job_id"].startswith("crit")]
ok = [r for r in rows if float(r["s_core"] or 0) >= 0.05 and float(r["s_far"] or 0) >= 0.05 and r["rho_max"] not in ("", "nan")]
ok.sort(key=lambda r: float(r["rho_max"]))
def write(job):
    path = os.path.join(Q, job["job_id"] + ".json")
    if os.path.exists(path) or os.path.isdir(os.path.join(ROOT, "runs", job["job_id"])): print("skip", job["job_id"]); return
    if dry: print("would write", job["job_id"], job["note"]); return
    json.dump(job, open(path + ".tmp", "w"), indent=1); os.replace(path + ".tmp", path); print("queued", job["job_id"])
for r in ok[:2]:
    jid = r["job_id"]; base = json.load(open(os.path.join(ROOT, "runs", jid, "job.json")))
    res = json.load(open(os.path.join(ROOT, "runs", jid, "result.json")))
    cfg = dict(res["cfg"]); cfg["cl"] = 0.5; cfg["free_cl"] = False
    for mode in ("ref", "cont"):
        j = copy.deepcopy(base); j["job_id"] = f"crit{mode}_{jid}"[:120]; j["priority"] = 8; j["stage"] = "II-critical"; j["max_retries"] = 2; j["ckpt_seconds"] = 300
        c = dict(cfg)
        if mode == "ref":
            c["D"] = 32; c["nmax"] = 16; c["shells"] = [[s[0], 22] for s in cfg["shells"]]; c["nR_ball"] = c["nR_shell"] = c["nR_ext"] = c["nmu"] = 0
        j["cfg"] = c; j["from_state"] = os.path.join(ROOT, "runs", jid, "final.pt"); j["auto_row_scale"] = True; j.pop("init", None)
        j["branch"] = (res.get("branch") or "generic") + ("_refine" if mode == "ref" else "_continue"); j["parent"] = jid
        j["tags"] = ["critical", "cl_half", "refine" if mode == "ref" else "continue", "from:" + jid]
        j["optimizer"] = [{"name": "lm", "max_iter": 1500 if mode == "ref" else 2000, "verbose": False, "time_limit": 3600, "ftol": 1e-12}]
        j["note"] = (f"c_l = 1/2 experiment: {'D32/n16/K22 refinement level' if mode == 'ref' else '2000 more LM iterations at D24'} of {jid} "
                     f"(holdout rho_max {float(r['rho_max']):.2f}, s_core {float(r['s_core']):.2f}, s_far {float(r['s_far']):.2f})")
        write(j)
print("selected:", [(r["job_id"], r["rho_max"][:6], r["s_core"][:5], r["s_far"][:5]) for r in ok[:2]])
