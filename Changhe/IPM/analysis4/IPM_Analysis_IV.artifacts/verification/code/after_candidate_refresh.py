"""Sequential CPU18 queue after the selected Candidate007 nonlinear check."""
from pathlib import Path
from datetime import datetime,timezone
import os,subprocess,sys,time,json

while True:
 try:
  if Path("/proc/3516452/stat").read_text().split()[2] == "Z":break
 except FileNotFoundError:break
 time.sleep(5)
print(json.dumps(dict(started_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
 previous_log=Path('logs/candidate_refresh_continue.log').read_text())),flush=True)
for tag,args,timeout in [
 ('edge_top_radii',['code/edge_top_radii_check.py'],240),
 ('selected_archive',['code/archive_selected_evidence.py'],120),
 ('raw_archive',['code/archive_old_raw_evidence.py'],180),
 ('canonical_refresh',['code/canonical_refresh.py'],1900),
 ('edge_top_polynomial',['code/edge_top_polynomial_check.py'],240),
]:
 with open(f'logs/after_candidate_{tag}.log','w') as out:
  result=subprocess.run([sys.executable,'-u',*args],stdout=out,stderr=subprocess.STDOUT,timeout=timeout)
 print(json.dumps(dict(step=tag,returncode=result.returncode)),flush=True)
 if result.returncode:raise SystemExit(result.returncode)
