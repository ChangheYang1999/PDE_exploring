"""One CPU18 worker after the prior queue, including the completed edge3 data."""
from pathlib import Path
from datetime import datetime,timezone
import os,time,sys,subprocess,json
while True:
 try:
  if Path('/proc/3596677/stat').read_text().split()[2]=='Z':break
 except FileNotFoundError:break
 time.sleep(5)
print(json.dumps(dict(started_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'))),flush=True)
for tag,args,timeout in [
 ('canonical_plain',['code/canonical_post_audit.py'],60),
 ('top_asymptotic',['code/top_coefficient_asymptotic_check.py'],300),
 ('selected_recipes',['code/archive_selected_recipes.py'],480),
 ('edge3_arb',['code/edge_arb_audit.py','3','--max-order','300'],1000),
]:
 with open('logs/post_refresh_'+tag+'.log','w') as out:
  result=subprocess.run([sys.executable,'-u',*args],stdout=out,stderr=subprocess.STDOUT,timeout=timeout)
 print(json.dumps(dict(step=tag,returncode=result.returncode)),flush=True)
 if result.returncode:raise SystemExit(result.returncode)
roots=sorted(Path('research/102_edge_recurrence_reference/verification').glob('arb_edge3_*/checks.json'));p=roots[-1];assert json.loads(p.read_text())['maximum_order']==300
with open('logs/post_refresh_edge3_nonlinear.log','w') as out:
 result=subprocess.run([sys.executable,'-u','code/edge_nonlinear_audit.py',str(p.parent)],stdout=out,stderr=subprocess.STDOUT,timeout=2400)
print(json.dumps(dict(step='edge3_nonlinear',returncode=result.returncode)),flush=True)
