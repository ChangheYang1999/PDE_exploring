#!/usr/bin/env python
"""Cap watcher v2 (lead d128 IP, requirements W1 to W10; S3-14). One detached CPU process per job; it enforces a whole-job cap and an absolute UTC end on
ONE worker process and never retries anything.
W1 identity: at binding the PID, its start ticks (field 22 of /proc/PID/stat) and its full argv are recorded; before EVERY signal the same pid, the same
   start ticks and exact argv equality are required; after binding no new PID is ever taken from the heartbeat or the command line.
W2 start clock: whole-job start = btime (/proc/stat) + start_ticks / CLK_TCK (the process start, covering imports and build); elapsed time after binding
   uses a monotonic clock, the absolute UTC end is a second guard; the supervisor-log launch line for the job is recorded beside it when found.
W3 deadlines: TERM at min(start + cap, abs_end) - (grace + poll + 10 s); KILL at TERM + grace; termination verification within the remaining margin; the
   binding loop also stops at abs_end.
W4 proof of termination: after KILL wait until /proc/PID is gone or its state is Z with the bound start ticks, AND until nvidia-smi --query-compute-apps
   lists no entry for the pid; both recorded; if either is not established within 30 s the record says "termination unverified".
W5 queue movement: a vanished queue/running entry while the bound process lives is NOT completion; monitoring continues.
W6 robust paths: nonfinite or nonpositive cap/poll/grace and a past abs_end are rejected; ProcessLookupError caught on every signal; main loop in
   try/finally writing a failure record; a failed record write is logged to stderr and the loop continues.
W7 no retry: at binding the job's queue JSON must have max_retries 0 (recorded; otherwise the watcher refuses to bind).
W8 battery choice (b): the worker is unchanged; the record states the heartbeat phase at TERM and at KILL; a stop in the battery reads 'battery incomplete;
   state not read'.
Usage: cap_watcher_v2.py --job JOB_ID --cap_seconds N --abs_end 2026-10-28T06:00:00Z [--poll 30] [--grace 120] [--heartbeat F] [--queue_dir D] [--record F]
       [--supervisor_log F] [--no_nvidia] [--pid P (smokes only: bind this pid instead of the heartbeat's)]"""
import sys, os, json, time, argparse, signal, datetime, math, subprocess, traceback
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ap = argparse.ArgumentParser()
ap.add_argument("--job", required=True); ap.add_argument("--cap_seconds", type=float, required=True); ap.add_argument("--abs_end", required=True)
ap.add_argument("--poll", type=float, default=30.0); ap.add_argument("--grace", type=float, default=120.0)
ap.add_argument("--heartbeat", default=None); ap.add_argument("--queue_dir", default=os.path.join(ROOT, "queue")); ap.add_argument("--record", default=None)
ap.add_argument("--supervisor_log", default=os.path.join(ROOT, "status", "supervisor.log")); ap.add_argument("--no_nvidia", action="store_true", help="smokes without a GPU process")
ap.add_argument("--pid", type=int, default=None, help="smokes only: bind this pid (the heartbeat's pid is still recorded)"); ap.add_argument("--bind_timeout", type=float, default=600.0)
a = ap.parse_args()
CLK = os.sysconf("SC_CLK_TCK")
def iso(t): return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def now(): return time.time()
rec_path = a.record or os.path.join(ROOT, "status", f"cap_watcher_{a.job}.json")
hb_path = a.heartbeat or os.path.join(ROOT, "status", f"heartbeat_{a.job}.json")
rec = dict(version="cap_watcher_v2", job=a.job, watcher_pid=os.getpid(), watcher_started=iso(now()), cap_seconds=a.cap_seconds, abs_end=a.abs_end, poll=a.poll, grace=a.grace, events=[], final=False)
def save():
    try:
        rec["updated"] = iso(now()); tmp = rec_path + ".tmp"; json.dump(rec, open(tmp, "w"), indent=1, default=str); os.replace(tmp, rec_path)
    except Exception as e:
        print(f"{iso(now())} record write failed: {e!r}", file=sys.stderr, flush=True)
def log(msg):
    rec["events"].append(f"{iso(now())} {msg}"); print(f"{iso(now())} {msg}", flush=True); save()
def finish(status, **kw):
    rec.update(kw); rec["status"] = status; rec["final"] = True; rec["finished"] = iso(now()); save(); log(f"FINAL {status}")
# W6 input validation
try:
    abs_end = datetime.datetime.strptime(a.abs_end, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc).timestamp()
except Exception:
    finish("rejected: abs_end not parseable"); sys.exit(2)
for name, v in (("cap_seconds", a.cap_seconds), ("poll", a.poll), ("grace", a.grace)):
    if not (math.isfinite(v) and v > 0):
        finish(f"rejected: {name} must be finite and positive"); sys.exit(2)
if abs_end <= now():
    finish("rejected: abs_end already past"); sys.exit(2)
def btime():
    for line in open("/proc/stat"):
        if line.startswith("btime"): return float(line.split()[1])
    raise RuntimeError("btime not found")
def proc_stat(pid):
    """(start_ticks, state) from /proc/PID/stat, robust to spaces in comm; None if the process is gone."""
    try:
        s = open(f"/proc/{pid}/stat").read()
    except FileNotFoundError:
        return None
    except ProcessLookupError:
        return None
    rest = s[s.rfind(")") + 2:].split()                 # fields from 3 on
    return int(rest[19]), rest[0]                         # field 22 = index 19 after the comm; field 3 = state
def proc_argv(pid):
    try:
        return open(f"/proc/{pid}/cmdline", "rb").read().split(b"\0")[:-1]
    except Exception:
        return None
def identity_ok(pid, ticks0, argv0):
    st = proc_stat(pid)
    if st is None: return False, "process gone"
    if st[0] != ticks0: return False, f"start ticks differ ({st[0]} != {ticks0})"
    av = proc_argv(pid)
    if av is None: return False, "argv unreadable"
    if av != argv0: return False, "argv differs"
    return True, st[1]
def heartbeat():
    try: return json.load(open(hb_path))
    except Exception: return None
def nvidia_has(pid):
    """True if nvidia-smi lists the pid, False if not, None if the query failed or timed out (Q_NV hard timeout; 'GPU release unverified')."""
    if a.no_nvidia: return False
    try:
        out = subprocess.run(["nvidia-smi", "--query-compute-apps=pid", "--format=csv,noheader"], capture_output=True, text=True, timeout=15.0).stdout
        return str(pid) in [l.strip() for l in out.splitlines()]
    except subprocess.TimeoutExpired:
        rec["nvidia_query_error"] = "timeout"; return None
    except Exception as e:
        rec["nvidia_query_error"] = repr(e); return None
def send(sig, pid, ticks0, argv0, label):
    ok, why = identity_ok(pid, ticks0, argv0)
    if not ok:
        log(f"{label}: identity check failed before the signal ({why}); NO signal sent"); return False
    try:
        os.kill(pid, sig); log(f"{label}: signal {sig} sent to pid {pid}"); return True
    except ProcessLookupError:
        log(f"{label}: ProcessLookupError (process gone); no signal"); return False
    except PermissionError as e:
        log(f"{label}: PermissionError {e!r}; no signal"); return False
# ----- binding (W1, W2, W7) -----
pid = ticks0 = argv0 = None; t_bind0 = now()
while now() < abs_end and now() - t_bind0 < a.bind_timeout:
    hb = heartbeat()
    cand = a.pid if a.pid is not None else (hb.get("pid") if hb and hb.get("job_id") == a.job else None)
    if cand is not None:
        st = proc_stat(cand); av = proc_argv(cand)
        if st is not None and av is not None:
            pid, ticks0, argv0 = int(cand), st[0], av; rec["heartbeat_at_bind"] = hb; break
    time.sleep(min(a.poll, 5.0))
if pid is None:
    finish("not bound: no live PID from the heartbeat before abs_end or the binding timeout; no action"); sys.exit(1)
argv_txt = [x.decode(errors="replace") for x in argv0]
def argv_names_job(av):                                                   # W1: an EXACT argv element (the job id itself or the job's JSON path), never a substring test
    return any(x == a.job or os.path.basename(x) == a.job + ".json" for x in av)
if not argv_names_job(argv_txt):
    finish("not bound: no argv element equals the job id or its JSON file name (exact match required, W1); no action", bound_pid=pid, argv=argv_txt); sys.exit(1)
# W7: max_retries 0 in the job's queue JSON
mr = None
for sub in ("running", "pending", "done", "failed"):
    p = os.path.join(a.queue_dir, sub, a.job + ".json")
    if os.path.exists(p):
        try: mr = json.load(open(p)).get("max_retries"); rec["queue_json"] = p
        except Exception as e: rec["queue_json_error"] = repr(e)
        break
rec["max_retries"] = mr
if mr != 0:
    finish(f"not bound: the job's queue JSON has max_retries {mr!r}, required 0 (W7); no action", bound_pid=pid); sys.exit(1)
start_epoch = btime() + ticks0 / CLK
mono0 = time.monotonic(); wall0 = now(); elapsed_at_bind = wall0 - start_epoch
launch_line = None
try:
    for line in open(a.supervisor_log):
        if a.job in line and ("launch" in line.lower() or "start" in line.lower()):
            launch_line = line.strip()[:300]
except Exception:
    pass
Q_NV = 15.0; V_VERIFY = 30.0 + Q_NV                                                  # lead amendment to W3/W4: V = 30 s /proc check + Q (nvidia-smi hard timeout 15 s)
t_term = min(start_epoch + a.cap_seconds, abs_end) - (a.grace + a.poll + V_VERIFY + 10.0)
rec.update(V_verify_seconds=V_VERIFY, nvidia_query_timeout_seconds=Q_NV)
if wall0 > t_term:
    rec["cap_incomplete"] = "cap incomplete: TERM deadline missed (bound after D_TERM)"; log(rec["cap_incomplete"])
rec.update(bound_pid=pid, start_ticks=ticks0, argv=argv_txt, process_start_epoch=start_epoch, process_start_utc=iso(start_epoch), elapsed_at_bind_s=elapsed_at_bind,
           supervisor_launch_line=launch_line, term_deadline_utc=iso(t_term), kill_deadline_utc=iso(t_term + a.grace), cap_utc=iso(start_epoch + a.cap_seconds))
log(f"bound pid {pid} (start ticks {ticks0}, process start {iso(start_epoch)}, elapsed {elapsed_at_bind:.0f} s at bind; cap at {iso(start_epoch + a.cap_seconds)}, abs_end {a.abs_end}; TERM deadline {iso(t_term)}, KILL {iso(t_term + a.grace)}); max_retries 0 confirmed")
if t_term <= wall0:
    log("the TERM deadline is already past at binding: acting now")
action = None
try:
    while True:
        t = wall0 + (time.monotonic() - mono0)                    # monotonic elapsed since binding, anchored at the bind wall time
        ok, state = identity_ok(pid, ticks0, argv0)
        if not ok:
            hbp = (heartbeat() or {}).get("phase")
            finish("job process ended on its own (identity check: %s); no action" % state, phase_at_exit=hbp, occupied_seconds=t - start_epoch); break
        if state == "Z":
            finish("process is a zombie (exited); no action", occupied_seconds=t - start_epoch); break
        running_entry = os.path.exists(os.path.join(a.queue_dir, "running", a.job + ".json"))
        if not running_entry and not rec.get("running_entry_vanished"):
            rec["running_entry_vanished"] = iso(t); log("queue/running entry vanished while the bound process lives: NOT completion (W5); monitoring continues")
        if t >= t_term:
            reason = "cap deadline" if (start_epoch + a.cap_seconds) <= abs_end else "absolute-end deadline"
            if t - t_term > a.poll and not rec.get("cap_incomplete"):
                rec["cap_incomplete"] = "cap incomplete: TERM deadline missed by %.0f s (more than one poll)" % (t - t_term); log(rec["cap_incomplete"])
            t_act0 = time.monotonic()
            hb = heartbeat() or {}; rec["phase_at_TERM"] = hb.get("phase"); rec["heartbeat_at_TERM"] = hb; rec["occupied_seconds_at_TERM"] = t - start_epoch
            sent = send(signal.SIGTERM, pid, ticks0, argv0, f"{reason}: TERM"); action = "SIGTERM" if sent else "none"
            t_kill = time.monotonic() + a.grace
            while time.monotonic() < t_kill and proc_stat(pid) is not None and proc_stat(pid)[1] != "Z": time.sleep(1.0)
            st = proc_stat(pid)
            if st is not None and st[1] != "Z":
                hb = heartbeat() or {}; rec["phase_at_KILL"] = hb.get("phase")
                if send(signal.SIGKILL, pid, ticks0, argv0, "grace elapsed: KILL"): action = "SIGKILL"
            # W4 proof of termination: /proc within 30 s, then ONE nvidia-smi query with a 15 s hard timeout (no retry beyond V)
            t_v0 = time.monotonic(); t_v = t_v0 + 30.0; proc_gone = False
            while time.monotonic() < t_v:
                st = proc_stat(pid); proc_gone = (st is None) or (st[1] == "Z")
                if proc_gone: break
                time.sleep(1.0)
            nvh = nvidia_has(pid); nv_clear = (nvh is False)
            if nvh is None: rec["gpu_release"] = "GPU release unverified (nvidia-smi query failed or timed out)"
            verify_s = time.monotonic() - t_v0; rec["verification_seconds"] = verify_s; rec["action_to_final_seconds"] = time.monotonic() - t_act0
            tt = wall0 + (time.monotonic() - mono0)
            verified = proc_gone and nv_clear
            battery_note = "battery incomplete; state not read" if (rec.get("phase_at_TERM") not in ("lm", None)) else None
            finish("stopped by the watcher: " + ("termination verified" if verified else "termination UNVERIFIED (report in NUM_REPORT)"), action=action, proc_gone=proc_gone, nvidia_clear=nv_clear,
                   action_wall_utc=iso(tt), occupied_seconds_final=tt - start_epoch, within_cap=(tt <= start_epoch + a.cap_seconds), within_abs_end=(tt <= abs_end), battery_note=battery_note)
            break
        rec["occupied_seconds"] = t - start_epoch; rec["last_phase"] = (heartbeat() or {}).get("phase"); save()
        time.sleep(a.poll)
except Exception as e:
    finish("watcher exception: " + repr(e), traceback=traceback.format_exc()[-1500:])
finally:
    if not rec.get("final"):
        finish("watcher exited without a final status (finally)")
