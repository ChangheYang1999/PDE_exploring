#!/usr/bin/env python
"""Cap watcher v3 (lead IP W1-W10, the W3/W4 amendment, and lead IU defects C1-C8; S3-14). One detached CPU process per job; enforces a whole-job cap and an
absolute UTC end on ONE worker process; never retries anything. Functions are unit-testable (--selftest runs fixture tests: stat strings with other ticks or Z
state, a short read, nvidia-smi outputs that fail or do not parse).
Identity (W1, C4, C6): bind only if argv == [python, ROOT/scripts/worker.py, ROOT/queue/running/<job>.json, ROOT/runs/<job>] (the supervisor's launch argv,
exact absolute paths); record pid, start ticks (/proc/PID/stat field 22) and argv; before every signal and at every decision require the same pid, ticks and argv.
'ended' only when /proc/PID is absent, the ticks differ, or the state is Z with the bound ticks; same ticks + alive + argv unreadable/different =
'ownership unverified; process alive; cap NOT enforced; manual action under S3-14 (b)'. Start clock (W2, C2): btime + ticks/CLK_TCK; monotonic cutoffs
M_TERM, M_KILL = M_TERM + grace, M_END = M_KILL + V computed at binding AND a wall-clock (time.time) guard on both deadlines; both clocks recorded at TERM, KILL, final.
Deadlines (W3, C1): D_TERM = min(start + cap, abs_end) - (grace + poll + V + 10 s), V = 30 s + Q (Q = nvidia-smi timeout 15 s); KILL at M_KILL (if TERM later than
M_KILL - 5 s: KILL at TERM + 5 s, 'grace shortened', 'cap incomplete'); every wait and the nvidia-smi timeout bounded by the time left to M_END (floor 5 s; below it
'GPU release unverified (no time left)'). Termination proof (W4, C3): /proc gone or Z with the bound ticks, and nvidia-smi --query-compute-apps=pid with returncode 0
and every non-empty line an integer and no line == pid; otherwise None = 'GPU release unverified'; --no_nvidia only with --pid (smoke mode): 'GPU release not
queried (smoke mode)', nvidia_clear null, status never 'termination verified'. Queue movement (W5): a vanished running entry is recorded, monitoring continues.
Robust paths (W6, C5): the whole body after argument parsing in one try/finally; one proc_stat read per decision; proc_stat distinguishes gone / unreadable / ok;
inputs validated (cap, poll, grace, bind_timeout finite and positive; abs_end in the future); max_retries must be the int 0 (W7). Battery (W8 (b), C8): the heartbeat
phase at TERM and at KILL is recorded; phase None at TERM -> 'phase unknown at TERM; state not read unless the saved LM endpoint is verified by sha'; a battery phase ->
'battery incomplete; state not read'.
Usage: cap_watcher_v3.py --job JOB_ID --cap_seconds N --abs_end 2026-10-28T06:00:00Z [--poll 30] [--grace 120] [--root ROOT] [--heartbeat F] [--queue_dir D] [--record F]
       [--supervisor_log F] [--bind_timeout 600] [--pid P --no_nvidia (smoke mode) --argv_override 'a|b|c|d' (smoke mode: the exact argv expected)]
       cap_watcher_v3.py --selftest"""
import sys, os, json, time, argparse, signal, datetime, math, subprocess, traceback

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
    if timeout < 5.0:
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

def selftest():
    ok = True
    def chk(name, cond):
        nonlocal ok; ok = ok and bool(cond); print(("PASS " if cond else "FAIL ") + name)
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
    print("SELFTEST", "PASS" if ok else "FAIL"); return 0 if ok else 1

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
    rec = dict(version="cap_watcher_v3", job=a.job, watcher_pid=os.getpid(), watcher_started_utc=iso(time.time()), cap_seconds=a.cap_seconds, abs_end=a.abs_end, poll=a.poll, grace=a.grace,
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
            time.sleep(max(0.5, min(a.poll, 5.0, abs_end - time.time())))
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
        rec["supervisor_log"] = sup_log; rec["launch_line_pid"] = launch_pid; rec["launch_line_gpu"] = launch_gpu
        if launch_line is None and "supervisor_log_unreadable" not in rec:
            rec["supervisor_launch_line_note"] = "launch line not found in the supervisor log" + (" (smoke mode)" if smoke_mode else "")
        if launch_pid is not None and launch_pid != pid:
            finish(f"not bound: launch-line pid mismatch (supervisor log pid {launch_pid}, candidate pid {pid}); no action", candidate_pid=pid, supervisor_launch_line=launch_line); sys.exit(1)
        rec.update(bound_pid=pid, start_ticks=ticks0, argv=argv0, process_start_epoch=start_epoch, process_start_utc=iso(start_epoch), elapsed_at_bind_s=wall - start_epoch,
                   bind_wall_utc=iso(wall), D_TERM_utc=iso(d_term), D_KILL_utc=iso(d_kill), D_END_utc=iso(d_end), cap_utc=iso(start_epoch + a.cap_seconds), supervisor_launch_line=launch_line)
        if wall > d_term:
            rec["cap_incomplete"] = f"cap incomplete: bound after D_TERM by {wall - d_term:.0f} s"
        log(f"bound pid {pid} (ticks {ticks0}, process start {iso(start_epoch)}, elapsed {wall - start_epoch:.0f} s; cap {iso(start_epoch + a.cap_seconds)}, abs_end {a.abs_end}; D_TERM {iso(d_term)}, D_KILL {iso(d_kill)}, D_END {iso(d_end)}); max_retries 0 confirmed" + ("; " + rec["cap_incomplete"] if rec.get("cap_incomplete") else ""))
        def clocks():
            return dict(wall_utc=iso(time.time()), wall_epoch=time.time(), monotonic_since_bind=time.monotonic() - mono)
        def ending(status, **kw):
            nv = nvidia_has(pid, min(Q_NV, max(5.0, M_END - time.monotonic())), rec, smoke_mode)
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
            try:
                with open(hb_path) as f: rec["last_phase"] = json.load(f).get("phase")
            except Exception:
                rec["last_phase"] = None
            if tm >= M_TERM or tw >= d_term or tw >= abs_end - (a.grace + a.poll + V_VERIFY + 10.0):
                late = tm - M_TERM
                if late > a.poll and not rec.get("cap_incomplete"):
                    rec["cap_incomplete"] = f"cap incomplete: TERM deadline missed by {late:.0f} s (more than one poll)"; log(rec["cap_incomplete"])
                rec["phase_at_TERM"] = rec.get("last_phase"); rec["clocks_at_TERM"] = clocks(); rec["occupied_seconds_at_TERM"] = tw - start_epoch
                reason = "cap deadline" if (start_epoch + a.cap_seconds) <= abs_end else "absolute-end deadline"
                cls2, why2 = classify(pid, ticks0, argv0)
                action = "none"
                if cls2 == "alive_ok":
                    try:
                        os.kill(pid, signal.SIGTERM); action = "SIGTERM"; log(f"{reason}: SIGTERM sent to pid {pid} ({rec['clocks_at_TERM']['wall_utc']})")
                    except ProcessLookupError:
                        log("TERM: ProcessLookupError (gone)")
                else:
                    log(f"TERM withheld: identity {cls2} ({why2})")
                t_sent = time.monotonic()
                kill_at = M_KILL
                if t_sent > M_KILL - 5.0:
                    kill_at = t_sent + 5.0; rec["grace_shortened_to_s"] = kill_at - t_sent
                    if not rec.get("cap_incomplete"): rec["cap_incomplete"] = "cap incomplete: grace shortened"
                    log(f"grace shortened to {kill_at - t_sent:.0f} s; " + rec["cap_incomplete"])
                while time.monotonic() < kill_at:
                    c, _ = classify(pid, ticks0, argv0)
                    if c == "ended": break
                    time.sleep(min(1.0, max(0.1, kill_at - time.monotonic())))
                c, why3 = classify(pid, ticks0, argv0)
                if c != "ended":
                    rec["phase_at_KILL"] = rec.get("last_phase"); rec["clocks_at_KILL"] = clocks()
                    if c == "alive_ok" or c == "unreadable":
                        try:
                            os.kill(pid, signal.SIGKILL); action = "SIGKILL"; log(f"KILL at D_KILL: SIGKILL sent to pid {pid} ({rec['clocks_at_KILL']['wall_utc']})")
                        except ProcessLookupError:
                            log("KILL: ProcessLookupError (gone)")
                    else:
                        log(f"KILL withheld: identity {c} ({why3})")
                # ---- verification (W4, C1, C3): bounded by the time left to M_END ----
                t_v0 = time.monotonic(); proc_gone = False
                while time.monotonic() < min(t_v0 + 30.0, M_END - Q_NV):
                    c, _ = classify(pid, ticks0, argv0); proc_gone = (c == "ended")
                    if proc_gone: break
                    time.sleep(0.5)
                if not proc_gone:
                    c, _ = classify(pid, ticks0, argv0); proc_gone = (c == "ended")
                nv = nvidia_has(pid, min(Q_NV, max(5.0, M_END - time.monotonic())), rec, smoke_mode)
                verify_s = time.monotonic() - t_v0
                verified = proc_gone and (nv is False)
                phase_t = rec.get("phase_at_TERM")
                if phase_t is None: note = "phase unknown at TERM; state not read unless the saved LM endpoint is verified by sha"
                elif phase_t != "lm": note = "battery incomplete; state not read"
                else: note = "stopped in the LM phase"
                tw2 = time.time()
                status = ("stopped by the watcher: termination verified" if verified else
                          ("stopped by the watcher: process gone, GPU release not verified" if proc_gone else "stopped by the watcher: termination UNVERIFIED (process still present)"))
                if smoke_mode and proc_gone: status = "stopped by the watcher: process gone (smoke mode; GPU release not queried)"
                finish(status, action=action, proc_gone=proc_gone, nvidia_listed=nv, nvidia_clear=(nv is False), verification_seconds=verify_s, battery_note=note,
                       occupied_seconds_final=tw2 - start_epoch, within_cap=(tw2 <= start_epoch + a.cap_seconds), within_abs_end=(tw2 <= abs_end), clocks_final=clocks(), action_wall_utc=iso(tw2))
                break
            rec["occupied_seconds"] = tw - start_epoch; save()
            time.sleep(min(a.poll, max(0.2, M_TERM - time.monotonic()), max(0.2, abs_end - time.time())))
    except SystemExit:
        raise
    except Exception as e:
        finish("watcher exception: " + repr(e), traceback=traceback.format_exc()[-1500:])
    finally:
        if not rec.get("final"):
            finish("watcher exited without a final status (finally)")

if __name__ == "__main__":
    main()
