"""Durable campaign supervisor: persistent file queue, GPU slots, bounded retries, heartbeats, logs.

Usage: python3 supervisor/supervisor.py [--poll 15]
Layout (all under the campaign directory):
  queue/pending/<job_id>.json   jobs waiting (priority: lower number first, then file mtime)
  queue/running/<job_id>.json   job copies with pid, gpu, attempt, start time
  queue/done/, queue/failed/    terminal states (result in runs/<job_id>/result.json or error.json)
  supervisor/gpus.txt           comma-separated physical GPU ids usable (re-read every poll; GPU_UPDATE compliance); names cpu0, cpu1, ...
                                are CPU slots (CUDA_VISIBLE_DEVICES empty, --device cpu, OMP_NUM_THREADS = limits.omp_threads)
  supervisor/limits.json        {"max_workers": 5, "per_gpu": 1, "stale_heartbeat_s": 900}
  supervisor/STOP               if present: launch nothing new (running jobs continue); STOP_ALL also terminates workers
  supervisor/heartbeat.json, logs/supervisor.log
Workers are launched with setsid (own session), CUDA_VISIBLE_DEVICES=<one gpu>, OMP_NUM_THREADS=1, nice 19 inherited.
Exit codes: 0 -> done; 3 -> interrupted (requeue, resume from checkpoint); other -> retry up to max_retries then failed.
A dead pid without an exit record is treated as interrupted (requeue with resume).  The supervisor is idempotent:
on start it reconciles queue/running against live pids.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import shutil
import signal
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
PY = sys.executable
Q = os.path.join(ROOT, "queue")
RUNS = os.path.join(ROOT, "runs")
LOGS = os.path.join(ROOT, "logs")
for d in ("pending", "running", "done", "failed"):
    os.makedirs(os.path.join(Q, d), exist_ok=True)
os.makedirs(RUNS, exist_ok=True); os.makedirs(os.path.join(LOGS, "jobs"), exist_ok=True)


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def log(msg):
    line = f"{now()} {msg}"
    with open(os.path.join(LOGS, "supervisor.log"), "a") as f:
        f.write(line + "\n")
    print(line, flush=True)


def atomic_json(obj, path):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(obj, f, indent=1)
    os.replace(tmp, path)


def pid_alive(pid):
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    # zombie check
    try:
        with open(f"/proc/{pid}/stat") as f:
            if f.read().split(")")[-1].split()[0] == "Z":
                return False
    except Exception:
        return False
    return True


def read_limits():
    p = os.path.join(HERE, "limits.json")
    d = dict(max_workers=5, per_gpu=1, stale_heartbeat_s=900)
    if os.path.exists(p):
        try:
            d.update(json.load(open(p)))
        except Exception:
            pass
    return d


def read_gpus():
    p = os.path.join(HERE, "gpus.txt")
    if os.path.exists(p):
        s = open(p).read().strip()
        return [g.strip() for g in s.split(",") if g.strip() != ""]
    return [g for g in os.environ.get("CUDA_VISIBLE_DEVICES", "").split(",") if g != ""]


class Supervisor:
    def __init__(self, poll):
        self.poll = poll
        self.procs = {}          # job_id -> Popen (only for jobs launched by this process)
        self.stop = False
        signal.signal(signal.SIGTERM, self._sig)
        signal.signal(signal.SIGINT, self._sig)

    def _sig(self, *a):
        self.stop = True

    # ---------------------------------------------------------------- queue helpers
    def running_jobs(self):
        out = []
        for p in sorted(glob.glob(os.path.join(Q, "running", "*.json"))):
            try:
                out.append((p, json.load(open(p))))
            except Exception:
                continue
        return out

    def pending_jobs(self):
        items = []
        for p in glob.glob(os.path.join(Q, "pending", "*.json")):
            try:
                j = json.load(open(p))
            except Exception:
                continue
            items.append((j.get("priority", 100), os.path.getmtime(p), p, j))
        items.sort(key=lambda t: (t[0], t[1]))
        return items

    def finish(self, path, job, outcome, code):
        jid = job["job_id"]
        job["finished"] = now(); job["exit_code"] = code
        if outcome == "done":
            dst = os.path.join(Q, "done", f"{jid}.json")
        elif outcome == "failed":
            dst = os.path.join(Q, "failed", f"{jid}.json")
        else:   # requeue (interrupted or retry)
            job["attempt"] = int(job.get("attempt", 0)) + (1 if outcome == "retry" else 0)
            dst = os.path.join(Q, "pending", f"{jid}.json")
        atomic_json(job, dst)
        if os.path.exists(path):
            os.remove(path)
        self.procs.pop(jid, None)
        log(f"job {jid} -> {outcome} (exit {code}, attempt {job.get('attempt', 0)})")

    # ---------------------------------------------------------------- reconcile
    def reconcile(self, limits):
        for path, job in self.running_jobs():
            jid = job["job_id"]
            pid = job.get("pid")
            run_dir = os.path.join(RUNS, jid)
            proc = self.procs.get(jid)
            code = None
            if proc is not None:
                code = proc.poll()
                if code is None and not pid_alive(pid):
                    code = -1
            elif pid is None or not pid_alive(pid):
                # not our child: infer the outcome from files
                if os.path.exists(os.path.join(run_dir, "result.json")):
                    code = 0
                elif os.path.exists(os.path.join(run_dir, "error.json")) and \
                        os.path.getmtime(os.path.join(run_dir, "error.json")) > job.get("start_ts", 0):
                    code = 1
                else:
                    code = 3
            if code is None:
                # alive: check heartbeat staleness
                hb = os.path.join(run_dir, "heartbeat.json")
                age = time.time() - os.path.getmtime(hb) if os.path.exists(hb) else time.time() - job.get("start_ts", time.time())
                if age > limits["stale_heartbeat_s"]:
                    log(f"job {jid} heartbeat stale ({age:.0f}s): terminating pid {pid}")
                    try:
                        os.killpg(os.getpgid(pid), signal.SIGTERM)
                    except Exception:
                        try:
                            os.kill(pid, signal.SIGTERM)
                        except Exception:
                            pass
                    job["stale_kills"] = int(job.get("stale_kills", 0)) + 1
                    atomic_json(job, path)
                continue
            if code == 0 and os.path.exists(os.path.join(run_dir, "result.json")):
                self.finish(path, job, "done", code)
            elif code == 3 or code == -1 or (code == 0 and not os.path.exists(os.path.join(run_dir, "result.json"))):
                self.finish(path, job, "requeue", code)
            else:
                if int(job.get("attempt", 0)) + 1 <= int(job.get("max_retries", 2)):
                    self.finish(path, job, "retry", code)
                else:
                    self.finish(path, job, "failed", code)

    # ---------------------------------------------------------------- launch
    def launch(self, limits, gpus):
        if os.path.exists(os.path.join(HERE, "STOP")) or os.path.exists(os.path.join(HERE, "STOP_ALL")):
            return
        running = self.running_jobs()
        n_run = len(running)
        if n_run >= limits["max_workers"] or not gpus:
            return
        load = {g: 0 for g in gpus}
        for _, j in running:
            if j.get("gpu") in load:
                load[j["gpu"]] += 1
        for prio, mt, path, job in self.pending_jobs():
            if n_run >= limits["max_workers"]:
                break
            free = [g for g in gpus if load[g] < limits["per_gpu"]]
            if not free:
                break
            gpu = min(free, key=lambda g: load[g])
            jid = job["job_id"]
            run_dir = os.path.join(RUNS, jid)
            os.makedirs(run_dir, exist_ok=True)
            env = dict(os.environ)
            cpu_slot = str(gpu).startswith("cpu")          # GPU REVOKED 2026-10-29T00:57:59Z: slots named cpu0.. run on CPU with no GPU visible
            nthr = str(int(limits.get("omp_threads", 1))) if cpu_slot else "1"
            env["CUDA_VISIBLE_DEVICES"] = "" if cpu_slot else str(gpu)
            env["OMP_NUM_THREADS"] = nthr; env["MKL_NUM_THREADS"] = nthr; env["OPENBLAS_NUM_THREADS"] = nthr
            out = open(os.path.join(LOGS, "jobs", f"{jid}.out"), "a")
            try:
                proc = subprocess.Popen([PY, os.path.join(HERE, "worker.py"), path if False else os.path.join(run_dir, "job.json"),
                                         "--run-dir", run_dir] + (["--device", "cpu"] if cpu_slot else []),
                                        stdout=out, stderr=subprocess.STDOUT, env=env, start_new_session=True, cwd=ROOT,
                                        preexec_fn=None)
            except Exception as ex:
                log(f"launch failed for {jid}: {ex}")
                continue
            job["pid"] = proc.pid; job["gpu"] = gpu; job["start"] = now(); job["start_ts"] = time.time()
            job["attempt"] = int(job.get("attempt", 0))
            self.procs[jid] = proc
            atomic_json(job, os.path.join(Q, "running", f"{jid}.json"))
            os.remove(path)
            load[gpu] += 1; n_run += 1
            log(f"launched {jid} pid {proc.pid} gpu {gpu} attempt {job['attempt']} (prio {prio})")

    def stage_job_file(self):
        """Copy each pending job into runs/<id>/job.json before launch (worker reads it there)."""
        for prio, mt, path, job in self.pending_jobs():
            run_dir = os.path.join(RUNS, job["job_id"])
            os.makedirs(run_dir, exist_ok=True)
            dst = os.path.join(run_dir, "job.json")
            if not os.path.exists(dst) or os.path.getmtime(dst) < mt:
                shutil.copyfile(path, dst)

    def terminate_all(self):
        for path, job in self.running_jobs():
            pid = job.get("pid")
            if pid and pid_alive(pid):
                try:
                    os.killpg(os.getpgid(pid), signal.SIGTERM)
                except Exception:
                    try:
                        os.kill(pid, signal.SIGTERM)
                    except Exception:
                        pass
                log(f"STOP_ALL: SIGTERM to {job['job_id']} pid {pid}")

    def heartbeat(self, limits, gpus):
        running = self.running_jobs()
        atomic_json(dict(time=now(), pid=os.getpid(), running=[dict(job_id=j["job_id"], gpu=j.get("gpu"), pid=j.get("pid"), start=j.get("start")) for _, j in running],
                         n_pending=len(glob.glob(os.path.join(Q, "pending", "*.json"))), n_done=len(glob.glob(os.path.join(Q, "done", "*.json"))),
                         n_failed=len(glob.glob(os.path.join(Q, "failed", "*.json"))), gpus=gpus, limits=limits),
                    os.path.join(HERE, "heartbeat.json"))

    def run(self):
        log(f"supervisor start pid {os.getpid()} python {PY}")
        atomic_json(dict(pid=os.getpid(), start=now()), os.path.join(HERE, "supervisor.pid.json"))
        last_hb = 0
        while not self.stop:
            try:
                limits = read_limits(); gpus = read_gpus()
                self.reconcile(limits)
                if os.path.exists(os.path.join(HERE, "STOP_ALL")):
                    self.terminate_all()
                else:
                    self.stage_job_file()
                    self.launch(limits, gpus)
                if time.time() - last_hb > 30:
                    self.heartbeat(limits, gpus); last_hb = time.time()
            except Exception as ex:
                import traceback
                log("supervisor loop error: " + traceback.format_exc())
            time.sleep(self.poll)
        log("supervisor stopping (signal); workers keep running and will be reconciled by the next supervisor")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--poll", type=float, default=15.0)
    a = ap.parse_args()
    Supervisor(a.poll).run()
