"""Bounded one-core execution of the reviewed complete-background consumer."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import argparse, json, os, resource, shutil, signal, subprocess, sys, time
R = Path(__file__).resolve().parents[1]
D = R / 'research/background_complete_union'; V = D / 'verification'
p = argparse.ArgumentParser()
p.add_argument('--host-sha256', required=True); p.add_argument('--matrix-sha256', required=True)
a = p.parse_args()
assert Path.cwd().resolve() == R and os.sched_getaffinity(0) == {50} and os.getpriority(os.PRIO_PROCESS,0) >= 19
assert all(os.environ.get(k) == '1' for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'])
resource.setrlimit(resource.RLIMIT_AS, (28_000_000_000,28_000_000_000))
def now(): return datetime.now(timezone.utc).isoformat()
def h(p): return sha256(p.read_bytes()).hexdigest()
def storage():
    total = 0
    for root, dirs, names in os.walk(R, followlinks=False):
        for name in names:
            q=Path(root)/name
            if not q.is_symlink(): total += q.stat().st_blocks*512
    return dict(lane_allocated_bytes=total, filesystem_free_bytes=shutil.disk_usage(R).free)
def allowed(s): return s['lane_allocated_bytes'] < 2_990_000_000 and s['filesystem_free_bytes'] >= 20_000_000_000
host='research/ordinary_slabs_host_method/verification/actual_review_v01.json'
matrix='research/ordinary_host_matrix_margin/verification/actual_review_v01.json'
program='research/background_complete_union/code/check_v01.py'
method=V/'method_adoption_v01.json'
z=json.loads(method.read_text()); assert z['status']=='BOUND' and z['manifest_sha256']=='de2d1b15b1b62ab10943c9c78f9b6cc46b7baccb9b0a4b11086984de17eed36f'
assert h(R/host)==a.host_sha256 and h(R/matrix)==a.matrix_sha256
assert json.loads((R/host).read_text())['status']=='CONFIRMED_EXTERNAL_HOST_RECOUNT_REVIEW'
assert json.loads((R/matrix).read_text())['status']=='CONFIRMED_EXTERNAL_HOST_MATRIX_REVIEW'
output=V/'check_v01.json'; receipt=V/'execution_v01.json'; log=V/'execution_v01.log'; launch=V/'started_v01.json'
assert not any(q.exists() for q in [output,receipt,log,launch])
before=storage(); assert allowed(before)
assert datetime.now(timezone.utc)<datetime.fromisoformat('2026-11-04T16:40:00+00:00')
argv=[program,'--host-adoption',host,'--host-sha256',a.host_sha256,'--matrix-adoption',matrix,'--matrix-sha256',a.matrix_sha256,'--output',str(output.relative_to(R))]
files={n:h(R/n) for n in [program,host,matrix,str(method.relative_to(R)),str(Path(__file__).relative_to(R)),'research/background_complete_union/verification/manifest_v01.json']}
start=now(); tick=time.monotonic(); limit=300; reason=None; signals=[]
initial=dict(started_utc=start,pid=os.getpid(),cpu=50,nice=19,threads=1,limit_seconds=limit,argv=argv,bindings=files,initial_storage=before)
with launch.open('x')as f: json.dump(dict(status='RUNNING',**initial),f,indent=2);f.write('\n')
with log.open('xb')as f:
    child=subprocess.Popen([sys.executable,'-B',*argv],stdin=subprocess.DEVNULL,stdout=f,stderr=subprocess.STDOUT,start_new_session=True)
    next_check=time.monotonic()+15
    while child.poll() is None:
        if time.monotonic()-tick>=limit: reason='time limit'
        if time.monotonic()>=next_check:
            if not allowed(storage()): reason='storage limit'
            next_check=time.monotonic()+15
        if reason:
            os.killpg(child.pid,signal.SIGTERM);signals.append('SIGTERM')
            try: child.wait(timeout=5)
            except subprocess.TimeoutExpired: os.killpg(child.pid,signal.SIGKILL);signals.append('SIGKILL');child.wait()
            break
        time.sleep(.5)
    code=child.wait()
raw=log.read_bytes(); red=raw.replace(str(R.parent).encode(),b'..')
if red!=raw: log.write_bytes(red)
unchanged=all(h(R/n)==v for n,v in files.items()); final=storage()
status='COMPLETED' if code==0 and reason is None and unchanged and output.exists() and allowed(final) else 'FAILED'
result=dict(initial,status=status,finished_utc=now(),elapsed_seconds=time.monotonic()-tick,exit_code=code,reason=reason,inputs_unchanged=unchanged,old_process_signals=0,own_child_signals=signals,final_storage=final,output=str(output.relative_to(R)),output_sha256=h(output) if output.exists() else None,log=str(log.relative_to(R)),log_sha256=h(log),scope='Successful execution alone is not an independent actual union review.')
with receipt.open('x')as f: json.dump(result,f,indent=2);f.write('\n')
print('COMPLETE_BACKGROUND_EXECUTION',status,result['elapsed_seconds'],flush=True)
sys.exit(0 if status=='COMPLETED' else 1)
