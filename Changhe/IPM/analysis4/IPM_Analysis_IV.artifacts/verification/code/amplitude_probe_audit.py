"""Independent finite comparison of the two K30 binary64 amplitude runs."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,math,time,sys
sys.dont_write_bytecode=True
root=Path('research/127_amplitude_probe_scope');start=time.monotonic();sources={}
def load(name):
 p=Path('../a4-num/logs')/name;raw=p.read_bytes();rows=[json.loads(line) for line in raw.decode().splitlines() if line.strip()];sources[name]=dict(bytes=len(raw),sha256=sha256(raw).hexdigest());(root/'sources'/name).write_bytes(raw)
 return rows[0],{r['n']:r for r in rows if 'n' in r}
h,a=load('log23_edge30_float.jsonl');hp,b=load('log23_edge30_float_pert.jsonl')
assert h['edge_only_min_ij_le']==hp['edge_only_min_ij_le']==30
assert h['ring']==hp['ring']=='float' and set(a)==set(b)==set(range(1,301))
amp=float(hp['f1'][0]);correction=math.log10(amp)
rows=[]
for n in sorted(a):
 row={'n':n}
 for field,key in [('log10_sum_cols','M'),('log10_sum_gcols','N')]:
  row['base_log_'+key]=a[n][field];row['normalized_twin_log_'+key]=b[n][field]-n*correction;row['absolute_difference_'+key]=abs(row['base_log_'+key]-row['normalized_twin_log_'+key])
 rows.append(row)
windows=[]
for end in [100,200,250,263,265,270,281,284,290,300]:
 part=[r for r in rows if r['n']<=end]
 windows.append(dict(end=end,**{key:dict(maximum=max(r['absolute_difference_'+key] for r in part),argmax=max(part,key=lambda r:r['absolute_difference_'+key])['n']) for key in ['M','N']}))
fullp=Path('../a4-num/logs/log_sin1_c3_p512.regen.jsonl')
if fullp.exists():
 _,full=load(fullp.name)
 comparison=[dict(n=n,**{key+'_edge_minus_full':a[n][field]-full[n][field] for field,key in [('log10_sum_cols','M'),('log10_sum_gcols','N')]}) for n in [250,265,270,280,290,300] if n in full]
else:comparison=[]
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),all_finite_comparisons_completed=True,amplitude_decimal=hp['f1'][0],amplitude_actual_binary_ratio=list(amp.as_integer_ratio()),rows=rows,windows=windows,edge_minus_full=comparison,sources=sources,classification='empirical sensitivity comparison, not a certified error bound',actual_elapsed_s=time.monotonic()-start)
(root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n');(root/'sources/checker.py.txt').write_bytes(Path(__file__).read_bytes())
# Freeze the claim being audited, without unrelated notes.
s=Path('../a4-num/NOTES_FOR_TEAM.md').read_text();section=s.split('## 2026-10-31T09:38Z',1)[1].split('\n## ',1)[0];(root/'sources/claim_0938.md').write_text('## 2026-10-31T09:38Z'+section+'\n')
files={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}
(root/'verification/MANIFEST.json').write_text(json.dumps(dict(files=files),indent=2)+'\n');print(json.dumps(dict(windows=windows,edge_minus_full=comparison,actual_elapsed_s=result['actual_elapsed_s'])),flush=True)
