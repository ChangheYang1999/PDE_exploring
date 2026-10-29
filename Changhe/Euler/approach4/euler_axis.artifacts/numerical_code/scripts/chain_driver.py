"""Small-step c_l continuation chain for the Stage II failure map (lead notes 21, 25 item 5 (c), 27).

The supervisor has no job dependencies, so this driver (a detached, sleeping CPU process) writes one queue job at a time: step k+1
is written when step k has a result.json (its final.pt is the from_state of step k+1).  At the c_l values listed in --levels-at the
driver also queues the two other resolution levels (down-projection to D24/n12/K16 and refinement to D48/n32/K32) and, where
--rm20-at lists the c_l, a run with the matching radius doubled (Rm 20, K scaled) for the outer-domain test of lead note 27 item 2.
All jobs are fixed-c_l Levenberg-Marquardt continuations with the parent's rows (S1 rows, q0 pin, slaved exterior) kept.

Usage:
  python3 scripts/chain_driver.py --start <run_dir> --tag fmA --cls 0.73,0.72,0.71,0.70,0.675,0.65,0.625,0.60,0.575,0.55 \
      --levels-at 0.70,0.65,0.60,0.55 --rm20-at 0.70 [--priority 6] [--iters 2500] [--poll 30]
Log: logs/chain_driver_<tag>.log ; state: logs/chain_driver_<tag>.json (resumable: rerun the same command, finished steps are skipped).
"""
import os, sys, json, time, argparse, glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
Q = os.path.join(ROOT, "queue", "pending")
RUNS = os.path.join(ROOT, "runs")


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def cl_tag(cl):
    return ("%.4f" % cl).rstrip("0").rstrip(".").replace(".", "p")


def write_job(job_id, cfg, from_state, prio, iters, tags, parent, branch, note):
    path = os.path.join(Q, job_id + ".json")
    if os.path.exists(path) or os.path.exists(os.path.join(RUNS, job_id)):
        return False
    job = dict(job_id=job_id, priority=prio, branch=branch, stage="II", max_retries=2, ckpt_seconds=300, cfg=cfg, from_state=from_state,
               auto_row_scale=True, optimizer=[{"name": "lm", "max_iter": iters, "verbose": False, "time_limit": 3600, "ftol": 1e-12}],
               tags=tags, parent=parent, note=note)
    tmp = path + ".tmp"
    json.dump(job, open(tmp, "w"), indent=1)
    os.replace(tmp, path)
    return True


def status(job_id):
    d = os.path.join(RUNS, job_id)
    if os.path.exists(os.path.join(d, "result.json")):
        return "done"
    if os.path.exists(os.path.join(d, "error.json")) and not os.path.exists(os.path.join(Q, job_id + ".json")) and \
            not glob.glob(os.path.join(ROOT, "queue", "running", job_id + ".json")):
        return "failed"
    return "pending"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--cls", required=True)
    ap.add_argument("--levels-at", default="")
    ap.add_argument("--rm20-at", default="")
    ap.add_argument("--priority", type=int, default=6)
    ap.add_argument("--iters", type=int, default=2500)
    ap.add_argument("--iters-level", type=int, default=2500)
    ap.add_argument("--poll", type=int, default=30)
    ap.add_argument("--merge-tol", type=float, default=None)
    ap.add_argument("--q0s", default="", help="optional q0 pin per step, aligned with --cls (lead note 29 item 4: raise q0 as c_l decreases)")
    a = ap.parse_args()
    log_path = os.path.join(ROOT, "logs", f"chain_driver_{a.tag}.log")
    st_path = os.path.join(ROOT, "logs", f"chain_driver_{a.tag}.json")

    def log(msg):
        with open(log_path, "a") as f:
            f.write(f"{now()} {msg}\n")

    cls = [float(v) for v in a.cls.split(",") if v]
    q0s = [float(v) for v in a.q0s.split(",") if v]
    assert not q0s or len(q0s) == len(cls), "--q0s must align with --cls"
    lv = set(float(v) for v in a.levels_at.split(",") if v)
    rm = set(float(v) for v in a.rm20_at.split(",") if v)
    start = a.start.rstrip("/")
    res0 = json.load(open(os.path.join(start, "result.json")))
    cfg = dict(res0["cfg"])
    cfg["cl"] = float(res0["cl"]); cfg["free_cl"] = False
    if a.merge_tol is not None:
        cfg["merge_tol"] = a.merge_tol
    cfg["nR_ball"] = cfg["nR_shell"] = cfg["nR_ext"] = cfg["nmu"] = 0
    base_branch = (res0.get("branch") or "") + "_chain"
    prev_id = os.path.basename(start); prev_state = os.path.join(start, "final.pt")
    state = dict(tag=a.tag, start=start, steps=[], levels=[])
    if os.path.exists(st_path):
        state = json.load(open(st_path))
    log(f"chain {a.tag} from {prev_id} (c_l {cfg['cl']:.4f}) through {cls}; levels at {sorted(lv)}; Rm20 at {sorted(rm)}; prio {a.priority}")
    level_jobs = []
    for step, cl in enumerate(cls):
        jid = f"{a.tag}_cl{cl_tag(cl)}" + (f"_q{cl_tag(q0s[step])}" if q0s else "")
        c = dict(cfg); c["cl"] = cl
        if q0s:
            c["q0_pin"] = q0s[step]
        if write_job(jid, c, prev_state, a.priority, a.iters, ["chain", a.tag, "from:" + prev_id], prev_id, base_branch,
                     f"small-step c_l chain {a.tag}: {prev_id} -> c_l {cl}"):
            log(f"queued {jid} from {prev_id}")
        else:
            log(f"{jid} exists (resume)")
        while status(jid) == "pending":
            time.sleep(a.poll)
        s = status(jid)
        if s != "done":
            log(f"{jid} {s}: chain stops"); break
        r = json.load(open(os.path.join(RUNS, jid, "result.json"))); v = r.get("validation") or {}
        log(f"{jid} done: cost {r.get('cost'):.3e} rho_max {v.get('rho_max')} s_core {v.get('s_core')} it {r.get('n_iter')} elapsed {r.get('elapsed_s', 0):.0f}s")
        state["steps"].append(dict(job=jid, cl=cl, cost=r.get("cost"), rho_max=v.get("rho_max"), s_core=v.get("s_core")))
        json.dump(state, open(st_path, "w"), indent=1)
        if cl in lv:
            # level 0: D24/n12/K16 (down-projection); level 2: D48/n32/K32 (refinement); both from this converged D36 state
            c0 = dict(c); c0["D"] = 24; c0["nmax"] = 12; c0["shells"] = [[sh[0], 16] for sh in c["shells"]]
            c2 = dict(c); c2["D"] = 48; c2["nmax"] = 32; c2["shells"] = [[sh[0], 32] for sh in c["shells"]]
            for lab, cc in (("L0", c0), ("L2", c2)):
                lj = f"{a.tag}{lab}_cl{cl_tag(cl)}" + (f"_q{cl_tag(q0s[step])}" if q0s else "")
                if write_job(lj, cc, os.path.join(RUNS, jid, "final.pt"), a.priority + 1, a.iters_level, ["chain-level", lab, a.tag, "from:" + jid], jid,
                             base_branch + "_" + lab, f"failure-map level {lab} at c_l {cl} from {jid}"):
                    log(f"queued level job {lj}"); level_jobs.append(lj)
        if cl in rm:
            cr = dict(c); cr["shells"] = [[2 * sh[0], int(round(sh[1] * 4 / 3))] for sh in c["shells"]]
            lj = f"{a.tag}Rm20_cl{cl_tag(cl)}" + (f"_q{cl_tag(q0s[step])}" if q0s else "")
            if write_job(lj, cr, os.path.join(RUNS, jid, "final.pt"), a.priority + 1, a.iters_level, ["chain-rm20", a.tag, "from:" + jid], jid,
                         base_branch + "_Rm20", f"matching radius doubled at c_l {cl} from {jid}"):
                log(f"queued Rm20 job {lj}"); level_jobs.append(lj)
        prev_id, prev_state = jid, os.path.join(RUNS, jid, "final.pt")
    # wait for the level jobs and record them
    for lj in level_jobs:
        while status(lj) == "pending":
            time.sleep(a.poll)
        s = status(lj)
        if s == "done":
            r = json.load(open(os.path.join(RUNS, lj, "result.json"))); v = r.get("validation") or {}
            log(f"{lj} done: cost {r.get('cost'):.3e} rho_max {v.get('rho_max')} s_core {v.get('s_core')}")
            state["levels"].append(dict(job=lj, cl=r.get("cl"), cost=r.get("cost"), rho_max=v.get("rho_max"), s_core=v.get("s_core"), D=r["cfg"]["D"], shells=r["cfg"]["shells"]))
        else:
            log(f"{lj} {s}")
        json.dump(state, open(st_path, "w"), indent=1)
    log("chain driver finished")


if __name__ == "__main__":
    main()
