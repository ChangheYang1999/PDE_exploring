from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys,difflib
if sys.flags.optimize:raise RuntimeError('unoptimized')
r=Path('research/fullgrid_interval225');dest=r/'verification/plan.json'
if dest.exists():raise RuntimeError('plan exists')
pins={}
def sha(p):p=Path(p).resolve();h=hashlib.sha256(p.read_bytes()).hexdigest();pins[str(p)]=h;return h
def read(p):sha(p);return json.loads(Path(p).read_bytes())
for p in [__file__,'code/run_fullgrid225.py','code/replay_fullgrid225.py',r/'PROOF.md',r/'PRELAUNCH_PROOF.md','code/check_fullgrid225_completion.py',r/'verification/producer_diff.txt',r/'verification/replay_diff.txt']:sha(p)
for a,b,label in [('code/run_residual221.py','code/run_fullgrid225.py','producer'),('code/replay_residual221.py','code/replay_fullgrid225.py','replay')]:
 sha(a);sha(b);p=r/'verification'/f'{label}_diff.txt';expected=''.join(difflib.unified_diff(Path(a).read_text().splitlines(True),Path(b).read_text().splitlines(True),fromfile=a,tofile=b)).encode()
 if p.read_bytes()!=expected:raise RuntimeError('exactdiff')
for oldname,newname in [('run_residual221.py','run_fullgrid225.py'),('replay_residual221.py','replay_fullgrid225.py')]:
 expected=Path('code',oldname).read_text().replace("r=Path('research/interval_residual221')","r=Path('research/fullgrid_interval225')")
 if oldname.startswith('replay'):
  anchor="   ck([v['index']for v in src['selected']]==sorted(reasons)"
  if expected.count(anchor)!=1:raise RuntimeError('unique selection anchor')
  expected=expected.replace(anchor,"   reasons={i:[[label,'full_grid']]for label,lo,hi in expected_regions for i in range(lo,hi)}\n"+anchor)
  expected=expected.replace('Finite data-informed selected points; maxima are not regional suprema. Fresh512 root check and rational aggregation, no fresh fourth derivatives.','Complete finite prescribed grid if all succeed; no regional supremum. Fresh512 root check and rational aggregation, no fresh fourth derivatives.')
 if Path('code',newname).read_text()!=expected:raise RuntimeError('only prescribed source changes')
sha('code/report_fullgrid225_incomplete.py')
sha('code/run_fullgrid225_queue.sh')
old=read('research/interval_residual221/verification/plan.json')
for p,h in old['hashes'].items():
 if sha(p)!=h:raise RuntimeError(('oldplanpin',p))
for name,count in [('completion',1372),('qualifications',1068)]:
 j=read(f'research/interval_residual221/verification/{name}.json')
 if j['check_count']!=count or not j['status'].startswith('PASS_'):raise RuntimeError('prior receipt')
 for p,h in j['hashes'].items():
  if sha(p)!=h:raise RuntimeError(('receipt pin',p))
rootpath=Path('research/implicit_root220/certificates/replay.jsonl');sha(rootpath);root={(v['name'],v['index']):v for v in map(json.loads,rootpath.read_bytes().splitlines())};sources=[];count=0
for src in old['sources']:
 raw={}
 for seg in src['raw_segments']:
  if sha(seg['path'])!=seg['sha256']:raise RuntimeError('rawpin')
  raw.update({v['index']:v for v in map(json.loads,Path(seg['path']).read_bytes().splitlines())})
 if sorted(raw)!=list(range(1183)):raise RuntimeError('complete raw')
 selected=[]
 for idx in range(1183):
  v=raw[idx];x,y=map(F,v['coordinate_exact_dyadics']);rr=root[src['name'],idx]
  if min(x,y)<=0 or v['status']!='COMPUTED'or v['dps']!=130 or v['source_sha256']!=src['source_sha256']or rr['status']!='CERTIFIED'or rr['source_sha256']!=src['source_sha256']:raise RuntimeError('exact source record')
  for k in ['R','D','N','N2','prompt_ratio','grouped_ratio','eta']:F(v['fields'][k])
  reasons=[[label,'full_grid']for label,lo,hi in old['regions']if lo<=idx<hi]
  if len(reasons)!=1:raise RuntimeError('unique region')
  selected.append({'index':idx,'reasons':reasons,'coordinate_exact_dyadics':v['coordinate_exact_dyadics'],'eta_hint':v['fields']['eta'],'old_l':rr['l'],'old_h':rr['h'],'scalar_fields':{k:v['fields'][k]for k in ['R','D','N','N2','prompt_ratio','grouped_ratio']}})
 sources.append({**src,'selected':selected});count+=len(selected)
if count!=2366:raise RuntimeError('2366')
o={**old,'utc':datetime.now(timezone.utc).isoformat(),'status':'PINNED_COMPLETE_FINITE_GRID_NOT_RESIDUAL_CERTIFICATE','total':count,'sources':sources,'selection':'every index0through1182 per source, unique region label','scope':'Complete finite sampled grids if all succeed. No independent interval regeneration of fourth derivative jet, no axes/center, continuum bound or A1endpoint.','hashes':pins};o.pop('relative_paths',None);dest.write_text(json.dumps(o,indent=2)+'\n');print(o['utc'],o['status'],count,len(pins))
