"""Refinement/continuation jobs from finished runs (Stage I end / Stage II).
Options: --top K --prefix p2_ --priority N --allow-swirlfree --set key=value (cfg override, JSON value) --tag NAME --iters N --dry

Usage: python3 scripts/make_refine.py <mode> [--top K] [--branch-filter S1] [--dry]
Modes:
  continue : same basis, 3000 more LM iterations from final.pt (does the crawl end?)
  refine   : resolution x1.33 (D 24->32, nmax 12->16, K 16->22), transfer of the state onto the new basis, 2000 LM iterations
  freecl   : same as refine but c_l freed (bounds 0.501..0.749), S1 rows kept if present
Selection: top K finished runs by SPEC rho_max (validation) or by holdout relative residual, excluding swirl-free states
(s_core < 0.02) unless --allow-swirlfree.
"""
import os, sys, json, glob, math
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
Q = os.path.join(ROOT, "queue", "pending")
mode = sys.argv[1]
top = int(sys.argv[sys.argv.index("--top") + 1]) if "--top" in sys.argv else 8
bf = sys.argv[sys.argv.index("--branch-filter") + 1] if "--branch-filter" in sys.argv else None
dry = "--dry" in sys.argv
allow_sf = "--allow-swirlfree" in sys.argv
prefix = sys.argv[sys.argv.index("--prefix") + 1] if "--prefix" in sys.argv else None
prio = int(sys.argv[sys.argv.index("--priority") + 1]) if "--priority" in sys.argv else 25
sets = {}   # --set key=value (JSON values) overrides applied to the child cfg, e.g. --set scale_divisor=2 --set scale_shell_normalize=true
for i, a in enumerate(sys.argv):
    if a == "--set":
        k, v = sys.argv[i + 1].split("=", 1); sets[k] = json.loads(v)
tag = sys.argv[sys.argv.index("--tag") + 1] if "--tag" in sys.argv else None
iters = int(sys.argv[sys.argv.index("--iters") + 1]) if "--iters" in sys.argv else None
rows = []
for f in glob.glob(os.path.join(ROOT, "runs", "*", "result.json")):
    jid = os.path.basename(os.path.dirname(f))
    if jid.startswith("zz_") or (prefix and not jid.startswith(prefix)):
        continue
    r = json.load(open(f))
    if bf and bf not in (r.get("branch") or ""):
        continue
    v = r.get("validation") or {}
    rep = r.get("report", {})
    s_core = v.get("s_core", rep.get("swirl_ratio_inner", 0))
    if not allow_sf and (s_core is None or s_core < 0.02):
        continue
    key = v.get("rho_max")
    if key is None or not math.isfinite(key):
        key = 100 + max(rep.get("rel_Rq_inner", 1e9), rep.get("rel_Reta_inner", 1e9))
    rows.append((key, jid, r))
rows.sort(key=lambda t: t[0])
n = 0
for key, jid, r in rows[:top]:
    cfg = dict(r["cfg"])
    if r.get("cl") is not None:
        cfg["cl"] = float(r["cl"])          # start the child at the parent's FINAL c_l (free-c_l parents end away from their start value)
    if mode in ("refine", "freecl"):
        cfg["D"] = int(round(cfg["D"] * 4 / 3)); cfg["nmax"] = int(round(cfg["nmax"] * 4 / 3))
        cfg["shells"] = [[s[0], int(round(s[1] * 4 / 3))] for s in cfg["shells"]]
        cfg["nR_ball"] = cfg["nR_shell"] = cfg["nR_ext"] = cfg["nmu"] = 0
    if mode == "freecl":
        cfg["free_cl"] = True
    cfg.update(sets)
    opt = [{"name": "lm", "max_iter": iters or (3000 if mode == "continue" else 2000), "verbose": False, "time_limit": 3000, "ftol": 1e-12}]
    job = dict(job_id=f"{tag or (mode[:4] + '1')}_{jid}"[:120], priority=prio, branch=(r.get("branch") or "") + f"_{mode}", stage="I-II", max_retries=2, ckpt_seconds=300,
               cfg=cfg, from_state=os.path.join(ROOT, "runs", jid, "final.pt"), auto_row_scale=True, optimizer=opt,
               tags=[mode, "from:" + jid], parent=jid, parent_metric=key)
    path = os.path.join(Q, job["job_id"] + ".json")
    if dry:
        print(job["job_id"], f"parent metric {key:.3e}"); continue
    if not os.path.exists(path) and not os.path.exists(os.path.join(ROOT, "runs", job["job_id"], "result.json")):
        json.dump(job, open(path, "w"), indent=1); n += 1
print(f"{mode}: {n} jobs written from {len(rows)} eligible finished runs")
