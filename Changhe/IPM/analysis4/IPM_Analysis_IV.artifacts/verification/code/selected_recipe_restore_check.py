"""Fresh-process byte verification of every selected JSON recipe."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,pickle,time,sys
sys.dont_write_bytecode=True
from read_checkpoint_archive import read_bytes
from read_selected_archive import reconstruct
start=time.monotonic();root=Path('research/64_log_precision_updates/verification');states={};rows=[]
for p in sorted(root.glob('log_sin1_c3_p512_N*/selected_packed_coefficients.json.recipe.json')):
 r=json.loads(p.read_text());key=r['base_checkpoint']
 if key not in states:
  raw=read_bytes(key);assert len(raw)==r['base_bytes'] and sha256(raw).hexdigest()==r['base_sha256'];states[key]=pickle.loads(raw)
 restored=reconstruct(r,state=states[key]);assert len(restored)==r['original_bytes'] and sha256(restored).hexdigest()==r['original_sha256'];rows.append(dict(recipe=str(p),format_version=r['format_version'],original_bytes=len(restored),original_sha256=sha256(restored).hexdigest()))
 print(json.dumps(rows[-1]),flush=True)
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
(root/'RECIPE_RESTORE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(complete=True,count=len(rows),actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
