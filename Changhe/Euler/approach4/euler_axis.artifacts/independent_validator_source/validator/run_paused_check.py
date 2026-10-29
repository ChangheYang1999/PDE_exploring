#!/usr/bin/env python3
"""Run one bounded local check while a verified own single process is stopped."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,os,signal,subprocess,sys,time
p=argparse.ArgumentParser();p.add_argument('pid',type=int);p.add_argument('record',type=Path);p.add_argument('command',nargs=argparse.REMAINDER);a=p.parse_args()
root=Path(__file__).resolve().parent.parent;proc=Path('/proc')/str(a.pid)
if not a.command or not a.record.resolve().is_relative_to(root):raise ValueError('invalid command or output')
if Path(os.readlink(proc/'cwd')).resolve()!=root:raise ValueError('worker outside this lane')
cmd=(proc/'cmdline').read_bytes().replace(b'\0',b' ').decode();allowed=['piecewise_pressure_audit.py','source_transport_audit.py','origin_pressure_audit.py','project_piecewise.py','two_series_data_audit.py','compare_ladder_geometry_pressure.py','piecewise_balance_audit.py']
if not any(s in cmd for s in allowed):raise ValueError('unexpected worker')
record=dict(started_utc=datetime.now(timezone.utc).isoformat(),paused_pid=a.pid,paused_command=cmd,check_command=a.command)
start=time.perf_counter();os.kill(a.pid,signal.SIGSTOP)
try:
 for _ in range(100):
  if 'T (stopped)' in (proc/'status').read_text():break
  time.sleep(.01)
 else:raise RuntimeError('worker did not stop')
 result=subprocess.run(a.command,timeout=300,check=False);record['returncode']=result.returncode
finally:
 os.kill(a.pid,signal.SIGCONT);record.update(resumed_utc=datetime.now(timezone.utc).isoformat(),pause_seconds=time.perf_counter()-start)
 a.record.write_text(json.dumps(record,indent=2)+'\n')
sys.exit(record.get('returncode',1))
