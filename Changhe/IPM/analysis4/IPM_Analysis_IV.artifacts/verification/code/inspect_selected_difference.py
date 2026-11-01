from pathlib import Path
import gzip,json,pickle,time,sys
sys.path.insert(0,'code')
from read_checkpoint_archive import read_bytes
base=Path('research/82_weighted_loss_criterion/update_N329_20261031T093225Z/verification/input_checkpoint.pkl.gz')
s=pickle.loads(read_bytes(base))
for p in sorted(Path('research/64_log_precision_updates/verification').glob('log_sin1_c3_p512_N*/selected_packed_coefficients.json.gz')):
 n=int(p.parent.name.split('_N')[1].split('_')[0])
 if n>=300: continue
 o=json.loads(gzip.decompress(p.read_bytes()))
 done=False
 for fld in ['f','g']:
  for order,v in o[fld].items():
   if v!=s[fld][int(order)]:
    new=s[fld][int(order)]
    print(json.dumps({'N':n,'field':fld,'order':order,'old_type':type(v).__name__,'new_type':type(new).__name__,'old_sample':str(v)[:350],'new_sample':str(new)[:350]}),flush=True)
    done=True;break
  if done:break
 if not done:print(json.dumps({'N':n,'equal_as_objects':True}),flush=True)
