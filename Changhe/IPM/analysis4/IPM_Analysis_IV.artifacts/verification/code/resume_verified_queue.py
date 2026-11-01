"""Sequential CPU18 recovery after the missing low-prefix input repair."""
from pathlib import Path
from datetime import datetime, timezone
import json, subprocess, sys, time
start=time.monotonic()
steps=[
 ('canonical_plain',['code/canonical_post_audit.py']),
 ('top_asymptotic',['code/top_coefficient_asymptotic_check.py']),
 ('selected_recipes',['code/archive_selected_recipes.py']),
 ('edge3_arb',['code/edge_arb_audit.py','3','--max-order','300']),
 ('edge_radius_approach',['code/edge_radius_approach_check.py']),
 ('edge_top_constant',['code/edge_top_constant_check.py']),
]
for tag,args in steps:
 print(json.dumps({'started_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'step':tag}),flush=True)
 with open('logs/recovered_'+tag+'.log','w') as out:
  r=subprocess.run([sys.executable,'-u',*args],stdout=out,stderr=subprocess.STDOUT)
 print(json.dumps({'step':tag,'returncode':r.returncode,'elapsed_s':time.monotonic()-start}),flush=True)
 if r.returncode:raise SystemExit(r.returncode)
roots=sorted(Path('research/102_edge_recurrence_reference/verification').glob('arb_edge3_*/checks.json'))
p=roots[-1];assert json.loads(p.read_text())['maximum_order']==300
with open('logs/recovered_edge3_nonlinear.log','w') as out:
 r=subprocess.run([sys.executable,'-u','code/edge_nonlinear_audit.py',str(p.parent)],stdout=out,stderr=subprocess.STDOUT)
print(json.dumps({'step':'edge3_nonlinear','returncode':r.returncode,'elapsed_s':time.monotonic()-start}),flush=True)
