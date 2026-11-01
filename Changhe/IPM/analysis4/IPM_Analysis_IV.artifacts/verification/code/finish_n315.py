"""Sequential CPU18 continuation of the finite inequality and N315 audits."""
from pathlib import Path
import subprocess,sys
steps=[('finite_edge_gevrey',['code/finite_edge_gevrey_check.py']),
 ('n315_pairs253_314',['code/bivariate_chunk_audit.py','--n','315','--first','253','--last','314','--checkpoint','research/82_weighted_loss_criterion/update_N315_20261031T0742Z/verification/input_checkpoint.pkl.gz'])]
for tag,args in steps:
 with open('logs/'+tag+'.jsonl','w') as out:
  result=subprocess.run([sys.executable,'-u',*args],stdout=out,stderr=subprocess.STDOUT,timeout=1400)
 print(tag,result.returncode,flush=True)
 if result.returncode:raise SystemExit(result.returncode)
base=Path('research/84_bivariate_residual_audit/verification')
parts=[]
for first,last in [(1,63),(64,126),(127,189),(190,252),(253,314)]:
 candidates=sorted(base.glob(f'n315_pairs{first}_{last}_*/partial.pkl.gz'))
 assert len(candidates)==1,(first,last,candidates)
 parts.append(str(candidates[0]))
with open('logs/n315_merge.jsonl','w') as out:
 result=subprocess.run([sys.executable,'-u','code/bivariate_chunk_audit.py','--n','315','--checkpoint','research/82_weighted_loss_criterion/update_N315_20261031T0742Z/verification/input_checkpoint.pkl.gz','--merge',*parts],stdout=out,stderr=subprocess.STDOUT,timeout=500)
print('n315_merge',result.returncode,flush=True)
raise SystemExit(result.returncode)
