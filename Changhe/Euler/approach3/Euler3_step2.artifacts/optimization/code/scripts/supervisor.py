#!/usr/bin/env python
"""Campaign supervisor: persistent job queue (queue/pending -> running -> done|failed), one or more worker slots
per assigned GPU, bounded retries, RSS memory limit, heartbeat monitoring, logs, machine-readable status.
Runs detached (scripts/start_supervisor.sh). Stops on status/STOP_SUPERVISOR or at the campaign end time."""
import sys, os, json, time, shutil, subprocess, signal, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)
import psutil
from src.campaign import ledger
from src.campaign.checkpoint import atomic_write_text

Q = os.path.join(ROOT, "queue"); ST = os.path.join(ROOT, "status"); RUNS = os.path.join(ROOT, "runs"); LOGS = os.path.join(ROOT, "logs")
LEDGER = os.path.join(ST, "ledger.jsonl")
CFG_PATH = os.environ.get("D6_SUPERVISOR_CFG", os.path.join(ROOT, "configs", "supervisor_cpu.json"))     # D6FP 2026-10-29: CPU-only default after the GPU revocation; override with D6_SUPERVISOR_CFG
PY = os.environ.get("D6_PYTHON", "python3")   # D6FP: the frozen Euler3 interpreter (read only)
WORKER = os.path.join(ROOT, "scripts", "worker_d6.py")


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def load_cfg():
    cfg = dict(gpus=[5, 6], slots_per_gpu=1, rss_limit_GB=40.0, heartbeat_stale_s=1500, poll_s=20,
               campaign_start="2026-10-28T20:30:31Z", campaign_hours=46.75, default_max_retries=2, cpu_cores="31-34", nice=10)
    if os.path.exists(CFG_PATH):
        cfg.update(json.load(open(CFG_PATH)))
    return cfg


class Supervisor:
    def __init__(self):
        self.cfg = load_cfg()
        self.running = {}   # job_id -> dict(proc, gpu, started, jobfile, run_dir, job)
        for d in ["pending", "running", "done", "failed"]:
            os.makedirs(os.path.join(Q, d), exist_ok=True)
        os.makedirs(RUNS, exist_ok=True); os.makedirs(LOGS, exist_ok=True)
        self.logf = open(os.path.join(LOGS, "supervisor.log"), "a")
        self.stop = False
        signal.signal(signal.SIGTERM, self._term); signal.signal(signal.SIGINT, self._term)
        # recover jobs left in running/ by a previous supervisor: back to pending (they resume from checkpoints)
        for f in glob.glob(os.path.join(Q, "running", "*.json")):
            self.log(f"recovering orphaned running job {os.path.basename(f)} -> pending")
            shutil.move(f, os.path.join(Q, "pending", os.path.basename(f)))
        self.log(f"supervisor started pid {os.getpid()} cfg={json.dumps(self.cfg)}")

    def _term(self, *a):
        self.stop = True

    def log(self, msg):
        line = f"{now()} {msg}"
        self.logf.write(line + "\n"); self.logf.flush()

    def elapsed_hours(self):
        t0 = time.mktime(time.strptime(self.cfg["campaign_start"], "%Y-%m-%dT%H:%M:%SZ")) - time.timezone
        return (time.time() - t0) / 3600.0

    def stage(self):
        h = self.elapsed_hours()
        return "I" if h < 4 else ("II" if h < 36 else ("III" if h < 44 else ("IV" if h < 47 else "ended")))

    def refresh_gpus(self):
        """D6FP: re-read the GPU list (and slots) from configs/supervisor.json at every poll, so that GPUs handed over during the run
        (GPU_UPDATE.md) are used without a restart. Jobs already running keep their GPU."""
        try:
            c = json.load(open(CFG_PATH))
            if c.get("gpus") != self.cfg["gpus"]:
                self.log(f"GPU list changed: {self.cfg['gpus']} -> {c['gpus']}")
            self.cfg["gpus"] = [("cpu" if str(g) == "cpu" else int(g)) for g in c.get("gpus", self.cfg["gpus"])]
            self.cfg["slots_per_gpu"] = int(c.get("slots_per_gpu", self.cfg["slots_per_gpu"]))
            self.cfg["max_running"] = int(c.get("max_running", 0) or 0)
            for k in ("rss_limit_GB", "heartbeat_stale_s", "default_max_retries", "campaign_hours"):
                if k in c:
                    self.cfg[k] = c[k]
        except Exception as e:
            self.log(f"config re-read failed: {e!r}")

    def free_slots(self):
        slots = {g: self.cfg["slots_per_gpu"] for g in self.cfg["gpus"]}
        for r in self.running.values():
            if r["gpu"] in slots:
                slots[r["gpu"]] -= (self.cfg["slots_per_gpu"] if r["job"].get("exclusive") else 1)
        mr = int(self.cfg.get("max_running", 0) or 0)                 # D6FP: optional cap on concurrently running workers (CPU limit of the lane)
        if mr and len(self.running) >= mr:
            return []
        return [g for g, n in slots.items() for _ in range(max(n, 0))]

    def gpu_fully_free(self, gpu):
        return all(r["gpu"] != gpu for r in self.running.values())

    def pending_jobs(self):
        files = glob.glob(os.path.join(Q, "pending", "*.json"))
        jobs = []
        for f in files:
            try:
                j = json.load(open(f))
            except Exception:
                continue
            st = j.get("stage")
            jobs.append((-(j.get("priority", 0)), j.get("created", ""), f, j))
        jobs.sort(key=lambda t: (t[0], t[1]))
        return [(f, j) for (_, _, f, j) in jobs]

    def launch(self, jobfile, job, gpu):
        job_id = job["job_id"]
        run_dir = os.path.join(RUNS, job_id)
        os.makedirs(run_dir, exist_ok=True)
        dst = os.path.join(Q, "running", os.path.basename(jobfile))
        shutil.move(jobfile, dst)
        env = dict(os.environ)
        cpu_mode = (str(gpu) == "cpu")                                        # D6FP 2026-10-29: GPUs revoked (GPU_UPDATE.md 00:57:59Z); slots named "cpu" run the worker on CPU only
        nth = str(job["config"].get("threads", 1))
        env.update(CUDA_VISIBLE_DEVICES=("" if cpu_mode else str(gpu)), OMP_NUM_THREADS=nth, MKL_NUM_THREADS=(nth if cpu_mode else "1"), OPENBLAS_NUM_THREADS=(nth if cpu_mode else "1"),
                   PYTHONUNBUFFERED="1", PYTHONDONTWRITEBYTECODE="1")
        out = open(os.path.join(run_dir, "stdout.log"), "a")
        cmd = ["nice", "-n", str(self.cfg.get("nice", 10)), "taskset", "-c", str(self.cfg.get("cpu_cores", "31-34")), PY, WORKER, dst, run_dir]   # D6FP: lane cores, low priority
        proc = subprocess.Popen(cmd, env=env, stdout=out, stderr=subprocess.STDOUT, start_new_session=True, cwd=ROOT)
        self.running[job_id] = dict(proc=proc, gpu=gpu, started=time.time(), jobfile=dst, run_dir=run_dir, job=job, max_rss=0.0)
        self.log(f"launched {job_id} on GPU {gpu} pid {proc.pid} (retries so far {job.get('retries', 0)})")
        ledger.append(LEDGER, dict(kind="launch", job_id=job_id, gpu=gpu, pid=proc.pid, stage=self.stage(), elapsed_h=self.elapsed_hours(), label=job.get("label"), objective=job.get("objective")))

    def heartbeat_age(self, job_id):
        p = os.path.join(ST, f"heartbeat_{job_id}.json")
        if not os.path.exists(p):
            return None
        try:
            return time.time() - json.load(open(p)).get("epoch", 0)
        except Exception:
            return None

    def check_running(self):
        for job_id, r in list(self.running.items()):
            proc = r["proc"]
            rc = proc.poll()
            if rc is None:
                # memory and heartbeat
                try:
                    rss = sum(c.memory_info().rss for c in [psutil.Process(proc.pid)] + psutil.Process(proc.pid).children(recursive=True)) / 2**30
                    r["max_rss"] = max(r["max_rss"], rss)
                except psutil.Error:
                    rss = 0.0
                age = self.heartbeat_age(job_id)
                started_ago = time.time() - r["started"]
                if rss > self.cfg["rss_limit_GB"]:
                    self.log(f"{job_id}: RSS {rss:.1f} GB exceeds limit; killing"); self.kill(r, "rss_limit")
                elif started_ago > 600 and (age is None or age > self.cfg["heartbeat_stale_s"]):
                    self.log(f"{job_id}: stale heartbeat (age {age}); killing"); self.kill(r, "stale_heartbeat")
                continue
            # finished
            del self.running[job_id]
            job = r["job"]
            if rc == 0:
                shutil.move(r["jobfile"], os.path.join(Q, "done", os.path.basename(r["jobfile"])))
                self.log(f"{job_id} finished OK (max RSS {r['max_rss']:.1f} GB, {(time.time()-r['started'])/60:.1f} min)")
                ledger.append(LEDGER, dict(kind="job_done", job_id=job_id, minutes=(time.time() - r['started']) / 60, max_rss_GB=r["max_rss"]))
            else:
                self.requeue_or_fail(r, f"exit {rc}")

    def kill(self, r, reason):
        try:
            os.killpg(os.getpgid(r["proc"].pid), signal.SIGTERM)
            for _ in range(60):
                if r["proc"].poll() is not None:
                    break
                time.sleep(1)
            if r["proc"].poll() is None:
                os.killpg(os.getpgid(r["proc"].pid), signal.SIGKILL)
        except ProcessLookupError:
            pass
        self.running.pop(r["job"]["job_id"], None)
        self.requeue_or_fail(r, reason)

    def requeue_or_fail(self, r, reason):
        job = r["job"]; job_id = job["job_id"]
        job["retries"] = job.get("retries", 0) + 1
        job.setdefault("failures", []).append(dict(ts=now(), reason=reason))
        maxr = job.get("max_retries", self.cfg["default_max_retries"])
        if job["retries"] <= maxr and not self.stop:
            dst = os.path.join(Q, "pending", os.path.basename(r["jobfile"]))
            json.dump(job, open(r["jobfile"], "w"), indent=1); shutil.move(r["jobfile"], dst)
            self.log(f"{job_id}: {reason}; requeued (retry {job['retries']}/{maxr}); resumes from checkpoint")
            ledger.append(LEDGER, dict(kind="job_retry", job_id=job_id, reason=reason, retry=job["retries"]))
        else:
            dst = os.path.join(Q, ("pending" if self.stop else "failed"), os.path.basename(r["jobfile"]))
            json.dump(job, open(r["jobfile"], "w"), indent=1); shutil.move(r["jobfile"], dst)
            self.log(f"{job_id}: {reason}; {'kept pending (supervisor stopping)' if self.stop else 'FAILED permanently'}")
            if not self.stop:
                ledger.append(LEDGER, dict(kind="job_failed", job_id=job_id, reason=reason))

    def write_status(self):
        recs = ledger.read(LEDGER)
        results = [x for x in recs if x.get("kind") == "start_result"]
        board = ledger.leaderboard(recs, n=10)
        gpu = {}
        try:
            out = subprocess.run(["nvidia-smi", "--query-gpu=index,memory.used,utilization.gpu", "--format=csv,noheader,nounits"], capture_output=True, text=True, timeout=20).stdout
            for line in out.strip().splitlines():
                i, m, u = [t.strip() for t in line.split(",")]
                if int(i) in [g for g in self.cfg["gpus"] if g != "cpu"]:
                    gpu[int(i)] = dict(mem_MiB=int(m), util=int(u))
        except Exception:
            pass
        du = shutil.disk_usage(ROOT)
        try:
            lane_GB = int(subprocess.run(["du", "-sb", "--exclude=.venv", os.path.dirname(ROOT)], capture_output=True, text=True, timeout=60).stdout.split()[0]) / 2**30
        except Exception:
            lane_GB = None
        st = dict(ts=now(), supervisor_pid=os.getpid(), campaign_start=self.cfg["campaign_start"], elapsed_hours=round(self.elapsed_hours(), 3),
                  stage=self.stage(), running={k: dict(gpu=v["gpu"], pid=v["proc"].pid, minutes=round((time.time() - v["started"]) / 60, 1),
                                                       heartbeat_age_s=self.heartbeat_age(k), max_rss_GB=round(v["max_rss"], 2)) for k, v in self.running.items()},
                  labels={k: v["job"].get("label") for k, v in self.running.items()},
                  pending=len(glob.glob(os.path.join(Q, "pending", "*.json"))), done=len(glob.glob(os.path.join(Q, "done", "*.json"))),
                  failed=len(glob.glob(os.path.join(Q, "failed", "*.json"))), starts_completed=len(results),
                  best_rms=(board[0]["rms_final"] if board else None), leaderboard=[{k: b.get(k) for k in ["job_id", "start", "family", "c_l", "omega", "L", "Nk", "formulation", "rms_final", "rms_mom", "max_abs_Omega", "rotation_content_rel", "tail_nonaxi", "strain_at_max", "r_peak_Omega", "zfile"]} for b in board],
                  gpus=gpu, disk_free_GB=round(du.free / 2**30, 1), lane_usage_GB=(round(lane_GB, 2) if lane_GB is not None else None),
                  load_avg=os.getloadavg())
        atomic_write_text(json.dumps(st, indent=1), os.path.join(ST, "STATUS.json"))
        atomic_write_text(json.dumps(dict(ts=now(), epoch=time.time(), pid=os.getpid())), os.path.join(ST, "supervisor_heartbeat.json"))

    def loop(self):
        last_status = 0
        while True:
            self.refresh_gpus()
            if os.path.exists(os.path.join(ST, "STOP_SUPERVISOR")) or os.path.exists(os.path.join(os.path.dirname(ROOT), "STOP")):
                self.log("STOP_SUPERVISOR (or lane STOP) found"); self.stop = True
            if self.elapsed_hours() >= self.cfg["campaign_hours"] and not self.stop:
                self.log("campaign budget reached; stopping"); self.stop = True
            self.check_running()
            if self.stop:
                if self.running:
                    for r in list(self.running.values()):
                        self.log(f"stopping {r['job']['job_id']} (SIGTERM, it checkpoints)")
                        self.kill(r, "supervisor_stop")
                self.write_status(); self.log("supervisor exiting"); return
            def allowed(j, g):
                # a job may carry "gpus_allowed": [..] (lead d128 BV 2 (b), 2026-10-26): it is launched only on one of those GPUs
                ga = j.get("gpus_allowed")
                return (ga is None) or (int(g) in [int(x) for x in ga])
            while True:
                free = self.free_slots()          # recomputed after every launch (exclusive jobs take a whole GPU)
                if not free:
                    break
                pend = self.pending_jobs()
                if not pend:
                    break
                launched = False
                for gpu in free:
                    # highest-priority pending job allowed on this GPU; exclusive jobs need a fully free GPU, otherwise the first
                    # non-exclusive allowed job; a GPU with no launchable job is skipped so that restricted jobs never idle the others
                    cands = [(f, j) for (f, j) in pend if allowed(j, gpu)]
                    if not cands:
                        continue
                    jobfile, job = cands[0]
                    if job.get("exclusive") and not self.gpu_fully_free(gpu):
                        alt = [(f, j) for (f, j) in cands if not j.get("exclusive")]
                        if not alt:
                            continue
                        jobfile, job = alt[0]
                    self.launch(jobfile, job, gpu); launched = True
                    break                          # recompute the free slots after a launch
                if not launched:
                    break
            if time.time() - last_status > 60:
                self.write_status(); last_status = time.time()
            time.sleep(self.cfg["poll_s"])


if __name__ == "__main__":
    Supervisor().loop()
