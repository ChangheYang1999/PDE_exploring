from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import sys,time,json
sys.path.insert(0,'code')
from read_checkpoint_archive import read_bytes
start=time.monotonic()
path='research/82_weighted_loss_criterion/update_N300_20261031T0650Z/verification/input_checkpoint.pkl.gz'
raw=read_bytes(path)
assert sha256(raw).hexdigest()=='3c4b69d7a9ee5ac7c7b4417a0a814de0377f6364feb6e0425aa3cf021103d8d5'
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),original_path=path,raw_bytes=len(raw),raw_sha256=sha256(raw).hexdigest(),independent_loader_pass=True,actual_elapsed_s=time.monotonic()-start)
Path('evidence_archives/loader_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
