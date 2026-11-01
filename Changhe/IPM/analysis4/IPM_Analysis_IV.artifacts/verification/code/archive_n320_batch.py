"""Two sequential storage operations, with no more than one busy child."""
from pathlib import Path
import subprocess,sys
for tag,args in [
 ('selected_after320',['code/archive_selected_evidence.py']),
 ('N280_against315',['code/delta_archive_checkpoint.py','research/82_weighted_loss_criterion/update_N315_20261031T0742Z/verification/input_checkpoint.pkl.gz','research/78_factorial_product_losses/verification/input_checkpoint.pkl.gz','--remove-original','--decode-timeout','300'])]:
 with open('evidence_archives/'+tag+'.log','w') as out:
  p=subprocess.run([sys.executable,*args],stdout=out,stderr=subprocess.STDOUT,timeout=570)
  print(tag,p.returncode,flush=True)
  if p.returncode:raise SystemExit(p.returncode)
