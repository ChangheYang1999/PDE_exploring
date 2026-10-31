#!/usr/bin/env python
"""Cap watcher v4.1 (lead IP W1-W10, IS amendment, IU C1-C8, IV C9, IY C10-C15, JE C16-C22; S3-14). One detached CPU process per job; enforces a whole-job cap and an absolute UTC
end on ONE worker process; never retries anything. Pure decision functions (kill_decision, launch_bind_check, nv_timeout, sleep_allowance, allowance, read_heartbeat_phase,
battery_note, argv_override_allowed, parse_stat, parse_nvidia, deadlines, classify) are covered by --selftest named checks; every record carries version 'cap_watcher_v4.1' and watcher_sha256 (C21).
Identity (W1, C4, C6, C10): bind only if argv == [python, ROOT/scripts/worker.py, ROOT/queue/running/<job>.json, ROOT/runs/<job>]; record pid, start ticks
(/proc/PID/stat field 22) and argv; every decision uses ONE fresh classification; SIGTERM and SIGKILL are sent only on a fresh 'alive_ok' immediately before the
signal. TERM: 'unreadable' is retried within the TERM allowance and never signalled. KILL (C20, C22): the phase and the clocks are read first, then ONE fresh classification with NO
retry allowance, then os.kill at once on 'alive_ok'; 'unreadable' or 'ownership_unverified' at KILL ends as 'ownership unverified; cap NOT enforced; manual action under S3-14 (b)' with no signal. 'ended' only when /proc/PID is absent, the ticks differ, or the state is Z
with the bound ticks.
Launch line (C9, C11): ROOT/logs/supervisor.log, 'launched <job> on GPU <g> pid <P>' matched token by token; in production an unreadable log, a missing launch line, an
unparsable launch pid or a pid mismatch REFUSES the binding (in smoke mode, --pid given, the launch line is recorded as not found).
Clocks and deadlines (W2, W3 amended, C1, C2, C13, C16, C17): every wait uses allowance() = the smaller of the monotonic and the wall-clock remainder (wall deadlines d_term, d_kill, d_end fixed at binding; a shortened grace also fixes kill_at_wall); the binding sleep is unfloored and bounded by abs_end and the bind_timeout remainder; start = btime + ticks/CLK_TCK; D_TERM = min(start + cap, abs_end) - (grace + poll + V + 10 s), V = 30 s + Q (Q = 15 s
nvidia-smi timeout); monotonic cutoffs M_TERM, M_KILL = M_TERM + grace, M_END = M_KILL + V fixed at binding; a wall-clock (time.time) test on abs_end in the main loop and in
every grace and verification iteration; no sleep longer than the remaining allowance (no floors); KILL at M_KILL (grace shortened to 5 s with 'cap incomplete' if the TERM
was late); the nvidia-smi timeout is min(Q, M_END - now) without a floor, and 'GPU release unverified (no time left)' when nothing is left (C12).
Termination proof (W4, C3): /proc gone or Z with the bound ticks, and nvidia-smi --query-compute-apps=pid with returncode 0, integer lines, pid absent; otherwise
unverified; smoke mode never yields 'termination verified'. Queue movement (W5): a vanished running entry is recorded, monitoring continues. Battery (W8 (b), C8, C14, C18, C19): one validated heartbeat reader (job_id and pid must match the bound job and pid, otherwise None with the reason recorded) is used for
last_phase, the TERM read and the KILL read; both raw phases are recorded; precedence: a known phase other than 'lm' at either observation -> 'battery incomplete; state not read'; otherwise
an unknown phase -> 'phase unknown; state not read unless the saved LM endpoint is verified by sha'; only 'lm' at both -> 'stopped in the LM phase'.
Robust paths (W6, C5, C15): inputs validated (cap, poll, grace, bind_timeout finite and positive; abs_end in the future; --no_nvidia and --argv_override only with --pid);
validation failures call finish() before the try; the body from the binding loop to the end is in one try/finally with a failure record; one /proc read per decision; max_retries
must be the int 0 (W7).
Usage: cap_watcher_v4_1.py --job JOB_ID --cap_seconds N --abs_end 2026-10-28T06:00:00Z [--poll 30] [--grace 120] [--root ROOT] [--heartbeat F] [--queue_dir D] [--record F]
       [--supervisor_log F] [--bind_timeout 600] [--pid P --no_nvidia --argv_override 'a|b|c|d' (smoke mode only)]      cap_watcher_v4_1.py --selftest"""
import sys, os, json, time, argparse, signal, datetime, math, subprocess, traceback, hashlib

CLK = os.sysconf("SC_CLK_TCK")
Q_NV = 15.0
V_VERIFY = 30.0 + Q_NV

def iso(t): return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def parse_utc(s): return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc).timestamp()

def btime(stat_text=None):
    txt = stat_text if stat_text is not None else open("/proc/stat").read()
    for line in txt.splitlines():
        if line.startswith("btime"): return float(line.split()[1])
    raise RuntimeError("btime not found")

def parse_stat(text):
    """/proc/PID/stat text -> (start_ticks, state) or ('unreadable', reason). Robust to spaces in comm (split after the last ')')."""
    try:
        k = text.rfind(")")
        if k < 0: return ("unreadable", "no comm")
        rest = text[k + 2:].split()
        if len(rest) < 20: return ("unreadable", "short read")
        return (int(rest[19]), rest[0])
    except Exception as e:
        return ("unreadable", repr(e))

def proc_stat(pid):
    """-> ('gone', None) | ('unreadable', reason) | ('ok', (ticks, state)). One read."""
    try:
        with open(f"/proc/{pid}/stat") as f:
            text = f.read()
    except (FileNotFoundError, ProcessLookupError):
        return ("gone", None)
    except OSError as e:
        return ("unreadable", repr(e))
    r = parse_stat(text)
    if r[0] == "unreadable": return r
    return ("ok", r)

def proc_argv(pid):
    try:
        with open(f"/proc/{pid}/cmdline", "rb") as f:
            raw = f.read()
        parts = raw.split(b"\0")
        if parts and parts[-1] == b"": parts = parts[:-1]
        return [p.decode(errors="replace") for p in parts]
    except OSError:
        return None

def classify(pid, ticks0, argv0):
    """Decision input (one stat read + one argv read): 'ended' | 'alive_ok' | 'ownership_unverified' | 'unreadable'."""
    st = proc_stat(pid)
    if st[0] == "gone": return ("ended", "process gone")
    if st[0] == "unreadable": return ("unreadable", st[1])
    ticks, state = st[1]
    if ticks != ticks0: return ("ended", f"start ticks differ ({ticks} != {ticks0}): pid reused")
    if state == "Z": return ("ended", "zombie with the bound ticks")
    av = proc_argv(pid)
    if av is None: return ("ownership_unverified", "argv unreadable while alive with the same ticks")
    if av != argv0: return ("ownership_unverified", "argv differs while alive with the same ticks")
    return ("alive_ok", state)

def parse_nvidia(returncode, stdout, pid):
    """-> True (pid listed) | False (clear) | None (unverified: nonzero exit or unparsable line)."""
    if returncode != 0: return None
    pids = []
    for line in stdout.splitlines():
        s = line.strip()
        if not s: continue
        if not s.isdigit(): return None
        pids.append(int(s))
    return int(pid) in pids

def nvidia_has(pid, timeout, rec, smoke_mode):
    if smoke_mode:
        rec["gpu_release"] = "GPU release not queried (smoke mode)"; return None
    if timeout <= 0:
        rec["gpu_release"] = "GPU release unverified (no time left)"; return None
    try:
        p = subprocess.run(["nvidia-smi", "--query-compute-apps=pid", "--format=csv,noheader"], capture_output=True, text=True, timeout=timeout)
        r = parse_nvidia(p.returncode, p.stdout, pid)
        if r is None: rec["gpu_release"] = f"GPU release unverified (nvidia-smi returncode {p.returncode} or unparsable output)"
        return r
    except subprocess.TimeoutExpired:
        rec["gpu_release"] = "GPU release unverified (nvidia-smi timeout)"; return None
    except Exception as e:
        rec["gpu_release"] = f"GPU release unverified ({e!r})"; return None

def expected_argv(root, job, python_exe):
    return [python_exe, os.path.join(root, "scripts", "worker.py"), os.path.join(root, "queue", "running", job + ".json"), os.path.join(root, "runs", job)]

def deadlines(start_epoch, cap, abs_end, grace, poll):
    d_term = min(start_epoch + cap, abs_end) - (grace + poll + V_VERIFY + 10.0)
    return d_term, d_term + grace, d_term + grace + V_VERIFY

def kill_decision(cls):
    """C10: 'kill' only on a fresh alive_ok; 'retry' on unreadable; 'stop' on ended; 'unverified' on ownership_unverified."""
    return {"alive_ok": "kill", "unreadable": "retry", "ended": "stop", "ownership_unverified": "unverified"}.get(cls, "unverified")

def launch_bind_check(smoke_mode, log_readable, launch_line, launch_pid, cand_pid):
    """C9/C11: -> (ok, reason). Production: refuse when the log is unreadable, the launch line is missing, its pid does not parse, or mismatches."""
    if smoke_mode:
        return (True, "smoke mode: launch line not required")
    if not log_readable: return (False, "supervisor log unreadable")
    if launch_line is None: return (False, "launch line missing")
    if launch_pid is None: return (False, "launch-line pid does not parse")
    if int(launch_pid) != int(cand_pid): return (False, f"launch-line pid mismatch ({launch_pid} != {cand_pid})")
    return (True, "launch line matches")

def nv_timeout(remaining):
    """C12: the nvidia-smi timeout is min(Q_NV, remaining) with no floor; None when nothing is left."""
    r = min(Q_NV, remaining)
    return r if r > 0 else None

def sleep_allowance(want, remaining):
    """C13: never sleep longer than the remaining allowance; 0 when nothing is left."""
    return max(0.0, min(want, remaining))

def allowance(mono_deadline, wall_deadline, mono_now, wall_now):
    """C17: the smaller of the monotonic and the wall-clock remainder; never negative."""
    return max(0.0, min(mono_deadline - mono_now, wall_deadline - wall_now))

def parse_heartbeat(text, job, pid):
    """C18: -> (phase, reason). phase only when job_id == job and pid == pid; else None with the reason."""
    try:
        hb = json.loads(text)
    except Exception as e:
        return (None, f"unreadable: {e!r}")
    if not isinstance(hb, dict): return (None, "unreadable: not an object")
    if hb.get("job_id") != job: return (None, f"job mismatch ({hb.get('job_id')!r})")
    try:
        if int(hb.get("pid")) != int(pid): return (None, f"pid mismatch ({hb.get('pid')!r} != {pid})")
    except Exception:
        return (None, f"pid mismatch ({hb.get('pid')!r} unparsable)")
    return (hb.get("phase"), "ok")

def read_heartbeat_phase(path, job, pid):
    try:
        with open(path) as f: text = f.read()
    except OSError as e:
        return (None, f"unreadable: {e!r}")
    return parse_heartbeat(text, job, pid)

def battery_note(phase_term, phase_kill, killed):
    """C8/C14/C19: a known non-LM phase at either observation dominates; then unknown; only lm at both -> LM."""
    phases = [phase_term] + ([phase_kill] if killed else [])
    if any((p is not None and p != "lm") for p in phases): return "battery incomplete; state not read"
    if any(p is None for p in phases): return "phase unknown; state not read unless the saved LM endpoint is verified by sha"
    return "stopped in the LM phase"

def argv_override_allowed(smoke_mode, override):
    """C15: --argv_override only in smoke mode."""
    return override is None or smoke_mode

NAMED_CHECKS = [0]
def selftest():
    ok = True
    def chk(name, cond):
        nonlocal ok; ok = ok and bool(cond); NAMED_CHECKS[0] += 1; print(("PASS " if cond else "FAIL ") + name)
    chk("parse_stat normal", parse_stat("1 (python) S 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 216673186 0 0 0") == (216673186, "S"))
    chk("parse_stat comm with spaces", parse_stat("1 (my proc (x)) R 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 42 0 0") == (42, "R"))
    chk("parse_stat zombie", parse_stat("1 (python) Z 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 216673186 0 0 0")[1] == "Z")
    chk("parse_stat short read", parse_stat("1 (python) S 0 0 0")[0] == "unreadable")
    chk("parse_nvidia clear", parse_nvidia(0, "123\n456\n", 999) is False)
    chk("parse_nvidia listed", parse_nvidia(0, "123\n999\n", 999) is True)
    chk("parse_nvidia nonzero exit empty", parse_nvidia(9, "", 999) is None)
    chk("parse_nvidia unparsable", parse_nvidia(0, "No devices were found\n", 999) is None)
    d = deadlines(1000.0, 1000.0, 1e12, 120.0, 30.0); chk("deadlines D_TERM", abs(d[0] - (2000.0 - (120 + 30 + 45 + 10))) < 1e-9 and abs(d[1] - d[0] - 120.0) < 1e-9 and abs(d[2] - d[1] - 45.0) < 1e-9)
    d2 = deadlines(1000.0, 1e6, 1500.0, 120.0, 30.0); chk("deadlines abs_end binds", abs(d2[0] - (1500.0 - 205.0)) < 1e-9)
    st = proc_stat(os.getpid()); chk("proc_stat self ok", st[0] == "ok" and st[1][1] in ("R", "S"))
    chk("proc_stat gone", proc_stat(2**22 - 1)[0] in ("gone", "unreadable"))
    chk("classify self alive_ok", classify(os.getpid(), st[1][0], proc_argv(os.getpid()))[0] == "alive_ok")
    chk("classify ticks differ -> ended", classify(os.getpid(), st[1][0] + 1, proc_argv(os.getpid()))[0] == "ended")
    chk("classify argv differs -> ownership_unverified", classify(os.getpid(), st[1][0], ["x"])[0] == "ownership_unverified")
    chk("C10 kill_decision alive_ok -> kill", kill_decision("alive_ok") == "kill")
    chk("C10 kill_decision unreadable -> retry (never signalled)", kill_decision("unreadable") == "retry")
    chk("C10 kill_decision ended -> stop", kill_decision("ended") == "stop")
    chk("C10 kill_decision ownership_unverified -> unverified", kill_decision("ownership_unverified") == "unverified")
    chk("C11 production unreadable log refuses", launch_bind_check(False, False, None, None, 5)[0] is False)
    chk("C11 production missing launch line refuses", launch_bind_check(False, True, None, None, 5)[0] is False)
    chk("C11 production unparsable pid refuses", launch_bind_check(False, True, "launched j on GPU 1 pid x", None, 5)[0] is False)
    chk("C11 production pid mismatch refuses", launch_bind_check(False, True, "launched j on GPU 1 pid 7", 7, 5)[0] is False)
    chk("C11 production match binds", launch_bind_check(False, True, "launched j on GPU 1 pid 5", 5, 5)[0] is True)
    chk("C11 smoke mode binds without a launch line", launch_bind_check(True, False, None, None, 5)[0] is True)
    chk("C12 nv_timeout min(Q, remaining)", nv_timeout(100.0) == Q_NV and nv_timeout(3.0) == 3.0)
    chk("C12 nv_timeout none when nothing left", nv_timeout(0.0) is None and nv_timeout(-4.0) is None)
    chk("C13 sleep_allowance bounded", sleep_allowance(30.0, 7.5) == 7.5 and sleep_allowance(30.0, -1.0) == 0.0 and sleep_allowance(2.0, 100.0) == 2.0)
    chk("C14 battery_note both lm", battery_note("lm", "lm", True) == "stopped in the LM phase")
    chk("C14/C19 battery at KILL only -> battery incomplete", battery_note("lm", "battery", True) == "battery incomplete; state not read")
    chk("C14 battery_note None at TERM", battery_note(None, "lm", True).startswith("phase unknown"))
    chk("C14 battery_note TERM only when not killed", battery_note("lm", None, False) == "stopped in the LM phase")
    chk("C15 argv_override rejected outside smoke mode", argv_override_allowed(False, "a|b") is False and argv_override_allowed(True, "a|b") is True and argv_override_allowed(False, None) is True)
    chk("C17 allowance forward wall jump (wall remainder binds)", allowance(100.0, 1000.0, 50.0, 990.0) == 10.0)
    chk("C17 allowance backward wall jump (monotonic remainder binds)", allowance(100.0, 1000.0, 90.0, 500.0) == 10.0)
    chk("C17 allowance both zero or negative -> 0", allowance(100.0, 1000.0, 100.0, 1000.0) == 0.0 and allowance(100.0, 1000.0, 120.0, 1200.0) == 0.0)
    chk("C18 heartbeat matching", parse_heartbeat('{"job_id": "j", "pid": 5, "phase": "lm"}', "j", 5) == ("lm", "ok"))
    chk("C18 heartbeat job mismatch", parse_heartbeat('{"job_id": "k", "pid": 5, "phase": "lm"}', "j", 5)[0] is None and "job mismatch" in parse_heartbeat('{"job_id": "k", "pid": 5, "phase": "lm"}', "j", 5)[1])
    chk("C18 heartbeat pid mismatch", parse_heartbeat('{"job_id": "j", "pid": 6, "phase": "lm"}', "j", 5)[0] is None and "pid mismatch" in parse_heartbeat('{"job_id": "j", "pid": 6, "phase": "lm"}', "j", 5)[1])
    chk("C18 heartbeat unreadable", parse_heartbeat('not json', "j", 5)[0] is None and "unreadable" in parse_heartbeat('not json', "j", 5)[1])
    chk("C19 (None, diagnostics, killed) -> battery incomplete", battery_note(None, "diagnostics", True) == "battery incomplete; state not read")
    chk("C19 (diagnostics, None, killed) -> battery incomplete", battery_note("diagnostics", None, True) == "battery incomplete; state not read")
    chk("C19 (None, None, killed) -> unknown", battery_note(None, None, True).startswith("phase unknown"))
    chk("C19 (lm, None, killed) -> unknown", battery_note("lm", None, True).startswith("phase unknown"))
    chk("C19 (lm, None, not killed) -> LM", battery_note("lm", None, False) == "stopped in the LM phase")
    n = NAMED_CHECKS[0]
    print(f"SELFTEST {'PASS' if ok else 'FAIL'} ({n} named checks)"); return 0 if ok else 1

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--job"); ap.add_argument("--cap_seconds", type=float); ap.add_argument("--abs_end")
    ap.add_argument("--poll", type=float, default=30.0); ap.add_argument("--grace", type=float, default=120.0); ap.add_argument("--bind_timeout", type=float, default=600.0)
    ap.add_argument("--root", default=os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    ap.add_argument("--python", default=None, help="the supervisor's python executable (default ROOT/.venv/bin/python)")
    ap.add_argument("--heartbeat", default=None); ap.add_argument("--queue_dir", default=None); ap.add_argument("--record", default=None); ap.add_argument("--supervisor_log", default=None)
    ap.add_argument("--pid", type=int, default=None, help="smoke mode only"); ap.add_argument("--no_nvidia", action="store_true", help="smoke mode only (with --pid)")
    ap.add_argument("--argv_override", default=None, help="smoke mode only: the exact expected argv, '|'-separated")
    a = ap.parse_args()
    if a.selftest: sys.exit(selftest())
    root = a.root; hb_path = a.heartbeat or os.path.join(root, "status", f"heartbeat_{a.job}.json"); qdir = a.queue_dir or os.path.join(root, "queue")
    rec_path = a.record or os.path.join(root, "status", f"cap_watcher_{a.job}.json"); sup_log = a.supervisor_log or os.path.join(root, "logs", "supervisor.log")   # C9: the supervisor writes ROOT/logs/supervisor.log
    smoke_mode = a.pid is not None
    rec = dict(version="cap_watcher_v4.1", watcher_sha256=hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(), job=a.job, watcher_pid=os.getpid(), watcher_started_utc=iso(time.time()), cap_seconds=a.cap_seconds, abs_end=a.abs_end, poll=a.poll, grace=a.grace,
               V_verify_seconds=V_VERIFY, nvidia_timeout_seconds=Q_NV, smoke_mode=smoke_mode, events=[], final=False)
    def save():
        try:
            tmp = rec_path + ".tmp"; rec["updated_utc"] = iso(time.time())
            with open(tmp, "w") as f: json.dump(rec, f, indent=1, default=str, allow_nan=False)
            os.replace(tmp, rec_path)
        except Exception as e:
            print(f"{iso(time.time())} record write failed: {e!r}", file=sys.stderr, flush=True)
    def log(msg):
        rec["events"].append(f"{iso(time.time())} {msg}"); print(f"{iso(time.time())} {msg}", flush=True); save()
    def finish(status, **kw):
        rec.update(kw); rec["status"] = status; rec["final"] = True; rec["finished_utc"] = iso(time.time()); rec["finished_monotonic"] = time.monotonic(); save(); print(f"{iso(time.time())} FINAL {status}", flush=True)
    # ---- validation (W6) ----
    problems = []
    if not a.job: problems.append("job missing")
    for name, v in (("cap_seconds", a.cap_seconds), ("poll", a.poll), ("grace", a.grace), ("bind_timeout", a.bind_timeout)):
        if v is None or not (math.isfinite(v) and v > 0): problems.append(f"{name} must be finite and positive")
    try:
        abs_end = parse_utc(a.abs_end)
        if abs_end <= time.time(): problems.append("abs_end already past")
    except Exception:
        abs_end = None; problems.append("abs_end not parseable (YYYY-MM-DDThh:mm:ssZ)")
    if a.no_nvidia and not smoke_mode: problems.append("--no_nvidia is allowed only with --pid (smoke mode)")
    if not argv_override_allowed(smoke_mode, a.argv_override): problems.append("--argv_override is allowed only with --pid (smoke mode) (C15)")
    if problems:
        finish("rejected: " + "; ".join(problems)); sys.exit(2)
    exp_argv = a.argv_override.split("|") if a.argv_override else expected_argv(root, a.job, a.python or os.path.join(root, ".venv", "bin", "python"))
    rec["expected_argv"] = exp_argv
    pid = ticks0 = argv0 = None; start_epoch = None; mono = None; wall = None
    try:
        # ---- binding (W1, W2, W7, C6; the binding loop stops at abs_end and is bounded by bind_timeout) ----
        t_b0 = time.time()
        while time.time() < abs_end and time.time() - t_b0 < a.bind_timeout:
            hb = None
            try:
                with open(hb_path) as f: hb = json.load(f)
            except Exception:
                hb = None
            cand = a.pid if smoke_mode else (hb.get("pid") if (hb and hb.get("job_id") == a.job) else None)
            if cand is not None:
                st = proc_stat(cand); av = proc_argv(cand)
                if st[0] == "ok" and av is not None:
                    if av == exp_argv:
                        pid, ticks0, argv0 = int(cand), st[1][0], av; rec["heartbeat_at_bind"] = hb; break
                    finish("not bound: the candidate PID's argv is not the supervisor launch argv for this job (W1/C6); no action", candidate_pid=int(cand), candidate_argv=av); sys.exit(1)
            time.sleep(sleep_allowance(min(a.poll, 5.0), min(abs_end - time.time(), t_b0 + a.bind_timeout - time.time())))      # C16: unfloored, bounded by abs_end and the bind_timeout remainder
        if pid is None:
            finish("not bound: no live PID with the expected argv before abs_end or the binding timeout; no action"); sys.exit(1)
        mr = None; qjson = None
        for sub in ("running", "pending", "done", "failed"):
            p = os.path.join(qdir, sub, a.job + ".json")
            if os.path.exists(p):
                qjson = p
                with open(p) as f: mr = json.load(f).get("max_retries")
                break
        rec["queue_json"] = qjson; rec["max_retries"] = mr
        if not (type(mr) is int and mr == 0):
            finish(f"not bound: max_retries is {mr!r} (type {type(mr).__name__}); the int 0 is required (W7); no action", bound_pid=pid); sys.exit(1)
        start_epoch = btime() + ticks0 / CLK
        wall = time.time(); mono = time.monotonic()
        d_term, d_kill, d_end = deadlines(start_epoch, a.cap_seconds, abs_end, a.grace, a.poll)
        M_TERM = mono + (d_term - wall); M_KILL = M_TERM + a.grace; M_END = M_KILL + V_VERIFY
        # C9: the launch line 'launched <job> on GPU <g> pid <P>' (supervisor.py line 96), matched token by token; an unreadable log is recorded explicitly; a pid mismatch refuses the binding
        launch_line = None; launch_pid = None; launch_gpu = None
        try:
            with open(sup_log) as f:
                for line in f:
                    toks = line.split()
                    if len(toks) >= 7 and toks[1] == "launched" and toks[2] == a.job and toks[3] == "on" and toks[4] == "GPU" and toks[6] == "pid":
                        launch_line = line.strip()[:300]; launch_gpu = toks[5]
                        try: launch_pid = int(toks[7])
                        except Exception: launch_pid = None
        except OSError as e:
            rec["supervisor_log_unreadable"] = f"{sup_log}: {e!r}"
        rec["supervisor_log"] = sup_log; rec["launch_line_pid"] = launch_pid; rec["launch_line_gpu"] = launch_gpu; rec["supervisor_launch_line"] = launch_line
        log_readable = "supervisor_log_unreadable" not in rec
        if launch_line is None and log_readable:
            rec["supervisor_launch_line_note"] = "launch line not found in the supervisor log" + (" (smoke mode)" if smoke_mode else "")
        ok_l, why_l = launch_bind_check(smoke_mode, log_readable, launch_line, launch_pid, pid)
        rec["launch_bind_check"] = why_l
        if not ok_l:
            finish(f"not bound: {why_l} (C9/C11); no action", candidate_pid=pid); sys.exit(1)
        rec.update(bound_pid=pid, start_ticks=ticks0, argv=argv0, process_start_epoch=start_epoch, process_start_utc=iso(start_epoch), elapsed_at_bind_s=wall - start_epoch,
                   bind_wall_utc=iso(wall), D_TERM_utc=iso(d_term), D_KILL_utc=iso(d_kill), D_END_utc=iso(d_end), cap_utc=iso(start_epoch + a.cap_seconds), supervisor_launch_line=launch_line)
        if wall > d_term:
            rec["cap_incomplete"] = f"cap incomplete: bound after D_TERM by {wall - d_term:.0f} s"
        log(f"bound pid {pid} (ticks {ticks0}, process start {iso(start_epoch)}, elapsed {wall - start_epoch:.0f} s; cap {iso(start_epoch + a.cap_seconds)}, abs_end {a.abs_end}; D_TERM {iso(d_term)}, D_KILL {iso(d_kill)}, D_END {iso(d_end)}); max_retries 0 confirmed" + ("; " + rec["cap_incomplete"] if rec.get("cap_incomplete") else ""))
        def clocks():
            return dict(wall_utc=iso(time.time()), wall_epoch=time.time(), monotonic_since_bind=time.monotonic() - mono)
        def ending(status, **kw):
            tq = nv_timeout(allowance(M_END, d_end, time.monotonic(), time.time()))
            if tq is None:
                rec["gpu_release"] = "GPU release unverified (no time left)"; nv = None
            else:
                nv = nvidia_has(pid, tq, rec, smoke_mode)
            finish(status, nvidia_listed=nv, nvidia_clear=(nv is False), clocks_final=clocks(), **kw)
        # ---- main loop ----
        while True:
            tw = time.time(); tm = time.monotonic()
            cls, why = classify(pid, ticks0, argv0)
            if cls == "ended":
                ending(f"job process ended on its own ({why}); no action", occupied_seconds=tw - start_epoch, phase_at_exit=(rec.get("last_phase"))); break
            if cls == "ownership_unverified":
                ending("ownership unverified; process alive; cap NOT enforced; manual action under S3-14 (b)", reason=why, occupied_seconds=tw - start_epoch); break
            if cls == "unreadable":
                log(f"/proc read unreadable ({why}); retrying next poll")
            if not os.path.exists(os.path.join(qdir, "running", a.job + ".json")) and not rec.get("running_entry_vanished"):
                rec["running_entry_vanished"] = iso(tw); log("queue/running entry vanished while the bound process lives: NOT completion (W5); monitoring continues")
            rec["last_phase"], rec["last_phase_reason"] = read_heartbeat_phase(hb_path, a.job, pid)                              # C18: validated reader
            if tm >= M_TERM or tw >= d_term or tw >= abs_end - (a.grace + a.poll + V_VERIFY + 10.0):
                late = tm - M_TERM
                if late > a.poll and not rec.get("cap_incomplete"):
                    rec["cap_incomplete"] = f"cap incomplete: TERM deadline missed by {late:.0f} s (more than one poll)"; log(rec["cap_incomplete"])
                rec["phase_at_TERM"], rec["phase_at_TERM_reason"] = read_heartbeat_phase(hb_path, a.job, pid); rec["clocks_at_TERM"] = clocks(); rec["occupied_seconds_at_TERM"] = tw - start_epoch
                reason = "cap deadline" if (start_epoch + a.cap_seconds) <= abs_end else "absolute-end deadline"
                action = "none"; killed = False
                # TERM: only on a fresh alive_ok (C10); 'unreadable' is retried within the TERM allowance (up to M_KILL - 5 s), never signalled
                term_sent = False
                while True:
                    cls2, why2 = classify(pid, ticks0, argv0); dec = kill_decision(cls2)
                    if dec == "kill":
                        try:
                            os.kill(pid, signal.SIGTERM); action = "SIGTERM"; term_sent = True; log(f"{reason}: SIGTERM sent to pid {pid} ({iso(time.time())})")
                        except ProcessLookupError:
                            log("TERM: ProcessLookupError (gone)")
                        break
                    if dec == "stop": log(f"TERM withheld: process ended ({why2})"); break
                    if dec == "unverified": log(f"TERM withheld: {why2}"); break
                    remaining = allowance(M_KILL - 5.0, d_kill - 5.0, time.monotonic(), time.time())                       # C17
                    if remaining <= 0: log(f"TERM withheld: identity unreadable until the deadline ({why2})"); break
                    time.sleep(sleep_allowance(1.0, remaining))
                t_sent = time.monotonic(); t_sent_wall = time.time()
                kill_at = M_KILL; kill_at_wall = d_kill
                if term_sent and t_sent > M_KILL - 5.0:
                    kill_at = t_sent + 5.0; kill_at_wall = t_sent_wall + 5.0; rec["grace_shortened_to_s"] = kill_at - t_sent
                    if not rec.get("cap_incomplete"): rec["cap_incomplete"] = "cap incomplete: grace shortened"
                    log(f"grace shortened to {kill_at - t_sent:.0f} s; " + rec["cap_incomplete"])
                # grace loop (C13, C17: the smaller of the monotonic and wall-clock remainders; no floors)
                while allowance(kill_at, min(kill_at_wall, abs_end), time.monotonic(), time.time()) > 0:
                    c, _ = classify(pid, ticks0, argv0)
                    if c == "ended": break
                    time.sleep(sleep_allowance(1.0, allowance(kill_at, min(kill_at_wall, abs_end), time.monotonic(), time.time())))
                # KILL (C10, C14, C20, C22): read the phase and the clocks FIRST, then ONE fresh classification, then os.kill at once on alive_ok; no retry allowance at KILL
                final_unverified = None
                rec["phase_at_KILL"], rec["phase_at_KILL_reason"] = read_heartbeat_phase(hb_path, a.job, pid); rec["clocks_at_KILL"] = clocks()
                c, why3 = classify(pid, ticks0, argv0); dec = kill_decision(c)
                if dec == "kill":
                    try:
                        os.kill(pid, signal.SIGKILL); action = "SIGKILL"; killed = True
                    except ProcessLookupError:
                        dec = "stop"
                    if killed: log(f"KILL at D_KILL: SIGKILL sent to pid {pid} ({rec['clocks_at_KILL']['wall_utc']}; phase {rec['phase_at_KILL']})")
                    else: log("KILL: ProcessLookupError (gone)")
                elif dec != "stop":
                    final_unverified = f"ownership unverified; cap NOT enforced; manual action under S3-14 (b) ({why3})"; log("KILL withheld (no retry allowance at KILL): " + final_unverified)
                if final_unverified is not None and action == "none":
                    tq0 = nv_timeout(allowance(M_END, d_end, time.monotonic(), time.time()))
                    if tq0 is None: rec["gpu_release"] = "GPU release unverified (no time left)"; nv = None
                    else: nv = nvidia_has(pid, tq0, rec, smoke_mode)
                    finish(final_unverified, action="none", nvidia_listed=nv, nvidia_clear=(nv is False), clocks_final=clocks(), occupied_seconds_final=time.time() - start_epoch, phases=dict(at_TERM=rec.get("phase_at_TERM"), at_KILL=rec.get("phase_at_KILL"))); break
                # verification (W4, C1, C3, C12, C13, C17): /proc within the allowance (monotonic and wall), then ONE nvidia-smi query bounded by the time left (no floor)
                t_v0 = time.monotonic(); proc_gone = False
                while allowance(min(t_v0 + 30.0, M_END - Q_NV), d_end - Q_NV, time.monotonic(), time.time()) > 0:
                    c, _ = classify(pid, ticks0, argv0); proc_gone = (c == "ended")
                    if proc_gone: break
                    time.sleep(sleep_allowance(0.5, allowance(M_END - Q_NV, d_end - Q_NV, time.monotonic(), time.time())))
                if not proc_gone:
                    c, _ = classify(pid, ticks0, argv0); proc_gone = (c == "ended")
                tq = nv_timeout(allowance(M_END, d_end, time.monotonic(), time.time()))
                if tq is None:
                    rec["gpu_release"] = "GPU release unverified (no time left)"; nv = None
                else:
                    nv = nvidia_has(pid, tq, rec, smoke_mode)
                verify_s = time.monotonic() - t_v0
                verified = proc_gone and (nv is False)
                note = battery_note(rec.get("phase_at_TERM"), rec.get("phase_at_KILL"), killed)
                if final_unverified is not None:
                    note = final_unverified
                tw2 = time.time()
                status = ("stopped by the watcher: termination verified" if verified else
                          ("stopped by the watcher: process gone, GPU release not verified" if proc_gone else "stopped by the watcher: termination UNVERIFIED (process still present)"))
                if smoke_mode and proc_gone: status = "stopped by the watcher: process gone (smoke mode; GPU release not queried)"
                if final_unverified is not None and not proc_gone: status = final_unverified
                finish(status, action=action, proc_gone=proc_gone, nvidia_listed=nv, nvidia_clear=(nv is False), verification_seconds=verify_s, battery_note=note, phases=dict(at_TERM=rec.get("phase_at_TERM"), at_KILL=rec.get("phase_at_KILL")),
                       occupied_seconds_final=tw2 - start_epoch, within_cap=(tw2 <= start_epoch + a.cap_seconds), within_abs_end=(tw2 <= abs_end), clocks_final=clocks(), action_wall_utc=iso(tw2))
                break
            rec["occupied_seconds"] = tw - start_epoch; save()
            time.sleep(sleep_allowance(a.poll, allowance(M_TERM, min(d_term, abs_end), time.monotonic(), time.time())))        # C17
    except SystemExit:
        raise
    except Exception as e:
        finish("watcher exception: " + repr(e), traceback=traceback.format_exc()[-1500:])
    finally:
        if not rec.get("final"):
            finish("watcher exited without a final status (finally)")

if __name__ == "__main__":
    main()
