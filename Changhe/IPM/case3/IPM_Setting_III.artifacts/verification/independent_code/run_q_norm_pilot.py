"""Two sequential radial quadrature levels, with durable child results."""
import subprocess,sys,json
from pathlib import Path
from datetime import datetime,timezone
out=Path('runs/q_norm_pilot_results.json');rec=dict(started_utc=datetime.now(timezone.utc).isoformat(),rows=[])
for q in [6,10]:
 args=[sys.executable,'independent_code/audit_q_derivative_norms.py','evidence/q_canonical_high_jets/R1C_CL3P0_N64/exact_input.json','--tag','R1C_CL3P0_N64','--order',str(q),'--dps','80']
 log=Path(f'runs/derivative_norms_R1C_CL3P0_N64_q{q}.log')
 with log.open('w') as f:r=subprocess.run(args,stdout=f,stderr=subprocess.STDOUT,timeout=100)
 rec['rows'].append(dict(order=q,returncode=r.returncode,log=str(log),utc=datetime.now(timezone.utc).isoformat()));out.write_text(json.dumps(rec,indent=2)+'\n')
 if r.returncode:raise SystemExit(r.returncode)
print(json.dumps(rec),flush=True)
