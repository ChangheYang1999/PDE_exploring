#!/usr/bin/env python3
"""Supervised, resumable job runner (detached supervisor process).

Queue layout (directory based, atomic renames):
  queue/pending/<exp_id>.json   waiting (fields: exp_id, priority, config, [gpu])
  queue/running/<exp_id>.json   launched (worker resumes from runs/<exp_id>/ckpt_last.pt automatically)
  queue/done/, queue/failed/, queue/stopped/
STOP: create project/STOP -> workers checkpoint and exit (code 3), their queue entries return to pending,
the runner exits. RESUME = start the runner again (bin/launch.sh). A runner restart also requeues entries
left in running/ by a previous runner. Worker count is bounded (CPU guard: at most 10 python processes).
"""
import json, os, signal, subprocess, sys, time, glob, shutil

PROJECT = os.path.dirname(os.path.abspath(__file__))
Q = os.path.join(PROJECT, "queue")
RUNS = os.path.join(PROJECT, "runs")
STATUS = os.path.join(PROJECT, "runner_status.json")
PIDFILE = os.path.join(PROJECT, "runner.pid")
LOG = os.path.join(PROJECT, "runner.log")
RCFG = os.path.join(PROJECT, "runner_config.json")
LANE_GPU_FILE = os.path.join(os.path.dirname(PROJECT), "GPU")


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def log(*a):
    with open(LOG, "a") as f:
        f.write(now() + " " + " ".join(str(x) for x in a) + "\n")


def load_rcfg():
    d = {"max_workers": 6, "per_gpu": 3, "poll_seconds": 20, "max_retries": 2, "gpus": None}
    if os.path.exists(RCFG):
        d.update(json.load(open(RCFG)))
    if d["gpus"] is None:
        try:
            d["gpus"] = [g.strip() for g in open(LANE_GPU_FILE).read().strip().split(",") if g.strip()]
        except Exception:
            d["gpus"] = ["0"]
    return d


def atomic_json(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=1, default=str)
    os.replace(tmp, path)


def ledger_hours():
    try:
        sys.path.insert(0, PROJECT)
        from ledger import summarize
        return summarize()["active_hours_union"]
    except Exception as e:
        return None


def main():
    for d in ("pending", "running", "done", "failed", "stopped"):
        os.makedirs(os.path.join(Q, d), exist_ok=True)
    os.makedirs(RUNS, exist_ok=True)
    with open(PIDFILE, "w") as f:
        f.write(str(os.getpid()))
    log("runner start pid", os.getpid())
    # requeue entries left running by a previous runner
    for p in glob.glob(os.path.join(Q, "running", "*.json")):
        os.replace(p, os.path.join(Q, "pending", os.path.basename(p)))
        log("requeued", os.path.basename(p))
    children = {}  # exp_id -> dict(proc, gpu, path, started)
    stop_requested = {"flag": False}

    def on_term(*a):
        stop_requested["flag"] = True
    signal.signal(signal.SIGTERM, on_term)
    signal.signal(signal.SIGINT, on_term)

    while True:
        rc = load_rcfg()
        stop = stop_requested["flag"] or os.path.exists(os.path.join(PROJECT, "STOP"))
        # reap children
        for eid, ch in list(children.items()):
            ret = ch["proc"].poll()
            if ret is None:
                continue
            src = ch["path"]
            if ret == 0:
                dst = os.path.join(Q, "done", eid + ".json")
            elif ret == 3:
                held = os.path.exists(os.path.join(RUNS, eid, "STOP"))
                dst = os.path.join(Q, "stopped" if (stop or held) else "pending", eid + ".json")
            else:
                ent = json.load(open(src)); ent["retries"] = ent.get("retries", 0) + 1; ent["last_exit"] = ret
                json.dump(ent, open(src, "w"), indent=1)
                dst = os.path.join(Q, "pending" if ent["retries"] <= rc["max_retries"] else "failed", eid + ".json")
            os.replace(src, dst)
            log("exp", eid, "exit", ret, "->", os.path.basename(os.path.dirname(dst)))
            del children[eid]
        if stop:
            if children:
                for eid, ch in children.items():
                    if ch.get("signalled") is None:
                        ch["proc"].send_signal(signal.SIGTERM); ch["signalled"] = time.time(); log("SIGTERM ->", eid)
                    elif time.time() - ch["signalled"] > 900:
                        ch["proc"].kill(); log("SIGKILL ->", eid)
            else:
                log("runner exit (stop)")
                atomic_json(STATUS, {"runner": "stopped", "time": now(), "pid": os.getpid()})
                try:
                    os.remove(PIDFILE)
                except OSError:
                    pass
                return
        else:
            # launch
            pend = sorted(glob.glob(os.path.join(Q, "pending", "*.json")),
                          key=lambda p: (-json.load(open(p)).get("priority", 0), os.path.getmtime(p)))
            per_gpu = {g: 0 for g in rc["gpus"]}
            for ch in children.values():
                per_gpu[ch["gpu"]] = per_gpu.get(ch["gpu"], 0) + 1
            for p in pend:
                if len(children) >= rc["max_workers"]:
                    break
                ent = json.load(open(p))
                eid = ent["exp_id"]
                if os.path.exists(os.path.join(RUNS, eid, "STOP")):  # held experiment
                    os.replace(p, os.path.join(Q, "stopped", eid + ".json")); log("held", eid); continue
                want = str(ent.get("gpu")) if ent.get("gpu") is not None else None
                cands = [g for g in rc["gpus"] if per_gpu[g] < rc["per_gpu"] and (want is None or g == want)]
                if not cands:
                    continue
                gpu = min(cands, key=lambda g: per_gpu[g])
                dst = os.path.join(Q, "running", eid + ".json")
                os.replace(p, dst)
                rd = os.path.join(RUNS, eid); os.makedirs(rd, exist_ok=True)
                env = dict(os.environ); env["CUDA_VISIBLE_DEVICES"] = gpu; env["OMP_NUM_THREADS"] = "1"; env["PYTHONDONTWRITEBYTECODE"] = "1"
                out = open(os.path.join(rd, "worker.out"), "a")
                proc = subprocess.Popen(["nice", "-n", "19", sys.executable, os.path.join(PROJECT, "train.py"), "--exp", dst, "--device", "cuda:0"],
                                        cwd=PROJECT, env=env, stdout=out, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
                children[eid] = {"proc": proc, "gpu": gpu, "path": dst, "started": now()}
                per_gpu[gpu] += 1
                log("launched", eid, "pid", proc.pid, "gpu", gpu)
        # status
        running = []
        for eid, ch in children.items():
            st = {}
            sp = os.path.join(RUNS, eid, "status.json")
            if os.path.exists(sp):
                try:
                    st = json.load(open(sp))
                except Exception:
                    st = {}
            running.append({"exp_id": eid, "pid": ch["proc"].pid, "gpu": ch["gpu"], "started": ch["started"],
                            "stage": st.get("stage"), "step": st.get("global_step"), "active_h": round((st.get("active_seconds") or 0) / 3600, 3),
                            "best_val": st.get("best_val"), "cl": st.get("cl"), "last_val": st.get("last_val")})
        atomic_json(STATUS, {"runner": "stopping" if stop else "running", "pid": os.getpid(), "time": now(), "running": running,
                             "pending": sorted(os.path.basename(p)[:-5] for p in glob.glob(os.path.join(Q, "pending", "*.json"))),
                             "done": len(glob.glob(os.path.join(Q, "done", "*.json"))), "failed": len(glob.glob(os.path.join(Q, "failed", "*.json"))),
                             "ledger_active_hours_union": ledger_hours(), "config": rc})
        time.sleep(rc["poll_seconds"] if not stop else 5)


if __name__ == "__main__":
    main()
