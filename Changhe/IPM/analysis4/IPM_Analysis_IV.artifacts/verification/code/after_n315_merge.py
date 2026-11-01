"""CPU18 evidence preservation and finite mass partitions after successful N315 merge."""
from pathlib import Path
import os,subprocess,sys,time
while True:
 try:os.kill(3320142,0)
 except ProcessLookupError:break
 time.sleep(5)
assert 'n315_merge 0' in Path('logs/finish_n315.log').read_text()
steps=[('archive_N315_against320',['code/delta_archive_checkpoint.py','research/82_weighted_loss_criterion/update_N320_20261031T083718Z/verification/input_checkpoint.pkl.gz','research/82_weighted_loss_criterion/update_N315_20261031T0742Z/verification/input_checkpoint.pkl.gz','--remove-original','--decode-timeout','200']),('diagonal_bands_N320',['code/diagonal_mass_audit.py','research/64_log_precision_updates/verification/log_sin1_c3_p512_N320_20261031T084011Z','--orders','316,317,318,319,320'])]
for tag,args in steps:
 with open('logs/'+tag+'.jsonl','w') as out:
  result=subprocess.run([sys.executable,'-u',*args],stdout=out,stderr=subprocess.STDOUT,timeout=700)
 print(tag,result.returncode,flush=True)
 if result.returncode:raise SystemExit(result.returncode)
