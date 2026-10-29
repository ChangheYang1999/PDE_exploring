from pathlib import Path
from datetime import datetime,timezone
import contextlib,json,sys,time
import transported_strain_audit
ROOT=Path(__file__).resolve().parent
out=ROOT/'results/strain_crosscheck_batch.json'
if out.exists():raise FileExistsError('Keep prior batch')
record=dict(started_utc=datetime.now(timezone.utc).isoformat(),purpose='Separate angular from radial-step refinement at fixed starting radius.',completed=[])
for level,directory in [('l1','T1_ladder_L1_20261028T232238Z'),('l2','T1_ladder_L2_20261028T235434Z')]:
 name='strain_'+level+'_n129_h010_s1.0e-04'
 sys.argv=['transported_strain_audit.py',str(ROOT/'external_exports'/directory/'coeffs.npz'),'--output',str(ROOT/'results'/name),'--angular','129','--dx','.01','--start','1e-4']
 start=time.perf_counter()
 with (ROOT/'results'/f'{name}.log').open('w') as log,contextlib.redirect_stdout(log):transported_strain_audit.main()
 result=json.loads((ROOT/'results'/name/'progress.json').read_text())
 row=dict(name=name,completed_utc=result['updated_utc'],wall_seconds=time.perf_counter()-start,last_band=result['bands'][-1]);record['completed'].append(row)
 out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(row),flush=True)
record.update(status='complete',completed_utc=datetime.now(timezone.utc).isoformat());out.write_text(json.dumps(record,indent=2)+'\n')
