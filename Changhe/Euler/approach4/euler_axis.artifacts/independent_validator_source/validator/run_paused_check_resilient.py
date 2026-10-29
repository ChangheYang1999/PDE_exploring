#!/usr/bin/env python3
"""Bounded own-lane check; persist state and resume the paused job on SIGTERM."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,os,signal,subprocess,sys,time
p=argparse.ArgumentParser();p.add_argument('pid',type=int);p.add_argument('record',type=Path);p.add_argument('command',nargs=argparse.REMAINDER);a=p.parse_args()
root=Path(__file__).resolve().parent.parent;proc=Path('/proc')/str(a.pid)
if not a.command or not a.record.resolve().is_relative_to(root):raise ValueError('invalid command or output')
if a.record.exists():raise FileExistsError(a.record)
if Path(os.readlink(proc/'cwd')).resolve()!=root:raise ValueError('worker outside this lane')
cmd=(proc/'cmdline').read_bytes().replace(b'\0',b' ').decode()
allowed=['piecewise_pressure_audit.py','source_transport_audit.py','origin_pressure_audit.py','project_piecewise.py','two_series_data_audit.py','compare_ladder_geometry_pressure.py','piecewise_balance_audit.py','registered_native.py','piecewise_pressure_audit_native.py','piecewise_balance_audit_native.py','cartesian_piecewise_check.py','reduced_screen_candidate.py']
if not any(s in cmd for s in allowed):raise ValueError('unexpected worker')
if (proc/'stat').read_text().split()[2]=='T':raise RuntimeError('worker already paused')
record=dict(started_utc=datetime.now(timezone.utc).isoformat(),paused_pid=a.pid,paused_command=cmd,check_command=a.command)
def save():
 tmp=a.record.with_suffix('.tmp');tmp.write_text(json.dumps(record,indent=2)+'\n');tmp.replace(a.record)
def interrupted(signum,frame):raise InterruptedError(f'received signal {signum}')
for sig in [signal.SIGTERM,signal.SIGINT,signal.SIGHUP]:signal.signal(sig,interrupted)
start=time.perf_counter();child=None;paused=False
try:
 save();os.kill(a.pid,signal.SIGSTOP);paused=True
 for _ in range(100):
  if 'T (stopped)' in (proc/'status').read_text():break
  time.sleep(.01)
 else:raise RuntimeError('worker did not stop')
 child=subprocess.Popen(a.command);record['child_pid']=child.pid;save()
 record['returncode']=child.wait(timeout=300)
except BaseException as exc:
 record['exception']=repr(exc);record['returncode']=1
 if child is not None and child.poll() is None:
  child.terminate()
  try:child.wait(timeout=5)
  except subprocess.TimeoutExpired:child.kill();child.wait()
finally:
 if paused:
  try:os.kill(a.pid,signal.SIGCONT);record['resumed']=True
  except ProcessLookupError:record['resumed']=False
 record.update(resumed_utc=datetime.now(timezone.utc).isoformat(),pause_seconds=time.perf_counter()-start);save()
sys.exit(record.get('returncode',1))
