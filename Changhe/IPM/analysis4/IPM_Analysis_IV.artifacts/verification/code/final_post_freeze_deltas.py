"""Freeze reconstructible changes since V617 without duplicating full reports."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,difflib
base=Path('research/301_final_claim_audit');now=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
out=base/'verification'/('post_freeze_'+now);out.mkdir()
rows=[]
for name,live in [('summary','FINAL_SUMMARY.md'),('theory','FARFIELD_CONVERGENCE_THEORY.md'),('report','FINAL_REPORT.md')]:
 previous=base/'sources'/f'{name}_changes_at_V617.json';d=json.loads(previous.read_text());bp=Path(d['base']['path']);raw=bp.read_bytes();assert sha256(raw).hexdigest()==d['base']['sha256']
 lines=raw.decode().splitlines(keepends=True)
 for r in reversed(d['changes']):lines[r['start']:r['stop']]=r['replacement']
 before=''.join(lines).encode();assert sha256(before).hexdigest()==d['result_sha256']
 source=Path('../a4-lead')/live;st=source.stat();raw=source.read_bytes();assert(st.st_size,st.st_mtime_ns)==(source.stat().st_size,source.stat().st_mtime_ns)
 current=raw.decode().splitlines(keepends=True);changes=[]
 for tag,a,b,c,e in difflib.SequenceMatcher(a=lines,b=current,autojunk=False).get_opcodes():
  if tag!='equal':changes.append(dict(start=a,stop=b,replacement=current[c:e],removed=lines[a:b]))
 replay=lines.copy()
 for r in reversed(changes):replay[r['start']:r['stop']]=r['replacement']
 assert ''.join(replay).encode()==raw
 result=dict(format='line-replacement-delta-v1',recorded_at=datetime.now(timezone.utc).isoformat(timespec='seconds'),base_delta=dict(path=str(previous),sha256=sha256(previous.read_bytes()).hexdigest()),base_sha256=sha256(before).hexdigest(),live_name=str(source),result_sha256=sha256(raw).hexdigest(),changes=changes,scope='Reconstructible text snapshot only; manual review required.')
 p=out/f'{name}.json';p.write_text(json.dumps(result,indent=2)+'\n');rows.append(dict(document=name,path=str(p),sha256=sha256(p.read_bytes()).hexdigest(),changed_blocks=len(changes)))
 (out/f'{name}.diff').write_text(''.join(difflib.unified_diff(lines,current,fromfile='V617',tofile='current',n=3)))
manifest=dict(at=datetime.now(timezone.utc).isoformat(timespec='seconds'),documents=rows,scope='Text snapshot only; not a new admission.')
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n');(base/'verification/latest_post_freeze_snapshot.json').write_text(json.dumps(dict(path=str(out)),indent=2)+'\n');print(json.dumps(manifest,indent=2))
