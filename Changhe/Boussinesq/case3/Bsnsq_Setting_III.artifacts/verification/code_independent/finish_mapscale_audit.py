"""One process for queued CPU work; no child Python process."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,runpy,sys,os,contextlib
root=Path(sys.argv[1]);start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'pid':os.getpid(),'status':'RUNNING','steps':[]}
for script in ['mapscale_grid_audit.py','regional_grid_summary.py','audit_native_tail_archive.py','certify_native_inverse_constants.py']:
 t=time.monotonic();sys.argv=[script,str(root)]
 with(root/('resume_'+script+'.log')).open('w') as f,contextlib.redirect_stdout(f),contextlib.redirect_stderr(f):
  runpy.run_path(str(Path('code_independent')/script),run_name='__main__')
 out['steps'].append({'script':script,'seconds':time.monotonic()-t,'status':'COMPLETE'})
 out['updated_utc']=datetime.now(timezone.utc).isoformat();(root/'job_summary.json').write_text(json.dumps(out,indent=2)+'\n');print(script,'COMPLETE',flush=True)
out.update(status='COMPLETE_WITH_RECOVERY',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);(root/'job_summary.json').write_text(json.dumps(out,indent=2)+'\n')
