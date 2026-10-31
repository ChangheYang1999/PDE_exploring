#!/usr/bin/env python
"""Cap watcher (lead d128 IF, condition S3-14): a detached CPU process bound to ONE job id and its owned worker PID. It enforces a whole-job
cap (setup + LM + battery, in occupied seconds since the job's first heartbeat or the given start epoch) and an absolute end time (UTC):
at either limit it sends SIGTERM to the owned PID (the worker checkpoints on SIGTERM), waits --grace seconds, then SIGKILL if still alive.
It never retries or relaunches anything. It records job id, owned PID, start epoch, cap, absolute end, the action taken and the occupied
GPU-seconds to status/cap_watcher_<job>.json (updated every poll; final record on exit). The PID is taken from status/heartbeat_<job>.json
(or --pid) and is verified against /proc/<pid>/cmdline, which must contain the job id; otherwise nothing is signalled.
Usage: cap_watcher.py --job JOB_ID --cap_seconds N --abs_end 2026-10-28T06:00:00Z [--pid P] [--poll 30] [--grace 120] [--dry_run]
Smoke (disposable): a fake heartbeat file and a sleeping process as the PID; see runs/stage3_smoke/capwatch_smoke_*.log."""
import sys, os, json, time, argparse, signal, datetime
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ap = argparse.ArgumentParser(); ap.add_argument("--job", required=True); ap.add_argument("--cap_seconds", type=float, required=True); ap.add_argument("--abs_end", required=True)
ap.add_argument("--pid", type=int, default=None); ap.add_argument("--poll", type=float, default=30.0); ap.add_argument("--grace", type=float, default=120.0)
ap.add_argument("--dry_run", action="store_true", help="log the decision but send no signal"); ap.add_argument("--heartbeat", default=None, help="heartbeat file (default status/heartbeat_<job>.json)")
ap.add_argument("--running_dir", default=os.path.join(ROOT, "queue", "running")); ap.add_argument("--record", default=None)
a = ap.parse_args()
hb_path = a.heartbeat or os.path.join(ROOT, "status", f"heartbeat_{a.job}.json")
rec_path = a.record or os.path.join(ROOT, "status", f"cap_watcher_{a.job}.json")
abs_end = datetime.datetime.strptime(a.abs_end, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc).timestamp()
def now(): return time.time()
def iso(t): return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def read_hb():
    try: return json.load(open(hb_path))
    except Exception: return None
def alive(pid):
    try: os.kill(pid, 0); return True
    except ProcessLookupError: return False
    except PermissionError: return True
def owns(pid):
    try: return a.job in open(f"/proc/{pid}/cmdline", "rb").read().replace(b"\0", b" ").decode(errors="replace")
    except Exception: return False
rec = dict(job=a.job, cap_seconds=a.cap_seconds, abs_end=a.abs_end, watcher_pid=os.getpid(), watcher_started=iso(now()), dry_run=a.dry_run, events=[])
def save(final=False):
    rec["updated"] = iso(now()); rec["final"] = final
    tmp = rec_path + ".tmp"; json.dump(rec, open(tmp, "w"), indent=1); os.replace(tmp, rec_path)
def log(msg):
    rec["events"].append(f"{iso(now())} {msg}"); print(f"{iso(now())} {msg}", flush=True)
# bind the PID and the start epoch
pid, start_epoch = a.pid, None
for _ in range(int(max(1, 600 / a.poll))):                      # wait up to 10 min for the first heartbeat
    hb = read_hb()
    if hb and hb.get("job_id") == a.job:
        pid = pid or hb.get("pid"); start_epoch = start_epoch or hb.get("epoch")
    if pid is not None and start_epoch is not None: break
    time.sleep(a.poll)
if pid is None or start_epoch is None:
    log("no heartbeat with a PID appeared within 10 min: nothing bound, exiting without action"); save(True); sys.exit(1)
if not owns(pid):
    log(f"PID {pid} cmdline does not contain the job id: NOT bound, exiting without action"); save(True); sys.exit(1)
rec.update(owned_pid=pid, start_epoch=start_epoch, start_utc=iso(start_epoch)); log(f"bound to PID {pid} (start {iso(start_epoch)}, cap {a.cap_seconds:.0f} s -> {iso(start_epoch + a.cap_seconds)}, absolute end {a.abs_end})"); save()
action = None
while True:
    t = now(); occupied = t - start_epoch
    running = os.path.exists(os.path.join(a.running_dir, a.job + ".json"))
    if not alive(pid) or not running:
        rec["occupied_seconds_at_exit"] = occupied; log(f"job ended on its own (pid alive {alive(pid)}, running entry {running}); occupied {occupied:.0f} s; no action"); save(True); break
    if occupied >= a.cap_seconds or t >= abs_end:
        reason = "whole-job cap reached" if occupied >= a.cap_seconds else "absolute end reached"
        rec["occupied_seconds_at_stop"] = occupied
        if a.dry_run:
            log(f"{reason}: DRY RUN, no signal sent (occupied {occupied:.0f} s)"); action = "dry_run"; save(True); break
        if not owns(pid):
            log(f"{reason} but PID {pid} no longer owned by the job: no signal"); save(True); break
        os.kill(pid, signal.SIGTERM); log(f"{reason}: SIGTERM sent to {pid} (occupied {occupied:.0f} s); grace {a.grace:.0f} s"); action = "SIGTERM"; save()
        t0 = now()
        while now() - t0 < a.grace and alive(pid): time.sleep(2)
        if alive(pid):
            os.kill(pid, signal.SIGKILL); log(f"SIGKILL sent to {pid} after the grace period"); action = "SIGKILL"
        rec["action"] = action; rec["occupied_seconds_final"] = now() - start_epoch; log("no retry: the watcher exits"); save(True); break
    rec["occupied_seconds"] = occupied; save(); time.sleep(a.poll)
