"""Freeze the actual saved canonical checkpoint, audit it, and archive its predecessor."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import gzip,json,pickle,shutil,subprocess,sys,time

start=time.monotonic();assert shutil.disk_usage('.').free>20*10**9
src=Path('../a4-num/ckpt/log_sin1_c3_p512.pkl')
raw=src.read_bytes();state=pickle.loads(raw)
assert (state['A'],state['B'],state['prec'],state['ring'])==('2','3',512,'arb')
N=max(state['f']);assert N>320;del state
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
root=Path('research/82_weighted_loss_criterion')/f'update_N{N}_{stamp}'
(root/'verification').mkdir(parents=True)
packed=gzip.compress(raw,compresslevel=1,mtime=0)
used=int(subprocess.run(['du','-s','-B1','.'],capture_output=True,text=True,check=True).stdout.split()[0])
assert used+len(packed)<2_985_000_000,('lane disk reserve',used,len(packed))
frozen=root/'verification/input_checkpoint.pkl.gz';frozen.write_bytes(packed)
assert sha256(gzip.decompress(frozen.read_bytes())).hexdigest()==sha256(raw).hexdigest()
record=dict(frozen_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
            original_path=str(src),input_path=str(frozen),maximum_order=N,
            raw_bytes=len(raw),raw_sha256=sha256(raw).hexdigest(),
            archive_bytes=len(packed),archive_sha256=sha256(packed).hexdigest())
(root/'verification/input_manifest.json').write_text(json.dumps(record,indent=2)+'\n')
del raw,packed
print(json.dumps(record),flush=True)
for tag,args,timeout in [
 ('precision',['code/log_precision_snapshot.py','log_sin1_c3_p512','--checkpoint',str(frozen),
               '--select',','.join(map(str,range(321,N+1)))],580),
 ('weighted',['code/weighted_loss_audit.py','--checkpoint',str(frozen),'--output',str(root)],580),
 ('archive320',['code/delta_archive_checkpoint.py',str(frozen),
                'research/82_weighted_loss_criterion/update_N320_20261031T083718Z/verification/input_checkpoint.pkl.gz',
                '--remove-original','--decode-timeout','200'],580),
 ('selected_archive',['code/archive_selected_evidence.py'],120),
]:
 with open(f'logs/canonical_refresh_{tag}.jsonl','w') as out:
  result=subprocess.run([sys.executable,'-u',*args],stdout=out,stderr=subprocess.STDOUT,timeout=timeout)
 print(json.dumps(dict(step=tag,maximum_order=N,returncode=result.returncode)),flush=True)
 if result.returncode:raise SystemExit(result.returncode)
print(json.dumps(dict(complete=True,root=str(root),actual_elapsed_s=time.monotonic()-start)),flush=True)
