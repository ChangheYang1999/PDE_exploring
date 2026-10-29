#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import json,subprocess,sys,time
from independent_artifacts import atomic_json,sha256
BASE=Path(__file__).resolve().parent;export=BASE/'external_exports/T1_ladder_L4rm5_20261029T024821.564842Z';out=BASE/'results/ladder_l4rm5_quick'
if out.exists():raise FileExistsError(out)
out.mkdir();start=time.perf_counter();record=dict(created_utc=datetime.now(timezone.utc).isoformat(),driver_sha256=sha256(__file__),runs=[])
for name,script,args in [('preflight','export_preflight.py',[str(export)]),('structure','piecewise_structure_audit.py',[str(export/'coeffs.npz')]),('interfaces','piecewise_interface_audit.py',[str(export/'coeffs.npz')]),('tail','coefficient_tail_audit.py',[str(export/'coeffs.npz')])]:
    cmd=[sys.executable,str(BASE/script),*args,'--output',str(out/(name+'.json'))];st=time.perf_counter()
    with(out/(name+'.log')).open('w')as log:result=subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT,timeout=60)
    record['runs'].append(dict(name=name,returncode=result.returncode,wall_seconds=time.perf_counter()-st))
    record.update(updated_utc=datetime.now(timezone.utc).isoformat(),wall_seconds=time.perf_counter()-start,phase=name)
    atomic_json(out/'driver.json',record)
    if result.returncode:raise RuntimeError(name)
record.update(phase='complete',completed_utc=datetime.now(timezone.utc).isoformat());atomic_json(out/'driver.json',record)
print(json.dumps(record,indent=2))
