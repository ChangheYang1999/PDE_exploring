"""Guard one already-reviewed local host recount or exact matrix adapter."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, json, os, resource, shutil, signal, subprocess, sys, time
R = Path(__file__).resolve().parents[3]
P = argparse.ArgumentParser()
P.add_argument('--stage', choices=['recount', 'matrix'], required=True)
a = P.parse_args()
assert Path.cwd().resolve() == R
assert os.sched_getaffinity(0) == {50} and os.getpriority(os.PRIO_PROCESS, 0) >= 19
assert all(os.environ.get(k) == '1' for k in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'])
resource.setrlimit(resource.RLIMIT_AS, (28_000_000_000, 28_000_000_000))
def stamp(): return datetime.now(timezone.utc).isoformat()
def digest(p):
    h = sha256()
    with p.open('rb') as f:
        for block in iter(lambda: f.read(1048576), b''): h.update(block)
    return h.hexdigest()
def storage():
    total = 0
    for root, dirs, names in os.walk(R, followlinks=False):
        for name in names:
            p = Path(root) / name
            if not p.is_symlink(): total += p.stat().st_blocks * 512
    return {'lane_allocated_bytes': total, 'filesystem_free_bytes': shutil.disk_usage(R).free}
def allowed(s): return s['lane_allocated_bytes'] < 2_990_000_000 and s['filesystem_free_bytes'] >= 20_000_000_000
host = R.parent / 'numerics_agent_2/source_host_049/ordinary_v01/execution_v01.json'
e = json.loads(host.read_text())
assert e['status'] == 'COMPLETED' and e['exit_code'] == 0 and e['reason'] is None
assert e['complete_source_record'] and e['old_process_signals'] == 0 and not e['own_child_signals']
recount = R / 'research/ordinary_slabs_host_method/verification/recount_v01.json'
if a.stage == 'recount':
    V = R / 'research/ordinary_slabs_host_method/verification'
    program = 'research/ordinary_slabs_host_method/code/recount_v01.py'
    argv = [program, '--directory', 'numerics_agent_2/source_host_049/ordinary_v01', '--output', str(recount.relative_to(R))]
    output = recount
    limit = 900
else:
    V = R / 'research/ordinary_host_matrix_margin/verification'
    program = 'research/ordinary_host_matrix_margin/code/check_v01.py'
    assert json.loads(recount.read_text())['status'] == 'CONFIRMED_RECOUNT'
    output = V / 'check_v01.json'
    argv = [program, '--recount', str(recount.relative_to(R)), '--recount-sha256', digest(recount), '--output', str(output.relative_to(R))]
    limit = 600
receipt = V / 'execution_v01.json'
log = V / 'local_recount_v01.log'
startfile = V / 'local_recount_started_v01.json'
assert not any(p.exists() for p in [receipt, log, startfile, output])
stop = datetime.fromisoformat('2026-11-04T16:45:00+00:00')
assert datetime.now(timezone.utc) < stop
before = storage()
assert allowed(before)
bindings = {'../numerics_agent_2/source_host_049/ordinary_v01/execution_v01.json': digest(host), program: digest(R / program), str(Path(__file__).relative_to(R)): digest(Path(__file__))}
if a.stage == 'matrix': bindings[str(recount.relative_to(R))] = digest(recount)
started = stamp(); tick = time.monotonic(); samples = [dict(utc=started, **before)]; signals = []
with startfile.open('x') as f:
    json.dump(dict(stage=a.stage, started_utc=started, pid=os.getpid(), cpu=50, nice=19, threads=1, limit_seconds=limit, argv=argv, bindings=bindings), f, indent=2); f.write('\n')
reason = None
with log.open('xb') as f:
    child = subprocess.Popen([sys.executable, '-B', *argv], cwd=R, stdin=subprocess.DEVNULL, stdout=f, stderr=subprocess.STDOUT, start_new_session=True)
    next_check = time.monotonic() + 15
    while child.poll() is None:
        if time.monotonic() - tick >= limit: reason = 'time limit'
        if datetime.now(timezone.utc) >= stop: reason = 'campaign stop'
        if time.monotonic() >= next_check:
            state = storage(); samples.append(dict(utc=stamp(), **state)); next_check = time.monotonic() + 15
            if not allowed(state): reason = 'storage stop'
        if reason:
            os.killpg(child.pid, signal.SIGTERM); signals.append('SIGTERM')
            try: child.wait(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(child.pid, signal.SIGKILL); signals.append('SIGKILL'); child.wait()
            break
        time.sleep(1)
    code = child.wait()
raw = log.read_bytes()
redacted = raw.replace(str(R.parent).encode(), b'..')
if redacted != raw: log.write_bytes(redacted)
unchanged = all(digest(R / name) == value for name, value in bindings.items())
finished = stamp(); elapsed = time.monotonic() - tick
status = 'COMPLETED' if code == 0 and reason is None and unchanged and output.exists() else 'FAILED'
result = dict(status=status, stage=a.stage, started_utc=started, finished_utc=finished, elapsed_seconds=elapsed, limit_seconds=limit, stop_at=stop.isoformat(), cpu=50, nice=19, threads=1, memory_limit_bytes=28_000_000_000, argv=argv, exit_code=code, reason=reason, bindings=bindings, inputs_unchanged=unchanged, old_process_signals=0, own_child_signals=signals, resource_samples=samples, final_storage=storage(), log=str(log.relative_to(R)), log_sha256=digest(log), log_redacted=(redacted != raw), output=str(output.relative_to(R)), output_sha256=digest(output) if output.exists() else None, scope='Bounded local execution only. A distinct actual review and adoption are still required.')
with receipt.open('x') as f: json.dump(result, f, indent=2); f.write('\n')
print('LOCAL_HOST_RECOUNT', a.stage, status, elapsed, flush=True)
sys.exit(0 if status == 'COMPLETED' else 1)
