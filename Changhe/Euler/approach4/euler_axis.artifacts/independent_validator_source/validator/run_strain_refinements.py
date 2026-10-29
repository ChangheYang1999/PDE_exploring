#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import contextlib,json,sys,time
import transported_strain_audit
ROOT=Path(__file__).resolve().parent
batch=sys.argv[1]
configs={
 'one':[('l1',129,.02,1e-4),('l1',257,.01,1e-4),('l2',65,.04,1e-4),('l2',129,.02,1e-4)],
 'two':[('l2',257,.01,1e-4),('l1',257,.01,2.5e-5),('l2',257,.01,2.5e-5)]
}[batch]
record=dict(started_utc=datetime.now(timezone.utc).isoformat(),batch=batch,configs=configs,completed=[])
manifest=ROOT/'results'/f'strain_refinement_batch_{batch}.json'
if manifest.exists():raise FileExistsError('Preserve previous batch')
manifest.write_text(json.dumps(record,indent=2)+'\n')
for level,n,dx,start in configs:
 name=f'strain_{level}_n{n}_h{int(round(1000*dx)):03d}_s{start:.1e}'
 candidate='T1_ladder_L1_20261028T232238Z' if level=='l1' else 'T1_ladder_L2_20261028T235434Z'
 sys.argv=['transported_strain_audit.py',str(ROOT/'external_exports'/candidate/'coeffs.npz'),'--output',str(ROOT/'results'/name),'--angular',str(n),'--dx',str(dx),'--start',str(start)]
 begin=time.perf_counter()
 with (ROOT/'results'/f'{name}.log').open('w') as log,contextlib.redirect_stdout(log):transported_strain_audit.main()
 result=json.loads((ROOT/'results'/name/'progress.json').read_text())
 row=dict(name=name,completed_utc=result['updated_utc'],wall_seconds=time.perf_counter()-begin,last_band=result['bands'][-1])
 record['completed'].append(row);manifest.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(row),flush=True)
record.update(completed_utc=datetime.now(timezone.utc).isoformat(),status='complete');manifest.write_text(json.dumps(record,indent=2)+'\n')
